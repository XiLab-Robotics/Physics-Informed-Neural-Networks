"""Build the Wave 5.2R Stage 15 official forward verification closeout."""

from __future__ import annotations

# Import Python Utilities
import csv
import json
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Plotting And Serialization Utilities
import matplotlib
import numpy as np
import yaml

matplotlib.use("Agg")
from matplotlib import pyplot as plt  # noqa: E402


# Define Canonical Evidence Paths
MATRIX_OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "track2_reference_comparison"
    / "2026-07-30-01-03-11__wave52r_stage15_official_forward_verification_"
    "wave52r_stage15_official_forward_verification"
)
DIAGNOSTIC_OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "wave52r_stage15_curve_payload_diagnostics"
    / "2026-07-30-01-11-50__track2c_curve_payload_diagnostics"
)
DEPLOYMENT_OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "wave52r_stage15_deployment_parity"
)
CLOSEOUT_OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage15_official_forward_verification"
    / "closeout"
)
REPORT_DIRECTORY = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "analysis"
    / "model_development_waves"
    / "wave_5_2"
    / "official_forward_verification_and_deployment_preparation"
    / "[2026-07-30]"
)
ASSET_DIRECTORY = REPORT_DIRECTORY / "assets"
REPORT_PATH = (
    REPORT_DIRECTORY
    / "stage15_official_forward_verification_and_deployment_preparation_"
    "report.md"
)


# Define Candidate Labels And Plot Styling
H04_ID = "wave52r_stage15_h04_bounded_coefficient_residual_Fw"
PF_A_ID = "wave52r_stage15_pf_a_setpoint_quadratic_Fw"
MLP_ID = "accepted_periodic_mlp_harmonic_Fw"
GRU_ID = "accepted_periodic_gru_sequence_Fw"
CANDIDATE_ID_LIST = [H04_ID, PF_A_ID, MLP_ID, GRU_ID]
CANDIDATE_LABEL_MAP = {
    H04_ID: "H04",
    PF_A_ID: "PF-A",
    MLP_ID: "Harmonic MLP",
    GRU_ID: "Periodic GRU",
}
CANDIDATE_COLOR_MAP = {
    H04_ID: "#0072B2",
    PF_A_ID: "#D55E00",
    MLP_ID: "#009E73",
    GRU_ID: "#CC79A7",
}


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML mapping: {path}"
    return payload


