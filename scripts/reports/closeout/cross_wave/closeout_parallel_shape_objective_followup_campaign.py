"""Close out the parallel shape-objective follow-up campaign."""

from __future__ import annotations

# Import Python Utilities
import os
import sys
from pathlib import Path
from typing import Any

# Import Plotting Utilities
import matplotlib.pyplot as plt

# Import YAML Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[4]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

CAMPAIGN_NAME = "parallel_shape_objective_followup_2026_07_21"
CAMPAIGN_OUTPUT_DIRECTORY = PROJECT_PATH / "output" / "training_campaigns" / "2026-07-21-18-52-44_parallel_shape_objective_followup_2026_07_21"
CAMPAIGN_RESULTS_REPORT_PATH = PROJECT_PATH / "doc" / "reports" / "campaign_results" / "cross_wave" / "shape_objective" / "2026-07-21-19-31-21_parallel_shape_objective_followup_campaign_results_report.md"
REPORT_ASSET_DIRECTORY = CAMPAIGN_RESULTS_REPORT_PATH.parent / "assets" / "2026-07-21_parallel_shape_objective_followup"
TRACK2_PLOT_ROOT = PROJECT_PATH / "doc" / "reports" / "campaign_results" / "track_2" / "verification_plots" / "shape_objective_followup_polished_setpoints_fw"
TRACK2_PLOT_SUMMARY_PATH = TRACK2_PLOT_ROOT / "track2_candidate_curve_plot_summary.yaml"
TRACK2_PLOT_CONFIG_PATH = PROJECT_PATH / "config" / "paper_reimplementation" / "rcim_ml_compensation" / "reference_family_vs_feedforward" / "shape_objective_followup_track2_plot_polished_setpoints_fw_matrix.yaml"
PLANNING_REPORT_PATH = PROJECT_PATH / "doc" / "reports" / "campaign_plans" / "cross_wave" / "shape_objective" / "2026-07-21-18-36-30_parallel_shape_objective_followup_campaign_plan_report.md"
TECHNICAL_DOCUMENT_PATH = PROJECT_PATH / "doc" / "technical" / "2026-07" / "2026-07-21" / "2026-07-21-18-36-30_parallel_shape_objective_followup.md"
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
DOC_INDEX_PATH = PROJECT_PATH / "doc" / "README.md"

RUN_LABEL_BY_FAMILY = {
    "shape_objective_v3_periodic_gru_sequence_fw": "Windowed GRU",
    "shape_objective_periodic_mlp_harmonic_fw": "Non-windowed MLP",
    "shape_objective_curve_aware_residual_fw": "Curve-aware residual",
}


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:
    """Load one YAML dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def write_yaml_dictionary(output_path: Path, payload: dict[str, Any]) -> None:
    """Write one YAML dictionary."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=False)


