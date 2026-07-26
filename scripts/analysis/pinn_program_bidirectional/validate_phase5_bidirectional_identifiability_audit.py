"""Validate the Wave 5.2 Phase 5 bidirectional audit artifacts."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONFIGURATION_PATH = (
    PROJECT_ROOT
    / "config"
    / "analysis"
    / "pinn_program_bidirectional"
    / "phase5_bidirectional_identifiability_audit.yaml"
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIGURATION_PATH,
        help="Phase 5 audit YAML configuration.",
    )
    return parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:
    """Resolve a repository-relative path."""

    path = Path(path_value)
    return path if path.is_absolute() else PROJECT_ROOT / path


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as stream:
        payload = yaml.safe_load(stream)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected YAML mapping: {path}")
    return payload


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    """Load one CSV artifact."""

    with path.open("r", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> None:
    """Validate Phase 5 artifacts and decision consistency."""

    arguments = parse_arguments()
    configuration = load_yaml_mapping(resolve_project_path(arguments.config))
    output_path_map = {
        key: resolve_project_path(value)
        for key, value in configuration["outputs"].items()
    }
    summary = load_yaml_mapping(output_path_map["audit_yaml"])
    condition_rows = load_csv_rows(output_path_map["condition_audit_csv"])
    split_rows = load_csv_rows(output_path_map["split_summary_csv"])
    formulation_rows = load_csv_rows(
        output_path_map["formulation_feasibility_csv"]
    )

    expected = configuration["expected"]
    expected_pair_count = int(expected["paired_condition_count"])
    assert len(condition_rows) == expected_pair_count
    assert int(summary["paired_condition_count"]) == expected_pair_count
    assert bool(summary["finite_value_pass"])
    assert len(split_rows) == 3
    assert {
        row["split"]: int(row["condition_count"]) for row in split_rows
    } == {
        key: int(value)
        for key, value in expected["condition_count_by_split"].items()
    }
    assert all(
        row["offline_gap_proxy_only"].lower() == "true"
        for row in condition_rows
    )

    numeric_field_list = [
        "absolute_mean_gap_arcmin",
        "raw_pair_rmse_deg",
        "centered_pair_rmse_deg",
        "centered_pair_correlation",
        "target_derived_best_shift_deg",
    ]
    for row in condition_rows:
        for field_name in numeric_field_list:
            float(row[field_name])

    assert len(formulation_rows) == 5
    assert {row["formulation_id"] for row in formulation_rows} == {
        "PINN-B1",
        "PINN-B2",
        "PINN-B3",
        "PINN-B4",
        "PINN-B5",
    }
    assert {
        row["formulation_id"]: row["feasibility_class"]
        for row in formulation_rows
    } == {
        "PINN-B1": "real_data_trainable",
        "PINN-B2": "blocked_by_data_contract",
        "PINN-B3": "offline_oracle_only",
        "PINN-B4": "synthetic_oracle_only",
        "PINN-B5": "offline_oracle_only",
    }
    assert all(
        row["full_pinn_eligible"].lower() == "false"
        for row in formulation_rows
    )

    observability = summary["observability"]
    assert bool(observability["direction_flag_causal"])
    assert not bool(
        observability[
            "independent_global_lost_motion_measurement_available"
        ]
    )
    assert not bool(observability["component_error_metrology_available"])
    assert not bool(observability["contact_clearance_available"])
    assert not bool(
        observability["repeated_transition_state_contract_available"]
    )

    exit_gate = summary["exit_gate"]
    assert exit_gate["status"] == "failed_no_training_authorized"
    assert not bool(exit_gate["full_pinn_training_authorized"])
    assert not bool(exit_gate["physical_residual_promoted"])
    assert bool(exit_gate["empirical_bidirectional_comparator_retained"])
    assert not bool(exit_gate["campaign_preparation_required"])
    assert bool(exit_gate["advance_to_phase6"])
    assert output_path_map["report_markdown"].is_file()

    print(
        "PHASE5_BIDIRECTIONAL_IDENTIFIABILITY_VALIDATION_OK "
        f"conditions={len(condition_rows)} "
        f"formulations={len(formulation_rows)} "
        "training_authorized=false"
    )


if __name__ == "__main__":
    main()
