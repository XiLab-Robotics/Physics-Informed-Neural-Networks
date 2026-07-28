"""Validate the Wave 5.2R Stage 4 model and campaign package."""

from __future__ import annotations

# Import Python Utilities
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import YAML Utilities
import yaml

# Import PyTorch Utilities
import torch
from torch.utils.data import TensorDataset

# Import Project Models And Training Utilities
from scripts.models.data_only_residual_capacity_network import (
    DataOnlyResidualCapacityNetwork,
)
from scripts.models.model_factory import create_model
from scripts.training.physics_guided_optimization_instrumentation import (
    build_deterministic_dataloader,
)
from scripts.training.physics_guided_optimization_instrumentation import (
    compute_dataloader_fingerprint,
)
from scripts.training.run_training_campaign import (
    SUPPORTED_MODEL_ENTRYPOINT_NAME_DICTIONARY,
)
from scripts.training.transmission_error_datamodule import (
    NormalizationStatistics,
)
from scripts.training.transmission_error_regression_module import (
    TransmissionErrorRegressionModule,
)


# Define Validation Paths
CAMPAIGN_MANIFEST_PATH = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "data_only_residual_capacity"
    / "campaigns"
    / "2026-07-28_wave52r_stage4_data_only_residual_capacity"
    / "campaign.yaml"
)
CALIBRATION_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
    / "stage4_training_only_calibration.yaml"
)
VALIDATION_SUMMARY_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
    / "stage4_preflight_validation_summary.json"
)
REAL_DATASET_ONE_BATCH_SUMMARY_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
    / "stage4_real_dataset_one_batch_summary.yaml"
)
LAUNCHER_PREFLIGHT_SUMMARY_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
    / "stage4_launcher_preflight_summary.yaml"
)


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as source_file:
        payload = yaml.safe_load(source_file)
    assert isinstance(payload, dict), f"Expected YAML mapping | {path}"
    return payload


def build_normalization_statistics() -> NormalizationStatistics:
    """Build stable physical-to-normalized statistics for model checks."""

    return NormalizationStatistics(
        input_feature_mean=torch.tensor(
            [180.0, 900.0, 900.0, 30.0, 1.0],
            dtype=torch.float32,
        ),
        input_feature_std=torch.tensor(
            [105.0, 500.0, 550.0, 5.0, 1.0],
            dtype=torch.float32,
        ),
        target_mean=torch.tensor([-0.018], dtype=torch.float32),
        target_std=torch.tensor([0.006], dtype=torch.float32),
    )


def build_input_tensor() -> torch.Tensor:
    """Build representative forward setpoint points."""

    return torch.tensor(
        [
            [0.0, 100.0, 0.0, 25.0, 1.0],
            [45.0, 500.0, 600.0, 30.0, 1.0],
            [90.0, 900.0, 1000.0, 35.0, 1.0],
            [180.0, 1400.0, 1400.0, 30.0, 1.0],
            [270.0, 1800.0, 1800.0, 25.0, 1.0],
            [359.5, 500.0, 200.0, 35.0, 1.0],
        ],
        dtype=torch.float32,
    )


def normalize_input_tensor(
    input_tensor: torch.Tensor,
    normalization_statistics: NormalizationStatistics,
) -> torch.Tensor:
    """Normalize one input tensor with the declared statistics."""

    return (
        input_tensor - normalization_statistics.input_feature_mean
    ) / normalization_statistics.input_feature_std


def load_model_from_configuration(
    configuration: dict[str, Any],
) -> DataOnlyResidualCapacityNetwork:
    """Instantiate and initialize one Stage 4 model."""

    model_configuration = dict(configuration["model"])
    model_configuration["input_size"] = 5
    model = create_model(
        configuration["experiment"]["model_type"],
        model_configuration,
    )
    assert isinstance(model, DataOnlyResidualCapacityNetwork)
    model.set_normalization_statistics(build_normalization_statistics())
    return model


