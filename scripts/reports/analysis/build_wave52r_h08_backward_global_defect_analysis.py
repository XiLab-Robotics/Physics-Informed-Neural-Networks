"""Build the non-training Wave 5.2R H08 backward/global defect diagnostic."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import json
import math
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import yaml

# Define Project Paths
PROJECT_PATH = Path(__file__).resolve().parents[3]
DEFAULT_CONFIG_PATH = PROJECT_PATH / "config" / "analysis" / "wave52r_h08_backward_global_defect_analysis.yaml"

# Define Stable Output Names
SUMMARY_FILENAME = "diagnostic_summary.yaml"
CANDIDATE_SUMMARY_FILENAME = "candidate_direction_summary.csv"
SELECTED_COMPARISON_FILENAME = "selected_incumbent_comparison.csv"
GLOBAL_INTERFERENCE_FILENAME = "global_interference_summary.csv"
CONDITION_FACTOR_FILENAME = "condition_factor_summary.csv"
WORST_CONDITION_FILENAME = "worst_condition_deltas.csv"
COEFFICIENT_BAND_FILENAME = "coefficient_band_summary.csv"
A0_SUMMARY_FILENAME = "coefficient_a0_summary.csv"
SEED_STABILITY_FILENAME = "seed_stability_summary.csv"
ARTIFACT_INVENTORY_FILENAME = "artifact_inventory.csv"

CONDITION_ID_PATTERN = re.compile(
    r"^speed_(?P<speed>-?[0-9.]+)rpm__torque_(?P<torque>-?[0-9.]+)Nm__"
    r"temperature_(?P<temperature>-?[0-9.]+)degC(?:__(?P<direction>Fw|Bw))?$"
)


@dataclass(frozen=True)
class CurveMetricRow:

    """Store one official CVP 1.2 per-curve metric row."""

    candidate_id: str
    candidate_surface: str
    direction_label: str
    source_file_path: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    raw_mae_deg: float
    signed_offset_error_deg: float
    absolute_offset_error_deg: float
    centered_mae_deg: float
    peak_to_peak_error_pct: float
    harmonic_amplitude_error_pct: float
    harmonic_phase_error_deg: float


@dataclass(frozen=True)
class H08RunPayload:

    """Store one immutable H08 curve and coefficient payload."""

    surface: str
    random_seed: int
    candidate_id: str
    run_directory: Path
    condition_id_array: np.ndarray
    measured_curve_matrix: np.ndarray
    predicted_curve_matrix: np.ndarray
    predicted_coefficient_matrix: np.ndarray
    correction_coefficient_matrix: np.ndarray
    anchor_coefficient_matrix: np.ndarray


def parse_arguments() -> argparse.Namespace:

    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    parser.add_argument("--run-id", type=str, default="")
    return parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:

    """Resolve a repository-relative or absolute path."""

    path = Path(path_value)
    return path if path.is_absolute() else PROJECT_PATH / path


def format_float(value: float) -> str:

    """Format a float for stable CSV output."""

    if not math.isfinite(float(value)):
        return "nan"
    return f"{float(value):.9f}"


def format_report_float(value: float, digit_count: int = 6) -> str:

    """Format a float for compact Markdown output."""

    if not math.isfinite(float(value)):
        return "nan"
    return f"{float(value):.{digit_count}f}"


def normalize_source_path(path_value: str) -> str:

    """Normalize source paths for deterministic joins."""

    return path_value.replace("\\", "/").strip().lower()


def load_configuration(config_path: Path) -> dict[str, Any]:

    """Load and validate the diagnostic configuration."""

    assert config_path.exists(), f"Diagnostic configuration not found | {config_path}"
    with config_path.open("r", encoding="utf-8") as config_file:
        configuration = yaml.safe_load(config_file)

    assert configuration["metadata"]["training_allowed"] is False
    assert configuration["metadata"]["checkpoint_modification_allowed"] is False
    assert configuration["metadata"]["registry_update_allowed"] is False
    assert len(configuration["h08_runs"]) == 9, "Expected nine H08 run entries"
    return configuration


def load_curve_metric_rows(input_path: Path) -> list[CurveMetricRow]:

    """Load official CVP 1.2 per-curve diagnostics."""

    assert input_path.exists(), f"Curve metric file not found | {input_path}"
    row_list: list[CurveMetricRow] = []
    with input_path.open("r", encoding="utf-8", newline="") as input_file:
        for row in csv.DictReader(input_file):
            row_list.append(
                CurveMetricRow(
                    candidate_id=row["candidate_id"],
                    candidate_surface=row["candidate_surface"],
                    direction_label=row["direction_label"],
                    source_file_path=normalize_source_path(row["source_file_path"]),
                    speed_rpm=float(row["speed_rpm"]),
                    torque_nm=float(row["torque_nm"]),
                    oil_temperature_deg=float(row["oil_temperature_deg"]),
                    raw_mae_deg=float(row["curve_mae_deg"]),
                    signed_offset_error_deg=float(row["signed_curve_mean_error_deg"]),
                    absolute_offset_error_deg=float(row["absolute_curve_mean_error_deg"]),
                    centered_mae_deg=float(row["centered_curve_mae_deg"]),
                    peak_to_peak_error_pct=float(row["peak_to_peak_error_pct"]),
                    harmonic_amplitude_error_pct=float(row["mean_harmonic_amplitude_error_pct"]),
                    harmonic_phase_error_deg=float(row["mean_harmonic_phase_error_deg"]),
                )
            )
    assert row_list, f"No curve metric rows loaded | {input_path}"
    return row_list


def load_h08_run_payload(run_config: dict[str, Any], expected_order_count: int, split_signature: str) -> H08RunPayload:

    """Load one H08 NPZ payload and validate its immutable metadata."""

    run_directory = resolve_project_path(run_config["run_directory"])
    prediction_path = run_directory / "test_predictions.npz"
    promotion_metadata_path = run_directory / "promotion_metadata.yaml"
    training_config_path = run_directory / "training_config.yaml"
    assert prediction_path.exists(), f"H08 prediction payload not found | {prediction_path}"
    assert promotion_metadata_path.exists(), f"H08 promotion metadata not found | {promotion_metadata_path}"
    assert training_config_path.exists(), f"H08 training config not found | {training_config_path}"

    # Validate Frozen Metadata
    with promotion_metadata_path.open("r", encoding="utf-8") as metadata_file:
        promotion_metadata = yaml.safe_load(metadata_file)
    with training_config_path.open("r", encoding="utf-8") as training_config_file:
        training_config = yaml.safe_load(training_config_file)
    assert promotion_metadata["surface"] == run_config["surface"]
    assert int(promotion_metadata["random_seed"]) == int(run_config["random_seed"])
    assert promotion_metadata["split_signature"] == split_signature
    assert training_config["formulation"] == "banded_coefficient"
    assert len(training_config["harmonic_order_list"]) == expected_order_count

    # Load Immutable Arrays
    with np.load(prediction_path, allow_pickle=False) as prediction_archive:
        expected_key_set = {
            "condition_id",
            "measured_curve",
            "predicted_curve",
            "predicted_coefficient",
            "coefficient_correction",
        }
        assert set(prediction_archive.files) == expected_key_set, (
            f"Unexpected H08 NPZ schema | {prediction_path} | {prediction_archive.files}"
        )
        condition_id_array = np.asarray(prediction_archive["condition_id"]).copy()
        measured_curve_matrix = np.asarray(prediction_archive["measured_curve"], dtype=np.float64).copy()
        predicted_curve_matrix = np.asarray(prediction_archive["predicted_curve"], dtype=np.float64).copy()
        predicted_coefficient_matrix = np.asarray(
            prediction_archive["predicted_coefficient"], dtype=np.float64
        ).copy()
        correction_coefficient_matrix = np.asarray(
            prediction_archive["coefficient_correction"], dtype=np.float64
        ).copy()

    expected_coefficient_count = 1 + (2 * expected_order_count)
    assert measured_curve_matrix.ndim == 2 and measured_curve_matrix.shape[1] == 2048
    assert predicted_curve_matrix.shape == measured_curve_matrix.shape
    assert predicted_coefficient_matrix.shape == (measured_curve_matrix.shape[0], expected_coefficient_count)
    assert correction_coefficient_matrix.shape == predicted_coefficient_matrix.shape
    assert condition_id_array.shape == (measured_curve_matrix.shape[0],)
    assert np.all(np.isfinite(measured_curve_matrix)) and np.all(np.isfinite(predicted_curve_matrix))

    return H08RunPayload(
        surface=run_config["surface"],
        random_seed=int(run_config["random_seed"]),
        candidate_id=run_config["candidate_id"],
        run_directory=run_directory,
        condition_id_array=condition_id_array,
        measured_curve_matrix=measured_curve_matrix,
        predicted_curve_matrix=predicted_curve_matrix,
        predicted_coefficient_matrix=predicted_coefficient_matrix,
        correction_coefficient_matrix=correction_coefficient_matrix,
        anchor_coefficient_matrix=predicted_coefficient_matrix - correction_coefficient_matrix,
    )


def parse_condition_id(condition_id: str, fallback_surface: str = "") -> dict[str, Any]:

    """Parse the frozen Stage 5 condition identifier.

    Args:
        condition_id: Frozen Stage 5 condition identifier.
        fallback_surface: Directional surface used when the identifier omits
            its redundant direction suffix.

    Returns:
        Parsed operating-condition fields.
    """

    match = CONDITION_ID_PATTERN.match(str(condition_id))
    assert match is not None, f"Unexpected H08 condition identifier | {condition_id}"
    direction_token = match.group("direction")
    if direction_token is None:
        assert fallback_surface in {"Fw", "Bw"}, (
            f"Directional fallback required for condition identifier | {condition_id} | {fallback_surface}"
        )
        direction_token = fallback_surface
    return {
        "direction_label": "forward" if direction_token == "Fw" else "backward",
        "speed_rpm": float(match.group("speed")),
        "torque_nm": float(match.group("torque")),
        "oil_temperature_deg": float(match.group("temperature")),
    }


def summarize_metric_rows(row_list: list[CurveMetricRow], group_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Summarize one candidate and direction metric group."""

    assert row_list, f"No rows provided for summary | {group_dictionary}"
    raw_array = np.asarray([row.raw_mae_deg for row in row_list], dtype=np.float64)
    signed_offset_array = np.asarray([row.signed_offset_error_deg for row in row_list], dtype=np.float64)
    absolute_offset_array = np.asarray([row.absolute_offset_error_deg for row in row_list], dtype=np.float64)
    centered_array = np.asarray([row.centered_mae_deg for row in row_list], dtype=np.float64)
    peak_to_peak_array = np.asarray([row.peak_to_peak_error_pct for row in row_list], dtype=np.float64)
    amplitude_array = np.asarray([row.harmonic_amplitude_error_pct for row in row_list], dtype=np.float64)
    phase_array = np.asarray([row.harmonic_phase_error_deg for row in row_list], dtype=np.float64)

    return {
        **group_dictionary,
        "curve_count": len(row_list),
        "raw_mae_deg": float(np.mean(raw_array)),
        "signed_offset_bias_deg": float(np.mean(signed_offset_array)),
        "absolute_offset_error_deg": float(np.mean(absolute_offset_array)),
        "centered_mae_deg": float(np.mean(centered_array)),
        "peak_to_peak_error_pct": float(np.mean(peak_to_peak_array)),
        "harmonic_amplitude_error_pct": float(np.mean(amplitude_array)),
        "harmonic_phase_error_deg": float(np.mean(phase_array)),
        "offset_to_raw_ratio": float(np.mean(absolute_offset_array) / np.mean(raw_array)),
        "p90_raw_mae_deg": float(np.percentile(raw_array, 90.0)),
        "p90_absolute_offset_error_deg": float(np.percentile(absolute_offset_array, 90.0)),
    }


