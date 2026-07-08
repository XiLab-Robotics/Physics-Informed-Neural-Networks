"""Build familywise ONNX TE Curve Verification Pipeline reports."""

from __future__ import annotations

# Import Python Utilities
import argparse, csv, shutil, sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import matplotlib.pyplot as plt
import numpy as np
import onnxruntime as ort
import yaml
from numpy.lib.stride_tricks import sliding_window_view
from tqdm import tqdm

# Import Project Utilities
from scripts.reports.analysis import track2_circular_plotting
from scripts.tooling import repository_path_support
from scripts.training import shared_training_infrastructure, transmission_error_datamodule

DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_familywise_onnx_report"
DEFAULT_REPORT_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "te_curve_verification_pipeline"
    / "03_family_reports"
)
DEFAULT_GROUP_SPECIFICATION_LIST = [
    "simplified_dataset:setpoints",
    "polished_dataset:setpoints",
    "polished_dataset:actual_values",
]
REPORT_FILENAME_TEMPLATE = "track2_{model_family}_familywise_onnx_report.md"
SUMMARY_FILENAME = "track2_familywise_onnx_report_summary.yaml"
MODEL_INVENTORY_FILENAME = "model_inventory.csv"
PER_CURVE_METRICS_FILENAME = "per_curve_metrics.csv"
DEFAULT_CURVES_PER_PAGE = 12
TEMPORAL_ONNX_INFERENCE_BATCH_SIZE = 65536
SURFACE_ORDER_LIST = ["forward", "backward", "global"]
GROUP_TITLE_DICTIONARY = {
    ("simplified_dataset", "setpoints"): "Simplified Dataset + Setpoints",
    ("polished_dataset", "setpoints"): "Polished Dataset + Setpoints",
    ("polished_dataset", "actual_values"): "Polished Dataset + Actual Values",
}


@dataclass(frozen=True)
class ExportedModelEntry:

    """Store one exported ONNX model entry from a model inventory.

    Attributes:
        dataset_id: Dataset identifier used by the source run.
        input_mode: Input-mode contract used by the source run.
        model_family: Base family requested by the report.
        model_type: Training/export model type.
        surface: Model surface, either ``forward``, ``backward``, or
            ``global``.
        run_name: Logical training run name.
        run_instance_id: Immutable source run instance identifier.
        dataset_schema: Dataset schema stored in the export inventory.
        onnx_model_path: Project-resolved ONNX model path.
        python_model_path: Project-resolved Python model path.
        training_config_path: Project-resolved source-run training config path.
        source_output_directory: Project-relative source output directory.
        source_best_checkpoint_path: Project-relative source model path.
        source_inventory_path: Project-resolved export inventory path.
    """

    dataset_id: str
    input_mode: str
    model_family: str
    model_type: str
    surface: str
    run_name: str
    run_instance_id: str
    dataset_schema: str
    onnx_model_path: Path
    python_model_path: Path
    training_config_path: Path
    source_output_directory: str
    source_best_checkpoint_path: str
    source_inventory_path: Path


@dataclass(frozen=True)
class CurveEvaluationEntry:

    """Store one evaluated test curve and prediction payload."""

    group_id: str
    surface: str
    dataset_index: int
    source_file_path: str
    direction_label: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    angular_position_deg: np.ndarray
    target_curve_deg: np.ndarray
    prediction_curve_deg: np.ndarray
    plot_measured_angular_position_deg: np.ndarray
    plot_measured_curve_deg: np.ndarray
    plot_prediction_angular_position_deg: np.ndarray
    plot_prediction_curve_deg: np.ndarray
    metrics: dict[str, float]


def build_argument_parser() -> argparse.ArgumentParser:

    """Build command-line arguments for the familywise report."""

    parser = argparse.ArgumentParser(description="Build a familywise ONNX TE Curve Verification Pipeline report.")
    parser.add_argument("--model-family", default="tree", help="Exported base model family to evaluate.")
    parser.add_argument("--group", action="append", dest="group_specification_list", default=None, help="Dataset/input-mode group as dataset_id:input_mode. May be repeated.")
    parser.add_argument("--curves-per-page", type=int, default=DEFAULT_CURVES_PER_PAGE, help="Representative curves shown on each surface page.")
    parser.add_argument("--report-date", default=None, help="Optional YYYY-MM-DD report folder date.")
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT, help="Root for machine-readable output artifacts.")
    parser.add_argument("--report-root", type=Path, default=DEFAULT_REPORT_ROOT, help="Root for dated family report bundles.")
    parser.add_argument("--onnx-provider", action="append", default=None, help="ONNX Runtime provider. Defaults to CPUExecutionProvider.")
    repository_path_support.add_platform_arguments(parser)
    return parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def load_yaml_dictionary(path_value: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    with path_value.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {path_value}"
    return payload


def save_yaml_dictionary(path_value: Path, payload: dict[str, Any]) -> None:

    """Save one YAML dictionary to disk."""

    path_value.parent.mkdir(parents=True, exist_ok=True)
    with path_value.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=False)


def format_project_path(path_value: str | Path) -> str:

    """Return a stable project-relative path string."""

    return shared_training_infrastructure.format_project_relative_path(path_value).replace("\\", "/")


def resolve_project_path(path_value: str | Path) -> Path:

    """Resolve a repository-relative or absolute path."""

    return shared_training_infrastructure.resolve_runtime_project_relative_path(path_value)


