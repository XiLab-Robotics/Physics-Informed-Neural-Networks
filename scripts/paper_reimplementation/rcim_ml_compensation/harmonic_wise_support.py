"""Support utilities for the harmonic-wise offline comparison pipeline."""

from __future__ import annotations

# Import Python Utilities
import pickle
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import numpy as np

# Import Scikit-Learn Utilities
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor

# Import Project Utilities
from scripts.datasets import transmission_error_dataset
from scripts.training import shared_training_infrastructure

HARMONIC_MODEL_FILENAME = "harmonic_model_bundle.pkl"
HARMONIC_REPORT_ROOT = shared_training_infrastructure.PROJECT_PATH / "doc" / "reports" / "analysis" / "validation_checks"
HARMONIC_REPORT_TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"
PLAYBACK_DIRECTION_FLAG_MAP = {
    "forward": float(transmission_error_dataset.FORWARD_DIRECTION_FLAG),
    "backward": float(transmission_error_dataset.BACKWARD_DIRECTION_FLAG),
}


@dataclass
class HarmonicCurveRecord:

    """One TE curve plus its harmonic decomposition targets."""

    source_file_path: Path
    direction_label: str
    direction_flag: float
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    angular_position_deg: np.ndarray
    transmission_error_deg: np.ndarray
    coefficient_dictionary: dict[str, float]
    amplitude_phase_dictionary: dict[str, float]


def load_harmonic_pipeline_config(config_path: str | Path) -> dict[str, Any]:

    """Load one harmonic-wise pipeline configuration file.

    Args:
        config_path: Harmonic-wise YAML configuration path.

    Returns:
        Parsed training-configuration dictionary.
    """

    return shared_training_infrastructure.load_training_config(config_path)


def resolve_selected_harmonic_list(training_config: dict[str, Any]) -> list[int]:

    """Resolve and validate the configured harmonic list."""

    # Read Selected Harmonics
    evaluation_configuration = training_config["evaluation"]
    selected_harmonic_list = [int(harmonic_order) for harmonic_order in evaluation_configuration["selected_harmonics"]]

    # Validate Harmonic Ordering
    assert len(selected_harmonic_list) > 0, "Selected harmonic list must not be empty"
    assert selected_harmonic_list[0] == 0, "Selected harmonic list must start with harmonic 0"
    return selected_harmonic_list


def resolve_feature_term_list(training_config: dict[str, Any]) -> list[str]:

    """Resolve the validated engineered feature term list.

    Args:
        training_config: Harmonic-wise pipeline configuration.

    Returns:
        Ordered engineered feature terms requested by the configuration.

    Raises:
        AssertionError: If unsupported engineered terms are requested.
    """

    # Read Requested Feature Terms
    feature_configuration = training_config.get("features", {})
    configured_feature_term_list = feature_configuration.get("engineered_terms", [])
    feature_term_list = [str(feature_term).strip() for feature_term in configured_feature_term_list if str(feature_term).strip()]

    # Validate Supported Feature Terms
    supported_feature_term_set = {
        "speed_torque_product",
        "speed_temperature_product",
        "torque_temperature_product",
        "speed_squared",
        "torque_squared",
    }
    unsupported_feature_term_list = sorted(set(feature_term_list) - supported_feature_term_set)
    assert not unsupported_feature_term_list, (
        "Unsupported harmonic-wise engineered features requested | "
        f"{', '.join(unsupported_feature_term_list)}"
    )
    return feature_term_list


def build_feature_vector(
    speed_rpm: float,
    torque_nm: float,
    oil_temperature_deg: float,
    direction_flag: float,
    engineered_feature_term_list: list[str] | None = None,
) -> np.ndarray:

    """Build one harmonic-regression feature vector.

    Args:
        speed_rpm: Input speed in revolutions per minute.
        torque_nm: Applied torque in newton meters.
        oil_temperature_deg: Oil temperature in degrees Celsius.
        direction_flag: Encoded motion direction flag.
        engineered_feature_term_list: Optional engineered feature terms.

    Returns:
        Ordered feature vector used by the harmonic estimators.
    """

    # Start From Base Operating Variables
    feature_value_list = [
        float(speed_rpm),
        float(torque_nm),
        float(oil_temperature_deg),
        float(direction_flag),
    ]

    # Append Requested Engineered Terms
    engineered_feature_term_list = engineered_feature_term_list or []
    for feature_term in engineered_feature_term_list:
        if feature_term == "speed_torque_product":
            feature_value_list.append(float(speed_rpm * torque_nm))
            continue
        if feature_term == "speed_temperature_product":
            feature_value_list.append(float(speed_rpm * oil_temperature_deg))
            continue
        if feature_term == "torque_temperature_product":
            feature_value_list.append(float(torque_nm * oil_temperature_deg))
            continue
        if feature_term == "speed_squared":
            feature_value_list.append(float(speed_rpm ** 2))
            continue
        if feature_term == "torque_squared":
            feature_value_list.append(float(torque_nm ** 2))
            continue

    return np.asarray(feature_value_list, dtype=np.float32)


def build_feature_name_list(engineered_feature_term_list: list[str]) -> list[str]:

    """Build the ordered feature-name list for the harmonic predictor."""

    # Start From Base Feature Names
    feature_name_list = [
        "speed_rpm",
        "torque_nm",
        "oil_temperature_deg",
        "direction_flag",
    ]

    # Map Engineered Terms To Stable Names
    feature_name_dictionary = {
        "speed_torque_product": "speed_times_torque",
        "speed_temperature_product": "speed_times_temperature",
        "torque_temperature_product": "torque_times_temperature",
        "speed_squared": "speed_squared",
        "torque_squared": "torque_squared",
    }
    for feature_term in engineered_feature_term_list:
        feature_name_list.append(feature_name_dictionary[feature_term])
    return feature_name_list


def build_target_name_list(selected_harmonic_list: list[int]) -> list[str]:

    """Build the ordered list of model target names."""

    # Seed The Constant Harmonic Target
    target_name_list = ["coefficient_cos_h0"]

    # Expand The Requested Harmonic Orders
    for harmonic_order in selected_harmonic_list:
        if harmonic_order == 0:
            continue
        target_name_list.append(f"coefficient_cos_h{harmonic_order}")
        target_name_list.append(f"coefficient_sin_h{harmonic_order}")
    return target_name_list


