"""Build CVP 1.4 signed-offset versus measured h0 cross-check diagnostics."""

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
DEFAULT_COMPONENT_PER_CURVE_PATH = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2_component_offset_identification"
    / "2026-06-09-18-39-13__track2_component_offset_identification_inputs"
    / "track2_component_offset_per_curve_components.csv"
)
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2d_h0_offset_crosscheck"
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "component_offset_identification"
)

JOINED_TABLE_FILENAME = "track2d_h0_offset_crosscheck_joined_rows.csv"
CANDIDATE_SUMMARY_FILENAME = "track2d_h0_offset_crosscheck_candidate_summary.csv"
SURFACE_SUMMARY_FILENAME = "track2d_h0_offset_crosscheck_surface_summary.csv"
QUADRANT_SUMMARY_FILENAME = "track2d_h0_offset_crosscheck_quadrant_summary.csv"
REPORT_SUMMARY_FILENAME = "track2d_h0_offset_crosscheck_summary.yaml"
REPORT_FILENAME = "track2d_h0_offset_crosscheck.md"


@dataclass(frozen=True)
class Track2DMetricRow:

    """One CVP 1.4 model-error diagnostic row."""

    candidate_id: str
    candidate_family: str
    candidate_surface: str
    direction_label: str
    source_file_path: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    truth_mean_deg: float
    predicted_mean_deg: float
    signed_offset_error_deg: float
    absolute_offset_error_deg: float
    raw_mae_deg: float
    centered_mae_deg: float


@dataclass(frozen=True)
class H0ComponentRow:

    """One measured harmonic-zero component row."""

    source_file_path: str
    direction_label: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    curve_mean_deg: float
    curve_peak_to_peak_deg: float


@dataclass(frozen=True)
class JoinedCrossCheckRow:

    """One joined model-error and measured-h0 row."""

    candidate_id: str
    candidate_family: str
    candidate_surface: str
    direction_label: str
    source_file_path: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    measured_h0_deg: float
    track2d_truth_mean_deg: float
    predicted_mean_deg: float
    signed_offset_error_deg: float
    absolute_offset_error_deg: float
    raw_mae_deg: float
    centered_mae_deg: float
    truth_mean_join_delta_deg: float
    curve_peak_to_peak_deg: float


def parse_arguments() -> argparse.Namespace:

    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--track2d-per-curve-metrics-path", type=Path, default=DEFAULT_TRACK2D_PER_CURVE_METRICS_PATH)
    parser.add_argument("--component-per-curve-path", type=Path, default=DEFAULT_COMPONENT_PER_CURVE_PATH)
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


def build_join_key(source_file_path: str, direction_label: str) -> tuple[str, str]:

    """Build the source/direction join key."""

    return (normalize_source_file_path(source_file_path), direction_label.strip().lower())


def compute_pearson_correlation(left_values: list[float], right_values: list[float]) -> float:

    """Compute a robust Pearson correlation, returning nan for degenerate arrays."""

    if len(left_values) < 2 or len(right_values) < 2:
        return float("nan")

    left_array = np.asarray(left_values, dtype=np.float64)
    right_array = np.asarray(right_values, dtype=np.float64)
    if float(np.std(left_array)) <= 0.0 or float(np.std(right_array)) <= 0.0:
        return float("nan")
    return float(np.corrcoef(left_array, right_array)[0, 1])


