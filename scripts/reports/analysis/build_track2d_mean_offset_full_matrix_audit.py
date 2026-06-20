"""Build CVP 1.4 mean-offset full-matrix diagnostics."""

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
from statistics import mean, pstdev
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
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)
from scripts.reports.analysis import build_track2_curve_payload_diagnostics_report as track2c_diagnostics
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "full_track2_matrix_template.yaml"
)
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2d_mean_offset_full_matrix_audit"
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "mean_offset_full_matrix_audit"
)
DEFAULT_HARMONIC_ORDER_LIST = [1, 3, 39, 40, 78, 81, 156, 162, 240]

REPORT_FILENAME = "track2d_mean_offset_full_matrix_audit.md"
SUMMARY_FILENAME = "track2d_mean_offset_full_matrix_audit_summary.yaml"
PER_CURVE_METRICS_FILENAME = "track2d_per_curve_metrics.csv"
CANDIDATE_SUMMARY_FILENAME = "track2d_candidate_summary.csv"
SURFACE_LEADERBOARD_FILENAME = "track2d_surface_leaderboard.csv"
CONDITION_STRATIFIED_FILENAME = "track2d_condition_stratified_summary.csv"


@dataclass(frozen=True)
class Track2DPerCurveMetric:

    """One full-matrix CVP 1.4 diagnostic row."""

    candidate_id: str
    candidate_family: str
    candidate_kind: str
    candidate_source_label: str
    candidate_surface: str
    direction_label: str
    source_file_path: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    raw_mae_deg: float
    raw_rmse_deg: float
    mean_percentage_error_pct: float
    truth_mean_deg: float
    predicted_mean_deg: float
    signed_offset_error_deg: float
    absolute_offset_error_deg: float
    centered_mae_deg: float
    centered_rmse_deg: float
    centered_mae_improvement_deg: float
    centered_mae_improvement_pct: float
    truth_peak_to_peak_deg: float
    predicted_peak_to_peak_deg: float
    peak_to_peak_error_pct: float
    residual_peak_to_peak_pct: float
    derivative_rmse_deg_per_deg: float
    mean_harmonic_amplitude_error_pct: float
    mean_harmonic_phase_error_deg: float
    max_harmonic_amplitude_error_pct: float
    max_harmonic_phase_error_deg: float

    def to_csv_row(self) -> dict[str, Any]:

        """Return a stable CSV row."""

        return {
            "candidate_id": self.candidate_id,
            "candidate_family": self.candidate_family,
            "candidate_kind": self.candidate_kind,
            "candidate_source_label": self.candidate_source_label,
            "candidate_surface": self.candidate_surface,
            "direction_label": self.direction_label,
            "source_file_path": self.source_file_path,
            "speed_rpm": format_float(self.speed_rpm),
            "torque_nm": format_float(self.torque_nm),
            "oil_temperature_deg": format_float(self.oil_temperature_deg),
            "raw_mae_deg": format_float(self.raw_mae_deg),
            "raw_rmse_deg": format_float(self.raw_rmse_deg),
            "mean_percentage_error_pct": format_float(self.mean_percentage_error_pct),
            "truth_mean_deg": format_float(self.truth_mean_deg),
            "predicted_mean_deg": format_float(self.predicted_mean_deg),
            "signed_offset_error_deg": format_float(self.signed_offset_error_deg),
            "absolute_offset_error_deg": format_float(self.absolute_offset_error_deg),
            "centered_mae_deg": format_float(self.centered_mae_deg),
            "centered_rmse_deg": format_float(self.centered_rmse_deg),
            "centered_mae_improvement_deg": format_float(self.centered_mae_improvement_deg),
            "centered_mae_improvement_pct": format_float(self.centered_mae_improvement_pct),
            "truth_peak_to_peak_deg": format_float(self.truth_peak_to_peak_deg),
            "predicted_peak_to_peak_deg": format_float(self.predicted_peak_to_peak_deg),
            "peak_to_peak_error_pct": format_float(self.peak_to_peak_error_pct),
            "residual_peak_to_peak_pct": format_float(self.residual_peak_to_peak_pct),
            "derivative_rmse_deg_per_deg": format_float(self.derivative_rmse_deg_per_deg),
            "mean_harmonic_amplitude_error_pct": format_float(self.mean_harmonic_amplitude_error_pct),
            "mean_harmonic_phase_error_deg": format_float(self.mean_harmonic_phase_error_deg),
            "max_harmonic_amplitude_error_pct": format_float(self.max_harmonic_amplitude_error_pct),
            "max_harmonic_phase_error_deg": format_float(self.max_harmonic_phase_error_deg),
        }


