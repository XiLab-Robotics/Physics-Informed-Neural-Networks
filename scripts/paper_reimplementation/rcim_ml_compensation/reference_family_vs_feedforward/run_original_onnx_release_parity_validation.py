"""Validate recovered original ONNX release parity against repo archives."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import pickle
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[4]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import numpy as np
import onnxruntime as ort
import pandas as pd
import yaml
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank import (
    exact_paper_model_bank_support,
)
from scripts.paper_reimplementation.rcim_ml_compensation.harmonic_wise_comparison import harmonic_wise_support
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support as track2_support,
)
from scripts.training import shared_training_infrastructure

DEFAULT_EXACT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "exact_model_bank"
    / "baseline.yaml"
)
DEFAULT_TRACK2_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "full_track2_matrix_template.yaml"
)
DEFAULT_ONNX_RELEASE_ROOT = (
    PROJECT_PATH
    / "reference"
    / "rcim_ml_compensation_recovered_assets"
    / "models"
    / "exact_onnx_paper_release"
)
DEFAULT_REPO_ARCHIVE_ROOT = PROJECT_PATH / "models" / "paper_reference" / "rcim_original" / "forward"
DEFAULT_SOURCE_DATAFRAME_PATH = (
    PROJECT_PATH
    / "reference"
    / "rcim_ml_compensation_recovered_assets"
    / "code"
    / "original_pipeline"
    / "dataFrame_prediction_Fw_v14_newFreq.csv"
)
DEFAULT_OUTPUT_ROOT = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "rcim_original_onnx_release_parity"
)
DEFAULT_REPORT_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "validation_checks"
    / "track2"
)

FAMILY_FOLDER_LOOKUP = {
    "SVR": "svm_reference_models",
    "MLP": "mlp_reference_models",
    "RF": "rf_reference_models",
    "DT": "dt_reference_models",
    "ET": "et_reference_models",
    "ERT": "ert_reference_models",
    "GBM": "gbm_reference_models",
    "HGBM": "hgbm_reference_models",
    "XGBM": "xgbm_reference_models",
    "LGBM": "lgbm_reference_models",
}
ONNX_TARGET_PATTERN = re.compile(r"_(ampl|phase)(\d+)(?: \(\d+\))?\.onnx$")


@dataclass(frozen=True)
class OnnxTargetEntry:

    """One recovered ONNX target model resolved from the release tree."""

    family_name: str
    target_kind: str
    harmonic_order: int
    target_name: str
    onnx_model_path: Path


def format_project_path(path_value: Path) -> str:

    """Format a path relative to the repository when possible."""

    return shared_training_infrastructure.format_project_relative_path(path_value)


def resolve_target_name(target_kind: str, harmonic_order: int) -> str:

    """Resolve the recovered exact-paper target name."""

    return f"fft_y_Fw_filtered_{target_kind}_{harmonic_order}"


def load_yaml_dictionary(yaml_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary."""

    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        loaded_dictionary = yaml.safe_load(yaml_file)
    assert isinstance(loaded_dictionary, dict), f"Expected YAML dictionary | {yaml_path}"
    return loaded_dictionary


def write_yaml_dictionary(yaml_path: Path, payload: dict[str, Any]) -> None:

    """Write one YAML dictionary with stable formatting."""

    yaml_path.parent.mkdir(parents=True, exist_ok=True)
    with yaml_path.open("w", encoding="utf-8", newline="\n") as yaml_file:
        yaml.safe_dump(payload, yaml_file, sort_keys=False, allow_unicode=False)


def build_onnx_release_manifest(
    onnx_release_root: Path,
) -> tuple[dict[tuple[str, str, int], OnnxTargetEntry], list[dict[str, Any]], list[dict[str, Any]]]:

    """Build a deterministic manifest for the recovered ONNX release."""

    grouped_path_dictionary: dict[tuple[str, str, int], list[Path]] = {}
    for onnx_model_path in sorted(onnx_release_root.rglob("*.onnx")):
        relative_part_list = onnx_model_path.relative_to(onnx_release_root).parts
        if len(relative_part_list) != 3:
            continue
        family_name, target_folder, file_name = relative_part_list
        match = ONNX_TARGET_PATTERN.search(file_name)
        if match is None:
            continue
        parsed_target_kind = str(match.group(1))
        harmonic_order = int(match.group(2))
        expected_target_folder = parsed_target_kind
        if target_folder != expected_target_folder:
            continue
        manifest_key = (family_name, parsed_target_kind, harmonic_order)
        grouped_path_dictionary.setdefault(manifest_key, []).append(onnx_model_path)

    manifest_dictionary: dict[tuple[str, str, int], OnnxTargetEntry] = {}
    duplicate_entry_list: list[dict[str, Any]] = []
    for manifest_key, path_list in sorted(grouped_path_dictionary.items()):
        selected_path = sorted(path_list, key=lambda path: (" (" in path.name, path.name))[0]
        family_name, target_kind, harmonic_order = manifest_key
        if len(path_list) > 1:
            duplicate_entry_list.append(
                {
                    "family_name": family_name,
                    "target_kind": target_kind,
                    "harmonic_order": harmonic_order,
                    "selected_path": format_project_path(selected_path),
                    "duplicate_path_list": [format_project_path(path) for path in path_list],
                }
            )
        manifest_dictionary[manifest_key] = OnnxTargetEntry(
            family_name=family_name,
            target_kind=target_kind,
            harmonic_order=harmonic_order,
            target_name=resolve_target_name(target_kind, harmonic_order),
            onnx_model_path=selected_path,
        )

    missing_entry_list: list[dict[str, Any]] = []
    expected_harmonic_order_list = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
    for family_name in FAMILY_FOLDER_LOOKUP:
        for target_kind in ["ampl", "phase"]:
            for harmonic_order in expected_harmonic_order_list:
                manifest_key = (family_name, target_kind, harmonic_order)
                if manifest_key not in manifest_dictionary:
                    missing_entry_list.append(
                        {
                            "family_name": family_name,
                            "target_kind": target_kind,
                            "harmonic_order": harmonic_order,
                        }
                    )

    return manifest_dictionary, duplicate_entry_list, missing_entry_list


