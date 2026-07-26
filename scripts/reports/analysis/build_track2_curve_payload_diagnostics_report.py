"""Build CVP 1.2 curve-payload diagnostics for screened candidates."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import json
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
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "full_track2_matrix_template.yaml"
)
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_curve_payload_diagnostics"
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "curve_payload_diagnostics_report"
)
DEFAULT_CANDIDATE_ID_LIST = [
    "rcim_retuned_GBM19_Fw",
    "rcim_retuned_GBM19_Bw",
    "periodic_gru_sequence_Bw",
    "periodic_lstm_sequence_global",
    "residual_harmonic_lstm_sequence_sparse_rcim_Bw",
    "residual_harmonic_lstm_sequence_sparse_rcim_global",
    "harmonic_regression_Bw",
    "tree_Bw",
    "tree_global",
]
DEFAULT_HARMONIC_ORDER_LIST = [1, 2, 3, 4, 5, 6, 8, 10, 12, 19]

REPORT_FILENAME = "track2_curve_payload_diagnostics_report.md"
SUMMARY_FILENAME = "track2_curve_payload_diagnostics_summary.yaml"
CURVE_DIAGNOSTICS_FILENAME = "curve_payload_diagnostics.csv"
CANDIDATE_DIAGNOSTICS_FILENAME = "candidate_payload_diagnostics.csv"
HARMONIC_DIAGNOSTICS_FILENAME = "harmonic_payload_diagnostics.csv"
PAYLOAD_JSONL_FILENAME = "curve_payload_samples.jsonl"


@dataclass(frozen=True)
class CurveDiagnosticEntry:

    """One curve-payload diagnostic row."""

    candidate_id: str
    candidate_family: str
    candidate_source_label: str
    candidate_surface: str
    direction_label: str
    source_file_path: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    curve_mae_deg: float
    curve_rmse_deg: float
    mean_percentage_error_pct: float
    truth_peak_to_peak_deg: float
    predicted_peak_to_peak_deg: float
    peak_to_peak_error_pct: float
    residual_peak_to_peak_pct: float
    derivative_rmse_deg_per_deg: float
    residual_smoothness_deg_per_deg2: float
    residual_lag1_autocorrelation: float
    closure_mismatch_deg: float
    mean_harmonic_amplitude_error_pct: float
    mean_harmonic_phase_error_deg: float
    max_harmonic_amplitude_error_pct: float
    max_harmonic_phase_error_deg: float

    def to_csv_row(self) -> dict[str, Any]:

        """Return a stable CSV row."""

        return {
            "candidate_id": self.candidate_id,
            "candidate_family": self.candidate_family,
            "candidate_source_label": self.candidate_source_label,
            "candidate_surface": self.candidate_surface,
            "direction_label": self.direction_label,
            "source_file_path": self.source_file_path,
            "speed_rpm": format_float(self.speed_rpm),
            "torque_nm": format_float(self.torque_nm),
            "oil_temperature_deg": format_float(self.oil_temperature_deg),
            "curve_mae_deg": format_float(self.curve_mae_deg),
            "curve_rmse_deg": format_float(self.curve_rmse_deg),
            "mean_percentage_error_pct": format_float(self.mean_percentage_error_pct),
            "truth_peak_to_peak_deg": format_float(self.truth_peak_to_peak_deg),
            "predicted_peak_to_peak_deg": format_float(self.predicted_peak_to_peak_deg),
            "peak_to_peak_error_pct": format_float(self.peak_to_peak_error_pct),
            "residual_peak_to_peak_pct": format_float(self.residual_peak_to_peak_pct),
            "derivative_rmse_deg_per_deg": format_float(self.derivative_rmse_deg_per_deg),
            "residual_smoothness_deg_per_deg2": format_float(self.residual_smoothness_deg_per_deg2),
            "residual_lag1_autocorrelation": format_float(self.residual_lag1_autocorrelation),
            "closure_mismatch_deg": format_float(self.closure_mismatch_deg),
            "mean_harmonic_amplitude_error_pct": format_float(self.mean_harmonic_amplitude_error_pct),
            "mean_harmonic_phase_error_deg": format_float(self.mean_harmonic_phase_error_deg),
            "max_harmonic_amplitude_error_pct": format_float(self.max_harmonic_amplitude_error_pct),
            "max_harmonic_phase_error_deg": format_float(self.max_harmonic_phase_error_deg),
        }


@dataclass(frozen=True)
class CandidateDiagnosticSummary:

    """Aggregate diagnostics for one candidate."""

    rank: int
    candidate_id: str
    candidate_family: str
    candidate_source_label: str
    candidate_surface: str
    valid_direction_list: tuple[str, ...]
    curve_count: int
    mean_percentage_error_pct: float
    mean_curve_mae_deg: float
    mean_peak_to_peak_error_pct: float
    mean_residual_peak_to_peak_pct: float
    mean_derivative_rmse_deg_per_deg: float
    mean_residual_smoothness_deg_per_deg2: float
    mean_residual_lag1_autocorrelation: float
    mean_closure_mismatch_deg: float
    mean_stitched_boundary_mismatch_deg: float
    mean_harmonic_amplitude_error_pct: float
    mean_harmonic_phase_error_deg: float
    max_harmonic_amplitude_error_pct: float
    max_harmonic_phase_error_deg: float
    diagnostic_score: float

    def to_csv_row(self) -> dict[str, Any]:

        """Return a stable CSV row."""

        return {
            "rank": self.rank,
            "candidate_id": self.candidate_id,
            "candidate_family": self.candidate_family,
            "candidate_source_label": self.candidate_source_label,
            "candidate_surface": self.candidate_surface,
            "valid_direction_list": ", ".join(self.valid_direction_list),
            "curve_count": self.curve_count,
            "mean_percentage_error_pct": format_float(self.mean_percentage_error_pct),
            "mean_curve_mae_deg": format_float(self.mean_curve_mae_deg),
            "mean_peak_to_peak_error_pct": format_float(self.mean_peak_to_peak_error_pct),
            "mean_residual_peak_to_peak_pct": format_float(self.mean_residual_peak_to_peak_pct),
            "mean_derivative_rmse_deg_per_deg": format_float(self.mean_derivative_rmse_deg_per_deg),
            "mean_residual_smoothness_deg_per_deg2": format_float(self.mean_residual_smoothness_deg_per_deg2),
            "mean_residual_lag1_autocorrelation": format_float(self.mean_residual_lag1_autocorrelation),
            "mean_closure_mismatch_deg": format_float(self.mean_closure_mismatch_deg),
            "mean_stitched_boundary_mismatch_deg": format_float(self.mean_stitched_boundary_mismatch_deg),
            "mean_harmonic_amplitude_error_pct": format_float(self.mean_harmonic_amplitude_error_pct),
            "mean_harmonic_phase_error_deg": format_float(self.mean_harmonic_phase_error_deg),
            "max_harmonic_amplitude_error_pct": format_float(self.max_harmonic_amplitude_error_pct),
            "max_harmonic_phase_error_deg": format_float(self.max_harmonic_phase_error_deg),
            "diagnostic_score": format_float(self.diagnostic_score),
        }


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Generate CVP 1.2 curve-payload diagnostics for screened candidates "
            "without changing model inputs or launching training."
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
        help="Root for machine-readable diagnostics and payload samples.",
    )
    argument_parser.add_argument(
        "--report-topic-root",
        type=Path,
        default=DEFAULT_REPORT_TOPIC_ROOT,
        help="Root for the dated Markdown report bundle.",
    )
    argument_parser.add_argument(
        "--candidate-id",
        dest="candidate_id_list",
        action="append",
        default=None,
        help="Candidate id to evaluate. May be provided multiple times.",
    )
    argument_parser.add_argument(
        "--harmonic-order",
        dest="harmonic_order_list",
        action="append",
        type=int,
        default=None,
        help="Harmonic order to diagnose. May be provided multiple times.",
    )
    argument_parser.add_argument(
        "--report-date",
        type=str,
        default=None,
        help="Optional YYYY-MM-DD report bundle date.",
    )
    argument_parser.add_argument(
        "--max-payload-curves-per-candidate",
        type=int,
        default=3,
        help="Maximum number of downsampled curve payload samples to store per candidate.",
    )
    argument_parser.add_argument(
        "--payload-point-stride",
        type=int,
        default=50,
        help="Point stride used only when writing payload samples. Diagnostics use full curves.",
    )
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def format_float(value: float) -> str:

    """Format a numeric value for stable text output."""

    if math.isnan(value):
        return ""
    return f"{value:.6f}"


def safe_mean(value_list: list[float]) -> float:

    """Return the mean of finite values."""

    finite_value_list = [float(value) for value in value_list if math.isfinite(float(value))]
    return mean(finite_value_list) if finite_value_list else math.nan


def resolve_timestamped_output_paths(
    output_root: Path,
    report_topic_root: Path,
    report_date: str | None,
) -> tuple[str, Path, Path]:

    """Resolve timestamped output and report directories."""

    current_timestamp = datetime.now().astimezone()
    run_instance_id = (
        f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}"
        "__track2c_curve_payload_diagnostics"
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
    candidate_id_list: list[str],
) -> list[dict[str, Any]]:

    """Resolve and filter TE Curve Verification Pipeline candidate configurations."""

    candidate_configuration_list = (
        reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(training_config)
    )
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


def compute_wrapped_phase_error_deg(predicted_phase_rad: float, truth_phase_rad: float) -> float:

    """Compute absolute wrapped phase error in degrees."""

    phase_delta_rad = math.atan2(
        math.sin(predicted_phase_rad - truth_phase_rad),
        math.cos(predicted_phase_rad - truth_phase_rad),
    )
    return abs(math.degrees(phase_delta_rad))


def compute_harmonic_component(signal_array: np.ndarray, angle_deg_array: np.ndarray, harmonic_order: int) -> complex:

    """Estimate one harmonic coefficient using angular-position projection."""

    angle_rad_array = np.deg2rad(angle_deg_array.astype(float))
    centered_signal_array = signal_array.astype(float) - float(np.mean(signal_array.astype(float)))
    return complex(
        2.0
        * np.mean(
            centered_signal_array
            * np.exp(-1j * float(harmonic_order) * angle_rad_array)
        )
    )


def compute_harmonic_diagnostics(
    truth_curve_deg: np.ndarray,
    predicted_curve_deg: np.ndarray,
    angle_deg_array: np.ndarray,
    harmonic_order_list: list[int],
) -> tuple[float, float, float, float, list[dict[str, float]]]:

    """Compute selected-harmonic amplitude and phase diagnostics."""

    harmonic_component_list: list[tuple[int, complex, complex]] = []
    for harmonic_order in harmonic_order_list:
        truth_coefficient = compute_harmonic_component(truth_curve_deg, angle_deg_array, harmonic_order)
        predicted_coefficient = compute_harmonic_component(predicted_curve_deg, angle_deg_array, harmonic_order)
        harmonic_component_list.append((harmonic_order, truth_coefficient, predicted_coefficient))

    truth_amplitude_list = [
        abs(truth_coefficient)
        for _, truth_coefficient, _ in harmonic_component_list
    ]
    harmonic_amplitude_floor = max(max(truth_amplitude_list) * 0.01, 1.0e-12)
    harmonic_row_list: list[dict[str, float]] = []
    amplitude_error_pct_list: list[float] = []
    phase_error_deg_list: list[float] = []
    for harmonic_order, truth_coefficient, predicted_coefficient in harmonic_component_list:
        truth_amplitude = abs(truth_coefficient)
        predicted_amplitude = abs(predicted_coefficient)
        amplitude_error_pct = (
            abs(predicted_amplitude - truth_amplitude) / truth_amplitude * 100.0
            if truth_amplitude > harmonic_amplitude_floor
            else math.nan
        )
        phase_error_deg = (
            compute_wrapped_phase_error_deg(
                predicted_phase_rad=float(np.angle(predicted_coefficient)),
                truth_phase_rad=float(np.angle(truth_coefficient)),
            )
            if truth_amplitude > harmonic_amplitude_floor
            else math.nan
        )
        harmonic_row = {
            "harmonic_order": float(harmonic_order),
            "truth_amplitude_deg": float(truth_amplitude),
            "predicted_amplitude_deg": float(predicted_amplitude),
            "amplitude_error_pct": float(amplitude_error_pct),
            "phase_error_deg": float(phase_error_deg),
        }
        harmonic_row_list.append(harmonic_row)
        if math.isfinite(amplitude_error_pct):
            amplitude_error_pct_list.append(float(amplitude_error_pct))
        if math.isfinite(phase_error_deg):
            phase_error_deg_list.append(float(phase_error_deg))

    return (
        safe_mean(amplitude_error_pct_list),
        safe_mean(phase_error_deg_list),
        max(amplitude_error_pct_list) if amplitude_error_pct_list else math.nan,
        max(phase_error_deg_list) if phase_error_deg_list else math.nan,
        harmonic_row_list,
    )


def compute_curve_diagnostic_entry(
    candidate_entry: dict[str, Any],
    harmonic_order_list: list[int],
) -> tuple[CurveDiagnosticEntry, list[dict[str, float]]]:

    """Compute diagnostics for one candidate curve payload."""

    angle_deg_array = np.asarray(candidate_entry["angular_position_deg"], dtype=float)
    truth_curve_deg = np.asarray(candidate_entry["truth_curve_deg"], dtype=float)
    predicted_curve_deg = np.asarray(candidate_entry["predicted_curve_deg"], dtype=float)
    residual_curve_deg = predicted_curve_deg - truth_curve_deg
    metric_dictionary = candidate_entry["metrics"]

    truth_peak_to_peak_deg = float(np.ptp(truth_curve_deg))
    predicted_peak_to_peak_deg = float(np.ptp(predicted_curve_deg))
    residual_peak_to_peak_deg = float(np.ptp(residual_curve_deg))
    denominator = truth_peak_to_peak_deg if truth_peak_to_peak_deg > 1.0e-12 else math.nan
    peak_to_peak_error_pct = abs(predicted_peak_to_peak_deg - truth_peak_to_peak_deg) / denominator * 100.0
    residual_peak_to_peak_pct = residual_peak_to_peak_deg / denominator * 100.0

    truth_derivative = np.gradient(truth_curve_deg, angle_deg_array)
    predicted_derivative = np.gradient(predicted_curve_deg, angle_deg_array)
    residual_second_derivative = np.gradient(np.gradient(residual_curve_deg, angle_deg_array), angle_deg_array)
    derivative_rmse_deg_per_deg = float(
        np.sqrt(np.mean(np.square(predicted_derivative - truth_derivative)))
    )
    residual_smoothness_deg_per_deg2 = float(np.sqrt(np.mean(np.square(residual_second_derivative))))
    residual_lag1_autocorrelation = compute_lag1_autocorrelation(residual_curve_deg)
    closure_mismatch_deg = float(abs(residual_curve_deg[-1] - residual_curve_deg[0]))

    (
        mean_harmonic_amplitude_error_pct,
        mean_harmonic_phase_error_deg,
        max_harmonic_amplitude_error_pct,
        max_harmonic_phase_error_deg,
        harmonic_row_list,
    ) = compute_harmonic_diagnostics(
        truth_curve_deg=truth_curve_deg,
        predicted_curve_deg=predicted_curve_deg,
        angle_deg_array=angle_deg_array,
        harmonic_order_list=harmonic_order_list,
    )

    diagnostic_entry = CurveDiagnosticEntry(
        candidate_id=str(candidate_entry["candidate_id"]),
        candidate_family=str(candidate_entry["candidate_family"]),
        candidate_source_label=str(candidate_entry["candidate_source_label"]),
        candidate_surface=str(candidate_entry["candidate_surface"]),
        direction_label=str(candidate_entry["direction_label"]),
        source_file_path=str(candidate_entry["source_file_path"]),
        speed_rpm=float(candidate_entry["speed_rpm"]),
        torque_nm=float(candidate_entry["torque_nm"]),
        oil_temperature_deg=float(candidate_entry["oil_temperature_deg"]),
        curve_mae_deg=float(metric_dictionary["mae"]),
        curve_rmse_deg=float(metric_dictionary["rmse"]),
        mean_percentage_error_pct=float(metric_dictionary["mean_percentage_error_pct"]),
        truth_peak_to_peak_deg=truth_peak_to_peak_deg,
        predicted_peak_to_peak_deg=predicted_peak_to_peak_deg,
        peak_to_peak_error_pct=float(peak_to_peak_error_pct),
        residual_peak_to_peak_pct=float(residual_peak_to_peak_pct),
        derivative_rmse_deg_per_deg=derivative_rmse_deg_per_deg,
        residual_smoothness_deg_per_deg2=residual_smoothness_deg_per_deg2,
        residual_lag1_autocorrelation=residual_lag1_autocorrelation,
        closure_mismatch_deg=closure_mismatch_deg,
        mean_harmonic_amplitude_error_pct=mean_harmonic_amplitude_error_pct,
        mean_harmonic_phase_error_deg=mean_harmonic_phase_error_deg,
        max_harmonic_amplitude_error_pct=max_harmonic_amplitude_error_pct,
        max_harmonic_phase_error_deg=max_harmonic_phase_error_deg,
    )
    return diagnostic_entry, harmonic_row_list


def compute_lag1_autocorrelation(value_array: np.ndarray) -> float:

    """Compute lag-one autocorrelation for a residual curve."""

    if value_array.shape[0] < 3:
        return math.nan
    leading_array = value_array[:-1] - float(np.mean(value_array[:-1]))
    trailing_array = value_array[1:] - float(np.mean(value_array[1:]))
    denominator = float(np.linalg.norm(leading_array) * np.linalg.norm(trailing_array))
    if denominator <= 1.0e-12:
        return math.nan
    return float(np.dot(leading_array, trailing_array) / denominator)


def compute_stitched_boundary_mismatch(entry_list: list[CurveDiagnosticEntry]) -> float:

    """Compute a deterministic surrogate stitched-curve boundary mismatch."""

    sorted_entry_list = sorted(
        entry_list,
        key=lambda entry: (
            entry.direction_label,
            entry.speed_rpm,
            entry.torque_nm,
            entry.oil_temperature_deg,
            entry.source_file_path,
        ),
    )
    if len(sorted_entry_list) < 2:
        return math.nan

    # The script stores closure mismatch per curve, so use adjacent closure
    # jumps as a deterministic surrogate until real chronological runs exist.
    mismatch_list = [
        abs(sorted_entry_list[index].closure_mismatch_deg - sorted_entry_list[index - 1].closure_mismatch_deg)
        for index in range(1, len(sorted_entry_list))
    ]
    return safe_mean(mismatch_list)


def compute_candidate_summary_list(
    curve_diagnostic_entry_list: list[CurveDiagnosticEntry],
) -> list[CandidateDiagnosticSummary]:

    """Aggregate curve diagnostics by candidate."""

    candidate_entry_map: dict[str, list[CurveDiagnosticEntry]] = defaultdict(list)
    for diagnostic_entry in curve_diagnostic_entry_list:
        candidate_entry_map[diagnostic_entry.candidate_id].append(diagnostic_entry)

    summary_list: list[CandidateDiagnosticSummary] = []
    for candidate_id, entry_list in candidate_entry_map.items():
        first_entry = entry_list[0]
        valid_direction_list = tuple(sorted({entry.direction_label for entry in entry_list}))
        mean_stitched_boundary_mismatch_deg = compute_stitched_boundary_mismatch(entry_list)
        diagnostic_score = (
            safe_mean([entry.mean_percentage_error_pct for entry in entry_list])
            + 0.10 * safe_mean([entry.mean_harmonic_amplitude_error_pct for entry in entry_list])
            + 0.05 * safe_mean([entry.mean_harmonic_phase_error_deg for entry in entry_list])
            + 10.0 * safe_mean([entry.derivative_rmse_deg_per_deg for entry in entry_list])
        )
        summary_list.append(
            CandidateDiagnosticSummary(
                rank=0,
                candidate_id=candidate_id,
                candidate_family=first_entry.candidate_family,
                candidate_source_label=first_entry.candidate_source_label,
                candidate_surface=first_entry.candidate_surface,
                valid_direction_list=valid_direction_list,
                curve_count=len(entry_list),
                mean_percentage_error_pct=safe_mean([entry.mean_percentage_error_pct for entry in entry_list]),
                mean_curve_mae_deg=safe_mean([entry.curve_mae_deg for entry in entry_list]),
                mean_peak_to_peak_error_pct=safe_mean([entry.peak_to_peak_error_pct for entry in entry_list]),
                mean_residual_peak_to_peak_pct=safe_mean([entry.residual_peak_to_peak_pct for entry in entry_list]),
                mean_derivative_rmse_deg_per_deg=safe_mean(
                    [entry.derivative_rmse_deg_per_deg for entry in entry_list]
                ),
                mean_residual_smoothness_deg_per_deg2=safe_mean(
                    [entry.residual_smoothness_deg_per_deg2 for entry in entry_list]
                ),
                mean_residual_lag1_autocorrelation=safe_mean(
                    [entry.residual_lag1_autocorrelation for entry in entry_list]
                ),
                mean_closure_mismatch_deg=safe_mean([entry.closure_mismatch_deg for entry in entry_list]),
                mean_stitched_boundary_mismatch_deg=mean_stitched_boundary_mismatch_deg,
                mean_harmonic_amplitude_error_pct=safe_mean(
                    [entry.mean_harmonic_amplitude_error_pct for entry in entry_list]
                ),
                mean_harmonic_phase_error_deg=safe_mean(
                    [entry.mean_harmonic_phase_error_deg for entry in entry_list]
                ),
                max_harmonic_amplitude_error_pct=max(
                    entry.max_harmonic_amplitude_error_pct
                    for entry in entry_list
                    if math.isfinite(entry.max_harmonic_amplitude_error_pct)
                ),
                max_harmonic_phase_error_deg=max(
                    entry.max_harmonic_phase_error_deg
                    for entry in entry_list
                    if math.isfinite(entry.max_harmonic_phase_error_deg)
                ),
                diagnostic_score=diagnostic_score,
            )
        )

    sorted_summary_list = sorted(
        summary_list,
        key=lambda summary: (
            summary.diagnostic_score,
            summary.mean_percentage_error_pct,
            summary.mean_harmonic_phase_error_deg,
            summary.candidate_id,
        ),
    )
    return [
        CandidateDiagnosticSummary(
            rank=index,
            candidate_id=summary.candidate_id,
            candidate_family=summary.candidate_family,
            candidate_source_label=summary.candidate_source_label,
            candidate_surface=summary.candidate_surface,
            valid_direction_list=summary.valid_direction_list,
            curve_count=summary.curve_count,
            mean_percentage_error_pct=summary.mean_percentage_error_pct,
            mean_curve_mae_deg=summary.mean_curve_mae_deg,
            mean_peak_to_peak_error_pct=summary.mean_peak_to_peak_error_pct,
            mean_residual_peak_to_peak_pct=summary.mean_residual_peak_to_peak_pct,
            mean_derivative_rmse_deg_per_deg=summary.mean_derivative_rmse_deg_per_deg,
            mean_residual_smoothness_deg_per_deg2=summary.mean_residual_smoothness_deg_per_deg2,
            mean_residual_lag1_autocorrelation=summary.mean_residual_lag1_autocorrelation,
            mean_closure_mismatch_deg=summary.mean_closure_mismatch_deg,
            mean_stitched_boundary_mismatch_deg=summary.mean_stitched_boundary_mismatch_deg,
            mean_harmonic_amplitude_error_pct=summary.mean_harmonic_amplitude_error_pct,
            mean_harmonic_phase_error_deg=summary.mean_harmonic_phase_error_deg,
            max_harmonic_amplitude_error_pct=summary.max_harmonic_amplitude_error_pct,
            max_harmonic_phase_error_deg=summary.max_harmonic_phase_error_deg,
            diagnostic_score=summary.diagnostic_score,
        )
        for index, summary in enumerate(sorted_summary_list, start=1)
    ]


def write_csv(csv_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write a CSV file with stable newline behavior."""

    field_name_list = list(row_list[0].keys()) if row_list else []
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_list, lineterminator="\n")
        writer.writeheader()
        for row in row_list:
            writer.writerow(row)


