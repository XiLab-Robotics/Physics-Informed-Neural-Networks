"""Shared training utilities for TE run identity, artifacts, and registries."""

from __future__ import annotations

# Import Python Utilities
from copy import deepcopy
from dataclasses import asdict
from dataclasses import dataclass
from datetime import datetime
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
TRAINING_RUN_TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"
OUTPUT_PATH = PROJECT_PATH / "output"
VALIDATION_OUTPUT_ROOT = OUTPUT_PATH / "validation_checks"
SMOKE_TEST_OUTPUT_ROOT = OUTPUT_PATH / "smoke_tests"
REGISTRY_OUTPUT_ROOT = OUTPUT_PATH / "registries"
FAMILY_REGISTRY_OUTPUT_ROOT = REGISTRY_OUTPUT_ROOT / "families"
PROGRAM_REGISTRY_OUTPUT_ROOT = REGISTRY_OUTPUT_ROOT / "program"
RUN_OUTPUT_ARTIFACT_KIND = "training_run"
VALIDATION_OUTPUT_ARTIFACT_KIND = "validation_check"
SMOKE_TEST_OUTPUT_ARTIFACT_KIND = "smoke_test"
COMMON_TRAINING_CONFIG_FILENAME = "training_config.yaml"
COMMON_METRICS_FILENAME = "metrics_summary.yaml"
COMMON_VALIDATION_FILENAME = "validation_summary.yaml"
COMMON_SMOKE_TEST_FILENAME = "smoke_test_summary.yaml"
COMMON_RUN_METADATA_FILENAME = "run_metadata.yaml"
COMMON_RUN_REPORT_FILENAME = "training_test_report.md"
FAMILY_LEADERBOARD_FILENAME = "leaderboard.yaml"
FAMILY_BEST_FILENAME = "latest_family_best.yaml"
PROGRAM_BEST_FILENAME = "current_best_solution.yaml"
SELECTION_POLICY_DICTIONARY = {
    "primary_metric": "test_mae",
    "first_tie_breaker": "test_rmse",
    "second_tie_breaker": "val_mae",
    "third_tie_breaker": "trainable_parameter_count",
    "direction": "minimize",
}

@dataclass
class ExperimentIdentity:

    """Logical experiment identity resolved from a training configuration."""

    model_family: str
    model_type: str
    run_name: str

@dataclass
class ModelParameterSummary:

    """Trainable, frozen, and total parameter counts for one backbone."""

    backbone_name: str
    trainable_parameter_count: int
    frozen_parameter_count: int
    total_parameter_count: int

@dataclass
class RunArtifactIdentity:

    """Physical artifact identity used for immutable output folders."""

    artifact_kind: str
    model_family: str
    run_name: str
    run_instance_id: str
    output_directory: Path

def load_training_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:

    """Load and validate a YAML training configuration.

    Args:
        config_path: Absolute or project-relative configuration path.

    Returns:
        dict[str, Any]: Parsed training configuration dictionary.
    """

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

def sanitize_name(name: str) -> str:

    """ Sanitize Name """

    sanitized_name = "".join(character.lower() if character.isalnum() else "_" for character in name.strip())
    sanitized_name = sanitized_name.strip("_")
    return sanitized_name or "run"

def resolve_experiment_identity(training_config: dict[str, Any]) -> ExperimentIdentity:

    """Resolve the logical experiment identity from the training config.

    Args:
        training_config: Parsed training configuration dictionary.

    Returns:
        ExperimentIdentity: Normalized model family, model type, and run name.
    """

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

    """Resolve runtime overrides merged with repository defaults."""

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

def build_run_instance_id(run_name: str) -> str:

    """ Build Run Instance Id """

    timestamp_string = datetime.now().strftime(TRAINING_RUN_TIMESTAMP_FORMAT)
    return f"{timestamp_string}__{sanitize_name(run_name)}"

