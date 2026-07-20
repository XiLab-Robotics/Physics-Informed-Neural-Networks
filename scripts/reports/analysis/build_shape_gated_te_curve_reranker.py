"""Build a shape-gated TE Curve Verification Pipeline reranker."""

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
from statistics import mean
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
    run_reference_family_vs_feedforward_comparison,
)
from scripts.reports.analysis import build_track2_curve_payload_diagnostics_report as track2c_diagnostics
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "selected_active_track2_polished_actual_values_matrix.yaml"
)
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "shape_gated_te_curve_reranker"
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "te_curve_verification_pipeline"
    / "03_cvp_diagnostics"
    / "shape_gated_reranker"
)
DEFAULT_DATASET_NAME = "polished_dataset"
DEFAULT_SURFACE_SCOPE_LIST = ["forward", "backward"]
DEFAULT_ACTIVE_FAMILY_LIST = [
    "periodic_gru_sequence",
    "wave4_1_mae_robust_loss",
    "wave4_2_quantile_p10_p50_p90",
    "periodic_mlp_harmonic",
    "tree",
    "feedforward",
    "harmonic_regression",
]
DEFAULT_HARMONIC_ORDER_LIST = [1, 3, 39, 40, 78, 81, 156, 162, 240]

PER_CURVE_METRICS_FILENAME = "shape_gated_per_curve_metrics.csv"
CANDIDATE_SUMMARY_FILENAME = "shape_gated_candidate_summary.csv"
SURFACE_DECISION_FILENAME = "shape_gated_surface_decisions.yaml"
THRESHOLD_SWEEP_FILENAME = "shape_gate_threshold_sweep.csv"
REPORT_FILENAME = "shape_gated_te_curve_reranker_report.md"
DERIVATIVE_SMOOTHING_WINDOW = 7
DERIVATIVE_SIGN_EPSILON = 1.0e-8
BASELINE_ANCHOR_FAMILY_SET = {"tree", "feedforward", "harmonic_regression"}


@dataclass(frozen=True)
class ShapeGateThresholds:

    """Store conservative shape-gate thresholds."""

    minimum_fft_amplitude_similarity: float
    minimum_derivative_correlation: float
    minimum_smoothed_derivative_correlation: float
    minimum_derivative_sign_agreement_rate: float
    maximum_normalized_derivative_rmse: float
    maximum_mean_harmonic_amplitude_error_pct: float
    maximum_mean_harmonic_phase_error_deg: float
    maximum_peak_to_peak_error_pct: float
    minimum_per_curve_shape_pass_rate: float
    near_pass_minimum_fft_amplitude_similarity: float
    near_pass_maximum_mean_harmonic_amplitude_error_pct: float
    near_pass_maximum_mean_harmonic_phase_error_deg: float
    near_pass_maximum_peak_to_peak_error_pct: float
    near_pass_minimum_derivative_sign_agreement_rate: float
    near_pass_maximum_normalized_derivative_rmse: float


@dataclass(frozen=True)
class ShapeCurveMetric:

    """Store one per-curve shape-gated metric row."""

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
    p95_candidate_percentage_error_pct: float
    absolute_offset_error_deg: float
    centered_mae_deg: float
    centered_rmse_deg: float
    peak_to_peak_error_pct: float
    fft_amplitude_similarity: float
    dominant_harmonic_order: int
    dominant_harmonic_retention_pct: float
    dominant_harmonic_phase_error_deg: float
    mean_harmonic_amplitude_error_pct: float
    mean_harmonic_phase_error_deg: float
    derivative_correlation: float
    centered_derivative_correlation: float
    smoothed_derivative_correlation: float
    derivative_sign_agreement_rate: float
    derivative_rmse_deg_per_deg: float
    normalized_derivative_rmse: float
    shape_failure_reason: str
    shape_pass: bool

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
            "p95_candidate_percentage_error_pct": format_float(self.p95_candidate_percentage_error_pct),
            "absolute_offset_error_deg": format_float(self.absolute_offset_error_deg),
            "centered_mae_deg": format_float(self.centered_mae_deg),
            "centered_rmse_deg": format_float(self.centered_rmse_deg),
            "peak_to_peak_error_pct": format_float(self.peak_to_peak_error_pct),
            "fft_amplitude_similarity": format_float(self.fft_amplitude_similarity),
            "dominant_harmonic_order": self.dominant_harmonic_order,
            "dominant_harmonic_retention_pct": format_float(self.dominant_harmonic_retention_pct),
            "dominant_harmonic_phase_error_deg": format_float(self.dominant_harmonic_phase_error_deg),
            "mean_harmonic_amplitude_error_pct": format_float(self.mean_harmonic_amplitude_error_pct),
            "mean_harmonic_phase_error_deg": format_float(self.mean_harmonic_phase_error_deg),
            "derivative_correlation": format_float(self.derivative_correlation),
            "centered_derivative_correlation": format_float(self.centered_derivative_correlation),
            "smoothed_derivative_correlation": format_float(self.smoothed_derivative_correlation),
            "derivative_sign_agreement_rate": format_float(self.derivative_sign_agreement_rate),
            "derivative_rmse_deg_per_deg": format_float(self.derivative_rmse_deg_per_deg),
            "normalized_derivative_rmse": format_float(self.normalized_derivative_rmse),
            "shape_failure_reason": self.shape_failure_reason,
            "shape_pass": str(self.shape_pass).lower(),
        }


@dataclass(frozen=True)
class EvaluationFailure:

    """Store one candidate evaluation failure."""

    candidate_id: str
    candidate_family: str
    candidate_kind: str
    candidate_source_label: str
    candidate_surface: str
    surface_scope: str
    error_type: str
    error_message: str


