"""Build CVP 1.4 predicted-mean versus measured-h0 surface diagnostics."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
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

DEFAULT_TRACK2D_PER_CURVE_METRICS_PATH = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2d_mean_offset_full_matrix_audit"
    / "2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit"
    / "track2d_per_curve_metrics.csv"
)
DEFAULT_TRACK2D_CANDIDATE_SUMMARY_PATH = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2d_mean_offset_full_matrix_audit"
    / "2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit"
    / "track2d_candidate_summary.csv"
)
DEFAULT_H0_CROSSCHECK_CANDIDATE_SUMMARY_PATH = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2d_h0_offset_crosscheck"
    / "2026-06-09-20-09-16__track2d_h0_offset_crosscheck"
    / "track2d_h0_offset_crosscheck_candidate_summary.csv"
)
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2d_predicted_mean_h0_surface_diagnostic"
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "component_offset_identification"
)

REPORT_FILENAME = "track2d_predicted_mean_h0_surface_diagnostic.md"
REPORT_SUMMARY_FILENAME = "track2d_predicted_mean_h0_surface_diagnostic_summary.yaml"
SELECTED_ROWS_FILENAME = "track2d_predicted_mean_h0_selected_rows.csv"
CANDIDATE_SUMMARY_FILENAME = "track2d_predicted_mean_h0_candidate_summary.csv"
DIRECTION_SUMMARY_FILENAME = "track2d_predicted_mean_h0_direction_summary.csv"
SELECTION_FILENAME = "track2d_predicted_mean_h0_candidate_selection.csv"


@dataclass(frozen=True)
class Track2DMetricRow:

    """One CVP 1.4 per-curve mean prediction diagnostic row."""

    candidate_id: str
    candidate_family: str
    candidate_surface: str
    direction_label: str
    source_file_path: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    measured_h0_deg: float
    predicted_mean_deg: float
    signed_offset_error_deg: float
    absolute_offset_error_deg: float
    raw_mae_deg: float
    centered_mae_deg: float


def parse_arguments() -> argparse.Namespace:

    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--track2d-per-curve-metrics-path", type=Path, default=DEFAULT_TRACK2D_PER_CURVE_METRICS_PATH)
    parser.add_argument("--track2d-candidate-summary-path", type=Path, default=DEFAULT_TRACK2D_CANDIDATE_SUMMARY_PATH)
    parser.add_argument(
        "--h0-crosscheck-candidate-summary-path",
        type=Path,
        default=DEFAULT_H0_CROSSCHECK_CANDIDATE_SUMMARY_PATH,
    )
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--report-topic-root", type=Path, default=DEFAULT_REPORT_TOPIC_ROOT)
    parser.add_argument("--run-id", type=str, default="")
    parser.add_argument("--report-date", type=str, default="")
    parser.add_argument("--top-count", type=int, default=10)
    return parser.parse_args()


def format_float(value: float) -> str:

    """Format a float for stable CSV output."""

    if not math.isfinite(float(value)):
        return "nan"
    return f"{float(value):.9f}"


def format_report_float(value: float) -> str:

    """Format a float for compact Markdown tables."""

    if not math.isfinite(float(value)):
        return "nan"
    return f"{float(value):.4f}"


def normalize_source_file_path(source_file_path: str) -> str:

    """Normalize repository-relative CSV paths across Windows and POSIX outputs."""

    return source_file_path.replace("\\", "/").strip()


def compute_pearson_correlation(left_values: list[float], right_values: list[float]) -> float:

    """Compute Pearson correlation, returning nan for degenerate arrays."""

    if len(left_values) < 2 or len(right_values) < 2:
        return float("nan")
    left_array = np.asarray(left_values, dtype=np.float64)
    right_array = np.asarray(right_values, dtype=np.float64)
    if float(np.std(left_array)) <= 0.0 or float(np.std(right_array)) <= 0.0:
        return float("nan")
    return float(np.corrcoef(left_array, right_array)[0, 1])


def compute_linear_fit(measured_values: list[float], predicted_values: list[float]) -> tuple[float, float]:

    """Fit predicted mean as slope * measured h0 + intercept."""

    if len(measured_values) < 2:
        return float("nan"), float("nan")
    measured_array = np.asarray(measured_values, dtype=np.float64)
    predicted_array = np.asarray(predicted_values, dtype=np.float64)
    if float(np.std(measured_array)) <= 0.0:
        return float("nan"), float("nan")
    slope, intercept = np.polyfit(measured_array, predicted_array, deg=1)
    return float(slope), float(intercept)


def load_track2d_metric_rows(input_path: Path) -> list[Track2DMetricRow]:

    """Load CVP 1.4 per-curve metrics."""

    assert input_path.exists(), f"CVP 1.4 per-curve metrics not found | {input_path}"
    row_list: list[Track2DMetricRow] = []
    with input_path.open("r", encoding="utf-8", newline="") as input_file:
        for row in csv.DictReader(input_file):
            row_list.append(
                Track2DMetricRow(
                    candidate_id=row["candidate_id"],
                    candidate_family=row["candidate_family"],
                    candidate_surface=row["candidate_surface"],
                    direction_label=row["direction_label"],
                    source_file_path=normalize_source_file_path(row["source_file_path"]),
                    speed_rpm=float(row["speed_rpm"]),
                    torque_nm=float(row["torque_nm"]),
                    oil_temperature_deg=float(row["oil_temperature_deg"]),
                    measured_h0_deg=float(row["truth_mean_deg"]),
                    predicted_mean_deg=float(row["predicted_mean_deg"]),
                    signed_offset_error_deg=float(row["signed_offset_error_deg"]),
                    absolute_offset_error_deg=float(row["absolute_offset_error_deg"]),
                    raw_mae_deg=float(row["raw_mae_deg"]),
                    centered_mae_deg=float(row["centered_mae_deg"]),
                )
            )
    assert row_list, f"No CVP 1.4 rows loaded | {input_path}"
    return row_list


def load_csv_dictionary_rows(input_path: Path) -> list[dict[str, str]]:

    """Load CSV rows as dictionaries."""

    assert input_path.exists(), f"CSV file not found | {input_path}"
    with input_path.open("r", encoding="utf-8", newline="") as input_file:
        return list(csv.DictReader(input_file))


def select_candidate_ids(
    track2d_candidate_summary_rows: list[dict[str, str]],
    h0_crosscheck_candidate_summary_rows: list[dict[str, str]],
    top_count: int,
) -> list[dict[str, Any]]:

    """Select candidate IDs for detailed mean-surface diagnostics."""

    selected_dictionary: dict[str, set[str]] = defaultdict(set)

    for row in sorted(track2d_candidate_summary_rows, key=lambda item: float(item["mean_absolute_offset_error_deg"]), reverse=True)[:top_count]:
        selected_dictionary[row["candidate_id"]].add("largest_mean_offset")

    for row in sorted(track2d_candidate_summary_rows, key=lambda item: int(item["rank"]))[:top_count]:
        selected_dictionary[row["candidate_id"]].add("track2d_top_rank")

    surface_best_seen: set[str] = set()
    for row in sorted(track2d_candidate_summary_rows, key=lambda item: int(item["rank"])):
        surface = row["candidate_surface"]
        if surface in surface_best_seen:
            continue
        selected_dictionary[row["candidate_id"]].add(f"surface_leader_{surface}")
        surface_best_seen.add(surface)

    for row in sorted(
        h0_crosscheck_candidate_summary_rows,
        key=lambda item: float(item["top_decile_overlap_lift_vs_random_decile"]),
        reverse=True,
    )[:top_count]:
        selected_dictionary[row["group_value"]].add("strong_h0_error_overlap")

    for row in sorted(
        [row for row in track2d_candidate_summary_rows if row["candidate_surface"] == "global"],
        key=lambda item: float(item["mean_absolute_offset_error_deg"]),
        reverse=True,
    )[:top_count]:
        selected_dictionary[row["candidate_id"]].add("global_high_offset")

    selection_rows: list[dict[str, Any]] = []
    for candidate_id, reason_set in sorted(selected_dictionary.items()):
        selection_rows.append(
            {
                "candidate_id": candidate_id,
                "selection_reason": ";".join(sorted(reason_set)),
            }
        )
    return selection_rows


def summarize_row_group(row_list: list[Track2DMetricRow], group_columns: dict[str, str]) -> dict[str, Any]:

    """Summarize predicted-mean behavior for one group."""

    measured_values = [row.measured_h0_deg for row in row_list]
    predicted_values = [row.predicted_mean_deg for row in row_list]
    signed_errors = [row.signed_offset_error_deg for row in row_list]
    absolute_errors = [row.absolute_offset_error_deg for row in row_list]
    slope, intercept = compute_linear_fit(measured_values, predicted_values)
    mean_bias = float(np.mean(np.asarray(signed_errors, dtype=np.float64)))
    residual_std = float(np.std(np.asarray(signed_errors, dtype=np.float64)))

    return {
        **group_columns,
        "curve_count": len(row_list),
        "mean_bias_deg": format_float(mean_bias),
        "mean_abs_offset_error_deg": format_float(float(np.mean(np.asarray(absolute_errors, dtype=np.float64)))),
        "p90_abs_offset_error_deg": format_float(float(np.percentile(np.asarray(absolute_errors, dtype=np.float64), 90.0))),
        "predicted_vs_measured_corr": format_float(compute_pearson_correlation(measured_values, predicted_values)),
        "predicted_vs_measured_slope": format_float(slope),
        "predicted_vs_measured_intercept_deg": format_float(intercept),
        "offset_residual_std_deg": format_float(residual_std),
        "mean_measured_h0_deg": format_float(float(np.mean(np.asarray(measured_values, dtype=np.float64)))),
        "mean_predicted_mean_deg": format_float(float(np.mean(np.asarray(predicted_values, dtype=np.float64)))),
    }


def build_candidate_summary_rows(row_list: list[Track2DMetricRow]) -> list[dict[str, Any]]:

    """Build candidate-level predicted mean summaries."""

    candidate_dictionary: dict[str, list[Track2DMetricRow]] = defaultdict(list)
    for row in row_list:
        candidate_dictionary[row.candidate_id].append(row)

    summary_rows: list[dict[str, Any]] = []
    for candidate_id, candidate_rows in candidate_dictionary.items():
        first_row = candidate_rows[0]
        summary_rows.append(
            summarize_row_group(
                candidate_rows,
                {
                    "candidate_id": candidate_id,
                    "candidate_family": first_row.candidate_family,
                    "candidate_surface": first_row.candidate_surface,
                },
            )
        )
    return sorted(summary_rows, key=lambda row: float(row["mean_abs_offset_error_deg"]), reverse=True)


def build_direction_summary_rows(row_list: list[Track2DMetricRow]) -> list[dict[str, Any]]:

    """Build candidate-direction predicted mean summaries."""

    group_dictionary: dict[tuple[str, str], list[Track2DMetricRow]] = defaultdict(list)
    for row in row_list:
        group_dictionary[(row.candidate_id, row.direction_label)].append(row)

    summary_rows: list[dict[str, Any]] = []
    for (candidate_id, direction_label), group_rows in sorted(group_dictionary.items()):
        first_row = group_rows[0]
        summary_rows.append(
            summarize_row_group(
                group_rows,
                {
                    "candidate_id": candidate_id,
                    "candidate_surface": first_row.candidate_surface,
                    "direction_label": direction_label,
                },
            )
        )
    return summary_rows


def metric_row_to_csv_row(row: Track2DMetricRow) -> dict[str, Any]:

    """Convert a CVP 1.4 row to a selected CSV row."""

    return {
        "candidate_id": row.candidate_id,
        "candidate_family": row.candidate_family,
        "candidate_surface": row.candidate_surface,
        "direction_label": row.direction_label,
        "source_file_path": row.source_file_path,
        "speed_rpm": format_float(row.speed_rpm),
        "torque_nm": format_float(row.torque_nm),
        "oil_temperature_deg": format_float(row.oil_temperature_deg),
        "measured_h0_deg": format_float(row.measured_h0_deg),
        "predicted_mean_deg": format_float(row.predicted_mean_deg),
        "signed_offset_error_deg": format_float(row.signed_offset_error_deg),
        "absolute_offset_error_deg": format_float(row.absolute_offset_error_deg),
        "raw_mae_deg": format_float(row.raw_mae_deg),
        "centered_mae_deg": format_float(row.centered_mae_deg),
    }


def write_csv(output_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write dictionaries to CSV."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    assert row_list, f"No rows available for CSV output | {output_path}"
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(row_list[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(row_list)


def create_predicted_vs_measured_grid(
    selected_row_dictionary: dict[str, list[Track2DMetricRow]],
    candidate_summary_rows: list[dict[str, Any]],
    output_path: Path,
    top_count: int,
) -> None:

    """Create predicted-mean versus measured-h0 scatter panels."""

    candidate_order = [row["candidate_id"] for row in candidate_summary_rows[: min(9, top_count)]]
    figure, axes = plt.subplots(3, 3, figsize=(10.2, 8.2), constrained_layout=True)
    flat_axes = list(axes.ravel())

    for axis, candidate_id in zip(flat_axes, candidate_order):
        rows = selected_row_dictionary[candidate_id]
        measured_values = np.asarray([row.measured_h0_deg for row in rows], dtype=np.float64)
        predicted_values = np.asarray([row.predicted_mean_deg for row in rows], dtype=np.float64)
        direction_values = [row.direction_label for row in rows]
        for direction_label, color in [("forward", "#c75f2a"), ("backward", "#2f6f9f")]:
            mask = np.asarray([direction == direction_label for direction in direction_values], dtype=bool)
            if bool(np.any(mask)):
                axis.scatter(measured_values[mask], predicted_values[mask], s=14, alpha=0.65, label=direction_label, color=color)
        lower = float(min(np.min(measured_values), np.min(predicted_values)))
        upper = float(max(np.max(measured_values), np.max(predicted_values)))
        axis.plot([lower, upper], [lower, upper], color="#444444", linewidth=0.8, linestyle="--")
        axis.set_title(candidate_id, fontsize=8)
        axis.grid(True, alpha=0.25)
        axis.tick_params(labelsize=7)

    for axis in flat_axes[len(candidate_order) :]:
        axis.axis("off")

    flat_axes[0].legend(loc="best", fontsize=7)
    figure.supxlabel("measured h0 / truth mean [deg]", fontsize=9)
    figure.supylabel("predicted mean [deg]", fontsize=9)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def create_speed_torque_error_panels(
    selected_row_dictionary: dict[str, list[Track2DMetricRow]],
    candidate_summary_rows: list[dict[str, Any]],
    output_path: Path,
    top_count: int,
) -> None:

    """Create speed/torque scatter panels colored by signed offset error."""

    candidate_order = [row["candidate_id"] for row in candidate_summary_rows[: min(6, top_count)]]
    figure, axes = plt.subplots(2, 3, figsize=(10.2, 6.3), constrained_layout=True)
    flat_axes = list(axes.ravel())

    max_abs_error = max(abs(row.signed_offset_error_deg) for candidate_id in candidate_order for row in selected_row_dictionary[candidate_id])
    for axis, candidate_id in zip(flat_axes, candidate_order):
        rows = selected_row_dictionary[candidate_id]
        scatter = axis.scatter(
            [row.speed_rpm for row in rows],
            [row.torque_nm for row in rows],
            c=[row.signed_offset_error_deg for row in rows],
            cmap="coolwarm",
            vmin=-max_abs_error,
            vmax=max_abs_error,
            s=18,
            alpha=0.75,
            edgecolors="none",
        )
        axis.set_title(candidate_id, fontsize=8)
        axis.set_xlabel("speed [rpm]", fontsize=8)
        axis.set_ylabel("torque [Nm]", fontsize=8)
        axis.tick_params(labelsize=7)
        axis.grid(True, alpha=0.25)

    for axis in flat_axes[len(candidate_order) :]:
        axis.axis("off")

    figure.colorbar(scatter, ax=flat_axes[: len(candidate_order)], shrink=0.8, label="signed offset error [deg]")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def build_report_lines(
    run_id: str,
    candidate_summary_rows: list[dict[str, Any]],
    direction_summary_rows: list[dict[str, Any]],
    selection_rows: list[dict[str, Any]],
    output_directory: Path,
    asset_relative_path_list: list[str],
    top_count: int,
) -> list[str]:

    """Build Markdown report lines."""

    median_slope = float(np.median([float(row["predicted_vs_measured_slope"]) for row in candidate_summary_rows]))
    median_bias = float(np.median([float(row["mean_bias_deg"]) for row in candidate_summary_rows]))
    median_abs_error = float(np.median([float(row["mean_abs_offset_error_deg"]) for row in candidate_summary_rows]))
    high_bias_rows = [row for row in candidate_summary_rows if abs(float(row["mean_bias_deg"])) >= 0.005]
    weak_slope_rows = [row for row in candidate_summary_rows if abs(float(row["predicted_vs_measured_slope"]) - 1.0) >= 0.50]

    report_lines = [
        "# CVP 1.4 Predicted Mean h0 Surface Diagnostic",
        "",
        "## Overview",
        "",
        (
            f"Predicted-mean versus measured-`h0` diagnostic over `{len(candidate_summary_rows)}` selected candidates "
            f"from the `CVP 1.4` per-curve matrix."
        ),
        "",
        "## Decision",
        "",
        "- The next intervention should target predicted mean / offset-surface behavior, not measured `h0` magnitude alone.",
        (
            f"- Median selected-candidate mean bias is `{format_report_float(median_bias)}` deg and median mean absolute "
            f"offset error is `{format_report_float(median_abs_error)}` deg."
        ),
        (
            f"- Median predicted-mean versus measured-`h0` slope is `{format_report_float(median_slope)}`; "
            f"`{len(weak_slope_rows)}` selected candidates deviate from unit slope by at least `0.50`."
        ),
        f"- `{len(high_bias_rows)}` selected candidates have absolute mean bias at least `0.005 deg`.",
        "",
        "## Candidate Selection",
        "",
        "| Candidate | Reason |",
        "| --- | --- |",
    ]

    for row in selection_rows:
        report_lines.append(f"| `{row['candidate_id']}` | `{row['selection_reason']}` |")

    report_lines.extend(
        [
            "",
            "## Candidate Mean-Surface Summary",
            "",
            "| Candidate | Surface | Bias | Mean AE | P90 AE | Corr | Slope | Intercept |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )

    for row in candidate_summary_rows[:top_count]:
        report_lines.append(
            f"| `{row['candidate_id']}` | `{row['candidate_surface']}` | {format_report_float(float(row['mean_bias_deg']))} | "
            f"{format_report_float(float(row['mean_abs_offset_error_deg']))} | {format_report_float(float(row['p90_abs_offset_error_deg']))} | "
            f"{format_report_float(float(row['predicted_vs_measured_corr']))} | {format_report_float(float(row['predicted_vs_measured_slope']))} | "
            f"{format_report_float(float(row['predicted_vs_measured_intercept_deg']))} |"
        )

    report_lines.extend(
        [
            "",
            "## Direction Split",
            "",
            "| Candidate | Direction | Bias | Mean AE | Corr | Slope |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )

    top_candidate_set = {row["candidate_id"] for row in candidate_summary_rows[: min(top_count, 12)]}
    for row in [row for row in direction_summary_rows if row["candidate_id"] in top_candidate_set]:
        report_lines.append(
            f"| `{row['candidate_id']}` | `{row['direction_label']}` | {format_report_float(float(row['mean_bias_deg']))} | "
            f"{format_report_float(float(row['mean_abs_offset_error_deg']))} | {format_report_float(float(row['predicted_vs_measured_corr']))} | "
            f"{format_report_float(float(row['predicted_vs_measured_slope']))} |"
        )

    report_lines.extend(
        [
            "",
            "## Visual Diagnostics",
            "",
            f"![Predicted mean versus measured h0](./{asset_relative_path_list[0]})",
            "",
            f"![Signed offset error by speed and torque](./{asset_relative_path_list[1]})",
            "",
            "## Interpretation",
            "",
            (
                "The useful signal is model-side mean-surface behavior: candidates with large offset error generally show "
                "candidate-specific bias, compressed or shifted predicted-mean surfaces, or direction-dependent behavior."
            ),
            (
                "This supports planning an offset/mean head or calibration branch that is evaluated per `Fw`, `Bw`, and "
                "`global` surface, while keeping centered-shape metrics separate."
            ),
            "",
            "## Machine-Readable Artifacts",
            "",
            f"- `{(output_directory / CANDIDATE_SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / DIRECTION_SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / SELECTION_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / SELECTED_ROWS_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / REPORT_SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            "",
            "## Reproduction",
            "",
            "```powershell",
            "conda run -n pinns_env python -B scripts/reports/analysis/build_track2d_predicted_mean_h0_surface_diagnostic.py",
            "```",
        ]
    )
    return report_lines


def write_report(report_path: Path, report_lines: list[str]) -> None:

    """Write Markdown report."""

    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="\n") as report_file:
        report_file.write("\n".join(report_lines).rstrip() + "\n")


def write_summary_yaml(output_path: Path, run_id: str, report_path: Path, candidate_summary_rows: list[dict[str, Any]]) -> None:

    """Write machine-readable report summary."""

    summary_dictionary = {
        "run_id": run_id,
        "report_path": report_path.relative_to(PROJECT_PATH).as_posix(),
        "selected_candidate_count": len(candidate_summary_rows),
        "median_mean_bias_deg": float(np.median([float(row["mean_bias_deg"]) for row in candidate_summary_rows])),
        "median_mean_abs_offset_error_deg": float(np.median([float(row["mean_abs_offset_error_deg"]) for row in candidate_summary_rows])),
        "median_predicted_vs_measured_slope": float(np.median([float(row["predicted_vs_measured_slope"]) for row in candidate_summary_rows])),
        "decision": "model_predicted_mean_surface_requires_dedicated_offset_intervention",
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(summary_dictionary, output_file, sort_keys=False)


def main() -> None:

    """Run the predicted-mean h0 surface diagnostic."""

    args = parse_arguments()
    run_id = args.run_id if args.run_id else f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}__track2d_predicted_mean_h0_surface_diagnostic"
    report_date = args.report_date if args.report_date else datetime.now().strftime("%Y-%m-%d")

    metric_rows = load_track2d_metric_rows(args.track2d_per_curve_metrics_path)
    track2d_candidate_summary_rows = load_csv_dictionary_rows(args.track2d_candidate_summary_path)
    h0_crosscheck_candidate_summary_rows = load_csv_dictionary_rows(args.h0_crosscheck_candidate_summary_path)
    selection_rows = select_candidate_ids(track2d_candidate_summary_rows, h0_crosscheck_candidate_summary_rows, args.top_count)
    selected_candidate_set = {row["candidate_id"] for row in selection_rows}
    selected_metric_rows = [row for row in metric_rows if row.candidate_id in selected_candidate_set]
    assert selected_metric_rows, "No rows selected for predicted-mean h0 diagnostic"

    output_directory = args.output_root / run_id
    report_directory = args.report_topic_root / f"[{report_date}]"
    asset_directory = report_directory / "assets"
    report_path = report_directory / REPORT_FILENAME

    candidate_summary_rows = build_candidate_summary_rows(selected_metric_rows)
    direction_summary_rows = build_direction_summary_rows(selected_metric_rows)
    selected_row_dictionary: dict[str, list[Track2DMetricRow]] = defaultdict(list)
    for row in selected_metric_rows:
        selected_row_dictionary[row.candidate_id].append(row)

    predicted_vs_measured_plot_path = asset_directory / "track2d_predicted_mean_vs_measured_h0_grid.png"
    speed_torque_error_plot_path = asset_directory / "track2d_predicted_mean_h0_speed_torque_error.png"
    create_predicted_vs_measured_grid(selected_row_dictionary, candidate_summary_rows, predicted_vs_measured_plot_path, args.top_count)
    create_speed_torque_error_panels(selected_row_dictionary, candidate_summary_rows, speed_torque_error_plot_path, args.top_count)

    write_csv(output_directory / SELECTION_FILENAME, selection_rows)
    write_csv(output_directory / CANDIDATE_SUMMARY_FILENAME, candidate_summary_rows)
    write_csv(output_directory / DIRECTION_SUMMARY_FILENAME, direction_summary_rows)
    write_csv(output_directory / SELECTED_ROWS_FILENAME, [metric_row_to_csv_row(row) for row in selected_metric_rows])
    write_summary_yaml(output_directory / REPORT_SUMMARY_FILENAME, run_id, report_path, candidate_summary_rows)

    asset_relative_path_list = [
        f"assets/{predicted_vs_measured_plot_path.name}",
        f"assets/{speed_torque_error_plot_path.name}",
    ]
    report_lines = build_report_lines(
        run_id=run_id,
        candidate_summary_rows=candidate_summary_rows,
        direction_summary_rows=direction_summary_rows,
        selection_rows=selection_rows,
        output_directory=output_directory,
        asset_relative_path_list=asset_relative_path_list,
        top_count=args.top_count,
    )
    write_report(report_path, report_lines)

    print(f"Prepared CVP 1.4 predicted-mean h0 diagnostic | {output_directory}")
    print(f"Prepared Markdown report | {report_path}")


if __name__ == "__main__":
    main()
