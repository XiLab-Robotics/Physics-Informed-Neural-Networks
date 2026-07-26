"""Validate the Wave 5.2 Phase 6 dynamic observability artifacts."""

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
    / "pinn_program_dynamics"
    / "phase6_dynamic_observability_audit.yaml"
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIGURATION_PATH,
        help="Phase 6 audit YAML configuration.",
    )
    return parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:
    """Resolve a repository-relative path."""

    path = Path(path_value)
    return path if path.is_absolute() else PROJECT_ROOT / path


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    """Load a YAML mapping."""

    with path.open("r", encoding="utf-8") as stream:
        payload = yaml.safe_load(stream)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected YAML mapping: {path}")
    return payload


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    """Load a CSV artifact."""

    with path.open("r", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> None:
    """Validate Phase 6 artifact and decision consistency."""

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
    expected_count = int(expected["canonical_condition_count"])
    assert len(condition_rows) == expected_count
    assert int(summary["condition_count"]) == expected_count
    assert len(split_rows) == 3
    assert {
        row["split"]: int(row["condition_count"]) for row in split_rows
    } == {
        key: int(value)
        for key, value in expected["condition_count_by_split"].items()
    }
    assert all(
        row["direction_window_order"] == "Fw_then_Bw"
        for row in condition_rows
    )
    assert all(
        row["finite_value_pass"].lower() == "true"
        for row in condition_rows
    )
    assert all(
        row["validated_transient_te_target_available"].lower() == "false"
        for row in condition_rows
    )
    assert all(
        row["load_inertia_available"].lower() == "false"
        for row in condition_rows
    )

    numeric_field_list = [
        "raw_speed_outlier_fraction",
        "forward_valid_speed_mad_rpm",
        "backward_valid_speed_mad_rpm",
        "valid_causal_101_acceleration_p95_rpm_per_s",
        "transition_causal_101_acceleration_p95_rpm_per_s",
        "causal_101_valid_to_transition_p95_ratio",
    ]
    for row in condition_rows:
        for field_name in numeric_field_list:
            float(row[field_name])

    assert len(formulation_rows) == 5
    assert {
        row["formulation_id"]: row["feasibility_class"]
        for row in formulation_rows
    } == {
        "PINN-D1": "offline_oracle_only",
        "PINN-D2": "blocked_by_data_contract",
        "PINN-D3": "offline_oracle_only",
        "PINN-D4": "real_data_trainable",
        "PINN-D5": "blocked_by_data_contract",
    }
    assert all(
        row["full_pinn_eligible"].lower() == "false"
        for row in formulation_rows
    )

    observability = summary["observability"]
    assert bool(observability["causal_acceleration_reconstructable"])
    assert bool(observability["causal_filter_policy_required"])
    assert not bool(observability["validated_transient_te_target_available"])
    assert not bool(observability["load_inertia_available"])
    assert not bool(observability["commanded_drive_law_available"])
    assert bool(observability["single_reversal_transition_available"])

    exit_gate = summary["exit_gate"]
    assert exit_gate["status"] == "failed_no_training_authorized"
    assert not bool(exit_gate["full_pinn_training_authorized"])
    assert not bool(exit_gate["physical_residual_promoted"])
    assert bool(exit_gate["empirical_temporal_comparator_retained"])
    assert not bool(exit_gate["campaign_preparation_required"])
    assert bool(exit_gate["advance_to_phase7"])
    assert output_path_map["report_markdown"].is_file()

    print(
        "PHASE6_DYNAMIC_OBSERVABILITY_VALIDATION_OK "
        f"conditions={len(condition_rows)} "
        f"formulations={len(formulation_rows)} "
        "training_authorized=false"
    )


if __name__ == "__main__":
    main()
