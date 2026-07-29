"""Build the Wave 5.2R Stage 7 mean and centered-shape closeout."""

from __future__ import annotations

# Import Python Utilities
import csv
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Plotting And Numerical Utilities
import matplotlib
import numpy as np
import yaml

matplotlib.use("Agg")
from matplotlib import pyplot as plt  # noqa: E402


# Define Canonical Paths
PROJECT_ROOT = Path(__file__).resolve().parents[4]
CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_campaigns"
    / "2026-07-29-17-46-21_wave52r_stage7_mean_centered_shape_"
    "multi_head_2026_07_29"
)
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage7_mean_centered_shape_multi_head"
    / "closeout"
)
REPORT_PATH = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "2026-07-29-17-47-24_wave52r_stage7_mean_centered_shape_"
    "multi_head_results_report.md"
)
ASSET_DIRECTORY = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "assets"
    / "2026-07-29_stage7_mean_centered_shape_multi_head"
)
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def load_leaderboard() -> list[dict[str, Any]]:
    """Load and convert the Stage 7 leaderboard."""

    numeric_field_set = {
        "mae_deg",
        "mean_mae_deg",
        "centered_shape_mae_deg",
        "sobolev_derivative_mae",
        "periodic_closure_error_deg",
        "retained_amplitude_mae_deg",
        "retained_phase_mae_rad",
        "per_curve_mae_p95",
        "parameter_count",
        "negative_gradient_conflict_fraction",
        "shape_cycle_mean_max_abs_deg",
        "reconstruction_identity_max_abs_deg",
    }
    with (
        CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.csv"
    ).open("r", encoding="utf-8-sig", newline="") as input_file:
        row_list = list(csv.DictReader(input_file))
    for row in row_list:
        for field_name in numeric_field_set:
            row[field_name] = float(row[field_name])
    return row_list


def improvement_percent(candidate_value: float, baseline_value: float) -> float:
    """Return positive improvement for one minimized metric."""

    return 100.0 * (baseline_value - candidate_value) / baseline_value