@dataclass(frozen=True)
class ShapeCandidateSummary:

    """Store one candidate-level shape-gated summary."""

    rank: int
    candidate_id: str
    candidate_family: str
    candidate_kind: str
    candidate_source_label: str
    candidate_surface: str
    direction_label: str
    curve_count: int
    mean_raw_mae_deg: float
    mean_raw_rmse_deg: float
    mean_percentage_error_pct: float
    p95_mean_percentage_error_pct: float
    mean_absolute_offset_error_deg: float
    mean_centered_mae_deg: float
    mean_centered_rmse_deg: float
    mean_peak_to_peak_error_pct: float
    mean_fft_amplitude_similarity: float
    mean_dominant_harmonic_retention_pct: float
    mean_dominant_harmonic_phase_error_deg: float
    mean_harmonic_amplitude_error_pct: float
    mean_harmonic_phase_error_deg: float
    mean_derivative_correlation: float
    mean_smoothed_derivative_correlation: float
    mean_derivative_sign_agreement_rate: float
    mean_derivative_rmse_deg_per_deg: float
    mean_normalized_derivative_rmse: float
    per_curve_shape_pass_rate: float
    raw_error_score: float
    shape_score: float
    harmonic_score: float
    offset_score: float
    robustness_score: float
    composite_score: float
    decision_label: str
    veto_reason: str

    def ranking_key(self) -> tuple[int, float, float, str]:

        """Return a deterministic reranking key."""

        decision_order = {
            "candidate": 0,
            "recommended_candidate": 0,
            "near_pass": 1,
            "baseline_anchor_only": 2,
            "shape_gate_failed": 3,
            "insufficient_evidence": 4,
        }
        return (
            decision_order.get(self.decision_label, 4),
            self.composite_score,
            self.mean_raw_mae_deg if math.isfinite(self.mean_raw_mae_deg) else math.inf,
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
            "direction_label": self.direction_label,
            "curve_count": self.curve_count,
            "mean_raw_mae_deg": format_float(self.mean_raw_mae_deg),
            "mean_raw_rmse_deg": format_float(self.mean_raw_rmse_deg),
            "mean_percentage_error_pct": format_float(self.mean_percentage_error_pct),
            "p95_mean_percentage_error_pct": format_float(self.p95_mean_percentage_error_pct),
            "mean_absolute_offset_error_deg": format_float(self.mean_absolute_offset_error_deg),
            "mean_centered_mae_deg": format_float(self.mean_centered_mae_deg),
            "mean_centered_rmse_deg": format_float(self.mean_centered_rmse_deg),
            "mean_peak_to_peak_error_pct": format_float(self.mean_peak_to_peak_error_pct),
            "mean_fft_amplitude_similarity": format_float(self.mean_fft_amplitude_similarity),
            "mean_dominant_harmonic_retention_pct": format_float(self.mean_dominant_harmonic_retention_pct),
            "mean_dominant_harmonic_phase_error_deg": format_float(self.mean_dominant_harmonic_phase_error_deg),
            "mean_harmonic_amplitude_error_pct": format_float(self.mean_harmonic_amplitude_error_pct),
            "mean_harmonic_phase_error_deg": format_float(self.mean_harmonic_phase_error_deg),
            "mean_derivative_correlation": format_float(self.mean_derivative_correlation),
            "mean_smoothed_derivative_correlation": format_float(self.mean_smoothed_derivative_correlation),
            "mean_derivative_sign_agreement_rate": format_float(self.mean_derivative_sign_agreement_rate),
            "mean_derivative_rmse_deg_per_deg": format_float(self.mean_derivative_rmse_deg_per_deg),
            "mean_normalized_derivative_rmse": format_float(self.mean_normalized_derivative_rmse),
            "per_curve_shape_pass_rate": format_float(self.per_curve_shape_pass_rate),
            "raw_error_score": format_float(self.raw_error_score),
            "shape_score": format_float(self.shape_score),
            "harmonic_score": format_float(self.harmonic_score),
            "offset_score": format_float(self.offset_score),
            "robustness_score": format_float(self.robustness_score),
            "composite_score": format_float(self.composite_score),
            "decision_label": self.decision_label,
            "veto_reason": self.veto_reason,
        }


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description="Build a reduced shape-gated TE Curve Verification Pipeline reranking report."
    )
    argument_parser.add_argument("--config-path", type=Path, default=DEFAULT_CONFIG_PATH)
    argument_parser.add_argument("--dataset", type=str, default=DEFAULT_DATASET_NAME)
    argument_parser.add_argument(
        "--surface-scope",
        action="append",
        default=None,
        help="Surface scope to evaluate. May be repeated. Defaults to forward and backward.",
    )
    argument_parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    argument_parser.add_argument("--report-topic-root", type=Path, default=DEFAULT_REPORT_TOPIC_ROOT)
    argument_parser.add_argument("--report-date", type=str, default=None)
    argument_parser.add_argument(
        "--active-family",
        dest="active_family_list",
        action="append",
        default=None,
        help="Candidate family to keep in the reduced active set. May be repeated.",
    )
    argument_parser.add_argument(
        "--harmonic-order",
        dest="harmonic_order_list",
        action="append",
        type=int,
        default=None,
        help="Harmonic order to score. May be repeated.",
    )
    argument_parser.add_argument("--minimum-fft-amplitude-similarity", type=float, default=0.82)
    argument_parser.add_argument("--minimum-derivative-correlation", type=float, default=0.70)
    argument_parser.add_argument("--minimum-smoothed-derivative-correlation", type=float, default=0.25)
    argument_parser.add_argument("--minimum-derivative-sign-agreement-rate", type=float, default=0.54)
    argument_parser.add_argument("--maximum-normalized-derivative-rmse", type=float, default=1.00)
    argument_parser.add_argument("--maximum-mean-harmonic-amplitude-error-pct", type=float, default=55.0)
    argument_parser.add_argument("--maximum-mean-harmonic-phase-error-deg", type=float, default=75.0)
    argument_parser.add_argument("--maximum-peak-to-peak-error-pct", type=float, default=35.0)
    argument_parser.add_argument("--minimum-per-curve-shape-pass-rate", type=float, default=0.60)
    argument_parser.add_argument("--near-pass-minimum-fft-amplitude-similarity", type=float, default=0.95)
    argument_parser.add_argument("--near-pass-maximum-mean-harmonic-amplitude-error-pct", type=float, default=38.0)
    argument_parser.add_argument("--near-pass-maximum-mean-harmonic-phase-error-deg", type=float, default=55.0)
    argument_parser.add_argument("--near-pass-maximum-peak-to-peak-error-pct", type=float, default=32.0)
    argument_parser.add_argument("--near-pass-minimum-derivative-sign-agreement-rate", type=float, default=0.50)
    argument_parser.add_argument("--near-pass-maximum-normalized-derivative-rmse", type=float, default=1.35)
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def format_float(value: float) -> str:

    """Format finite floats for stable artifacts."""

    if not math.isfinite(float(value)):
        return ""
    return f"{float(value):.6f}"


def safe_mean(value_list: list[float]) -> float:

    """Return the finite-value mean."""

    finite_value_list = [float(value) for value in value_list if math.isfinite(float(value))]
    return mean(finite_value_list) if finite_value_list else math.nan


def percentile(value_list: list[float], percentile_value: float) -> float:

    """Compute a deterministic percentile from finite values."""

    clean_value_list = sorted(float(value) for value in value_list if math.isfinite(float(value)))
    if not clean_value_list:
        return math.nan
    if len(clean_value_list) == 1:
        return clean_value_list[0]
    fractional_index = (len(clean_value_list) - 1) * percentile_value / 100.0
    lower_index = math.floor(fractional_index)
    upper_index = math.ceil(fractional_index)
    if lower_index == upper_index:
        return clean_value_list[int(fractional_index)]
    weight = fractional_index - lower_index
    return clean_value_list[lower_index] + (clean_value_list[upper_index] - clean_value_list[lower_index]) * weight


def normalize_score(value: float, value_list: list[float], higher_is_better: bool = False) -> float:

    """Normalize one metric into a bounded zero-best score."""

    finite_value_list = [float(item) for item in value_list if math.isfinite(float(item))]
    if not finite_value_list or not math.isfinite(float(value)):
        return 1.0
    minimum_value = min(finite_value_list)
    maximum_value = max(finite_value_list)
    if math.isclose(minimum_value, maximum_value):
        return 0.0
    if higher_is_better:
        return float((maximum_value - value) / (maximum_value - minimum_value))
    return float((value - minimum_value) / (maximum_value - minimum_value))


def compute_correlation(left_array: np.ndarray, right_array: np.ndarray) -> float:

    """Compute Pearson correlation with constant-signal guards."""

    if left_array.size < 2 or right_array.size < 2:
        return math.nan
    if float(np.std(left_array)) <= 1.0e-12 or float(np.std(right_array)) <= 1.0e-12:
        return math.nan
    return float(np.corrcoef(left_array, right_array)[0, 1])


def compute_centered_array(value_array: np.ndarray) -> np.ndarray:

    """Return a mean-centered float array."""

    return value_array.astype(float) - float(np.mean(value_array.astype(float)))


def compute_moving_average(value_array: np.ndarray, window_size: int) -> np.ndarray:

    """Return an edge-padded moving average with a fixed odd window."""

    if window_size <= 1 or value_array.size < window_size:
        return value_array.astype(float)
    assert window_size % 2 == 1, "The smoothing window must be odd."
    pad_width = window_size // 2
    padded_array = np.pad(value_array.astype(float), pad_width=pad_width, mode="edge")
    kernel_array = np.ones(window_size, dtype=float) / float(window_size)
    return np.convolve(padded_array, kernel_array, mode="valid")


