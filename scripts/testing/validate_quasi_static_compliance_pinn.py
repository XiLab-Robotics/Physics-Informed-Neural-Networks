"""Run deterministic non-training checks for the Phase 3 compliance PINN."""

from __future__ import annotations

# Import Python Utilities
import sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import PyTorch Utilities
import torch

# Import Project Models And Training Utilities
from scripts.models.model_factory import create_model
from scripts.models.quasi_static_compliance_pinn_network import (
    QuasiStaticCompliancePinnNetwork,
)
from scripts.training.transmission_error_datamodule import (
    NormalizationStatistics,
)
from scripts.training.transmission_error_regression_module import (
    TransmissionErrorRegressionModule,
)


HARMONIC_INDEX_LIST = [1, 3, 39, 40, 156, 162, 240]


def build_normalization_statistics() -> NormalizationStatistics:
    """Build deterministic five-input normalization statistics."""

    return NormalizationStatistics(
        input_feature_mean=torch.tensor(
            [180.0, 800.0, 700.0, 30.0, 0.0],
        ),
        input_feature_std=torch.tensor(
            [180.0, 500.0, 500.0, 5.0, 1.0],
        ),
        target_mean=torch.tensor([-0.015]),
        target_std=torch.tensor([0.05]),
    )


def build_input_tensors(
    point_count_per_direction: int = 64,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Build paired Fw and Bw operating conditions over one cycle."""

    angle_tensor = torch.arange(
        point_count_per_direction,
        dtype=torch.float32,
    ).reshape(-1, 1)
    angle_tensor = angle_tensor * (
        360.0 / point_count_per_direction
    )
    speed_tensor = torch.full_like(angle_tensor, 700.0)
    torque_tensor = torch.linspace(
        100.0,
        1800.0,
        steps=point_count_per_direction,
    ).reshape(-1, 1)
    temperature_tensor = torch.linspace(
        24.0,
        36.0,
        steps=point_count_per_direction,
    ).reshape(-1, 1)
    forward_direction_tensor = torch.ones_like(angle_tensor)
    backward_direction_tensor = -torch.ones_like(angle_tensor)

    forward_input_tensor = torch.cat(
        (
            angle_tensor,
            speed_tensor,
            torque_tensor,
            temperature_tensor,
            forward_direction_tensor,
        ),
        dim=-1,
    )
    backward_input_tensor = torch.cat(
        (
            angle_tensor,
            speed_tensor,
            torque_tensor,
            temperature_tensor,
            backward_direction_tensor,
        ),
        dim=-1,
    )
    input_tensor = torch.cat(
        (forward_input_tensor, backward_input_tensor),
        dim=0,
    )
    normalization_statistics = build_normalization_statistics()
    normalized_input_tensor = (
        input_tensor - normalization_statistics.input_feature_mean
    ) / normalization_statistics.input_feature_std
    return input_tensor, normalized_input_tensor


def create_phase3_model(
    formulation: str,
    torque_input_mode: str = "nominal_magnitude",
) -> QuasiStaticCompliancePinnNetwork:
    """Create one compact deterministic Phase 3 formulation."""

    torch.manual_seed(100 + int(formulation[1:]))
    model = create_model(
        "quasi_static_compliance_pinn",
        {
            "input_size": 5,
            "output_size": 1,
            "harmonic_index_list": HARMONIC_INDEX_LIST,
            "condition_hidden_size": [24, 16],
            "condition_latent_size": 12,
            "mean_hidden_size": [16, 12],
            "formulation": formulation,
            "activation_name": "Tanh",
            "dropout_probability": 0.0,
            "use_layer_norm": False,
            "minimum_stiffness_nm_per_deg": 5000.0,
            "maximum_stiffness_nm_per_deg": 100000.0,
            "initial_stiffness_nm_per_deg": 27250.0,
            "initial_forward_intercept_deg": -0.0217,
            "initial_backward_intercept_deg": -0.0116,
            "reference_temperature_deg_c": 30.0,
            "temperature_scale_deg_c": 10.0,
            "nonlinear_torque_scale_nm": 400.0,
            "maximum_nonlinear_amplitude_deg": 0.02,
            "torque_input_mode": torque_input_mode,
        },
    )
    assert isinstance(model, QuasiStaticCompliancePinnNetwork)
    model.set_normalization_statistics(build_normalization_statistics())
    return model


def validate_torque_sign_and_stiffness_contract() -> dict[str, float]:
    """Verify measured-sign reconstruction and bounded stiffness."""

    input_tensor, _ = build_input_tensors(point_count_per_direction=16)
    model = create_phase3_model("C2")
    signed_torque_tensor = model.compute_signed_torque_tensor(input_tensor)
    forward_signed_torque_tensor = signed_torque_tensor[:16]
    backward_signed_torque_tensor = signed_torque_tensor[16:]
    assert torch.all(forward_signed_torque_tensor < 0.0)
    assert torch.all(backward_signed_torque_tensor > 0.0)

    stiffness_tensor = model.compute_effective_stiffness_tensor(input_tensor)
    assert torch.all(
        stiffness_tensor > model.minimum_stiffness_nm_per_deg
    )
    assert torch.all(
        stiffness_tensor < model.maximum_stiffness_nm_per_deg
    )

    measured_signed_input_tensor = input_tensor.clone()
    measured_signed_input_tensor[:, 2:3] = signed_torque_tensor
    measured_signed_model = create_phase3_model(
        "C4",
        torque_input_mode="measured_signed",
    )
    measured_reconstruction_error = float(
        torch.max(
            torch.abs(
                measured_signed_model.compute_signed_torque_tensor(
                    measured_signed_input_tensor
                )
                - signed_torque_tensor
            )
        )
    )
    assert measured_reconstruction_error < 1.0e-8
    return {
        "forward_max_signed_torque_nm": float(
            torch.max(forward_signed_torque_tensor)
        ),
        "backward_min_signed_torque_nm": float(
            torch.min(backward_signed_torque_tensor)
        ),
        "minimum_effective_stiffness_nm_per_deg": float(
            torch.min(stiffness_tensor).detach()
        ),
        "maximum_effective_stiffness_nm_per_deg": float(
            torch.max(stiffness_tensor).detach()
        ),
        "measured_signed_reconstruction_error": (
            measured_reconstruction_error
        ),
    }


def validate_formulation(
    formulation: str,
) -> dict[str, float | int | str]:
    """Validate output, residual, gradient, and hard-equation contracts."""

    input_tensor, normalized_input_tensor = build_input_tensors()
    model = create_phase3_model(formulation)
    output_dictionary = model.compute_auxiliary_output_dictionary(
        input_tensor,
        normalized_input_tensor,
    )
    assert output_dictionary["prediction_tensor"].shape == (128, 1)
    assert output_dictionary["periodic_component_tensor"].shape == (
        128,
        len(HARMONIC_INDEX_LIST),
    )
    assert torch.isfinite(output_dictionary["prediction_tensor"]).all()

    physics_dictionary = model.compute_physics_residual_dictionary(
        input_tensor,
        normalized_input_tensor,
        maximum_collocation_points=48,
        maximum_boundary_conditions=8,
    )
    for physics_value in physics_dictionary.values():
        assert torch.isfinite(physics_value).all()

    compliance_loss = physics_dictionary[
        "physics_compliance_equation_loss"
    ]
    periodic_mean_loss = physics_dictionary[
        "physics_periodic_mean_loss"
    ]
    stiffness_bounds_loss = physics_dictionary[
        "physics_stiffness_bounds_loss"
    ]
    assert float(periodic_mean_loss.detach()) < 1.0e-8
    assert float(stiffness_bounds_loss.detach()) < 1.0e-8

    if formulation == "C0":
        assert float(compliance_loss.detach()) < 1.0e-8
        parameter_gradient_norm = 0.0
    else:
        model.zero_grad(set_to_none=True)
        (
            compliance_loss
            + physics_dictionary["physics_zero_torque_boundary_loss"]
            + periodic_mean_loss
        ).backward()
        parameter_gradient_norm = sum(
            float(torch.linalg.vector_norm(parameter.grad).detach())
            for parameter in model.parameters()
            if parameter.grad is not None
        )

    if formulation in model.SOFT_RESIDUAL_FORMULATION_SET:
        assert float(compliance_loss.detach()) > 0.0
        assert parameter_gradient_norm > 0.0
    elif formulation in model.HARD_EQUATION_FORMULATION_SET:
        assert float(compliance_loss.detach()) < 1.0e-8
        assert (
            float(
                physics_dictionary[
                    "physics_zero_torque_boundary_loss"
                ].detach()
            )
            < 1.0e-10
        )

        hard_mean_prediction_tensor = (
            model.compute_hard_mean_prediction_deg(input_tensor)
        )
        reconstructed_mean_tensor = (
            output_dictionary["direction_intercept_deg"]
            + output_dictionary["elastic_prediction_deg"]
        )
        hard_reconstruction_error = float(
            torch.max(
                torch.abs(
                    hard_mean_prediction_tensor
                    - reconstructed_mean_tensor
                )
            ).detach()
        )
        assert hard_reconstruction_error < 1.0e-8

    return {
        "formulation": formulation,
        "parameter_count": sum(
            parameter.numel() for parameter in model.parameters()
        ),
        "compliance_loss": float(compliance_loss.detach()),
        "zero_torque_boundary_loss": float(
            physics_dictionary[
                "physics_zero_torque_boundary_loss"
            ].detach()
        ),
        "monotonicity_loss": float(
            physics_dictionary[
                "physics_compliance_monotonicity_loss"
            ].detach()
        ),
        "periodic_mean_loss": float(periodic_mean_loss.detach()),
        "parameter_gradient_norm": parameter_gradient_norm,
    }


def validate_c2_temperature_and_c3_nonlinear_laws() -> dict[str, float]:
    """Verify positive temperature-conditioned and nonlinear compliance."""

    input_tensor, _ = build_input_tensors(point_count_per_direction=32)
    c2_model = create_phase3_model("C2")
    with torch.no_grad():
        c2_model.raw_temperature_slope.copy_(
            torch.tensor([0.4, -0.3])
        )
    c2_compliance_tensor = (
        c2_model.compute_target_compliance_derivative_tensor(input_tensor)
    )
    assert torch.all(c2_compliance_tensor > 0.0)

    c3_model = create_phase3_model("C3")
    c3_compliance_tensor = (
        c3_model.compute_target_compliance_derivative_tensor(input_tensor)
    )
    linear_compliance_tensor = (
        1.0 / c3_model.compute_effective_stiffness_tensor(input_tensor)
    )
    nonlinear_increment_tensor = (
        c3_compliance_tensor - linear_compliance_tensor
    )
    assert torch.all(nonlinear_increment_tensor >= 0.0)
    assert torch.max(nonlinear_increment_tensor) > 0.0
    return {
        "minimum_c2_compliance_deg_per_nm": float(
            torch.min(c2_compliance_tensor).detach()
        ),
        "maximum_c2_compliance_deg_per_nm": float(
            torch.max(c2_compliance_tensor).detach()
        ),
        "minimum_c3_nonlinear_increment_deg_per_nm": float(
            torch.min(nonlinear_increment_tensor).detach()
        ),
        "maximum_c3_nonlinear_increment_deg_per_nm": float(
            torch.max(nonlinear_increment_tensor).detach()
        ),
    }


def validate_shared_stiffness_contract() -> dict[str, float]:
    """Verify C5 uses one stiffness for both directions."""

    input_tensor, _ = build_input_tensors(point_count_per_direction=16)
    model = create_phase3_model("C5")
    stiffness_tensor = model.compute_effective_stiffness_tensor(input_tensor)
    forward_stiffness_tensor = stiffness_tensor[:16]
    backward_stiffness_tensor = stiffness_tensor[16:]
    direction_difference = float(
        torch.max(
            torch.abs(
                forward_stiffness_tensor - backward_stiffness_tensor
            )
        ).detach()
    )
    assert direction_difference < 1.0e-8
    return {
        "shared_stiffness_nm_per_deg": float(
            torch.mean(stiffness_tensor).detach()
        ),
        "direction_difference_nm_per_deg": direction_difference,
    }


def validate_lightning_loss_integration() -> dict[str, float]:
    """Prove Phase 3 residuals enter the repository training contract."""

    input_tensor, _ = build_input_tensors()
    model = create_phase3_model("C2")
    regression_module = TransmissionErrorRegressionModule(
        regression_model=model,
        input_feature_dim=5,
        target_feature_dim=1,
        normalization_statistics=build_normalization_statistics(),
        loss_configuration={
            "profile": "phase3_quasi_static_compliance_pinn",
            "pointwise_loss": "mse",
            "enable_physics_diagnostics": True,
            "physics_maximum_collocation_points": 32,
            "physics_maximum_boundary_conditions": 6,
            "weights": {
                "point": 1.0,
                "physics_compliance_equation": 0.05,
                "physics_zero_torque_boundary": 0.02,
                "physics_compliance_monotonicity": 0.01,
                "physics_stiffness_bounds": 0.01,
                "physics_periodic_mean": 0.01,
            },
        },
    )
    signed_torque_tensor = model.compute_signed_torque_tensor(input_tensor)
    target_tensor = (
        -0.015
        + signed_torque_tensor / 27250.0
        + 0.01
        * torch.sin(
            39.0 * torch.deg2rad(input_tensor[:, 0:1])
        )
    )
    batch_dictionary = {
        "input_tensor": input_tensor,
        "target_tensor": target_tensor,
        "angular_position_deg": input_tensor[:, 0],
        "point_count_per_curve": torch.tensor([64, 64]),
        "curve_count": 2,
    }
    batch_output_dictionary = regression_module.compute_batch_outputs(
        batch_dictionary
    )
    assert torch.isfinite(batch_output_dictionary["loss"])
    assert (
        float(
            batch_output_dictionary[
                "physics_compliance_equation_loss"
            ].detach()
        )
        > 0.0
    )
    regression_module.zero_grad(set_to_none=True)
    batch_output_dictionary["loss"].backward()
    integrated_gradient_norm = sum(
        float(torch.linalg.vector_norm(parameter.grad).detach())
        for parameter in regression_module.parameters()
        if parameter.grad is not None
    )
    assert integrated_gradient_norm > 0.0

    with torch.inference_mode():
        inference_output_dictionary = regression_module.compute_batch_outputs(
            batch_dictionary
        )
    assert torch.isfinite(inference_output_dictionary["loss"])
    return {
        "integrated_loss": float(batch_output_dictionary["loss"].detach()),
        "physics_compliance_equation_loss": float(
            batch_output_dictionary[
                "physics_compliance_equation_loss"
            ].detach()
        ),
        "integrated_gradient_norm": integrated_gradient_norm,
        "inference_context_loss": float(
            inference_output_dictionary["loss"].detach()
        ),
    }


def main() -> None:
    """Run all deterministic Phase 3 primitive checks."""

    torque_result = validate_torque_sign_and_stiffness_contract()
    formulation_result_list = [
        validate_formulation(formulation)
        for formulation in ["C0", "C1", "C2", "C3", "C4", "C5"]
    ]
    nonlinear_result = validate_c2_temperature_and_c3_nonlinear_laws()
    shared_stiffness_result = validate_shared_stiffness_contract()
    integration_result = validate_lightning_loss_integration()
    print("PHASE3_QUASI_STATIC_COMPLIANCE_PINN_VALIDATION_OK")
    print(f"torque={torque_result}")
    print(f"formulations={formulation_result_list}")
    print(f"nonlinear={nonlinear_result}")
    print(f"shared_stiffness={shared_stiffness_result}")
    print(f"integration={integration_result}")


if __name__ == "__main__":
    main()