def load_csv(path: Path) -> list[dict[str, str]]:
    """Load one CSV table as dictionaries."""

    with path.open("r", encoding="utf-8-sig", newline="") as input_file:
        return list(csv.DictReader(input_file))


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    """Write one deterministic YAML mapping."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
        )


def improvement_percent(candidate_value: float, reference_value: float) -> float:
    """Return positive percent improvement for one minimized metric."""

    return 100.0 * (reference_value - candidate_value) / reference_value


def build_metric_maps() -> tuple[
    dict[str, dict[str, float]],
    dict[str, dict[str, float]],
]:
    """Load raw Track 2 metrics and CVP 1.2 diagnostic metrics."""

    matrix_summary = load_yaml(MATRIX_OUTPUT_DIRECTORY / "validation_summary.yaml")
    raw_metric_map = {
        candidate_id: {
            metric_name: float(metric_value)
            for metric_name, metric_value in metric_map.items()
        }
        for candidate_id, metric_map in matrix_summary[
            "candidate_metric_summary"
        ].items()
    }

    diagnostic_row_list = load_csv(
        DIAGNOSTIC_OUTPUT_DIRECTORY / "candidate_payload_diagnostics.csv"
    )
    diagnostic_metric_map: dict[str, dict[str, float]] = {}
    for row in diagnostic_row_list:
        candidate_id = row["candidate_id"]
        diagnostic_metric_map[candidate_id] = {
            key: float(value)
            for key, value in row.items()
            if key
            not in {
                "rank",
                "candidate_id",
                "candidate_family",
                "candidate_source_label",
                "candidate_surface",
                "valid_direction_list",
                "curve_count",
            }
        }

    assert set(raw_metric_map) == set(CANDIDATE_ID_LIST)
    assert set(diagnostic_metric_map) == set(CANDIDATE_ID_LIST)
    return raw_metric_map, diagnostic_metric_map


def build_multi_index_plot(
    raw_metric_map: dict[str, dict[str, float]],
    diagnostic_metric_map: dict[str, dict[str, float]],
) -> Path:
    """Plot each minimized metric relative to its best Stage 15 value."""

    metric_definition_list = [
        ("Raw MAE", "raw", "mae"),
        ("P95 MPE", "raw", "p95_mean_percentage_error_pct"),
        ("Centered", "diagnostic", "mean_centered_curve_mae_deg"),
        ("Offset", "diagnostic", "mean_absolute_curve_mean_error_deg"),
        ("P2P", "diagnostic", "mean_peak_to_peak_error_pct"),
        ("Derivative", "diagnostic", "mean_derivative_rmse_deg_per_deg"),
        ("Harmonic amp.", "diagnostic", "mean_harmonic_amplitude_error_pct"),
        ("Harmonic phase", "diagnostic", "mean_harmonic_phase_error_deg"),
    ]
    x_position = np.arange(len(metric_definition_list), dtype=np.float64)
    width = 0.19
    figure, axis = plt.subplots(
        figsize=(13.0, 6.2),
        layout="constrained",
    )

    for candidate_position, candidate_id in enumerate(CANDIDATE_ID_LIST):
        normalized_value_list: list[float] = []
        for _, metric_source, metric_name in metric_definition_list:
            source_map = (
                raw_metric_map
                if metric_source == "raw"
                else diagnostic_metric_map
            )
            best_value = min(
                source_map[entry_id][metric_name]
                for entry_id in CANDIDATE_ID_LIST
            )
            normalized_value_list.append(
                source_map[candidate_id][metric_name] / best_value
            )
        axis.bar(
            x_position + (candidate_position - 1.5) * width,
            normalized_value_list,
            width,
            color=CANDIDATE_COLOR_MAP[candidate_id],
            label=CANDIDATE_LABEL_MAP[candidate_id],
        )

    axis.axhline(1.0, color="#202020", linewidth=1.0, linestyle="--")
    axis.set_xticks(x_position)
    axis.set_xticklabels(
        [entry[0] for entry in metric_definition_list],
        rotation=22,
        ha="right",
    )
    axis.set_ylabel("Metric divided by best Stage 15 value")
    axis.set_title("Stage 15 Official Forward Multi-Index Comparison")
    axis.grid(axis="y", alpha=0.25)
    axis.legend(ncol=4)

    ASSET_DIRECTORY.mkdir(parents=True, exist_ok=True)
    output_path = ASSET_DIRECTORY / "stage15_multi_index_comparison.png"
    figure.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(figure)
    return output_path


def load_curve_payloads() -> dict[str, dict[str, dict[str, Any]]]:
    """Load the downsampled CVP 1.2 curve payloads by condition and candidate."""

    payload_map: dict[str, dict[str, dict[str, Any]]] = {}
    payload_path = (
        DIAGNOSTIC_OUTPUT_DIRECTORY / "curve_payload_samples.jsonl"
    )
    with payload_path.open("r", encoding="utf-8") as input_file:
        for line in input_file:
            payload = json.loads(line)
            condition_id = Path(payload["source_file_path"]).name
            candidate_id = payload["candidate_id"]
            payload_map.setdefault(condition_id, {})[candidate_id] = payload

    assert len(payload_map) == 4
    for candidate_map in payload_map.values():
        assert set(candidate_map) == set(CANDIDATE_ID_LIST)
    return payload_map


def build_representative_curve_plot(
    payload_map: dict[str, dict[str, dict[str, Any]]],
) -> Path:
    """Plot measured and predicted curves for four representative conditions."""

    figure, axis_array = plt.subplots(
        2,
        2,
        figsize=(14.0, 8.2),
        sharex=True,
        layout="constrained",
    )
    for axis, condition_id in zip(
        axis_array.flat,
        sorted(payload_map),
        strict=True,
    ):
        candidate_map = payload_map[condition_id]
        reference_payload = candidate_map[H04_ID]
        angle_array = np.asarray(
            reference_payload["angular_position_deg"],
            dtype=np.float64,
        )
        truth_array = np.asarray(
            reference_payload["truth_curve_deg"],
            dtype=np.float64,
        )
        axis.plot(
            angle_array,
            truth_array,
            color="#202020",
            linewidth=1.5,
            label="Measured",
        )
        for candidate_id in CANDIDATE_ID_LIST:
            prediction_array = np.asarray(
                candidate_map[candidate_id]["predicted_curve_deg"],
                dtype=np.float64,
            )
            axis.plot(
                angle_array,
                prediction_array,
                color=CANDIDATE_COLOR_MAP[candidate_id],
                linewidth=1.0,
                alpha=0.92,
                label=CANDIDATE_LABEL_MAP[candidate_id],
            )
        axis.set_title(condition_id.replace(".csv", ""))
        axis.set_xlabel("Output angle [deg]")
        axis.set_ylabel("TE [deg]")
        axis.grid(alpha=0.2)

    handle_list, label_list = axis_array.flat[0].get_legend_handles_labels()
    figure.legend(
        handle_list,
        label_list,
        loc="outside upper center",
        ncol=5,
    )
    output_path = ASSET_DIRECTORY / "stage15_representative_curve_overlays.png"
    figure.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(figure)
    return output_path


def build_deployment_parity_plot(
    onnx_summary: dict[str, Any],
    plc_summary: dict[str, Any],
) -> Path:
    """Plot ONNX and static PLC-reference parity against declared tolerances."""

    comparison_list = [
        (
            "ONNX curve",
            float(
                onnx_summary["maximum_absolute_difference_deg_by_output"][
                    "prediction_curve"
                ]
            ),
            float(onnx_summary["curve_max_abs_tolerance_deg"]),
        ),
        (
            "ONNX coeff.",
            float(
                onnx_summary["maximum_absolute_difference_deg_by_output"][
                    "prediction_coefficients"
                ]
            ),
            float(onnx_summary["coefficient_max_abs_tolerance_deg"]),
        ),
        (
            "PLC-ref curve",
            float(plc_summary["curve_max_abs_difference_deg"]),
            float(plc_summary["curve_max_abs_tolerance_deg"]),
        ),
        (
            "PLC-ref coeff.",
            float(plc_summary["coefficient_max_abs_difference_deg"]),
            float(plc_summary["coefficient_max_abs_tolerance_deg"]),
        ),
    ]
    x_position = np.arange(len(comparison_list), dtype=np.float64)
    observed_array = np.asarray(
        [entry[1] for entry in comparison_list],
        dtype=np.float64,
    )
    tolerance_array = np.asarray(
        [entry[2] for entry in comparison_list],
        dtype=np.float64,
    )

    figure, axis = plt.subplots(
        figsize=(10.0, 5.5),
        layout="constrained",
    )
    axis.bar(
        x_position - 0.18,
        observed_array,
        0.36,
        color="#0072B2",
        label="Observed maximum difference",
    )
    axis.bar(
        x_position + 0.18,
        tolerance_array,
        0.36,
        color="#E69F00",
        label="Declared tolerance",
    )
    axis.set_yscale("log")
    axis.set_xticks(x_position)
    axis.set_xticklabels([entry[0] for entry in comparison_list])
    axis.set_ylabel("Maximum absolute difference [deg]")
    axis.set_title("H04 Export Parity Margin")
    axis.grid(axis="y", alpha=0.25, which="both")
    axis.legend()

    output_path = ASSET_DIRECTORY / "stage15_deployment_parity.png"
    figure.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(figure)
    return output_path


def build_metric_table(
    raw_metric_map: dict[str, dict[str, float]],
    diagnostic_metric_map: dict[str, dict[str, float]],
) -> str:
    """Build the central official comparison table."""

    row_definition_list = [
        ("Raw MAE [deg]", "raw", "mae"),
        ("RMSE [deg]", "raw", "rmse"),
        ("MPE [%]", "raw", "mean_percentage_error_pct"),
        ("P95 MPE [%]", "raw", "p95_mean_percentage_error_pct"),
        (
            "Centered shape MAE [deg]",
            "diagnostic",
            "mean_centered_curve_mae_deg",
        ),
        (
            "Absolute offset error [deg]",
            "diagnostic",
            "mean_absolute_curve_mean_error_deg",
        ),
        (
            "Peak-to-peak error [%]",
            "diagnostic",
            "mean_peak_to_peak_error_pct",
        ),
        (
            "Derivative RMSE [deg/deg]",
            "diagnostic",
            "mean_derivative_rmse_deg_per_deg",
        ),
        (
            "Harmonic amplitude error [%]",
            "diagnostic",
            "mean_harmonic_amplitude_error_pct",
        ),
        (
            "Harmonic phase error [deg]",
            "diagnostic",
            "mean_harmonic_phase_error_deg",
        ),
        (
            "Closure mismatch [deg]",
            "diagnostic",
            "mean_closure_mismatch_deg",
        ),
    ]
    line_list = [
        "| Metric | H04 | PF-A | MLP | GRU | Best |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for display_name, metric_source, metric_name in row_definition_list:
        source_map = (
            raw_metric_map
            if metric_source == "raw"
            else diagnostic_metric_map
        )
        best_id = min(
            CANDIDATE_ID_LIST,
            key=lambda candidate_id: source_map[candidate_id][metric_name],
        )
        line_list.append(
            "| "
            f"{display_name} | "
            f"{source_map[H04_ID][metric_name]:.7f} | "
            f"{source_map[PF_A_ID][metric_name]:.7f} | "
            f"{source_map[MLP_ID][metric_name]:.7f} | "
            f"{source_map[GRU_ID][metric_name]:.7f} | "
            f"{CANDIDATE_LABEL_MAP[best_id]} |"
        )
    return "\n".join(line_list)


def build_decision_payload(
    raw_metric_map: dict[str, dict[str, float]],
    diagnostic_metric_map: dict[str, dict[str, float]],
    onnx_summary: dict[str, Any],
    plc_summary: dict[str, Any],
) -> dict[str, Any]:
    """Build the machine-readable Stage 15 acceptance decision."""

    h04_raw_mae = raw_metric_map[H04_ID]["mae"]
    pf_a_raw_mae = raw_metric_map[PF_A_ID]["mae"]
    gru_raw_mae = raw_metric_map[GRU_ID]["mae"]
    h04_centered = diagnostic_metric_map[H04_ID][
        "mean_centered_curve_mae_deg"
    ]
    gru_centered = diagnostic_metric_map[GRU_ID][
        "mean_centered_curve_mae_deg"
    ]
    h04_offset = diagnostic_metric_map[H04_ID][
        "mean_absolute_curve_mean_error_deg"
    ]
    gru_offset = diagnostic_metric_map[GRU_ID][
        "mean_absolute_curve_mean_error_deg"
    ]

    return {
        "schema_version": 1,
        "stage": "wave52r_stage15_official_forward_verification",
        "status": "completed_without_promotion",
        "official_surface": "polished_dataset_setpoint_forward",
        "curve_count": 97,
        "challenger_candidate_id": H04_ID,
        "incumbent_candidate_id": GRU_ID,
        "registry_promotion": False,
        "decision": (
            "retain_periodic_gru_sequence_fw_incumbent_and_keep_h04_"
            "exploratory_export_prepared"
        ),
        "evidence": {
            "h04_raw_mae_deg": h04_raw_mae,
            "h04_vs_pf_a_raw_mae_improvement_pct": improvement_percent(
                h04_raw_mae,
                pf_a_raw_mae,
            ),
            "h04_vs_gru_raw_mae_improvement_pct": improvement_percent(
                h04_raw_mae,
                gru_raw_mae,
            ),
            "h04_centered_shape_mae_deg": h04_centered,
            "h04_vs_gru_centered_shape_improvement_pct": improvement_percent(
                h04_centered,
                gru_centered,
            ),
            "h04_absolute_offset_error_deg": h04_offset,
            "h04_vs_gru_offset_improvement_pct": improvement_percent(
                h04_offset,
                gru_offset,
            ),
            "python_onnx_parity_passed": bool(
                onnx_summary["python_onnx_parity_passed"]
            ),
            "static_plc_reference_parity_passed": bool(
                plc_summary["static_plc_reference_parity_passed"]
            ),
            "twincat_compile_status": plc_summary["twincat_compile_status"],
            "twincat_runtime_status": plc_summary["twincat_runtime_status"],
        },
        "acceptance_gate_list": [
            {
                "gate_id": "official_forward_curve_first_matrix_complete",
                "passed": True,
            },
            {
                "gate_id": "challenger_improves_pf_a_raw_mae",
                "passed": h04_raw_mae < pf_a_raw_mae,
            },
            {
                "gate_id": "challenger_improves_incumbent_raw_mae",
                "passed": h04_raw_mae < gru_raw_mae,
            },
            {
                "gate_id": "challenger_improves_incumbent_centered_shape",
                "passed": h04_centered < gru_centered,
            },
            {
                "gate_id": "challenger_improves_incumbent_offset",
                "passed": h04_offset < gru_offset,
            },
            {
                "gate_id": "python_onnx_parity",
                "passed": bool(onnx_summary["python_onnx_parity_passed"]),
            },
            {
                "gate_id": "static_plc_reference_parity",
                "passed": bool(
                    plc_summary["static_plc_reference_parity_passed"]
                ),
            },
            {
                "gate_id": "twincat_compile_and_runtime_parity",
                "passed": False,
            },
        ],
        "next_step": (
            "Close Wave 5.2R without H04 registry promotion. Preserve the "
            "export package for a future TwinCAT runtime integration task."
        ),
    }


def build_report(
    raw_metric_map: dict[str, dict[str, float]],
    diagnostic_metric_map: dict[str, dict[str, float]],
    onnx_summary: dict[str, Any],
    plc_summary: dict[str, Any],
    decision_payload: dict[str, Any],
) -> None:
    """Write the canonical Stage 15 analytical closeout report."""

    evidence = decision_payload["evidence"]
    report_text = f"""# Wave 5.2R Stage 15 Official Forward Verification And Deployment Preparation