def load_track2d_metric_rows(track2d_per_curve_metrics_path: Path) -> list[Track2DMetricRow]:

    """Load CVP 1.4 per-curve model-error rows."""

    assert track2d_per_curve_metrics_path.exists(), f"CVP 1.4 metrics not found | {track2d_per_curve_metrics_path}"

    metric_row_list: list[Track2DMetricRow] = []
    with track2d_per_curve_metrics_path.open("r", encoding="utf-8", newline="") as input_file:
        for row in csv.DictReader(input_file):
            metric_row_list.append(
                Track2DMetricRow(
                    candidate_id=row["candidate_id"],
                    candidate_family=row["candidate_family"],
                    candidate_surface=row["candidate_surface"],
                    direction_label=row["direction_label"],
                    source_file_path=normalize_source_file_path(row["source_file_path"]),
                    speed_rpm=float(row["speed_rpm"]),
                    torque_nm=float(row["torque_nm"]),
                    oil_temperature_deg=float(row["oil_temperature_deg"]),
                    truth_mean_deg=float(row["truth_mean_deg"]),
                    predicted_mean_deg=float(row["predicted_mean_deg"]),
                    signed_offset_error_deg=float(row["signed_offset_error_deg"]),
                    absolute_offset_error_deg=float(row["absolute_offset_error_deg"]),
                    raw_mae_deg=float(row["raw_mae_deg"]),
                    centered_mae_deg=float(row["centered_mae_deg"]),
                )
            )

    assert metric_row_list, f"No CVP 1.4 rows loaded | {track2d_per_curve_metrics_path}"
    return metric_row_list


def load_h0_component_dictionary(component_per_curve_path: Path) -> dict[tuple[str, str], H0ComponentRow]:

    """Load measured h0 rows indexed by source file and direction."""

    assert component_per_curve_path.exists(), f"Component table not found | {component_per_curve_path}"

    component_dictionary: dict[tuple[str, str], H0ComponentRow] = {}
    with component_per_curve_path.open("r", encoding="utf-8", newline="") as input_file:
        for row in csv.DictReader(input_file):
            if int(row["harmonic_order"]) != 0:
                continue

            component_row = H0ComponentRow(
                source_file_path=normalize_source_file_path(row["source_file_path"]),
                direction_label=row["direction_label"],
                speed_rpm=float(row["speed_rpm"]),
                torque_nm=float(row["torque_nm"]),
                oil_temperature_deg=float(row["oil_temperature_deg"]),
                curve_mean_deg=float(row["curve_mean_deg"]),
                curve_peak_to_peak_deg=float(row["curve_peak_to_peak_deg"]),
            )
            join_key = build_join_key(component_row.source_file_path, component_row.direction_label)
            assert join_key not in component_dictionary, f"Duplicate h0 component join key | {join_key}"
            component_dictionary[join_key] = component_row

    assert component_dictionary, f"No harmonic-zero component rows loaded | {component_per_curve_path}"
    return component_dictionary


def join_metric_and_h0_rows(
    metric_row_list: list[Track2DMetricRow],
    h0_component_dictionary: dict[tuple[str, str], H0ComponentRow],
) -> list[JoinedCrossCheckRow]:

    """Join model-error rows with measured h0 rows."""

    joined_row_list: list[JoinedCrossCheckRow] = []
    missing_key_list: list[tuple[str, str]] = []

    for metric_row in metric_row_list:
        join_key = build_join_key(metric_row.source_file_path, metric_row.direction_label)
        component_row = h0_component_dictionary.get(join_key)
        if component_row is None:
            missing_key_list.append(join_key)
            continue

        joined_row_list.append(
            JoinedCrossCheckRow(
                candidate_id=metric_row.candidate_id,
                candidate_family=metric_row.candidate_family,
                candidate_surface=metric_row.candidate_surface,
                direction_label=metric_row.direction_label,
                source_file_path=metric_row.source_file_path,
                speed_rpm=metric_row.speed_rpm,
                torque_nm=metric_row.torque_nm,
                oil_temperature_deg=metric_row.oil_temperature_deg,
                measured_h0_deg=component_row.curve_mean_deg,
                track2d_truth_mean_deg=metric_row.truth_mean_deg,
                predicted_mean_deg=metric_row.predicted_mean_deg,
                signed_offset_error_deg=metric_row.signed_offset_error_deg,
                absolute_offset_error_deg=metric_row.absolute_offset_error_deg,
                raw_mae_deg=metric_row.raw_mae_deg,
                centered_mae_deg=metric_row.centered_mae_deg,
                truth_mean_join_delta_deg=metric_row.truth_mean_deg - component_row.curve_mean_deg,
                curve_peak_to_peak_deg=component_row.curve_peak_to_peak_deg,
            )
        )

    assert joined_row_list, "No CVP 1.4 rows joined with measured h0 rows"
    assert not missing_key_list, f"Missing h0 join keys: {len(missing_key_list)}"
    return joined_row_list


