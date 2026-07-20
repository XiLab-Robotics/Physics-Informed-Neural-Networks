"""Build familywise Track 2 reports for RCIM Track1 model-bank archives."""

from __future__ import annotations

# Import Python Utilities
import argparse, csv, shutil, sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import numpy as np
import onnxruntime as ort
import pandas as pd
import yaml
from tqdm import tqdm

# Import Project Utilities
from scripts.datasets import transmission_error_dataset
from scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank import (
    exact_paper_model_bank_support,
)
from scripts.paper_reimplementation.rcim_ml_compensation.harmonic_wise_comparison import (
    harmonic_wise_support,
)
from scripts.reports.analysis import build_track2_familywise_onnx_report
from scripts.tooling import repository_path_support
from scripts.training import shared_training_infrastructure

DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_familywise_onnx_report"
DEFAULT_REPORT_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "te_curve_verification_pipeline"
    / "03_family_reports"
)
REPORT_FILENAME = "track2_rcim_track1_familywise_onnx_report.md"
SUMMARY_FILENAME = "track2_familywise_onnx_report_summary.yaml"
MODEL_INVENTORY_FILENAME = "model_inventory.csv"
COMPONENT_MODEL_INVENTORY_FILENAME = "component_model_inventory.csv"
PER_CURVE_METRICS_FILENAME = "per_curve_metrics.csv"
DEFAULT_CURVES_PER_PAGE = 12
SURFACE_ORDER_LIST = ["forward", "backward", "global"]
SURFACE_SHORT_NAME_MAP = {"forward": "fw", "backward": "bw", "global": "global"}
GROUP_SPECIFICATION_LIST = [
    ("simplified_dataset", "setpoints"),
    ("polished_dataset", "setpoints"),
    ("polished_dataset", "actual_values"),
]
GROUP_TITLE_DICTIONARY = {
    ("simplified_dataset", "setpoints"): "Simplified Dataset + Setpoints",
    ("polished_dataset", "setpoints"): "Polished Dataset + Setpoints",
    ("polished_dataset", "actual_values"): "Polished Dataset + Actual Values",
}
RCIM_SELECTED_HARMONIC_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
RCIM_TARGET_KIND_ORDER = {"amplitude": 0, "phase": 1}


@dataclass(frozen=True)
class RcimComponentModelEntry:

    """Store one selected RCIM component model."""

    target_name: str
    target_kind: str
    harmonic_order: int
    family_name: str
    estimator_name: str
    onnx_model_path: Path
    python_model_path: Path
    reference_inventory_path: Path


@dataclass(frozen=True)
class RcimSurfaceModelBank:

    """Store one evaluated RCIM surface model-bank archive."""

    dataset_id: str
    input_mode: str
    surface: str
    run_name: str
    run_instance_id: str
    dataset_schema: str
    archive_root: Path
    source_validation_summary_path: Path | None
    training_config: dict[str, Any]
    component_entry_list: list[RcimComponentModelEntry]


@dataclass(frozen=True)
class RcimDatasetEvaluationBundle:

    """Store the RCIM held-out test records and matrices for one surface."""

    feature_name_list: list[str]
    target_name_list: list[str]
    test_feature_matrix: pd.DataFrame
    test_target_matrix: pd.DataFrame
    test_record_list: list[harmonic_wise_support.HarmonicCurveRecord]
    dataset_root: Path
    dataset_config_path: Path
    direction_label: str
    direction_prefix: str
    selected_harmonic_list: list[int]


def build_argument_parser() -> argparse.ArgumentParser:

    """Build command-line arguments."""

    parser = argparse.ArgumentParser(description="Build the RCIM Track1 familywise Track 2 report.")
    parser.add_argument("--curves-per-page", type=int, default=DEFAULT_CURVES_PER_PAGE)
    parser.add_argument("--report-date", default=None)
    parser.add_argument("--group-specification", action="append", default=None)
    parser.add_argument("--report-filename", default=REPORT_FILENAME)
    parser.add_argument("--asset-directory-name", default="assets")
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--report-root", type=Path, default=DEFAULT_REPORT_ROOT)
    parser.add_argument("--onnx-provider", action="append", default=None)
    repository_path_support.add_platform_arguments(parser)
    return parser


def load_yaml_dictionary(path_value: Path) -> dict[str, Any]:

    """Load one YAML dictionary."""

    with path_value.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {path_value}"
    return payload


def save_yaml_dictionary(path_value: Path, payload: dict[str, Any]) -> None:

    """Save one YAML dictionary."""

    path_value.parent.mkdir(parents=True, exist_ok=True)
    with path_value.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=False)


def parse_group_specification(group_specification: str) -> tuple[str, str]:

    """Parse one dataset/input-mode group specification."""

    normalized_group_specification = str(group_specification).strip()
    if ":" in normalized_group_specification:
        dataset_id, input_mode = normalized_group_specification.split(":", 1)
    elif "," in normalized_group_specification:
        dataset_id, input_mode = normalized_group_specification.split(",", 1)
    else:
        raise ValueError(
            "Expected group specification as dataset_id:input_mode | "
            f"{group_specification}"
        )
    group_tuple = (dataset_id.strip(), input_mode.strip())
    assert group_tuple in GROUP_TITLE_DICTIONARY, f"Unsupported RCIM group | {group_tuple}"
    return group_tuple