@dataclass(frozen=True)
class Track2DCandidateSummary:

    """Aggregate CVP 1.4 diagnostics for one candidate."""

    rank: int
    candidate_id: str
    candidate_family: str
    candidate_kind: str
    candidate_source_label: str
    candidate_surface: str
    valid_direction_list: tuple[str, ...]
    curve_count: int
    mean_raw_mae_deg: float
    mean_raw_rmse_deg: float
    mean_percentage_error_pct: float
    p95_mean_percentage_error_pct: float
    mean_absolute_offset_error_deg: float
    mean_centered_mae_deg: float
    mean_centered_rmse_deg: float
    mean_centered_mae_improvement_pct: float
    mean_peak_to_peak_error_pct: float
    mean_harmonic_amplitude_error_pct: float
    mean_harmonic_phase_error_deg: float
    mean_derivative_rmse_deg_per_deg: float
    centered_shape_ratio: float
    offset_share_ratio: float
    diagnostic_label: str
    diagnostic_score: float

    def ranking_key(self) -> tuple[float, float, float, str]:

        """Return the deterministic candidate ordering key."""

        return (
            self.diagnostic_score,
            self.mean_centered_mae_deg,
            self.mean_raw_mae_deg,
            self.candidate_id,
        )

    def to_csv_row(self) -> dict[str, Any]:

        """Return a stable CSV row."""

        return {
            "rank": self.rank,
            "candidate_id": self.candidate_id,
            "candidate_family": self.candidate_family,
            "candidate_kind": self.candidate_kind,
            "candidate_source_label": self.candidate_source_label,
            "candidate_surface": self.candidate_surface,
            "valid_direction_list": ", ".join(self.valid_direction_list),
            "curve_count": self.curve_count,
            "mean_raw_mae_deg": format_float(self.mean_raw_mae_deg),
            "mean_raw_rmse_deg": format_float(self.mean_raw_rmse_deg),
            "mean_percentage_error_pct": format_float(self.mean_percentage_error_pct),
            "p95_mean_percentage_error_pct": format_float(self.p95_mean_percentage_error_pct),
            "mean_absolute_offset_error_deg": format_float(self.mean_absolute_offset_error_deg),
            "mean_centered_mae_deg": format_float(self.mean_centered_mae_deg),
            "mean_centered_rmse_deg": format_float(self.mean_centered_rmse_deg),
            "mean_centered_mae_improvement_pct": format_float(self.mean_centered_mae_improvement_pct),
            "mean_peak_to_peak_error_pct": format_float(self.mean_peak_to_peak_error_pct),
            "mean_harmonic_amplitude_error_pct": format_float(self.mean_harmonic_amplitude_error_pct),
            "mean_harmonic_phase_error_deg": format_float(self.mean_harmonic_phase_error_deg),
            "mean_derivative_rmse_deg_per_deg": format_float(self.mean_derivative_rmse_deg_per_deg),
            "centered_shape_ratio": format_float(self.centered_shape_ratio),
            "offset_share_ratio": format_float(self.offset_share_ratio),
            "diagnostic_label": self.diagnostic_label,
            "diagnostic_score": format_float(self.diagnostic_score),
        }


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Generate CVP 1.4 full-matrix mean-offset diagnostics without "
            "training models or changing the causal input contract."
        )
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="curve-verification matrix config used to resolve candidates and held-out curve records.",
    )
    argument_parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root for generated machine-readable CVP 1.4 artifacts.",
    )
    argument_parser.add_argument(
        "--report-topic-root",
        type=Path,
        default=DEFAULT_REPORT_TOPIC_ROOT,
        help="Root for the dated CVP 1.4 Markdown report bundle.",
    )
    argument_parser.add_argument(
        "--candidate-id",
        dest="candidate_id_list",
        action="append",
        default=None,
        help="Optional candidate id filter. May be provided multiple times.",
    )
    argument_parser.add_argument(
        "--candidate-start-index",
        type=int,
        default=None,
        help="Optional 1-based inclusive start index in the resolved candidate matrix.",
    )
    argument_parser.add_argument(
        "--candidate-end-index",
        type=int,
        default=None,
        help="Optional 1-based inclusive end index in the resolved candidate matrix.",
    )
    argument_parser.add_argument(
        "--merge-only",
        action="store_true",
        help="Merge existing CVP 1.4 per-curve CSV outputs into a final report without inference.",
    )
    argument_parser.add_argument(
        "--harmonic-order",
        dest="harmonic_order_list",
        action="append",
        type=int,
        default=None,
        help="Optional harmonic order to diagnose. May be provided multiple times.",
    )
    argument_parser.add_argument(
        "--report-date",
        type=str,
        default=None,
        help="Optional YYYY-MM-DD report bundle date.",
    )
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def format_float(value: float) -> str:

    """Format a numeric value for stable CSV and Markdown output."""

    if not math.isfinite(float(value)):
        return ""
    return f"{float(value):.6f}"


def safe_mean(value_list: list[float]) -> float:

    """Return the mean of finite values."""

    finite_value_list = [float(value) for value in value_list if math.isfinite(float(value))]
    return mean(finite_value_list) if finite_value_list else math.nan


def safe_pstdev(value_list: list[float]) -> float:

    """Return the population standard deviation of finite values."""

    finite_value_list = [float(value) for value in value_list if math.isfinite(float(value))]
    return pstdev(finite_value_list) if len(finite_value_list) > 1 else 0.0


def percentile(value_list: list[float], percentile_value: float) -> float:

    """Compute a deterministic linear percentile without extra dependencies."""

    clean_value_list = sorted(value for value in value_list if math.isfinite(float(value)))
    if not clean_value_list:
        return math.nan
    if len(clean_value_list) == 1:
        return float(clean_value_list[0])
    fractional_index = (len(clean_value_list) - 1) * percentile_value / 100.0
    lower_index = math.floor(fractional_index)
    upper_index = math.ceil(fractional_index)
    if lower_index == upper_index:
        return float(clean_value_list[int(fractional_index)])
    lower_value = clean_value_list[lower_index]
    upper_value = clean_value_list[upper_index]
    weight = fractional_index - lower_index
    return float(lower_value + (upper_value - lower_value) * weight)


def resolve_timestamped_output_paths(
    output_root: Path,
    report_topic_root: Path,
    report_date: str | None,
) -> tuple[str, Path, Path]:

    """Resolve timestamped output and report directories."""

    current_timestamp = datetime.now().astimezone()
    run_instance_id = (
        f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}"
        "__track2d_mean_offset_full_matrix_audit"
    )
    if report_date is None:
        report_date = current_timestamp.strftime("%Y-%m-%d")
    else:
        datetime.strptime(report_date, "%Y-%m-%d")

    output_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(output_root)
        / run_instance_id
    )
    report_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(report_topic_root)
        / f"[{report_date}]"
    )
    output_directory.mkdir(parents=True, exist_ok=True)
    report_directory.mkdir(parents=True, exist_ok=True)
    return run_instance_id, output_directory, report_directory


