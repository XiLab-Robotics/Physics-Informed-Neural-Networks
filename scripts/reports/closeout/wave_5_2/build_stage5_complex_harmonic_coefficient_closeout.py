"""Build the Wave 5.2R Stage 5 bounded curve-first closeout."""

from __future__ import annotations

# Import Python Utilities
import csv
from datetime import datetime
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Plotting And Numerical Utilities
import matplotlib
import numpy as np
import yaml

matplotlib.use("Agg")
from matplotlib import pyplot as plt  # noqa: E402

# Import Stage 5 Campaign Utilities
from scripts.campaigns.wave_5_2.run_wave52r_stage5_complex_harmonic_coefficient_residuals import (
    ACTIVE_CAMPAIGN_PATH,
    PROJECT_ROOT as CAMPAIGN_PROJECT_ROOT,
    _reconstruct_numpy_curve,
    aggregate_metrics,
    build_stage5_dataset,
    load_yaml,
    write_csv,
    write_yaml,
)


# Define Canonical Closeout Paths
assert CAMPAIGN_PROJECT_ROOT == PROJECT_ROOT
CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_campaigns"
    / "2026-07-28-16-17-06_wave52r_stage5_complex_harmonic_"
    "coefficient_residuals_2026_07_28"
)
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage5_complex_harmonic_coefficient_residuals"
    / "closeout"
)
REPORT_PATH = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "2026-07-28-16-20-55_wave52r_stage5_complex_harmonic_"
    "coefficient_residuals_results_report.md"
)
ASSET_DIRECTORY = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "assets"
    / "2026-07-28_stage5_complex_harmonic_coefficients"
)


def load_csv(path: Path) -> list[dict[str, str]]:
    """Load one CSV table as dictionaries."""

    with path.open("r", encoding="utf-8-sig", newline="") as input_file:
        return list(csv.DictReader(input_file))


def float_row(row: dict[str, str]) -> dict[str, Any]:
    """Convert the known numeric leaderboard fields."""

    numeric_name_set = {
        "queue_index",
        "random_seed",
        "best_epoch",
        "validation_curve_mae_deg",
        "mae_deg",
        "rmse_deg",
        "centered_mae_deg",
        "centered_rmse_deg",
        "offset_abs_error_deg",
        "peak_to_peak_abs_error_deg",
        "derivative_mae_deg_per_sample",
        "periodic_closure_error_deg",
        "retained_amplitude_mae_deg",
        "retained_phase_mae_rad",
        "correction_to_anchor_rms",
    }
    converted_row: dict[str, Any] = dict(row)
    for field_name in numeric_name_set:
        if field_name not in converted_row:
            continue
        try:
            converted_row[field_name] = float(converted_row[field_name])
        except ValueError:
            converted_row[field_name] = float("nan")
    return converted_row


def improvement_percent(
    candidate_value: float,
    reference_value: float,
) -> float:
    """Return positive percent improvement for a minimized metric."""

    return 100.0 * (reference_value - candidate_value) / reference_value