def format_project_path(path_value: str | Path | None) -> str:

    """Return a stable project-relative path."""

    if path_value is None:
        return ""
    return shared_training_infrastructure.format_project_relative_path(path_value).replace("\\", "/")


def resolve_project_path(path_value: str | Path) -> Path:

    """Resolve a project-relative or absolute path."""

    return shared_training_infrastructure.resolve_runtime_project_relative_path(path_value)


def normalize_archived_path(path_value: str | Path, dataset_id: str) -> Path:

    """Resolve a stored archive path after dataset-root migration."""

    path_text = str(path_value).replace("\\", "/")
    candidate_path = resolve_project_path(path_text)
    if candidate_path.exists():
        return candidate_path
    if dataset_id == "simplified_dataset" and path_text.startswith("models/paper_reference/rcim_track1/"):
        migrated_path_text = path_text.replace(
            "models/paper_reference/rcim_track1/",
            "models/simplified_dataset/paper_reference/rcim_track1/",
            1,
        )
        migrated_path = resolve_project_path(migrated_path_text)
        if migrated_path.exists():
            return migrated_path
    return candidate_path


def load_reference_inventory_component_list(
    reference_inventory_path: Path,
    dataset_id: str,
) -> list[RcimComponentModelEntry]:

    """Load component entries from one RCIM reference inventory."""

    inventory = load_yaml_dictionary(reference_inventory_path)
    family_name = str(
        inventory.get("implementation_family_name")
        or exact_paper_model_bank_support.EXACT_PAPER_FAMILY_NAME_ALIAS_MAP[str(inventory["paper_family_name"])]
    )
    component_entry_list: list[RcimComponentModelEntry] = []
    for raw_entry in inventory.get("reference_models", []):
        target_kind = str(raw_entry["target_kind"])
        harmonic_order = int(raw_entry["harmonic_order"])
        component_entry_list.append(
            RcimComponentModelEntry(
                target_name=str(raw_entry["target_name"]),
                target_kind=target_kind,
                harmonic_order=harmonic_order,
                family_name=family_name,
                estimator_name=str(raw_entry.get("export_estimator_name") or raw_entry.get("python_estimator_class_name")),
                onnx_model_path=normalize_archived_path(raw_entry["archived_model_path"], dataset_id),
                python_model_path=normalize_archived_path(raw_entry["python_model_path"], dataset_id),
                reference_inventory_path=reference_inventory_path,
            )
        )
    return component_entry_list


def build_component_key(component_entry: RcimComponentModelEntry) -> tuple[int, int]:

    """Build a stable harmonic target ordering key."""

    return (
        int(component_entry.harmonic_order),
        int(RCIM_TARGET_KIND_ORDER[component_entry.target_kind]),
    )


def resolve_simplified_surface_bank(dataset_id: str, input_mode: str, surface: str) -> RcimSurfaceModelBank | None:

    """Resolve one historical simplified RCIM surface archive."""

    archive_root = PROJECT_PATH / "models" / dataset_id / "paper_reference" / "rcim_track1" / surface
    if not archive_root.exists():
        return None

    candidate_dictionary: dict[str, list[tuple[float, float, RcimComponentModelEntry]]] = {}
    for reference_inventory_path in sorted(archive_root.rglob("reference_inventory.yaml")):
        for component_entry in load_reference_inventory_component_list(reference_inventory_path, dataset_id):
            inventory = load_yaml_dictionary(reference_inventory_path)
            raw_component = next(
                entry
                for entry in inventory["reference_models"]
                if str(entry["target_name"]) == component_entry.target_name
            )
            mape_value = float(raw_component.get("training_metric_mape_percent", raw_component.get("benchmark_mape_percent", 1.0e30)))
            mae_value = float(raw_component.get("training_metric_mae", raw_component.get("benchmark_mae", 1.0e30)))
            candidate_dictionary.setdefault(component_entry.target_name, []).append((mape_value, mae_value, component_entry))

    component_entry_list: list[RcimComponentModelEntry] = []
    for target_name, candidate_list in candidate_dictionary.items():
        candidate_list.sort(key=lambda item: (item[0], item[1], item[2].family_name))
        component_entry_list.append(candidate_list[0][2])
    component_entry_list.sort(key=build_component_key)
    assert len(component_entry_list) == 19, f"Expected 19 selected components | {archive_root}"

    first_entry = component_entry_list[0]
    first_inventory = load_yaml_dictionary(first_entry.reference_inventory_path)
    source_config_path = normalize_archived_path(
        first_inventory["reference_models"][0]["source_training_config_snapshot_path"],
        dataset_id,
    )
    training_config = build_simplified_training_config_from_snapshot(source_config_path, surface)
    return RcimSurfaceModelBank(
        dataset_id=dataset_id,
        input_mode=input_mode,
        surface=surface,
        run_name=f"rcim_track1_simplified_setpoints_{surface}",
        run_instance_id="historical_simplified_rcim_track1_component_winner_bank",
        dataset_schema="simplified_curve_v1",
        archive_root=archive_root,
        source_validation_summary_path=None,
        training_config=training_config,
        component_entry_list=component_entry_list,
    )