## Executive Decision

Stage 15 is complete on the official polished-dataset setpoint-forward surface.
The matrix evaluated 97 held-out forward curves with the exact same split and
runtime-valid input contract for H04, PF-A, the accepted harmonic MLP, and the
accepted periodic GRU.

H04 remains exploratory and receives no family or program registry promotion.
It improves PF-A raw MAE by
`{evidence["h04_vs_pf_a_raw_mae_improvement_pct"]:.3f}%` and is the best
candidate for mean-centered shape, derivative fidelity, and mean harmonic
phase. It does not displace the GRU: its raw MAE is
`{abs(evidence["h04_vs_gru_raw_mae_improvement_pct"]):.3f}%` worse and its
absolute offset error is
`{abs(evidence["h04_vs_gru_offset_improvement_pct"]):.3f}%` worse. The GRU
also retains the best P95 error and peak-to-peak behavior.

The Python/ONNX and independent float32 PLC-reference parity gates pass. A
TwinCAT compile and runtime replay were not performed, so this report makes no
PLC runtime claim. The accepted periodic GRU remains the forward incumbent.

## Scope And Evidence Contract

- dataset: `data/polished_dataset`;
- surface: setpoint `Fw` only;
- held-out curves: `97`;
- angular samples per full curve: `2048`;
- candidates: H04, PF-A, accepted harmonic MLP, accepted periodic GRU;
- selection policy: multi-index curve-first, never scalar MAE alone;
- curve payload diagnostics: CVP 1.2 with full curves and downsampled visual
  payloads;
