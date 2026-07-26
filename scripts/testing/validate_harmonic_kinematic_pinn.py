"""Run deterministic non-training checks for the Phase 2 PINN primitives."""

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

# Import Project Models
from scripts.models.harmonic_kinematic_pinn_network import (
    HarmonicKinematicPinnNetwork,
)
from scripts.models.model_factory import create_model
from scripts.training.transmission_error_datamodule import (
    NormalizationStatistics,
)
from scripts.training.transmission_error_regression_module import (
    TransmissionErrorRegressionModule,
)


def build_input_tensors(
    point_count: int = 96,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Build deterministic raw and normalized causal test inputs."""

    theta_deg_tensor = torch.linspace(
        0.0,
        360.0,
        steps=point_count,
    ).reshape(-1, 1)
    speed_tensor = torch.full_like(theta_deg_tensor, 700.0)
    torque_tensor = torch.full_like(theta_deg_tensor, 600.0)
    temperature_tensor = torch.full_like(theta_deg_tensor, 30.0)
    input_tensor = torch.cat(
        (
            theta_deg_tensor,
            speed_tensor,
            torque_tensor,
            temperature_tensor,
        ),
        dim=-1,
    )
    normalized_input_tensor = input_tensor.clone()
    normalized_input_tensor[:, 0] = (
        normalized_input_tensor[:, 0] - 180.0
    ) / 180.0
    normalized_input_tensor[:, 1] = (
        normalized_input_tensor[:, 1] - 800.0
    ) / 500.0
    normalized_input_tensor[:, 2] = (
        normalized_input_tensor[:, 2] - 700.0
    ) / 500.0
    normalized_input_tensor[:, 3] = (
        normalized_input_tensor[:, 3] - 30.0
    ) / 5.0
    return input_tensor, normalized_input_tensor


def validate_exact_oscillator_identity() -> dict[str, float]:
    """Prove exact harmonics pass and an inadmissible order fails."""

    theta_rad_tensor = torch.linspace(
        0.0,
        2.0 * torch.pi,
        steps=257,
    ).reshape(-1, 1).requires_grad_(True)
    admissible_component_tensor = (
        0.7 * torch.sin(39.0 * theta_rad_tensor)
        - 0.2 * torch.cos(39.0 * theta_rad_tensor)
    )
    _, _, admissible_residual_tensor = (
        HarmonicKinematicPinnNetwork.compute_normalized_oscillator_residual(
            admissible_component_tensor,
            theta_rad_tensor,
            39,
        )
    )
    admissible_max_abs_residual = float(
        torch.max(torch.abs(admissible_residual_tensor)).detach()
    )
    assert admissible_max_abs_residual < 1.0e-5

    inadmissible_component_tensor = torch.sin(5.0 * theta_rad_tensor)
    _, _, inadmissible_residual_tensor = (
        HarmonicKinematicPinnNetwork.compute_normalized_oscillator_residual(
            inadmissible_component_tensor,
            theta_rad_tensor,
            3,
        )
    )
    inadmissible_mean_square_residual = float(
        torch.mean(torch.square(inadmissible_residual_tensor)).detach()
    )
    assert inadmissible_mean_square_residual > 0.1
    return {
        "admissible_max_abs_residual": admissible_max_abs_residual,
        "inadmissible_mean_square_residual": (
            inadmissible_mean_square_residual
        ),
    }


def validate_model_mode(
    head_mode: str,
) -> dict[str, float | int | str]:
    """Validate one factory-created control or PINN mode."""

    torch.manual_seed(42)
    model = create_model(
        "harmonic_kinematic_pinn",
        {
            "input_size": 4,
            "output_size": 1,
            "harmonic_index_list": [1, 3, 39, 40],
            "condition_hidden_size": [24, 16],
            "condition_latent_size": 12,
            "component_hidden_size": [16, 12],
            "head_mode": head_mode,
            "activation_name": "Tanh",
            "dropout_probability": 0.0,
            "use_layer_norm": False,
        },
    )
    assert isinstance(model, HarmonicKinematicPinnNetwork)
    input_tensor, normalized_input_tensor = build_input_tensors()
    output_dictionary = model.compute_auxiliary_output_dictionary(
        input_tensor,
        normalized_input_tensor,
    )
    assert output_dictionary["prediction_tensor"].shape == (96, 1)
    assert output_dictionary["harmonic_component_tensor"].shape == (96, 4)
    assert torch.isfinite(output_dictionary["prediction_tensor"]).all()

    physics_dictionary = model.compute_physics_residual_dictionary(
        input_tensor,
        normalized_input_tensor,
        maximum_collocation_points=48,
        maximum_boundary_conditions=8,
    )
    for physics_value in physics_dictionary.values():
        assert torch.isfinite(physics_value).all()

    oscillator_loss = physics_dictionary[
        "physics_oscillator_residual_loss"
    ]
    model.zero_grad(set_to_none=True)
    oscillator_loss.backward()
    parameter_gradient_norm = sum(
        float(torch.linalg.vector_norm(parameter.grad).detach())
        for parameter in model.parameters()
        if parameter.grad is not None
    )
    if head_mode == "implicit_pinn":
        assert parameter_gradient_norm > 0.0
    else:
        assert float(oscillator_loss.detach()) < 1.0e-8

    shifted_input_tensor = input_tensor.clone()
    shifted_input_tensor[:, 0] += 360.0
    shifted_prediction_tensor = model.compute_auxiliary_output_dictionary(
        shifted_input_tensor,
        normalized_input_tensor,
    )["prediction_tensor"]
    shift_error = float(
        torch.max(
            torch.abs(
                shifted_prediction_tensor
                - output_dictionary["prediction_tensor"]
            )
        ).detach()
    )
    if head_mode == "explicit_fourier":
        assert shift_error < 1.0e-5

    return {
        "head_mode": head_mode,
        "parameter_count": sum(
            parameter.numel() for parameter in model.parameters()
        ),
        "oscillator_loss": float(oscillator_loss.detach()),
        "periodic_value_loss": float(
            physics_dictionary["physics_periodic_value_loss"].detach()
        ),
        "periodic_slope_loss": float(
            physics_dictionary["physics_periodic_slope_loss"].detach()
        ),
        "parameter_gradient_norm": parameter_gradient_norm,
        "angular_shift_max_abs_error": shift_error,
    }


def validate_lightning_loss_integration() -> dict[str, float]:
    """Prove physics residuals enter the repository training-loss contract."""

    torch.manual_seed(84)
    input_tensor, normalized_input_tensor = build_input_tensors()
    model = create_model(
        "harmonic_kinematic_pinn",
        {
            "input_size": 4,
            "output_size": 1,
            "harmonic_index_list": [1, 3, 39, 40],
            "condition_hidden_size": [20, 16],
            "condition_latent_size": 12,
            "component_hidden_size": [16, 12],
            "head_mode": "implicit_pinn",
            "activation_name": "Tanh",
            "dropout_probability": 0.0,
            "use_layer_norm": False,
        },
    )
    normalization_statistics = NormalizationStatistics(
        input_feature_mean=torch.tensor([180.0, 800.0, 700.0, 30.0]),
        input_feature_std=torch.tensor([180.0, 500.0, 500.0, 5.0]),
        target_mean=torch.tensor([0.0]),
        target_std=torch.tensor([0.05]),
    )
    regression_module = TransmissionErrorRegressionModule(
        regression_model=model,
        input_feature_dim=4,
        target_feature_dim=1,
        normalization_statistics=normalization_statistics,
        loss_configuration={
            "profile": "phase2_harmonic_kinematic_pinn",
            "pointwise_loss": "mse",
            "enable_physics_diagnostics": True,
            "physics_maximum_collocation_points": 32,
            "physics_maximum_boundary_conditions": 6,
            "weights": {
                "point": 1.0,
                "physics_oscillator": 0.05,
                "physics_periodic_value": 0.01,
                "physics_periodic_slope": 0.005,
            },
        },
    )
    target_tensor = (
        0.02 * torch.sin(torch.deg2rad(input_tensor[:, 0:1]))
    )
    batch_dictionary = {
        "input_tensor": input_tensor,
        "target_tensor": target_tensor,
        "angular_position_deg": input_tensor[:, 0],
        "point_count_per_curve": torch.tensor([input_tensor.shape[0]]),
        "curve_count": 1,
    }
    batch_output_dictionary = regression_module.compute_batch_outputs(
        batch_dictionary
    )
    assert torch.isfinite(batch_output_dictionary["loss"])
    assert (
        float(
            batch_output_dictionary[
                "physics_oscillator_residual_loss"
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

    # Lightning Validation Uses Inference Contexts In Normal Operation
    with torch.inference_mode():
        inference_output_dictionary = regression_module.compute_batch_outputs(
            batch_dictionary
        )
    assert torch.isfinite(inference_output_dictionary["loss"])
    return {
        "integrated_loss": float(batch_output_dictionary["loss"].detach()),
        "integrated_gradient_norm": integrated_gradient_norm,
        "inference_context_loss": float(
            inference_output_dictionary["loss"].detach()
        ),
        "normalized_input_reconstruction_error": float(
            torch.max(
                torch.abs(
                    regression_module.normalize_input_tensor(input_tensor)
                    - normalized_input_tensor
                )
            )
        ),
    }


def validate_frozen_analytical_anchor() -> dict[str, float]:
    """Prove the frozen Bauer payload reconstructs an exact known curve."""

    harmonic_index_list = [1, 3, 39, 40]
    coefficient_matrix = torch.zeros(
        (10, 1 + (2 * len(harmonic_index_list))),
        dtype=torch.float32,
    )
    coefficient_matrix[9, 0] = 0.01
    coefficient_matrix[9, 1] = 0.02
    coefficient_matrix[9, 4] = -0.005
    model = create_model(
        "harmonic_kinematic_pinn",
        {
            "input_size": 4,
            "output_size": 1,
            "harmonic_index_list": harmonic_index_list,
            "condition_hidden_size": [16, 12],
            "condition_latent_size": 8,
            "component_hidden_size": [12, 8],
            "head_mode": "implicit_pinn",
            "activation_name": "Tanh",
            "analytical_anchor_feature_mean": [0.0, 0.0, 0.0],
            "analytical_anchor_feature_scale": [1.0, 1.0, 1.0],
            "analytical_anchor_coefficient_matrix": (
                coefficient_matrix.tolist()
            ),
        },
    )
    input_tensor, normalized_input_tensor = build_input_tensors()
    theta_rad_tensor = torch.deg2rad(input_tensor[:, 0:1])
    expected_anchor_tensor = (
        0.01
        + (0.02 * torch.sin(theta_rad_tensor))
        - (0.005 * torch.cos(3.0 * theta_rad_tensor))
    )
    actual_anchor_tensor = model.compute_analytical_anchor_prediction_tensor(
        input_tensor
    )
    reconstruction_error = float(
        torch.max(torch.abs(actual_anchor_tensor - expected_anchor_tensor))
    )
    assert reconstruction_error < 1.0e-7

    physics_dictionary = model.compute_physics_residual_dictionary(
        input_tensor,
        normalized_input_tensor,
        maximum_collocation_points=32,
        maximum_boundary_conditions=6,
        target_mean_tensor=torch.tensor([0.0]),
        target_std_tensor=torch.tensor([0.05]),
    )
    analytical_anchor_loss = float(
        physics_dictionary["physics_analytical_anchor_loss"].detach()
    )
    assert analytical_anchor_loss > 0.0
    return {
        "anchor_reconstruction_max_abs_error": reconstruction_error,
        "analytical_anchor_loss": analytical_anchor_loss,
    }


def main() -> None:
    """Run all deterministic Phase 2 primitive checks."""

    identity_result = validate_exact_oscillator_identity()
    control_result = validate_model_mode("explicit_fourier")
    pinn_result = validate_model_mode("implicit_pinn")
    integration_result = validate_lightning_loss_integration()
    anchor_result = validate_frozen_analytical_anchor()
    print("PHASE2_HARMONIC_KINEMATIC_PINN_VALIDATION_OK")
    print(f"identity={identity_result}")
    print(f"control={control_result}")
    print(f"pinn={pinn_result}")
    print(f"integration={integration_result}")
    print(f"anchor={anchor_result}")


if __name__ == "__main__":
    main()