def prepare_output_artifact_training_config(
    training_config: dict[str, Any],
    artifact_kind: str = RUN_OUTPUT_ARTIFACT_KIND,
    run_name_suffix: str | None = None,
    run_instance_id: str | None = None,
) -> dict[str, Any]:

    """Attach output-artifact metadata to a cloned training configuration.

    Args:
        training_config: Source training configuration.
        artifact_kind: Artifact family such as training run or validation check.
        run_name_suffix: Optional suffix appended to the logical run name.
        run_instance_id: Optional explicit immutable run instance identifier.

    Returns:
        dict[str, Any]: Cloned training configuration enriched with artifact
        metadata under the `metadata` section.
    """

    # Clone the Training Config
    prepared_training_config = clone_training_config(training_config)
    prepared_run_name = build_run_name(prepared_training_config, run_name_suffix)
    metadata_dictionary = prepared_training_config.setdefault("metadata", {})
    existing_artifact_kind = str(metadata_dictionary.get("output_artifact_kind", "")).strip()
    existing_output_run_name = str(metadata_dictionary.get("output_run_name", "")).strip()
    existing_run_instance_id = str(metadata_dictionary.get("run_instance_id", "")).strip()

    # Preserve Existing Artifact Identity When the Config is Already Prepared
    preserve_existing_identity = (
        run_instance_id is None
        and run_name_suffix is None
        and existing_run_instance_id not in ["", None]
        and existing_output_run_name == prepared_run_name
        and existing_artifact_kind in ["", artifact_kind]
    )
    resolved_run_instance_id = existing_run_instance_id if preserve_existing_identity else (run_instance_id or build_run_instance_id(prepared_run_name))

    # Persist Output Artifact Identity Inside Training Metadata
    metadata_dictionary["output_artifact_kind"] = artifact_kind
    metadata_dictionary["output_run_name"] = prepared_run_name
    metadata_dictionary["run_instance_id"] = resolved_run_instance_id

    return prepared_training_config

def resolve_output_artifact_kind(training_config: dict[str, Any]) -> str:

    """ Resolve Output Artifact Kind """

    # Check Training Metadata for Explicit Output Artifact Kind
    metadata_dictionary = training_config.get("metadata", {})
    if isinstance(metadata_dictionary, dict):
        output_artifact_kind = str(metadata_dictionary.get("output_artifact_kind", RUN_OUTPUT_ARTIFACT_KIND)).strip()
        if output_artifact_kind:
            return output_artifact_kind

    return RUN_OUTPUT_ARTIFACT_KIND

def resolve_output_run_name(training_config: dict[str, Any]) -> str:

    """ Resolve Output Run Name """

    # Check Training Metadata for Explicit Output Run Name
    metadata_dictionary = training_config.get("metadata", {})
    if isinstance(metadata_dictionary, dict):
        output_run_name = str(metadata_dictionary.get("output_run_name", "")).strip()
        if output_run_name:
            return output_run_name

    return build_run_name(training_config)

def resolve_run_instance_id(training_config: dict[str, Any]) -> str:

    """ Resolve Run Instance Id """

    # Check Training Metadata for Explicit run_instance_id
    metadata_dictionary = training_config.get("metadata", {})
    assert isinstance(metadata_dictionary, dict), "Training metadata dictionary is required to resolve run_instance_id"

    # If run_instance_id is Present and Non-Empty in Metadata
    run_instance_id = str(metadata_dictionary.get("run_instance_id", "")).strip()
    assert run_instance_id, "Training metadata must contain a non-empty run_instance_id"
    return run_instance_id

