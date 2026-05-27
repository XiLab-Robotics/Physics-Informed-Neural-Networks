"""Run the Track 2 reference-family vs feedforward TE-curve comparison."""

from __future__ import annotations

# Import Python Utilities
import argparse
import copy
import csv
import gc
import shutil
import sys
from pathlib import Path

# Import Third-Party Libraries
import numpy as np

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

    # Resolve Configured Candidate Matrix
    candidate_configuration_list = reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(
        training_config
    )
    baseline_summary: dict[str, object] | None = None
    baseline_candidate_id_set: set[str] = set()
    baseline_summary_path_text = training_config["comparison"].get("baseline_summary_path")
    if baseline_summary_path_text is not None:
        baseline_summary_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
            baseline_summary_path_text
        )
        baseline_summary = reference_family_vs_feedforward_support.load_yaml_dictionary(baseline_summary_path)
        baseline_candidate_id_set = {
            str(candidate_entry["candidate_id"])
            for candidate_entry in baseline_summary["candidate_list"]
        }
        candidate_configuration_list = [
            candidate_configuration
            for candidate_configuration in candidate_configuration_list
            if str(candidate_configuration["candidate_id"]) not in baseline_candidate_id_set
        ]
        print(
            "[INFO] Running incremental Track 2 matrix refresh | "
            f"baseline_candidates={len(baseline_candidate_id_set)} | "
            f"new_candidates={len(candidate_configuration_list)}",
            flush=True,
        )
        assert candidate_configuration_list, "Incremental Track 2 refresh found no new candidates."
    report_plot_generation_scope = str(
        training_config["comparison"].get("report_plot_generation_scope", "incremental_current_candidates")
    ).strip()
    if baseline_summary is not None and report_plot_generation_scope == "incremental_current_candidates":
        print(
            "[INFO] Track 2 grouped report plots are limited to current incremental candidates.",
            flush=True,
        )
    selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]

    # Build Held-Out Curve Records
    print("[INFO] Building Track 2 held-out curve records", flush=True)
    curve_record_list, _, _, dataset_root = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    print(
        "[INFO] Built Track 2 held-out curve records | "
        f"curve_count={len(curve_record_list)}",
        flush=True,
    )

    # Evaluate Candidates On Their Direction-Valid Held-Out Curves
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])
    per_condition_metrics_csv_path = output_directory / "per_condition_metrics.csv"
    candidate_metric_accumulator: dict[str, dict[str, object]] = {}
    direction_metric_accumulator: dict[str, dict[str, dict[str, object]]] = {}
    temperature_metric_accumulator: dict[str, dict[str, dict[str, object]]] = {}
    target_metric_dictionary: dict[str, dict[str, float]] = {}
    candidate_metadata_list: list[reference_family_vs_feedforward_support.Track2Candidate] = []
    sample_preview_list: list[dict[str, object]] = []

    def update_metric_accumulator(metric_accumulator: dict[str, object], metric_dictionary: dict[str, float]) -> None:
        metric_accumulator["count"] = int(metric_accumulator.get("count", 0)) + 1
        for metric_name, metric_value in metric_dictionary.items():
            if metric_name == "mean_percentage_error_pct":
                metric_accumulator.setdefault("percentage_error_list", []).append(float(metric_value))
            metric_accumulator[metric_name] = float(metric_accumulator.get(metric_name, 0.0)) + float(metric_value)

    def summarize_metric_accumulator(metric_accumulator: dict[str, object]) -> dict[str, float]:
        metric_count = int(metric_accumulator["count"])
        percentage_error_list = metric_accumulator["percentage_error_list"]
        assert isinstance(percentage_error_list, list)
        return {
            "mse": float(metric_accumulator["mse"]) / metric_count,
            "mae": float(metric_accumulator["mae"]) / metric_count,
            "rmse": float(metric_accumulator["rmse"]) / metric_count,
            "mean_percentage_error_pct": float(metric_accumulator["mean_percentage_error_pct"]) / metric_count,
            "p95_mean_percentage_error_pct": float(np.percentile(percentage_error_list, 95.0)),
        }

    def summarize_nested_metric_accumulator(
        nested_metric_accumulator: dict[str, dict[str, dict[str, object]]],
    ) -> dict[str, dict[str, dict[str, float]]]:
        return {
            group_key: {
                candidate_id: summarize_metric_accumulator(metric_accumulator)
                for candidate_id, metric_accumulator in candidate_metric_dictionary.items()
            }
            for group_key, candidate_metric_dictionary in nested_metric_accumulator.items()
        }

    if baseline_summary is not None:
        baseline_csv_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
            baseline_summary["per_condition_metrics_csv_path"]
        )
        shutil.copyfile(baseline_csv_path, per_condition_metrics_csv_path)
        csv_file_mode = "a"
    else:
        csv_file_mode = "w"

    with per_condition_metrics_csv_path.open(csv_file_mode, encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        if baseline_summary is None:
            csv_writer.writerow(
                [
                    "source_file_path",
                    "direction_label",
                    "speed_rpm",
                    "torque_nm",
                    "oil_temperature_deg",
                    "candidate_id",
                    "candidate_family",
                    "candidate_kind",
                    "candidate_source_label",
                    "candidate_surface",
                    "curve_mae_deg",
                    "curve_rmse_deg",
                    "mean_percentage_error_pct",
                ]
        )

        for candidate_index, candidate_configuration in enumerate(candidate_configuration_list, start=1):
            print(
                "[INFO] Loading Track 2 candidate | "
                f"{candidate_index}/{len(candidate_configuration_list)} | "
                f"{candidate_configuration['candidate_id']}",
                flush=True,
            )
            candidate = reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)
            candidate_metadata_list.append(
                reference_family_vs_feedforward_support.Track2Candidate(
                    candidate_id=candidate.candidate_id,
                    candidate_family=candidate.candidate_family,
                    candidate_kind=candidate.candidate_kind,
                    candidate_source_label=candidate.candidate_source_label,
                    candidate_surface=candidate.candidate_surface,
                    allowed_direction_list=list(candidate.allowed_direction_list),
                    source_path=candidate.source_path,
                    selected_harmonic_list=list(candidate.selected_harmonic_list),
                    model_entry_list=None,
                    model_dictionary=None,
                    registry_entry=candidate.registry_entry,
                    training_config=None,
                    model_object=None,
                )
            )
            print(
                "[INFO] Evaluating Track 2 candidate | "
                f"{candidate_index}/{len(candidate_configuration_list)} | {candidate.candidate_id}",
                flush=True,
            )
            candidate_entry_list, candidate_target_metric_dictionary = (
                reference_family_vs_feedforward_support.evaluate_track2_candidate(
                    candidate,
                    curve_record_list,
                    percentage_error_denominator,
                    include_curve_payload=False,
                )
            )
            if candidate_target_metric_dictionary is not None:
                target_metric_dictionary[candidate.candidate_id] = candidate_target_metric_dictionary

            for candidate_entry in candidate_entry_list:
                metric_dictionary = candidate_entry["metrics"]
                candidate_id = str(candidate_entry["candidate_id"])
                direction_label = str(candidate_entry["direction_label"])
                temperature_label = str(candidate_entry["oil_temperature_deg"])

                update_metric_accumulator(
                    candidate_metric_accumulator.setdefault(candidate_id, {}),
                    metric_dictionary,
                )
                direction_metric_accumulator.setdefault(direction_label, {})
                update_metric_accumulator(
                    direction_metric_accumulator[direction_label].setdefault(candidate_id, {}),
                    metric_dictionary,
                )
                temperature_metric_accumulator.setdefault(temperature_label, {})
                update_metric_accumulator(
                    temperature_metric_accumulator[temperature_label].setdefault(candidate_id, {}),
                    metric_dictionary,
                )

                csv_writer.writerow(
                    [
                        candidate_entry["source_file_path"],
                        direction_label,
                        candidate_entry["speed_rpm"],
                        candidate_entry["torque_nm"],
                        candidate_entry["oil_temperature_deg"],
                        candidate_id,
                        candidate_entry["candidate_family"],
                        candidate_entry["candidate_kind"],
                        candidate_entry["candidate_source_label"],
                        candidate_entry["candidate_surface"],
                        metric_dictionary["mae"],
                        metric_dictionary["rmse"],
                        metric_dictionary["mean_percentage_error_pct"],
                    ]
                )

                if len(sample_preview_list) < 5:
                    sample_preview_list.append(
                        {
                            "source_file_path": candidate_entry["source_file_path"],
                            "direction_label": direction_label,
                            "candidate_id": candidate_id,
                            "speed_rpm": candidate_entry["speed_rpm"],
                            "torque_nm": candidate_entry["torque_nm"],
                            "oil_temperature_deg": candidate_entry["oil_temperature_deg"],
                            "mean_percentage_error_pct": metric_dictionary["mean_percentage_error_pct"],
                        }
                    )

            csv_file.flush()
            del candidate_entry_list
            del candidate
            gc.collect()

    # Build Aggregate Summaries And Artifacts
    candidate_metric_summary = {
        candidate_id: summarize_metric_accumulator(metric_accumulator)
        for candidate_id, metric_accumulator in candidate_metric_accumulator.items()
    }
    direction_metric_summary = summarize_nested_metric_accumulator(direction_metric_accumulator)
    temperature_metric_summary = summarize_nested_metric_accumulator(temperature_metric_accumulator)
    per_candidate_entry_list: list[dict[str, object]] = []
    preview_plot_path_list = reference_family_vs_feedforward_support.maybe_generate_track2_preview_plots(
        output_directory,
        per_candidate_entry_list,
        int(training_config["comparison"]["preview_curve_count"]),
    )
    report_plot_root = reference_family_vs_feedforward_support.resolve_track2_report_plot_root(training_config)
    report_plot_path_list = reference_family_vs_feedforward_support.maybe_generate_track2_grouped_report_plots(
        report_plot_root,
        per_candidate_entry_list,
        int(training_config["comparison"]["preview_curve_count"]),
    )

    # Save Summary And Report
    comparison_summary = reference_family_vs_feedforward_support.build_track2_directional_comparison_summary(
        resolved_config_path,
        output_directory,
        training_config,
        curve_record_list,
        candidate_metadata_list,
        target_metric_dictionary,
        per_candidate_entry_list,
        preview_plot_path_list,
        report_plot_root,
        report_plot_path_list,
        per_condition_metrics_csv_path,
        dataset_root,
        candidate_metric_summary_override=candidate_metric_summary,
        direction_metric_summary_override=direction_metric_summary,
        temperature_metric_summary_override=temperature_metric_summary,
        sample_preview_list_override=sample_preview_list,
    )
    if baseline_summary is not None:
        comparison_summary = copy.deepcopy(baseline_summary)
        new_candidate_summary = reference_family_vs_feedforward_support.build_track2_directional_comparison_summary(
            resolved_config_path,
            output_directory,
            training_config,
            curve_record_list,
            candidate_metadata_list,
            target_metric_dictionary,
            per_candidate_entry_list,
            preview_plot_path_list,
            report_plot_root,
            report_plot_path_list,
            per_condition_metrics_csv_path,
            dataset_root,
            candidate_metric_summary_override=candidate_metric_summary,
            direction_metric_summary_override=direction_metric_summary,
            temperature_metric_summary_override=temperature_metric_summary,
            sample_preview_list_override=sample_preview_list,
        )
        comparison_summary["config_path"] = shared_training_infrastructure.format_project_relative_path(
            resolved_config_path
        )
        comparison_summary["output_directory"] = shared_training_infrastructure.format_project_relative_path(
            output_directory
        )
        comparison_summary["comparison_scope"]["candidate_count"] = (
            int(comparison_summary["comparison_scope"]["candidate_count"])
            + len(new_candidate_summary["candidate_list"])
        )
        comparison_summary["candidate_list"].extend(new_candidate_summary["candidate_list"])
        comparison_summary["candidate_target_metric_summary"].update(
            new_candidate_summary["candidate_target_metric_summary"]
        )
        comparison_summary["candidate_metric_summary"].update(new_candidate_summary["candidate_metric_summary"])
        for direction_label, direction_entry in new_candidate_summary["direction_breakdown"].items():
            comparison_summary["direction_breakdown"].setdefault(direction_label, {}).update(direction_entry)
        for temperature_label, temperature_entry in new_candidate_summary["temperature_breakdown"].items():
            comparison_summary["temperature_breakdown"].setdefault(temperature_label, {}).update(temperature_entry)
        comparison_summary["preview_plot_path_list"] = preview_plot_path_list
        comparison_summary["report_plot_root"] = new_candidate_summary["report_plot_root"]
        comparison_summary["report_plot_path_list"] = report_plot_path_list
        comparison_summary["report_plot_count"] = int(len(report_plot_path_list))
        comparison_summary["per_condition_metrics_csv_path"] = (
            shared_training_infrastructure.format_project_relative_path(per_condition_metrics_csv_path)
        )
        comparison_summary["sample_preview_list"] = (
            list(comparison_summary.get("sample_preview_list", [])[:5])
            + list(new_candidate_summary.get("sample_preview_list", [])[:5])
        )[:5]
    validation_summary_path = output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME
    shared_training_infrastructure.save_yaml_snapshot(comparison_summary, validation_summary_path)

    validation_report_path = reference_family_vs_feedforward_support.build_comparison_report_path(training_config)
    validation_report_path.parent.mkdir(parents=True, exist_ok=True)
    validation_report_path.write_text(
        reference_family_vs_feedforward_support.build_track2_directional_comparison_report_markdown(comparison_summary),
        encoding="utf-8",
    )
    if str(training_config["comparison"].get("comparison_mode", "")).strip() == "full_directional_candidate_matrix":
        canonical_report_path = reference_family_vs_feedforward_support.build_canonical_track2_report_path(
            training_config
        )
        canonical_report_path.parent.mkdir(parents=True, exist_ok=True)
        canonical_report_path.write_text(
            reference_family_vs_feedforward_support.build_track2_directional_comparison_report_markdown(
                comparison_summary
            ),
            encoding="utf-8",
        )
    else:
        canonical_report_path = None

    print(
        "[DONE] Reference family comparison summary written | "
        f"{shared_training_infrastructure.format_project_relative_path(validation_summary_path)}"
    )
    print(
        "[DONE] Reference family comparison report written | "
        f"{shared_training_infrastructure.format_project_relative_path(validation_report_path)}"
    )
    if canonical_report_path is not None:
        print(
            "[DONE] Canonical Track 2 report written | "
            f"{shared_training_infrastructure.format_project_relative_path(canonical_report_path)}"
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
