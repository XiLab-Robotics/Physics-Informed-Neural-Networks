"""Portable original RCIM paper ONNX curve plotter.

This script is intentionally self-contained. It can be copied outside the
repository and run after editing the hardcoded user configuration block below.

Required external packages:
    numpy pandas matplotlib onnxruntime
"""

from __future__ import annotations

# Import Python Utilities
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import numpy as np
import onnxruntime as ort
import pandas as pd


# =============================================================================
# USER CONFIGURATION
# =============================================================================

# Relative paths are resolved from this directory. Use Path.cwd() when launching
# from the repository root, or replace it with an absolute folder when copying
# this script elsewhere.
BASE_DIRECTORY_PATH = Path.cwd()

# Select the harmonic orders to use for reconstruction. Set this to None to use
# every harmonic represented by ONNX_TARGET_CONFIGURATION_LIST.
SELECTED_HARMONIC_ORDER_LIST: list[int] | None = None

# Example sparse configuration:
# SELECTED_HARMONIC_ORDER_LIST = [0, 1, 39, 40]

# Provide one or more curve CSV files explicitly.
CURVE_CSV_PATH_LIST = [
    "data/simplified_dataset/Test_25degree/100rpm/100.0rpm100.0Nm25.0deg.csv",
]

# Optionally process every CSV in one folder. Leave as an empty string to disable.
CURVE_CSV_DIRECTORY_PATH = ""
CURVE_CSV_GLOB_PATTERN = "*.csv"
PROCESS_CURVE_DIRECTORY_RECURSIVELY = True

# Output directory for plots, predicted CSV files, and summary CSV.
OUTPUT_DIRECTORY_PATH = "output/validation_checks/portable_original_onnx_curve_plotter"

# Plot behavior.
SAVE_PLOTS = True
SHOW_PLOTS = False
SAVE_PREDICTED_CURVE_CSV = True

# If a custom CSV does not contain speed/torque/temperature columns and its file
# name does not follow the original pattern, set these defaults explicitly.
DEFAULT_SPEED_RPM: float | None = None
DEFAULT_TORQUE_NM: float | None = None
DEFAULT_OIL_TEMPERATURE_DEG: float | None = None

# ONNX feature order used by the recovered original paper forward models.
ONNX_FEATURE_ORDER = ["speed_rpm", "oil_temperature_deg", "torque_nm"]