def build_harmonic_design_matrix(angular_position_deg: np.ndarray, selected_harmonic_list: list[int]) -> np.ndarray:

    """Build the least-squares design matrix for the selected harmonics."""

    # Convert Positions To Radians
    angle_radians = np.deg2rad(angular_position_deg.astype(np.float64))
    design_column_list = [np.ones_like(angle_radians, dtype=np.float64)]

    # Append Cosine And Sine Harmonic Columns
    for harmonic_order in selected_harmonic_list:
        if harmonic_order == 0:
            continue
        design_column_list.append(np.cos(float(harmonic_order) * angle_radians))
        design_column_list.append(np.sin(float(harmonic_order) * angle_radians))

    return np.column_stack(design_column_list).astype(np.float64)


def decompose_curve_to_harmonic_targets(
    angular_position_deg: np.ndarray,
    transmission_error_deg: np.ndarray,
    selected_harmonic_list: list[int],
    point_stride: int,
) -> tuple[dict[str, float], dict[str, float]]:

    """Decompose one TE curve into harmonic coefficients plus amplitude/phase."""

    # Downsample The Curve Before Solving The Truncated Harmonic Fit
    stride_value = max(int(point_stride), 1)
    reduced_angular_position_deg = angular_position_deg[::stride_value].astype(np.float64)
    reduced_transmission_error_deg = transmission_error_deg[::stride_value].astype(np.float64)

    design_matrix = build_harmonic_design_matrix(reduced_angular_position_deg, selected_harmonic_list)
    coefficient_vector, *_ = np.linalg.lstsq(
        design_matrix,
        reduced_transmission_error_deg,
        rcond=None,
    )

    coefficient_dictionary: dict[str, float] = {}
    amplitude_phase_dictionary: dict[str, float] = {}
    vector_index = 0

    for harmonic_order in selected_harmonic_list:
        if harmonic_order == 0:
            coefficient_cos = float(coefficient_vector[vector_index])
            coefficient_dictionary["coefficient_cos_h0"] = coefficient_cos
            amplitude_phase_dictionary["amplitude_h0"] = abs(coefficient_cos)
            amplitude_phase_dictionary["phase_rad_h0"] = 0.0
            vector_index += 1
            continue

        coefficient_cos = float(coefficient_vector[vector_index])
        coefficient_sin = float(coefficient_vector[vector_index + 1])
        amplitude_value = float(np.sqrt((coefficient_cos ** 2) + (coefficient_sin ** 2)))
        phase_value = float(np.arctan2(-coefficient_sin, coefficient_cos))

        coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"] = coefficient_cos
        coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"] = coefficient_sin
        amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"] = amplitude_value
        amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"] = phase_value
        vector_index += 2

    return coefficient_dictionary, amplitude_phase_dictionary


def build_curve_record(
    csv_file_path: Path,
    direction_label: str,
    selected_harmonic_list: list[int],
    decomposition_point_stride: int,
) -> HarmonicCurveRecord:

    """Build one curve record with decomposition targets."""

    curve_sample = transmission_error_dataset.build_validated_directional_sample(csv_file_path, direction_label)
    coefficient_dictionary, amplitude_phase_dictionary = decompose_curve_to_harmonic_targets(
        curve_sample.angular_position_deg,
        curve_sample.transmission_error_deg,
        selected_harmonic_list,
        decomposition_point_stride,
    )

    return HarmonicCurveRecord(
        source_file_path=curve_sample.source_file_path,
        direction_label=curve_sample.direction_label,
        direction_flag=float(curve_sample.direction_flag),
        speed_rpm=float(curve_sample.speed_rpm),
        torque_nm=float(curve_sample.torque_nm),
        oil_temperature_deg=float(curve_sample.oil_temperature_deg),
        angular_position_deg=curve_sample.angular_position_deg.astype(np.float32),
        transmission_error_deg=curve_sample.transmission_error_deg.astype(np.float32),
        coefficient_dictionary=coefficient_dictionary,
        amplitude_phase_dictionary=amplitude_phase_dictionary,
    )


def build_curve_record_list(
    directional_file_manifest: list[tuple[Path, str]],
    selected_harmonic_list: list[int],
    decomposition_point_stride: int,
) -> list[HarmonicCurveRecord]:

    """Build harmonic curve records for one manifest."""

    curve_record_list: list[HarmonicCurveRecord] = []
    for csv_file_path, direction_label in directional_file_manifest:
        curve_record_list.append(
            build_curve_record(
                csv_file_path.resolve(),
                direction_label,
                selected_harmonic_list,
                decomposition_point_stride,
            )
        )
    return curve_record_list


def build_split_record_bundle(
    training_config: dict[str, Any],
) -> tuple[dict[str, list[HarmonicCurveRecord]], dict[str, int], dict[str, int], Path]:

    """Build train, validation, and test curve bundles for the pipeline."""

    dataset_configuration = transmission_error_dataset.load_dataset_processing_config(
        training_config["paths"]["dataset_config_path"]
    )
    dataset_root = transmission_error_dataset.resolve_project_relative_path(
        dataset_configuration["paths"]["dataset_root"]
    )
    direction_configuration = dataset_configuration["directions"]
    split_configuration = dataset_configuration["split"]
    evaluation_configuration = training_config["evaluation"]

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

    selected_harmonic_list = resolve_selected_harmonic_list(training_config)
    decomposition_point_stride = int(evaluation_configuration["decomposition_point_stride"])

    split_record_bundle = {
        "train": build_curve_record_list(train_manifest, selected_harmonic_list, decomposition_point_stride),
        "validation": build_curve_record_list(validation_manifest, selected_harmonic_list, decomposition_point_stride),
        "test": build_curve_record_list(test_manifest, selected_harmonic_list, decomposition_point_stride),
    }
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
    return split_record_bundle, directional_count_dictionary, file_count_dictionary, dataset_root