def load_training_config(config_path: Path, output_suffix: str) -> dict[str, Any]:

    """Load and prepare the TE Curve Verification Pipeline runtime config."""

    raw_training_config = reference_family_vs_feedforward_support.load_reference_family_comparison_config(config_path)
    return shared_training_infrastructure.prepare_output_artifact_training_config(
        raw_training_config,
        artifact_kind=shared_training_infrastructure.VALIDATION_OUTPUT_ARTIFACT_KIND,
        run_name_suffix=output_suffix,
    )


def filter_candidate_configuration_list(
    training_config: dict[str, Any],
    candidate_id_list: list[str] | None,
    candidate_start_index: int | None,
    candidate_end_index: int | None,
) -> list[dict[str, Any]]:

    """Resolve and optionally filter TE Curve Verification Pipeline candidate configurations."""

    candidate_configuration_list = (
        reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(training_config)
    )
    if candidate_start_index is not None or candidate_end_index is not None:
        start_index = 1 if candidate_start_index is None else int(candidate_start_index)
        end_index = len(candidate_configuration_list) if candidate_end_index is None else int(candidate_end_index)
        if start_index < 1 or end_index < start_index:
            raise ValueError(
                "Candidate slice must use 1-based indexes with end >= start | "
                f"start={start_index} end={end_index}"
            )
        candidate_configuration_list = candidate_configuration_list[start_index - 1 : end_index]

    if not candidate_id_list:
        return candidate_configuration_list

    candidate_configuration_map = {
        str(candidate_configuration["candidate_id"]): candidate_configuration
        for candidate_configuration in candidate_configuration_list
    }
    missing_candidate_id_list = [
        candidate_id
        for candidate_id in candidate_id_list
        if candidate_id not in candidate_configuration_map
    ]
    if missing_candidate_id_list:
        raise KeyError(f"Missing TE Curve Verification Pipeline candidate ids: {missing_candidate_id_list}")
    return [candidate_configuration_map[candidate_id] for candidate_id in candidate_id_list]


def compute_improvement_pct(raw_metric_value: float, adjusted_metric_value: float) -> float:

    """Compute percentage improvement from raw to adjusted metric."""

    if raw_metric_value <= 1.0e-12:
        return 0.0
    return float(100.0 * (raw_metric_value - adjusted_metric_value) / raw_metric_value)


def compute_curve_metric(candidate_entry: dict[str, Any], harmonic_order_list: list[int]) -> Track2DPerCurveMetric:

    """Compute one full-matrix CVP 1.4 metric row."""

    angle_deg_array = np.asarray(candidate_entry["angular_position_deg"], dtype=float)
    truth_curve_deg = np.asarray(candidate_entry["truth_curve_deg"], dtype=float)
    predicted_curve_deg = np.asarray(candidate_entry["predicted_curve_deg"], dtype=float)
    residual_curve_deg = predicted_curve_deg - truth_curve_deg
    metric_dictionary = candidate_entry["metrics"]

    truth_mean_deg = float(np.mean(truth_curve_deg))
    predicted_mean_deg = float(np.mean(predicted_curve_deg))
    truth_centered_deg = truth_curve_deg - truth_mean_deg
    predicted_centered_deg = predicted_curve_deg - predicted_mean_deg
    centered_residual_deg = predicted_centered_deg - truth_centered_deg

    raw_mae_deg = float(metric_dictionary["mae"])
    raw_rmse_deg = float(metric_dictionary["rmse"])
    centered_mae_deg = float(np.mean(np.abs(centered_residual_deg)))
    centered_rmse_deg = float(np.sqrt(np.mean(np.square(centered_residual_deg))))
    signed_offset_error_deg = predicted_mean_deg - truth_mean_deg
    truth_peak_to_peak_deg = float(np.ptp(truth_curve_deg))
    predicted_peak_to_peak_deg = float(np.ptp(predicted_curve_deg))
    residual_peak_to_peak_deg = float(np.ptp(residual_curve_deg))
    denominator = truth_peak_to_peak_deg if truth_peak_to_peak_deg > 1.0e-12 else math.nan
    peak_to_peak_error_pct = (
        abs(predicted_peak_to_peak_deg - truth_peak_to_peak_deg) / denominator * 100.0
        if math.isfinite(denominator)
        else math.nan
    )
    residual_peak_to_peak_pct = (
        residual_peak_to_peak_deg / denominator * 100.0
        if math.isfinite(denominator)
        else math.nan
    )

    truth_derivative = np.gradient(truth_curve_deg, angle_deg_array)
    predicted_derivative = np.gradient(predicted_curve_deg, angle_deg_array)
    derivative_rmse_deg_per_deg = float(
        np.sqrt(np.mean(np.square(predicted_derivative - truth_derivative)))
    )

    (
        mean_harmonic_amplitude_error_pct,
        mean_harmonic_phase_error_deg,
        max_harmonic_amplitude_error_pct,
        max_harmonic_phase_error_deg,
        _,
    ) = track2c_diagnostics.compute_harmonic_diagnostics(
        truth_curve_deg=truth_curve_deg,
        predicted_curve_deg=predicted_curve_deg,
        angle_deg_array=angle_deg_array,
        harmonic_order_list=harmonic_order_list,
    )

    return Track2DPerCurveMetric(
        candidate_id=str(candidate_entry["candidate_id"]),
        candidate_family=str(candidate_entry["candidate_family"]),
        candidate_kind=str(candidate_entry["candidate_kind"]),
        candidate_source_label=str(candidate_entry["candidate_source_label"]),
        candidate_surface=str(candidate_entry["candidate_surface"]),
        direction_label=str(candidate_entry["direction_label"]),
        source_file_path=str(candidate_entry["source_file_path"]),
        speed_rpm=float(candidate_entry["speed_rpm"]),
        torque_nm=float(candidate_entry["torque_nm"]),
        oil_temperature_deg=float(candidate_entry["oil_temperature_deg"]),
        raw_mae_deg=raw_mae_deg,
        raw_rmse_deg=raw_rmse_deg,
        mean_percentage_error_pct=float(metric_dictionary["mean_percentage_error_pct"]),
        truth_mean_deg=truth_mean_deg,
        predicted_mean_deg=predicted_mean_deg,
        signed_offset_error_deg=signed_offset_error_deg,
        absolute_offset_error_deg=float(abs(signed_offset_error_deg)),
        centered_mae_deg=centered_mae_deg,
        centered_rmse_deg=centered_rmse_deg,
        centered_mae_improvement_deg=float(raw_mae_deg - centered_mae_deg),
        centered_mae_improvement_pct=compute_improvement_pct(raw_mae_deg, centered_mae_deg),
        truth_peak_to_peak_deg=truth_peak_to_peak_deg,
        predicted_peak_to_peak_deg=predicted_peak_to_peak_deg,
        peak_to_peak_error_pct=float(peak_to_peak_error_pct),
        residual_peak_to_peak_pct=float(residual_peak_to_peak_pct),
        derivative_rmse_deg_per_deg=derivative_rmse_deg_per_deg,
        mean_harmonic_amplitude_error_pct=mean_harmonic_amplitude_error_pct,
        mean_harmonic_phase_error_deg=mean_harmonic_phase_error_deg,
        max_harmonic_amplitude_error_pct=max_harmonic_amplitude_error_pct,
        max_harmonic_phase_error_deg=max_harmonic_phase_error_deg,
    )


