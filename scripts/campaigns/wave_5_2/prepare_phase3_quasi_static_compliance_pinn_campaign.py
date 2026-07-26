"""Prepare the bounded Wave 5.2 Phase 3 compliance-PINN campaign."""

from __future__ import annotations

# Import Python Utilities
from copy import deepcopy
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Campaign Constants
PROJECT_ROOT = Path(__file__).resolve().parents[3]
CAMPAIGN_NAME = "phase3_quasi_static_compliance_pinn_2026_07_26"
CAMPAIGN_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "quasi_static_compliance_pinn"
    / "campaigns"
    / "2026-07-26_phase3_quasi_static_compliance_pinn"
)
QUEUE_DIRECTORY = CAMPAIGN_DIRECTORY / "queue"
PLANNING_REPORT_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "quasi_static_compliance_pinn/"
    "2026-07-26-17-16-41_phase3_quasi_static_compliance_pinn_"
    "campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-26/"
    "2026-07-26-17-14-40_phase_3_quasi_static_compliance_pinn.md"
)
MODEL_REPORT_PATH = (
    "doc/reports/analysis/model_development_waves/wave_5_2/"
    "quasi_static_compliance_pinn/[2026-07-26]/"
    "phase3_quasi_static_compliance_pinn_model_report.md"
)
AUDIT_ARTIFACT_PATH = (
    "output/analysis/pinn_program_compliance/"
    "phase3_compliance_audit.yaml"
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
FORMULATION_NAME_DICTIONARY = {
    "C0": "learned_mean_control",
    "C1": "linear_compliance_soft",
    "C2": "temperature_compliance_soft",
    "C3": "nonlinear_compliance_soft",
    "C4": "hard_elastic_offset",
    "C5": "shared_stiffness",
}


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
            "dataset_config_path": (
                "config/datasets/transmission_error_dataset.yaml"
            ),
            "output_root": (
                "output/training_runs/quasi_static_compliance_pinn"
            ),
        },
        "experiment": {
            "run_name": "",
            "model_family": "",
            "model_type": "quasi_static_compliance_pinn",
        },
        "metadata": {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": PLANNING_REPORT_PATH,
            "technical_document_path": TECHNICAL_DOCUMENT_PATH,
            "model_report_path": MODEL_REPORT_PATH,
            "audit_artifact_path": AUDIT_ARTIFACT_PATH,
            "phase_name": (
                "wave_5_2_phase_3_quasi_static_compliance_pinn"
            ),
            "campaign_config_id": "",
            "queue_index": 0,
            "intervention": "",
            "probe_group": "phase3_quasi_static_compliance_pinn",
            "loss_profile": "",
            "dataset_name": "polished_dataset",
            "input_mode": "setpoints",
            "dataset_schema": "polished_setpoint_curve_v1",
            "source_dataset_root": "data/polished_dataset",
            "training_variant": "",
            "direction_scope_label": "",
            "use_forward_direction": False,
            "use_backward_direction": False,
            "signed_torque_convention": (
                "Fw measured torque negative; Bw measured torque positive"
            ),
            "initial_stiffness_source": (
                "Phase 3 training-only identifiability audit"
            ),
            "promotion_rule": (
                "No scalar-only promotion. Retain only a bounded positive "
                "stiffness formulation that improves held-out raw and offset "
                "behavior without material centered-shape or harmonic "
                "regression."
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
            "excluded_condition_id_list": list(
                EXCLUDED_CONDITION_ID_LIST
            ),
            "expected_curve_count_by_split": {},
        },
        "model": {
            "input_size": "auto",
            "output_size": 1,
            "harmonic_index_list": list(HARMONIC_INDEX_LIST),
            "condition_hidden_size": [64, 48],
            "condition_latent_size": 32,
            "mean_hidden_size": [32, 16],
            "formulation": "",
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
            "torque_input_mode": "nominal_magnitude",
        },
        "training": {
            "learning_rate": 5.0e-4,
            "weight_decay": 1.0e-5,
            "min_epochs": 4,
            "max_epochs": 20,
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
                    "offset": 0.12,
                    "amplitude": 0.04,
                    "harmonic": 0.10,
                    "derivative": 0.01,
                    "physics_oscillator": 0.0,
                    "physics_periodic_value": 0.0,
                    "physics_periodic_slope": 0.0,
                    "physics_analytical_anchor": 0.0,
                    "physics_compliance_equation": 0.0,
                    "physics_zero_torque_boundary": 0.0,
                    "physics_compliance_monotonicity": 0.0,
                    "physics_stiffness_bounds": 0.0,
                    "physics_periodic_mean": 0.0,
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
    formulation: str,
    surface: str,
) -> dict[str, Any]:
    """Build one formulation and directional-surface configuration."""

    assert formulation in FORMULATION_NAME_DICTIONARY
    assert surface in {"fw", "bw", "global"}
    configuration = deepcopy(build_base_configuration())
    formulation_name = FORMULATION_NAME_DICTIONARY[formulation]
    formulation_slug = formulation.lower()
    run_slug = (
        f"phase3_pinn_{formulation_slug}_{formulation_name}_{surface}"
    )
    use_forward_direction = surface in {"fw", "global"}
    use_backward_direction = surface in {"bw", "global"}
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
            "intervention": formulation_name,
            "loss_profile": f"phase3_{formulation_name}",
            "training_variant": surface,
            "direction_scope_label": {
                "fw": "forward_only",
                "bw": "backward_only",
                "global": "bidirectional",
            }[surface],
            "use_forward_direction": use_forward_direction,
            "use_backward_direction": use_backward_direction,
            "roadmap_role_coverage": {
                "C0": ["learned_mean_external_control"],
                "C1": ["linear_compliance_soft_residual"],
                "C2": ["temperature_conditioned_soft_residual"],
                "C3": ["nonlinear_monotonic_soft_residual"],
                "C4": ["hard_directional_elastic_equation"],
                "C5": ["hard_shared_stiffness_equation"],
            }[formulation],
        }
    )
    direction_multiplier = 2 if surface == "global" else 1
    configuration["dataset"]["expected_curve_count_by_split"] = {
        "train": 675 * direction_multiplier,
        "validation": 194 * direction_multiplier,
        "test": 97 * direction_multiplier,
    }
    configuration["model"]["formulation"] = formulation
    configuration["training"]["loss"]["profile"] = (
        f"phase3_{formulation_name}"
    )
    weights = configuration["training"]["loss"]["weights"]

    if formulation == "C0":
        configuration["training"]["loss"][
            "enable_physics_diagnostics"
        ] = False
    elif formulation in {"C1", "C2", "C3"}:
        weights["physics_compliance_equation"] = 0.02
        weights["physics_zero_torque_boundary"] = 0.01
        weights["physics_compliance_monotonicity"] = 0.01
        weights["physics_stiffness_bounds"] = 0.001
        weights["physics_periodic_mean"] = 0.005
    else:
        weights["physics_compliance_equation"] = 0.001
        weights["physics_zero_torque_boundary"] = 0.001
        weights["physics_stiffness_bounds"] = 0.001
        weights["physics_periodic_mean"] = 0.005
    return configuration