def reconstruct_explicitly(
    input_tensor: torch.Tensor,
    coefficient_tensor: torch.Tensor,
    order_list: list[int],
) -> torch.Tensor:
    """Independently reconstruct a periodic signal from explicit coefficients."""

    theta_rad_tensor = torch.deg2rad(input_tensor[:, 0:1])
    result_tensor = coefficient_tensor[:, 0:1].clone()
    for order_position, order_value in enumerate(order_list):
        result_tensor = result_tensor + (
            coefficient_tensor[:, 1 + (2 * order_position) : 2 + (2 * order_position)]
            * torch.sin(float(order_value) * theta_rad_tensor)
            + coefficient_tensor[:, 2 + (2 * order_position) : 3 + (2 * order_position)]
            * torch.cos(float(order_value) * theta_rad_tensor)
        )
    return result_tensor


def validate_dataloader_reproducibility() -> dict[str, str]:
    """Prove same-seed identity and different-seed shuffled order."""

    dataset = TensorDataset(torch.arange(64, dtype=torch.int64))
    first_loader = build_deterministic_dataloader(
        dataset,
        batch_size=8,
        random_seed=314159,
    )
    repeated_loader = build_deterministic_dataloader(
        dataset,
        batch_size=8,
        random_seed=314159,
    )
    different_loader = build_deterministic_dataloader(
        dataset,
        batch_size=8,
        random_seed=271828,
    )
    first_fingerprint = compute_dataloader_fingerprint(first_loader)
    repeated_fingerprint = compute_dataloader_fingerprint(repeated_loader)
    different_fingerprint = compute_dataloader_fingerprint(different_loader)
    assert first_fingerprint == repeated_fingerprint
    assert first_fingerprint != different_fingerprint
    return {
        "seed_314159_fingerprint": first_fingerprint,
        "seed_314159_repeat_fingerprint": repeated_fingerprint,
        "seed_271828_fingerprint": different_fingerprint,
    }


