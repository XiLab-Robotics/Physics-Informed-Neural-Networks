"""Build TE Curve Verification Pipeline component-offset identification input tables."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import numpy as np
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.datasets import transmission_error_dataset

DEFAULT_DATASET_CONFIG_PATH = PROJECT_PATH / "config" / "datasets" / "transmission_error_dataset.yaml"
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_component_offset_identification"
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "component_offset_identification"
)

REPORT_FILENAME = "track2_component_offset_identification_inputs.md"
SUMMARY_FILENAME = "track2_component_offset_identification_inputs_summary.yaml"
PER_CURVE_COMPONENT_FILENAME = "track2_component_offset_per_curve_components.csv"
CONDITION_SUMMARY_FILENAME = "track2_component_offset_condition_summary.csv"

DEFAULT_HARMONIC_ORDER_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]


@dataclass(frozen=True)
class PerCurveComponentRow:

    """One measured curve component diagnostic row."""

    source_file_path: str
    direction_label: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    sample_count: int
    curve_mean_deg: float
    curve_peak_to_peak_deg: float
    harmonic_order: int
    cosine_coefficient_deg: float
    sine_coefficient_deg: float
    amplitude_deg: float
    phase_deg: float

    def to_csv_row(self) -> dict[str, Any]:

        """Return a stable CSV row."""

        return {
            "source_file_path": self.source_file_path,
            "direction_label": self.direction_label,
            "speed_rpm": format_float(self.speed_rpm),
            "torque_nm": format_float(self.torque_nm),
            "oil_temperature_deg": format_float(self.oil_temperature_deg),
            "sample_count": self.sample_count,
            "curve_mean_deg": format_float(self.curve_mean_deg),
            "curve_peak_to_peak_deg": format_float(self.curve_peak_to_peak_deg),
            "harmonic_order": self.harmonic_order,
            "cosine_coefficient_deg": format_float(self.cosine_coefficient_deg),
            "sine_coefficient_deg": format_float(self.sine_coefficient_deg),
            "amplitude_deg": format_float(self.amplitude_deg),
            "phase_deg": format_float(self.phase_deg),
        }


@dataclass(frozen=True)
class ConditionSummaryRow:

    """Aggregate measured component diagnostics for one condition."""

    direction_label: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    harmonic_order: int
    curve_count: int
    mean_curve_mean_deg: float
    std_curve_mean_deg: float
    mean_component_amplitude_deg: float
    std_component_amplitude_deg: float

    def to_csv_row(self) -> dict[str, Any]:

        """Return a stable CSV row."""

        return {
            "direction_label": self.direction_label,
            "speed_rpm": format_float(self.speed_rpm),
            "torque_nm": format_float(self.torque_nm),
            "oil_temperature_deg": format_float(self.oil_temperature_deg),
            "harmonic_order": self.harmonic_order,
            "curve_count": self.curve_count,
            "mean_curve_mean_deg": format_float(self.mean_curve_mean_deg),
            "std_curve_mean_deg": format_float(self.std_curve_mean_deg),
            "mean_component_amplitude_deg": format_float(self.mean_component_amplitude_deg),
            "std_component_amplitude_deg": format_float(self.std_component_amplitude_deg),
        }


def parse_arguments() -> argparse.Namespace:

    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset-config-path", type=Path, default=DEFAULT_DATASET_CONFIG_PATH)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--report-topic-root", type=Path, default=DEFAULT_REPORT_TOPIC_ROOT)
    parser.add_argument("--run-id", type=str, default="")
    parser.add_argument("--max-files", type=int, default=0)
    parser.add_argument(
        "--harmonic-orders",
        type=str,
        default=",".join(str(harmonic_order) for harmonic_order in DEFAULT_HARMONIC_ORDER_LIST),
    )
    parser.add_argument("--skip-report", action="store_true")
    return parser.parse_args()


def format_float(value: float) -> str:

    """Format a float for stable CSV output."""

    if not math.isfinite(float(value)):
        return "nan"
    return f"{float(value):.9f}"


def parse_harmonic_order_list(raw_value: str) -> list[int]:

    """Parse a comma-separated harmonic order list."""

    harmonic_order_list = [int(token.strip()) for token in raw_value.split(",") if token.strip()]
    assert len(harmonic_order_list) > 0, "At least one harmonic order is required"
    assert all(harmonic_order >= 0 for harmonic_order in harmonic_order_list), "Harmonic orders must be non-negative"
    return sorted(set(harmonic_order_list))


def compute_harmonic_coefficients(
    angular_position_deg: np.ndarray,
    transmission_error_deg: np.ndarray,
    harmonic_order: int,
) -> tuple[float, float, float, float]:

    """Compute measured cosine/sine coefficients for one harmonic."""

    # Convert To Double Precision Arrays
    angular_position_rad = np.deg2rad(np.asarray(angular_position_deg, dtype=np.float64))
    transmission_error_array = np.asarray(transmission_error_deg, dtype=np.float64)

    # Harmonic Zero Is The Curve Mean / DC Component
    if harmonic_order == 0:
        curve_mean = float(np.mean(transmission_error_array))
        return curve_mean, 0.0, abs(curve_mean), 0.0

    # Estimate Fourier-Like Coefficients On The Measured Rotation Samples
    cosine_basis = np.cos(float(harmonic_order) * angular_position_rad)
    sine_basis = np.sin(float(harmonic_order) * angular_position_rad)
    cosine_coefficient = float(2.0 * np.mean(transmission_error_array * cosine_basis))
    sine_coefficient = float(2.0 * np.mean(transmission_error_array * sine_basis))
    amplitude = float(math.hypot(cosine_coefficient, sine_coefficient))
    phase = float(math.degrees(math.atan2(-sine_coefficient, cosine_coefficient)))

    return cosine_coefficient, sine_coefficient, amplitude, phase


def build_per_curve_component_rows(
    dataset_config_path: Path,
    harmonic_order_list: list[int],
    max_files: int,
) -> list[PerCurveComponentRow]:

    """Build measured component rows for all selected dataset curves."""

    # Resolve Dataset Root From The Canonical Config
    dataset_root = transmission_error_dataset.resolve_dataset_root_from_config(dataset_config_path)
    csv_file_path_list = transmission_error_dataset.collect_dataset_csv_paths(dataset_root)

    # Apply Optional Smoke-Test Limit
    if max_files > 0:
        csv_file_path_list = csv_file_path_list[:max_files]

    # Build Per-Curve Component Diagnostics
    per_curve_component_row_list: list[PerCurveComponentRow] = []

    for csv_file_path in csv_file_path_list:
        directional_sample_list = transmission_error_dataset.build_validated_directional_samples(csv_file_path)

        for directional_sample in directional_sample_list:
            curve_mean = float(np.mean(directional_sample.transmission_error_deg))
            curve_peak_to_peak = float(np.max(directional_sample.transmission_error_deg) - np.min(directional_sample.transmission_error_deg))
            relative_source_path = directional_sample.source_file_path.relative_to(PROJECT_PATH).as_posix()

            for harmonic_order in harmonic_order_list:
                cosine_coefficient, sine_coefficient, amplitude, phase = compute_harmonic_coefficients(
                    directional_sample.angular_position_deg,
                    directional_sample.transmission_error_deg,
                    harmonic_order,
                )
                per_curve_component_row_list.append(
                    PerCurveComponentRow(
                        source_file_path=relative_source_path,
                        direction_label=directional_sample.direction_label,
                        speed_rpm=directional_sample.speed_rpm,
                        torque_nm=directional_sample.torque_nm,
                        oil_temperature_deg=directional_sample.oil_temperature_deg,
                        sample_count=int(directional_sample.transmission_error_deg.size),
                        curve_mean_deg=curve_mean,
                        curve_peak_to_peak_deg=curve_peak_to_peak,
                        harmonic_order=harmonic_order,
                        cosine_coefficient_deg=cosine_coefficient,
                        sine_coefficient_deg=sine_coefficient,
                        amplitude_deg=amplitude,
                        phase_deg=phase,
                    )
                )

    return per_curve_component_row_list


def build_condition_summary_rows(per_curve_component_row_list: list[PerCurveComponentRow]) -> list[ConditionSummaryRow]:

    """Aggregate measured component rows by operating condition."""

    grouped_row_dictionary: dict[tuple[str, float, float, float, int], list[PerCurveComponentRow]] = {}

    for row in per_curve_component_row_list:
        group_key = (
            row.direction_label,
            row.speed_rpm,
            row.torque_nm,
            row.oil_temperature_deg,
            row.harmonic_order,
        )
        grouped_row_dictionary.setdefault(group_key, []).append(row)

    condition_summary_row_list: list[ConditionSummaryRow] = []

    for group_key, group_row_list in sorted(grouped_row_dictionary.items()):
        direction_label, speed_rpm, torque_nm, oil_temperature_deg, harmonic_order = group_key
        curve_mean_array = np.asarray([row.curve_mean_deg for row in group_row_list], dtype=np.float64)
        amplitude_array = np.asarray([row.amplitude_deg for row in group_row_list], dtype=np.float64)
        condition_summary_row_list.append(
            ConditionSummaryRow(
                direction_label=direction_label,
                speed_rpm=speed_rpm,
                torque_nm=torque_nm,
                oil_temperature_deg=oil_temperature_deg,
                harmonic_order=harmonic_order,
                curve_count=len(group_row_list),
                mean_curve_mean_deg=float(np.mean(curve_mean_array)),
                std_curve_mean_deg=float(np.std(curve_mean_array)),
                mean_component_amplitude_deg=float(np.mean(amplitude_array)),
                std_component_amplitude_deg=float(np.std(amplitude_array)),
            )
        )

    return condition_summary_row_list


def write_csv(output_path: Path, row_list: list[Any]) -> None:

    """Write dataclass rows to CSV."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    assert len(row_list) > 0, f"No rows available for CSV output | {output_path}"

    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(row_list[0].to_csv_row().keys()), lineterminator="\n")
        writer.writeheader()
        for row in row_list:
            writer.writerow(row.to_csv_row())


