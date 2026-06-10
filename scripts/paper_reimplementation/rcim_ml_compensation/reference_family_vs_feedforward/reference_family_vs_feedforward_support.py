"""Support utilities for Track 2 reference-family vs feedforward comparison."""

from __future__ import annotations

# Import Python Utilities
import csv
import pickle
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import numpy as np
import pandas as pd
import yaml

# Import PyTorch Utilities
import torch

# Import Project Utilities
from scripts.datasets import transmission_error_dataset
from scripts.models.model_factory import create_model
from scripts.paper_reimplementation.rcim_ml_compensation.harmonic_wise_comparison import harmonic_wise_support
from scripts.training import shared_training_infrastructure
from scripts.training import tree_regression_support
from scripts.training.transmission_error_regression_module import TransmissionErrorRegressionModule

COMPARISON_REPORT_ROOT = (
    shared_training_infrastructure.PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "validation_checks"
    / "track2"
)
COMPARISON_REPORT_TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"
CANONICAL_TRACK2_REPORT_PATH = (
    shared_training_infrastructure.PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "Track 2 Directional Model Comparison.md"
)
REFERENCE_CANDIDATE_KIND_SET = {
    "track1_reference_bank",
    "composite_reference_bank",
}
TEMPORAL_SEQUENCE_MODEL_TYPE_SET = {
    "temporal_convolution",
    "gru_sequence",
    "lstm_sequence",
    "periodic_temporal_convolution",
    "periodic_gru_sequence",
    "periodic_lstm_sequence",
    "residual_harmonic_gru_sequence",
    "residual_harmonic_lstm_sequence",
    "sequential_residual_offset_probe",
    "harmonic_residual_offset_probe",
    "curve_aware_harmonic_residual_offset_probe",
}
REFERENCE_BANK_PREDICTION_BATCH_SIZE = 64
TEMPORAL_SEQUENCE_INFERENCE_BATCH_SIZE = 2048


@dataclass(frozen=True)
class ReferenceModelEntry:

    """One archived reference target model from the curated family inventory."""

    target_name: str
    target_kind: str
    harmonic_order: int
    python_model_path: Path
    feature_name_list: list[str]


@dataclass(frozen=True)
class Track2Candidate:

    """One model candidate in the direction-aware Track 2 comparison matrix."""

    candidate_id: str
    candidate_family: str
    candidate_kind: str
    candidate_source_label: str
    candidate_surface: str
    allowed_direction_list: list[str]
    source_path: Path
    selected_harmonic_list: list[int]
    model_entry_list: list[ReferenceModelEntry] | None
    model_dictionary: dict[str, Any] | None
    registry_entry: dict[str, Any] | None
    training_config: dict[str, Any] | None
    model_object: Any | None


def load_reference_family_comparison_config(config_path: str | Path) -> dict[str, Any]:

    """Load one Track 2 reference-family comparison configuration file."""

    return shared_training_infrastructure.load_training_config(config_path)


def load_yaml_dictionary(yaml_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        loaded_dictionary = yaml.safe_load(yaml_file)
    assert isinstance(loaded_dictionary, dict), f"Expected YAML dictionary | {yaml_path}"
    return loaded_dictionary


def build_comparison_report_path(training_config: dict[str, Any]) -> Path:

    """Build the canonical Markdown report path for one comparison run."""

    report_timestamp = datetime.now().strftime(COMPARISON_REPORT_TIMESTAMP_FORMAT)
    run_name = shared_training_infrastructure.sanitize_name(
        shared_training_infrastructure.resolve_output_run_name(training_config)
    )
    return COMPARISON_REPORT_ROOT / f"{report_timestamp}_{run_name}_report.md"


def build_canonical_track2_report_path(training_config: dict[str, Any]) -> Path:

    """Resolve the stable Track 2 report path for canonical full-matrix runs."""

    configured_report_path = training_config.get("comparison", {}).get("canonical_report_path")
    if configured_report_path is None:
        return CANONICAL_TRACK2_REPORT_PATH
    return shared_training_infrastructure.resolve_runtime_project_relative_path(configured_report_path)


def load_reference_inventory(reference_inventory_path: str | Path) -> dict[str, Any]:

    """Load one curated Track 1 family reference inventory."""

    resolved_inventory_path = shared_training_infrastructure.resolve_runtime_project_relative_path(reference_inventory_path)
    assert resolved_inventory_path.exists(), f"Reference Inventory Path does not exist | {resolved_inventory_path}"
    return load_yaml_dictionary(resolved_inventory_path)


def resolve_selected_harmonic_list(reference_inventory: dict[str, Any]) -> list[int]:

    """Resolve the harmonic orders covered by the curated reference inventory."""

    archive_scope = reference_inventory["archive_scope"]
    if isinstance(archive_scope, dict):
        amplitude_harmonic_order_list = [
            int(harmonic_order)
            for harmonic_order in archive_scope["amplitude_harmonic_order_list"]
        ]
        phase_harmonic_order_list = [
            int(harmonic_order)
            for harmonic_order in archive_scope["phase_harmonic_order_list"]
        ]
    else:
        amplitude_harmonic_order_list = [
            int(reference_entry["harmonic_order"])
            for reference_entry in reference_inventory["reference_models"]
            if str(reference_entry["target_kind"]).strip().lower() == "amplitude"
        ]
        phase_harmonic_order_list = [
            int(reference_entry["harmonic_order"])
            for reference_entry in reference_inventory["reference_models"]
            if str(reference_entry["target_kind"]).strip().lower() == "phase"
        ]
    selected_harmonic_list = sorted(set(amplitude_harmonic_order_list) | set(phase_harmonic_order_list))
    assert selected_harmonic_list and selected_harmonic_list[0] == 0, "Reference bank must include harmonic 0"
    return selected_harmonic_list


def load_reference_model_entries(reference_inventory: dict[str, Any]) -> list[ReferenceModelEntry]:

    """Load and validate the reference target-model inventory entries."""

    reference_model_entry_list: list[ReferenceModelEntry] = []
    for reference_entry in reference_inventory["reference_models"]:
        python_model_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
            reference_entry["python_model_path"]
        )
        reference_model_entry_list.append(
            ReferenceModelEntry(
                target_name=str(reference_entry["target_name"]),
                target_kind=str(reference_entry["target_kind"]).strip().lower(),
                harmonic_order=int(reference_entry["harmonic_order"]),
                python_model_path=python_model_path,
                feature_name_list=[str(feature_name) for feature_name in reference_entry["feature_name_list"]],
            )
        )

    assert reference_model_entry_list, "Reference inventory produced no model entries"
    return reference_model_entry_list


def find_reference_model_entry(
    reference_model_entry_list: list[ReferenceModelEntry],
    target_kind: str,
    harmonic_order: int,
) -> ReferenceModelEntry:

    """Find one target entry in a reference inventory."""

    normalized_target_kind = str(target_kind).strip().lower()
    matching_entry_list = [
        reference_entry
        for reference_entry in reference_model_entry_list
        if reference_entry.target_kind == normalized_target_kind
        and reference_entry.harmonic_order == int(harmonic_order)
    ]
    assert len(matching_entry_list) == 1, (
        "Expected exactly one reference target entry | "
        f"target_kind={normalized_target_kind} | harmonic_order={harmonic_order}"
    )
    return matching_entry_list[0]


def load_reference_model_dictionary(reference_model_entry_list: list[ReferenceModelEntry]) -> dict[str, Any]:

    """Load the archived Python estimators for one curated reference bank."""

    reference_model_dictionary: dict[str, Any] = {}
    for reference_entry in reference_model_entry_list:
        with reference_entry.python_model_path.open("rb") as model_file:
            reference_model_dictionary[reference_entry.target_name] = pickle.load(model_file)
    return reference_model_dictionary


def resolve_feedforward_best_entry(feedforward_leaderboard_path: str | Path) -> dict[str, Any]:

    """Resolve the current canonical best feedforward registry entry."""

    leaderboard_dictionary = load_yaml_dictionary(
        shared_training_infrastructure.resolve_runtime_project_relative_path(feedforward_leaderboard_path)
    )
    entry_list = leaderboard_dictionary["entry_list"]
    assert isinstance(entry_list, list) and entry_list, "Feedforward leaderboard entry_list is empty"
    best_entry = entry_list[0]
    assert str(best_entry["model_family"]).strip().lower() == "feedforward", "Unexpected best-entry family"
    return best_entry


def resolve_family_best_entry(registry_path: str | Path) -> dict[str, Any]:

    """Resolve one family-best registry entry from a registry YAML file."""

    registry_dictionary = load_yaml_dictionary(
        shared_training_infrastructure.resolve_runtime_project_relative_path(registry_path)
    )
    if "best_entry" in registry_dictionary:
        best_entry = registry_dictionary["best_entry"]
    else:
        entry_list = registry_dictionary["entry_list"]
        assert isinstance(entry_list, list) and entry_list, f"Registry entry_list is empty | {registry_path}"
        best_entry = entry_list[0]
    assert isinstance(best_entry, dict), f"Registry best entry must be a dictionary | {registry_path}"
    return best_entry


def load_lightning_regression_module_for_inference(
    checkpoint_path: Path,
    training_config: dict[str, Any],
) -> TransmissionErrorRegressionModule:

    """Load one Lightning TE checkpoint without constructing the full datamodule."""

    inference_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    checkpoint_dictionary = torch.load(checkpoint_path, map_location=torch.device("cpu"), weights_only=False)
    hyperparameter_dictionary = checkpoint_dictionary.get("hyper_parameters", {})
    input_feature_dim = int(
        hyperparameter_dictionary.get(
            "input_feature_dim",
            training_config.get("model", {}).get("input_size", 5),
        )
    )
    target_feature_dim = int(hyperparameter_dictionary.get("target_feature_dim", 1))
    del checkpoint_dictionary

    regression_module = TransmissionErrorRegressionModule.load_from_checkpoint(
        checkpoint_path=checkpoint_path,
        regression_model=create_model(
            model_type=str(training_config["experiment"]["model_type"]),
            model_configuration=training_config["model"],
        ),
        input_feature_dim=input_feature_dim,
        target_feature_dim=target_feature_dim,
        normalization_statistics=None,
        map_location=torch.device("cpu"),
    )
    regression_module.normalization_statistics_initialized = True
    regression_module.to(inference_device)
    regression_module.eval()
    return regression_module


def load_feedforward_regression_module(feedforward_best_entry: dict[str, Any]) -> tuple[TransmissionErrorRegressionModule, dict[str, Any]]:

    """Load the canonical best feedforward checkpoint plus its config snapshot."""

    output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(
        feedforward_best_entry["output_directory"]
    )
    training_config_path = output_directory / shared_training_infrastructure.COMMON_TRAINING_CONFIG_FILENAME
    training_config = shared_training_infrastructure.load_training_config(training_config_path)
    best_checkpoint_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        feedforward_best_entry["best_checkpoint_path"]
    )
    return (
        load_lightning_regression_module_for_inference(
            best_checkpoint_path,
            training_config,
        ),
        training_config,
    )


def load_wave1_registry_model(registry_entry: dict[str, Any]) -> tuple[Any, dict[str, Any]]:

    """Load one Wave 1 registry-backed model artifact."""

    output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(
        registry_entry["output_directory"]
    )
    training_config_path = output_directory / shared_training_infrastructure.COMMON_TRAINING_CONFIG_FILENAME
    training_config = shared_training_infrastructure.load_training_config(training_config_path)
    model_type = str(registry_entry["model_type"]).strip().lower()
    if model_type in {"hist_gradient_boosting", "random_forest"}:
        model_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
            registry_entry["best_checkpoint_path"]
        )
        return tree_regression_support.load_tree_model(model_path), training_config

    best_checkpoint_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        registry_entry["best_checkpoint_path"]
    )
    return (
        load_lightning_regression_module_for_inference(
            best_checkpoint_path,
            training_config,
        ),
        training_config,
    )