def write_text_file(output_path: Path, text: str) -> None:
    """Write one UTF-8 text file with a single final newline."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    output_path.write_text(text, encoding="utf-8", newline="\n")


def format_relative_path(path_value: Path | str) -> str:
    """Format one path as repository-relative text when possible."""

    path_candidate = Path(path_value)
    if not path_candidate.is_absolute():
        return str(path_candidate).replace("\\", "/")

    try:
        return str(path_candidate.resolve().relative_to(PROJECT_PATH)).replace("\\", "/")
    except ValueError:
        return str(path_candidate).replace("\\", "/")


def format_report_local_path(path_value: Path | str) -> str:
    """Format one path relative to the campaign report directory."""

    path_candidate = Path(path_value)
    if not path_candidate.is_absolute():
        path_candidate = PROJECT_PATH / path_candidate
    return os.path.relpath(
        str(path_candidate.resolve()),
        str(CAMPAIGN_RESULTS_REPORT_PATH.parent.resolve()),
    ).replace("\\", "/")


def format_metric(value: Any) -> str:
    """Format one scalar metric value."""

    return f"{float(value):.6f}"


def format_metric_delta(candidate_value: Any, baseline_value: Any) -> str:
    """Format percentage delta versus a baseline."""

    candidate_float = float(candidate_value)
    baseline_float = float(baseline_value)
    if baseline_float == 0.0:
        return "n/a"
    return f"{((candidate_float / baseline_float) - 1.0) * 100.0:+.1f}%"


def format_improvement_phrase(candidate_value: Any, baseline_value: Any) -> str:
    """Format a sentence-safe improvement phrase."""

    delta_text = format_metric_delta(candidate_value, baseline_value)
    if delta_text == "n/a":
        return delta_text

    delta_value = float(delta_text.rstrip("%"))
    if delta_value < 0.0:
        return f"{abs(delta_value):.1f}% lower"
    if delta_value > 0.0:
        return f"{delta_value:.1f}% higher"
    return "unchanged"


def load_run_metrics(entry: dict[str, Any]) -> dict[str, Any]:
    """Load the metrics summary for one leaderboard entry."""

    metrics_path = PROJECT_PATH / str(entry["metrics_path"]).replace("\\", "/")
    return load_yaml_dictionary(metrics_path)


def resolve_run_label(entry: dict[str, Any]) -> str:
    """Resolve a compact plot/report label for one run."""

    model_family = str(entry["model_family"])
    return RUN_LABEL_BY_FAMILY.get(model_family, model_family)


def build_metric_breakdown_table(best_metrics: dict[str, Any]) -> str:
    """Build a metric breakdown table with PDF-stable headers."""

    validation_metrics = best_metrics["validation_metrics"]
    test_metrics = best_metrics["test_metrics"]
    row_list = [
        ("MAE", validation_metrics["val_mae"], test_metrics["test_mae"]),
        ("RMSE", validation_metrics["val_rmse"], test_metrics["test_rmse"]),
        ("Centered curve shape loss", validation_metrics["val_centered_curve_shape_loss"], test_metrics["test_centered_curve_shape_loss"]),
        ("Curve offset loss", validation_metrics["val_curve_offset_loss"], test_metrics["test_curve_offset_loss"]),
        ("Curve amplitude loss", validation_metrics["val_curve_amplitude_loss"], test_metrics["test_curve_amplitude_loss"]),
        ("Sparse harmonic shape loss", validation_metrics["val_sparse_harmonic_shape_loss"], test_metrics["test_sparse_harmonic_shape_loss"]),
    ]

    line_list = [
        "| Metric | Validation | Test |",
        "| --- | --- | --- |",
    ]
    for metric_name, validation_value, test_value in row_list:
        line_list.append(f"| {metric_name} | {format_metric(validation_value)} | {format_metric(test_value)} |")
    return "\n".join(line_list)


def build_pilot_comparison_table(entry_list: list[dict[str, Any]]) -> str:
    """Build the pilot comparison table with PDF-stable headers."""

    best_test_mae = min(float(entry["test_mae"]) for entry in entry_list)
    line_list = [
        "| Family | Surface | Validation MAE | Test MAE | Decision |",
        "| --- | --- | --- | --- | --- |",
    ]

    for index, entry in enumerate(entry_list, start=1):
        label = resolve_run_label(entry)
        decision = "Pilot scalar leader; requires curve-first screen" if float(entry["test_mae"]) == best_test_mae else "Do not promote from scalar closeout"
        line_list.append(
            "| "
            f"`{label}` | "
            "Fw | "
            f"{format_metric(entry['val_mae'])} | "
            f"{format_metric(entry['test_mae'])} | "
            f"{decision} |"
        )
    return "\n".join(line_list)


def build_artifact_table() -> str:
    """Build the report artifact table."""

    row_list = [
        ("Campaign output", CAMPAIGN_OUTPUT_DIRECTORY),
        ("Campaign leaderboard", CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.yaml"),
        ("Campaign best run", CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.yaml"),
        ("Campaign execution report", CAMPAIGN_OUTPUT_DIRECTORY / "campaign_execution_report.md"),
        ("Planning report", PLANNING_REPORT_PATH),
        ("Technical document", TECHNICAL_DOCUMENT_PATH),
        ("Track 2 pilot plot config", TRACK2_PLOT_CONFIG_PATH),
        ("Track 2 pilot curve plot summary", TRACK2_PLOT_SUMMARY_PATH),
        ("Secondary scalar graph bundle", REPORT_ASSET_DIRECTORY),
    ]
    line_list = [
        "| Artifact | Path |",
        "| --- | --- |",
    ]
    for label, path in row_list:
        line_list.append(f"| {label} | `{format_relative_path(path)}` |")
    return "\n".join(line_list)


def group_track2_plot_paths_by_candidate(plot_path_list: list[str]) -> dict[str, list[Path]]:
    """Group Track 2 plot paths by candidate directory name."""

    grouped_plot_path_dictionary: dict[str, list[Path]] = {}
    for plot_path_text in plot_path_list:
        plot_path = PROJECT_PATH / str(plot_path_text).replace("\\", "/")
        if not plot_path.exists():
            continue
        grouped_plot_path_dictionary.setdefault(plot_path.parent.name, []).append(plot_path)
    return grouped_plot_path_dictionary


def build_track2_curve_plot_section() -> str:
    """Build the Track 2 measured-versus-predicted graph section."""

    if not TRACK2_PLOT_SUMMARY_PATH.exists():
        command_text = (
            "conda run --no-capture-output -n pinns_env python -B "
            "scripts/reports/analysis/build_track2_candidate_curve_plots.py "
            "--config-path "
            f"{format_relative_path(TRACK2_PLOT_CONFIG_PATH)} "
            "--output-root "
            f"{format_relative_path(TRACK2_PLOT_ROOT)} "
            "--dataset polished_dataset "
            "--surface-scope forward "
            "--max-plots-per-candidate 2"
        )
        return (
            "Track 2 measured-versus-predicted plot artifacts are pending. "
            "Generate them with:\n\n"
            f"```powershell\n{command_text}\n```\n"
        )

    plot_summary = load_yaml_dictionary(TRACK2_PLOT_SUMMARY_PATH)
    plot_path_list = [str(path_text) for path_text in plot_summary.get("plot_path_list", [])]
    grouped_plot_path_dictionary = group_track2_plot_paths_by_candidate(plot_path_list)
    if not grouped_plot_path_dictionary:
        return (
            "Track 2 measured-versus-predicted plot artifacts were requested, "
            f"but no readable PNG paths were found in `{format_relative_path(TRACK2_PLOT_SUMMARY_PATH)}`."
        )

    preferred_candidate_order = [
        "shape_objective_periodic_mlp_harmonic_Fw",
        "shape_objective_v3_periodic_gru_sequence_Fw",
        "shape_objective_curve_aware_residual_Fw",
        "polished_setpoints_periodic_mlp_harmonic_Fw",
        "polished_setpoints_periodic_gru_sequence_Fw",
    ]
    line_list = [
        "The following plots are bounded Track 2 TE curve overlays. The dark "
        "curve is measured TE and the colored curve is the candidate "
        "prediction, rendered on held-out `polished_dataset` setpoint `Fw` "
        "curves.",
    ]
    for candidate_id in preferred_candidate_order:
        candidate_plot_path_list = grouped_plot_path_dictionary.get(candidate_id, [])
        if not candidate_plot_path_list:
            continue
        if line_list[-1] != "":
            line_list.append("")
        line_list.extend([f"### {candidate_id}", ""])
        for plot_path in sorted(candidate_plot_path_list)[:2]:
            line_list.append(
                f"![{candidate_id} measured-versus-predicted TE curve]"
                f"({format_report_local_path(plot_path)})"
            )
            line_list.append("")

    return "\n".join(line_list).rstrip()


def plot_scalar_metric_summary(entry_list: list[dict[str, Any]], output_path: Path) -> None:
    """Plot validation and test MAE/RMSE for each pilot arm."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    label_list = [resolve_run_label(entry) for entry in entry_list]
    x_index_list = list(range(len(entry_list)))
    metric_pairs = [
        ("Validation MAE", [float(entry["val_mae"]) for entry in entry_list], "#2f6f9f"),
        ("Test MAE", [float(entry["test_mae"]) for entry in entry_list], "#d08c32"),
        ("Validation RMSE", [float(entry["val_rmse"]) for entry in entry_list], "#6a9f58"),
        ("Test RMSE", [float(entry["test_rmse"]) for entry in entry_list], "#9d4f5f"),
    ]

    figure, axis = plt.subplots(figsize=(8.4, 4.8), dpi=160)
    bar_width = 0.18
    for metric_index, (metric_label, metric_value_list, color) in enumerate(metric_pairs):
        offset = (metric_index - 1.5) * bar_width
        axis.bar(
            [x_value + offset for x_value in x_index_list],
            metric_value_list,
            width=bar_width,
            label=metric_label,
            color=color,
        )

    axis.set_ylabel("Error [deg]")
    axis.set_title("Pilot Scalar Metrics")
    axis.set_xticks(x_index_list)
    axis.set_xticklabels(label_list, rotation=12, ha="right")
    axis.grid(axis="y", alpha=0.25)
    axis.legend(ncols=2, frameon=False)
    figure.tight_layout()
    figure.savefig(output_path)
    plt.close(figure)


