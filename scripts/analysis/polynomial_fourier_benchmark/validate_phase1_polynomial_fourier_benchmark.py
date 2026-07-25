"""Validate the Wave 5.2 Phase 1 Polynomial-Fourier evidence package."""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path
from typing import Any

import yaml

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(
            "config/analysis/polynomial_fourier_benchmark/"
            "phase1_benchmark.yaml"
        ),
    )
    return parser.parse_args()


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as source_file:
        payload = yaml.safe_load(source_file)
    assert isinstance(payload, dict), f"Expected YAML mapping | {path}"
    return payload


def csv_row_count(path: Path) -> int:
    """Count CSV data rows."""

    with path.open("r", encoding="utf-8-sig", newline="") as source_file:
        return sum(1 for _ in csv.DictReader(source_file))


def assert_csv_numeric_values_are_finite(
    path: Path,
    ignored_column_name_set: set[str],
) -> None:
    """Require every non-identifier CSV value to parse as finite."""

    with path.open("r", encoding="utf-8-sig", newline="") as source_file:
        for row_index, row in enumerate(csv.DictReader(source_file), start=2):
            for column_name, value_text in row.items():
                if column_name in ignored_column_name_set:
                    continue
                try:
                    numeric_value = float(value_text)
                except ValueError:
                    continue
                assert math.isfinite(numeric_value), (
                    f"Non-finite CSV value | {path} | row {row_index} | "
                    f"{column_name}"
                )


def main() -> None:
    """Validate Phase 1 contracts and cardinalities."""

    arguments = parse_arguments()
    configuration_path = (
        arguments.config
        if arguments.config.is_absolute()
        else REPOSITORY_ROOT / arguments.config
    )
    configuration = load_yaml(configuration_path)
    output_map = configuration["outputs"]
    output_path_map = {
        key: REPOSITORY_ROOT / value for key, value in output_map.items()
    }
    for output_name, output_path in output_path_map.items():
        assert output_path.exists(), f"Missing output | {output_name} | {output_path}"

    summary = load_yaml(output_path_map["benchmark_yaml"])
    assert summary["status"] == "complete"
    assert summary["training_executed"] is False
    assert summary["coverage"]["eligible_condition_count"] == 966
    assert summary["coverage"]["directional_curve_count"] == 1932
    assert summary["coverage"]["curve_count_by_split"] == {
        "train": 1350,
        "validation": 388,
        "test": 194,
    }
    assert summary["deterministic_tests"]["status"] == "pass"
    assert summary["selection"]["full_pinn_claim"] is False
    assert summary["selection"]["analytical_reference_model_id"] in {
        "PF_A_LOCAL_QUADRATIC",
        "PF_A_PAPER_QUADRATIC",
        "PF_C_PLC_ORDER10",
        "PF_E_REDUCED_QUADRATIC",
    }
    assert summary["selection"]["alternative_comparator_model_id"] in {
        "PF_C_PLC_ORDER10",
        "PF_E_REDUCED_QUADRATIC",
    }
    assert csv_row_count(output_path_map["per_curve_metrics_csv"]) == 1932 * 6
    assert csv_row_count(output_path_map["aggregate_metrics_csv"]) == 36
    assert csv_row_count(output_path_map["preprocessing_audit_csv"]) == 194
    assert csv_row_count(output_path_map["onnx_example_metrics_csv"]) == 5
    assert_csv_numeric_values_are_finite(
        output_path_map["per_curve_metrics_csv"],
        {"condition_id", "split", "direction", "model_id", "validity_scope"},
    )
    assert_csv_numeric_values_are_finite(
        output_path_map["onnx_example_metrics_csv"],
        {"example_file"},
    )
    assert len(summary["plot_path_list"]) == 4
    for plot_path_text in summary["plot_path_list"]:
        assert (REPOSITORY_ROOT / plot_path_text).is_file()

    coefficient_payload = load_yaml(output_path_map["coefficient_models_yaml"])
    assert set(coefficient_payload["surface_map"]) == {
        "PF_A_LOCAL_QUADRATIC",
        "PF_A_PAPER_QUADRATIC",
        "PF_E_REDUCED_QUADRATIC",
    }
    plc_parity = load_yaml(output_path_map["plc_parity_yaml"])
    assert plc_parity["status"] == "pass"
    assert plc_parity["basis_term_count"] == 35
    assert plc_parity["active_polynomial_degree"] == 10
    assert len(plc_parity["harmonic_order_list"]) == 9
    print(
        "Phase 1 validation passed | reference="
        f"{summary['selection']['analytical_reference_model_id']} | "
        "alternative="
        f"{summary['selection']['alternative_comparator_model_id']}"
    )


if __name__ == "__main__":
    main()
