"""Build the Track 2 best-model collage report and plot artifacts."""

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
import yaml

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
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_best_model_collage_report"
DEFAULT_REPORT_TOPIC_ROOT = PROJECT_PATH / "doc" / "reports" / "analysis" / "track2" / "best_model_collage_report"
DEFAULT_FAMILY_REGISTRY_ROOT = PROJECT_PATH / "output" / "registries" / "families"
DEFAULT_PERIODIC_MLP_HARMONIC_CAMPAIGN_LEADERBOARD_PATH = (
    PROJECT_PATH
    / "output"
    / "training_campaigns"
    / "2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42"
    / "campaign_leaderboard.yaml"
)
SUMMARY_FILENAME = "track2_best_model_collage_summary.yaml"
METRICS_FILENAME = "track2_best_model_collage_metrics.csv"
REPORT_FILENAME = "track2_best_model_collage_report.md"

WAVE1_BASE_FAMILY_LIST = [
    "feedforward",
    "harmonic_regression",
    "periodic_mlp",
    "residual_harmonic_mlp",
    "tree",
]
WAVE2_BASE_FAMILY_LIST = [
    "temporal_convolution",
    "gru_sequence",
    "lstm_sequence",
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
class ReportCandidateGroup:

    """One logical report group for a set of candidates."""

    group_id: str
    group_title: str
    candidate_id_list: list[str]
    selection_mode: str


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Generate the Track 2 best-model visual report with one four-curve "
            "collage per selected reference, Wave 1 directional, and Wave 1 "
            "global candidate."
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
        help="Root for generated collage artifacts and machine-readable summaries.",
    )
    argument_parser.add_argument(
        "--report-topic-root",
        type=Path,
        default=DEFAULT_REPORT_TOPIC_ROOT,
        help="Root for the dated Markdown/PDF report bundle.",
    )
    argument_parser.add_argument(
        "--report-date",
        type=str,
        default=None,
        help=(
            "Optional YYYY-MM-DD report bundle date to refresh instead of "
            "creating a report folder from the current date."
        ),
    )
    argument_parser.add_argument(
        "--family-registry-root",
        type=Path,
        default=DEFAULT_FAMILY_REGISTRY_ROOT,
        help="Root containing current Wave 1 family latest_family_best.yaml registries.",
    )
    argument_parser.add_argument(
        "--periodic-mlp-harmonic-campaign-leaderboard-path",
        type=Path,
        default=DEFAULT_PERIODIC_MLP_HARMONIC_CAMPAIGN_LEADERBOARD_PATH,
        help="Completed campaign leaderboard used to add explicit-harmonic periodic MLP candidates.",
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
        "__track2_best_model_collage_report"
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
                    "candidate_id": f"{base_family_name}_global",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave1_current_registry",
                    "candidate_surface": "global",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}/latest_family_best.yaml",
                    "allowed_direction_list": ["forward", "backward"],
                },
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


def build_wave2_registry_candidate_configuration_list(family_registry_root: Path) -> list[dict[str, Any]]:

    """Build current-registry Wave 2 temporal candidate configurations."""

    registry_root_text = shared_training_infrastructure.format_project_relative_path(
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
    ).replace("\\", "/")
    candidate_configuration_list: list[dict[str, Any]] = []

    for base_family_name in WAVE2_BASE_FAMILY_LIST:
        candidate_configuration_list.extend(
            [
                {
                    "candidate_id": f"{base_family_name}_global",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave2_temporal_entry_registry",
                    "candidate_surface": "global",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}/latest_family_best.yaml",
                    "allowed_direction_list": ["forward", "backward"],
                },
                {
                    "candidate_id": f"{base_family_name}_fw",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave2_temporal_entry_registry",
                    "candidate_surface": "Fw",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}_fw/latest_family_best.yaml",
                    "allowed_direction_list": ["forward"],
                },
                {
                    "candidate_id": f"{base_family_name}_bw",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave2_temporal_entry_registry",
                    "candidate_surface": "Bw",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}_bw/latest_family_best.yaml",
                    "allowed_direction_list": ["backward"],
                },
            ]
        )

    return candidate_configuration_list