def plot_loss_breakdown(entry_list: list[dict[str, Any]], metrics_by_run_instance: dict[str, dict[str, Any]], output_path: Path) -> None:
    """Plot test loss components for each pilot arm."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    component_key_list = [
        "test_centered_curve_shape_loss",
        "test_curve_offset_loss",
        "test_curve_amplitude_loss",
        "test_sparse_harmonic_shape_loss",
    ]
    component_label_list = ["Centered shape", "Offset", "Amplitude", "Sparse harmonic"]
    color_list = ["#2f6f9f", "#d08c32", "#6a9f58", "#9d4f5f"]
    x_index_list = list(range(len(entry_list)))

    figure, axis = plt.subplots(figsize=(8.4, 4.8), dpi=160)
    bottom_list = [0.0 for _ in entry_list]

    for component_key, component_label, color in zip(component_key_list, component_label_list, color_list):
        value_list = []
        for entry in entry_list:
            metrics = metrics_by_run_instance[str(entry["run_instance_id"])]
            value_list.append(float(metrics["test_metrics"].get(component_key, 0.0)))

        axis.bar(x_index_list, value_list, bottom=bottom_list, label=component_label, color=color)
        bottom_list = [old_bottom + value for old_bottom, value in zip(bottom_list, value_list)]

    axis.set_ylabel("Loss component value")
    axis.set_title("Pilot Test Shape-Loss Breakdown")
    axis.set_xticks(x_index_list)
    axis.set_xticklabels([resolve_run_label(entry) for entry in entry_list], rotation=12, ha="right")
    axis.grid(axis="y", alpha=0.25)
    axis.legend(ncols=2, frameon=False)
    figure.tight_layout()
    figure.savefig(output_path)
    plt.close(figure)


def build_closeout_report() -> str:
    """Build the campaign closeout Markdown report."""

    leaderboard = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.yaml")
    best_run = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.yaml")["best_entry"]
    manifest = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_manifest.yaml")
    entry_list = list(leaderboard["entry_list"])
    metrics_by_run_instance = {str(entry["run_instance_id"]): load_run_metrics(entry) for entry in entry_list}
    best_metrics = metrics_by_run_instance[str(best_run["run_instance_id"])]

    completed_run_list = [run for run in manifest["run_list"] if str(run["queue_status"]) == "completed"]
    failed_run_list = [run for run in manifest["run_list"] if str(run["queue_status"]) != "completed"]
    started_at = str(completed_run_list[0]["start_time"])
    finished_at = str(completed_run_list[-1]["end_time"])

    scalar_graph_path = REPORT_ASSET_DIRECTORY / "pilot_scalar_metric_summary.png"
    loss_graph_path = REPORT_ASSET_DIRECTORY / "pilot_shape_loss_breakdown.png"
    plot_scalar_metric_summary(entry_list, scalar_graph_path)
    plot_loss_breakdown(entry_list, metrics_by_run_instance, loss_graph_path)

    gru_entry = next(entry for entry in entry_list if str(entry["model_family"]) == "shape_objective_v3_periodic_gru_sequence_fw")
    residual_entry = next(entry for entry in entry_list if str(entry["model_family"]) == "shape_objective_curve_aware_residual_fw")

    return f"""# Parallel Shape-Objective Follow-Up Campaign Results

