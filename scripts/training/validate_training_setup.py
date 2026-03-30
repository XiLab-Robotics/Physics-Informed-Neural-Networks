"""One-batch validation check for TE training and tree baselines."""

from __future__ import annotations

# Import Python Utilities
import sys, argparse
from datetime import datetime
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import PyTorch Utilities
import torch
import numpy as np

# Import Project Utilities
from scripts.training import shared_training_infrastructure
from scripts.training import tree_regression_support

TREE_MODEL_TYPE_LIST = ["random_forest", "hist_gradient_boosting"]
VALIDATION_REPORT_ROOT = PROJECT_PATH / "doc" / "reports" / "analysis" / "validation_checks"
VALIDATION_REPORT_TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"

def build_validation_summary(
    config_path: Path,
    output_directory: Path,
    batch_summary: dict[str, object],
    batch_output_dictionary: dict[str, torch.Tensor],
    training_config: dict[str, object],
) -> dict[str, object]:

    """Build the persisted validation summary for one setup check.

    Args:
        config_path: Canonical training configuration path.
        output_directory: Validation artifact directory.
        batch_summary: Structural batch summary from the validation step.
        batch_output_dictionary: Output tensors and metrics computed by the
            regression module.
        training_config: Prepared training configuration with artifact metadata.

    Returns:
        dict[str, object]: YAML-serializable validation summary.
    """

    # Resolve Experiment Identity For Validation Summary
    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)

    return {
        "schema_version": 1,
        "config_path": str(config_path),
        "output_directory": str(output_directory),
        "experiment": {
            "run_name": experiment_identity.run_name,
            "output_run_name": shared_training_infrastructure.resolve_output_run_name(training_config),
            "run_instance_id": shared_training_infrastructure.resolve_run_instance_id(training_config),
            "model_family": experiment_identity.model_family,
            "model_type": experiment_identity.model_type,
        },
        "batch_summary": batch_summary,
        "checks": {
            "finite_loss": bool(torch.isfinite(batch_output_dictionary["loss"]).item()),
            "finite_mae": bool(torch.isfinite(batch_output_dictionary["mae"]).item()),
            "finite_rmse": bool(torch.isfinite(batch_output_dictionary["rmse"]).item()),
            "finite_prediction_tensor": bool(torch.isfinite(batch_output_dictionary["prediction_tensor"]).all().item()),
        },
        "metrics": {
            "loss": float(batch_output_dictionary["loss"].detach().cpu().item()),
            "mae": float(batch_output_dictionary["mae"].detach().cpu().item()),
            "rmse": float(batch_output_dictionary["rmse"].detach().cpu().item()),
        },
    }

def build_tree_validation_summary(
    config_path: Path,
    output_directory: Path,
    validation_input: np.ndarray,
    validation_prediction_vector: np.ndarray,
    validation_metric_dictionary: dict[str, float],
    datamodule,
    training_config: dict[str, object],
) -> dict[str, object]:

    """ Build Tree Validation Summary """

    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)

    return {
        "schema_version": 1,
        "config_path": str(shared_training_infrastructure.resolve_project_relative_path(config_path)),
        "output_directory": str(output_directory),
        "experiment": {
            "run_name": experiment_identity.run_name,
            "output_run_name": shared_training_infrastructure.resolve_output_run_name(training_config),
            "run_instance_id": shared_training_infrastructure.resolve_run_instance_id(training_config),
            "model_family": experiment_identity.model_family,
            "model_type": experiment_identity.model_type,
        },
        "batch_summary": {
            "point_batch_size": int(validation_input.shape[0]),
            "input_feature_dim": int(validation_input.shape[1]),
            "target_feature_dim": 1,
            "curve_count": int(datamodule.get_dataset_split_summary().validation_curve_count),
        },
        "checks": {
            "finite_loss": bool(torch.isfinite(torch.tensor(validation_metric_dictionary["loss"])).item()),
            "finite_mae": bool(torch.isfinite(torch.tensor(validation_metric_dictionary["mae"])).item()),
            "finite_rmse": bool(torch.isfinite(torch.tensor(validation_metric_dictionary["rmse"])).item()),
            "finite_prediction_tensor": bool(np.isfinite(validation_prediction_vector).all()),
        },
        "metrics": {
            "loss": float(validation_metric_dictionary["loss"]),
            "mae": float(validation_metric_dictionary["mae"]),
            "rmse": float(validation_metric_dictionary["rmse"]),
        },
    }

def build_validation_report_path(training_config: dict[str, object]) -> Path:

    """ Build Validation Report Path """

    # Resolve Experiment Identity For Report Naming
    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    output_run_name = shared_training_infrastructure.resolve_output_run_name(training_config)
    timestamp_string = datetime.now().strftime(VALIDATION_REPORT_TIMESTAMP_FORMAT)
    sanitized_model_family = shared_training_infrastructure.sanitize_name(experiment_identity.model_family)
    sanitized_output_run_name = shared_training_infrastructure.sanitize_name(output_run_name)

    # Build Canonical Validation Report Path
    validation_report_filename = (
        f"{timestamp_string}_{sanitized_model_family}_{sanitized_output_run_name}_validation_setup_report.md"
    )
    validation_report_path = VALIDATION_REPORT_ROOT / validation_report_filename
    validation_report_path.parent.mkdir(parents=True, exist_ok=True)
    return validation_report_path