def build_periodic_mlp_harmonic_campaign_candidate_configuration_list(
    campaign_leaderboard_path: Path,
    output_directory: Path,
) -> list[dict[str, Any]]:

    """Build explicit-harmonic periodic MLP candidate configs from one campaign."""

    resolved_leaderboard_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        campaign_leaderboard_path
    )
    if not resolved_leaderboard_path.exists():
        return []

    with resolved_leaderboard_path.open("r", encoding="utf-8") as input_stream:
        leaderboard = yaml.safe_load(input_stream)
    entry_list = list(leaderboard["entry_list"])
    model_family_to_candidate_metadata = {
        "periodic_mlp": {
            "candidate_id": "periodic_mlp_harmonic_global",
            "candidate_surface": "global",
            "allowed_direction_list": ["forward", "backward"],
        },
        "periodic_mlp_fw": {
            "candidate_id": "periodic_mlp_harmonic_fw",
            "candidate_surface": "Fw",
            "allowed_direction_list": ["forward"],
        },
        "periodic_mlp_bw": {
            "candidate_id": "periodic_mlp_harmonic_bw",
            "candidate_surface": "Bw",
            "allowed_direction_list": ["backward"],
        },
    }
    snapshot_directory = output_directory / "registry_snapshots" / "periodic_mlp_harmonic_campaign"
    snapshot_directory.mkdir(parents=True, exist_ok=True)
    candidate_configuration_list: list[dict[str, Any]] = []

    for model_family, candidate_metadata in model_family_to_candidate_metadata.items():
        matching_entry_list = [
            entry
            for entry in entry_list
            if str(entry["model_family"]).strip() == model_family
        ]
        if not matching_entry_list:
            continue

        best_entry = min(
            matching_entry_list,
            key=lambda entry: (
                float(entry["test_mae"]),
                float(entry["test_rmse"]),
                float(entry["val_mae"]),
                int(entry["trainable_parameter_count"]),
            ),
        )
        snapshot_path = snapshot_directory / f"{candidate_metadata['candidate_id']}.yaml"
        shared_training_infrastructure.save_yaml_snapshot(
            {
                "schema_version": 1,
                "source_campaign_leaderboard_path": shared_training_infrastructure.format_project_relative_path(
                    resolved_leaderboard_path
                ),
                "best_entry": best_entry,
            },
            snapshot_path,
        )
        candidate_configuration_list.append(
            {
                "candidate_id": candidate_metadata["candidate_id"],
                "candidate_family": "periodic_mlp_harmonic",
                "candidate_kind": "wave1_registry_model",
                "candidate_source_label": "wave1_periodic_mlp_harmonic_campaign",
                "candidate_surface": candidate_metadata["candidate_surface"],
                "family_registry_path": shared_training_infrastructure.format_project_relative_path(
                    snapshot_path
                ).replace("\\", "/"),
                "allowed_direction_list": candidate_metadata["allowed_direction_list"],
            }
        )

    return candidate_configuration_list


