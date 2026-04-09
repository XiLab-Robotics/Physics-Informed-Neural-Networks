"""Run the offline harmonic-wise comparison pipeline against the paper reference."""

from __future__ import annotations

# Import Python Utilities
import argparse
import sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation import harmonic_wise_support
from scripts.reports.generate_training_results_master_summary import generate_training_results_master_summary
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = PROJECT_PATH / "config" / "paper_reimplementation" / "rcim_ml_compensation" / "harmonic_wise" / "baseline.yaml"


def run_harmonic_wise_comparison_pipeline(
    config_path: Path,
    output_suffix: str = "baseline_validation",
) -> tuple[Path, Path, Path]:

    """Run the repository-owned offline harmonic-wise validation pipeline.

    Args:
        config_path: Harmonic-wise configuration path.
        output_suffix: Suffix appended to the immutable validation artifact.

    Returns:
        Tuple containing the validation summary path, Markdown report path, and
        regenerated master summary path.
    """

    # Load And Prepare Configuration
    training_config = shared_training_infrastructure.prepare_output_artifact_training_config(
        harmonic_wise_support.load_harmonic_pipeline_config(config_path),
        artifact_kind=shared_training_infrastructure.VALIDATION_OUTPUT_ARTIFACT_KIND,
        run_name_suffix=output_suffix,
    )
    resolved_config_path = shared_training_infrastructure.resolve_project_relative_path(config_path)
    output_directory = shared_training_infrastructure.resolve_output_directory(training_config)
    output_directory.mkdir(parents=True, exist_ok=True)

    # Persist Canonical Artifact Metadata
    shared_training_infrastructure.save_training_config_snapshot(training_config, output_directory)
    shared_training_infrastructure.save_run_metadata_snapshot(training_config, output_directory)

    # Build Harmonic-Wise Datasets
    selected_harmonic_list = harmonic_wise_support.resolve_selected_harmonic_list(training_config)
    split_record_bundle, directional_count_dictionary, file_count_dictionary, _ = harmonic_wise_support.build_split_record_bundle(training_config)
    train_feature_matrix, train_target_matrix, target_name_list = harmonic_wise_support.build_feature_target_matrix(
        split_record_bundle["train"],
        selected_harmonic_list,
    )

    # Fit Harmonic Target Models
    harmonic_model_dictionary = harmonic_wise_support.fit_harmonic_target_models(
        train_feature_matrix,
        train_target_matrix,
        target_name_list,
        training_config["model"],
    )
    harmonic_wise_support.save_harmonic_model_bundle(
        harmonic_model_dictionary,
        output_directory,
        selected_harmonic_list,
        target_name_list,
    )

    # Evaluate Validation And Test Splits
    percentage_error_denominator = str(training_config["evaluation"]["percentage_error_denominator"])
    validation_evaluation = harmonic_wise_support.evaluate_curve_record_split(
        split_record_bundle["validation"],
        harmonic_model_dictionary,
        selected_harmonic_list,
        target_name_list,
        percentage_error_denominator,
    )
    test_evaluation = harmonic_wise_support.evaluate_curve_record_split(
        split_record_bundle["test"],
        harmonic_model_dictionary,
        selected_harmonic_list,
        target_name_list,
        percentage_error_denominator,
    )

    # Run Offline Motion-Profile Playback
    playback_summary_dictionary = harmonic_wise_support.run_motion_profile_playback(
        training_config,
        harmonic_model_dictionary,
        selected_harmonic_list,
        target_name_list,
    )

    # Save Validation Summary And Markdown Report
    validation_summary = harmonic_wise_support.build_validation_summary(
        resolved_config_path,
        output_directory,
        training_config,
        selected_harmonic_list,
        directional_count_dictionary,
        file_count_dictionary,
        validation_evaluation,
        test_evaluation,
        playback_summary_dictionary,
    )
    validation_summary_path = output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

    validation_report_path = harmonic_wise_support.build_validation_report_path(training_config)
    validation_report_path.write_text(
        harmonic_wise_support.build_harmonic_report_markdown(validation_summary),
        encoding="utf-8",
    )

    # Refresh The Canonical Training Master Summary
    master_summary_path = generate_training_results_master_summary(
        PROJECT_PATH / "doc" / "reports" / "analysis" / "Training Results Master Summary.md"
    )

    print(f"[DONE] Harmonic-wise validation summary written | {shared_training_infrastructure.format_project_relative_path(validation_summary_path)}")
    print(f"[DONE] Harmonic-wise report written | {shared_training_infrastructure.format_project_relative_path(validation_report_path)}")
    print(f"[DONE] Training master summary refreshed | {shared_training_infrastructure.format_project_relative_path(master_summary_path)}")
    return validation_summary_path, validation_report_path, master_summary_path


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the harmonic-wise pipeline."""

    argument_parser = argparse.ArgumentParser(
        description="Run the repository-owned offline harmonic-wise comparison pipeline."
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the harmonic-wise YAML configuration file.",
    )
    argument_parser.add_argument(
        "--output-suffix",
        type=str,
        default="baseline_validation",
        help="Suffix appended to the immutable validation-check artifact.",
    )
    return argument_parser.parse_args()


def main() -> None:

    """Run the harmonic-wise comparison pipeline entry point."""

    command_line_arguments = parse_command_line_arguments()
    run_harmonic_wise_comparison_pipeline(
        command_line_arguments.config_path,
        command_line_arguments.output_suffix,
    )


if __name__ == "__main__":

    main()