def resolve_output_root(training_config: dict[str, Any]) -> Path:

    """ Resolve Output Root """

    # Determine Output Root Directory Based on Output Artifact Kind and Experiment Identity
    experiment_identity = resolve_experiment_identity(training_config)
    output_artifact_kind = resolve_output_artifact_kind(training_config)

    # Resolve Standard Training-Run Output Root
    if output_artifact_kind == RUN_OUTPUT_ARTIFACT_KIND:
        return resolve_project_relative_path(training_config["paths"]["output_root"])

    # Resolve Validation Output Root
    if output_artifact_kind == VALIDATION_OUTPUT_ARTIFACT_KIND:
        return (VALIDATION_OUTPUT_ROOT / experiment_identity.model_family).resolve()

    # Smoke Test Outputs are Organized Under a Separate Root Directory
    if output_artifact_kind == SMOKE_TEST_OUTPUT_ARTIFACT_KIND:
        return (SMOKE_TEST_OUTPUT_ROOT / experiment_identity.model_family).resolve()

    raise ValueError(f"Unsupported output_artifact_kind | {output_artifact_kind}")

def resolve_output_directory(training_config: dict[str, Any]) -> Path:

    """Resolve the immutable output directory for the prepared artifact."""

    # Construct Output Directory Path Based on Prepared Training Metadata
    output_root = resolve_output_root(training_config)
    run_instance_id = resolve_run_instance_id(training_config)
    return output_root / run_instance_id

def resolve_run_artifact_identity(training_config: dict[str, Any]) -> RunArtifactIdentity:

    """Resolve the full physical artifact identity for one prepared config."""

    # Resolve Experiment Identity
    experiment_identity = resolve_experiment_identity(training_config)
    output_directory = resolve_output_directory(training_config)
    return RunArtifactIdentity(
        artifact_kind=resolve_output_artifact_kind(training_config),
        model_family=experiment_identity.model_family,
        run_name=resolve_output_run_name(training_config),
        run_instance_id=resolve_run_instance_id(training_config),
        output_directory=output_directory,
    )

def load_run_metadata_snapshot(output_directory: Path) -> dict[str, Any] | None:

    """Load one run-metadata snapshot when it exists.

    Args:
        output_directory: Candidate immutable artifact directory.

    Returns:
        dict[str, Any] | None: Parsed run metadata dictionary, or `None` when
        the snapshot is absent or malformed.
    """

    # Resolve Run-Metadata Path
    run_metadata_path = output_directory / COMMON_RUN_METADATA_FILENAME
    if not run_metadata_path.exists():
        return None

    # Load and Validate Run Metadata
    with run_metadata_path.open("r", encoding="utf-8") as metadata_file:
        run_metadata_dictionary = yaml.safe_load(metadata_file)

    if not isinstance(run_metadata_dictionary, dict):
        return None

    return run_metadata_dictionary

def find_run_output_directory(
    model_family: str,
    run_name: str | None = None,
    run_instance_id: str | None = None,
) -> Path | None:

    """Find one immutable run output directory from canonical run metadata.

    Args:
        model_family: Model-family folder under `output/training_runs/`.
        run_name: Optional logical run name to match.
        run_instance_id: Optional immutable run instance identifier to match.

    Returns:
        Path | None: Matching artifact directory, or `None` when no canonical
        match can be recovered.
    """

    # Resolve Candidate Family Root
    family_output_root = OUTPUT_PATH / "training_runs" / str(model_family).strip().lower()
    if not family_output_root.exists():
        return None

    normalized_run_name = str(run_name).strip() if run_name not in [None, ""] else ""
    normalized_run_instance_id = str(run_instance_id).strip() if run_instance_id not in [None, ""] else ""
    run_instance_match_path: Path | None = None
    run_name_match_path_list: list[Path] = []

    # Scan Immutable Run Directories for Matching Metadata
    for candidate_output_directory in sorted([path for path in family_output_root.iterdir() if path.is_dir()]):
        run_metadata_dictionary = load_run_metadata_snapshot(candidate_output_directory)
        if run_metadata_dictionary is None:
            continue

        metadata_run_instance_id = str(run_metadata_dictionary.get("run_instance_id", "")).strip()
        metadata_run_name = str(run_metadata_dictionary.get("run_name", "")).strip()

        if normalized_run_instance_id and metadata_run_instance_id == normalized_run_instance_id:
            run_instance_match_path = candidate_output_directory.resolve()
            break

        if normalized_run_name and metadata_run_name == normalized_run_name:
            run_name_match_path_list.append(candidate_output_directory.resolve())

    if run_instance_match_path is not None:
        return run_instance_match_path

    if len(run_name_match_path_list) > 0:
        return sorted(run_name_match_path_list)[-1]

    return None