def write_summary_yaml(
    output_path: Path,
    run_id: str,
    per_curve_component_row_list: list[PerCurveComponentRow],
    condition_summary_row_list: list[ConditionSummaryRow],
    harmonic_order_list: list[int],
) -> None:

    """Write machine-readable summary YAML."""

    direction_list = sorted({row.direction_label for row in per_curve_component_row_list})
    source_file_count = len({row.source_file_path for row in per_curve_component_row_list})
    curve_count = len({(row.source_file_path, row.direction_label) for row in per_curve_component_row_list})

    summary_dictionary = {
        "run_id": run_id,
        "source_file_count": source_file_count,
        "direction_list": direction_list,
        "curve_count": curve_count,
        "harmonic_order_list": harmonic_order_list,
        "per_curve_component_row_count": len(per_curve_component_row_list),
        "condition_summary_row_count": len(condition_summary_row_list),
        "per_curve_component_table": PER_CURVE_COMPONENT_FILENAME,
        "condition_summary_table": CONDITION_SUMMARY_FILENAME,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(summary_dictionary, output_file, sort_keys=False)


def write_markdown_report(
    report_path: Path,
    output_directory: Path,
    run_id: str,
    per_curve_component_row_list: list[PerCurveComponentRow],
    condition_summary_row_list: list[ConditionSummaryRow],
    harmonic_order_list: list[int],
) -> None:

    """Write a lightweight Markdown report for the prepared input tables."""

    source_file_count = len({row.source_file_path for row in per_curve_component_row_list})
    curve_count = len({(row.source_file_path, row.direction_label) for row in per_curve_component_row_list})
    direction_list = ", ".join(f"`{direction}`" for direction in sorted({row.direction_label for row in per_curve_component_row_list}))
    harmonic_order_text = ", ".join(f"`{harmonic_order}`" for harmonic_order in harmonic_order_list)

    report_lines = [
        "# TE Curve Verification Pipeline Component Offset Identification Inputs",
        "",
        "## Overview",
        "",
        "This report prepares measured component-offset input tables for the",
        "`TE Curve Verification Pipeline` component-offset identification branch. It does not train",
        "models, alter registries, or assert that `a_0` / `Component 0` is the",
        "confirmed cause of the observed curve-offset symptom.",
        "",
        f"- Run Instance: `{run_id}`",
        f"- Output Directory: `{output_directory.relative_to(PROJECT_PATH).as_posix()}`",
        f"- Source CSV Files: `{source_file_count}`",
        f"- Directional Curves: `{curve_count}`",
        f"- Directions: {direction_list}",
        f"- Harmonic Orders: {harmonic_order_text}",
        "",
        "## Output Tables",
        "",
        "| Artifact | Purpose |",
        "| --- | --- |",
        f"| `{PER_CURVE_COMPONENT_FILENAME}` | Per-curve measured mean / `a_0` proxy and selected harmonic coefficients. |",
        f"| `{CONDITION_SUMMARY_FILENAME}` | Condition-level aggregates by direction, speed, torque, oil temperature, and harmonic order. |",
        f"| `{SUMMARY_FILENAME}` | Machine-readable run summary. |",
        "",
        "## Next Use",
        "",
        "Use these tables to plot experimental `a_0` and curve-mean surfaces over",
        "speed and torque, split by oil temperature and direction. The follow-up",
        "diagnostic should compare high-offset cases against multiple harmonic",
        "orders before deciding whether the issue is `a_0`-dominant,",
        "multi-component, condition/regime-driven, or repeatability-limited.",
        "",
        "## Table Counts",
        "",
        f"- Per-curve component rows: `{len(per_curve_component_row_list)}`",
        f"- Condition summary rows: `{len(condition_summary_row_list)}`",
        "",
    ]

    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="\n") as report_file:
        report_file.write("\n".join(report_lines).rstrip() + "\n")