def validate_model_formulations(
    queue_configuration_list: list[dict[str, Any]],
) -> dict[str, Any]:
    """Validate analytical separation, bounds, masks, and finite gradients."""

    normalization_statistics = build_normalization_statistics()
    input_tensor = build_input_tensor()
    normalized_input_tensor = normalize_input_tensor(
        input_tensor,
        normalization_statistics,
    )
    configuration_by_candidate = {
        configuration["metadata"]["candidate_id"]: configuration
        for configuration in queue_configuration_list
    }

    # R1 Must Never Evaluate The Analytical Path
    direct_model = load_model_from_configuration(
        configuration_by_candidate["C01"]
    )
    direct_model._compute_anchor_dictionary = lambda _: (_ for _ in ()).throw(
        AssertionError("R1 evaluated the analytical path")
    )
    direct_output = direct_model.compute_auxiliary_output_dictionary(
        input_tensor,
        normalized_input_tensor,
    )
    assert set(direct_output) == {
        "prediction_tensor",
        "direct_prediction_tensor",
        "direct_prediction_deg",
    }

    # Every Frozen Hybrid Must Reproduce PF-A Exactly At Initialization
    maximum_zero_initialization_error = 0.0
    maximum_signed_torque_replay_error = 0.0
    for candidate_id in ["H01", "H03", "H05", "H07"]:
        model = load_model_from_configuration(
            configuration_by_candidate[candidate_id]
        )
        output_dictionary = model.compute_auxiliary_output_dictionary(
            input_tensor,
            normalized_input_tensor,
        )
        current_error = float(
            torch.max(
                torch.abs(
                    output_dictionary["prediction_tensor"]
                    - output_dictionary["analytical_prediction_tensor"]
                )
            ).item()
        )
        maximum_zero_initialization_error = max(
            maximum_zero_initialization_error,
            current_error,
        )
        assert current_error == 0.0
        assert not model.anchor_surface_delta.requires_grad
        if candidate_id == "H01":
            operating_tensor = torch.cat(
                (
                    -torch.abs(input_tensor[:, 2:3]),
                    torch.abs(input_tensor[:, 1:2]),
                    input_tensor[:, 3:4],
                ),
                dim=-1,
            )
            standardized_tensor = (
                operating_tensor
                - model.analytical_anchor_feature_mean
            ) / model.analytical_anchor_feature_scale
            torque_tensor = standardized_tensor[:, 0:1]
            speed_tensor = standardized_tensor[:, 1:2]
            temperature_tensor = standardized_tensor[:, 2:3]
            independent_design_tensor = torch.cat(
                (
                    torch.square(torque_tensor),
                    torch.square(speed_tensor),
                    torch.square(temperature_tensor),
                    torque_tensor * speed_tensor,
                    torque_tensor * temperature_tensor,
                    speed_tensor * temperature_tensor,
                    torque_tensor,
                    speed_tensor,
                    temperature_tensor,
                    torch.ones_like(torque_tensor),
                ),
                dim=-1,
            )
            independent_coefficient_tensor = (
                independent_design_tensor
                @ model.frozen_analytical_anchor_coefficient_matrix
            )
            independent_anchor_deg = reconstruct_explicitly(
                input_tensor,
                independent_coefficient_tensor,
                model.harmonic_index_list,
            )
            maximum_signed_torque_replay_error = float(
                torch.max(
                    torch.abs(
                        independent_anchor_deg
                        - output_dictionary[
                            "frozen_analytical_prediction_deg"
                        ]
                    )
                ).item()
            )
            assert maximum_signed_torque_replay_error <= 1.0e-9

    # R3 Hard Bound Must Hold Under Saturating Raw Output
    bounded_model = load_model_from_configuration(
        configuration_by_candidate["H03"]
    )
    assert bounded_model.pointwise_network is not None
    output_layer = (
        bounded_model.pointwise_network.feature_network.network[-1]
    )
    assert isinstance(output_layer, torch.nn.Linear)
    with torch.no_grad():
        output_layer.bias.fill_(100.0)
    bounded_output = bounded_model.compute_auxiliary_output_dictionary(
        input_tensor,
        normalized_input_tensor,
    )
    maximum_bounded_residual = float(
        torch.max(
            torch.abs(bounded_output["residual_prediction_deg"])
        ).item()
    )
    assert maximum_bounded_residual <= (
        bounded_model.residual_bound_deg + 1.0e-7
    )

    # R4 And R5 Reconstructions Must Equal An Independent Explicit Sum
    reconstruction_error_map: dict[str, float] = {}
    for candidate_id, order_list in [
        (
            "H05",
            configuration_by_candidate["H05"]["model"][
                "residual_basis_order_list"
            ],
        ),
        ("H07", list(bounded_model.harmonic_index_list)),
    ]:
        model = load_model_from_configuration(
            configuration_by_candidate[candidate_id]
        )
        assert model.condition_coefficient_network is not None
        with torch.no_grad():
            model.condition_coefficient_network.network[-1].bias.fill_(0.1)
        output_dictionary = model.compute_auxiliary_output_dictionary(
            input_tensor,
            normalized_input_tensor,
        )
        explicit_residual_deg = reconstruct_explicitly(
            input_tensor,
            output_dictionary["residual_coefficient_tensor"],
            [int(value) for value in order_list],
        )
        reconstruction_error = float(
            torch.max(
                torch.abs(
                    explicit_residual_deg
                    - output_dictionary["residual_prediction_deg"]
                )
            ).item()
        )
        assert reconstruction_error <= 1.0e-7
        reconstruction_error_map[candidate_id] = reconstruction_error

    # Partial Unfreeze Must Touch Only Offset And Orders 1 And 3
    partial_model = load_model_from_configuration(
        configuration_by_candidate["A03"]
    )
    partial_output = partial_model.compute_auxiliary_output_dictionary(
        input_tensor,
        normalized_input_tensor,
    )
    torch.sum(partial_output["prediction_tensor"]).backward()
    partial_gradient = partial_model.anchor_surface_delta.grad
    assert partial_gradient is not None
    partial_mask = partial_model.anchor_surface_trainable_mask
    assert bool(torch.all(partial_gradient[partial_mask == 0.0] == 0.0))
    assert bool(torch.any(torch.abs(partial_gradient[partial_mask == 1.0]) > 0.0))
    expected_nonzero_column_set = {0, 1, 2, 3, 4}
    actual_nonzero_column_set = set(
        torch.nonzero(
            torch.any(partial_mask > 0.0, dim=0),
            as_tuple=False,
        )
        .reshape(-1)
        .tolist()
    )
    assert actual_nonzero_column_set == expected_nonzero_column_set

    # Full Unfreeze Must Preserve The Original Frozen Surface Buffer
    full_model = load_model_from_configuration(
        configuration_by_candidate["A04"]
    )
    original_surface_hash = hashlib.sha256(
        full_model.frozen_analytical_anchor_coefficient_matrix
        .detach()
        .cpu()
        .numpy()
        .tobytes()
    ).hexdigest()
    assert full_model.anchor_surface_delta.requires_grad
    assert bool(
        torch.all(full_model.anchor_surface_trainable_mask == 1.0)
    )
    assert (
        "frozen_analytical_anchor_coefficient_matrix"
        in full_model.state_dict()
    )

    # One Full Synthetic Batch Must Produce Finite Loss And Gradients
    gradient_model = load_model_from_configuration(
        configuration_by_candidate["A02"]
    )
    regression_module = TransmissionErrorRegressionModule(
        regression_model=gradient_model,
        input_feature_dim=5,
        target_feature_dim=1,
        learning_rate=5.0e-4,
        weight_decay=1.0e-5,
        normalization_statistics=normalization_statistics,
        loss_configuration=configuration_by_candidate["A02"][
            "training"
        ]["loss"],
    )
    target_tensor = torch.linspace(
        -0.022,
        -0.010,
        input_tensor.shape[0],
    ).reshape(-1, 1)
    batch_dictionary = {
        "input_tensor": input_tensor,
        "target_tensor": target_tensor,
        "angular_position_deg": input_tensor[:, 0],
        "point_count_per_curve": torch.tensor(
            [input_tensor.shape[0]],
            dtype=torch.long,
        ),
        "curve_count": 1,
        "direction_label": ["Fw"],
        "source_file_path": ["synthetic_stage4_preflight"],
    }
    batch_output_dictionary = regression_module.compute_batch_outputs(
        batch_dictionary
    )
    loss = batch_output_dictionary["loss"]
    assert bool(torch.isfinite(loss))
    loss.backward()
    finite_gradient_count = 0
    for parameter in gradient_model.parameters():
        if parameter.grad is None:
            continue
        assert bool(torch.all(torch.isfinite(parameter.grad)))
        finite_gradient_count += 1
    assert finite_gradient_count > 0
    optimizer = regression_module.configure_optimizers()
    frozen_parameter_id_set = {
        id(parameter)
        for parameter in gradient_model.parameters()
        if not parameter.requires_grad
    }
    optimizer_parameter_id_set = {
        id(parameter)
        for group in optimizer.param_groups
        for parameter in group["params"]
    }
    assert not (frozen_parameter_id_set & optimizer_parameter_id_set)

    return {
        "maximum_zero_initialization_error": (
            maximum_zero_initialization_error
        ),
        "maximum_signed_torque_replay_error": (
            maximum_signed_torque_replay_error
        ),
        "maximum_bounded_residual_deg": maximum_bounded_residual,
        "declared_residual_bound_deg": (
            bounded_model.residual_bound_deg
        ),
        "reconstruction_error_by_candidate": (
            reconstruction_error_map
        ),
        "partial_unfreeze_column_set": sorted(
            actual_nonzero_column_set
        ),
        "frozen_surface_sha256": original_surface_hash,
        "finite_gradient_tensor_count": finite_gradient_count,
        "frozen_parameters_absent_from_optimizer": True,
    }