def format_boolean_status(is_enabled: bool) -> str:

    """ Format Boolean Status """

    return "Pass" if is_enabled else "Fail"

def build_report_display_path(path_value: Path) -> str:

    """ Build Report Display Path """

    try:
        return str(path_value.resolve().relative_to(PROJECT_PATH)).replace("\\", "/")
    except ValueError:
        return str(path_value)

def build_validation_report_markdown(
    validation_summary: dict[str, object],
    config_path: Path,
    training_config: dict[str, object],
) -> str:

    """ Build Validation Report Markdown """

    experiment_dictionary = validation_summary["experiment"]
    batch_summary_dictionary = validation_summary["batch_summary"]
    check_dictionary = validation_summary["checks"]
    metric_dictionary = validation_summary["metrics"]
    all_checks_passed = all(bool(value) for value in check_dictionary.values())
    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    output_directory = Path(str(validation_summary["output_directory"]))
    display_config_path = build_report_display_path(config_path)
    display_output_directory = build_report_display_path(output_directory)

    overview_text = (
        "This report summarizes a repository-owned lightweight validation pass "
        "executed through `scripts/training/validate_training_setup.py`."
    )
    interpretation_text = (
        "The validation setup passed all finite checks on the selected batch or reduced validation subset. "
        "This means the current training wiring is structurally healthy enough for further smoke-test or training work."
        if all_checks_passed else
        "The validation setup failed at least one finite check. The configuration should not be promoted to broader smoke-test "
        "or training work until the underlying issue is resolved."
    )

    return f"""# Validation Setup Report

## Overview

{overview_text}

- model family: `{experiment_identity.model_family}`;
- model type: `{experiment_identity.model_type}`;
- logical run name: `{experiment_dictionary["run_name"]}`;
- output run name: `{experiment_dictionary["output_run_name"]}`;
- run instance id: `{experiment_dictionary["run_instance_id"]}`;
- lightweight validation result: **{"pass" if all_checks_passed else "fail"}**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `{display_config_path}` |
| Output Directory | `{display_output_directory}` |
| Model Family | `{experiment_dictionary["model_family"]}` |
| Model Type | `{experiment_dictionary["model_type"]}` |
| Run Name | `{experiment_dictionary["run_name"]}` |
| Output Run Name | `{experiment_dictionary["output_run_name"]}` |
| Run Instance ID | `{experiment_dictionary["run_instance_id"]}` |

## Batch Structure

| Field | Value |
| --- | ---: |
| Point Batch Size | {batch_summary_dictionary["point_batch_size"]} |
| Input Feature Dim | {batch_summary_dictionary["input_feature_dim"]} |
| Target Feature Dim | {batch_summary_dictionary["target_feature_dim"]} |
| Curve Count | {batch_summary_dictionary["curve_count"]} |

## Finite Checks

| Check | Status |
| --- | --- |
| Finite Loss | {format_boolean_status(bool(check_dictionary["finite_loss"]))} |
| Finite MAE | {format_boolean_status(bool(check_dictionary["finite_mae"]))} |
| Finite RMSE | {format_boolean_status(bool(check_dictionary["finite_rmse"]))} |
| Finite Prediction Tensor | {format_boolean_status(bool(check_dictionary["finite_prediction_tensor"]))} |

## Metrics

| Metric | Value |
| --- | ---: |
| Loss | {float(metric_dictionary["loss"]):.8f} |
| MAE | {float(metric_dictionary["mae"]):.8f} |
| RMSE | {float(metric_dictionary["rmse"]):.8f} |

## Interpretation

{interpretation_text}

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
"""

def save_validation_report(
    validation_summary: dict[str, object],
    config_path: Path,
    training_config: dict[str, object],
) -> Path:

    """ Save Validation Report """

    validation_report_path = build_validation_report_path(training_config)
    validation_report_markdown = build_validation_report_markdown(
        validation_summary,
        config_path,
        training_config,
    )
    validation_report_path.write_text(validation_report_markdown, encoding="utf-8")
    return validation_report_path

def save_validation_outputs(
    validation_summary: dict[str, object],
    resolved_config_path: Path,
    output_directory: Path,
    training_config: dict[str, object],
) -> tuple[Path, Path]:

    """ Save Validation Outputs """

    validation_summary_path = output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME
    shared_training_infrastructure.save_yaml_snapshot(
        validation_summary,
        validation_summary_path,
    )

    validation_report_path = save_validation_report(
        validation_summary,
        resolved_config_path,
        training_config,
    )

    return validation_summary_path, validation_report_path

