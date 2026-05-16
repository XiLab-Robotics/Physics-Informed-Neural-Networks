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
from scripts.tooling import repository_path_support
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


def resolve_stage_execution_flags(
    workflow_stage: str,
    no_eval: bool,
    no_export: bool,
) -> tuple[bool, bool]:

    """Resolve whether evaluation and export stages should run."""

    normalized_stage = exact_paper_model_bank_support.resolve_exact_paper_workflow_stage(workflow_stage)
    if normalized_stage == "search":
        return (not no_eval), (not no_export)
    if normalized_stage == "loadbest":
        return (not no_eval), (not no_export)
    if normalized_stage == "eval":
        return True, False
    if normalized_stage == "export":
        return False, True
    raise AssertionError(f"Unsupported exact-paper workflow stage | {normalized_stage}")


def resolve_best_parameter_summary_payload(
    workflow_stage: str,
    training_config: dict[str, object],
    dataset_bundle: exact_paper_model_bank_support.ExactPaperDatasetBundle,
    enabled_family_list: list[str],
    workflow_variant: str,
    best_parameter_summary_path: Path | None,
    best_parameter_registry_path: Path | None,
) -> tuple[dict[str, object], str]:

    """Resolve the summary payload used for exact-paper `LoadBest` style runs."""

    normalized_stage = exact_paper_model_bank_support.resolve_exact_paper_workflow_stage(workflow_stage)
    if normalized_stage == "search":
        return {}, "grid_search"

    if best_parameter_summary_path is not None:
        exact_paper_model_bank_support.emit_exact_paper_progress_log(
            "INFO",
            "Loading explicit best-parameter summary | "
            f"path={best_parameter_summary_path.resolve()}",
        )
        return (
            exact_paper_model_bank_support.load_exact_paper_best_parameter_summary(best_parameter_summary_path),
            "explicit_summary",
        )

    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Resolving stored best-parameter summary from registry | "
        f"workflow_variant={workflow_variant} "
        f"registry={Path(best_parameter_registry_path or exact_paper_model_bank_support.EXACT_PAPER_BEST_PARAMETER_REGISTRY_PATH).resolve()}",
    )
    return (
        exact_paper_model_bank_support.resolve_exact_paper_best_parameter_summary_from_registry(
            training_config=training_config,
            dataset_bundle=dataset_bundle,
            workflow_variant=workflow_variant,
            enabled_family_list=enabled_family_list,
            registry_path=best_parameter_registry_path,
        ),
        "stored_registry",
    )


