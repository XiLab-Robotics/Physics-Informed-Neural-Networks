"""Build the Wave 5.2R Stage 12 campaign closeout."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from datetime import datetime
from pathlib import Path
import sys
from typing import Any

# Import Scientific And Serialization Utilities
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import yaml


# Resolve Repository Paths
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
CAMPAIGN_NAME = (
    "wave52r_stage12_advanced_constraint_optimization_2026_07_29"
)
SPLIT_SIGNATURE = (
    "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16"
)
REPORT_TIMESTAMP = "2026-07-29-23-10-48"
REPORT_PATH = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / (
        f"{REPORT_TIMESTAMP}_wave52r_stage12_advanced_constraint_"
        "optimization_results_report.md"
    )
)
ASSET_DIRECTORY = (
    REPORT_PATH.parent
    / "assets"
    / "2026-07-29_stage12_advanced_constraint_optimization"
)
CLOSEOUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage12_advanced_constraint_optimization"
    / "closeout"
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


def find_campaign_directory() -> Path:
    """Resolve the unique latest completed Stage 12 campaign."""

    campaign_root = PROJECT_ROOT / "output" / "training_campaigns"
    candidate_list = sorted(
        [
            path
            for path in campaign_root.iterdir()
            if path.is_dir() and CAMPAIGN_NAME in path.name
        ],
        key=lambda path: path.stat().st_mtime,
    )
    assert candidate_list, "No completed Stage 12 campaign was found"
    campaign_directory = candidate_list[-1]
    execution = load_yaml(
        campaign_directory / "campaign_execution_summary.yaml"
    )
    assert execution["status"] == "completed"
    assert execution["completed_first_screen_count"] == 10
    assert execution["failed_first_screen_count"] == 0
    return campaign_directory


def read_leaderboard(campaign_directory: Path) -> list[dict[str, Any]]:
    """Read and type the Stage 12 leaderboard."""

    with (
        campaign_directory / "campaign_leaderboard.csv"
    ).open("r", encoding="utf-8", newline="") as input_file:
        row_list = list(csv.DictReader(input_file))
    assert len(row_list) == 10
    integer_field_set = {
        "random_seed",
        "best_epoch",
        "parameter_count",
        "runtime_target_derived_input_count",
        "lbfgs_evaluation_count",
    }
    text_field_set = {
        "candidate_id",
        "optimization_profile",
        "run_instance_id",
        "checkpoint_path",
    }
    typed_row_list: list[dict[str, Any]] = []
    for row in row_list:
        typed_row: dict[str, Any] = {}
        for key, value in row.items():
            if key in text_field_set:
                typed_row[key] = value
            elif key in integer_field_set:
                typed_row[key] = int(float(value))
            else:
                typed_row[key] = float(value)
        typed_row_list.append(typed_row)
    return typed_row_list


def plot_accuracy_surface(
    row_list: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """Plot raw, mean, and shape error relative to C01."""

    row_map = {row["candidate_id"]: row for row in row_list}
    control = row_map["C01"]
    candidate_id_list = [row["candidate_id"] for row in row_list]
    metric_list = [
        ("mae_deg", "Raw"),
        ("mean_mae_deg", "Mean"),
        ("centered_shape_mae_deg", "Shape"),
    ]
    x = np.arange(len(candidate_id_list))
    width = 0.24
    figure, axis = plt.subplots(figsize=(11.0, 5.3))
    for metric_index, (metric_name, label) in enumerate(metric_list):
        relative_value = [
            100.0
            * (
                row_map[candidate_id][metric_name]
                / control[metric_name]
                - 1.0
            )
            for candidate_id in candidate_id_list
        ]
        axis.bar(
            x + (metric_index - 1) * width,
            relative_value,
            width,
            label=label,
        )
    axis.axhline(0.0, color="#222222", linewidth=1.0)
    axis.axhline(-1.0, color="#2f8f5b", linestyle="--", linewidth=1.0)
    axis.set_xticks(x, candidate_id_list)
    axis.set_ylabel("Change relative to C01 [%]")
    axis.set_title("Stage 12 Accuracy Decomposition")
    axis.legend(ncol=3)
    axis.grid(axis="y", alpha=0.25)
    figure.tight_layout()
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def plot_constraint_surface(
    row_list: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """Plot closure against chunk-equivalence behavior."""

    figure, axis = plt.subplots(figsize=(9.5, 5.4))
    coordinate_group_map: dict[tuple[float, float], list[dict[str, Any]]] = {}
    for row in row_list:
        coordinate_key = (
            round(row["periodic_closure_error_deg"], 12),
            round(row["chunk_equivalence_max_abs_deg"], 12),
        )
        coordinate_group_map.setdefault(coordinate_key, []).append(row)
    for coordinate_group in coordinate_group_map.values():
        row = coordinate_group[0]
        candidate_id_label = "/".join(
            item["candidate_id"] for item in coordinate_group
        )
        axis.scatter(
            row["periodic_closure_error_deg"],
            row["chunk_equivalence_max_abs_deg"],
            s=65,
            color=(
                "#2f8f5b"
                if any(
                    item["candidate_id"] in {"F01", "S01"}
                    for item in coordinate_group
                )
                else "#3569a8"
            ),
        )
        axis.annotate(
            candidate_id_label,
            (
                row["periodic_closure_error_deg"],
                row["chunk_equivalence_max_abs_deg"],
            ),
            xytext=(5, 4),
            textcoords="offset points",
            fontsize=9,
        )
    axis.axhline(
        1.0e-6,
        color="#d73a49",
        linestyle="--",
        label="Chunk gate",
    )
    axis.set_yscale("log")
    axis.set_xlabel("Periodic closure error [deg]")
    axis.set_ylabel("Chunk max absolute difference [deg]")
    axis.set_title("Closure And Deployment-State Consistency")
    axis.grid(alpha=0.25)
    axis.legend()
    figure.tight_layout()
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def plot_tail_and_correction(
    row_list: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """Plot P95 error and maximum residual correction."""

    candidate_id_list = [row["candidate_id"] for row in row_list]
    x = np.arange(len(candidate_id_list))
    figure, left_axis = plt.subplots(figsize=(10.5, 5.2))
    left_axis.bar(
        x - 0.18,
        [row["per_curve_mae_p95"] for row in row_list],
        0.36,
        color="#3569a8",
        label="P95 curve MAE",
    )
    right_axis = left_axis.twinx()
    right_axis.bar(
        x + 0.18,
        [row["residual_abs_max_deg"] for row in row_list],
        0.36,
        color="#d9822b",
        label="Max residual",
    )
    left_axis.set_xticks(x, candidate_id_list)
    left_axis.set_ylabel("P95 curve MAE [deg]")
    right_axis.set_ylabel("Maximum correction [deg]")
    left_axis.set_title("Tail Error And Correction Magnitude")
    left_axis.grid(axis="y", alpha=0.22)
    handle_list = [
        left_axis.patches[0],
        right_axis.patches[0],
    ]
    left_axis.legend(
        handle_list,
        ["P95 curve MAE", "Max residual"],
        loc="upper left",
    )
    figure.tight_layout()
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def plot_gate_matrix(
    gate_row_list: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """Plot the complete Boolean candidate-gate matrix."""

    key_list = [
        "accuracy_improved",
        "mean_preserved",
        "p95_preserved",
        "closure_improved",
        "reset_reproducible",
        "chunk_equivalent",
        "bounded_correction",
        "beats_frozen_k01",
        "runtime_contract_passed",
        "deployment_cost_preserved",
    ]
    label_list = [
        "Accuracy",
        "Mean",
        "P95",
        "Closure",
        "Reset",
        "Chunk",
        "Bound",
        "C00",
        "Runtime",
        "Cost",
    ]
    matrix = np.asarray(
        [
            [1.0 if row[key] else 0.0 for key in key_list]
            for row in gate_row_list
        ]
    )
    figure, axis = plt.subplots(figsize=(11.2, 5.0))
    axis.imshow(
        matrix,
        aspect="auto",
        cmap=matplotlib.colors.ListedColormap(["#d73a49", "#2f8f5b"]),
        vmin=0.0,
        vmax=1.0,
    )
    axis.set_xticks(np.arange(len(label_list)), label_list, rotation=35)
    axis.set_yticks(
        np.arange(len(gate_row_list)),
        [row["candidate_id"] for row in gate_row_list],
    )
    for row_index in range(matrix.shape[0]):
        for column_index in range(matrix.shape[1]):
            axis.text(
                column_index,
                row_index,
                "P" if matrix[row_index, column_index] else "F",
                ha="center",
                va="center",
                color="white",
                fontweight="bold",
                fontsize=8,
            )
    axis.set_title("Stage 12 First-Screen Gate Matrix")
    figure.tight_layout()
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def format_table(row_list: list[dict[str, Any]]) -> str:
    """Format a compact five-row Markdown metric table."""

    line_list = [
        "| ID | Raw MAE | Mean MAE | Shape MAE | P95 | Closure | Chunk |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in row_list:
        line_list.append(
            f"| `{row['candidate_id']}` | "
            f"{row['mae_deg']:.6f} | "
            f"{row['mean_mae_deg']:.6f} | "
            f"{row['centered_shape_mae_deg']:.6f} | "
            f"{row['per_curve_mae_p95']:.6f} | "
            f"{row['periodic_closure_error_deg']:.6f} | "
            f"{row['chunk_equivalence_max_abs_deg']:.2e} |"
        )
    return "\n".join(line_list)


def build_closeout() -> Path:
    """Generate plots, decision artifact, and Markdown report."""

    campaign_directory = find_campaign_directory()
    execution = load_yaml(
        campaign_directory / "campaign_execution_summary.yaml"
    )
    best_run = load_yaml(campaign_directory / "campaign_best_run.yaml")
    gate = load_yaml(
        campaign_directory / "campaign_first_screen_gate_summary.yaml"
    )
    row_list = read_leaderboard(campaign_directory)
    row_map = {row["candidate_id"]: row for row in row_list}
    ASSET_DIRECTORY.mkdir(parents=True, exist_ok=True)
    plot_path_list = [
        ASSET_DIRECTORY / "stage12_accuracy_decomposition.png",
        ASSET_DIRECTORY / "stage12_closure_chunk_surface.png",
        ASSET_DIRECTORY / "stage12_tail_correction_surface.png",
        ASSET_DIRECTORY / "stage12_gate_matrix.png",
    ]
    plot_accuracy_surface(row_list, plot_path_list[0])
    plot_constraint_surface(row_list, plot_path_list[1])
    plot_tail_and_correction(row_list, plot_path_list[2])
    plot_gate_matrix(gate["gate_row_list"], plot_path_list[3])

    c00 = row_map["C00"]
    c01 = row_map["C01"]
    f01 = row_map["F01"]
    s01 = row_map["S01"]
    relative_plot_path_list = [
        path.relative_to(REPORT_PATH.parent).as_posix()
        for path in plot_path_list
    ]
    report_text = f"""# Wave 5.2R Stage 12 Advanced Constraint Optimization Results

