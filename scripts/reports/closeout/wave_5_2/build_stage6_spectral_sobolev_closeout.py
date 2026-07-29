"""Build the Wave 5.2R Stage 6 spectral and Sobolev closeout."""

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
    / "2026-07-29-15-34-05_wave52r_stage6_spectral_sobolev_"
    "guidance_2026_07_29"
)
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage6_spectral_sobolev_guidance"
    / "closeout"
)
REPORT_PATH = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "2026-07-29-15-35-41_wave52r_stage6_spectral_sobolev_"
    "guidance_results_report.md"
)
ASSET_DIRECTORY = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "assets"
    / "2026-07-29_stage6_spectral_sobolev_guidance"
)
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML mapping: {path}"
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
    """Load and convert the campaign leaderboard."""

    numeric_field_set = {
        "mae_deg",
        "centered_mae_deg",
        "offset_abs_error_deg",
        "periodic_closure_error_deg",
        "retained_amplitude_mae_deg",
        "retained_phase_mae_rad",
        "sobolev_derivative_mae",
        "sobolev_derivative_correlation",
        "per_curve_mae_p95",
        "unsupported_high_frequency_energy_ratio",
    }
    leaderboard_path = CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.csv"
    with leaderboard_path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as input_file:
        row_list = list(csv.DictReader(input_file))
    for row in row_list:
        for field_name in numeric_field_set:
            row[field_name] = float(row[field_name])
    return row_list


def improvement_percent(candidate_value: float, baseline_value: float) -> float:
    """Return positive percent improvement for one minimized metric."""

    return 100.0 * (baseline_value - candidate_value) / baseline_value


