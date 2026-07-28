"""Build the Wave 5.2R Stage 4 capacity and cancellation audit."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import math
from pathlib import Path
from statistics import mean
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
import torch
import yaml

# Import Project Analysis And Inference Utilities
from scripts.analysis.polynomial_fourier_benchmark.polynomial_fourier_models import (
    reconstruct_from_projected_coefficients,
)
from scripts.campaigns.wave_5_2.prepare_wave52r_stage4_data_only_residual_capacity_ladder_campaign import (
    build_surface_from_payload,
)
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)
from scripts.reports.analysis import (
    build_track2_curve_payload_diagnostics_report as curve_diagnostics,
)
from scripts.training import shared_training_infrastructure


# Define Stable Paths And Gates
MATRIX_CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "wave52r_stage4_data_only_residual_common_test_matrix.yaml"
)
CAUSAL_ANCHOR_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
    / "stage4_causal_setpoint_pf_a_surface.yaml"
)
VALIDITY_CONDITION_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
    / "stage4_causal_setpoint_validity_envelope_conditions.csv"
)
OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
    / "closeout"
)
AUDIT_SUMMARY_PATH = OUTPUT_DIRECTORY / "stage4_exit_gate_summary.yaml"
DECISION_MATRIX_PATH = (
    OUTPUT_DIRECTORY / "stage4_candidate_decision_matrix.csv"
)
DECOMPOSITION_PATH = (
    OUTPUT_DIRECTORY / "stage4_residual_decomposition_metrics.csv"
)
AUDIT_REPORT_PATH = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "analysis"
    / "model_development_waves"
    / "wave_5_2"
    / "physics_guided_pinn_reassessment"
    / "[2026-07-28]"
    / "stage4_data_only_residual_capacity_ladder"
    / "stage4_curve_first_and_cancellation_audit.md"
)
RESIDUAL_TO_ANCHOR_RMS_MAXIMUM = 0.50
GENERAL_REGRESSION_MULTIPLIER = 1.05
PEAK_TO_PEAK_REGRESSION_MULTIPLIER = 1.10


def parse_arguments() -> argparse.Namespace:
    """Parse the diagnostics-directory argument."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--diagnostics-directory",
        type=Path,
        required=True,
        help="Completed bounded curve-payload diagnostics directory.",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    resolved_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        path
    )
    assert resolved_path.is_file(), f"Required YAML does not exist | {path}"
    payload = yaml.safe_load(resolved_path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload


def load_csv(path: Path) -> list[dict[str, str]]:
    """Load one CSV table."""

    resolved_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        path
    )
    with resolved_path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as input_file:
        return list(csv.DictReader(input_file))


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