def write_payload_sample_jsonl(
    payload_path: Path,
    candidate_entry_list: list[dict[str, Any]],
    harmonic_diagnostic_map: dict[tuple[str, str], list[dict[str, float]]],
    max_payload_curves_per_candidate: int,
    payload_point_stride: int,
) -> None:

    """Write limited downsampled curve payload samples for inspection."""

    candidate_payload_count_map: dict[str, int] = defaultdict(int)
    point_stride = max(1, int(payload_point_stride))
    with payload_path.open("w", encoding="utf-8", newline="\n") as payload_file:
        for candidate_entry in candidate_entry_list:
            candidate_id = str(candidate_entry["candidate_id"])
            if candidate_payload_count_map[candidate_id] >= max_payload_curves_per_candidate:
                continue
            source_file_path = str(candidate_entry["source_file_path"])
            payload_record = {
                "candidate_id": candidate_id,
                "candidate_family": candidate_entry["candidate_family"],
                "candidate_source_label": candidate_entry["candidate_source_label"],
                "candidate_surface": candidate_entry["candidate_surface"],
                "direction_label": candidate_entry["direction_label"],
                "source_file_path": source_file_path,
                "speed_rpm": candidate_entry["speed_rpm"],
                "torque_nm": candidate_entry["torque_nm"],
                "oil_temperature_deg": candidate_entry["oil_temperature_deg"],
                "payload_point_stride": point_stride,
                "angular_position_deg": candidate_entry["angular_position_deg"][::point_stride],
                "truth_curve_deg": candidate_entry["truth_curve_deg"][::point_stride],
                "predicted_curve_deg": candidate_entry["predicted_curve_deg"][::point_stride],
                "harmonic_diagnostics": harmonic_diagnostic_map[(candidate_id, source_file_path)],
            }
            payload_file.write(json.dumps(payload_record, sort_keys=True) + "\n")
            candidate_payload_count_map[candidate_id] += 1


