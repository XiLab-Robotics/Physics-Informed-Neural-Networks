"""Prepare registry pointers and the bounded Phase 3 curve-first matrix."""

from __future__ import annotations

# Import Python Utilities
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Repository Paths
PROJECT_PATH = Path(__file__).resolve().parents[4]
CAMPAIGN_NAME = "phase3_quasi_static_compliance_pinn_2026_07_26"
CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "training_campaigns"
    / "2026-07-26-17-46-18_phase3_quasi_static_compliance_pinn_2026_07_26"
)
CAMPAIGN_LEADERBOARD_PATH = (
    CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.yaml"
)
CANDIDATE_REGISTRY_DIRECTORY = (
    CAMPAIGN_OUTPUT_DIRECTORY / "candidate_registries"
)
MATRIX_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "phase3_quasi_static_compliance_pinn_common_test_matrix.yaml"
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


def resolve_formulation_and_surface(
    leaderboard_entry: dict[str, Any],
) -> tuple[str, str, str]:
    """Resolve formulation, readable role, and report surface."""

    output_directory = PROJECT_PATH / str(
        leaderboard_entry["output_directory"]
    ).replace("\\", "/")
    training_configuration = read_yaml(
        output_directory / "training_config.yaml"
    )
    formulation = str(
        training_configuration["model"]["formulation"]
    ).strip().upper()
    role_name = str(
        training_configuration["metadata"]["intervention"]
    ).strip()
    training_variant = str(
        leaderboard_entry["training_variant"]
    ).strip().lower()
    surface = {
        "fw": "Fw",
        "bw": "Bw",
        "global": "global",
    }[training_variant]
    return formulation, role_name, surface


def build_phase3_candidate_configuration_list(
    leaderboard_entry_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Persist one registry pointer and matrix row per canonical run."""

    candidate_configuration_list: list[dict[str, Any]] = []
    for leaderboard_entry in sorted(
        leaderboard_entry_list,
        key=lambda entry: (
            str(entry["training_variant"]),
            str(entry["model_family"]),
        ),
    ):
        formulation, role_name, surface = resolve_formulation_and_surface(
            leaderboard_entry
        )
        registry_filename = (
            f"{formulation.lower()}_{role_name}_{surface.lower()}.yaml"
        )
        registry_path = (
            CANDIDATE_REGISTRY_DIRECTORY / registry_filename
        )
        registry_payload = {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "selection_role": "canonical_campaign_checkpoint",
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

        allowed_direction_list = (
            ["forward", "backward"]
            if surface == "global"
            else [surface.lower().replace("fw", "forward").replace(
                "bw",
                "backward",
            )]
        )
        candidate_configuration_list.append(
            {
                "candidate_id": (
                    f"phase3_{formulation.lower()}_{role_name}_{surface}"
                ),
                "candidate_family": leaderboard_entry["model_family"],
                "candidate_kind": "wave1_registry_model",
                "candidate_source_label": (
                    "phase3_canonical_campaign"
                ),
                "candidate_surface": surface,
                "family_registry_path": (
                    format_project_relative_path(registry_path)
                ),
                "expected_dataset_name": "polished_dataset",
                "allowed_direction_list": allowed_direction_list,
            }
        )
    return candidate_configuration_list


def build_accepted_reference_configuration_list() -> list[dict[str, Any]]:
    """Build the accepted non-windowed and time-windowed comparators."""

    candidate_configuration_list: list[dict[str, Any]] = []
    for surface, direction_name, archive_direction in [
        ("Fw", "forward", "forward"),
        ("Bw", "backward", "backward"),
    ]:
        candidate_configuration_list.extend(
            [
                {
                    "candidate_id": (
                        f"accepted_periodic_mlp_harmonic_{surface}"
                    ),
                    "candidate_family": "periodic_mlp_harmonic",
                    "candidate_kind": "wave1_exported_model",
                    "candidate_source_label": (
                        "accepted_non_windowed_reference"
                    ),
                    "candidate_surface": surface,
                    "reference_inventory_path": (
                        "models/polished_dataset/setpoints/"
                        f"periodic_mlp_harmonic/{archive_direction}/"
                        "reference_inventory.yaml"
                    ),
                    "allowed_direction_list": [direction_name],
                },
                {
                    "candidate_id": (
                        f"accepted_periodic_gru_sequence_{surface}"
                    ),
                    "candidate_family": "periodic_gru_sequence",
                    "candidate_kind": "wave1_exported_model",
                    "candidate_source_label": (
                        "accepted_time_windowed_reference"
                    ),
                    "candidate_surface": surface,
                    "reference_inventory_path": (
                        "models/polished_dataset/setpoints/"
                        f"periodic_gru_sequence/{archive_direction}/"
                        "reference_inventory.yaml"
                    ),
                    "allowed_direction_list": [direction_name],
                },
            ]
        )
    return candidate_configuration_list


def main() -> None:
    """Create the canonical Phase 3 bounded curve-first matrix."""

    leaderboard_payload = read_yaml(CAMPAIGN_LEADERBOARD_PATH)
    leaderboard_entry_list = leaderboard_payload["entry_list"]
    assert isinstance(leaderboard_entry_list, list)
    assert len(leaderboard_entry_list) == 12

    candidate_configuration_list = (
        build_phase3_candidate_configuration_list(leaderboard_entry_list)
        + build_accepted_reference_configuration_list()
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
                "phase3_quasi_static_compliance_pinn_common_test_matrix"
            ),
            "model_family": "track2_reference_comparison",
            "model_type": "reference_family_vs_feedforward",
        },
        "comparison": {
            "comparison_mode": (
                "phase3_common_split_bounded_curve_payload_diagnostics"
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
    }
    write_yaml(MATRIX_CONFIG_PATH, matrix_payload)
    print(
        "PHASE3_CURVE_FIRST_MATRIX_PREPARED "
        f"phase3_candidates=12 references=4 "
        f"registries={CANDIDATE_REGISTRY_DIRECTORY.relative_to(PROJECT_PATH)}"
    )
    print(MATRIX_CONFIG_PATH.relative_to(PROJECT_PATH).as_posix())


if __name__ == "__main__":
    main()