def validate_parameter_matching(
    queue_configuration_list: list[dict[str, Any]],
    calibration_payload: dict[str, Any],
) -> list[dict[str, Any]]:
    """Confirm real trainable parameter counts and the five-percent gate."""

    real_parameter_count_map: dict[str, int] = {}
    for configuration in queue_configuration_list:
        candidate_id = str(configuration["metadata"]["candidate_id"])
        model = load_model_from_configuration(configuration)
        real_parameter_count_map[candidate_id] = sum(
            parameter.numel()
            for parameter in model.parameters()
            if parameter.requires_grad
        )

    result_row_list: list[dict[str, Any]] = []
    for calibration_row in calibration_payload[
        "parameter_match_row_list"
    ]:
        control_id = calibration_row["control_id"]
        hybrid_id = calibration_row["hybrid_id"]
        control_count = real_parameter_count_map[control_id]
        hybrid_count = real_parameter_count_map[hybrid_id]
        mismatch_fraction = abs(control_count - hybrid_count) / hybrid_count
        assert mismatch_fraction <= 0.05
        result_row_list.append(
            {
                "control_id": control_id,
                "hybrid_id": hybrid_id,
                "control_parameter_count": control_count,
                "hybrid_parameter_count": hybrid_count,
                "mismatch_fraction": mismatch_fraction,
                "passes": True,
            }
        )
    return result_row_list