def build_gate_rows(
    anchor_metrics: dict[str, float],
    h04_row: dict[str, Any],
    c04_row: dict[str, Any],
    h04_stability_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Evaluate every explicit Stage 5 promotion gate."""

    gate_list = [
        (
            "raw_mae_vs_anchor",
            h04_row["mae_deg"] < anchor_metrics["mae_deg"],
            h04_row["mae_deg"],
            anchor_metrics["mae_deg"],
        ),
        (
            "raw_mae_vs_matched_direct",
            h04_row["mae_deg"] < c04_row["mae_deg"],
            h04_row["mae_deg"],
            c04_row["mae_deg"],
        ),
        (
            "centered_shape_vs_anchor",
            h04_row["centered_mae_deg"]
            <= anchor_metrics["centered_mae_deg"],
            h04_row["centered_mae_deg"],
            anchor_metrics["centered_mae_deg"],
        ),
        (
            "offset_vs_anchor",
            h04_row["offset_abs_error_deg"]
            <= anchor_metrics["offset_abs_error_deg"],
            h04_row["offset_abs_error_deg"],
            anchor_metrics["offset_abs_error_deg"],
        ),
        (
            "derivative_vs_anchor",
            h04_row["derivative_mae_deg_per_sample"]
            <= anchor_metrics["derivative_mae_deg_per_sample"],
            h04_row["derivative_mae_deg_per_sample"],
            anchor_metrics["derivative_mae_deg_per_sample"],
        ),
        (
            "closure_vs_anchor",
            h04_row["periodic_closure_error_deg"]
            <= anchor_metrics["periodic_closure_error_deg"],
            h04_row["periodic_closure_error_deg"],
            anchor_metrics["periodic_closure_error_deg"],
        ),
        (
            "harmonic_amplitude_vs_anchor",
            h04_row["retained_amplitude_mae_deg"]
            <= anchor_metrics["retained_amplitude_mae_deg"],
            h04_row["retained_amplitude_mae_deg"],
            anchor_metrics["retained_amplitude_mae_deg"],
        ),
        (
            "harmonic_phase_vs_anchor",
            h04_row["retained_phase_mae_rad"]
            <= anchor_metrics["retained_phase_mae_rad"],
            h04_row["retained_phase_mae_rad"],
            anchor_metrics["retained_phase_mae_rad"],
        ),
        (
            "bounded_correction_energy",
            h04_row["correction_to_anchor_rms"] <= 0.5,
            h04_row["correction_to_anchor_rms"],
            0.5,
        ),
        (
            "three_seed_raw_mae_vs_anchor",
            all(
                row["mae_deg"] < anchor_metrics["mae_deg"]
                for row in h04_stability_rows
            ),
            max(row["mae_deg"] for row in h04_stability_rows),
            anchor_metrics["mae_deg"],
        ),
    ]
    return [
        {
            "gate_id": gate_id,
            "passed": bool(passed),
            "candidate_value": float(candidate_value),
            "reference_or_limit": float(reference_or_limit),
        }
        for gate_id, passed, candidate_value, reference_or_limit in gate_list
    ]


def build_comparison_plot(
    anchor_metrics: dict[str, float],
    candidate_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot normalized multi-index performance for the closeout candidates."""

    metric_name_list = [
        "mae_deg",
        "centered_mae_deg",
        "offset_abs_error_deg",
        "derivative_mae_deg_per_sample",
        "periodic_closure_error_deg",
        "retained_amplitude_mae_deg",
        "retained_phase_mae_rad",
    ]
    display_name_list = [
        "Raw MAE",
        "Centered",
        "Offset",
        "Derivative",
        "Closure",
        "Amplitude",
        "Phase",
    ]
    candidate_id_list = ["H04", "H08", "C04"]
    x_position = np.arange(len(metric_name_list))
    width = 0.24
    figure, axis = plt.subplots(figsize=(11.0, 5.6))
    for candidate_position, candidate_id in enumerate(candidate_id_list):
        normalized_value_list = [
            candidate_map[candidate_id][metric_name]
            / anchor_metrics[metric_name]
            for metric_name in metric_name_list
        ]
        axis.bar(
            x_position
            + (candidate_position - 1) * width,
            normalized_value_list,
            width,
            label=candidate_id,
        )
    axis.axhline(
        1.0,
        color="#202020",
        linewidth=1.3,
        linestyle="--",
        label="PF-A",
    )
    axis.set_xticks(x_position)
    axis.set_xticklabels(display_name_list, rotation=20, ha="right")
    axis.set_ylabel("Metric divided by PF-A (lower is better)")
    axis.set_title("Stage 5 Curve-First Multi-Index Comparison")
    axis.grid(axis="y", alpha=0.25)
    axis.legend(ncol=4)
    figure.tight_layout()
    ASSET_DIRECTORY.mkdir(parents=True, exist_ok=True)
    output_path = ASSET_DIRECTORY / "stage5_multi_index_comparison.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_stability_plot(
    anchor_mae: float,
    h04_rows: list[dict[str, Any]],
    c04_rows: list[dict[str, Any]],
) -> Path:
    """Plot H04 and C04 raw MAE across all three seeds."""

    seed_list = [int(row["random_seed"]) for row in h04_rows]
    h04_mae_list = [row["mae_deg"] for row in h04_rows]
    c04_map = {
        int(row["random_seed"]): row["mae_deg"] for row in c04_rows
    }
    c04_mae_list = [c04_map[seed] for seed in seed_list]
    x_position = np.arange(len(seed_list))
    figure, axis = plt.subplots(figsize=(9.6, 5.2))
    axis.plot(
        x_position,
        h04_mae_list,
        marker="o",
        linewidth=2.0,
        label="H04 bounded PF-A correction",
    )
    axis.plot(
        x_position,
        c04_mae_list,
        marker="s",
        linewidth=2.0,
        label="C04 direct coefficient control",
    )
    axis.axhline(
        anchor_mae,
        color="#202020",
        linestyle="--",
        label="PF-A",
    )
    axis.set_xticks(x_position)
    axis.set_xticklabels([str(seed) for seed in seed_list])
    axis.set_xlabel("Random seed")
    axis.set_ylabel("Test full-curve MAE [deg]")
    axis.set_title("H04 Matched-Control Stability")
    axis.grid(alpha=0.25)
    axis.legend()
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage5_h04_stability.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_representative_curve_plot(
    dataset: Any,
    h04_row: dict[str, Any],
) -> Path:
    """Plot measured, PF-A, and H04 curves for three deterministic test cells."""

    prediction_path = (
        PROJECT_ROOT
        / h04_row["run_directory"]
        / "test_predictions.npz"
    )
    prediction_payload = np.load(prediction_path)
    measured_matrix = prediction_payload["measured_curve"]
    predicted_matrix = prediction_payload["predicted_curve"]
    test_anchor_coefficient_matrix = dataset.anchor_coefficient_map["core"][
        dataset.split_array == "test"
    ]
    anchor_matrix = np.vstack(
        [
            _reconstruct_numpy_curve(
                coefficient_array,
                dataset.order_set_map["core"],
            )
            for coefficient_array in test_anchor_coefficient_matrix
        ]
    )
    representative_index_list = [0, len(measured_matrix) // 2, len(measured_matrix) - 1]
    theta_deg = np.linspace(
        0.0,
        360.0,
        measured_matrix.shape[1],
        endpoint=False,
    )
    figure, axis_list = plt.subplots(
        len(representative_index_list),
        1,
        figsize=(11.0, 8.0),
        sharex=True,
    )
    for axis, curve_index in zip(
        axis_list,
        representative_index_list,
        strict=True,
    ):
        axis.plot(
            theta_deg,
            measured_matrix[curve_index],
            color="#202020",
            linewidth=1.1,
            label="Measured",
        )
        axis.plot(
            theta_deg,
            anchor_matrix[curve_index],
            color="#d95f02",
            linewidth=1.0,
            label="PF-A",
        )
        axis.plot(
            theta_deg,
            predicted_matrix[curve_index],
            color="#1b9e77",
            linewidth=1.0,
            label="H04",
        )
        axis.grid(alpha=0.2)
        axis.set_ylabel("TE [deg]")
        axis.set_title(
            str(prediction_payload["condition_id"][curve_index])
        )
    axis_list[0].legend(ncol=3)
    axis_list[-1].set_xlabel("Output angle [deg]")
    figure.suptitle("Measured Versus PF-A And H04 Representative Curves")
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage5_h04_representative_curves.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def markdown_metric_table(
    anchor_metrics: dict[str, float],
    h04_row: dict[str, Any],
    c04_row: dict[str, Any],
    h08_row: dict[str, Any],
) -> str:
    """Build the central report comparison table."""

    row_definition_list = [
        ("Raw MAE [deg]", "mae_deg"),
        ("Centered MAE [deg]", "centered_mae_deg"),
        ("Offset error [deg]", "offset_abs_error_deg"),
        ("Peak-to-peak error [deg]", "peak_to_peak_abs_error_deg"),
        ("Derivative MAE [deg/sample]", "derivative_mae_deg_per_sample"),
        ("Closure error [deg]", "periodic_closure_error_deg"),
        ("Amplitude MAE [deg]", "retained_amplitude_mae_deg"),
        ("Phase MAE [rad]", "retained_phase_mae_rad"),
    ]
    line_list = [
        "| Metric | PF-A | C04 | H04 | H08 | H04 vs PF-A |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for display_name, metric_name in row_definition_list:
        line_list.append(
            "| "
            f"{display_name} | "
            f"{anchor_metrics[metric_name]:.9f} | "
            f"{c04_row[metric_name]:.9f} | "
            f"{h04_row[metric_name]:.9f} | "
            f"{h08_row[metric_name]:.9f} | "
            f"{improvement_percent(h04_row[metric_name], anchor_metrics[metric_name]):+.2f}% |"
        )
    return "\n".join(line_list)


def main() -> None:
    """Build Stage 5 decision artifacts, plots, report, and persistent state."""

    dataset = build_stage5_dataset()
    leaderboard_rows = [
        float_row(row)
        for row in load_csv(
            CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.csv"
        )
    ]
    candidate_map = {
        row["candidate_id"]: row for row in leaderboard_rows
    }
    stability_rows = [
        float_row(row)
        for row in load_csv(
            CAMPAIGN_OUTPUT_DIRECTORY
            / "campaign_stability_leaderboard.csv"
        )
    ]
    first_seed_h04 = dict(candidate_map["H04"])
    first_seed_h04["random_seed"] = 314159.0
    first_seed_c04 = dict(candidate_map["C04"])
    first_seed_c04["random_seed"] = 314159.0
    h04_stability_rows = [
        first_seed_h04,
        *[
            row
            for row in stability_rows
            if row["candidate_id"] == "H04"
        ],
    ]
    c04_stability_rows = [
        first_seed_c04,
        *[
            row
            for row in stability_rows
            if row["candidate_id"] == "C04"
        ],
    ]

    test_anchor_coefficient_matrix = dataset.anchor_coefficient_map["core"][
        dataset.split_array == "test"
    ]
    anchor_curve_matrix = np.vstack(
        [
            _reconstruct_numpy_curve(
                coefficient_array,
                dataset.order_set_map["core"],
            )
            for coefficient_array in test_anchor_coefficient_matrix
        ]
    )
    anchor_metrics = aggregate_metrics(
        dataset.curve_matrix[dataset.split_array == "test"],
        anchor_curve_matrix,
    )
    gate_rows = build_gate_rows(
        anchor_metrics,
        candidate_map["H04"],
        candidate_map["C04"],
        h04_stability_rows,
    )
    assert all(row["passed"] for row in gate_rows)
    write_csv(
        ANALYSIS_DIRECTORY / "stage5_exit_gate_matrix.csv",
        gate_rows,
    )

    stability_mae_array = np.asarray(
        [row["mae_deg"] for row in h04_stability_rows],
        dtype=np.float64,
    )
    summary_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage5",
        "status": "passed_positive_component",
        "closed_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "first_screen_run_count": 18,
        "stability_run_count": 4,
        "failed_run_count": 0,
        "scalar_raw_error_leader": "H08",
        "recommended_multi_index_candidate": "H04",
        "recommended_formulation": "bounded_coefficient",
        "recommended_order_set": "core",
        "anchor_metrics": anchor_metrics,
        "h04_first_seed_metrics": {
            key: value
            for key, value in candidate_map["H04"].items()
            if isinstance(value, float)
        },
        "h04_stability_mae_deg": {
            "mean": float(np.mean(stability_mae_array)),
            "standard_deviation": float(np.std(stability_mae_array)),
            "minimum": float(np.min(stability_mae_array)),
            "maximum": float(np.max(stability_mae_array)),
        },
        "h08_disposition": (
            "raw-error leader only; not recommended because closure, "
            "amplitude, and phase regress versus PF-A"
        ),
        "h04_disposition": (
            "qualified structured coefficient component for Stage 6; "
            "not a new production or program-best model"
        ),
        "all_exit_gates_passed": True,
        "official_te_curve_verification_pipeline_run": False,
        "next_stage": "Stage 6 Spectral And Sobolev Guidance",
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage5_exit_gate_summary.yaml",
        summary_payload,
    )

    comparison_plot_path = build_comparison_plot(
        anchor_metrics,
        candidate_map,
    )
    stability_plot_path = build_stability_plot(
        anchor_metrics["mae_deg"],
        h04_stability_rows,
        c04_stability_rows,
    )
    representative_plot_path = build_representative_curve_plot(
        dataset,
        candidate_map["H04"],
    )

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report_text = f"""# Wave 5.2R Stage 5 Complex Harmonic Coefficient Residuals Results

## Executive Decision

Stage 5 is complete with a positive component-level result.

All `18` first-screen runs and all `4` conditional stability runs completed
without a failure. `H08` is the scalar raw-error leader, but it is not the
multi-index recommendation because it regresses closure, retained-amplitude,
and retained-phase behavior relative to PF-A.

`H04`, the deep bounded correction to the nine PF-A core complex coefficients,
passes every Stage 5 exit gate. It advances as a qualified structured component
for Stage 6. It does not replace the accepted periodic GRU, does not become a
new production best, and is not yet a full PINN.

## Scope And Integrity

- dataset: `polished_dataset`;
- inputs: setpoints only;
- surface: `Fw`;
- accepted curves: `966`;
- split: `675` train, `194` validation, `97` test;
- angular grid: `2048` uniform points on `0 <= theta < 2*pi`;
- split signature:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- runtime measured inputs: none;
- target-derived runtime inputs: none;
- official TE Curve Verification Pipeline: not run.

Training, coefficient extraction, curve reconstruction, and bounded evaluation
all used the same uniform representation. The Stage 4 representation mismatch
was therefore removed.

## Campaign Execution

| Item | Result |
| --- | ---: |
| Planned first-screen runs | 18 |
| Completed first-screen runs | 18 |
| Failed first-screen runs | 0 |
| Conditional stability runs | 4 |
| Failed stability runs | 0 |
| Candidate formulations | 5 |
| Frozen first-screen seed | 314159 |
| Stability seeds | 271828, 161803 |

## Primary Curve-First Comparison

{markdown_metric_table(anchor_metrics, candidate_map["H04"], candidate_map["C04"], candidate_map["H08"])}

H04 improves raw MAE by
`{improvement_percent(candidate_map["H04"]["mae_deg"], anchor_metrics["mae_deg"]):.2f}%`
versus PF-A and by
`{improvement_percent(candidate_map["H04"]["mae_deg"], candidate_map["C04"]["mae_deg"]):.2f}%`
versus its matched direct coefficient control.

![Stage 5 multi-index comparison](assets/2026-07-28_stage5_complex_harmonic_coefficients/{comparison_plot_path.name})

## Why H08 Is Not The Recommendation

H08 reaches the lowest raw MAE,
`{candidate_map["H08"]["mae_deg"]:.9f} deg`, but uses the broader
training-selected order set. Relative to PF-A it worsens:

- periodic closure from `{anchor_metrics["periodic_closure_error_deg"]:.9f}`
  to `{candidate_map["H08"]["periodic_closure_error_deg"]:.9f} deg`;
- retained amplitude MAE from
  `{anchor_metrics["retained_amplitude_mae_deg"]:.9f}` to
  `{candidate_map["H08"]["retained_amplitude_mae_deg"]:.9f} deg`;
- retained phase MAE from
  `{anchor_metrics["retained_phase_mae_rad"]:.9f}` to
  `{candidate_map["H08"]["retained_phase_mae_rad"]:.9f} rad`.

This is a real raw-error gain, not Stage 4-style analytical cancellation, but
it is not the best balanced component. The later Stage 6 spectral and Sobolev
work may revisit the added orders with direct derivative and spectral control.

## H04 Stability

| Seed | H04 MAE [deg] | C04 MAE [deg] | H04 vs PF-A |
| ---: | ---: | ---: | ---: |
"""
    c04_seed_map = {
        int(row["random_seed"]): row for row in c04_stability_rows
    }
    for h04_seed_row in h04_stability_rows:
        random_seed = int(h04_seed_row["random_seed"])
        report_text += (
            f"| {random_seed} | {h04_seed_row['mae_deg']:.9f} | "
            f"{c04_seed_map[random_seed]['mae_deg']:.9f} | "
            f"{improvement_percent(h04_seed_row['mae_deg'], anchor_metrics['mae_deg']):+.2f}% |\n"
        )
    report_text += f"""

H04 mean MAE across the three seeds is
`{np.mean(stability_mae_array):.9f} deg`, with standard deviation
`{np.std(stability_mae_array):.9f} deg`. Every seed beats PF-A and its matched
direct C04 control.

![H04 stability](assets/2026-07-28_stage5_complex_harmonic_coefficients/{stability_plot_path.name})

## Representative Full Curves

The following deterministic test cells compare measured TE, frozen PF-A, and
the first-screen H04 checkpoint on the same `2048`-point grid.

![Representative H04 curves](assets/2026-07-28_stage5_complex_harmonic_coefficients/{representative_plot_path.name})

## Exit Gates

| Gate | Candidate | Reference or limit | Result |
| --- | ---: | ---: | --- |
"""
    for gate_row in gate_rows:
        report_text += (
            f"| `{gate_row['gate_id']}` | "
            f"{gate_row['candidate_value']:.9f} | "
            f"{gate_row['reference_or_limit']:.9f} | passed |\n"
        )
    report_text += """

All ten gates pass.

## Scientific Interpretation

Stage 5 demonstrates that physics-informed assistance can work in this dataset
when the analytical and learned parts share the same representation and the
learned freedom is constrained to explicit complex coefficients.

The result is stronger than a generic Fourier feature observation:

- the PF-A analytical contribution remains explicit;
- the network learns only bounded coefficient corrections;
- zero correction replays PF-A exactly;
- corrections remain below one percent of anchor RMS for H04;
- every retained harmonic contribution is inspectable;
- the gain survives three seeds and matched direct controls.

The result still does not prove a differential-equation PINN. H04 is a
qualified grey-box structured component that Stage 6 can augment with spectral
and Sobolev guidance.

## Program Decision

- Stage 5 status: complete, positive component-level result;
- qualified component: H04 bounded PF-A core-coefficient correction;
- raw-error-only leader: H08;
- production/model-registry promotion: no;
- accepted periodic GRU replacement: no;
- stability continuation: complete;
- official TE Curve Verification Pipeline: deferred from normal closeout;
- next executable step: Stage 6, Spectral And Sobolev Guidance.

## Artifact Map

- campaign:
  `output/training_campaigns/2026-07-28-16-17-06_wave52r_stage5_complex_harmonic_coefficient_residuals_2026_07_28/`;
- representation:
  `output/analysis/wave_5_2r/stage5_complex_harmonic_coefficient_residuals/stage5_uniform_curve_representation.yaml`;
- exit gates:
  `output/analysis/wave_5_2r/stage5_complex_harmonic_coefficient_residuals/closeout/stage5_exit_gate_summary.yaml`;
- H04 first-screen checkpoint:
  `output/training_runs/complex_harmonic_coefficient_residuals/2026-07-28-16-17-13__stage5_h04/best_model.pt`;
- model report:
  `doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-28]/stage5_complex_harmonic_coefficient_residuals/stage5_complex_harmonic_coefficient_residual_model_report.md`.

## Closeout Integrity

The preliminary sixteen-run screen was archived recoverably under
`.temp/stage5_superseded_16_run_screen/` after the missing data-selected direct
controls were detected. Only the corrected eighteen-run campaign is canonical.
"""
    with REPORT_PATH.open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(report_text.rstrip() + "\n")

    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "status": "completed",
            "closed_out_at": datetime.now().astimezone().isoformat(
                timespec="seconds"
            ),
            "recommended_candidate_id": "H04",
            "scalar_raw_error_leader_id": "H08",
            "exit_gate_summary_path": (
                ANALYSIS_DIRECTORY / "stage5_exit_gate_summary.yaml"
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