def build_feature_target_matrix(
    curve_record_list: list[HarmonicCurveRecord],
    selected_harmonic_list: list[int],
    engineered_feature_term_list: list[str],
) -> tuple[np.ndarray, np.ndarray, list[str], list[str]]:

    """Build feature and target matrices for one split."""

    target_name_list = build_target_name_list(selected_harmonic_list)
    feature_name_list = build_feature_name_list(engineered_feature_term_list)
    feature_matrix = np.asarray(
        [
            build_feature_vector(
                record.speed_rpm,
                record.torque_nm,
                record.oil_temperature_deg,
                record.direction_flag,
                engineered_feature_term_list,
            )
            for record in curve_record_list
        ],
        dtype=np.float32,
    )
    target_matrix = np.asarray(
        [
            [record.coefficient_dictionary[target_name] for target_name in target_name_list]
            for record in curve_record_list
        ],
        dtype=np.float32,
    )
    return feature_matrix, target_matrix, target_name_list, feature_name_list


def resolve_harmonic_order_from_target_name(target_name: str) -> int:

    """Resolve the harmonic order encoded in one target name."""

    return int(str(target_name).split("_h", maxsplit=1)[1])


def build_target_specific_model_configuration(
    model_configuration: dict[str, Any],
    target_name: str,
) -> dict[str, Any]:

    """Build the effective model configuration for one target."""

    effective_model_configuration = dict(model_configuration)
    harmonic_override_dictionary = {
        str(harmonic_order): override_dictionary
        for harmonic_order, override_dictionary in model_configuration.get("harmonic_overrides", {}).items()
    }
    target_harmonic_order = resolve_harmonic_order_from_target_name(target_name)
    target_override_dictionary = harmonic_override_dictionary.get(str(target_harmonic_order), {})
    effective_model_configuration.update(target_override_dictionary)
    return effective_model_configuration


def build_estimator(model_configuration: dict[str, Any], target_name: str):

    """Build one scikit-learn estimator for a harmonic target."""

    estimator_type = str(model_configuration["estimator_type"]).strip().lower()
    random_seed = int(model_configuration.get("random_seed", 42))

    if estimator_type == "hist_gradient_boosting":
        return HistGradientBoostingRegressor(
            learning_rate=float(model_configuration["learning_rate"]),
            max_iter=int(model_configuration["max_iter"]),
            max_depth=int(model_configuration["max_depth"]),
            min_samples_leaf=int(model_configuration["min_samples_leaf"]),
            max_bins=int(model_configuration.get("max_bins", 255)),
            random_state=random_seed,
        )

    if estimator_type == "random_forest":
        return RandomForestRegressor(
            n_estimators=int(model_configuration.get("n_estimators", 300)),
            max_depth=model_configuration.get("max_depth"),
            min_samples_leaf=int(model_configuration.get("min_samples_leaf", 1)),
            n_jobs=int(model_configuration.get("n_jobs", 1)),
            random_state=random_seed,
        )

    raise ValueError(f"Unsupported harmonic-wise estimator_type | {estimator_type}")


def fit_harmonic_target_models(
    feature_matrix: np.ndarray,
    target_matrix: np.ndarray,
    target_name_list: list[str],
    model_configuration: dict[str, Any],
) -> dict[str, Any]:

    """Fit one estimator per harmonic coefficient target."""

    harmonic_model_dictionary: dict[str, Any] = {}
    for target_index, target_name in enumerate(target_name_list):
        estimator = build_estimator(
            build_target_specific_model_configuration(model_configuration, target_name),
            target_name,
        )
        estimator.fit(feature_matrix, target_matrix[:, target_index])
        harmonic_model_dictionary[target_name] = estimator
    return harmonic_model_dictionary


def predict_target_matrix(
    harmonic_model_dictionary: dict[str, Any],
    feature_matrix: np.ndarray,
    target_name_list: list[str],
) -> np.ndarray:

    """Predict the full harmonic target matrix for one feature matrix."""

    prediction_column_list = [
        np.asarray(harmonic_model_dictionary[target_name].predict(feature_matrix), dtype=np.float32).reshape(-1, 1)
        for target_name in target_name_list
    ]
    return np.concatenate(prediction_column_list, axis=1).astype(np.float32)


def target_matrix_to_dictionary(
    target_vector: np.ndarray,
    target_name_list: list[str],
    selected_harmonic_list: list[int],
) -> tuple[dict[str, float], dict[str, float]]:

    """Convert one target vector into coefficient and amplitude/phase dictionaries."""

    coefficient_dictionary = {
        target_name: float(target_vector[target_index])
        for target_index, target_name in enumerate(target_name_list)
    }
    amplitude_phase_dictionary: dict[str, float] = {
        "amplitude_h0": abs(float(coefficient_dictionary["coefficient_cos_h0"])),
        "phase_rad_h0": 0.0,
    }

    for harmonic_order in selected_harmonic_list:
        if harmonic_order == 0:
            continue

        coefficient_cos = coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"]
        coefficient_sin = coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"]
        amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"] = float(
            np.sqrt((coefficient_cos ** 2) + (coefficient_sin ** 2))
        )
        amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"] = float(
            np.arctan2(-coefficient_sin, coefficient_cos)
        )

    return coefficient_dictionary, amplitude_phase_dictionary