def main() -> None:
    """Create the twelve-run manifest and queue package."""

    run_specification_list = [
        ("C0", "fw"),
        ("C0", "bw"),
        ("C0", "global"),
        ("C1", "fw"),
        ("C1", "bw"),
        ("C2", "fw"),
        ("C2", "bw"),
        ("C3", "fw"),
        ("C3", "bw"),
        ("C4", "fw"),
        ("C4", "bw"),
        ("C5", "global"),
    ]
    queue_path_list: list[str] = []
    for queue_index, (formulation, surface) in enumerate(
        run_specification_list,
        start=1,
    ):
        configuration = build_run_configuration(
            queue_index,
            formulation,
            surface,
        )
        formulation_name = FORMULATION_NAME_DICTIONARY[formulation]
        queue_path = QUEUE_DIRECTORY / (
            f"{queue_index:03d}_{formulation.lower()}_"
            f"{formulation_name}_{surface}.yaml"
        )
        write_yaml(queue_path, configuration)
        queue_path_list.append(
            queue_path.relative_to(PROJECT_ROOT).as_posix()
        )

    campaign_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": (
            "wave_5_2_phase_3_quasi_static_compliance_pinn"
        ),
        "family_name": "quasi_static_compliance_pinn",
        "dataset_name": "polished_dataset",
        "input_mode": "setpoints",
        "dataset_schema": "polished_setpoint_curve_v1",
        "source_dataset_root": "data/polished_dataset",
        "primary_surface": "direction_separated_with_global_controls",
        "expected_surface_list": ["fw", "bw", "global"],
        "expected_run_count": len(queue_path_list),
        "planning_report_path": PLANNING_REPORT_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "model_report_path": MODEL_REPORT_PATH,
        "audit_artifact_path": AUDIT_ARTIFACT_PATH,
        "common_split_manifest_path": COMMON_SPLIT_MANIFEST_PATH,
        "common_split_signature": (
            "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f"
            "4376aa64f8e16"
        ),
        "excluded_condition_id_list": list(
            EXCLUDED_CONDITION_ID_LIST
        ),
        "directional_curve_count_by_split": {
            "train": 675,
            "validation": 194,
            "test": 97,
        },
        "global_curve_count_by_split": {
            "train": 1350,
            "validation": 388,
            "test": 194,
        },
        "queue_root": (
            "config/training/queue/quasi_static_compliance_pinn/"
            f"{CAMPAIGN_NAME}"
        ),
        "queue_config_path_list": queue_path_list,
        "execution_policy": {
            "operator_run_required": False,
            "standing_approval_applies": True,
            "stop_on_error": True,
            "run_te_curve_verification_pipeline": False,
            "scalar_mae_only_promotion_allowed": False,
        },
    }
    write_yaml(CAMPAIGN_DIRECTORY / "campaign.yaml", campaign_payload)
    print(
        f"Prepared {len(queue_path_list)} Phase 3 queue configurations"
    )
    print(CAMPAIGN_DIRECTORY.relative_to(PROJECT_ROOT).as_posix())


if __name__ == "__main__":
    main()
