from __future__ import annotations

# Import Python Utilities
import pickle
from dataclasses import asdict
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import numpy as np

# Import Scikit-Learn Utilities
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor

# Import Project Utilities
from scripts.training import shared_training_infrastructure
from scripts.training.transmission_error_datamodule import DatasetSplitSummary
from scripts.training.transmission_error_datamodule import NormalizationStatistics
from scripts.training.transmission_error_datamodule import extract_point_tensor_from_curve_sample

TREE_MODEL_FILENAME = "tree_model.pkl"
TREE_VALIDATION_SAMPLE_COUNT = 2048
TREE_SMOKE_TRAIN_SAMPLE_COUNT = 4096
TREE_SMOKE_EVAL_SAMPLE_COUNT = 1024

def flatten_curve_dataset_to_numpy(
    curve_dataset,
    point_stride: int,
    maximum_points_per_curve: int | None,
    maximum_total_point_count: int | None = None,
) -> tuple[np.ndarray, np.ndarray]:

    """ Flatten Curve Dataset To Numpy """

    input_array_list: list[np.ndarray] = []
    target_array_list: list[np.ndarray] = []
    collected_point_count = 0

    for dataset_index in range(len(curve_dataset)):

        # Extract Point Sample Dictionary From The Current Curve
        curve_sample_dictionary = curve_dataset[dataset_index]
        point_sample_dictionary = extract_point_tensor_from_curve_sample(
            curve_sample_dictionary,
            point_stride,
            maximum_points_per_curve,
        )

        # Convert Point Tensors To Numpy Arrays
        input_array = point_sample_dictionary["input_tensor"].cpu().numpy().astype(np.float32)
        target_array = point_sample_dictionary["target_tensor"].cpu().numpy().astype(np.float32)

        # Optionally Truncate The Final Curve Contribution To Respect The Requested Point Budget
        if maximum_total_point_count is not None:
            remaining_point_budget = maximum_total_point_count - collected_point_count
            if remaining_point_budget <= 0:
                break
            input_array = input_array[:remaining_point_budget]
            target_array = target_array[:remaining_point_budget]

        # Append Point Tensors To The List
        input_array_list.append(input_array)
        target_array_list.append(target_array)
        collected_point_count += int(input_array.shape[0])

    # Concatenate Point Tensors
    assert len(input_array_list) > 0, "Flattened input array list is empty"
    input_feature_matrix = np.concatenate(input_array_list, axis=0)
    target_vector = np.concatenate(target_array_list, axis=0).reshape(-1)
    return input_feature_matrix, target_vector

def build_tree_split_bundle(training_config: dict[str, Any]) -> tuple[Any, dict[str, np.ndarray]]:

    """ Build Tree Split Bundle """

    # Build Datamodule
    datamodule = shared_training_infrastructure.create_datamodule_from_training_config(training_config)
    datamodule.setup(stage="fit")

    # Validate Dataset Initialization
    assert datamodule.train_dataset is not None, "Train Dataset is not initialized"
    assert datamodule.validation_dataset is not None, "Validation Dataset is not initialized"
    assert datamodule.test_dataset is not None, "Test Dataset is not initialized"

    # Build Split Dictionary From Datasets
    dataset_configuration = training_config["dataset"]
    point_stride = int(dataset_configuration["point_stride"])
    maximum_points_per_curve = dataset_configuration["maximum_points_per_curve"]
    train_input, train_target = flatten_curve_dataset_to_numpy(datamodule.train_dataset, point_stride, maximum_points_per_curve)
    validation_input, validation_target = flatten_curve_dataset_to_numpy(datamodule.validation_dataset, point_stride, maximum_points_per_curve)
    test_input, test_target = flatten_curve_dataset_to_numpy(datamodule.test_dataset, point_stride, maximum_points_per_curve)

    # Build Split Dictionary
    split_dictionary = {
        "train_input": train_input,
        "train_target": train_target,
        "validation_input": validation_input,
        "validation_target": validation_target,
        "test_input": test_input,
        "test_target": test_target,
    }

    return datamodule, split_dictionary

def build_tree_estimator(training_config: dict[str, Any]):

    """ Build Tree Estimator """

    # Build Estimator
    model_type = str(training_config["experiment"]["model_type"]).strip().lower()
    model_configuration = training_config["model"]
    random_seed = int(training_config.get("metadata", {}).get("random_seed", 42))

    # Build Random Forest Regressor
    if model_type == "random_forest":
        return RandomForestRegressor(
            n_estimators=int(model_configuration["n_estimators"]),
            max_depth=model_configuration.get("max_depth"),
            min_samples_leaf=int(model_configuration.get("min_samples_leaf", 1)),
            n_jobs=int(model_configuration.get("n_jobs", -1)),
            random_state=random_seed,
        )

    # Build Hist Gradient Boosting Regressor
    if model_type == "hist_gradient_boosting":
        return HistGradientBoostingRegressor(
            learning_rate=float(model_configuration["learning_rate"]),
            max_iter=int(model_configuration["max_iter"]),
            max_depth=model_configuration.get("max_depth"),
            min_samples_leaf=int(model_configuration.get("min_samples_leaf", 20)),
            max_bins=int(model_configuration.get("max_bins", 255)),
            random_state=random_seed,
        )

    raise ValueError(f"Unsupported Tree Model Type | {model_type}")