def parse_group_specification(group_specification: str) -> tuple[str, str]:

    """Parse one dataset/input-mode group specification."""

    token_list = str(group_specification).strip().split(":")
    assert len(token_list) == 2, f"Group must use dataset_id:input_mode format | {group_specification}"
    dataset_id, input_mode = [token.strip() for token in token_list]
    assert dataset_id and input_mode, f"Group contains an empty token | {group_specification}"
    return dataset_id, input_mode


def resolve_inventory_path(dataset_id: str, input_mode: str) -> Path:

    """Resolve the exported model-development inventory for one group."""

    return PROJECT_PATH / "models" / dataset_id / input_mode / "exported" / "model_development_export_inventory.yaml"


def normalize_surface_name(surface_name: str) -> str:

    """Normalize inventory and report surface labels."""

    normalized_surface = str(surface_name).strip().lower()
    surface_alias_dictionary = {"fw": "forward", "bw": "backward"}
    normalized_surface = surface_alias_dictionary.get(normalized_surface, normalized_surface)
    assert normalized_surface in {"forward", "backward", "global"}, f"Unsupported surface | {surface_name}"
    return normalized_surface


def load_group_model_entries(dataset_id: str, input_mode: str, model_family: str) -> dict[str, ExportedModelEntry]:

    """Load and validate exported model entries for one dataset/input-mode group."""

    inventory_path = resolve_inventory_path(dataset_id, input_mode)
    assert inventory_path.exists(), f"Missing export inventory | {inventory_path}"
    inventory_dictionary = load_yaml_dictionary(inventory_path)
    entry_list = inventory_dictionary.get("entries", [])
    assert isinstance(entry_list, list), f"Inventory entries must be a list | {inventory_path}"

    surface_entry_dictionary: dict[str, ExportedModelEntry] = {}
    for raw_entry in entry_list:
        if str(raw_entry.get("model_family", "")).strip() != model_family:
            continue
        surface_name = normalize_surface_name(str(raw_entry["surface"]))
        assert surface_name not in surface_entry_dictionary, (
            "Duplicate exported model surface in inventory | "
            f"dataset={dataset_id} | input_mode={input_mode} | surface={surface_name}"
        )
        onnx_model_path = resolve_project_path(raw_entry["onnx_model_path"])
        python_model_path = resolve_project_path(raw_entry["python_model_path"])
        training_config_path = resolve_project_path(raw_entry["source_run_snapshot_path_map"]["training_config.snapshot.yaml"])
        assert onnx_model_path.exists(), f"Missing ONNX model | {onnx_model_path}"
        assert python_model_path.exists(), f"Missing Python model | {python_model_path}"
        assert training_config_path.exists(), f"Missing source training config | {training_config_path}"
        assert str(raw_entry.get("onnx_export_status", "")).strip() == "exported", (
            f"ONNX export is not marked exported | {onnx_model_path}"
        )
        surface_entry_dictionary[surface_name] = ExportedModelEntry(
            dataset_id=str(raw_entry["dataset_id"]),
            input_mode=str(raw_entry["input_mode"]),
            model_family=str(raw_entry["model_family"]),
            model_type=str(raw_entry["model_type"]),
            surface=surface_name,
            run_name=str(raw_entry["run_name"]),
            run_instance_id=str(raw_entry["run_instance_id"]),
            dataset_schema=str(raw_entry["dataset_schema"]),
            onnx_model_path=onnx_model_path,
            python_model_path=python_model_path,
            training_config_path=training_config_path,
            source_output_directory=str(raw_entry["source_output_directory"]),
            source_best_checkpoint_path=str(raw_entry["source_best_checkpoint_path"]),
            source_inventory_path=inventory_path,
        )

    missing_surface_list = [surface_name for surface_name in SURFACE_ORDER_LIST if surface_name not in surface_entry_dictionary]
    assert not missing_surface_list, (
        "Missing required exported model surfaces | "
        f"dataset={dataset_id} | input_mode={input_mode} | missing={missing_surface_list}"
    )
    return surface_entry_dictionary


def load_test_dataset(model_entry: ExportedModelEntry):

    """Build the source-run test dataset for one exported model."""

    training_config = load_yaml_dictionary(model_entry.training_config_path)
    datamodule = shared_training_infrastructure.create_datamodule_from_training_config(training_config)
    datamodule.setup(stage="fit")
    assert datamodule.test_dataset is not None, f"Test dataset is missing | {model_entry.training_config_path}"
    return datamodule.test_dataset


def compute_curve_metrics(target_curve_deg: np.ndarray, prediction_curve_deg: np.ndarray) -> dict[str, float]:

    """Compute TE curve metrics for one prediction."""

    target_curve = np.asarray(target_curve_deg, dtype=np.float64).reshape(-1)
    prediction_curve = np.asarray(prediction_curve_deg, dtype=np.float64).reshape(-1)
    residual_curve = prediction_curve - target_curve
    mse = float(np.mean(np.square(residual_curve)))
    mae = float(np.mean(np.abs(residual_curve)))
    rmse = float(np.sqrt(mse))
    denominator_value = float(np.ptp(target_curve))
    if denominator_value <= 1.0e-12:
        denominator_value = float(np.mean(np.abs(target_curve)))
    if denominator_value <= 1.0e-12:
        denominator_value = 1.0
    centered_target_curve = target_curve - float(np.mean(target_curve))
    centered_prediction_curve = prediction_curve - float(np.mean(prediction_curve))
    centered_residual_curve = centered_prediction_curve - centered_target_curve
    return {
        "mse": mse,
        "mae": mae,
        "rmse": rmse,
        "mean_percentage_error_pct": float(100.0 * mae / denominator_value),
        "signed_mean_offset_deg": float(np.mean(residual_curve)),
        "absolute_mean_offset_deg": float(abs(np.mean(residual_curve))),
        "peak_to_peak_error_deg": float(abs(np.ptp(prediction_curve) - np.ptp(target_curve))),
        "centered_mae_deg": float(np.mean(np.abs(centered_residual_curve))),
        "centered_rmse_deg": float(np.sqrt(np.mean(np.square(centered_residual_curve)))),
    }