def summarize_model_parameters(regression_backbone: nn.Module) -> ModelParameterSummary:

    """Count trainable, frozen, and total parameters for one backbone."""

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

    """Instantiate the TE LightningDataModule from the training config."""

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

    """Instantiate the regression backbone declared in the config.

    Args:
        training_config: Parsed training configuration dictionary.
        input_feature_dim: Input dimension resolved from the prepared dataset.

    Returns:
        nn.Module: Configured regression backbone.
    """

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

    """Wrap a configured backbone in the shared Lightning regression module."""

    # Build Regression Module With Optimization Hyperparameters
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

    """Build the datamodule, backbone, module, and normalization bundle.

    Args:
        training_config: Parsed training configuration dictionary.

    Returns:
        tuple[TransmissionErrorDataModule, nn.Module, TransmissionErrorRegressionModule, NormalizationStatistics]:
        Fully initialized training components ready for fit or validation work.
    """

    # Create DataModule and Setup to Access Dataset Statistics
    datamodule = create_datamodule_from_training_config(training_config)
    datamodule.setup(stage="fit")

    # Create Regression Backbone and Regression Module Based on Training Config and Dataset Statistics
    input_feature_dim = datamodule.get_input_feature_dim()
    target_feature_dim = datamodule.get_target_feature_dim()
    normalization_statistics = datamodule.get_normalization_statistics()

    # Build Regression Backbone From The Resolved Dataset Feature Dimensions
    regression_backbone = create_regression_backbone_from_training_config(
        training_config,
        input_feature_dim,
    )

    # Build Regression Module With Shared Normalization Statistics
    regression_module = create_regression_module_from_training_config(
        training_config,
        regression_backbone,
        input_feature_dim,
        target_feature_dim,
        normalization_statistics,
    )

    return datamodule, regression_backbone, regression_module, normalization_statistics

def fetch_first_batch(datamodule: TransmissionErrorDataModule, split_name: str = "train") -> dict[str, Any]:

    """Fetch the first batch from one requested dataloader split."""

    # Fetch First Batch from Specified Data Split and Return as Dictionary
    if split_name == "train":        dataloader = datamodule.train_dataloader()
    elif split_name == "validation": dataloader = datamodule.val_dataloader()
    elif split_name == "test":       dataloader = datamodule.test_dataloader()
    else: raise ValueError(f"Unsupported split_name | {split_name}")

    return next(iter(dataloader))