## Overview

This report closes the approved `parallel_shape_objective_followup_2026_07_21`
pilot campaign. The campaign tested three `polished_dataset` setpoint `Fw`
arms after the prior shape-gate v2 branch failed bounded promotion:

- a windowed `periodic_gru_sequence` continuation with the stronger shape
  objective;
- a non-windowed `periodic_mlp_harmonic` arm;
- a curve-aware residual arm.

All three remote runs completed. The scalar campaign leader is
`{best_run['run_name']}` with test MAE `{format_metric(best_run['test_mae'])}`.
This is a pilot scalar result, not an official promotion. Promotion still
requires the bounded `TE Curve Verification Pipeline` shape-first screen
against both windowed and non-windowed references.

## Campaign Artifacts

{build_artifact_table()}

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `{CAMPAIGN_NAME}` |
| Started at | `{started_at}` |
| Finished at | `{finished_at}` |
| Completed runs | {len(completed_run_list)} |
| Failed runs | {len(failed_run_list)} |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| Surface | `Fw` |
| Remote sync note | Manual sync recovery was required after the local SSH wrapper became stale post-training. |

## Campaign Winner

| Field | Value |
| --- | --- |
| Run name | `{best_run['run_name']}` |
| Run instance | `{best_run['run_instance_id']}` |
| Model family | `{best_run['model_family']}` |
| Model type | `{best_run['model_type']}` |
| Runtime contract | non-windowed pointwise setpoint model |
| Trainable parameters | {int(best_run['trainable_parameter_count']):,} |
| Validation MAE | {format_metric(best_run['val_mae'])} |
| Validation RMSE | {format_metric(best_run['val_rmse'])} |
| Test MAE | {format_metric(best_run['test_mae'])} |
| Test RMSE | {format_metric(best_run['test_rmse'])} |

