"""Build the Wave 5.2R Stage 8 weak forward compliance closeout."""

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
    / "2026-07-29-18-19-20_wave52r_stage8_weak_forward_"
    "compliance_priors_2026_07_29"
)
STAGE_ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage8_weak_forward_compliance_priors"
)
ANALYSIS_DIRECTORY = STAGE_ANALYSIS_DIRECTORY / "closeout"
REPORT_PATH = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "2026-07-29-18-22-31_wave52r_stage8_weak_forward_"
    "compliance_priors_results_report.md"
)
ASSET_DIRECTORY = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "assets"
    / "2026-07-29_stage8_weak_forward_compliance_priors"
)
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping.

    Args:
        path: YAML path.

    Returns:
        Parsed YAML mapping.
    """

    with path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping.

    Args:
        path: Destination path.
        payload: YAML mapping.
    """

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
    """Load and convert the Stage 8 leaderboard."""

    numeric_field_set = {
        "mae_deg",
        "mean_mae_deg",
        "centered_shape_mae_deg",
        "sobolev_derivative_mae",
        "periodic_closure_error_deg",
        "retained_amplitude_mae_deg",
        "retained_phase_mae_rad",
        "per_curve_mae_p95",
        "compliance_derivative_mean_deg_per_nm",
        "compliance_derivative_min_deg_per_nm",
        "compliance_derivative_max_deg_per_nm",
        "compliance_negative_fraction",
        "effective_stiffness_nm_per_deg",
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
    candidate_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot normalized multi-index behavior against frozen H04."""

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
    candidate_id_list = ["C00", "S01", "A01", "B01", "H01"]
    color_list = ["#005A9C", "#2E8B57", "#D97706", "#8B5CF6", "#B91C1C"]
    x_position_array = np.arange(len(metric_name_list))
    width = 0.15
    figure, axis = plt.subplots(figsize=(11.3, 5.9))
    for candidate_index, candidate_id in enumerate(candidate_id_list):
        normalized_value_list = [
            candidate_map[candidate_id][metric_name]
            / candidate_map["D00"][metric_name]
            for metric_name in metric_name_list
        ]
        axis.bar(
            x_position_array + (candidate_index - 2.0) * width,
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
    axis.set_xticks(x_position_array)
    axis.set_xticklabels(display_name_list)
    axis.set_ylabel("Normalized error (lower is better)")
    axis.set_title("Stage 8 Multi-Index Comparison")
    axis.set_ylim(0.94, 1.85)
    axis.grid(axis="y", alpha=0.25)
    axis.legend(ncol=6, loc="upper center", fontsize=8)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage8_multi_index_comparison.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_bootstrap_plot(
    bootstrap_payload: dict[str, Any],
) -> Path:
    """Plot train-only observed and shuffled torque-slope bootstraps."""

    bootstrap_csv_path = (
        STAGE_ANALYSIS_DIRECTORY / "stage8_training_only_bootstrap.csv"
    )
    with bootstrap_csv_path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as input_file:
        row_list = list(csv.DictReader(input_file))
    observed_array = 1.0e6 * np.asarray(
        [float(row["torque_slope_deg_per_nm"]) for row in row_list]
    )
    shuffled_array = 1.0e6 * np.asarray(
        [
            float(row["shuffled_torque_slope_deg_per_nm"])
            for row in row_list
        ]
    )
    figure, axis = plt.subplots(figsize=(9.2, 5.3))
    common_bins = np.linspace(
        min(float(shuffled_array.min()), 0.0),
        float(observed_array.max()) * 1.05,
        42,
    )
    axis.hist(
        shuffled_array,
        bins=common_bins,
        color="#9CA3AF",
        alpha=0.8,
        label="Shuffled torque",
    )
    axis.hist(
        observed_array,
        bins=common_bins,
        color="#005A9C",
        alpha=0.8,
        label="Observed torque",
    )
    axis.axvline(0.0, color="#202020", linewidth=1.0, linestyle="--")
    axis.set_xlabel("Train-only mean-TE slope [microdeg/Nm]")
    axis.set_ylabel("Bootstrap count")
    axis.set_title(
        "Train-Only Compliance Signal And Shuffled Specificity Control"
    )
    axis.text(
        0.98,
        0.94,
        (
            "Observed positive support: "
            f"{100.0 * bootstrap_payload['sign_support_fraction']:.1f}%\n"
            "Shuffled positive support: "
            f"{100.0 * bootstrap_payload['shuffled_sign_support_fraction']:.1f}%"
        ),
        transform=axis.transAxes,
        ha="right",
        va="top",
        fontsize=9,
        bbox={"facecolor": "white", "edgecolor": "#D1D5DB", "alpha": 0.9},
    )
    axis.grid(axis="y", alpha=0.2)
    axis.legend()
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage8_training_bootstrap.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_derivative_plot(
    candidate_map: dict[str, dict[str, Any]],
    bootstrap_payload: dict[str, Any],
) -> Path:
    """Plot model-local compliance derivative ranges."""

    candidate_id_list = [
        "D00",
        "C00",
        "N01",
        "S01",
        "A01",
        "B01",
        "W01",
        "T01",
        "R01",
        "H01",
    ]
    mean_array = 1.0e6 * np.asarray(
        [
            candidate_map[candidate_id][
                "compliance_derivative_mean_deg_per_nm"
            ]
            for candidate_id in candidate_id_list
        ]
    )
    minimum_array = 1.0e6 * np.asarray(
        [
            candidate_map[candidate_id][
                "compliance_derivative_min_deg_per_nm"
            ]
            for candidate_id in candidate_id_list
        ]
    )
    maximum_array = 1.0e6 * np.asarray(
        [
            candidate_map[candidate_id][
                "compliance_derivative_max_deg_per_nm"
            ]
            for candidate_id in candidate_id_list
        ]
    )
    lower_error_array = np.maximum(mean_array - minimum_array, 0.0)
    upper_error_array = np.maximum(maximum_array - mean_array, 0.0)
    x_position_array = np.arange(len(candidate_id_list))
    figure, axis = plt.subplots(figsize=(10.2, 5.5))
    axis.errorbar(
        x_position_array,
        mean_array,
        yerr=np.vstack((lower_error_array, upper_error_array)),
        fmt="o",
        color="#005A9C",
        ecolor="#93A4B5",
        capsize=4,
        label="Test local derivative range",
    )
    axis.axhspan(
        1.0e6 * bootstrap_payload["lower_derivative_deg_per_nm"],
        1.0e6 * bootstrap_payload["upper_derivative_deg_per_nm"],
        color="#2E8B57",
        alpha=0.18,
        label="Train-only population interval",
    )
    axis.axhline(0.0, color="#202020", linewidth=1.0, linestyle="--")
    axis.set_xticks(x_position_array)
    axis.set_xticklabels(candidate_id_list)
    axis.set_ylabel("d(mean TE)/d(torque) [microdeg/Nm]")
    axis.set_title("Population Signal Versus Model-Local Response")
    axis.grid(axis="y", alpha=0.2)
    axis.legend(fontsize=8)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage8_compliance_derivatives.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_negative_fraction_plot(
    candidate_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot the fraction of negative model-local torque derivatives."""

    candidate_id_list = [
        "D00",
        "C00",
        "N01",
        "S01",
        "A01",
        "B01",
        "W01",
        "T01",
        "R01",
        "H01",
    ]
    fraction_percent_array = 100.0 * np.asarray(
        [
            candidate_map[candidate_id]["compliance_negative_fraction"]
            for candidate_id in candidate_id_list
        ]
    )
    color_list = [
        "#2E8B57" if value == 0.0 else "#B45309"
        for value in fraction_percent_array
    ]
    figure, axis = plt.subplots(figsize=(10.2, 4.8))
    axis.bar(candidate_id_list, fraction_percent_array, color=color_list)
    axis.set_ylabel("Negative local derivatives [%]")
    axis.set_title("Local Compliance Sign Violations")
    axis.set_ylim(0.0, 70.0)
    axis.grid(axis="y", alpha=0.2)
    for index, value in enumerate(fraction_percent_array):
        axis.text(index, value + 1.5, f"{value:.1f}%", ha="center", fontsize=8)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage8_negative_derivative_fraction.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_representative_curve_plot(
    candidate_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot representative control, weak-prior, and hard-control curves."""

    prediction_payload_map: dict[str, dict[str, np.ndarray]] = {}
    for candidate_id in ["D00", "C00", "S01", "H01"]:
        prediction_path = (
            PROJECT_ROOT / candidate_map[candidate_id]["checkpoint_path"]
        ).parent / "test_predictions.npz"
        with np.load(prediction_path) as payload:
            prediction_payload_map[candidate_id] = {
                "measured_curve": payload["measured_curve"].copy(),
                "predicted_curve": payload["predicted_curve"].copy(),
            }
    measured_curve_matrix = prediction_payload_map["C00"]["measured_curve"]
    c00_prediction_matrix = prediction_payload_map["C00"]["predicted_curve"]
    per_curve_mae_array = np.mean(
        np.abs(c00_prediction_matrix - measured_curve_matrix),
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
    figure, axis_array = plt.subplots(3, 1, figsize=(11.2, 8.2), sharex=True)
    color_map = {
        "D00": "#D97706",
        "C00": "#005A9C",
        "S01": "#2E8B57",
        "H01": "#B91C1C",
    }
    for axis, curve_index in zip(axis_array, selected_index_list, strict=True):
        axis.plot(
            angle_array,
            measured_curve_matrix[curve_index],
            color="#111827",
            linewidth=1.1,
            label="Measured",
        )
        for candidate_id in ["D00", "C00", "S01", "H01"]:
            axis.plot(
                angle_array,
                prediction_payload_map[candidate_id]["predicted_curve"][
                    curve_index
                ],
                color=color_map[candidate_id],
                linewidth=0.9,
                label=candidate_id,
            )
        axis.set_title(
            f"Test curve {curve_index} | "
            f"C00 MAE {per_curve_mae_array[curve_index]:.6f} deg",
            fontsize=9,
        )
        axis.set_ylabel("TE [deg]")
        axis.grid(alpha=0.2)
    axis_array[0].legend(ncol=5, fontsize=8)
    axis_array[-1].set_xlabel("Angular position [deg]")
    figure.suptitle("Representative Weak-Compliance Reconstructions")
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage8_representative_curves.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_gate_table(gate_payload: dict[str, Any]) -> str:
    """Render the compact Stage 8 promotion-gate matrix."""

    line_list = [
        "| ID | R-H04 | R-C00 | M-H04 | M-C00 | Shape | "
        "Curve | N01 | Sign | Final |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in gate_payload["gate_row_list"]:
        curve_preserved = all(
            [
                row["derivative_preserved"],
                row["closure_preserved"],
                row["amplitude_preserved"],
                row["phase_preserved"],
                row["p95_preserved"],
            ]
        )
        value_list = [
            row["raw_beats_frozen"],
            row["raw_beats_control"],
            row["mean_beats_frozen"],
            row["mean_beats_control"],
            row["shape_preserved"],
            curve_preserved,
            row["beats_shuffled_control"],
            row["positive_derivative_supported"],
        ]
        rendered_value_list = [
            "pass" if value else "fail" for value in value_list
        ]
        final_result = (
            "pass" if row["all_first_screen_gates_passed"] else "fail"
        )
        line_list.append(
            f"| {row['candidate_id']} | "
            + " | ".join(rendered_value_list)
            + f" | {final_result} |"
        )
    return "\n".join(line_list)


def main() -> None:
    """Build Stage 8 decisions, figures, report, and state."""

    leaderboard_row_list = load_leaderboard()
    candidate_map = {
        row["candidate_id"]: row for row in leaderboard_row_list
    }
    gate_payload = load_yaml(
        CAMPAIGN_OUTPUT_DIRECTORY
        / "campaign_first_screen_gate_summary.yaml"
    )
    execution_payload = load_yaml(
        CAMPAIGN_OUTPUT_DIRECTORY / "campaign_execution_summary.yaml"
    )
    preflight_payload = load_yaml(
        STAGE_ANALYSIS_DIRECTORY / "stage8_preflight_validation_summary.yaml"
    )
    bootstrap_payload = load_yaml(
        STAGE_ANALYSIS_DIRECTORY / "stage8_training_only_bootstrap.yaml"
    )

    assert len(leaderboard_row_list) == 10
    assert gate_payload["passing_candidate_id_list"] == []
    assert gate_payload["recommended_candidate_id"] is None
    assert execution_payload["first_screen_completed_count"] == 10
    assert execution_payload["first_screen_failed_count"] == 0
    assert execution_payload["stability_completed_count"] == 0
    assert preflight_payload["all_checks_passed"] is True
    assert bootstrap_payload["validation_or_test_target_used"] is False
    assert bootstrap_payload["sign_support_fraction"] == 1.0

    multi_index_plot_path = build_multi_index_plot(candidate_map)
    bootstrap_plot_path = build_bootstrap_plot(bootstrap_payload)
    derivative_plot_path = build_derivative_plot(
        candidate_map,
        bootstrap_payload,
    )
    negative_fraction_plot_path = build_negative_fraction_plot(candidate_map)
    representative_plot_path = build_representative_curve_plot(candidate_map)

    c00_raw_improvement = improvement_percent(
        candidate_map["C00"]["mae_deg"],
        candidate_map["D00"]["mae_deg"],
    )
    c00_mean_improvement = improvement_percent(
        candidate_map["C00"]["mean_mae_deg"],
        candidate_map["D00"]["mean_mae_deg"],
    )
    c00_shape_improvement = improvement_percent(
        candidate_map["C00"]["centered_shape_mae_deg"],
        candidate_map["D00"]["centered_shape_mae_deg"],
    )
    s01_raw_improvement = improvement_percent(
        candidate_map["S01"]["mae_deg"],
        candidate_map["D00"]["mae_deg"],
    )
    s01_mean_improvement = improvement_percent(
        candidate_map["S01"]["mean_mae_deg"],
        candidate_map["D00"]["mean_mae_deg"],
    )
    summary_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage8",
        "status": "completed_negative_result",
        "closed_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "first_screen_run_count": 10,
        "stability_run_count": 0,
        "failed_run_count": 0,
        "train_only_bootstrap_sign_support_fraction": (
            bootstrap_payload["sign_support_fraction"]
        ),
        "train_only_bootstrap_derivative_interval_deg_per_nm": [
            bootstrap_payload["lower_derivative_deg_per_nm"],
            bootstrap_payload["upper_derivative_deg_per_nm"],
        ],
        "shuffled_bootstrap_sign_support_fraction": (
            bootstrap_payload["shuffled_sign_support_fraction"]
        ),
        "raw_error_leader": "C00",
        "raw_error_leader_mae_deg": candidate_map["C00"]["mae_deg"],
        "raw_error_improvement_vs_frozen_h04_percent": c00_raw_improvement,
        "multi_index_recommended_candidate": None,
        "all_exit_gates_passed": False,
        "failed_decision_reason": (
            "no weak compliance arm beat the data-only C00 control and "
            "preserved positive model-local torque derivatives"
        ),
        "weak_prior_disposition": (
            "observable population compliance is supported, but the tested "
            "weak priors add no predictive value over data-only fine-tuning"
        ),
        "hard_equation_disposition": (
            "positive derivatives are enforced, but the fixed compliance "
            "equation materially underfits raw and mean TE"
        ),
        "stage5_h04_disposition": (
            "retained as the qualified structured component entering Stage 9"
        ),
        "official_te_curve_verification_pipeline_run": False,
        "next_stage": "Stage 9 Temporal Analytical-Residual Models",
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage8_exit_gate_summary.yaml",
        summary_payload,
    )

    report_text = f"""# Wave 5.2R Stage 8 Weak Forward Compliance Priors Results

## Executive Decision

Stage 8 is complete as a valid negative result.

All `10 / 10` first-screen runs completed without failure. No weak-compliance
candidate passed the complete multi-index gate, so the conditional stability
continuation was correctly skipped.

The training-only diagnostic strongly supports a positive *population*
association between applied torque and curve-mean TE: all `512 / 512`
bootstraps are positive, with a 95% interval from
`{bootstrap_payload["lower_derivative_deg_per_nm"]:.9e}` to
`{bootstrap_payload["upper_derivative_deg_per_nm"]:.9e} deg/Nm`. The
shuffled-torque control returns `{100.0 * bootstrap_payload["shuffled_sign_support_fraction"]:.2f}%`
positive support, as expected under loss of specificity.

That valid observable relationship does not transfer into useful local
physics guidance. No weak-prior arm beats data-only C00, and all weak arms
retain negative model-local derivatives for `35.1%` to `44.3%` of test
conditions. H01 enforces a positive derivative everywhere, but materially
underfits raw and mean TE.

Stage 5 H04 remains the qualified structured component entering Stage 9. No
Stage 8 model replaces the accepted periodic GRU or becomes a production
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
- completed runs: `10 / 10`;
- failed runs: `0`;
- target-derived runtime inputs: none;
- validation or test targets used for prior estimation: no;
- official TE Curve Verification Pipeline: not run.

This stage intentionally tests an observable response prior, not an identified
contact-stiffness law. The dataset does not contain ordered load-unload cycles,
clearances, contact forces, hysteretic internal states, or component-level
stiffness measurements required by the Xu mechanical formulation.

## Candidate Matrix

| ID | Formulation | Role |
| --- | --- | --- |
| D00 | frozen H04 | immutable structured baseline |
| C00 | data-only H04 fine-tune | learned control |
| S01 | sign-only derivative penalty | weakest physics arm |
| B01 | broad bootstrap interval | interval arm |
| W01 | confidence-weighted interval | support-aware arm |
| T01 | temperature-stratified interval | conditional arm |
| A01 | delayed interval activation | curriculum arm |
| R01 | adaptive interval weighting | optimization arm |
| N01 | shuffled-torque interval | specificity control |
| H01 | fixed compliance equation | misspecification control |

## Primary Results

| ID | Raw [deg] | Mean [deg] | Shape [deg] | dTE/dT [deg/Nm] | Negative [%] |
| --- | ---: | ---: | ---: | ---: | ---: |
| D00 | {candidate_map["D00"]["mae_deg"]:.7f} | {candidate_map["D00"]["mean_mae_deg"]:.7f} | {candidate_map["D00"]["centered_shape_mae_deg"]:.7f} | {candidate_map["D00"]["compliance_derivative_mean_deg_per_nm"]:.3e} | {100.0 * candidate_map["D00"]["compliance_negative_fraction"]:.1f} |
| C00 | {candidate_map["C00"]["mae_deg"]:.7f} | {candidate_map["C00"]["mean_mae_deg"]:.7f} | {candidate_map["C00"]["centered_shape_mae_deg"]:.7f} | {candidate_map["C00"]["compliance_derivative_mean_deg_per_nm"]:.3e} | {100.0 * candidate_map["C00"]["compliance_negative_fraction"]:.1f} |
| S01 | {candidate_map["S01"]["mae_deg"]:.7f} | {candidate_map["S01"]["mean_mae_deg"]:.7f} | {candidate_map["S01"]["centered_shape_mae_deg"]:.7f} | {candidate_map["S01"]["compliance_derivative_mean_deg_per_nm"]:.3e} | {100.0 * candidate_map["S01"]["compliance_negative_fraction"]:.1f} |
| A01 | {candidate_map["A01"]["mae_deg"]:.7f} | {candidate_map["A01"]["mean_mae_deg"]:.7f} | {candidate_map["A01"]["centered_shape_mae_deg"]:.7f} | {candidate_map["A01"]["compliance_derivative_mean_deg_per_nm"]:.3e} | {100.0 * candidate_map["A01"]["compliance_negative_fraction"]:.1f} |
| B01 | {candidate_map["B01"]["mae_deg"]:.7f} | {candidate_map["B01"]["mean_mae_deg"]:.7f} | {candidate_map["B01"]["centered_shape_mae_deg"]:.7f} | {candidate_map["B01"]["compliance_derivative_mean_deg_per_nm"]:.3e} | {100.0 * candidate_map["B01"]["compliance_negative_fraction"]:.1f} |
| N01 | {candidate_map["N01"]["mae_deg"]:.7f} | {candidate_map["N01"]["mean_mae_deg"]:.7f} | {candidate_map["N01"]["centered_shape_mae_deg"]:.7f} | {candidate_map["N01"]["compliance_derivative_mean_deg_per_nm"]:.3e} | {100.0 * candidate_map["N01"]["compliance_negative_fraction"]:.1f} |
| H01 | {candidate_map["H01"]["mae_deg"]:.7f} | {candidate_map["H01"]["mean_mae_deg"]:.7f} | {candidate_map["H01"]["centered_shape_mae_deg"]:.7f} | {candidate_map["H01"]["compliance_derivative_mean_deg_per_nm"]:.3e} | {100.0 * candidate_map["H01"]["compliance_negative_fraction"]:.1f} |

![Stage 8 multi-index comparison](assets/2026-07-29_stage8_weak_forward_compliance_priors/{multi_index_plot_path.name})

C00 is the raw-error leader at `{candidate_map["C00"]["mae_deg"]:.9f} deg`.
It improves raw MAE by `{c00_raw_improvement:.2f}%` and mean MAE by
`{c00_mean_improvement:.2f}%` relative to frozen H04, while centered-shape MAE
changes by `{c00_shape_improvement:+.2f}%`. This gain is attributable to
bounded data-only fine-tuning, not to a compliance constraint.

S01 improves raw MAE by `{s01_raw_improvement:.2f}%` and mean MAE by
`{s01_mean_improvement:.2f}%` relative to frozen H04, but it is worse than C00
on both quantities and does not establish a consistently positive local
response.

## Train-Only Identifiability Diagnostic

![Training bootstrap](assets/2026-07-29_stage8_weak_forward_compliance_priors/{bootstrap_plot_path.name})

The population slope is stable and specific to the real torque ordering. Its
median corresponds to an effective response scale of
`{bootstrap_payload["effective_stiffness_from_median_nm_per_deg"]:.1f} Nm/deg`.
This number is a descriptive reciprocal slope, not an identified reducer
stiffness. It conflates operating-condition sampling, offsets, temperature,
speed, contact state, and unobserved hysteresis.

## Local Derivative Behavior

![Compliance derivative ranges](assets/2026-07-29_stage8_weak_forward_compliance_priors/{derivative_plot_path.name})

The green band is the train-only population interval. The learned model-local
derivatives are roughly three orders of magnitude smaller and cross zero for
every weak arm. The diagnostic therefore distinguishes two different claims:

1. higher-torque operating cells have higher mean TE on average;
2. each learned curve should respond monotonically to an infinitesimal torque
   perturbation while every other input remains fixed.

The first claim is supported. The second is not identified by this dataset and
is not recovered by the tested penalties.

### Sign Violations

![Negative derivative fractions](assets/2026-07-29_stage8_weak_forward_compliance_priors/{negative_fraction_plot_path.name})

H01 is the only formulation with zero sign violations. Its derivative is
fixed near the train-only population slope, but raw MAE rises to
`{candidate_map["H01"]["mae_deg"]:.7f} deg` and mean MAE to
`{candidate_map["H01"]["mean_mae_deg"]:.7f} deg`. This is direct evidence that
the hard equation is misspecified for pointwise prediction.

## Gate Matrix

{build_gate_table(gate_payload)}

No candidate passes. S01 and A01 beat frozen H04 on raw and mean error, but
neither beats C00 or the shuffled-control requirement, and neither has
positive local derivatives throughout the test surface. B01, W01, T01, and
R01 additionally regress raw and mean behavior.

## What Worked

- the train-only bootstrap found a strong positive population association;
- the shuffled-torque bootstrap removed that directional support;
- autograd derivatives were computed without target-derived runtime inputs;
- the weak-to-hard ladder exposed the tradeoff between predictive fit and
  derivative enforcement;
- all curve-first diagnostics and failure controls completed deterministically.

## What Did Not Work

- no weak physics arm outperformed data-only C00;
- N01 is numerically identical to C00 because its shuffled interval does not
  activate a useful constraint;
- sign-only and delayed penalties leave `37.1%` and `44.3%` negative local
  derivatives, respectively;
- broad, weighted, temperature, and adaptive intervals converge to nearly the
  same inferior solution;
- the hard compliance equation removes sign violations only by sacrificing
  raw and mean accuracy;
- no candidate earns stability continuation or promotion.

## Representative Full Curves

![Representative curves](assets/2026-07-29_stage8_weak_forward_compliance_priors/{representative_plot_path.name})

C00 and S01 remain visually close to frozen H04. H01 shifts whole-curve levels
because the fixed compliance term dominates the mean response; its slightly
better centered-shape metric does not compensate for the offset error.

## Scientific Interpretation

The Stage 8 result does not show that compliance is absent. It shows that a
cross-sectional population trend is insufficient to define a causal,
pointwise constitutive residual. A PINN can compensate for an incomplete
mechanical model only when the residual constrains the intended state without
forcing the network to absorb systematic misspecification.

Here the missing load history, direction reversals, contact regime, clearance,
and internal torsional states make the local derivative ambiguous. The network
therefore treats the compliance penalties as optimization bias rather than
additional identifiable information.

This evidence justifies moving to Stage 9, where causal history is tested as
the missing information channel through temporal analytical-residual models.
Stage 9 must preserve the same negative-control and data-only comparison
discipline.

## Program Decision

- Stage 8 status: complete, valid negative result;
- completed runs: `10 / 10`;
- stability runs: `0`, correctly skipped;
- raw-error leader: C00 data-only control;
- promoted Stage 8 candidate: none;
- retained component: Stage 5 H04;
- production or registry promotion: no;
- next step: Stage 9, Temporal Analytical-Residual Models.

## Artifact Map

- campaign:
  `output/training_campaigns/2026-07-29-18-19-20_wave52r_stage8_weak_forward_compliance_priors_2026_07_29/`;
- gate summary:
  `output/analysis/wave_5_2r/stage8_weak_forward_compliance_priors/closeout/stage8_exit_gate_summary.yaml`;
- bootstrap:
  `output/analysis/wave_5_2r/stage8_weak_forward_compliance_priors/stage8_training_only_bootstrap.yaml`;
- preflight:
  `output/analysis/wave_5_2r/stage8_weak_forward_compliance_priors/stage8_preflight_validation_summary.yaml`;
- C00 checkpoint:
  `{candidate_map["C00"]["checkpoint_path"]}`;
- model report:
  `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-29]/stage8_weak_forward_compliance_priors/stage8_weak_forward_compliance_priors_model_report.md`.
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
            "scalar_raw_error_leader_id": "C00",
            "stage_decision": "completed_negative_result",
            "exit_gate_summary_path": (
                ANALYSIS_DIRECTORY / "stage8_exit_gate_summary.yaml"
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