def validate_batch_dictionary(batch_dictionary: dict[str, Any], input_feature_dim: int, target_feature_dim: int) -> dict[str, Any]:

    """Validate the structural contract of a collated point batch.

    Args:
        batch_dictionary: Batch emitted by the datamodule collate function.
        input_feature_dim: Expected final input feature dimension.
        target_feature_dim: Expected final target feature dimension.

    Returns:
        dict[str, Any]: Small structural summary of the validated batch.
    """

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
    output_directory: Path,
    datamodule: TransmissionErrorDataModule,
    parameter_summary: ModelParameterSummary,
    runtime_config: dict[str, object],
    best_model_path: str,
    validation_metric_list: list[dict[str, object]],
    test_metric_list: list[dict[str, object]],
) -> dict[str, object]:

    """Build the canonical metrics snapshot stored with a training artifact."""

    # Resolve Experiment Identity and Dataset Split Summary for Snapshot
    experiment_identity = resolve_experiment_identity(training_config)
    run_artifact_identity = resolve_run_artifact_identity(training_config)
    dataset_split_summary = datamodule.get_dataset_split_summary()
    normalization_statistics = datamodule.get_normalization_statistics()

    # Serialize Validation and Test Metric Dictionaries for Snapshot
    validation_metric_dictionary = serialize_metric_dictionary(validation_metric_list[0] if len(validation_metric_list) > 0 else {})
    test_metric_dictionary = serialize_metric_dictionary(test_metric_list[0] if len(test_metric_list) > 0 else {})

    return {
        "schema_version": 1,
        "config_path": str(resolve_project_relative_path(config_path)),
        "experiment": {
            **asdict(experiment_identity),
            "output_run_name": run_artifact_identity.run_name,
            "run_instance_id": run_artifact_identity.run_instance_id,
            "output_artifact_kind": run_artifact_identity.artifact_kind,
        },
        "artifacts": {
            "output_directory": str(output_directory),
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

def format_project_relative_path(path_value: str | Path | None) -> str:

    """ Format Project Relative Path """

    if path_value is None:
        return "N/A"

    # Handle Special Case for Checkpoint Paths When Best Checkpoint is Not Available
    if isinstance(path_value, str) and "Best checkpoint not available" in path_value:
        return path_value

    resolved_path = Path(path_value).resolve()

    # Format Path as Project-Relative if Possible, Otherwise Return Absolute Path
    try: return resolved_path.relative_to(PROJECT_PATH).as_posix()
    except ValueError: return resolved_path.as_posix()

def load_yaml_snapshot(input_path: Path) -> dict[str, Any]:

    """Load a YAML snapshot and validate that it is dictionary-shaped."""

    # Load the YAML Snapshot from the Specified Input Path
    with input_path.open("r", encoding="utf-8") as input_file:
        snapshot_dictionary = yaml.safe_load(input_file)

    # Validate that the Loaded Snapshot is a Dictionary
    assert isinstance(snapshot_dictionary, dict), f"YAML snapshot must contain a dictionary | {input_path}"
    return snapshot_dictionary

def save_yaml_snapshot(snapshot_dictionary: dict[str, Any], output_path: Path) -> None:

    """Persist one YAML snapshot to disk, creating parent folders as needed."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the Snapshot Dictionary to the Specified Output Path in YAML Format
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(snapshot_dictionary, output_file, sort_keys=False)

def save_training_config_snapshot(training_config: dict[str, Any], output_directory: Path) -> None:

    """Persist the effective training configuration inside an artifact folder."""

    output_directory.mkdir(parents=True, exist_ok=True)

    # Save the Training Config Snapshot to the Output Directory
    save_yaml_snapshot(training_config, output_directory / COMMON_TRAINING_CONFIG_FILENAME)

def save_common_metrics_snapshot(metrics_snapshot_dictionary: dict[str, Any], output_directory: Path) -> None:

    """Persist the common metrics snapshot inside an artifact folder."""

    # Save the Common Metrics Snapshot to the Output Directory
    save_yaml_snapshot(metrics_snapshot_dictionary, output_directory / COMMON_METRICS_FILENAME)

def build_registry_entry(metrics_snapshot_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Convert a metrics snapshot into a comparable registry entry."""

    # Extract Relevant Information from the Common Metrics Snapshot to Build a Registry Entry
    experiment_dictionary = metrics_snapshot_dictionary["experiment"]
    comparison_payload = metrics_snapshot_dictionary["comparison_payload"]
    model_summary_dictionary = metrics_snapshot_dictionary["model_summary"]
    artifacts_dictionary = metrics_snapshot_dictionary["artifacts"]

    return {
        "run_instance_id": experiment_dictionary["run_instance_id"],
        "run_name": experiment_dictionary["run_name"],
        "output_run_name": experiment_dictionary["output_run_name"],
        "output_artifact_kind": experiment_dictionary["output_artifact_kind"],
        "model_family": comparison_payload["model_family"],
        "model_type": comparison_payload["model_type"],
        "trainable_parameter_count": model_summary_dictionary["trainable_parameter_count"],
        "total_parameter_count": model_summary_dictionary["total_parameter_count"],
        "val_mae": comparison_payload.get("val_mae"),
        "val_rmse": comparison_payload.get("val_rmse"),
        "test_mae": comparison_payload.get("test_mae"),
        "test_rmse": comparison_payload.get("test_rmse"),
        "output_directory": format_project_relative_path(artifacts_dictionary.get("output_directory")),
        "best_checkpoint_path": format_project_relative_path(artifacts_dictionary.get("best_checkpoint_path")),
        "metrics_path": (
            f"{format_project_relative_path(artifacts_dictionary.get('output_directory'))}/{COMMON_METRICS_FILENAME}"
            if artifacts_dictionary.get("output_directory") not in [None, ""]
            else "N/A"
        ),
        "report_path": (
            f"{format_project_relative_path(artifacts_dictionary.get('output_directory'))}/{COMMON_RUN_REPORT_FILENAME}"
            if artifacts_dictionary.get("output_directory") not in [None, ""]
            else "N/A"
        ),
        "selection_policy": dict(SELECTION_POLICY_DICTIONARY),
        "selected_at": datetime.now().isoformat(timespec="seconds"),
    }

def resolve_selection_value(metric_value: object) -> float:

    """ Resolve Selection Value """

    # Convert the Metric Value to a Float if it is a Numeric Type
    if isinstance(metric_value, (int, float)):
        return float(metric_value)

    return float("inf")

def build_selection_key(registry_entry: dict[str, Any]) -> tuple[float, float, float, float, str]:

    """ Build Selection Key """

    # Build a Selection Key Tuple Based on the Registry Entry's Metrics
    return (
        resolve_selection_value(registry_entry.get("test_mae")),
        resolve_selection_value(registry_entry.get("test_rmse")),
        resolve_selection_value(registry_entry.get("val_mae")),
        resolve_selection_value(registry_entry.get("trainable_parameter_count")),
        str(registry_entry.get("run_instance_id", "")),
    )

def sort_registry_entries(registry_entry_list: list[dict[str, Any]]) -> list[dict[str, Any]]:

    """ Sort Registry Entries """

    # Sort the Registry Entry List Based on the Selection Key Built from Each Entry's Metrics
    return sorted(registry_entry_list, key=build_selection_key)

def load_registry_entry_list(leaderboard_path: Path) -> list[dict[str, Any]]:

    """ Load Registry Entry List """

    if not leaderboard_path.exists():
        return []

    # Load the Leaderboard YAML Snapshot and Extract the Registry Entry List, Validating its Structure
    leaderboard_dictionary = load_yaml_snapshot(leaderboard_path)
    registry_entry_list = leaderboard_dictionary.get("entry_list", [])
    assert isinstance(registry_entry_list, list), f"Registry entry_list must be a list | {leaderboard_path}"
    return [registry_entry for registry_entry in registry_entry_list if isinstance(registry_entry, dict)]

def build_family_registry_directory(model_family: str) -> Path:

    """ Build Family Registry Directory """

    # Construct the Family Registry Directory Path Based on the Model Family Name
    return (FAMILY_REGISTRY_OUTPUT_ROOT / model_family).resolve()

def update_family_registry(metrics_snapshot_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Update the family leaderboard and latest-family-best snapshots.

    Args:
        metrics_snapshot_dictionary: Common metrics snapshot for one completed
            training artifact.

    Returns:
        dict[str, Any]: Selected best entry for the model family after update.
    """

    # Build a Registry Entry from the Common Metrics Snapshot and Update the Family Registry Leaderboard
    registry_entry = build_registry_entry(metrics_snapshot_dictionary)
    family_registry_directory = build_family_registry_directory(registry_entry["model_family"])
    leaderboard_path = family_registry_directory / FAMILY_LEADERBOARD_FILENAME
    best_entry_path = family_registry_directory / FAMILY_BEST_FILENAME

    # Load Existing Registry Entries, Filter Out Any Entry with the Same run_instance_id
    existing_registry_entry_list = load_registry_entry_list(leaderboard_path)
    filtered_registry_entry_list = [
        existing_registry_entry
        for existing_registry_entry in existing_registry_entry_list
        if existing_registry_entry.get("run_instance_id") != registry_entry["run_instance_id"]
    ]
    filtered_registry_entry_list.append(registry_entry)
    sorted_registry_entry_list = sort_registry_entries(filtered_registry_entry_list)
    best_registry_entry = sorted_registry_entry_list[0]

    # Build the Leaderboard and Best Entry Dictionaries with Updated Information and Save Them as YAML Snapshots
    leaderboard_dictionary = {
        "schema_version": 1,
        "model_family": registry_entry["model_family"],
        "selection_policy": dict(SELECTION_POLICY_DICTIONARY),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "entry_count": len(sorted_registry_entry_list),
        "entry_list": sorted_registry_entry_list,
    }

    # Best Entry Dictionary
    best_entry_dictionary = {
        "schema_version": 1,
        "model_family": registry_entry["model_family"],
        "selection_policy": dict(SELECTION_POLICY_DICTIONARY),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "best_entry": best_registry_entry,
    }

    # Save the Updated Leaderboard and Best Entry as YAML Snapshots in the Family Registry Directory
    save_yaml_snapshot(leaderboard_dictionary, leaderboard_path)
    save_yaml_snapshot(best_entry_dictionary, best_entry_path)

    return best_registry_entry

def update_program_registry(best_registry_entry: dict[str, Any]) -> dict[str, Any]:

    """Update the program-wide best-solution registry entry."""

    program_best_path = PROGRAM_REGISTRY_OUTPUT_ROOT / PROGRAM_BEST_FILENAME
    current_best_entry = None

    # If a Current Best Entry Exists in the Program Registry, Load it for Comparison
    if program_best_path.exists():
        program_best_dictionary = load_yaml_snapshot(program_best_path)
        loaded_best_entry = program_best_dictionary.get("best_entry")
        if isinstance(loaded_best_entry, dict):
            current_best_entry = loaded_best_entry

    # Compare the New Best Registry Entry with the Current Best Entry
    selected_best_entry = best_registry_entry
    if isinstance(current_best_entry, dict) and build_selection_key(current_best_entry) <= build_selection_key(best_registry_entry):
        selected_best_entry = current_best_entry

    # Build the Program Best Dictionary with the Selected Best Entry
    program_best_dictionary = {
        "schema_version": 1,
        "selection_policy": dict(SELECTION_POLICY_DICTIONARY),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "best_entry": selected_best_entry,
    }

    # Save the Updated Program Best Dictionary as a YAML Snapshot in the Program Registry Directory
    save_yaml_snapshot(program_best_dictionary, program_best_path)
    return selected_best_entry

def save_run_metadata_snapshot(training_config: dict[str, Any], output_directory: Path) -> None:

    """Persist the resolved artifact identity inside an output directory."""

    # Resolve Run Artifact Identity and Save it as a YAML Snapshot in the Output Directory for Reference and Traceability
    run_artifact_identity = resolve_run_artifact_identity(training_config)
    save_yaml_snapshot(
        {
            "schema_version": 1,
            "artifact_kind": run_artifact_identity.artifact_kind,
            "model_family": run_artifact_identity.model_family,
            "run_name": run_artifact_identity.run_name,
            "run_instance_id": run_artifact_identity.run_instance_id,
            "output_directory": format_project_relative_path(run_artifact_identity.output_directory),
        },
        output_directory / COMMON_RUN_METADATA_FILENAME,
    )