## Executive Outcome

Stage 12 completed all `10 / 10` first-screen entries. The initial P01 and L01
implementation failures were corrected and recovered without rerunning the
other eight valid entries. The final campaign has zero residual failures.

No advanced optimizer passed the complete gate. The frozen Stage 9 K01 replay
C00 remains the raw-error leader at `{c00['mae_deg']:.9f} deg`, and no
candidate beat C00 while preserving the full curve-first, constraint, causal,
and deployment contract. Conditional stability was therefore skipped.

## Campaign Integrity

- Campaign: `{CAMPAIGN_NAME}`
- Output: `{campaign_directory.relative_to(PROJECT_ROOT).as_posix()}`
- Completed first-screen entries: `{execution['completed_first_screen_count']}`
- Residual failures: `{execution['failed_first_screen_count']}`
- Recovered entries: `P01`, `L01`
- Qualified winner: `{best_run['qualified_winner_id']}`
- Test curves: `97`
- Runtime target-derived inputs: `0`

## Primary Metric Surface

### Raw Leader Through Adaptive Weighting

{format_table(row_list[:5])}

### Standard And Advanced Constraint Methods

{format_table(row_list[5:])}

![Stage 12 accuracy decomposition]({relative_plot_path_list[0]})

Relative to the matched C01 retraining, F01 improves centered-shape MAE by
`{100.0 * (1.0 - f01['centered_shape_mae_deg'] / c01['centered_shape_mae_deg']):.2f}%`
and raw MAE by
`{100.0 * (1.0 - f01['mae_deg'] / c01['mae_deg']):.2f}%`.
It nevertheless worsens mean MAE to `{f01['mean_mae_deg']:.6f} deg`, exceeds
the correction bound, and does not beat frozen C00.

