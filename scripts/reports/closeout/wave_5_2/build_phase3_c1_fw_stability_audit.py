"""Build the Phase 3 C1-Fw parameter and curve-first stability audit."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import math
import textwrap
from pathlib import Path
from statistics import mean, pstdev
from typing import Any

# Import Scientific Python Utilities
import torch
import yaml

# Define Repository Paths
PROJECT_PATH = Path(__file__).resolve().parents[4]
PARENT_C1_REGISTRY_PATH = (
    PROJECT_PATH
    / "output"
    / "training_campaigns"
    / "2026-07-26-17-46-18_phase3_quasi_static_compliance_pinn_2026_07_26"
    / "candidate_registries"
    / "c1_linear_compliance_soft_fw.yaml"
)
REPEAT_CAMPAIGN_NAME = "phase3_c1_fw_stability_repeat_2026_07_26"
OUTPUT_DIRECTORY = (
    PROJECT_PATH / "output" / "analysis" / "pinn_program_compliance"
)
AUDIT_YAML_PATH = OUTPUT_DIRECTORY / "phase3_c1_fw_stability_audit.yaml"
AUDIT_CSV_PATH = OUTPUT_DIRECTORY / "phase3_c1_fw_stability_audit.csv"
REPORT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "model_development_waves"
    / "wave_5_2"
    / "quasi_static_compliance_pinn"
    / "[2026-07-26]"
    / "phase3_c1_fw_stability_audit.md"
)
STIFFNESS_STABILITY_CV_LIMIT = 0.10
CENTERED_SHAPE_REGRESSION_LIMIT = 1.02
HARMONIC_REGRESSION_LIMIT = 1.05


def read_yaml(path: Path) -> dict[str, Any]:
    """Read one required YAML mapping."""

    assert path.is_file(), f"Required YAML path does not exist | {path}"
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict), f"YAML root must be a mapping | {path}"
    return payload


def format_project_relative_path(path: Path) -> str:
    """Format one repository path with portable separators."""

    return path.resolve().relative_to(PROJECT_PATH.resolve()).as_posix()


def resolve_repeat_campaign_output_directory() -> Path:
    """Resolve the unique completed repeat-campaign output directory."""

    matching_path_list = sorted(
        (
            PROJECT_PATH / "output" / "training_campaigns"
        ).glob(f"*_{REPEAT_CAMPAIGN_NAME}")
    )
    assert len(matching_path_list) == 1, (
        "Expected exactly one stability-repeat campaign output | "
        f"matches={len(matching_path_list)}"
    )
    return matching_path_list[0]


def build_candidate_run_list() -> list[dict[str, Any]]:
    """Resolve the initial C1-Fw run and both seeded repeat runs."""

    parent_registry = read_yaml(PARENT_C1_REGISTRY_PATH)
    parent_entry = dict(parent_registry["best_entry"])
    parent_entry.update(
        {
            "candidate_id": "phase3_c1_linear_compliance_soft_Fw",
            "run_role": "initial_screen",
        }
    )

    repeat_campaign_output_directory = (
        resolve_repeat_campaign_output_directory()
    )
    repeat_leaderboard = read_yaml(
        repeat_campaign_output_directory / "campaign_leaderboard.yaml"
    )
    repeat_entry_list: list[dict[str, Any]] = []
    for entry in repeat_leaderboard["entry_list"]:
        output_directory = PROJECT_PATH / str(
            entry["output_directory"]
        ).replace("\\", "/")
        training_config = read_yaml(
            output_directory / "training_config.yaml"
        )
        random_seed = int(training_config["training"]["random_seed"])
        repeat_entry = dict(entry)
        repeat_entry.update(
            {
                "candidate_id": f"phase3_c1_fw_seed_{random_seed}",
                "run_role": "seeded_repeat",
            }
        )
        repeat_entry_list.append(repeat_entry)
    assert len(repeat_entry_list) == 2
    return [parent_entry] + sorted(
        repeat_entry_list,
        key=lambda entry: str(entry["candidate_id"]),
    )


def resolve_forward_stiffness(
    state_dictionary: dict[str, torch.Tensor],
    minimum_stiffness: float,
    maximum_stiffness: float,
) -> float:
    """Decode the bounded forward stiffness from the learned checkpoint."""

    raw_logit = state_dictionary[
        "regression_model.raw_direction_stiffness_logit"
    ][0]
    stiffness_fraction = float(torch.sigmoid(raw_logit).item())
    return (
        minimum_stiffness
        + (maximum_stiffness - minimum_stiffness)
        * stiffness_fraction
    )


def build_parameter_row(entry: dict[str, Any]) -> dict[str, Any]:
    """Extract one run's physical parameters and training diagnostics."""

    output_directory = PROJECT_PATH / str(
        entry["output_directory"]
    ).replace("\\", "/")
    training_config = read_yaml(output_directory / "training_config.yaml")
    metrics_summary = read_yaml(output_directory / "metrics_summary.yaml")
    checkpoint_path = PROJECT_PATH / str(
        entry["best_checkpoint_path"]
    ).replace("\\", "/")
    checkpoint_payload = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
    state_dictionary = checkpoint_payload["state_dict"]
    model_config = training_config["model"]
    minimum_stiffness = float(
        model_config["minimum_stiffness_nm_per_deg"]
    )
    maximum_stiffness = float(
        model_config["maximum_stiffness_nm_per_deg"]
    )
    fitted_forward_stiffness = resolve_forward_stiffness(
        state_dictionary,
        minimum_stiffness,
        maximum_stiffness,
    )
    fitted_forward_intercept = float(
        state_dictionary[
            "regression_model.direction_intercept_deg"
        ][0].item()
    )
    training_random_seed = training_config["training"].get(
        "random_seed"
    )
    test_metrics = metrics_summary["test_metrics"]
    validation_metrics = metrics_summary["validation_metrics"]
    return {
        "candidate_id": entry["candidate_id"],
        "run_role": entry["run_role"],
        "run_instance_id": entry["run_instance_id"],
        "training_random_seed": (
            int(training_random_seed)
            if training_random_seed is not None
            else None
        ),
        "output_directory": format_project_relative_path(
            output_directory
        ),
        "best_checkpoint_path": format_project_relative_path(
            checkpoint_path
        ),
        "minimum_stiffness_nm_per_deg": minimum_stiffness,
        "maximum_stiffness_nm_per_deg": maximum_stiffness,
        "fitted_forward_stiffness_nm_per_deg": (
            fitted_forward_stiffness
        ),
        "fitted_forward_intercept_deg": fitted_forward_intercept,
        "validation_mae_deg": float(validation_metrics["val_mae"]),
        "test_mae_deg": float(test_metrics["test_mae"]),
        "test_rmse_deg": float(test_metrics["test_rmse"]),
        "test_physics_compliance_equation_loss": float(
            test_metrics["test_physics_compliance_equation_loss"]
        ),
        "test_physics_zero_torque_boundary_loss": float(
            test_metrics["test_physics_zero_torque_boundary_loss"]
        ),
        "test_physics_compliance_monotonicity_loss": float(
            test_metrics["test_physics_compliance_monotonicity_loss"]
        ),
        "test_physics_stiffness_bounds_loss": float(
            test_metrics["test_physics_stiffness_bounds_loss"]
        ),
    }


