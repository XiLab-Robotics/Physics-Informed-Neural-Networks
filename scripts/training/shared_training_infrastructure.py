from __future__ import annotations

# Import Python Utilities
from copy import deepcopy
from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import YAML Utilities
import yaml

# Import Project Utilities
from scripts.datasets.transmission_error_dataset import resolve_project_relative_path
from scripts.models.model_factory import create_model
from scripts.training.transmission_error_datamodule import NormalizationStatistics
from scripts.training.transmission_error_datamodule import TransmissionErrorDataModule
from scripts.training.transmission_error_regression_module import TransmissionErrorRegressionModule

PROJECT_PATH = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = PROJECT_PATH / "config" / "training" / "feedforward" / "presets" / "baseline.yaml"
DEFAULT_RUNTIME_CONFIG_DICTIONARY = {
    "accelerator": "auto",
    "devices": "auto",
    "precision": "32",
    "benchmark": True,
    "use_non_blocking_transfer": True,
}
COMMON_TRAINING_CONFIG_FILENAME = "training_config.yaml"
COMMON_METRICS_FILENAME = "metrics_summary.yaml"
COMMON_VALIDATION_FILENAME = "validation_summary.yaml"
COMMON_SMOKE_TEST_FILENAME = "smoke_test_summary.yaml"
LEGACY_FEEDFORWARD_CONFIG_FILENAME = "feedforward_network_training.yaml"
LEGACY_FEEDFORWARD_METRICS_FILENAME = "training_test_metrics.yaml"

@dataclass
class ExperimentIdentity:

    """ Experiment Identity """

    model_family: str
    model_type: str
    run_name: str

@dataclass
class ModelParameterSummary:

    """ Model Parameter Summary """

    backbone_name: str
    trainable_parameter_count: int
    frozen_parameter_count: int
    total_parameter_count: int

def load_training_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:

    """ Load Training Config """

    # Resolve Config Path
    resolved_config_path = resolve_project_relative_path(config_path)
    assert resolved_config_path.exists(), f"Training Config Path does not exist | {resolved_config_path}"

    # Load YAML Configuration
    with resolved_config_path.open("r", encoding="utf-8") as config_file:
        training_config = yaml.safe_load(config_file)

    # Validate Configuration Type
    assert isinstance(training_config, dict), "Training Config must be a dictionary"
    return training_config

def clone_training_config(training_config: dict[str, Any]) -> dict[str, Any]:

    """ Clone Training Config """

    return deepcopy(training_config)

def resolve_experiment_identity(training_config: dict[str, Any]) -> ExperimentIdentity:

    """ Resolve Experiment Identity """

    experiment_config = training_config["experiment"]

    # Extract and Validate Experiment Identity Components
    model_type = str(experiment_config["model_type"]).strip()
    assert model_type, "Experiment model_type must not be empty"

    # Extract model_family with Fallback to model_type if not Explicitly Provided
    model_family = str(experiment_config.get("model_family", model_type)).strip().lower()
    assert model_family, "Experiment model_family must not be empty"

    # Extract and Validate run_name
    run_name = str(experiment_config["run_name"]).strip()
    assert run_name, "Experiment run_name must not be empty"

    return ExperimentIdentity(
        model_family=model_family,
        model_type=model_type.lower(),
        run_name=run_name,
    )

def resolve_runtime_config(training_config: dict[str, Any]) -> dict[str, object]:

    """ Resolve Runtime Config """

    # Start with Default Runtime Config and Update with Training Config Overrides
    runtime_config = dict(DEFAULT_RUNTIME_CONFIG_DICTIONARY)
    raw_runtime_config = training_config.get("runtime", {})

    if isinstance(raw_runtime_config, dict):
        runtime_config.update(raw_runtime_config)

    if bool(training_config["training"]["deterministic"]):
        runtime_config["benchmark"] = False

    return runtime_config

def build_run_name(training_config: dict[str, Any], run_name_suffix: str | None = None) -> str:

    """ Build Run Name """

    # Construct Run Name with Optional Suffix for Uniqueness if Needed
    experiment_identity = resolve_experiment_identity(training_config)
    if not run_name_suffix: return experiment_identity.run_name
    return f"{experiment_identity.run_name}_{run_name_suffix}"