def compute_derivative_sign_agreement_rate(
    truth_derivative: np.ndarray,
    predicted_derivative: np.ndarray,
) -> float:

    """Compute derivative sign agreement while ignoring near-flat truth samples."""

    finite_mask = np.isfinite(truth_derivative) & np.isfinite(predicted_derivative)
    informative_mask = finite_mask & (np.abs(truth_derivative) > DERIVATIVE_SIGN_EPSILON)
    if not bool(np.any(informative_mask)):
        return math.nan
    truth_sign_array = np.sign(truth_derivative[informative_mask])
    predicted_sign_array = np.sign(predicted_derivative[informative_mask])
    return float(np.mean(truth_sign_array == predicted_sign_array))


def compute_fft_amplitude_similarity(truth_curve_deg: np.ndarray, predicted_curve_deg: np.ndarray) -> float:

    """Compute cosine similarity between centered real-FFT amplitude spectra."""

    truth_centered = truth_curve_deg.astype(float) - float(np.mean(truth_curve_deg.astype(float)))
    predicted_centered = predicted_curve_deg.astype(float) - float(np.mean(predicted_curve_deg.astype(float)))
    truth_amplitude = np.abs(np.fft.rfft(truth_centered))[1:]
    predicted_amplitude = np.abs(np.fft.rfft(predicted_centered))[1:]
    denominator = float(np.linalg.norm(truth_amplitude) * np.linalg.norm(predicted_amplitude))
    if denominator <= 1.0e-12:
        return math.nan
    return float(np.dot(truth_amplitude, predicted_amplitude) / denominator)


def prepare_curve_arrays(candidate_entry: dict[str, Any]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

    """Resolve finite sorted curve arrays with unique angular positions."""

    angle_deg_array = np.asarray(candidate_entry["angular_position_deg"], dtype=float)
    truth_curve_deg = np.asarray(candidate_entry["truth_curve_deg"], dtype=float)
    predicted_curve_deg = np.asarray(candidate_entry["predicted_curve_deg"], dtype=float)
    finite_mask = (
        np.isfinite(angle_deg_array)
        & np.isfinite(truth_curve_deg)
        & np.isfinite(predicted_curve_deg)
    )
    angle_deg_array = angle_deg_array[finite_mask]
    truth_curve_deg = truth_curve_deg[finite_mask]
    predicted_curve_deg = predicted_curve_deg[finite_mask]
    assert angle_deg_array.size >= 3, "A curve needs at least three finite samples for shape diagnostics."

    sorting_index_array = np.argsort(angle_deg_array)
    angle_deg_array = angle_deg_array[sorting_index_array]
    truth_curve_deg = truth_curve_deg[sorting_index_array]
    predicted_curve_deg = predicted_curve_deg[sorting_index_array]

    unique_angle_array, unique_index_array = np.unique(angle_deg_array, return_index=True)
    assert unique_angle_array.size >= 3, "A curve needs at least three unique angular samples for derivatives."
    return (
        unique_angle_array.astype(float),
        truth_curve_deg[unique_index_array].astype(float),
        predicted_curve_deg[unique_index_array].astype(float),
    )


def compute_dominant_harmonic_metrics(
    harmonic_row_list: list[dict[str, float]],
) -> tuple[int, float, float]:

    """Select the strongest truth harmonic and return retention and phase error."""

    finite_harmonic_row_list = [
        harmonic_row
        for harmonic_row in harmonic_row_list
        if math.isfinite(float(harmonic_row["truth_amplitude_deg"]))
        and float(harmonic_row["truth_amplitude_deg"]) > 1.0e-12
    ]
    if not finite_harmonic_row_list:
        return 0, math.nan, math.nan

    dominant_row = max(finite_harmonic_row_list, key=lambda row: float(row["truth_amplitude_deg"]))
    retention_pct = (
        float(dominant_row["predicted_amplitude_deg"])
        / max(float(dominant_row["truth_amplitude_deg"]), 1.0e-12)
        * 100.0
    )
    return (
        int(dominant_row["harmonic_order"]),
        retention_pct,
        float(dominant_row["phase_error_deg"]),
    )


def compute_shape_pass(metric: ShapeCurveMetric, thresholds: ShapeGateThresholds) -> bool:

    """Return whether one curve satisfies the shape gate."""

    return not build_shape_failure_reason_list(metric, thresholds)


def build_shape_failure_reason_list(metric: ShapeCurveMetric, thresholds: ShapeGateThresholds) -> list[str]:

    """Return the strict shape-gate failure reasons for one curve."""

    failure_reason_list: list[str] = []
    if metric.fft_amplitude_similarity < thresholds.minimum_fft_amplitude_similarity:
        failure_reason_list.append("fft_amplitude_similarity")
    if metric.mean_harmonic_amplitude_error_pct > thresholds.maximum_mean_harmonic_amplitude_error_pct:
        failure_reason_list.append("mean_harmonic_amplitude_error")
    if metric.mean_harmonic_phase_error_deg > thresholds.maximum_mean_harmonic_phase_error_deg:
        failure_reason_list.append("mean_harmonic_phase_error")
    if metric.peak_to_peak_error_pct > thresholds.maximum_peak_to_peak_error_pct:
        failure_reason_list.append("peak_to_peak_error")
    if not derivative_gate_passes(metric, thresholds):
        failure_reason_list.append("derivative_agreement")
    return failure_reason_list


def derivative_gate_passes(metric: ShapeCurveMetric, thresholds: ShapeGateThresholds) -> bool:

    """Return whether one curve passes at least one derivative-agreement screen."""

    return (
        metric.derivative_correlation >= thresholds.minimum_derivative_correlation
        or metric.smoothed_derivative_correlation >= thresholds.minimum_smoothed_derivative_correlation
        or metric.derivative_sign_agreement_rate >= thresholds.minimum_derivative_sign_agreement_rate
        or metric.normalized_derivative_rmse <= thresholds.maximum_normalized_derivative_rmse
    )


def near_pass_gate_passes(summary: ShapeCandidateSummary, thresholds: ShapeGateThresholds) -> bool:

    """Return whether a failed active candidate is close enough to keep under review."""

    derivative_near_pass = (
        summary.mean_derivative_sign_agreement_rate >= thresholds.near_pass_minimum_derivative_sign_agreement_rate
        or summary.mean_normalized_derivative_rmse <= thresholds.near_pass_maximum_normalized_derivative_rmse
    )
    return (
        summary.mean_fft_amplitude_similarity >= thresholds.near_pass_minimum_fft_amplitude_similarity
        and summary.mean_harmonic_amplitude_error_pct
        <= thresholds.near_pass_maximum_mean_harmonic_amplitude_error_pct
        and summary.mean_harmonic_phase_error_deg <= thresholds.near_pass_maximum_mean_harmonic_phase_error_deg
        and summary.mean_peak_to_peak_error_pct <= thresholds.near_pass_maximum_peak_to_peak_error_pct
        and derivative_near_pass
    )


def build_thresholds(arguments: argparse.Namespace) -> ShapeGateThresholds:

    """Build threshold configuration from CLI arguments."""

    return ShapeGateThresholds(
        minimum_fft_amplitude_similarity=float(arguments.minimum_fft_amplitude_similarity),
        minimum_derivative_correlation=float(arguments.minimum_derivative_correlation),
        minimum_smoothed_derivative_correlation=float(arguments.minimum_smoothed_derivative_correlation),
        minimum_derivative_sign_agreement_rate=float(arguments.minimum_derivative_sign_agreement_rate),
        maximum_normalized_derivative_rmse=float(arguments.maximum_normalized_derivative_rmse),
        maximum_mean_harmonic_amplitude_error_pct=float(arguments.maximum_mean_harmonic_amplitude_error_pct),
        maximum_mean_harmonic_phase_error_deg=float(arguments.maximum_mean_harmonic_phase_error_deg),
        maximum_peak_to_peak_error_pct=float(arguments.maximum_peak_to_peak_error_pct),
        minimum_per_curve_shape_pass_rate=float(arguments.minimum_per_curve_shape_pass_rate),
        near_pass_minimum_fft_amplitude_similarity=float(arguments.near_pass_minimum_fft_amplitude_similarity),
        near_pass_maximum_mean_harmonic_amplitude_error_pct=float(
            arguments.near_pass_maximum_mean_harmonic_amplitude_error_pct
        ),
        near_pass_maximum_mean_harmonic_phase_error_deg=float(
            arguments.near_pass_maximum_mean_harmonic_phase_error_deg
        ),
        near_pass_maximum_peak_to_peak_error_pct=float(arguments.near_pass_maximum_peak_to_peak_error_pct),
        near_pass_minimum_derivative_sign_agreement_rate=float(
            arguments.near_pass_minimum_derivative_sign_agreement_rate
        ),
        near_pass_maximum_normalized_derivative_rmse=float(arguments.near_pass_maximum_normalized_derivative_rmse),
    )


def resolve_timestamped_output_paths(
    output_root: Path,
    report_topic_root: Path,
    report_date: str | None,
) -> tuple[str, Path, Path]:

    """Resolve timestamped output and report directories."""

    current_timestamp = datetime.now().astimezone()
    run_instance_id = f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}__shape_gated_te_curve_reranker"
    if report_date is None:
        report_date = current_timestamp.strftime("%Y-%m-%d")
    else:
        datetime.strptime(report_date, "%Y-%m-%d")

    output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(output_root) / run_instance_id
    report_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(report_topic_root) / f"[{report_date}]"
    output_directory.mkdir(parents=True, exist_ok=True)
    report_directory.mkdir(parents=True, exist_ok=True)
    return run_instance_id, output_directory, report_directory


