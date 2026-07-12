"""Portable Track 2 ONNX curve plotter.

The script supports two inference families:

* ``rcim``: harmonic amplitude/phase ONNX banks under
  ``models/<dataset>/rcim_track1/<surface>/<family>/``.
* ``direct_te``: TE-prediction ONNX models under
  ``models/<dataset>/<input_mode>/<family>/<surface>.onnx``.

It is intentionally self-contained and does not import the research repo.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import onnxruntime as ort


# =============================================================================
# USER CONFIGURATION
# =============================================================================

BASE_DIRECTORY_PATH = Path.cwd()

# Main selectors. Command-line flags override these values.
DATASET_NAME = "simplified_dataset"  # simplified_dataset | polished_dataset
INPUT_MODE = "setpoints"  # setpoints | actual_values
MODEL_KIND = "rcim"  # rcim | direct_te
SURFACE = "forward"  # forward | backward | global
MODEL_FAMILY = "SVR"  # RCIM family or direct-TE family folder

# RCIM reconstruction options.
SELECTED_HARMONIC_ORDER_LIST: list[int] | None = None

# Direct TE sequence-model options. The exported sequence models were trained
# with finite rolling windows; 33 is the current Track 2 retraining default.
DIRECT_SEQUENCE_LENGTH = 33
DIRECT_SEQUENCE_TARGET_POSITION = "center"  # center | last
DIRECT_BATCH_SIZE = 4096

# Provide CSV files explicitly, or leave empty and use CURVE_CSV_DIRECTORY_PATH.
CURVE_CSV_PATH_LIST = [
    "data/simplified_dataset/Test_25degree/1000rpm/1000.0rpm0.0Nm25.0deg.csv",
    "data/simplified_dataset/Test_30degree/700rpm/700.0rpm1400.0Nm30.0deg.csv",
    "data/simplified_dataset/Test_35degree/800rpm/800.0rpm1800.0Nm35.0deg.csv",
]

CURVE_CSV_DIRECTORY_PATH = ""
CURVE_CSV_GLOB_PATTERN = "*.csv"
PROCESS_CURVE_DIRECTORY_RECURSIVELY = True
MAXIMUM_CURVES_TO_PROCESS: int | None = None

OUTPUT_DIRECTORY_PATH = "output"
SAVE_PLOTS = True
SHOW_PLOTS = False
SAVE_PREDICTED_CURVE_CSV = True

DEFAULT_SPEED_RPM: float | None = None
DEFAULT_TORQUE_NM: float | None = None
DEFAULT_OIL_TEMPERATURE_DEG: float | None = None


# =============================================================================
# IMPLEMENTATION
# =============================================================================

FILENAME_OPERATING_POINT_PATTERN = re.compile(
    r"(?P<speed_rpm>[0-9.]+)rpm(?P<torque_nm>[0-9.]+)Nm(?P<temperature_deg>[0-9.]+)deg\.csv$",
    re.IGNORECASE,
)

RCIM_MODEL_PATTERN = re.compile(r"(?P<target>ampl|phase)(?P<harmonic>[0-9]+)\.onnx$", re.IGNORECASE)

FORWARD_DIRECTION = "forward"
BACKWARD_DIRECTION = "backward"
GLOBAL_SURFACE = "global"

DIRECTION_FLAG = {
    FORWARD_DIRECTION: 1.0,
    BACKWARD_DIRECTION: -1.0,
}

SIMPLIFIED_FORWARD_POSITION_COLUMNS = ["Poisition_Output_Reducer_Fw", "Position_Output_Reducer_Fw"]
SIMPLIFIED_FORWARD_TE_COLUMNS = ["Transmission_Error_Fw"]
SIMPLIFIED_BACKWARD_POSITION_COLUMNS = ["Position_Output_Reducer_Bw"]
SIMPLIFIED_BACKWARD_TE_COLUMNS = ["Transmission_Error_Bw"]


@dataclass(frozen=True)
class CurveRecord:
    source_csv_path: Path
    dataset_name: str
    input_mode: str
    direction_label: str
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    angular_position_deg: np.ndarray
    measured_transmission_error_deg: np.ndarray
    direct_input_feature_matrix: np.ndarray


@dataclass(frozen=True)
class RcimTargetConfiguration:
    target_kind: str
    harmonic_order: int
    family_name: str
    model_path: Path


@dataclass(frozen=True)
class LoadedOnnxTarget:
    configuration: RcimTargetConfiguration
    session: ort.InferenceSession
    input_name: str


@dataclass(frozen=True)
class DirectTeModel:
    family_name: str
    model_path: Path
    session: ort.InferenceSession
    input_name: str
    input_rank: int


def normalize_selector(value: str) -> str:
    return str(value).strip().lower()


def resolve_configured_path(path_value: str | Path) -> Path:
    candidate_path = Path(path_value).expanduser()
    if candidate_path.is_absolute():
        return candidate_path.resolve()
    return (BASE_DIRECTORY_PATH / candidate_path).resolve()


def parse_operating_point_from_filename(csv_path: Path) -> dict[str, float] | None:
    filename_match = FILENAME_OPERATING_POINT_PATTERN.search(csv_path.name)
    if filename_match is None:
        return None
    return {
        "speed_rpm": float(filename_match.group("speed_rpm")),
        "torque_nm": float(filename_match.group("torque_nm")),
        "oil_temperature_deg": float(filename_match.group("temperature_deg")),
    }


def resolve_operating_point(csv_path: Path) -> dict[str, float]:
    filename_metadata = parse_operating_point_from_filename(csv_path) or {}
    speed_rpm = filename_metadata.get("speed_rpm")
    torque_nm = filename_metadata.get("torque_nm")
    oil_temperature_deg = filename_metadata.get("oil_temperature_deg")
    if speed_rpm is None:
        speed_rpm = DEFAULT_SPEED_RPM
    if torque_nm is None:
        torque_nm = DEFAULT_TORQUE_NM
    if oil_temperature_deg is None:
        oil_temperature_deg = DEFAULT_OIL_TEMPERATURE_DEG
    missing_role_list = []
    if speed_rpm is None:
        missing_role_list.append("speed_rpm")
    if torque_nm is None:
        missing_role_list.append("torque_nm")
    if oil_temperature_deg is None:
        missing_role_list.append("oil_temperature_deg")
    if missing_role_list:
        raise ValueError(
            f"Missing operating-point metadata {missing_role_list} for {csv_path}. "
            "Use an original-style filename or set DEFAULT_* values."
        )
    return {
        "speed_rpm": float(speed_rpm),
        "torque_nm": float(torque_nm),
        "oil_temperature_deg": float(oil_temperature_deg),
    }


def read_csv_as_columns(csv_path: Path) -> dict[str, np.ndarray]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None:
            raise ValueError(f"CSV has no header | {csv_path}")
        column_values: dict[str, list[float]] = {field_name: [] for field_name in reader.fieldnames}
        for row in reader:
            for field_name in reader.fieldnames:
                raw_value = row.get(field_name, "")
                try:
                    value = float(raw_value)
                except (TypeError, ValueError):
                    value = math.nan
                column_values[field_name].append(value)
    return {
        field_name: np.asarray(value_list, dtype=np.float64)
        for field_name, value_list in column_values.items()
    }


def find_first_existing_column(column_dictionary: dict[str, np.ndarray], candidate_list: list[str], role_label: str) -> str:
    for candidate_column in candidate_list:
        if candidate_column in column_dictionary:
            return candidate_column
    raise ValueError(
        f"Missing {role_label} column. Expected one of {candidate_list}; "
        f"available columns are {list(column_dictionary)}"
    )


def infer_polished_direction_from_path(csv_path: Path) -> str:
    lower_parts = [path_part.lower() for path_part in csv_path.parts]
    if FORWARD_DIRECTION in lower_parts:
        return FORWARD_DIRECTION
    if BACKWARD_DIRECTION in lower_parts:
        return BACKWARD_DIRECTION
    raise ValueError(f"Cannot infer polished direction from path | {csv_path}")


def sort_and_filter_curve(
    angular_position_deg: np.ndarray,
    measured_te_deg: np.ndarray,
    feature_matrix: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    finite_mask = np.isfinite(angular_position_deg) & np.isfinite(measured_te_deg) & np.all(np.isfinite(feature_matrix), axis=1)
    angular_position_deg = angular_position_deg[finite_mask]
    measured_te_deg = measured_te_deg[finite_mask]
    feature_matrix = feature_matrix[finite_mask]

    rotation_mask = (angular_position_deg >= 0.0) & (angular_position_deg <= 360.0)
    angular_position_deg = angular_position_deg[rotation_mask]
    measured_te_deg = measured_te_deg[rotation_mask]
    feature_matrix = feature_matrix[rotation_mask]

    sorting_index_array = np.argsort(angular_position_deg)
    angular_position_deg = angular_position_deg[sorting_index_array]
    measured_te_deg = measured_te_deg[sorting_index_array]
    feature_matrix = feature_matrix[sorting_index_array]
    if angular_position_deg.size == 0:
        raise ValueError("Empty curve after filtering.")
    return (
        angular_position_deg.astype(np.float32),
        measured_te_deg.astype(np.float32),
        feature_matrix.astype(np.float32),
    )


def build_setpoint_feature_matrix(
    angular_position_deg: np.ndarray,
    speed_rpm: float,
    torque_nm: float,
    oil_temperature_deg: float,
    direction_flag: float,
) -> np.ndarray:
    point_count = angular_position_deg.shape[0]
    return np.column_stack(
        [
            angular_position_deg.astype(np.float64),
            np.full(point_count, float(speed_rpm), dtype=np.float64),
            np.full(point_count, float(torque_nm), dtype=np.float64),
            np.full(point_count, float(oil_temperature_deg), dtype=np.float64),
            np.full(point_count, float(direction_flag), dtype=np.float64),
        ]
    )


def load_polished_curve_record(csv_path: Path, dataset_name: str, input_mode: str) -> CurveRecord:
    direction_label = infer_polished_direction_from_path(csv_path)
    direction_flag = DIRECTION_FLAG[direction_label]
    columns = read_csv_as_columns(csv_path)
    for required_column in ["theta", "theta_dot", "tau_load", "T", "theta_TE"]:
        if required_column not in columns:
            raise ValueError(f"Missing polished column {required_column!r} | {csv_path}")

    angular_position_deg = columns["theta"]
    measured_te_deg = columns["theta_TE"]
    operating_point = resolve_operating_point(csv_path)

    if input_mode == "actual_values":
        feature_matrix = np.column_stack(
            [
                columns["theta"],
                columns["theta_dot"],
                columns["tau_load"],
                columns["T"],
                np.full(columns["theta"].shape[0], direction_flag, dtype=np.float64),
            ]
        )
        speed_rpm = float(np.nanmedian(columns["theta_dot"]))
        torque_nm = float(np.nanmedian(columns["tau_load"]))
        oil_temperature_deg = float(np.nanmedian(columns["T"]))
    else:
        feature_matrix = build_setpoint_feature_matrix(
            angular_position_deg,
            operating_point["speed_rpm"],
            operating_point["torque_nm"],
            operating_point["oil_temperature_deg"],
            direction_flag,
        )
        speed_rpm = operating_point["speed_rpm"]
        torque_nm = operating_point["torque_nm"]
        oil_temperature_deg = operating_point["oil_temperature_deg"]

    angular_position_deg, measured_te_deg, feature_matrix = sort_and_filter_curve(
        angular_position_deg,
        measured_te_deg,
        feature_matrix,
    )
    return CurveRecord(
        source_csv_path=csv_path,
        dataset_name=dataset_name,
        input_mode=input_mode,
        direction_label=direction_label,
        speed_rpm=speed_rpm,
        torque_nm=torque_nm,
        oil_temperature_deg=oil_temperature_deg,
        angular_position_deg=angular_position_deg,
        measured_transmission_error_deg=measured_te_deg,
        direct_input_feature_matrix=feature_matrix,
    )


def build_simplified_curve_record(csv_path: Path, dataset_name: str, direction_label: str) -> CurveRecord:
    columns = read_csv_as_columns(csv_path)
    operating_point = resolve_operating_point(csv_path)
    if direction_label == FORWARD_DIRECTION:
        angular_column = find_first_existing_column(columns, SIMPLIFIED_FORWARD_POSITION_COLUMNS, "forward angular position")
        te_column = find_first_existing_column(columns, SIMPLIFIED_FORWARD_TE_COLUMNS, "forward transmission error")
    elif direction_label == BACKWARD_DIRECTION:
        angular_column = find_first_existing_column(columns, SIMPLIFIED_BACKWARD_POSITION_COLUMNS, "backward angular position")
        te_column = find_first_existing_column(columns, SIMPLIFIED_BACKWARD_TE_COLUMNS, "backward transmission error")
    else:
        raise ValueError(f"simplified_dataset does not have a single {direction_label!r} curve in one CSV.")

    direction_flag = DIRECTION_FLAG[direction_label]
    angular_position_deg = columns[angular_column]
    measured_te_deg = columns[te_column]
    feature_matrix = build_setpoint_feature_matrix(
        angular_position_deg,
        operating_point["speed_rpm"],
        operating_point["torque_nm"],
        operating_point["oil_temperature_deg"],
        direction_flag,
    )
    angular_position_deg, measured_te_deg, feature_matrix = sort_and_filter_curve(
        angular_position_deg,
        measured_te_deg,
        feature_matrix,
    )
    return CurveRecord(
        source_csv_path=csv_path,
        dataset_name=dataset_name,
        input_mode="setpoints",
        direction_label=direction_label,
        speed_rpm=operating_point["speed_rpm"],
        torque_nm=operating_point["torque_nm"],
        oil_temperature_deg=operating_point["oil_temperature_deg"],
        angular_position_deg=angular_position_deg,
        measured_transmission_error_deg=measured_te_deg,
        direct_input_feature_matrix=feature_matrix,
    )


def load_curve_record_list(csv_path: Path, dataset_name: str, input_mode: str, surface: str) -> list[CurveRecord]:
    if dataset_name == "polished_dataset":
        record = load_polished_curve_record(csv_path, dataset_name, input_mode)
        if surface in {FORWARD_DIRECTION, BACKWARD_DIRECTION} and record.direction_label != surface:
            return []
        return [record]

    if input_mode != "setpoints":
        raise ValueError("simplified_dataset only supports setpoints input mode.")
    if surface == GLOBAL_SURFACE:
        return [
            build_simplified_curve_record(csv_path, dataset_name, FORWARD_DIRECTION),
            build_simplified_curve_record(csv_path, dataset_name, BACKWARD_DIRECTION),
        ]
    return [build_simplified_curve_record(csv_path, dataset_name, surface)]


def collect_curve_csv_path_list(arguments: argparse.Namespace) -> list[Path]:
    path_text_list = arguments.curve_csv or CURVE_CSV_PATH_LIST
    collected_path_list = [
        resolve_configured_path(csv_path)
        for csv_path in path_text_list
        if str(csv_path).strip()
    ]
    directory_text = arguments.curve_dir or CURVE_CSV_DIRECTORY_PATH
    if str(directory_text).strip():
        directory_path = resolve_configured_path(directory_text)
        if not directory_path.exists():
            raise FileNotFoundError(f"Configured curve CSV directory does not exist | {directory_path}")
        if PROCESS_CURVE_DIRECTORY_RECURSIVELY:
            collected_path_list.extend(sorted(directory_path.rglob(CURVE_CSV_GLOB_PATTERN)))
        else:
            collected_path_list.extend(sorted(directory_path.glob(CURVE_CSV_GLOB_PATTERN)))

    unique_path_list = sorted(set(path.resolve() for path in collected_path_list))
    maximum_curves = arguments.max_curves if arguments.max_curves is not None else MAXIMUM_CURVES_TO_PROCESS
    if maximum_curves is not None:
        unique_path_list = unique_path_list[: int(maximum_curves)]
    if not unique_path_list:
        raise ValueError("No input curve CSV files configured.")
    for csv_path in unique_path_list:
        if not csv_path.exists():
            raise FileNotFoundError(f"Configured curve CSV file does not exist | {csv_path}")
    return unique_path_list


def resolve_rcim_model_root(dataset_name: str, surface: str, family_name: str) -> Path:
    model_root = resolve_configured_path(Path("models") / dataset_name / "rcim_track1" / surface / family_name)
    if model_root.exists():
        return model_root
    alias_dictionary = {
        "SVR": "SVM",
        "SVM": "SVR",
    }
    alias_family_name = alias_dictionary.get(family_name.upper())
    if alias_family_name:
        alias_model_root = resolve_configured_path(Path("models") / dataset_name / "rcim_track1" / surface / alias_family_name)
        if alias_model_root.exists():
            return alias_model_root
    raise FileNotFoundError(f"RCIM model family directory does not exist | {model_root}")
    return model_root


def discover_rcim_target_configuration_list(dataset_name: str, surface: str, family_name: str) -> list[RcimTargetConfiguration]:
    model_root = resolve_rcim_model_root(dataset_name, surface, family_name)
    configuration_list: list[RcimTargetConfiguration] = []
    for model_path in sorted(model_root.glob("*.onnx")):
        match = RCIM_MODEL_PATTERN.search(model_path.name)
        if match is None:
            continue
        target_kind = "amplitude" if match.group("target").lower() == "ampl" else "phase"
        configuration_list.append(
            RcimTargetConfiguration(
                target_kind=target_kind,
                harmonic_order=int(match.group("harmonic")),
                family_name=family_name,
                model_path=model_path.resolve(),
            )
        )
    if not configuration_list:
        raise ValueError(f"No RCIM amplitude/phase ONNX files found | {model_root}")
    return configuration_list


def resolve_selected_harmonic_order_list(configuration_list: list[RcimTargetConfiguration]) -> list[int]:
    available_amplitude_set = {
        target_configuration.harmonic_order
        for target_configuration in configuration_list
        if target_configuration.target_kind == "amplitude"
    }
    available_phase_set = {
        target_configuration.harmonic_order
        for target_configuration in configuration_list
        if target_configuration.target_kind == "phase"
    }
    if SELECTED_HARMONIC_ORDER_LIST is None:
        selected_harmonic_order_list = sorted(available_amplitude_set)
    else:
        selected_harmonic_order_list = sorted({int(harmonic_order) for harmonic_order in SELECTED_HARMONIC_ORDER_LIST})

    for harmonic_order in selected_harmonic_order_list:
        if harmonic_order not in available_amplitude_set:
            raise ValueError(f"Selected harmonic {harmonic_order} has no amplitude ONNX target.")
        if harmonic_order != 0 and harmonic_order not in available_phase_set:
            raise ValueError(f"Selected harmonic {harmonic_order} has no phase ONNX target.")
    return selected_harmonic_order_list


def load_selected_rcim_target_list(
    configuration_list: list[RcimTargetConfiguration],
    selected_harmonic_order_list: list[int],
) -> list[LoadedOnnxTarget]:
    selected_harmonic_order_set = set(selected_harmonic_order_list)
    loaded_target_list: list[LoadedOnnxTarget] = []
    for target_configuration in configuration_list:
        if target_configuration.harmonic_order not in selected_harmonic_order_set:
            continue
        session = ort.InferenceSession(str(target_configuration.model_path), providers=["CPUExecutionProvider"])
        loaded_target_list.append(
            LoadedOnnxTarget(
                configuration=target_configuration,
                session=session,
                input_name=session.get_inputs()[0].name,
            )
        )
    return loaded_target_list


def build_rcim_feature_matrix(curve_record: CurveRecord) -> np.ndarray:
    return np.asarray(
        [[curve_record.speed_rpm, curve_record.oil_temperature_deg, abs(curve_record.torque_nm)]],
        dtype=np.float32,
    )


def predict_rcim_target_dictionary(
    curve_record: CurveRecord,
    loaded_target_list: list[LoadedOnnxTarget],
) -> dict[tuple[str, int], float]:
    feature_matrix = build_rcim_feature_matrix(curve_record)
    prediction_dictionary: dict[tuple[str, int], float] = {}
    for loaded_target in loaded_target_list:
        prediction_array = loaded_target.session.run(None, {loaded_target.input_name: feature_matrix})[0]
        prediction_value = float(np.asarray(prediction_array, dtype=np.float64).reshape(-1)[0])
        target_configuration = loaded_target.configuration
        prediction_dictionary[(target_configuration.target_kind, target_configuration.harmonic_order)] = prediction_value
    return prediction_dictionary


def reconstruct_curve_from_prediction_dictionary(
    angular_position_deg: np.ndarray,
    selected_harmonic_order_list: list[int],
    prediction_dictionary: dict[tuple[str, int], float],
) -> np.ndarray:
    angle_radians = np.deg2rad(angular_position_deg.astype(np.float64))
    reconstructed_curve = np.zeros_like(angle_radians, dtype=np.float64)
    for harmonic_order in selected_harmonic_order_list:
        amplitude = float(prediction_dictionary[("amplitude", harmonic_order)])
        if harmonic_order == 0:
            reconstructed_curve += amplitude
            continue
        phase_rad = float(prediction_dictionary[("phase", harmonic_order)])
        cosine_coefficient = amplitude * np.cos(phase_rad)
        sine_coefficient = -amplitude * np.sin(phase_rad)
        reconstructed_curve += (
            cosine_coefficient * np.cos(float(harmonic_order) * angle_radians)
            + sine_coefficient * np.sin(float(harmonic_order) * angle_radians)
        )
    return reconstructed_curve.astype(np.float32)


def load_direct_te_model(dataset_name: str, input_mode: str, family_name: str, surface: str) -> DirectTeModel:
    model_path = resolve_configured_path(Path("models") / dataset_name / input_mode / family_name / f"{surface}.onnx")
    if not model_path.exists():
        raise FileNotFoundError(f"Direct TE ONNX model does not exist | {model_path}")
    session = ort.InferenceSession(str(model_path), providers=["CPUExecutionProvider"])
    model_input = session.get_inputs()[0]
    input_rank = len(model_input.shape)
    if input_rank not in {2, 3}:
        raise ValueError(f"Unsupported direct TE ONNX input rank {input_rank} | {model_path}")
    return DirectTeModel(
        family_name=family_name,
        model_path=model_path,
        session=session,
        input_name=model_input.name,
        input_rank=input_rank,
    )


def predict_direct_pointwise(curve_record: CurveRecord, direct_model: DirectTeModel) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    feature_matrix = curve_record.direct_input_feature_matrix.astype(np.float32)
    prediction_list: list[np.ndarray] = []
    for start_index in range(0, feature_matrix.shape[0], DIRECT_BATCH_SIZE):
        batch = feature_matrix[start_index : start_index + DIRECT_BATCH_SIZE]
        prediction = direct_model.session.run(None, {direct_model.input_name: batch})[0]
        prediction_list.append(np.asarray(prediction, dtype=np.float32).reshape(-1))
    predicted_curve = np.concatenate(prediction_list, axis=0)
    return (
        curve_record.angular_position_deg,
        curve_record.measured_transmission_error_deg,
        predicted_curve.astype(np.float32),
    )


def build_sequence_windows(feature_matrix: np.ndarray, sequence_length: int, target_position: str) -> tuple[np.ndarray, np.ndarray]:
    if feature_matrix.shape[0] < sequence_length:
        raise ValueError(f"Curve has fewer points than sequence length | {feature_matrix.shape[0]} < {sequence_length}")
    target_position = target_position.strip().lower()
    if target_position == "center":
        if sequence_length % 2 != 1:
            raise ValueError("Center target position requires an odd sequence length.")
        target_offset = sequence_length // 2
    elif target_position == "last":
        target_offset = sequence_length - 1
    else:
        raise ValueError(f"Unsupported sequence target position | {target_position}")

    window_count = feature_matrix.shape[0] - sequence_length + 1
    window_array = np.stack(
        [feature_matrix[index : index + sequence_length] for index in range(window_count)],
        axis=0,
    ).astype(np.float32)
    target_index_array = np.arange(window_count, dtype=np.int64) + target_offset
    return window_array, target_index_array


def predict_direct_sequence(curve_record: CurveRecord, direct_model: DirectTeModel) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    window_array, target_index_array = build_sequence_windows(
        curve_record.direct_input_feature_matrix.astype(np.float32),
        DIRECT_SEQUENCE_LENGTH,
        DIRECT_SEQUENCE_TARGET_POSITION,
    )
    prediction_list: list[np.ndarray] = []
    for start_index in range(0, window_array.shape[0], DIRECT_BATCH_SIZE):
        batch = window_array[start_index : start_index + DIRECT_BATCH_SIZE]
        prediction = direct_model.session.run(None, {direct_model.input_name: batch})[0]
        prediction_list.append(np.asarray(prediction, dtype=np.float32).reshape(-1))
    predicted_curve = np.concatenate(prediction_list, axis=0)
    return (
        curve_record.angular_position_deg[target_index_array],
        curve_record.measured_transmission_error_deg[target_index_array],
        predicted_curve.astype(np.float32),
    )


def predict_direct_curve(curve_record: CurveRecord, direct_model: DirectTeModel) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if direct_model.input_rank == 2:
        return predict_direct_pointwise(curve_record, direct_model)
    return predict_direct_sequence(curve_record, direct_model)


def compute_metric_dictionary(measured_curve_deg: np.ndarray, predicted_curve_deg: np.ndarray) -> dict[str, float]:
    measured_curve = measured_curve_deg.astype(np.float64).reshape(-1)
    predicted_curve = predicted_curve_deg.astype(np.float64).reshape(-1)
    residual_curve = predicted_curve - measured_curve
    mse = float(np.mean(np.square(residual_curve)))
    mae = float(np.mean(np.abs(residual_curve)))
    rmse = float(np.sqrt(mse))
    peak_to_peak_denominator = max(float(np.ptp(measured_curve)), 1.0e-8)
    mean_error_pct = float(np.mean(np.abs(residual_curve) / peak_to_peak_denominator) * 100.0)
    p95_error_pct = float(np.percentile(np.abs(residual_curve) / peak_to_peak_denominator, 95.0) * 100.0)
    return {
        "mae_deg": mae,
        "rmse_deg": rmse,
        "mean_error_pct": mean_error_pct,
        "p95_error_pct": p95_error_pct,
    }


def sanitize_path_stem(path: Path) -> str:
    sanitized_stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", path.stem).strip("._")
    return sanitized_stem or "curve"


def save_predicted_curve_csv(
    curve_record: CurveRecord,
    angular_position_deg: np.ndarray,
    measured_curve_deg: np.ndarray,
    predicted_curve_deg: np.ndarray,
    output_csv_path: Path,
) -> None:
    output_csv_path.parent.mkdir(parents=True, exist_ok=True)
    with output_csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "angular_position_deg",
                "measured_te_deg",
                "predicted_te_deg",
                "residual_te_deg",
                "speed_rpm",
                "torque_nm",
                "oil_temperature_deg",
                "direction_label",
                "direction_flag",
            ],
        )
        writer.writeheader()
        for angle_deg, measured_te, predicted_te in zip(angular_position_deg, measured_curve_deg, predicted_curve_deg):
            writer.writerow(
                {
                    "angular_position_deg": float(angle_deg),
                    "measured_te_deg": float(measured_te),
                    "predicted_te_deg": float(predicted_te),
                    "residual_te_deg": float(predicted_te - measured_te),
                    "speed_rpm": float(curve_record.speed_rpm),
                    "torque_nm": float(curve_record.torque_nm),
                    "oil_temperature_deg": float(curve_record.oil_temperature_deg),
                    "direction_label": curve_record.direction_label,
                    "direction_flag": float(DIRECTION_FLAG[curve_record.direction_label]),
                }
            )


def save_curve_plot(
    curve_record: CurveRecord,
    angular_position_deg: np.ndarray,
    measured_curve_deg: np.ndarray,
    predicted_curve_deg: np.ndarray,
    metric_dictionary: dict[str, float],
    output_plot_path: Path,
) -> None:
    try:
        import matplotlib

        if not SHOW_PLOTS:
            matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as error:
        raise ModuleNotFoundError(
            "matplotlib is required for plot generation. Install it or run with --no-save-plots."
        ) from error

    output_plot_path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(10.0, 5.0))
    axis.plot(angular_position_deg, measured_curve_deg, label="Measured TE", linewidth=1.2, color="#4a4a4a")
    axis.plot(angular_position_deg, predicted_curve_deg, label="Predicted TE", linewidth=1.2, color="#1f77b4")
    axis.set_title(
        (
            f"{curve_record.dataset_name} | {curve_record.direction_label} | "
            f"{curve_record.speed_rpm:.0f} rpm | {curve_record.torque_nm:.0f} Nm | "
            f"{curve_record.oil_temperature_deg:.0f} C | MAE {metric_dictionary['mae_deg']:.6f} deg"
        ),
        fontsize=10,
    )
    axis.set_xlabel("Angular Position [deg]")
    axis.set_ylabel("Transmission Error [deg]")
    axis.grid(True, alpha=0.28)
    axis.legend(loc="best", fontsize=8)
    figure.tight_layout()
    if SAVE_PLOTS:
        figure.savefig(output_plot_path, dpi=180)
    if SHOW_PLOTS:
        plt.show()
    plt.close(figure)


def process_curve_record(
    curve_record: CurveRecord,
    arguments: argparse.Namespace,
    output_directory_path: Path,
    rcim_loaded_target_list: list[LoadedOnnxTarget] | None = None,
    rcim_selected_harmonic_order_list: list[int] | None = None,
    direct_model: DirectTeModel | None = None,
) -> dict[str, Any]:
    if arguments.model_kind == "rcim":
        if rcim_loaded_target_list is None or rcim_selected_harmonic_order_list is None:
            raise ValueError("RCIM targets were not loaded.")
        prediction_dictionary = predict_rcim_target_dictionary(curve_record, rcim_loaded_target_list)
        angular_position_deg = curve_record.angular_position_deg
        measured_curve_deg = curve_record.measured_transmission_error_deg
        predicted_curve_deg = reconstruct_curve_from_prediction_dictionary(
            angular_position_deg,
            rcim_selected_harmonic_order_list,
            prediction_dictionary,
        )
        model_descriptor = f"rcim_{arguments.model_family}"
    else:
        if direct_model is None:
            raise ValueError("Direct TE model was not loaded.")
        angular_position_deg, measured_curve_deg, predicted_curve_deg = predict_direct_curve(curve_record, direct_model)
        model_descriptor = f"direct_te_{arguments.model_family}"

    metric_dictionary = compute_metric_dictionary(measured_curve_deg, predicted_curve_deg)
    curve_stem = sanitize_path_stem(curve_record.source_csv_path)
    output_stem = f"{curve_stem}_{curve_record.direction_label}_{model_descriptor}"
    output_plot_path = output_directory_path / "plots" / f"{output_stem}.png"
    output_prediction_csv_path = output_directory_path / "predicted_curves" / f"{output_stem}_predicted.csv"
    if arguments.save_plots:
        save_curve_plot(
            curve_record,
            angular_position_deg,
            measured_curve_deg,
            predicted_curve_deg,
            metric_dictionary,
            output_plot_path,
        )
    if arguments.save_predicted_csv:
        save_predicted_curve_csv(
            curve_record,
            angular_position_deg,
            measured_curve_deg,
            predicted_curve_deg,
            output_prediction_csv_path,
        )

    return {
        "source_csv_path": str(curve_record.source_csv_path),
        "dataset_name": curve_record.dataset_name,
        "input_mode": curve_record.input_mode,
        "model_kind": arguments.model_kind,
        "model_family": arguments.model_family,
        "surface": arguments.surface,
        "direction_label": curve_record.direction_label,
        "plot_path": str(output_plot_path) if arguments.save_plots else "",
        "predicted_csv_path": str(output_prediction_csv_path) if arguments.save_predicted_csv else "",
        "speed_rpm": float(curve_record.speed_rpm),
        "torque_nm": float(curve_record.torque_nm),
        "oil_temperature_deg": float(curve_record.oil_temperature_deg),
        "point_count": int(angular_position_deg.size),
        **metric_dictionary,
    }


def write_summary_csv(summary_entry_list: list[dict[str, Any]], summary_csv_path: Path) -> None:
    summary_csv_path.parent.mkdir(parents=True, exist_ok=True)
    if not summary_entry_list:
        raise ValueError("No summary entries to write.")
    fieldnames = list(summary_entry_list[0].keys())
    with summary_csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary_entry_list)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run portable Track 2 ONNX curve plotting.")
    parser.add_argument("--dataset-name", choices=["simplified_dataset", "polished_dataset"], default=DATASET_NAME)
    parser.add_argument("--input-mode", choices=["setpoints", "actual_values"], default=INPUT_MODE)
    parser.add_argument("--model-kind", choices=["rcim", "direct_te"], default=MODEL_KIND)
    parser.add_argument("--surface", choices=["forward", "backward", "global"], default=SURFACE)
    parser.add_argument("--model-family", default=MODEL_FAMILY)
    parser.add_argument("--curve-csv", action="append", default=None, help="Input curve CSV path. May be repeated.")
    parser.add_argument("--curve-dir", default=None, help="Input curve directory. Uses recursive *.csv collection.")
    parser.add_argument("--max-curves", type=int, default=None, help="Limit the number of CSV files collected from config/directory.")
    parser.add_argument("--output-dir", default=OUTPUT_DIRECTORY_PATH)
    parser.add_argument("--no-save-plots", dest="save_plots", action="store_false", default=SAVE_PLOTS)
    parser.add_argument("--no-save-predicted-csv", dest="save_predicted_csv", action="store_false", default=SAVE_PREDICTED_CURVE_CSV)
    return parser.parse_args()


def run_portable_plotter() -> list[dict[str, Any]]:
    arguments = parse_arguments()
    arguments.dataset_name = normalize_selector(arguments.dataset_name)
    arguments.input_mode = normalize_selector(arguments.input_mode)
    arguments.model_kind = normalize_selector(arguments.model_kind)
    arguments.surface = normalize_selector(arguments.surface)

    if arguments.dataset_name == "simplified_dataset" and arguments.input_mode != "setpoints":
        raise ValueError("simplified_dataset only supports --input-mode setpoints.")
    if arguments.model_kind == "rcim" and arguments.surface == GLOBAL_SURFACE:
        raise ValueError("rcim models are direction-specific; use --surface forward or --surface backward.")

    output_directory_path = resolve_configured_path(arguments.output_dir)
    output_directory_path.mkdir(parents=True, exist_ok=True)

    rcim_loaded_target_list: list[LoadedOnnxTarget] | None = None
    rcim_selected_harmonic_order_list: list[int] | None = None
    direct_model: DirectTeModel | None = None
    if arguments.model_kind == "rcim":
        rcim_configuration_list = discover_rcim_target_configuration_list(
            arguments.dataset_name,
            arguments.surface,
            arguments.model_family,
        )
        rcim_selected_harmonic_order_list = resolve_selected_harmonic_order_list(rcim_configuration_list)
        rcim_loaded_target_list = load_selected_rcim_target_list(
            rcim_configuration_list,
            rcim_selected_harmonic_order_list,
        )
    else:
        direct_model = load_direct_te_model(
            arguments.dataset_name,
            arguments.input_mode,
            arguments.model_family,
            arguments.surface,
        )

    curve_csv_path_list = collect_curve_csv_path_list(arguments)
    print("Portable Track 2 ONNX curve plotter")
    print(f"Dataset: {arguments.dataset_name}")
    print(f"Input mode: {arguments.input_mode}")
    print(f"Model kind: {arguments.model_kind}")
    print(f"Model family: {arguments.model_family}")
    print(f"Surface: {arguments.surface}")
    if rcim_selected_harmonic_order_list is not None:
        print(f"Selected harmonics: {rcim_selected_harmonic_order_list}")
        print(f"Loaded RCIM ONNX targets: {len(rcim_loaded_target_list or [])}")
    if direct_model is not None:
        print(f"Direct TE model: {direct_model.model_path}")
        print(f"Direct TE input rank: {direct_model.input_rank}")
    print(f"Input curve CSV files: {len(curve_csv_path_list)}")
    print(f"Output directory: {output_directory_path}")

    summary_entry_list: list[dict[str, Any]] = []
    processed_curve_count = 0
    for csv_index, curve_csv_path in enumerate(curve_csv_path_list, start=1):
        curve_record_list = load_curve_record_list(
            curve_csv_path,
            arguments.dataset_name,
            arguments.input_mode,
            arguments.surface,
        )
        for curve_record in curve_record_list:
            processed_curve_count += 1
            print(f"[{processed_curve_count}] Processing {curve_record.direction_label} | {curve_csv_path}")
            summary_entry = process_curve_record(
                curve_record,
                arguments,
                output_directory_path,
                rcim_loaded_target_list=rcim_loaded_target_list,
                rcim_selected_harmonic_order_list=rcim_selected_harmonic_order_list,
                direct_model=direct_model,
            )
            summary_entry_list.append(summary_entry)

    if not summary_entry_list:
        raise ValueError("No curve records matched the selected dataset/surface.")
    summary_csv_path = output_directory_path / "portable_track2_onnx_curve_summary.csv"
    write_summary_csv(summary_entry_list, summary_csv_path)
    print(f"Summary written to: {summary_csv_path}")
    return summary_entry_list


if __name__ == "__main__":
    run_portable_plotter()