def classify_candidate_failure_mode(
    mean_raw_mae_deg: float,
    mean_absolute_offset_error_deg: float,
    mean_centered_mae_deg: float,
    mean_centered_mae_improvement_pct: float,
    mean_peak_to_peak_error_pct: float,
    mean_harmonic_phase_error_deg: float,
    p95_mean_percentage_error_pct: float,
    mean_percentage_error_pct: float,
) -> str:

    """Classify the dominant diagnostic limitation for a candidate."""

    offset_share_ratio = mean_absolute_offset_error_deg / max(mean_raw_mae_deg, 1.0e-12)
    centered_shape_ratio = mean_centered_mae_deg / max(mean_raw_mae_deg, 1.0e-12)
    p95_to_mean_ratio = p95_mean_percentage_error_pct / max(mean_percentage_error_pct, 1.0e-12)
    flag_list: list[str] = []

    if offset_share_ratio >= 0.60 and mean_centered_mae_improvement_pct >= 25.0:
        flag_list.append("offset-limited")
    if centered_shape_ratio >= 0.70:
        flag_list.append("centered-shape-limited")
    if mean_peak_to_peak_error_pct >= 20.0:
        flag_list.append("amplitude-limited")
    if mean_harmonic_phase_error_deg >= 60.0:
        flag_list.append("phase-limited")
    if p95_to_mean_ratio >= 2.25:
        flag_list.append("condition-regime-limited")

    if not flag_list:
        return "balanced-or-low-limited"
    if len(flag_list) == 1:
        return flag_list[0]
    return "mixed-limited:" + "+".join(flag_list)


def build_candidate_summary(candidate_id: str, entry_list: list[Track2DPerCurveMetric]) -> Track2DCandidateSummary:

    """Build one candidate-level diagnostic summary."""

    first_entry = entry_list[0]
    mean_raw_mae_deg = safe_mean([entry.raw_mae_deg for entry in entry_list])
    mean_raw_rmse_deg = safe_mean([entry.raw_rmse_deg for entry in entry_list])
    mean_percentage_error_pct = safe_mean([entry.mean_percentage_error_pct for entry in entry_list])
    p95_mean_percentage_error_pct = percentile([entry.mean_percentage_error_pct for entry in entry_list], 95.0)
    mean_absolute_offset_error_deg = safe_mean([entry.absolute_offset_error_deg for entry in entry_list])
    mean_centered_mae_deg = safe_mean([entry.centered_mae_deg for entry in entry_list])
    mean_centered_rmse_deg = safe_mean([entry.centered_rmse_deg for entry in entry_list])
    mean_centered_mae_improvement_pct = safe_mean(
        [entry.centered_mae_improvement_pct for entry in entry_list]
    )
    mean_peak_to_peak_error_pct = safe_mean([entry.peak_to_peak_error_pct for entry in entry_list])
    mean_harmonic_amplitude_error_pct = safe_mean(
        [entry.mean_harmonic_amplitude_error_pct for entry in entry_list]
    )
    mean_harmonic_phase_error_deg = safe_mean([entry.mean_harmonic_phase_error_deg for entry in entry_list])
    mean_derivative_rmse_deg_per_deg = safe_mean([entry.derivative_rmse_deg_per_deg for entry in entry_list])
    centered_shape_ratio = mean_centered_mae_deg / max(mean_raw_mae_deg, 1.0e-12)
    offset_share_ratio = mean_absolute_offset_error_deg / max(mean_raw_mae_deg, 1.0e-12)
    diagnostic_label = classify_candidate_failure_mode(
        mean_raw_mae_deg=mean_raw_mae_deg,
        mean_absolute_offset_error_deg=mean_absolute_offset_error_deg,
        mean_centered_mae_deg=mean_centered_mae_deg,
        mean_centered_mae_improvement_pct=mean_centered_mae_improvement_pct,
        mean_peak_to_peak_error_pct=mean_peak_to_peak_error_pct,
        mean_harmonic_phase_error_deg=mean_harmonic_phase_error_deg,
        p95_mean_percentage_error_pct=p95_mean_percentage_error_pct,
        mean_percentage_error_pct=mean_percentage_error_pct,
    )
    diagnostic_score = (
        mean_centered_mae_deg
        + 0.50 * mean_absolute_offset_error_deg
        + 0.0002 * mean_peak_to_peak_error_pct
        + 0.0001 * mean_harmonic_amplitude_error_pct
        + 0.00002 * mean_harmonic_phase_error_deg
        + 2.0 * mean_derivative_rmse_deg_per_deg
    )

    return Track2DCandidateSummary(
        rank=0,
        candidate_id=candidate_id,
        candidate_family=first_entry.candidate_family,
        candidate_kind=first_entry.candidate_kind,
        candidate_source_label=first_entry.candidate_source_label,
        candidate_surface=first_entry.candidate_surface,
        valid_direction_list=tuple(sorted({entry.direction_label for entry in entry_list})),
        curve_count=len(entry_list),
        mean_raw_mae_deg=mean_raw_mae_deg,
        mean_raw_rmse_deg=mean_raw_rmse_deg,
        mean_percentage_error_pct=mean_percentage_error_pct,
        p95_mean_percentage_error_pct=p95_mean_percentage_error_pct,
        mean_absolute_offset_error_deg=mean_absolute_offset_error_deg,
        mean_centered_mae_deg=mean_centered_mae_deg,
        mean_centered_rmse_deg=mean_centered_rmse_deg,
        mean_centered_mae_improvement_pct=mean_centered_mae_improvement_pct,
        mean_peak_to_peak_error_pct=mean_peak_to_peak_error_pct,
        mean_harmonic_amplitude_error_pct=mean_harmonic_amplitude_error_pct,
        mean_harmonic_phase_error_deg=mean_harmonic_phase_error_deg,
        mean_derivative_rmse_deg_per_deg=mean_derivative_rmse_deg_per_deg,
        centered_shape_ratio=centered_shape_ratio,
        offset_share_ratio=offset_share_ratio,
        diagnostic_label=diagnostic_label,
        diagnostic_score=diagnostic_score,
    )