def markdown_table(header_list: list[str], row_list: list[list[str]]) -> list[str]:

    """Build a Markdown table."""

    line_list = [
        "| " + " | ".join(header_list) + " |",
        "| " + " | ".join(["---"] * len(header_list)) + " |",
    ]
    for row in row_list:
        line_list.append("| " + " | ".join(row) + " |")
    return line_list


def build_report_lines(
    run_instance_id: str,
    config_path: Path,
    output_directory: Path,
    candidate_summary_list: list[CandidateDiagnosticSummary],
    harmonic_order_list: list[int],
    curve_payload_count: int,
) -> list[str]:

    """Build the Markdown report body."""

    line_list = [
        "# CVP 1.2 Curve Payload Diagnostics Report",
        "",
        "## Overview",
        "",
        (
            "This report evaluates a screened `TE Curve Verification Pipeline` candidate set with full "
            "truth/prediction curve payloads. It does not train models, alter the "
            "dataset structure, or provide future curve samples to runtime model inputs."
        ),
        "",
        f"- Run Instance: `{run_instance_id}`",
        f"- Config Path: `{config_path.relative_to(PROJECT_PATH)}`",
        f"- Output Directory: `{output_directory.relative_to(PROJECT_PATH)}`",
        f"- Evaluated Curve Payload Count: `{curve_payload_count}`",
        f"- Harmonic Orders: `{', '.join(str(order) for order in harmonic_order_list)}`",
        "- Stored payload samples are downsampled for repository-size control.",
        "",
        "## Method",
        "",
        (
            "Diagnostics are computed on full held-out `TE` curves after each "
            "candidate produces pointwise predictions through its normal causal "
            "input path. The report separates the validation surface from the "
            "runtime input contract."
        ),
        "",
        "Computed diagnostics:",
        "",
        "- peak-to-peak amplitude error and residual peak-to-peak ratio;",
        "- selected-harmonic amplitude and wrapped phase error;",
        "- local derivative `RMSE`;",
        "- residual second-derivative smoothness;",
        "- residual lag-one autocorrelation;",
        "- per-revolution closure mismatch and deterministic stitched-boundary surrogate.",
        "",
        "## Candidate Diagnostic Ranking",
        "",
    ]
    table_row_list = []
    for summary in candidate_summary_list:
        table_row_list.append(
            [
                str(summary.rank),
                f"`{summary.candidate_id}`",
                f"`{summary.candidate_family}`",
                summary.candidate_surface,
                ", ".join(summary.valid_direction_list),
                str(summary.curve_count),
                format_float(summary.mean_percentage_error_pct),
                format_float(summary.mean_harmonic_amplitude_error_pct),
                format_float(summary.mean_harmonic_phase_error_deg),
                format_float(summary.mean_peak_to_peak_error_pct),
                format_float(summary.mean_derivative_rmse_deg_per_deg),
                format_float(summary.mean_closure_mismatch_deg),
                format_float(summary.diagnostic_score),
            ]
        )
    line_list.extend(
        markdown_table(
            [
                "Rank",
                "Candidate",
                "Family",
                "Surface",
                "Directions",
                "Curves",
                "Mean MPE [%]",
                "Mean Harmonic Amp Error [%]",
                "Mean Harmonic Phase Error [deg]",
                "Mean P2P Error [%]",
                "Derivative RMSE",
                "Closure Mismatch [deg]",
                "Diagnostic Score",
            ],
            table_row_list,
        )
    )
    line_list.extend(
        [
            "",
            "## Interpretation",
            "",
        ]
    )
    best_summary = candidate_summary_list[0]
    line_list.extend(
        [
            (
                f"The strongest screened diagnostic score is `{best_summary.candidate_id}`. "
                "The score is an analysis aid, not a registry-promotion rule."
            ),
            "",
            (
                "Paper-reference and tree-bank candidates may remain strong on curve "
                "shape metrics while still being less attractive for deployment. "
                "Repository-owned neural candidates should therefore be judged by both "
                "diagnostic behavior and future export/runtime feasibility."
            ),
            "",
            "## Decision",
            "",
            (
                "The next work should not start from `tree` only because of scalar "
                "strength. The practical direction is a set of parallel curve-aware "
                "retraining or reranking branches: keep searching the `Fw` surface "
                "for a deployable repository-owned candidate, prioritize periodic "
                "temporal candidates on the `Bw` surface, and carry the best neural "
                "`global` candidate as a dedicated cross-direction surface. "
                "Harmonic/phase-aware validation stays separate from runtime inputs."
            ),
            "",
            "## Runtime Input Boundary",
            "",
            (
                "All diagnostics are computed after prediction. Candidate models still "
                "consume only current point-level operating state, supported short "
                "causal history, or derived causal features. Full curves remain a "
                "validation and promotion surface only."
            ),
            "",
            "## Machine-Readable Artifacts",
            "",
            f"- `{(output_directory / CANDIDATE_DIAGNOSTICS_FILENAME).relative_to(PROJECT_PATH)}`",
            f"- `{(output_directory / CURVE_DIAGNOSTICS_FILENAME).relative_to(PROJECT_PATH)}`",
            f"- `{(output_directory / HARMONIC_DIAGNOSTICS_FILENAME).relative_to(PROJECT_PATH)}`",
            f"- `{(output_directory / PAYLOAD_JSONL_FILENAME).relative_to(PROJECT_PATH)}`",
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
    candidate_summary_list: list[CandidateDiagnosticSummary],
    harmonic_order_list: list[int],
) -> None:

    """Write a machine-readable diagnostics summary."""

    summary_payload = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "config_path": str(config_path.relative_to(PROJECT_PATH)),
        "output_directory": str(output_directory.relative_to(PROJECT_PATH)),
        "report_path": str(report_path.relative_to(PROJECT_PATH)),
        "harmonic_order_list": harmonic_order_list,
        "ranking_policy": {
            "diagnostic_score": (
                "mean_mpe + 0.10 * mean_harmonic_amplitude_error_pct + "
                "0.05 * mean_harmonic_phase_error_deg + 10.0 * derivative_rmse"
            ),
            "direction": "minimize",
            "registry_promotion": "not_automatic",
        },
        "best_candidate": candidate_summary_list[0].to_csv_row() if candidate_summary_list else {},
        "candidate_summary_list": [
            summary.to_csv_row()
            for summary in candidate_summary_list
        ],
    }
    with summary_path.open("w", encoding="utf-8") as summary_file:
        yaml.safe_dump(summary_payload, summary_file, sort_keys=False, allow_unicode=False)