# Original paper-best forward ONNX target list. Replace these strings with
# absolute paths after copying the script outside this repository.
ONNX_TARGET_CONFIGURATION_LIST = [
    ("amplitude", 0, "SVR", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/SVR/ampl/SVR_ampl0.onnx"),
    ("amplitude", 1, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/ampl/RandomForestRegressor_ampl1.onnx"),
    ("amplitude", 3, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl3.onnx"),
    ("amplitude", 39, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl39.onnx"),
    ("amplitude", 40, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/ampl/ExtraTreesRegressor_ampl40.onnx"),
    ("amplitude", 78, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl78.onnx"),
    ("amplitude", 81, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/ampl/RandomForestRegressor_ampl81.onnx"),
    ("amplitude", 156, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/ampl/ExtraTreesRegressor_ampl156.onnx"),
    ("amplitude", 162, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/ampl/ExtraTreesRegressor_ampl162.onnx"),
    ("amplitude", 240, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/ampl/ExtraTreesRegressor_ampl240.onnx"),
    ("phase", 1, "LGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/LGBM/phase/LGBMRegressor_phase1.onnx"),
    ("phase", 3, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase3.onnx"),
    ("phase", 39, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase39.onnx"),
    ("phase", 40, "GBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/GBM/phase/GradientBoostingRegressor_phase40.onnx"),
    ("phase", 78, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/phase/RandomForestRegressor_phase78.onnx"),
    ("phase", 81, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/phase/RandomForestRegressor_phase81.onnx"),
    ("phase", 156, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/phase/RandomForestRegressor_phase156.onnx"),
    ("phase", 162, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/phase/ExtraTreesRegressor_phase162.onnx"),
    ("phase", 240, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/phase/ExtraTreesRegressor_phase240.onnx"),
]


# =============================================================================
# PORTABLE IMPLEMENTATION
# =============================================================================

FILENAME_OPERATING_POINT_PATTERN = re.compile(
    r"(?P<speed_rpm>[0-9.]+)rpm(?P<torque_nm>[0-9.]+)Nm(?P<temperature_deg>[0-9.]+)deg\.csv$",
    re.IGNORECASE,
)

ANGULAR_POSITION_COLUMN_CANDIDATE_LIST = [
    "angular_position_deg",
    "position_output_reducer_fw_deg",
    "Poisition_Output_Reducer_Fw",
    "Position_Output_Reducer_Fw",
    "position_deg",
    "angle_deg",
    "theta_deg",
    "Angular Position [deg]",
]

MEASURED_TE_COLUMN_CANDIDATE_LIST = [
    "transmission_error_deg",
    "transmission_error_fw_deg",
    "Transmission_Error_Fw",
    "te_deg",
    "measured_te_deg",
    "Measured TE [deg]",
    "Transmission Error [deg]",
]

SPEED_COLUMN_CANDIDATE_LIST = [
    "speed_rpm",
    "rpm",
    "input_speed_rpm",
    "Input Speed [rpm]",
]

TORQUE_COLUMN_CANDIDATE_LIST = [
    "torque_nm",
    "tor",
    "applied_torque_nm",
    "Torque [Nm]",
]

OIL_TEMPERATURE_COLUMN_CANDIDATE_LIST = [
    "oil_temperature_deg",
    "temperature_deg",
    "oil_temperature_c",
    "deg",
    "Oil Temperature [deg]",
    "Oil Temperature [C]",
]


@dataclass(frozen=True)
class OnnxTargetConfiguration:

    """One hardcoded ONNX target configuration."""

    target_kind: str
    harmonic_order: int
    family_name: str
    model_path: Path


@dataclass(frozen=True)
class LoadedOnnxTarget:

    """One loaded ONNX target model."""

    configuration: OnnxTargetConfiguration
    session: ort.InferenceSession
    input_name: str


@dataclass(frozen=True)
class CurveRecord:

    """One measured curve and its operating point."""

    source_csv_path: Path
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    angular_position_deg: np.ndarray
    measured_transmission_error_deg: np.ndarray


def resolve_configured_path(path_value: str | Path) -> Path:

    """Resolve one hardcoded path from the configured base directory."""

    candidate_path = Path(path_value).expanduser()
    if candidate_path.is_absolute():
        return candidate_path.resolve()
    return (BASE_DIRECTORY_PATH / candidate_path).resolve()


def find_first_existing_column(dataframe: pd.DataFrame, candidate_list: list[str], role_label: str) -> str:

    """Find the first configured column name present in a dataframe."""

    for candidate_column in candidate_list:
        if candidate_column in dataframe.columns:
            return candidate_column
    raise ValueError(
        f"Missing {role_label} column. Expected one of {candidate_list}; "
        f"available columns are {dataframe.columns.tolist()}"
    )


def read_constant_value_from_column(dataframe: pd.DataFrame, column_name: str, role_label: str) -> float:

    """Read one finite operating-point scalar from a CSV column."""

    value_array = pd.to_numeric(dataframe[column_name], errors="coerce").to_numpy(dtype=np.float64)
    value_array = value_array[np.isfinite(value_array)]
    if value_array.size == 0:
        raise ValueError(f"Column {column_name} does not contain a finite {role_label} value.")
    return float(value_array[0])


def read_optional_operating_point_column(
    dataframe: pd.DataFrame,
    candidate_list: list[str],
    role_label: str,
) -> float | None:

    """Read one optional operating-point scalar from a CSV column."""

    for candidate_column in candidate_list:
        if candidate_column in dataframe.columns:
            return read_constant_value_from_column(dataframe, candidate_column, role_label)
    return None


def parse_operating_point_from_filename(csv_path: Path) -> dict[str, float] | None:

    """Parse original-dataset operating-point metadata from a CSV filename."""

    filename_match = FILENAME_OPERATING_POINT_PATTERN.search(csv_path.name)
    if filename_match is None:
        return None
    return {
        "speed_rpm": float(filename_match.group("speed_rpm")),
        "torque_nm": float(filename_match.group("torque_nm")),
        "oil_temperature_deg": float(filename_match.group("temperature_deg")),
    }


def resolve_operating_point(dataframe: pd.DataFrame, csv_path: Path) -> dict[str, float]:

    """Resolve speed, torque, and oil temperature for one input curve."""

    filename_metadata = parse_operating_point_from_filename(csv_path) or {}
    speed_rpm = (
        read_optional_operating_point_column(dataframe, SPEED_COLUMN_CANDIDATE_LIST, "speed")
        or filename_metadata.get("speed_rpm")
        or DEFAULT_SPEED_RPM
    )
    torque_nm = (
        read_optional_operating_point_column(dataframe, TORQUE_COLUMN_CANDIDATE_LIST, "torque")
        or filename_metadata.get("torque_nm")
        or DEFAULT_TORQUE_NM
    )
    oil_temperature_deg = (
        read_optional_operating_point_column(dataframe, OIL_TEMPERATURE_COLUMN_CANDIDATE_LIST, "oil temperature")
        or filename_metadata.get("oil_temperature_deg")
        or DEFAULT_OIL_TEMPERATURE_DEG
    )
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
            "Add columns, use an original-style filename, or hardcode DEFAULT_* values."
        )
    return {
        "speed_rpm": float(speed_rpm),
        "torque_nm": float(torque_nm),
        "oil_temperature_deg": float(oil_temperature_deg),
    }


def load_curve_record(csv_path: Path) -> CurveRecord:

    """Load one measured curve CSV."""

    dataframe = pd.read_csv(csv_path)
    angular_position_column = find_first_existing_column(
        dataframe,
        ANGULAR_POSITION_COLUMN_CANDIDATE_LIST,
        "angular position",
    )
    measured_te_column = find_first_existing_column(
        dataframe,
        MEASURED_TE_COLUMN_CANDIDATE_LIST,
        "measured transmission error",
    )
    operating_point_dictionary = resolve_operating_point(dataframe, csv_path)
    angular_position_deg = pd.to_numeric(dataframe[angular_position_column], errors="coerce").to_numpy(dtype=np.float64)
    measured_te_deg = pd.to_numeric(dataframe[measured_te_column], errors="coerce").to_numpy(dtype=np.float64)

    finite_mask = np.isfinite(angular_position_deg) & np.isfinite(measured_te_deg)
    angular_position_deg = angular_position_deg[finite_mask]
    measured_te_deg = measured_te_deg[finite_mask]

    rotation_mask = (angular_position_deg >= 0.0) & (angular_position_deg <= 360.0)
    angular_position_deg = angular_position_deg[rotation_mask]
    measured_te_deg = measured_te_deg[rotation_mask]

    sorting_index_array = np.argsort(angular_position_deg)
    angular_position_deg = angular_position_deg[sorting_index_array]
    measured_te_deg = measured_te_deg[sorting_index_array]
    if angular_position_deg.size == 0:
        raise ValueError(f"Empty angular-position curve after filtering | {csv_path}")

    return CurveRecord(
        source_csv_path=csv_path,
        speed_rpm=operating_point_dictionary["speed_rpm"],
        torque_nm=operating_point_dictionary["torque_nm"],
        oil_temperature_deg=operating_point_dictionary["oil_temperature_deg"],
        angular_position_deg=angular_position_deg.astype(np.float32),
        measured_transmission_error_deg=measured_te_deg.astype(np.float32),
    )


def collect_curve_csv_path_list() -> list[Path]:

    """Collect explicit and directory-based input CSV paths."""

    collected_path_list = [
        resolve_configured_path(csv_path)
        for csv_path in CURVE_CSV_PATH_LIST
        if str(csv_path).strip()
    ]
    if str(CURVE_CSV_DIRECTORY_PATH).strip():
        directory_path = resolve_configured_path(CURVE_CSV_DIRECTORY_PATH)
        if not directory_path.exists():
            raise FileNotFoundError(f"Configured curve CSV directory does not exist | {directory_path}")
        if PROCESS_CURVE_DIRECTORY_RECURSIVELY:
            collected_path_list.extend(sorted(directory_path.rglob(CURVE_CSV_GLOB_PATTERN)))
        else:
            collected_path_list.extend(sorted(directory_path.glob(CURVE_CSV_GLOB_PATTERN)))

    unique_path_list = sorted(set(path.resolve() for path in collected_path_list))
    if not unique_path_list:
        raise ValueError("No input curve CSV files configured.")
    for csv_path in unique_path_list:
        if not csv_path.exists():
            raise FileNotFoundError(f"Configured curve CSV file does not exist | {csv_path}")
    return unique_path_list


def load_onnx_target_configuration_list() -> list[OnnxTargetConfiguration]:

    """Load and validate hardcoded ONNX target configurations."""

    configuration_list: list[OnnxTargetConfiguration] = []
    for target_kind, harmonic_order, family_name, path_text in ONNX_TARGET_CONFIGURATION_LIST:
        if target_kind not in {"amplitude", "phase"}:
            raise ValueError(f"Unsupported target kind {target_kind!r}. Use 'amplitude' or 'phase'.")
        model_path = resolve_configured_path(path_text)
        if not model_path.exists():
            raise FileNotFoundError(f"Configured ONNX model does not exist | {model_path}")
        configuration_list.append(
            OnnxTargetConfiguration(
                target_kind=str(target_kind),
                harmonic_order=int(harmonic_order),
                family_name=str(family_name),
                model_path=model_path,
            )
        )
    return configuration_list


def resolve_selected_harmonic_order_list(configuration_list: list[OnnxTargetConfiguration]) -> list[int]:

    """Resolve and validate the selected harmonic list."""

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


def load_selected_onnx_target_list(
    configuration_list: list[OnnxTargetConfiguration],
    selected_harmonic_order_list: list[int],
) -> list[LoadedOnnxTarget]:

    """Load ONNX Runtime sessions for the selected target models."""

    selected_harmonic_order_set = set(selected_harmonic_order_list)
    loaded_target_list: list[LoadedOnnxTarget] = []
    for target_configuration in configuration_list:
        if target_configuration.harmonic_order not in selected_harmonic_order_set:
            continue
        session = ort.InferenceSession(
            str(target_configuration.model_path),
            providers=["CPUExecutionProvider"],
        )
        loaded_target_list.append(
            LoadedOnnxTarget(
                configuration=target_configuration,
                session=session,
                input_name=session.get_inputs()[0].name,
            )
        )
    return loaded_target_list


def build_feature_matrix(curve_record: CurveRecord) -> np.ndarray:

    """Build one ONNX input feature row."""

    feature_value_dictionary = {
        "speed_rpm": float(curve_record.speed_rpm),
        "torque_nm": float(curve_record.torque_nm),
        "oil_temperature_deg": float(curve_record.oil_temperature_deg),
    }
    return np.asarray(
        [[feature_value_dictionary[feature_name] for feature_name in ONNX_FEATURE_ORDER]],
        dtype=np.float32,
    )


def predict_target_dictionary(
    curve_record: CurveRecord,
    loaded_target_list: list[LoadedOnnxTarget],
) -> dict[tuple[str, int], float]:

    """Predict amplitude and phase targets for one curve."""

    feature_matrix = build_feature_matrix(curve_record)
    prediction_dictionary: dict[tuple[str, int], float] = {}
    for loaded_target in loaded_target_list:
        prediction_array = loaded_target.session.run(None, {loaded_target.input_name: feature_matrix})[0]
        prediction_value = float(np.asarray(prediction_array, dtype=np.float64).reshape(-1)[0])
        target_configuration = loaded_target.configuration
        prediction_dictionary[
            (target_configuration.target_kind, target_configuration.harmonic_order)
        ] = prediction_value
    return prediction_dictionary


def reconstruct_curve_from_prediction_dictionary(
    angular_position_deg: np.ndarray,
    selected_harmonic_order_list: list[int],
    prediction_dictionary: dict[tuple[str, int], float],
) -> np.ndarray:

    """Reconstruct one transmission-error curve from predicted harmonic targets."""

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


def compute_metric_dictionary(measured_curve_deg: np.ndarray, predicted_curve_deg: np.ndarray) -> dict[str, float]:

    """Compute simple curve metrics against measured TE."""

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

    """Build a filesystem-safe output stem from one input path."""

    sanitized_stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", path.stem).strip("._")
    return sanitized_stem or "curve"


def save_predicted_curve_csv(
    curve_record: CurveRecord,
    predicted_curve_deg: np.ndarray,
    output_csv_path: Path,
) -> None:

    """Save measured, predicted, and residual TE arrays for one curve."""

    output_csv_path.parent.mkdir(parents=True, exist_ok=True)
    output_dataframe = pd.DataFrame(
        {
            "angular_position_deg": curve_record.angular_position_deg.astype(np.float64),
            "measured_te_deg": curve_record.measured_transmission_error_deg.astype(np.float64),
            "predicted_te_deg": predicted_curve_deg.astype(np.float64),
            "residual_te_deg": (
                predicted_curve_deg.astype(np.float64)
                - curve_record.measured_transmission_error_deg.astype(np.float64)
            ),
            "speed_rpm": float(curve_record.speed_rpm),
            "torque_nm": float(curve_record.torque_nm),
            "oil_temperature_deg": float(curve_record.oil_temperature_deg),
        }
    )
    output_dataframe.to_csv(output_csv_path, index=False)


def save_curve_plot(
    curve_record: CurveRecord,
    predicted_curve_deg: np.ndarray,
    metric_dictionary: dict[str, float],
    output_plot_path: Path,
) -> None:

    """Save or show one measured-versus-predicted TE plot."""

    import matplotlib

    if not SHOW_PLOTS:
        matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    output_plot_path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(10.0, 5.0))
    axis.plot(
        curve_record.angular_position_deg,
        curve_record.measured_transmission_error_deg,
        label="Measured TE",
        linewidth=1.2,
        color="#4a4a4a",
    )
    axis.plot(
        curve_record.angular_position_deg,
        predicted_curve_deg,
        label="Predicted TE",
        linewidth=1.2,
        color="#1f77b4",
    )
    axis.set_title(
        (
            f"{curve_record.speed_rpm:.0f} rpm | {curve_record.torque_nm:.0f} Nm | "
            f"{curve_record.oil_temperature_deg:.0f} C | "
            f"MAE {metric_dictionary['mae_deg']:.6f} deg"
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
    loaded_target_list: list[LoadedOnnxTarget],
    selected_harmonic_order_list: list[int],
    output_directory_path: Path,
) -> dict[str, Any]:

    """Run prediction, reconstruction, metrics, and artifacts for one curve."""

    prediction_dictionary = predict_target_dictionary(curve_record, loaded_target_list)
    predicted_curve_deg = reconstruct_curve_from_prediction_dictionary(
        curve_record.angular_position_deg,
        selected_harmonic_order_list,
        prediction_dictionary,
    )
    metric_dictionary = compute_metric_dictionary(
        curve_record.measured_transmission_error_deg,
        predicted_curve_deg,
    )
    curve_stem = sanitize_path_stem(curve_record.source_csv_path)
    output_plot_path = output_directory_path / "plots" / f"{curve_stem}.png"
    output_prediction_csv_path = output_directory_path / "predicted_curves" / f"{curve_stem}_predicted.csv"
    save_curve_plot(curve_record, predicted_curve_deg, metric_dictionary, output_plot_path)
    if SAVE_PREDICTED_CURVE_CSV:
        save_predicted_curve_csv(curve_record, predicted_curve_deg, output_prediction_csv_path)

    return {
        "source_csv_path": str(curve_record.source_csv_path),
        "plot_path": str(output_plot_path) if SAVE_PLOTS else "",
        "predicted_csv_path": str(output_prediction_csv_path) if SAVE_PREDICTED_CURVE_CSV else "",
        "speed_rpm": float(curve_record.speed_rpm),
        "torque_nm": float(curve_record.torque_nm),
        "oil_temperature_deg": float(curve_record.oil_temperature_deg),
        "point_count": int(curve_record.angular_position_deg.size),
        **metric_dictionary,
    }


def run_portable_plotter() -> list[dict[str, Any]]:

    """Run the portable original-ONNX curve plotter."""

    output_directory_path = resolve_configured_path(OUTPUT_DIRECTORY_PATH)
    output_directory_path.mkdir(parents=True, exist_ok=True)
    configuration_list = load_onnx_target_configuration_list()
    selected_harmonic_order_list = resolve_selected_harmonic_order_list(configuration_list)
    loaded_target_list = load_selected_onnx_target_list(
        configuration_list,
        selected_harmonic_order_list,
    )
    curve_csv_path_list = collect_curve_csv_path_list()

    print("Portable original ONNX curve plotter")
    print(f"Selected harmonics: {selected_harmonic_order_list}")
    print(f"Loaded ONNX targets: {len(loaded_target_list)}")
    print(f"Input curve CSV files: {len(curve_csv_path_list)}")
    print(f"Output directory: {output_directory_path}")

    summary_entry_list = []
    for curve_index, curve_csv_path in enumerate(curve_csv_path_list, start=1):
        print(f"[{curve_index}/{len(curve_csv_path_list)}] Processing {curve_csv_path}")
        curve_record = load_curve_record(curve_csv_path)
        summary_entry = process_curve_record(
            curve_record,
            loaded_target_list,
            selected_harmonic_order_list,
            output_directory_path,
        )
        summary_entry_list.append(summary_entry)

    summary_csv_path = output_directory_path / "portable_original_onnx_curve_summary.csv"
    pd.DataFrame(summary_entry_list).to_csv(summary_csv_path, index=False)
    print(f"Summary written to: {summary_csv_path}")
    return summary_entry_list


if __name__ == "__main__":
    run_portable_plotter()
