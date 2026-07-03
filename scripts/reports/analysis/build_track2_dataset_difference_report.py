"""Build TE Curve Verification Pipeline dataset-difference visual reports."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.harmonic_wise_comparison import harmonic_wise_support
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)
from scripts.tooling import repository_path_support
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "full_track2_matrix_template.yaml"
)
DEFAULT_OUTPUT_ROOT = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2_dataset_difference_report"
)
DEFAULT_REPORT_TOPIC_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "dataset_difference_report"
)
REPORT_FILENAME = "track2_dataset_difference_report.md"
SUMMARY_FILENAME = "track2_dataset_difference_summary.yaml"
METRICS_FILENAME = "track2_dataset_difference_metrics.csv"


@dataclass(frozen=True)
class CandidatePair:

    """One simplified-trained versus polished-trained candidate pair."""

    pair_id: str
    simplified_candidate_id: str
    polished_candidate_id: str


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description="Build a TE Curve Verification Pipeline dataset-difference report."
    )
    argument_parser.add_argument("--config-path", type=Path, default=DEFAULT_CONFIG_PATH)
    argument_parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    argument_parser.add_argument("--report-topic-root", type=Path, default=DEFAULT_REPORT_TOPIC_ROOT)
    argument_parser.add_argument("--report-date", type=str, default=None)
    argument_parser.add_argument(
        "--dataset",
        choices=["polished_dataset", "simplified_dataset"],
        required=True,
        help="Evaluation dataset used for measured curves in this difference report.",
    )
    argument_parser.add_argument(
        "--surface-scope",
        choices=["forward", "backward", "global"],
        required=True,
        help="Surface report scope for the difference report.",
    )
    argument_parser.add_argument(
        "--candidate-pair",
        action="append",
        required=True,
        metavar="PAIR_ID:SIMPLIFIED_CANDIDATE:POLISHED_CANDIDATE",
        help="Candidate pair to compare. Repeat for multiple pairs.",
    )
    argument_parser.add_argument(
        "--curves-per-pair",
        type=int,
        default=4,
        help="Number of deterministic representative curves to plot per pair.",
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def parse_candidate_pair(pair_text: str) -> CandidatePair:

    """Parse one CLI candidate-pair specification."""

    part_list = [part.strip() for part in str(pair_text).split(":")]
    assert len(part_list) == 3 and all(part_list), (
        "Candidate pair must use PAIR_ID:SIMPLIFIED_CANDIDATE:POLISHED_CANDIDATE | "
        f"{pair_text}"
    )
    return CandidatePair(
        pair_id=part_list[0],
        simplified_candidate_id=part_list[1],
        polished_candidate_id=part_list[2],
    )


def resolve_timestamped_output_paths(
    output_root: Path,
    report_topic_root: Path,
    report_date: str | None,
    dataset_name: str,
    surface_scope: str,
) -> tuple[str, Path, Path]:

    """Resolve output paths for one dataset-difference report run."""

    current_timestamp = datetime.now().astimezone()
    run_instance_id = (
        f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}"
        f"__track2_dataset_difference_{dataset_name}_{surface_scope}"
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
        / dataset_name
        / surface_scope
    )
    output_directory.mkdir(parents=True, exist_ok=True)
    report_directory.mkdir(parents=True, exist_ok=True)
    return run_instance_id, output_directory, report_directory


def filter_curve_record_list_by_surface_scope(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    surface_scope: str,
) -> list[harmonic_wise_support.HarmonicCurveRecord]:

    """Filter curve records for one surface scope."""

    normalized_scope = str(surface_scope).strip().lower()
    if normalized_scope == "global":
        return curve_record_list
    filtered_curve_record_list = [
        curve_record
        for curve_record in curve_record_list
        if str(curve_record.direction_label).strip().lower() == normalized_scope
    ]
    assert filtered_curve_record_list, f"No curve records available for surface scope | {surface_scope}"
    return filtered_curve_record_list


def load_candidate_lookup(training_config: dict[str, Any]) -> dict[str, dict[str, Any]]:

    """Load configured candidate dictionaries by candidate id."""

    candidate_configuration_list = reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(
        training_config
    )
    return {
        str(candidate_configuration["candidate_id"]): candidate_configuration
        for candidate_configuration in candidate_configuration_list
    }


def select_representative_curve_record_list(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    curve_count: int,
) -> list[harmonic_wise_support.HarmonicCurveRecord]:

    """Select deterministic representative curves across the filtered scope."""

    assert curve_count > 0, "curves-per-pair must be positive"
    sorted_curve_record_list = sorted(
        curve_record_list,
        key=lambda curve_record: (
            str(curve_record.direction_label),
            float(curve_record.oil_temperature_deg),
            float(curve_record.torque_nm),
            float(curve_record.speed_rpm),
            str(curve_record.source_file_path),
        ),
    )
    if len(sorted_curve_record_list) <= curve_count:
        return sorted_curve_record_list
    selected_index_array = np.linspace(0, len(sorted_curve_record_list) - 1, curve_count, dtype=int)
    return [sorted_curve_record_list[int(index)] for index in selected_index_array]


def build_curve_key(entry_dictionary: dict[str, Any]) -> tuple[str, str]:

    """Build a stable key for one payload entry."""

    return (
        str(entry_dictionary["source_file_path"]),
        str(entry_dictionary["direction_label"]),
    )


def save_pair_difference_plot(
    plot_path: Path,
    pair: CandidatePair,
    simplified_entry_list: list[dict[str, Any]],
    polished_entry_lookup: dict[tuple[str, str], dict[str, Any]],
) -> list[dict[str, Any]]:

    """Save one multi-curve pair difference plot and return metric rows."""

    plot_path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis_array = plt.subplots(
        len(simplified_entry_list),
        2,
        figsize=(11.0, max(3.0, 2.7 * len(simplified_entry_list))),
        squeeze=False,
    )
    metric_row_list: list[dict[str, Any]] = []

    for row_index, simplified_entry in enumerate(simplified_entry_list):
        curve_key = build_curve_key(simplified_entry)
        polished_entry = polished_entry_lookup[curve_key]
        angular_position_deg = np.asarray(simplified_entry["angular_position_deg"], dtype=float)
        truth_curve_deg = np.asarray(simplified_entry["truth_curve_deg"], dtype=float)
        simplified_curve_deg = np.asarray(simplified_entry["predicted_curve_deg"], dtype=float)
        polished_curve_deg = np.asarray(polished_entry["predicted_curve_deg"], dtype=float)
        prediction_delta_deg = polished_curve_deg - simplified_curve_deg

        curve_axis = axis_array[row_index][0]
        delta_axis = axis_array[row_index][1]
        curve_axis.plot(angular_position_deg, truth_curve_deg, color="#111111", linewidth=1.5, label="measured")
        curve_axis.plot(angular_position_deg, simplified_curve_deg, color="#2563eb", linewidth=1.2, label="simplified")
        curve_axis.plot(angular_position_deg, polished_curve_deg, color="#dc2626", linewidth=1.2, label="polished")
        curve_axis.set_title(
            (
                f"{simplified_entry['direction_label']} | "
                f"{simplified_entry['speed_rpm']:.0f} rpm | "
                f"{simplified_entry['torque_nm']:.0f} Nm | "
                f"{simplified_entry['oil_temperature_deg']:.0f} C"
            ),
            fontsize=9,
        )
        curve_axis.set_xlabel("Angular position [deg]")
        curve_axis.set_ylabel("TE [deg]")
        curve_axis.grid(True, alpha=0.25)
        curve_axis.legend(loc="best", fontsize=8)

        delta_axis.plot(angular_position_deg, prediction_delta_deg, color="#7c3aed", linewidth=1.2)
        delta_axis.axhline(0.0, color="#555555", linewidth=0.8)
        delta_axis.set_title("polished - simplified prediction", fontsize=9)
        delta_axis.set_xlabel("Angular position [deg]")
        delta_axis.set_ylabel("Delta [deg]")
        delta_axis.grid(True, alpha=0.25)

        metric_row_list.append(
            {
                "pair_id": pair.pair_id,
                "source_file_path": simplified_entry["source_file_path"],
                "direction_label": simplified_entry["direction_label"],
                "speed_rpm": float(simplified_entry["speed_rpm"]),
                "torque_nm": float(simplified_entry["torque_nm"]),
                "oil_temperature_deg": float(simplified_entry["oil_temperature_deg"]),
                "simplified_mae": float(simplified_entry["metrics"]["mae"]),
                "polished_mae": float(polished_entry["metrics"]["mae"]),
                "delta_mean_abs_deg": float(np.mean(np.abs(prediction_delta_deg))),
            }
        )

    figure.suptitle(pair.pair_id, fontsize=12)
    figure.tight_layout(rect=(0.0, 0.0, 1.0, 0.98))
    figure.savefig(plot_path, dpi=170)
    plt.close(figure)
    return metric_row_list


def save_metrics_csv(metrics_csv_path: Path, metric_row_list: list[dict[str, Any]]) -> None:

    """Save dataset-difference metrics to CSV."""

    metrics_csv_path.parent.mkdir(parents=True, exist_ok=True)
    with metrics_csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "pair_id",
                "source_file_path",
                "direction_label",
                "speed_rpm",
                "torque_nm",
                "oil_temperature_deg",
                "simplified_mae",
                "polished_mae",
                "delta_mean_abs_deg",
            ],
        )
        writer.writeheader()
        writer.writerows(metric_row_list)


def build_report_markdown(
    report_path: Path,
    validation_summary: dict[str, Any],
) -> str:

    """Build the dataset-difference Markdown report."""

    report_line_list = [
        "# TE Curve Verification Pipeline Dataset Difference Report",
        "",
        "## Scope",
        "",
        f"- evaluation dataset: `{validation_summary['dataset']['dataset_name']}`;",
        f"- dataset root: `{validation_summary['dataset']['dataset_root']}`;",
        f"- surface scope: `{validation_summary['surface_scope']}`;",
        f"- curve count per pair: `{validation_summary['curves_per_pair']}`;",
        f"- metrics CSV: `{validation_summary['metrics_csv_path']}`;",
        "",
        "## Candidate Pairs",
        "",
        "| Pair | Simplified-trained candidate | Polished-trained candidate | Plot |",
        "| --- | --- | --- | --- |",
    ]
    for pair_summary in validation_summary["pair_summary_list"]:
        report_line_list.append(
            f"| `{pair_summary['pair_id']}` | "
            f"`{pair_summary['simplified_candidate_id']}` | "
            f"`{pair_summary['polished_candidate_id']}` | "
            f"[plot]({pair_summary['plot_markdown_path']}) |"
        )

    report_line_list.extend(["", "## Plots", ""])
    for pair_summary in validation_summary["pair_summary_list"]:
        report_line_list.extend(
            [
                f"### {pair_summary['pair_id']}",
                "",
                f"![{pair_summary['pair_id']}]({pair_summary['plot_markdown_path']})",
                "",
            ]
        )

    return "\n".join(report_line_list).rstrip() + "\n"


def build_relative_markdown_path(target_path: Path, markdown_directory: Path) -> str:

    """Build a Markdown-safe relative path from a report to an artifact."""

    return target_path.resolve().relative_to(markdown_directory.resolve()).as_posix()


def run_dataset_difference_report(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the dataset-difference report builder."""

    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(arguments)
    )
    candidate_pair_list = [parse_candidate_pair(pair_text) for pair_text in arguments.candidate_pair]
    run_instance_id, output_directory, report_directory = resolve_timestamped_output_paths(
        arguments.output_root,
        arguments.report_topic_root,
        arguments.report_date,
        arguments.dataset,
        arguments.surface_scope,
    )
    report_path = report_directory / REPORT_FILENAME
    metrics_csv_path = output_directory / METRICS_FILENAME
    validation_summary_path = output_directory / SUMMARY_FILENAME
    asset_directory = report_directory / "assets"
    asset_directory.mkdir(parents=True, exist_ok=True)

    training_config = shared_training_infrastructure.apply_dataset_override(
        reference_family_vs_feedforward_support.load_reference_family_comparison_config(arguments.config_path),
        arguments.dataset,
    )
    selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
    curve_record_list, _, _, dataset_root = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    curve_record_list = filter_curve_record_list_by_surface_scope(curve_record_list, arguments.surface_scope)
    representative_curve_record_list = select_representative_curve_record_list(
        curve_record_list,
        int(arguments.curves_per_pair),
    )
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])
    candidate_configuration_lookup = load_candidate_lookup(training_config)

    pair_summary_list: list[dict[str, Any]] = []
    metric_row_list: list[dict[str, Any]] = []
    for pair in tqdm(candidate_pair_list, desc="Dataset difference pairs", unit="pair"):
        assert pair.simplified_candidate_id in candidate_configuration_lookup, (
            f"Missing simplified candidate | {pair.simplified_candidate_id}"
        )
        assert pair.polished_candidate_id in candidate_configuration_lookup, (
            f"Missing polished candidate | {pair.polished_candidate_id}"
        )
        simplified_candidate = reference_family_vs_feedforward_support.load_track2_candidate(
            candidate_configuration_lookup[pair.simplified_candidate_id]
        )
        polished_candidate = reference_family_vs_feedforward_support.load_track2_candidate(
            candidate_configuration_lookup[pair.polished_candidate_id]
        )
        simplified_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
            simplified_candidate,
            representative_curve_record_list,
            percentage_error_denominator,
            include_curve_payload=True,
        )
        polished_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
            polished_candidate,
            representative_curve_record_list,
            percentage_error_denominator,
            include_curve_payload=True,
        )
        polished_entry_lookup = {
            build_curve_key(polished_entry): polished_entry
            for polished_entry in polished_entry_list
        }
        plot_path = output_directory / "plots" / f"{pair.pair_id}.png"
        pair_metric_row_list = save_pair_difference_plot(
            plot_path,
            pair,
            simplified_entry_list,
            polished_entry_lookup,
        )
        report_plot_path = asset_directory / f"{pair.pair_id}.png"
        report_plot_path.write_bytes(plot_path.read_bytes())
        metric_row_list.extend(pair_metric_row_list)
        pair_summary_list.append(
            {
                "pair_id": pair.pair_id,
                "simplified_candidate_id": pair.simplified_candidate_id,
                "polished_candidate_id": pair.polished_candidate_id,
                "plot_path": shared_training_infrastructure.format_project_relative_path(plot_path),
                "plot_markdown_path": build_relative_markdown_path(report_plot_path, report_path.parent),
            }
        )

    save_metrics_csv(metrics_csv_path, metric_row_list)
    validation_summary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "report_path": shared_training_infrastructure.format_project_relative_path(report_path),
        "surface_scope": str(arguments.surface_scope),
        "curves_per_pair": int(arguments.curves_per_pair),
        "dataset": {
            "dataset_name": str(arguments.dataset),
            "dataset_root": shared_training_infrastructure.format_project_relative_path(dataset_root),
            "selected_harmonic_list": selected_harmonic_list,
        },
        "pair_summary_list": pair_summary_list,
        "metrics_csv_path": shared_training_infrastructure.format_project_relative_path(metrics_csv_path),
    }
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)
    report_path.write_text(build_report_markdown(report_path, validation_summary), encoding="utf-8")
    return validation_summary


def main() -> None:

    """Run the command-line entry point."""

    validation_summary = run_dataset_difference_report(parse_command_line_arguments())
    print(f"[DONE] Dataset difference report: {validation_summary['report_path']}")
    print(f"[DONE] Artifacts: {validation_summary['output_directory']}")


if __name__ == "__main__":
    main()