def rerank_candidate_summary_list(summary_list: list[Track2DCandidateSummary]) -> list[Track2DCandidateSummary]:

    """Sort summaries and assign deterministic ranks."""

    reranked_summary_list: list[Track2DCandidateSummary] = []
    for rank_index, summary in enumerate(sorted(summary_list, key=lambda item: item.ranking_key()), start=1):
        reranked_summary_list.append(
            Track2DCandidateSummary(
                rank=rank_index,
                candidate_id=summary.candidate_id,
                candidate_family=summary.candidate_family,
                candidate_kind=summary.candidate_kind,
                candidate_source_label=summary.candidate_source_label,
                candidate_surface=summary.candidate_surface,
                valid_direction_list=summary.valid_direction_list,
                curve_count=summary.curve_count,
                mean_raw_mae_deg=summary.mean_raw_mae_deg,
                mean_raw_rmse_deg=summary.mean_raw_rmse_deg,
                mean_percentage_error_pct=summary.mean_percentage_error_pct,
                p95_mean_percentage_error_pct=summary.p95_mean_percentage_error_pct,
                mean_absolute_offset_error_deg=summary.mean_absolute_offset_error_deg,
                mean_centered_mae_deg=summary.mean_centered_mae_deg,
                mean_centered_rmse_deg=summary.mean_centered_rmse_deg,
                mean_centered_mae_improvement_pct=summary.mean_centered_mae_improvement_pct,
                mean_peak_to_peak_error_pct=summary.mean_peak_to_peak_error_pct,
                mean_harmonic_amplitude_error_pct=summary.mean_harmonic_amplitude_error_pct,
                mean_harmonic_phase_error_deg=summary.mean_harmonic_phase_error_deg,
                mean_derivative_rmse_deg_per_deg=summary.mean_derivative_rmse_deg_per_deg,
                centered_shape_ratio=summary.centered_shape_ratio,
                offset_share_ratio=summary.offset_share_ratio,
                diagnostic_label=summary.diagnostic_label,
                diagnostic_score=summary.diagnostic_score,
            )
        )
    return reranked_summary_list


def build_candidate_summary_list(
    per_curve_metric_list: list[Track2DPerCurveMetric],
) -> list[Track2DCandidateSummary]:

    """Aggregate per-curve metrics by candidate."""

    candidate_entry_map: dict[str, list[Track2DPerCurveMetric]] = defaultdict(list)
    for metric_entry in per_curve_metric_list:
        candidate_entry_map[metric_entry.candidate_id].append(metric_entry)
    return rerank_candidate_summary_list(
        [
            build_candidate_summary(candidate_id, entry_list)
            for candidate_id, entry_list in candidate_entry_map.items()
        ]
    )


def build_surface_leaderboard(summary_list: list[Track2DCandidateSummary]) -> list[Track2DCandidateSummary]:

    """Return one best CVP 1.4 candidate per candidate surface."""

    surface_summary_map: dict[str, list[Track2DCandidateSummary]] = defaultdict(list)
    for summary in summary_list:
        surface_summary_map[summary.candidate_surface].append(summary)

    surface_leader_list: list[Track2DCandidateSummary] = []
    for surface in sorted(surface_summary_map):
        surface_leader_list.extend(rerank_candidate_summary_list(surface_summary_map[surface])[:1])
    return surface_leader_list


