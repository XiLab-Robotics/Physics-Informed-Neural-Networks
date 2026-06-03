"""Build Track 2E offset-predictability feasibility diagnostics."""

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
from statistics import mean, median, pstdev
from typing import Any

# Import Scientific Python Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.training import shared_training_infrastructure

DEFAULT_TRACK2D_OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2d_mean_offset_full_matrix_audit"
    / "2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit"
)
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2e_offset_predictability_feasibility"
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "offset_predictability_feasibility"
)

REPORT_FILENAME = "track2e_offset_predictability_feasibility.md"
SUMMARY_FILENAME = "track2e_offset_predictability_feasibility_summary.yaml"
CANDIDATE_FEASIBILITY_FILENAME = "track2e_candidate_feasibility_summary.csv"
SURFACE_RECOMMENDATION_FILENAME = "track2e_surface_intervention_recommendation.csv"
CONDITION_STABILITY_FILENAME = "track2e_condition_offset_stability.csv"

TRACK2D_PER_CURVE_FILENAME = "track2d_per_curve_metrics.csv"
TRACK2D_CANDIDATE_SUMMARY_FILENAME = "track2d_candidate_summary.csv"


@dataclass(frozen=True)
class PerCurveMetric:

    """One imported Track 2D per-curve diagnostic row."""

    candidate_id: str
    candidate_family: str
    candidate_kind: str
    candidate_source_label: str
    candidate_surface: str
    direction_label: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    raw_mae_deg: float
    centered_mae_deg: float
    signed_offset_error_deg: float
    absolute_offset_error_deg: float
    centered_mae_improvement_pct: float
    peak_to_peak_error_pct: float
    mean_harmonic_amplitude_error_pct: float
    mean_harmonic_phase_error_deg: float


@dataclass(frozen=True)
class CandidateTrack2DSummary:

    """One imported Track 2D candidate summary row."""

    rank: int
    candidate_id: str
    candidate_family: str
    candidate_kind: str
    candidate_source_label: str
    candidate_surface: str
    curve_count: int
    mean_raw_mae_deg: float
    mean_centered_mae_deg: float
    mean_absolute_offset_error_deg: float
    mean_centered_mae_improvement_pct: float
    mean_peak_to_peak_error_pct: float
    mean_harmonic_amplitude_error_pct: float
    mean_harmonic_phase_error_deg: float
    centered_shape_ratio: float
    offset_share_ratio: float
    diagnostic_label: str
    diagnostic_score: float


@dataclass(frozen=True)
class GroupCorrectionResult:

    """Diagnostic result for one causal grouping baseline."""

    group_name: str
    group_count: int
    corrected_mae_upper_bound_deg: float
    correction_gain_pct: float
    residual_offset_mae_deg: float
    offset_explainable_share_pct: float