def build_simplified_training_config_from_snapshot(source_config_path: Path, surface: str) -> dict[str, Any]:

    """Build a simplified setpoint evaluation config from a historical snapshot."""

    source_config = load_yaml_dictionary(source_config_path)
    source_config.setdefault("paths", {})["dataset_config_path"] = "config/datasets/transmission_error_dataset.yaml"
    source_config.setdefault("experiment", {})["run_name"] = f"rcim_track1_simplified_setpoints_{surface}"
    source_config["experiment"]["model_family"] = "rcim_track1"
    source_config["experiment"]["model_type"] = f"exact_model_bank_{surface}"
    source_config["dataset"] = {"name": "simplified_dataset", "input_mode": "setpoints"}
    source_config.setdefault("data", {})["direction_label"] = surface
    source_config["data"]["input_feature_names"] = ["rpm", "deg", "tor"]
    source_config.setdefault("evaluation", {})["selected_harmonics"] = list(RCIM_SELECTED_HARMONIC_LIST)
    source_config["evaluation"]["decomposition_point_stride"] = int(
        source_config["evaluation"].get("decomposition_point_stride", 1)
    )
    source_config.setdefault("target_scope", {})["mode"] = "all"
    source_config["target_scope"]["include_phase_zero"] = False
    source_config.setdefault("training", {})["validation_split"] = float(source_config["training"].get("validation_split", 0.2))
    source_config["training"]["test_size"] = float(source_config["training"].get("test_size", 0.1))
    source_config["training"]["random_seed"] = int(source_config["training"].get("random_seed", 0))
    return source_config


def resolve_polished_surface_bank(dataset_id: str, input_mode: str, surface: str) -> RcimSurfaceModelBank:

    """Resolve one promoted polished RCIM surface archive."""

    promotion_inventory_path = PROJECT_PATH / "models" / dataset_id / "paper_reference" / "rcim_track1" / input_mode / "promotion_inventory.yaml"
    promotion_inventory = load_yaml_dictionary(promotion_inventory_path)
    surface_entry = next(
        entry
        for entry in promotion_inventory["surfaces"]
        if str(entry["surface"]) == surface
    )
    source_validation_summary_path = resolve_project_path(surface_entry["source_validation_directory"]) / "validation_summary.yaml"
    validation_summary = load_yaml_dictionary(source_validation_summary_path)
    target_winner_dictionary = {
        str(entry["target_name"]): str(entry["winning_family"])
        for entry in validation_summary["target_winner_registry"]
    }
    family_inventory_dictionary = {
        str(entry["family_name"]): resolve_project_path(entry["reference_inventory_path"])
        for entry in surface_entry["family_archives"]
    }

    component_entry_list: list[RcimComponentModelEntry] = []
    for target_name, family_name in target_winner_dictionary.items():
        inventory_path = family_inventory_dictionary[family_name]
        matching_component_list = [
            component_entry
            for component_entry in load_reference_inventory_component_list(inventory_path, dataset_id)
            if component_entry.target_name == target_name
        ]
        assert len(matching_component_list) == 1, f"Missing polished target component | {target_name} | {inventory_path}"
        component_entry_list.append(matching_component_list[0])
    component_entry_list.sort(key=build_component_key)

    training_config_path = resolve_project_path(validation_summary["experiment"]["output_directory"]) / "training_config.yaml"
    training_config = load_yaml_dictionary(training_config_path)
    return RcimSurfaceModelBank(
        dataset_id=dataset_id,
        input_mode=input_mode,
        surface=surface,
        run_name=str(validation_summary["experiment"]["run_name"]),
        run_instance_id=str(validation_summary["experiment"]["run_instance_id"]),
        dataset_schema=str(training_config.get("metadata", {}).get("dataset_schema", "polished_point_v1")),
        archive_root=resolve_project_path(surface_entry["surface_archive_root"]),
        source_validation_summary_path=source_validation_summary_path,
        training_config=training_config,
        component_entry_list=component_entry_list,
    )


def resolve_surface_bank(dataset_id: str, input_mode: str, surface: str) -> RcimSurfaceModelBank | None:

    """Resolve one RCIM surface bank for a dataset/input-mode group."""

    if dataset_id == "simplified_dataset":
        return resolve_simplified_surface_bank(dataset_id, input_mode, surface)
    return resolve_polished_surface_bank(dataset_id, input_mode, surface)