def average_metric_dictionary(metric_dictionary_list: list[dict[str, float]]) -> dict[str, float]:

    """Average curve-level metrics for one model."""

    assert metric_dictionary_list, "Metric dictionary list is empty"
    averaged_dictionary = {
        metric_name: float(np.mean([metric_dictionary[metric_name] for metric_dictionary in metric_dictionary_list]))
        for metric_name in metric_dictionary_list[0]
    }
    averaged_dictionary["p95_mean_percentage_error_pct"] = float(
        np.percentile(
            [metric_dictionary["mean_percentage_error_pct"] for metric_dictionary in metric_dictionary_list],
            95.0,
        )
    )
    return averaged_dictionary


def load_onnx_session(model_entry: ExportedModelEntry, provider_list: list[str]) -> ort.InferenceSession:

    """Load one ONNX Runtime session."""

    return ort.InferenceSession(str(model_entry.onnx_model_path), providers=provider_list)


def resolve_static_onnx_dimension(dimension_value: Any) -> int | None:

    """Return an ONNX dimension when it is a concrete integer."""

    if isinstance(dimension_value, int):
        return int(dimension_value)
    return None


def build_temporal_sequence_window_view(padded_feature_matrix: np.ndarray, sequence_length: int) -> np.ndarray:

    """Build a vectorized temporal sequence-window view."""

    window_view = sliding_window_view(padded_feature_matrix, window_shape=sequence_length, axis=0)
    return np.transpose(window_view, axes=(0, 2, 1))


def predict_rank2_curve(session: ort.InferenceSession, input_feature_matrix: np.ndarray) -> np.ndarray:

    """Predict one pointwise TE curve with a rank-2 ONNX input."""

    input_metadata = session.get_inputs()[0]
    output_metadata = session.get_outputs()[0]
    feature_matrix = np.asarray(input_feature_matrix, dtype=np.float32)
    assert feature_matrix.ndim == 2, f"Expected rank-2 feature matrix | observed={feature_matrix.shape}"
    expected_feature_count = resolve_static_onnx_dimension(input_metadata.shape[1])
    if expected_feature_count is not None:
        assert feature_matrix.shape[1] == expected_feature_count, (
            "ONNX feature width mismatch | "
            f"expected={expected_feature_count} | observed={feature_matrix.shape[1]}"
        )
    prediction_array = session.run([output_metadata.name], {input_metadata.name: feature_matrix})[0]
    return np.asarray(prediction_array, dtype=np.float32).reshape(-1)


def predict_rank3_curve(
    session: ort.InferenceSession,
    input_feature_matrix: np.ndarray,
    training_config: dict[str, Any],
) -> np.ndarray:

    """Predict one full TE curve for a temporal rank-3 ONNX input."""

    input_metadata = session.get_inputs()[0]
    output_metadata = session.get_outputs()[0]
    feature_matrix = np.asarray(input_feature_matrix, dtype=np.float32)

    if feature_matrix.ndim == 3:
        input_tensor = np.ascontiguousarray(feature_matrix, dtype=np.float32)
        prediction_array = session.run([output_metadata.name], {input_metadata.name: input_tensor})[0]
        return np.asarray(prediction_array, dtype=np.float32).reshape(-1)

    assert feature_matrix.ndim == 2, f"Expected rank-2 point matrix for temporal windowing | observed={feature_matrix.shape}"
    dataset_configuration = training_config.get("dataset", {})
    configured_sequence_length = int(dataset_configuration.get("sequence_length", 0))
    expected_sequence_length = resolve_static_onnx_dimension(input_metadata.shape[1]) or configured_sequence_length
    expected_feature_count = resolve_static_onnx_dimension(input_metadata.shape[2])
    sequence_target_position = str(dataset_configuration.get("sequence_target_position", "center")).strip().lower()

    assert expected_sequence_length > 0, (
        "Temporal ONNX input requires a concrete sequence length from the model shape or training config"
    )
    assert sequence_target_position in {"center", "last"}, (
        f"Unsupported Sequence Target Position | {sequence_target_position}"
    )
    if sequence_target_position == "center":
        assert expected_sequence_length % 2 == 1, (
            "Center-readout full-curve evaluation requires an odd sequence length | "
            f"{expected_sequence_length}"
        )
        left_padding_count = expected_sequence_length // 2
        right_padding_count = expected_sequence_length // 2
    else:
        left_padding_count = expected_sequence_length - 1
        right_padding_count = 0

    if expected_feature_count is not None:
        assert feature_matrix.shape[1] == expected_feature_count, (
            "ONNX feature width mismatch | "
            f"expected={expected_feature_count} | observed={feature_matrix.shape[1]}"
        )

    padded_feature_matrix = np.pad(
        feature_matrix,
        pad_width=((left_padding_count, right_padding_count), (0, 0)),
        mode="edge",
    )
    sequence_window_view = build_temporal_sequence_window_view(
        padded_feature_matrix=padded_feature_matrix,
        sequence_length=expected_sequence_length,
    )
    prediction_array_list: list[np.ndarray] = []
    point_count = int(feature_matrix.shape[0])
    for batch_start_index in range(0, point_count, TEMPORAL_ONNX_INFERENCE_BATCH_SIZE):
        batch_end_index = min(batch_start_index + TEMPORAL_ONNX_INFERENCE_BATCH_SIZE, point_count)
        input_tensor = np.ascontiguousarray(sequence_window_view[batch_start_index:batch_end_index], dtype=np.float32)
        batch_prediction_array = session.run([output_metadata.name], {input_metadata.name: input_tensor})[0]
        prediction_array_list.append(np.asarray(batch_prediction_array, dtype=np.float32).reshape(-1))

    return np.concatenate(prediction_array_list, axis=0).astype(np.float32)


