"""Build TE Curve Verification Pipeline mean-centered collage diagnostics."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import numpy as np
import yaml

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)
from scripts.reports.analysis import build_track2_best_model_collage_report
from scripts.tooling import repository_path_support
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = build_track2_best_model_collage_report.DEFAULT_CONFIG_PATH
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_mean_centered_collage_report"
DEFAULT_REPORT_TOPIC_ROOT = PROJECT_PATH / "doc" / "reports" / "analysis" / "track2" / "mean_centered_collage_report"
DEFAULT_FAMILY_REGISTRY_ROOT = build_track2_best_model_collage_report.DEFAULT_FAMILY_REGISTRY_ROOT
DEFAULT_PERIODIC_MLP_HARMONIC_CAMPAIGN_LEADERBOARD_PATH = (
    build_track2_best_model_collage_report.DEFAULT_PERIODIC_MLP_HARMONIC_CAMPAIGN_LEADERBOARD_PATH
)
DEFAULT_SOURCE_COLLAGE_SUMMARY_PATH = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2_best_model_collage_report"
    / "2026-05-28-13-37-39__track2_best_model_collage_report"
    / "track2_best_model_collage_summary.yaml"
)

SUMMARY_FILENAME = "track2_mean_centered_collage_summary.yaml"
CANDIDATE_METRICS_FILENAME = "track2_mean_centered_candidate_metrics.csv"
PER_CURVE_METRICS_FILENAME = "track2_mean_centered_per_curve_metrics.csv"
REPORT_FILENAME = "track2_mean_centered_collage_report.md"


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Generate a TE Curve Verification Pipeline diagnostic report that subtracts the measured "
            "and predicted per-curve means before recomputing curve MAE/RMSE."
        )
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="TE Curve Verification Pipeline comparison config used for candidate metadata and dataset loading.",
    )
    argument_parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root for generated mean-centered artifacts and summaries.",
    )
    argument_parser.add_argument(
        "--report-topic-root",
        type=Path,
        default=DEFAULT_REPORT_TOPIC_ROOT,
        help="Root for the dated Markdown report bundle.",
    )
    argument_parser.add_argument(
        "--report-date",
        type=str,
        default=None,
        help="Optional YYYY-MM-DD report bundle date to refresh.",
    )
    argument_parser.add_argument(
        "--family-registry-root",
        type=Path,
        default=DEFAULT_FAMILY_REGISTRY_ROOT,
        help="Root containing current family latest_family_best.yaml registries.",
    )
    argument_parser.add_argument(
        "--periodic-mlp-harmonic-campaign-leaderboard-path",
        type=Path,
        default=DEFAULT_PERIODIC_MLP_HARMONIC_CAMPAIGN_LEADERBOARD_PATH,
        help="Completed campaign leaderboard used to add explicit-harmonic periodic MLP candidates.",
    )
    argument_parser.add_argument(
        "--source-collage-summary-path",
        type=Path,
        default=DEFAULT_SOURCE_COLLAGE_SUMMARY_PATH,
        help="Existing best-model collage summary that defines candidate order and selected curves.",
    )
    argument_parser.add_argument(
        "--curves-per-collage",
        type=int,
        default=4,
        help="Number of deterministic representative curves to draw per candidate collage.",
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def resolve_timestamped_output_paths(
    output_root: Path,
    report_topic_root: Path,
    report_date: str | None,
) -> tuple[str, Path, Path]:

    """Resolve timestamped output and report directories."""

    current_timestamp = datetime.now().astimezone()
    run_instance_id = (
        f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}"
        "__track2_mean_centered_collage_report"
    )
    if report_date is None:
        report_date = current_timestamp.strftime("%Y-%m-%d")
    else:
        datetime.strptime(report_date, "%Y-%m-%d")

    output_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(output_root)
        / run_instance_id
    )
    report_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(report_topic_root)
        / f"[{report_date}]"
    )
    output_directory.mkdir(parents=True, exist_ok=True)
    report_directory.mkdir(parents=True, exist_ok=True)
    return run_instance_id, output_directory, report_directory


def compute_curve_mean_centering_metrics(entry_dictionary: dict[str, Any]) -> dict[str, float]:

    """Compute raw and mean-centered metrics for one predicted curve."""

    truth_curve_deg = np.asarray(entry_dictionary["truth_curve_deg"], dtype=np.float64)
    predicted_curve_deg = np.asarray(entry_dictionary["predicted_curve_deg"], dtype=np.float64)
    raw_residual_deg = predicted_curve_deg - truth_curve_deg

    truth_mean_deg = float(np.mean(truth_curve_deg))
    predicted_mean_deg = float(np.mean(predicted_curve_deg))
    centered_truth_curve_deg = truth_curve_deg - truth_mean_deg
    centered_predicted_curve_deg = predicted_curve_deg - predicted_mean_deg
    centered_residual_deg = centered_predicted_curve_deg - centered_truth_curve_deg

    raw_mae_deg = float(np.mean(np.abs(raw_residual_deg)))
    raw_rmse_deg = float(np.sqrt(np.mean(raw_residual_deg ** 2)))
    centered_mae_deg = float(np.mean(np.abs(centered_residual_deg)))
    centered_rmse_deg = float(np.sqrt(np.mean(centered_residual_deg ** 2)))
    offset_error_deg = predicted_mean_deg - truth_mean_deg

    return {
        "truth_mean_deg": truth_mean_deg,
        "predicted_mean_deg": predicted_mean_deg,
        "offset_error_deg": float(offset_error_deg),
        "absolute_offset_error_deg": float(abs(offset_error_deg)),
        "raw_mae_deg": raw_mae_deg,
        "raw_rmse_deg": raw_rmse_deg,
        "mean_centered_mae_deg": centered_mae_deg,
        "mean_centered_rmse_deg": centered_rmse_deg,
        "mae_improvement_deg": float(raw_mae_deg - centered_mae_deg),
        "rmse_improvement_deg": float(raw_rmse_deg - centered_rmse_deg),
        "mae_improvement_pct": compute_improvement_pct(raw_mae_deg, centered_mae_deg),
        "rmse_improvement_pct": compute_improvement_pct(raw_rmse_deg, centered_rmse_deg),
    }


def compute_improvement_pct(raw_metric_value: float, adjusted_metric_value: float) -> float:

    """Compute percentage improvement from one raw metric to one adjusted metric."""

    if raw_metric_value <= 0.0:
        return 0.0
    return float(100.0 * (raw_metric_value - adjusted_metric_value) / raw_metric_value)


def append_mean_centering_metrics(entry_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Return one entry enriched with mean-centering metrics."""

    enriched_entry_dictionary = dict(entry_dictionary)
    enriched_entry_dictionary["mean_centering_metrics"] = compute_curve_mean_centering_metrics(
        entry_dictionary
    )
    return enriched_entry_dictionary