def load_wave1_exported_model(export_inventory: dict[str, Any]) -> tuple[Any, dict[str, Any]]:

    """Load one Wave 1 exported model directly from the `models/` tree."""

    source_run_snapshot_path_map = export_inventory["source_run_snapshot_path_map"]
    training_config_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        source_run_snapshot_path_map["training_config.snapshot.yaml"]
    )
    training_config = shared_training_infrastructure.load_training_config(training_config_path)
    model_type = str(export_inventory["model_type"]).strip().lower()
    model_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        export_inventory["python_model_path"]
    )

    if model_type in {"hist_gradient_boosting", "random_forest"}:
        return tree_regression_support.load_tree_model(model_path), training_config

    return (
        load_lightning_regression_module_for_inference(
            model_path,
            training_config,
        ),
        training_config,
    )


def build_curve_record_list(
    training_config: dict[str, Any],
    selected_harmonic_list: list[int],
) -> tuple[list[harmonic_wise_support.HarmonicCurveRecord], dict[str, int], dict[str, int], Path]:

    """Build the held-out TE-curve record list used by the comparison."""

    if bool(training_config.get("comparison", {}).get("lightweight_test_curve_records", False)):
        dataset_configuration = transmission_error_dataset.load_dataset_processing_config(
            training_config["paths"]["dataset_config_path"]
        )
        dataset_root = transmission_error_dataset.resolve_project_relative_path(
            dataset_configuration["paths"]["dataset_root"]
        )
        direction_configuration = dataset_configuration["directions"]
        split_configuration = dataset_configuration["split"]
        directional_file_manifest = transmission_error_dataset.build_directional_file_manifest(
            dataset_root=dataset_root,
            use_forward_direction=bool(direction_configuration["use_forward_direction"]),
            use_backward_direction=bool(direction_configuration["use_backward_direction"]),
        )
        train_manifest, validation_manifest, test_manifest = transmission_error_dataset.split_directional_file_manifest(
            directional_file_manifest,
            validation_split=float(split_configuration["validation_split"]),
            test_split=float(split_configuration["test_split"]),
            random_seed=int(split_configuration["random_seed"]),
        )
        curve_record_list = []
        for csv_file_path, direction_label in test_manifest:
            curve_sample = transmission_error_dataset.build_validated_directional_sample(
                csv_file_path.resolve(),
                direction_label,
            )
            curve_record_list.append(
                harmonic_wise_support.HarmonicCurveRecord(
                    source_file_path=curve_sample.source_file_path,
                    direction_label=curve_sample.direction_label,
                    direction_flag=float(curve_sample.direction_flag),
                    speed_rpm=float(curve_sample.speed_rpm),
                    torque_nm=float(curve_sample.torque_nm),
                    oil_temperature_deg=float(curve_sample.oil_temperature_deg),
                    angular_position_deg=curve_sample.angular_position_deg.astype(np.float32),
                    transmission_error_deg=curve_sample.transmission_error_deg.astype(np.float32),
                    coefficient_dictionary={},
                    amplitude_phase_dictionary={},
                )
            )
        directional_count_dictionary = {
            "train": len(train_manifest),
            "validation": len(validation_manifest),
            "test": len(test_manifest),
        }
        file_count_dictionary = {
            "train": len({csv_file_path for csv_file_path, _ in train_manifest}),
            "validation": len({csv_file_path for csv_file_path, _ in validation_manifest}),
            "test": len({csv_file_path for csv_file_path, _ in test_manifest}),
        }
        return curve_record_list, directional_count_dictionary, file_count_dictionary, dataset_root

    split_record_bundle, directional_count_dictionary, file_count_dictionary, dataset_root = (
        harmonic_wise_support.build_split_record_bundle(training_config)
    )
    return split_record_bundle["test"], directional_count_dictionary, file_count_dictionary, dataset_root


def build_reference_feature_matrix(curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord]) -> pd.DataFrame:

    """Build the reference-bank feature matrix aligned with the archived models."""

    return pd.DataFrame(
        data=[
            {
                "rpm": float(curve_record.speed_rpm),
                "deg": float(curve_record.oil_temperature_deg),
                "tor": float(curve_record.torque_nm),
            }
            for curve_record in curve_record_list
        ],
        columns=["rpm", "deg", "tor"],
    )


def predict_reference_model_in_batches(model_object: Any, reference_feature_matrix: pd.DataFrame) -> np.ndarray:

    """Predict one archived reference target with a bounded inference batch size."""

    prediction_array_list: list[np.ndarray] = []
    for batch_start_index in range(0, len(reference_feature_matrix), REFERENCE_BANK_PREDICTION_BATCH_SIZE):
        batch_feature_matrix = reference_feature_matrix.iloc[
            batch_start_index : batch_start_index + REFERENCE_BANK_PREDICTION_BATCH_SIZE
        ]
        prediction_array_list.append(
            np.asarray(
                model_object.predict(batch_feature_matrix),
                dtype=np.float32,
            ).reshape(-1)
        )

    return np.concatenate(prediction_array_list).reshape(-1)


def predict_reference_bank_target_dictionary(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    reference_model_entry_list: list[ReferenceModelEntry],
    reference_model_dictionary: dict[str, Any] | None,
) -> dict[str, np.ndarray]:

    """Predict all archived amplitude and phase targets for the held-out curves."""

    reference_feature_matrix = build_reference_feature_matrix(curve_record_list)
    predicted_target_dictionary: dict[str, np.ndarray] = {}
    for reference_entry in reference_model_entry_list:
        assert reference_entry.feature_name_list == ["rpm", "deg", "tor"], (
            "Unexpected reference feature schema | "
            f"{reference_entry.feature_name_list}"
        )
        if reference_model_dictionary is None:
            with reference_entry.python_model_path.open("rb") as model_file:
                reference_model_object = pickle.load(model_file)
        else:
            reference_model_object = reference_model_dictionary[reference_entry.target_name]
        predicted_target_dictionary[reference_entry.target_name] = predict_reference_model_in_batches(
            reference_model_object,
            reference_feature_matrix,
        )
        del reference_model_object
    return predicted_target_dictionary


def build_reference_coefficient_dictionary(
    predicted_target_dictionary: dict[str, np.ndarray],
    sample_index: int,
    selected_harmonic_list: list[int],
) -> tuple[dict[str, float], dict[str, float]]:

    """Convert one amplitude/phase prediction set into harmonic coefficients."""

    coefficient_dictionary: dict[str, float] = {}
    amplitude_phase_dictionary: dict[str, float] = {}

    for harmonic_order in selected_harmonic_list:
        amplitude_target_name = f"fft_y_Fw_filtered_ampl_{harmonic_order}"
        predicted_amplitude = float(predicted_target_dictionary[amplitude_target_name][sample_index])

        if harmonic_order == 0:
            coefficient_dictionary["coefficient_cos_h0"] = predicted_amplitude
            amplitude_phase_dictionary["amplitude_h0"] = abs(predicted_amplitude)
            amplitude_phase_dictionary["phase_rad_h0"] = 0.0
            continue

        phase_target_name = f"fft_y_Fw_filtered_phase_{harmonic_order}"
        predicted_phase = float(predicted_target_dictionary[phase_target_name][sample_index])
        coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"] = float(predicted_amplitude * np.cos(predicted_phase))
        coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"] = float(-predicted_amplitude * np.sin(predicted_phase))
        amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"] = float(predicted_amplitude)
        amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"] = float(predicted_phase)

    return coefficient_dictionary, amplitude_phase_dictionary


def build_reference_prediction_lookup(
    reference_model_entry_list: list[ReferenceModelEntry],
    predicted_target_dictionary: dict[str, np.ndarray],
) -> dict[tuple[str, int], np.ndarray]:

    """Build a target lookup keyed by target kind and harmonic order."""

    prediction_lookup: dict[tuple[str, int], np.ndarray] = {}
    for reference_entry in reference_model_entry_list:
        lookup_key = (reference_entry.target_kind, int(reference_entry.harmonic_order))
        prediction_lookup[lookup_key] = predicted_target_dictionary[reference_entry.target_name]
    return prediction_lookup


def build_reference_coefficient_dictionary_from_entries(
    prediction_lookup: dict[tuple[str, int], np.ndarray],
    sample_index: int,
    selected_harmonic_list: list[int],
    h0_sign_multiplier: float = 1.0,
) -> tuple[dict[str, float], dict[str, float]]:

    """Convert one generic Track 1 bank prediction into harmonic coefficients."""

    coefficient_dictionary: dict[str, float] = {}
    amplitude_phase_dictionary: dict[str, float] = {}

    for harmonic_order in selected_harmonic_list:
        predicted_amplitude = float(prediction_lookup[("amplitude", harmonic_order)][sample_index])

        if harmonic_order == 0:
            signed_amplitude = float(h0_sign_multiplier * predicted_amplitude)
            coefficient_dictionary["coefficient_cos_h0"] = signed_amplitude
            amplitude_phase_dictionary["amplitude_h0"] = abs(signed_amplitude)
            amplitude_phase_dictionary["phase_rad_h0"] = 0.0
            continue

        predicted_phase = float(prediction_lookup[("phase", harmonic_order)][sample_index])
        coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"] = float(
            predicted_amplitude * np.cos(predicted_phase)
        )
        coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"] = float(
            -predicted_amplitude * np.sin(predicted_phase)
        )
        amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"] = float(predicted_amplitude)
        amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"] = float(predicted_phase)

    return coefficient_dictionary, amplitude_phase_dictionary


def resolve_reference_h0_sign_multiplier(candidate: Track2Candidate) -> float:

    """Resolve source-specific `h0` sign compatibility for reference banks."""

    if candidate.candidate_source_label == "rcim_track1" and candidate.candidate_surface == "Fw":
        return -1.0
    return 1.0


