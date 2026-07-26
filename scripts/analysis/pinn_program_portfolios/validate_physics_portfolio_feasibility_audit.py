"""Validate a configuration-driven Wave 5.2 portfolio audit."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        required=True,
        help="Phase-specific portfolio YAML configuration.",
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
    """Validate a phase-specific portfolio audit."""

    arguments = parse_arguments()
    configuration = load_yaml_mapping(resolve_project_path(arguments.config))
    output_path_map = {
        key: resolve_project_path(value)
        for key, value in configuration["outputs"].items()
    }
    summary = load_yaml_mapping(output_path_map["audit_yaml"])
    evidence_rows = load_csv_rows(output_path_map["evidence_csv"])
    quantity_rows = load_csv_rows(output_path_map["quantity_csv"])
    formulation_rows = load_csv_rows(output_path_map["formulation_csv"])

    assert int(summary["phase_number"]) == int(
        configuration["metadata"]["phase_number"]
    )
    assert len(evidence_rows) == len(configuration["evidence_files"])
    assert len(quantity_rows) == len(configuration["required_quantities"])
    assert len(formulation_rows) == len(
        configuration["candidate_formulations"]
    )
    assert all(
        row["exists"].lower() == "true"
        for row in evidence_rows
        if row["required"].lower() == "true"
    )
    assert bool(summary["all_required_evidence_files_exist"])
    assert not bool(summary["full_pinn_training_authorized"])
    assert all(
        row["full_pinn_eligible"].lower() == "false"
        for row in formulation_rows
    )
    decision = summary["decision"]
    assert decision["status"] == "failed_no_training_authorized"
    assert not bool(decision["physical_residual_promoted"])
    assert not bool(decision["campaign_preparation_required"])
    assert bool(decision["advance_to_next_phase"])
    assert output_path_map["report_markdown"].is_file()

    print(
        "PHYSICS_PORTFOLIO_FEASIBILITY_VALIDATION_OK "
        f"phase={summary['phase_number']} "
        f"evidence={len(evidence_rows)} "
        f"quantities={len(quantity_rows)} "
        f"formulations={len(formulation_rows)} "
        "training_authorized=false"
    )


if __name__ == "__main__":
    main()