def resolve_report_candidate_configuration_list(
    training_config: dict[str, Any],
    family_registry_root: Path,
    periodic_mlp_harmonic_campaign_leaderboard_path: Path,
    output_directory: Path,
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

    return (
        reference_candidate_configuration_list
        + build_wave1_registry_candidate_configuration_list(family_registry_root)
        + build_wave2_registry_candidate_configuration_list(family_registry_root)
        + build_periodic_mlp_harmonic_campaign_candidate_configuration_list(
            periodic_mlp_harmonic_campaign_leaderboard_path,
            output_directory,
        )
    )


def build_report_group_list() -> list[ReportCandidateGroup]:

    """Build the ordered report groups."""

    wave1_forward_candidate_id_list = [f"{family_name}_fw" for family_name in WAVE1_BASE_FAMILY_LIST]
    wave1_forward_candidate_id_list.append("periodic_mlp_harmonic_fw")
    wave1_backward_candidate_id_list = [f"{family_name}_bw" for family_name in WAVE1_BASE_FAMILY_LIST]
    wave1_backward_candidate_id_list.append("periodic_mlp_harmonic_bw")
    wave1_global_candidate_id_list = [f"{family_name}_global" for family_name in WAVE1_BASE_FAMILY_LIST]
    wave1_global_candidate_id_list.append("periodic_mlp_harmonic_global")
    wave2_forward_candidate_id_list = [f"{family_name}_fw" for family_name in WAVE2_BASE_FAMILY_LIST]
    wave2_backward_candidate_id_list = [f"{family_name}_bw" for family_name in WAVE2_BASE_FAMILY_LIST]
    wave2_global_candidate_id_list = [f"{family_name}_global" for family_name in WAVE2_BASE_FAMILY_LIST]

    return [
        ReportCandidateGroup(
            group_id="forward_reference",
            group_title="Forward Reference Best Models",
            candidate_id_list=FORWARD_REFERENCE_CANDIDATE_ID_LIST,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="forward_wave1",
            group_title="Forward Wave 1 Family Best Models",
            candidate_id_list=wave1_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_reference",
            group_title="Backward Reference Best Models",
            candidate_id_list=BACKWARD_REFERENCE_CANDIDATE_ID_LIST,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="backward_wave1",
            group_title="Backward Wave 1 Family Best Models",
            candidate_id_list=wave1_backward_candidate_id_list,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="forward_wave2",
            group_title="Forward Wave 2 Temporal Family Best Models",
            candidate_id_list=wave2_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_wave2",
            group_title="Backward Wave 2 Temporal Family Best Models",
            candidate_id_list=wave2_backward_candidate_id_list,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="global_wave1",
            group_title="Global Wave 1 Family Best Models",
            candidate_id_list=wave1_global_candidate_id_list,
            selection_mode="mixed",
        ),
        ReportCandidateGroup(
            group_id="global_wave2",
            group_title="Global Wave 2 Temporal Family Best Models",
            candidate_id_list=wave2_global_candidate_id_list,
            selection_mode="mixed",
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


def select_candidate_collage_entries(
    candidate_entry_list: list[dict[str, Any]],
    selection_mode: str,
    curves_per_collage: int,
) -> list[dict[str, Any]]:

    """Select the representative entries for one candidate collage."""

    assert curves_per_collage == 4, "The current report layout expects four curves per collage."
    if selection_mode != "mixed":
        direction_entry_list = [
            entry
            for entry in candidate_entry_list
            if str(entry["direction_label"]).strip().lower() == selection_mode
        ]
        return select_spread_entries(direction_entry_list, curves_per_collage)

    forward_entry_list = [
        entry
        for entry in candidate_entry_list
        if str(entry["direction_label"]).strip().lower() == "forward"
    ]
    backward_entry_list = [
        entry
        for entry in candidate_entry_list
        if str(entry["direction_label"]).strip().lower() == "backward"
    ]
    return select_spread_entries(forward_entry_list, 2) + select_spread_entries(backward_entry_list, 2)


def sanitize_filename_fragment(raw_value: str) -> str:

    """Sanitize one filename fragment."""

    return shared_training_infrastructure.sanitize_name(str(raw_value).strip().lower())


def save_candidate_collage(
    collage_path: Path,
    candidate_id: str,
    selected_entry_list: list[dict[str, Any]],
) -> None:

    """Save one four-curve collage for a candidate."""

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    collage_path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis_array = plt.subplots(2, 2, figsize=(12.0, 7.0), sharex=False, sharey=False)
    flattened_axis_list = list(axis_array.reshape(-1))

    for axis, per_candidate_entry in zip(flattened_axis_list, selected_entry_list):
        angular_position_deg = np.asarray(per_candidate_entry["angular_position_deg"], dtype=np.float32)
        truth_curve_deg = np.asarray(per_candidate_entry["truth_curve_deg"], dtype=np.float32)
        predicted_curve_deg = np.asarray(per_candidate_entry["predicted_curve_deg"], dtype=np.float32)
        axis.plot(angular_position_deg, truth_curve_deg, label="Measured TE", linewidth=1.2, color="#4a4a4a")
        axis.plot(angular_position_deg, predicted_curve_deg, label=candidate_id, linewidth=1.2, color="#1f77b4")
        axis.set_title(
            (
                f"{per_candidate_entry['direction_label']} | "
                f"{float(per_candidate_entry['speed_rpm']):.0f} rpm | "
                f"{float(per_candidate_entry['torque_nm']):.0f} Nm | "
                f"{float(per_candidate_entry['oil_temperature_deg']):.0f} C"
            ),
            fontsize=9,
        )
        axis.set_xlabel("Angular Position [deg]", fontsize=8)
        axis.set_ylabel("TE [deg]", fontsize=8)
        axis.grid(True, alpha=0.28)
        axis.tick_params(labelsize=8)

    for empty_axis in flattened_axis_list[len(selected_entry_list):]:
        empty_axis.axis("off")

    flattened_axis_list[0].legend(loc="best", fontsize=8)
    figure.suptitle(candidate_id, fontsize=13)
    figure.tight_layout(rect=[0.0, 0.0, 1.0, 0.95])
    figure.savefig(collage_path, dpi=180)
    plt.close(figure)


def build_relative_markdown_path(target_path: Path, markdown_directory: Path) -> str:

    """Build a Markdown-safe relative path from a report to an artifact."""

    relative_path = os.path.relpath(target_path.resolve(), markdown_directory.resolve())
    return relative_path.replace("\\", "/")


def save_candidate_metrics_csv(
    csv_path: Path,
    candidate_summary_list: list[dict[str, Any]],
) -> None:

    """Save compact metrics for every collaged candidate."""

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
                "collage_path",
            ]
        )
        for candidate_summary in candidate_summary_list:
            metric_dictionary = candidate_summary["metrics"]
            writer.writerow(
                [
                    candidate_summary["group_id"],
                    candidate_summary["candidate_id"],
                    candidate_summary["candidate_family"],
                    candidate_summary["candidate_source_label"],
                    candidate_summary["candidate_surface"],
                    candidate_summary["direction_scope"],
                    f"{metric_dictionary['mae']:.9f}",
                    f"{metric_dictionary['rmse']:.9f}",
                    f"{metric_dictionary['mean_percentage_error_pct']:.9f}",
                    f"{metric_dictionary['p95_mean_percentage_error_pct']:.9f}",
                    candidate_summary["collage_path"],
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


def get_gallery_section_title(group_title: str, chunk_index: int) -> str:

    """Return a stable gallery section title for two-model PDF pages."""

    base_title = f"Collage Gallery - {group_title}"
    if chunk_index == 0:
        return base_title
    if chunk_index == 1:
        return f"{base_title} Continued"
    return f"{base_title} Continued {chunk_index}"


def build_report_markdown(
    report_path: Path,
    output_directory: Path,
    candidate_summary_list: list[dict[str, Any]],
    group_list: list[ReportCandidateGroup],
    metrics_csv_path: Path,
    validation_summary_path: Path,
) -> str:

    """Build the Markdown report body."""

    report_line_list = [
        "# Track 2 Best Model Collage Report",
        "",
        "## Overview",
        "",
        "This report compares representative `Track 2` TE-curve predictions for",
        "the current best reference, Track 1, Wave 1 directional, and Wave 1",
        "global models. Each model is shown as one four-image collage so local",
        "oscillation tracking can be inspected directly.",
        "",
        "## Scope",
        "",
        "- each collage contains four deterministic held-out test curves;",
        "- forward models are shown on forward curves only;",
        "- backward models are shown on backward curves only;",
        "- global Wave 1 models are shown on two forward and two backward curves;",
        "- `Measured TE` uses the same line width as predictions and a dark-gray",
        "  color for balanced visual comparison.",
        "",
        "## Metrics Summary",
        "",
    ]

    candidate_summary_by_group = {
        group.group_id: [
            candidate_summary
            for candidate_summary in candidate_summary_list
            if candidate_summary["group_id"] == group.group_id
        ]
        for group in group_list
    }

    for group in group_list:
        report_line_list.extend(
            [
                f"### {group.group_title}",
                "",
            ]
        )
        append_candidate_table(report_line_list, candidate_summary_by_group[group.group_id])
        report_line_list.append("")

    for group in group_list:
        group_summary_list = candidate_summary_by_group[group.group_id]
        for chunk_start_index in range(0, len(group_summary_list), 2):
            chunk_index = chunk_start_index // 2
            section_title = get_gallery_section_title(group.group_title, chunk_index)
            report_line_list.extend([f"## {section_title}", ""])
            for candidate_summary in group_summary_list[chunk_start_index : chunk_start_index + 2]:
                report_line_list.extend(
                    [
                        f"{candidate_summary['candidate_id']}:",
                        "",
                        (
                            f"![{candidate_summary['candidate_id']} Track 2 collage]"
                            f"({candidate_summary['collage_markdown_path']})"
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


def run_track2_best_model_collage_report(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the full Track 2 best-model collage report generation."""

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

    candidate_metric_summary = reference_family_vs_feedforward_support.build_candidate_metric_summary(
        per_candidate_entry_list
    )
    direction_metric_summary = reference_family_vs_feedforward_support.build_generic_group_metric_summary(
        per_candidate_entry_list,
        "direction_label",
    )
    group_list = build_report_group_list()
    candidate_summary_list: list[dict[str, Any]] = []

    for group in group_list:
        for candidate_id in group.candidate_id_list:
            candidate = candidate_lookup[candidate_id]
            selected_entry_list = select_candidate_collage_entries(
                grouped_entry_dictionary[candidate_id],
                group.selection_mode,
                int(arguments.curves_per_collage),
            )
            collage_path = (
                output_directory
                / "collages"
                / group.group_id
                / f"{sanitize_filename_fragment(candidate_id)}.png"
            )
            save_candidate_collage(collage_path, candidate_id, selected_entry_list)

            if group.selection_mode in {"forward", "backward"}:
                metric_dictionary = direction_metric_summary[group.selection_mode][candidate_id]
            else:
                metric_dictionary = candidate_metric_summary[candidate_id]

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
                    "source_path": shared_training_infrastructure.format_project_relative_path(
                        candidate.source_path
                    ),
                    "metrics": metric_dictionary,
                    "collage_path": shared_training_infrastructure.format_project_relative_path(collage_path),
                    "collage_markdown_path": build_relative_markdown_path(collage_path, report_path.parent),
                    "selected_curve_list": [
                        {
                            "source_file_path": entry["source_file_path"],
                            "direction_label": entry["direction_label"],
                            "speed_rpm": float(entry["speed_rpm"]),
                            "torque_nm": float(entry["torque_nm"]),
                            "oil_temperature_deg": float(entry["oil_temperature_deg"]),
                            "metrics": entry["metrics"],
                        }
                        for entry in selected_entry_list
                    ],
                }
            )

    save_candidate_metrics_csv(metrics_csv_path, candidate_summary_list)
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
        "candidate_summary_list": candidate_summary_list,
        "metrics_csv_path": shared_training_infrastructure.format_project_relative_path(metrics_csv_path),
    }
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

    report_markdown = build_report_markdown(
        report_path,
        output_directory,
        candidate_summary_list,
        group_list,
        metrics_csv_path,
        validation_summary_path,
    )
    report_path.write_text(report_markdown, encoding="utf-8")
    return validation_summary


def main() -> None:

    """Run the command-line entry point."""

    validation_summary = run_track2_best_model_collage_report(parse_command_line_arguments())
    print(f"[DONE] Track 2 collage report: {validation_summary['report_path']}")
    print(f"[DONE] Artifacts: {validation_summary['output_directory']}")


if __name__ == "__main__":
    main()
