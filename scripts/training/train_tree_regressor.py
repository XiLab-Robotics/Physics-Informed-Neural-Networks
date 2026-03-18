from __future__ import annotations

# Import Python Utilities
import sys, argparse
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.training import shared_training_infrastructure
from scripts.training import tree_regression_support

def build_tree_training_report(metrics_snapshot_dictionary: dict[str, object]) -> str:

    """ Build Tree Training Report """

    # Extract Relevant Information From The Metrics Snapshot Dictionary To Build The Report
    experiment_dictionary = metrics_snapshot_dictionary["experiment"]
    dataset_split_dictionary = metrics_snapshot_dictionary["dataset_split"]
    validation_metric_dictionary = metrics_snapshot_dictionary["validation_metrics"]
    test_metric_dictionary = metrics_snapshot_dictionary["test_metrics"]

    # Build The Report As A List Of Lines To Be Joined With Newlines For Output
    report_line_list = [
        "# Tree Regression Training And Testing Report",
        "",
        "## Overview",
        "",
        f"- Run Name: `{experiment_dictionary['run_name']}`",
        f"- Model Family: `{experiment_dictionary['model_family']}`",
        f"- Model Type: `{experiment_dictionary['model_type']}`",
        f"- Saved Model Artifact: `{metrics_snapshot_dictionary['artifacts']['best_checkpoint_path']}`",
        "",
        "## Dataset Split",
        "",
        f"- Train Curves: `{dataset_split_dictionary['train_curve_count']}`",
        f"- Validation Curves: `{dataset_split_dictionary['validation_curve_count']}`",
        f"- Test Curves: `{dataset_split_dictionary['test_curve_count']}`",
        "",
        "## Validation Metrics",
        "",
    ]

    # Build Validation Metrics Report
    for metric_name, metric_value in validation_metric_dictionary.items():
        report_line_list.append(f"- {metric_name}: `{metric_value}`")

    # Add Test Metrics Section Header
    report_line_list.extend([
        "",
        "## Test Metrics",
        "",
    ])

    # Append Test Metric Lines
    for metric_name, metric_value in test_metric_dictionary.items():
        report_line_list.append(f"- {metric_name}: `{metric_value}`")

    # Add Interpretation
    report_line_list.extend([
        "",
        "## Interpretation",
        "",
        "This report records the static tabular tree benchmark under the shared TE artifact schema.",
    ])

    return "\n".join(report_line_list) + "\n"

def train_tree_regressor(config_path: str | Path) -> None:

    """ Train Tree Regressor """

    # Load Training Configuration And Resolve Output Directory
    training_config = shared_training_infrastructure.prepare_output_artifact_training_config(
        shared_training_infrastructure.load_training_config(config_path)
    )
    output_directory = shared_training_infrastructure.resolve_output_directory(training_config)
    output_directory.mkdir(parents=True, exist_ok=True)
    shared_training_infrastructure.save_training_config_snapshot(training_config, output_directory)
    shared_training_infrastructure.save_run_metadata_snapshot(training_config, output_directory)

    # Build Dataset Splits And Estimator
    datamodule, split_dictionary = tree_regression_support.build_tree_split_bundle(training_config)
    estimator = tree_regression_support.build_tree_estimator(training_config)

    # Fit The Estimator On The Flattened Train Split
    estimator.fit(split_dictionary["train_input"], split_dictionary["train_target"])

    # Evaluate Validation And Test Splits
    validation_prediction_vector = estimator.predict(split_dictionary["validation_input"])
    test_prediction_vector = estimator.predict(split_dictionary["test_input"])
    validation_metric_dictionary = tree_regression_support.compute_regression_metric_dictionary(
        split_dictionary["validation_target"],
        validation_prediction_vector,
    )
    test_metric_dictionary = tree_regression_support.compute_regression_metric_dictionary(
        split_dictionary["test_target"],
        test_prediction_vector,
    )

    # Save Model Artifact And Metrics Snapshot
    model_artifact_path = tree_regression_support.save_tree_model(estimator, output_directory)
    parameter_summary = tree_regression_support.resolve_tree_parameter_summary(training_config, estimator)
    runtime_config = tree_regression_support.build_tree_runtime_config(training_config)
    metrics_snapshot_dictionary = tree_regression_support.build_tree_metrics_snapshot(
        training_config,
        shared_training_infrastructure.resolve_project_relative_path(config_path),
        output_directory,
        datamodule,
        parameter_summary,
        runtime_config,
        model_artifact_path,
        validation_metric_dictionary,
        test_metric_dictionary,
    )
    shared_training_infrastructure.save_common_metrics_snapshot(metrics_snapshot_dictionary, output_directory)

    # Save Report And Update Registries
    report_path = output_directory / shared_training_infrastructure.COMMON_RUN_REPORT_FILENAME
    report_path.write_text(build_tree_training_report(metrics_snapshot_dictionary), encoding="utf-8")
    family_best_entry = shared_training_infrastructure.update_family_registry(metrics_snapshot_dictionary)
    shared_training_infrastructure.update_program_registry(family_best_entry)

    print(f"[DONE] Tree regression training workflow completed | {output_directory}")

def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command Line Arguments """

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(description="Train the configured TE tree-regression baseline.")
    argument_parser.add_argument("--config-path", type=Path, required=True, help="Path to the YAML training configuration file.")
    return argument_parser.parse_args()

def main() -> None:

    """ Main Function """

    # Parse Command Line Arguments
    command_line_arguments = parse_command_line_arguments()
    train_tree_regressor(command_line_arguments.config_path)

if __name__ == "__main__":

    main()