def index_curve_first_summary(
    diagnostics_summary: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    """Index CVP 1.2 candidate summaries by candidate identifier."""

    return {
        str(entry["candidate_id"]): entry
        for entry in diagnostics_summary["candidate_summary_list"]
    }


def add_curve_first_metrics(
    parameter_row: dict[str, Any],
    curve_summary_by_candidate: dict[str, dict[str, Any]],
    control_summary: dict[str, Any],
) -> None:
    """Attach curve-first metrics and gate booleans to one C1-Fw row."""

    candidate_summary = curve_summary_by_candidate[
        str(parameter_row["candidate_id"])
    ]
    for metric_name in [
        "mean_curve_mae_deg",
        "mean_signed_curve_mean_error_deg",
        "mean_absolute_curve_mean_error_deg",
        "mean_centered_curve_mae_deg",
        "mean_peak_to_peak_error_pct",
        "mean_harmonic_amplitude_error_pct",
        "mean_harmonic_phase_error_deg",
    ]:
        parameter_row[metric_name] = float(
            candidate_summary[metric_name]
        )

    parameter_row["raw_error_improves_control"] = (
        parameter_row["mean_curve_mae_deg"]
        < float(control_summary["mean_curve_mae_deg"])
    )
    parameter_row["offset_error_improves_control"] = (
        parameter_row["mean_absolute_curve_mean_error_deg"]
        < float(control_summary["mean_absolute_curve_mean_error_deg"])
    )
    parameter_row["centered_shape_within_gate"] = (
        parameter_row["mean_centered_curve_mae_deg"]
        <= CENTERED_SHAPE_REGRESSION_LIMIT
        * float(control_summary["mean_centered_curve_mae_deg"])
    )
    parameter_row["harmonic_amplitude_within_gate"] = (
        parameter_row["mean_harmonic_amplitude_error_pct"]
        <= HARMONIC_REGRESSION_LIMIT
        * float(control_summary["mean_harmonic_amplitude_error_pct"])
    )
    parameter_row["harmonic_phase_within_gate"] = (
        parameter_row["mean_harmonic_phase_error_deg"]
        <= HARMONIC_REGRESSION_LIMIT
        * float(control_summary["mean_harmonic_phase_error_deg"])
    )
    parameter_row["run_curve_first_gate_pass"] = all(
        bool(parameter_row[key])
        for key in [
            "raw_error_improves_control",
            "offset_error_improves_control",
            "centered_shape_within_gate",
            "harmonic_amplitude_within_gate",
            "harmonic_phase_within_gate",
        ]
    )


def write_csv_file(row_list: list[dict[str, Any]]) -> None:
    """Write the per-run audit table."""

    field_name_list = list(row_list[0].keys())
    with AUDIT_CSV_PATH.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=field_name_list,
        )
        writer.writeheader()
        writer.writerows(row_list)


