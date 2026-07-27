"""Validate Wave 5.2R Stage 3 analytical-anchor evidence."""

from __future__ import annotations

# Import Python Utilities
import csv
import json
import os
from pathlib import Path
from typing import Any

# Define Project Paths
PROJECT_PATH = Path(os.path.abspath(__file__)).parents[4]
OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage3_analytical_anchor_reproduction_and_stress_tests"
)
REPORT_ASSET_DIRECTORY = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "model_development_waves"
    / "wave_5_2"
    / "physics_guided_pinn_reassessment"
    / "[2026-07-27]"
    / "stage3_analytical_anchor_reproduction_and_stress_tests"
    / "assets"
)

EXIT_GATE_PATH = OUTPUT_DIRECTORY / "stage3_exit_gate_summary.json"
REPRODUCTION_PATH = OUTPUT_DIRECTORY / "stage3_reproduction_comparison.csv"
VARIANT_PATH = OUTPUT_DIRECTORY / "stage3_forward_variant_comparison.csv"
BOOTSTRAP_PATH = OUTPUT_DIRECTORY / "stage3_bootstrap_repeat_diagnostics.csv"
HOLDOUT_PATH = OUTPUT_DIRECTORY / "stage3_train_only_holdout_diagnostics.csv"
CORRUPTION_PATH = OUTPUT_DIRECTORY / "stage3_anchor_corruption_diagnostics.csv"
ENVELOPE_PATH = OUTPUT_DIRECTORY / "stage3_validity_envelope_conditions.csv"

EXPECTED_SPLIT_SIGNATURE = (
    "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16"
)
EXPECTED_GATE_COUNT = 12
EXPECTED_VARIANT_COUNT = 6
EXPECTED_BOOTSTRAP_COUNT = 64
EXPECTED_HOLDOUT_COUNT = 17
EXPECTED_CORRUPTION_COUNT = 38
EXPECTED_FORWARD_CURVE_COUNT = 966
EXPECTED_PLOT_NAME_LIST = [
    "stage3_variant_comparison.png",
    "stage3_stability_holdouts.png",
    "stage3_corruption_sensitivity.png",
]


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    """Read a CSV artifact into a list of dictionaries.

    Args:
        path: CSV artifact path.

    Returns:
        Parsed CSV rows.
    """

    assert path.is_file(), f"Missing Stage 3 artifact: {path}"
    with path.open("r", encoding="utf-8", newline="") as input_file:
        return list(csv.DictReader(input_file))


def load_exit_gate_summary() -> dict[str, Any]:
    """Load and validate the top-level exit-gate artifact."""

    assert EXIT_GATE_PATH.is_file(), f"Missing exit-gate summary: {EXIT_GATE_PATH}"
    payload = json.loads(EXIT_GATE_PATH.read_text(encoding="utf-8"))
    assert payload["status"] == "pass"
    assert payload["training_executed"] is False
    assert payload["split_signature"] == EXPECTED_SPLIT_SIGNATURE
    assert payload["canonical_anchor"] == "PF_A_LOCAL_QUADRATIC"
    assert payload["canonical_anchor_status"] == "qualified_analytical_component"
    assert payload["gate_count"] == EXPECTED_GATE_COUNT
    assert payload["gate_pass_count"] == EXPECTED_GATE_COUNT
    assert all(payload["gate_dictionary"].values())
    return payload


def main() -> int:
    """Validate all Stage 3 machine-readable and visual evidence."""

    exit_gate_summary = load_exit_gate_summary()

    # Validate Exact Phase 1 Reproduction
    reproduction_row_list = read_csv_rows(REPRODUCTION_PATH)
    assert reproduction_row_list
    assert all(row["status"] == "pass" for row in reproduction_row_list)
    assert all(float(row["absolute_difference"]) <= float(row["tolerance"]) for row in reproduction_row_list)

    # Validate Required Experimental Rosters
    variant_row_list = read_csv_rows(VARIANT_PATH)
    bootstrap_row_list = read_csv_rows(BOOTSTRAP_PATH)
    holdout_row_list = read_csv_rows(HOLDOUT_PATH)
    corruption_row_list = read_csv_rows(CORRUPTION_PATH)
    envelope_row_list = read_csv_rows(ENVELOPE_PATH)
    assert len(variant_row_list) == EXPECTED_VARIANT_COUNT
    assert len(bootstrap_row_list) == EXPECTED_BOOTSTRAP_COUNT
    assert len(holdout_row_list) == EXPECTED_HOLDOUT_COUNT
    assert len(corruption_row_list) == EXPECTED_CORRUPTION_COUNT
    assert len(envelope_row_list) == EXPECTED_FORWARD_CURVE_COUNT
    assert {row["deployment_status"] for row in variant_row_list} == {
        "qualified_anchor",
        "comparator_only",
    }
    assert all(row["finite"] == "True" for row in bootstrap_row_list)
    assert all(row["finite"] == "True" for row in holdout_row_list)
    assert all(row["finite"] == "True" for row in corruption_row_list)
    assert all(row["prediction_finite"] == "True" for row in envelope_row_list)

    # Validate Report Visual Assets
    for plot_name in EXPECTED_PLOT_NAME_LIST:
        plot_path = REPORT_ASSET_DIRECTORY / plot_name
        assert plot_path.is_file(), f"Missing Stage 3 plot: {plot_path}"
        assert plot_path.stat().st_size > 10_000, (
            f"Stage 3 plot is unexpectedly small: {plot_path}"
        )

    assert exit_gate_summary["validity_envelope"]["finite_prediction_count"] == (
        EXPECTED_FORWARD_CURVE_COUNT
    )
    print(
        "WAVE52R_STAGE3_VALIDATION_OK "
        f"gates={EXPECTED_GATE_COUNT} "
        f"variants={EXPECTED_VARIANT_COUNT} "
        f"bootstraps={EXPECTED_BOOTSTRAP_COUNT} "
        f"holdouts={EXPECTED_HOLDOUT_COUNT} "
        f"corruptions={EXPECTED_CORRUPTION_COUNT} "
        f"forward_curves={EXPECTED_FORWARD_CURVE_COUNT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