def predict_onnx_model(onnx_model_path: Path, feature_matrix: pd.DataFrame | np.ndarray) -> np.ndarray:

    """Run one ONNX target model on the CPU provider."""

    session = ort.InferenceSession(str(onnx_model_path), providers=["CPUExecutionProvider"])
    input_name = session.get_inputs()[0].name
    input_array = np.asarray(feature_matrix, dtype=np.float32)
    input_array = np.ascontiguousarray(input_array)
    output_array = session.run(None, {input_name: input_array})[0]
    return np.asarray(output_array, dtype=np.float64).reshape(-1)


def predict_python_model(
    python_model_path: Path,
    family_name: str,
    feature_matrix: pd.DataFrame,
) -> np.ndarray:

    """Run one archived Python target model."""

    with python_model_path.open("rb") as model_file:
        model_object = pickle.load(model_file)
    if family_name == "XGBM":
        model_input: pd.DataFrame | np.ndarray = feature_matrix.to_numpy(dtype=np.float32)
    else:
        model_input = feature_matrix
    prediction_array = model_object.predict(model_input)
    return np.asarray(prediction_array, dtype=np.float64).reshape(-1)


def build_repo_reference_entry_lookup(repo_archive_root: Path) -> dict[tuple[str, str, int], dict[str, Any]]:

    """Build a lookup for current repo archived original forward models."""

    reference_entry_lookup: dict[tuple[str, str, int], dict[str, Any]] = {}
    for family_name, archive_folder in FAMILY_FOLDER_LOOKUP.items():
        inventory_path = repo_archive_root / archive_folder / "reference_inventory.yaml"
        inventory_dictionary = load_yaml_dictionary(inventory_path)
        for reference_entry in inventory_dictionary["reference_models"]:
            target_kind = "ampl" if reference_entry["target_kind"] == "amplitude" else "phase"
            manifest_key = (family_name, target_kind, int(reference_entry["harmonic_order"]))
            reference_entry_lookup[manifest_key] = reference_entry
    return reference_entry_lookup


def compute_target_metric_dictionary(
    truth_vector: np.ndarray,
    prediction_vector: np.ndarray,
) -> dict[str, float]:

    """Compute target-level regression metrics."""

    mse_value = float(mean_squared_error(truth_vector, prediction_vector))
    return {
        "mse": mse_value,
        "rmse": float(np.sqrt(mse_value)),
        "mae": float(mean_absolute_error(truth_vector, prediction_vector)),
        "mape_percent": exact_paper_model_bank_support._safe_mape(truth_vector, prediction_vector),
    }


def compute_curve_mean_centering_metric_dictionary(
    truth_curve_deg: np.ndarray,
    predicted_curve_deg: np.ndarray,
) -> dict[str, float]:

    """Compute raw and mean-centered metrics for one Track 2 curve."""

    truth_curve = np.asarray(truth_curve_deg, dtype=np.float64).reshape(-1)
    predicted_curve = np.asarray(predicted_curve_deg, dtype=np.float64).reshape(-1)
    raw_residual_curve = predicted_curve - truth_curve

    truth_mean_deg = float(np.mean(truth_curve))
    predicted_mean_deg = float(np.mean(predicted_curve))
    centered_truth_curve = truth_curve - truth_mean_deg
    centered_predicted_curve = predicted_curve - predicted_mean_deg
    centered_residual_curve = centered_predicted_curve - centered_truth_curve

    raw_mae_deg = float(np.mean(np.abs(raw_residual_curve)))
    raw_rmse_deg = float(np.sqrt(np.mean(raw_residual_curve ** 2)))
    mean_centered_mae_deg = float(np.mean(np.abs(centered_residual_curve)))
    mean_centered_rmse_deg = float(np.sqrt(np.mean(centered_residual_curve ** 2)))
    offset_error_deg = float(predicted_mean_deg - truth_mean_deg)

    return {
        "truth_mean_deg": truth_mean_deg,
        "predicted_mean_deg": predicted_mean_deg,
        "offset_error_deg": offset_error_deg,
        "absolute_offset_error_deg": float(abs(offset_error_deg)),
        "raw_mae_deg": raw_mae_deg,
        "raw_rmse_deg": raw_rmse_deg,
        "mean_centered_mae_deg": mean_centered_mae_deg,
        "mean_centered_rmse_deg": mean_centered_rmse_deg,
        "mae_improvement_deg": float(raw_mae_deg - mean_centered_mae_deg),
        "rmse_improvement_deg": float(raw_rmse_deg - mean_centered_rmse_deg),
        "mae_improvement_pct": compute_improvement_percent(raw_mae_deg, mean_centered_mae_deg),
        "rmse_improvement_pct": compute_improvement_percent(raw_rmse_deg, mean_centered_rmse_deg),
    }