def summarize_mean_centering_metrics(entry_list: list[dict[str, Any]]) -> dict[str, float]:

    """Summarize mean-centering metrics across one candidate/surface."""

    assert entry_list, "Cannot summarize an empty mean-centering entry list."
    metric_key_list = [
        "truth_mean_deg",
        "predicted_mean_deg",
        "offset_error_deg",
        "absolute_offset_error_deg",
        "raw_mae_deg",
        "raw_rmse_deg",
        "mean_centered_mae_deg",
        "mean_centered_rmse_deg",
        "mae_improvement_deg",
        "rmse_improvement_deg",
        "mae_improvement_pct",
        "rmse_improvement_pct",
    ]
    metric_dictionary_list = [
        entry_dictionary["mean_centering_metrics"]
        for entry_dictionary in entry_list
    ]
    summary_dictionary = {
        metric_key: float(np.mean([metric_dictionary[metric_key] for metric_dictionary in metric_dictionary_list]))
        for metric_key in metric_key_list
    }
    summary_dictionary["curve_count"] = int(len(entry_list))
    return summary_dictionary


def save_mean_centered_candidate_collage(
    collage_path: Path,
    candidate_id: str,
    selected_entry_list: list[dict[str, Any]],
) -> None:

    """Save one four-curve mean-centered collage for a candidate."""

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    collage_path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis_array = plt.subplots(2, 2, figsize=(12.0, 7.0), sharex=False, sharey=False)
    flattened_axis_list = list(axis_array.reshape(-1))

    for axis, per_candidate_entry in zip(flattened_axis_list, selected_entry_list):
        angular_position_deg = np.asarray(per_candidate_entry["angular_position_deg"], dtype=np.float64)
        truth_curve_deg = np.asarray(per_candidate_entry["truth_curve_deg"], dtype=np.float64)
        predicted_curve_deg = np.asarray(per_candidate_entry["predicted_curve_deg"], dtype=np.float64)
        truth_centered_deg = truth_curve_deg - np.mean(truth_curve_deg)
        predicted_centered_deg = predicted_curve_deg - np.mean(predicted_curve_deg)
        metric_dictionary = per_candidate_entry["mean_centering_metrics"]

        axis.plot(angular_position_deg, truth_centered_deg, label="Measured TE centered", linewidth=1.2, color="#4a4a4a")
        axis.plot(angular_position_deg, predicted_centered_deg, label=f"{candidate_id} centered", linewidth=1.2, color="#1f77b4")
        axis.set_title(
            (
                f"{per_candidate_entry['direction_label']} | "
                f"{float(per_candidate_entry['speed_rpm']):.0f} rpm | "
                f"{float(per_candidate_entry['torque_nm']):.0f} Nm | "
                f"{float(per_candidate_entry['oil_temperature_deg']):.0f} C\n"
                f"MAE {metric_dictionary['raw_mae_deg']:.4f} -> "
                f"{metric_dictionary['mean_centered_mae_deg']:.4f} deg"
            ),
            fontsize=8,
        )
        axis.set_xlabel("Angular Position [deg]", fontsize=8)
        axis.set_ylabel("Mean-centered TE [deg]", fontsize=8)
        axis.grid(True, alpha=0.28)
        axis.tick_params(labelsize=8)

    for empty_axis in flattened_axis_list[len(selected_entry_list):]:
        empty_axis.axis("off")

    flattened_axis_list[0].legend(loc="best", fontsize=8)
    figure.suptitle(f"{candidate_id} | mean-centered TE", fontsize=13)
    figure.tight_layout(rect=[0.0, 0.0, 1.0, 0.94])
    figure.savefig(collage_path, dpi=180)
    plt.close(figure)