def build_candidate_summary_rows(metric_rows: list[CurveMetricRow], relevant_candidate_ids: set[str]) -> list[dict[str, Any]]:

    """Build candidate-direction summaries for H08 and matched incumbents."""

    group_dictionary: dict[tuple[str, str], list[CurveMetricRow]] = defaultdict(list)
    for row in metric_rows:
        if row.candidate_id in relevant_candidate_ids:
            group_dictionary[(row.candidate_id, row.direction_label)].append(row)

    summary_rows: list[dict[str, Any]] = []
    for (candidate_id, direction_label), row_list in sorted(group_dictionary.items()):
        summary_rows.append(
            summarize_metric_rows(
                row_list,
                {
                    "candidate_id": candidate_id,
                    "candidate_surface": row_list[0].candidate_surface,
                    "direction_label": direction_label,
                },
            )
        )
    return summary_rows


def index_metric_rows(metric_rows: list[CurveMetricRow]) -> dict[tuple[str, str], CurveMetricRow]:

    """Index per-curve metric rows by candidate and source path."""

    indexed_rows: dict[tuple[str, str], CurveMetricRow] = {}
    for row in metric_rows:
        key = (row.candidate_id, row.source_file_path)
        assert key not in indexed_rows, f"Duplicate per-curve metric row | {key}"
        indexed_rows[key] = row
    return indexed_rows


def compute_improvement_percentage(candidate_value: float, incumbent_value: float) -> float:

    """Compute positive-is-better improvement percentage."""

    assert incumbent_value > 0.0
    return 100.0 * (incumbent_value - candidate_value) / incumbent_value