def compute_improvement_percent(raw_metric_value: float, adjusted_metric_value: float) -> float:

    """Compute percentage improvement from a raw metric to an adjusted metric."""

    if abs(raw_metric_value) < 1.0e-12:
        return 0.0
    return float(100.0 * (raw_metric_value - adjusted_metric_value) / raw_metric_value)


def summarize_mean_centering_metric_dictionary(
    metric_dictionary_list: list[dict[str, float]],
) -> dict[str, float]:

    """Summarize one list of mean-centering metric dictionaries."""

    assert metric_dictionary_list, "Mean-centering metric dictionary list must not be empty"
    metric_name_list = list(metric_dictionary_list[0].keys())
    summary_dictionary = {
        metric_name: float(np.mean([metric_dictionary[metric_name] for metric_dictionary in metric_dictionary_list]))
        for metric_name in metric_name_list
    }
    summary_dictionary["curve_count"] = int(len(metric_dictionary_list))
    summary_dictionary["p95_absolute_offset_error_deg"] = float(
        np.percentile(
            [metric_dictionary["absolute_offset_error_deg"] for metric_dictionary in metric_dictionary_list],
            95.0,
        )
    )
    return summary_dictionary


def build_table_parity_result(
    exact_config_path: Path,
    source_dataframe_path: Path,
    onnx_manifest_dictionary: dict[tuple[str, str, int], OnnxTargetEntry],
    repo_reference_entry_lookup: dict[tuple[str, str, int], dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:

    """Evaluate ONNX and repo original archives on the exact-paper split."""

    exact_training_config = exact_paper_model_bank_support.load_exact_model_bank_config(exact_config_path)
    exact_training_config["paths"]["source_dataframe_path"] = format_project_path(source_dataframe_path)
    dataset_bundle = exact_paper_model_bank_support.build_exact_paper_dataset_bundle(exact_training_config)
    feature_matrix = dataset_bundle.test_feature_matrix
    truth_matrix = dataset_bundle.test_target_matrix
    target_index_lookup = {
        target_name: target_index
        for target_index, target_name in enumerate(dataset_bundle.target_name_list)
    }

    target_result_list: list[dict[str, Any]] = []
    failure_entry_list: list[dict[str, Any]] = []
    for manifest_key, onnx_entry in sorted(onnx_manifest_dictionary.items()):
        if manifest_key not in repo_reference_entry_lookup:
            continue
        target_name = onnx_entry.target_name
        if target_name not in target_index_lookup:
            continue
        truth_vector = truth_matrix.to_numpy(dtype=np.float64)[:, target_index_lookup[target_name]]
        repo_entry = repo_reference_entry_lookup[manifest_key]
        repo_python_model_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
            repo_entry["python_model_path"]
        )
        try:
            onnx_prediction = predict_onnx_model(onnx_entry.onnx_model_path, feature_matrix)
            repo_prediction = predict_python_model(repo_python_model_path, onnx_entry.family_name, feature_matrix)
        except Exception as error:
            failure_entry_list.append(
                {
                    "stage": "tables_2_5",
                    "family_name": onnx_entry.family_name,
                    "target_kind": onnx_entry.target_kind,
                    "harmonic_order": onnx_entry.harmonic_order,
                    "onnx_model_path": format_project_path(onnx_entry.onnx_model_path),
                    "error_type": type(error).__name__,
                    "error_message": str(error),
                }
            )
            continue

        onnx_metric_dictionary = compute_target_metric_dictionary(truth_vector, onnx_prediction)
        repo_metric_dictionary = compute_target_metric_dictionary(truth_vector, repo_prediction)
        target_result_list.append(
            {
                "family_name": onnx_entry.family_name,
                "target_name": target_name,
                "target_kind": onnx_entry.target_kind,
                "harmonic_order": onnx_entry.harmonic_order,
                "onnx_model_path": format_project_path(onnx_entry.onnx_model_path),
                "repo_python_model_path": format_project_path(repo_python_model_path),
                "onnx_metrics": onnx_metric_dictionary,
                "repo_metrics": repo_metric_dictionary,
                "delta_metrics": {
                    metric_name: float(onnx_metric_dictionary[metric_name] - repo_metric_dictionary[metric_name])
                    for metric_name in ["mae", "rmse", "mape_percent"]
                },
                "max_abs_prediction_delta": float(np.max(np.abs(onnx_prediction - repo_prediction))),
                "mean_abs_prediction_delta": float(np.mean(np.abs(onnx_prediction - repo_prediction))),
            }
        )

    return target_result_list, failure_entry_list


def build_onnx_prediction_dictionary_for_track2(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    family_name: str,
    onnx_manifest_dictionary: dict[tuple[str, str, int], OnnxTargetEntry],
    selected_harmonic_list: list[int],
) -> dict[str, np.ndarray]:

    """Predict all ONNX targets needed by one Track 2 family."""

    feature_matrix = track2_support.build_reference_feature_matrix(curve_record_list)
    prediction_dictionary: dict[str, np.ndarray] = {}
    for harmonic_order in selected_harmonic_list:
        for target_kind in ["ampl", "phase"]:
            if target_kind == "phase" and harmonic_order == 0:
                continue
            manifest_key = (family_name, target_kind, harmonic_order)
            onnx_entry = onnx_manifest_dictionary[manifest_key]
            prediction_dictionary[(target_kind, harmonic_order)] = predict_onnx_model(
                onnx_entry.onnx_model_path,
                feature_matrix,
            )
    return prediction_dictionary


def evaluate_track2_onnx_family(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    family_name: str,
    onnx_manifest_dictionary: dict[tuple[str, str, int], OnnxTargetEntry],
    selected_harmonic_list: list[int],
    percentage_error_denominator: str,
) -> tuple[list[dict[str, Any]], dict[str, float]]:

    """Evaluate one recovered ONNX family through Track 2 curve reconstruction."""

    prediction_dictionary = build_onnx_prediction_dictionary_for_track2(
        curve_record_list,
        family_name,
        onnx_manifest_dictionary,
        selected_harmonic_list,
    )
    metric_entry_list: list[dict[str, Any]] = []
    for sample_index, curve_record in enumerate(curve_record_list):
        coefficient_dictionary: dict[str, float] = {}
        for harmonic_order in selected_harmonic_list:
            predicted_amplitude = float(prediction_dictionary[("ampl", harmonic_order)][sample_index])
            if harmonic_order == 0:
                coefficient_dictionary["coefficient_cos_h0"] = predicted_amplitude
                continue
            predicted_phase = float(prediction_dictionary[("phase", harmonic_order)][sample_index])
            coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"] = float(
                predicted_amplitude * np.cos(predicted_phase)
            )
            coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"] = float(
                -predicted_amplitude * np.sin(predicted_phase)
            )
        predicted_curve_deg = harmonic_wise_support.reconstruct_curve_from_coefficients(
            curve_record.angular_position_deg,
            selected_harmonic_list,
            coefficient_dictionary,
        )
        metric_dictionary = harmonic_wise_support.compute_curve_metric_dictionary(
            curve_record.transmission_error_deg,
            predicted_curve_deg,
            percentage_error_denominator,
        )
        mean_centering_metric_dictionary = compute_curve_mean_centering_metric_dictionary(
            curve_record.transmission_error_deg,
            predicted_curve_deg,
        )
        metric_entry_list.append(
            {
                "candidate_id": f"{family_name}_original_onnx_Fw",
                "family_name": family_name,
                "source_file_path": format_project_path(curve_record.source_file_path),
                "direction_label": curve_record.direction_label,
                "speed_rpm": float(curve_record.speed_rpm),
                "torque_nm": float(curve_record.torque_nm),
                "oil_temperature_deg": float(curve_record.oil_temperature_deg),
                "metrics": metric_dictionary,
                "mean_centering_metrics": mean_centering_metric_dictionary,
            }
        )

    return metric_entry_list, track2_support.summarize_metric_dictionary(
        [entry["metrics"] for entry in metric_entry_list]
    )


