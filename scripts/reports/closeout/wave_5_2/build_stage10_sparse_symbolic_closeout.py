"""Build the Wave 5.2R Stage 10 sparse-symbolic closeout."""

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
    / "2026-07-29-20-21-49_wave52r_stage10_sparse_symbolic_"
    "discovery_2026_07_29"
)
RUN_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "sparse_symbolic_formulation_discovery"
)
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage10_sparse_symbolic_formulation_discovery"
    / "closeout"
)
REPORT_PATH = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "2026-07-29-20-23-30_wave52r_stage10_sparse_and_symbolic_"
    "formulation_discovery_results_report.md"
)
ASSET_DIRECTORY = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "assets"
    / "2026-07-29_stage10_sparse_symbolic_discovery"
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


def run_directory(candidate_id: str) -> Path:
    """Resolve one unique Stage 10 fitted-run directory."""

    path_list = list(
        RUN_ROOT_DIRECTORY.glob(f"*__stage10_{candidate_id.lower()}")
    )
    assert len(path_list) == 1
    return path_list[0]


def build_multi_index_plot(row_map: dict[str, dict[str, Any]]) -> Path:
    """Plot errors normalized to the complete-quadratic control."""

    metric_list = [
        ("mae_deg", "Raw"),
        ("mean_mae_deg", "Mean"),
        ("centered_shape_mae_deg", "Shape"),
        ("sobolev_derivative_mae", "Derivative"),
        ("retained_amplitude_mae_deg", "Amplitude"),
        ("per_curve_mae_p95", "P95"),
    ]
    candidate_id_list = ["D01", "Q00", "R00", "S01", "S02", "S03", "Y01"]
    color_list = [
        "#6B7280",
        "#202020",
        "#005A9C",
        "#2E8B57",
        "#D97706",
        "#8B5CF6",
        "#B91C1C",
    ]
    x_position_array = np.arange(len(metric_list))
    width = 0.115
    figure, axis = plt.subplots(figsize=(11.5, 6.1))
    for candidate_index, (candidate_id, color) in enumerate(
        zip(candidate_id_list, color_list, strict=True)
    ):
        normalized_value_list = [
            float(row_map[candidate_id][metric_name])
            / float(row_map["Q00"][metric_name])
            for metric_name, _ in metric_list
        ]
        axis.bar(
            x_position_array + (candidate_index - 3.0) * width,
            normalized_value_list,
            width,
            color=color,
            label=candidate_id,
        )
    axis.axhline(1.0, color="#202020", linestyle="--", linewidth=1.0)
    axis.set_xticks(x_position_array)
    axis.set_xticklabels([label for _, label in metric_list])
    axis.set_ylabel("Normalized error vs Q00 (lower is better)")
    axis.set_title("Stage 10 Multi-Index Comparison")
    axis.grid(axis="y", alpha=0.22)
    axis.legend(ncol=7, fontsize=8)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage10_multi_index_comparison.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_complexity_tradeoff_plot(
    row_map: dict[str, dict[str, Any]],
) -> Path:
    """Plot raw error against active coefficient slots."""

    candidate_id_list = ["Q00", "R00", "S01", "S02", "S03", "Y01", "N01"]
    figure, axis = plt.subplots(figsize=(8.8, 6.0))
    for candidate_id in candidate_id_list:
        row = row_map[candidate_id]
        color = "#B91C1C" if candidate_id == "Y01" else "#005A9C"
        axis.scatter(
            float(row["active_fraction"]),
            float(row["mae_deg"]),
            s=70 if candidate_id == "Y01" else 48,
            color=color,
        )
        axis.annotate(
            candidate_id,
            (
                float(row["active_fraction"]),
                float(row["mae_deg"]),
            ),
            xytext=(6, 5),
            textcoords="offset points",
        )
    axis.axvline(
        0.40,
        color="#D97706",
        linestyle="--",
        label="Complexity gate",
    )
    axis.axhline(
        float(row_map["Q00"]["mae_deg"]),
        color="#202020",
        linestyle="--",
        label="Q00 raw MAE",
    )
    axis.set_xlabel("Active coefficient-slot fraction")
    axis.set_ylabel("Raw test MAE [deg]")
    axis.set_title("Accuracy-Complexity Tradeoff")
    axis.grid(alpha=0.22)
    axis.legend()
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage10_complexity_tradeoff.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_stability_plot() -> Path:
    """Plot selected-term stability for S02 and Y01."""

    candidate_id_list = ["S02", "S03", "Y01", "N01"]
    probability_list: list[float] = []
    sign_list: list[float] = []
    for candidate_id in candidate_id_list:
        with np.load(
            run_directory(candidate_id) / "model_parameters.npz"
        ) as payload:
            coefficient_matrix = payload["coefficient_matrix"]
            active_mask = np.abs(coefficient_matrix) > 0.0
            probability_list.append(
                float(np.median(payload["selection_probability"][active_mask]))
            )
            sign_list.append(
                float(np.median(payload["sign_agreement"][active_mask]))
            )
    x_position_array = np.arange(len(candidate_id_list))
    figure, axis = plt.subplots(figsize=(8.8, 5.5))
    axis.bar(
        x_position_array - 0.18,
        probability_list,
        0.36,
        color="#005A9C",
        label="Median selection probability",
    )
    axis.bar(
        x_position_array + 0.18,
        sign_list,
        0.36,
        color="#D97706",
        label="Median sign agreement",
    )
    axis.axhline(0.75, color="#005A9C", linestyle="--", linewidth=1.0)
    axis.axhline(0.85, color="#D97706", linestyle="--", linewidth=1.0)
    axis.set_xticks(x_position_array)
    axis.set_xticklabels(candidate_id_list)
    axis.set_ylim(0.0, 1.05)
    axis.set_ylabel("Bootstrap stability")
    axis.set_title("Selected-Term Bootstrap Stability")
    axis.grid(axis="y", alpha=0.22)
    axis.legend()
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage10_bootstrap_stability.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def build_representative_curve_plot() -> Path:
    """Plot one representative measured and sparse-model curve."""

    payload_map: dict[str, dict[str, np.ndarray]] = {}
    for candidate_id in ["Q00", "R00", "S02", "Y01"]:
        with np.load(
            run_directory(candidate_id) / "test_predictions.npz"
        ) as payload:
            payload_map[candidate_id] = {
                key: payload[key] for key in payload.files
            }
    reference_payload = payload_map["R00"]
    curve_mae_array = np.mean(
        np.abs(
            reference_payload["predicted_curve"]
            - reference_payload["measured_curve"]
        ),
        axis=1,
    )
    curve_index = int(np.argsort(curve_mae_array)[len(curve_mae_array) // 2])
    angle_array = np.linspace(
        0.0,
        360.0,
        reference_payload["measured_curve"].shape[1],
        endpoint=False,
    )
    figure, axis = plt.subplots(figsize=(11.3, 5.7))
    axis.plot(
        angle_array,
        reference_payload["measured_curve"][curve_index],
        color="#202020",
        linewidth=1.8,
        label="Measured",
    )
    style_map = {
        "Q00": ("#6B7280", "--"),
        "R00": ("#005A9C", "-"),
        "S02": ("#D97706", "-"),
        "Y01": ("#B91C1C", "-"),
    }
    for candidate_id, (color, line_style) in style_map.items():
        axis.plot(
            angle_array,
            payload_map[candidate_id]["predicted_curve"][curve_index],
            color=color,
            linestyle=line_style,
            linewidth=1.0,
            label=candidate_id,
        )
    axis.set_xlabel("Output angle [deg]")
    axis.set_ylabel("Transmission error [deg]")
    axis.set_title(f"Representative Test Curve (index {curve_index})")
    axis.grid(alpha=0.2)
    axis.legend(ncol=5)
    figure.tight_layout()
    output_path = ASSET_DIRECTORY / "stage10_representative_curve.png"
    figure.savefig(output_path, dpi=180)
    plt.close(figure)
    return output_path


def main() -> None:
    """Generate Stage 10 plots, decision record, and Markdown report."""

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
    q00_row = row_map["Q00"]
    r00_row = row_map["R00"]
    y01_row = row_map["Y01"]
    summary_payload = {
        "schema_version": 1,
        "stage": "Wave 5.2R Stage 10",
        "status": "completed_without_qualified_sparse_terms",
        "completed_entry_count": 10,
        "failed_entry_count": 0,
        "raw_error_leader_id": "D02",
        "best_discovery_candidate_id": "R00",
        "recommended_candidate_id": None,
        "passing_candidate_id_list": gate_payload[
            "passing_candidate_id_list"
        ],
        "r00_improvement_percent_vs_q00": {
            "raw_mae": improvement_percent(
                float(r00_row["mae_deg"]), float(q00_row["mae_deg"])
            ),
            "mean_mae": improvement_percent(
                float(r00_row["mean_mae_deg"]),
                float(q00_row["mean_mae_deg"]),
            ),
            "shape_mae": improvement_percent(
                float(r00_row["centered_shape_mae_deg"]),
                float(q00_row["centered_shape_mae_deg"]),
            ),
        },
        "most_compact_real_candidate": {
            "candidate_id": "Y01",
            "active_fraction": y01_row["active_fraction"],
            "active_term_count": y01_row["active_term_count"],
        },
        "decision": (
            "The extended library contains predictive interactions, but no "
            "candidate is simultaneously stable, low-complexity, and better "
            "than Q00 on raw and centered-shape error."
        ),
        "next_stage": "Wave 5.2R Stage 11 uncertainty and physics-trust calibration",
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage10_exit_gate_summary.yaml",
        summary_payload,
    )
    plot_path_list = [
        build_multi_index_plot(row_map),
        build_complexity_tradeoff_plot(row_map),
        build_stability_plot(),
        build_representative_curve_plot(),
    ]
    relative_plot_path_list = [
        path.relative_to(REPORT_PATH.parent).as_posix()
        for path in plot_path_list
    ]
    report_text = f"""# Wave 5.2R Stage 10 Sparse And Symbolic Formulation Discovery Results

## Executive Summary

Stage 10 completed all ten diagnostic and fitted entries without runtime
failure. The extended condition library contains useful predictive structure:
dense ridge `R00` improved raw MAE by
{summary_payload['r00_improvement_percent_vs_q00']['raw_mae']:.2f}% and mean
error by {summary_payload['r00_improvement_percent_vs_q00']['mean_mae']:.2f}%
relative to the complete-quadratic `Q00` control.

No sparse or constrained-symbolic candidate passed the full exit gate. The
candidate laws improved raw error but did not improve centered-shape error,
retained too many coefficient slots, and exposed weak sign stability in their
least stable selected terms. No expression is promoted or relabeled as a
physical law.

## Scope And Method

- Dataset: polished dataset, setpoint inputs, forward surface only.
- Split: frozen Stage 0 `675/194/97` grouped split.
- Harmonic representation: offset plus Stage 5 core sine/cosine orders.
- Baselines: PF-A, H04, and Stage 9 K01.
- Sparse selection: train-only threshold selection and `96` deterministic
  bootstraps.
- Validation: bounded alpha and threshold grid.
- Test access: one evaluation after term definitions were frozen.
- Runtime target-derived inputs: zero.

## First-Screen Results

| ID | Formulation | Raw MAE | Mean MAE | Shape MAE | Active fraction | Coefficient MAE |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
"""
    for candidate_id in [
        "D02",
        "R00",
        "S01",
        "S03",
        "S02",
        "Y01",
        "D01",
        "D00",
        "Q00",
        "N01",
    ]:
        row = row_map[candidate_id]
        coefficient_text = (
            "N/A"
            if not np.isfinite(float(row["coefficient_mae"]))
            else f"{float(row['coefficient_mae']):.6f}"
        )
        report_text += (
            f"| `{candidate_id}` | `{row['formulation']}` | "
            f"{float(row['mae_deg']):.6f} | "
            f"{float(row['mean_mae_deg']):.6f} | "
            f"{float(row['centered_shape_mae_deg']):.6f} | "
            f"{float(row['active_fraction']):.3f} | "
            f"{coefficient_text} |\n"
        )
    report_text += f"""
![Stage 10 multi-index comparison]({relative_plot_path_list[0]})

## What Worked

`R00` reached raw MAE `{float(r00_row['mae_deg']):.6f} deg`, compared with
`{float(q00_row['mae_deg']):.6f} deg` for `Q00`. The result demonstrates that
the extended library contains condition interactions absent from the complete
quadratic control.

All discovered laws remain periodic by construction. Their closure metrics
stay near the analytical references, deterministic replay is exact, and no
runtime target-derived feature is used.

The sparse and symbolic candidates also beat the shuffled-label control on raw
and coefficient error. Their improvement is therefore not reproduced by the
specificity control.

![Accuracy-complexity tradeoff]({relative_plot_path_list[1]})

![Representative measured and predicted curve]({relative_plot_path_list[3]})

## What Did Not Pass

The predictive gain was not parsimonious enough. Active fractions were:

- `S01`: `{float(row_map['S01']['active_fraction']):.3f}`;
- `S02`: `{float(row_map['S02']['active_fraction']):.3f}`;
- `S03`: `{float(row_map['S03']['active_fraction']):.3f}`;
- `Y01`: `{float(row_map['Y01']['active_fraction']):.3f}`.

The predeclared maximum was `0.40`. The most compact real candidate, `Y01`,
still retained {int(y01_row['active_term_count'])} of
{int(y01_row['dense_coefficient_slot_count'])} coefficient slots.

No sparse candidate improved centered-shape MAE over `Q00`. The least-stable
selected signs in the bootstrap candidates fell to approximately `0.53`, well
below the required `0.85`. Strong hierarchy added parent terms but could not
repair stability or complexity.

### Stability Diagnostic

![Bootstrap term stability]({relative_plot_path_list[2]})

## Scientific Interpretation

Stage 10 finds evidence for nonlinear condition interactions, but not for one
small universal correction law. The extended dense library improves curve
level and mean behavior while the shape surface remains difficult. This
suggests that useful interactions are distributed across harmonic channels or
that correlated library terms can exchange explanatory weight.

The correct conclusion is narrower than “symbolic regression failed.” A
predeclared compact library did not yield a stable low-complexity term set
under the current split and thresholds. Dense-library evidence can inform
future neural feature design, but it is not promoted as identified physics.

## Decision

- Stage 10 status: completed without qualified sparse terms.
- Official promoted candidate: none.
- Stable symbolic law: none.
- Diagnostic evidence retained: the extended library improves raw and mean
  error relative to the complete quadratic control.
- Stage 11 proceeds with uncertainty and physics-trust calibration.

## Reproducibility Evidence

- Campaign leaderboard:
  `output/training_campaigns/2026-07-29-20-21-49_wave52r_stage10_sparse_symbolic_discovery_2026_07_29/campaign_leaderboard.yaml`
- Gate summary:
  `output/training_campaigns/2026-07-29-20-21-49_wave52r_stage10_sparse_symbolic_discovery_2026_07_29/campaign_first_screen_gate_summary.yaml`
- Exit-gate summary:
  `output/analysis/wave_5_2r/stage10_sparse_symbolic_formulation_discovery/closeout/stage10_exit_gate_summary.yaml`
- Preflight:
  `output/analysis/wave_5_2r/stage10_sparse_symbolic_formulation_discovery/stage10_preflight_validation_summary.yaml`
"""
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_text, encoding="utf-8", newline="\n")
    print(REPORT_PATH)


if __name__ == "__main__":
    main()
