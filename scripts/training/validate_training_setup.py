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

# Import Project Utilities
from scripts.training import shared_training_infrastructure

def build_validation_summary(
    config_path: Path,
    output_directory: Path,
    batch_summary: dict[str, object],
    batch_output_dictionary: dict[str, torch.Tensor],
    training_config: dict[str, object],
) -> dict[str, object]:

    """ Build Validation Summary """

    # Resolve Experiment Identity For Validation Summary
    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config=training_config)

    return {
        "schema_version": 1,
        "config_path": str(config_path),
        "output_directory": str(output_directory),
        "experiment": {
            "run_name": experiment_identity.run_name,
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
    training_config = shared_training_infrastructure.load_training_config(config_path=config_path)
    output_directory = shared_training_infrastructure.resolve_output_directory(training_config, output_suffix)
    output_directory.mkdir(parents=True, exist_ok=True)

    # Initialize Training Components
    datamodule, regression_backbone, regression_module, _ = shared_training_infrastructure.initialize_training_components(training_config)
    input_feature_dim = datamodule.get_input_feature_dim()
    target_feature_dim = datamodule.get_target_feature_dim()

    # Fetch First Batch And Validate Batch Dictionary
    batch_dictionary = shared_training_infrastructure.fetch_first_batch(datamodule=datamodule, split_name="train")
    batch_summary = shared_training_infrastructure.validate_batch_dictionary(
        batch_dictionary=batch_dictionary,
        input_feature_dim=input_feature_dim,
        target_feature_dim=target_feature_dim,
    )

    # Set Models To Evaluation Mode For Validation Check
    regression_module.eval()
    regression_backbone.eval()

    # Compute Batch Outputs And Metrics With No Gradient Tracking For Validation Check
    with torch.no_grad():
        batch_output_dictionary = regression_module.compute_batch_outputs(batch_dictionary=batch_dictionary)

    # Build Validation Summary And Save Snapshot For Validation Check
    validation_summary = build_validation_summary(
        config_path=shared_training_infrastructure.resolve_project_relative_path(config_path),
        output_directory=output_directory,
        batch_summary=batch_summary,
        batch_output_dictionary=batch_output_dictionary,
        training_config=training_config,
    )

    # Save Validation Summary Snapshot For Validation Check
    shared_training_infrastructure.save_yaml_snapshot(
        snapshot_dictionary=validation_summary,
        output_path=output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME,
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
        config_path=command_line_arguments.config_path,
        output_suffix=command_line_arguments.output_suffix,
    )

if __name__ == "__main__":

    main()