def load_training_config(config_path: Path, dataset_name: str) -> dict[str, Any]:

    """Load and prepare a selected-active TE Curve Verification config."""

    raw_training_config = reference_family_vs_feedforward_support.load_reference_family_comparison_config(config_path)
    training_config = shared_training_infrastructure.apply_dataset_override(raw_training_config, dataset_name)
    return shared_training_infrastructure.prepare_output_artifact_training_config(
        training_config,
        artifact_kind=shared_training_infrastructure.VALIDATION_OUTPUT_ARTIFACT_KIND,
        run_name_suffix="shape_gated_te_curve_reranker",
    )


def resolve_candidate_configuration_list(
    training_config: dict[str, Any],
    dataset_name: str,
    surface_scope: str,
    active_family_list: list[str],
) -> list[dict[str, Any]]:

    """Resolve the reduced candidate list for one dataset and surface."""

    candidate_configuration_list = reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(
        training_config
    )
    candidate_configuration_list = (
        run_reference_family_vs_feedforward_comparison.filter_candidate_configuration_list_by_dataset_scope(
            candidate_configuration_list,
            dataset_name,
        )
    )
    candidate_configuration_list = (
        run_reference_family_vs_feedforward_comparison.filter_candidate_configuration_list_by_surface_scope(
            candidate_configuration_list,
            surface_scope,
        )
    )
    active_family_set = {family_name.strip() for family_name in active_family_list}
    return [
        candidate_configuration
        for candidate_configuration in candidate_configuration_list
        if str(candidate_configuration["candidate_family"]) in active_family_set
    ]


def evaluate_surface_candidate_payloads(
    training_config: dict[str, Any],
    dataset_name: str,
    surface_scope: str,
    candidate_configuration_list: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[EvaluationFailure]]:

    """Evaluate selected candidates and return curve payload entries."""

    selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
    curve_record_list, _, _, _ = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    curve_record_list = run_reference_family_vs_feedforward_comparison.filter_curve_record_list_by_surface_scope(
        curve_record_list,
        surface_scope,
    )

    per_candidate_entry_list: list[dict[str, Any]] = []
    failure_list: list[EvaluationFailure] = []
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])
    for candidate_configuration in candidate_configuration_list:
        try:
            candidate = reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)
            candidate_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
                candidate,
                curve_record_list,
                percentage_error_denominator,
                include_curve_payload=True,
            )
            per_candidate_entry_list.extend(candidate_entry_list)
        except Exception as error:
            failure_list.append(
                EvaluationFailure(
                    candidate_id=str(candidate_configuration["candidate_id"]),
                    candidate_family=str(candidate_configuration["candidate_family"]),
                    candidate_kind=str(candidate_configuration["candidate_kind"]),
                    candidate_source_label=str(candidate_configuration["candidate_source_label"]),
                    candidate_surface=str(candidate_configuration["candidate_surface"]),
                    surface_scope=surface_scope,
                    error_type=type(error).__name__,
                    error_message=str(error).replace("\n", " ")[:500],
                )
            )

    return per_candidate_entry_list, failure_list