The winning checkpoint is stored at
`{format_relative_path(best_run['best_checkpoint_path'])}`.

## Pilot Comparison

{build_pilot_comparison_table(entry_list)}

The non-windowed MLP arm has scalar test MAE
{format_improvement_phrase(best_run['test_mae'], gru_entry['test_mae'])} than
the windowed GRU continuation and
{format_improvement_phrase(best_run['test_mae'], residual_entry['test_mae'])}
than the curve-aware residual arm. This answers the branch question directly:
the best result in this pilot is not the time-windowed GRU branch.

## Metric Breakdown

{build_metric_breakdown_table(best_metrics)}

## Pilot Graphs

### Track 2 Measured-Versus-Predicted Curves

{build_track2_curve_plot_section()}

### Secondary Scalar Diagnostics

![Pilot scalar metric summary]({format_report_local_path(scalar_graph_path)})

![Pilot shape loss breakdown]({format_report_local_path(loss_graph_path)})

## Technical Interpretation

The scalar outcome rejects further investment in the v3 windowed GRU branch as
the immediate next candidate. It improved enough to remain informative, but the
non-windowed MLP produced lower validation MAE, lower test MAE, lower test
RMSE, and lower centered curve-shape loss in this pilot.

The curve-aware residual branch recovered from a poor first epoch but finished
behind both leading neural candidates on scalar error. Its structured residual
diagnostics remain useful for understanding offset behavior, but it should not
be expanded before a stronger scalar or curve-screen signal appears.

The practical next step is a bounded shape-gated `TE Curve Verification
Pipeline` screen for the non-windowed MLP winner, comparing it explicitly
against the current windowed forward reference and the best non-windowed
forward reference. Do not promote from this campaign leaderboard alone.

## Closeout Decision