def build_rcim_dataset_evaluation_bundle(training_config: dict[str, Any]) -> RcimDatasetEvaluationBundle:

    """Build RCIM held-out test records and feature matrices."""

    dataset_config_path = shared_training_infrastructure.resolve_project_relative_path(
        training_config["paths"]["dataset_config_path"]
    )
    dataset_configuration = transmission_error_dataset.load_dataset_processing_config(dataset_config_path)
    selected_dataset_name, dataset_root = transmission_error_dataset.resolve_dataset_selection(
        dataset_configuration,
        training_config.get("dataset", {}).get("name"),
    )
    selected_input_mode = transmission_error_dataset.resolve_input_mode_selection(
        dataset_configuration,
        selected_dataset_name,
        training_config.get("dataset", {}).get("input_mode"),
    )
    direction_label, direction_prefix = resolve_rcim_direction_settings(training_config)
    directional_file_manifest = transmission_error_dataset.build_directional_file_manifest(
        dataset_root=dataset_root,
        use_forward_direction=(direction_label in [transmission_error_dataset.FORWARD_DIRECTION, "global"]),
        use_backward_direction=(direction_label in [transmission_error_dataset.BACKWARD_DIRECTION, "global"]),
        dataset_name=selected_dataset_name,
    )
    _, _, test_manifest = transmission_error_dataset.split_directional_file_manifest(
        directional_file_manifest,
        validation_split=float(training_config["training"]["validation_split"]),
        test_split=float(training_config["training"]["test_size"]),
        random_seed=int(training_config["training"]["random_seed"]),
    )
    selected_harmonic_list = [
        int(harmonic_order)
        for harmonic_order in training_config["evaluation"]["selected_harmonics"]
    ]
    decomposition_point_stride = int(training_config["evaluation"]["decomposition_point_stride"])
    test_record_list = harmonic_wise_support.build_curve_record_list(
        test_manifest,
        selected_harmonic_list,
        decomposition_point_stride,
        selected_dataset_name,
        selected_input_mode,
    )
    feature_row_list: list[dict[str, float]] = []
    target_row_list: list[dict[str, float]] = []
    target_name_list = build_rcim_target_name_list(direction_prefix, selected_harmonic_list)
    for curve_record in test_record_list:
        feature_row_list.append(
            {
                "rpm": float(curve_record.speed_rpm),
                "deg": float(curve_record.oil_temperature_deg),
                "tor": float(curve_record.torque_nm),
                "angular_position_deg": 0.0,
                "input_speed_rpm": float(curve_record.speed_rpm),
                "input_torque_nm": float(curve_record.torque_nm),
                "oil_temperature_deg": float(curve_record.oil_temperature_deg),
                "direction_flag": float(curve_record.direction_flag),
            }
        )
        target_dictionary: dict[str, float] = {}
        for harmonic_order in selected_harmonic_list:
            target_dictionary[f"fft_y_{direction_prefix}_filtered_ampl_{harmonic_order}"] = float(
                curve_record.amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"]
            )
            if harmonic_order != 0:
                target_dictionary[f"fft_y_{direction_prefix}_filtered_phase_{harmonic_order}"] = float(
                    curve_record.amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"]
                )
        target_row_list.append(target_dictionary)
    feature_name_list = exact_paper_model_bank_support.resolve_paper_input_feature_name_list(training_config)
    test_feature_matrix = pd.DataFrame(feature_row_list)[feature_name_list].copy()
    test_target_matrix = pd.DataFrame(target_row_list)[target_name_list].copy()
    return RcimDatasetEvaluationBundle(
        feature_name_list=feature_name_list,
        target_name_list=target_name_list,
        test_feature_matrix=test_feature_matrix,
        test_target_matrix=test_target_matrix,
        test_record_list=test_record_list,
        dataset_root=dataset_root,
        dataset_config_path=dataset_config_path,
        direction_label=direction_label,
        direction_prefix=direction_prefix,
        selected_harmonic_list=selected_harmonic_list,
    )


def resolve_rcim_direction_settings(training_config: dict[str, Any]) -> tuple[str, str]:

    """Resolve one direction label and target prefix."""

    direction_label = str(training_config["data"]["direction_label"]).strip().lower()
    prefix_dictionary = {"forward": "Fw", "backward": "Bw", "global": "Global"}
    assert direction_label in prefix_dictionary, f"Unsupported direction | {direction_label}"
    return direction_label, prefix_dictionary[direction_label]


def build_rcim_target_name_list(direction_prefix: str, selected_harmonic_list: list[int]) -> list[str]:

    """Build ordered RCIM amplitude/phase target names."""

    target_name_list: list[str] = []
    for harmonic_order in selected_harmonic_list:
        target_name_list.append(f"fft_y_{direction_prefix}_filtered_ampl_{harmonic_order}")
        if harmonic_order != 0:
            target_name_list.append(f"fft_y_{direction_prefix}_filtered_phase_{harmonic_order}")
    return target_name_list


