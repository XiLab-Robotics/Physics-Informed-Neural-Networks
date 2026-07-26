"""Prepare the direction-separated Wave 5.2 Phase 2 PINN campaign package."""

from __future__ import annotations

# Import Python Utilities
from copy import deepcopy
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Campaign Constants
PROJECT_ROOT = Path(__file__).resolve().parents[3]
CAMPAIGN_NAME = (
    "phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26"
)
CAMPAIGN_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "harmonic_kinematic_pinn"
    / "campaigns"
    / "2026-07-26_phase2_harmonic_kinematic_pinn"
)
QUEUE_DIRECTORY = CAMPAIGN_DIRECTORY / "queue"
PLANNING_REPORT_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "harmonic_kinematic_pinn/"
    "2026-07-25-20-44-23_phase2_harmonic_kinematic_pinn_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-25/"
    "2026-07-25-20-40-44_phase_2_harmonic_kinematic_pinn.md"
)
MODEL_REPORT_PATH = (
    "doc/reports/analysis/model_development_waves/wave_5_2/"
    "harmonic_kinematic_pinn/[2026-07-26]/"
    "phase2_harmonic_kinematic_pinn_model_report.md"
)
ANALYTICAL_ANCHOR_PATH = (
    "output/analysis/polynomial_fourier_benchmark/"
    "phase1_coefficient_models.yaml"
)
COMMON_SPLIT_MANIFEST_PATH = (
    "output/analysis/polynomial_fourier_benchmark/"
    "common_split_manifest.yaml"
)
EXCLUDED_CONDITION_ID_LIST = [
    "speed_500rpm__torque_600Nm__temperature_35degC",
    "speed_800rpm__torque_200Nm__temperature_25degC",
    "speed_1400rpm__torque_800Nm__temperature_35degC",
]
HARMONIC_INDEX_LIST = [1, 3, 39, 40, 78, 81, 156, 162, 240]


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping with a normal final newline."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def build_base_configuration() -> dict[str, Any]:
    """Build the common causal data, model, training, and runtime contract."""

    return {
        "paths": {
            "dataset_config_path": "config/datasets/transmission_error_dataset.yaml",
            "output_root": "output/training_runs/harmonic_kinematic_pinn",
        },
        "experiment": {
            "run_name": "",
            "model_family": "",
            "model_type": "harmonic_kinematic_pinn",
        },
        "metadata": {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": PLANNING_REPORT_PATH,
            "technical_document_path": TECHNICAL_DOCUMENT_PATH,
            "model_report_path": MODEL_REPORT_PATH,
            "phase_name": "wave_5_2_phase_2_harmonic_kinematic_pinn",
            "campaign_config_id": "",
            "queue_index": 0,
            "intervention": "",
            "probe_group": "phase2_harmonic_kinematic_pinn",
            "loss_profile": "",
            "dataset_name": "polished_dataset",
            "input_mode": "setpoints",
            "dataset_schema": "polished_setpoint_curve_v1",
            "source_dataset_root": "data/polished_dataset",
            "training_variant": "",
            "direction_scope_label": "",
            "use_forward_direction": False,
            "use_backward_direction": False,
            "analytical_reference_model_id": "PF_A_LOCAL_QUADRATIC",
            "alternative_comparator_model_id": "PF_E_REDUCED_QUADRATIC",
            "harmonic_index_list": list(HARMONIC_INDEX_LIST),
            "promotion_rule": (
                "No scalar-only promotion. A physics arm must improve held-out "
                "harmonic fidelity without material raw-error, offset, or "
                "continuity regression."
            ),
        },
        "dataset": {
            "curve_batch_size": 4,
            "point_stride": 8,
            "maximum_points_per_curve": 4096,
            "num_workers": 2,
            "pin_memory": True,
            "name": "polished_dataset",
            "input_mode": "setpoints",
            "split_manifest_path": COMMON_SPLIT_MANIFEST_PATH,
            "excluded_condition_id_list": list(EXCLUDED_CONDITION_ID_LIST),
            "expected_curve_count_by_split": {
                "train": 675,
                "validation": 194,
                "test": 97,
            },
        },
        "model": {
            "input_size": "auto",
            "output_size": 1,
            "harmonic_index_list": list(HARMONIC_INDEX_LIST),
            "condition_hidden_size": [64, 48],
            "condition_latent_size": 32,
            "component_hidden_size": [24, 16],
            "head_mode": "implicit_pinn",
            "activation_name": "Tanh",
            "dropout_probability": 0.0,
            "use_layer_norm": False,
        },
        "training": {
            "learning_rate": 5.0e-4,
            "weight_decay": 1.0e-5,
            "min_epochs": 4,
            "max_epochs": 24,
            "patience": 5,
            "min_delta": 1.0e-5,
            "log_every_n_steps": 1,
            "fast_dev_run": False,
            "deterministic": False,
            "loss": {
                "profile": "",
                "pointwise_loss": "mse",
                "enable_physics_diagnostics": True,
                "physics_maximum_collocation_points": 64,
                "physics_maximum_boundary_conditions": 12,
                "weights": {
                    "point": 1.0,
                    "centered": 0.10,
                    "offset": 0.08,
                    "amplitude": 0.04,
                    "harmonic": 0.10,
                    "derivative": 0.01,
                    "physics_oscillator": 0.0,
                    "physics_periodic_value": 0.0,
                    "physics_periodic_slope": 0.0,
                    "physics_analytical_anchor": 0.0,
                },
                "harmonic_index_list": list(HARMONIC_INDEX_LIST),
            },
        },
        "runtime": {
            "accelerator": "auto",
            "devices": "auto",
            "precision": "32",
            "benchmark": True,
            "use_non_blocking_transfer": True,
        },
    }