def save_per_curve_metrics_csv(csv_path: Path, entry_list: list[dict[str, Any]]) -> None:

    """Save raw and mean-centered metrics for every evaluated curve."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "candidate_id",
                "candidate_family",
                "candidate_source_label",
                "candidate_surface",
                "source_file_path",
                "direction_label",
                "speed_rpm",
                "torque_nm",
                "oil_temperature_deg",
                "truth_mean_deg",
                "predicted_mean_deg",
                "offset_error_deg",
                "absolute_offset_error_deg",
                "raw_mae_deg",
                "raw_rmse_deg",
                "mean_centered_mae_deg",
                "mean_centered_rmse_deg",
                "mae_improvement_deg",
                "rmse_improvement_deg",
                "mae_improvement_pct",
                "rmse_improvement_pct",
            ]
        )
        for entry_dictionary in entry_list:
            metric_dictionary = entry_dictionary["mean_centering_metrics"]
            writer.writerow(
                [
                    entry_dictionary["candidate_id"],
                    entry_dictionary["candidate_family"],
                    entry_dictionary["candidate_source_label"],
                    entry_dictionary["candidate_surface"],
                    entry_dictionary["source_file_path"],
                    entry_dictionary["direction_label"],
                    f"{float(entry_dictionary['speed_rpm']):.9f}",
                    f"{float(entry_dictionary['torque_nm']):.9f}",
                    f"{float(entry_dictionary['oil_temperature_deg']):.9f}",
                    f"{metric_dictionary['truth_mean_deg']:.12f}",
                    f"{metric_dictionary['predicted_mean_deg']:.12f}",
                    f"{metric_dictionary['offset_error_deg']:.12f}",
                    f"{metric_dictionary['absolute_offset_error_deg']:.12f}",
                    f"{metric_dictionary['raw_mae_deg']:.12f}",
                    f"{metric_dictionary['raw_rmse_deg']:.12f}",
                    f"{metric_dictionary['mean_centered_mae_deg']:.12f}",
                    f"{metric_dictionary['mean_centered_rmse_deg']:.12f}",
                    f"{metric_dictionary['mae_improvement_deg']:.12f}",
                    f"{metric_dictionary['rmse_improvement_deg']:.12f}",
                    f"{metric_dictionary['mae_improvement_pct']:.9f}",
                    f"{metric_dictionary['rmse_improvement_pct']:.9f}",
                ]
            )


def save_candidate_metrics_csv(csv_path: Path, candidate_summary_list: list[dict[str, Any]]) -> None:

    """Save aggregate raw and mean-centered metrics for every candidate."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "group_id",
                "candidate_id",
                "candidate_family",
                "candidate_source_label",
                "candidate_surface",
                "direction_scope",
                "curve_count",
                "mean_absolute_offset_error_deg",
                "raw_mae_deg",
                "raw_rmse_deg",
                "mean_centered_mae_deg",
                "mean_centered_rmse_deg",
                "mae_improvement_deg",
                "rmse_improvement_deg",
                "mae_improvement_pct",
                "rmse_improvement_pct",
                "collage_path",
            ]
        )
        for candidate_summary in candidate_summary_list:
            metric_dictionary = candidate_summary["mean_centering_metrics"]
            writer.writerow(
                [
                    candidate_summary["group_id"],
                    candidate_summary["candidate_id"],
                    candidate_summary["candidate_family"],
                    candidate_summary["candidate_source_label"],
                    candidate_summary["candidate_surface"],
                    candidate_summary["direction_scope"],
                    metric_dictionary["curve_count"],
                    f"{metric_dictionary['absolute_offset_error_deg']:.12f}",
                    f"{metric_dictionary['raw_mae_deg']:.12f}",
                    f"{metric_dictionary['raw_rmse_deg']:.12f}",
                    f"{metric_dictionary['mean_centered_mae_deg']:.12f}",
                    f"{metric_dictionary['mean_centered_rmse_deg']:.12f}",
                    f"{metric_dictionary['mae_improvement_deg']:.12f}",
                    f"{metric_dictionary['rmse_improvement_deg']:.12f}",
                    f"{metric_dictionary['mae_improvement_pct']:.9f}",
                    f"{metric_dictionary['rmse_improvement_pct']:.9f}",
                    candidate_summary["collage_path"],
                ]
            )