def main() -> None:

    """Run the CVP 1.2 diagnostics workflow."""

    arguments = parse_command_line_arguments()
    candidate_id_list = arguments.candidate_id_list or DEFAULT_CANDIDATE_ID_LIST
    harmonic_order_list = arguments.harmonic_order_list or DEFAULT_HARMONIC_ORDER_LIST
    resolved_config_path = shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.config_path)
    run_instance_id, output_directory, report_directory = resolve_timestamped_output_paths(
        output_root=arguments.output_root,
        report_topic_root=arguments.report_topic_root,
        report_date=arguments.report_date,
    )
    report_path = report_directory / REPORT_FILENAME

    training_config = load_training_config(resolved_config_path, output_suffix=run_instance_id)
    selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
    candidate_configuration_list = filter_candidate_configuration_list(training_config, candidate_id_list)
    curve_record_list, _, _, _ = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])

    all_candidate_entry_list: list[dict[str, Any]] = []
    curve_diagnostic_entry_list: list[CurveDiagnosticEntry] = []
    harmonic_diagnostic_row_list: list[dict[str, Any]] = []
    harmonic_diagnostic_map: dict[tuple[str, str], list[dict[str, float]]] = {}
    for candidate_index, candidate_configuration in enumerate(candidate_configuration_list, start=1):
        print(
            "[INFO] Evaluating CVP 1.2 candidate | "
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
            diagnostic_entry, harmonic_row_list = compute_curve_diagnostic_entry(
                candidate_entry,
                harmonic_order_list,
            )
            curve_diagnostic_entry_list.append(diagnostic_entry)
            harmonic_diagnostic_map[(diagnostic_entry.candidate_id, diagnostic_entry.source_file_path)] = harmonic_row_list
            for harmonic_row in harmonic_row_list:
                harmonic_diagnostic_row_list.append(
                    {
                        "candidate_id": diagnostic_entry.candidate_id,
                        "candidate_family": diagnostic_entry.candidate_family,
                        "candidate_source_label": diagnostic_entry.candidate_source_label,
                        "candidate_surface": diagnostic_entry.candidate_surface,
                        "direction_label": diagnostic_entry.direction_label,
                        "source_file_path": diagnostic_entry.source_file_path,
                        "speed_rpm": format_float(diagnostic_entry.speed_rpm),
                        "torque_nm": format_float(diagnostic_entry.torque_nm),
                        "oil_temperature_deg": format_float(
                            diagnostic_entry.oil_temperature_deg
                        ),
                        "harmonic_order": int(harmonic_row["harmonic_order"]),
                        "truth_amplitude_deg": format_float(
                            harmonic_row["truth_amplitude_deg"]
                        ),
                        "predicted_amplitude_deg": format_float(
                            harmonic_row["predicted_amplitude_deg"]
                        ),
                        "amplitude_error_pct": format_float(
                            harmonic_row["amplitude_error_pct"]
                        ),
                        "phase_error_deg": format_float(
                            harmonic_row["phase_error_deg"]
                        ),
                    }
                )
        all_candidate_entry_list.extend(candidate_entry_list)

    candidate_summary_list = compute_candidate_summary_list(curve_diagnostic_entry_list)
    write_csv(
        output_directory / CURVE_DIAGNOSTICS_FILENAME,
        [entry.to_csv_row() for entry in curve_diagnostic_entry_list],
    )
    write_csv(
        output_directory / CANDIDATE_DIAGNOSTICS_FILENAME,
        [summary.to_csv_row() for summary in candidate_summary_list],
    )
    write_csv(
        output_directory / HARMONIC_DIAGNOSTICS_FILENAME,
        harmonic_diagnostic_row_list,
    )
    write_payload_sample_jsonl(
        payload_path=output_directory / PAYLOAD_JSONL_FILENAME,
        candidate_entry_list=all_candidate_entry_list,
        harmonic_diagnostic_map=harmonic_diagnostic_map,
        max_payload_curves_per_candidate=int(arguments.max_payload_curves_per_candidate),
        payload_point_stride=int(arguments.payload_point_stride),
    )
    write_summary_yaml(
        summary_path=output_directory / SUMMARY_FILENAME,
        run_instance_id=run_instance_id,
        config_path=resolved_config_path,
        output_directory=output_directory,
        report_path=report_path,
        candidate_summary_list=candidate_summary_list,
        harmonic_order_list=harmonic_order_list,
    )
    report_lines = build_report_lines(
        run_instance_id=run_instance_id,
        config_path=resolved_config_path,
        output_directory=output_directory,
        candidate_summary_list=candidate_summary_list,
        harmonic_order_list=harmonic_order_list,
        curve_payload_count=len(all_candidate_entry_list),
    )
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Wrote CVP 1.2 diagnostics report: {report_path}")
    print(f"Wrote CVP 1.2 diagnostics artifacts: {output_directory}")


if __name__ == "__main__":
    main()