def format_metric(value: Any, digits: int = 6) -> str:
    """Format one numeric report cell."""

    if value is None:
        return "screening run"
    if isinstance(value, bool):
        return "pass" if value else "fail"
    if isinstance(value, int):
        return str(value)
    return f"{float(value):.{digits}f}"


def write_report(
    row_list: list[dict[str, Any]],
    audit_payload: dict[str, Any],
) -> None:
    """Write the human-readable stability audit report."""

    aggregate = audit_payload["aggregate"]
    table_line_list = [
        (
            "| Run | Seed | Stiffness [Nm/deg] | Raw MAE [deg] | "
            "Offset [deg] | Centered [deg] | Harmonic amp [%] | "
            "Phase [deg] | P2P [%] | Gate |"
        ),
        (
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | "
            "---: | ---: | --- |"
        ),
    ]
    for row in row_list:
        table_line_list.append(
            "| "
            + " | ".join(
                [
                    f"`{row['candidate_id']}`",
                    format_metric(row["training_random_seed"]),
                    format_metric(
                        row["fitted_forward_stiffness_nm_per_deg"],
                        2,
                    ),
                    format_metric(row["mean_curve_mae_deg"]),
                    format_metric(
                        row["mean_absolute_curve_mean_error_deg"]
                    ),
                    format_metric(
                        row["mean_centered_curve_mae_deg"]
                    ),
                    format_metric(
                        row["mean_harmonic_amplitude_error_pct"],
                        3,
                    ),
                    format_metric(
                        row["mean_harmonic_phase_error_deg"],
                        3,
                    ),
                    format_metric(
                        row["mean_peak_to_peak_error_pct"],
                        3,
                    ),
                    format_metric(row["run_curve_first_gate_pass"]),
                ]
            )
            + " |"
        )

    decision_text = (
        "C1-Fw is retained as a conditional Phase 3 physical ingredient "
        "for later PINN compositions, but it does not replace either accepted "
        "Fw reference."
        if audit_payload["decision"]["retain_c1_fw_physical_ingredient"]
        else (
            "C1-Fw is not retained as a stable Phase 3 physical ingredient. "
            "The linear-compliance residual remains documented evidence only."
        )
    )
    report_line_list = [
        "# Phase 3 C1-Fw Stability Audit",
        "",
        "## Overview",
        "",
        (
            "This audit compares the initial C1-Fw screening run with two "
            "reproducibly seeded repeats on the same immutable 97-curve Fw "
            "held-out surface. It combines fitted physical parameters with "
            "CVP 1.2 raw, offset, centered-shape, harmonic, phase, and "
            "peak-to-peak evidence."
        ),
        "",
        "## Reproducibility Contract",
        "",
        (
            "The repeat runs preserve architecture, data split, loss weights, "
            "and runtime profile. Only `training.random_seed` changes. "
            "`seed_everything(seed, workers=True)` seeds Python, NumPy, "
            "PyTorch, samplers, and DataLoader workers before model creation."
        ),
        "",
        *table_line_list,
        "",
        "## Aggregate Stability",
        "",
        (
            f"- fitted stiffness mean: "
            f"{aggregate['stiffness_mean_nm_per_deg']:.2f} Nm/deg;"
        ),
        (
            f"- fitted stiffness population CV: "
            f"{aggregate['stiffness_population_cv']:.4f};"
        ),
        (
            f"- per-run curve-first gate passes: "
            f"{aggregate['curve_first_gate_pass_count']}/3;"
        ),
        (
            f"- all stiffness-bound losses are zero: "
            f"`{str(aggregate['all_stiffness_bound_losses_zero']).lower()}`;"
        ),
        (
            f"- accepted-reference replacement: "
            f"`{str(audit_payload['decision']['replace_accepted_reference']).lower()}`."
        ),
        "",
        "The peak-to-peak column remains visible as a separate caution. It is "
        "not hidden by the aggregate gate.",
        "",
        "## Decision",
        "",
        decision_text,
        "",
        (
            "This is a Phase 3 ingredient-selection decision, not an official "
            "TE Curve Verification Pipeline promotion and not a claim that "
            "the C1 model is the best deployed predictor."
        ),
        "",
        "## Machine-Readable Evidence",
        "",
        f"- `{format_project_relative_path(AUDIT_YAML_PATH)}`",
        f"- `{format_project_relative_path(AUDIT_CSV_PATH)}`",
        "",
    ]
    wrapped_report_line_list: list[str] = []
    for report_line in report_line_list:
        if (
            not report_line
            or report_line.startswith(("#", "|", "- `", "```"))
        ):
            wrapped_report_line_list.append(report_line)
            continue
        wrapped_report_line_list.extend(
            textwrap.wrap(
                report_line,
                width=96,
                break_long_words=False,
                break_on_hyphens=False,
            )
        )

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(
        "\n".join(wrapped_report_line_list),
        encoding="utf-8",
    )


