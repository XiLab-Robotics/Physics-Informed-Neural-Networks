"""Prepare the bounded Phase 3 C1-Fw initialization-stability matrix."""

from __future__ import annotations

# Import Python Utilities
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Repository Paths
PROJECT_PATH = Path(__file__).resolve().parents[4]
PARENT_CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "training_campaigns"
    / "2026-07-26-17-46-18_phase3_quasi_static_compliance_pinn_2026_07_26"
)
REPEAT_CAMPAIGN_NAME = "phase3_c1_fw_stability_repeat_2026_07_26"
MATRIX_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "phase3_c1_fw_stability_common_test_matrix.yaml"
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
SELECTED_HARMONIC_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]


def read_yaml(path: Path) -> dict[str, Any]:
    """Read one required YAML mapping."""

    assert path.is_file(), f"Required YAML path does not exist | {path}"
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict), f"YAML root must be a mapping | {path}"
    return payload


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


def format_project_relative_path(path: Path) -> str:
    """Format one repository path with portable separators."""

    return path.resolve().relative_to(PROJECT_PATH.resolve()).as_posix()


def resolve_repeat_campaign_output_directory() -> Path:
    """Resolve the unique completed repeat-campaign output directory."""

    campaign_root = PROJECT_PATH / "output" / "training_campaigns"
    matching_path_list = sorted(
        campaign_root.glob(f"*_{REPEAT_CAMPAIGN_NAME}")
    )
    assert len(matching_path_list) == 1, (
        "Expected exactly one stability-repeat campaign output | "
        f"matches={len(matching_path_list)}"
    )
    return matching_path_list[0]


def build_registry_candidate(
    candidate_id: str,
    family_registry_path: Path,
    candidate_family: str,
    source_label: str,
) -> dict[str, Any]:
    """Build one forward-only registry-backed comparison candidate."""

    return {
        "candidate_id": candidate_id,
        "candidate_family": candidate_family,
        "candidate_kind": "wave1_registry_model",
        "candidate_source_label": source_label,
        "candidate_surface": "Fw",
        "family_registry_path": format_project_relative_path(
            family_registry_path
        ),
        "expected_dataset_name": "polished_dataset",
        "allowed_direction_list": ["forward"],
    }


def build_repeat_candidate_list(
    repeat_campaign_output_directory: Path,
) -> list[dict[str, Any]]:
    """Persist repeat registry pointers and return their matrix rows."""

    leaderboard_payload = read_yaml(
        repeat_campaign_output_directory / "campaign_leaderboard.yaml"
    )
    entry_list = leaderboard_payload["entry_list"]
    assert isinstance(entry_list, list)
    assert len(entry_list) == 2

    candidate_registry_directory = (
        repeat_campaign_output_directory / "candidate_registries"
    )
    candidate_list: list[dict[str, Any]] = []
    for leaderboard_entry in sorted(
        entry_list,
        key=lambda entry: str(entry["model_family"]),
    ):
        output_directory = PROJECT_PATH / str(
            leaderboard_entry["output_directory"]
        ).replace("\\", "/")
        training_config = read_yaml(
            output_directory / "training_config.yaml"
        )
        random_seed = int(training_config["training"]["random_seed"])
        registry_path = (
            candidate_registry_directory
            / f"c1_linear_compliance_soft_fw_seed_{random_seed}.yaml"
        )
        registry_payload = {
            "schema_version": 1,
            "campaign_name": REPEAT_CAMPAIGN_NAME,
            "selection_role": "initialization_stability_checkpoint",
            "training_random_seed": random_seed,
            "best_entry": {
                "run_instance_id": leaderboard_entry["run_instance_id"],
                "model_family": leaderboard_entry["model_family"],
                "model_type": leaderboard_entry["model_type"],
                "dataset_id": leaderboard_entry["dataset_id"],
                "output_directory": str(
                    leaderboard_entry["output_directory"]
                ).replace("\\", "/"),
                "best_checkpoint_path": str(
                    leaderboard_entry["best_checkpoint_path"]
                ).replace("\\", "/"),
            },
        }
        write_yaml(registry_path, registry_payload)
        candidate_list.append(
            build_registry_candidate(
                candidate_id=f"phase3_c1_fw_seed_{random_seed}",
                family_registry_path=registry_path,
                candidate_family=str(leaderboard_entry["model_family"]),
                source_label="phase3_initialization_stability_repeat",
            )
        )
    return candidate_list