@dataclass(frozen=True)
class CandidateFeasibilitySummary:

    """Track 2E feasibility decision for one candidate."""

    rank: int
    candidate_id: str
    candidate_family: str
    candidate_surface: str
    curve_count: int
    track2d_label: str
    recommended_intervention: str
    feasibility_label: str
    mean_raw_mae_deg: float
    mean_centered_mae_deg: float
    mean_absolute_offset_error_deg: float
    offset_share_ratio: float
    centered_shape_ratio: float
    best_group_name: str
    best_group_count: int
    corrected_mae_upper_bound_deg: float
    correction_gain_pct: float
    offset_explainable_share_pct: float
    offset_signed_std_deg: float
    offset_signed_median_deg: float
    offset_direction_balance_deg: float
    mean_peak_to_peak_error_pct: float
    mean_harmonic_phase_error_deg: float

    def ranking_key(self) -> tuple[float, float, float, str]:

        """Return deterministic feasibility ordering."""

        return (
            intervention_priority(self.recommended_intervention),
            -self.correction_gain_pct,
            self.mean_centered_mae_deg,
            self.candidate_id,
        )

    def to_csv_row(self) -> dict[str, Any]:

        """Return a stable CSV row."""

        return {
            "rank": self.rank,
            "candidate_id": self.candidate_id,
            "candidate_family": self.candidate_family,
            "candidate_surface": self.candidate_surface,
            "curve_count": self.curve_count,
            "track2d_label": self.track2d_label,
            "recommended_intervention": self.recommended_intervention,
            "feasibility_label": self.feasibility_label,
            "mean_raw_mae_deg": format_float(self.mean_raw_mae_deg),
            "mean_centered_mae_deg": format_float(self.mean_centered_mae_deg),
            "mean_absolute_offset_error_deg": format_float(self.mean_absolute_offset_error_deg),
            "offset_share_ratio": format_float(self.offset_share_ratio),
            "centered_shape_ratio": format_float(self.centered_shape_ratio),
            "best_group_name": self.best_group_name,
            "best_group_count": self.best_group_count,
            "corrected_mae_upper_bound_deg": format_float(self.corrected_mae_upper_bound_deg),
            "correction_gain_pct": format_float(self.correction_gain_pct),
            "offset_explainable_share_pct": format_float(self.offset_explainable_share_pct),
            "offset_signed_std_deg": format_float(self.offset_signed_std_deg),
            "offset_signed_median_deg": format_float(self.offset_signed_median_deg),
            "offset_direction_balance_deg": format_float(self.offset_direction_balance_deg),
            "mean_peak_to_peak_error_pct": format_float(self.mean_peak_to_peak_error_pct),
            "mean_harmonic_phase_error_deg": format_float(self.mean_harmonic_phase_error_deg),
        }


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Generate Track 2E offset-predictability feasibility diagnostics "
            "from completed Track 2D artifacts without training models."
        )
    )
    argument_parser.add_argument(
        "--track2d-output-directory",
        type=Path,
        default=DEFAULT_TRACK2D_OUTPUT_DIRECTORY,
        help="Track 2D artifact directory containing per-curve and candidate summary CSV files.",
    )
    argument_parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root for generated Track 2E validation artifacts.",
    )
    argument_parser.add_argument(
        "--report-topic-root",
        type=Path,
        default=DEFAULT_REPORT_TOPIC_ROOT,
        help="Root for the dated Track 2E Markdown report bundle.",
    )
    argument_parser.add_argument(
        "--report-date",
        type=str,
        default=None,
        help="Optional report date folder in YYYY-MM-DD form.",
    )
    argument_parser.add_argument(
        "--candidate-id",
        dest="candidate_id_list",
        action="append",
        default=None,
        help="Optional candidate id filter. May be provided multiple times.",
    )
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def format_float(value: float) -> str:

    """Format a float for stable CSV and Markdown output."""

    if not math.isfinite(value):
        return "nan"
    return f"{value:.6f}"


def parse_float_cell(value: Any) -> float:

    """Parse a CSV float cell."""

    text_value = str(value or "").strip()
    if not text_value or text_value.lower() == "nan":
        return math.nan
    return float(text_value)


def parse_int_cell(value: Any) -> int:

    """Parse a CSV integer cell."""

    text_value = str(value or "").strip()
    if not text_value:
        return 0
    return int(float(text_value))


def safe_mean(value_list: list[float]) -> float:

    """Return finite mean or NaN."""

    finite_value_list = [value for value in value_list if math.isfinite(value)]
    return mean(finite_value_list) if finite_value_list else math.nan


def safe_median(value_list: list[float]) -> float:

    """Return finite median or NaN."""

    finite_value_list = [value for value in value_list if math.isfinite(value)]
    return median(finite_value_list) if finite_value_list else math.nan


def safe_pstdev(value_list: list[float]) -> float:

    """Return finite population standard deviation or NaN."""

    finite_value_list = [value for value in value_list if math.isfinite(value)]
    if len(finite_value_list) <= 1:
        return 0.0
    return pstdev(finite_value_list)


def safe_divide(numerator: float, denominator: float) -> float:

    """Divide with finite guards."""

    if not math.isfinite(numerator) or not math.isfinite(denominator) or abs(denominator) < 1.0e-12:
        return math.nan
    return numerator / denominator


def relative_path(path: Path) -> str:

    """Return a project-relative path when possible."""

    try:
        return str(path.relative_to(PROJECT_PATH))
    except ValueError:
        return str(path)


def resolve_timestamped_output_paths(
    output_root: Path,
    report_topic_root: Path,
    report_date: str | None,
) -> tuple[str, Path, Path]:

    """Resolve run, output, and report paths."""

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    run_instance_id = f"{timestamp}__track2e_offset_predictability_feasibility"
    output_directory = output_root / run_instance_id
    report_folder_name = f"[{report_date or datetime.now().strftime('%Y-%m-%d')}]"
    report_directory = report_topic_root / report_folder_name
    output_directory.mkdir(parents=True, exist_ok=True)
    report_directory.mkdir(parents=True, exist_ok=True)
    return run_instance_id, output_directory, report_directory


def load_csv_rows(csv_path: Path) -> list[dict[str, str]]:

    """Load CSV rows."""

    with csv_path.open("r", encoding="utf-8", newline="") as csv_file:
        return [dict(row) for row in csv.DictReader(csv_file)]


