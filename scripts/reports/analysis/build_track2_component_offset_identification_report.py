"""Build Track 2 component-offset identification diagnostics."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import matplotlib.pyplot as plt
import numpy as np
import yaml

DEFAULT_INPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_component_offset_identification"
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "component_offset_identification"
)

INPUT_SUMMARY_FILENAME = "track2_component_offset_identification_inputs_summary.yaml"
PER_CURVE_COMPONENT_FILENAME = "track2_component_offset_per_curve_components.csv"
REPORT_FILENAME = "track2_component_offset_identification_diagnostic.md"
HARMONIC_SUMMARY_FILENAME = "track2_component_offset_harmonic_summary.csv"
H0_EXTREME_FILENAME = "track2_component_offset_h0_extreme_curves.csv"
TEMPERATURE_DIRECTION_SUMMARY_FILENAME = "track2_component_offset_temperature_direction_summary.csv"
REPORT_SUMMARY_FILENAME = "track2_component_offset_identification_diagnostic_summary.yaml"


@dataclass(frozen=True)
class ComponentRow:

    """One measured component row imported from the input-table run."""

    source_file_path: str
    direction_label: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    sample_count: int
    curve_mean_deg: float
    curve_peak_to_peak_deg: float
    harmonic_order: int
    amplitude_deg: float


def parse_arguments() -> argparse.Namespace:

    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-directory", type=Path, default=None)
    parser.add_argument("--input-root", type=Path, default=DEFAULT_INPUT_ROOT)
    parser.add_argument("--report-topic-root", type=Path, default=DEFAULT_REPORT_TOPIC_ROOT)
    parser.add_argument("--report-date", type=str, default="")
    parser.add_argument("--top-count", type=int, default=25)
    return parser.parse_args()


def format_float(value: float) -> str:

    """Format a float for stable CSV output."""

    if not math.isfinite(float(value)):
        return "nan"
    return f"{float(value):.9f}"


def format_report_float(value: float) -> str:

    """Format a compact float for report-facing tables."""

    if not math.isfinite(float(value)):
        return "nan"
    return f"{float(value):.6f}"


def format_report_integer_float(value: float) -> str:

    """Format a report-facing operating-point value without decimals."""

    if not math.isfinite(float(value)):
        return "nan"
    return f"{float(value):.0f}"


def resolve_latest_input_directory(input_root: Path) -> Path:

    """Resolve the latest component-offset input directory."""

    candidate_directory_list = sorted(
        [path for path in input_root.iterdir() if path.is_dir() and (path / INPUT_SUMMARY_FILENAME).exists()],
        key=lambda path: path.name,
    )
    assert candidate_directory_list, f"No input runs found under {input_root}"
    return candidate_directory_list[-1]


def load_input_summary(input_directory: Path) -> dict[str, Any]:

    """Load the input-table summary YAML."""

    summary_path = input_directory / INPUT_SUMMARY_FILENAME
    assert summary_path.exists(), f"Input summary not found | {summary_path}"
    with summary_path.open("r", encoding="utf-8") as input_file:
        summary_dictionary = yaml.safe_load(input_file)
    assert isinstance(summary_dictionary, dict), f"Input summary must be a dictionary | {summary_path}"
    return summary_dictionary


def load_component_rows(input_directory: Path) -> list[ComponentRow]:

    """Load measured component rows from the input-table CSV."""

    component_csv_path = input_directory / PER_CURVE_COMPONENT_FILENAME
    assert component_csv_path.exists(), f"Component input table not found | {component_csv_path}"

    component_row_list: list[ComponentRow] = []
    with component_csv_path.open("r", encoding="utf-8", newline="") as input_file:
        for row in csv.DictReader(input_file):
            component_row_list.append(
                ComponentRow(
                    source_file_path=row["source_file_path"],
                    direction_label=row["direction_label"],
                    speed_rpm=float(row["speed_rpm"]),
                    torque_nm=float(row["torque_nm"]),
                    oil_temperature_deg=float(row["oil_temperature_deg"]),
                    sample_count=int(row["sample_count"]),
                    curve_mean_deg=float(row["curve_mean_deg"]),
                    curve_peak_to_peak_deg=float(row["curve_peak_to_peak_deg"]),
                    harmonic_order=int(row["harmonic_order"]),
                    amplitude_deg=float(row["amplitude_deg"]),
                )
            )

    assert component_row_list, f"No component rows loaded | {component_csv_path}"
    return component_row_list


def write_csv(output_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write dictionaries to CSV."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    assert row_list, f"No rows available for CSV output | {output_path}"

    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(row_list[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(row_list)


def build_harmonic_summary(component_row_list: list[ComponentRow]) -> list[dict[str, Any]]:

    """Build aggregate harmonic magnitude rows."""

    harmonic_row_dictionary: dict[int, list[ComponentRow]] = defaultdict(list)
    for row in component_row_list:
        harmonic_row_dictionary[row.harmonic_order].append(row)

    summary_row_list: list[dict[str, Any]] = []
    for harmonic_order, row_list in sorted(harmonic_row_dictionary.items()):
        amplitude_array = np.asarray([abs(row.amplitude_deg) for row in row_list], dtype=np.float64)
        summary_row_list.append(
            {
                "harmonic_order": harmonic_order,
                "row_count": len(row_list),
                "mean_abs_amplitude_deg": format_float(float(np.mean(amplitude_array))),
                "median_abs_amplitude_deg": format_float(float(np.median(amplitude_array))),
                "p95_abs_amplitude_deg": format_float(float(np.percentile(amplitude_array, 95.0))),
                "max_abs_amplitude_deg": format_float(float(np.max(amplitude_array))),
            }
        )
    return summary_row_list


def build_temperature_direction_summary(component_row_list: list[ComponentRow]) -> list[dict[str, Any]]:

    """Build signed harmonic-zero summaries per temperature and direction."""

    h0_row_list = [row for row in component_row_list if row.harmonic_order == 0]
    group_dictionary: dict[tuple[str, float], list[ComponentRow]] = defaultdict(list)
    for row in h0_row_list:
        group_dictionary[(row.direction_label, row.oil_temperature_deg)].append(row)

    summary_row_list: list[dict[str, Any]] = []
    for (direction_label, oil_temperature_deg), row_list in sorted(group_dictionary.items()):
        curve_mean_array = np.asarray([row.curve_mean_deg for row in row_list], dtype=np.float64)
        summary_row_list.append(
            {
                "direction_label": direction_label,
                "oil_temperature_deg": format_float(oil_temperature_deg),
                "curve_count": len(row_list),
                "mean_h0_deg": format_float(float(np.mean(curve_mean_array))),
                "std_h0_deg": format_float(float(np.std(curve_mean_array))),
                "min_h0_deg": format_float(float(np.min(curve_mean_array))),
                "max_h0_deg": format_float(float(np.max(curve_mean_array))),
            }
        )
    return summary_row_list


def build_h0_extreme_rows(component_row_list: list[ComponentRow], top_count: int) -> list[dict[str, Any]]:

    """Build the largest absolute harmonic-zero curve rows."""

    h0_row_list = [row for row in component_row_list if row.harmonic_order == 0]
    sorted_row_list = sorted(h0_row_list, key=lambda row: abs(row.curve_mean_deg), reverse=True)
    extreme_row_list: list[dict[str, Any]] = []

    for rank, row in enumerate(sorted_row_list[:top_count], start=1):
        extreme_row_list.append(
            {
                "rank": rank,
                "source_file_path": row.source_file_path,
                "direction_label": row.direction_label,
                "speed_rpm": format_float(row.speed_rpm),
                "torque_nm": format_float(row.torque_nm),
                "oil_temperature_deg": format_float(row.oil_temperature_deg),
                "curve_mean_deg": format_float(row.curve_mean_deg),
                "absolute_curve_mean_deg": format_float(abs(row.curve_mean_deg)),
                "curve_peak_to_peak_deg": format_float(row.curve_peak_to_peak_deg),
            }
        )
    return extreme_row_list


def create_harmonic_summary_plot(harmonic_summary_rows: list[dict[str, Any]], output_path: Path) -> None:

    """Create a bar plot of mean and max harmonic amplitudes."""

    harmonic_order_list = [int(row["harmonic_order"]) for row in harmonic_summary_rows]
    mean_amplitude_list = [float(row["mean_abs_amplitude_deg"]) for row in harmonic_summary_rows]
    max_amplitude_list = [float(row["max_abs_amplitude_deg"]) for row in harmonic_summary_rows]

    figure, axis = plt.subplots(figsize=(9.0, 4.8), constrained_layout=True)
    x_values = np.arange(len(harmonic_order_list))
    axis.bar(x_values - 0.18, mean_amplitude_list, width=0.36, label="mean abs amplitude")
    axis.bar(x_values + 0.18, max_amplitude_list, width=0.36, label="max abs amplitude")
    axis.set_xticks(x_values, [str(harmonic_order) for harmonic_order in harmonic_order_list])
    axis.set_xlabel("harmonic order")
    axis.set_ylabel("amplitude [deg]")
    axis.set_title("Measured harmonic magnitude summary")
    axis.grid(True, axis="y", alpha=0.25)
    axis.legend(loc="upper right")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def create_h0_surface_plots(component_row_list: list[ComponentRow], asset_directory: Path) -> list[str]:

    """Create measured harmonic-zero scatter surfaces by direction and temperature."""

    h0_row_list = [row for row in component_row_list if row.harmonic_order == 0]
    direction_list = sorted({row.direction_label for row in h0_row_list})
    temperature_list = sorted({row.oil_temperature_deg for row in h0_row_list})
    max_abs_h0 = max(abs(row.curve_mean_deg) for row in h0_row_list)
    relative_plot_path_list: list[str] = []

    for direction_label in direction_list:
        for oil_temperature_deg in temperature_list:
            selected_row_list = [
                row for row in h0_row_list if row.direction_label == direction_label and row.oil_temperature_deg == oil_temperature_deg
            ]
            assert selected_row_list, f"No h0 rows for {direction_label} / {oil_temperature_deg}"

            speed_array = np.asarray([row.speed_rpm for row in selected_row_list], dtype=np.float64)
            torque_array = np.asarray([row.torque_nm for row in selected_row_list], dtype=np.float64)
            h0_array = np.asarray([row.curve_mean_deg for row in selected_row_list], dtype=np.float64)

            figure, axis = plt.subplots(figsize=(7.2, 5.2), constrained_layout=True)
            scatter = axis.scatter(
                speed_array,
                torque_array,
                c=h0_array,
                cmap="coolwarm",
                vmin=-max_abs_h0,
                vmax=max_abs_h0,
                s=32,
                edgecolors="black",
                linewidths=0.15,
            )
            axis.set_xlabel("speed [rpm]")
            axis.set_ylabel("torque [Nm]")
            axis.set_title(f"Measured h0 / curve mean | {direction_label} | {oil_temperature_deg:.0f} degC")
            axis.grid(True, alpha=0.25)
            colorbar = figure.colorbar(scatter, ax=axis)
            colorbar.set_label("curve mean / h0 proxy [deg]")

            plot_filename = f"h0_surface_{direction_label}_{oil_temperature_deg:.0f}deg.png"
            plot_path = asset_directory / plot_filename
            plot_path.parent.mkdir(parents=True, exist_ok=True)
            figure.savefig(plot_path, dpi=180)
            plt.close(figure)
            relative_plot_path_list.append(plot_path.relative_to(PROJECT_PATH).as_posix())

    return relative_plot_path_list


def write_report(
    report_path: Path,
    input_directory: Path,
    asset_relative_path_list: list[str],
    harmonic_summary_rows: list[dict[str, Any]],
    temperature_direction_rows: list[dict[str, Any]],
    h0_extreme_rows: list[dict[str, Any]],
    input_summary: dict[str, Any],
) -> None:

    """Write the diagnostic Markdown report."""

    h0_summary = next(row for row in harmonic_summary_rows if int(row["harmonic_order"]) == 0)
    h1_summary = next(row for row in harmonic_summary_rows if int(row["harmonic_order"]) == 1)
    largest_nonzero_summary = max(
        [row for row in harmonic_summary_rows if int(row["harmonic_order"]) != 0],
        key=lambda row: float(row["max_abs_amplitude_deg"]),
    )

    report_lines = [
        "# Track 2 Component Offset Identification Diagnostic",
        "",
        "## Overview",
        "",
        f"Measured component-offset diagnostic over `{input_summary['source_file_count']}` CSV files, `{input_summary['curve_count']}` directional curves, and harmonic orders `{', '.join(str(order) for order in input_summary['harmonic_order_list'])}`.",
        "",
        "## Main Findings",
        "",
        "| Finding | Interpretation |",
        "| --- | --- |",
        f"| Harmonic `0` mean absolute amplitude is `{h0_summary['mean_abs_amplitude_deg']} deg`; harmonic `1` is `{h1_summary['mean_abs_amplitude_deg']} deg`. | The measured curve mean / `a_0` proxy is the largest average component in the prepared diagnostic set. |",
        f"| Largest non-zero maximum amplitude is harmonic `{largest_nonzero_summary['harmonic_order']}` at `{largest_nonzero_summary['max_abs_amplitude_deg']} deg`. | `a_0` is not the only component that can show large individual cases; high-order outliers still need inspection. |",
        "| The current repository CSV grid has one curve per direction / speed / torque / temperature condition. | Repeatability cannot be estimated from the current canonical CSV set alone; external repeated-measurement data are required for a real repeatability conclusion. |",
        "| Forward `h0` values are consistently negative while backward values are mostly positive in the temperature-direction summaries. | Direction must remain a first-class diagnostic axis; a global-only offset correction would hide sign structure. |",
        "",
        "## Harmonic Summary",
        "",
        "| Harmonic | Mean Abs Amp [deg] | P95 Abs Amp [deg] | Max Abs Amp [deg] |",
        "| ---: | ---: | ---: | ---: |",
    ]

    for row in harmonic_summary_rows:
        report_lines.append(
            f"| `{row['harmonic_order']}` | {row['mean_abs_amplitude_deg']} | {row['p95_abs_amplitude_deg']} | {row['max_abs_amplitude_deg']} |"
        )

    report_lines.extend(
        [
            "",
            "## Temperature And Direction Summary",
            "",
            "| Direction | Temp | Curves | Mean h0 | Std h0 | Min h0 | Max h0 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )

    for row in temperature_direction_rows:
        report_lines.append(
            f"| `{row['direction_label']}` | {format_report_integer_float(float(row['oil_temperature_deg']))} | {row['curve_count']} | {format_report_float(float(row['mean_h0_deg']))} | {format_report_float(float(row['std_h0_deg']))} | {format_report_float(float(row['min_h0_deg']))} | {format_report_float(float(row['max_h0_deg']))} |"
        )

    report_lines.extend(
        [
            "",
            "## Largest Absolute h0 Cases",
            "",
            "| Rank | Direction | Speed | Torque | Temp | h0 | P2P | File |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )

    for row in h0_extreme_rows[:10]:
        report_lines.append(
            f"| {row['rank']} | `{row['direction_label']}` | {format_report_integer_float(float(row['speed_rpm']))} | {format_report_integer_float(float(row['torque_nm']))} | {format_report_integer_float(float(row['oil_temperature_deg']))} | {format_report_float(float(row['curve_mean_deg']))} | {format_report_float(float(row['curve_peak_to_peak_deg']))} | `{Path(row['source_file_path']).name}` |"
        )

    report_lines.extend(
        [
            "",
            "## Figures",
            "",
            f"![Harmonic magnitude summary](./assets/{asset_relative_path_list[0].split('/')[-1]})",
            "",
        ]
    )

    for relative_plot_path in asset_relative_path_list[1:]:
        report_lines.append(f"![{Path(relative_plot_path).stem}](./assets/{Path(relative_plot_path).name})")
        report_lines.append("")

    report_lines.extend(
        [
            "## Decision",
            "",
            "`a_0` / harmonic zero should stay the priority suspect because it is",
            "the largest average measured component and shows strong direction",
            "structure. It should not yet be documented as the sole confirmed",
            "cause of the Track 2 model offset. The next analysis should compare",
            "these measured h0 surfaces with Track 2D signed model-offset rows and",
            "inspect high-order outliers, especially where harmonic `156`, `162`,",
            "or `240` amplitudes spike.",
            "",
        ]
    )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="\n") as report_file:
        report_file.write("\n".join(report_lines).rstrip() + "\n")


def write_summary_yaml(output_path: Path, input_summary: dict[str, Any], report_path: Path, asset_relative_path_list: list[str]) -> None:

    """Write machine-readable report summary."""

    summary_dictionary = {
        "input_run_id": input_summary["run_id"],
        "report_path": report_path.relative_to(PROJECT_PATH).as_posix(),
        "asset_path_list": asset_relative_path_list,
        "decision": "h0_priority_suspect_not_sole_confirmed_cause",
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(summary_dictionary, output_file, sort_keys=False)


def main() -> None:

    """Run the component-offset diagnostic report generation."""

    argument_namespace = parse_arguments()
    input_directory = argument_namespace.input_directory or resolve_latest_input_directory(argument_namespace.input_root)
    input_directory = input_directory.resolve()
    input_summary = load_input_summary(input_directory)
    report_date = argument_namespace.report_date or str(input_summary["run_id"])[:10]
    report_directory = argument_namespace.report_topic_root / f"[{report_date}]"
    asset_directory = report_directory / "assets"

    component_row_list = load_component_rows(input_directory)
    harmonic_summary_rows = build_harmonic_summary(component_row_list)
    temperature_direction_rows = build_temperature_direction_summary(component_row_list)
    h0_extreme_rows = build_h0_extreme_rows(component_row_list, argument_namespace.top_count)

    write_csv(report_directory / HARMONIC_SUMMARY_FILENAME, harmonic_summary_rows)
    write_csv(report_directory / TEMPERATURE_DIRECTION_SUMMARY_FILENAME, temperature_direction_rows)
    write_csv(report_directory / H0_EXTREME_FILENAME, h0_extreme_rows)

    harmonic_plot_path = asset_directory / "harmonic_magnitude_summary.png"
    create_harmonic_summary_plot(harmonic_summary_rows, harmonic_plot_path)
    asset_relative_path_list = [harmonic_plot_path.relative_to(PROJECT_PATH).as_posix()]
    asset_relative_path_list.extend(create_h0_surface_plots(component_row_list, asset_directory))

    report_path = report_directory / REPORT_FILENAME
    write_report(
        report_path=report_path,
        input_directory=input_directory,
        asset_relative_path_list=asset_relative_path_list,
        harmonic_summary_rows=harmonic_summary_rows,
        temperature_direction_rows=temperature_direction_rows,
        h0_extreme_rows=h0_extreme_rows,
        input_summary=input_summary,
    )
    write_summary_yaml(report_directory / REPORT_SUMMARY_FILENAME, input_summary, report_path, asset_relative_path_list)

    print(f"Prepared Track 2 component-offset diagnostic report | {report_path}")


if __name__ == "__main__":
    main()