def build_reference_target_metric_dictionary(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    predicted_target_dictionary: dict[str, np.ndarray],
    selected_harmonic_list: list[int],
) -> dict[str, float]:

    """Build compact amplitude and phase diagnostics for the archived bank."""

    amplitude_error_list: list[float] = []
    phase_error_list: list[float] = []

    for sample_index, curve_record in enumerate(curve_record_list):
        for harmonic_order in selected_harmonic_list:
            amplitude_target_name = f"fft_y_Fw_filtered_ampl_{harmonic_order}"
            truth_amplitude = float(curve_record.amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"])
            predicted_amplitude = float(predicted_target_dictionary[amplitude_target_name][sample_index])
            amplitude_error_list.append(abs(predicted_amplitude - truth_amplitude))

            if harmonic_order == 0:
                continue

            phase_target_name = f"fft_y_Fw_filtered_phase_{harmonic_order}"
            truth_phase = float(curve_record.amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"])
            predicted_phase = float(predicted_target_dictionary[phase_target_name][sample_index])
            wrapped_phase_error = abs(harmonic_wise_support.wrap_phase_difference_radians(predicted_phase - truth_phase))
            phase_error_list.append(float(wrapped_phase_error))

    return {
        "amplitude_mae": float(np.mean(amplitude_error_list)),
        "amplitude_rmse": float(np.sqrt(np.mean(np.square(amplitude_error_list)))),
        "phase_mae_rad": float(np.mean(phase_error_list)) if phase_error_list else 0.0,
        "phase_rmse_rad": float(np.sqrt(np.mean(np.square(phase_error_list)))) if phase_error_list else 0.0,
    }


def build_reference_target_metric_dictionary_from_entries(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    reference_model_entry_list: list[ReferenceModelEntry],
    predicted_target_dictionary: dict[str, np.ndarray],
    selected_harmonic_list: list[int],
) -> dict[str, float]:

    """Build target diagnostics for a generic forward or backward reference bank."""

    prediction_lookup = build_reference_prediction_lookup(reference_model_entry_list, predicted_target_dictionary)
    amplitude_error_list: list[float] = []
    phase_error_list: list[float] = []

    for sample_index, curve_record in enumerate(curve_record_list):
        for harmonic_order in selected_harmonic_list:
            truth_amplitude = float(curve_record.amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"])
            predicted_amplitude = float(prediction_lookup[("amplitude", harmonic_order)][sample_index])
            amplitude_error_list.append(abs(predicted_amplitude - truth_amplitude))

            if harmonic_order == 0:
                continue

            truth_phase = float(curve_record.amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"])
            predicted_phase = float(prediction_lookup[("phase", harmonic_order)][sample_index])
            wrapped_phase_error = abs(harmonic_wise_support.wrap_phase_difference_radians(predicted_phase - truth_phase))
            phase_error_list.append(float(wrapped_phase_error))

    return {
        "amplitude_mae": float(np.mean(amplitude_error_list)),
        "amplitude_rmse": float(np.sqrt(np.mean(np.square(amplitude_error_list)))),
        "phase_mae_rad": float(np.mean(phase_error_list)) if phase_error_list else 0.0,
        "phase_rmse_rad": float(np.sqrt(np.mean(np.square(phase_error_list)))) if phase_error_list else 0.0,
    }


def build_feedforward_input_tensor(curve_record: harmonic_wise_support.HarmonicCurveRecord) -> torch.Tensor:

    """Build the pointwise feedforward input tensor for one curve record."""

    sequence_length = int(curve_record.angular_position_deg.shape[0])
    input_feature_matrix = np.column_stack(
        [
            curve_record.angular_position_deg.astype(np.float32),
            np.full(sequence_length, curve_record.speed_rpm, dtype=np.float32),
            np.full(sequence_length, curve_record.torque_nm, dtype=np.float32),
            np.full(sequence_length, curve_record.oil_temperature_deg, dtype=np.float32),
            np.full(sequence_length, curve_record.direction_flag, dtype=np.float32),
        ]
    ).astype(np.float32)
    return torch.from_numpy(input_feature_matrix)


def build_temporal_sequence_input_tensor(
    curve_record: harmonic_wise_support.HarmonicCurveRecord,
    training_config: dict[str, Any],
) -> torch.Tensor:

    """Build full-curve sequence windows for one temporal registry model."""

    point_input_tensor = build_feedforward_input_tensor(curve_record).float()
    dataset_configuration = training_config.get("dataset", {})
    sequence_length = int(dataset_configuration.get("sequence_length", 1))
    sequence_target_position = str(dataset_configuration.get("sequence_target_position", "center")).strip().lower()

    assert sequence_length > 0, f"Sequence Length must be positive | {sequence_length}"
    assert sequence_target_position in {"center", "last"}, (
        f"Unsupported Sequence Target Position | {sequence_target_position}"
    )

    if sequence_target_position == "center":
        assert sequence_length % 2 == 1, (
            "Center-readout full-curve evaluation requires an odd sequence length | "
            f"{sequence_length}"
        )
        left_padding_count = sequence_length // 2
        right_padding_count = sequence_length // 2
    else:
        left_padding_count = sequence_length - 1
        right_padding_count = 0

    feature_count = int(point_input_tensor.shape[1])
    empty_padding_tensor = point_input_tensor.new_empty((0, feature_count))
    left_padding_tensor = (
        point_input_tensor[:1].repeat(left_padding_count, 1)
        if left_padding_count > 0
        else empty_padding_tensor
    )
    right_padding_tensor = (
        point_input_tensor[-1:].repeat(right_padding_count, 1)
        if right_padding_count > 0
        else empty_padding_tensor
    )
    padded_input_tensor = torch.cat(
        [left_padding_tensor, point_input_tensor, right_padding_tensor],
        dim=0,
    )
    sequence_window_list = [
        padded_input_tensor[start_index:start_index + sequence_length]
        for start_index in range(int(point_input_tensor.shape[0]))
    ]
    return torch.stack(sequence_window_list, dim=0)


def predict_temporal_sequence_curve_in_batches(
    model_object: TransmissionErrorRegressionModule,
    curve_record: harmonic_wise_support.HarmonicCurveRecord,
    training_config: dict[str, Any],
) -> np.ndarray:

    """Predict one temporal TE curve without materializing every sequence window at once."""

    inference_device = model_object.input_feature_mean.device
    point_input_tensor = build_feedforward_input_tensor(curve_record).float().to(inference_device)
    dataset_configuration = training_config.get("dataset", {})
    sequence_length = int(dataset_configuration.get("sequence_length", 1))
    sequence_target_position = str(dataset_configuration.get("sequence_target_position", "center")).strip().lower()

    assert sequence_length > 0, f"Sequence Length must be positive | {sequence_length}"
    assert sequence_target_position in {"center", "last"}, (
        f"Unsupported Sequence Target Position | {sequence_target_position}"
    )

    if sequence_target_position == "center":
        assert sequence_length % 2 == 1, (
            "Center-readout full-curve evaluation requires an odd sequence length | "
            f"{sequence_length}"
        )
        left_padding_count = sequence_length // 2
        right_padding_count = sequence_length // 2
    else:
        left_padding_count = sequence_length - 1
        right_padding_count = 0

    feature_count = int(point_input_tensor.shape[1])
    empty_padding_tensor = point_input_tensor.new_empty((0, feature_count))
    left_padding_tensor = (
        point_input_tensor[:1].repeat(left_padding_count, 1)
        if left_padding_count > 0
        else empty_padding_tensor
    )
    right_padding_tensor = (
        point_input_tensor[-1:].repeat(right_padding_count, 1)
        if right_padding_count > 0
        else empty_padding_tensor
    )
    padded_input_tensor = torch.cat(
        [left_padding_tensor, point_input_tensor, right_padding_tensor],
        dim=0,
    )
    prediction_tensor_list: list[torch.Tensor] = []

    with torch.no_grad():
        for batch_start_index in range(0, int(point_input_tensor.shape[0]), TEMPORAL_SEQUENCE_INFERENCE_BATCH_SIZE):
            batch_end_index = min(
                batch_start_index + TEMPORAL_SEQUENCE_INFERENCE_BATCH_SIZE,
                int(point_input_tensor.shape[0]),
            )
            sequence_window_list = [
                padded_input_tensor[start_index:start_index + sequence_length]
                for start_index in range(batch_start_index, batch_end_index)
            ]
            input_tensor = torch.stack(sequence_window_list, dim=0)
            normalized_input_tensor = model_object.normalize_input_tensor(input_tensor)
            normalized_prediction_tensor, _ = model_object.forward_regression_model(
                input_tensor,
                normalized_input_tensor,
            )
            predicted_curve_tensor = model_object.denormalize_target_tensor(normalized_prediction_tensor)
            prediction_tensor_list.append(predicted_curve_tensor.detach().cpu())

    return torch.cat(prediction_tensor_list, dim=0).numpy().reshape(-1).astype(np.float32)


def predict_feedforward_curve(
    regression_module: TransmissionErrorRegressionModule,
    curve_record: harmonic_wise_support.HarmonicCurveRecord,
) -> np.ndarray:

    """Predict one TE curve with the canonical feedforward checkpoint."""

    inference_device = regression_module.input_feature_mean.device
    input_tensor = build_feedforward_input_tensor(curve_record).float().to(inference_device)
    with torch.no_grad():
        normalized_input_tensor = regression_module.normalize_input_tensor(input_tensor)
        normalized_prediction_tensor, _ = regression_module.forward_regression_model(
            input_tensor,
            normalized_input_tensor,
        )
        predicted_curve_tensor = regression_module.denormalize_target_tensor(normalized_prediction_tensor)
    return predicted_curve_tensor.detach().cpu().numpy().reshape(-1).astype(np.float32)


def predict_wave1_registry_curve(
    model_object: Any,
    training_config: dict[str, Any],
    curve_record: harmonic_wise_support.HarmonicCurveRecord,
) -> np.ndarray:

    """Predict one TE curve with a loaded registry-backed model."""

    model_type = str(training_config["experiment"]["model_type"]).strip().lower()
    if model_type in {"hist_gradient_boosting", "random_forest"}:
        input_tensor = build_feedforward_input_tensor(curve_record).float()
        input_feature_matrix = input_tensor.detach().cpu().numpy().astype(np.float32)
        return np.asarray(model_object.predict(input_feature_matrix), dtype=np.float32).reshape(-1)

    assert isinstance(model_object, TransmissionErrorRegressionModule), (
        f"Expected TransmissionErrorRegressionModule | {model_type}"
    )
    if model_type in TEMPORAL_SEQUENCE_MODEL_TYPE_SET:
        return predict_temporal_sequence_curve_in_batches(
            model_object,
            curve_record,
            training_config,
        )
    else:
        input_tensor = build_feedforward_input_tensor(curve_record).float().to(model_object.input_feature_mean.device)

    with torch.no_grad():
        normalized_input_tensor = model_object.normalize_input_tensor(input_tensor)
        normalized_prediction_tensor, _ = model_object.forward_regression_model(
            input_tensor,
            normalized_input_tensor,
        )
        predicted_curve_tensor = model_object.denormalize_target_tensor(normalized_prediction_tensor)
    return predicted_curve_tensor.detach().cpu().numpy().reshape(-1).astype(np.float32)


def normalize_allowed_direction_list(candidate_configuration: dict[str, Any]) -> list[str]:

    """Resolve allowed evaluation directions for one candidate configuration."""

    if "allowed_direction_list" in candidate_configuration:
        raw_direction_list = candidate_configuration["allowed_direction_list"]
    elif "allowed_directions" in candidate_configuration:
        raw_direction_list = candidate_configuration["allowed_directions"]
    else:
        candidate_surface = str(candidate_configuration["candidate_surface"]).strip()
        if candidate_surface == "Fw":
            raw_direction_list = ["forward"]
        elif candidate_surface == "Bw":
            raw_direction_list = ["backward"]
        else:
            raw_direction_list = ["forward", "backward"]

    direction_list = [str(direction_label).strip().lower() for direction_label in raw_direction_list]
    unsupported_direction_list = sorted(set(direction_list) - {"forward", "backward"})
    assert not unsupported_direction_list, (
        "Unsupported Track 2 candidate evaluation directions | "
        f"{', '.join(unsupported_direction_list)}"
    )
    assert direction_list, "Track 2 candidate must have at least one allowed direction"
    return direction_list


def build_legacy_candidate_configuration_list(training_config: dict[str, Any]) -> list[dict[str, Any]]:

    """Build candidate configurations for the historical single-bank config."""

    return [
        {
            "candidate_id": "lgbm19_reference_bank",
            "candidate_family": "LGBM",
            "candidate_kind": "track1_reference_bank",
            "candidate_surface": "global",
            "reference_inventory_path": training_config["paths"]["reference_inventory_path"],
            "allowed_direction_list": ["forward", "backward"],
        },
        {
            "candidate_id": "feedforward_best",
            "candidate_family": "feedforward",
            "candidate_kind": "wave1_registry_model",
            "candidate_surface": "global",
            "family_registry_path": training_config["paths"]["feedforward_leaderboard_path"],
            "allowed_direction_list": ["forward", "backward"],
        },
    ]


def build_reference_family_folder_lookup(family_configuration_list: list[dict[str, Any]]) -> dict[str, str]:

    """Build a paper-family to archive-folder lookup from compact config rows."""

    family_folder_lookup: dict[str, str] = {}
    for family_configuration in family_configuration_list:
        family_id = str(family_configuration["family_id"]).strip()
        archive_folder = str(family_configuration["archive_folder"]).strip()
        family_folder_lookup[family_id] = archive_folder
    return family_folder_lookup


def build_composite_reference_candidate_configuration_list(
    generation_configuration: dict[str, Any],
) -> list[dict[str, Any]]:

    """Build configured composed reference-bank candidates."""

    composite_configuration = generation_configuration.get("composite_reference_models", {})
    if not composite_configuration:
        return []

    family_folder_lookup = build_reference_family_folder_lookup(composite_configuration["family_list"])
    candidate_configuration_list: list[dict[str, Any]] = []
    for composite_candidate in composite_configuration["candidate_list"]:
        archive_root = str(composite_candidate["archive_root"]).rstrip("/")
        candidate_configuration_list.append(
            {
                "candidate_id": str(composite_candidate["candidate_id"]).strip(),
                "candidate_family": str(composite_candidate["candidate_family"]).strip(),
                "candidate_kind": "composite_reference_bank",
                "candidate_source_label": str(composite_candidate["candidate_source_label"]).strip(),
                "candidate_surface": str(composite_candidate["candidate_surface"]).strip(),
                "archive_root": archive_root,
                "family_folder_lookup": dict(family_folder_lookup),
                "amplitude_family_by_harmonic": {
                    str(harmonic_order): str(family_id).strip()
                    for harmonic_order, family_id in composite_candidate["amplitude_family_by_harmonic"].items()
                },
                "phase_family_by_harmonic": {
                    str(harmonic_order): str(family_id).strip()
                    for harmonic_order, family_id in composite_candidate["phase_family_by_harmonic"].items()
                },
                "allowed_direction_list": [str(direction_label).strip().lower() for direction_label in composite_candidate["allowed_direction_list"]],
            }
        )
    return candidate_configuration_list


def build_registry_candidate_configuration_list(
    registry_group_configuration: dict[str, Any],
    default_source_label: str,
) -> list[dict[str, Any]]:

    """Generate registry-backed Track 2 candidates from compact family metadata."""

    family_registry_root = str(registry_group_configuration["family_registry_root"]).rstrip("/")
    source_label = str(registry_group_configuration.get("source_label", default_source_label)).strip()
    candidate_configuration_list: list[dict[str, Any]] = []

    for family_configuration in registry_group_configuration["base_family_list"]:
        if isinstance(family_configuration, dict):
            candidate_id_prefix = str(family_configuration["candidate_id_prefix"]).strip()
            candidate_family = str(family_configuration.get("candidate_family", candidate_id_prefix)).strip()
            surface_family_dictionary = {
                "global": str(family_configuration["global_family"]).strip(),
                "Fw": str(family_configuration["fw_family"]).strip(),
                "Bw": str(family_configuration["bw_family"]).strip(),
            }
        else:
            candidate_id_prefix = str(family_configuration).strip()
            candidate_family = candidate_id_prefix
            surface_family_dictionary = {
                "global": candidate_id_prefix,
                "Fw": f"{candidate_id_prefix}_fw",
                "Bw": f"{candidate_id_prefix}_bw",
            }

        for candidate_surface, allowed_direction_list in [
            ("global", ["forward", "backward"]),
            ("Fw", ["forward"]),
            ("Bw", ["backward"]),
        ]:
            registry_family_name = surface_family_dictionary[candidate_surface]
            candidate_configuration_list.append(
                {
                    "candidate_id": f"{candidate_id_prefix}_{candidate_surface}",
                    "candidate_family": candidate_family,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": source_label,
                    "candidate_surface": candidate_surface,
                    "family_registry_path": (
                        f"{family_registry_root}/{registry_family_name}/latest_family_best.yaml"
                    ),
                    "allowed_direction_list": allowed_direction_list,
                }
            )

    return candidate_configuration_list


def build_generated_candidate_configuration_list(training_config: dict[str, Any]) -> list[dict[str, Any]]:

    """Generate a full Track 2 candidate matrix from compact config metadata."""

    generation_configuration = training_config["comparison"]["candidate_generation"]
    candidate_configuration_list: list[dict[str, Any]] = []

    track1_configuration = generation_configuration.get("track1_reference_banks", {})
    if track1_configuration:
        forward_archive_root = str(track1_configuration["forward_archive_root"]).rstrip("/")
        backward_archive_root = str(track1_configuration["backward_archive_root"]).rstrip("/")
        for family_configuration in track1_configuration["family_list"]:
            family_id = str(family_configuration["family_id"]).strip()
            family_label = str(family_configuration["family_label"]).strip()
            archive_folder = str(family_configuration["archive_folder"]).strip()
            candidate_configuration_list.append(
                {
                    "candidate_id": f"{family_id}19_Fw",
                    "candidate_family": family_label,
                    "candidate_kind": "track1_reference_bank",
                    "candidate_source_label": "rcim_track1",
                    "candidate_surface": "Fw",
                    "reference_inventory_path": (
                        f"{forward_archive_root}/{archive_folder}/reference_inventory.yaml"
                    ),
                    "allowed_direction_list": ["forward"],
                }
            )
            candidate_configuration_list.append(
                {
                    "candidate_id": f"{family_id}19_Bw",
                    "candidate_family": family_label,
                    "candidate_kind": "track1_reference_bank",
                    "candidate_source_label": "rcim_track1",
                    "candidate_surface": "Bw",
                    "reference_inventory_path": (
                        f"{backward_archive_root}/{archive_folder}/reference_inventory.yaml"
                    ),
                    "allowed_direction_list": ["backward"],
                }
            )

    paper_reference_group_list = generation_configuration.get("paper_reference_archive_groups", [])
    for paper_reference_group in paper_reference_group_list:
        source_label = str(paper_reference_group["source_label"]).strip()
        for direction_configuration in paper_reference_group["direction_list"]:
            direction_label = str(direction_configuration["direction_label"]).strip().lower()
            candidate_surface = str(direction_configuration["candidate_surface"]).strip()
            archive_root = str(direction_configuration["archive_root"]).rstrip("/")
            allowed_direction_list = [direction_label]
            for family_configuration in paper_reference_group["family_list"]:
                family_id = str(family_configuration["family_id"]).strip()
                family_label = str(family_configuration["family_label"]).strip()
                archive_folder = str(family_configuration["archive_folder"]).strip()
                candidate_configuration_list.append(
                    {
                        "candidate_id": f"{source_label}_{family_id}19_{candidate_surface}",
                        "candidate_family": family_label,
                        "candidate_kind": "track1_reference_bank",
                        "candidate_source_label": source_label,
                        "candidate_surface": candidate_surface,
                        "reference_inventory_path": f"{archive_root}/{archive_folder}/reference_inventory.yaml",
                        "allowed_direction_list": allowed_direction_list,
                    }
                )

    wave1_configuration = generation_configuration.get("wave1_registry_models", {})
    if wave1_configuration:
        candidate_configuration_list.extend(
            build_registry_candidate_configuration_list(wave1_configuration, "wave1")
        )

    wave2_configuration = generation_configuration.get("wave2_registry_models", {})
    if wave2_configuration:
        candidate_configuration_list.extend(
            build_registry_candidate_configuration_list(wave2_configuration, "wave2_temporal_entry_registry")
        )

    wave2c_configuration = generation_configuration.get("wave2c_registry_models", {})
    if wave2c_configuration:
        candidate_configuration_list.extend(
            build_registry_candidate_configuration_list(
                wave2c_configuration,
                "wave2c_residual_harmonic_temporal_registry",
            )
        )

    track2f_configuration = generation_configuration.get("track2f_registry_models", {})
    if track2f_configuration:
        candidate_configuration_list.extend(
            build_registry_candidate_configuration_list(
                track2f_configuration,
                "track2f_offset_aware_probe_registry",
            )
        )

    track2f_bis_configuration = generation_configuration.get("track2f_bis_registry_models", {})
    if track2f_bis_configuration:
        candidate_configuration_list.extend(
            build_registry_candidate_configuration_list(
                track2f_bis_configuration,
                "track2f_bis_harmonic_offset_probe_registry",
            )
        )

    track2g_configuration = generation_configuration.get("track2g_registry_models", {})
    if track2g_configuration:
        candidate_configuration_list.extend(
            build_registry_candidate_configuration_list(
                track2g_configuration,
                "track2g_curve_aware_training_registry",
            )
        )

    wave1_export_configuration = generation_configuration.get("wave1_exported_models", {})
    if wave1_export_configuration:
        exported_model_root = str(wave1_export_configuration["exported_model_root"]).rstrip("/")
        for base_family in wave1_export_configuration["base_family_list"]:
            base_family_name = str(base_family).strip()
            candidate_configuration_list.extend(
                [
                    {
                        "candidate_id": f"{base_family_name}_global",
                        "candidate_family": base_family_name,
                        "candidate_kind": "wave1_exported_model",
                        "candidate_source_label": "wave1",
                        "candidate_surface": "global",
                        "reference_inventory_path": (
                            f"{exported_model_root}/{base_family_name}/global/reference_inventory.yaml"
                        ),
                        "allowed_direction_list": ["forward", "backward"],
                    },
                    {
                        "candidate_id": f"{base_family_name}_Fw",
                        "candidate_family": base_family_name,
                        "candidate_kind": "wave1_exported_model",
                        "candidate_source_label": "wave1",
                        "candidate_surface": "Fw",
                        "reference_inventory_path": (
                            f"{exported_model_root}/{base_family_name}/forward/reference_inventory.yaml"
                        ),
                        "allowed_direction_list": ["forward"],
                    },
                    {
                        "candidate_id": f"{base_family_name}_Bw",
                        "candidate_family": base_family_name,
                        "candidate_kind": "wave1_exported_model",
                        "candidate_source_label": "wave1",
                        "candidate_surface": "Bw",
                        "reference_inventory_path": (
                            f"{exported_model_root}/{base_family_name}/backward/reference_inventory.yaml"
                        ),
                        "allowed_direction_list": ["backward"],
                    },
                ]
            )

    candidate_configuration_list.extend(
        build_composite_reference_candidate_configuration_list(generation_configuration)
    )

    assert candidate_configuration_list, "Generated Track 2 candidate list is empty"
    return candidate_configuration_list


def resolve_track2_candidate_configuration_list(training_config: dict[str, Any]) -> list[dict[str, Any]]:

    """Resolve the configured Track 2 candidate list."""

    comparison_configuration = training_config.get("comparison", {})
    if "candidate_list" in comparison_configuration:
        candidate_configuration_list = comparison_configuration["candidate_list"]
    elif "candidate_generation" in comparison_configuration:
        candidate_configuration_list = build_generated_candidate_configuration_list(training_config)
    else:
        candidate_configuration_list = build_legacy_candidate_configuration_list(training_config)
    assert isinstance(candidate_configuration_list, list) and candidate_configuration_list, (
        "Track 2 comparison candidate_list must not be empty"
    )
    return candidate_configuration_list


def load_track2_candidate(candidate_configuration: dict[str, Any]) -> Track2Candidate:

    """Load one configured Track 2 candidate."""

    candidate_id = str(candidate_configuration["candidate_id"]).strip()
    candidate_family = str(candidate_configuration["candidate_family"]).strip()
    candidate_kind = str(candidate_configuration["candidate_kind"]).strip()
    candidate_source_label = str(candidate_configuration.get("candidate_source_label", candidate_kind)).strip()
    candidate_surface = str(candidate_configuration["candidate_surface"]).strip()
    allowed_direction_list = normalize_allowed_direction_list(candidate_configuration)

    if candidate_kind == "track1_reference_bank":
        reference_inventory_path = candidate_configuration["reference_inventory_path"]
        reference_inventory = load_reference_inventory(reference_inventory_path)
        selected_harmonic_list = resolve_selected_harmonic_list(reference_inventory)
        model_entry_list = load_reference_model_entries(reference_inventory)
        return Track2Candidate(
            candidate_id=candidate_id,
            candidate_family=candidate_family,
            candidate_kind=candidate_kind,
            candidate_source_label=candidate_source_label,
            candidate_surface=candidate_surface,
            allowed_direction_list=allowed_direction_list,
            source_path=shared_training_infrastructure.resolve_runtime_project_relative_path(reference_inventory_path),
            selected_harmonic_list=selected_harmonic_list,
            model_entry_list=model_entry_list,
            model_dictionary=None,
            registry_entry=None,
            training_config=None,
            model_object=None,
        )

    if candidate_kind == "composite_reference_bank":
        archive_root = str(candidate_configuration["archive_root"]).rstrip("/")
        family_folder_lookup = candidate_configuration["family_folder_lookup"]
        model_entry_list: list[ReferenceModelEntry] = []
        inventory_entry_cache: dict[str, list[ReferenceModelEntry]] = {}
        inventory_path_cache: dict[str, Path] = {}

        for target_kind, selection_dictionary in [
            ("amplitude", candidate_configuration["amplitude_family_by_harmonic"]),
            ("phase", candidate_configuration["phase_family_by_harmonic"]),
        ]:
            for harmonic_order_text, family_id in selection_dictionary.items():
                archive_folder = family_folder_lookup[str(family_id)]
                reference_inventory_path = f"{archive_root}/{archive_folder}/reference_inventory.yaml"
                if family_id not in inventory_entry_cache:
                    reference_inventory = load_reference_inventory(reference_inventory_path)
                    inventory_entry_cache[family_id] = load_reference_model_entries(reference_inventory)
                    inventory_path_cache[family_id] = shared_training_infrastructure.resolve_runtime_project_relative_path(
                        reference_inventory_path
                    )
                model_entry_list.append(
                    find_reference_model_entry(
                        inventory_entry_cache[family_id],
                        target_kind,
                        int(harmonic_order_text),
                    )
                )

        selected_harmonic_list = sorted(
            {
                reference_entry.harmonic_order
                for reference_entry in model_entry_list
            }
        )
        return Track2Candidate(
            candidate_id=candidate_id,
            candidate_family=candidate_family,
            candidate_kind=candidate_kind,
            candidate_source_label=candidate_source_label,
            candidate_surface=candidate_surface,
            allowed_direction_list=allowed_direction_list,
            source_path=shared_training_infrastructure.resolve_runtime_project_relative_path(archive_root),
            selected_harmonic_list=selected_harmonic_list,
            model_entry_list=model_entry_list,
            model_dictionary=None,
            registry_entry={
                "composite_selection": {
                    "amplitude_family_by_harmonic": candidate_configuration["amplitude_family_by_harmonic"],
                    "phase_family_by_harmonic": candidate_configuration["phase_family_by_harmonic"],
                    "inventory_path_by_family": {
                        family_id: shared_training_infrastructure.format_project_relative_path(inventory_path)
                        for family_id, inventory_path in sorted(inventory_path_cache.items())
                    },
                },
            },
            training_config=None,
            model_object=None,
        )

    if candidate_kind == "wave1_registry_model":
        family_registry_path = candidate_configuration["family_registry_path"]
        registry_entry = resolve_family_best_entry(family_registry_path)
        model_object, training_config = load_wave1_registry_model(registry_entry)
        return Track2Candidate(
            candidate_id=candidate_id,
            candidate_family=candidate_family,
            candidate_kind=candidate_kind,
            candidate_source_label=candidate_source_label,
            candidate_surface=candidate_surface,
            allowed_direction_list=allowed_direction_list,
            source_path=shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_path),
            selected_harmonic_list=[],
            model_entry_list=None,
            model_dictionary=None,
            registry_entry=registry_entry,
            training_config=training_config,
            model_object=model_object,
        )

    if candidate_kind == "wave1_exported_model":
        reference_inventory_path = candidate_configuration["reference_inventory_path"]
        resolved_inventory_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
            reference_inventory_path
        )
        export_inventory = load_yaml_dictionary(resolved_inventory_path)
        model_object, training_config = load_wave1_exported_model(export_inventory)
        return Track2Candidate(
            candidate_id=candidate_id,
            candidate_family=candidate_family,
            candidate_kind=candidate_kind,
            candidate_source_label=candidate_source_label,
            candidate_surface=candidate_surface,
            allowed_direction_list=allowed_direction_list,
            source_path=resolved_inventory_path,
            selected_harmonic_list=[],
            model_entry_list=None,
            model_dictionary=None,
            registry_entry=export_inventory,
            training_config=training_config,
            model_object=model_object,
        )

    raise ValueError(f"Unsupported Track 2 candidate kind | {candidate_kind}")


def filter_curve_records_for_candidate(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    candidate: Track2Candidate,
) -> list[harmonic_wise_support.HarmonicCurveRecord]:

    """Filter held-out curves to the directions valid for one candidate."""

    filtered_curve_record_list = [
        curve_record
        for curve_record in curve_record_list
        if str(curve_record.direction_label).strip().lower() in candidate.allowed_direction_list
    ]
    assert filtered_curve_record_list, f"No curves available for Track 2 candidate | {candidate.candidate_id}"
    return filtered_curve_record_list


def evaluate_track2_candidate(
    candidate: Track2Candidate,
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    percentage_error_denominator: str,
    include_curve_payload: bool = True,
) -> tuple[list[dict[str, Any]], dict[str, float] | None]:

    """Evaluate one Track 2 candidate on its valid held-out curve records."""

    candidate_curve_record_list = filter_curve_records_for_candidate(curve_record_list, candidate)
    target_metric_dictionary: dict[str, float] | None = None

    if candidate.candidate_kind in REFERENCE_CANDIDATE_KIND_SET:
        assert candidate.model_entry_list is not None
        predicted_target_dictionary = predict_reference_bank_target_dictionary(
            candidate_curve_record_list,
            candidate.model_entry_list,
            candidate.model_dictionary,
        )
        if all(curve_record.amplitude_phase_dictionary for curve_record in candidate_curve_record_list):
            target_metric_dictionary = build_reference_target_metric_dictionary_from_entries(
                candidate_curve_record_list,
                candidate.model_entry_list,
                predicted_target_dictionary,
                candidate.selected_harmonic_list,
            )
        prediction_lookup = build_reference_prediction_lookup(
            candidate.model_entry_list,
            predicted_target_dictionary,
        )
    else:
        predicted_target_dictionary = {}
        prediction_lookup = {}

    per_candidate_entry_list: list[dict[str, Any]] = []
    for sample_index, curve_record in enumerate(candidate_curve_record_list):
        if candidate.candidate_kind in REFERENCE_CANDIDATE_KIND_SET:
            coefficient_dictionary, _ = build_reference_coefficient_dictionary_from_entries(
                prediction_lookup,
                sample_index,
                candidate.selected_harmonic_list,
                resolve_reference_h0_sign_multiplier(candidate),
            )
            predicted_curve_deg = harmonic_wise_support.reconstruct_curve_from_coefficients(
                curve_record.angular_position_deg,
                candidate.selected_harmonic_list,
                coefficient_dictionary,
            )
        else:
            assert candidate.training_config is not None
            predicted_curve_deg = predict_wave1_registry_curve(
                candidate.model_object,
                candidate.training_config,
                curve_record,
            )

        metric_dictionary = harmonic_wise_support.compute_curve_metric_dictionary(
            curve_record.transmission_error_deg,
            predicted_curve_deg,
            percentage_error_denominator,
        )
        per_candidate_entry = {
            "candidate_id": candidate.candidate_id,
            "candidate_family": candidate.candidate_family,
            "candidate_kind": candidate.candidate_kind,
            "candidate_source_label": candidate.candidate_source_label,
            "candidate_surface": candidate.candidate_surface,
            "allowed_direction_list": list(candidate.allowed_direction_list),
            "source_path": shared_training_infrastructure.format_project_relative_path(candidate.source_path),
            "source_file_path": shared_training_infrastructure.format_project_relative_path(curve_record.source_file_path),
            "direction_label": curve_record.direction_label,
            "speed_rpm": float(curve_record.speed_rpm),
            "torque_nm": float(curve_record.torque_nm),
            "oil_temperature_deg": float(curve_record.oil_temperature_deg),
            "metrics": metric_dictionary,
        }
        if include_curve_payload:
            per_candidate_entry.update(
                {
                    "angular_position_deg": curve_record.angular_position_deg.astype(float).tolist(),
                    "truth_curve_deg": curve_record.transmission_error_deg.astype(float).tolist(),
                    "predicted_curve_deg": predicted_curve_deg.astype(float).tolist(),
                }
            )
        per_candidate_entry_list.append(per_candidate_entry)

    return per_candidate_entry_list, target_metric_dictionary


def summarize_metric_dictionary(metric_dictionary_list: list[dict[str, float]]) -> dict[str, float]:

    """Average one metric-dictionary list and add a `p95` percentage statistic."""

    mean_metric_dictionary = harmonic_wise_support.average_metric_dictionary(metric_dictionary_list)
    percentage_error_list = [metric_dictionary["mean_percentage_error_pct"] for metric_dictionary in metric_dictionary_list]
    mean_metric_dictionary["p95_mean_percentage_error_pct"] = float(np.percentile(percentage_error_list, 95.0))
    return mean_metric_dictionary


def build_group_metric_summary(
    per_sample_entry_list: list[dict[str, Any]],
    group_key_name: str,
) -> dict[str, dict[str, dict[str, float]]]:

    """Aggregate per-model metrics by one chosen grouping key."""

    grouped_metric_accumulator: dict[str, dict[str, list[dict[str, float]]]] = {}
    for per_sample_entry in per_sample_entry_list:
        group_key = str(per_sample_entry[group_key_name])
        grouped_metric_accumulator.setdefault(group_key, {})
        for model_name in ["lgbm19_reference_bank", "feedforward_best", "oracle_harmonic_truncation"]:
            metric_dictionary = per_sample_entry[f"{model_name}_metrics"]
            grouped_metric_accumulator[group_key].setdefault(model_name, []).append(metric_dictionary)

    return {
        group_key: {
            model_name: summarize_metric_dictionary(metric_dictionary_list)
            for model_name, metric_dictionary_list in model_metric_dictionary.items()
        }
        for group_key, model_metric_dictionary in grouped_metric_accumulator.items()
    }


def build_candidate_metric_summary(per_candidate_entry_list: list[dict[str, Any]]) -> dict[str, dict[str, float]]:

    """Summarize metrics for every evaluated Track 2 candidate."""

    candidate_metric_accumulator: dict[str, list[dict[str, float]]] = {}
    for per_candidate_entry in per_candidate_entry_list:
        candidate_id = str(per_candidate_entry["candidate_id"])
        candidate_metric_accumulator.setdefault(candidate_id, []).append(per_candidate_entry["metrics"])
    return {
        candidate_id: summarize_metric_dictionary(metric_dictionary_list)
        for candidate_id, metric_dictionary_list in candidate_metric_accumulator.items()
    }


def build_generic_group_metric_summary(
    per_candidate_entry_list: list[dict[str, Any]],
    group_key_name: str,
) -> dict[str, dict[str, dict[str, float]]]:

    """Summarize candidate metrics by one grouping key."""

    grouped_metric_accumulator: dict[str, dict[str, list[dict[str, float]]]] = {}
    for per_candidate_entry in per_candidate_entry_list:
        group_key = str(per_candidate_entry[group_key_name])
        candidate_id = str(per_candidate_entry["candidate_id"])
        grouped_metric_accumulator.setdefault(group_key, {})
        grouped_metric_accumulator[group_key].setdefault(candidate_id, []).append(per_candidate_entry["metrics"])

    return {
        group_key: {
            candidate_id: summarize_metric_dictionary(metric_dictionary_list)
            for candidate_id, metric_dictionary_list in candidate_metric_dictionary.items()
        }
        for group_key, candidate_metric_dictionary in grouped_metric_accumulator.items()
    }


def save_track2_per_condition_metrics_csv(
    output_directory: Path,
    per_candidate_entry_list: list[dict[str, Any]],
) -> Path:

    """Save the direction-aware Track 2 per-condition metric table."""

    csv_path = output_directory / "per_condition_metrics.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "source_file_path",
                "direction_label",
                "speed_rpm",
                "torque_nm",
                "oil_temperature_deg",
                "candidate_id",
                "candidate_family",
                "candidate_kind",
                "candidate_source_label",
                "candidate_surface",
                "curve_mae_deg",
                "curve_rmse_deg",
                "mean_percentage_error_pct",
            ]
        )
        for per_candidate_entry in per_candidate_entry_list:
            metric_dictionary = per_candidate_entry["metrics"]
            writer.writerow(
                [
                    per_candidate_entry["source_file_path"],
                    per_candidate_entry["direction_label"],
                    per_candidate_entry["speed_rpm"],
                    per_candidate_entry["torque_nm"],
                    per_candidate_entry["oil_temperature_deg"],
                    per_candidate_entry["candidate_id"],
                    per_candidate_entry["candidate_family"],
                    per_candidate_entry["candidate_kind"],
                    per_candidate_entry["candidate_source_label"],
                    per_candidate_entry["candidate_surface"],
                    metric_dictionary["mae"],
                    metric_dictionary["rmse"],
                    metric_dictionary["mean_percentage_error_pct"],
                ]
            )
    return csv_path


