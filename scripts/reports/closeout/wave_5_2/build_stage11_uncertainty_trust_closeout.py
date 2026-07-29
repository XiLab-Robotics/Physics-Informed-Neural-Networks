"""Build the Wave 5.2R Stage 11 uncertainty-trust closeout."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
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
CAMPAIGN_ROOT_DIRECTORY = PROJECT_ROOT / "output" / "training_campaigns"
RUN_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "uncertainty_physics_trust_calibration"
)
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage11_uncertainty_physics_trust_calibration"
    / "closeout"
)
REPORT_DIRECTORY = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
)
ASSET_DIRECTORY = (
    REPORT_DIRECTORY
    / "assets"
    / "2026-07-29_stage11_uncertainty_trust_calibration"
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


def load_csv(path: Path) -> list[dict[str, str]]:
    """Load one CSV table."""

    with path.open("r", encoding="utf-8", newline="") as input_file:
        return list(csv.DictReader(input_file))


def find_campaign_output_directory() -> Path:
    """Resolve the unique latest completed Stage 11 campaign."""

    path_list = sorted(
        CAMPAIGN_ROOT_DIRECTORY.glob(
            "*_wave52r_stage11_uncertainty_trust_calibration_2026_07_29"
        ),
        key=lambda path: path.stat().st_mtime,
    )
    assert path_list
    campaign_path = path_list[-1]
    execution_payload = load_yaml(
        campaign_path / "campaign_execution_summary.yaml"
    )
    assert execution_payload["status"] == "completed"
    return campaign_path


def run_directory(
    row_map: dict[str, dict[str, Any]],
    candidate_id: str,
) -> Path:
    """Resolve one candidate run directory from the leaderboard."""

    path = RUN_ROOT_DIRECTORY / row_map[candidate_id]["run_instance_id"]
    assert path.is_dir()
    return path


def build_localization_plot(
    row_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot rank, average precision, and high-error capture."""

    candidate_id_list = [
        "C00",
        "S01",
        "S02",
        "A01",
        "A02",
        "A03",
        "D01",
        "E01",
        "M01",
        "N01",
    ]
    x_position_array = np.arange(len(candidate_id_list))
    width = 0.25
    figure, axis = plt.subplots(figsize=(11.5, 6.0))
    axis.bar(
        x_position_array - width,
        [
            float(row_map[candidate_id]["spearman_correlation"])
            for candidate_id in candidate_id_list
        ],
        width,
        color="#005A9C",
        label="Spearman",
    )
    axis.bar(
        x_position_array,
        [
            float(
                row_map[candidate_id][
                    "top_quintile_average_precision"
                ]
            )
            for candidate_id in candidate_id_list
        ],
        width,
        color="#D97706",
        label="Average precision",
    )
    axis.bar(
        x_position_array + width,
        [
            float(
                row_map[candidate_id][
                    "top_20_percent_error_capture_rate"
                ]
            )
            for candidate_id in candidate_id_list
        ],
        width,
        color="#2E8B57",
        label="High-error capture",
    )
    axis.axhline(0.30, color="#005A9C", linestyle="--", linewidth=0.9)
    axis.axhline(0.35, color="#D97706", linestyle="--", linewidth=0.9)
    axis.axhline(0.40, color="#2E8B57", linestyle="--", linewidth=0.9)
    axis.set_xticks(x_position_array)
    axis.set_xticklabels(candidate_id_list)
    axis.set_ylim(
        min(
            -0.2,
            min(
                float(row_map[candidate_id]["spearman_correlation"])
                for candidate_id in candidate_id_list
            )
            - 0.05,
        ),
        1.05,
    )
    axis.set_ylabel("Localization metric")
    axis.set_title("Stage 11 Error-Localization Evidence")
    axis.grid(axis="y", alpha=0.22)
    axis.legend(ncol=3)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage11_localization_metrics.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_selective_risk_plot(
    row_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot 80-percent selective risk against unfiltered K01 risk."""

    candidate_id_list = [
        "S01",
        "S02",
        "A01",
        "A02",
        "A03",
        "D01",
        "E01",
        "M01",
        "N01",
    ]
    unfiltered_mae = float(
        row_map["C00"]["selective_curve_mae_80_percent_deg"]
    )
    # C00 has constant scores, so its stable tie order is not a true filter.
    # Recover the unfiltered curve MAE from the candidate metrics file.
    c00_metrics = load_yaml(
        run_directory(row_map, "C00") / "metrics_summary.yaml"
    )
    unfiltered_mae = float(
        c00_metrics["localization"]["unfiltered_curve_mae_deg"]
    )
    selected_value_list = [
        float(
            row_map[candidate_id][
                "selective_curve_mae_80_percent_deg"
            ]
        )
        for candidate_id in candidate_id_list
    ]
    figure, axis = plt.subplots(figsize=(10.2, 5.8))
    bar_color_list = [
        "#2E8B57" if value <= 0.90 * unfiltered_mae else "#6B7280"
        for value in selected_value_list
    ]
    axis.bar(
        candidate_id_list,
        selected_value_list,
        color=bar_color_list,
    )
    axis.axhline(
        unfiltered_mae,
        color="#202020",
        linestyle="-",
        label="Unfiltered K01",
    )
    axis.axhline(
        0.90 * unfiltered_mae,
        color="#B91C1C",
        linestyle="--",
        label="10% reduction gate",
    )
    axis.set_ylabel("Curve MAE at 80% coverage [deg]")
    axis.set_title("Selective-Risk Test")
    axis.grid(axis="y", alpha=0.22)
    axis.legend()
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage11_selective_risk.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_coverage_width_plot(
    row_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot marginal coverage against interval width."""

    candidate_id_list = [
        "C00",
        "S01",
        "S02",
        "A01",
        "A02",
        "A03",
        "D01",
        "E01",
        "M01",
        "N01",
    ]
    annotation_offset_map = {
        "C00": (7, 12),
        "S01": (7, -17),
        "S02": (-38, 12),
        "N01": (7, -17),
        "M01": (7, -11),
    }
    figure, axis = plt.subplots(figsize=(9.2, 6.2))
    for candidate_id in candidate_id_list:
        color = (
            "#B91C1C"
            if candidate_id in {"C00", "N01"}
            else "#005A9C"
        )
        axis.scatter(
            float(row_map[candidate_id]["marginal_90_mean_width_deg"]),
            float(row_map[candidate_id]["marginal_90_coverage"]),
            color=color,
            s=56,
        )
        axis.annotate(
            candidate_id,
            (
                float(
                    row_map[candidate_id][
                        "marginal_90_mean_width_deg"
                    ]
                ),
                float(row_map[candidate_id]["marginal_90_coverage"]),
            ),
            xytext=annotation_offset_map.get(candidate_id, (7, 5)),
            textcoords="offset points",
        )
    axis.axhspan(0.85, 0.95, color="#2E8B57", alpha=0.10)
    axis.axhline(0.90, color="#202020", linestyle="--", linewidth=1.0)
    axis.axvline(
        1.05 * float(row_map["C00"]["marginal_90_mean_width_deg"]),
        color="#D97706",
        linestyle="--",
        linewidth=1.0,
        label="Width gate",
    )
    axis.set_xlabel("Mean 90% interval width [deg]")
    axis.set_ylabel("Empirical marginal coverage")
    axis.set_title("Calibration-Width Tradeoff")
    axis.grid(alpha=0.22)
    axis.legend()
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage11_coverage_width.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_group_coverage_plot(
    row_map: dict[str, dict[str, Any]],
    candidate_id: str,
) -> Path:
    """Plot operating-band coverage for the selected diagnostic candidate."""

    row_list = load_csv(
        run_directory(row_map, candidate_id) / "group_metrics.csv"
    )
    row_list = [
        row
        for row in row_list
        if row["group_domain"] in {"torque", "speed", "temperature"}
    ]
    domain_label_map = {
        "torque": "Torque",
        "speed": "Speed",
        "temperature": "Temp",
    }
    band_label_map = {
        "low": "L",
        "mid": "M",
        "high": "H",
    }
    label_list = [
        (
            f"{domain_label_map[row['group_domain']]}:"
            f"{band_label_map[row['group'].split('_')[-1]]}"
        )
        for row in row_list
    ]
    coverage_list = [
        float(row["marginal_90_coverage"]) for row in row_list
    ]
    x_position_array = np.arange(len(label_list))
    figure, axis = plt.subplots(figsize=(10.5, 5.8))
    point_color_list = [
        "#2E8B57" if value >= 0.75 else "#B91C1C"
        for value in coverage_list
    ]
    axis.vlines(
        x_position_array,
        0.0,
        coverage_list,
        color=point_color_list,
        linewidth=6.0,
        alpha=0.65,
    )
    axis.scatter(
        x_position_array,
        coverage_list,
        color=point_color_list,
        s=80,
        zorder=3,
    )
    axis.set_xticks(x_position_array)
    axis.set_xticklabels(label_list)
    axis.axhline(0.90, color="#202020", linestyle="--", label="Nominal 90%")
    axis.axhline(0.75, color="#B91C1C", linestyle=":", label="Band gate")
    axis.set_ylim(0.0, 1.05)
    axis.set_ylabel("Marginal 90% coverage")
    axis.set_title(f"{candidate_id} Operating-Band Calibration")
    axis.grid(axis="y", alpha=0.22)
    axis.legend()
    figure.tight_layout()
    output_path = (
        ASSET_DIRECTORY / "stage11_operating_band_coverage.png"
    )
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_representative_interval_plot(
    row_map: dict[str, dict[str, Any]],
    candidate_id: str,
) -> Path:
    """Plot the highest-uncertainty test curve and calibrated interval."""

    candidate_directory = run_directory(row_map, candidate_id)
    with np.load(
        candidate_directory / "test_uncertainty.npz"
    ) as payload:
        measured_curve = np.asarray(payload["measured_curve"])
        predicted_curve = np.asarray(payload["predicted_curve"])
        calibrated_scale = np.asarray(
            payload["calibrated_curve_scale"]
        )
    calibration_payload = load_yaml(
        candidate_directory / "calibration_state.yaml"
    )
    marginal_90_quantile = float(
        calibration_payload["conformal"]["marginal_quantile_map"]["90"]
    )
    curve_index = int(np.argmax(calibrated_scale))
    half_width = (
        calibrated_scale[curve_index] * marginal_90_quantile
    )
    angle_array = np.linspace(
        0.0,
        360.0,
        measured_curve.shape[1],
        endpoint=False,
    )
    figure, axis = plt.subplots(figsize=(11.3, 5.8))
    axis.fill_between(
        angle_array,
        predicted_curve[curve_index] - half_width,
        predicted_curve[curve_index] + half_width,
        color="#8EC5FF",
        alpha=0.45,
        label="Calibrated 90% marginal interval",
    )
    axis.plot(
        angle_array,
        measured_curve[curve_index],
        color="#202020",
        linewidth=1.6,
        label="Measured",
    )
    axis.plot(
        angle_array,
        predicted_curve[curve_index],
        color="#005A9C",
        linewidth=1.3,
        label="Frozen K01",
    )
    axis.set_xlabel("Output angle [deg]")
    axis.set_ylabel("Transmission error [deg]")
    axis.set_title(
        f"{candidate_id} Highest-Uncertainty Test Curve "
        f"(index {curve_index})"
    )
    axis.grid(alpha=0.22)
    axis.legend()
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage11_representative_interval.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def parse_arguments() -> argparse.Namespace:
    """Parse closeout arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--report-timestamp",
        required=True,
        help="Timestamp prefix in YYYY-MM-DD-HH-mm-ss format.",
    )
    return parser.parse_args()


def main() -> None:
    """Generate Stage 11 plots, decision record, and Markdown report."""

    arguments = parse_arguments()
    campaign_output_directory = find_campaign_output_directory()
    leaderboard_payload = load_yaml(
        campaign_output_directory / "campaign_leaderboard.yaml"
    )
    gate_payload = load_yaml(
        campaign_output_directory
        / "campaign_first_screen_gate_summary.yaml"
    )
    best_run_payload = load_yaml(
        campaign_output_directory / "campaign_best_run.yaml"
    )
    row_list = leaderboard_payload["ranked_candidate_list"]
    row_map = {row["candidate_id"]: row for row in row_list}
    diagnostic_best_candidate_id = best_run_payload[
        "diagnostic_best_candidate"
    ]["candidate_id"]
    selected_candidate_id = gate_payload["selected_candidate_id"]
    report_candidate_id = (
        selected_candidate_id or diagnostic_best_candidate_id
    )
    report_path = (
        REPORT_DIRECTORY
        / (
            f"{arguments.report_timestamp}_wave52r_stage11_uncertainty_"
            "and_physics_trust_calibration_results_report.md"
        )
    )

    summary_payload = {
        "schema_version": 1,
        "stage": "Wave 5.2R Stage 11",
        "status": (
            "completed_with_qualified_trust_component"
            if selected_candidate_id is not None
            else "completed_without_qualified_trust_component"
        ),
        "completed_entry_count": 10,
        "failed_entry_count": 0,
        "qualified_candidate_id_list": gate_payload[
            "qualified_candidate_id_list"
        ],
        "selected_candidate_id": selected_candidate_id,
        "diagnostic_best_candidate_id": diagnostic_best_candidate_id,
        "official_mean_prediction_changed": False,
        "wave6_entry_authorized": False,
        "next_stage": (
            "Wave 5.2R Stage 12 advanced constraint optimization"
        ),
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage11_exit_gate_summary.yaml",
        summary_payload,
    )
    plot_path_list = [
        build_localization_plot(row_map),
        build_selective_risk_plot(row_map),
        build_coverage_width_plot(row_map),
        build_group_coverage_plot(row_map, report_candidate_id),
        build_representative_interval_plot(
            row_map,
            report_candidate_id,
        ),
    ]
    relative_plot_path_list = [
        path.relative_to(report_path.parent).as_posix()
        for path in plot_path_list
    ]
    report_candidate_row = row_map[report_candidate_id]
    selected_text = (
        f"`{selected_candidate_id}`"
        if selected_candidate_id is not None
        else "none"
    )
    report_text = f"""# Wave 5.2R Stage 11 Uncertainty And Physics-Trust Calibration Results

## Executive Summary

Stage 11 completed all ten calibration entries without campaign failure. The
frozen K01 curve remained the prediction center throughout. The campaign
tested whether causal operating-support, analytical-disagreement,
dense-model-disagreement, and five-seed ensemble signals could localize K01
error and support non-vacuous empirical intervals.

The qualified Stage 11 trust component is {selected_text}. The strongest
diagnostic candidate is `{diagnostic_best_candidate_id}` with Spearman
correlation `{float(report_candidate_row['spearman_correlation']):.3f}`,
top-quintile average precision
`{float(report_candidate_row['top_quintile_average_precision']):.3f}`, and
high-error capture
`{float(report_candidate_row['top_20_percent_error_capture_rate']):.3f}`.
No result changes K01 promotion status or authorizes Wave 6.

## Scope And Leakage Boundary

- Dataset: polished dataset, setpoint inputs, forward surface only.
- Split: frozen `675/194/97` grouped split.
- Mean prediction: primary Stage 9 K01, unchanged.
- Calibration: validation partition only.
- Final evaluation: one held-out test pass.
- Runtime target-derived inputs: zero.
- Ensemble: five deterministic K01 seeds with identical architecture and
  optimization rules.

## Candidate Results

Candidate labels are: `C00` constant control, `S01` condition distance, `S02`
support boundary, `A01` PF-A/H04 disagreement, `A02` H04/K01 disagreement,
`A03` PF-A/K01 disagreement, `D01` R00/K01 disagreement, `E01` five-seed
spread, `M01` composite trust, and `N01` shuffled control.

| ID | Spearman | AP | Capture | MAE@80 | Cov90 | Width90 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
"""
    first_table_order = [
        "C00",
        "S01",
        "S02",
        "A01",
        "A02",
    ]
    second_table_order = [
        "A03",
        "D01",
        "E01",
        "M01",
        "N01",
    ]
    for candidate_id in first_table_order:
        row = row_map[candidate_id]
        report_text += (
            f"| `{candidate_id}` | "
            f"{float(row['spearman_correlation']):.3f} | "
            f"{float(row['top_quintile_average_precision']):.3f} | "
            f"{float(row['top_20_percent_error_capture_rate']):.3f} | "
            f"{float(row['selective_curve_mae_80_percent_deg']):.6f} | "
            f"{float(row['marginal_90_coverage']):.3f} | "
            f"{float(row['marginal_90_mean_width_deg']):.6f} |\n"
        )
    report_text += """

### Residual, Ensemble, And Composite Signals

| ID | Spearman | AP | Capture | MAE@80 | Cov90 | Width90 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
"""
    for candidate_id in second_table_order:
        row = row_map[candidate_id]
        report_text += (
            f"| `{candidate_id}` | "
            f"{float(row['spearman_correlation']):.3f} | "
            f"{float(row['top_quintile_average_precision']):.3f} | "
            f"{float(row['top_20_percent_error_capture_rate']):.3f} | "
            f"{float(row['selective_curve_mae_80_percent_deg']):.6f} | "
            f"{float(row['marginal_90_coverage']):.3f} | "
            f"{float(row['marginal_90_mean_width_deg']):.6f} |\n"
        )
    report_text += f"""
![Stage 11 localization metrics]({relative_plot_path_list[0]})

## Error Localization

The primary question is whether uncertainty ranks actual held-out curve error.
The constant control has no meaningful localization by construction, while the
shuffled control tests whether the observed score distribution alone can
reproduce the result. A candidate must exceed both controls and pass the fixed
rank, average-precision, capture, and selective-risk gates.

![Stage 11 selective-risk test]({relative_plot_path_list[1]})

## Interval Calibration

All intervals are centered on the frozen K01 prediction. Validation absolute
residuals determine split-conformal quantiles; test labels do not tune widths.
The fixed gate requires empirical 90-percent marginal coverage between `0.85`
and `0.95` with mean width no more than `1.05` times the constant conformal
control.

![Stage 11 calibration-width tradeoff]({relative_plot_path_list[2]})

## Operating-Band Evidence

Torque, speed, and temperature bands use train-defined terciles. Any populated
band with at least ten test curves must retain at least `0.75` marginal
coverage. The Stage 3 support tier remains visible separately because only a
small number of test curves occupy sparse or extrapolation tiers.

![Stage 11 operating-band coverage]({relative_plot_path_list[3]})

## Representative Calibrated Curve

The plot below shows the highest-uncertainty test curve for
`{report_candidate_id}`. The interval is an empirical error band, not a
mechanistic probability distribution of reducer TE.

![Stage 11 representative interval]({relative_plot_path_list[4]})

## Deployment Cost

Simple condition or disagreement signals retain one primary K01 checkpoint.
The ensemble candidate requires five K01 checkpoints and is therefore eligible
only as offline research evidence unless a future single-pass trust head
matches its calibration. The deployment gate remains a maximum `1.25` times
the primary K01 checkpoint cost.

## Decision

- Stage 11 status: `{summary_payload['status']}`.
- Qualified trust component: {selected_text}.
- Diagnostic best candidate: `{diagnostic_best_candidate_id}`.
- Official mean prediction changed: no.
- K01 promoted: no.
- Physics-integrated Wave 6 authorized: no.
- Next step: Stage 12 advanced constraint optimization, applied only to
  ingredients that already showed isolated signal.

## Reproducibility Evidence

- Campaign leaderboard:
  `{(campaign_output_directory / 'campaign_leaderboard.yaml').relative_to(PROJECT_ROOT).as_posix()}`
- Gate summary:
  `{(campaign_output_directory / 'campaign_first_screen_gate_summary.yaml').relative_to(PROJECT_ROOT).as_posix()}`
- Exit-gate summary:
  `output/analysis/wave_5_2r/stage11_uncertainty_physics_trust_calibration/closeout/stage11_exit_gate_summary.yaml`
- Preflight:
  `output/analysis/wave_5_2r/stage11_uncertainty_physics_trust_calibration/stage11_preflight_validation_summary.yaml`
"""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_text, encoding="utf-8", newline="\n")
    print(report_path)


if __name__ == "__main__":
    main()