def predict_component_vector(
    component_entry: RcimComponentModelEntry,
    test_feature_matrix: pd.DataFrame,
    provider_list: list[str],
) -> np.ndarray:

    """Predict one RCIM harmonic component through ONNX Runtime."""

    assert component_entry.onnx_model_path.exists(), f"Missing ONNX model | {component_entry.onnx_model_path}"
    session = ort.InferenceSession(str(component_entry.onnx_model_path), providers=provider_list)
    input_metadata = session.get_inputs()[0]
    output_metadata = session.get_outputs()[0]
    feature_matrix = np.asarray(test_feature_matrix.to_numpy(dtype=np.float32), dtype=np.float32)
    expected_width = input_metadata.shape[1] if len(input_metadata.shape) > 1 else None
    if isinstance(expected_width, int):
        assert expected_width == feature_matrix.shape[1], (
            "RCIM ONNX feature width mismatch | "
            f"model={component_entry.onnx_model_path} expected={expected_width} observed={feature_matrix.shape[1]}"
        )
    prediction_array = session.run([output_metadata.name], {input_metadata.name: feature_matrix})[0]
    return np.asarray(prediction_array, dtype=np.float64).reshape(-1)


def resolve_h0_sign_multiplier(direction_label: str) -> float:

    """Return the paper-faithful RCIM h0 sign convention for one curve direction."""

    normalized_direction_label = str(direction_label).strip().lower()
    if normalized_direction_label == transmission_error_dataset.FORWARD_DIRECTION:
        return -1.0
    return 1.0


def convert_amplitude_phase_vector_to_coefficient_dictionary(
    target_vector: np.ndarray,
    target_name_list: list[str],
    selected_harmonic_list: list[int],
    h0_sign_multiplier: float,
) -> dict[str, float]:

    """Convert one amplitude/phase vector into harmonic coefficients."""

    target_dictionary = {
        target_name: float(target_vector[target_index])
        for target_index, target_name in enumerate(target_name_list)
    }
    coefficient_dictionary: dict[str, float] = {}
    for harmonic_order in selected_harmonic_list:
        amplitude_value = float(
            target_dictionary[
                next(target_name for target_name in target_name_list if target_name.endswith(f"_ampl_{harmonic_order}"))
            ]
        )
        if harmonic_order == 0:
            coefficient_dictionary["coefficient_cos_h0"] = float(h0_sign_multiplier) * amplitude_value
            continue
        phase_value = float(
            target_dictionary[
                next(target_name for target_name in target_name_list if target_name.endswith(f"_phase_{harmonic_order}"))
            ]
        )
        coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"] = float(amplitude_value * np.cos(phase_value))
        coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"] = float(-amplitude_value * np.sin(phase_value))
    return coefficient_dictionary


def evaluate_surface_bank(
    group_id: str,
    surface_bank: RcimSurfaceModelBank,
    provider_list: list[str],
) -> tuple[list[build_track2_familywise_onnx_report.CurveEvaluationEntry], dict[str, float]]:

    """Evaluate one RCIM surface model bank on held-out test curves."""

    evaluation_bundle = build_rcim_dataset_evaluation_bundle(surface_bank.training_config)
    component_dictionary = {
        component_entry.target_name: component_entry
        for component_entry in surface_bank.component_entry_list
    }
    prediction_column_list = [
        predict_component_vector(component_dictionary[target_name], evaluation_bundle.test_feature_matrix, provider_list)
        for target_name in evaluation_bundle.target_name_list
    ]
    prediction_matrix = np.column_stack(prediction_column_list).astype(np.float64)
    curve_entry_list: list[build_track2_familywise_onnx_report.CurveEvaluationEntry] = []
    for sample_index, curve_record in enumerate(evaluation_bundle.test_record_list):
        h0_sign_multiplier = resolve_h0_sign_multiplier(str(curve_record.direction_label))
        predicted_coefficient_dictionary = convert_amplitude_phase_vector_to_coefficient_dictionary(
            prediction_matrix[sample_index],
            evaluation_bundle.target_name_list,
            evaluation_bundle.selected_harmonic_list,
            h0_sign_multiplier,
        )
        prediction_curve_deg = harmonic_wise_support.reconstruct_curve_from_coefficients(
            curve_record.angular_position_deg,
            evaluation_bundle.selected_harmonic_list,
            predicted_coefficient_dictionary,
        )
        metric_dictionary = build_track2_familywise_onnx_report.compute_curve_metrics(
            curve_record.transmission_error_deg,
            prediction_curve_deg,
        )
        curve_entry_list.append(
            build_track2_familywise_onnx_report.CurveEvaluationEntry(
                group_id=group_id,
                surface=surface_bank.surface,
                dataset_index=sample_index,
                source_file_path=format_project_path(curve_record.source_file_path),
                direction_label=str(curve_record.direction_label),
                speed_rpm=float(curve_record.speed_rpm),
                torque_nm=float(curve_record.torque_nm),
                oil_temperature_deg=float(curve_record.oil_temperature_deg),
                angular_position_deg=np.asarray(curve_record.angular_position_deg, dtype=np.float32),
                target_curve_deg=np.asarray(curve_record.transmission_error_deg, dtype=np.float32),
                prediction_curve_deg=np.asarray(prediction_curve_deg, dtype=np.float32),
                plot_measured_angular_position_deg=np.asarray(curve_record.angular_position_deg, dtype=np.float32),
                plot_measured_curve_deg=np.asarray(curve_record.transmission_error_deg, dtype=np.float32),
                plot_prediction_angular_position_deg=np.asarray(curve_record.angular_position_deg, dtype=np.float32),
                plot_prediction_curve_deg=np.asarray(prediction_curve_deg, dtype=np.float32),
                metrics=metric_dictionary,
            )
        )
    return curve_entry_list, build_track2_familywise_onnx_report.average_metric_dictionary(
        [curve_entry.metrics for curve_entry in curve_entry_list]
    )