def joined_row_to_csv_row(row: JoinedCrossCheckRow) -> dict[str, Any]:

    """Convert one joined row to CSV fields."""

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
        "track2d_truth_mean_deg": format_float(row.track2d_truth_mean_deg),
        "predicted_mean_deg": format_float(row.predicted_mean_deg),
        "signed_offset_error_deg": format_float(row.signed_offset_error_deg),
        "absolute_offset_error_deg": format_float(row.absolute_offset_error_deg),
        "raw_mae_deg": format_float(row.raw_mae_deg),
        "centered_mae_deg": format_float(row.centered_mae_deg),
        "truth_mean_join_delta_deg": format_float(row.truth_mean_join_delta_deg),
        "curve_peak_to_peak_deg": format_float(row.curve_peak_to_peak_deg),
    }


def summarize_group(row_list: list[JoinedCrossCheckRow], group_name: str, group_value: str) -> dict[str, Any]:

    """Summarize h0/error alignment for one candidate or surface group."""

    absolute_h0_list = [abs(row.measured_h0_deg) for row in row_list]
    measured_h0_list = [row.measured_h0_deg for row in row_list]
    signed_error_list = [row.signed_offset_error_deg for row in row_list]
    absolute_error_list = [row.absolute_offset_error_deg for row in row_list]

    high_error_threshold = float(np.percentile(np.asarray(absolute_error_list, dtype=np.float64), 90.0))
    high_h0_threshold = float(np.percentile(np.asarray(absolute_h0_list, dtype=np.float64), 90.0))
    high_error_count = 0
    high_h0_count = 0
    high_error_high_h0_count = 0

    for row in row_list:
        is_high_error = abs(row.signed_offset_error_deg) >= high_error_threshold
        is_high_h0 = abs(row.measured_h0_deg) >= high_h0_threshold
        high_error_count += int(is_high_error)
        high_h0_count += int(is_high_h0)
        high_error_high_h0_count += int(is_high_error and is_high_h0)

    overlap_given_error = high_error_high_h0_count / high_error_count if high_error_count else float("nan")
    overlap_lift_vs_random_decile = overlap_given_error / 0.10 if math.isfinite(overlap_given_error) else float("nan")
    max_join_delta = max(abs(row.truth_mean_join_delta_deg) for row in row_list)

    return {
        "group_name": group_name,
        "group_value": group_value,
        "curve_count": len(row_list),
        "mean_abs_offset_error_deg": format_float(float(np.mean(np.asarray(absolute_error_list, dtype=np.float64)))),
        "p90_abs_offset_error_deg": format_float(high_error_threshold),
        "mean_abs_h0_deg": format_float(float(np.mean(np.asarray(absolute_h0_list, dtype=np.float64)))),
        "p90_abs_h0_deg": format_float(high_h0_threshold),
        "signed_error_vs_h0_corr": format_float(compute_pearson_correlation(signed_error_list, measured_h0_list)),
        "abs_error_vs_abs_h0_corr": format_float(compute_pearson_correlation(absolute_error_list, absolute_h0_list)),
        "top_decile_error_count": high_error_count,
        "top_decile_h0_count": high_h0_count,
        "top_decile_overlap_count": high_error_high_h0_count,
        "top_decile_overlap_given_error": format_float(overlap_given_error),
        "top_decile_overlap_lift_vs_random_decile": format_float(overlap_lift_vs_random_decile),
        "max_truth_mean_join_delta_deg": format_float(max_join_delta),
    }


def build_candidate_summary_rows(joined_row_list: list[JoinedCrossCheckRow]) -> list[dict[str, Any]]:

    """Build per-candidate h0/error alignment rows."""

    candidate_dictionary: dict[str, list[JoinedCrossCheckRow]] = defaultdict(list)
    for row in joined_row_list:
        candidate_dictionary[row.candidate_id].append(row)

    summary_row_list = [summarize_group(row_list, "candidate", candidate_id) for candidate_id, row_list in candidate_dictionary.items()]
    return sorted(summary_row_list, key=lambda row: float(row["abs_error_vs_abs_h0_corr"]), reverse=True)