def reconstruct_curve_from_coefficients(
    angular_position_deg: np.ndarray,
    selected_harmonic_list: list[int],
    coefficient_dictionary: dict[str, float],
) -> np.ndarray:

    """Reconstruct one TE curve from harmonic coefficients."""

    angle_radians = np.deg2rad(angular_position_deg.astype(np.float64))
    reconstructed_curve = np.zeros_like(angle_radians, dtype=np.float64)

    for harmonic_order in selected_harmonic_list:
        if harmonic_order == 0:
            reconstructed_curve += float(coefficient_dictionary["coefficient_cos_h0"])
            continue

        reconstructed_curve += (
            float(coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"]) * np.cos(float(harmonic_order) * angle_radians)
            + float(coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"]) * np.sin(float(harmonic_order) * angle_radians)
        )

    return reconstructed_curve.astype(np.float32)


def compute_curve_metric_dictionary(
    target_curve_deg: np.ndarray,
    predicted_curve_deg: np.ndarray,
    percentage_error_denominator: str,
) -> dict[str, float]:

    """Compute offline TE-curve error metrics.

    Args:
        target_curve_deg: Reference TE curve in degrees.
        predicted_curve_deg: Predicted TE curve in degrees.
        percentage_error_denominator: Percentage-denominator selection policy.

    Returns:
        Aggregate curve-error metrics for one reconstructed curve.
    """

    # Prepare Flat Float64 Curves
    target_curve = target_curve_deg.astype(np.float64).reshape(-1)
    predicted_curve = predicted_curve_deg.astype(np.float64).reshape(-1)
    residual_curve = predicted_curve - target_curve

    # Compute Absolute And Squared Error Metrics
    mse = float(np.mean(np.square(residual_curve)))
    mae = float(np.mean(np.abs(residual_curve)))
    rmse = float(np.sqrt(mse))

    # Resolve Percentage Denominator
    if percentage_error_denominator == "peak_to_peak_truth":
        denominator_value = float(np.ptp(target_curve))
    else:
        denominator_value = float(np.mean(np.abs(target_curve)))

    # Compute Relative Error Percentage
    denominator_value = max(denominator_value, 1.0e-8)
    mean_percentage_error_pct = float(100.0 * np.mean(np.abs(residual_curve)) / denominator_value)

    return {
        "mse": mse,
        "mae": mae,
        "rmse": rmse,
        "mean_percentage_error_pct": mean_percentage_error_pct,
    }


def average_metric_dictionary(metric_dictionary_list: list[dict[str, float]]) -> dict[str, float]:

    """Average a list of curve-level metric dictionaries."""

    assert len(metric_dictionary_list) > 0, "Metric dictionary list must not be empty"
    metric_name_list = list(metric_dictionary_list[0].keys())
    return {
        metric_name: float(np.mean([metric_dictionary[metric_name] for metric_dictionary in metric_dictionary_list]))
        for metric_name in metric_name_list
    }


def compute_harmonic_target_metric_dictionary(
    target_matrix: np.ndarray,
    prediction_matrix: np.ndarray,
) -> dict[str, float]:

    """Compute aggregate coefficient-prediction metrics.

    Args:
        target_matrix: Reference harmonic coefficient matrix.
        prediction_matrix: Predicted harmonic coefficient matrix.

    Returns:
        Aggregate coefficient-level MSE, MAE, and RMSE metrics.
    """

    # Compute Aggregate Residual Matrix
    residual_matrix = prediction_matrix.astype(np.float64) - target_matrix.astype(np.float64)
    mse = float(np.mean(np.square(residual_matrix)))
    mae = float(np.mean(np.abs(residual_matrix)))
    rmse = float(np.sqrt(mse))
    return {
        "mse": mse,
        "mae": mae,
        "rmse": rmse,
    }


def compute_per_target_metric_dictionary(
    target_matrix: np.ndarray,
    prediction_matrix: np.ndarray,
    target_name_list: list[str],
) -> dict[str, dict[str, float]]:

    """Compute per-target coefficient metrics.

    Args:
        target_matrix: Reference harmonic coefficient matrix.
        prediction_matrix: Predicted harmonic coefficient matrix.
        target_name_list: Ordered harmonic target names.

    Returns:
        Per-target metric dictionary keyed by target name.
    """

    # Accumulate Metrics Per Coefficient Target
    per_target_metric_dictionary: dict[str, dict[str, float]] = {}
    for target_index, target_name in enumerate(target_name_list):
        residual_vector = prediction_matrix[:, target_index].astype(np.float64) - target_matrix[:, target_index].astype(np.float64)
        mse = float(np.mean(np.square(residual_vector)))
        mae = float(np.mean(np.abs(residual_vector)))
        rmse = float(np.sqrt(mse))
        per_target_metric_dictionary[target_name] = {
            "mse": mse,
            "mae": mae,
            "rmse": rmse,
        }
    return per_target_metric_dictionary


def wrap_phase_difference_radians(phase_difference_radians: float) -> float:

    """Wrap one phase difference into the principal interval."""

    return float(np.arctan2(np.sin(phase_difference_radians), np.cos(phase_difference_radians)))


def compute_per_harmonic_metric_dictionary(
    curve_record_list: list[HarmonicCurveRecord],
    prediction_matrix: np.ndarray,
    target_name_list: list[str],
    selected_harmonic_list: list[int],
) -> tuple[dict[str, dict[str, float]], list[dict[str, float]]]:

    """Compute per-harmonic diagnostic metrics and ranking.

    Args:
        curve_record_list: Curve records for the evaluated split.
        prediction_matrix: Predicted harmonic coefficient matrix.
        target_name_list: Ordered harmonic target names.
        selected_harmonic_list: Harmonic orders included in the model.

    Returns:
        Tuple containing per-harmonic summary metrics and the ranked dominant
        harmonic error list.
    """

    # Initialize Per-Harmonic Error Accumulators
    per_harmonic_accumulator_dictionary: dict[str, dict[str, list[float]]] = {}
    for harmonic_order in selected_harmonic_list:
        per_harmonic_accumulator_dictionary[str(harmonic_order)] = {
            "coefficient_abs_error": [],
            "amplitude_abs_error": [],
            "phase_abs_error_rad": [],
        }

    # Accumulate Sample-Level Harmonic Errors
    for sample_index, curve_record in enumerate(curve_record_list):
        predicted_coefficient_dictionary, predicted_amplitude_phase_dictionary = target_matrix_to_dictionary(
            prediction_matrix[sample_index],
            target_name_list,
            selected_harmonic_list,
        )
        for harmonic_order in selected_harmonic_list:
            harmonic_key = str(harmonic_order)
            accumulator_dictionary = per_harmonic_accumulator_dictionary[harmonic_key]

            if harmonic_order == 0:
                coefficient_error = abs(
                    predicted_coefficient_dictionary["coefficient_cos_h0"]
                    - curve_record.coefficient_dictionary["coefficient_cos_h0"]
                )
            else:
                coefficient_error = 0.5 * (
                    abs(
                        predicted_coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"]
                        - curve_record.coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"]
                    )
                    + abs(
                        predicted_coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"]
                        - curve_record.coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"]
                    )
                )

            amplitude_error = abs(
                predicted_amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"]
                - curve_record.amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"]
            )
            phase_error = 0.0
            if harmonic_order != 0:
                phase_error = abs(
                    wrap_phase_difference_radians(
                        predicted_amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"]
                        - curve_record.amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"]
                    )
                )

            accumulator_dictionary["coefficient_abs_error"].append(float(coefficient_error))
            accumulator_dictionary["amplitude_abs_error"].append(float(amplitude_error))
            accumulator_dictionary["phase_abs_error_rad"].append(float(phase_error))

    # Average Harmonic-Level Diagnostics
    per_harmonic_metric_dictionary: dict[str, dict[str, float]] = {}
    for harmonic_key, accumulator_dictionary in per_harmonic_accumulator_dictionary.items():
        per_harmonic_metric_dictionary[harmonic_key] = {
            "coefficient_mae": float(np.mean(accumulator_dictionary["coefficient_abs_error"])),
            "coefficient_rmse": float(np.sqrt(np.mean(np.square(accumulator_dictionary["coefficient_abs_error"])))),
            "amplitude_mae": float(np.mean(accumulator_dictionary["amplitude_abs_error"])),
            "phase_mae_rad": float(np.mean(accumulator_dictionary["phase_abs_error_rad"])),
        }

    dominant_harmonic_error_ranking = [
        {
            "harmonic_order": int(harmonic_key),
            "coefficient_mae": float(metric_dictionary["coefficient_mae"]),
            "amplitude_mae": float(metric_dictionary["amplitude_mae"]),
        }
        for harmonic_key, metric_dictionary in per_harmonic_metric_dictionary.items()
    ]
    dominant_harmonic_error_ranking.sort(key=lambda ranking_entry: ranking_entry["coefficient_mae"], reverse=True)
    return per_harmonic_metric_dictionary, dominant_harmonic_error_ranking


def evaluate_curve_record_split(
    curve_record_list: list[HarmonicCurveRecord],
    harmonic_model_dictionary: dict[str, Any],
    selected_harmonic_list: list[int],
    target_name_list: list[str],
    percentage_error_denominator: str,
    engineered_feature_term_list: list[str],
) -> dict[str, Any]:

    """Evaluate one split by reconstructing TE curves from predicted harmonics."""

    feature_matrix, target_matrix, _, _ = build_feature_target_matrix(
        curve_record_list,
        selected_harmonic_list,
        engineered_feature_term_list,
    )
    prediction_matrix = predict_target_matrix(harmonic_model_dictionary, feature_matrix, target_name_list)
    harmonic_target_metrics = compute_harmonic_target_metric_dictionary(target_matrix, prediction_matrix)
    per_target_metric_dictionary = compute_per_target_metric_dictionary(target_matrix, prediction_matrix, target_name_list)
    per_harmonic_metric_dictionary, dominant_harmonic_error_ranking = compute_per_harmonic_metric_dictionary(
        curve_record_list,
        prediction_matrix,
        target_name_list,
        selected_harmonic_list,
    )

    predicted_curve_metric_list: list[dict[str, float]] = []
    oracle_curve_metric_list: list[dict[str, float]] = []
    sample_preview_list: list[dict[str, Any]] = []

    for sample_index, curve_record in enumerate(curve_record_list):
        predicted_coefficient_dictionary, predicted_amplitude_phase_dictionary = target_matrix_to_dictionary(
            prediction_matrix[sample_index],
            target_name_list,
            selected_harmonic_list,
        )
        predicted_curve_deg = reconstruct_curve_from_coefficients(
            curve_record.angular_position_deg,
            selected_harmonic_list,
            predicted_coefficient_dictionary,
        )
        oracle_curve_deg = reconstruct_curve_from_coefficients(
            curve_record.angular_position_deg,
            selected_harmonic_list,
            curve_record.coefficient_dictionary,
        )

        predicted_curve_metric_dictionary = compute_curve_metric_dictionary(
            curve_record.transmission_error_deg,
            predicted_curve_deg,
            percentage_error_denominator,
        )
        oracle_curve_metric_dictionary = compute_curve_metric_dictionary(
            curve_record.transmission_error_deg,
            oracle_curve_deg,
            percentage_error_denominator,
        )
        predicted_curve_metric_list.append(predicted_curve_metric_dictionary)
        oracle_curve_metric_list.append(oracle_curve_metric_dictionary)

        if sample_index >= 3:
            continue

        sample_preview_list.append(
            {
                "source_file_path": shared_training_infrastructure.format_project_relative_path(curve_record.source_file_path),
                "direction_label": curve_record.direction_label,
                "speed_rpm": float(curve_record.speed_rpm),
                "torque_nm": float(curve_record.torque_nm),
                "oil_temperature_deg": float(curve_record.oil_temperature_deg),
                "predicted_curve_mae_deg": float(predicted_curve_metric_dictionary["mae"]),
                "predicted_curve_rmse_deg": float(predicted_curve_metric_dictionary["rmse"]),
                "predicted_curve_mean_percentage_error_pct": float(predicted_curve_metric_dictionary["mean_percentage_error_pct"]),
                "oracle_curve_mean_percentage_error_pct": float(oracle_curve_metric_dictionary["mean_percentage_error_pct"]),
                "predicted_primary_amplitudes": {
                    f"h{harmonic_order}": float(predicted_amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"])
                    for harmonic_order in selected_harmonic_list[:5]
                },
            }
        )

    return {
        "sample_count": len(curve_record_list),
        "harmonic_target_metrics": harmonic_target_metrics,
        "per_target_metrics": per_target_metric_dictionary,
        "per_harmonic_metrics": per_harmonic_metric_dictionary,
        "dominant_harmonic_error_ranking": dominant_harmonic_error_ranking[:5],
        "curve_metrics": average_metric_dictionary(predicted_curve_metric_list),
        "oracle_curve_metrics": average_metric_dictionary(oracle_curve_metric_list),
        "sample_preview_list": sample_preview_list,
    }


def build_robot_style_profile(
    step_count: int,
    max_speed_rpm: float,
    max_torque_nm: float,
    oil_temperature_deg: float,
) -> dict[str, np.ndarray]:

    """Build a smooth robot-style operating profile.

    Args:
        step_count: Playback sample count.
        max_speed_rpm: Maximum playback speed.
        max_torque_nm: Maximum playback torque.
        oil_temperature_deg: Playback oil temperature.

    Returns:
        Operating-profile dictionary for the robot-style playback scenario.
    """

    # Build Smooth Playback Axes
    normalized_time = np.linspace(0.0, 1.0, step_count, dtype=np.float64)

    # Shape Speed And Torque Profiles
    speed_profile_rpm = max_speed_rpm * np.clip(
        0.35 + 0.55 * np.sin(np.pi * normalized_time) ** 2 + 0.10 * np.sin(4.0 * np.pi * normalized_time),
        0.0,
        1.0,
    )
    torque_profile_nm = max_torque_nm * np.clip(
        0.20 + 0.65 * np.exp(-((normalized_time - 0.55) / 0.20) ** 2) + 0.10 * np.sin(2.0 * np.pi * normalized_time + 0.4),
        0.0,
        1.0,
    )

    # Hold Temperature Constant
    temperature_profile_deg = np.full(step_count, oil_temperature_deg, dtype=np.float64)

    return {
        "normalized_time": normalized_time.astype(np.float32),
        "speed_profile_rpm": speed_profile_rpm.astype(np.float32),
        "torque_profile_nm": torque_profile_nm.astype(np.float32),
        "temperature_profile_deg": temperature_profile_deg.astype(np.float32),
    }


def build_cycloidal_style_profile(
    step_count: int,
    max_speed_rpm: float,
    max_torque_nm: float,
    oil_temperature_deg: float,
) -> dict[str, np.ndarray]:

    """Build a cycloidal-style operating profile.

    Args:
        step_count: Playback sample count.
        max_speed_rpm: Maximum playback speed.
        max_torque_nm: Maximum playback torque.
        oil_temperature_deg: Playback oil temperature.

    Returns:
        Operating-profile dictionary for the cycloidal playback scenario.
    """

    # Build Smooth Playback Axes
    normalized_time = np.linspace(0.0, 1.0, step_count, dtype=np.float64)

    # Shape Speed And Torque Profiles
    speed_profile_rpm = max_speed_rpm * 0.5 * (1.0 - np.cos(2.0 * np.pi * normalized_time))
    torque_profile_nm = max_torque_nm * np.clip(
        0.15 + 0.80 * np.sin(np.pi * normalized_time) ** 2,
        0.0,
        1.0,
    )

    # Hold Temperature Constant
    temperature_profile_deg = np.full(step_count, oil_temperature_deg, dtype=np.float64)

    return {
        "normalized_time": normalized_time.astype(np.float32),
        "speed_profile_rpm": speed_profile_rpm.astype(np.float32),
        "torque_profile_nm": torque_profile_nm.astype(np.float32),
        "temperature_profile_deg": temperature_profile_deg.astype(np.float32),
    }


def run_motion_profile_playback(
    training_config: dict[str, Any],
    harmonic_model_dictionary: dict[str, Any],
    selected_harmonic_list: list[int],
    target_name_list: list[str],
) -> dict[str, Any]:

    """Run offline Robot and Cycloidal style playback from the predicted harmonics."""

    evaluation_configuration = training_config["evaluation"]
    playback_profiles_configuration = training_config["playback_profiles"]
    step_count = int(evaluation_configuration["playback_step_count"])
    angle_probe_count = int(evaluation_configuration["playback_angle_probe_count"])
    playback_direction_label = str(evaluation_configuration["playback_direction_label"]).strip().lower()
    direction_flag = PLAYBACK_DIRECTION_FLAG_MAP[playback_direction_label]
    angle_probe_deg = np.linspace(0.0, 360.0, angle_probe_count, endpoint=False, dtype=np.float32)

    playback_summary_dictionary: dict[str, Any] = {}
    profile_builder_dictionary = {
        "robot": build_robot_style_profile,
        "cycloidal": build_cycloidal_style_profile,
    }

    for profile_name, profile_builder in profile_builder_dictionary.items():
        profile_configuration = playback_profiles_configuration[profile_name]
        profile_dictionary = profile_builder(
            step_count,
            float(profile_configuration["max_speed_rpm"]),
            float(profile_configuration["max_torque_nm"]),
            float(profile_configuration["oil_temperature_deg"]),
        )

        feature_matrix = np.asarray(
            [
                build_feature_vector(
                    float(speed_rpm),
                    float(torque_nm),
                    float(temperature_deg),
                    direction_flag,
                    resolve_feature_term_list(training_config),
                )
                for speed_rpm, torque_nm, temperature_deg in zip(
                    profile_dictionary["speed_profile_rpm"],
                    profile_dictionary["torque_profile_nm"],
                    profile_dictionary["temperature_profile_deg"],
                )
            ],
            dtype=np.float32,
        )
        prediction_matrix = predict_target_matrix(harmonic_model_dictionary, feature_matrix, target_name_list)

        step_rms_list: list[float] = []
        step_max_list: list[float] = []
        for prediction_vector in prediction_matrix:
            predicted_coefficient_dictionary, _ = target_matrix_to_dictionary(
                prediction_vector,
                target_name_list,
                selected_harmonic_list,
            )
            reconstructed_curve_deg = reconstruct_curve_from_coefficients(
                angle_probe_deg,
                selected_harmonic_list,
                predicted_coefficient_dictionary,
            )
            step_rms_list.append(float(np.sqrt(np.mean(np.square(reconstructed_curve_deg.astype(np.float64))))))
            step_max_list.append(float(np.max(np.abs(reconstructed_curve_deg.astype(np.float64)))))

        playback_summary_dictionary[profile_name] = {
            "profile_style": f"{profile_name}_style_offline_playback",
            "step_count": step_count,
            "angle_probe_count": angle_probe_count,
            "direction_label": playback_direction_label,
            "max_speed_rpm": float(np.max(profile_dictionary["speed_profile_rpm"])),
            "max_torque_nm": float(np.max(profile_dictionary["torque_profile_nm"])),
            "oil_temperature_deg": float(profile_configuration["oil_temperature_deg"]),
            "mean_reconstructed_te_rms_deg": float(np.mean(step_rms_list)),
            "max_reconstructed_te_rms_deg": float(np.max(step_rms_list)),
            "mean_reconstructed_te_max_deg": float(np.mean(step_max_list)),
            "peak_reconstructed_te_max_deg": float(np.max(step_max_list)),
        }

    return playback_summary_dictionary


def build_validation_summary(
    config_path: Path,
    output_directory: Path,
    training_config: dict[str, Any],
    selected_harmonic_list: list[int],
    directional_count_dictionary: dict[str, int],
    file_count_dictionary: dict[str, int],
    validation_evaluation: dict[str, Any],
    test_evaluation: dict[str, Any],
    playback_summary_dictionary: dict[str, Any],
    feature_name_list: list[str],
) -> dict[str, Any]:

    """Build the persisted validation summary for the harmonic pipeline."""

    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    model_configuration = training_config["model"]
    evaluation_configuration = training_config["evaluation"]
    target_a_threshold = 4.7
    test_percentage_error = float(test_evaluation["curve_metrics"]["mean_percentage_error_pct"])

    return {
        "schema_version": 1,
        "config_path": shared_training_infrastructure.format_project_relative_path(config_path),
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "experiment": {
            "run_name": experiment_identity.run_name,
            "output_run_name": shared_training_infrastructure.resolve_output_run_name(training_config),
            "run_instance_id": shared_training_infrastructure.resolve_run_instance_id(training_config),
            "model_family": experiment_identity.model_family,
            "model_type": experiment_identity.model_type,
        },
        "harmonic_configuration": {
            "selected_harmonics": [int(harmonic_order) for harmonic_order in selected_harmonic_list],
            "decomposition_point_stride": int(evaluation_configuration["decomposition_point_stride"]),
            "percentage_error_denominator": str(evaluation_configuration["percentage_error_denominator"]),
        },
        "feature_configuration": {
            "feature_name_list": feature_name_list,
            "engineered_feature_terms": resolve_feature_term_list(training_config),
        },
        "split_counts": {
            "train_directional_curve_count": directional_count_dictionary["train"],
            "validation_directional_curve_count": directional_count_dictionary["validation"],
            "test_directional_curve_count": directional_count_dictionary["test"],
            "train_file_count": file_count_dictionary["train"],
            "validation_file_count": file_count_dictionary["validation"],
            "test_file_count": file_count_dictionary["test"],
        },
        "model_configuration": {
            "estimator_type": str(model_configuration["estimator_type"]),
            "learning_rate": float(model_configuration.get("learning_rate", 0.0)),
            "max_iter": int(model_configuration.get("max_iter", 0)),
            "max_depth": int(model_configuration.get("max_depth", 0)),
            "min_samples_leaf": int(model_configuration.get("min_samples_leaf", 0)),
            "n_estimators": int(model_configuration.get("n_estimators", 0)),
            "harmonic_overrides": model_configuration.get("harmonic_overrides", {}),
        },
        "validation_metrics": validation_evaluation,
        "test_metrics": test_evaluation,
        "playback_summary": playback_summary_dictionary,
        "paper_reference_alignment": {
            "target_a_threshold_mean_percentage_error_pct": target_a_threshold,
            "test_mean_percentage_error_pct": test_percentage_error,
            "target_a_status": "met" if test_percentage_error <= target_a_threshold else "not_yet_met",
            "comparison_scope": "offline_only",
        },
    }


def build_validation_report_path(training_config: dict[str, Any]) -> Path:

    """Build the Markdown report path for one harmonic-wise validation run."""

    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    output_run_name = shared_training_infrastructure.resolve_output_run_name(training_config)
    timestamp_string = datetime.now().strftime(HARMONIC_REPORT_TIMESTAMP_FORMAT)
    validation_report_filename = (
        f"{timestamp_string}_{shared_training_infrastructure.sanitize_name(experiment_identity.model_family)}_"
        f"{shared_training_infrastructure.sanitize_name(output_run_name)}_harmonic_wise_comparison_report.md"
    )
    validation_report_path = HARMONIC_REPORT_ROOT / validation_report_filename
    validation_report_path.parent.mkdir(parents=True, exist_ok=True)
    return validation_report_path


def build_harmonic_report_markdown(validation_summary: dict[str, Any]) -> str:

    """Build the human-readable Markdown report for one harmonic-wise run."""

    experiment_dictionary = validation_summary["experiment"]
    harmonic_configuration = validation_summary["harmonic_configuration"]
    feature_configuration = validation_summary["feature_configuration"]
    split_counts = validation_summary["split_counts"]
    validation_metrics = validation_summary["validation_metrics"]
    test_metrics = validation_summary["test_metrics"]
    playback_summary = validation_summary["playback_summary"]
    paper_reference_alignment = validation_summary["paper_reference_alignment"]

    playback_row_list = []
    for profile_name, profile_dictionary in playback_summary.items():
        playback_row_list.append(
            f"| `{profile_name}` | {profile_dictionary['step_count']} | "
            f"{profile_dictionary['mean_reconstructed_te_rms_deg']:.6f} | "
            f"{profile_dictionary['peak_reconstructed_te_max_deg']:.6f} | "
            f"{profile_dictionary['max_speed_rpm']:.1f} | "
            f"{profile_dictionary['max_torque_nm']:.1f} | "
            f"{profile_dictionary['oil_temperature_deg']:.1f} |"
        )

    preview_bullet_list = []
    for preview_dictionary in test_metrics["sample_preview_list"]:
        preview_bullet_list.append(
            "- "
            f"`{preview_dictionary['source_file_path']}` | "
            f"{preview_dictionary['direction_label']} | "
            f"mean percentage error `{preview_dictionary['predicted_curve_mean_percentage_error_pct']:.3f}%` | "
            f"curve MAE `{preview_dictionary['predicted_curve_mae_deg']:.6f}`"
        )

    return "\n".join([
        "# Harmonic-Wise Comparison Pipeline Report",
        "",
        "## Overview",
        "",
        "This report summarizes one repository-owned offline validation run of the paper-aligned harmonic-wise comparison pipeline.",
        "",
        f"- model family: `{experiment_dictionary['model_family']}`;",
        f"- model type: `{experiment_dictionary['model_type']}`;",
        f"- run name: `{experiment_dictionary['run_name']}`;",
        f"- output run name: `{experiment_dictionary['output_run_name']}`;",
        f"- run instance id: `{experiment_dictionary['run_instance_id']}`;",
        f"- comparison scope: `{paper_reference_alignment['comparison_scope']}`;",
        f"- `Target A` status: **{paper_reference_alignment['target_a_status']}**",
        "",
        "## Harmonic Configuration",
        "",
        f"- selected harmonics: `{', '.join(str(harmonic_order) for harmonic_order in harmonic_configuration['selected_harmonics'])}`",
        f"- decomposition point stride: `{harmonic_configuration['decomposition_point_stride']}`",
        f"- percentage-error denominator: `{harmonic_configuration['percentage_error_denominator']}`",
        f"- feature terms: `{', '.join(feature_configuration['engineered_feature_terms']) if feature_configuration['engineered_feature_terms'] else 'base_only'}`",
        "",
        "## Split Coverage",
        "",
        "| Split | Directional Curves | Files |",
        "| --- | ---: | ---: |",
        f"| Train | {split_counts['train_directional_curve_count']} | {split_counts['train_file_count']} |",
        f"| Validation | {split_counts['validation_directional_curve_count']} | {split_counts['validation_file_count']} |",
        f"| Test | {split_counts['test_directional_curve_count']} | {split_counts['test_file_count']} |",
        "",
        "## Offline Curve Reconstruction Metrics",
        "",
        "| Split | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | Oracle Mean Percentage Error [%] | Harmonic Target MAE |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        f"| Validation | {validation_metrics['curve_metrics']['mae']:.6f} | {validation_metrics['curve_metrics']['rmse']:.6f} | {validation_metrics['curve_metrics']['mean_percentage_error_pct']:.3f} | {validation_metrics['oracle_curve_metrics']['mean_percentage_error_pct']:.3f} | {validation_metrics['harmonic_target_metrics']['mae']:.6f} |",
        f"| Test | {test_metrics['curve_metrics']['mae']:.6f} | {test_metrics['curve_metrics']['rmse']:.6f} | {test_metrics['curve_metrics']['mean_percentage_error_pct']:.3f} | {test_metrics['oracle_curve_metrics']['mean_percentage_error_pct']:.3f} | {test_metrics['harmonic_target_metrics']['mae']:.6f} |",
        "",
        "## Paper Alignment",
        "",
        f"- Paper offline threshold for `Target A`: `{paper_reference_alignment['target_a_threshold_mean_percentage_error_pct']:.1f}%` mean percentage error.",
        f"- Current repository test result: `{paper_reference_alignment['test_mean_percentage_error_pct']:.3f}%` mean percentage error.",
        f"- Current verdict: `{paper_reference_alignment['target_a_status']}`.",
        f"- Oracle truncation-only test error with the selected harmonics: `{test_metrics['oracle_curve_metrics']['mean_percentage_error_pct']:.3f}%`.",
        "",
        "## Per-Harmonic Error Diagnostics",
        "",
        "| Harmonic | Coefficient MAE | Coefficient RMSE | Amplitude MAE | Phase MAE [rad] |",
        "| --- | ---: | ---: | ---: | ---: |",
        *[
            (
                f"| `h{harmonic_order}` | "
                f"{test_metrics['per_harmonic_metrics'][str(harmonic_order)]['coefficient_mae']:.6f} | "
                f"{test_metrics['per_harmonic_metrics'][str(harmonic_order)]['coefficient_rmse']:.6f} | "
                f"{test_metrics['per_harmonic_metrics'][str(harmonic_order)]['amplitude_mae']:.6f} | "
                f"{test_metrics['per_harmonic_metrics'][str(harmonic_order)]['phase_mae_rad']:.6f} |"
            )
            for harmonic_order in harmonic_configuration['selected_harmonics']
        ],
        "",
        "Top coefficient-error contributors on the test split:",
        "",
        *[
            (
                f"- `h{ranking_entry['harmonic_order']}` | coefficient MAE "
                f"`{ranking_entry['coefficient_mae']:.6f}` | amplitude MAE "
                f"`{ranking_entry['amplitude_mae']:.6f}`"
            )
            for ranking_entry in test_metrics["dominant_harmonic_error_ranking"]
        ],
        "",
        "## Offline Motion-Profile Playback",
        "",
        "These playback summaries are repository-owned `Robot` and `Cycloidal` style offline probes built from the predicted harmonic stack. They are not yet the final online `Table 9` benchmark.",
        "",
        "| Profile | Step Count | Mean Reconstructed TE RMS [deg] | Peak Reconstructed TE Max [deg] | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        *playback_row_list,
        "",
        "## Test Preview Samples",
        "",
        *(preview_bullet_list if preview_bullet_list else ["- No preview samples were collected."]),
        "",
        "## Interpretation",
        "",
        "The harmonic-wise pipeline is now implemented as a repository-owned offline benchmark path. The key comparison number is the TE-curve mean percentage error on held-out curves, while the offline playback block prepares the later online branch without claiming a real `Table 9` equivalence yet.",
        "",
    ]) + "\n"


def save_harmonic_model_bundle(
    harmonic_model_dictionary: dict[str, Any],
    output_directory: Path,
    selected_harmonic_list: list[int],
    target_name_list: list[str],
) -> Path:

    """Save the fitted harmonic model bundle.

    Args:
        harmonic_model_dictionary: Fitted per-target estimator dictionary.
        output_directory: Output artifact directory for the current run.
        selected_harmonic_list: Harmonic orders included in the bundle.
        target_name_list: Ordered target names predicted by the bundle.

    Returns:
        Serialized harmonic-model bundle path.
    """

    # Resolve Bundle Output Path
    model_bundle_path = output_directory / HARMONIC_MODEL_FILENAME

    # Serialize Bundle Payload
    with model_bundle_path.open("wb") as output_file:
        pickle.dump(
            {
                "selected_harmonics": selected_harmonic_list,
                "target_name_list": target_name_list,
                "model_dictionary": harmonic_model_dictionary,
            },
            output_file,
        )
    return model_bundle_path