def predict_curve(
    session: ort.InferenceSession,
    input_feature_matrix: np.ndarray,
    training_config: dict[str, Any],
) -> np.ndarray:

    """Predict one TE curve with an ONNX Runtime session."""

    input_metadata = session.get_inputs()[0]
    expected_rank = len(input_metadata.shape)
    if expected_rank == 2:
        return predict_rank2_curve(session, input_feature_matrix)
    if expected_rank == 3:
        return predict_rank3_curve(session, input_feature_matrix, training_config)
    raise AssertionError(f"Unsupported ONNX input rank | shape={input_metadata.shape}")


def build_model_input_payload(
    curve_sample: dict[str, Any],
    session: ort.InferenceSession,
    training_config: dict[str, Any],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

    """Build input, target, and angular-position arrays for one model contract."""

    input_metadata = session.get_inputs()[0]
    expected_rank = len(input_metadata.shape)
    if expected_rank == 2:
        input_feature_matrix = curve_sample["input_tensor"].detach().cpu().numpy().astype(np.float32)
        target_curve_deg = curve_sample["target_tensor"].detach().cpu().numpy().reshape(-1).astype(np.float32)
        angular_position_deg = curve_sample["angular_position_deg"].detach().cpu().numpy().reshape(-1).astype(np.float32)
        return input_feature_matrix, target_curve_deg, angular_position_deg

    if expected_rank == 3:
        dataset_configuration = training_config.get("dataset", {})
        maximum_sequences_per_curve_value = dataset_configuration.get("maximum_sequences_per_curve")
        maximum_sequences_per_curve = (
            int(maximum_sequences_per_curve_value)
            if maximum_sequences_per_curve_value is not None
            else None
        )
        sequence_sample = transmission_error_datamodule.extract_sequence_tensor_from_curve_sample(
            curve_sample_dictionary=curve_sample,
            point_stride=int(dataset_configuration.get("point_stride", 1)),
            sequence_length=int(dataset_configuration.get("sequence_length", 17)),
            sequence_stride=int(dataset_configuration.get("sequence_stride", 1)),
            target_position=str(dataset_configuration.get("sequence_target_position", "center")),
            maximum_sequences_per_curve=maximum_sequences_per_curve,
        )
        input_tensor = sequence_sample["input_tensor"].detach().cpu().numpy().astype(np.float32)
        target_curve_deg = sequence_sample["target_tensor"].detach().cpu().numpy().reshape(-1).astype(np.float32)
        angular_position_deg = sequence_sample["angular_position_deg"].detach().cpu().numpy().reshape(-1).astype(np.float32)
        return input_tensor, target_curve_deg, angular_position_deg

    raise AssertionError(f"Unsupported ONNX input rank | shape={input_metadata.shape}")


def build_plot_payload(
    curve_sample: dict[str, Any],
    prediction_curve_deg: np.ndarray,
    prediction_angular_position_deg: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:

    """Build full measured and model-aligned prediction arrays for plotting."""

    measured_curve_deg = curve_sample["target_tensor"].detach().cpu().numpy().reshape(-1).astype(np.float32)
    measured_angular_position_deg = (
        curve_sample["angular_position_deg"].detach().cpu().numpy().reshape(-1).astype(np.float32)
    )
    prediction_curve = np.asarray(prediction_curve_deg, dtype=np.float32).reshape(-1)
    prediction_angular_position = np.asarray(prediction_angular_position_deg, dtype=np.float32).reshape(-1)
    return measured_angular_position_deg, measured_curve_deg, prediction_angular_position, prediction_curve


def surface_accepts_direction(surface_name: str, direction_label: str) -> bool:

    """Return whether one model surface should evaluate one direction."""

    normalized_surface = normalize_surface_name(surface_name)
    normalized_direction = str(direction_label).strip().lower()
    if normalized_surface == "global":
        return normalized_direction in {"forward", "backward"}
    return normalized_surface == normalized_direction


def evaluate_model_entry(
    group_id: str,
    model_entry: ExportedModelEntry,
    provider_list: list[str],
) -> tuple[list[CurveEvaluationEntry], dict[str, float], dict[str, Any]]:

    """Evaluate one exported ONNX model over its valid test curves."""

    session = load_onnx_session(model_entry, provider_list)
    training_config = load_yaml_dictionary(model_entry.training_config_path)
    test_dataset = load_test_dataset(model_entry)
    curve_entry_list: list[CurveEvaluationEntry] = []

    for dataset_index in tqdm(
        range(len(test_dataset)),
        desc=f"{group_id}:{model_entry.surface}",
        unit="curve",
        ascii=True,
        ncols=80,
        dynamic_ncols=False,
        leave=False,
    ):
        curve_sample = test_dataset[dataset_index]
        direction_label = str(curve_sample["direction_label"]).strip().lower()
        if not surface_accepts_direction(model_entry.surface, direction_label):
            continue
        input_feature_matrix, target_curve_deg, angular_position_deg = build_model_input_payload(
            curve_sample=curve_sample,
            session=session,
            training_config=training_config,
        )
        prediction_curve_deg = predict_curve(session, input_feature_matrix, training_config)
        assert prediction_curve_deg.shape == target_curve_deg.shape, (
            "Prediction and target curve shapes differ | "
            f"{prediction_curve_deg.shape} vs {target_curve_deg.shape}"
        )
        metric_dictionary = compute_curve_metrics(target_curve_deg, prediction_curve_deg)
        (
            plot_measured_angular_position_deg,
            plot_measured_curve_deg,
            plot_prediction_angular_position_deg,
            plot_prediction_curve_deg,
        ) = build_plot_payload(
            curve_sample=curve_sample,
            prediction_curve_deg=prediction_curve_deg,
            prediction_angular_position_deg=angular_position_deg,
        )
        curve_entry_list.append(
            CurveEvaluationEntry(
                group_id=group_id,
                surface=model_entry.surface,
                dataset_index=int(dataset_index),
                source_file_path=format_project_path(curve_sample["source_file_path"]),
                direction_label=direction_label,
                speed_rpm=float(curve_sample["speed_rpm"]),
                torque_nm=float(curve_sample["torque_nm"]),
                oil_temperature_deg=float(curve_sample["oil_temperature_deg"]),
                angular_position_deg=angular_position_deg,
                target_curve_deg=target_curve_deg,
                prediction_curve_deg=prediction_curve_deg,
                plot_measured_angular_position_deg=plot_measured_angular_position_deg,
                plot_measured_curve_deg=plot_measured_curve_deg,
                plot_prediction_angular_position_deg=plot_prediction_angular_position_deg,
                plot_prediction_curve_deg=plot_prediction_curve_deg,
                metrics=metric_dictionary,
            )
        )

    assert curve_entry_list, f"No valid curves evaluated | {group_id} | {model_entry.surface}"
    aggregate_metrics = average_metric_dictionary([curve_entry.metrics for curve_entry in curve_entry_list])
    onnx_metadata = {
        "input_list": [
            {"name": input_info.name, "shape": [str(value) for value in input_info.shape], "type": input_info.type}
            for input_info in session.get_inputs()
        ],
        "output_list": [
            {"name": output_info.name, "shape": [str(value) for value in output_info.shape], "type": output_info.type}
            for output_info in session.get_outputs()
        ],
        "provider_list": list(session.get_providers()),
    }
    return curve_entry_list, aggregate_metrics, onnx_metadata


def select_representative_curve_entries(
    curve_entry_list: list[CurveEvaluationEntry],
    curves_per_page: int,
) -> list[CurveEvaluationEntry]:

    """Select deterministic representative curves for one collage page."""

    assert curves_per_page > 0, f"Curves per page must be positive | {curves_per_page}"
    sorted_entry_list = sorted(
        curve_entry_list,
        key=lambda entry: (
            entry.direction_label,
            entry.speed_rpm,
            entry.torque_nm,
            entry.oil_temperature_deg,
            entry.dataset_index,
        ),
    )
    if len(sorted_entry_list) <= curves_per_page:
        return sorted_entry_list
    selected_index_array = np.linspace(0, len(sorted_entry_list) - 1, curves_per_page, dtype=int)
    selected_index_list = sorted({int(index_value) for index_value in selected_index_array})
    cursor_index = 0
    while len(selected_index_list) < curves_per_page:
        if cursor_index not in selected_index_list:
            selected_index_list.append(cursor_index)
        cursor_index += 1
    return [sorted_entry_list[index_value] for index_value in sorted(selected_index_list[:curves_per_page])]


def save_surface_collage(
    collage_path: Path,
    title_text: str,
    selected_curve_entry_list: list[CurveEvaluationEntry],
) -> None:

    """Save one measured-versus-predicted curve collage."""

    collage_path.parent.mkdir(parents=True, exist_ok=True)
    column_count = 2
    row_count = int(np.ceil(len(selected_curve_entry_list) / column_count))
    figure, axis_array = plt.subplots(row_count, column_count, figsize=(12.5, max(9.0, 3.0 * row_count)))
    flat_axis_list = np.asarray(axis_array).reshape(-1)

    for axis_index, axis in enumerate(flat_axis_list):
        if axis_index >= len(selected_curve_entry_list):
            axis.axis("off")
            continue
        curve_entry = selected_curve_entry_list[axis_index]
        track2_circular_plotting.plot_circular_angle_curve(
            axis,
            curve_entry.plot_measured_angular_position_deg,
            curve_entry.plot_measured_curve_deg,
            label="Measured TE",
            color="#343434",
            linewidth=1.25,
        )
        track2_circular_plotting.plot_circular_angle_curve(
            axis,
            curve_entry.plot_prediction_angular_position_deg,
            curve_entry.plot_prediction_curve_deg,
            label="ONNX prediction",
            color="#0072b2",
            linewidth=1.15,
            alpha=0.92,
        )
        axis.set_title(
            (
                f"{curve_entry.direction_label} | {curve_entry.speed_rpm:.0f} rpm | "
                f"{curve_entry.torque_nm:.0f} Nm | {curve_entry.oil_temperature_deg:.0f} C | "
                f"MAE {curve_entry.metrics['mae']:.5f}"
            ),
            fontsize=9,
        )
        axis.set_xlabel("Angle [deg]", fontsize=8)
        axis.set_ylabel("TE [deg]", fontsize=8)
        axis.tick_params(axis="both", labelsize=8)
        axis.grid(True, alpha=0.25)
        axis.legend(loc="best", fontsize=7)

    figure.suptitle(title_text, fontsize=13)
    figure.tight_layout(rect=(0.0, 0.0, 1.0, 0.975))
    figure.savefig(collage_path, dpi=160)
    plt.close(figure)


def save_model_inventory_csv(csv_path: Path, model_entry_list: list[ExportedModelEntry]) -> None:

    """Save the model inventory used by the report."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file, lineterminator="\n")
        writer.writerow(
            [
                "dataset_id",
                "input_mode",
                "surface",
                "run_name",
                "run_instance_id",
                "dataset_schema",
                "model_type",
                "onnx_model_path",
                "python_model_path",
                "training_config_path",
            ]
        )
        for model_entry in model_entry_list:
            writer.writerow(
                [
                    model_entry.dataset_id,
                    model_entry.input_mode,
                    model_entry.surface,
                    model_entry.run_name,
                    model_entry.run_instance_id,
                    model_entry.dataset_schema,
                    model_entry.model_type,
                    format_project_path(model_entry.onnx_model_path),
                    format_project_path(model_entry.python_model_path),
                    format_project_path(model_entry.training_config_path),
                ]
            )


def save_per_curve_metrics_csv(csv_path: Path, curve_summary_list: list[dict[str, Any]]) -> None:

    """Save one per-curve metric table."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    metric_name_list = [
        "mse",
        "mae",
        "rmse",
        "mean_percentage_error_pct",
        "signed_mean_offset_deg",
        "absolute_mean_offset_deg",
        "peak_to_peak_error_deg",
        "centered_mae_deg",
        "centered_rmse_deg",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file, lineterminator="\n")
        writer.writerow(
            [
                "group_id",
                "dataset_id",
                "input_mode",
                "surface",
                "run_name",
                "run_instance_id",
                "dataset_index",
                "direction_label",
                "speed_rpm",
                "torque_nm",
                "oil_temperature_deg",
                "source_file_path",
                *metric_name_list,
            ]
        )
        for curve_summary in curve_summary_list:
            metric_dictionary = curve_summary["metrics"]
            writer.writerow(
                [
                    curve_summary["group_id"],
                    curve_summary["dataset_id"],
                    curve_summary["input_mode"],
                    curve_summary["surface"],
                    curve_summary["run_name"],
                    curve_summary["run_instance_id"],
                    curve_summary["dataset_index"],
                    curve_summary["direction_label"],
                    f"{curve_summary['speed_rpm']:.9f}",
                    f"{curve_summary['torque_nm']:.9f}",
                    f"{curve_summary['oil_temperature_deg']:.9f}",
                    curve_summary["source_file_path"],
                    *[f"{metric_dictionary[metric_name]:.12f}" for metric_name in metric_name_list],
                ]
            )


def build_relative_markdown_path(target_path: Path, markdown_directory: Path) -> str:

    """Build a Markdown-safe relative path."""

    return Path(target_path).resolve().relative_to(markdown_directory.resolve()).as_posix()


def append_model_inventory_table(report_line_list: list[str], model_summary_list: list[dict[str, Any]]) -> None:

    """Append a compact model inventory table to the report."""

    report_line_list.extend(
        [
            "| Surface | Run Name | Run Instance | Dataset Schema |",
            "| --- | --- | --- | --- |",
        ]
    )
    for model_summary in model_summary_list:
        report_line_list.append(
            f"| {model_summary['surface']} | `{model_summary['run_name']}` | "
            f"`{model_summary['run_instance_id']}` | `{model_summary['dataset_schema']}` |"
        )

    report_line_list.extend(
        [
            "",
            "Exact model paths:",
            "",
            "| Surface | ONNX Model Path | Python Model Path |",
            "| --- | --- | --- |",
        ]
    )
    for model_summary in model_summary_list:
        report_line_list.append(
            f"| {model_summary['surface']} | `{model_summary['onnx_model_path']}` | "
            f"`{model_summary['python_model_path']}` |"
        )
    report_line_list.append("")


def append_metric_table(report_line_list: list[str], model_summary_list: list[dict[str, Any]]) -> None:

    """Append the aggregate metrics table."""

    report_line_list.extend(
        [
            "| Surface | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for model_summary in model_summary_list:
        metric_dictionary = model_summary["aggregate_metrics"]
        report_line_list.append(
            f"| {model_summary['surface']} | {model_summary['evaluated_curve_count']} | "
            f"{metric_dictionary['mae']:.6f} | {metric_dictionary['rmse']:.6f} | "
            f"{metric_dictionary['mean_percentage_error_pct']:.3f} | "
            f"{metric_dictionary['p95_mean_percentage_error_pct']:.3f} |"
        )
    report_line_list.extend(["", "Offset And Shape Metrics:", ""])
    report_line_list.extend(
        [
            "| Surface | Signed Offset [deg] | Absolute Offset [deg] | Centered MAE [deg] | P2P Error [deg] |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for model_summary in model_summary_list:
        metric_dictionary = model_summary["aggregate_metrics"]
        report_line_list.append(
            f"| {model_summary['surface']} | "
            f"{metric_dictionary['signed_mean_offset_deg']:.6f} | "
            f"{metric_dictionary['absolute_mean_offset_deg']:.6f} | "
            f"{metric_dictionary['centered_mae_deg']:.6f} | "
            f"{metric_dictionary['peak_to_peak_error_deg']:.6f} |"
        )
    report_line_list.append("")


def build_report_markdown(
    report_path: Path,
    model_family: str,
    group_summary_list: list[dict[str, Any]],
    summary_path: Path,
    model_inventory_csv_path: Path,
    per_curve_metrics_csv_path: Path,
    output_directory: Path,
    curves_per_page: int,
) -> str:

    """Build the Markdown report body."""

    report_line_list = [
        f"# TE Curve Verification Pipeline Familywise ONNX Report - {model_family}",
        "",
        "## Overview",
        "",
        "This report evaluates exported ONNX models from the dataset input-mode",
        "retraining program. Each dataset/input-mode section uses dataset-matched",
        "held-out test curves and lists the exact model artifacts loaded from",
        "`models/`.",
        "",
        "Rank-3 temporal ONNX exports are evaluated on the sequence-window test",
        "contract stored in each `training_config.snapshot.yaml`, including",
        "`sequence_length`, `sequence_stride`, `sequence_target_position`, and",
        "`maximum_sequences_per_curve`.",
        "The collage pages keep the measured TE trace at the original full-curve",
        "resolution; temporal ONNX predictions are overlaid at the evaluated",
        "sequence-target angles.",
        "",
        "The report is diagnostic and family-specific. It does not replace an",
        "official multi-index model-promotion decision.",
        "",
        "## Output Artifacts",
        "",
        f"- output directory: `{format_project_path(output_directory)}`;",
        f"- summary YAML: `{format_project_path(summary_path)}`;",
        f"- model inventory CSV: `{format_project_path(model_inventory_csv_path)}`;",
        f"- per-curve metrics CSV: `{format_project_path(per_curve_metrics_csv_path)}`.",
        "",
    ]

    for group_summary in group_summary_list:
        report_line_list.extend(
            [
                f"## {group_summary['group_title']}",
                "",
                f"- dataset: `{group_summary['dataset_id']}`;",
                f"- input mode: `{group_summary['input_mode']}`;",
                f"- evaluated family: `{model_family}`;",
                f"- dataset root: `{group_summary['dataset_root']}`.",
                "",
                "### Models Used",
                "",
            ]
        )
        append_model_inventory_table(report_line_list, group_summary["model_summary_list"])
        report_line_list.extend(["### Aggregate Metrics", ""])
        append_metric_table(report_line_list, group_summary["model_summary_list"])

        for model_summary in group_summary["model_summary_list"]:
            report_line_list.extend(
                [
                    f"### {model_summary['surface'].title()} {curves_per_page}-Curve Page",
                    "",
                    (
                        f"![{group_summary['group_id']} {model_summary['surface']} {curves_per_page}-curve collage]"
                        f"({model_summary['collage_markdown_path']})"
                    ),
                    "",
                ]
            )

    while report_line_list and not report_line_list[-1]:
        report_line_list.pop()
    return "\n".join(report_line_list) + "\n"


def run_familywise_onnx_report(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run familywise ONNX evaluation and report generation."""

    repository_path_support.set_runtime_platform(repository_path_support.resolve_argument_platform(arguments))
    model_family = str(arguments.model_family).strip()
    assert model_family, "Model family cannot be empty"
    curves_per_page = int(arguments.curves_per_page)
    assert curves_per_page > 0, f"Curves per page must be positive | {curves_per_page}"
    provider_list = list(arguments.onnx_provider or ["CPUExecutionProvider"])
    group_specification_list = list(arguments.group_specification_list or DEFAULT_GROUP_SPECIFICATION_LIST)
    group_pair_list = [parse_group_specification(group_specification) for group_specification in group_specification_list]

    current_timestamp = datetime.now().astimezone()
    report_date = arguments.report_date or current_timestamp.strftime("%Y-%m-%d")
    datetime.strptime(report_date, "%Y-%m-%d")
    run_instance_id = f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}__track2_{model_family}_familywise_onnx_report"
    output_directory = resolve_project_path(arguments.output_root) / model_family / run_instance_id
    report_directory = resolve_project_path(arguments.report_root) / model_family / f"[{report_date}]"
    report_asset_root = report_directory / "assets"
    if report_asset_root.exists():
        shutil.rmtree(report_asset_root)
    output_directory.mkdir(parents=True, exist_ok=True)
    report_asset_root.mkdir(parents=True, exist_ok=True)

    all_model_entry_list: list[ExportedModelEntry] = []
    all_curve_summary_list: list[dict[str, Any]] = []
    group_summary_list: list[dict[str, Any]] = []

    for dataset_id, input_mode in tqdm(group_pair_list, desc="Dataset/input groups", unit="group", ascii=True, ncols=80):
        group_id = f"{dataset_id}__{input_mode}"
        model_entry_dictionary = load_group_model_entries(dataset_id, input_mode, model_family)
        all_model_entry_list.extend([model_entry_dictionary[surface_name] for surface_name in SURFACE_ORDER_LIST])
        group_title = GROUP_TITLE_DICTIONARY.get((dataset_id, input_mode), f"{dataset_id} + {input_mode}")
        model_summary_list: list[dict[str, Any]] = []
        dataset_root_text = ""

        for surface_name in SURFACE_ORDER_LIST:
            model_entry = model_entry_dictionary[surface_name]
            curve_entry_list, aggregate_metrics, onnx_metadata = evaluate_model_entry(group_id, model_entry, provider_list)
            selected_curve_entry_list = select_representative_curve_entries(curve_entry_list, curves_per_page)
            collage_filename = f"{surface_name}_{curves_per_page}_curve_collage.png"
            collage_path = output_directory / "collages" / group_id / collage_filename
            report_collage_path = report_asset_root / group_id / collage_filename
            save_surface_collage(
                collage_path,
                f"{group_title} | {model_family} | {surface_name}",
                selected_curve_entry_list,
            )
            report_collage_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(collage_path, report_collage_path)

            training_config = load_yaml_dictionary(model_entry.training_config_path)
            dataset_root_text = format_project_path(training_config["metadata"].get("source_dataset_root", ""))
            model_summary = {
                "dataset_id": model_entry.dataset_id,
                "input_mode": model_entry.input_mode,
                "surface": model_entry.surface,
                "run_name": model_entry.run_name,
                "run_instance_id": model_entry.run_instance_id,
                "dataset_schema": model_entry.dataset_schema,
                "model_type": model_entry.model_type,
                "onnx_model_path": format_project_path(model_entry.onnx_model_path),
                "python_model_path": format_project_path(model_entry.python_model_path),
                "training_config_path": format_project_path(model_entry.training_config_path),
                "source_inventory_path": format_project_path(model_entry.source_inventory_path),
                "evaluated_curve_count": int(len(curve_entry_list)),
                "aggregate_metrics": aggregate_metrics,
                "onnx_metadata": onnx_metadata,
                "collage_path": format_project_path(collage_path),
                "collage_markdown_path": build_relative_markdown_path(report_collage_path, report_directory),
                "selected_curve_list": [
                    {
                        "dataset_index": int(curve_entry.dataset_index),
                        "source_file_path": curve_entry.source_file_path,
                        "direction_label": curve_entry.direction_label,
                        "speed_rpm": float(curve_entry.speed_rpm),
                        "torque_nm": float(curve_entry.torque_nm),
                        "oil_temperature_deg": float(curve_entry.oil_temperature_deg),
                        "metrics": curve_entry.metrics,
                    }
                    for curve_entry in selected_curve_entry_list
                ],
            }
            model_summary_list.append(model_summary)

            for curve_entry in curve_entry_list:
                all_curve_summary_list.append(
                    {
                        "group_id": group_id,
                        "dataset_id": model_entry.dataset_id,
                        "input_mode": model_entry.input_mode,
                        "surface": model_entry.surface,
                        "run_name": model_entry.run_name,
                        "run_instance_id": model_entry.run_instance_id,
                        "dataset_index": int(curve_entry.dataset_index),
                        "source_file_path": curve_entry.source_file_path,
                        "direction_label": curve_entry.direction_label,
                        "speed_rpm": float(curve_entry.speed_rpm),
                        "torque_nm": float(curve_entry.torque_nm),
                        "oil_temperature_deg": float(curve_entry.oil_temperature_deg),
                        "metrics": curve_entry.metrics,
                    }
                )

        group_summary_list.append(
            {
                "group_id": group_id,
                "group_title": group_title,
                "dataset_id": dataset_id,
                "input_mode": input_mode,
                "dataset_root": dataset_root_text,
                "model_summary_list": model_summary_list,
            }
        )

    summary_path = output_directory / SUMMARY_FILENAME
    model_inventory_csv_path = output_directory / MODEL_INVENTORY_FILENAME
    per_curve_metrics_csv_path = output_directory / PER_CURVE_METRICS_FILENAME
    report_path = report_directory / REPORT_FILENAME_TEMPLATE.format(model_family=model_family)

    save_model_inventory_csv(model_inventory_csv_path, all_model_entry_list)
    save_per_curve_metrics_csv(per_curve_metrics_csv_path, all_curve_summary_list)
    summary_dictionary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "model_family": model_family,
        "report_path": format_project_path(report_path),
        "output_directory": format_project_path(output_directory),
        "summary_path": format_project_path(summary_path),
        "model_inventory_csv_path": format_project_path(model_inventory_csv_path),
        "per_curve_metrics_csv_path": format_project_path(per_curve_metrics_csv_path),
        "curves_per_page": curves_per_page,
        "provider_list": provider_list,
        "group_summary_list": group_summary_list,
    }
    save_yaml_dictionary(summary_path, summary_dictionary)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        build_report_markdown(
            report_path,
            model_family,
            group_summary_list,
            summary_path,
            model_inventory_csv_path,
            per_curve_metrics_csv_path,
            output_directory,
            curves_per_page,
        ),
        encoding="utf-8",
    )
    print(f"[DONE] Familywise ONNX report: {format_project_path(report_path)}")
    print(f"[DONE] Artifacts: {format_project_path(output_directory)}")
    return summary_dictionary


def main() -> None:

    """Run the command-line entry point."""

    run_familywise_onnx_report(parse_command_line_arguments())


if __name__ == "__main__":
    main()