def save_per_condition_metrics_csv(output_directory: Path, per_sample_entry_list: list[dict[str, Any]]) -> Path:

    """Save one per-condition comparison table for downstream inspection."""

    csv_path = output_directory / "per_condition_metrics.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "source_file_path",
                "direction_label",
                "speed_rpm",
                "torque_nm",
                "oil_temperature_deg",
                "model_name",
                "curve_mae_deg",
                "curve_rmse_deg",
                "mean_percentage_error_pct",
            ]
        )
        for per_sample_entry in per_sample_entry_list:
            for model_name in ["lgbm19_reference_bank", "feedforward_best", "oracle_harmonic_truncation"]:
                metric_dictionary = per_sample_entry[f"{model_name}_metrics"]
                writer.writerow(
                    [
                        per_sample_entry["source_file_path"],
                        per_sample_entry["direction_label"],
                        per_sample_entry["speed_rpm"],
                        per_sample_entry["torque_nm"],
                        per_sample_entry["oil_temperature_deg"],
                        model_name,
                        metric_dictionary["mae"],
                        metric_dictionary["rmse"],
                        metric_dictionary["mean_percentage_error_pct"],
                    ]
                )
    return csv_path


def maybe_generate_preview_plots(
    output_directory: Path,
    per_sample_entry_list: list[dict[str, Any]],
    preview_curve_count: int,
) -> list[str]:

    """Generate a few representative overlay plots when matplotlib is available."""

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return []

    preview_directory = output_directory / "preview_curves"
    preview_directory.mkdir(parents=True, exist_ok=True)
    preview_plot_path_list: list[str] = []

    for preview_index, per_sample_entry in enumerate(per_sample_entry_list[:preview_curve_count]):
        figure, axis = plt.subplots(figsize=(8.0, 4.0))
        angular_position_deg = np.asarray(per_sample_entry["angular_position_deg"], dtype=np.float32)
        axis.plot(angular_position_deg, per_sample_entry["truth_curve_deg"], label="Truth", linewidth=1.5)
        axis.plot(angular_position_deg, per_sample_entry["lgbm19_curve_deg"], label="LGBM-19", linewidth=1.1)
        axis.plot(angular_position_deg, per_sample_entry["feedforward_curve_deg"], label="Feedforward", linewidth=1.1)
        axis.set_xlabel("Angular Position [deg]")
        axis.set_ylabel("Transmission Error [deg]")
        axis.set_title(
            f"Preview {preview_index + 1} | "
            f"{per_sample_entry['speed_rpm']:.0f} rpm | "
            f"{per_sample_entry['torque_nm']:.0f} Nm | "
            f"{per_sample_entry['oil_temperature_deg']:.0f} C | "
            f"{per_sample_entry['direction_label']}"
        )
        axis.grid(True, alpha=0.3)
        axis.legend(loc="best")
        plot_path = preview_directory / f"preview_{preview_index + 1:02d}.png"
        figure.tight_layout()
        figure.savefig(plot_path, dpi=180)
        plt.close(figure)
        preview_plot_path_list.append(shared_training_infrastructure.format_project_relative_path(plot_path))

    return preview_plot_path_list


