"""Build the Wave 5.2R Stage 9 temporal residual closeout."""

from __future__ import annotations

# Import Python Utilities
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
    / "2026-07-29-18-52-55_wave52r_stage9_temporal_analytical_"
    "residual_models_2026_07_29"
)
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage9_temporal_analytical_residual_models"
    / "closeout"
)
REPORT_PATH = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "2026-07-29-19-52-39_wave52r_stage9_temporal_analytical_"
    "residual_models_results_report.md"
)
ASSET_DIRECTORY = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "assets"
    / "2026-07-29_stage9_temporal_analytical_residual_models"
)
RUN_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "temporal_analytical_residual_models"
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


def improvement_percent(candidate_value: float, baseline_value: float) -> float:
    """Return positive improvement for a minimized metric."""

    return 100.0 * (baseline_value - candidate_value) / baseline_value


def build_multi_index_plot(row_map: dict[str, dict[str, Any]]) -> Path:
    """Plot normalized multi-index errors against frozen H04."""

    metric_list = [
        ("mae_deg", "Raw"),
        ("mean_mae_deg", "Mean"),
        ("centered_shape_mae_deg", "Shape"),
        ("sobolev_derivative_mae", "Derivative"),
        ("retained_amplitude_mae_deg", "Amplitude"),
        ("per_curve_mae_p95", "P95"),
    ]
    candidate_id_list = ["G00", "C00", "P01", "H01", "K01", "N01"]
    color_list = [
        "#6B7280",
        "#005A9C",
        "#2E8B57",
        "#D97706",
        "#B91C1C",
        "#8B5CF6",
    ]
    x_position_array = np.arange(len(metric_list))
    width = 0.13
    figure, axis = plt.subplots(figsize=(11.4, 5.8))
    for candidate_index, (candidate_id, color) in enumerate(
        zip(candidate_id_list, color_list, strict=True)
    ):
        normalized_array = [
            float(row_map[candidate_id][metric_name])
            / float(row_map["D00"][metric_name])
            for metric_name, _ in metric_list
        ]
        axis.bar(
            x_position_array + (candidate_index - 2.5) * width,
            normalized_array,
            width,
            color=color,
            label=candidate_id,
        )
    axis.axhline(1.0, color="#202020", linestyle="--", linewidth=1.2)
    axis.set_xticks(x_position_array)
    axis.set_xticklabels([label for _, label in metric_list])
    axis.set_ylabel("Normalized error vs H04 (lower is better)")
    axis.set_title("Stage 9 Multi-Index First Screen")
    axis.grid(axis="y", alpha=0.22)
    axis.legend(ncol=6, fontsize=8)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage9_multi_index_comparison.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_tradeoff_plot(row_map: dict[str, dict[str, Any]]) -> Path:
    """Plot mean-versus-shape error with raw MAE annotations."""

    candidate_id_list = [
        "D00",
        "G00",
        "C00",
        "R00",
        "P01",
        "H01",
        "K01",
        "M01",
        "L01",
        "N01",
    ]
    annotation_offset_map = {
        "D00": (8, 12),
        "G00": (8, 8),
        "C00": (8, -18),
        "R00": (8, -34),
        "P01": (8, 25),
        "H01": (8, 10),
        "K01": (8, 8),
        "M01": (8, 8),
        "L01": (8, -18),
        "N01": (8, 12),
    }
    figure, axis = plt.subplots(figsize=(8.8, 9.5))
    for candidate_id in candidate_id_list:
        row = row_map[candidate_id]
        color = "#B91C1C" if candidate_id == "K01" else "#005A9C"
        axis.scatter(
            float(row["mean_mae_deg"]),
            float(row["centered_shape_mae_deg"]),
            s=72 if candidate_id == "K01" else 45,
            color=color,
        )
        axis.annotate(
            f"{candidate_id}\nraw={float(row['mae_deg']):.6f}",
            (
                float(row["mean_mae_deg"]),
                float(row["centered_shape_mae_deg"]),
            ),
            xytext=annotation_offset_map[candidate_id],
            textcoords="offset points",
            fontsize=7.5,
        )
    axis.set_xlabel("Mean / offset MAE [deg]")
    axis.set_ylabel("Mean-centered shape MAE [deg]")
    axis.set_title("Offset-Shape Tradeoff")
    axis.grid(alpha=0.22)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage9_offset_shape_tradeoff.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def load_prediction(candidate_id: str) -> dict[str, np.ndarray]:
    """Load test predictions for one trainable candidate."""

    prediction_path_list = list(
        RUN_ROOT_DIRECTORY.glob(
            f"*__stage9_{candidate_id.lower()}/test_predictions.npz"
        )
    )
    assert len(prediction_path_list) == 1, (
        f"Expected one prediction file for {candidate_id}"
    )
    with np.load(prediction_path_list[0]) as payload:
        return {key: payload[key] for key in payload.files}