def run_exact_paper_model_bank_validation(
    config_path: Path,
    output_suffix: str = "exact_paper_validation",
    workflow_stage: str = "search",
    best_parameter_summary_path: Path | None = None,
    best_parameter_registry_path: Path | None = None,
    no_eval: bool = False,
    no_export: bool = False,
    grid_search_verbose_override: int | None = None,
    historical_cross_validate_verbose_override: int | None = None,
) -> tuple[Path | None, Path | None]:

    """Run the paper-faithful RCIM family-bank validation workflow.

    Args:
        config_path: Exact-paper YAML configuration path.
        output_suffix: Suffix appended to the immutable validation artifact.

    Returns:
        Tuple containing the validation summary path and Markdown report path.
    """

    # Load And Prepare Configuration
    normalized_stage = exact_paper_model_bank_support.resolve_exact_paper_workflow_stage(workflow_stage)
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Loading exact-paper config | "
        f"config={config_path} "
        f"stage={normalized_stage}",
    )
    training_config = shared_training_infrastructure.prepare_output_artifact_training_config(
        exact_paper_model_bank_support.load_exact_model_bank_config(config_path),
        artifact_kind=shared_training_infrastructure.VALIDATION_OUTPUT_ARTIFACT_KIND,
        run_name_suffix=output_suffix,
    )
    training_config.setdefault("training", {})
    training_config["training"].setdefault("hyperparameter_search", {})
    if grid_search_verbose_override is not None and int(grid_search_verbose_override) >= 0:
        training_config["training"]["hyperparameter_search"]["grid_search_verbose"] = int(grid_search_verbose_override)
    if historical_cross_validate_verbose_override is not None and int(historical_cross_validate_verbose_override) >= 0:
        training_config["training"]["hyperparameter_search"]["historical_cross_validate_verbose"] = int(
            historical_cross_validate_verbose_override
        )
    resolved_config_path = shared_training_infrastructure.resolve_project_relative_path(config_path)
    output_directory = shared_training_infrastructure.resolve_output_directory(training_config)
    output_directory.mkdir(parents=True, exist_ok=True)
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Exact-paper output directory | "
        f"{shared_training_infrastructure.format_project_relative_path(output_directory)}",
    )
    should_run_evaluation, should_run_export = resolve_stage_execution_flags(
        workflow_stage=normalized_stage,
        no_eval=no_eval,
        no_export=no_export,
    )
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Exact-paper stage execution plan | "
        f"stage={normalized_stage} "
        f"run_evaluation={should_run_evaluation} "
        f"run_export={should_run_export}",
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
        f"historical_cross_validate_verbose={search_settings['historical_cross_validate_verbose']} "
        f"grid_search_pre_dispatch={search_settings['grid_search_pre_dispatch']} "
        f"families={','.join(enabled_family_list)}",
    )

    # Resolve Optional Stored Best Parameters
    best_parameter_override_map = None
    best_parameter_source_name = "grid_search"
    if normalized_stage != "search":
        best_parameter_summary_payload, best_parameter_source_name = resolve_best_parameter_summary_payload(
            workflow_stage=normalized_stage,
            training_config=training_config,
            dataset_bundle=dataset_bundle,
            enabled_family_list=enabled_family_list,
            workflow_variant="exact_paper_model_bank",
            best_parameter_summary_path=best_parameter_summary_path,
            best_parameter_registry_path=best_parameter_registry_path,
        )
        best_parameter_override_map = exact_paper_model_bank_support.build_exact_paper_best_parameter_override_map(
            best_parameter_summary_payload,
            enabled_family_list,
        )
        exact_paper_model_bank_support.emit_exact_paper_progress_log(
            "INFO",
            "Exact-paper stored best-parameter source resolved | "
            f"stage={normalized_stage} "
            f"source={best_parameter_source_name} "
            f"families={','.join(enabled_family_list)}",
        )

    # Fit And Persist The Family Bank
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "INFO",
        "Fitting family bank | "
        f"stage={normalized_stage} "
        f"best_parameter_source={best_parameter_source_name} "
        f"families={', '.join(enabled_family_list)}",
    )
    fitted_family_model_dictionary, family_search_summary_dictionary = exact_paper_model_bank_support.fit_exact_family_model_bank(
        dataset_bundle,
        enabled_family_list,
        training_config,
        best_parameter_override_map=best_parameter_override_map,
        workflow_stage=normalized_stage,
    )
    model_bundle_path = exact_paper_model_bank_support.save_exact_family_model_bundle(
        fitted_family_model_dictionary,
        output_directory,
    )
    exact_paper_model_bank_support.emit_exact_paper_progress_log(
        "DONE",
        "Exact-paper model bundle written | "
        f"{shared_training_infrastructure.format_project_relative_path(model_bundle_path)}",
    )

    # Optionally Evaluate The Family Bank
    family_summary_list: list[dict[str, object]] = []
    per_target_ranking_dictionary: dict[str, list[dict[str, object]]] = {}
    if should_run_evaluation:
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
    else:
        exact_paper_model_bank_support.emit_exact_paper_progress_log(
            "INFO",
            "Evaluation stage skipped by operator stage selection",
        )

    # Persist Search-Time Best Parameters When Available
    best_parameter_summary_path_written: Path | None = None
    if any(
        family_search_entry.get("best_params") is not None
        for family_search_entry in family_search_summary_dictionary.values()
    ):
        best_parameter_summary = exact_paper_model_bank_support.build_exact_paper_best_parameter_summary(
            workflow_variant="exact_paper_model_bank",
            training_config=training_config,
            dataset_bundle=dataset_bundle,
            family_summary_list=family_summary_list,
            family_search_summary_dictionary=family_search_summary_dictionary,
            validation_summary_path=None,
            output_directory=output_directory,
        )
        best_parameter_summary_path_written = exact_paper_model_bank_support.save_exact_paper_best_parameter_summary(
            best_parameter_summary,
            output_directory,
        )
        best_parameter_summary["best_parameter_summary_path"] = shared_training_infrastructure.format_project_relative_path(
            best_parameter_summary_path_written
        )
        exact_paper_model_bank_support.update_exact_paper_best_parameter_registry(best_parameter_summary)
        exact_paper_model_bank_support.emit_exact_paper_progress_log(
            "DONE",
            "Best-parameter summary written | "
            f"{shared_training_infrastructure.format_project_relative_path(best_parameter_summary_path_written)}",
        )

    # Optionally Export Python And ONNX Artifacts
    if should_run_export:
        exact_paper_model_bank_support.emit_exact_paper_progress_log(
            "INFO",
            "Exporting Python+ONNX family bank",
        )
        onnx_export_summary = exact_paper_model_bank_support.export_exact_family_python_and_onnx_bank(
            dataset_bundle,
            fitted_family_model_dictionary,
            training_config,
            output_directory,
        )
        failed_export_count = int(
            sum(
                family_entry["failed_onnx_target_count"]
                for family_entry in onnx_export_summary["family_exports"]
            )
        )
        exact_paper_model_bank_support.emit_exact_paper_progress_log(
            "INFO",
            "Python+ONNX export complete | "
            f"python_exported={onnx_export_summary['python_exported_file_count']} "
            f"onnx_exported={onnx_export_summary['onnx_exported_file_count']} "
            f"onnx_failed={failed_export_count}",
        )
    else:
        onnx_export_summary = {
            "enabled": False,
            "target_opset": int(training_config["export"]["target_opset"]),
            "export_failure_mode": str(training_config["export"].get("export_failure_mode", "continue")),
            "enable_empty_svr_constant_surrogate": bool(training_config["export"].get("enable_empty_svr_constant_surrogate", True)),
            "python_export_root": shared_training_infrastructure.format_project_relative_path(output_directory / exact_paper_model_bank_support.EXACT_PYTHON_EXPORT_ROOTNAME),
            "python_exported_file_count": 0,
            "onnx_export_root": shared_training_infrastructure.format_project_relative_path(output_directory / exact_paper_model_bank_support.EXACT_ONNX_EXPORT_ROOTNAME),
            "onnx_exported_file_count": 0,
            "recovered_reference_root": None,
            "recovered_reference_file_count": 0,
            "matched_reference_relative_paths": [],
            "missing_against_reference_relative_paths": [],
            "extra_export_relative_paths": [],
            "family_exports": [],
        }
        exact_paper_model_bank_support.emit_exact_paper_progress_log(
            "INFO",
            "Export stage skipped by operator stage selection",
        )

    # Persist Validation Summary And Markdown Report When Evaluation Is Enabled
    validation_summary_path: Path | None = None
    validation_report_path: Path | None = None
    if should_run_evaluation:
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
        if best_parameter_summary_path_written is not None:
            validation_summary["artifacts"]["best_parameter_summary_path"] = (
                shared_training_infrastructure.format_project_relative_path(best_parameter_summary_path_written)
            )
        validation_summary_path = output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME
        shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

        validation_report_path = exact_paper_model_bank_support.build_validation_report_path(training_config)
        validation_report_path.write_text(
            exact_paper_model_bank_support.build_exact_model_report_markdown(validation_summary),
            encoding="utf-8",
        )
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
    else:
        exact_paper_model_bank_support.emit_exact_paper_progress_log(
            "INFO",
            "Validation summary and Markdown report skipped because evaluation was not requested",
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
    argument_parser.add_argument(
        "--stage",
        type=str,
        default="search",
        help="Operator stage: search, eval, export, or loadbest.",
    )
    argument_parser.add_argument(
        "--best-parameter-summary-path",
        type=Path,
        default=None,
        help="Optional exact-paper best-parameter summary used by eval/export/loadbest.",
    )
    argument_parser.add_argument(
        "--best-parameter-registry-path",
        type=Path,
        default=None,
        help="Optional registry override for exact-paper stored best parameters.",
    )
    argument_parser.add_argument(
        "--no-eval",
        action="store_true",
        help="Skip evaluation after search or loadbest.",
    )
    argument_parser.add_argument(
        "--no-export",
        action="store_true",
        help="Skip ONNX export after search or loadbest.",
    )
    argument_parser.add_argument(
        "--grid-search-verbose-override",
        type=int,
        default=-1,
        help="Optional runtime override for GridSearchCV verbose.",
    )
    argument_parser.add_argument(
        "--historical-cross-validate-verbose-override",
        type=int,
        default=-1,
        help="Optional runtime override for historical cross_validate verbose.",
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser.parse_args()


def main() -> None:

    """Run the exact-paper validation entry point."""

    command_line_arguments = parse_command_line_arguments()
    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(command_line_arguments)
    )
    run_exact_paper_model_bank_validation(
        command_line_arguments.config_path,
        command_line_arguments.output_suffix,
        workflow_stage=command_line_arguments.stage,
        best_parameter_summary_path=command_line_arguments.best_parameter_summary_path,
        best_parameter_registry_path=command_line_arguments.best_parameter_registry_path,
        no_eval=bool(command_line_arguments.no_eval),
        no_export=bool(command_line_arguments.no_export),
        grid_search_verbose_override=(
            command_line_arguments.grid_search_verbose_override
            if command_line_arguments.grid_search_verbose_override >= 0
            else None
        ),
        historical_cross_validate_verbose_override=(
            command_line_arguments.historical_cross_validate_verbose_override
            if command_line_arguments.historical_cross_validate_verbose_override >= 0
            else None
        ),
    )


if __name__ == "__main__":

    main()
