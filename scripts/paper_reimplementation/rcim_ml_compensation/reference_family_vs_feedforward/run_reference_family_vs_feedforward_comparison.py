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

    """Run the first Track 2 comparison between one reference bank and feedforward."""

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

    # Load Canonical Baselines
    reference_inventory = reference_family_vs_feedforward_support.load_reference_inventory(
        training_config["paths"]["reference_inventory_path"]
    )
    selected_harmonic_list = reference_family_vs_feedforward_support.resolve_selected_harmonic_list(reference_inventory)
    reference_model_entry_list = reference_family_vs_feedforward_support.load_reference_model_entries(reference_inventory)
    reference_model_dictionary = reference_family_vs_feedforward_support.load_reference_model_dictionary(
        reference_model_entry_list
    )
    feedforward_best_entry = reference_family_vs_feedforward_support.resolve_feedforward_best_entry(
        training_config["paths"]["feedforward_leaderboard_path"]
    )
    feedforward_regression_module, _ = reference_family_vs_feedforward_support.load_feedforward_regression_module(
        feedforward_best_entry
    )

    # Build Held-Out Curve Records
    curve_record_list, _, _, _ = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )

    # Predict The Full Reference Bank Once Across The Held-Out Split
    predicted_target_dictionary = reference_family_vs_feedforward_support.predict_reference_bank_target_dictionary(
        curve_record_list,
        reference_model_entry_list,
        reference_model_dictionary,
    )
    reference_target_metric_dictionary = reference_family_vs_feedforward_support.build_reference_target_metric_dictionary(
        curve_record_list,
        predicted_target_dictionary,
        selected_harmonic_list,
    )

    # Evaluate All Curves On The Shared Offline Surface
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])
    lgbm_metric_list: list[dict[str, float]] = []
    feedforward_metric_list: list[dict[str, float]] = []
    oracle_metric_list: list[dict[str, float]] = []
    per_sample_entry_list: list[dict[str, object]] = []

    for sample_index, curve_record in enumerate(curve_record_list):
        lgbm_coefficient_dictionary, _ = reference_family_vs_feedforward_support.build_reference_coefficient_dictionary(
            predicted_target_dictionary,
            sample_index,
            selected_harmonic_list,
        )
        lgbm_curve_deg = harmonic_wise_support.reconstruct_curve_from_coefficients(
            curve_record.angular_position_deg,
            selected_harmonic_list,
            lgbm_coefficient_dictionary,
        )
        feedforward_curve_deg = reference_family_vs_feedforward_support.predict_feedforward_curve(
            feedforward_regression_module,
            curve_record,
        )
        oracle_curve_deg = harmonic_wise_support.reconstruct_curve_from_coefficients(
            curve_record.angular_position_deg,
            selected_harmonic_list,
            curve_record.coefficient_dictionary,
        )

        lgbm_metric_dictionary = harmonic_wise_support.compute_curve_metric_dictionary(
            curve_record.transmission_error_deg,
            lgbm_curve_deg,
            percentage_error_denominator,
        )
        feedforward_metric_dictionary = harmonic_wise_support.compute_curve_metric_dictionary(
            curve_record.transmission_error_deg,
            feedforward_curve_deg,
            percentage_error_denominator,
        )
        oracle_metric_dictionary = harmonic_wise_support.compute_curve_metric_dictionary(
            curve_record.transmission_error_deg,
            oracle_curve_deg,
            percentage_error_denominator,
        )

        lgbm_metric_list.append(lgbm_metric_dictionary)
        feedforward_metric_list.append(feedforward_metric_dictionary)
        oracle_metric_list.append(oracle_metric_dictionary)
        per_sample_entry_list.append(
            {
                "source_file_path": shared_training_infrastructure.format_project_relative_path(curve_record.source_file_path),
                "direction_label": curve_record.direction_label,
                "speed_rpm": float(curve_record.speed_rpm),
                "torque_nm": float(curve_record.torque_nm),
                "oil_temperature_deg": float(curve_record.oil_temperature_deg),
                "angular_position_deg": curve_record.angular_position_deg.astype(float).tolist(),
                "truth_curve_deg": curve_record.transmission_error_deg.astype(float).tolist(),
                "lgbm19_curve_deg": lgbm_curve_deg.astype(float).tolist(),
                "feedforward_curve_deg": feedforward_curve_deg.astype(float).tolist(),
                "lgbm19_reference_bank_metrics": lgbm_metric_dictionary,
                "feedforward_best_metrics": feedforward_metric_dictionary,
                "oracle_harmonic_truncation_metrics": oracle_metric_dictionary,
            }
        )

    # Build Aggregate Summaries And Artifacts
    aggregate_metric_dictionary = {
        "lgbm19_reference_bank": reference_family_vs_feedforward_support.summarize_metric_dictionary(lgbm_metric_list),
        "feedforward_best": reference_family_vs_feedforward_support.summarize_metric_dictionary(feedforward_metric_list),
        "oracle_harmonic_truncation": reference_family_vs_feedforward_support.summarize_metric_dictionary(oracle_metric_list),
    }
    direction_metric_summary = reference_family_vs_feedforward_support.build_group_metric_summary(
        per_sample_entry_list,
        "direction_label",
    )
    temperature_metric_summary = reference_family_vs_feedforward_support.build_group_metric_summary(
        per_sample_entry_list,
        "oil_temperature_deg",
    )
    per_condition_metrics_csv_path = reference_family_vs_feedforward_support.save_per_condition_metrics_csv(
        output_directory,
        per_sample_entry_list,
    )
    preview_plot_path_list = reference_family_vs_feedforward_support.maybe_generate_preview_plots(
        output_directory,
        per_sample_entry_list,
        int(training_config["comparison"]["preview_curve_count"]),
    )

    # Save Summary And Report
    comparison_summary = reference_family_vs_feedforward_support.build_comparison_summary(
        resolved_config_path,
        output_directory,
        training_config,
        reference_inventory,
        feedforward_best_entry,
        curve_record_list,
        reference_target_metric_dictionary,
        aggregate_metric_dictionary,
        per_sample_entry_list,
        direction_metric_summary,
        temperature_metric_summary,
        preview_plot_path_list,
        per_condition_metrics_csv_path,
        selected_harmonic_list,
    )
    validation_summary_path = output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME
    shared_training_infrastructure.save_yaml_snapshot(comparison_summary, validation_summary_path)

    validation_report_path = reference_family_vs_feedforward_support.build_comparison_report_path(training_config)
    validation_report_path.parent.mkdir(parents=True, exist_ok=True)
    validation_report_path.write_text(
        reference_family_vs_feedforward_support.build_reference_family_vs_feedforward_report_markdown(
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
    return argument_parser.parse_args()


def main() -> None:

    """Run the command-line comparison entry point."""

    command_line_arguments = parse_command_line_arguments()
    run_reference_family_vs_feedforward_comparison(
        command_line_arguments.config_path,
        command_line_arguments.output_suffix,
    )


if __name__ == "__main__":

    main()