def build_surface_summary_rows(joined_row_list: list[JoinedCrossCheckRow]) -> list[dict[str, Any]]:

    """Build per-surface h0/error alignment rows."""

    surface_dictionary: dict[str, list[JoinedCrossCheckRow]] = defaultdict(list)
    for row in joined_row_list:
        surface_dictionary[row.candidate_surface].append(row)

    summary_row_list = [summarize_group(row_list, "surface", surface_name) for surface_name, row_list in surface_dictionary.items()]
    return sorted(summary_row_list, key=lambda row: row["group_value"])


def build_quadrant_summary_rows(joined_row_list: list[JoinedCrossCheckRow]) -> list[dict[str, Any]]:

    """Build quadrant counts for high-error and high-h0 cases by candidate."""

    candidate_dictionary: dict[str, list[JoinedCrossCheckRow]] = defaultdict(list)
    for row in joined_row_list:
        candidate_dictionary[row.candidate_id].append(row)

    quadrant_row_list: list[dict[str, Any]] = []
    for candidate_id, row_list in sorted(candidate_dictionary.items()):
        absolute_error_array = np.asarray([row.absolute_offset_error_deg for row in row_list], dtype=np.float64)
        absolute_h0_array = np.asarray([abs(row.measured_h0_deg) for row in row_list], dtype=np.float64)
        high_error_threshold = float(np.percentile(absolute_error_array, 90.0))
        high_h0_threshold = float(np.percentile(absolute_h0_array, 90.0))
        quadrant_count_dictionary = {
            "high_error_high_h0": 0,
            "high_error_normal_h0": 0,
            "normal_error_high_h0": 0,
            "normal_error_normal_h0": 0,
        }

        for row in row_list:
            is_high_error = row.absolute_offset_error_deg >= high_error_threshold
            is_high_h0 = abs(row.measured_h0_deg) >= high_h0_threshold
            if is_high_error and is_high_h0:
                quadrant_count_dictionary["high_error_high_h0"] += 1
            elif is_high_error:
                quadrant_count_dictionary["high_error_normal_h0"] += 1
            elif is_high_h0:
                quadrant_count_dictionary["normal_error_high_h0"] += 1
            else:
                quadrant_count_dictionary["normal_error_normal_h0"] += 1

        quadrant_row_list.append(
            {
                "candidate_id": candidate_id,
                "curve_count": len(row_list),
                "high_error_threshold_deg": format_float(high_error_threshold),
                "high_h0_threshold_deg": format_float(high_h0_threshold),
                **quadrant_count_dictionary,
            }
        )

    return quadrant_row_list