def compute_curve_metric(
    candidate_entry: dict[str, Any],
    harmonic_order_list: list[int],
    thresholds: ShapeGateThresholds,
) -> ShapeCurveMetric:

    """Compute one per-curve shape-gated metric."""

    angle_deg_array, truth_curve_deg, predicted_curve_deg = prepare_curve_arrays(candidate_entry)
    residual_curve_deg = predicted_curve_deg - truth_curve_deg
    metric_dictionary = candidate_entry["metrics"]

    truth_mean_deg = float(np.mean(truth_curve_deg))
    predicted_mean_deg = float(np.mean(predicted_curve_deg))
    truth_centered_deg = compute_centered_array(truth_curve_deg)
    predicted_centered_deg = compute_centered_array(predicted_curve_deg)
    centered_residual_deg = predicted_centered_deg - truth_centered_deg
    truth_peak_to_peak_deg = float(np.ptp(truth_curve_deg))
    predicted_peak_to_peak_deg = float(np.ptp(predicted_curve_deg))
    peak_denominator = truth_peak_to_peak_deg if truth_peak_to_peak_deg > 1.0e-12 else math.nan
    peak_to_peak_error_pct = (
        abs(predicted_peak_to_peak_deg - truth_peak_to_peak_deg) / peak_denominator * 100.0
        if math.isfinite(peak_denominator)
        else math.nan
    )

    truth_derivative = np.gradient(truth_curve_deg, angle_deg_array)
    predicted_derivative = np.gradient(predicted_curve_deg, angle_deg_array)
    truth_centered_derivative = np.gradient(truth_centered_deg, angle_deg_array)
    predicted_centered_derivative = np.gradient(predicted_centered_deg, angle_deg_array)
    smoothed_truth_curve_deg = compute_moving_average(truth_curve_deg, DERIVATIVE_SMOOTHING_WINDOW)
    smoothed_predicted_curve_deg = compute_moving_average(predicted_curve_deg, DERIVATIVE_SMOOTHING_WINDOW)
    smoothed_truth_derivative = np.gradient(smoothed_truth_curve_deg, angle_deg_array)
    smoothed_predicted_derivative = np.gradient(smoothed_predicted_curve_deg, angle_deg_array)
    derivative_difference = predicted_derivative - truth_derivative
    derivative_rmse_deg_per_deg = float(np.sqrt(np.mean(np.square(derivative_difference))))
    derivative_correlation = compute_correlation(truth_derivative, predicted_derivative)
    centered_derivative_correlation = compute_correlation(truth_centered_derivative, predicted_centered_derivative)
    smoothed_derivative_correlation = compute_correlation(smoothed_truth_derivative, smoothed_predicted_derivative)
    derivative_sign_agreement_rate = compute_derivative_sign_agreement_rate(truth_derivative, predicted_derivative)
    normalized_derivative_rmse = derivative_rmse_deg_per_deg / max(truth_peak_to_peak_deg, 1.0e-12)

    (
        mean_harmonic_amplitude_error_pct,
        mean_harmonic_phase_error_deg,
        _,
        _,
        harmonic_row_list,
    ) = track2c_diagnostics.compute_harmonic_diagnostics(
        truth_curve_deg=truth_curve_deg,
        predicted_curve_deg=predicted_curve_deg,
        angle_deg_array=angle_deg_array,
        harmonic_order_list=harmonic_order_list,
    )
    dominant_harmonic_order, dominant_retention_pct, dominant_phase_error_deg = compute_dominant_harmonic_metrics(
        harmonic_row_list
    )

    pending_metric = ShapeCurveMetric(
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
        raw_mae_deg=float(metric_dictionary["mae"]),
        raw_rmse_deg=float(metric_dictionary["rmse"]),
        mean_percentage_error_pct=float(metric_dictionary["mean_percentage_error_pct"]),
        p95_candidate_percentage_error_pct=math.nan,
        absolute_offset_error_deg=float(abs(predicted_mean_deg - truth_mean_deg)),
        centered_mae_deg=float(np.mean(np.abs(centered_residual_deg))),
        centered_rmse_deg=float(np.sqrt(np.mean(np.square(centered_residual_deg)))),
        peak_to_peak_error_pct=float(peak_to_peak_error_pct),
        fft_amplitude_similarity=compute_fft_amplitude_similarity(truth_curve_deg, predicted_curve_deg),
        dominant_harmonic_order=dominant_harmonic_order,
        dominant_harmonic_retention_pct=dominant_retention_pct,
        dominant_harmonic_phase_error_deg=dominant_phase_error_deg,
        mean_harmonic_amplitude_error_pct=mean_harmonic_amplitude_error_pct,
        mean_harmonic_phase_error_deg=mean_harmonic_phase_error_deg,
        derivative_correlation=derivative_correlation,
        centered_derivative_correlation=centered_derivative_correlation,
        smoothed_derivative_correlation=smoothed_derivative_correlation,
        derivative_sign_agreement_rate=derivative_sign_agreement_rate,
        derivative_rmse_deg_per_deg=derivative_rmse_deg_per_deg,
        normalized_derivative_rmse=normalized_derivative_rmse,
        shape_failure_reason="",
        shape_pass=False,
    )
    failure_reason_list = build_shape_failure_reason_list(pending_metric, thresholds)
    return ShapeCurveMetric(
        **{
            **pending_metric.__dict__,
            "shape_failure_reason": ";".join(failure_reason_list),
            "shape_pass": not failure_reason_list,
        }
    )


def attach_candidate_p95(metric_list: list[ShapeCurveMetric]) -> list[ShapeCurveMetric]:

    """Attach candidate-level P95 raw percentage error to every per-curve row."""

    candidate_metric_map: dict[str, list[ShapeCurveMetric]] = defaultdict(list)
    for metric in metric_list:
        candidate_metric_map[metric.candidate_id].append(metric)

    updated_metric_list: list[ShapeCurveMetric] = []
    for metric in metric_list:
        p95_value = percentile(
            [
                candidate_metric.mean_percentage_error_pct
                for candidate_metric in candidate_metric_map[metric.candidate_id]
            ],
            95.0,
        )
        updated_metric_list.append(
            ShapeCurveMetric(
                **{
                    **metric.__dict__,
                    "p95_candidate_percentage_error_pct": p95_value,
                }
            )
        )
    return updated_metric_list


def build_candidate_summary_list(
    per_curve_metric_list: list[ShapeCurveMetric],
    thresholds: ShapeGateThresholds,
    failure_list: list[EvaluationFailure],
) -> list[ShapeCandidateSummary]:

    """Build ranked candidate summaries from per-curve metrics."""

    grouped_metric_map: dict[str, list[ShapeCurveMetric]] = defaultdict(list)
    for metric in per_curve_metric_list:
        grouped_metric_map[metric.candidate_id].append(metric)

    pending_summary_list: list[ShapeCandidateSummary] = []
    for candidate_id, metric_list in sorted(grouped_metric_map.items()):
        first_metric = metric_list[0]
        pass_rate = safe_mean([1.0 if metric.shape_pass else 0.0 for metric in metric_list])
        failure_reason_counter: dict[str, int] = defaultdict(int)
        for metric in metric_list:
            for failure_reason in metric.shape_failure_reason.split(";"):
                if failure_reason:
                    failure_reason_counter[failure_reason] += 1
        dominant_failure_reason = ", ".join(
            f"{reason}:{count}" for reason, count in sorted(failure_reason_counter.items())
        )

        summary_dictionary = {
            "rank": 0,
            "candidate_id": candidate_id,
            "candidate_family": first_metric.candidate_family,
            "candidate_kind": first_metric.candidate_kind,
            "candidate_source_label": first_metric.candidate_source_label,
            "candidate_surface": first_metric.candidate_surface,
            "direction_label": first_metric.direction_label,
            "curve_count": len(metric_list),
            "mean_raw_mae_deg": safe_mean([metric.raw_mae_deg for metric in metric_list]),
            "mean_raw_rmse_deg": safe_mean([metric.raw_rmse_deg for metric in metric_list]),
            "mean_percentage_error_pct": safe_mean([metric.mean_percentage_error_pct for metric in metric_list]),
            "p95_mean_percentage_error_pct": percentile(
                [metric.mean_percentage_error_pct for metric in metric_list],
                95.0,
            ),
            "mean_absolute_offset_error_deg": safe_mean([metric.absolute_offset_error_deg for metric in metric_list]),
            "mean_centered_mae_deg": safe_mean([metric.centered_mae_deg for metric in metric_list]),
            "mean_centered_rmse_deg": safe_mean([metric.centered_rmse_deg for metric in metric_list]),
            "mean_peak_to_peak_error_pct": safe_mean([metric.peak_to_peak_error_pct for metric in metric_list]),
            "mean_fft_amplitude_similarity": safe_mean(
                [metric.fft_amplitude_similarity for metric in metric_list]
            ),
            "mean_dominant_harmonic_retention_pct": safe_mean(
                [metric.dominant_harmonic_retention_pct for metric in metric_list]
            ),
            "mean_dominant_harmonic_phase_error_deg": safe_mean(
                [metric.dominant_harmonic_phase_error_deg for metric in metric_list]
            ),
            "mean_harmonic_amplitude_error_pct": safe_mean(
                [metric.mean_harmonic_amplitude_error_pct for metric in metric_list]
            ),
            "mean_harmonic_phase_error_deg": safe_mean(
                [metric.mean_harmonic_phase_error_deg for metric in metric_list]
            ),
            "mean_derivative_correlation": safe_mean([metric.derivative_correlation for metric in metric_list]),
            "mean_smoothed_derivative_correlation": safe_mean(
                [metric.smoothed_derivative_correlation for metric in metric_list]
            ),
            "mean_derivative_sign_agreement_rate": safe_mean(
                [metric.derivative_sign_agreement_rate for metric in metric_list]
            ),
            "mean_derivative_rmse_deg_per_deg": safe_mean(
                [metric.derivative_rmse_deg_per_deg for metric in metric_list]
            ),
            "mean_normalized_derivative_rmse": safe_mean(
                [metric.normalized_derivative_rmse for metric in metric_list]
            ),
            "per_curve_shape_pass_rate": pass_rate,
            "raw_error_score": 0.0,
            "shape_score": 0.0,
            "harmonic_score": 0.0,
            "offset_score": 0.0,
            "robustness_score": 0.0,
            "composite_score": 0.0,
            "decision_label": "candidate",
            "veto_reason": "",
        }
        pending_summary = ShapeCandidateSummary(**summary_dictionary)

        decision_label = "candidate"
        veto_reason = ""
        if pass_rate < thresholds.minimum_per_curve_shape_pass_rate:
            if first_metric.candidate_family not in BASELINE_ANCHOR_FAMILY_SET and near_pass_gate_passes(
                pending_summary,
                thresholds,
            ):
                decision_label = "near_pass"
                veto_reason = "below strict pass rate but retained by aggregate near-pass screen"
            else:
                decision_label = "shape_gate_failed"
                veto_reason = f"per-curve shape pass rate below threshold; failures={dominant_failure_reason}"
        elif first_metric.candidate_family in BASELINE_ANCHOR_FAMILY_SET:
            decision_label = "baseline_anchor_only"

        pending_summary_list.append(
            ShapeCandidateSummary(
                **{
                    **summary_dictionary,
                    "decision_label": decision_label,
                    "veto_reason": veto_reason,
                }
            )
        )

    pending_summary_list.extend(build_failure_summary_list(failure_list))
    return rerank_candidate_summaries(add_block_scores(pending_summary_list))


