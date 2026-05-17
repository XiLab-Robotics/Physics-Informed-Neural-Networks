"""Run the Track 2 reference-family vs feedforward TE-curve comparison."""

from __future__ import annotations

# Import Python Utilities
import argparse
import sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[4]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.tooling import repository_path_support
from scripts.paper_reimplementation.rcim_ml_compensation.harmonic_wise_comparison import harmonic_wise_support
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import reference_family_vs_feedforward_support
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "baseline.yaml"
)


def run_reference_family_vs_feedforward_comparison(
    config_path: Path,
    output_suffix: str = "baseline_validation",
) -> tuple[Path, Path]:

    """Run one Track 2 comparison over the configured candidate matrix."""

    # Load And Prepare Configuration
    training_config = shared_training_infrastructure.prepare_output_artifact_training_config(
        reference_family_vs_feedforward_support.load_reference_family_comparison_config(config_path),
        artifact_kind=shared_training_infrastructure.VALIDATION_OUTPUT_ARTIFACT_KIND,
        run_name_suffix=output_suffix,
    )
    resolved_config_path = shared_training_infrastructure.resolve_project_relative_path(config_path)
    output_directory = shared_training_infrastructure.resolve_output_directory(training_config)
    output_directory.mkdir(parents=True, exist_ok=True)
    shared_training_infrastructure.save_training_config_snapshot(training_config, output_directory)
    shared_training_infrastructure.save_run_metadata_snapshot(training_config, output_directory)

    # Load Configured Candidate Matrix
    candidate_configuration_list = reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(
        training_config
    )
    candidate_list = [
        reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)
        for candidate_configuration in candidate_configuration_list
    ]
    selected_harmonic_list = sorted(
        {
            harmonic_order
            for candidate in candidate_list
            for harmonic_order in candidate.selected_harmonic_list
        }
    )

    # Build Held-Out Curve Records
    curve_record_list, _, _, dataset_root = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )

    # Evaluate Candidates On Their Direction-Valid Held-Out Curves
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])
    per_candidate_entry_list: list[dict[str, object]] = []
    target_metric_dictionary: dict[str, dict[str, float]] = {}
    for candidate in candidate_list:
        candidate_entry_list, candidate_target_metric_dictionary = (
            reference_family_vs_feedforward_support.evaluate_track2_candidate(
                candidate,
                curve_record_list,
                percentage_error_denominator,
            )
        )
        per_candidate_entry_list.extend(candidate_entry_list)
        if candidate_target_metric_dictionary is not None:
            target_metric_dictionary[candidate.candidate_id] = candidate_target_metric_dictionary

    # Build Aggregate Summaries And Artifacts
    per_condition_metrics_csv_path = reference_family_vs_feedforward_support.save_track2_per_condition_metrics_csv(
        output_directory,
        per_candidate_entry_list,
    )
    preview_plot_path_list = reference_family_vs_feedforward_support.maybe_generate_track2_preview_plots(
        output_directory,
        per_candidate_entry_list,
        int(training_config["comparison"]["preview_curve_count"]),
    )

    # Save Summary And Report
    comparison_summary = reference_family_vs_feedforward_support.build_track2_directional_comparison_summary(
        resolved_config_path,
        output_directory,
        training_config,
        curve_record_list,
        candidate_list,
        target_metric_dictionary,
        per_candidate_entry_list,
        preview_plot_path_list,
        per_condition_metrics_csv_path,
        dataset_root,
    )
    validation_summary_path = output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME
    shared_training_infrastructure.save_yaml_snapshot(comparison_summary, validation_summary_path)

    validation_report_path = reference_family_vs_feedforward_support.build_comparison_report_path(training_config)
    validation_report_path.parent.mkdir(parents=True, exist_ok=True)
    validation_report_path.write_text(
        reference_family_vs_feedforward_support.build_track2_directional_comparison_report_markdown(
            comparison_summary
        ),
        encoding="utf-8",
    )

    print(
        "[DONE] Reference family comparison summary written | "
        f"{shared_training_infrastructure.format_project_relative_path(validation_summary_path)}"
    )
    print(
        "[DONE] Reference family comparison report written | "
        f"{shared_training_infrastructure.format_project_relative_path(validation_report_path)}"
    )
    return validation_summary_path, validation_report_path


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the comparison entry point."""

    argument_parser = argparse.ArgumentParser(
        description="Run the Track 2 reference-family vs feedforward comparison."
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the YAML comparison configuration file.",
    )
    argument_parser.add_argument(
        "--output-suffix",
        type=str,
        default="baseline_validation",
        help="Suffix appended to the immutable validation-check artifact.",
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser.parse_args()


def main() -> None:

    """Run the command-line comparison entry point."""

    command_line_arguments = parse_command_line_arguments()
    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(command_line_arguments)
    )
    run_reference_family_vs_feedforward_comparison(
        command_line_arguments.config_path,
        command_line_arguments.output_suffix,
    )


if __name__ == "__main__":

    main()