def maybe_generate_track2_preview_plots(
    output_directory: Path,
    per_candidate_entry_list: list[dict[str, Any]],
    preview_curve_count: int,
) -> list[str]:

    """Generate direction-aware Track 2 overlay plots."""

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return []

    preview_directory = output_directory / "preview_curves"
    preview_directory.mkdir(parents=True, exist_ok=True)
    preview_plot_path_list: list[str] = []
    selected_entry_list = [
        per_candidate_entry
        for per_candidate_entry in per_candidate_entry_list
        if "angular_position_deg" in per_candidate_entry
    ][: max(int(preview_curve_count), 0)]

    for preview_index, per_candidate_entry in enumerate(selected_entry_list):
        figure, axis = plt.subplots(figsize=(8.0, 4.0))
        angular_position_deg = np.asarray(per_candidate_entry["angular_position_deg"], dtype=np.float32)
        axis.plot(angular_position_deg, per_candidate_entry["truth_curve_deg"], label="Truth", linewidth=1.5)
        axis.plot(
            angular_position_deg,
            per_candidate_entry["predicted_curve_deg"],
            label=str(per_candidate_entry["candidate_id"]),
            linewidth=1.1,
        )
        axis.set_xlabel("Angular Position [deg]")
        axis.set_ylabel("Transmission Error [deg]")
        axis.set_title(
            f"Preview {preview_index + 1} | "
            f"{per_candidate_entry['candidate_id']} | "
            f"{per_candidate_entry['direction_label']} | "
            f"{per_candidate_entry['speed_rpm']:.0f} rpm | "
            f"{per_candidate_entry['torque_nm']:.0f} Nm | "
            f"{per_candidate_entry['oil_temperature_deg']:.0f} C"
        )
        axis.grid(True, alpha=0.3)
        axis.legend(loc="best")
        plot_path = preview_directory / f"preview_{preview_index + 1:02d}.png"
        figure.tight_layout()
        figure.savefig(plot_path, dpi=180)
        plt.close(figure)
        preview_plot_path_list.append(shared_training_infrastructure.format_project_relative_path(plot_path))

    return preview_plot_path_list


