"""Build the Track 2 multi-model curve comparison report and plot artifacts."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import os
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
import numpy as np

# Import Project Utilities
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
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_multi_model_curve_comparison_report"
DEFAULT_REPORT_TOPIC_ROOT = PROJECT_PATH / "doc" / "reports" / "analysis" / "track2" / "multi_model_curve_comparison_report"
DEFAULT_FAMILY_REGISTRY_ROOT = PROJECT_PATH / "output" / "registries" / "families"
SUMMARY_FILENAME = "track2_multi_model_curve_comparison_summary.yaml"
METRICS_FILENAME = "track2_multi_model_curve_comparison_metrics.csv"
REPORT_FILENAME = "track2_multi_model_curve_comparison_report.md"
SCREENED_WAVE1_MODEL_COUNT = 3

WAVE1_BASE_FAMILY_LIST = [
    "feedforward",
    "harmonic_regression",
    "periodic_mlp",
    "residual_harmonic_mlp",
    "tree",
]
FORWARD_REFERENCE_CANDIDATE_ID_LIST = [
    "paper_original_best_Fw",
    "paper_retuned_best_Fw",
    "track1_best_Fw",
]
BACKWARD_REFERENCE_CANDIDATE_ID_LIST = [
    "paper_retuned_best_Bw",
    "track1_best_Bw",
]


@dataclass(frozen=True)
class ReportComparisonGroup:

    """One logical report group for a multi-model curve overlay."""

    group_id: str
    group_title: str
    candidate_id_list: list[str]
    selection_mode: str


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Generate the Track 2 multi-model curve comparison report with "
            "four-curve overlay collages for selected reference and Wave 1 "
            "model groups."
        )
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Track 2 comparison config used for reference candidate metadata and dataset loading.",
    )
    argument_parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root for generated comparison artifacts and machine-readable summaries.",
    )
    argument_parser.add_argument(
        "--report-topic-root",
        type=Path,
        default=DEFAULT_REPORT_TOPIC_ROOT,
        help="Root for the dated Markdown/PDF report bundle.",
    )
    argument_parser.add_argument(
        "--family-registry-root",
        type=Path,
        default=DEFAULT_FAMILY_REGISTRY_ROOT,
        help="Root containing current Wave 1 family latest_family_best.yaml registries.",
    )
    argument_parser.add_argument(
        "--curves-per-comparison",
        dest="curves_per_comparison",
        type=int,
        default=4,
        help="Number of deterministic representative curves to draw per comparison group.",
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def resolve_timestamped_output_paths(output_root: Path, report_topic_root: Path) -> tuple[str, Path, Path]:

    """Resolve timestamped output and report directories."""

    current_timestamp = datetime.now().astimezone()
    run_instance_id = (
        f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}"
        "__track2_multi_model_curve_comparison_report"
    )
    output_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(output_root)
        / run_instance_id
    )
    report_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(report_topic_root)
        / f"[{current_timestamp.strftime('%Y-%m-%d')}]"
    )
    output_directory.mkdir(parents=True, exist_ok=True)
    report_directory.mkdir(parents=True, exist_ok=True)
    return run_instance_id, output_directory, report_directory


def build_wave1_registry_candidate_configuration_list(family_registry_root: Path) -> list[dict[str, Any]]:

    """Build current-registry Wave 1 candidate configurations."""

    registry_root_text = shared_training_infrastructure.format_project_relative_path(
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
    ).replace("\\", "/")
    candidate_configuration_list: list[dict[str, Any]] = []

    for base_family_name in WAVE1_BASE_FAMILY_LIST:
        candidate_configuration_list.extend(
            [
                {
                    "candidate_id": f"{base_family_name}_fw",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave1_current_registry",
                    "candidate_surface": "Fw",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}_fw/latest_family_best.yaml",
                    "allowed_direction_list": ["forward"],
                },
                {
                    "candidate_id": f"{base_family_name}_bw",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave1_current_registry",
                    "candidate_surface": "Bw",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}_bw/latest_family_best.yaml",
                    "allowed_direction_list": ["backward"],
                },
            ]
        )

    return candidate_configuration_list


def resolve_report_candidate_configuration_list(
    training_config: dict[str, Any],
    family_registry_root: Path,
) -> list[dict[str, Any]]:

    """Resolve the selected Track 2 report candidates."""

    all_candidate_configuration_list = (
        reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(training_config)
    )
    wanted_reference_candidate_id_set = set(FORWARD_REFERENCE_CANDIDATE_ID_LIST + BACKWARD_REFERENCE_CANDIDATE_ID_LIST)
    reference_candidate_configuration_list = [
        candidate_configuration
        for candidate_configuration in all_candidate_configuration_list
        if str(candidate_configuration["candidate_id"]) in wanted_reference_candidate_id_set
    ]
    assert len(reference_candidate_configuration_list) == len(wanted_reference_candidate_id_set), (
        "Could not resolve every requested Track 2 reference best candidate."
    )

    return reference_candidate_configuration_list + build_wave1_registry_candidate_configuration_list(
        family_registry_root
    )


def build_base_comparison_group_list() -> list[ReportComparisonGroup]:

    """Build the ordered report groups before screened comparisons."""

    wave1_forward_candidate_id_list = [f"{family_name}_fw" for family_name in WAVE1_BASE_FAMILY_LIST]
    wave1_backward_candidate_id_list = [f"{family_name}_bw" for family_name in WAVE1_BASE_FAMILY_LIST]
    return [
        ReportComparisonGroup(
            group_id="forward_reference",
            group_title="Forward Reference Model Overlay",
            candidate_id_list=FORWARD_REFERENCE_CANDIDATE_ID_LIST,
            selection_mode="forward",
        ),
        ReportComparisonGroup(
            group_id="forward_wave1",
            group_title="Forward Wave 1 Family Model Overlay",
            candidate_id_list=wave1_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportComparisonGroup(
            group_id="backward_reference",
            group_title="Backward Reference Model Overlay",
            candidate_id_list=BACKWARD_REFERENCE_CANDIDATE_ID_LIST,
            selection_mode="backward",
        ),
        ReportComparisonGroup(
            group_id="backward_wave1",
            group_title="Backward Wave 1 Family Model Overlay",
            candidate_id_list=wave1_backward_candidate_id_list,
            selection_mode="backward",
        ),
    ]


def sort_curve_entry_list(entry_list: list[dict[str, Any]]) -> list[dict[str, Any]]:

    """Sort curve entries into a stable visual-inspection order."""

    return sorted(
        entry_list,
        key=lambda entry: (
            str(entry["direction_label"]),
            float(entry["oil_temperature_deg"]),
            float(entry["torque_nm"]),
            float(entry["speed_rpm"]),
            str(entry["source_file_path"]),
        ),
    )


def select_spread_entries(entry_list: list[dict[str, Any]], requested_count: int) -> list[dict[str, Any]]:

    """Select entries spread across the available sorted curve list."""

    sorted_entry_list = sort_curve_entry_list(entry_list)
    if len(sorted_entry_list) <= requested_count:
        return sorted_entry_list
    selected_position_array = np.linspace(0, len(sorted_entry_list) - 1, requested_count)
    selected_index_list = sorted({int(round(position)) for position in selected_position_array})
    while len(selected_index_list) < requested_count:
        selected_index_list.append(len(selected_index_list))
        selected_index_list = sorted(set(selected_index_list))
    return [sorted_entry_list[index_value] for index_value in selected_index_list[:requested_count]]


def select_group_reference_entries(
    candidate_entry_list: list[dict[str, Any]],
    selection_mode: str,
    curves_per_comparison: int,
) -> list[dict[str, Any]]:

    """Select representative curve entries for one comparison group."""

    assert curves_per_comparison == 4, "The current report layout expects four curves per comparison."
    direction_entry_list = [
        entry
        for entry in candidate_entry_list
        if str(entry["direction_label"]).strip().lower() == selection_mode
    ]
    return select_spread_entries(direction_entry_list, curves_per_comparison)

def build_entry_lookup_by_candidate_and_curve(
    per_candidate_entry_list: list[dict[str, Any]],
) -> dict[str, dict[str, dict[str, Any]]]:

    """Build a candidate/curve lookup for multi-model overlays."""

    grouped_lookup: dict[str, dict[str, dict[str, Any]]] = {}
    for per_candidate_entry in per_candidate_entry_list:
        candidate_id = str(per_candidate_entry["candidate_id"])
        curve_key = str(per_candidate_entry["source_file_path"])
        grouped_lookup.setdefault(candidate_id, {})[curve_key] = per_candidate_entry
    return grouped_lookup


def sanitize_filename_fragment(raw_value: str) -> str:

    """Sanitize one filename fragment."""

    return shared_training_infrastructure.sanitize_name(str(raw_value).strip().lower())


def save_comparison_collage(
    comparison_path: Path,
    group_title: str,
    candidate_id_list: list[str],
    selected_reference_entry_list: list[dict[str, Any]],
    entry_lookup_by_candidate_and_curve: dict[str, dict[str, dict[str, Any]]],
) -> None:

    """Save one four-curve collage with all group models overlaid."""

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    comparison_path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis_array = plt.subplots(2, 2, figsize=(12.0, 7.0), sharex=False, sharey=False)
    flattened_axis_list = list(axis_array.reshape(-1))
    candidate_color_list = [
        "#1f77b4",
        "#d62728",
        "#2ca02c",
        "#9467bd",
        "#ff7f0e",
        "#17becf",
    ]

    for axis, reference_entry in zip(flattened_axis_list, selected_reference_entry_list):
        curve_key = str(reference_entry["source_file_path"])
        angular_position_deg = np.asarray(reference_entry["angular_position_deg"], dtype=np.float32)
        truth_curve_deg = np.asarray(reference_entry["truth_curve_deg"], dtype=np.float32)
        axis.plot(angular_position_deg, truth_curve_deg, label="Original Curve", linewidth=1.2, color="#4a4a4a")

        for candidate_index, candidate_id in enumerate(candidate_id_list):
            per_candidate_entry = entry_lookup_by_candidate_and_curve[candidate_id][curve_key]
            predicted_curve_deg = np.asarray(per_candidate_entry["predicted_curve_deg"], dtype=np.float32)
            axis.plot(
                angular_position_deg,
                predicted_curve_deg,
                label=candidate_id,
                linewidth=1.05,
                color=candidate_color_list[candidate_index % len(candidate_color_list)],
            )

        axis.set_title(
            (
                f"{reference_entry['direction_label']} | "
                f"{float(reference_entry['speed_rpm']):.0f} rpm | "
                f"{float(reference_entry['torque_nm']):.0f} Nm | "
                f"{float(reference_entry['oil_temperature_deg']):.0f} C"
            ),
            fontsize=9,
        )
        axis.set_xlabel("Angular Position [deg]", fontsize=8)
        axis.set_ylabel("TE [deg]", fontsize=8)
        axis.grid(True, alpha=0.28)
        axis.tick_params(labelsize=8)

    for empty_axis in flattened_axis_list[len(selected_reference_entry_list):]:
        empty_axis.axis("off")

    flattened_axis_list[0].legend(loc="best", fontsize=7)
    figure.suptitle(group_title, fontsize=13)
    figure.tight_layout(rect=[0.0, 0.0, 1.0, 0.95])
    figure.savefig(comparison_path, dpi=180)
    plt.close(figure)


def build_relative_markdown_path(target_path: Path, markdown_directory: Path) -> str:

    """Build a Markdown-safe relative path from a report to an artifact."""

    relative_path = os.path.relpath(target_path.resolve(), markdown_directory.resolve())
    return relative_path.replace("\\", "/")


def save_candidate_metrics_csv(
    csv_path: Path,
    comparison_summary_list: list[dict[str, Any]],
) -> None:

    """Save compact metrics for every plotted comparison candidate."""

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
                "curve_mae_deg",
                "curve_rmse_deg",
                "mean_percentage_error_pct",
                "p95_mean_percentage_error_pct",
                "comparison_path",
            ]
        )
        for comparison_summary in comparison_summary_list:
            for candidate_summary in comparison_summary["candidate_summary_list"]:
                metric_dictionary = candidate_summary["metrics"]
                writer.writerow(
                    [
                        comparison_summary["group_id"],
                        candidate_summary["candidate_id"],
                        candidate_summary["candidate_family"],
                        candidate_summary["candidate_source_label"],
                        candidate_summary["candidate_surface"],
                        comparison_summary["direction_scope"],
                        f"{metric_dictionary['mae']:.9f}",
                        f"{metric_dictionary['rmse']:.9f}",
                        f"{metric_dictionary['mean_percentage_error_pct']:.9f}",
                        f"{metric_dictionary['p95_mean_percentage_error_pct']:.9f}",
                        comparison_summary["comparison_path"],
                    ]
                )


def append_candidate_table(
    report_line_list: list[str],
    group_summary_list: list[dict[str, Any]],
) -> None:

    """Append one compact candidate table."""

    report_line_list.extend(
        [
            "| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |",
            "| --- | --- | --- | ---: | ---: | ---: |",
        ]
    )
    for candidate_summary in group_summary_list:
        metric_dictionary = candidate_summary["metrics"]
        report_line_list.append(
            f"| `{candidate_summary['candidate_id']}` | "
            f"`{candidate_summary['candidate_source_label']}` | "
            f"{candidate_summary['candidate_surface']} | "
            f"{metric_dictionary['mae']:.6f} | "
            f"{metric_dictionary['rmse']:.6f} | "
            f"{metric_dictionary['mean_percentage_error_pct']:.3f} |"
        )


def get_gallery_section_title(group_title: str) -> str:

    """Return a stable gallery section title for one comparison page."""

    return f"Comparison Gallery - {group_title}"


def build_report_markdown(
    report_path: Path,
    output_directory: Path,
    comparison_summary_list: list[dict[str, Any]],
    metrics_csv_path: Path,
    validation_summary_path: Path,
) -> str:

    """Build the Markdown report body."""

    report_line_list = [
        "# Track 2 Multi-Model Curve Comparison Report",
        "",
        "## Overview",
        "",
        "This report compares representative `Track 2` TE curves by overlaying",
        "multiple model predictions on the same original measured curve. The",
        "plots are intended to show whether each model tracks the local harmonic",
        "oscillations rather than only the broad mean trend.",
        "",
        "## Scope",
        "",
        "- each comparison image contains four deterministic held-out test curves;",
        "- forward comparisons are shown on forward curves only;",
        "- backward comparisons are shown on backward curves only;",
        "- Wave 1 screening keeps the three strongest family-best models by",
        "  `Curve MAE [deg]` within each direction;",
        "- `Original Curve` uses the same visual weight as predictions and a",
        "  dark-gray color for balanced comparison.",
        "",
        "## Metrics Summary",
        "",
    ]

    for comparison_summary in comparison_summary_list:
        report_line_list.extend(
            [
                f"### {comparison_summary['group_title']}",
                "",
            ]
        )
        append_candidate_table(report_line_list, comparison_summary["candidate_summary_list"])
        report_line_list.append("")

    for comparison_summary in comparison_summary_list:
        report_line_list.extend(
            [
                f"## {get_gallery_section_title(comparison_summary['group_title'])}",
                "",
                "Included models: "
                + ", ".join(f"`{candidate_id}`" for candidate_id in comparison_summary["candidate_id_list"])
                + ".",
                "",
                (
                    f"![{comparison_summary['group_title']} Track 2 comparison]"
                    f"({comparison_summary['comparison_markdown_path']})"
                ),
                "",
            ]
        )

    report_line_list.extend(["## Output Artifacts", ""])

    report_line_list.extend(
        [
            f"- output directory: `{shared_training_infrastructure.format_project_relative_path(output_directory)}`;",
            f"- summary YAML: `{shared_training_infrastructure.format_project_relative_path(validation_summary_path)}`;",
            f"- metrics CSV: `{shared_training_infrastructure.format_project_relative_path(metrics_csv_path)}`;",
            f"- report Markdown: `{shared_training_infrastructure.format_project_relative_path(report_path)}`.",
        ]
    )

    return "\n".join(report_line_list) + "\n"


def select_screened_wave1_candidate_id_list(
    candidate_id_list: list[str],
    direction_label: str,
    direction_metric_summary: dict[str, dict[str, dict[str, float]]],
) -> list[str]:

    """Select the best Wave 1 candidates for a readable combined overlay."""

    ranked_candidate_id_list = sorted(
        candidate_id_list,
        key=lambda candidate_id: float(direction_metric_summary[direction_label][candidate_id]["mae"]),
    )
    return ranked_candidate_id_list[:SCREENED_WAVE1_MODEL_COUNT]


def build_full_comparison_group_list(
    direction_metric_summary: dict[str, dict[str, dict[str, float]]],
) -> list[ReportComparisonGroup]:

    """Build all report groups, including screened Track 1 plus Wave 1 groups."""

    group_list = build_base_comparison_group_list()
    wave1_forward_candidate_id_list = [f"{family_name}_fw" for family_name in WAVE1_BASE_FAMILY_LIST]
    wave1_backward_candidate_id_list = [f"{family_name}_bw" for family_name in WAVE1_BASE_FAMILY_LIST]
    screened_forward_candidate_id_list = select_screened_wave1_candidate_id_list(
        wave1_forward_candidate_id_list,
        "forward",
        direction_metric_summary,
    )
    screened_backward_candidate_id_list = select_screened_wave1_candidate_id_list(
        wave1_backward_candidate_id_list,
        "backward",
        direction_metric_summary,
    )
    group_list.extend(
        [
            ReportComparisonGroup(
                group_id="forward_track1_screened_wave1",
                group_title="Forward Track 1 And Screened Wave 1 Overlay",
                candidate_id_list=["track1_best_Fw"] + screened_forward_candidate_id_list,
                selection_mode="forward",
            ),
            ReportComparisonGroup(
                group_id="backward_track1_screened_wave1",
                group_title="Backward Track 1 And Screened Wave 1 Overlay",
                candidate_id_list=["track1_best_Bw"] + screened_backward_candidate_id_list,
                selection_mode="backward",
            ),
        ]
    )
    return group_list


def build_group_candidate_summary_list(
    group: ReportComparisonGroup,
    candidate_lookup: dict[str, Any],
    direction_metric_summary: dict[str, dict[str, dict[str, float]]],
) -> list[dict[str, Any]]:

    """Build per-candidate metric summary rows for one comparison group."""

    candidate_summary_list: list[dict[str, Any]] = []
    for candidate_id in group.candidate_id_list:
        candidate = candidate_lookup[candidate_id]
        candidate_summary_list.append(
            {
                "candidate_id": candidate_id,
                "candidate_family": candidate.candidate_family,
                "candidate_kind": candidate.candidate_kind,
                "candidate_source_label": candidate.candidate_source_label,
                "candidate_surface": candidate.candidate_surface,
                "allowed_direction_list": candidate.allowed_direction_list,
                "source_path": shared_training_infrastructure.format_project_relative_path(
                    candidate.source_path
                ),
                "metrics": direction_metric_summary[group.selection_mode][candidate_id],
            }
        )
    return candidate_summary_list


def run_track2_multi_model_curve_comparison_report(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the full Track 2 multi-model curve comparison report generation."""

    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(arguments)
    )
    assert int(arguments.curves_per_comparison) == 4, "This report requires exactly four curves per comparison."

    run_instance_id, output_directory, report_directory = resolve_timestamped_output_paths(
        arguments.output_root,
        arguments.report_topic_root,
    )
    report_path = report_directory / REPORT_FILENAME
    metrics_csv_path = output_directory / METRICS_FILENAME
    validation_summary_path = output_directory / SUMMARY_FILENAME

    training_config = shared_training_infrastructure.load_training_config(arguments.config_path)
    selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
    curve_record_list, _, _, dataset_root = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])

    candidate_configuration_list = resolve_report_candidate_configuration_list(
        training_config,
        arguments.family_registry_root,
    )
    candidate_list = [
        reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)
        for candidate_configuration in candidate_configuration_list
    ]
    candidate_lookup = {
        candidate.candidate_id: candidate
        for candidate in candidate_list
    }

    per_candidate_entry_list: list[dict[str, Any]] = []
    for candidate in candidate_list:
        candidate_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
            candidate,
            curve_record_list,
            percentage_error_denominator,
        )
        per_candidate_entry_list.extend(candidate_entry_list)

    grouped_entry_dictionary: dict[str, list[dict[str, Any]]] = {}
    for per_candidate_entry in per_candidate_entry_list:
        grouped_entry_dictionary.setdefault(str(per_candidate_entry["candidate_id"]), []).append(per_candidate_entry)

    direction_metric_summary = reference_family_vs_feedforward_support.build_generic_group_metric_summary(
        per_candidate_entry_list,
        "direction_label",
    )
    group_list = build_full_comparison_group_list(direction_metric_summary)
    entry_lookup_by_candidate_and_curve = build_entry_lookup_by_candidate_and_curve(per_candidate_entry_list)
    comparison_summary_list: list[dict[str, Any]] = []

    for group in group_list:
        selected_reference_entry_list = select_group_reference_entries(
            grouped_entry_dictionary[group.candidate_id_list[0]],
            group.selection_mode,
            int(arguments.curves_per_comparison),
        )
        comparison_path = (
            output_directory
            / "comparisons"
            / f"{sanitize_filename_fragment(group.group_id)}.png"
        )
        save_comparison_collage(
            comparison_path,
            group.group_title,
            group.candidate_id_list,
            selected_reference_entry_list,
            entry_lookup_by_candidate_and_curve,
        )
        comparison_summary_list.append(
            {
                "group_id": group.group_id,
                "group_title": group.group_title,
                "candidate_id_list": group.candidate_id_list,
                "direction_scope": group.selection_mode,
                "candidate_summary_list": build_group_candidate_summary_list(
                    group,
                    candidate_lookup,
                    direction_metric_summary,
                ),
                "comparison_path": shared_training_infrastructure.format_project_relative_path(comparison_path),
                "comparison_markdown_path": build_relative_markdown_path(comparison_path, report_path.parent),
                "selected_curve_list": [
                    {
                        "source_file_path": entry["source_file_path"],
                        "direction_label": entry["direction_label"],
                        "speed_rpm": float(entry["speed_rpm"]),
                        "torque_nm": float(entry["torque_nm"]),
                        "oil_temperature_deg": float(entry["oil_temperature_deg"]),
                    }
                    for entry in selected_reference_entry_list
                ],
            }
        )

    save_candidate_metrics_csv(metrics_csv_path, comparison_summary_list)
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
        "comparison_count": int(len(comparison_summary_list)),
        "comparison_summary_list": comparison_summary_list,
        "metrics_csv_path": shared_training_infrastructure.format_project_relative_path(metrics_csv_path),
    }
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

    report_markdown = build_report_markdown(
        report_path,
        output_directory,
        comparison_summary_list,
        metrics_csv_path,
        validation_summary_path,
    )
    report_path.write_text(report_markdown, encoding="utf-8")
    return validation_summary


def main() -> None:

    """Run the command-line entry point."""

    validation_summary = run_track2_multi_model_curve_comparison_report(parse_command_line_arguments())
    print(f"[DONE] Track 2 multi-model comparison report: {validation_summary['report_path']}")
    print(f"[DONE] Artifacts: {validation_summary['output_directory']}")


if __name__ == "__main__":
    main()