def validate_training_setup(config_path: Path, output_suffix: str = "validation_check") -> tuple[Path, Path]:

    """Run a lightweight validation check for the configured training setup.

    Args:
        config_path: YAML training configuration path.
        output_suffix: Suffix appended to the validation artifact run name.

    Returns:
        tuple[Path, Path]: Validation summary YAML path plus generated Markdown
        report path.
    """

    # Load Training Config And Resolve Output Directory
    training_config = shared_training_infrastructure.prepare_output_artifact_training_config(
        shared_training_infrastructure.load_training_config(config_path),
        artifact_kind=shared_training_infrastructure.VALIDATION_OUTPUT_ARTIFACT_KIND,
        run_name_suffix=output_suffix,
    )
    resolved_config_path = shared_training_infrastructure.resolve_project_relative_path(config_path)

    # Force Single-Process Validation To Keep The Check Robust In Restricted Environments
    training_config["dataset"]["num_workers"] = 0
    training_config["dataset"]["pin_memory"] = False
    if "n_jobs" in training_config["model"]:
        training_config["model"]["n_jobs"] = 1

    # Prepare Output Directory
    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    output_directory = shared_training_infrastructure.resolve_output_directory(training_config)
    output_directory.mkdir(parents=True, exist_ok=True)
    shared_training_infrastructure.save_run_metadata_snapshot(training_config, output_directory)

    # Run Tree-Specific Validation For The Scikit-Learn Baselines
    if experiment_identity.model_type in TREE_MODEL_TYPE_LIST:

        # Build Dataset Splits And Estimator
        datamodule, split_dictionary = tree_regression_support.build_tree_split_bundle(training_config)
        estimator = tree_regression_support.build_tree_estimator(training_config)
        train_input = split_dictionary["train_input"][:tree_regression_support.TREE_VALIDATION_SAMPLE_COUNT]
        train_target = split_dictionary["train_target"][:tree_regression_support.TREE_VALIDATION_SAMPLE_COUNT]
        validation_input = split_dictionary["validation_input"][:tree_regression_support.TREE_VALIDATION_SAMPLE_COUNT]
        validation_target = split_dictionary["validation_target"][:tree_regression_support.TREE_VALIDATION_SAMPLE_COUNT]

        # Fit The Estimator On The Flattened Train Split
        estimator.fit(train_input, train_target)
        validation_prediction_vector = estimator.predict(validation_input)
        validation_metric_dictionary = tree_regression_support.compute_regression_metric_dictionary(
            validation_target,
            validation_prediction_vector,
        )

        # Build Validation Summary
        validation_summary = build_tree_validation_summary(
            resolved_config_path,
            output_directory,
            validation_input,
            validation_prediction_vector,
            validation_metric_dictionary,
            datamodule,
            training_config,
        )

        # Save Validation Outputs
        validation_summary_path, validation_report_path = save_validation_outputs(
            validation_summary,
            resolved_config_path,
            output_directory,
            training_config,
        )
        print(f"[DONE] Validation setup check completed | {validation_summary_path}")
        print(f"[DONE] Validation setup report written | {validation_report_path}")
        return validation_summary_path, validation_report_path

    # Initialize Training Components
    datamodule, regression_backbone, regression_module, _ = shared_training_infrastructure.initialize_training_components(training_config)
    input_feature_dim = datamodule.get_input_feature_dim()
    target_feature_dim = datamodule.get_target_feature_dim()

    # Fetch First Batch And Validate Batch Dictionary
    batch_dictionary = shared_training_infrastructure.fetch_first_batch(datamodule, split_name="train")
    batch_summary = shared_training_infrastructure.validate_batch_dictionary(
        batch_dictionary,
        input_feature_dim,
        target_feature_dim,
    )

    # Set Models To Evaluation Mode For Validation Check
    regression_module.eval()
    regression_backbone.eval()

    # Compute Batch Outputs And Metrics With No Gradient Tracking For Validation Check
    with torch.no_grad():
        batch_output_dictionary = regression_module.compute_batch_outputs(batch_dictionary)

    # Build Validation Summary And Save Outputs For Validation Check
    validation_summary = build_validation_summary(
        resolved_config_path,
        output_directory,
        batch_summary,
        batch_output_dictionary,
        training_config,
    )
    validation_summary_path, validation_report_path = save_validation_outputs(
        validation_summary,
        resolved_config_path,
        output_directory,
        training_config,
    )

    print(f"[DONE] Validation setup check completed | {validation_summary_path}")
    print(f"[DONE] Validation setup report written | {validation_report_path}")
    return validation_summary_path, validation_report_path

def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the validation helper script."""

    # Create Argument Parser For Validation Check
    argument_parser = argparse.ArgumentParser(description="Run a one-batch validation check for the current TE training setup.")
    argument_parser.add_argument("--config-path", type=Path, default=shared_training_infrastructure.DEFAULT_CONFIG_PATH, help="Path to the YAML training configuration file.")
    argument_parser.add_argument("--output-suffix", type=str, default="validation_check", help="Suffix appended to the run directory for the validation summary.")
    return argument_parser.parse_args()

def main() -> None:

    """Run the validation helper entry point from the command line."""

    # Parse Command Line Arguments
    command_line_arguments = parse_command_line_arguments()

    # Run Validation Check For Training Setup
    validate_training_setup(
        command_line_arguments.config_path,
        command_line_arguments.output_suffix,
    )

if __name__ == "__main__":

    main()