def resolve_track2_report_plot_root(training_config: dict[str, Any]) -> Path | None:

    """Resolve the optional report-facing grouped PNG root."""

    report_plot_root = training_config.get("comparison", {}).get("report_plot_root")
    if report_plot_root in [None, ""]:
        return None
    return shared_training_infrastructure.resolve_runtime_project_relative_path(report_plot_root)


def build_track2_plot_source_folder_name(candidate_source_label: str) -> str:

    """Map a candidate source label to the requested report-folder name."""

    source_label = str(candidate_source_label).strip()
    if source_label == "rcim_original":
        return "original"
    if source_label == "rcim_retuned":
        return "original retuned"
    if source_label == "rcim_track1":
        return "track 1"
    if source_label == "wave1":
        return "wave 1"
    return shared_training_infrastructure.sanitize_name(source_label)


def build_track2_condition_slug(per_candidate_entry: dict[str, Any]) -> str:

    """Build a stable condition slug for one plotted Track 2 curve."""

    return (
        f"{per_candidate_entry['direction_label']}_"
        f"{float(per_candidate_entry['speed_rpm']):.0f}rpm_"
        f"{float(per_candidate_entry['torque_nm']):.0f}Nm_"
        f"{float(per_candidate_entry['oil_temperature_deg']):.0f}C"
    )


def maybe_generate_track2_grouped_report_plots(
    report_plot_root: Path | None,
    per_candidate_entry_list: list[dict[str, Any]],
    preview_curve_count_per_candidate: int,
) -> list[str]:

    """Generate report-facing Track 2 PNG overlays for every evaluated model."""

    if report_plot_root is None:
        return []

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return []

    grouped_entry_dictionary: dict[str, list[dict[str, Any]]] = {}
    for per_candidate_entry in per_candidate_entry_list:
        if "angular_position_deg" not in per_candidate_entry:
            continue
        candidate_id = str(per_candidate_entry["candidate_id"])
        grouped_entry_dictionary.setdefault(candidate_id, []).append(per_candidate_entry)

    report_plot_path_list: list[str] = []
    max_plot_count = max(int(preview_curve_count_per_candidate), 1)
    for candidate_id in sorted(grouped_entry_dictionary):
        selected_entry_list = grouped_entry_dictionary[candidate_id][:max_plot_count]
        for plot_index, per_candidate_entry in enumerate(selected_entry_list, start=1):
            source_folder_name = build_track2_plot_source_folder_name(
                str(per_candidate_entry["candidate_source_label"])
            )
            family_folder_name = shared_training_infrastructure.sanitize_name(
                str(per_candidate_entry["candidate_family"]).lower()
            )
            plot_directory = report_plot_root / source_folder_name / family_folder_name
            plot_directory.mkdir(parents=True, exist_ok=True)

            condition_slug = build_track2_condition_slug(per_candidate_entry)
            plot_filename = (
                f"{plot_index:02d}_"
                f"{shared_training_infrastructure.sanitize_name(candidate_id)}_"
                f"{shared_training_infrastructure.sanitize_name(condition_slug)}.png"
            )
            plot_path = plot_directory / plot_filename

            figure, axis = plt.subplots(figsize=(8.0, 4.0))
            angular_position_deg = np.asarray(per_candidate_entry["angular_position_deg"], dtype=np.float32)
            axis.plot(angular_position_deg, per_candidate_entry["truth_curve_deg"], label="Truth", linewidth=1.5)
            axis.plot(
                angular_position_deg,
                per_candidate_entry["predicted_curve_deg"],
                label=candidate_id,
                linewidth=1.1,
            )
            axis.set_xlabel("Angular Position [deg]")
            axis.set_ylabel("Transmission Error [deg]")
            axis.set_title(
                f"{candidate_id} | "
                f"{per_candidate_entry['direction_label']} | "
                f"{per_candidate_entry['speed_rpm']:.0f} rpm | "
                f"{per_candidate_entry['torque_nm']:.0f} Nm | "
                f"{per_candidate_entry['oil_temperature_deg']:.0f} C"
            )
            axis.grid(True, alpha=0.3)
            axis.legend(loc="best")
            figure.tight_layout()
            figure.savefig(plot_path, dpi=180)
            plt.close(figure)
            report_plot_path_list.append(shared_training_infrastructure.format_project_relative_path(plot_path))

    return report_plot_path_list


def build_comparison_summary(
    resolved_config_path: Path,
    output_directory: Path,
    training_config: dict[str, Any],
    reference_inventory: dict[str, Any],
    feedforward_best_entry: dict[str, Any],
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    reference_target_metric_dictionary: dict[str, float],
    aggregate_metric_dictionary: dict[str, dict[str, float]],
    per_sample_entry_list: list[dict[str, Any]],
    direction_metric_summary: dict[str, dict[str, dict[str, float]]],
    temperature_metric_summary: dict[str, dict[str, dict[str, float]]],
    preview_plot_path_list: list[str],
    per_condition_metrics_csv_path: Path,
    selected_harmonic_list: list[int],
) -> dict[str, Any]:

    """Build the machine-readable comparison summary."""

    comparison_configuration = training_config["comparison"]
    return {
        "config_path": shared_training_infrastructure.format_project_relative_path(resolved_config_path),
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "comparison_scope": {
            "reference_family_name": str(reference_inventory["paper_family_name"]),
            "reference_bank_model_count": int(len(reference_inventory["reference_models"])),
            "selected_harmonic_list": list(selected_harmonic_list),
            "percentage_error_denominator": str(comparison_configuration["percentage_error_denominator"]),
            "curve_count": int(len(curve_record_list)),
        },
        "feedforward_reference": {
            "run_instance_id": str(feedforward_best_entry["run_instance_id"]),
            "run_name": str(feedforward_best_entry["run_name"]),
            "best_checkpoint_path": str(feedforward_best_entry["best_checkpoint_path"]),
            "registry_test_mae": float(feedforward_best_entry["test_mae"]),
            "registry_test_rmse": float(feedforward_best_entry["test_rmse"]),
        },
        "reference_bank": {
            "reference_inventory_path": shared_training_infrastructure.format_project_relative_path(
                shared_training_infrastructure.resolve_runtime_project_relative_path(
                    training_config["paths"]["reference_inventory_path"]
                )
            ),
            "paper_family_name": str(reference_inventory["paper_family_name"]),
            "target_metric_summary": reference_target_metric_dictionary,
        },
        "aggregate_metrics": aggregate_metric_dictionary,
        "direction_breakdown": direction_metric_summary,
        "temperature_breakdown": temperature_metric_summary,
        "preview_plot_path_list": preview_plot_path_list,
        "per_condition_metrics_csv_path": shared_training_infrastructure.format_project_relative_path(
            per_condition_metrics_csv_path
        ),
        "sample_preview_list": [
            {
                "source_file_path": per_sample_entry["source_file_path"],
                "direction_label": per_sample_entry["direction_label"],
                "speed_rpm": per_sample_entry["speed_rpm"],
                "torque_nm": per_sample_entry["torque_nm"],
                "oil_temperature_deg": per_sample_entry["oil_temperature_deg"],
                "lgbm19_mean_percentage_error_pct": per_sample_entry["lgbm19_reference_bank_metrics"]["mean_percentage_error_pct"],
                "feedforward_mean_percentage_error_pct": per_sample_entry["feedforward_best_metrics"]["mean_percentage_error_pct"],
                "oracle_mean_percentage_error_pct": per_sample_entry["oracle_harmonic_truncation_metrics"]["mean_percentage_error_pct"],
            }
            for per_sample_entry in per_sample_entry_list[:3]
        ],
    }


