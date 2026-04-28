"""Run the exact RCIM paper model-bank validation workflow."""

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
from scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank import exact_paper_model_bank_support
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "exact_model_bank"
    / "baseline.yaml"
)


def run_exact_paper_model_bank_validation(
    config_path: Path,
    output_suffix: str = "exact_paper_validation",
) -> tuple[Path, Path]:

    """Run the paper-faithful RCIM family-bank validation workflow.

    Args:
        config_path: Exact-paper YAML configuration path.
        output_suffix: Suffix appended to the immutable validation artifact.

    Returns:
        Tuple containing the validation summary path and Markdown report path.
    """

    # Load And Prepare Configuration
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        f"Loading exact-paper config | {config_path}",
    )
    training_config = shared_training_infrastructure.prepare_output_artifact_training_config(
        exact_paper_model_bank_support.load_exact_model_bank_config(config_path),
        artifact_kind=shared_training_infrastructure.VALIDATION_OUTPUT_ARTIFACT_KIND,
        run_name_suffix=output_suffix,
    )
    resolved_config_path = shared_training_infrastructure.resolve_project_relative_path(config_path)
    output_directory = shared_training_infrastructure.resolve_output_directory(training_config)
    output_directory.mkdir(parents=True, exist_ok=True)
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Exact-paper output directory | "
        f"{shared_training_infrastructure.format_project_relative_path(output_directory)}",
    )

    # Persist Canonical Artifact Metadata
    shared_training_infrastructure.save_training_config_snapshot(training_config, output_directory)
    shared_training_infrastructure.save_run_metadata_snapshot(training_config, output_directory)

    # Build The Exact Paper Dataset
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Building exact-paper dataset bundle",
    )
    dataset_bundle = exact_paper_model_bank_support.build_exact_paper_dataset_bundle(training_config)
    enabled_family_list = exact_paper_model_bank_support.resolve_enabled_family_list(training_config)
    target_scope = exact_paper_model_bank_support.resolve_exact_target_scope(training_config)
    search_settings = exact_paper_model_bank_support.resolve_exact_paper_hyperparameter_search_settings(training_config)
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Exact-paper dataset ready | "
        f"rows={len(dataset_bundle.full_dataframe)} "
        f"targets={len(dataset_bundle.target_name_list)} "
        f"families={len(enabled_family_list)} "
        f"scope_mode={target_scope['mode']}",
    )
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Exact-paper target scope | "
        f"{exact_paper_model_bank_support.build_exact_target_scope_log_summary(dataset_bundle.target_name_list)}",
    )
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Exact-paper search settings | "
        f"mode={search_settings['mode']} "
        f"grid_search_n_jobs={search_settings['grid_search_n_jobs']} "
        f"grid_search_verbose={search_settings['grid_search_verbose']} "
        f"grid_search_pre_dispatch={search_settings['grid_search_pre_dispatch']} "
        f"families={','.join(enabled_family_list)}",
    )

    # Fit And Persist The Family Bank
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        f"Fitting family bank | {', '.join(enabled_family_list)}",
    )
    fitted_family_model_dictionary, family_search_summary_dictionary = exact_paper_model_bank_support.fit_exact_family_model_bank(
        dataset_bundle,
        enabled_family_list,
        training_config,
    )
    model_bundle_path = exact_paper_model_bank_support.save_exact_family_model_bundle(
        fitted_family_model_dictionary,
        output_directory,
    )

    # Evaluate And Export ONNX Artifacts
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Evaluating family bank",
    )
    family_summary_list, per_target_ranking_dictionary = (
        exact_paper_model_bank_support.evaluate_exact_family_model_bank(
            dataset_bundle,
            fitted_family_model_dictionary,
        )
    )
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Evaluation complete | "
        f"winner={family_summary_list[0]['family_name']} "
        f"mean_component_mape={family_summary_list[0]['mean_component_mape_percent']:.3f}%",
    )
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Exporting ONNX family bank",
    )
    onnx_export_summary = exact_paper_model_bank_support.export_exact_family_onnx_bank(
        dataset_bundle,
        fitted_family_model_dictionary,
        training_config,
        output_directory,
    )
    failed_export_count = int(
        sum(
            family_entry["failed_target_count"]
            for family_entry in onnx_export_summary["family_exports"]
        )
    )
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "ONNX export complete | "
        f"exported={onnx_export_summary['exported_file_count']} "
        f"failed={failed_export_count}",
    )

    # Persist Validation Summary And Markdown Report
    validation_summary = exact_paper_model_bank_support.build_exact_model_validation_summary(
        resolved_config_path,
        output_directory,
        training_config,
        dataset_bundle,
        family_summary_list,
        family_search_summary_dictionary,
        per_target_ranking_dictionary,
        onnx_export_summary,
        model_bundle_path,
    )
    validation_summary_path = output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

    validation_report_path = exact_paper_model_bank_support.build_validation_report_path(training_config)
    validation_report_path.write_text(
        exact_paper_model_bank_support.build_exact_model_report_markdown(validation_summary),
        encoding="utf-8",
    )

    # Report Final Artifact Locations
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "DONE",
        "Exact paper validation summary written | "
        f"{shared_training_infrastructure.format_project_relative_path(validation_summary_path)}",
    )
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "DONE",
        "Exact paper Markdown report written | "
        f"{shared_training_infrastructure.format_project_relative_path(validation_report_path)}",
    )
    return validation_summary_path, validation_report_path


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the exact paper workflow."""

    argument_parser = argparse.ArgumentParser(
        description="Run the exact paper-faithful RCIM family-bank validation workflow."
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the exact-paper YAML configuration file.",
    )
    argument_parser.add_argument(
        "--output-suffix",
        type=str,
        default="exact_paper_validation",
        help="Suffix appended to the immutable validation-check artifact.",
    )
    return argument_parser.parse_args()


def main() -> None:

    """Run the exact-paper validation entry point."""

    command_line_arguments = parse_command_line_arguments()
    run_exact_paper_model_bank_validation(
        command_line_arguments.config_path,
        command_line_arguments.output_suffix,
    )


if __name__ == "__main__":

    main()
