"""Validate the Wave 5.2 Phase 4 hysteresis feasibility artifacts."""

from __future__ import annotations

# Import Standard Library Utilities
import argparse
import csv
from pathlib import Path
from typing import Any

# Import Configuration Utilities
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONFIGURATION_PATH = (
    PROJECT_ROOT
    / "config"
    / "analysis"
    / "pinn_program_hysteresis"
    / "phase4_hysteresis_feasibility_audit.yaml"
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Validate the Phase 4 hysteresis feasibility audit.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIGURATION_PATH,
        help="Phase 4 audit configuration path.",
    )
    return parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:
    """Resolve one project-relative path."""

    path = Path(path_value)
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle)
    assert isinstance(payload, dict), f"Expected YAML mapping | {path}"
    return payload


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    """Load all rows from one CSV artifact."""

    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    """Validate Phase 4 row counts, decisions, and gate consistency."""

    arguments = parse_arguments()
    configuration = load_yaml(resolve_project_path(arguments.config))
    output_paths = configuration["output_paths"]
    expected_inventory = configuration["expected_inventory"]
    output_directory = resolve_project_path(output_paths["output_directory"])

    raw_trajectory_path = output_directory / output_paths["raw_trajectory_csv"]
    dataset_contract_path = output_directory / output_paths["dataset_contract_csv"]
    formulation_path = (
        output_directory / output_paths["formulation_feasibility_csv"]
    )
    summary_path = output_directory / output_paths["summary_yaml"]
    report_path = resolve_project_path(output_paths["report_markdown"])

    for artifact_path in [
        raw_trajectory_path,
        dataset_contract_path,
        formulation_path,
        summary_path,
        report_path,
    ]:
        assert artifact_path.exists(), f"Missing Phase 4 artifact | {artifact_path}"

    raw_row_list = load_csv_rows(raw_trajectory_path)
    dataset_row_list = load_csv_rows(dataset_contract_path)
    formulation_row_list = load_csv_rows(formulation_path)
    summary = load_yaml(summary_path)

    assert len(raw_row_list) == int(
        expected_inventory["canonical_raw_condition_count"]
    ), f"Raw trajectory row count mismatch | {len(raw_row_list)}"
    assert len(dataset_row_list) == 4, (
        f"Dataset contract row count mismatch | {len(dataset_row_list)}"
    )
    assert len(formulation_row_list) == int(
        expected_inventory["formulation_count"]
    ), f"Formulation row count mismatch | {len(formulation_row_list)}"

    condition_id_set = {row["condition_id"] for row in raw_row_list}
    assert len(condition_id_set) == len(raw_row_list), (
        "Raw trajectory conditions must be unique"
    )
    assert {row["split"] for row in raw_row_list} == {
        "train",
        "validation",
        "test",
    }, "All common split surfaces must remain represented"
    assert all(
        row["valid_window_direction_sign_pass"] == "True"
        for row in raw_row_list
    ), "Directional speed signs must pass for every raw trajectory"
    assert all(
        row["real_hysteresis_training_eligible"] == "False"
        for row in raw_row_list
    ), "No current raw trajectory may authorize real-data hysteresis training"

    formulation_id_set = {
        row["formulation_id"] for row in formulation_row_list
    }
    assert formulation_id_set == {
        "PINN-Y1",
        "PINN-Y2",
        "PINN-Y3",
        "PINN-Y4",
        "PINN-Y5",
        "PINN-Y6",
    }, f"Unexpected Phase 4 formulation IDs | {formulation_id_set}"
    assert all(
        row["real_data_training_authorized"] == "False"
        for row in formulation_row_list
    ), "No Phase 4 formulation may be real-data trainable"

    chronology = summary["chronology_evidence"]
    assert chronology["ordered_direction_window_count"] == len(raw_row_list)
    assert chronology["single_reversal_pair_count"] > 0
    assert chronology["repeated_reversal_cycle_count"] == 0
    assert chronology["repeated_major_loop_count"] == 0
    assert chronology["minor_loop_marker_count"] == 0
    assert chronology["deterministic_reset_marker_count"] == 0

    exit_gate = summary["exit_gate"]
    assert exit_gate["status"] == "failed_no_training_authorized"
    assert exit_gate["real_data_training_authorized"] is False
    assert exit_gate["phase4_physical_residual_promoted"] is False
    assert exit_gate["advance_to_phase5"] is True
    assert exit_gate["check_map"]["all_canonical_raw_files_scanned"] is True
    assert exit_gate["check_map"]["ordered_acquisition_available"] is True
    assert exit_gate["check_map"]["repeated_reversal_cycles_available"] is False

    print(
        "PHASE4_HYSTERESIS_FEASIBILITY_VALIDATION_OK "
        f"raw_rows={len(raw_row_list)} "
        f"formulations={len(formulation_row_list)} "
        "training_authorized=false"
    )


if __name__ == "__main__":
    main()
