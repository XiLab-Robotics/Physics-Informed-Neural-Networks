"""Validate the Wave 5.2R H08 backward/global defect diagnostic package."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import matplotlib.image as mpimg
import yaml

# Define Project Paths
PROJECT_PATH = Path(__file__).resolve().parents[3]
DEFAULT_CONFIG_PATH = PROJECT_PATH / "config" / "analysis" / "wave52r_h08_backward_global_defect_analysis.yaml"

REQUIRED_OUTPUT_FILENAME_LIST = [
    "diagnostic_summary.yaml",
    "candidate_direction_summary.csv",
    "selected_incumbent_comparison.csv",
    "global_interference_summary.csv",
    "condition_factor_summary.csv",
    "worst_condition_deltas.csv",
    "coefficient_band_summary.csv",
    "coefficient_a0_summary.csv",
    "seed_stability_summary.csv",
    "official_metric_reproduction.csv",
    "artifact_inventory.csv",
]


def parse_arguments() -> argparse.Namespace:

    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    parser.add_argument("--run-directory", type=Path, required=True)
    return parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:

    """Resolve a repository-relative or absolute path."""

    path = Path(path_value)
    return path if path.is_absolute() else PROJECT_PATH / path


def load_yaml(input_path: Path) -> dict[str, Any]:

    """Load one YAML mapping."""

    assert input_path.exists(), f"YAML file not found | {input_path}"
    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML mapping | {input_path}"
    return payload


def count_csv_rows(input_path: Path) -> int:

    """Count data rows in one CSV file."""

    with input_path.open("r", encoding="utf-8", newline="") as input_file:
        return sum(1 for _ in csv.DictReader(input_file))


def main() -> None:

    """Validate the complete H08 diagnostic package."""

    argument_namespace = parse_arguments()
    configuration = load_yaml(argument_namespace.config)
    run_directory = resolve_project_path(argument_namespace.run_directory)
    assert run_directory.exists(), f"Diagnostic run directory not found | {run_directory}"

    # Validate Machine-Readable Package
    for filename in REQUIRED_OUTPUT_FILENAME_LIST:
        output_path = run_directory / filename
        assert output_path.exists() and output_path.stat().st_size > 0, f"Required output missing | {output_path}"
    summary = load_yaml(run_directory / "diagnostic_summary.yaml")
    assert summary["training_executed"] is False
    assert summary["checkpoint_modified"] is False
    assert summary["registry_updated"] is False
    assert summary["h08_run_count"] == 9
    assert summary["official_metric_reproduction_passed"] is True
    assert float(summary["official_metric_max_abs_difference_deg"]) <= float(
        configuration["analysis"]["official_reproduction_tolerance_deg"]
    )
    assert summary["decision"] == "offset_dominant_direction_conditioned_with_global_interference"
    assert len(summary["selected_comparison_list"]) == 3
    assert len(summary["global_interference_list"]) == 2

    # Validate Table Coverage
    assert count_csv_rows(run_directory / "candidate_direction_summary.csv") == 16
    assert count_csv_rows(run_directory / "selected_incumbent_comparison.csv") == 3
    assert count_csv_rows(run_directory / "global_interference_summary.csv") == 2
    assert count_csv_rows(run_directory / "coefficient_a0_summary.csv") == 12
    assert count_csv_rows(run_directory / "seed_stability_summary.csv") == 12
    assert count_csv_rows(run_directory / "official_metric_reproduction.csv") == 9
    assert count_csv_rows(run_directory / "artifact_inventory.csv") == 12

    # Validate Canonical Report And Plots
    report_path = resolve_project_path(summary["report_path"])
    assert report_path.exists() and report_path.stat().st_size > 0, f"Canonical report missing | {report_path}"
    report_text = report_path.read_text(encoding="utf-8")
    for required_text in [
        "offset_dominant_direction_conditioned_with_global_interference",
        "Global Model Interference",
        "Scientific Boundary",
        "Recommended Next Gate",
    ]:
        assert required_text in report_text, f"Required report content missing | {required_text}"

    for relative_plot_path in summary["plot_path_list"]:
        plot_path = resolve_project_path(relative_plot_path)
        assert plot_path.exists() and plot_path.stat().st_size > 10_000, f"Plot missing or too small | {plot_path}"
        image_array = mpimg.imread(plot_path)
        assert image_array.ndim in {2, 3} and min(image_array.shape[:2]) >= 500, (
            f"Plot dimensions are too small | {plot_path} | {image_array.shape}"
        )

    print(f"H08_DIAGNOSTIC_VALID | {run_directory}")
    print(f"H08_DIAGNOSTIC_DECISION | {summary['decision']}")


if __name__ == "__main__":
    main()