- deployment evidence: immutable Python checkpoint replay, ONNX parity, and
  static Structured Text reference parity.

## Official Multi-Index Results

{build_metric_table(raw_metric_map, diagnostic_metric_map)}

![Stage 15 official forward multi-index comparison](assets/stage15_multi_index_comparison.png)

The official matrix and CVP 1.2 diagnostics separate the winners:

- best raw MAE, RMSE, MPE, P95 MPE, offset, and peak-to-peak behavior:
  periodic GRU;
- best centered shape, derivative fidelity, and mean harmonic phase: H04;
- best aggregate CVP 1.2 diagnostic score and harmonic amplitude error:
  harmonic MLP;
- PF-A is improved by H04 but is not the official winner on any decisive
  acceptance axis.

H04's shape improvement over the GRU is
`{evidence["h04_vs_gru_centered_shape_improvement_pct"]:.3f}%`. This confirms
that the bounded analytical residual learned useful periodic structure. The
simultaneous raw and offset regressions show that this advantage is not a
balanced replacement for the incumbent.

## Representative Curve Evidence

![Stage 15 representative forward overlays](assets/stage15_representative_curve_overlays.png)

The overlays use four deterministic CVP 1.2 payload conditions. They are
visual evidence only; the decision above uses all 97 full-resolution curves.
All models reproduce the dominant periodic structure. Their separation is
small enough that scalar or hand-selected visual inspection alone would be
misleading, which is why the official decision retains the multi-index table.