def build_track2_parity_result(
    track2_config_path: Path,
    onnx_manifest_dictionary: dict[tuple[str, str, int], OnnxTargetEntry],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:

    """Evaluate recovered ONNX release and repo original archive in Track 2."""

    track2_config = track2_support.load_reference_family_comparison_config(track2_config_path)
    selected_harmonic_list = [
        int(harmonic_order)
        for harmonic_order in track2_config["evaluation"]["selected_harmonics"]
    ]
    curve_record_list, _, _, _ = track2_support.build_curve_record_list(track2_config, selected_harmonic_list)
    forward_curve_record_list = [
        curve_record
        for curve_record in curve_record_list
        if str(curve_record.direction_label).strip().lower() == "forward"
    ]
    percentage_error_denominator = str(track2_config["comparison"]["percentage_error_denominator"])

    generated_candidate_list = track2_support.build_generated_candidate_configuration_list(track2_config)
    repo_candidate_configuration_list = [
        candidate_configuration
        for candidate_configuration in generated_candidate_list
        if candidate_configuration["candidate_source_label"] == "rcim_original"
        and candidate_configuration["candidate_surface"] == "Fw"
        and candidate_configuration["candidate_family"] in FAMILY_FOLDER_LOOKUP
    ]

    repo_track2_summary_list: list[dict[str, Any]] = []
    track2_offset_entry_list: list[dict[str, Any]] = []
    for candidate_configuration in repo_candidate_configuration_list:
        candidate = track2_support.load_track2_candidate(candidate_configuration)
        per_candidate_entry_list, _ = track2_support.evaluate_track2_candidate(
            candidate,
            curve_record_list,
            percentage_error_denominator,
            include_curve_payload=True,
        )
        repo_mean_centering_metric_list: list[dict[str, float]] = []
        for per_candidate_entry in per_candidate_entry_list:
            mean_centering_metric_dictionary = compute_curve_mean_centering_metric_dictionary(
                np.asarray(per_candidate_entry["truth_curve_deg"], dtype=np.float64),
                np.asarray(per_candidate_entry["predicted_curve_deg"], dtype=np.float64),
            )
            repo_mean_centering_metric_list.append(mean_centering_metric_dictionary)
            track2_offset_entry_list.append(
                {
                    "source": "repo_python_archive",
                    "family_name": candidate.candidate_family,
                    "candidate_id": candidate.candidate_id,
                    "source_file_path": per_candidate_entry["source_file_path"],
                    "direction_label": per_candidate_entry["direction_label"],
                    "speed_rpm": float(per_candidate_entry["speed_rpm"]),
                    "torque_nm": float(per_candidate_entry["torque_nm"]),
                    "oil_temperature_deg": float(per_candidate_entry["oil_temperature_deg"]),
                    "raw_metrics": per_candidate_entry["metrics"],
                    "mean_centering_metrics": mean_centering_metric_dictionary,
                }
            )
        repo_track2_summary_list.append(
            {
                "family_name": candidate.candidate_family,
                "candidate_id": candidate.candidate_id,
                "metrics": track2_support.summarize_metric_dictionary(
                    [entry["metrics"] for entry in per_candidate_entry_list]
                ),
                "mean_centering_metrics": summarize_mean_centering_metric_dictionary(
                    repo_mean_centering_metric_list
                ),
            }
        )

    onnx_track2_summary_list: list[dict[str, Any]] = []
    failure_entry_list: list[dict[str, Any]] = []
    for family_name in FAMILY_FOLDER_LOOKUP:
        try:
            onnx_metric_entry_list, metric_dictionary = evaluate_track2_onnx_family(
                forward_curve_record_list,
                family_name,
                onnx_manifest_dictionary,
                selected_harmonic_list,
                percentage_error_denominator,
            )
        except Exception as error:
            failure_entry_list.append(
                {
                    "stage": "track2",
                    "family_name": family_name,
                    "error_type": type(error).__name__,
                    "error_message": str(error),
                }
            )
            continue
        for onnx_metric_entry in onnx_metric_entry_list:
            track2_offset_entry_list.append(
                {
                    "source": "original_onnx_release",
                    "family_name": family_name,
                    "candidate_id": onnx_metric_entry["candidate_id"],
                    "source_file_path": onnx_metric_entry["source_file_path"],
                    "direction_label": onnx_metric_entry["direction_label"],
                    "speed_rpm": float(onnx_metric_entry["speed_rpm"]),
                    "torque_nm": float(onnx_metric_entry["torque_nm"]),
                    "oil_temperature_deg": float(onnx_metric_entry["oil_temperature_deg"]),
                    "raw_metrics": onnx_metric_entry["metrics"],
                    "mean_centering_metrics": onnx_metric_entry["mean_centering_metrics"],
                }
            )
        onnx_track2_summary_list.append(
            {
                "family_name": family_name,
                "candidate_id": f"{family_name}_original_onnx_Fw",
                "metrics": metric_dictionary,
                "mean_centering_metrics": summarize_mean_centering_metric_dictionary(
                    [entry["mean_centering_metrics"] for entry in onnx_metric_entry_list]
                ),
            }
        )

    repo_metric_lookup = {
        entry["family_name"]: entry["metrics"]
        for entry in repo_track2_summary_list
    }
    track2_delta_list: list[dict[str, Any]] = []
    for onnx_entry in onnx_track2_summary_list:
        family_name = onnx_entry["family_name"]
        repo_metrics = repo_metric_lookup.get(family_name)
        if repo_metrics is None:
            continue
        onnx_metrics = onnx_entry["metrics"]
        track2_delta_list.append(
            {
                "family_name": family_name,
                "onnx_candidate_id": onnx_entry["candidate_id"],
                "repo_candidate_id": next(
                    entry["candidate_id"]
                    for entry in repo_track2_summary_list
                    if entry["family_name"] == family_name
                ),
                "onnx_metrics": onnx_metrics,
                "repo_metrics": repo_metrics,
                "delta_metrics": {
                    metric_name: float(onnx_metrics[metric_name] - repo_metrics[metric_name])
                    for metric_name in ["mae", "rmse", "mean_percentage_error_pct", "p95_mean_percentage_error_pct"]
                },
            }
        )

    return (
        repo_track2_summary_list,
        onnx_track2_summary_list,
        track2_delta_list + failure_entry_list,
        track2_offset_entry_list,
    )


def summarize_table_parity(target_result_list: list[dict[str, Any]]) -> list[dict[str, Any]]:

    """Build family-level Tables 2-5 parity summary."""

    family_summary_list: list[dict[str, Any]] = []
    for family_name in FAMILY_FOLDER_LOOKUP:
        family_target_list = [
            entry
            for entry in target_result_list
            if entry["family_name"] == family_name
        ]
        if not family_target_list:
            continue
        family_summary_list.append(
            {
                "family_name": family_name,
                "target_count": len(family_target_list),
                "mean_onnx_mae": float(np.mean([entry["onnx_metrics"]["mae"] for entry in family_target_list])),
                "mean_repo_mae": float(np.mean([entry["repo_metrics"]["mae"] for entry in family_target_list])),
                "mean_onnx_rmse": float(np.mean([entry["onnx_metrics"]["rmse"] for entry in family_target_list])),
                "mean_repo_rmse": float(np.mean([entry["repo_metrics"]["rmse"] for entry in family_target_list])),
                "max_abs_prediction_delta": float(
                    np.max([entry["max_abs_prediction_delta"] for entry in family_target_list])
                ),
                "mean_abs_prediction_delta": float(
                    np.mean([entry["mean_abs_prediction_delta"] for entry in family_target_list])
                ),
            }
        )
    return family_summary_list


def write_target_parity_csv(csv_path: Path, target_result_list: list[dict[str, Any]]) -> None:

    """Write target-level parity rows to CSV."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        field_name_list = [
            "family_name",
            "target_name",
            "onnx_mae",
            "repo_mae",
            "delta_mae",
            "onnx_rmse",
            "repo_rmse",
            "delta_rmse",
            "max_abs_prediction_delta",
            "mean_abs_prediction_delta",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=field_name_list, lineterminator="\n")
        writer.writeheader()
        for entry in target_result_list:
            writer.writerow(
                {
                    "family_name": entry["family_name"],
                    "target_name": entry["target_name"],
                    "onnx_mae": entry["onnx_metrics"]["mae"],
                    "repo_mae": entry["repo_metrics"]["mae"],
                    "delta_mae": entry["delta_metrics"]["mae"],
                    "onnx_rmse": entry["onnx_metrics"]["rmse"],
                    "repo_rmse": entry["repo_metrics"]["rmse"],
                    "delta_rmse": entry["delta_metrics"]["rmse"],
                    "max_abs_prediction_delta": entry["max_abs_prediction_delta"],
                    "mean_abs_prediction_delta": entry["mean_abs_prediction_delta"],
                }
            )


def write_track2_offset_diagnostic_csv(csv_path: Path, offset_entry_list: list[dict[str, Any]]) -> None:

    """Write Track 2 per-curve raw and mean-centered diagnostic rows."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        field_name_list = [
            "source",
            "family_name",
            "candidate_id",
            "source_file_path",
            "direction_label",
            "speed_rpm",
            "torque_nm",
            "oil_temperature_deg",
            "raw_mae_deg",
            "raw_rmse_deg",
            "raw_mean_percentage_error_pct",
            "truth_mean_deg",
            "predicted_mean_deg",
            "offset_error_deg",
            "absolute_offset_error_deg",
            "mean_centered_mae_deg",
            "mean_centered_rmse_deg",
            "mae_improvement_deg",
            "mae_improvement_pct",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=field_name_list, lineterminator="\n")
        writer.writeheader()
        for entry in offset_entry_list:
            raw_metric_dictionary = entry["raw_metrics"]
            mean_centering_dictionary = entry["mean_centering_metrics"]
            writer.writerow(
                {
                    "source": entry["source"],
                    "family_name": entry["family_name"],
                    "candidate_id": entry["candidate_id"],
                    "source_file_path": entry["source_file_path"],
                    "direction_label": entry["direction_label"],
                    "speed_rpm": entry["speed_rpm"],
                    "torque_nm": entry["torque_nm"],
                    "oil_temperature_deg": entry["oil_temperature_deg"],
                    "raw_mae_deg": raw_metric_dictionary["mae"],
                    "raw_rmse_deg": raw_metric_dictionary["rmse"],
                    "raw_mean_percentage_error_pct": raw_metric_dictionary["mean_percentage_error_pct"],
                    "truth_mean_deg": mean_centering_dictionary["truth_mean_deg"],
                    "predicted_mean_deg": mean_centering_dictionary["predicted_mean_deg"],
                    "offset_error_deg": mean_centering_dictionary["offset_error_deg"],
                    "absolute_offset_error_deg": mean_centering_dictionary["absolute_offset_error_deg"],
                    "mean_centered_mae_deg": mean_centering_dictionary["mean_centered_mae_deg"],
                    "mean_centered_rmse_deg": mean_centering_dictionary["mean_centered_rmse_deg"],
                    "mae_improvement_deg": mean_centering_dictionary["mae_improvement_deg"],
                    "mae_improvement_pct": mean_centering_dictionary["mae_improvement_pct"],
                }
            )