def build_run_configuration(
    queue_index: int,
    role_id: str,
    direction: str,
) -> dict[str, Any]:
    """Build one Phase 2 role and direction configuration."""

    assert role_id in {"h0", "h1", "h2", "h3"}
    assert direction in {"fw", "bw"}
    configuration = deepcopy(build_base_configuration())
    role_name_map = {
        "h0": "fourier_control",
        "h1": "oscillator_residual",
        "h2": "oscillator_periodic_closure",
        "h3": "oscillator_periodic_bauer_anchor",
    }
    role_name = role_name_map[role_id]
    run_slug = f"phase2_pinn_{role_id}_{role_name}_{direction}"
    direction_label = "Fw" if direction == "fw" else "Bw"
    configuration["experiment"].update(
        {
            "run_name": f"te_{run_slug}__polished_setpoints",
            "model_family": run_slug,
        }
    )
    configuration["metadata"].update(
        {
            "campaign_config_id": run_slug,
            "queue_index": queue_index,
            "intervention": role_name,
            "loss_profile": f"phase2_{role_name}",
            "training_variant": direction,
            "direction_scope_label": (
                "forward_only" if direction == "fw" else "backward_only"
            ),
            "use_forward_direction": direction == "fw",
            "use_backward_direction": direction == "bw",
            "roadmap_role_coverage": {
                "h0": ["fourier_head_only_external_control"],
                "h1": ["PINN-H2", "PINN-H5"],
                "h2": ["PINN-H1", "PINN-H2", "PINN-H5"],
                "h3": ["PINN-H3", "PINN-H4", "PINN-H5"],
            }[role_id],
        }
    )
    configuration["training"]["loss"]["profile"] = f"phase2_{role_name}"
    weights = configuration["training"]["loss"]["weights"]

    if role_id == "h0":
        configuration["model"]["head_mode"] = "explicit_fourier"
        configuration["training"]["loss"]["enable_physics_diagnostics"] = False
    if role_id == "h1":
        weights["physics_oscillator"] = 0.01
    if role_id in {"h2", "h3"}:
        weights["physics_oscillator"] = 0.01
        weights["physics_periodic_value"] = 0.01
        weights["physics_periodic_slope"] = 0.001
    if role_id == "h3":
        weights["physics_analytical_anchor"] = 0.05
        configuration["model"].update(
            {
                "analytical_anchor_path": ANALYTICAL_ANCHOR_PATH,
                "analytical_anchor_model_id": "PF_A_LOCAL_QUADRATIC",
                "analytical_anchor_direction": direction_label,
            }
        )
    return configuration


def main() -> None:
    """Create the eight-run manifest and queue package."""

    run_specification_list = [
        ("h0", "fw"),
        ("h0", "bw"),
        ("h1", "fw"),
        ("h1", "bw"),
        ("h2", "fw"),
        ("h2", "bw"),
        ("h3", "fw"),
        ("h3", "bw"),
    ]
    queue_path_list: list[str] = []
    for queue_index, (role_id, direction) in enumerate(
        run_specification_list,
        start=1,
    ):
        configuration = build_run_configuration(
            queue_index,
            role_id,
            direction,
        )
        role_name = configuration["metadata"]["intervention"]
        queue_path = QUEUE_DIRECTORY / (
            f"{queue_index:03d}_{role_id}_{role_name}_{direction}.yaml"
        )
        write_yaml(queue_path, configuration)
        queue_path_list.append(queue_path.relative_to(PROJECT_ROOT).as_posix())

    campaign_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": "wave_5_2_phase_2_harmonic_kinematic_pinn",
        "family_name": "harmonic_kinematic_pinn",
        "dataset_name": "polished_dataset",
        "input_mode": "setpoints",
        "dataset_schema": "polished_setpoint_curve_v1",
        "source_dataset_root": "data/polished_dataset",
        "primary_surface": "direction_separated",
        "expected_surface_list": ["fw", "bw"],
        "expected_run_count": len(queue_path_list),
        "planning_report_path": PLANNING_REPORT_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "model_report_path": MODEL_REPORT_PATH,
        "analytical_anchor_path": ANALYTICAL_ANCHOR_PATH,
        "common_split_manifest_path": COMMON_SPLIT_MANIFEST_PATH,
        "excluded_condition_id_list": list(EXCLUDED_CONDITION_ID_LIST),
        "expected_curve_count_by_split": {
            "train": 675,
            "validation": 194,
            "test": 97,
        },
        "queue_root": (
            "config/training/queue/harmonic_kinematic_pinn/"
            f"{CAMPAIGN_NAME}"
        ),
        "queue_config_path_list": queue_path_list,
        "execution_policy": {
            "operator_run_required": True,
            "stop_on_error": True,
            "run_te_curve_verification_pipeline": False,
            "scalar_mae_only_promotion_allowed": False,
        },
    }
    write_yaml(CAMPAIGN_DIRECTORY / "campaign.yaml", campaign_payload)
    print(f"Prepared {len(queue_path_list)} Phase 2 queue configurations")
    print(CAMPAIGN_DIRECTORY.relative_to(PROJECT_ROOT).as_posix())


if __name__ == "__main__":
    main()