def build_condition_stratified_rows(
    per_curve_metric_list: list[Track2DPerCurveMetric],
) -> list[dict[str, Any]]:

    """Build condition-stratified metric summaries."""

    grouped_metric_map: dict[tuple[str, str, str, str, str], list[Track2DPerCurveMetric]] = defaultdict(list)
    for metric_entry in per_curve_metric_list:
        grouping_key_list = [
            ("direction", metric_entry.direction_label),
            ("speed_rpm", f"{metric_entry.speed_rpm:.0f}"),
            ("torque_nm", f"{metric_entry.torque_nm:.0f}"),
            ("oil_temperature_deg", f"{metric_entry.oil_temperature_deg:.0f}"),
        ]
        for group_type, group_value in grouping_key_list:
            grouped_metric_map[
                (
                    metric_entry.candidate_id,
                    metric_entry.candidate_surface,
                    group_type,
                    group_value,
                    metric_entry.direction_label,
                )
            ].append(metric_entry)

    row_list: list[dict[str, Any]] = []
    for grouping_key, entry_list in sorted(grouped_metric_map.items()):
        candidate_id, candidate_surface, group_type, group_value, direction_label = grouping_key
        row_list.append(
            {
                "candidate_id": candidate_id,
                "candidate_surface": candidate_surface,
                "group_type": group_type,
                "group_value": group_value,
                "direction_label": direction_label,
                "curve_count": len(entry_list),
                "mean_raw_mae_deg": format_float(safe_mean([entry.raw_mae_deg for entry in entry_list])),
                "mean_absolute_offset_error_deg": format_float(
                    safe_mean([entry.absolute_offset_error_deg for entry in entry_list])
                ),
                "mean_centered_mae_deg": format_float(safe_mean([entry.centered_mae_deg for entry in entry_list])),
                "std_centered_mae_deg": format_float(safe_pstdev([entry.centered_mae_deg for entry in entry_list])),
                "mean_peak_to_peak_error_pct": format_float(
                    safe_mean([entry.peak_to_peak_error_pct for entry in entry_list])
                ),
                "mean_harmonic_phase_error_deg": format_float(
                    safe_mean([entry.mean_harmonic_phase_error_deg for entry in entry_list])
                ),
            }
        )
    return row_list