## Robustness Interpretation

The temperature slices preserve the same overall conclusion:

| Temperature | H04 MAE [deg] | PF-A MAE [deg] | MLP MAE [deg] | GRU MAE [deg] |
| ---: | ---: | ---: | ---: | ---: |
| 25 C | 0.0013770 | 0.0014953 | 0.0012815 | 0.0013628 |
| 30 C | 0.0018189 | 0.0018381 | 0.0017768 | 0.0016156 |
| 35 C | 0.0018864 | 0.0020149 | 0.0019034 | 0.0018093 |

H04 improves PF-A at every available temperature. It does not establish a
uniform advantage over the accepted neural references: the MLP leads at 25 C,
while the GRU leads at 30 C and 35 C. The result supports retaining H04 as a
compact grey-box formulation, not promoting it as the balanced forward
incumbent.

## Deployment Preparation And Parity

![Stage 15 deployment parity](assets/stage15_deployment_parity.png)

| Check | Observed maximum difference | Tolerance | Result |
| --- | ---: | ---: | --- |
| ONNX reconstructed curve | {onnx_summary["maximum_absolute_difference_deg_by_output"]["prediction_curve"]:.9e} deg | {onnx_summary["curve_max_abs_tolerance_deg"]:.1e} deg | pass |
| ONNX final coefficients | {onnx_summary["maximum_absolute_difference_deg_by_output"]["prediction_coefficients"]:.9e} deg | {onnx_summary["coefficient_max_abs_tolerance_deg"]:.1e} deg | pass |
| PLC-reference reconstructed curve | {plc_summary["curve_max_abs_difference_deg"]:.9e} deg | {plc_summary["curve_max_abs_tolerance_deg"]:.1e} deg | pass |
| PLC-reference final coefficients | {plc_summary["coefficient_max_abs_difference_deg"]:.9e} deg | {plc_summary["coefficient_max_abs_tolerance_deg"]:.1e} deg | pass |