The campaign is closed as a successful pilot with no training failures. The
recommended candidate for the next bounded curve-first screen is
`shape_objective_periodic_mlp_harmonic_fw`. The windowed GRU continuation and
curve-aware residual arms should remain as negative/secondary evidence unless
the curve screen contradicts the scalar ranking.
"""


def update_active_campaign_state() -> None:
    """Update the active campaign state after successful closeout."""

    active_state = load_yaml_dictionary(ACTIVE_CAMPAIGN_STATE_PATH)
    active_state["status"] = "completed"
    active_state["completed_at"] = "2026-07-21T19:31:21+02:00"
    active_state["closeout_report_path"] = format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH)
    active_state["pilot_graph_bundle_path"] = format_relative_path(TRACK2_PLOT_ROOT)
    active_state["secondary_scalar_graph_bundle_path"] = format_relative_path(REPORT_ASSET_DIRECTORY)
    active_state["track2_pilot_plot_config_path"] = format_relative_path(TRACK2_PLOT_CONFIG_PATH)
    active_state["track2_pilot_plot_summary_path"] = format_relative_path(TRACK2_PLOT_SUMMARY_PATH)
    active_state["recommended_next_step"] = "Run bounded TE Curve Verification Pipeline screen for shape_objective_periodic_mlp_harmonic_fw before any promotion."
    active_state["protected_file_list"] = []
    active_state["monitoring"] = {
        "last_checked_at": "2026-07-21T19:31:21+02:00",
        "remote_status": "completed",
        "remote_stage": "completed_with_manual_sync_recovery",
        "current_queue_state": {
            "running": [],
            "pending": [],
            "completed": [
                "2026-07-21-18-52-44__te_shape_objective_v3_periodic_gru_sequence_fw__polished_setpoints",
                "2026-07-21-19-02-58__te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints",
                "2026-07-21-19-12-09__te_shape_objective_curve_aware_residual_fw__polished_setpoints",
            ],
            "failed": [],
        },
        "remote_campaign_output_directory": "C:\\Users\\Martina Salami\\Documents\\Davide\\Physics-Informed-Neural-Networks\\output\\training_campaigns\\2026-07-21-18-52-44_parallel_shape_objective_followup_2026_07_21",
        "latest_observation": "Campaign completed; non-windowed periodic MLP harmonic arm is the scalar pilot leader and requires bounded curve-first screening before promotion.",
    }
    write_yaml_dictionary(ACTIVE_CAMPAIGN_STATE_PATH, active_state)


def update_doc_index() -> None:
    """Register the campaign-results report from the canonical doc index."""

    index_text = DOC_INDEX_PATH.read_text(encoding="utf-8")
    report_relative_path = str(CAMPAIGN_RESULTS_REPORT_PATH.resolve().relative_to(DOC_INDEX_PATH.parent)).replace("\\", "/")
    plot_summary_relative_path = str(TRACK2_PLOT_SUMMARY_PATH.resolve().relative_to(DOC_INDEX_PATH.parent)).replace("\\", "/")
    entry_text_list = [
        (
            f"- [Parallel Shape-Objective Follow-Up Campaign Results]({report_relative_path})",
            "  Final results report for the completed three-arm shape-objective "
            "follow-up campaign, including Track 2 measured-versus-predicted "
            "pilot curve plots.",
        ),
        (
            f"- [Parallel Shape-Objective Follow-Up Track 2 Curve Plot Summary]({plot_summary_relative_path})",
            "  Manifest for the bounded Track 2 measured-versus-predicted TE "
            "curve plots generated for the shape-objective follow-up pilot.",
        ),
    ]
    missing_entry_text_list = [
        f"{index_line}\n{description_line}"
        for index_line, description_line in entry_text_list
        if index_line not in index_text
    ]
    if not missing_entry_text_list:
        return

    marker = "## Reports\n"
    insertion_text = "\n".join(missing_entry_text_list)
    if marker in index_text:
        index_text = index_text.replace(marker, f"{marker}\n{insertion_text}\n", 1)
    else:
        index_text = f"{index_text.rstrip()}\n\n## Reports\n\n{insertion_text}\n"
    write_text_file(DOC_INDEX_PATH, index_text)


def main() -> None:
    """Run the campaign closeout workflow."""

    report_text = build_closeout_report()
    write_text_file(CAMPAIGN_RESULTS_REPORT_PATH, report_text)
    update_active_campaign_state()
    update_doc_index()
    print(f"[DONE] Wrote campaign closeout report: {format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH)}")
    print(f"[DONE] Wrote pilot graph bundle: {format_relative_path(REPORT_ASSET_DIRECTORY)}")


if __name__ == "__main__":
    main()