def build_representative_curve_plot() -> Path:
    """Plot representative curves for the anchor and temporal candidates."""

    k01_payload = load_prediction("K01")
    h01_payload = load_prediction("H01")
    n01_payload = load_prediction("N01")
    curve_mae_array = np.mean(
        np.abs(
            k01_payload["predicted_curve"] - k01_payload["measured_curve"]
        ),
        axis=1,
    )
    curve_index = int(np.argsort(curve_mae_array)[len(curve_mae_array) // 2])
    angle_array = np.linspace(
        0.0,
        360.0,
        k01_payload["measured_curve"].shape[1],
        endpoint=False,
    )
    figure, axis = plt.subplots(figsize=(11.4, 5.8))
    axis.plot(
        angle_array,
        k01_payload["measured_curve"][curve_index],
        color="#202020",
        linewidth=1.8,
        label="Measured",
    )
    axis.plot(
        angle_array,
        k01_payload["anchor_curve"][curve_index],
        color="#6B7280",
        linewidth=1.1,
        linestyle="--",
        label="H04 anchor",
    )
    axis.plot(
        angle_array,
        h01_payload["predicted_curve"][curve_index],
        color="#D97706",
        linewidth=1.0,
        label="H01 point residual",
    )
    axis.plot(
        angle_array,
        k01_payload["predicted_curve"][curve_index],
        color="#B91C1C",
        linewidth=1.2,
        label="K01 coefficient residual",
    )
    axis.plot(
        angle_array,
        n01_payload["predicted_curve"][curve_index],
        color="#8B5CF6",
        linewidth=0.9,
        alpha=0.85,
        label="N01 shuffled-order control",
    )
    axis.set_xlabel("Output angle [deg]")
    axis.set_ylabel("Transmission error [deg]")
    axis.set_title(f"Representative Test Curve (index {curve_index})")
    axis.grid(alpha=0.2)
    axis.legend(ncol=3, fontsize=8)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage9_representative_curve.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_prefix_plot(row_map: dict[str, dict[str, Any]]) -> Path:
    """Plot causal prefix accuracy."""

    prefix_length_list = [1, 9, 17, 33, 129, 512, 2048]
    candidate_id_list = ["C00", "P01", "H01", "K01", "L01", "N01"]
    figure, axis = plt.subplots(figsize=(9.2, 5.5))
    for candidate_id in candidate_id_list:
        axis.plot(
            prefix_length_list,
            [
                float(row_map[candidate_id][f"prefix_{length}_mae_deg"])
                for length in prefix_length_list
            ],
            marker="o",
            linewidth=1.4,
            label=candidate_id,
        )
    axis.set_xscale("log")
    axis.set_xlabel("Available causal prefix [samples]")
    axis.set_ylabel("Prefix MAE [deg]")
    axis.set_title("Causal Prefix Accuracy")
    axis.grid(alpha=0.22)
    axis.legend(ncol=3)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage9_prefix_accuracy.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_state_diagnostic_plot(row_map: dict[str, dict[str, Any]]) -> Path:
    """Plot hidden-state and chunk-equivalence diagnostics."""

    candidate_id_list = ["C00", "R00", "P01", "H01", "K01", "M01", "L01", "N01"]
    x_position_array = np.arange(len(candidate_id_list))
    chunk_array = np.asarray(
        [
            float(row_map[candidate_id]["chunk_equivalence_max_abs_deg"])
            for candidate_id in candidate_id_list
        ]
    )
    state_array = np.asarray(
        [
            float(row_map[candidate_id]["hidden_state_mean_norm"])
            for candidate_id in candidate_id_list
        ]
    )
    figure, first_axis = plt.subplots(figsize=(10.2, 5.5))
    first_axis.bar(
        x_position_array - 0.18,
        np.maximum(chunk_array, 1.0e-9),
        0.36,
        color="#005A9C",
        label="Chunk max difference",
    )
    first_axis.axhline(
        1.0e-6,
        color="#B91C1C",
        linestyle="--",
        linewidth=1.2,
        label="Declared tolerance",
    )
    first_axis.set_yscale("log")
    first_axis.set_ylabel("Chunk equivalence max abs [deg]")
    second_axis = first_axis.twinx()
    second_axis.bar(
        x_position_array + 0.18,
        state_array,
        0.36,
        color="#D97706",
        alpha=0.75,
        label="Hidden-state mean norm",
    )
    second_axis.set_ylabel("Hidden-state mean norm")
    first_axis.set_xticks(x_position_array)
    first_axis.set_xticklabels(candidate_id_list)
    first_axis.set_title("Temporal-State And Chunk Diagnostics")
    first_axis.grid(axis="y", alpha=0.2)
    first_axis.legend(loc="upper left", fontsize=8)
    second_axis.legend(loc="upper right", fontsize=8)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage9_state_chunk_diagnostics.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def main() -> None:
    """Generate Stage 9 plots, decision record, and Markdown report."""

    leaderboard_payload = load_yaml(
        CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.yaml"
    )
    gate_payload = load_yaml(
        CAMPAIGN_OUTPUT_DIRECTORY
        / "campaign_first_screen_gate_summary.yaml"
    )
    row_map = {
        row["candidate_id"]: row
        for row in leaderboard_payload["row_list"]
    }
    k01_row = row_map["K01"]
    h04_row = row_map["D00"]
    gru_row = row_map["G00"]
    summary_payload = {
        "schema_version": 1,
        "stage": "Wave 5.2R Stage 9",
        "status": "completed_without_promotion",
        "first_screen_completed_count": 10,
        "first_screen_failed_count": 0,
        "stability_completed_count": 0,
        "raw_error_leader_id": "K01",
        "recommended_candidate_id": None,
        "passing_candidate_id_list": gate_payload[
            "passing_candidate_id_list"
        ],
        "k01_metrics": {
            key: k01_row[key]
            for key in [
                "mae_deg",
                "mean_mae_deg",
                "centered_shape_mae_deg",
                "sobolev_derivative_mae",
                "periodic_closure_error_deg",
                "per_curve_mae_p95",
                "chunk_equivalence_max_abs_deg",
            ]
        },
        "k01_improvement_percent_vs_h04": {
            "raw_mae": improvement_percent(
                float(k01_row["mae_deg"]), float(h04_row["mae_deg"])
            ),
            "mean_mae": improvement_percent(
                float(k01_row["mean_mae_deg"]),
                float(h04_row["mean_mae_deg"]),
            ),
            "shape_mae": improvement_percent(
                float(k01_row["centered_shape_mae_deg"]),
                float(h04_row["centered_shape_mae_deg"]),
            ),
        },
        "accepted_gru_replay": {
            "candidate_id": "G00",
            "mae_deg": gru_row["mae_deg"],
            "checkpoint_path": gru_row["checkpoint_path"],
            "contract": "polished_dataset setpoints forward",
        },
        "decision": (
            "Retain K01 as a qualified research component, but do not "
            "promote it because closure, P95, and declared chunk-equivalence "
            "gates failed."
        ),
        "next_stage": "Wave 5.2R Stage 10 sparse and symbolic formulation discovery",
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage9_exit_gate_summary.yaml",
        summary_payload,
    )
    plot_path_list = [
        build_multi_index_plot(row_map),
        build_tradeoff_plot(row_map),
        build_representative_curve_plot(),
        build_prefix_plot(row_map),
        build_state_diagnostic_plot(row_map),
    ]
    relative_plot_path_list = [
        path.relative_to(REPORT_PATH.parent).as_posix()
        for path in plot_path_list
    ]
    report_text = f"""# Wave 5.2R Stage 9 Temporal Analytical-Residual Models Results

## Executive Summary

Stage 9 completed all 10 first-screen entries without runtime failures. The
causal coefficient-residual formulation `K01` is the clear scalar and component
leader: it improves raw MAE by
{summary_payload['k01_improvement_percent_vs_h04']['raw_mae']:.2f}%, mean
error by {summary_payload['k01_improvement_percent_vs_h04']['mean_mae']:.2f}%,
and mean-centered shape error by
{summary_payload['k01_improvement_percent_vs_h04']['shape_mae']:.2f}% relative
to the frozen `H04` analytical anchor.

No candidate passed the complete predeclared gate. The result is therefore a
scientifically useful temporal-residual lead, not an official model promotion.
`K01` is retained as a qualified research component for later integration and
repair work. Stage 10 remains the next roadmap step.

## Scope And Controls

- Dataset: polished dataset, setpoint inputs, forward surface only.
- Split: frozen Stage 0 grouped `675/194/97` train/validation/test split.
- Analytical anchor: frozen Stage 8 `H04`.
- Historical temporal comparator: archived
  `polished_setpoints_periodic_gru_sequence_Fw` checkpoint.
- Temporal contract: unidirectional two-layer GRU with explicit zero-state
  initialization and state carry across causal chunks.
- First-screen seed: `314159`.
- Target-derived runtime inputs: zero.

The historical `G00` replay was regenerated after detecting that the initial
campaign script referenced the older actual-values checkpoint. The corrected
replay uses the canonical five-input polished-setpoint forward archive,
including the forward direction flag. No candidate was retrained.

## First-Screen Results

| Candidate | Formulation | Raw MAE | Mean MAE | Shape MAE | Closure | P95 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
"""
    for candidate_id in [
        "K01",
        "L01",
        "H01",
        "P01",
        "N01",
        "M01",
        "D00",
        "C00",
        "R00",
        "G00",
    ]:
        row = row_map[candidate_id]
        report_text += (
            f"| `{candidate_id}` | `{row['formulation']}` | "
            f"{float(row['mae_deg']):.6f} | "
            f"{float(row['mean_mae_deg']):.6f} | "
            f"{float(row['centered_shape_mae_deg']):.6f} | "
            f"{float(row['periodic_closure_error_deg']):.6f} | "
            f"{float(row['per_curve_mae_p95']):.6f} |\n"
        )
    report_text += f"""
![Stage 9 multi-index comparison]({relative_plot_path_list[0]})

![Stage 9 offset-shape tradeoff]({relative_plot_path_list[1]})

## What Worked

The analytical anchor plus a learned temporal correction is materially better
than either constituent alone. `K01` reached raw MAE
`{float(k01_row['mae_deg']):.6f} deg`, mean MAE
`{float(k01_row['mean_mae_deg']):.6f} deg`, and shape MAE
`{float(k01_row['centered_shape_mae_deg']):.6f} deg`. It also beats the
corrected accepted GRU replay (`{float(gru_row['mae_deg']):.6f} deg`) and the
direct causal GRU control.

The coefficient-residual path was stronger than direct point residuals. This
supports the premise that the temporal network is most useful when it adjusts
an interpretable low-dimensional harmonic representation instead of freely
redrawing every angular sample.

`H01`, `K01`, and `L01` all beat the shuffled-order control on raw and mean
error. Chronological state therefore adds measurable value. However, the
shuffled control itself remains strong, showing that a substantial part of the
gain comes from angular features, analytical anchoring, and model capacity
rather than temporal ordering alone.

![Representative measured and predicted curve]({relative_plot_path_list[2]})

![Causal prefix accuracy]({relative_plot_path_list[3]})

## What Did Not Pass

The direct causal GRU control `C00` did not beat `H04`; its raw MAE was
`{float(row_map['C00']['mae_deg']):.6f} deg`. Temporal memory without the
analytical residual structure is therefore not sufficient on this screen.

All physics-guided candidates failed the strict complete gate:

- periodic closure was worse than the best retained baseline;
- per-curve P95 did not remain within the declared 2% tolerance;
- GPU one-pass versus 33-sample chunk evaluation exceeded the predeclared
  `1e-6 deg` maximum-difference tolerance.

The chunk deviations are small in absolute terms, from approximately
`1.25e-6` to `2.84e-5 deg`, and reset reproducibility remained exact. They are
consistent with numerical execution-order sensitivity, but the threshold is a
predeclared gate and was not relaxed after observing the results.

### Temporal-State Diagnostic

![Temporal-state and chunk diagnostics]({relative_plot_path_list[4]})

## Scientific Interpretation

Stage 9 validates the central hybrid-PINN argument: incomplete analytical
knowledge can guide the representation while a neural residual compensates for
missing effects. The strongest outcome is not a fully free neural sequence
model. It is a causal GRU operating on top of the `H04` harmonic anchor and
modifying harmonic coefficients.

The result is nevertheless not deployment-ready. The average behavior improves
strongly, while tail curves and periodic boundary consistency regress. Future
use of `K01` should therefore preserve its coefficient-residual structure but
add explicit boundary-consistent parameterization, tail-risk selection, and a
numerically calibrated chunk-equivalence audit.

## Decision

- Stage 9 status: completed without promotion.
- Official promoted candidate: none.
- Retained research component: `K01`.
- Stability repeats: not launched because no candidate passed every
  first-screen gate.
- Next roadmap action: Stage 10 sparse and symbolic formulation discovery.

## Reproducibility Evidence

- Campaign leaderboard:
  `output/training_campaigns/2026-07-29-18-52-55_wave52r_stage9_temporal_analytical_residual_models_2026_07_29/campaign_leaderboard.yaml`
- Gate summary:
  `output/training_campaigns/2026-07-29-18-52-55_wave52r_stage9_temporal_analytical_residual_models_2026_07_29/campaign_first_screen_gate_summary.yaml`
- Exit-gate summary:
  `output/analysis/wave_5_2r/stage9_temporal_analytical_residual_models/closeout/stage9_exit_gate_summary.yaml`
- Accepted GRU replay:
  `output/analysis/wave_5_2r/stage9_temporal_analytical_residual_models/stage9_accepted_gru_replay.npz`
"""
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_text, encoding="utf-8", newline="\n")
    print(REPORT_PATH)


if __name__ == "__main__":
    main()