def build_multi_index_plot(
    baseline_metrics: dict[str, float],
    candidate_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot normalized Stage 7 multi-index behavior."""

    metric_name_list = [
        "mae_deg",
        "mean_mae_deg",
        "centered_shape_mae_deg",
        "sobolev_derivative_mae",
        "retained_amplitude_mae_deg",
        "per_curve_mae_p95",
    ]
    display_name_list = [
        "Raw",
        "Mean",
        "Shape",
        "Derivative",
        "Amplitude",
        "P95",
    ]
    candidate_id_list = ["C01", "I01", "S01", "P01"]
    color_list = ["#005A9C", "#2E8B57", "#D97706", "#8B5CF6"]
    x_position = np.arange(len(metric_name_list))
    width = 0.19
    figure, axis = plt.subplots(figsize=(11.3, 5.7))
    for candidate_index, candidate_id in enumerate(candidate_id_list):
        normalized_value_list = [
            candidate_map[candidate_id][metric_name]
            / baseline_metrics[metric_name]
            for metric_name in metric_name_list
        ]
        axis.bar(
            x_position + (candidate_index - 1.5) * width,
            normalized_value_list,
            width,
            color=color_list[candidate_index],
            label=candidate_id,
        )
    axis.axhline(
        1.0,
        color="#202020",
        linewidth=1.2,
        linestyle="--",
        label="Frozen H04",
    )
    axis.set_xticks(x_position)
    axis.set_xticklabels(display_name_list)
    axis.set_ylabel("Normalized error (lower is better)")
    axis.set_title("Stage 7 Multi-Index Comparison")
    axis.set_ylim(0.96, 1.12)
    axis.grid(axis="y", alpha=0.25)
    axis.legend(ncol=5, loc="upper center", fontsize=8)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage7_multi_index_comparison.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_mean_shape_tradeoff_plot(
    baseline_metrics: dict[str, float],
    leaderboard_row_list: list[dict[str, Any]],
) -> Path:
    """Plot the explicit mean-versus-shape tradeoff."""

    figure, axis = plt.subplots(figsize=(8.4, 6.2))
    axis.axvline(1.0, color="#202020", linewidth=1.0, linestyle="--")
    axis.axhline(1.0, color="#202020", linewidth=1.0, linestyle="--")
    annotation_offset_map = {
        "C01": (6, -12),
        "I01": (6, 5),
        "A02": (6, -12),
        "G01": (6, 6),
        "S01": (-24, -12),
        "P01": (6, 6),
        "A01": (6, -12),
    }
    for row in leaderboard_row_list:
        mean_ratio = (
            row["mean_mae_deg"] / baseline_metrics["mean_mae_deg"]
        )
        shape_ratio = (
            row["centered_shape_mae_deg"]
            / baseline_metrics["centered_shape_mae_deg"]
        )
        color = (
            "#005A9C"
            if row["candidate_id"] in {"S01", "P01", "G01"}
            else "#6B7280"
        )
        axis.scatter(mean_ratio, shape_ratio, color=color, s=58)
        axis.annotate(
            row["candidate_id"],
            (mean_ratio, shape_ratio),
            xytext=annotation_offset_map[row["candidate_id"]],
            textcoords="offset points",
            fontsize=8,
        )
    axis.set_xlabel("Mean MAE / frozen H04")
    axis.set_ylabel("Centered-shape MAE / frozen H04")
    axis.set_title("Mean And Centered-Shape Tradeoff")
    axis.grid(alpha=0.25)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage7_mean_shape_tradeoff.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_gradient_conflict_plot(
    leaderboard_row_list: list[dict[str, Any]],
) -> Path:
    """Plot observed mean-versus-shape conflict frequency."""

    sorted_row_list = sorted(
        leaderboard_row_list,
        key=lambda row: row["candidate_id"],
    )
    candidate_id_list = [
        row["candidate_id"] for row in sorted_row_list
    ]
    conflict_percent_array = 100.0 * np.asarray(
        [
            row["negative_gradient_conflict_fraction"]
            for row in sorted_row_list
        ]
    )
    color_list = [
        "#005A9C" if candidate_id == "C01" else "#8B9AA8"
        for candidate_id in candidate_id_list
    ]
    figure, axis = plt.subplots(figsize=(9.2, 4.8))
    axis.bar(
        candidate_id_list,
        conflict_percent_array,
        color=color_list,
    )
    axis.set_ylabel("Epochs with negative cosine [%]")
    axis.set_title("Observed Mean-Shape Gradient Conflict")
    axis.set_ylim(0.0, 105.0)
    axis.grid(axis="y", alpha=0.25)
    for index, value in enumerate(conflict_percent_array):
        axis.text(
            index,
            value + 2.0,
            f"{value:.1f}%",
            ha="center",
            fontsize=8,
        )
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage7_gradient_conflict.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_representative_curve_plot(
    candidate_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot representative C01 component reconstructions."""

    prediction_path = (
        PROJECT_ROOT
        / candidate_map["C01"]["checkpoint_path"]
    ).parent / "test_predictions.npz"
    with np.load(prediction_path) as payload:
        measured_curve_matrix = payload["measured_curve"]
        predicted_curve_matrix = payload["predicted_curve"]
        analytical_curve_matrix = payload["analytical_curve"]
        predicted_mean_array = payload["predicted_mean"]
        condition_id_array = payload["condition_id"]
    per_curve_mae_array = np.mean(
        np.abs(predicted_curve_matrix - measured_curve_matrix),
        axis=1,
    )
    ordered_index_array = np.argsort(per_curve_mae_array)
    selected_index_list = [
        int(ordered_index_array[len(ordered_index_array) // 4]),
        int(ordered_index_array[len(ordered_index_array) // 2]),
        int(ordered_index_array[-1]),
    ]
    angle_array = np.linspace(
        0.0,
        360.0,
        predicted_curve_matrix.shape[1],
        endpoint=False,
    )
    figure, axis_array = plt.subplots(3, 1, figsize=(11.2, 8.1), sharex=True)
    for axis, curve_index in zip(
        axis_array,
        selected_index_list,
        strict=True,
    ):
        axis.plot(
            angle_array,
            measured_curve_matrix[curve_index],
            color="#111827",
            linewidth=1.1,
            label="Measured",
        )
        axis.plot(
            angle_array,
            analytical_curve_matrix[curve_index],
            color="#D97706",
            linewidth=1.0,
            label="PF-A",
        )
        axis.plot(
            angle_array,
            predicted_curve_matrix[curve_index],
            color="#005A9C",
            linewidth=1.0,
            label="C01",
        )
        axis.axhline(
            float(predicted_mean_array[curve_index, 0]),
            color="#2E8B57",
            linewidth=0.9,
            linestyle="--",
            label="Predicted mean",
        )
        axis.set_title(
            f"{condition_id_array[curve_index]} | "
            f"C01 MAE {per_curve_mae_array[curve_index]:.6f} deg",
            fontsize=9,
        )
        axis.set_ylabel("TE [deg]")
        axis.grid(alpha=0.2)
    axis_array[0].legend(ncol=4, fontsize=8)
    axis_array[-1].set_xlabel("Angular position [deg]")
    figure.suptitle("Representative Stage 7 C01 Reconstructions")
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage7_c01_representative_curves.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_gate_table(gate_payload: dict[str, Any]) -> str:
    """Render the compact shared-candidate gate matrix."""

    line_list = [
        "| ID | Raw | Mean | Shape | Deriv. | Harm. | P95 | Shared | "
        "Invariant | Final |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in gate_payload["gate_row_list"]:
        value_list = [
            row["raw_mae_preserved"],
            row["mean_mae_improved"],
            row["centered_shape_improved"],
            row["derivative_preserved"],
            (
                row["amplitude_preserved"]
                and row["phase_preserved"]
                and row["closure_preserved"]
            ),
            row["p95_preserved"],
            row["shared_advantage_passed"],
            (
                row["shape_invariant_passed"]
                and row["reconstruction_invariant_passed"]
            ),
        ]
        rendered_value_list = [
            "pass" if value else "fail" for value in value_list
        ]
        final_result = (
            "pass"
            if row["all_first_screen_gates_passed"]
            else "fail"
        )
        line_list.append(
            f"| {row['candidate_id']} | "
            + " | ".join(rendered_value_list)
            + f" | {final_result} |"
        )
    return "\n".join(line_list)


def main() -> None:
    """Build Stage 7 decisions, figures, report, and state."""

    leaderboard_row_list = load_leaderboard()
    candidate_map = {
        row["candidate_id"]: row for row in leaderboard_row_list
    }
    gate_payload = load_yaml(
        CAMPAIGN_OUTPUT_DIRECTORY
        / "campaign_first_screen_gate_summary.yaml"
    )
    preflight_payload = load_yaml(
        PROJECT_ROOT
        / "output"
        / "analysis"
        / "wave_5_2r"
        / "stage7_mean_centered_shape_multi_head"
        / "stage7_preflight_validation_summary.yaml"
    )
    baseline_metrics = gate_payload["baseline_metrics"]
    assert len(leaderboard_row_list) == 7
    assert gate_payload["passing_candidate_id_list"] == []
    assert preflight_payload["all_checks_passed"] is True

    multi_index_plot_path = build_multi_index_plot(
        baseline_metrics,
        candidate_map,
    )
    tradeoff_plot_path = build_mean_shape_tradeoff_plot(
        baseline_metrics,
        leaderboard_row_list,
    )
    conflict_plot_path = build_gradient_conflict_plot(
        leaderboard_row_list
    )
    representative_plot_path = build_representative_curve_plot(candidate_map)

    c01_raw_improvement = improvement_percent(
        candidate_map["C01"]["mae_deg"],
        baseline_metrics["mae_deg"],
    )
    c01_mean_improvement = improvement_percent(
        candidate_map["C01"]["mean_mae_deg"],
        baseline_metrics["mean_mae_deg"],
    )
    c01_shape_improvement = improvement_percent(
        candidate_map["C01"]["centered_shape_mae_deg"],
        baseline_metrics["centered_shape_mae_deg"],
    )
    summary_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage7",
        "status": "completed_negative_result",
        "closed_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "first_screen_run_count": 7,
        "stability_run_count": 0,
        "failed_run_count": 0,
        "raw_error_leader": "C01",
        "raw_error_leader_mae_deg": candidate_map["C01"]["mae_deg"],
        "raw_error_improvement_vs_frozen_h04_percent": (
            c01_raw_improvement
        ),
        "multi_index_recommended_candidate": None,
        "all_exit_gates_passed": False,
        "failed_decision_reason": (
            "no shared or partially shared formulation improved both mean "
            "and centered shape while preserving the complete curve gate"
        ),
        "c01_disposition": (
            "monolithic fine-tuning control only; raw and mean gains do not "
            "qualify because centered shape did not improve"
        ),
        "stage5_h04_disposition": (
            "retained as the qualified structured component entering Stage 8"
        ),
        "official_te_curve_verification_pipeline_run": False,
        "next_stage": "Stage 8 Weak Forward Compliance Priors",
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage7_exit_gate_summary.yaml",
        summary_payload,
    )

    report_text = f"""# Wave 5.2R Stage 7 Mean And Centered-Shape Multi-Head Results

## Executive Decision

Stage 7 is complete as a valid negative result.

All `7 / 7` first-screen runs completed without failure. No shared or partially
shared candidate passed the complete multi-index gate, so the conditional
stability continuation was correctly skipped.

C01, the monolithic H04 fine-tuning control, is the raw-error leader at
`{candidate_map["C01"]["mae_deg"]:.9f} deg`. It improves raw MAE by
`{c01_raw_improvement:.2f}%` and mean MAE by `{c01_mean_improvement:.2f}%`
relative to frozen H04, but centered-shape MAE changes by
`{c01_shape_improvement:+.2f}%`. C01 is not a multi-head candidate and does not
qualify for promotion.

Stage 5 H04 remains the qualified structured component entering Stage 8. No
Stage 7 model replaces the accepted periodic GRU or becomes a production
candidate.

## Scope And Integrity

- dataset: `polished_dataset`;
- input contract: setpoints only;
- surface: `Fw`;
- accepted curves: `966`;
- split: `675` train, `194` validation, `97` test;
- angular grid: `2048` uniform points;
- split signature:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- first-screen seed: `314159`;
- completed runs: `7 / 7`;
- target-derived runtime inputs: none;
- official TE Curve Verification Pipeline: not run.

Every candidate satisfies exact decomposition invariants. Maximum observed
centered-shape mean is below `3.4e-10 deg`, and reconstruction identity error
is exactly zero on the test split.

## Candidate Matrix

| ID | Architecture | Parameters | Relative to I01 | Role |
| --- | --- | ---: | ---: | --- |
| C01 | monolithic H04 | {int(candidate_map["C01"]["parameter_count"])} | {candidate_map["C01"]["parameter_count"] / candidate_map["I01"]["parameter_count"]:.3f} | fine-tuning control |
| S01 | fully shared heads | {int(candidate_map["S01"]["parameter_count"])} | {candidate_map["S01"]["parameter_count"] / candidate_map["I01"]["parameter_count"]:.3f} | promotion candidate |
| P01 | partially shared | {int(candidate_map["P01"]["parameter_count"])} | {candidate_map["P01"]["parameter_count"] / candidate_map["I01"]["parameter_count"]:.3f} | promotion candidate |
| I01 | independent heads | {int(candidate_map["I01"]["parameter_count"])} | 1.000 | matched control |
| G01 | shared plus projection | {int(candidate_map["G01"]["parameter_count"])} | {candidate_map["G01"]["parameter_count"] / candidate_map["I01"]["parameter_count"]:.3f} | promotion candidate |
| A01 | analytical mean | {int(candidate_map["A01"]["parameter_count"])} | {candidate_map["A01"]["parameter_count"] / candidate_map["I01"]["parameter_count"]:.3f} | ablation |
| A02 | analytical shape | {int(candidate_map["A02"]["parameter_count"])} | {candidate_map["A02"]["parameter_count"] / candidate_map["I01"]["parameter_count"]:.3f} | ablation |

## Primary Results

| ID | Raw [deg] | Mean [deg] | Shape [deg] | D-MAE | Phase [rad] | P95 [deg] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Frozen H04 | {baseline_metrics["mae_deg"]:.7f} | {baseline_metrics["mean_mae_deg"]:.7f} | {baseline_metrics["centered_shape_mae_deg"]:.7f} | {baseline_metrics["sobolev_derivative_mae"]:.7f} | {baseline_metrics["retained_phase_mae_rad"]:.7f} | {baseline_metrics["per_curve_mae_p95"]:.7f} |
| C01 | {candidate_map["C01"]["mae_deg"]:.7f} | {candidate_map["C01"]["mean_mae_deg"]:.7f} | {candidate_map["C01"]["centered_shape_mae_deg"]:.7f} | {candidate_map["C01"]["sobolev_derivative_mae"]:.7f} | {candidate_map["C01"]["retained_phase_mae_rad"]:.7f} | {candidate_map["C01"]["per_curve_mae_p95"]:.7f} |
| I01 | {candidate_map["I01"]["mae_deg"]:.7f} | {candidate_map["I01"]["mean_mae_deg"]:.7f} | {candidate_map["I01"]["centered_shape_mae_deg"]:.7f} | {candidate_map["I01"]["sobolev_derivative_mae"]:.7f} | {candidate_map["I01"]["retained_phase_mae_rad"]:.7f} | {candidate_map["I01"]["per_curve_mae_p95"]:.7f} |
| S01 | {candidate_map["S01"]["mae_deg"]:.7f} | {candidate_map["S01"]["mean_mae_deg"]:.7f} | {candidate_map["S01"]["centered_shape_mae_deg"]:.7f} | {candidate_map["S01"]["sobolev_derivative_mae"]:.7f} | {candidate_map["S01"]["retained_phase_mae_rad"]:.7f} | {candidate_map["S01"]["per_curve_mae_p95"]:.7f} |
| P01 | {candidate_map["P01"]["mae_deg"]:.7f} | {candidate_map["P01"]["mean_mae_deg"]:.7f} | {candidate_map["P01"]["centered_shape_mae_deg"]:.7f} | {candidate_map["P01"]["sobolev_derivative_mae"]:.7f} | {candidate_map["P01"]["retained_phase_mae_rad"]:.7f} | {candidate_map["P01"]["per_curve_mae_p95"]:.7f} |
| G01 | {candidate_map["G01"]["mae_deg"]:.7f} | {candidate_map["G01"]["mean_mae_deg"]:.7f} | {candidate_map["G01"]["centered_shape_mae_deg"]:.7f} | {candidate_map["G01"]["sobolev_derivative_mae"]:.7f} | {candidate_map["G01"]["retained_phase_mae_rad"]:.7f} | {candidate_map["G01"]["per_curve_mae_p95"]:.7f} |

![Stage 7 multi-index comparison](assets/2026-07-29_stage7_mean_centered_shape_multi_head/{multi_index_plot_path.name})

## Gate Matrix

{build_gate_table(gate_payload)}

No shared formulation passes any predictive improvement gate. The structural
invariants pass for all candidates.

## What Worked

- the mean-plus-shape reconstruction is exact and numerically stable;
- S01 uses `60.1%` and P01 uses `75.3%` of I01 parameters;
- C01 shows that continued bounded H04 optimization can improve raw and mean
  error while preserving closure, amplitude, phase, and P95;
- the campaign directly measures mean-shape gradient conflict;
- the analytical ablations localize the need to learn both components.

## What Did Not Work

- S01, P01, and G01 worsen raw, mean, shape, derivative, harmonic, and P95
  behavior relative to frozen H04;
- the parameter savings do not compensate for their predictive regression;
- I01 is the closest balanced decomposition but does not achieve the required
  mean and shape gains despite using the most parameters;
- A01 shows that a frozen analytical mean is insufficient;
- A02 shows that learning only the mean does not preserve the qualified shape;
- no candidate earns stability continuation or promotion.

## Mean And Shape Tradeoff

The lower-left quadrant improves both explicit quantities. C01 improves the
mean but sits slightly above the frozen shape baseline. Every multi-head
candidate remains outside the required improvement region.

![Mean and shape tradeoff](assets/2026-07-29_stage7_mean_centered_shape_multi_head/{tradeoff_plot_path.name})

## Gradient Conflict

C01 records negative mean-versus-shape cosine in
`{100.0 * candidate_map["C01"]["negative_gradient_conflict_fraction"]:.1f}%`
of epochs. In the explicit shared-head models the measured shared gradient
cosine is non-negative, so G01's projection is never activated and G01 is
numerically equivalent to S01. This explains why gradient surgery does not
recover performance in this screen.

![Mean-shape gradient conflict](assets/2026-07-29_stage7_mean_centered_shape_multi_head/{conflict_plot_path.name})

## Representative Full Curves

C01 remains close to frozen H04 and improves the mean component, but its worst
cell still exposes unresolved high-order shape error.

![Representative C01 curves](assets/2026-07-29_stage7_mean_centered_shape_multi_head/{representative_plot_path.name})

## Scientific Interpretation

Exact decomposition improves interpretability but does not by itself add
predictive information. The current dataset and bounded coefficient target
allow the monolithic model to trade mean against small shape changes more
effectively than the explicit multi-head models.

The result also distinguishes architectural conflict from gradient conflict.
C01 exhibits frequent negative cosine, while explicit shared heads do not.
Their failure therefore cannot be repaired by conflict projection alone; the
shared representation and optimization path are the limiting factors in this
screen.

Stage 8 returns to a weaker, mechanism-specific hypothesis: forward compliance
priors. It will start with diagnostics and sign-only or broad-bound constraints
rather than a hard equation.

## Program Decision

- Stage 7 status: complete, valid negative result;
- completed runs: `7 / 7`;
- stability runs: `0`, correctly skipped;
- raw-error leader: C01 monolithic control;
- promoted Stage 7 candidate: none;
- retained component: Stage 5 H04;
- production or registry promotion: no;
- next step: Stage 8, Weak Forward Compliance Priors.

## Artifact Map

- campaign:
  `output/training_campaigns/2026-07-29-17-46-21_wave52r_stage7_mean_centered_shape_multi_head_2026_07_29/`;
- gate summary:
  `output/analysis/wave_5_2r/stage7_mean_centered_shape_multi_head/closeout/stage7_exit_gate_summary.yaml`;
- preflight:
  `output/analysis/wave_5_2r/stage7_mean_centered_shape_multi_head/stage7_preflight_validation_summary.yaml`;
- C01 checkpoint:
  `{candidate_map["C01"]["checkpoint_path"]}`;
- model report:
  `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-29]/stage7_mean_centered_shape_multi_head/stage7_mean_centered_shape_multi_head_model_report.md`.
"""
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_PATH.open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(report_text.rstrip() + "\n")

    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "status": "completed",
            "closed_out_at": datetime.now().astimezone().isoformat(
                timespec="seconds"
            ),
            "recommended_candidate_id": None,
            "scalar_raw_error_leader_id": "C01",
            "stage_decision": "completed_negative_result",
            "exit_gate_summary_path": (
                ANALYSIS_DIRECTORY / "stage7_exit_gate_summary.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
            "campaign_results_report_path": REPORT_PATH.relative_to(
                PROJECT_ROOT
            ).as_posix(),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    print(yaml.safe_dump(summary_payload, sort_keys=False))


if __name__ == "__main__":
    main()