The export package contains the ONNX graph, immutable parity payload,
Structured Text function block, Structured Text parameter GVL, and the
parameter archive. This proves reproducible static numerical translation.
TwinCAT compilation, execution-time measurement, task integration, invalid
input behavior, saturation behavior, and online `DataValid` replay remain
future deployment work.

## Acceptance Gate

| Gate | Result |
| --- | --- |
| Official common forward matrix completed | pass |
| H04 improves PF-A raw MAE | pass |
| H04 improves incumbent raw MAE | fail |
| H04 improves incumbent centered shape | pass |
| H04 improves incumbent offset | fail |
| Python/ONNX parity | pass |
| Static PLC-reference parity | pass |
| TwinCAT compile and runtime parity | pending / not claimed |

The Stage 15 exit gate therefore closes without promotion. This is a valid
negative acceptance result: the challenger demonstrated real shape value and
excellent export parity, but it did not provide a balanced predictive gain and
does not yet have runtime PLC evidence.

## Program Decision

Wave 5.2R has completed all stages 0 through 15. The program conclusions are:

1. observable analytical and harmonic priors are useful when treated as
   bounded structure, diagnostics, or auxiliary objectives;
2. useful physics guidance does not guarantee a better balanced predictor;
3. H04 is the strongest compact grey-box output of the wave and should be
   preserved for future deployment research;