S01 improves raw, mean, shape, P95, and closure relative to C01. Its raw MAE
remains `{100.0 * (s01['mae_deg'] / c00['mae_deg'] - 1.0):.2f}%` worse than
C00, its maximum correction grows to `{s01['residual_abs_max_deg']:.6f} deg`,
and chunk equivalence remains above the `1e-6 deg` gate.

## Constraint And Deployment Behavior

![Stage 12 closure and chunk surface]({relative_plot_path_list[1]})

Every trainable candidate fails the declared chunk-equivalence threshold.
C01 reaches `{c01['chunk_equivalence_max_abs_deg']:.2e} deg`, which is close
but still above the frozen `1e-6 deg` gate. F01 and S01 improve parts of the
accuracy or closure surface while increasing state sensitivity.

The A01 augmented-Lagrangian inequalities remained inactive under the
predeclared budgets and therefore reproduced C01 exactly. This is evidence
that those particular budgets do not constrain the observed training regime;
they are not changed after observing test results.

![Stage 12 tail and correction surface]({relative_plot_path_list[2]})

## Method-Specific Findings

- G01 gradient-statistics balancing regresses raw and mean error and does not
  repair closure or chunk behavior.
- R01 relative-progress balancing slightly improves closure relative to C01
  but regresses raw, mean, and shape.