def build_failure_summary_list(failure_list: list[EvaluationFailure]) -> list[ShapeCandidateSummary]:

    """Build insufficient-evidence summaries for candidates that failed evaluation."""

    return [
        ShapeCandidateSummary(
            rank=0,
            candidate_id=failure.candidate_id,
            candidate_family=failure.candidate_family,
            candidate_kind=failure.candidate_kind,
            candidate_source_label=failure.candidate_source_label,
            candidate_surface=failure.candidate_surface,
            direction_label=failure.surface_scope,
            curve_count=0,
            mean_raw_mae_deg=math.nan,
            mean_raw_rmse_deg=math.nan,
            mean_percentage_error_pct=math.nan,
            p95_mean_percentage_error_pct=math.nan,
            mean_absolute_offset_error_deg=math.nan,
            mean_centered_mae_deg=math.nan,
            mean_centered_rmse_deg=math.nan,
            mean_peak_to_peak_error_pct=math.nan,
            mean_fft_amplitude_similarity=math.nan,
            mean_dominant_harmonic_retention_pct=math.nan,
            mean_dominant_harmonic_phase_error_deg=math.nan,
            mean_harmonic_amplitude_error_pct=math.nan,
            mean_harmonic_phase_error_deg=math.nan,
            mean_derivative_correlation=math.nan,
            mean_smoothed_derivative_correlation=math.nan,
            mean_derivative_sign_agreement_rate=math.nan,
            mean_derivative_rmse_deg_per_deg=math.nan,
            mean_normalized_derivative_rmse=math.nan,
            per_curve_shape_pass_rate=0.0,
            raw_error_score=1.0,
            shape_score=1.0,
            harmonic_score=1.0,
            offset_score=1.0,
            robustness_score=1.0,
            composite_score=1.0,
            decision_label="insufficient_evidence",
            veto_reason=f"{failure.error_type}: {failure.error_message}",
        )
        for failure in failure_list
    ]


def add_block_scores(summary_list: list[ShapeCandidateSummary]) -> list[ShapeCandidateSummary]:

    """Attach normalized block scores and composite scores."""

    raw_mae_list = [summary.mean_raw_mae_deg for summary in summary_list]
    raw_rmse_list = [summary.mean_raw_rmse_deg for summary in summary_list]
    centered_mae_list = [summary.mean_centered_mae_deg for summary in summary_list]
    fft_similarity_list = [summary.mean_fft_amplitude_similarity for summary in summary_list]
    derivative_correlation_list = [summary.mean_derivative_correlation for summary in summary_list]
    smoothed_derivative_correlation_list = [
        summary.mean_smoothed_derivative_correlation for summary in summary_list
    ]
    derivative_sign_agreement_rate_list = [
        summary.mean_derivative_sign_agreement_rate for summary in summary_list
    ]
    normalized_derivative_rmse_list = [summary.mean_normalized_derivative_rmse for summary in summary_list]
    harmonic_amplitude_error_list = [summary.mean_harmonic_amplitude_error_pct for summary in summary_list]
    harmonic_phase_error_list = [summary.mean_harmonic_phase_error_deg for summary in summary_list]
    offset_error_list = [summary.mean_absolute_offset_error_deg for summary in summary_list]
    p95_percentage_error_list = [summary.p95_mean_percentage_error_pct for summary in summary_list]

    scored_summary_list: list[ShapeCandidateSummary] = []
    for summary in summary_list:
        raw_error_score = safe_mean(
            [
                normalize_score(summary.mean_raw_mae_deg, raw_mae_list),
                normalize_score(summary.mean_raw_rmse_deg, raw_rmse_list),
            ]
        )
        shape_score = safe_mean(
            [
                normalize_score(summary.mean_centered_mae_deg, centered_mae_list),
                normalize_score(summary.mean_fft_amplitude_similarity, fft_similarity_list, higher_is_better=True),
                normalize_score(summary.mean_derivative_correlation, derivative_correlation_list, higher_is_better=True),
                normalize_score(
                    summary.mean_smoothed_derivative_correlation,
                    smoothed_derivative_correlation_list,
                    higher_is_better=True,
                ),
                normalize_score(
                    summary.mean_derivative_sign_agreement_rate,
                    derivative_sign_agreement_rate_list,
                    higher_is_better=True,
                ),
                normalize_score(summary.mean_normalized_derivative_rmse, normalized_derivative_rmse_list),
            ]
        )
        harmonic_score = safe_mean(
            [
                normalize_score(summary.mean_harmonic_amplitude_error_pct, harmonic_amplitude_error_list),
                normalize_score(summary.mean_harmonic_phase_error_deg, harmonic_phase_error_list),
            ]
        )
        offset_score = normalize_score(summary.mean_absolute_offset_error_deg, offset_error_list)
        robustness_score = normalize_score(summary.p95_mean_percentage_error_pct, p95_percentage_error_list)
        composite_score = (
            0.35 * shape_score
            + 0.20 * raw_error_score
            + 0.20 * offset_score
            + 0.15 * robustness_score
            + 0.10 * harmonic_score
        )
        scored_summary_list.append(
            ShapeCandidateSummary(
                **{
                    **summary.__dict__,
                    "raw_error_score": raw_error_score,
                    "shape_score": shape_score,
                    "harmonic_score": harmonic_score,
                    "offset_score": offset_score,
                    "robustness_score": robustness_score,
                    "composite_score": composite_score,
                }
            )
        )
    return scored_summary_list


def rerank_candidate_summaries(summary_list: list[ShapeCandidateSummary]) -> list[ShapeCandidateSummary]:

    """Sort summaries and assign ranks plus recommendation labels."""

    ranked_summary_list: list[ShapeCandidateSummary] = []
    recommended_assigned = False
    for rank, summary in enumerate(sorted(summary_list, key=lambda item: item.ranking_key()), start=1):
        decision_label = summary.decision_label
        if not recommended_assigned and decision_label == "candidate":
            decision_label = "recommended_candidate"
            recommended_assigned = True
        ranked_summary_list.append(
            ShapeCandidateSummary(
                **{
                    **summary.__dict__,
                    "rank": rank,
                    "decision_label": decision_label,
                }
            )
        )
    return ranked_summary_list


def resolve_surface_scope_list(arguments: argparse.Namespace) -> list[str]:

    """Resolve CLI surface scopes."""

    return arguments.surface_scope if arguments.surface_scope else list(DEFAULT_SURFACE_SCOPE_LIST)