def resolve_output_directory(training_config: dict[str, Any], run_name_suffix: str | None = None) -> Path:

    """ Resolve Output Directory """

    # Construct Output Directory Path Based on Training Config and Experiment Identity
    output_root = resolve_project_relative_path(training_config["paths"]["output_root"])
    run_name = build_run_name(training_config, run_name_suffix)
    return output_root / run_name

def summarize_model_parameters(regression_backbone: nn.Module) -> ModelParameterSummary:

    """ Summarize Model Parameters """

    # Calculate Trainable, Frozen, and Total Parameter Counts
    trainable_parameter_count = sum(parameter.numel() for parameter in regression_backbone.parameters() if parameter.requires_grad)
    total_parameter_count = sum(parameter.numel() for parameter in regression_backbone.parameters())
    frozen_parameter_count = total_parameter_count - trainable_parameter_count

    # Build and Return ModelParameterSummary Dataclass Instance
    return ModelParameterSummary(
        backbone_name=regression_backbone.__class__.__name__,
        trainable_parameter_count=int(trainable_parameter_count),
        frozen_parameter_count=int(frozen_parameter_count),
        total_parameter_count=int(total_parameter_count),
    )

def create_datamodule_from_training_config(training_config: dict[str, Any]) -> TransmissionErrorDataModule:

    """ Create DataModule From Training Config """

    # Resolve Runtime Config for DataModule Creation
    runtime_config = resolve_runtime_config(training_config)

    # Create and Return TransmissionErrorDataModule
    return TransmissionErrorDataModule(
        dataset_config_path=training_config["paths"]["dataset_config_path"],
        curve_batch_size=int(training_config["dataset"]["curve_batch_size"]),
        point_stride=int(training_config["dataset"]["point_stride"]),
        maximum_points_per_curve=training_config["dataset"]["maximum_points_per_curve"],
        num_workers=int(training_config["dataset"]["num_workers"]),
        pin_memory=bool(training_config["dataset"]["pin_memory"]),
        use_non_blocking_transfer=bool(runtime_config["use_non_blocking_transfer"]),
    )

def create_regression_backbone_from_training_config(training_config: dict[str, Any], input_feature_dim: int) -> nn.Module:

    """ Create Regression Backbone From Training Config """

    # Validate Configured Input Size Matches Dataset Input Feature Dim
    configured_input_size = int(training_config["model"]["input_size"])
    assert configured_input_size == input_feature_dim, (
        f"Configured Input Size and Dataset Input Feature Dim mismatch | {configured_input_size} vs {input_feature_dim}"
    )

    # Create and Return Regression Backbone Model Based on Training Config
    return create_model(
        model_type=str(training_config["experiment"]["model_type"]),
        model_configuration=training_config["model"],
    )

def create_regression_module_from_training_config(
    training_config: dict[str, Any],
    regression_backbone: nn.Module,
    input_feature_dim: int,
    target_feature_dim: int,
    normalization_statistics: NormalizationStatistics,
) -> TransmissionErrorRegressionModule:

    """ Create Regression Module From Training Config """

    # Validate Configured Learning Rate and Weight Decay
    return TransmissionErrorRegressionModule(
        regression_model=regression_backbone,
        input_feature_dim=input_feature_dim,
        target_feature_dim=target_feature_dim,
        learning_rate=float(training_config["training"]["learning_rate"]),
        weight_decay=float(training_config["training"]["weight_decay"]),
        normalization_statistics=normalization_statistics,
    )