def main() -> None:

    """Run the component-offset input preparation."""

    # Parse Inputs
    argument_namespace = parse_arguments()
    harmonic_order_list = parse_harmonic_order_list(argument_namespace.harmonic_orders)
    run_id = argument_namespace.run_id.strip() or datetime.now().strftime("%Y-%m-%d-%H-%M-%S__track2_component_offset_identification_inputs")

    # Build Output Paths
    output_directory = argument_namespace.output_root / run_id
    report_date = run_id.split("__", maxsplit=1)[0][:10]
    report_directory = argument_namespace.report_topic_root / f"[{report_date}]"

    # Build Diagnostics
    per_curve_component_row_list = build_per_curve_component_rows(
        dataset_config_path=argument_namespace.dataset_config_path,
        harmonic_order_list=harmonic_order_list,
        max_files=argument_namespace.max_files,
    )
    condition_summary_row_list = build_condition_summary_rows(per_curve_component_row_list)

    # Write Artifacts
    write_csv(output_directory / PER_CURVE_COMPONENT_FILENAME, per_curve_component_row_list)
    write_csv(output_directory / CONDITION_SUMMARY_FILENAME, condition_summary_row_list)
    write_summary_yaml(
        output_path=output_directory / SUMMARY_FILENAME,
        run_id=run_id,
        per_curve_component_row_list=per_curve_component_row_list,
        condition_summary_row_list=condition_summary_row_list,
        harmonic_order_list=harmonic_order_list,
    )

    if not argument_namespace.skip_report:
        write_markdown_report(
            report_path=report_directory / REPORT_FILENAME,
            output_directory=output_directory,
            run_id=run_id,
            per_curve_component_row_list=per_curve_component_row_list,
            condition_summary_row_list=condition_summary_row_list,
            harmonic_order_list=harmonic_order_list,
        )

    print(f"Prepared TE Curve Verification Pipeline component-offset input tables | {output_directory}")
    if not argument_namespace.skip_report:
        print(f"Prepared Markdown report | {report_directory / REPORT_FILENAME}")


if __name__ == "__main__":
    main()