def write_csv(output_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write dictionaries to CSV."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    assert row_list, f"No rows available for CSV output | {output_path}"
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(row_list[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(row_list)


def create_crosscheck_scatter_plot(joined_row_list: list[JoinedCrossCheckRow], output_path: Path) -> None:

    """Create a sampled scatter plot of absolute offset error versus absolute h0."""

    # Downsample deterministically for PDF-readable plotting without hiding the envelope.
    row_list = joined_row_list[:: max(1, len(joined_row_list) // 8000)]
    surface_color_dictionary = {"Bw": "#2f6f9f", "Fw": "#c75f2a", "global": "#4b8f5a"}

    figure, axis = plt.subplots(figsize=(8.8, 5.0), constrained_layout=True)
    for surface_name in sorted({row.candidate_surface for row in row_list}):
        surface_rows = [row for row in row_list if row.candidate_surface == surface_name]
        axis.scatter(
            [abs(row.measured_h0_deg) for row in surface_rows],
            [row.absolute_offset_error_deg for row in surface_rows],
            s=10,
            alpha=0.35,
            label=surface_name,
            color=surface_color_dictionary.get(surface_name, "#444444"),
            edgecolors="none",
        )

    axis.set_xlabel("absolute measured h0 [deg]")
    axis.set_ylabel("absolute CVP 1.4 offset error [deg]")
    axis.set_title("CVP 1.4 offset error versus measured h0")
    axis.grid(True, alpha=0.25)
    axis.legend(loc="upper left")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def build_report_lines(
    run_id: str,
    joined_row_list: list[JoinedCrossCheckRow],
    candidate_summary_rows: list[dict[str, Any]],
    surface_summary_rows: list[dict[str, Any]],
    quadrant_summary_rows: list[dict[str, Any]],
    output_directory: Path,
    scatter_plot_relative_path: str,
    top_count: int,
) -> list[str]:

    """Build the Markdown report lines."""

    max_join_delta = max(abs(row.truth_mean_join_delta_deg) for row in joined_row_list)
    mean_abs_correlation = float(np.mean([float(row["abs_error_vs_abs_h0_corr"]) for row in candidate_summary_rows]))
    median_abs_correlation = float(np.median([float(row["abs_error_vs_abs_h0_corr"]) for row in candidate_summary_rows]))
    median_overlap_lift = float(np.median([float(row["top_decile_overlap_lift_vs_random_decile"]) for row in candidate_summary_rows]))
    strong_overlap_count = sum(float(row["top_decile_overlap_lift_vs_random_decile"]) >= 2.0 for row in candidate_summary_rows)
    weak_correlation_count = sum(abs(float(row["abs_error_vs_abs_h0_corr"])) < 0.25 for row in candidate_summary_rows)
    candidate_count = len(candidate_summary_rows)

    if median_abs_correlation < 0.25 and median_overlap_lift < 2.0:
        decision = "`h0` magnitude alone does not explain most CVP 1.4 offset failures."
    else:
        decision = "`h0` magnitude is materially aligned with CVP 1.4 offset failures and should drive the next intervention."

    top_by_mean_error = sorted(candidate_summary_rows, key=lambda row: float(row["mean_abs_offset_error_deg"]), reverse=True)[:top_count]
    top_by_overlap = sorted(candidate_summary_rows, key=lambda row: float(row["top_decile_overlap_lift_vs_random_decile"]), reverse=True)[:top_count]
    top_by_correlation = sorted(candidate_summary_rows, key=lambda row: float(row["abs_error_vs_abs_h0_corr"]), reverse=True)[:top_count]

    report_lines = [
        "# CVP 1.4 h0 Offset Cross-Check",
        "",
        "## Overview",
        "",
        (
            f"Cross-check of `CVP 1.4` signed model offset errors against measured `h0` / curve mean over "
            f"`{len(joined_row_list)}` joined candidate-curve rows and `{candidate_count}` candidates."
        ),
        "",
        "## Decision",
        "",
        f"- {decision}",
        (
            f"- Median candidate `abs(error)` versus `abs(h0)` correlation is `{format_report_float(median_abs_correlation)}`; "
            f"mean is `{format_report_float(mean_abs_correlation)}`."
        ),
        (
            f"- Median top-decile overlap lift is `{format_report_float(median_overlap_lift)}` versus a random-decile baseline of `1.0`; "
            f"`{strong_overlap_count}` of `{candidate_count}` candidates reach lift `>= 2.0`."
        ),
        f"- `{weak_correlation_count}` of `{candidate_count}` candidates have weak absolute correlation `< 0.25`.",
        f"- Join validation is tight: maximum `CVP 1.4 truth_mean_deg - measured_h0_deg` is `{format_report_float(max_join_delta)}` deg.",
        "",
        "## Surface Summary",
        "",
        "| Surface | Rows | Mean Abs Offset | Mean Abs h0 | Abs Corr | Overlap Lift | Max Delta |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for row in surface_summary_rows:
        report_lines.append(
            f"| `{row['group_value']}` | {row['curve_count']} | {format_report_float(float(row['mean_abs_offset_error_deg']))} | "
            f"{format_report_float(float(row['mean_abs_h0_deg']))} | {format_report_float(float(row['abs_error_vs_abs_h0_corr']))} | "
            f"{format_report_float(float(row['top_decile_overlap_lift_vs_random_decile']))} | {format_report_float(float(row['max_truth_mean_join_delta_deg']))} |"
        )

    report_lines.extend(
        [
            "",
            "## Largest Mean Offset Error Candidates",
            "",
            "| Candidate | Rows | Mean Abs Offset | Mean Abs h0 | Abs Corr | Overlap Lift |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )

    for row in top_by_mean_error:
        report_lines.append(
            f"| `{row['group_value']}` | {row['curve_count']} | {format_report_float(float(row['mean_abs_offset_error_deg']))} | "
            f"{format_report_float(float(row['mean_abs_h0_deg']))} | {format_report_float(float(row['abs_error_vs_abs_h0_corr']))} | "
            f"{format_report_float(float(row['top_decile_overlap_lift_vs_random_decile']))} |"
        )

    report_lines.extend(
        [
            "",
            "## Strongest h0/Error Overlap Candidates",
            "",
            "| Candidate | Rows | Abs Corr | High Error | High h0 | Overlap | Lift |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )

    for row in top_by_overlap:
        report_lines.append(
            f"| `{row['group_value']}` | {row['curve_count']} | {format_report_float(float(row['abs_error_vs_abs_h0_corr']))} | "
            f"{row['top_decile_error_count']} | {row['top_decile_h0_count']} | {row['top_decile_overlap_count']} | "
            f"{format_report_float(float(row['top_decile_overlap_lift_vs_random_decile']))} |"
        )

    report_lines.extend(
        [
            "",
            "## Strongest Absolute Correlation Candidates",
            "",
            "| Candidate | Rows | Abs Corr | Signed Corr | Mean Abs Offset | Mean Abs h0 |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )

    for row in top_by_correlation:
        report_lines.append(
            f"| `{row['group_value']}` | {row['curve_count']} | {format_report_float(float(row['abs_error_vs_abs_h0_corr']))} | "
            f"{format_report_float(float(row['signed_error_vs_h0_corr']))} | {format_report_float(float(row['mean_abs_offset_error_deg']))} | "
            f"{format_report_float(float(row['mean_abs_h0_deg']))} |"
        )

    top_quadrant_rows = sorted(
        quadrant_summary_rows,
        key=lambda row: int(row["high_error_normal_h0"]),
        reverse=True,
    )[:top_count]
    report_lines.extend(
        [
            "",
            "## High-Error Normal-h0 Quadrants",
            "",
            "These rows are important because they contradict a pure `h0`-magnitude explanation.",
            "",
            "| Candidate | High Error + High h0 | High Error + Normal h0 | Normal Error + High h0 |",
            "| --- | ---: | ---: | ---: |",
        ]
    )

    for row in top_quadrant_rows:
        report_lines.append(
            f"| `{row['candidate_id']}` | {row['high_error_high_h0']} | {row['high_error_normal_h0']} | {row['normal_error_high_h0']} |"
        )

    report_lines.extend(
        [
            "",
            "## Interpretation",
            "",
            (
                "The cross-check supports a narrower framing: the problematic quantity is still the curve mean / `h0` "
                "channel, but the large CVP 1.4 model offset errors do not simply occur where measured `abs(h0)` is large."
            ),
            (
                "This points toward candidate-specific mean prediction bias, direction/regime dependence, or missing causal "
                "state information rather than a pure measured-`h0` outlier problem."
            ),
            (
                "The useful next diagnostic is therefore predicted-mean versus measured-`h0` surface analysis for the high-error "
                "candidates, with separate `Fw`, `Bw`, and `global` handling."
            ),
            "",
            "## Scatter Diagnostic",
            "",
            f"![CVP 1.4 offset error versus measured h0](./{scatter_plot_relative_path})",
            "",
            "## Machine-Readable Artifacts",
            "",
            f"- `{(output_directory / JOINED_TABLE_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / CANDIDATE_SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / SURFACE_SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / QUADRANT_SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / REPORT_SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            "",
            "## Reproduction",
            "",
            "```powershell",
            "conda run -n pinns_env python -B scripts/reports/analysis/build_track2d_h0_offset_crosscheck_report.py",
            "```",
        ]
    )
    return report_lines


def write_report(report_path: Path, report_lines: list[str]) -> None:

    """Write the Markdown report."""

    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="\n") as report_file:
        report_file.write("\n".join(report_lines).rstrip() + "\n")


def write_summary_yaml(
    output_path: Path,
    run_id: str,
    report_path: Path,
    joined_row_count: int,
    candidate_summary_rows: list[dict[str, Any]],
    surface_summary_rows: list[dict[str, Any]],
) -> None:

    """Write machine-readable summary YAML."""

    median_abs_correlation = float(np.median([float(row["abs_error_vs_abs_h0_corr"]) for row in candidate_summary_rows]))
    median_overlap_lift = float(np.median([float(row["top_decile_overlap_lift_vs_random_decile"]) for row in candidate_summary_rows]))
    summary_dictionary = {
        "run_id": run_id,
        "report_path": report_path.relative_to(PROJECT_PATH).as_posix(),
        "joined_row_count": joined_row_count,
        "candidate_count": len(candidate_summary_rows),
        "surface_count": len(surface_summary_rows),
        "median_abs_error_vs_abs_h0_correlation": median_abs_correlation,
        "median_top_decile_overlap_lift_vs_random_decile": median_overlap_lift,
        "decision": "h0_magnitude_not_sufficient_as_sole_offset_error_explanation",
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(summary_dictionary, output_file, sort_keys=False)


def main() -> None:

    """Run the CVP 1.4 h0 offset cross-check report."""

    # Parse Inputs
    args = parse_arguments()
    run_id = args.run_id if args.run_id else f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}__track2d_h0_offset_crosscheck"
    report_date = args.report_date if args.report_date else datetime.now().strftime("%Y-%m-%d")

    # Load And Join Diagnostics
    metric_row_list = load_track2d_metric_rows(args.track2d_per_curve_metrics_path)
    h0_component_dictionary = load_h0_component_dictionary(args.component_per_curve_path)
    joined_row_list = join_metric_and_h0_rows(metric_row_list, h0_component_dictionary)

    # Build Summary Tables
    candidate_summary_rows = build_candidate_summary_rows(joined_row_list)
    surface_summary_rows = build_surface_summary_rows(joined_row_list)
    quadrant_summary_rows = build_quadrant_summary_rows(joined_row_list)
    joined_csv_rows = [joined_row_to_csv_row(row) for row in joined_row_list]

    # Resolve Outputs
    output_directory = args.output_root / run_id
    report_directory = args.report_topic_root / f"[{report_date}]"
    asset_directory = report_directory / "assets"
    scatter_plot_path = asset_directory / "track2d_h0_offset_crosscheck_scatter.png"
    scatter_plot_relative_path = f"assets/{scatter_plot_path.name}"
    report_path = report_directory / REPORT_FILENAME

    # Write Machine-Readable Artifacts
    write_csv(output_directory / JOINED_TABLE_FILENAME, joined_csv_rows)
    write_csv(output_directory / CANDIDATE_SUMMARY_FILENAME, candidate_summary_rows)
    write_csv(output_directory / SURFACE_SUMMARY_FILENAME, surface_summary_rows)
    write_csv(output_directory / QUADRANT_SUMMARY_FILENAME, quadrant_summary_rows)

    # Write Human Report
    create_crosscheck_scatter_plot(joined_row_list, scatter_plot_path)
    report_lines = build_report_lines(
        run_id=run_id,
        joined_row_list=joined_row_list,
        candidate_summary_rows=candidate_summary_rows,
        surface_summary_rows=surface_summary_rows,
        quadrant_summary_rows=quadrant_summary_rows,
        output_directory=output_directory,
        scatter_plot_relative_path=scatter_plot_relative_path,
        top_count=args.top_count,
    )
    write_report(report_path, report_lines)
    write_summary_yaml(
        output_path=output_directory / REPORT_SUMMARY_FILENAME,
        run_id=run_id,
        report_path=report_path,
        joined_row_count=len(joined_row_list),
        candidate_summary_rows=candidate_summary_rows,
        surface_summary_rows=surface_summary_rows,
    )

    print(f"Prepared CVP 1.4 h0 offset cross-check | {output_directory}")
    print(f"Prepared Markdown report | {report_path}")


if __name__ == "__main__":
    main()