def main() -> None:
    """Run all deterministic Stage 4 preflight gates."""

    campaign_manifest = load_yaml(CAMPAIGN_MANIFEST_PATH)
    calibration_payload = load_yaml(CALIBRATION_PATH)
    assert campaign_manifest["expected_run_count"] == 18
    assert len(campaign_manifest["queue_config_path_list"]) == 18
    assert campaign_manifest["dataset_name"] == "polished_dataset"
    assert campaign_manifest["input_mode"] == "setpoints"
    assert campaign_manifest["primary_surface"] == "fw"
    assert (
        SUPPORTED_MODEL_ENTRYPOINT_NAME_DICTIONARY[
            "data_only_residual_capacity"
        ]
        == "scripts/training/train_feedforward_network.py"
    )
    assert (
        campaign_manifest["common_split_signature"]
        == calibration_payload["split_signature"]
    )

    queue_configuration_list = [
        load_yaml(PROJECT_ROOT / queue_path_text)
        for queue_path_text in campaign_manifest[
            "queue_config_path_list"
        ]
    ]
    candidate_id_list = [
        configuration["metadata"]["candidate_id"]
        for configuration in queue_configuration_list
    ]
    assert candidate_id_list == [
        "C01",
        "C02",
        "C03",
        "C04",
        "C05",
        "C06",
        "H01",
        "H02",
        "H03",
        "H04",
        "H05",
        "H06",
        "H07",
        "H08",
        "A01",
        "A02",
        "A03",
        "A04",
    ]
    assert all(
        configuration["metadata"]["use_forward_direction"]
        and not configuration["metadata"]["use_backward_direction"]
        and configuration["metadata"]["input_mode"] == "setpoints"
        for configuration in queue_configuration_list
    )

    model_validation = validate_model_formulations(
        queue_configuration_list
    )
    parameter_match_row_list = validate_parameter_matching(
        queue_configuration_list,
        calibration_payload,
    )
    dataloader_fingerprint_map = validate_dataloader_reproducibility()
    real_dataset_gate_passed = False
    if REAL_DATASET_ONE_BATCH_SUMMARY_PATH.is_file():
        real_dataset_payload = load_yaml(
            REAL_DATASET_ONE_BATCH_SUMMARY_PATH
        )
        real_dataset_gate_passed = (
            real_dataset_payload["status"] == "passed"
            and int(
                real_dataset_payload["completed_configuration_count"]
            )
            == 18
            and int(
                real_dataset_payload["failed_configuration_count"]
            )
            == 0
        )
    launcher_gate_passed = False
    if LAUNCHER_PREFLIGHT_SUMMARY_PATH.is_file():
        launcher_payload = load_yaml(LAUNCHER_PREFLIGHT_SUMMARY_PATH)
        launcher_gate_passed = (
            launcher_payload["status"] == "passed"
            and int(
                launcher_payload["local_preflight"]["exit_code"]
            )
            == 0
            and int(
                launcher_payload["remote_compatible_preflight"][
                    "exit_code"
                ]
            )
            == 0
        )
    pending_external_gate_list: list[str] = []
    if not real_dataset_gate_passed:
        pending_external_gate_list.append(
            "all eighteen real dataset one-batch validations"
        )
    if not launcher_gate_passed:
        pending_external_gate_list.extend(
            [
                "local launcher preflight",
                "remote launcher dry preflight",
            ]
        )
    validation_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage4",
        "status": "passed",
        "validated_queue_count": len(queue_configuration_list),
        "candidate_id_list": candidate_id_list,
        "model_validation": model_validation,
        "parameter_match_row_list": parameter_match_row_list,
        "dataloader_fingerprint_map": dataloader_fingerprint_map,
        "external_gate_status": {
            "real_dataset_one_batch_passed": (
                real_dataset_gate_passed
            ),
            "local_launcher_preflight_passed": launcher_gate_passed,
            "remote_launcher_preflight_passed": launcher_gate_passed,
        },
        "gate_summary": {
            "passed_gate_count": (
                13
                + int(real_dataset_gate_passed)
                + (2 * int(launcher_gate_passed))
            ),
            "failed_gate_count": 0,
            "pending_external_gate_list": pending_external_gate_list,
        },
    }
    VALIDATION_SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    VALIDATION_SUMMARY_PATH.write_text(
        json.dumps(validation_payload, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(validation_payload, indent=2))


if __name__ == "__main__":
    main()