def build_shape_metrics_for_surface(
    training_config: dict[str, Any],
    dataset_name: str,
    surface_scope: str,
    active_family_list: list[str],
    harmonic_order_list: list[int],
    thresholds: ShapeGateThresholds,
) -> tuple[list[ShapeCurveMetric], list[EvaluationFailure]]:

    """Build all per-curve shape metrics for one surface."""

    candidate_configuration_list = resolve_candidate_configuration_list(
        training_config,
        dataset_name,
        surface_scope,
        active_family_list,
    )
    assert candidate_configuration_list, f"No active candidates resolved for surface scope | {surface_scope}"
    candidate_entry_list, failure_list = evaluate_surface_candidate_payloads(
        training_config,
        dataset_name,
        surface_scope,
        candidate_configuration_list,
    )
    metric_list = [
        compute_curve_metric(candidate_entry, harmonic_order_list, thresholds)
        for candidate_entry in candidate_entry_list
    ]
    return attach_candidate_p95(metric_list), failure_list


def build_threshold_sweep_row_list(
    per_curve_metric_list: list[ShapeCurveMetric],
    thresholds: ShapeGateThresholds,
) -> list[dict[str, Any]]:

    """Build compact derivative-threshold sweep rows for calibration review."""

    grouped_metric_map: dict[str, list[ShapeCurveMetric]] = defaultdict(list)
    for metric in per_curve_metric_list:
        grouped_metric_map[metric.candidate_id].append(metric)

    sweep_configuration_list = [
        (
            "strict_raw_derivative",
            f"raw_corr>={thresholds.minimum_derivative_correlation:.2f}",
            lambda metric: metric.derivative_correlation >= thresholds.minimum_derivative_correlation,
        ),
        (
            "strict_smoothed_derivative",
            f"smoothed_corr>={thresholds.minimum_smoothed_derivative_correlation:.2f}",
            lambda metric: metric.smoothed_derivative_correlation
            >= thresholds.minimum_smoothed_derivative_correlation,
        ),
        (
            "strict_sign_agreement",
            f"sign_agreement>={thresholds.minimum_derivative_sign_agreement_rate:.2f}",
            lambda metric: metric.derivative_sign_agreement_rate
            >= thresholds.minimum_derivative_sign_agreement_rate,
        ),
        (
            "strict_normalized_derivative_rmse",
            f"normalized_rmse<={thresholds.maximum_normalized_derivative_rmse:.2f}",
            lambda metric: metric.normalized_derivative_rmse <= thresholds.maximum_normalized_derivative_rmse,
        ),
        (
            "near_pass_sign_agreement",
            f"sign_agreement>={thresholds.near_pass_minimum_derivative_sign_agreement_rate:.2f}",
            lambda metric: metric.derivative_sign_agreement_rate
            >= thresholds.near_pass_minimum_derivative_sign_agreement_rate,
        ),
        (
            "near_pass_normalized_derivative_rmse",
            f"normalized_rmse<={thresholds.near_pass_maximum_normalized_derivative_rmse:.2f}",
            lambda metric: metric.normalized_derivative_rmse
            <= thresholds.near_pass_maximum_normalized_derivative_rmse,
        ),
    ]

    row_list: list[dict[str, Any]] = []
    for candidate_id, metric_list in sorted(grouped_metric_map.items()):
        first_metric = metric_list[0]
        non_derivative_pass_list = [
            metric.fft_amplitude_similarity >= thresholds.minimum_fft_amplitude_similarity
            and metric.mean_harmonic_amplitude_error_pct <= thresholds.maximum_mean_harmonic_amplitude_error_pct
            and metric.mean_harmonic_phase_error_deg <= thresholds.maximum_mean_harmonic_phase_error_deg
            and metric.peak_to_peak_error_pct <= thresholds.maximum_peak_to_peak_error_pct
            for metric in metric_list
        ]
        for sweep_name, sweep_rule, derivative_pass_function in sweep_configuration_list:
            curve_pass_list = [
                non_derivative_pass and derivative_pass_function(metric)
                for metric, non_derivative_pass in zip(metric_list, non_derivative_pass_list)
            ]
            pass_rate = safe_mean([1.0 if curve_pass else 0.0 for curve_pass in curve_pass_list])
            row_list.append(
                {
                    "candidate_id": candidate_id,
                    "candidate_family": first_metric.candidate_family,
                    "candidate_surface": first_metric.candidate_surface,
                    "direction_label": first_metric.direction_label,
                    "sweep_name": sweep_name,
                    "sweep_rule": sweep_rule,
                    "curve_count": len(metric_list),
                    "per_curve_shape_pass_rate": format_float(pass_rate),
                    "candidate_passes_threshold": str(
                        pass_rate >= thresholds.minimum_per_curve_shape_pass_rate
                    ).lower(),
                }
            )
    return row_list