def build_selected_comparison_rows(
    configuration: dict[str, Any], metric_rows: list[CurveMetricRow]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:

    """Compare selected H08 checkpoints with matched incumbents per curve."""

    metric_index = index_metric_rows(metric_rows)
    comparison_summary_rows: list[dict[str, Any]] = []
    condition_delta_rows: list[dict[str, Any]] = []

    for comparison in configuration["selected_comparisons"]:
        h08_candidate_id = comparison["h08_candidate_id"]
        incumbent_candidate_id = comparison["incumbent_candidate_id"]
        direction_filter = comparison["direction_label"]
        h08_rows = [
            row
            for row in metric_rows
            if row.candidate_id == h08_candidate_id
            and (direction_filter == "all" or row.direction_label == direction_filter)
        ]
        incumbent_rows: list[CurveMetricRow] = []

        for h08_row in h08_rows:
            incumbent_key = (incumbent_candidate_id, h08_row.source_file_path)
            assert incumbent_key in metric_index, f"Matched incumbent row not found | {incumbent_key}"
            incumbent_row = metric_index[incumbent_key]
            incumbent_rows.append(incumbent_row)
            condition_delta_rows.append(
                {
                    "surface": comparison["surface"],
                    "direction_label": h08_row.direction_label,
                    "source_file_path": h08_row.source_file_path,
                    "speed_rpm": h08_row.speed_rpm,
                    "torque_nm": h08_row.torque_nm,
                    "oil_temperature_deg": h08_row.oil_temperature_deg,
                    "h08_candidate_id": h08_candidate_id,
                    "incumbent_candidate_id": incumbent_candidate_id,
                    "raw_delta_deg": h08_row.raw_mae_deg - incumbent_row.raw_mae_deg,
                    "offset_delta_deg": h08_row.absolute_offset_error_deg - incumbent_row.absolute_offset_error_deg,
                    "shape_delta_deg": h08_row.centered_mae_deg - incumbent_row.centered_mae_deg,
                    "peak_to_peak_delta_pct": h08_row.peak_to_peak_error_pct - incumbent_row.peak_to_peak_error_pct,
                }
            )

        assert h08_rows and len(h08_rows) == len(incumbent_rows)
        h08_summary = summarize_metric_rows(h08_rows, {})
        incumbent_summary = summarize_metric_rows(incumbent_rows, {})
        comparison_summary_rows.append(
            {
                "surface": comparison["surface"],
                "direction_label": direction_filter,
                "h08_candidate_id": h08_candidate_id,
                "incumbent_candidate_id": incumbent_candidate_id,
                "curve_count": len(h08_rows),
                "h08_raw_mae_deg": h08_summary["raw_mae_deg"],
                "incumbent_raw_mae_deg": incumbent_summary["raw_mae_deg"],
                "raw_improvement_pct": compute_improvement_percentage(
                    h08_summary["raw_mae_deg"], incumbent_summary["raw_mae_deg"]
                ),
                "h08_absolute_offset_error_deg": h08_summary["absolute_offset_error_deg"],
                "incumbent_absolute_offset_error_deg": incumbent_summary["absolute_offset_error_deg"],
                "offset_improvement_pct": compute_improvement_percentage(
                    h08_summary["absolute_offset_error_deg"], incumbent_summary["absolute_offset_error_deg"]
                ),
                "h08_centered_mae_deg": h08_summary["centered_mae_deg"],
                "incumbent_centered_mae_deg": incumbent_summary["centered_mae_deg"],
                "shape_improvement_pct": compute_improvement_percentage(
                    h08_summary["centered_mae_deg"], incumbent_summary["centered_mae_deg"]
                ),
                "h08_peak_to_peak_error_pct": h08_summary["peak_to_peak_error_pct"],
                "incumbent_peak_to_peak_error_pct": incumbent_summary["peak_to_peak_error_pct"],
                "peak_to_peak_improvement_pct": compute_improvement_percentage(
                    h08_summary["peak_to_peak_error_pct"], incumbent_summary["peak_to_peak_error_pct"]
                ),
            }
        )
    return comparison_summary_rows, condition_delta_rows


def build_global_interference_rows(metric_rows: list[CurveMetricRow]) -> list[dict[str, Any]]:

    """Compare the selected global H08 checkpoint with directional specialists."""

    selected_pairs = [
        ("forward", "wave52r_promotion_h08_global_seed_314159", "wave52r_promotion_h08_fw_seed_161803"),
        ("backward", "wave52r_promotion_h08_global_seed_314159", "wave52r_promotion_h08_bw_seed_161803"),
    ]
    metric_index = index_metric_rows(metric_rows)
    output_rows: list[dict[str, Any]] = []

    for direction_label, global_candidate_id, specialist_candidate_id in selected_pairs:
        global_rows = [
            row
            for row in metric_rows
            if row.candidate_id == global_candidate_id and row.direction_label == direction_label
        ]
        specialist_rows = [
            metric_index[(specialist_candidate_id, row.source_file_path)] for row in global_rows
        ]
        global_summary = summarize_metric_rows(global_rows, {})
        specialist_summary = summarize_metric_rows(specialist_rows, {})
        output_rows.append(
            {
                "direction_label": direction_label,
                "global_candidate_id": global_candidate_id,
                "specialist_candidate_id": specialist_candidate_id,
                "curve_count": len(global_rows),
                "global_raw_mae_deg": global_summary["raw_mae_deg"],
                "specialist_raw_mae_deg": specialist_summary["raw_mae_deg"],
                "global_raw_penalty_pct": 100.0
                * (global_summary["raw_mae_deg"] - specialist_summary["raw_mae_deg"])
                / specialist_summary["raw_mae_deg"],
                "global_offset_error_deg": global_summary["absolute_offset_error_deg"],
                "specialist_offset_error_deg": specialist_summary["absolute_offset_error_deg"],
                "global_offset_penalty_pct": 100.0
                * (global_summary["absolute_offset_error_deg"] - specialist_summary["absolute_offset_error_deg"])
                / specialist_summary["absolute_offset_error_deg"],
                "global_centered_mae_deg": global_summary["centered_mae_deg"],
                "specialist_centered_mae_deg": specialist_summary["centered_mae_deg"],
                "global_shape_penalty_pct": 100.0
                * (global_summary["centered_mae_deg"] - specialist_summary["centered_mae_deg"])
                / specialist_summary["centered_mae_deg"],
            }
        )
    return output_rows


def build_condition_factor_rows(condition_delta_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:

    """Summarize H08-minus-incumbent deltas by operating factor."""

    output_rows: list[dict[str, Any]] = []
    factor_list = ["speed_rpm", "torque_nm", "oil_temperature_deg"]
    for surface in ["Fw", "Bw", "global"]:
        surface_rows = [row for row in condition_delta_rows if row["surface"] == surface]
        for direction_label in sorted({row["direction_label"] for row in surface_rows}):
            direction_rows = [row for row in surface_rows if row["direction_label"] == direction_label]
            for factor_name in factor_list:
                group_dictionary: dict[float, list[dict[str, Any]]] = defaultdict(list)
                for row in direction_rows:
                    group_dictionary[float(row[factor_name])].append(row)
                for factor_value, group_rows in sorted(group_dictionary.items()):
                    output_rows.append(
                        {
                            "surface": surface,
                            "direction_label": direction_label,
                            "factor_name": factor_name,
                            "factor_value": factor_value,
                            "condition_count": len(group_rows),
                            "mean_raw_delta_deg": float(np.mean([row["raw_delta_deg"] for row in group_rows])),
                            "mean_offset_delta_deg": float(np.mean([row["offset_delta_deg"] for row in group_rows])),
                            "mean_shape_delta_deg": float(np.mean([row["shape_delta_deg"] for row in group_rows])),
                        }
                    )
    return output_rows


def coefficient_band_name(order: int, band_dictionary: dict[str, list[int]]) -> str:

    """Resolve one harmonic order to its configured diagnostic band."""

    matching_band_list = [band_name for band_name, order_list in band_dictionary.items() if order in order_list]
    assert len(matching_band_list) == 1, f"Harmonic order must map to one band | {order} | {matching_band_list}"
    return matching_band_list[0]


def build_coefficient_rows(
    run_payload_list: list[H08RunPayload], harmonic_order_list: list[int], band_dictionary: dict[str, list[int]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:

    """Build coefficient-band and coefficient-a0 summaries."""

    band_group_dictionary: dict[tuple[str, int, str, str], list[tuple[float, float, float]]] = defaultdict(list)
    a0_group_dictionary: dict[tuple[str, int, str], list[tuple[float, float, float, float]]] = defaultdict(list)

    for payload in run_payload_list:
        for condition_index, condition_id in enumerate(payload.condition_id_array):
            condition = parse_condition_id(str(condition_id), payload.surface)
            direction_label = condition["direction_label"]
            measured_mean = float(np.mean(payload.measured_curve_matrix[condition_index]))
            predicted_mean = float(np.mean(payload.predicted_curve_matrix[condition_index]))
            anchor_a0 = float(payload.anchor_coefficient_matrix[condition_index, 0])
            correction_a0 = float(payload.correction_coefficient_matrix[condition_index, 0])
            predicted_a0 = float(payload.predicted_coefficient_matrix[condition_index, 0])
            assert abs(predicted_mean - predicted_a0) <= 2.0e-6, (
                f"Prediction mean and coefficient a0 disagree | {payload.candidate_id} | {condition_id}"
            )
            a0_group_dictionary[(payload.surface, payload.random_seed, direction_label)].append(
                (anchor_a0, correction_a0, predicted_a0, predicted_a0 - measured_mean)
            )

            for order_index, harmonic_order in enumerate(harmonic_order_list):
                sine_index = 1 + (2 * order_index)
                cosine_index = sine_index + 1
                anchor_amplitude = float(
                    np.hypot(
                        payload.anchor_coefficient_matrix[condition_index, sine_index],
                        payload.anchor_coefficient_matrix[condition_index, cosine_index],
                    )
                )
                correction_amplitude = float(
                    np.hypot(
                        payload.correction_coefficient_matrix[condition_index, sine_index],
                        payload.correction_coefficient_matrix[condition_index, cosine_index],
                    )
                )
                predicted_amplitude = float(
                    np.hypot(
                        payload.predicted_coefficient_matrix[condition_index, sine_index],
                        payload.predicted_coefficient_matrix[condition_index, cosine_index],
                    )
                )
                band_name = coefficient_band_name(harmonic_order, band_dictionary)
                band_group_dictionary[(payload.surface, payload.random_seed, direction_label, band_name)].append(
                    (anchor_amplitude, correction_amplitude, predicted_amplitude)
                )

    coefficient_band_rows: list[dict[str, Any]] = []
    for (surface, random_seed, direction_label, band_name), value_list in sorted(band_group_dictionary.items()):
        value_array = np.asarray(value_list, dtype=np.float64)
        mean_anchor = float(np.mean(value_array[:, 0]))
        mean_correction = float(np.mean(value_array[:, 1]))
        coefficient_band_rows.append(
            {
                "surface": surface,
                "random_seed": random_seed,
                "direction_label": direction_label,
                "band_name": band_name,
                "value_count": value_array.shape[0],
                "mean_anchor_amplitude_deg": mean_anchor,
                "mean_correction_amplitude_deg": mean_correction,
                "mean_predicted_amplitude_deg": float(np.mean(value_array[:, 2])),
                "correction_to_anchor_ratio": mean_correction / max(mean_anchor, 1.0e-12),
            }
        )

    a0_summary_rows: list[dict[str, Any]] = []
    for (surface, random_seed, direction_label), value_list in sorted(a0_group_dictionary.items()):
        value_array = np.asarray(value_list, dtype=np.float64)
        a0_summary_rows.append(
            {
                "surface": surface,
                "random_seed": random_seed,
                "direction_label": direction_label,
                "condition_count": value_array.shape[0],
                "mean_anchor_a0_deg": float(np.mean(value_array[:, 0])),
                "mean_abs_anchor_a0_deg": float(np.mean(np.abs(value_array[:, 0]))),
                "mean_correction_a0_deg": float(np.mean(value_array[:, 1])),
                "mean_abs_correction_a0_deg": float(np.mean(np.abs(value_array[:, 1]))),
                "mean_predicted_a0_deg": float(np.mean(value_array[:, 2])),
                "mean_signed_a0_error_deg": float(np.mean(value_array[:, 3])),
                "mean_absolute_a0_error_deg": float(np.mean(np.abs(value_array[:, 3]))),
                "p90_absolute_a0_error_deg": float(np.percentile(np.abs(value_array[:, 3]), 90.0)),
            }
        )
    return coefficient_band_rows, a0_summary_rows


def build_seed_stability_rows(candidate_summary_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:

    """Summarize aggregate H08 variability across three seeds."""

    group_dictionary: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in candidate_summary_rows:
        if row["candidate_id"].startswith("wave52r_promotion_h08_"):
            group_dictionary[(row["candidate_surface"], row["direction_label"])].append(row)

    output_rows: list[dict[str, Any]] = []
    for (surface, direction_label), row_list in sorted(group_dictionary.items()):
        assert len(row_list) == 3, f"Expected three H08 seeds | {surface} | {direction_label} | {len(row_list)}"
        for metric_name in ["raw_mae_deg", "absolute_offset_error_deg", "centered_mae_deg"]:
            metric_array = np.asarray([float(row[metric_name]) for row in row_list], dtype=np.float64)
            output_rows.append(
                {
                    "surface": surface,
                    "direction_label": direction_label,
                    "metric_name": metric_name,
                    "seed_count": len(row_list),
                    "mean_value": float(np.mean(metric_array)),
                    "standard_deviation": float(np.std(metric_array)),
                    "minimum_value": float(np.min(metric_array)),
                    "maximum_value": float(np.max(metric_array)),
                    "coefficient_of_variation": float(np.std(metric_array) / np.mean(metric_array)),
                }
            )
    return output_rows


def write_csv(output_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write dictionaries to a deterministic CSV file."""

    assert row_list, f"No rows available for CSV output | {output_path}"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    serialized_rows: list[dict[str, Any]] = []
    for row in row_list:
        serialized_rows.append(
            {key: format_float(value) if isinstance(value, float) else value for key, value in row.items()}
        )
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(serialized_rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(serialized_rows)


def create_selected_metric_plot(comparison_rows: list[dict[str, Any]], output_path: Path) -> None:

    """Plot selected H08 improvements against matched incumbents."""

    metric_list = ["raw_improvement_pct", "offset_improvement_pct", "shape_improvement_pct", "peak_to_peak_improvement_pct"]
    metric_label_list = ["raw", "offset", "centered shape", "peak-to-peak"]
    x_values = np.arange(len(comparison_rows), dtype=np.float64)
    width = 0.18
    figure, axis = plt.subplots(figsize=(9.2, 4.8), layout="constrained")
    for metric_index, (metric_name, metric_label) in enumerate(zip(metric_list, metric_label_list)):
        offset = (metric_index - 1.5) * width
        axis.bar(x_values + offset, [row[metric_name] for row in comparison_rows], width=width, label=metric_label)
    axis.axhline(0.0, color="#333333", linewidth=0.9)
    axis.set_xticks(x_values, [row["surface"] for row in comparison_rows])
    axis.set_ylabel("improvement over matched incumbent [%]")
    axis.set_title("H08 selected checkpoints: positive is better")
    axis.grid(True, axis="y", alpha=0.25)
    axis.legend(ncol=4, fontsize=8)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def create_global_interference_plot(interference_rows: list[dict[str, Any]], output_path: Path) -> None:

    """Plot the global-model penalty relative to direction-specific H08."""

    metric_list = ["global_raw_penalty_pct", "global_offset_penalty_pct", "global_shape_penalty_pct"]
    metric_label_list = ["raw", "offset", "centered shape"]
    x_values = np.arange(len(interference_rows), dtype=np.float64)
    width = 0.24
    figure, axis = plt.subplots(figsize=(7.8, 4.6), layout="constrained")
    for metric_index, (metric_name, metric_label) in enumerate(zip(metric_list, metric_label_list)):
        offset = (metric_index - 1.0) * width
        axis.bar(x_values + offset, [row[metric_name] for row in interference_rows], width=width, label=metric_label)
    axis.axhline(0.0, color="#333333", linewidth=0.9)
    axis.set_xticks(x_values, [row["direction_label"] for row in interference_rows])
    axis.set_ylabel("global-model penalty vs specialist [%]")
    axis.set_title("Direction-aware global H08 interference")
    axis.grid(True, axis="y", alpha=0.25)
    axis.legend(ncol=3, fontsize=8)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def create_condition_delta_plot(condition_delta_rows: list[dict[str, Any]], output_path: Path) -> None:

    """Plot condition-level offset deltas for the failing surfaces."""

    panel_contract = [("Bw", "backward"), ("global", "forward"), ("global", "backward")]
    selected_rows = [
        row
        for row in condition_delta_rows
        if (row["surface"], row["direction_label"]) in panel_contract
    ]
    max_abs_delta = max(abs(float(row["offset_delta_deg"])) for row in selected_rows)
    figure, axes = plt.subplots(1, 3, figsize=(11.0, 3.9), layout="constrained", sharex=True, sharey=True)
    scatter = None
    for axis, (surface, direction_label) in zip(axes, panel_contract):
        panel_rows = [
            row for row in selected_rows if row["surface"] == surface and row["direction_label"] == direction_label
        ]
        scatter = axis.scatter(
            [row["speed_rpm"] for row in panel_rows],
            [row["torque_nm"] for row in panel_rows],
            c=[row["offset_delta_deg"] for row in panel_rows],
            cmap="coolwarm",
            vmin=-max_abs_delta,
            vmax=max_abs_delta,
            s=[30.0 + (2.0 * row["oil_temperature_deg"]) for row in panel_rows],
            edgecolors="black",
            linewidths=0.2,
        )
        axis.set_title(f"{surface} / {direction_label}")
        axis.set_xlabel("speed [rpm]")
        axis.grid(True, alpha=0.25)
    axes[0].set_ylabel("torque [Nm]")
    assert scatter is not None
    figure.colorbar(scatter, ax=axes, label="H08 - incumbent offset error [deg]", shrink=0.9)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def create_a0_plot(a0_rows: list[dict[str, Any]], output_path: Path) -> None:

    """Plot selected H08 offset-coefficient decomposition."""

    selected_contract = [("Fw", 161803, "forward"), ("Bw", 161803, "backward"), ("global", 314159, "forward"), ("global", 314159, "backward")]
    selected_rows = [
        next(
            row
            for row in a0_rows
            if (row["surface"], row["random_seed"], row["direction_label"]) == contract
        )
        for contract in selected_contract
    ]
    x_values = np.arange(len(selected_rows), dtype=np.float64)
    width = 0.22
    figure, axis = plt.subplots(figsize=(9.0, 4.8), layout="constrained")
    axis.bar(x_values - width, [row["mean_abs_anchor_a0_deg"] for row in selected_rows], width, label="anchor |a0|")
    axis.bar(x_values, [row["mean_abs_correction_a0_deg"] for row in selected_rows], width, label="correction |a0|")
    axis.bar(x_values + width, [row["mean_absolute_a0_error_deg"] for row in selected_rows], width, label="final |a0 error|")
    axis.set_xticks(x_values, [f"{row['surface']}\n{row['direction_label']}" for row in selected_rows])
    axis.set_ylabel("mean absolute magnitude [deg]")
    axis.set_title("H08 coefficient a0 decomposition")
    axis.grid(True, axis="y", alpha=0.25)
    axis.legend(ncol=3, fontsize=8)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def create_band_plot(coefficient_rows: list[dict[str, Any]], output_path: Path) -> None:

    """Plot selected H08 coefficient correction-to-anchor ratios by band."""

    selected_contract = [("Fw", 161803, "forward"), ("Bw", 161803, "backward"), ("global", 314159, "forward"), ("global", 314159, "backward")]
    band_order = ["order_1", "low_orders", "reducer_middle", "high_ripple"]
    figure, axes = plt.subplots(2, 2, figsize=(9.6, 6.8), layout="constrained", sharey=True)
    for axis, contract in zip(axes.ravel(), selected_contract):
        selected_rows = [
            row
            for row in coefficient_rows
            if (row["surface"], row["random_seed"], row["direction_label"]) == contract
        ]
        row_dictionary = {row["band_name"]: row for row in selected_rows}
        axis.bar(band_order, [100.0 * row_dictionary[band]["correction_to_anchor_ratio"] for band in band_order])
        axis.set_title(f"{contract[0]} / {contract[2]}")
        axis.tick_params(axis="x", labelrotation=20)
        axis.grid(True, axis="y", alpha=0.25)
    figure.supylabel("mean correction / anchor amplitude [%]")
    figure.suptitle("H08 learned coefficient correction by harmonic band")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def reconstruct_curve(coefficient_vector: np.ndarray, harmonic_order_list: list[int]) -> np.ndarray:

    """Reconstruct one uniform curve from the Stage 5 coefficient contract."""

    angle_rad = np.linspace(0.0, 2.0 * np.pi, 2048, endpoint=False, dtype=np.float64)
    curve = np.full_like(angle_rad, coefficient_vector[0], dtype=np.float64)
    for order_index, harmonic_order in enumerate(harmonic_order_list):
        sine_index = 1 + (2 * order_index)
        cosine_index = sine_index + 1
        curve += coefficient_vector[sine_index] * np.sin(harmonic_order * angle_rad)
        curve += coefficient_vector[cosine_index] * np.cos(harmonic_order * angle_rad)
    return curve


def create_representative_curve_plot(
    run_payload_list: list[H08RunPayload], harmonic_order_list: list[int], output_path: Path
) -> None:

    """Plot deterministic worst-offset H08 curves and analytical anchors."""

    selected_contract = [("Bw", 161803, "backward", 2), ("global", 314159, "forward", 1), ("global", 314159, "backward", 1)]
    panel_records: list[tuple[H08RunPayload, int, str]] = []
    for surface, random_seed, direction_label, panel_count in selected_contract:
        payload = next(
            item for item in run_payload_list if item.surface == surface and item.random_seed == random_seed
        )
        eligible_indices = [
            index
            for index, condition_id in enumerate(payload.condition_id_array)
            if parse_condition_id(str(condition_id), payload.surface)["direction_label"] == direction_label
        ]
        sorted_indices = sorted(
            eligible_indices,
            key=lambda index: abs(
                float(np.mean(payload.predicted_curve_matrix[index] - payload.measured_curve_matrix[index]))
            ),
            reverse=True,
        )
        panel_records.extend((payload, index, direction_label) for index in sorted_indices[:panel_count])

    figure, axes = plt.subplots(2, 2, figsize=(10.4, 7.0), layout="constrained", sharex=True)
    angle_deg = np.linspace(0.0, 360.0, 2048, endpoint=False)
    for axis, (payload, condition_index, direction_label) in zip(axes.ravel(), panel_records):
        anchor_curve = reconstruct_curve(payload.anchor_coefficient_matrix[condition_index], harmonic_order_list)
        axis.plot(angle_deg, payload.measured_curve_matrix[condition_index], label="measured", linewidth=1.0)
        axis.plot(angle_deg, payload.predicted_curve_matrix[condition_index], label="H08", linewidth=0.9)
        axis.plot(angle_deg, anchor_curve, label="analytical anchor", linewidth=0.8, alpha=0.8)
        axis.set_title(f"{payload.surface} / {direction_label}\n{payload.condition_id_array[condition_index]}", fontsize=8)
        axis.grid(True, alpha=0.2)
    axes[0, 0].legend(fontsize=8, ncol=3)
    figure.supxlabel("output angle [deg]")
    figure.supylabel("transmission error [deg]")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def reproduce_official_metrics(
    configuration: dict[str, Any], comparison_rows: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], float]:

    """Reproduce the rounded official selected H08 metrics."""

    output_rows: list[dict[str, Any]] = []
    maximum_difference = 0.0
    metric_mapping = {
        "raw_mae_deg": "h08_raw_mae_deg",
        "absolute_offset_error_deg": "h08_absolute_offset_error_deg",
        "centered_mae_deg": "h08_centered_mae_deg",
    }
    for surface, expected_metrics in configuration["official_selected_metrics"].items():
        comparison_row = next(row for row in comparison_rows if row["surface"] == surface)
        for official_metric_name, comparison_metric_name in metric_mapping.items():
            recomputed_value = float(comparison_row[comparison_metric_name])
            expected_value = float(expected_metrics[official_metric_name])
            absolute_difference = abs(recomputed_value - expected_value)
            maximum_difference = max(maximum_difference, absolute_difference)
            output_rows.append(
                {
                    "surface": surface,
                    "metric_name": official_metric_name,
                    "official_rounded_value": expected_value,
                    "recomputed_value": recomputed_value,
                    "absolute_difference": absolute_difference,
                }
            )
    return output_rows, maximum_difference


def build_artifact_inventory(configuration: dict[str, Any], run_payload_list: list[H08RunPayload]) -> list[dict[str, Any]]:

    """Build the immutable diagnostic input inventory."""

    inventory_rows = [
        {"artifact_role": "curve_metrics", "path": configuration["paths"]["curve_metrics_path"]},
        {"artifact_role": "curve_payload_samples", "path": configuration["paths"]["curve_payload_samples_path"]},
        {"artifact_role": "official_decision", "path": configuration["paths"]["official_decision_path"]},
    ]
    for payload in run_payload_list:
        inventory_rows.append(
            {
                "artifact_role": f"h08_{payload.surface}_{payload.random_seed}",
                "path": (payload.run_directory / "test_predictions.npz").relative_to(PROJECT_PATH).as_posix(),
            }
        )
    for row in inventory_rows:
        path = resolve_project_path(row["path"])
        assert path.exists(), f"Inventory artifact not found | {path}"
        row["size_bytes"] = path.stat().st_size
    return inventory_rows


def build_report(
    report_path: Path,
    run_id: str,
    comparison_rows: list[dict[str, Any]],
    interference_rows: list[dict[str, Any]],
    condition_factor_rows: list[dict[str, Any]],
    a0_rows: list[dict[str, Any]],
    seed_rows: list[dict[str, Any]],
    plot_path_list: list[Path],
    reproduction_difference: float,
) -> None:

    """Write the canonical H08 defect analysis report."""

    fw_row = next(row for row in comparison_rows if row["surface"] == "Fw")
    bw_row = next(row for row in comparison_rows if row["surface"] == "Bw")
    global_row = next(row for row in comparison_rows if row["surface"] == "global")
    forward_interference = next(row for row in interference_rows if row["direction_label"] == "forward")
    backward_interference = next(row for row in interference_rows if row["direction_label"] == "backward")
    bw_a0 = next(
        row
        for row in a0_rows
        if row["surface"] == "Bw" and row["random_seed"] == 161803 and row["direction_label"] == "backward"
    )
    worst_offset_factor = max(
        [row for row in condition_factor_rows if row["surface"] in {"Bw", "global"}],
        key=lambda row: float(row["mean_offset_delta_deg"]),
    )
    maximum_seed_cv = max(float(row["coefficient_of_variation"]) for row in seed_rows)

    report_lines = [
        "# Wave 5.2R H08 Backward And Global Defect Analysis",
        "",
        "## Overview",
        "",
        (
            "This non-training diagnostic replays the nine frozen H08 promotion payloads and the official "
            "CVP 1.2 per-curve evidence. It separates raw error, curve-mean offset, centered shape, operating "
            "condition, direction, seed, coefficient `a0`, and harmonic-band behavior."
        ),
        "",
        f"Diagnostic run: `{run_id}`.",
        "",
        "## Decision",
        "",
        "**Outcome: `offset_dominant_direction_conditioned_with_global_interference`.**",
        "",
        (
            "The backward specialist retains a small centered-shape advantage but loses the matched-incumbent "
            "comparison mainly through offset. The combined global H08 model is worse than the corresponding "
            "direction-specific H08 specialist on both directions, so global-fit interference is confirmed. "
            "H08 should remain frozen as a forward specialist. If a repair is studied later, the first bounded "
            "candidate should be a direction-specific, causal `a0`/offset calibration with the existing harmonic "
            "coefficients frozen; broad retraining is not justified by this diagnostic."
        ),
        "",
        "This decision does not authorize training, model replacement, registry promotion, or integrated-specialist work.",
        "",
        "## Official Metric Reproduction",
        "",
        (
            f"The selected H08 raw, offset, and centered-shape metrics reproduce the rounded official decision "
            f"with maximum absolute difference `{format_report_float(reproduction_difference, 9)} deg`."
        ),
        "",
        "## Selected H08 Versus Matched Incumbent",
        "",
        "| Surface | Raw improvement | Offset improvement | Shape improvement | P2P improvement |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in comparison_rows:
        report_lines.append(
            f"| `{row['surface']}` | {format_report_float(row['raw_improvement_pct'], 2)}% | "
            f"{format_report_float(row['offset_improvement_pct'], 2)}% | "
            f"{format_report_float(row['shape_improvement_pct'], 2)}% | "
            f"{format_report_float(row['peak_to_peak_improvement_pct'], 2)}% |"
        )

    report_lines.extend(
        [
            "",
            (
                f"The `Bw` checkpoint changes raw MAE by `{format_report_float(bw_row['raw_improvement_pct'], 2)}%`, "
                f"offset by `{format_report_float(bw_row['offset_improvement_pct'], 2)}%`, and centered shape by "
                f"`{format_report_float(bw_row['shape_improvement_pct'], 2)}%`. The offset regression is therefore "
                "larger than the raw regression while shape still improves."
            ),
            "",
            (
                f"The selected `Fw` checkpoint remains useful on raw, centered shape, and peak-to-peak evidence, "
                f"although its offset changes by `{format_report_float(fw_row['offset_improvement_pct'], 2)}%`. "
                f"The `global` checkpoint regresses raw, offset, and shape by "
                f"`{format_report_float(abs(global_row['raw_improvement_pct']), 2)}%`, "
                f"`{format_report_float(abs(global_row['offset_improvement_pct']), 2)}%`, and "
                f"`{format_report_float(abs(global_row['shape_improvement_pct']), 2)}%`, respectively."
            ),
            "",
            "## Global Model Interference",
            "",
            "| Direction subset | Raw penalty | Offset penalty | Shape penalty |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for row in interference_rows:
        report_lines.append(
            f"| `{row['direction_label']}` | {format_report_float(row['global_raw_penalty_pct'], 2)}% | "
            f"{format_report_float(row['global_offset_penalty_pct'], 2)}% | "
            f"{format_report_float(row['global_shape_penalty_pct'], 2)}% |"
        )

    report_lines.extend(
        [
            "",
            (
                f"The global checkpoint adds raw penalties of `{format_report_float(forward_interference['global_raw_penalty_pct'], 2)}%` "
                f"on Fw and `{format_report_float(backward_interference['global_raw_penalty_pct'], 2)}%` on Bw relative "
                "to the corresponding directional H08 specialists. This rules out a backward-only explanation for the global failure."
            ),
            "",
            "## Coefficient a0 And Harmonic Interpretation",
            "",
            (
                f"For selected backward H08, mean absolute final `a0` error is "
                f"`{format_report_float(bw_a0['mean_absolute_a0_error_deg'], 6)} deg` and P90 is "
                f"`{format_report_float(bw_a0['p90_absolute_a0_error_deg'], 6)} deg`. The frozen payload confirms "
                "that predicted curve mean and coefficient `a0` agree within the diagnostic tolerance."
            ),
            "",
            "The coefficient plots show where learned corrections sit relative to the analytical anchor. They support attribution to an inspectable coefficient surface; they do not identify hysteresis, compliance, or lost motion as the physical cause.",
            "",
            "## Operating-Condition And Seed Evidence",
            "",
            (
                f"The largest mean offset degradation group is `{worst_offset_factor['surface']}` / "
                f"`{worst_offset_factor['direction_label']}` at `{worst_offset_factor['factor_name']}="
                f"{format_report_float(worst_offset_factor['factor_value'], 1)}`, with mean H08-minus-incumbent "
                f"offset delta `{format_report_float(worst_offset_factor['mean_offset_delta_deg'], 6)} deg`. "
                "This is an explanatory concentration, not a causal mechanism claim."
            ),
            "",
            (
                f"The maximum aggregate coefficient of variation across the three H08 seeds is "
                f"`{format_report_float(100.0 * maximum_seed_cv, 2)}%`; the cross-surface defect is not explained "
                "by one unstable selected seed alone."
            ),
            "",
            "## Visual Evidence",
            "",
        ]
    )
    plot_caption_list = [
        "Selected H08 metric improvements",
        "Global-model interference",
        "Condition-level offset deltas",
        "Coefficient a0 decomposition",
        "Harmonic-band correction ratios",
        "Representative H08 and analytical-anchor curves",
    ]
    for caption, plot_path in zip(plot_caption_list, plot_path_list):
        report_lines.append(f"![{caption}](./assets/{plot_path.name})")
        report_lines.append("")

    report_lines.extend(
        [
            "## Scientific Boundary",
            "",
            "Repository references support keeping direction, torque, speed, temperature, periodic shape, offset, and possible memory state separate. The present artifacts confirm a direction-conditioned coefficient and offset defect plus global-fit interference. They do not identify an underlying contact, hysteresis, compliance, or lost-motion law.",
            "",
            "## Recommended Next Gate",
            "",
            "1. Keep H08 frozen as the non-temporal `Fw` specialist.",
            "2. Do not transfer the current global H08 formulation into the integrated-specialist roadmap.",
            "3. If an H08 repair is desired, prepare a separate bounded technical plan for direction-specific causal `a0` calibration with all non-offset coefficients frozen.",
            "4. Use this defect report as an exclusion and ablation contract when the integrated-specialist roadmap is prepared.",
            "",
            "## Reproducibility",
            "",
            "```powershell",
            "conda run --no-capture-output -n pinns_env python -B scripts/reports/analysis/build_wave52r_h08_backward_global_defect_analysis.py `",
            "  --config config/analysis/wave52r_h08_backward_global_defect_analysis.yaml `",
            f"  --run-id {run_id}",
            "",
            "conda run --no-capture-output -n pinns_env python -B scripts/reports/analysis/validate_wave52r_h08_backward_global_defect_analysis.py `",
            "  --config config/analysis/wave52r_h08_backward_global_defect_analysis.yaml `",
            f"  --run-directory output/analysis/wave_5_2r/h08_backward_global_defect_analysis/{run_id}",
            "```",
            "",
        ]
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="\n") as report_file:
        report_file.write("\n".join(report_lines).rstrip() + "\n")


def write_summary_yaml(
    output_path: Path,
    run_id: str,
    report_path: Path,
    run_payload_list: list[H08RunPayload],
    comparison_rows: list[dict[str, Any]],
    interference_rows: list[dict[str, Any]],
    plot_path_list: list[Path],
    reproduction_difference: float,
) -> None:

    """Write the machine-readable diagnostic summary."""

    summary_dictionary = {
        "schema_version": 1,
        "diagnostic_id": "wave52r_h08_backward_global_defect_analysis",
        "run_id": run_id,
        "training_executed": False,
        "checkpoint_modified": False,
        "registry_updated": False,
        "h08_run_count": len(run_payload_list),
        "surface_list": ["Fw", "Bw", "global"],
        "seed_list": [314159, 271828, 161803],
        "official_metric_max_abs_difference_deg": reproduction_difference,
        "official_metric_reproduction_passed": reproduction_difference <= 1.0e-6,
        "decision": "offset_dominant_direction_conditioned_with_global_interference",
        "h08_role": "forward_non_temporal_offline_specialist",
        "training_authorized": False,
        "integrated_specialist_authorized": False,
        "recommended_next_gate": "direction_specific_causal_a0_calibration_plan_if_desired",
        "selected_comparison_list": comparison_rows,
        "global_interference_list": interference_rows,
        "report_path": report_path.relative_to(PROJECT_PATH).as_posix(),
        "plot_path_list": [path.relative_to(PROJECT_PATH).as_posix() for path in plot_path_list],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(summary_dictionary, output_file, sort_keys=False)


def main() -> None:

    """Run the H08 backward/global defect diagnostic."""

    argument_namespace = parse_arguments()
    configuration = load_configuration(argument_namespace.config)
    run_id = argument_namespace.run_id or datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")
    output_directory = resolve_project_path(configuration["paths"]["output_root"]) / run_id
    report_path = resolve_project_path(configuration["paths"]["report_path"])
    asset_directory = report_path.parent / "assets"

    # Load Frozen Evidence
    metric_rows = load_curve_metric_rows(resolve_project_path(configuration["paths"]["curve_metrics_path"]))
    harmonic_order_list = [int(value) for value in configuration["analysis"]["harmonic_order_list"]]
    run_payload_list = [
        load_h08_run_payload(
            run_config,
            len(harmonic_order_list),
            configuration["metadata"]["split_signature"],
        )
        for run_config in configuration["h08_runs"]
    ]
    for payload in run_payload_list:
        expected_curve_count = int(configuration["analysis"]["expected_curve_count_by_surface"][payload.surface])
        assert payload.measured_curve_matrix.shape[0] == expected_curve_count

    # Build Diagnostic Tables
    relevant_candidate_ids = {run_config["candidate_id"] for run_config in configuration["h08_runs"]}
    relevant_candidate_ids.update(
        comparison["incumbent_candidate_id"] for comparison in configuration["selected_comparisons"]
    )
    candidate_summary_rows = build_candidate_summary_rows(metric_rows, relevant_candidate_ids)
    selected_comparison_rows, condition_delta_rows = build_selected_comparison_rows(configuration, metric_rows)
    global_interference_rows = build_global_interference_rows(metric_rows)
    condition_factor_rows = build_condition_factor_rows(condition_delta_rows)
    coefficient_band_rows, a0_summary_rows = build_coefficient_rows(
        run_payload_list,
        harmonic_order_list,
        configuration["analysis"]["harmonic_band_dictionary"],
    )
    seed_stability_rows = build_seed_stability_rows(candidate_summary_rows)
    reproduction_rows, reproduction_difference = reproduce_official_metrics(configuration, selected_comparison_rows)
    assert reproduction_difference <= float(configuration["analysis"]["official_reproduction_tolerance_deg"]), (
        f"Official selected metrics did not reproduce | max difference {reproduction_difference}"
    )

    # Write Machine-Readable Evidence
    write_csv(output_directory / CANDIDATE_SUMMARY_FILENAME, candidate_summary_rows)
    write_csv(output_directory / SELECTED_COMPARISON_FILENAME, selected_comparison_rows)
    write_csv(output_directory / GLOBAL_INTERFERENCE_FILENAME, global_interference_rows)
    write_csv(output_directory / CONDITION_FACTOR_FILENAME, condition_factor_rows)
    write_csv(
        output_directory / WORST_CONDITION_FILENAME,
        sorted(condition_delta_rows, key=lambda row: float(row["offset_delta_deg"]), reverse=True)[:30],
    )
    write_csv(output_directory / COEFFICIENT_BAND_FILENAME, coefficient_band_rows)
    write_csv(output_directory / A0_SUMMARY_FILENAME, a0_summary_rows)
    write_csv(output_directory / SEED_STABILITY_FILENAME, seed_stability_rows)
    write_csv(output_directory / "official_metric_reproduction.csv", reproduction_rows)
    write_csv(output_directory / ARTIFACT_INVENTORY_FILENAME, build_artifact_inventory(configuration, run_payload_list))

    # Generate Visual Evidence
    plot_path_list = [
        asset_directory / "selected_metric_improvements.png",
        asset_directory / "global_direction_interference.png",
        asset_directory / "condition_offset_deltas.png",
        asset_directory / "coefficient_a0_decomposition.png",
        asset_directory / "harmonic_band_correction_ratios.png",
        asset_directory / "representative_h08_curves.png",
    ]
    create_selected_metric_plot(selected_comparison_rows, plot_path_list[0])
    create_global_interference_plot(global_interference_rows, plot_path_list[1])
    create_condition_delta_plot(condition_delta_rows, plot_path_list[2])
    create_a0_plot(a0_summary_rows, plot_path_list[3])
    create_band_plot(coefficient_band_rows, plot_path_list[4])
    create_representative_curve_plot(run_payload_list, harmonic_order_list, plot_path_list[5])

    # Build Canonical Report And Summary
    build_report(
        report_path,
        run_id,
        selected_comparison_rows,
        global_interference_rows,
        condition_factor_rows,
        a0_summary_rows,
        seed_stability_rows,
        plot_path_list,
        reproduction_difference,
    )
    write_summary_yaml(
        output_directory / SUMMARY_FILENAME,
        run_id,
        report_path,
        run_payload_list,
        selected_comparison_rows,
        global_interference_rows,
        plot_path_list,
        reproduction_difference,
    )
    with (resolve_project_path(configuration["paths"]["output_root"]) / "latest_run.yaml").open(
        "w", encoding="utf-8", newline="\n"
    ) as latest_file:
        yaml.safe_dump({"run_id": run_id, "run_directory": output_directory.relative_to(PROJECT_PATH).as_posix()}, latest_file, sort_keys=False)

    print(f"H08 backward/global defect diagnostic complete | {output_directory}")
    print(f"Canonical report | {report_path}")


if __name__ == "__main__":
    main()
