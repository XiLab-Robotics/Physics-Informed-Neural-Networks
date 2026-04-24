"""Run the original-dataset exact RCIM model-bank validation workflow."""

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
from scripts.paper_reimplementation.rcim_ml_compensation import exact_paper_model_bank_support
from scripts.paper_reimplementation.rcim_ml_compensation import original_dataset_exact_model_bank_support
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "original_dataset_exact_model_bank"
    / "baseline_forward.yaml"
)


def run_original_dataset_exact_model_bank_validation(
    config_path: Path,
    output_suffix: str = "original_dataset_exact_validation",
) -> tuple[Path, Path]:

    """Run the direction-specific original-dataset exact-model workflow."""

    # Load And Prepare Configuration
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        f"Loading original-dataset exact config | {config_path}",
    )
    training_config = shared_training_infrastructure.prepare_output_artifact_training_config(
        original_dataset_exact_model_bank_support.load_original_dataset_exact_model_bank_config(config_path),
        artifact_kind=shared_training_infrastructure.VALIDATION_OUTPUT_ARTIFACT_KIND,
        run_name_suffix=output_suffix,
    )
    resolved_config_path = shared_training_infrastructure.resolve_project_relative_path(config_path)
    output_directory = shared_training_infrastructure.resolve_output_directory(training_config)
    output_directory.mkdir(parents=True, exist_ok=True)
    shared_training_infrastructure.save_training_config_snapshot(training_config, output_directory)
    shared_training_infrastructure.save_run_metadata_snapshot(training_config, output_directory)

    # Build The Direction-Specific Dataset Bundle
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Building original-dataset exact bundle",
    )
    original_dataset_bundle = (
        original_dataset_exact_model_bank_support.build_original_dataset_exact_model_bank_bundle(
            training_config
        )
    )
    exact_dataset_bundle = original_dataset_bundle.exact_dataset_bundle
    enabled_family_list = exact_paper_model_bank_support.resolve_enabled_family_list(training_config)
    direction_label = original_dataset_bundle.direction_label
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Original-dataset exact bundle ready | "
        f"direction={direction_label} "
        f"rows={len(exact_dataset_bundle.full_dataframe)} "
        f"targets={len(exact_dataset_bundle.target_name_list)} "
        f"families={len(enabled_family_list)}",
    )

    # Fit And Persist The Family Bank
    fitted_family_model_dictionary, family_search_summary_dictionary = (
        exact_paper_model_bank_support.fit_exact_family_model_bank(
            exact_dataset_bundle,
            enabled_family_list,
            training_config,
        )
    )
    model_bundle_path = exact_paper_model_bank_support.save_exact_family_model_bundle(
        fitted_family_model_dictionary,
        output_directory,
    )

    # Evaluate And Export ONNX Artifacts
    family_summary_list, per_target_ranking_dictionary = (
        exact_paper_model_bank_support.evaluate_exact_family_model_bank(
            exact_dataset_bundle,
            fitted_family_model_dictionary,
        )
    )
    onnx_export_summary = exact_paper_model_bank_support.export_exact_family_onnx_bank(
        exact_dataset_bundle,
        fitted_family_model_dictionary,
        training_config,
        output_directory,
    )

    # Persist Validation Summary And Markdown Report
    validation_summary = (
        original_dataset_exact_model_bank_support.build_original_dataset_validation_summary(
            resolved_config_path,
            output_directory,
            training_config,
            original_dataset_bundle,
            family_summary_list,
            family_search_summary_dictionary,
            per_target_ranking_dictionary,
            onnx_export_summary,
            model_bundle_path,
        )
    )
    validation_summary_path = output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

    validation_report_path = (
        original_dataset_exact_model_bank_support.build_original_dataset_validation_report_path(
            training_config
        )
    )
    validation_report_path.write_text(
        original_dataset_exact_model_bank_support.build_original_dataset_validation_report_markdown(
            validation_summary
        ),
        encoding="utf-8",
    )
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "DONE",
        "Original-dataset exact validation complete | "
        f"summary={shared_training_infrastructure.format_project_relative_path(validation_summary_path)} "
        f"report={shared_training_infrastructure.format_project_relative_path(validation_report_path)}",
    )
    return validation_summary_path, validation_report_path


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the original-dataset exact workflow."""

    argument_parser = argparse.ArgumentParser(
        description="Run the original-dataset exact RCIM model-bank validation workflow."
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the original-dataset exact-model-bank YAML configuration file.",
    )
    argument_parser.add_argument(
        "--output-suffix",
        type=str,
        default="original_dataset_exact_validation",
        help="Suffix appended to the immutable validation-check artifact.",
    )
    return argument_parser.parse_args()


def main() -> None:

    """Run the original-dataset exact validation entry point."""

    command_line_arguments = parse_command_line_arguments()
    run_original_dataset_exact_model_bank_validation(
        command_line_arguments.config_path,
        command_line_arguments.output_suffix,
    )


if __name__ == "__main__":

    main()