def build_reference_family_vs_feedforward_report_markdown(comparison_summary: dict[str, Any]) -> str:

    """Build the Markdown comparison report."""

    comparison_scope = comparison_summary["comparison_scope"]
    feedforward_reference = comparison_summary["feedforward_reference"]
    reference_bank = comparison_summary["reference_bank"]
    aggregate_metrics = comparison_summary["aggregate_metrics"]

    report_line_list = [
        "# Track 2 LGBM19 Vs Feedforward Comparison Report",
        "",
        "## Overview",
        "",
        "This report compares the curated paper-faithful `LGBM-19` harmonic bank",
        "against the canonical best direct-TE `feedforward` baseline on the",
        "repository held-out TE-curve test split.",
        "",
        "## Scope",
        "",
        f"- reference family: `{reference_bank['paper_family_name']}`;",
        f"- reference bank size: `{comparison_scope['reference_bank_model_count']}` archived target models;",
        f"- selected harmonics: `{', '.join(str(harmonic_order) for harmonic_order in comparison_scope['selected_harmonic_list'])}`;",
        f"- held-out curve count: `{comparison_scope['curve_count']}`;",
        f"- percentage-error denominator: `{comparison_scope['percentage_error_denominator']}`;",
        f"- canonical feedforward run: `{feedforward_reference['run_instance_id']}`;",
        "",
        "## Aggregate Comparison",
        "",
        "| Model | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |",
        "| --- | ---: | ---: | ---: | ---: |",
        (
            f"| `LGBM-19 reference bank` | "
            f"{aggregate_metrics['lgbm19_reference_bank']['mae']:.6f} | "
            f"{aggregate_metrics['lgbm19_reference_bank']['rmse']:.6f} | "
            f"{aggregate_metrics['lgbm19_reference_bank']['mean_percentage_error_pct']:.3f} | "
            f"{aggregate_metrics['lgbm19_reference_bank']['p95_mean_percentage_error_pct']:.3f} |"
        ),
        (
            f"| `feedforward best` | "
            f"{aggregate_metrics['feedforward_best']['mae']:.6f} | "
            f"{aggregate_metrics['feedforward_best']['rmse']:.6f} | "
            f"{aggregate_metrics['feedforward_best']['mean_percentage_error_pct']:.3f} | "
            f"{aggregate_metrics['feedforward_best']['p95_mean_percentage_error_pct']:.3f} |"
        ),
        (
            f"| `oracle harmonic truncation` | "
            f"{aggregate_metrics['oracle_harmonic_truncation']['mae']:.6f} | "
            f"{aggregate_metrics['oracle_harmonic_truncation']['rmse']:.6f} | "
            f"{aggregate_metrics['oracle_harmonic_truncation']['mean_percentage_error_pct']:.3f} | "
            f"{aggregate_metrics['oracle_harmonic_truncation']['p95_mean_percentage_error_pct']:.3f} |"
        ),
        "",
        "## Reference Bank Diagnostics",
        "",
        f"- amplitude MAE on repository harmonic decomposition: `{reference_bank['target_metric_summary']['amplitude_mae']:.6f}`.",
        f"- amplitude RMSE on repository harmonic decomposition: `{reference_bank['target_metric_summary']['amplitude_rmse']:.6f}`.",
        f"- phase MAE on repository harmonic decomposition: `{reference_bank['target_metric_summary']['phase_mae_rad']:.6f} rad`.",
        f"- phase RMSE on repository harmonic decomposition: `{reference_bank['target_metric_summary']['phase_rmse_rad']:.6f} rad`.",
        "",
        "## Direction Breakdown",
        "",
        "| Direction | Model | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] |",
        "| --- | --- | ---: | ---: | ---: |",
    ]

    for direction_label, direction_entry in comparison_summary["direction_breakdown"].items():
        for model_name, metric_dictionary in direction_entry.items():
            report_line_list.append(
                f"| `{direction_label}` | `{model_name}` | "
                f"{metric_dictionary['mae']:.6f} | "
                f"{metric_dictionary['rmse']:.6f} | "
                f"{metric_dictionary['mean_percentage_error_pct']:.3f} |"
            )

    report_line_list.extend(
        [
            "",
            "## Temperature Breakdown",
            "",
            "| Temperature [C] | Model | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] |",
            "| ---: | --- | ---: | ---: | ---: |",
        ]
    )

    for temperature_label, temperature_entry in comparison_summary["temperature_breakdown"].items():
        for model_name, metric_dictionary in temperature_entry.items():
            report_line_list.append(
                f"| `{temperature_label}` | `{model_name}` | "
                f"{metric_dictionary['mae']:.6f} | "
                f"{metric_dictionary['rmse']:.6f} | "
                f"{metric_dictionary['mean_percentage_error_pct']:.3f} |"
            )

    report_line_list.extend(
        [
            "",
            "## Sample Preview",
            "",
        ]
    )

    for preview_entry in comparison_summary["sample_preview_list"]:
        report_line_list.append(
            (
                f"- `{preview_entry['source_file_path']}` | `{preview_entry['direction_label']}` | "
                f"`{preview_entry['speed_rpm']:.0f} rpm` | "
                f"`{preview_entry['torque_nm']:.0f} Nm` | "
                f"`{preview_entry['oil_temperature_deg']:.0f} C` | "
                f"`LGBM={preview_entry['lgbm19_mean_percentage_error_pct']:.3f}%` | "
                f"`feedforward={preview_entry['feedforward_mean_percentage_error_pct']:.3f}%` | "
                f"`oracle={preview_entry['oracle_mean_percentage_error_pct']:.3f}%`"
            )
        )

    report_line_list.extend(
        [
            "",
            "## Output Artifacts",
            "",
            f"- summary YAML: `{comparison_summary['output_directory']}/validation_summary.yaml`;",
            f"- per-condition CSV: `{comparison_summary['per_condition_metrics_csv_path']}`;",
        ]
    )

    for preview_plot_path in comparison_summary["preview_plot_path_list"]:
        report_line_list.append(f"- preview plot: `{preview_plot_path}`;")

    return "\n".join(report_line_list) + "\n"


def build_track2_directional_comparison_summary(
    resolved_config_path: Path,
    output_directory: Path,
    training_config: dict[str, Any],
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    candidate_list: list[Track2Candidate],
    target_metric_dictionary: dict[str, dict[str, float]],
    per_candidate_entry_list: list[dict[str, Any]],
    preview_plot_path_list: list[str],
    report_plot_root: Path | None,
    report_plot_path_list: list[str],
    per_condition_metrics_csv_path: Path,
    dataset_root: Path,
    candidate_metric_summary_override: dict[str, dict[str, float]] | None = None,
    direction_metric_summary_override: dict[str, dict[str, dict[str, float]]] | None = None,
    temperature_metric_summary_override: dict[str, dict[str, dict[str, float]]] | None = None,
    sample_preview_list_override: list[dict[str, object]] | None = None,
) -> dict[str, Any]:

    """Build the direction-aware Track 2 comparison summary."""

    comparison_configuration = training_config["comparison"]
    candidate_metric_summary = (
        candidate_metric_summary_override
        if candidate_metric_summary_override is not None
        else build_candidate_metric_summary(per_candidate_entry_list)
    )
    direction_metric_summary = (
        direction_metric_summary_override
        if direction_metric_summary_override is not None
        else build_generic_group_metric_summary(per_candidate_entry_list, "direction_label")
    )
    temperature_metric_summary = (
        temperature_metric_summary_override
        if temperature_metric_summary_override is not None
        else build_generic_group_metric_summary(per_candidate_entry_list, "oil_temperature_deg")
    )
    sample_preview_list = (
        sample_preview_list_override
        if sample_preview_list_override is not None
        else [
            {
                "source_file_path": per_candidate_entry["source_file_path"],
                "direction_label": per_candidate_entry["direction_label"],
                "candidate_id": per_candidate_entry["candidate_id"],
                "speed_rpm": per_candidate_entry["speed_rpm"],
                "torque_nm": per_candidate_entry["torque_nm"],
                "oil_temperature_deg": per_candidate_entry["oil_temperature_deg"],
                "mean_percentage_error_pct": per_candidate_entry["metrics"]["mean_percentage_error_pct"],
            }
            for per_candidate_entry in per_candidate_entry_list[:5]
        ]
    )

    return {
        "config_path": shared_training_infrastructure.format_project_relative_path(resolved_config_path),
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "dataset": {
            "dataset_config_path": training_config["paths"]["dataset_config_path"],
            "dataset_root": shared_training_infrastructure.format_project_relative_path(dataset_root),
            "source_contract": "data/datasets",
        },
        "comparison_scope": {
            "comparison_mode": str(comparison_configuration.get("comparison_mode", "directional_candidate_matrix")),
            "percentage_error_denominator": str(comparison_configuration["percentage_error_denominator"]),
            "curve_count": int(len(curve_record_list)),
            "candidate_count": int(len(candidate_list)),
            "directional_policy": {
                "global": ["forward", "backward"],
                "Fw": ["forward"],
                "Bw": ["backward"],
            },
            "reference_bank_compatibility_policy": {
                "rcim_track1_Fw_h0_sign_multiplier": -1.0,
                "reason": (
                    "Track 1 forward reference banks store the constant harmonic with "
                    "the opposite sign convention relative to the Track 2 TE-curve "
                    "reconstruction contract."
                ),
            },
        },
        "candidate_list": [
            {
                "candidate_id": candidate.candidate_id,
                "candidate_family": candidate.candidate_family,
                "candidate_kind": candidate.candidate_kind,
                "candidate_source_label": candidate.candidate_source_label,
                "candidate_surface": candidate.candidate_surface,
                "allowed_direction_list": candidate.allowed_direction_list,
                "source_path": shared_training_infrastructure.format_project_relative_path(candidate.source_path),
                "selected_harmonic_list": candidate.selected_harmonic_list,
                "registry_run_instance_id": (
                    str(candidate.registry_entry["run_instance_id"])
                    if candidate.registry_entry is not None and "run_instance_id" in candidate.registry_entry
                    else None
                ),
                "model_file_path": (
                    str(candidate.registry_entry["python_model_path"])
                    if candidate.registry_entry is not None and "python_model_path" in candidate.registry_entry
                    else None
                ),
                "composite_selection": (
                    candidate.registry_entry.get("composite_selection")
                    if candidate.registry_entry is not None
                    else None
                ),
            }
            for candidate in candidate_list
        ],
        "candidate_target_metric_summary": target_metric_dictionary,
        "candidate_metric_summary": candidate_metric_summary,
        "direction_breakdown": direction_metric_summary,
        "temperature_breakdown": temperature_metric_summary,
        "preview_plot_path_list": preview_plot_path_list,
        "report_plot_root": (
            shared_training_infrastructure.format_project_relative_path(report_plot_root)
            if report_plot_root is not None
            else None
        ),
        "report_plot_path_list": report_plot_path_list,
        "report_plot_count": int(len(report_plot_path_list)),
        "per_condition_metrics_csv_path": shared_training_infrastructure.format_project_relative_path(
            per_condition_metrics_csv_path
        ),
        "sample_preview_list": sample_preview_list,
    }