4. the periodic GRU remains the accepted forward incumbent;
5. no family or program registry changes are authorized by this result;
6. physics-integrated Wave 6 remains a separate future decision and must not
   inherit an unearned H04 acceptance claim.

## Reproducibility Artifacts

- official matrix:
  `output/validation_checks/track2_reference_comparison/2026-07-30-01-03-11__wave52r_stage15_official_forward_verification_wave52r_stage15_official_forward_verification/`;
- CVP 1.2 diagnostics:
  `output/validation_checks/wave52r_stage15_curve_payload_diagnostics/2026-07-30-01-11-50__track2c_curve_payload_diagnostics/`;
- deployment parity:
  `output/validation_checks/wave52r_stage15_deployment_parity/`;
- machine-readable decision:
  `output/analysis/wave_5_2r/stage15_official_forward_verification/closeout/stage15_official_forward_verification_decision.yaml`.
"""
    REPORT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_text, encoding="utf-8", newline="\n")


def validate_closeout(decision_payload: dict[str, Any]) -> None:
    """Validate the Stage 15 closeout contract."""

    assert decision_payload["status"] == "completed_without_promotion"
    assert decision_payload["registry_promotion"] is False
    gate_map = {
        row["gate_id"]: row["passed"]
        for row in decision_payload["acceptance_gate_list"]
    }
    assert gate_map["official_forward_curve_first_matrix_complete"] is True
    assert gate_map["challenger_improves_pf_a_raw_mae"] is True
    assert gate_map["challenger_improves_incumbent_raw_mae"] is False
    assert gate_map["challenger_improves_incumbent_centered_shape"] is True
    assert gate_map["challenger_improves_incumbent_offset"] is False
    assert gate_map["python_onnx_parity"] is True
    assert gate_map["static_plc_reference_parity"] is True
    assert gate_map["twincat_compile_and_runtime_parity"] is False
    assert REPORT_PATH.is_file()
    for asset_name in {
        "stage15_multi_index_comparison.png",
        "stage15_representative_curve_overlays.png",
        "stage15_deployment_parity.png",
    }:
        assert (ASSET_DIRECTORY / asset_name).is_file()


def main() -> None:
    """Build and validate all Stage 15 closeout artifacts."""

    raw_metric_map, diagnostic_metric_map = build_metric_maps()
    onnx_summary = load_yaml(
        DEPLOYMENT_OUTPUT_DIRECTORY / "stage15_onnx_parity_summary.yaml"
    )
    plc_summary = load_yaml(
        DEPLOYMENT_OUTPUT_DIRECTORY / "stage15_plc_static_parity_summary.yaml"
    )

    build_multi_index_plot(raw_metric_map, diagnostic_metric_map)
    build_representative_curve_plot(load_curve_payloads())
    build_deployment_parity_plot(onnx_summary, plc_summary)

    decision_payload = build_decision_payload(
        raw_metric_map,
        diagnostic_metric_map,
        onnx_summary,
        plc_summary,
    )
    write_yaml(
        CLOSEOUT_OUTPUT_DIRECTORY
        / "stage15_official_forward_verification_decision.yaml",
        decision_payload,
    )
    build_report(
        raw_metric_map,
        diagnostic_metric_map,
        onnx_summary,
        plc_summary,
        decision_payload,
    )
    validate_closeout(decision_payload)
    print(
        "Stage 15 official forward verification closeout completed | "
        f"report={REPORT_PATH.relative_to(PROJECT_ROOT)}"
    )


if __name__ == "__main__":
    main()
