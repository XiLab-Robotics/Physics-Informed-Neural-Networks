from __future__ import annotations

# Import Python Utilities
import sys, argparse
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import PyTorch Lightning Utilities
from lightning.pytorch import Trainer

# Import YAML Utilities
import yaml
import numpy as np

# Import Project Utilities
from scripts.training import shared_training_infrastructure
from scripts.training import tree_regression_support
from scripts.training.transmission_error_regression_module import TransmissionErrorRegressionModule

TREE_MODEL_TYPE_LIST = ["random_forest", "hist_gradient_boosting"]

def build_smoke_test_summary(
    config_path: Path,
    output_directory: Path,
    checkpoint_path: Path,
    training_config: dict[str, object],
    fast_dev_run_batches: int,
) -> dict[str, object]:

    """ Build Smoke Test Summary """

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
        "fast_dev_run_batches": int(fast_dev_run_batches),
        "checkpoint_path": str(checkpoint_path),
        "checks": {
            "checkpoint_exists": bool(checkpoint_path.exists()),
        },
    }

def run_training_smoke_test(config_path: Path, output_suffix: str = "smoke_test", fast_dev_run_batches: int = 1) -> None:

    """ Run Training Smoke Test """

    assert fast_dev_run_batches > 0, f"fast_dev_run_batches must be positive | {fast_dev_run_batches}"

    # Prepare Training Config and Output Directory
    training_config = shared_training_infrastructure.prepare_output_artifact_training_config(
        shared_training_infrastructure.load_training_config(config_path),
        artifact_kind=shared_training_infrastructure.SMOKE_TEST_OUTPUT_ARTIFACT_KIND,
        run_name_suffix=output_suffix,
    )

    # Force Single-Process Smoke Testing To Keep The Check Robust In Restricted Environments
    training_config["dataset"]["num_workers"] = 0
    training_config["dataset"]["pin_memory"] = False
    if "n_jobs" in training_config["model"]:
        training_config["model"]["n_jobs"] = 1

    # Prepare Output Directory
    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    output_directory = shared_training_infrastructure.resolve_output_directory(training_config)
    output_directory.mkdir(parents=True, exist_ok=True)
    shared_training_infrastructure.save_run_metadata_snapshot(training_config, output_directory)

    # Run Tree-Specific Smoke Test For The Scikit-Learn Baselines
    if experiment_identity.model_type in TREE_MODEL_TYPE_LIST:

        # Build Dataset Splits And Estimator
        datamodule, split_dictionary = tree_regression_support.build_tree_split_bundle(training_config)
        estimator = tree_regression_support.build_tree_estimator(training_config)
        train_input = split_dictionary["train_input"][:tree_regression_support.TREE_SMOKE_TRAIN_SAMPLE_COUNT]
        train_target = split_dictionary["train_target"][:tree_regression_support.TREE_SMOKE_TRAIN_SAMPLE_COUNT]
        validation_input = split_dictionary["validation_input"][:tree_regression_support.TREE_SMOKE_EVAL_SAMPLE_COUNT]

        # Fit The Estimator On The Flattened Train Split
        estimator.fit(train_input, train_target)
        checkpoint_path = tree_regression_support.save_tree_model(estimator, output_directory)
        reloaded_estimator = tree_regression_support.load_tree_model(checkpoint_path)
        reloaded_prediction_vector = reloaded_estimator.predict(validation_input)

        # Build Smoke Test Summary
        smoke_test_summary = build_smoke_test_summary(
            shared_training_infrastructure.resolve_project_relative_path(config_path),
            output_directory,
            checkpoint_path,
            training_config,
            fast_dev_run_batches,
        )

        # Perform Smoke Test Checks
        smoke_test_summary["checks"]["reload_prediction_finite"] = bool(np.isfinite(reloaded_prediction_vector).all())
        smoke_test_summary["checks"]["checkpoint_exists"] = bool(checkpoint_path.exists())

        # Save Smoke Test Summary
        with (output_directory / shared_training_infrastructure.COMMON_SMOKE_TEST_FILENAME).open("w", encoding="utf-8") as output_file:
            yaml.safe_dump(smoke_test_summary, output_file, sort_keys=False)

        print(f"[DONE] Training smoke test completed | {output_directory / shared_training_infrastructure.COMMON_SMOKE_TEST_FILENAME}")
        return

    # Initialize Training Components
    datamodule, regression_backbone, regression_module, normalization_statistics = shared_training_infrastructure.initialize_training_components(training_config)
    input_feature_dim = datamodule.get_input_feature_dim()
    target_feature_dim = datamodule.get_target_feature_dim()

    # Initialize Lightning Trainer
    trainer = Trainer(
        default_root_dir=str(output_directory),
        accelerator="cpu",
        devices=1,
        precision="32",
        logger=False,
        enable_checkpointing=False,
        enable_model_summary=False,
        enable_progress_bar=False,
        fast_dev_run=fast_dev_run_batches,
        deterministic=True,
    )

    # Run Training Loop
    trainer.fit(regression_module, datamodule=datamodule)

    # Save Checkpoint After Training Loop Completes
    checkpoint_path = output_directory / "smoke_test_checkpoint.ckpt"
    trainer.save_checkpoint(str(checkpoint_path))

    # Reload the Regression Module from the Checkpoint
    reloaded_regression_module = TransmissionErrorRegressionModule.load_from_checkpoint(
        checkpoint_path=str(checkpoint_path),
        regression_model=shared_training_infrastructure.create_regression_backbone_from_training_config(
            training_config,
            input_feature_dim,
        ),
        input_feature_dim=input_feature_dim,
        target_feature_dim=target_feature_dim,
        normalization_statistics=normalization_statistics,
    )
    reloaded_regression_module.eval()

    # Build Smoke Test Summary
    smoke_test_summary = build_smoke_test_summary(
        shared_training_infrastructure.resolve_project_relative_path(config_path),
        output_directory,
        checkpoint_path,
        training_config,
        fast_dev_run_batches,
    )

    # Save Smoke Test Summary
    with (output_directory / shared_training_infrastructure.COMMON_SMOKE_TEST_FILENAME).open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(smoke_test_summary, output_file, sort_keys=False)

    print(f"[DONE] Training smoke test completed | {output_directory / shared_training_infrastructure.COMMON_SMOKE_TEST_FILENAME}")

def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command Line Arguments """

    # Define Command Line Arguments
    argument_parser = argparse.ArgumentParser(description="Run a minimal Lightning smoke test for the current TE training workflow.")
    argument_parser.add_argument("--config-path", type=Path, default=shared_training_infrastructure.DEFAULT_CONFIG_PATH, help="Path to the YAML training configuration file.")
    argument_parser.add_argument("--output-suffix", type=str, default="smoke_test", help="Suffix appended to the run directory for the smoke-test artifacts.")
    argument_parser.add_argument("--fast-dev-run-batches", type=int, default=1, help="Number of fast_dev_run batches used by Lightning.")
    return argument_parser.parse_args()

def main() -> None:

    """ Main Function """

    # Parse Command Line Arguments
    command_line_arguments = parse_command_line_arguments()

    # Run Training Smoke Test
    run_training_smoke_test(
        command_line_arguments.config_path,
        command_line_arguments.output_suffix,
        command_line_arguments.fast_dev_run_batches,
    )

if __name__ == "__main__":

    main()