def write_csv(path: Path, row_list: list[dict[str, Any]]) -> None:
    """Write one stable CSV table."""

    assert row_list
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=list(row_list[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)


def condition_id_from_operating_values(
    speed_rpm: float,
    torque_nm: float,
    temperature_deg_c: float,
) -> str:
    """Build one canonical condition identifier."""

    return (
        f"speed_{int(round(abs(speed_rpm)))}rpm__"
        f"torque_{int(round(abs(torque_nm)))}Nm__"
        f"temperature_{int(round(temperature_deg_c))}degC"
    )


def build_support_tier_map() -> dict[str, str]:
    """Index the causal setpoint support tier by condition."""

    return {
        row["condition_id"]: row["support_tier"]
        for row in load_csv(VALIDITY_CONDITION_PATH)
    }


def build_r0_diagnostic_entry_list(
    training_config: dict[str, Any],
    curve_record_list: list[Any],
    harmonic_order_list: list[int],
) -> list[curve_diagnostics.CurveDiagnosticEntry]:
    """Evaluate the frozen causal setpoint PF-A control."""

    anchor_payload = load_yaml(CAUSAL_ANCHOR_PATH)
    causal_surface = build_surface_from_payload(anchor_payload["surface"])
    entry_list: list[curve_diagnostics.CurveDiagnosticEntry] = []
    for curve_record in curve_record_list:
        if str(curve_record.direction_label).strip().lower() != "forward":
            continue
        operating_feature_matrix = (
            reference_family_vs_feedforward_support.build_feedforward_input_tensor(
                curve_record,
                training_config,
                expected_input_feature_dim=5,
            )
            .detach()
            .cpu()
            .numpy()
        )
        operating_feature_array = np.asarray(
            [
                (
                    -operating_feature_matrix[0, 4]
                    * abs(operating_feature_matrix[0, 2])
                ),
                abs(operating_feature_matrix[0, 1]),
                operating_feature_matrix[0, 3],
            ],
            dtype=np.float64,
        )
        coefficient_array = causal_surface.predict(
            operating_feature_array[np.newaxis, :]
        )[0]
        prediction_curve = reconstruct_from_projected_coefficients(
            np.deg2rad(curve_record.angular_position_deg),
            coefficient_array,
            list(causal_surface.harmonic_order_list),
        )
        candidate_entry = {
            "candidate_id": "stage4_r0_causal_setpoint_pf_a",
            "candidate_family": "PF_A_SETPOINT_QUADRATIC",
            "candidate_source_label": "stage4_frozen_analytical_control",
            "candidate_surface": "Fw",
            "direction_label": "forward",
            "source_file_path": (
                shared_training_infrastructure.format_project_relative_path(
                    curve_record.source_file_path
                )
            ),
            "speed_rpm": float(curve_record.speed_rpm),
            "torque_nm": float(curve_record.torque_nm),
            "oil_temperature_deg": float(
                curve_record.oil_temperature_deg
            ),
            "metrics": {
                "mae": float(
                    np.mean(
                        np.abs(
                            prediction_curve
                            - curve_record.transmission_error_deg
                        )
                    )
                ),
                "rmse": float(
                    np.sqrt(
                        np.mean(
                            np.square(
                                prediction_curve
                                - curve_record.transmission_error_deg
                            )
                        )
                    )
                ),
                "mean_percentage_error_pct": 0.0,
            },
            "angular_position_deg": (
                curve_record.angular_position_deg.astype(float).tolist()
            ),
            "truth_curve_deg": (
                curve_record.transmission_error_deg.astype(float).tolist()
            ),
            "predicted_curve_deg": prediction_curve.astype(float).tolist(),
        }
        truth_peak_to_peak = float(
            np.ptp(curve_record.transmission_error_deg)
        )
        candidate_entry["metrics"]["mean_percentage_error_pct"] = (
            100.0
            * candidate_entry["metrics"]["mae"]
            / max(truth_peak_to_peak, 1.0e-12)
        )
        diagnostic_entry, _ = (
            curve_diagnostics.compute_curve_diagnostic_entry(
                candidate_entry,
                harmonic_order_list,
            )
        )
        entry_list.append(diagnostic_entry)
    assert len(entry_list) == 97
    return entry_list


def diagnostic_entry_to_metric_dictionary(
    entry: curve_diagnostics.CurveDiagnosticEntry,
) -> dict[str, float]:
    """Extract the metrics used by Stage 4 gates."""

    return {
        "curve_mae_deg": entry.curve_mae_deg,
        "centered_curve_mae_deg": entry.centered_curve_mae_deg,
        "absolute_curve_mean_error_deg": (
            entry.absolute_curve_mean_error_deg
        ),
        "peak_to_peak_error_pct": entry.peak_to_peak_error_pct,
        "derivative_rmse_deg_per_deg": (
            entry.derivative_rmse_deg_per_deg
        ),
        "mean_harmonic_amplitude_error_pct": (
            entry.mean_harmonic_amplitude_error_pct
        ),
        "mean_harmonic_phase_error_deg": (
            entry.mean_harmonic_phase_error_deg
        ),
    }


def summarize_supported_core_metrics(
    metric_row_list: list[dict[str, Any]],
) -> dict[str, float]:
    """Aggregate one candidate over causal supported-core test curves."""

    assert len(metric_row_list) == 96
    metric_name_list = [
        "curve_mae_deg",
        "centered_curve_mae_deg",
        "absolute_curve_mean_error_deg",
        "peak_to_peak_error_pct",
        "derivative_rmse_deg_per_deg",
        "mean_harmonic_amplitude_error_pct",
        "mean_harmonic_phase_error_deg",
    ]
    summary = {
        metric_name: float(
            mean(float(row[metric_name]) for row in metric_row_list)
        )
        for metric_name in metric_name_list
    }
    summary["p95_curve_mae_deg"] = float(
        np.quantile(
            [float(row["curve_mae_deg"]) for row in metric_row_list],
            0.95,
        )
    )
    summary["worst_curve_mae_deg"] = float(
        max(float(row["curve_mae_deg"]) for row in metric_row_list)
    )
    return summary


def build_supported_core_summary_map(
    diagnostics_directory: Path,
    r0_entry_list: list[curve_diagnostics.CurveDiagnosticEntry],
) -> dict[str, dict[str, float]]:
    """Join candidate diagnostics with the causal support envelope."""

    support_tier_map = build_support_tier_map()
    curve_row_list = load_csv(
        diagnostics_directory / "curve_payload_diagnostics.csv"
    )
    row_list_by_candidate: dict[str, list[dict[str, Any]]] = {}
    for row in curve_row_list:
        condition_id = condition_id_from_operating_values(
            float(row["speed_rpm"]),
            float(row["torque_nm"]),
            float(row["oil_temperature_deg"]),
        )
        if support_tier_map[condition_id] != "supported_core":
            continue
        row_list_by_candidate.setdefault(
            row["candidate_id"],
            [],
        ).append(row)

    r0_supported_row_list: list[dict[str, Any]] = []
    for entry in r0_entry_list:
        condition_id = condition_id_from_operating_values(
            entry.speed_rpm,
            entry.torque_nm,
            entry.oil_temperature_deg,
        )
        if support_tier_map[condition_id] != "supported_core":
            continue
        r0_supported_row_list.append(
            diagnostic_entry_to_metric_dictionary(entry)
        )
    row_list_by_candidate[
        "stage4_r0_causal_setpoint_pf_a"
    ] = r0_supported_row_list
    return {
        candidate_id: summarize_supported_core_metrics(row_list)
        for candidate_id, row_list in row_list_by_candidate.items()
    }


def build_all_eligible_forward_input_tensor(record: Any) -> torch.Tensor:
    """Build one causal five-column full-resolution forward input."""

    return torch.from_numpy(
        np.column_stack(
            (
                record.theta_deg.astype(np.float32),
                np.full(
                    record.theta_deg.size,
                    abs(record.nominal_speed_rpm),
                    dtype=np.float32,
                ),
                np.full(
                    record.theta_deg.size,
                    abs(record.nominal_torque_nm),
                    dtype=np.float32,
                ),
                np.full(
                    record.theta_deg.size,
                    record.nominal_temperature_deg_c,
                    dtype=np.float32,
                ),
                np.ones(record.theta_deg.size, dtype=np.float32),
            )
        ).astype(np.float32)
    )


def evaluate_residual_decomposition(
    candidate_configuration: dict[str, Any],
    forward_record_list: list[Any],
) -> dict[str, Any]:
    """Evaluate residual size, correlation, bounds, and finiteness."""

    candidate = (
        reference_family_vs_feedforward_support.load_track2_candidate(
            candidate_configuration
        )
    )
    assert candidate.training_config is not None
    model_object = candidate.model_object
    assert hasattr(model_object, "forward_regression_model")
    device = model_object.input_feature_mean.device
    residual_square_sum = 0.0
    analytical_square_sum = 0.0
    maximum_curve_ratio = 0.0
    maximum_absolute_residual_deg = 0.0
    correlation_value_list: list[float] = []
    finite_curve_count = 0
    bound_violation_count = 0
    declared_bound = float(
        candidate.training_config["model"]["residual_bound_deg"]
    )
    formulation = str(
        candidate.training_config["model"]["formulation"]
    ).upper()
    for record in forward_record_list:
        input_tensor = build_all_eligible_forward_input_tensor(
            record
        ).to(device)
        with torch.no_grad():
            normalized_input_tensor = model_object.normalize_input_tensor(
                input_tensor
            )
            _, auxiliary_dictionary = (
                model_object.forward_regression_model(
                    input_tensor,
                    normalized_input_tensor,
                )
            )
        residual_array = (
            auxiliary_dictionary["residual_prediction_deg"]
            .detach()
            .cpu()
            .numpy()
            .reshape(-1)
            .astype(np.float64)
        )
        analytical_array = (
            auxiliary_dictionary["analytical_prediction_deg"]
            .detach()
            .cpu()
            .numpy()
            .reshape(-1)
            .astype(np.float64)
        )
        finite_curve = bool(
            np.all(np.isfinite(residual_array))
            and np.all(np.isfinite(analytical_array))
        )
        finite_curve_count += int(finite_curve)
        residual_square_sum += float(np.sum(np.square(residual_array)))
        analytical_square_sum += float(
            np.sum(np.square(analytical_array))
        )
        residual_rms = float(
            np.sqrt(np.mean(np.square(residual_array)))
        )
        analytical_rms = float(
            np.sqrt(np.mean(np.square(analytical_array)))
        )
        maximum_curve_ratio = max(
            maximum_curve_ratio,
            residual_rms / max(analytical_rms, 1.0e-15),
        )
        maximum_absolute_residual_deg = max(
            maximum_absolute_residual_deg,
            float(np.max(np.abs(residual_array))),
        )
        if formulation == "R3":
            bound_violation_count += int(
                bool(
                    np.any(
                        np.abs(residual_array)
                        > declared_bound + 1.0e-7
                    )
                )
            )
        centered_residual = residual_array - np.mean(residual_array)
        centered_analytical = (
            analytical_array - np.mean(analytical_array)
        )
        denominator = float(
            np.linalg.norm(centered_residual)
            * np.linalg.norm(centered_analytical)
        )
        if denominator > 1.0e-15:
            correlation_value_list.append(
                float(
                    np.dot(centered_residual, centered_analytical)
                    / denominator
                )
            )
    population_ratio = math.sqrt(
        residual_square_sum / max(analytical_square_sum, 1.0e-30)
    )
    return {
        "candidate_id": candidate.candidate_id,
        "formulation": formulation,
        "eligible_curve_count": len(forward_record_list),
        "finite_curve_count": finite_curve_count,
        "population_residual_to_anchor_rms_ratio": population_ratio,
        "maximum_curve_residual_to_anchor_rms_ratio": (
            maximum_curve_ratio
        ),
        "maximum_absolute_residual_deg": (
            maximum_absolute_residual_deg
        ),
        "declared_residual_bound_deg": declared_bound,
        "bound_violation_curve_count": bound_violation_count,
        "mean_analytical_residual_correlation": (
            float(mean(correlation_value_list))
            if correlation_value_list
            else math.nan
        ),
    }


def build_decision_rows(
    supported_summary_map: dict[str, dict[str, float]],
    decomposition_map: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Apply the predeclared Stage 4 first-screen gates."""

    r0_summary = supported_summary_map[
        "stage4_r0_causal_setpoint_pf_a"
    ]
    matched_control_map = {
        "stage4_h01_r2_compact": "stage4_c01_r1_compact",
        "stage4_h02_r2_deep": "stage4_c02_r1_deep",
        "stage4_h03_r3_compact": "stage4_c01_r1_compact",
        "stage4_h04_r3_deep": "stage4_c02_r1_deep",
        "stage4_h05_r4_compact": "stage4_c03_r1_compact",
        "stage4_h06_r4_deep": "stage4_c04_r1_deep",
        "stage4_h07_r5_compact": "stage4_c05_r1_compact",
        "stage4_h08_r5_deep": "stage4_c06_r1_deep",
    }
    decision_row_list: list[dict[str, Any]] = []
    for hybrid_id, control_id in matched_control_map.items():
        hybrid_summary = supported_summary_map[hybrid_id]
        control_summary = supported_summary_map[control_id]
        decomposition = decomposition_map[hybrid_id]
        gate_dictionary = {
            "beats_r0_raw_mae": (
                hybrid_summary["curve_mae_deg"]
                < r0_summary["curve_mae_deg"]
            ),
            "beats_matched_control_raw_mae": (
                hybrid_summary["curve_mae_deg"]
                < control_summary["curve_mae_deg"]
            ),
            "centered_shape_within_gate": (
                hybrid_summary["centered_curve_mae_deg"]
                <= GENERAL_REGRESSION_MULTIPLIER
                * r0_summary["centered_curve_mae_deg"]
            ),
            "offset_within_gate": (
                hybrid_summary["absolute_curve_mean_error_deg"]
                <= GENERAL_REGRESSION_MULTIPLIER
                * r0_summary["absolute_curve_mean_error_deg"]
            ),
            "p95_within_gate": (
                hybrid_summary["p95_curve_mae_deg"]
                <= GENERAL_REGRESSION_MULTIPLIER
                * r0_summary["p95_curve_mae_deg"]
            ),
            "derivative_within_gate": (
                hybrid_summary["derivative_rmse_deg_per_deg"]
                <= GENERAL_REGRESSION_MULTIPLIER
                * r0_summary["derivative_rmse_deg_per_deg"]
            ),
            "amplitude_within_gate": (
                hybrid_summary["mean_harmonic_amplitude_error_pct"]
                <= GENERAL_REGRESSION_MULTIPLIER
                * r0_summary["mean_harmonic_amplitude_error_pct"]
            ),
            "phase_within_gate": (
                hybrid_summary["mean_harmonic_phase_error_deg"]
                <= GENERAL_REGRESSION_MULTIPLIER
                * r0_summary["mean_harmonic_phase_error_deg"]
            ),
            "peak_to_peak_within_gate": (
                hybrid_summary["peak_to_peak_error_pct"]
                <= PEAK_TO_PEAK_REGRESSION_MULTIPLIER
                * r0_summary["peak_to_peak_error_pct"]
            ),
            "finite_all_eligible_curves": (
                decomposition["finite_curve_count"]
                == decomposition["eligible_curve_count"]
            ),
            "residual_ratio_within_gate": (
                decomposition[
                    "population_residual_to_anchor_rms_ratio"
                ]
                <= RESIDUAL_TO_ANCHOR_RMS_MAXIMUM
            ),
            "residual_bound_respected": (
                decomposition["bound_violation_curve_count"] == 0
            ),
        }
        decision_row = {
            "hybrid_id": hybrid_id,
            "matched_control_id": control_id,
            "supported_core_curve_count": 96,
            "hybrid_raw_mae_deg": hybrid_summary["curve_mae_deg"],
            "r0_raw_mae_deg": r0_summary["curve_mae_deg"],
            "control_raw_mae_deg": control_summary["curve_mae_deg"],
            "hybrid_centered_mae_deg": hybrid_summary[
                "centered_curve_mae_deg"
            ],
            "hybrid_offset_error_deg": hybrid_summary[
                "absolute_curve_mean_error_deg"
            ],
            "hybrid_p95_curve_mae_deg": hybrid_summary[
                "p95_curve_mae_deg"
            ],
            "population_residual_to_anchor_rms_ratio": (
                decomposition[
                    "population_residual_to_anchor_rms_ratio"
                ]
            ),
            **gate_dictionary,
            "first_screen_pass": all(gate_dictionary.values()),
        }
        decision_row_list.append(decision_row)
    return decision_row_list


def markdown_table(
    header_list: list[str],
    row_list: list[list[str]],
) -> list[str]:
    """Build one compact Markdown table."""

    return [
        "| " + " | ".join(header_list) + " |",
        "| " + " | ".join(["---"] * len(header_list)) + " |",
        *[
            "| " + " | ".join(row) + " |"
            for row in row_list
        ],
    ]


def write_audit_report(
    decision_row_list: list[dict[str, Any]],
    decomposition_row_list: list[dict[str, Any]],
    r0_summary: dict[str, float],
) -> None:
    """Write the human-readable Stage 4 decision audit."""

    passing_id_list = [
        row["hybrid_id"]
        for row in decision_row_list
        if row["first_screen_pass"]
    ]
    line_list = [
        "# Stage 4 Curve-First And Cancellation Audit",
        "",
        "## Overview",
        "",
        "This audit applies the predeclared Stage 4 first-screen and opaque-",
        "cancellation gates to the eighteen-run data-only campaign.",
        "",
        "The primary surface contains `96` causal `supported_core` forward test",
        "conditions. One sparse/corner condition remains visible outside the",
        "promotion calculation. All decomposition checks span all `966` eligible",
        "forward conditions.",
        "",
        "## Frozen R0 Control",
        "",
        f"- supported-core raw MAE: `{r0_summary['curve_mae_deg']:.9f} deg`;",
        (
            "- supported-core centered-shape MAE: "
            f"`{r0_summary['centered_curve_mae_deg']:.9f} deg`;"
        ),
        (
            "- supported-core absolute offset error: "
            f"`{r0_summary['absolute_curve_mean_error_deg']:.9f} deg`;"
        ),
        f"- supported-core P95 curve MAE: `{r0_summary['p95_curve_mae_deg']:.9f} deg`.",
        "",
        "## Primary Hybrid Decisions",
        "",
    ]
    line_list.extend(
        markdown_table(
            [
                "Hybrid",
                "Control",
                "MAE [deg]",
                "R0 [deg]",
                "Control [deg]",
                "Residual/anchor RMS",
                "Pass",
            ],
            [
                [
                    str(row["hybrid_id"]),
                    str(row["matched_control_id"]),
                    f"{row['hybrid_raw_mae_deg']:.6f}",
                    f"{row['r0_raw_mae_deg']:.6f}",
                    f"{row['control_raw_mae_deg']:.6f}",
                    (
                        f"{row['population_residual_to_anchor_rms_ratio']:.4f}"
                    ),
                    "yes" if row["first_screen_pass"] else "no",
                ]
                for row in decision_row_list
            ],
        )
    )
    line_list.extend(
        [
            "",
            "## Decomposition",
            "",
        ]
    )
    line_list.extend(
        markdown_table(
            [
                "Candidate",
                "Formulation",
                "Finite",
                "Population RMS ratio",
                "Max curve ratio",
                "Max residual [deg]",
                "Bound violations",
            ],
            [
                [
                    str(row["candidate_id"]),
                    str(row["formulation"]),
                    (
                        f"{row['finite_curve_count']}/"
                        f"{row['eligible_curve_count']}"
                    ),
                    (
                        f"{row['population_residual_to_anchor_rms_ratio']:.4f}"
                    ),
                    (
                        f"{row['maximum_curve_residual_to_anchor_rms_ratio']:.4f}"
                    ),
                    f"{row['maximum_absolute_residual_deg']:.6f}",
                    str(row["bound_violation_curve_count"]),
                ]
                for row in decomposition_row_list
            ],
        )
    )
    line_list.extend(
        [
            "",
            "## Exit Decision",
            "",
        ]
    )
    if passing_id_list:
        line_list.extend(
            [
                (
                    "The following primary hybrid candidates pass the initial "
                    "screen: "
                    + ", ".join(f"`{value}`" for value in passing_id_list)
                    + "."
                ),
                "",
                (
                    "The simplest passing hybrid and its matched direct control "
                    "must continue to the two additional fixed seeds before "
                    "Stage 4 can close positively."
                ),
            ]
        )
    else:
        line_list.extend(
            [
                "No primary hybrid passes every first-screen gate.",
                "",
                (
                    "Stage 4 therefore closes as a valid negative result with "
                    "no residual architecture promoted and no stability-repeat "
                    "campaign required."
                ),
            ]
        )
    line_list.extend(
        [
            "",
            "The heavy official TE Curve Verification Pipeline was not run.",
            "This is a bounded Stage 4 campaign-closeout diagnostic only.",
            "",
        ]
    )
    AUDIT_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_REPORT_PATH.write_text(
        "\n".join(line_list),
        encoding="utf-8",
    )


def main() -> None:
    """Build the complete Stage 4 audit."""

    arguments = parse_arguments()
    diagnostics_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(
            arguments.diagnostics_directory
        )
    )
    assert (
        diagnostics_directory / "curve_payload_diagnostics.csv"
    ).is_file()
    matrix_config = load_yaml(MATRIX_CONFIG_PATH)
    selected_harmonic_list = [
        int(value)
        for value in matrix_config["evaluation"]["selected_harmonics"]
    ]
    curve_record_list, _, _, _ = (
        reference_family_vs_feedforward_support.build_curve_record_list(
            matrix_config,
            selected_harmonic_list,
        )
    )
    r0_entry_list = build_r0_diagnostic_entry_list(
        matrix_config,
        curve_record_list,
        selected_harmonic_list,
    )
    supported_summary_map = build_supported_core_summary_map(
        diagnostics_directory,
        r0_entry_list,
    )

    # Load All Eligible Curves For Decomposition Finiteness
    from scripts.analysis.polynomial_fourier_benchmark.run_phase1_polynomial_fourier_benchmark import (
        load_curve_records,
    )

    phase1_config = load_yaml(
        PROJECT_ROOT
        / "config"
        / "analysis"
        / "polynomial_fourier_benchmark"
        / "phase1_benchmark.yaml"
    )
    split_manifest = load_yaml(
        PROJECT_ROOT
        / "output"
        / "analysis"
        / "polynomial_fourier_benchmark"
        / "common_split_manifest.yaml"
    )
    excluded_condition_id_set = set(
        matrix_config["dataset"]["excluded_condition_id_list"]
    )
    all_curve_record_list = load_curve_records(
        phase1_config,
        split_manifest,
    )
    forward_record_list = [
        record
        for record in all_curve_record_list
        if record.direction == "Fw"
        and record.condition_id not in excluded_condition_id_set
    ]
    assert len(forward_record_list) == 966

    hybrid_candidate_configuration_list = [
        configuration
        for configuration in matrix_config["comparison"]["candidate_list"]
        if str(configuration["candidate_id"]).split("_")[1][0]
        in {"h", "a"}
    ]
    decomposition_row_list = [
        evaluate_residual_decomposition(
            candidate_configuration,
            forward_record_list,
        )
        for candidate_configuration in hybrid_candidate_configuration_list
    ]
    decomposition_map = {
        row["candidate_id"]: row for row in decomposition_row_list
    }
    decision_row_list = build_decision_rows(
        supported_summary_map,
        decomposition_map,
    )
    passing_candidate_id_list = [
        row["hybrid_id"]
        for row in decision_row_list
        if row["first_screen_pass"]
    ]
    simplest_passing_candidate_id = (
        passing_candidate_id_list[0]
        if passing_candidate_id_list
        else None
    )
    matched_control_id = (
        next(
            row["matched_control_id"]
            for row in decision_row_list
            if row["hybrid_id"] == simplest_passing_candidate_id
        )
        if simplest_passing_candidate_id is not None
        else None
    )
    audit_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage4",
        "status": "passed_with_continuation" if passing_candidate_id_list else "passed_negative",
        "diagnostics_directory": (
            shared_training_infrastructure.format_project_relative_path(
                diagnostics_directory
            )
        ),
        "causal_supported_core_test_curve_count": 96,
        "eligible_forward_curve_count": 966,
        "r0_supported_core_metrics": supported_summary_map[
            "stage4_r0_causal_setpoint_pf_a"
        ],
        "primary_candidate_count": len(decision_row_list),
        "passing_candidate_id_list": passing_candidate_id_list,
        "simplest_passing_candidate_id": simplest_passing_candidate_id,
        "matched_control_id_for_repeat": matched_control_id,
        "stability_repeat_required": bool(passing_candidate_id_list),
        "residual_to_anchor_rms_maximum": (
            RESIDUAL_TO_ANCHOR_RMS_MAXIMUM
        ),
        "general_regression_multiplier": (
            GENERAL_REGRESSION_MULTIPLIER
        ),
        "peak_to_peak_regression_multiplier": (
            PEAK_TO_PEAK_REGRESSION_MULTIPLIER
        ),
        "decision_matrix_path": (
            shared_training_infrastructure.format_project_relative_path(
                DECISION_MATRIX_PATH
            )
        ),
        "decomposition_path": (
            shared_training_infrastructure.format_project_relative_path(
                DECOMPOSITION_PATH
            )
        ),
        "audit_report_path": (
            shared_training_infrastructure.format_project_relative_path(
                AUDIT_REPORT_PATH
            )
        ),
        "official_te_curve_verification_pipeline_executed": False,
    }
    write_csv(DECISION_MATRIX_PATH, decision_row_list)
    write_csv(DECOMPOSITION_PATH, decomposition_row_list)
    write_yaml(AUDIT_SUMMARY_PATH, audit_payload)
    write_audit_report(
        decision_row_list,
        decomposition_row_list,
        supported_summary_map[
            "stage4_r0_causal_setpoint_pf_a"
        ],
    )
    print(yaml.safe_dump(audit_payload, sort_keys=False))


if __name__ == "__main__":
    main()
