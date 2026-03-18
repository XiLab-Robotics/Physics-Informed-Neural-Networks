from __future__ import annotations

# Import Python Utilities
import sys, argparse
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

def build_validation_summary(
    config_path: Path,
    output_directory: Path,
    batch_summary: dict[str, object],
    batch_output_dictionary: dict[str, torch.Tensor],
    training_config: dict[str, object],
) -> dict[str, object]:

    """ Build Validation Summary """

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

def validate_training_setup(config_path: Path, output_suffix: str = "validation_check") -> None:

    """ Validate Training Setup """

    # Load Training Config And Resolve Output Directory
    training_config = shared_training_infrastructure.prepare_output_artifact_training_config(
        shared_training_infrastructure.load_training_config(config_path),
        artifact_kind=shared_training_infrastructure.VALIDATION_OUTPUT_ARTIFACT_KIND,
        run_name_suffix=output_suffix,
    )

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
        validation_summary = {
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

        # Save Validation Summary
        shared_training_infrastructure.save_yaml_snapshot(
            validation_summary,
            output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME,
        )
        print(f"[DONE] Validation setup check completed | {output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME}")
        return

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

    # Build Validation Summary And Save Snapshot For Validation Check
    validation_summary = build_validation_summary(
        shared_training_infrastructure.resolve_project_relative_path(config_path),
        output_directory,
        batch_summary,
        batch_output_dictionary,
        training_config,
    )

    # Save Validation Summary Snapshot For Validation Check
    shared_training_infrastructure.save_yaml_snapshot(
        validation_summary,
        output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME,
    )

    print(f"[DONE] Validation setup check completed | {output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME}")

def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command Line Arguments """

    # Create Argument Parser For Validation Check
    argument_parser = argparse.ArgumentParser(description="Run a one-batch validation check for the current TE training setup.")
    argument_parser.add_argument("--config-path", type=Path, default=shared_training_infrastructure.DEFAULT_CONFIG_PATH, help="Path to the YAML training configuration file.")
    argument_parser.add_argument("--output-suffix", type=str, default="validation_check", help="Suffix appended to the run directory for the validation summary.")
    return argument_parser.parse_args()

def main() -> None:

    """ Main Function """

    # Parse Command Line Arguments
    command_line_arguments = parse_command_line_arguments()

    # Run Validation Check For Training Setup
    validate_training_setup(
        command_line_arguments.config_path,
        command_line_arguments.output_suffix,
    )

if __name__ == "__main__":

    main()