def build_multi_index_plot(
    baseline_metrics: dict[str, float],
    candidate_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot normalized Stage 6 multi-index behavior."""

    metric_name_list = [
        "mae_deg",
        "centered_mae_deg",
        "offset_abs_error_deg",
        "sobolev_derivative_mae",
        "retained_amplitude_mae_deg",
        "retained_phase_mae_rad",
        "per_curve_mae_p95",
    ]
    display_name_list = [
        "Raw",
        "Centered",
        "Offset",
        "Derivative",
        "Amplitude",
        "Phase",
        "P95",
    ]
    candidate_id_list = ["FI01", "D01", "W01", "FF01"]
    color_list = ["#005A9C", "#2E8B57", "#D97706", "#8B5CF6"]
    x_position = np.arange(len(metric_name_list))
    width = 0.19
    figure, axis = plt.subplots(figsize=(11.4, 5.7))
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
        label="Stage 5 H04",
    )
    axis.set_xticks(x_position)
    axis.set_xticklabels(display_name_list)
    axis.set_ylabel("Normalized error (lower is better)")
    axis.set_title("Stage 6 Multi-Index Comparison")
    axis.set_ylim(0.94, 1.08)
    axis.grid(axis="y", alpha=0.25)
    axis.legend(ncol=5, loc="upper center", fontsize=8)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage6_multi_index_comparison.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_guidance_tradeoff_plot(
    baseline_metrics: dict[str, float],
    candidate_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot raw and derivative tradeoffs for eligible guidance arms."""

    candidate_id_list = [
        "D01",
        "DS01",
        "CU01",
        "FI01",
        "W01",
        "S02",
        "DS02",
        "FF01",
        "SI01",
    ]
    raw_ratio_array = np.asarray(
        [
            candidate_map[candidate_id]["mae_deg"]
            / baseline_metrics["mae_deg"]
            for candidate_id in candidate_id_list
        ]
    )
    derivative_ratio_array = np.asarray(
        [
            candidate_map[candidate_id]["sobolev_derivative_mae"]
            / baseline_metrics["sobolev_derivative_mae"]
            for candidate_id in candidate_id_list
        ]
    )
    figure, axis = plt.subplots(figsize=(8.4, 6.2))
    axis.axvline(1.0, color="#202020", linewidth=1.0, linestyle="--")
    axis.axhline(1.0, color="#202020", linewidth=1.0, linestyle="--")
    axis.scatter(
        raw_ratio_array,
        derivative_ratio_array,
        color="#005A9C",
        s=58,
    )
    annotation_offset_map = {
        "D01": (5, -12),
        "DS01": (5, 10),
        "CU01": (5, 19),
        "FI01": (5, -20),
        "W01": (5, 5),
        "S02": (5, 9),
        "DS02": (5, -11),
        "FF01": (5, 6),
        "SI01": (5, -10),
    }
    for candidate_id, x_value, y_value in zip(
        candidate_id_list,
        raw_ratio_array,
        derivative_ratio_array,
        strict=True,
    ):
        axis.annotate(
            candidate_id,
            (x_value, y_value),
            xytext=annotation_offset_map[candidate_id],
            textcoords="offset points",
            fontsize=8,
        )
    axis.set_xlabel("Raw MAE / Stage 5 H04")
    axis.set_ylabel("Sobolev derivative MAE / Stage 5 H04")
    axis.set_title("Raw-Error And Derivative Tradeoff")
    axis.grid(alpha=0.25)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage6_guidance_tradeoff.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_representative_curve_plot(
    candidate_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot representative test curves for the raw-error leader."""

    prediction_path = (
        PROJECT_ROOT
        / candidate_map["FI01"]["checkpoint_path"]
    ).parent / "test_predictions.npz"
    with np.load(prediction_path) as payload:
        measured_curve_matrix = payload["measured_curve"]
        predicted_curve_matrix = payload["predicted_curve"]
        analytical_curve_matrix = payload["analytical_curve"]
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
        measured_curve_matrix.shape[1],
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
            linewidth=1.2,
            label="Measured",
        )
        axis.plot(
            angle_array,
            analytical_curve_matrix[curve_index],
            color="#D97706",
            linewidth=1.0,
            label="Stage 5 H04 anchor",
        )
        axis.plot(
            angle_array,
            predicted_curve_matrix[curve_index],
            color="#005A9C",
            linewidth=1.0,
            label="Stage 6 FI01",
        )
        axis.set_title(
            f"{condition_id_array[curve_index]} | "
            f"FI01 MAE {per_curve_mae_array[curve_index]:.6f} deg",
            fontsize=9,
        )
        axis.set_ylabel("TE [deg]")
        axis.grid(alpha=0.2)
    axis_array[0].legend(ncol=3, fontsize=8)
    axis_array[-1].set_xlabel("Angular position [deg]")
    figure.suptitle("Representative Stage 6 Full-Curve Predictions")
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage6_fi01_representative_curves.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_gate_table(gate_payload: dict[str, Any]) -> str:
    """Render the first-screen gate matrix."""

    line_list = [
        "| Candidate | Raw | Centered | Offset | D-MAE | D-corr. | "
        "Amp. | Phase | P95 | Ctrl. | Final |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in gate_payload["gate_row_list"]:
        value_list = [
            row["raw_mae_preserved"],
            row["centered_mae_preserved"],
            row["offset_preserved"],
            row["derivative_mae_improved"],
            row["derivative_correlation_improved"],
            row["harmonic_amplitude_improved"],
            row["harmonic_phase_improved"],
            row["p95_improved"],
            row["matched_control_beaten"],
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
    """Build plots, decision artifacts, report, and persistent state."""

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
        / "stage6_spectral_sobolev_guidance"
        / "stage6_preflight_validation_summary.yaml"
    )
    baseline_metrics = gate_payload["baseline_metrics"]
    assert gate_payload["passing_candidate_id_list"] == []
    assert preflight_payload["all_checks_passed"] is True
    assert len(leaderboard_row_list) == 15

    multi_index_plot_path = build_multi_index_plot(
        baseline_metrics,
        candidate_map,
    )
    tradeoff_plot_path = build_guidance_tradeoff_plot(
        baseline_metrics,
        candidate_map,
    )
    representative_plot_path = build_representative_curve_plot(candidate_map)

    raw_improvement = improvement_percent(
        candidate_map["FI01"]["mae_deg"],
        baseline_metrics["mae_deg"],
    )
    derivative_change = improvement_percent(
        candidate_map["FI01"]["sobolev_derivative_mae"],
        baseline_metrics["sobolev_derivative_mae"],
    )
    correlation_change = (
        candidate_map["FI01"]["sobolev_derivative_correlation"]
        - baseline_metrics["sobolev_derivative_correlation"]
    )
    summary_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage6",
        "status": "completed_negative_result",
        "closed_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "first_screen_run_count": 15,
        "stability_run_count": 0,
        "failed_run_count": 0,
        "raw_error_leader": "FI01",
        "raw_error_leader_mae_deg": candidate_map["FI01"]["mae_deg"],
        "raw_error_improvement_vs_stage5_h04_percent": raw_improvement,
        "multi_index_recommended_candidate": None,
        "all_exit_gates_passed": False,
        "failed_decision_reason": (
            "no eligible formulation simultaneously passed derivative MAE, "
            "derivative correlation, harmonic, tail, and matched-control gates"
        ),
        "second_derivative_guidance_enabled": False,
        "second_derivative_gate_passed": preflight_payload[
            "second_derivative_gate_passed"
        ],
        "stage5_h04_disposition": (
            "retained as the qualified structured component entering Stage 7"
        ),
        "official_te_curve_verification_pipeline_run": False,
        "next_stage": "Stage 7 Mean And Centered-Shape Multi-Head Model",
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage6_exit_gate_summary.yaml",
        summary_payload,
    )

    report_text = f"""# Wave 5.2R Stage 6 Spectral And Sobolev Guidance Results

## Executive Decision

Stage 6 is complete as a valid negative result.

All `15` first-screen candidates completed without runtime failures, but no
eligible formulation passed the complete multi-index gate. The conditional
stability continuation was therefore correctly not started.

`FI01`, which combines bounded H04 coefficients, derivative and spectral
guidance, and training-only failure-informed angular weights, is the raw-error
leader at `{candidate_map["FI01"]["mae_deg"]:.9f} deg`. This is a
`{raw_improvement:.2f}%` improvement over the frozen Stage 5 H04 seed.
Nevertheless, FI01 slightly worsens Sobolev derivative MAE by
`{-derivative_change:.3f}%` and reduces derivative correlation by
`{-correlation_change:.6f}`. It is not promoted.

Stage 5 H04 remains the qualified structured component entering Stage 7. No
Stage 6 model replaces the accepted periodic GRU or becomes a production
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
- target-derived runtime inputs: none;
- failed runs: `0`;
- official TE Curve Verification Pipeline: not run.

The preflight passed every derivative, spectrum, coordinate-bound, model-shape,
and leakage check. The second-derivative sensitivity gate failed, so curvature
supervision remained disabled before training as designed.

## Campaign Matrix

| Family | Candidates | Scientific question |
| --- | --- | --- |
| Coefficient controls | C01, C02, C03, C04 | Does representation or direct coefficient prediction explain the gain? |
| Sobolev and spectral | D01, S02, DS01, DS02 | Do first derivatives or complex frequency targets add held-out value? |
| Training strategies | CU01, FI01 | Does curriculum or localized failure weighting help? |
| Coordinate networks | FF00, FF01, SI00, SI01 | Do Fourier features or SIREN resolve missed angular structure? |
| Weak form | W01 | Do local Fourier moments help without pointwise derivative noise? |

## Primary Results

| Candidate | Raw MAE [deg] | Centered [deg] | Offset [deg] | D-MAE | D-corr. | P95 [deg] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Stage 5 H04 | {baseline_metrics["mae_deg"]:.7f} | {baseline_metrics["centered_mae_deg"]:.7f} | {baseline_metrics["offset_abs_error_deg"]:.7f} | {baseline_metrics["sobolev_derivative_mae"]:.7f} | {baseline_metrics["sobolev_derivative_correlation"]:.7f} | {baseline_metrics["per_curve_mae_p95"]:.7f} |
| FI01 | {candidate_map["FI01"]["mae_deg"]:.7f} | {candidate_map["FI01"]["centered_mae_deg"]:.7f} | {candidate_map["FI01"]["offset_abs_error_deg"]:.7f} | {candidate_map["FI01"]["sobolev_derivative_mae"]:.7f} | {candidate_map["FI01"]["sobolev_derivative_correlation"]:.7f} | {candidate_map["FI01"]["per_curve_mae_p95"]:.7f} |
| D01 | {candidate_map["D01"]["mae_deg"]:.7f} | {candidate_map["D01"]["centered_mae_deg"]:.7f} | {candidate_map["D01"]["offset_abs_error_deg"]:.7f} | {candidate_map["D01"]["sobolev_derivative_mae"]:.7f} | {candidate_map["D01"]["sobolev_derivative_correlation"]:.7f} | {candidate_map["D01"]["per_curve_mae_p95"]:.7f} |
| W01 | {candidate_map["W01"]["mae_deg"]:.7f} | {candidate_map["W01"]["centered_mae_deg"]:.7f} | {candidate_map["W01"]["offset_abs_error_deg"]:.7f} | {candidate_map["W01"]["sobolev_derivative_mae"]:.7f} | {candidate_map["W01"]["sobolev_derivative_correlation"]:.7f} | {candidate_map["W01"]["per_curve_mae_p95"]:.7f} |
| FF01 | {candidate_map["FF01"]["mae_deg"]:.7f} | {candidate_map["FF01"]["centered_mae_deg"]:.7f} | {candidate_map["FF01"]["offset_abs_error_deg"]:.7f} | {candidate_map["FF01"]["sobolev_derivative_mae"]:.7f} | {candidate_map["FF01"]["sobolev_derivative_correlation"]:.7f} | {candidate_map["FF01"]["per_curve_mae_p95"]:.7f} |

![Stage 6 multi-index comparison](assets/2026-07-29_stage6_spectral_sobolev_guidance/{multi_index_plot_path.name})

## Gate Matrix

{build_gate_table(gate_payload)}

No row passes all gates.

## What Worked

- FI01, CU01, DS01, and C02 all reduce raw MAE relative to Stage 5 H04.
- FI01 preserves centered shape, offset, amplitude, phase, and P95 within the
  declared gates while beating its DS01 matched control.
- D01 obtains the best centered-shape result among the leading bounded
  coefficient candidates and improves harmonic amplitude and phase.
- W01 produces the best derivative MAE and derivative correlation in the
  first screen, showing that weak local moments can alter the intended
  differential behavior.
- Every model keeps unsupported high-frequency energy bounded.
- The preflight successfully rejected unstable second-derivative supervision.

## What Did Not Work

- The pointwise derivative candidates fail the required derivative improvement
  thresholds despite their explicit Sobolev losses.
- FI01's raw-error gain does not transfer to derivative correlation.
- W01's derivative gain costs raw error, amplitude, and tail quality and does
  not beat its C01 control.
- Fragile-band H08 formulations S02 and DS02 worsen raw error and offset.
- Direct coefficient candidates C03 and C04 remain substantially worse.
- Fourier-feature and SIREN coordinate residuals do not beat the bounded
  coefficient family and do not demonstrate a useful spectral-bias correction.
- No candidate earns stability continuation or model promotion.

## Raw-Error And Derivative Tradeoff

The lower-left quadrant would improve both quantities relative to Stage 5 H04.
No candidate reaches the required improvement region with the remaining gates.

![Raw-error and derivative tradeoff](assets/2026-07-29_stage6_spectral_sobolev_guidance/{tradeoff_plot_path.name})

## Representative Full Curves

FI01 remains visually close to the qualified H04 component. Its improvement is
small and distributed; it does not expose a new localized correction capable
of satisfying the derivative gate.

![Representative FI01 curves](assets/2026-07-29_stage6_spectral_sobolev_guidance/{representative_plot_path.name})

## Scientific Interpretation

Stage 6 does not show that spectral or Sobolev guidance is useless. It shows
that, on the current bounded coefficient representation and fixed split, the
tested loss formulations mostly redistribute error among already correlated
curve metrics. A raw-curve gain can coexist with a worse derivative field, and
a weak-form derivative gain can coexist with worse tails or harmonic
amplitude.

This is exactly why the multi-index gate is necessary. Selecting FI01 by MAE
alone would overstate the physics contribution.

The next controlled hypothesis is decomposition rather than another global
loss mixture: Stage 7 separates the mean/offset quantity from the
mean-centered periodic shape. That design directly targets the offset-shape
competition visible here while preserving H04 as an inspectable structured
component.

## Program Decision

- Stage 6 status: complete, valid negative result;
- completed runs: `15 / 15`;
- stability runs: `0`, correctly skipped;
- raw-error leader: FI01;
- promoted Stage 6 candidate: none;
- retained component: Stage 5 H04;
- production or registry promotion: no;
- next step: Stage 7, Mean And Centered-Shape Multi-Head Model.

## Artifact Map

- campaign:
  `output/training_campaigns/2026-07-29-15-34-05_wave52r_stage6_spectral_sobolev_guidance_2026_07_29/`;
- gate summary:
  `output/analysis/wave_5_2r/stage6_spectral_sobolev_guidance/closeout/stage6_exit_gate_summary.yaml`;
- preflight:
  `output/analysis/wave_5_2r/stage6_spectral_sobolev_guidance/stage6_preflight_validation_summary.yaml`;
- FI01 checkpoint:
  `{candidate_map["FI01"]["checkpoint_path"]}`;
- model report:
  `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-29]/stage6_spectral_sobolev_guidance/stage6_spectral_sobolev_guided_residual_model_report.md`.
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
            "scalar_raw_error_leader_id": "FI01",
            "stage_decision": "completed_negative_result",
            "exit_gate_summary_path": (
                ANALYSIS_DIRECTORY / "stage6_exit_gate_summary.yaml"
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