def append_group_metric_table(
    report_line_list: list[str],
    group_summary_list: list[dict[str, Any]],
) -> None:

    """Append one mean-centered candidate metric table."""

    report_line_list.extend(
        [
            "| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for candidate_summary in group_summary_list:
        metric_dictionary = candidate_summary["mean_centering_metrics"]
        report_line_list.append(
            f"| `{candidate_summary['candidate_id']}` | "
            f"{candidate_summary['candidate_surface']} | "
            f"{metric_dictionary['raw_mae_deg']:.6f} | "
            f"{metric_dictionary['mean_centered_mae_deg']:.6f} | "
            f"{metric_dictionary['mae_improvement_pct']:.1f}% | "
            f"{metric_dictionary['absolute_offset_error_deg']:.6f} |"
        )


def append_top_improvement_table(
    report_line_list: list[str],
    candidate_summary_list: list[dict[str, Any]],
    row_count: int = 12,
) -> None:

    """Append top candidates by MAE improvement."""

    sorted_summary_list = sorted(
        candidate_summary_list,
        key=lambda candidate_summary: candidate_summary["mean_centering_metrics"]["mae_improvement_pct"],
        reverse=True,
    )
    report_line_list.extend(
        [
            "| Rank | Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |",
            "| ---: | --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for rank_index, candidate_summary in enumerate(sorted_summary_list[:row_count], start=1):
        metric_dictionary = candidate_summary["mean_centering_metrics"]
        report_line_list.append(
            f"| {rank_index} | `{candidate_summary['candidate_id']}` | "
            f"{candidate_summary['candidate_surface']} | "
            f"{metric_dictionary['raw_mae_deg']:.6f} | "
            f"{metric_dictionary['mean_centered_mae_deg']:.6f} | "
            f"{metric_dictionary['mae_improvement_pct']:.1f}% | "
            f"{metric_dictionary['absolute_offset_error_deg']:.6f} |"
        )


def build_report_markdown(
    report_path: Path,
    output_directory: Path,
    candidate_summary_list: list[dict[str, Any]],
    group_list: list[build_track2_best_model_collage_report.ReportCandidateGroup],
    candidate_metrics_csv_path: Path,
    per_curve_metrics_csv_path: Path,
    validation_summary_path: Path,
) -> str:

    """Build the Markdown report body."""

    report_line_list = [
        "# TE Curve Verification Pipeline Mean-Centered Collage Diagnostics Report",
        "",
        "## Overview",
        "",
        "This report tests whether the persistent vertical offset observed in",
        "the `TE Curve Verification Pipeline` best-model collage hides stronger waveform tracking.",
        "For each candidate and curve, the measured `TE` curve is centered by",
        "its own mean and the predicted curve is centered by its own mean before",
        "`MAE` and `RMSE` are recomputed.",
        "",
        "This is a diagnostic post-prediction view. It does not train models,",
        "change the dataset, or make mean-centering a deployable runtime",
        "correction.",
        "",
        "## Method",
        "",
        "- candidates and representative curves match the best-model collage",
        "  report structure;",
        "- aggregate metrics are computed on the same deterministic four-curve",
        "  selection used by the source collage report;",
        "- this keeps the diagnostic directly comparable with the visual offset",
        "  observed in the original collage PDF;",
        "- raw `MAE`/`RMSE` are compared against metrics after subtracting each",
        "  curve's own mean from truth and prediction separately.",
        "",
        "## Top Mean-Centering Improvements",
        "",
    ]
    append_top_improvement_table(report_line_list, candidate_summary_list)
    report_line_list.append("")

    candidate_summary_by_group = {
        group.group_id: [
            candidate_summary
            for candidate_summary in candidate_summary_list
            if candidate_summary["group_id"] == group.group_id
        ]
        for group in group_list
    }

    report_line_list.extend(["## Group Metrics", ""])
    for group in group_list:
        report_line_list.extend([f"### {group.group_title}", ""])
        append_group_metric_table(report_line_list, candidate_summary_by_group[group.group_id])
        report_line_list.append("")

    for group in group_list:
        group_summary_list = candidate_summary_by_group[group.group_id]
        for chunk_start_index in range(0, len(group_summary_list), 2):
            chunk_index = chunk_start_index // 2
            section_title = build_track2_best_model_collage_report.get_gallery_section_title(
                group.group_title,
                chunk_index,
            )
            report_line_list.extend([f"## Mean-Centered {section_title}", ""])
            for candidate_summary in group_summary_list[chunk_start_index : chunk_start_index + 2]:
                report_line_list.extend(
                    [
                        f"{candidate_summary['candidate_id']}:",
                        "",
                        (
                            f"![{candidate_summary['candidate_id']} mean-centered TE Curve Verification Pipeline collage]"
                            f"({candidate_summary['collage_markdown_path']})"
                        ),
                        "",
                    ]
                )

    report_line_list.extend(
        [
            "## Output Artifacts",
            "",
            f"- output directory: `{shared_training_infrastructure.format_project_relative_path(output_directory)}`;",
            f"- summary YAML: `{shared_training_infrastructure.format_project_relative_path(validation_summary_path)}`;",
            f"- candidate metrics CSV: `{shared_training_infrastructure.format_project_relative_path(candidate_metrics_csv_path)}`;",
            f"- per-curve metrics CSV: `{shared_training_infrastructure.format_project_relative_path(per_curve_metrics_csv_path)}`;",
            f"- report Markdown: `{shared_training_infrastructure.format_project_relative_path(report_path)}`;",
            "- styled PDF: generated from the Markdown report with "
            "`python -B scripts/reports/pdf/run_report_pipeline.py`.",
        ]
    )
    return "\n".join(report_line_list) + "\n"


def build_curve_key(entry_dictionary: dict[str, Any]) -> tuple[str, str]:

    """Build a stable key for one curve entry."""

    return (
        str(entry_dictionary["source_file_path"]),
        str(entry_dictionary["direction_label"]),
    )


def load_source_collage_summary(summary_path: Path) -> dict[str, Any]:

    """Load the source best-model collage summary."""

    resolved_summary_path = shared_training_infrastructure.resolve_runtime_project_relative_path(summary_path)
    assert resolved_summary_path.exists(), f"Source Collage Summary does not exist | {resolved_summary_path}"
    with resolved_summary_path.open("r", encoding="utf-8") as summary_file:
        summary_dictionary = yaml.safe_load(summary_file)
    assert isinstance(summary_dictionary, dict), f"Invalid source collage summary | {resolved_summary_path}"
    return summary_dictionary


def run_track2_mean_centered_collage_report(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the full TE Curve Verification Pipeline mean-centered collage report generation."""

    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(arguments)
    )
    assert int(arguments.curves_per_collage) == 4, "This report requires exactly four curves per collage."

    run_instance_id, output_directory, report_directory = resolve_timestamped_output_paths(
        arguments.output_root,
        arguments.report_topic_root,
        arguments.report_date,
    )
    report_path = report_directory / REPORT_FILENAME
    candidate_metrics_csv_path = output_directory / CANDIDATE_METRICS_FILENAME
    per_curve_metrics_csv_path = output_directory / PER_CURVE_METRICS_FILENAME
    validation_summary_path = output_directory / SUMMARY_FILENAME

    training_config = shared_training_infrastructure.load_training_config(arguments.config_path)
    source_collage_summary = load_source_collage_summary(arguments.source_collage_summary_path)
    selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
    curve_record_list, _, _, dataset_root = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])

    candidate_configuration_list = build_track2_best_model_collage_report.resolve_report_candidate_configuration_list(
        training_config,
        arguments.family_registry_root,
        arguments.periodic_mlp_harmonic_campaign_leaderboard_path,
        output_directory,
    )
    candidate_list = [
        reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)
        for candidate_configuration in candidate_configuration_list
    ]
    candidate_lookup = {
        candidate.candidate_id: candidate
        for candidate in candidate_list
    }

    curve_record_lookup = {
        (
            shared_training_infrastructure.format_project_relative_path(curve_record.source_file_path),
            str(curve_record.direction_label),
        ): curve_record
        for curve_record in curve_record_list
    }

    group_list = build_track2_best_model_collage_report.build_report_group_list()
    candidate_summary_list: list[dict[str, Any]] = []
    per_curve_entry_list: list[dict[str, Any]] = []
    source_candidate_summary_lookup = {
        str(candidate_summary["candidate_id"]): candidate_summary
        for candidate_summary in source_collage_summary["candidate_summary_list"]
    }

    for group in group_list:
        for candidate_id in group.candidate_id_list:
            candidate = candidate_lookup[candidate_id]
            source_candidate_summary = source_candidate_summary_lookup[candidate_id]
            selected_curve_record_list = [
                curve_record_lookup[build_curve_key(source_curve_entry)]
                for source_curve_entry in source_candidate_summary["selected_curve_list"]
            ]
            selected_payload_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
                candidate,
                selected_curve_record_list,
                percentage_error_denominator,
                include_curve_payload=True,
            )
            selected_payload_lookup = {
                build_curve_key(selected_payload_entry): append_mean_centering_metrics(selected_payload_entry)
                for selected_payload_entry in selected_payload_entry_list
            }
            selected_entry_list = [
                selected_payload_lookup[build_curve_key(source_curve_entry)]
                for source_curve_entry in source_candidate_summary["selected_curve_list"]
            ]
            per_curve_entry_list.extend(selected_entry_list)

            collage_path = (
                output_directory
                / "collages"
                / group.group_id
                / f"{build_track2_best_model_collage_report.sanitize_filename_fragment(candidate_id)}.png"
            )
            report_asset_path = (
                report_path.parent
                / "assets"
                / group.group_id
                / f"{build_track2_best_model_collage_report.sanitize_filename_fragment(candidate_id)}.png"
            )
            save_mean_centered_candidate_collage(collage_path, candidate_id, selected_entry_list)
            report_asset_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(collage_path, report_asset_path)

            candidate_summary_list.append(
                {
                    "group_id": group.group_id,
                    "candidate_id": candidate_id,
                    "candidate_family": candidate.candidate_family,
                    "candidate_kind": candidate.candidate_kind,
                    "candidate_source_label": candidate.candidate_source_label,
                    "candidate_surface": candidate.candidate_surface,
                    "direction_scope": group.selection_mode,
                    "allowed_direction_list": candidate.allowed_direction_list,
                    "source_path": shared_training_infrastructure.format_project_relative_path(candidate.source_path),
                    "mean_centering_metrics": summarize_mean_centering_metrics(selected_entry_list),
                    "collage_path": shared_training_infrastructure.format_project_relative_path(collage_path),
                    "collage_markdown_path": build_track2_best_model_collage_report.build_relative_markdown_path(
                        report_asset_path,
                        report_path.parent,
                    ),
                    "selected_curve_list": [
                        {
                            "source_file_path": entry["source_file_path"],
                            "direction_label": entry["direction_label"],
                            "speed_rpm": float(entry["speed_rpm"]),
                            "torque_nm": float(entry["torque_nm"]),
                            "oil_temperature_deg": float(entry["oil_temperature_deg"]),
                            "mean_centering_metrics": entry["mean_centering_metrics"],
                        }
                        for entry in selected_entry_list
                    ],
                }
            )

    save_per_curve_metrics_csv(per_curve_metrics_csv_path, per_curve_entry_list)
    save_candidate_metrics_csv(candidate_metrics_csv_path, candidate_summary_list)

    validation_summary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "report_path": shared_training_infrastructure.format_project_relative_path(report_path),
        "dataset": {
            "config_path": str(training_config["paths"]["dataset_config_path"]),
            "dataset_root": shared_training_infrastructure.format_project_relative_path(dataset_root),
            "curve_count": int(len(curve_record_list)),
            "selected_harmonic_list": selected_harmonic_list,
        },
        "candidate_count": int(len(candidate_summary_list)),
        "evaluated_curve_payload_count": int(len(per_curve_entry_list)),
        "candidate_summary_list": candidate_summary_list,
        "candidate_metrics_csv_path": shared_training_infrastructure.format_project_relative_path(candidate_metrics_csv_path),
        "per_curve_metrics_csv_path": shared_training_infrastructure.format_project_relative_path(per_curve_metrics_csv_path),
    }
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

    report_markdown = build_report_markdown(
        report_path,
        output_directory,
        candidate_summary_list,
        group_list,
        candidate_metrics_csv_path,
        per_curve_metrics_csv_path,
        validation_summary_path,
    )
    report_path.write_text(report_markdown, encoding="utf-8")
    return validation_summary


def main() -> None:

    """Run the command-line entry point."""

    validation_summary = run_track2_mean_centered_collage_report(parse_command_line_arguments())
    print(f"[DONE] TE Curve Verification Pipeline mean-centered collage report: {validation_summary['report_path']}")
    print(f"[DONE] Artifacts: {validation_summary['output_directory']}")


if __name__ == "__main__":
    main()