def write_csv(csv_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write a CSV file with stable newline behavior."""

    field_name_list = list(row_list[0].keys()) if row_list else []
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_list, lineterminator="\n")
        writer.writeheader()
        for row in row_list:
            writer.writerow(row)


def parse_float_cell(value: Any) -> float:

    """Parse a CSV float cell."""

    text_value = str(value or "").strip()
    if not text_value:
        return math.nan
    return float(text_value)


def load_per_curve_metric_csv(csv_path: Path) -> list[Track2DPerCurveMetric]:

    """Load CVP 1.4 per-curve metrics from one CSV."""

    with csv_path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        row_list = [dict(row) for row in reader]

    metric_list: list[Track2DPerCurveMetric] = []
    for row in row_list:
        metric_list.append(
            Track2DPerCurveMetric(
                candidate_id=str(row["candidate_id"]),
                candidate_family=str(row["candidate_family"]),
                candidate_kind=str(row["candidate_kind"]),
                candidate_source_label=str(row["candidate_source_label"]),
                candidate_surface=str(row["candidate_surface"]),
                direction_label=str(row["direction_label"]),
                source_file_path=str(row["source_file_path"]),
                speed_rpm=parse_float_cell(row["speed_rpm"]),
                torque_nm=parse_float_cell(row["torque_nm"]),
                oil_temperature_deg=parse_float_cell(row["oil_temperature_deg"]),
                raw_mae_deg=parse_float_cell(row["raw_mae_deg"]),
                raw_rmse_deg=parse_float_cell(row["raw_rmse_deg"]),
                mean_percentage_error_pct=parse_float_cell(row["mean_percentage_error_pct"]),
                truth_mean_deg=parse_float_cell(row["truth_mean_deg"]),
                predicted_mean_deg=parse_float_cell(row["predicted_mean_deg"]),
                signed_offset_error_deg=parse_float_cell(row["signed_offset_error_deg"]),
                absolute_offset_error_deg=parse_float_cell(row["absolute_offset_error_deg"]),
                centered_mae_deg=parse_float_cell(row["centered_mae_deg"]),
                centered_rmse_deg=parse_float_cell(row["centered_rmse_deg"]),
                centered_mae_improvement_deg=parse_float_cell(row["centered_mae_improvement_deg"]),
                centered_mae_improvement_pct=parse_float_cell(row["centered_mae_improvement_pct"]),
                truth_peak_to_peak_deg=parse_float_cell(row["truth_peak_to_peak_deg"]),
                predicted_peak_to_peak_deg=parse_float_cell(row["predicted_peak_to_peak_deg"]),
                peak_to_peak_error_pct=parse_float_cell(row["peak_to_peak_error_pct"]),
                residual_peak_to_peak_pct=parse_float_cell(row["residual_peak_to_peak_pct"]),
                derivative_rmse_deg_per_deg=parse_float_cell(row["derivative_rmse_deg_per_deg"]),
                mean_harmonic_amplitude_error_pct=parse_float_cell(row["mean_harmonic_amplitude_error_pct"]),
                mean_harmonic_phase_error_deg=parse_float_cell(row["mean_harmonic_phase_error_deg"]),
                max_harmonic_amplitude_error_pct=parse_float_cell(row["max_harmonic_amplitude_error_pct"]),
                max_harmonic_phase_error_deg=parse_float_cell(row["max_harmonic_phase_error_deg"]),
            )
        )
    return metric_list


def metric_identity_key(metric_entry: Track2DPerCurveMetric) -> tuple[str, str, str]:

    """Build a stable deduplication key for one metric row."""

    return (
        metric_entry.candidate_id,
        metric_entry.source_file_path,
        metric_entry.direction_label,
    )


def load_merge_per_curve_metric_list(output_root: Path) -> list[Track2DPerCurveMetric]:

    """Load and deduplicate all existing CVP 1.4 per-curve metrics."""

    resolved_output_root = shared_training_infrastructure.resolve_runtime_project_relative_path(output_root)
    if not resolved_output_root.exists():
        raise FileNotFoundError(f"CVP 1.4 output root does not exist: {resolved_output_root}")

    metric_map: dict[tuple[str, str, str], Track2DPerCurveMetric] = {}
    for csv_path in sorted(resolved_output_root.glob(f"*__track2d_mean_offset_full_matrix_audit/{PER_CURVE_METRICS_FILENAME}")):
        for metric_entry in load_per_curve_metric_csv(csv_path):
            metric_map[metric_identity_key(metric_entry)] = metric_entry
    if not metric_map:
        raise FileNotFoundError(f"No CVP 1.4 per-curve CSV files found under {resolved_output_root}")
    return list(metric_map.values())


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

    """Return a compact report label for wide tables."""

    label_text = str(label)
    replacement_pair_list = [
        ("mixed-limited:", "mixed:"),
        ("centered-shape-limited", "shape"),
        ("offset-limited", "offset"),
        ("amplitude-limited", "amp"),
        ("phase-limited", "phase"),
        ("condition-regime-limited", "regime"),
        ("balanced-or-low-limited", "balanced"),
    ]
    for source_text, target_text in replacement_pair_list:
        label_text = label_text.replace(source_text, target_text)
    return label_text


def build_summary_table_rows(summary_list: list[Track2DCandidateSummary], limit: int) -> list[list[str]]:

    """Build compact Markdown rows for candidate summaries."""

    return [
        [
            str(summary.rank),
            f"`{summary.candidate_id}`",
            summary.candidate_surface,
            format_float(summary.mean_raw_mae_deg),
            format_float(summary.mean_centered_mae_deg),
            format_float(summary.mean_absolute_offset_error_deg),
            f"{summary.mean_centered_mae_improvement_pct:.1f}",
            compact_label(summary.diagnostic_label),
        ]
        for summary in summary_list[:limit]
    ]


def append_candidate_table(
    line_list: list[str],
    title: str,
    summary_list: list[Track2DCandidateSummary],
    limit: int,
) -> None:

    """Append one candidate summary table."""

    line_list.extend([f"## {title}", ""])
    line_list.extend(
        markdown_table(
            [
                "Rank",
                "Candidate",
                "Surface",
                "Raw MAE",
                "Centered MAE",
                "Offset",
                "Gain [%]",
                "Label",
            ],
            build_summary_table_rows(summary_list, limit),
        )
    )
    line_list.append("")


def build_report_lines(
    run_instance_id: str,
    config_path: Path,
    output_directory: Path,
    per_curve_metric_list: list[Track2DPerCurveMetric],
    candidate_summary_list: list[Track2DCandidateSummary],
    surface_leader_list: list[Track2DCandidateSummary],
    harmonic_order_list: list[int],
) -> list[str]:

    """Build the Markdown report body."""

    label_count_map: dict[str, int] = defaultdict(int)
    for summary in candidate_summary_list:
        label_count_map[summary.diagnostic_label] += 1

    line_list = [
        "# CVP 1.4 Mean-Offset Full-Matrix Audit",
        "",
        "## Overview",
        "",
        (
            "This report extends the `TE Curve Verification Pipeline` mean-centered collage diagnostic "
            "to the full official direction-valid candidate matrix. It computes "
            "raw curve error, curve-bias / `DC` offset, centered-shape error, "
            "peak-to-peak amplitude error, harmonic amplitude error, and harmonic "
            "phase error after every candidate produces predictions through its "
            "normal causal input path."
        ),
        "",
        "This is an analysis-only diagnostic. It does not train models, alter the",
        "dataset structure, update registries, or make full-curve mean-centering",
        "a deployment-time correction.",
        "",
        f"- Run Instance: `{run_instance_id}`",
        f"- Config Path: `{config_path.relative_to(PROJECT_PATH)}`",
        f"- Output Directory: `{output_directory.relative_to(PROJECT_PATH)}`",
        f"- Candidate Count: `{len(candidate_summary_list)}`",
        f"- Evaluated Curve Count: `{len(per_curve_metric_list)}`",
        f"- Harmonic Orders: `{', '.join(str(order) for order in harmonic_order_list)}`",
        "",
        "## Method",
        "",
        "- raw `MAE` and `RMSE` are computed on the normal prediction residual;",
        "- offset is the absolute difference between predicted and measured curve",
        "  means;",
        "- centered metrics subtract each curve's own mean from truth and",
        "  prediction separately after inference;",
        "- amplitude error compares predicted and measured peak-to-peak TE;",
        "- harmonic amplitude and phase diagnostics are computed on selected",
        "  sparse `RCIM` harmonic orders;",
        "- condition summaries stratify by direction, speed, torque, and oil",
        "  temperature.",
        "",
        "## Diagnostic Label Counts",
        "",
    ]
    line_list.extend(
        markdown_table(
            ["Label", "Candidate Count"],
            [[f"`{compact_label(label)}`", str(count)] for label, count in sorted(label_count_map.items())],
        )
    )
    line_list.append("")
    append_candidate_table(line_list, "CVP 1.4 Diagnostic Ranking", candidate_summary_list, 20)
    append_candidate_table(line_list, "Surface Leaders", surface_leader_list, len(surface_leader_list))
    append_candidate_table(
        line_list,
        "Largest Mean-Offset Improvements",
        sorted(candidate_summary_list, key=lambda summary: summary.mean_centered_mae_improvement_pct, reverse=True),
        15,
    )

    line_list.extend(
        [
            "## Interpretation",
            "",
            (
                "The ranking is a diagnostic ordering, not a promotion rule. "
                "Offset-limited candidates need a causal offset-calibration or "
                "offset-aware loss strategy. Centered-shape-limited candidates "
                "need waveform-shape, derivative, harmonic amplitude, or phase "
                "improvements before retraining should be expanded."
            ),
            "",
            (
                "The next training decision should keep `Fw`, `Bw`, and `global` "
                "surfaces in parallel. A forward leader does not close the "
                "backward or global branch, and a backward leader does not close "
                "the forward or global branch."
            ),
            "",
            "## Runtime Input Boundary",
            "",
            (
                "All full-curve operations are post-prediction diagnostics. "
                "Candidate models still consume only current point-level state, "
                "an explicitly supported short causal history, or causal derived "
                "features. The audit does not use future TE samples as model "
                "inputs."
            ),
            "",
            "## Machine-Readable Artifacts",
            "",
            f"- `{(output_directory / PER_CURVE_METRICS_FILENAME).relative_to(PROJECT_PATH)}`",
            f"- `{(output_directory / CANDIDATE_SUMMARY_FILENAME).relative_to(PROJECT_PATH)}`",
            f"- `{(output_directory / SURFACE_LEADERBOARD_FILENAME).relative_to(PROJECT_PATH)}`",
            f"- `{(output_directory / CONDITION_STRATIFIED_FILENAME).relative_to(PROJECT_PATH)}`",
            f"- `{(output_directory / SUMMARY_FILENAME).relative_to(PROJECT_PATH)}`",
            "",
        ]
    )
    return line_list


def write_summary_yaml(
    summary_path: Path,
    run_instance_id: str,
    config_path: Path,
    output_directory: Path,
    report_path: Path,
    candidate_summary_list: list[Track2DCandidateSummary],
    surface_leader_list: list[Track2DCandidateSummary],
    harmonic_order_list: list[int],
) -> None:

    """Write a machine-readable CVP 1.4 summary."""

    summary_payload = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "config_path": str(config_path.relative_to(PROJECT_PATH)),
        "output_directory": str(output_directory.relative_to(PROJECT_PATH)),
        "report_path": str(report_path.relative_to(PROJECT_PATH)),
        "harmonic_order_list": harmonic_order_list,
        "ranking_policy": {
            "primary_interpretation": "diagnostic_failure_mode_classification",
            "registry_promotion": "not_automatic",
            "causal_input_contract": (
                "current point, optional short causal history, or derived causal features only"
            ),
        },
        "overall_diagnostic_leader": candidate_summary_list[0].to_csv_row() if candidate_summary_list else {},
        "surface_leader_list": [
            summary.to_csv_row()
            for summary in surface_leader_list
        ],
        "candidate_summary_list": [
            summary.to_csv_row()
            for summary in candidate_summary_list
        ],
    }
    with summary_path.open("w", encoding="utf-8") as summary_file:
        yaml.safe_dump(summary_payload, summary_file, sort_keys=False, allow_unicode=False)


def run_track2d_mean_offset_full_matrix_audit(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the CVP 1.4 full-matrix diagnostic workflow."""

    harmonic_order_list = arguments.harmonic_order_list or DEFAULT_HARMONIC_ORDER_LIST
    resolved_config_path = shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.config_path)
    run_instance_id, output_directory, report_directory = resolve_timestamped_output_paths(
        output_root=arguments.output_root,
        report_topic_root=arguments.report_topic_root,
        report_date=arguments.report_date,
    )
    report_path = report_directory / REPORT_FILENAME

    if arguments.merge_only:
        print("[INFO] Merging existing CVP 1.4 chunk outputs", flush=True)
        per_curve_metric_list = load_merge_per_curve_metric_list(arguments.output_root)
    else:
        training_config = load_training_config(resolved_config_path, output_suffix=run_instance_id)
        selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
        candidate_configuration_list = filter_candidate_configuration_list(
            training_config,
            arguments.candidate_id_list,
            arguments.candidate_start_index,
            arguments.candidate_end_index,
        )
        curve_record_list, _, _, _ = reference_family_vs_feedforward_support.build_curve_record_list(
            training_config,
            selected_harmonic_list,
        )
        percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])

        per_curve_metric_list = []
        for candidate_index, candidate_configuration in enumerate(candidate_configuration_list, start=1):
            print(
                "[INFO] Evaluating CVP 1.4 candidate | "
                f"{candidate_index}/{len(candidate_configuration_list)} | "
                f"{candidate_configuration['candidate_id']}",
                flush=True,
            )
            candidate = reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)
            candidate_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
                candidate,
                curve_record_list,
                percentage_error_denominator,
                include_curve_payload=True,
            )
            for candidate_entry in candidate_entry_list:
                per_curve_metric_list.append(compute_curve_metric(candidate_entry, harmonic_order_list))

    candidate_summary_list = build_candidate_summary_list(per_curve_metric_list)
    surface_leader_list = build_surface_leaderboard(candidate_summary_list)
    condition_stratified_row_list = build_condition_stratified_rows(per_curve_metric_list)

    write_csv(
        output_directory / PER_CURVE_METRICS_FILENAME,
        [entry.to_csv_row() for entry in per_curve_metric_list],
    )
    write_csv(
        output_directory / CANDIDATE_SUMMARY_FILENAME,
        [summary.to_csv_row() for summary in candidate_summary_list],
    )
    write_csv(
        output_directory / SURFACE_LEADERBOARD_FILENAME,
        [summary.to_csv_row() for summary in surface_leader_list],
    )
    write_csv(output_directory / CONDITION_STRATIFIED_FILENAME, condition_stratified_row_list)
    write_summary_yaml(
        summary_path=output_directory / SUMMARY_FILENAME,
        run_instance_id=run_instance_id,
        config_path=resolved_config_path,
        output_directory=output_directory,
        report_path=report_path,
        candidate_summary_list=candidate_summary_list,
        surface_leader_list=surface_leader_list,
        harmonic_order_list=harmonic_order_list,
    )

    report_lines = build_report_lines(
        run_instance_id=run_instance_id,
        config_path=resolved_config_path,
        output_directory=output_directory,
        per_curve_metric_list=per_curve_metric_list,
        candidate_summary_list=candidate_summary_list,
        surface_leader_list=surface_leader_list,
        harmonic_order_list=harmonic_order_list,
    )
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    return {
        "run_instance_id": run_instance_id,
        "output_directory": str(output_directory.relative_to(PROJECT_PATH)),
        "report_path": str(report_path.relative_to(PROJECT_PATH)),
        "candidate_count": len(candidate_summary_list),
        "curve_count": len(per_curve_metric_list),
    }


def main() -> None:

    """Run the CVP 1.4 diagnostics workflow."""

    summary = run_track2d_mean_offset_full_matrix_audit(parse_command_line_arguments())
    print(f"[DONE] CVP 1.4 report: {summary['report_path']}")
    print(f"[DONE] CVP 1.4 artifacts: {summary['output_directory']}")


if __name__ == "__main__":
    main()