def write_csv(csv_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write a CSV file from dictionaries."""

    assert row_list, f"Cannot write an empty CSV | {csv_path}"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=list(row_list[0].keys()), lineterminator="\n")
        csv_writer.writeheader()
        csv_writer.writerows(row_list)


def build_surface_decision_payload(
    run_instance_id: str,
    config_path: Path,
    dataset_name: str,
    surface_summary_map: dict[str, list[ShapeCandidateSummary]],
    thresholds: ShapeGateThresholds,
) -> dict[str, Any]:

    """Build a machine-readable reranking decision payload."""

    surface_payload_map: dict[str, Any] = {}
    for surface_scope, summary_list in surface_summary_map.items():
        recommended_summary = next(
            (summary for summary in summary_list if summary.decision_label == "recommended_candidate"),
            None,
        )
        surface_payload_map[surface_scope] = {
            "recommended_candidate": recommended_summary.candidate_id if recommended_summary else None,
            "summary_list": [summary.to_csv_row() for summary in summary_list],
        }

    return {
        "run_instance_id": run_instance_id,
        "config_path": shared_training_infrastructure.format_project_relative_path(config_path),
        "dataset_name": dataset_name,
        "thresholds": thresholds.__dict__,
        "surface_decisions": surface_payload_map,
    }


def build_report_markdown(
    run_instance_id: str,
    config_path: Path,
    dataset_name: str,
    surface_summary_map: dict[str, list[ShapeCandidateSummary]],
    thresholds: ShapeGateThresholds,
    output_directory: Path,
) -> str:

    """Build the human-readable shape-gated reranking report."""

    report_line_list = [
        "# Shape-Gated TE Curve Reranker Report",
        "",
        "## Overview",
        "",
        "This report applies a reduced forward/backward shape-first gate to the",
        "selected-active `TE Curve Verification Pipeline` candidate set. It does",
        "not run training and does not change the deployable runtime input",
        "contract.",
        "",
        "## Scope",
        "",
        f"- run instance: `{run_instance_id}`;",
        f"- config path: `{shared_training_infrastructure.format_project_relative_path(config_path)}`;",
        f"- dataset: `{dataset_name}`;",
        "- reduced surfaces: `forward`, `backward`;",
        "- `global` remains paused for this reduced selection pass;",
        "",
        "## Gate Thresholds",
        "",
        "| Metric | Threshold |",
        "| --- | ---: |",
        f"| FFT amplitude similarity | >= {thresholds.minimum_fft_amplitude_similarity:.3f} |",
        f"| Raw derivative correlation | >= {thresholds.minimum_derivative_correlation:.3f} |",
        f"| Smoothed derivative correlation | >= {thresholds.minimum_smoothed_derivative_correlation:.3f} |",
        f"| Derivative sign agreement rate | >= {thresholds.minimum_derivative_sign_agreement_rate:.3f} |",
        f"| Normalized derivative RMSE | <= {thresholds.maximum_normalized_derivative_rmse:.3f} |",
        f"| Mean harmonic amplitude error [%] | <= {thresholds.maximum_mean_harmonic_amplitude_error_pct:.3f} |",
        f"| Mean harmonic phase error [deg] | <= {thresholds.maximum_mean_harmonic_phase_error_deg:.3f} |",
        f"| Peak-to-peak error [%] | <= {thresholds.maximum_peak_to_peak_error_pct:.3f} |",
        f"| Per-curve shape pass rate | >= {thresholds.minimum_per_curve_shape_pass_rate:.3f} |",
        f"| Near-pass FFT amplitude similarity | >= {thresholds.near_pass_minimum_fft_amplitude_similarity:.3f} |",
        f"| Near-pass mean harmonic amplitude error [%] | <= {thresholds.near_pass_maximum_mean_harmonic_amplitude_error_pct:.3f} |",
        f"| Near-pass mean harmonic phase error [deg] | <= {thresholds.near_pass_maximum_mean_harmonic_phase_error_deg:.3f} |",
        f"| Near-pass peak-to-peak error [%] | <= {thresholds.near_pass_maximum_peak_to_peak_error_pct:.3f} |",
        f"| Near-pass derivative sign agreement rate | >= {thresholds.near_pass_minimum_derivative_sign_agreement_rate:.3f} |",
        f"| Near-pass normalized derivative RMSE | <= {thresholds.near_pass_maximum_normalized_derivative_rmse:.3f} |",
        "",
        "## Surface Decisions",
        "",
    ]

    for surface_scope, summary_list in surface_summary_map.items():
        report_line_list.extend(
            [
                f"### {surface_scope.title()}",
                "",
                "| Rank | Candidate | Label | Raw MAE [deg] | Centered MAE [deg] | FFT Similarity | Harmonic Amp Err [%] | Harmonic Phase Err [deg] | Raw Deriv Corr | Smoothed Deriv Corr | Deriv Sign Rate | Norm Deriv RMSE | Shape Pass Rate | Composite |",
                "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for summary in summary_list:
            report_line_list.append(
                f"| {summary.rank} | `{summary.candidate_id}` | `{summary.decision_label}` | "
                f"{summary.mean_raw_mae_deg:.6f} | "
                f"{summary.mean_centered_mae_deg:.6f} | "
                f"{summary.mean_fft_amplitude_similarity:.3f} | "
                f"{summary.mean_harmonic_amplitude_error_pct:.3f} | "
                f"{summary.mean_harmonic_phase_error_deg:.3f} | "
                f"{summary.mean_derivative_correlation:.3f} | "
                f"{summary.mean_smoothed_derivative_correlation:.3f} | "
                f"{summary.mean_derivative_sign_agreement_rate:.3f} | "
                f"{summary.mean_normalized_derivative_rmse:.3f} | "
                f"{summary.per_curve_shape_pass_rate:.3f} | "
                f"{summary.composite_score:.3f} |"
            )
        report_line_list.append("")

    report_line_list.extend(
        [
            "## Interpretation Rules",
            "",
            "- `recommended_candidate` is the first active candidate that passes the",
            "  shape gate after block-score reranking.",
            "- `baseline_anchor_only` entries remain useful references, but they do not",
            "  replace the active development baseline in this reduced pass.",
            "- `near_pass` entries miss the strict per-curve pass-rate gate but keep",
            "  enough aggregate FFT, harmonic, peak-to-peak, and derivative evidence",
            "  to remain visible for review.",
            "- `shape_gate_failed` entries may still have good scalar error, but they",
            "  are demoted until the curve-shape evidence improves.",
            "- `insufficient_evidence` entries could not be evaluated from their",
            "  referenced artifact and must not be promoted until provenance is",
            "  repaired.",
            "- All FFT, centered-shape, derivative, and harmonic diagnostics are",
            "  validation-time evidence only, not deployable runtime corrections.",
            "- The threshold sweep is calibration evidence only; it is not a second",
            "  promotion policy.",
            "",
            "## Output Artifacts",
            "",
            f"- per-curve metrics: `{shared_training_infrastructure.format_project_relative_path(output_directory / PER_CURVE_METRICS_FILENAME)}`;",
            f"- candidate summary: `{shared_training_infrastructure.format_project_relative_path(output_directory / CANDIDATE_SUMMARY_FILENAME)}`;",
            f"- threshold sweep: `{shared_training_infrastructure.format_project_relative_path(output_directory / THRESHOLD_SWEEP_FILENAME)}`;",
            f"- surface decisions: `{shared_training_infrastructure.format_project_relative_path(output_directory / SURFACE_DECISION_FILENAME)}`;",
        ]
    )
    return "\n".join(report_line_list) + "\n"


def build_report_filename(config_path: Path) -> str:

    """Build a report filename scoped to the evaluated config."""

    config_stem = shared_training_infrastructure.sanitize_name(config_path.stem)
    return f"{config_stem}_{REPORT_FILENAME}"


def main() -> None:

    """Run the command-line entry point."""

    arguments = parse_command_line_arguments()
    surface_scope_list = resolve_surface_scope_list(arguments)
    active_family_list = arguments.active_family_list or list(DEFAULT_ACTIVE_FAMILY_LIST)
    harmonic_order_list = arguments.harmonic_order_list or list(DEFAULT_HARMONIC_ORDER_LIST)
    thresholds = build_thresholds(arguments)

    run_instance_id, output_directory, report_directory = resolve_timestamped_output_paths(
        arguments.output_root,
        arguments.report_topic_root,
        arguments.report_date,
    )
    training_config = load_training_config(arguments.config_path, arguments.dataset)

    all_metric_list: list[ShapeCurveMetric] = []
    surface_summary_map: dict[str, list[ShapeCandidateSummary]] = {}
    for surface_scope in surface_scope_list:
        metric_list, failure_list = build_shape_metrics_for_surface(
            training_config,
            arguments.dataset,
            surface_scope,
            active_family_list,
            harmonic_order_list,
            thresholds,
        )
        all_metric_list.extend(metric_list)
        surface_summary_map[surface_scope] = build_candidate_summary_list(metric_list, thresholds, failure_list)

    write_csv(output_directory / PER_CURVE_METRICS_FILENAME, [metric.to_csv_row() for metric in all_metric_list])
    write_csv(
        output_directory / CANDIDATE_SUMMARY_FILENAME,
        [
            summary.to_csv_row()
            for surface_scope in surface_scope_list
            for summary in surface_summary_map[surface_scope]
        ],
    )
    write_csv(output_directory / THRESHOLD_SWEEP_FILENAME, build_threshold_sweep_row_list(all_metric_list, thresholds))

    decision_payload = build_surface_decision_payload(
        run_instance_id,
        arguments.config_path,
        arguments.dataset,
        surface_summary_map,
        thresholds,
    )
    with (output_directory / SURFACE_DECISION_FILENAME).open("w", encoding="utf-8", newline="\n") as yaml_file:
        yaml.safe_dump(decision_payload, yaml_file, sort_keys=False, allow_unicode=False)

    report_markdown = build_report_markdown(
        run_instance_id,
        arguments.config_path,
        arguments.dataset,
        surface_summary_map,
        thresholds,
        output_directory,
    )
    report_path = report_directory / build_report_filename(arguments.config_path)
    report_path.write_text(report_markdown, encoding="utf-8", newline="\n")
    print(f"[DONE] Shape-gated reranker report written | {report_path}")
    print(f"[DONE] Shape-gated reranker artifacts written | {output_directory}")


if __name__ == "__main__":
    main()