def main() -> None:
    """Build the complete C1-Fw stability audit."""

    argument_parser = argparse.ArgumentParser(
        description="Build Phase 3 C1-Fw stability evidence."
    )
    argument_parser.add_argument(
        "--curve-diagnostics-summary-path",
        type=Path,
        required=True,
    )
    arguments = argument_parser.parse_args()
    diagnostics_summary_path = (
        arguments.curve_diagnostics_summary_path.resolve()
    )
    diagnostics_summary = read_yaml(diagnostics_summary_path)
    curve_summary_by_candidate = index_curve_first_summary(
        diagnostics_summary
    )
    control_summary = curve_summary_by_candidate[
        "phase3_c0_learned_mean_control_Fw"
    ]

    row_list = [
        build_parameter_row(entry)
        for entry in build_candidate_run_list()
    ]
    for row in row_list:
        add_curve_first_metrics(
            row,
            curve_summary_by_candidate,
            control_summary,
        )

    stiffness_value_list = [
        float(row["fitted_forward_stiffness_nm_per_deg"])
        for row in row_list
    ]
    stiffness_mean = mean(stiffness_value_list)
    stiffness_population_cv = (
        pstdev(stiffness_value_list) / stiffness_mean
        if not math.isclose(stiffness_mean, 0.0)
        else math.inf
    )
    all_stiffness_bound_losses_zero = all(
        math.isclose(
            float(row["test_physics_stiffness_bounds_loss"]),
            0.0,
            abs_tol=1.0e-12,
        )
        for row in row_list
    )
    curve_first_gate_pass_count = sum(
        bool(row["run_curve_first_gate_pass"])
        for row in row_list
    )
    retain_c1_fw_physical_ingredient = (
        curve_first_gate_pass_count == len(row_list)
        and stiffness_population_cv <= STIFFNESS_STABILITY_CV_LIMIT
        and all_stiffness_bound_losses_zero
    )
    audit_payload = {
        "schema_version": 1,
        "audit_name": "phase3_c1_fw_initialization_stability",
        "curve_diagnostics_summary_path": (
            format_project_relative_path(diagnostics_summary_path)
        ),
        "run_count": len(row_list),
        "control_candidate_id": (
            "phase3_c0_learned_mean_control_Fw"
        ),
        "thresholds": {
            "stiffness_population_cv_maximum": (
                STIFFNESS_STABILITY_CV_LIMIT
            ),
            "centered_shape_control_ratio_maximum": (
                CENTERED_SHAPE_REGRESSION_LIMIT
            ),
            "harmonic_control_ratio_maximum": (
                HARMONIC_REGRESSION_LIMIT
            ),
        },
        "run_list": row_list,
        "aggregate": {
            "stiffness_mean_nm_per_deg": stiffness_mean,
            "stiffness_population_std_nm_per_deg": pstdev(
                stiffness_value_list
            ),
            "stiffness_population_cv": stiffness_population_cv,
            "curve_first_gate_pass_count": curve_first_gate_pass_count,
            "all_stiffness_bound_losses_zero": (
                all_stiffness_bound_losses_zero
            ),
        },
        "decision": {
            "retain_c1_fw_physical_ingredient": (
                retain_c1_fw_physical_ingredient
            ),
            "replace_accepted_reference": False,
            "official_track2_promotion": False,
            "decision_scope": (
                "Phase 3 physical-ingredient selection only"
            ),
        },
        "artifact_paths": {
            "csv": format_project_relative_path(AUDIT_CSV_PATH),
            "report": format_project_relative_path(REPORT_PATH),
        },
    }
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    with AUDIT_YAML_PATH.open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as output_file:
        yaml.safe_dump(
            audit_payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )
    write_csv_file(row_list)
    write_report(row_list, audit_payload)
    print(
        "PHASE3_C1_FW_STABILITY_AUDIT_OK "
        f"gate_passes={curve_first_gate_pass_count}/{len(row_list)} "
        f"stiffness_cv={stiffness_population_cv:.6f} "
        f"retain={str(retain_c1_fw_physical_ingredient).lower()}"
    )
    print(format_project_relative_path(AUDIT_YAML_PATH))
    print(format_project_relative_path(REPORT_PATH))


if __name__ == "__main__":
    main()
