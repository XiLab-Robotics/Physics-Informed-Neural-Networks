"""Prepare the bounded Stage 4 data-only residual curve-first matrix."""

from __future__ import annotations

# Import Python Utilities
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml


# Define Repository Paths
PROJECT_ROOT = Path(__file__).resolve().parents[4]
CAMPAIGN_NAME = "wave52r_stage4_data_only_residual_capacity_2026_07_28"
CAMPAIGN_OUTPUT_ROOT = PROJECT_ROOT / "output" / "training_campaigns"
MATRIX_CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "wave52r_stage4_data_only_residual_common_test_matrix.yaml"
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

    return path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix()


def resolve_completed_campaign_output_directory() -> Path:
    """Resolve the unique successful eighteen-run Stage 4 campaign."""

    candidate_directory_list = sorted(
        CAMPAIGN_OUTPUT_ROOT.glob(f"*_{CAMPAIGN_NAME}")
    )
    completed_directory_list: list[Path] = []
    for candidate_directory in candidate_directory_list:
        leaderboard_path = candidate_directory / "campaign_leaderboard.yaml"
        if not leaderboard_path.is_file():
            continue
        leaderboard_payload = read_yaml(leaderboard_path)
        entry_list = leaderboard_payload.get("entry_list", [])
        if isinstance(entry_list, list) and len(entry_list) == 18:
            completed_directory_list.append(candidate_directory)
    assert len(completed_directory_list) == 1, (
        "Expected one successful Stage 4 campaign | "
        f"matches={len(completed_directory_list)}"
    )
    return completed_directory_list[0]


def build_candidate_configuration_list(
    campaign_output_directory: Path,
) -> list[dict[str, Any]]:
    """Persist one registry pointer and matrix row per Stage 4 run."""

    leaderboard_payload = read_yaml(
        campaign_output_directory / "campaign_leaderboard.yaml"
    )
    leaderboard_entry_list = leaderboard_payload["entry_list"]
    assert isinstance(leaderboard_entry_list, list)
    assert len(leaderboard_entry_list) == 18

    candidate_registry_directory = (
        campaign_output_directory / "candidate_registries"
    )
    candidate_configuration_list: list[dict[str, Any]] = []
    sortable_entry_list: list[tuple[int, dict[str, Any], dict[str, Any]]] = []
    for leaderboard_entry in leaderboard_entry_list:
        output_directory = (
            PROJECT_ROOT
            / str(leaderboard_entry["output_directory"]).replace("\\", "/")
        )
        training_configuration = read_yaml(
            output_directory / "training_config.yaml"
        )
        queue_index = int(
            training_configuration["metadata"]["queue_index"]
        )
        sortable_entry_list.append(
            (queue_index, leaderboard_entry, training_configuration)
        )

    for (
        queue_index,
        leaderboard_entry,
        training_configuration,
    ) in sorted(sortable_entry_list, key=lambda value: value[0]):
        metadata = training_configuration["metadata"]
        candidate_id = str(metadata["candidate_id"])
        formulation = str(
            training_configuration["model"]["formulation"]
        ).upper()
        capacity_level = str(metadata["capacity_level"])
        registry_path = (
            candidate_registry_directory
            / f"{queue_index:03d}_{candidate_id.lower()}_"
            f"{formulation.lower()}_{capacity_level}.yaml"
        )
        registry_payload = {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "selection_role": "stage4_screening_checkpoint",
            "candidate_id": candidate_id,
            "formulation": formulation,
            "capacity_level": capacity_level,
            "matched_candidate_id": metadata["matched_candidate_id"],
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
        candidate_configuration_list.append(
            {
                "candidate_id": (
                    f"stage4_{candidate_id.lower()}_"
                    f"{formulation.lower()}_{capacity_level}"
                ),
                "candidate_family": leaderboard_entry["model_family"],
                "candidate_kind": "wave1_registry_model",
                "candidate_source_label": (
                    "wave52r_stage4_screening_campaign"
                ),
                "candidate_surface": "Fw",
                "family_registry_path": (
                    format_project_relative_path(registry_path)
                ),
                "expected_dataset_name": "polished_dataset",
                "allowed_direction_list": ["forward"],
            }
        )
    return candidate_configuration_list


def main() -> None:
    """Create the eighteen-candidate bounded forward comparison matrix."""

    campaign_output_directory = (
        resolve_completed_campaign_output_directory()
    )
    candidate_configuration_list = build_candidate_configuration_list(
        campaign_output_directory
    )
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
            "run_name": (
                "wave52r_stage4_data_only_residual_common_test_matrix"
            ),
            "model_family": "track2_reference_comparison",
            "model_type": "reference_family_vs_feedforward",
        },
        "comparison": {
            "comparison_mode": (
                "wave52r_stage4_bounded_forward_curve_first"
            ),
            "lightweight_test_curve_records": True,
            "percentage_error_denominator": "peak_to_peak_truth",
            "preview_curve_count": 3,
            "candidate_list": candidate_configuration_list,
        },
        "evaluation": {
            "selected_harmonics": list(SELECTED_HARMONIC_LIST),
            "decomposition_point_stride": 1,
        },
        "metadata": {
            "campaign_output_directory": (
                format_project_relative_path(campaign_output_directory)
            ),
            "official_te_curve_verification_pipeline_refresh": False,
            "usage": (
                "bounded Stage 4 campaign closeout comparison only"
            ),
        },
    }
    write_yaml(MATRIX_CONFIG_PATH, matrix_payload)
    print(
        "STAGE4_CURVE_FIRST_MATRIX_PREPARED "
        f"candidates={len(candidate_configuration_list)}"
    )
    print(format_project_relative_path(MATRIX_CONFIG_PATH))


if __name__ == "__main__":
    main()