def write_csv(csv_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write a CSV file with stable newline behavior."""

    field_name_list = list(row_list[0].keys()) if row_list else []
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_list, lineterminator="\n")
        writer.writeheader()
        for row in row_list:
            writer.writerow(row)


def load_per_curve_metric_list(track2d_output_directory: Path) -> list[PerCurveMetric]:

    """Load Track 2D per-curve metrics."""

    csv_path = track2d_output_directory / TRACK2D_PER_CURVE_FILENAME
    metric_list: list[PerCurveMetric] = []
    for row in load_csv_rows(csv_path):
        metric_list.append(
            PerCurveMetric(
                candidate_id=str(row["candidate_id"]),
                candidate_family=str(row["candidate_family"]),
                candidate_kind=str(row["candidate_kind"]),
                candidate_source_label=str(row["candidate_source_label"]),
                candidate_surface=str(row["candidate_surface"]),
                direction_label=str(row["direction_label"]),
                speed_rpm=parse_float_cell(row["speed_rpm"]),
                torque_nm=parse_float_cell(row["torque_nm"]),
                oil_temperature_deg=parse_float_cell(row["oil_temperature_deg"]),
                raw_mae_deg=parse_float_cell(row["raw_mae_deg"]),
                centered_mae_deg=parse_float_cell(row["centered_mae_deg"]),
                signed_offset_error_deg=parse_float_cell(row["signed_offset_error_deg"]),
                absolute_offset_error_deg=parse_float_cell(row["absolute_offset_error_deg"]),
                centered_mae_improvement_pct=parse_float_cell(row["centered_mae_improvement_pct"]),
                peak_to_peak_error_pct=parse_float_cell(row["peak_to_peak_error_pct"]),
                mean_harmonic_amplitude_error_pct=parse_float_cell(row["mean_harmonic_amplitude_error_pct"]),
                mean_harmonic_phase_error_deg=parse_float_cell(row["mean_harmonic_phase_error_deg"]),
            )
        )
    return metric_list


def load_candidate_summary_map(track2d_output_directory: Path) -> dict[str, CandidateTrack2DSummary]:

    """Load Track 2D candidate summaries."""

    csv_path = track2d_output_directory / TRACK2D_CANDIDATE_SUMMARY_FILENAME
    summary_map: dict[str, CandidateTrack2DSummary] = {}
    for row in load_csv_rows(csv_path):
        summary = CandidateTrack2DSummary(
            rank=parse_int_cell(row["rank"]),
            candidate_id=str(row["candidate_id"]),
            candidate_family=str(row["candidate_family"]),
            candidate_kind=str(row["candidate_kind"]),
            candidate_source_label=str(row["candidate_source_label"]),
            candidate_surface=str(row["candidate_surface"]),
            curve_count=parse_int_cell(row["curve_count"]),
            mean_raw_mae_deg=parse_float_cell(row["mean_raw_mae_deg"]),
            mean_centered_mae_deg=parse_float_cell(row["mean_centered_mae_deg"]),
            mean_absolute_offset_error_deg=parse_float_cell(row["mean_absolute_offset_error_deg"]),
            mean_centered_mae_improvement_pct=parse_float_cell(row["mean_centered_mae_improvement_pct"]),
            mean_peak_to_peak_error_pct=parse_float_cell(row["mean_peak_to_peak_error_pct"]),
            mean_harmonic_amplitude_error_pct=parse_float_cell(row["mean_harmonic_amplitude_error_pct"]),
            mean_harmonic_phase_error_deg=parse_float_cell(row["mean_harmonic_phase_error_deg"]),
            centered_shape_ratio=parse_float_cell(row["centered_shape_ratio"]),
            offset_share_ratio=parse_float_cell(row["offset_share_ratio"]),
            diagnostic_label=str(row["diagnostic_label"]),
            diagnostic_score=parse_float_cell(row["diagnostic_score"]),
        )
        summary_map[summary.candidate_id] = summary
    return summary_map


def build_group_key(metric: PerCurveMetric, group_name: str) -> str:

    """Return the causal grouping key for one metric row."""

    if group_name == "direction":
        return metric.direction_label
    if group_name == "speed":
        return f"{metric.speed_rpm:.0f}"
    if group_name == "torque":
        return f"{metric.torque_nm:.0f}"
    if group_name == "oil_temperature":
        return f"{metric.oil_temperature_deg:.0f}"
    if group_name == "direction_speed":
        return f"{metric.direction_label}|{metric.speed_rpm:.0f}"
    if group_name == "direction_torque":
        return f"{metric.direction_label}|{metric.torque_nm:.0f}"
    if group_name == "direction_oil_temperature":
        return f"{metric.direction_label}|{metric.oil_temperature_deg:.0f}"
    raise ValueError(f"Unsupported group name: {group_name}")


def compute_group_correction_result(
    group_name: str,
    metric_list: list[PerCurveMetric],
) -> GroupCorrectionResult:

    """Compute an upper-bound causal grouping correction diagnostic."""

    grouped_metric_map: dict[str, list[PerCurveMetric]] = defaultdict(list)
    for metric in metric_list:
        grouped_metric_map[build_group_key(metric, group_name)].append(metric)

    group_mean_offset_map = {
        group_key: safe_mean([metric.signed_offset_error_deg for metric in group_metric_list])
        for group_key, group_metric_list in grouped_metric_map.items()
    }

    corrected_mae_estimate_list: list[float] = []
    residual_offset_abs_list: list[float] = []
    for metric in metric_list:
        group_mean_offset = group_mean_offset_map[build_group_key(metric, group_name)]
        residual_offset = metric.signed_offset_error_deg - group_mean_offset
        residual_offset_abs = abs(residual_offset)
        residual_offset_abs_list.append(residual_offset_abs)
        corrected_mae_estimate_list.append(metric.centered_mae_deg + residual_offset_abs)

    raw_mae = safe_mean([metric.raw_mae_deg for metric in metric_list])
    absolute_offset = safe_mean([metric.absolute_offset_error_deg for metric in metric_list])
    corrected_mae = safe_mean(corrected_mae_estimate_list)
    residual_offset_mae = safe_mean(residual_offset_abs_list)
    correction_gain_pct = 100.0 * safe_divide(raw_mae - corrected_mae, raw_mae)
    offset_explainable_share_pct = 100.0 * safe_divide(absolute_offset - residual_offset_mae, absolute_offset)

    return GroupCorrectionResult(
        group_name=group_name,
        group_count=len(grouped_metric_map),
        corrected_mae_upper_bound_deg=corrected_mae,
        correction_gain_pct=max(0.0, correction_gain_pct if math.isfinite(correction_gain_pct) else 0.0),
        residual_offset_mae_deg=residual_offset_mae,
        offset_explainable_share_pct=max(
            0.0,
            offset_explainable_share_pct if math.isfinite(offset_explainable_share_pct) else 0.0,
        ),
    )


def compute_offset_direction_balance(metric_list: list[PerCurveMetric]) -> float:

    """Compute signed-offset distance between forward and backward rows."""

    direction_map: dict[str, list[float]] = defaultdict(list)
    for metric in metric_list:
        direction_map[metric.direction_label].append(metric.signed_offset_error_deg)
    if "forward" not in direction_map or "backward" not in direction_map:
        return 0.0
    return abs(safe_mean(direction_map["forward"]) - safe_mean(direction_map["backward"]))


def choose_recommended_intervention(
    track2d_summary: CandidateTrack2DSummary,
    best_group_result: GroupCorrectionResult,
    offset_signed_std_deg: float,
) -> tuple[str, str]:

    """Choose the next intervention label for one candidate."""

    offset_share = track2d_summary.offset_share_ratio
    shape_ratio = track2d_summary.centered_shape_ratio
    correction_gain = best_group_result.correction_gain_pct
    explainable_share = best_group_result.offset_explainable_share_pct
    normalized_offset_std = safe_divide(offset_signed_std_deg, track2d_summary.mean_absolute_offset_error_deg)
    stable_offset = math.isfinite(normalized_offset_std) and normalized_offset_std <= 1.25

    if offset_share >= 0.70 and correction_gain >= 40.0 and explainable_share >= 45.0 and stable_offset:
        return (
            "sequential_offset_model",
            "offset-dominant and condition-predictable enough for a causal residual-offset probe",
        )
    if offset_share >= 0.65 and correction_gain >= 25.0 and explainable_share >= 30.0:
        return (
            "posthoc_offset_baseline",
            "offset-dominant with a useful conservative causal aggregate baseline",
        )
    if offset_share >= 0.50 and shape_ratio <= 0.65:
        return (
            "multi_head_shape_offset",
            "offset and centered shape are both material and should be separated",
        )
    if "offset" in track2d_summary.diagnostic_label and correction_gain < 20.0:
        return (
            "loss_reweighting",
            "offset is visible but the simple causal grouping baseline is weak",
        )
    if shape_ratio >= 0.70 or track2d_summary.mean_peak_to_peak_error_pct >= 12.0:
        return (
            "not_offset_first",
            "centered shape, amplitude, or phase error remains the dominant limitation",
        )
    return (
        "loss_reweighting",
        "mixed behavior suggests a raw plus centered-shape plus offset loss before new families",
    )


def intervention_priority(intervention: str) -> float:

    """Return sortable intervention priority."""

    priority_map = {
        "sequential_offset_model": 0.0,
        "posthoc_offset_baseline": 1.0,
        "multi_head_shape_offset": 2.0,
        "loss_reweighting": 3.0,
        "not_offset_first": 4.0,
    }
    return priority_map.get(intervention, 9.0)


def build_candidate_feasibility_summary(
    candidate_id: str,
    metric_list: list[PerCurveMetric],
    track2d_summary: CandidateTrack2DSummary,
) -> CandidateFeasibilitySummary:

    """Build one candidate feasibility summary."""

    group_name_list = [
        "direction",
        "speed",
        "torque",
        "oil_temperature",
        "direction_speed",
        "direction_torque",
        "direction_oil_temperature",
    ]
    group_result_list = [
        compute_group_correction_result(group_name, metric_list)
        for group_name in group_name_list
    ]
    best_group_result = sorted(
        group_result_list,
        key=lambda result: (
            -result.correction_gain_pct,
            -result.offset_explainable_share_pct,
            result.group_count,
            result.group_name,
        ),
    )[0]
    offset_value_list = [metric.signed_offset_error_deg for metric in metric_list]
    intervention, feasibility_label = choose_recommended_intervention(
        track2d_summary,
        best_group_result,
        safe_pstdev(offset_value_list),
    )

    return CandidateFeasibilitySummary(
        rank=0,
        candidate_id=candidate_id,
        candidate_family=track2d_summary.candidate_family,
        candidate_surface=track2d_summary.candidate_surface,
        curve_count=len(metric_list),
        track2d_label=track2d_summary.diagnostic_label,
        recommended_intervention=intervention,
        feasibility_label=feasibility_label,
        mean_raw_mae_deg=track2d_summary.mean_raw_mae_deg,
        mean_centered_mae_deg=track2d_summary.mean_centered_mae_deg,
        mean_absolute_offset_error_deg=track2d_summary.mean_absolute_offset_error_deg,
        offset_share_ratio=track2d_summary.offset_share_ratio,
        centered_shape_ratio=track2d_summary.centered_shape_ratio,
        best_group_name=best_group_result.group_name,
        best_group_count=best_group_result.group_count,
        corrected_mae_upper_bound_deg=best_group_result.corrected_mae_upper_bound_deg,
        correction_gain_pct=best_group_result.correction_gain_pct,
        offset_explainable_share_pct=best_group_result.offset_explainable_share_pct,
        offset_signed_std_deg=safe_pstdev(offset_value_list),
        offset_signed_median_deg=safe_median(offset_value_list),
        offset_direction_balance_deg=compute_offset_direction_balance(metric_list),
        mean_peak_to_peak_error_pct=track2d_summary.mean_peak_to_peak_error_pct,
        mean_harmonic_phase_error_deg=track2d_summary.mean_harmonic_phase_error_deg,
    )


def rerank_candidate_feasibility_list(
    feasibility_list: list[CandidateFeasibilitySummary],
) -> list[CandidateFeasibilitySummary]:

    """Rank candidate feasibility summaries."""

    ranked_list: list[CandidateFeasibilitySummary] = []
    for rank, summary in enumerate(sorted(feasibility_list, key=lambda item: item.ranking_key()), start=1):
        ranked_list.append(
            CandidateFeasibilitySummary(
                rank=rank,
                candidate_id=summary.candidate_id,
                candidate_family=summary.candidate_family,
                candidate_surface=summary.candidate_surface,
                curve_count=summary.curve_count,
                track2d_label=summary.track2d_label,
                recommended_intervention=summary.recommended_intervention,
                feasibility_label=summary.feasibility_label,
                mean_raw_mae_deg=summary.mean_raw_mae_deg,
                mean_centered_mae_deg=summary.mean_centered_mae_deg,
                mean_absolute_offset_error_deg=summary.mean_absolute_offset_error_deg,
                offset_share_ratio=summary.offset_share_ratio,
                centered_shape_ratio=summary.centered_shape_ratio,
                best_group_name=summary.best_group_name,
                best_group_count=summary.best_group_count,
                corrected_mae_upper_bound_deg=summary.corrected_mae_upper_bound_deg,
                correction_gain_pct=summary.correction_gain_pct,
                offset_explainable_share_pct=summary.offset_explainable_share_pct,
                offset_signed_std_deg=summary.offset_signed_std_deg,
                offset_signed_median_deg=summary.offset_signed_median_deg,
                offset_direction_balance_deg=summary.offset_direction_balance_deg,
                mean_peak_to_peak_error_pct=summary.mean_peak_to_peak_error_pct,
                mean_harmonic_phase_error_deg=summary.mean_harmonic_phase_error_deg,
            )
        )
    return ranked_list


def build_feasibility_summary_list(
    per_curve_metric_list: list[PerCurveMetric],
    track2d_summary_map: dict[str, CandidateTrack2DSummary],
    candidate_id_filter: set[str] | None,
) -> list[CandidateFeasibilitySummary]:

    """Build Track 2E candidate feasibility summaries."""

    candidate_metric_map: dict[str, list[PerCurveMetric]] = defaultdict(list)
    for metric in per_curve_metric_list:
        if candidate_id_filter is not None and metric.candidate_id not in candidate_id_filter:
            continue
        candidate_metric_map[metric.candidate_id].append(metric)

    feasibility_list: list[CandidateFeasibilitySummary] = []
    for candidate_id, metric_list in sorted(candidate_metric_map.items()):
        track2d_summary = track2d_summary_map.get(candidate_id)
        if track2d_summary is None:
            continue
        feasibility_list.append(build_candidate_feasibility_summary(candidate_id, metric_list, track2d_summary))
    return rerank_candidate_feasibility_list(feasibility_list)


def build_surface_recommendation_list(
    feasibility_list: list[CandidateFeasibilitySummary],
) -> list[CandidateFeasibilitySummary]:

    """Return one recommended candidate per surface."""

    surface_map: dict[str, list[CandidateFeasibilitySummary]] = defaultdict(list)
    for summary in feasibility_list:
        surface_map[summary.candidate_surface].append(summary)

    surface_recommendation_list: list[CandidateFeasibilitySummary] = []
    for surface in sorted(surface_map):
        surface_recommendation_list.append(sorted(surface_map[surface], key=lambda item: item.ranking_key())[0])
    return surface_recommendation_list


def build_condition_stability_rows(per_curve_metric_list: list[PerCurveMetric]) -> list[dict[str, Any]]:

    """Build condition-level offset stability rows."""

    grouped_metric_map: dict[tuple[str, str, str, str], list[PerCurveMetric]] = defaultdict(list)
    for metric in per_curve_metric_list:
        grouping_list = [
            ("direction", metric.direction_label),
            ("speed_rpm", f"{metric.speed_rpm:.0f}"),
            ("torque_nm", f"{metric.torque_nm:.0f}"),
            ("oil_temperature_deg", f"{metric.oil_temperature_deg:.0f}"),
        ]
        for group_type, group_value in grouping_list:
            grouped_metric_map[
                (
                    metric.candidate_id,
                    metric.candidate_surface,
                    group_type,
                    group_value,
                )
            ].append(metric)

    row_list: list[dict[str, Any]] = []
    for grouping_key, metric_list in sorted(grouped_metric_map.items()):
        candidate_id, surface, group_type, group_value = grouping_key
        signed_offset_list = [metric.signed_offset_error_deg for metric in metric_list]
        absolute_offset_list = [metric.absolute_offset_error_deg for metric in metric_list]
        row_list.append(
            {
                "candidate_id": candidate_id,
                "candidate_surface": surface,
                "group_type": group_type,
                "group_value": group_value,
                "curve_count": len(metric_list),
                "mean_signed_offset_error_deg": format_float(safe_mean(signed_offset_list)),
                "median_signed_offset_error_deg": format_float(safe_median(signed_offset_list)),
                "std_signed_offset_error_deg": format_float(safe_pstdev(signed_offset_list)),
                "mean_absolute_offset_error_deg": format_float(safe_mean(absolute_offset_list)),
                "mean_raw_mae_deg": format_float(safe_mean([metric.raw_mae_deg for metric in metric_list])),
                "mean_centered_mae_deg": format_float(safe_mean([metric.centered_mae_deg for metric in metric_list])),
            }
        )
    return row_list


def markdown_table(header_list: list[str], row_list: list[list[str]]) -> list[str]:

    """Build a Markdown table."""

    line_list = [
        "| " + " | ".join(header_list) + " |",
        "| " + " | ".join(["---"] * len(header_list)) + " |",
    ]
    for row in row_list:
        line_list.append("| " + " | ".join(row) + " |")
    return line_list


def compact_label(label: str) -> str:

    """Compact long labels for table cells."""

    return label.replace("centered-shape", "shape").replace("-limited", "").replace("_", " ")


def compact_intervention(intervention: str) -> str:

    """Return a compact intervention label for report tables."""

    label_map = {
        "sequential_offset_model": "seq",
        "posthoc_offset_baseline": "post",
        "multi_head_shape_offset": "head",
        "loss_reweighting": "loss",
        "not_offset_first": "shape",
    }
    return label_map.get(intervention, intervention)


def compact_group_name(group_name: str) -> str:

    """Return a compact causal group label for report tables."""

    label_map = {
        "direction": "dir",
        "speed": "speed",
        "torque": "torque",
        "oil_temperature": "oil",
        "direction_speed": "dir_speed",
        "direction_torque": "dir_torque",
        "direction_oil_temperature": "dir_oil",
    }
    return label_map.get(group_name, group_name)


def append_feasibility_table(
    line_list: list[str],
    title: str,
    feasibility_list: list[CandidateFeasibilitySummary],
    limit: int,
) -> None:

    """Append a candidate feasibility table."""

    line_list.extend([f"## {title}", ""])
    row_list: list[list[str]] = []
    for summary in feasibility_list[:limit]:
        row_list.append(
            [
                str(summary.rank),
                f"`{summary.candidate_id}`",
                summary.candidate_surface,
                compact_intervention(summary.recommended_intervention),
                format_float(summary.mean_raw_mae_deg),
                format_float(summary.corrected_mae_upper_bound_deg),
                f"{summary.correction_gain_pct:.1f}",
                f"{summary.offset_explainable_share_pct:.1f}",
                compact_group_name(summary.best_group_name),
            ]
        )
    line_list.extend(
        markdown_table(
            [
                "Rank",
                "Candidate",
                "Surface",
                "Interv.",
                "Raw MAE",
                "Corr. MAE",
                "Gain [%]",
                "Explain [%]",
                "Best Group",
            ],
            row_list,
        )
    )
    line_list.append("")


def build_intervention_count_rows(feasibility_list: list[CandidateFeasibilitySummary]) -> list[list[str]]:

    """Build intervention count table rows."""

    count_map: dict[tuple[str, str], int] = defaultdict(int)
    for summary in feasibility_list:
        count_map[(summary.candidate_surface, summary.recommended_intervention)] += 1
    return [
        [surface, f"`{intervention}`", str(count)]
        for (surface, intervention), count in sorted(count_map.items())
    ]


def build_report_lines(
    run_instance_id: str,
    track2d_output_directory: Path,
    output_directory: Path,
    feasibility_list: list[CandidateFeasibilitySummary],
    surface_recommendation_list: list[CandidateFeasibilitySummary],
) -> list[str]:

    """Build the Markdown report body."""

    line_list = [
        "# Track 2E Offset Predictability Feasibility",
        "",
        "## Overview",
        "",
        (
            "This report consumes the completed `Track 2D` mean-offset artifacts "
            "and asks whether the vertical curve offset is predictable enough "
            "from causal condition information to justify an offset-aware next "
            "branch."
        ),
        "",
        "This is an analysis-only feasibility diagnostic. It does not train",
        "models, alter the dataset, update registries, or use future TE samples",
        "as model inputs.",
        "",
        f"- Run Instance: `{run_instance_id}`",
        f"- Track 2D Source: `{relative_path(track2d_output_directory)}`",
        f"- Output Directory: `{relative_path(output_directory)}`",
        f"- Candidate Count: `{len(feasibility_list)}`",
        "",
        "## Method",
        "",
        "- candidate raw, centered-shape, and offset metrics are imported from",
        "  `Track 2D`;",
        "- candidate offsets are summarized by causal groups: direction, speed,",
        "  torque, oil temperature, and their direction-aware combinations;",
        "- exact full-condition groups such as speed plus torque plus oil",
        "  temperature are intentionally excluded from the recommendation",
        "  ranking because they can collapse to one evaluated curve and",
        "  overstate deployable offset predictability;",
        "- the corrected `MAE` is an upper-bound diagnostic approximation:",
        "  centered `MAE` plus the remaining absolute offset after subtracting a",
        "  group mean offset;",
        "- the correction baseline is not a production model and is not a valid",
        "  registry promotion rule;",
        "- `Fw`, `Bw`, and `global` are interpreted as parallel branches.",
        "",
        "## Intervention Counts",
        "",
    ]
    line_list.extend(markdown_table(["Surface", "Intervention", "Candidate Count"], build_intervention_count_rows(feasibility_list)))
    line_list.append("")

    append_feasibility_table(
        line_list,
        "Surface Recommendations",
        surface_recommendation_list,
        len(surface_recommendation_list),
    )
    append_feasibility_table(line_list, "Track 2E Feasibility Ranking", feasibility_list, 20)
    append_feasibility_table(
        line_list,
        "Largest Conservative Offset-Correction Gains",
        sorted(feasibility_list, key=lambda summary: summary.correction_gain_pct, reverse=True),
        15,
    )

    line_list.extend(
        [
            "## Decision Interpretation",
            "",
            (
                "`sequential_offset_model` means the offset component appears "
                "large and condition-predictable enough to justify a future "
                "causal residual-offset probe. `posthoc_offset_baseline` means "
                "a simple causal aggregate calibration is worth keeping as a "
                "benchmark before training a second model."
            ),
            "",
            (
                "`multi_head_shape_offset` means the next model should split "
                "centered waveform shape from offset / low-frequency behavior. "
                "`loss_reweighting` means the next safer step is a raw plus "
                "centered-shape plus offset loss. `not_offset_first` means "
                "amplitude, phase, or centered shape should stay ahead of offset "
                "correction."
            ),
            "",
            "## Runtime Input Boundary",
            "",
            (
                "The causal grouping baselines use only direction and operating "
                "condition metadata already present in the Track 2 payload. The "
                "analysis never gives a model the future TE curve. Any learned "
                "offset model still requires a later technical document and "
                "campaign plan before it can become a training branch."
            ),
            "",
            "## Machine-Readable Artifacts",
            "",
            f"- `{relative_path(output_directory / CANDIDATE_FEASIBILITY_FILENAME)}`",
            f"- `{relative_path(output_directory / SURFACE_RECOMMENDATION_FILENAME)}`",
            f"- `{relative_path(output_directory / CONDITION_STABILITY_FILENAME)}`",
            f"- `{relative_path(output_directory / SUMMARY_FILENAME)}`",
            "",
        ]
    )
    return line_list


def write_summary_yaml(
    summary_path: Path,
    run_instance_id: str,
    track2d_output_directory: Path,
    output_directory: Path,
    report_path: Path,
    feasibility_list: list[CandidateFeasibilitySummary],
    surface_recommendation_list: list[CandidateFeasibilitySummary],
) -> None:

    """Write a machine-readable Track 2E summary."""

    summary_payload = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "track2d_output_directory": relative_path(track2d_output_directory),
        "output_directory": relative_path(output_directory),
        "report_path": relative_path(report_path),
        "causal_input_contract": (
            "current point, optional short causal history, or derived causal features only"
        ),
        "registry_promotion": "not_automatic",
        "surface_recommendation_list": [
            summary.to_csv_row()
            for summary in surface_recommendation_list
        ],
        "candidate_feasibility_list": [
            summary.to_csv_row()
            for summary in feasibility_list
        ],
    }
    with summary_path.open("w", encoding="utf-8") as summary_file:
        yaml.safe_dump(summary_payload, summary_file, sort_keys=False, allow_unicode=False)


def run_track2e_offset_predictability_feasibility(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the Track 2E feasibility workflow."""

    track2d_output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(
        arguments.track2d_output_directory
    )
    output_root = shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.output_root)
    report_topic_root = shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.report_topic_root)

    run_instance_id, output_directory, report_directory = resolve_timestamped_output_paths(
        output_root=output_root,
        report_topic_root=report_topic_root,
        report_date=arguments.report_date,
    )
    report_path = report_directory / REPORT_FILENAME

    candidate_id_filter = set(arguments.candidate_id_list) if arguments.candidate_id_list else None
    per_curve_metric_list = load_per_curve_metric_list(track2d_output_directory)
    candidate_summary_map = load_candidate_summary_map(track2d_output_directory)
    feasibility_list = build_feasibility_summary_list(
        per_curve_metric_list,
        candidate_summary_map,
        candidate_id_filter,
    )
    surface_recommendation_list = build_surface_recommendation_list(feasibility_list)
    condition_stability_row_list = build_condition_stability_rows(per_curve_metric_list)

    write_csv(
        output_directory / CANDIDATE_FEASIBILITY_FILENAME,
        [summary.to_csv_row() for summary in feasibility_list],
    )
    write_csv(
        output_directory / SURFACE_RECOMMENDATION_FILENAME,
        [summary.to_csv_row() for summary in surface_recommendation_list],
    )
    write_csv(output_directory / CONDITION_STABILITY_FILENAME, condition_stability_row_list)
    write_summary_yaml(
        summary_path=output_directory / SUMMARY_FILENAME,
        run_instance_id=run_instance_id,
        track2d_output_directory=track2d_output_directory,
        output_directory=output_directory,
        report_path=report_path,
        feasibility_list=feasibility_list,
        surface_recommendation_list=surface_recommendation_list,
    )

    report_lines = build_report_lines(
        run_instance_id=run_instance_id,
        track2d_output_directory=track2d_output_directory,
        output_directory=output_directory,
        feasibility_list=feasibility_list,
        surface_recommendation_list=surface_recommendation_list,
    )
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    return {
        "run_instance_id": run_instance_id,
        "output_directory": relative_path(output_directory),
        "report_path": relative_path(report_path),
        "candidate_count": len(feasibility_list),
    }


def main() -> None:

    """Run the Track 2E diagnostics workflow."""

    summary = run_track2e_offset_predictability_feasibility(parse_command_line_arguments())
    print(f"[DONE] Track 2E report: {summary['report_path']}")
    print(f"[DONE] Track 2E artifacts: {summary['output_directory']}")


if __name__ == "__main__":
    main()