def write_csv(path_value: Path, header_list: list[str], row_list: list[list[Any]]) -> None:

    """Write one CSV file."""

    path_value.parent.mkdir(parents=True, exist_ok=True)
    with path_value.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file, lineterminator="\n")
        writer.writerow(header_list)
        writer.writerows(row_list)


def build_report_markdown(
    report_path: Path,
    output_directory: Path,
    summary_path: Path,
    model_inventory_csv_path: Path,
    component_inventory_csv_path: Path,
    per_curve_metrics_csv_path: Path,
    group_summary_list: list[dict[str, Any]],
    curves_per_page: int,
) -> str:

    """Build the RCIM familywise Markdown report."""

    line_list = [
        "# TE Curve Verification Pipeline Familywise ONNX Report - rcim_track1",
        "",
        "## Overview",
        "",
        "This report evaluates `rcim_track1` paper-reference model-bank archives.",
        "Each surface loads the selected harmonic amplitude/phase ONNX components",
        "from `models/`, reconstructs full TE curves, and compares those curves",
        "against dataset-matched held-out measured TE traces.",
        "",
        "Unlike standard familywise model-development exports, `rcim_track1` uses",
        "a component bank rather than one ONNX file per surface. The surface tables",
        "therefore list archive roots and inventory paths; every exact component",
        "ONNX and Python path is recorded in the component inventory CSV.",
        "The surface path table intentionally uses archive-root glob patterns",
        "because one `rcim_track1` surface is assembled from 19 component ONNX",
        "models rather than from a single surface-level ONNX file.",
        "The harmonic reconstruction applies the paper-faithful `h0` sign",
        "convention per curve direction: forward curves use `-1`, backward",
        "curves use `+1`.",
        "",
        "## Output Artifacts",
        "",
        f"- output directory: `{format_project_path(output_directory)}`;",
        f"- summary YAML: `{format_project_path(summary_path)}`;",
        f"- model inventory CSV: `{format_project_path(model_inventory_csv_path)}`;",
        f"- component model inventory CSV: `{format_project_path(component_inventory_csv_path)}`;",
        f"- per-curve metrics CSV: `{format_project_path(per_curve_metrics_csv_path)}`.",
        "",
    ]
    for group_summary in group_summary_list:
        line_list.extend(
            [
                f"## {group_summary['group_title']}",
                "",
                f"- dataset: `{group_summary['dataset_id']}`;",
                f"- input mode: `{group_summary['input_mode']}`;",
                "- evaluated family: `rcim_track1`;",
                f"- dataset root: `{group_summary['dataset_root']}`.",
                "",
                "### Models Used",
                "",
                "| Surface | Run Name | Run Instance | Dataset Schema |",
                "| --- | --- | --- | --- |",
            ]
        )
        for model_summary in group_summary["model_summary_list"]:
            line_list.append(
                f"| {model_summary['surface']} | `{model_summary['run_name']}` | "
                f"`{model_summary['run_instance_id']}` | `{model_summary['dataset_schema']}` |"
            )
        line_list.extend(
            [
                "",
                "Exact model paths:",
                "",
                "| Surface | ONNX Model Path | Python Model Path |",
                "| --- | --- | --- |",
            ]
        )
        for model_summary in group_summary["model_summary_list"]:
            line_list.append(
                f"| {model_summary['surface']} | `{model_summary['onnx_model_path']}` | "
                f"`{model_summary['python_model_path']}` |"
            )
        if group_summary["missing_surface_list"]:
            for surface_name in group_summary["missing_surface_list"]:
                line_list.append(f"| {surface_name} | `not available in archive` | `not available in archive` |")
        line_list.extend(["", "### Aggregate Metrics", ""])
        build_track2_familywise_onnx_report.append_metric_table(line_list, group_summary["model_summary_list"])
        if group_summary["missing_surface_list"]:
            line_list.extend(
                [
                    "Unavailable surfaces:",
                    "",
                    *[
                        f"- `{surface_name}`: no archive exists under the dataset-matched `paper_reference/rcim_track1` root."
                        for surface_name in group_summary["missing_surface_list"]
                    ],
                    "",
                ]
            )
        for model_summary in group_summary["model_summary_list"]:
            line_list.extend(
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
    while line_list and not line_list[-1]:
        line_list.pop()
    return "\n".join(line_list) + "\n"


def run_familywise_rcim_track1_report(arguments: argparse.Namespace) -> dict[str, Any]:

    """Generate the RCIM Track1 familywise report."""

    repository_path_support.set_runtime_platform(repository_path_support.resolve_argument_platform(arguments))
    provider_list = list(arguments.onnx_provider or ["CPUExecutionProvider"])
    curves_per_page = int(arguments.curves_per_page)
    group_specification_list = [
        parse_group_specification(group_specification)
        for group_specification in (arguments.group_specification or [])
    ] or list(GROUP_SPECIFICATION_LIST)
    report_filename = str(arguments.report_filename).strip()
    assert report_filename.endswith(".md"), f"Report filename must be Markdown | {report_filename}"
    asset_directory_name = str(arguments.asset_directory_name).strip()
    assert asset_directory_name, "Asset directory name cannot be empty"
    current_timestamp = datetime.now().astimezone()
    report_date = arguments.report_date or current_timestamp.strftime("%Y-%m-%d")
    datetime.strptime(report_date, "%Y-%m-%d")
    run_instance_id = f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}__{Path(report_filename).stem}"
    output_directory = resolve_project_path(arguments.output_root) / "rcim_track1" / run_instance_id
    report_directory = resolve_project_path(arguments.report_root) / "rcim_track1" / f"[{report_date}]"
    report_asset_root = report_directory / asset_directory_name
    if report_asset_root.exists():
        shutil.rmtree(report_asset_root)
    output_directory.mkdir(parents=True, exist_ok=True)
    report_asset_root.mkdir(parents=True, exist_ok=True)

    model_inventory_row_list: list[list[Any]] = []
    component_inventory_row_list: list[list[Any]] = []
    per_curve_metric_row_list: list[list[Any]] = []
    group_summary_list: list[dict[str, Any]] = []

    for dataset_id, input_mode in tqdm(group_specification_list, desc="RCIM groups", unit="group", ascii=True, ncols=80):
        group_id = f"{dataset_id}__{input_mode}"
        group_title = GROUP_TITLE_DICTIONARY[(dataset_id, input_mode)]
        model_summary_list: list[dict[str, Any]] = []
        missing_surface_list: list[str] = []
        dataset_root_text = ""
        for surface in SURFACE_ORDER_LIST:
            surface_bank = resolve_surface_bank(dataset_id, input_mode, surface)
            if surface_bank is None:
                missing_surface_list.append(surface)
                continue
            curve_entry_list, aggregate_metrics = evaluate_surface_bank(group_id, surface_bank, provider_list)
            selected_curve_entry_list = build_track2_familywise_onnx_report.select_representative_curve_entries(
                curve_entry_list,
                curves_per_page,
            )
            collage_filename = f"{surface}_{curves_per_page}_curve_collage.png"
            collage_path = output_directory / "collages" / group_id / collage_filename
            report_collage_path = report_asset_root / group_id / collage_filename
            build_track2_familywise_onnx_report.save_surface_collage(
                collage_path,
                f"{group_title} | rcim_track1 | {surface}",
                selected_curve_entry_list,
            )
            report_collage_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(collage_path, report_collage_path)
            dataset_root_text = format_project_path(build_rcim_dataset_evaluation_bundle(surface_bank.training_config).dataset_root)
            component_inventory_path_text = format_project_path(component_inventory_csv_path_placeholder(output_directory))
            model_summary = {
                "dataset_id": dataset_id,
                "input_mode": input_mode,
                "surface": surface,
                "run_name": surface_bank.run_name,
                "run_instance_id": surface_bank.run_instance_id,
                "dataset_schema": surface_bank.dataset_schema,
                "model_type": "rcim_track1_component_bank",
                "onnx_model_path": format_project_path(surface_bank.archive_root / "*/onnx/*/*.onnx"),
                "python_model_path": format_project_path(surface_bank.archive_root / "*/python/*/*.pkl"),
                "source_inventory_path": component_inventory_path_text,
                "archive_root": format_project_path(surface_bank.archive_root),
                "source_validation_summary_path": format_project_path(surface_bank.source_validation_summary_path),
                "evaluated_curve_count": int(len(curve_entry_list)),
                "aggregate_metrics": aggregate_metrics,
                "collage_path": format_project_path(collage_path),
                "collage_markdown_path": build_track2_familywise_onnx_report.build_relative_markdown_path(
                    report_collage_path,
                    report_directory,
                ),
                "selected_component_count": len(surface_bank.component_entry_list),
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
            model_inventory_row_list.append(
                [
                    dataset_id,
                    input_mode,
                    surface,
                    surface_bank.run_name,
                    surface_bank.run_instance_id,
                    surface_bank.dataset_schema,
                    format_project_path(surface_bank.archive_root),
                    format_project_path(surface_bank.source_validation_summary_path),
                    len(surface_bank.component_entry_list),
                ]
            )
            for component_entry in surface_bank.component_entry_list:
                component_inventory_row_list.append(
                    [
                        dataset_id,
                        input_mode,
                        surface,
                        component_entry.target_name,
                        component_entry.target_kind,
                        component_entry.harmonic_order,
                        component_entry.family_name,
                        component_entry.estimator_name,
                        format_project_path(component_entry.onnx_model_path),
                        format_project_path(component_entry.python_model_path),
                        format_project_path(component_entry.reference_inventory_path),
                    ]
                )
            for curve_entry in curve_entry_list:
                metric_dictionary = curve_entry.metrics
                per_curve_metric_row_list.append(
                    [
                        group_id,
                        dataset_id,
                        input_mode,
                        surface,
                        surface_bank.run_name,
                        surface_bank.run_instance_id,
                        curve_entry.dataset_index,
                        curve_entry.direction_label,
                        f"{curve_entry.speed_rpm:.9f}",
                        f"{curve_entry.torque_nm:.9f}",
                        f"{curve_entry.oil_temperature_deg:.9f}",
                        curve_entry.source_file_path,
                        f"{metric_dictionary['mse']:.12f}",
                        f"{metric_dictionary['mae']:.12f}",
                        f"{metric_dictionary['rmse']:.12f}",
                        f"{metric_dictionary['mean_percentage_error_pct']:.12f}",
                        f"{metric_dictionary['signed_mean_offset_deg']:.12f}",
                        f"{metric_dictionary['absolute_mean_offset_deg']:.12f}",
                        f"{metric_dictionary['peak_to_peak_error_deg']:.12f}",
                        f"{metric_dictionary['centered_mae_deg']:.12f}",
                        f"{metric_dictionary['centered_rmse_deg']:.12f}",
                    ]
                )
        group_summary_list.append(
            {
                "group_id": group_id,
                "group_title": group_title,
                "dataset_id": dataset_id,
                "input_mode": input_mode,
                "dataset_root": dataset_root_text or (
                    "data/simplified_dataset" if dataset_id == "simplified_dataset" else "data/polished_dataset"
                ),
                "model_summary_list": model_summary_list,
                "missing_surface_list": missing_surface_list,
            }
        )

    summary_path = output_directory / SUMMARY_FILENAME
    model_inventory_csv_path = output_directory / MODEL_INVENTORY_FILENAME
    component_inventory_csv_path = output_directory / COMPONENT_MODEL_INVENTORY_FILENAME
    per_curve_metrics_csv_path = output_directory / PER_CURVE_METRICS_FILENAME
    report_path = report_directory / report_filename

    write_csv(
        model_inventory_csv_path,
        [
            "dataset_id",
            "input_mode",
            "surface",
            "run_name",
            "run_instance_id",
            "dataset_schema",
            "archive_root",
            "source_validation_summary_path",
            "selected_component_count",
        ],
        model_inventory_row_list,
    )
    write_csv(
        component_inventory_csv_path,
        [
            "dataset_id",
            "input_mode",
            "surface",
            "target_name",
            "target_kind",
            "harmonic_order",
            "family_name",
            "estimator_name",
            "onnx_model_path",
            "python_model_path",
            "reference_inventory_path",
        ],
        component_inventory_row_list,
    )
    write_csv(
        per_curve_metrics_csv_path,
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
            "mse",
            "mae",
            "rmse",
            "mean_percentage_error_pct",
            "signed_mean_offset_deg",
            "absolute_mean_offset_deg",
            "peak_to_peak_error_deg",
            "centered_mae_deg",
            "centered_rmse_deg",
        ],
        per_curve_metric_row_list,
    )
    summary_dictionary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "model_family": "rcim_track1",
        "report_path": format_project_path(report_path),
        "output_directory": format_project_path(output_directory),
        "summary_path": format_project_path(summary_path),
        "model_inventory_csv_path": format_project_path(model_inventory_csv_path),
        "component_model_inventory_csv_path": format_project_path(component_inventory_csv_path),
        "per_curve_metrics_csv_path": format_project_path(per_curve_metrics_csv_path),
        "curves_per_page": curves_per_page,
        "provider_list": provider_list,
        "h0_sign_convention": "forward=-1, backward=+1",
        "group_summary_list": group_summary_list,
    }
    save_yaml_dictionary(summary_path, summary_dictionary)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        build_report_markdown(
            report_path,
            output_directory,
            summary_path,
            model_inventory_csv_path,
            component_inventory_csv_path,
            per_curve_metrics_csv_path,
            group_summary_list,
            curves_per_page,
        ),
        encoding="utf-8",
    )
    print(f"[DONE] RCIM Track1 familywise report: {format_project_path(report_path)}")
    print(f"[DONE] Artifacts: {format_project_path(output_directory)}")
    return summary_dictionary


def component_inventory_csv_path_placeholder(output_directory: Path) -> Path:

    """Return the component inventory path before the file is written."""

    return output_directory / COMPONENT_MODEL_INVENTORY_FILENAME


def main() -> None:

    """Run the command-line entry point."""

    run_familywise_rcim_track1_report(build_argument_parser().parse_args())


if __name__ == "__main__":
    main()