def build_track2_directional_comparison_report_markdown(comparison_summary: dict[str, Any]) -> str:

    """Build the direction-aware Track 2 Markdown report."""

    comparison_scope = comparison_summary["comparison_scope"]
    candidate_metric_summary = comparison_summary["candidate_metric_summary"]
    direction_breakdown = comparison_summary["direction_breakdown"]
    candidate_source_lookup = {
        str(candidate_entry["candidate_id"]): str(candidate_entry["candidate_source_label"])
        for candidate_entry in comparison_summary["candidate_list"]
    }

    def append_best_composite_reference_table(report_line_list: list[str]) -> None:
        composite_row_list = []
        source_order_lookup = {
            "rcim_original": 0,
            "rcim_retuned": 1,
            "rcim_track1": 2,
        }
        surface_order_lookup = {
            "Fw": 0,
            "Bw": 1,
        }

        for candidate_entry in comparison_summary["candidate_list"]:
            if str(candidate_entry["candidate_kind"]) != "composite_reference_bank":
                continue

            candidate_id = str(candidate_entry["candidate_id"])
            for direction_label in candidate_entry["allowed_direction_list"]:
                metric_dictionary = direction_breakdown.get(direction_label, {}).get(candidate_id)
                if metric_dictionary is None:
                    continue
                composite_row_list.append(
                    (
                        candidate_id,
                        str(candidate_entry["candidate_source_label"]),
                        str(candidate_entry["candidate_surface"]),
                        str(direction_label),
                        metric_dictionary,
                    )
                )

        composite_row_list.sort(
            key=lambda row: (
                surface_order_lookup.get(row[2], 99),
                source_order_lookup.get(row[1], 99),
                row[0],
            )
        )
        if not composite_row_list:
            return

        report_line_list.extend(
            [
                "",
                "## Best Composite Reference Models",
                "",
                "These candidates combine the approved best harmonic-wise cells into",
                "one Track 2 curve-reconstruction candidate. They are also repeated",
                "inside the source-group tables below, but this section keeps the",
                "composed models explicit.",
                "",
                "| Candidate | Source | Surface | Direction | Curve MAE [deg] | Curve RMSE [deg] | "
                "Mean Percentage Error [%] | P95 Mean Percentage Error [%] |",
                "| --- | --- | --- | --- | ---: | ---: | ---: | ---: |",
            ]
        )
        for (
            candidate_id,
            source_label,
            surface_label,
            direction_label,
            metric_dictionary,
        ) in composite_row_list:
            report_line_list.append(
                f"| `{candidate_id}` | "
                f"`{source_label}` | "
                f"`{surface_label}` | "
                f"`{direction_label}` | "
                f"{metric_dictionary['mae']:.6f} | "
                f"{metric_dictionary['rmse']:.6f} | "
                f"{metric_dictionary['mean_percentage_error_pct']:.3f} | "
                f"{metric_dictionary['p95_mean_percentage_error_pct']:.3f} |"
            )

    def append_grouped_direction_table(
        report_line_list: list[str],
        section_title: str,
        direction_label: str,
        source_label: str,
        include_global_models: bool = False,
    ) -> None:
        direction_entry = direction_breakdown.get(direction_label, {})
        table_row_list = [
            (candidate_id, metric_dictionary)
            for candidate_id, metric_dictionary in direction_entry.items()
            if candidate_source_lookup.get(candidate_id) == source_label
            and (
                candidate_id.endswith("_Fw")
                or candidate_id.endswith("_Bw")
                or (include_global_models and candidate_id.endswith("_global"))
            )
        ]
        table_row_list.sort(key=lambda row: row[1]["mean_percentage_error_pct"])
        if not table_row_list:
            return

        report_line_list.extend(
            [
                "",
                f"### {section_title}",
                "",
                "| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |",
                "| --- | ---: | ---: | ---: | ---: |",
            ]
        )
        for candidate_id, metric_dictionary in table_row_list:
            report_line_list.append(
                f"| `{candidate_id}` | "
                f"{metric_dictionary['mae']:.6f} | "
                f"{metric_dictionary['rmse']:.6f} | "
                f"{metric_dictionary['mean_percentage_error_pct']:.3f} | "
                f"{metric_dictionary['p95_mean_percentage_error_pct']:.3f} |"
            )

    report_line_list = [
        "# Track 2 Directional Model Comparison",
        "",
        "## Overview",
        "",
        "This report is the canonical `Track 2` offline comparison between",
        "`Track 1`, recovered original, retuned paper-reference model banks, and",
        "repository-owned `Wave 1` and `Wave 2` model candidates. It starts from",
        "the current direction-aware comparison matrix.",
        "",
        "## Dataset And Split",
        "",
        f"- dataset config: `{comparison_summary['dataset']['dataset_config_path']}`;",
        f"- dataset root: `{comparison_summary['dataset']['dataset_root']}`;",
        f"- comparison mode: `{comparison_scope['comparison_mode']}`;",
        f"- candidate count: `{comparison_scope['candidate_count']}`;",
        f"- held-out curve count before candidate filtering: `{comparison_scope['curve_count']}`;",
        f"- percentage-error denominator: `{comparison_scope['percentage_error_denominator']}`;",
        "- `Fw` candidates are evaluated only on forward curves;",
        "- `Bw` candidates are evaluated only on backward curves;",
        "- `global` candidates are evaluated on both directions and reported with",
        "  direction-separated metrics.",
        "",
        "## Candidate Inventory",
        "",
        "| Candidate | Family | Source | Kind | Surface | Valid Directions | Model Source |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]

    for candidate_entry in comparison_summary["candidate_list"]:
        model_source = candidate_entry["model_file_path"] or candidate_entry["source_path"]
        report_line_list.append(
            f"| `{candidate_entry['candidate_id']}` | "
            f"`{candidate_entry['candidate_family']}` | "
            f"`{candidate_entry['candidate_source_label']}` | "
            f"`{candidate_entry['candidate_kind']}` | "
            f"`{candidate_entry['candidate_surface']}` | "
            f"`{', '.join(candidate_entry['allowed_direction_list'])}` | "
            f"`{model_source}` |"
        )

    append_best_composite_reference_table(report_line_list)

    report_line_list.extend(
        [
            "",
            "## Forward Comparison",
        ]
    )
    append_grouped_direction_table(report_line_list, "Original Forward Models", "forward", "rcim_original")
    append_grouped_direction_table(report_line_list, "Retuned Forward Models", "forward", "rcim_retuned")
    append_grouped_direction_table(report_line_list, "Track 1 Forward Models", "forward", "rcim_track1")
    append_grouped_direction_table(
        report_line_list,
        "Wave 1 Forward And Global Models",
        "forward",
        "wave1",
        include_global_models=True,
    )
    append_grouped_direction_table(
        report_line_list,
        "Wave 2 Temporal Forward And Global Models",
        "forward",
        "wave2_temporal_entry_registry",
        include_global_models=True,
    )
    append_grouped_direction_table(
        report_line_list,
        "Wave 2C Residual Harmonic Temporal Forward And Global Models",
        "forward",
        "wave2c_residual_harmonic_temporal_registry",
        include_global_models=True,
    )
    append_grouped_direction_table(
        report_line_list,
        "Track 2F Offset-Aware Forward And Global Models",
        "forward",
        "track2f_offset_aware_probe_registry",
        include_global_models=True,
    )

    report_line_list.extend(
        [
            "",
            "## Backward Comparison",
        ]
    )
    append_grouped_direction_table(report_line_list, "Retuned Backward Models", "backward", "rcim_retuned")
    append_grouped_direction_table(report_line_list, "Track 1 Backward Models", "backward", "rcim_track1")
    append_grouped_direction_table(
        report_line_list,
        "Wave 1 Backward And Global Models",
        "backward",
        "wave1",
        include_global_models=True,
    )
    append_grouped_direction_table(
        report_line_list,
        "Wave 2 Temporal Backward And Global Models",
        "backward",
        "wave2_temporal_entry_registry",
        include_global_models=True,
    )
    append_grouped_direction_table(
        report_line_list,
        "Wave 2C Residual Harmonic Temporal Backward And Global Models",
        "backward",
        "wave2c_residual_harmonic_temporal_registry",
        include_global_models=True,
    )
    append_grouped_direction_table(
        report_line_list,
        "Track 2F Offset-Aware Backward And Global Models",
        "backward",
        "track2f_offset_aware_probe_registry",
        include_global_models=True,
    )

    report_line_list.extend(
        [
            "",
            "## Global Model Direction Breakdown",
            "",
            "| Candidate | Direction | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )

    for candidate_id in sorted(
        candidate_id
        for candidate_id in candidate_metric_summary
        if candidate_id.endswith("_global")
    ):
        for direction_label in ["forward", "backward"]:
            metric_dictionary = direction_breakdown.get(direction_label, {}).get(candidate_id)
            if metric_dictionary is None:
                continue
            report_line_list.append(
                f"| `{candidate_id}` | `{direction_label}` | "
                f"{metric_dictionary['mae']:.6f} | "
                f"{metric_dictionary['rmse']:.6f} | "
                f"{metric_dictionary['mean_percentage_error_pct']:.3f} | "
                f"{metric_dictionary['p95_mean_percentage_error_pct']:.3f} |"
            )
        combined_metric_dictionary = candidate_metric_summary[candidate_id]
        report_line_list.append(
            f"| `{candidate_id}` | `combined` | "
            f"{combined_metric_dictionary['mae']:.6f} | "
            f"{combined_metric_dictionary['rmse']:.6f} | "
            f"{combined_metric_dictionary['mean_percentage_error_pct']:.3f} | "
            f"{combined_metric_dictionary['p95_mean_percentage_error_pct']:.3f} |"
        )

    report_line_list.extend(
        [
            "",
            "## Artifacts",
            "",
            f"- summary YAML: `{comparison_summary['output_directory']}/validation_summary.yaml`;",
            f"- per-condition CSV: `{comparison_summary['per_condition_metrics_csv_path']}`;",
            f"- grouped report plot root: `{comparison_summary['report_plot_root']}`;",
            f"- grouped report plot count: `{comparison_summary['report_plot_count']}`;",
        ]
    )

    for preview_plot_path in comparison_summary["preview_plot_path_list"]:
        report_line_list.append(f"- preview plot: `{preview_plot_path}`;")

    report_line_list.extend(
        [
            "",
            "## Interpretation",
            "",
            "Rows are ranked by mean percentage error within each source group",
            "and direction. Directional paper-reference, Wave 1, and Wave 2",
            "models are never evaluated on the opposite direction. Global Wave",
            "models remain valid on both directions and are therefore shown in",
            "the directional sections and again in the global breakdown.",
            "The `rcim_track1` forward reference banks use the opposite stored",
            "`h0` sign convention relative to the Track 2 reconstruction",
            "contract, so the Track 2 comparison applies the documented",
            "source-specific `h0` compatibility multiplier before curve",
            "reconstruction.",
            "",
            "## Open Gaps",
            "",
            "- This remains an offline TE-curve comparison and does not replace the",
            "  future online `Table 9` compensation benchmark.",
            "- The report uses the saved Python model artifacts from `models/`; ONNX",
            "  parity checks remain a separate deployment-readiness task.",
        ]
    )

    return "\n".join(report_line_list) + "\n"