def initialize_training_components(
    training_config: dict[str, Any],
) -> tuple[TransmissionErrorDataModule, nn.Module, TransmissionErrorRegressionModule, NormalizationStatistics]:

    """ Initialize Training Components """

    # Create DataModule and Setup to Access Dataset Statistics
    datamodule = create_datamodule_from_training_config(training_config)
    datamodule.setup(stage="fit")

    # Create Regression Backbone and Regression Module Based on Training Config and Dataset Statistics
    input_feature_dim = datamodule.get_input_feature_dim()
    target_feature_dim = datamodule.get_target_feature_dim()
    normalization_statistics = datamodule.get_normalization_statistics()

    # Validate Normalization Statistics Dimensions Match Dataset Feature Dimensions
    regression_backbone = create_regression_backbone_from_training_config(
        training_config,
        input_feature_dim,
    )

    # Validate Normalization Statistics Dimensions Match Dataset Feature Dimensions
    regression_module = create_regression_module_from_training_config(
        training_config,
        regression_backbone,
        input_feature_dim,
        target_feature_dim,
        normalization_statistics,
    )

    return datamodule, regression_backbone, regression_module, normalization_statistics

def fetch_first_batch(datamodule: TransmissionErrorDataModule, split_name: str = "train") -> dict[str, Any]:

    """ Fetch First Batch """

    # Fetch First Batch from Specified Data Split and Return as Dictionary
    if split_name == "train":        dataloader = datamodule.train_dataloader()
    elif split_name == "validation": dataloader = datamodule.val_dataloader()
    elif split_name == "test":       dataloader = datamodule.test_dataloader()
    else: raise ValueError(f"Unsupported split_name | {split_name}")

    return next(iter(dataloader))

def validate_batch_dictionary(batch_dictionary: dict[str, Any], input_feature_dim: int, target_feature_dim: int) -> dict[str, Any]:

    """ Validate Batch Dictionary """

    input_tensor = batch_dictionary["input_tensor"]
    target_tensor = batch_dictionary["target_tensor"]

    # Validate Batch Dictionary Contains Required Tensors with Correct Shapes and Types
    assert isinstance(input_tensor, torch.Tensor), "input_tensor must be a torch.Tensor"
    assert isinstance(target_tensor, torch.Tensor), "target_tensor must be a torch.Tensor"
    assert input_tensor.ndim == 2, f"input_tensor must be rank-2 | {tuple(input_tensor.shape)}"
    assert target_tensor.ndim == 2, f"target_tensor must be rank-2 | {tuple(target_tensor.shape)}"
    assert input_tensor.shape[-1] == input_feature_dim, (f"Input feature mismatch | {input_tensor.shape[-1]} vs {input_feature_dim}")
    assert target_tensor.shape[-1] == target_feature_dim, (f"Target feature mismatch | {target_tensor.shape[-1]} vs {target_feature_dim}")

    return {
        "point_batch_size": int(input_tensor.shape[0]),
        "input_feature_dim": int(input_tensor.shape[-1]),
        "target_feature_dim": int(target_tensor.shape[-1]),
        "curve_count": int(batch_dictionary.get("curve_count", 0)),
    }

def serialize_metric_dictionary(metric_dictionary: dict[str, object]) -> dict[str, object]:

    """ Serialize Metric Dictionary """

    serialized_metric_dictionary: dict[str, object] = {}

    for metric_name, metric_value in metric_dictionary.items():

        # Serialize Metric Values to Ensure They are JSON/YAML Serializable Types
        if isinstance(metric_value, torch.Tensor):
            serialized_metric_dictionary[metric_name] = float(metric_value.detach().cpu().item())
            continue

        # Handle Common Numeric Types Directly
        if isinstance(metric_value, float):
            serialized_metric_dictionary[metric_name] = float(metric_value)
            continue

        # Handle Integer Types Directly
        if isinstance(metric_value, int):
            serialized_metric_dictionary[metric_name] = int(metric_value)
            continue

        # Fallback to String Representation for Unsupported Types
        serialized_metric_dictionary[metric_name] = str(metric_value)

    return serialized_metric_dictionary

def build_comparison_payload(
    experiment_identity: ExperimentIdentity,
    parameter_summary: ModelParameterSummary,
    validation_metric_dictionary: dict[str, object],
    test_metric_dictionary: dict[str, object],
) -> dict[str, object]:

    """ Build Comparison Payload """

    return {
        "model_family": experiment_identity.model_family,
        "model_type": experiment_identity.model_type,
        "run_name": experiment_identity.run_name,
        "backbone_name": parameter_summary.backbone_name,
        "trainable_parameter_count": parameter_summary.trainable_parameter_count,
        "total_parameter_count": parameter_summary.total_parameter_count,
        "val_mae": validation_metric_dictionary.get("val_mae"),
        "val_rmse": validation_metric_dictionary.get("val_rmse"),
        "test_mae": test_metric_dictionary.get("test_mae"),
        "test_rmse": test_metric_dictionary.get("test_rmse"),
        "deployment_notes": "",
        "interpretability_notes": "",
    }