def build_accepted_reference_list() -> list[dict[str, Any]]:
    """Build accepted non-windowed and time-windowed Fw references."""

    return [
        {
            "candidate_id": "accepted_periodic_mlp_harmonic_Fw",
            "candidate_family": "periodic_mlp_harmonic",
            "candidate_kind": "wave1_exported_model",
            "candidate_source_label": "accepted_non_windowed_reference",
            "candidate_surface": "Fw",
            "reference_inventory_path": (
                "models/polished_dataset/setpoints/"
                "periodic_mlp_harmonic/forward/reference_inventory.yaml"
            ),
            "allowed_direction_list": ["forward"],
        },
        {
            "candidate_id": "accepted_periodic_gru_sequence_Fw",
            "candidate_family": "periodic_gru_sequence",
            "candidate_kind": "wave1_exported_model",
            "candidate_source_label": "accepted_time_windowed_reference",
            "candidate_surface": "Fw",
            "reference_inventory_path": (
                "models/polished_dataset/setpoints/"
                "periodic_gru_sequence/forward/reference_inventory.yaml"
            ),
            "allowed_direction_list": ["forward"],
        },
    ]


def main() -> None:
    """Create the six-candidate C1-Fw stability comparison matrix."""

    repeat_campaign_output_directory = (
        resolve_repeat_campaign_output_directory()
    )
    parent_registry_directory = (
        PARENT_CAMPAIGN_OUTPUT_DIRECTORY / "candidate_registries"
    )
    candidate_list = [
        build_registry_candidate(
            candidate_id="phase3_c0_learned_mean_control_Fw",
            family_registry_path=(
                parent_registry_directory
                / "c0_learned_mean_control_fw.yaml"
            ),
            candidate_family="phase3_pinn_c0_learned_mean_control_fw",
            source_label="phase3_canonical_campaign_control",
        ),
        build_registry_candidate(
            candidate_id="phase3_c1_linear_compliance_soft_Fw",
            family_registry_path=(
                parent_registry_directory
                / "c1_linear_compliance_soft_fw.yaml"
            ),
            candidate_family="phase3_pinn_c1_linear_compliance_soft_fw",
            source_label="phase3_canonical_campaign_initial_run",
        ),
    ]
    candidate_list.extend(
        build_repeat_candidate_list(repeat_campaign_output_directory)
    )
    candidate_list.extend(build_accepted_reference_list())

    matrix_payload = {
        "paths": {
            "dataset_config_path": (
                "config/datasets/transmission_error_dataset.yaml"
            ),
        },
        "dataset": {
            "name": "polished_dataset",
            "input_mode": "setpoints",
            "split_manifest_path": COMMON_SPLIT_MANIFEST_PATH,
            "excluded_condition_id_list": list(
                EXCLUDED_CONDITION_ID_LIST
            ),
            "expected_curve_count_by_split": {
                "train": 1350,
                "validation": 388,
                "test": 194,
            },
        },
        "experiment": {
            "run_name": "phase3_c1_fw_stability_common_test_matrix",
            "model_family": "track2_reference_comparison",
            "model_type": "reference_family_vs_feedforward",
        },
        "comparison": {
            "comparison_mode": (
                "phase3_c1_fw_initialization_stability_curve_first"
            ),
            "lightweight_test_curve_records": True,
            "percentage_error_denominator": "peak_to_peak_truth",
            "preview_curve_count": 3,
            "candidate_list": candidate_list,
        },
        "evaluation": {
            "selected_harmonics": list(SELECTED_HARMONIC_LIST),
            "decomposition_point_stride": 1,
        },
    }
    write_yaml(MATRIX_CONFIG_PATH, matrix_payload)
    print(
        "PHASE3_C1_FW_STABILITY_MATRIX_PREPARED "
        f"candidates={len(candidate_list)} "
        f"repeat_campaign={repeat_campaign_output_directory.name}"
    )
    print(MATRIX_CONFIG_PATH.relative_to(PROJECT_PATH).as_posix())


if __name__ == "__main__":
    main()