def compute_regression_metric_dictionary(target_vector: np.ndarray, prediction_vector: np.ndarray) -> dict[str, float]:

    """ Compute Regression Metric Dictionary """

    # Compute Regression Metrics
    residual_vector = prediction_vector.reshape(-1) - target_vector.reshape(-1)
    mse = float(np.mean(np.square(residual_vector)))
    mae = float(np.mean(np.abs(residual_vector)))
    rmse = float(np.sqrt(mse))

    return {
        "loss": mse,
        "mae": mae,
        "rmse": rmse,
    }

def resolve_tree_parameter_summary(training_config: dict[str, Any], estimator) -> shared_training_infrastructure.ModelParameterSummary:

    """ Resolve Tree Parameter Summary """

    # Resolve Tree Parameter Summary
    model_configuration = training_config["model"]

    # Compute Total Parameter Count
    if hasattr(estimator, "n_features_in_"): total_parameter_count = int(estimator.n_features_in_)
    else: total_parameter_count = int(model_configuration.get("n_estimators", model_configuration.get("max_iter", 0)))

    # Return Model Parameter Summary
    return shared_training_infrastructure.ModelParameterSummary(
        backbone_name=estimator.__class__.__name__,
        trainable_parameter_count=total_parameter_count,
        frozen_parameter_count=0,
        total_parameter_count=total_parameter_count,
    )

def build_tree_runtime_config(training_config: dict[str, Any]) -> dict[str, object]:

    """ Build Tree Runtime Config """

    # Build Runtime Config
    runtime_configuration = shared_training_infrastructure.resolve_runtime_config(training_config)
    runtime_configuration["estimator_backend"] = "scikit-learn"
    runtime_configuration["precision"] = "n/a"
    runtime_configuration["benchmark"] = False
    runtime_configuration["use_non_blocking_transfer"] = False
    return runtime_configuration

def build_tree_metrics_snapshot(
    training_config: dict[str, Any],
    config_path: Path,
    output_directory: Path,
    datamodule,
    parameter_summary: shared_training_infrastructure.ModelParameterSummary,
    runtime_config: dict[str, object],
    model_artifact_path: Path,
    validation_metric_dictionary: dict[str, float],
    test_metric_dictionary: dict[str, float],
) -> dict[str, object]:

    """ Build Tree Metrics Snapshot """

    # Resolve Experiment Identity and Dataset Split Summary for Snapshot
    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    run_artifact_identity = shared_training_infrastructure.resolve_run_artifact_identity(training_config)
    dataset_split_summary = datamodule.get_dataset_split_summary()
    normalization_statistics = datamodule.get_normalization_statistics()

    # Serialize Validation Metric Dictionary for Snapshot
    serialized_validation_metric_dictionary = {
        "val_loss": float(validation_metric_dictionary["loss"]),
        "val_mae": float(validation_metric_dictionary["mae"]),
        "val_rmse": float(validation_metric_dictionary["rmse"]),
    }

    # Serialize Test Metric Dictionary for Snapshot
    serialized_test_metric_dictionary = {
        "test_loss": float(test_metric_dictionary["loss"]),
        "test_mae": float(test_metric_dictionary["mae"]),
        "test_rmse": float(test_metric_dictionary["rmse"]),
    }

    return {
        "schema_version": 1,
        "config_path": str(shared_training_infrastructure.resolve_project_relative_path(config_path)),
        "experiment": {
            **asdict(experiment_identity),
            "output_run_name": run_artifact_identity.run_name,
            "run_instance_id": run_artifact_identity.run_instance_id,
            "output_artifact_kind": run_artifact_identity.artifact_kind,
        },
        "artifacts": {
            "output_directory": str(output_directory),
            "best_checkpoint_path": str(model_artifact_path),
        },
        "dataset_split": asdict(dataset_split_summary),
        "model_summary": asdict(parameter_summary),
        "runtime_config": runtime_config,
        "normalization_statistics": {
            "input_feature_mean": [float(value) for value in normalization_statistics.input_feature_mean.tolist()],
            "input_feature_std": [float(value) for value in normalization_statistics.input_feature_std.tolist()],
            "target_mean": [float(value) for value in normalization_statistics.target_mean.tolist()],
            "target_std": [float(value) for value in normalization_statistics.target_std.tolist()],
        },
        "validation_metrics": serialized_validation_metric_dictionary,
        "test_metrics": serialized_test_metric_dictionary,
        "comparison_payload": {
            "model_family": experiment_identity.model_family,
            "model_type": experiment_identity.model_type,
            "run_name": experiment_identity.run_name,
            "backbone_name": parameter_summary.backbone_name,
            "trainable_parameter_count": parameter_summary.trainable_parameter_count,
            "total_parameter_count": parameter_summary.total_parameter_count,
            "val_mae": serialized_validation_metric_dictionary["val_mae"],
            "val_rmse": serialized_validation_metric_dictionary["val_rmse"],
            "test_mae": serialized_test_metric_dictionary["test_mae"],
            "test_rmse": serialized_test_metric_dictionary["test_rmse"],
            "deployment_notes": "",
            "interpretability_notes": "",
        },
    }

def save_tree_model(estimator, output_directory: Path) -> Path:

    """ Save Tree Model """

    # Save Model Artifact
    model_artifact_path = output_directory / TREE_MODEL_FILENAME
    with model_artifact_path.open("wb") as output_file:
        pickle.dump(estimator, output_file)
    return model_artifact_path

def load_tree_model(model_artifact_path: Path):

    """ Load Tree Model """

    # Load Model Artifact
    with model_artifact_path.open("rb") as input_file:
        return pickle.load(input_file)