def build_common_metrics_snapshot(
    training_config: dict[str, Any],
    config_path: str | Path,
    datamodule: TransmissionErrorDataModule,
    parameter_summary: ModelParameterSummary,
    runtime_config: dict[str, object],
    best_model_path: str,
    validation_metric_list: list[dict[str, object]],
    test_metric_list: list[dict[str, object]],
) -> dict[str, object]:

    """ Build Common Metrics Snapshot """

    # Resolve Experiment Identity and Dataset Split Summary for Snapshot
    experiment_identity = resolve_experiment_identity(training_config)
    dataset_split_summary = datamodule.get_dataset_split_summary()
    normalization_statistics = datamodule.get_normalization_statistics()

    # Serialize Validation and Test Metric Dictionaries for Snapshot
    validation_metric_dictionary = serialize_metric_dictionary(validation_metric_list[0] if len(validation_metric_list) > 0 else {})
    test_metric_dictionary = serialize_metric_dictionary(test_metric_list[0] if len(test_metric_list) > 0 else {})

    return {
        "schema_version": 1,
        "config_path": str(resolve_project_relative_path(config_path)),
        "experiment": asdict(experiment_identity),
        "artifacts": {
            "best_checkpoint_path": best_model_path,
        },
        "dataset_split": asdict(dataset_split_summary),
        "model_summary": asdict(parameter_summary),
        "runtime_config": {key: str(value) if isinstance(value, Path) else value for key, value in runtime_config.items()},
        "normalization_statistics": {
            "input_feature_mean": [float(value) for value in normalization_statistics.input_feature_mean.tolist()],
            "input_feature_std": [float(value) for value in normalization_statistics.input_feature_std.tolist()],
            "target_mean": [float(value) for value in normalization_statistics.target_mean.tolist()],
            "target_std": [float(value) for value in normalization_statistics.target_std.tolist()],
        },
        "validation_metrics": validation_metric_dictionary,
        "test_metrics": test_metric_dictionary,
        "comparison_payload": build_comparison_payload(
            experiment_identity,
            parameter_summary,
            validation_metric_dictionary,
            test_metric_dictionary,
        ),
    }

def save_yaml_snapshot(snapshot_dictionary: dict[str, Any], output_path: Path) -> None:

    """ Save YAML Snapshot """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the Snapshot Dictionary to the Specified Output Path in YAML Format
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(snapshot_dictionary, output_file, sort_keys=False)

def save_training_config_snapshot(training_config: dict[str, Any], output_directory: Path, experiment_identity: ExperimentIdentity) -> None:

    """ Save Training Config Snapshot """

    output_directory.mkdir(parents=True, exist_ok=True)

    # Save the Training Config Snapshot to the Output Directory
    save_yaml_snapshot(training_config, output_directory / COMMON_TRAINING_CONFIG_FILENAME)

    # Optionally Save a Legacy Config Format for Feedforward Models for Backwards Compatibility
    if experiment_identity.model_family == "feedforward":
        save_yaml_snapshot(training_config, output_directory / LEGACY_FEEDFORWARD_CONFIG_FILENAME)

def save_common_metrics_snapshot(metrics_snapshot_dictionary: dict[str, Any], output_directory: Path, experiment_identity: ExperimentIdentity) -> None:

    """ Save Common Metrics Snapshot """

    # Save the Common Metrics Snapshot to the Output Directory
    save_yaml_snapshot(metrics_snapshot_dictionary, output_directory / COMMON_METRICS_FILENAME)

    # Optionally Save a Legacy Metrics Format for Feedforward Models for Backwards Compatibility
    if experiment_identity.model_family == "feedforward":
        save_yaml_snapshot(metrics_snapshot_dictionary, output_directory / LEGACY_FEEDFORWARD_METRICS_FILENAME)