def build_parity_report_markdown(validation_summary: dict[str, Any]) -> str:

    """Build the Markdown report for original ONNX release parity."""

    manifest_summary = validation_summary["manifest_summary"]
    table_family_summary = validation_summary["tables_2_5_family_summary"]
    track2_delta_list = validation_summary["track2_delta_summary"]
    onnx_track2_summary_list = validation_summary["track2_onnx_family_summary"]
    repo_track2_summary_list = validation_summary["track2_repo_family_summary"]

    line_list = [
        "# RCIM Original ONNX Release Parity Validation",
        "",
        "## Overview",
        "",
        "This report compares the recovered original ONNX release against the",
        "current repository `rcim_original` forward archives using the same",
        "forward evaluation surfaces.",
        "",
        "## Manifest Status",
        "",
        f"- ONNX release root: `{validation_summary['onnx_release_root']}`;",
        f"- repo original archive root: `{validation_summary['repo_archive_root']}`;",
        f"- exact-paper source dataframe: `{validation_summary['source_dataframe_path']}`;",
        f"- ONNX file count: `{manifest_summary['onnx_file_count']}`;",
        f"- resolved target model count: `{manifest_summary['resolved_target_model_count']}`;",
        f"- expected target model count: `{manifest_summary['expected_target_model_count']}`;",
        f"- duplicate target keys: `{manifest_summary['duplicate_target_key_count']}`;",
        f"- missing target keys: `{manifest_summary['missing_target_key_count']}`.",
        "",
        "## Tables 2-5 Split Parity",
        "",
        "| Family | Targets | ONNX Mean MAE | Repo Mean MAE | ONNX Mean RMSE | Repo Mean RMSE | Max Prediction Delta | Mean Prediction Delta |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for family_entry in table_family_summary:
        line_list.append(
            f"| `{family_entry['family_name']}` | "
            f"{family_entry['target_count']} | "
            f"{family_entry['mean_onnx_mae']:.6f} | "
            f"{family_entry['mean_repo_mae']:.6f} | "
            f"{family_entry['mean_onnx_rmse']:.6f} | "
            f"{family_entry['mean_repo_rmse']:.6f} | "
            f"{family_entry['max_abs_prediction_delta']:.6f} | "
            f"{family_entry['mean_abs_prediction_delta']:.6f} |"
        )

    line_list.extend(
        [
            "",
            "## Track 2 Forward Curve Parity",
            "",
            "| Family | ONNX MAE [deg] | Repo MAE [deg] | Delta MAE [deg] | ONNX MPE [%] | Repo MPE [%] | Delta MPE [%] |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for delta_entry in track2_delta_list:
        if "delta_metrics" not in delta_entry:
            continue
        line_list.append(
            f"| `{delta_entry['family_name']}` | "
            f"{delta_entry['onnx_metrics']['mae']:.6f} | "
            f"{delta_entry['repo_metrics']['mae']:.6f} | "
            f"{delta_entry['delta_metrics']['mae']:.6f} | "
            f"{delta_entry['onnx_metrics']['mean_percentage_error_pct']:.3f} | "
            f"{delta_entry['repo_metrics']['mean_percentage_error_pct']:.3f} | "
            f"{delta_entry['delta_metrics']['mean_percentage_error_pct']:.3f} |"
        )

    line_list.extend(
        [
            "",
            "## Track 2 Mean-Centered Offset Diagnostics",
            "",
            "| Source | Family | Raw MAE [deg] | Centered MAE [deg] | Mean Abs Offset [deg] | MAE Improvement [%] |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for source_label, family_summary_list in [
        ("ONNX", onnx_track2_summary_list),
        ("Repo", repo_track2_summary_list),
    ]:
        for family_entry in family_summary_list:
            mean_centering_dictionary = family_entry["mean_centering_metrics"]
            line_list.append(
                f"| {source_label} | `{family_entry['family_name']}` | "
                f"{mean_centering_dictionary['raw_mae_deg']:.6f} | "
                f"{mean_centering_dictionary['mean_centered_mae_deg']:.6f} | "
                f"{mean_centering_dictionary['absolute_offset_error_deg']:.6f} | "
                f"{mean_centering_dictionary['mae_improvement_pct']:.3f} |"
            )

    line_list.extend(
        [
            "",
            "## Artifacts",
            "",
            f"- validation summary: `{validation_summary['validation_summary_path']}`;",
            f"- target parity CSV: `{validation_summary['target_parity_csv_path']}`;",
            f"- Track 2 offset diagnostics CSV: `{validation_summary['track2_offset_diagnostic_csv_path']}`.",
        ]
    )

    failure_entry_list = validation_summary["failure_entry_list"]
    if failure_entry_list:
        failure_summary_dictionary: dict[tuple[str, str, str], int] = {}
        for failure_entry in failure_entry_list:
            summary_key = (
                str(failure_entry.get("stage", "unknown")),
                str(failure_entry.get("family_name", "unknown")),
                str(failure_entry.get("error_type", "unknown")),
            )
            failure_summary_dictionary[summary_key] = failure_summary_dictionary.get(summary_key, 0) + 1

        line_list.extend(
            [
                "",
                "## Failures",
                "",
                "Raw ONNX Runtime messages are preserved in the validation YAML.",
                "",
                "| Stage | Family | Error Type | Count |",
                "| --- | --- | --- | ---: |",
            ]
        )
        for (stage_name, family_name, error_type), failure_count in sorted(failure_summary_dictionary.items()):
            line_list.append(
                f"| `{stage_name}` | `{family_name}` | `{error_type}` | {failure_count} |"
            )

    return "\n".join(line_list) + "\n"


def run_original_onnx_release_parity_validation(
    exact_config_path: Path,
    track2_config_path: Path,
    onnx_release_root: Path,
    repo_archive_root: Path,
    source_dataframe_path: Path,
    output_suffix: str,
) -> tuple[Path, Path]:

    """Run the original ONNX release parity validation."""

    run_timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    run_instance_id = f"{run_timestamp}__original_onnx_release_{output_suffix}"
    output_directory = DEFAULT_OUTPUT_ROOT / run_instance_id
    output_directory.mkdir(parents=True, exist_ok=True)

    manifest_dictionary, duplicate_entry_list, missing_entry_list = build_onnx_release_manifest(onnx_release_root)
    repo_reference_entry_lookup = build_repo_reference_entry_lookup(repo_archive_root)
    target_result_list, table_failure_entry_list = build_table_parity_result(
        exact_config_path,
        source_dataframe_path,
        manifest_dictionary,
        repo_reference_entry_lookup,
    )
    table_family_summary = summarize_table_parity(target_result_list)
    (
        repo_track2_summary_list,
        onnx_track2_summary_list,
        track2_delta_or_failure_list,
        track2_offset_entry_list,
    ) = build_track2_parity_result(track2_config_path, manifest_dictionary)
    track2_failure_entry_list = [
        entry
        for entry in track2_delta_or_failure_list
        if "delta_metrics" not in entry
    ]
    track2_delta_list = [
        entry
        for entry in track2_delta_or_failure_list
        if "delta_metrics" in entry
    ]

    target_parity_csv_path = output_directory / "tables_2_5_target_parity.csv"
    write_target_parity_csv(target_parity_csv_path, target_result_list)
    track2_offset_diagnostic_csv_path = output_directory / "track2_curve_offset_diagnostics.csv"
    write_track2_offset_diagnostic_csv(track2_offset_diagnostic_csv_path, track2_offset_entry_list)

    validation_summary_path = output_directory / "validation_summary.yaml"
    report_path = DEFAULT_REPORT_ROOT / f"{run_timestamp}_original_onnx_release_{output_suffix}_report.md"
    validation_summary = {
        "run_instance_id": run_instance_id,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "onnx_release_root": format_project_path(onnx_release_root),
        "repo_archive_root": format_project_path(repo_archive_root),
        "source_dataframe_path": format_project_path(source_dataframe_path),
        "exact_config_path": format_project_path(exact_config_path),
        "track2_config_path": format_project_path(track2_config_path),
        "manifest_summary": {
            "onnx_file_count": len(list(onnx_release_root.rglob("*.onnx"))),
            "resolved_target_model_count": len(manifest_dictionary),
            "expected_target_model_count": len(FAMILY_FOLDER_LOOKUP) * 20,
            "duplicate_target_key_count": len(duplicate_entry_list),
            "missing_target_key_count": len(missing_entry_list),
            "duplicate_entry_list": duplicate_entry_list,
            "missing_entry_list": missing_entry_list,
        },
        "tables_2_5_family_summary": table_family_summary,
        "tables_2_5_target_result_count": len(target_result_list),
        "track2_repo_family_summary": repo_track2_summary_list,
        "track2_onnx_family_summary": onnx_track2_summary_list,
        "track2_delta_summary": track2_delta_list,
        "track2_offset_entry_count": len(track2_offset_entry_list),
        "failure_entry_list": table_failure_entry_list + track2_failure_entry_list,
        "validation_summary_path": format_project_path(validation_summary_path),
        "target_parity_csv_path": format_project_path(target_parity_csv_path),
        "track2_offset_diagnostic_csv_path": format_project_path(track2_offset_diagnostic_csv_path),
        "report_path": format_project_path(report_path),
    }
    write_yaml_dictionary(validation_summary_path, validation_summary)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(build_parity_report_markdown(validation_summary), encoding="utf-8", newline="\n")
    return validation_summary_path, report_path


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Validate recovered original ONNX release parity."
    )
    argument_parser.add_argument("--exact-config-path", type=Path, default=DEFAULT_EXACT_CONFIG_PATH)
    argument_parser.add_argument("--track2-config-path", type=Path, default=DEFAULT_TRACK2_CONFIG_PATH)
    argument_parser.add_argument("--onnx-release-root", type=Path, default=DEFAULT_ONNX_RELEASE_ROOT)
    argument_parser.add_argument("--repo-archive-root", type=Path, default=DEFAULT_REPO_ARCHIVE_ROOT)
    argument_parser.add_argument("--source-dataframe-path", type=Path, default=DEFAULT_SOURCE_DATAFRAME_PATH)
    argument_parser.add_argument("--output-suffix", type=str, default="parity_validation")
    return argument_parser.parse_args()


def main() -> None:

    """Run the command-line entry point."""

    arguments = parse_arguments()
    validation_summary_path, report_path = run_original_onnx_release_parity_validation(
        exact_config_path=shared_training_infrastructure.resolve_runtime_project_relative_path(
            arguments.exact_config_path
        ),
        track2_config_path=shared_training_infrastructure.resolve_runtime_project_relative_path(
            arguments.track2_config_path
        ),
        onnx_release_root=shared_training_infrastructure.resolve_runtime_project_relative_path(
            arguments.onnx_release_root
        ),
        repo_archive_root=shared_training_infrastructure.resolve_runtime_project_relative_path(
            arguments.repo_archive_root
        ),
        source_dataframe_path=shared_training_infrastructure.resolve_runtime_project_relative_path(
            arguments.source_dataframe_path
        ),
        output_suffix=arguments.output_suffix,
    )
    print(f"[DONE] Original ONNX parity summary written | {format_project_path(validation_summary_path)}")
    print(f"[DONE] Original ONNX parity report written | {format_project_path(report_path)}")


if __name__ == "__main__":
    main()