- P01 main-loss-preserving projection is the weakest raw-error result and
  also misses mean, P95, closure, and chunk gates.
- S01 adaptive curve weighting is the strongest multi-index diagnostic
  optimizer, but its larger corrections and failure against C00 prevent
  qualification.
- F01 failure-informed resampling gives the best trained raw and shape result,
  with favorable P95, but trades away mean fidelity, closure, bounded
  correction, and frozen-K01 superiority.
- U01 curriculum regularization improves closure but regresses raw, mean,
  shape, and P95.
- L01 performs seven L-BFGS closure evaluations; validation rejects the
  refinement and restores the C01 checkpoint exactly.

### Complete Gate Matrix

![Stage 12 gate matrix]({relative_plot_path_list[3]})

## Decision

Stage 12 promotes no optimizer and no new physics-informed component. The
accepted evidence remains:

- H04 as the qualified structured coefficient component;
- K01 as a qualified research component without official promotion;
- F01 and S01 as diagnostic evidence that hard-curve emphasis can trade shape
  and tail error against mean, correction magnitude, and state consistency.

Advanced optimization does not rescue the unresolved K01 closure and
chunk-equivalence limitations. Stage 13 Synthetic And Weak-Form Oracle Lane is
the next roadmap step. Physics-integrated Wave 6 remains closed.

## Reproducibility

The campaign uses the Stage 0 split signature
`{SPLIT_SIGNATURE}`, frozen H04 and K01 provenance, seed `314159`, immutable
run directories, validation-only checkpoint selection, and one held-out test
evaluation per completed candidate. The two initial implementation failures
remain recorded in the campaign folder; the execution summary separately
records their successful recovery.
"""
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_text, encoding="utf-8", newline="\n")
    closeout_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage12",
        "status": "completed_no_qualified_optimizer",
        "campaign_output_directory": (
            campaign_directory.relative_to(PROJECT_ROOT).as_posix()
        ),
        "completed_first_screen_count": 10,
        "failed_first_screen_count": 0,
        "recovered_candidate_id_list": ["P01", "L01"],
        "raw_error_leader_id": "C00",
        "qualified_winner_id": None,
        "conditional_stability_executed": False,
        "diagnostic_candidate_id_list": ["F01", "S01"],
        "next_stage": "stage13_synthetic_and_weak_form_oracle_lane",
        "report_path": REPORT_PATH.relative_to(PROJECT_ROOT).as_posix(),
        "generated_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
    }
    write_yaml(
        CLOSEOUT_DIRECTORY / "stage12_exit_gate_summary.yaml",
        closeout_payload,
    )
    return REPORT_PATH


def parse_arguments() -> argparse.Namespace:
    """Parse closeout commands."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Build the Stage 12 closeout."""

    arguments = parse_arguments()
    if arguments.build:
        print(build_closeout())
    else:
        print(build_closeout())


if __name__ == "__main__":
    main()
