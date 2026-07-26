"""Build the Phase 3 quasi-static compliance identifiability audit."""

from __future__ import annotations

import argparse
import csv
import hashlib
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import yaml


# Repository Paths
PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "analysis"
    / "pinn_program_compliance"
    / "phase3_compliance_audit.yaml"
)

# Audit Constants
DIRECTION_NAME_LIST = ("Fw", "Bw")
SPLIT_NAME_LIST = ("train", "validation", "test")
CONDITION_AUDIT_FIELD_NAME_LIST = [
    "condition_id",
    "split",
    "direction",
    "nominal_speed_rpm",
    "nominal_torque_nm",
    "measured_signed_torque_nm",
    "measured_temperature_deg_c",
    "measured_curve_mean_te_deg",
    "measured_curve_peak_to_peak_te_deg",
    "low_torque_condition",
    "direction_torque_sign_pass",
]
FORMULATION_METRIC_FIELD_NAME_LIST = [
    "formulation",
    "surface",
    "split",
    "curve_count",
    "mae_deg",
    "rmse_deg",
    "signed_bias_deg",
    "design_rank",
    "design_column_count",
    "design_condition_number",
    "linear_compliance_deg_per_nm",
    "effective_stiffness_nm_per_deg",
    "minimum_compliance_derivative_deg_per_nm",
    "positive_stiffness_pass",
    "monotonicity_pass",
]


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Build the non-training observability, identifiability, and "
            "analytical-transfer audit required before Wave 5.2 Phase 3."
        )
    )
    argument_parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the Phase 3 compliance-audit configuration.",
    )
    return argument_parser.parse_args()


def load_configuration(config_path: Path) -> dict[str, Any]:

    """Load and validate the Phase 3 audit configuration.

    Args:
        config_path: Repository-relative or absolute configuration path.

    Returns:
        Parsed configuration mapping.
    """

    resolved_config_path = _resolve_project_path(config_path)
    assert resolved_config_path.is_file(), (
        f"Phase 3 audit configuration does not exist | {resolved_config_path}"
    )
    configuration = yaml.safe_load(
        resolved_config_path.read_text(encoding="utf-8")
    )
    assert configuration["schema_version"] == 1, (
        "Unsupported Phase 3 audit configuration schema"
    )
    return configuration


def build_phase3_compliance_audit(
    configuration: dict[str, Any],
    config_path: Path,
) -> dict[str, Any]:

    """Build and persist the complete Phase 3 entry-gate package.

    Args:
        configuration: Validated Phase 3 audit configuration.
        config_path: Configuration path used for provenance.

    Returns:
        Persisted summary payload.
    """

    # Load Canonical Phase 0 And Phase 1 Evidence
    phase0_curve_audit_path = _resolve_project_path(
        configuration["inputs"]["phase0_curve_audit_csv"]
    )
    common_split_manifest_csv_path = _resolve_project_path(
        configuration["inputs"]["common_split_manifest_csv"]
    )
    common_split_manifest_yaml_path = _resolve_project_path(
        configuration["inputs"]["common_split_manifest_yaml"]
    )
    phase0_row_list = _read_csv_rows(phase0_curve_audit_path)
    manifest_row_list = _read_csv_rows(common_split_manifest_csv_path)
    manifest_payload = yaml.safe_load(
        common_split_manifest_yaml_path.read_text(encoding="utf-8")
    )

    # Restrict Audit To Exact Eligible Manifest Conditions
    operating_metadata_pass_by_condition_id: dict[str, list[bool]] = (
        defaultdict(list)
    )
    for phase0_row in phase0_row_list:
        operating_metadata_pass_by_condition_id[
            phase0_row["condition_id"]
        ].append(phase0_row["operating_metadata_pass"].lower() == "true")
    eligible_condition_id_set = {
        condition_id
        for condition_id, pass_list in (
            operating_metadata_pass_by_condition_id.items()
        )
        if len(pass_list) == 2 and all(pass_list)
    }
    expected_condition_count = int(
        configuration["analysis"]["expected_eligible_condition_count"]
    )
    assert len(eligible_condition_id_set) == expected_condition_count, (
        "Unexpected eligible-condition count | "
        f"{len(eligible_condition_id_set)} != {expected_condition_count}"
    )
    manifest_row_by_condition_id = {
        row["condition_id"]: row
        for row in manifest_row_list
        if row["condition_id"] in eligible_condition_id_set
    }

    condition_audit_row_list = _build_condition_audit_rows(
        phase0_row_list,
        manifest_row_by_condition_id,
        configuration,
    )
    _validate_condition_contract(condition_audit_row_list, configuration)

    # Fit Training-Only Analytical Probes
    formulation_result_list = _build_formulation_results(
        condition_audit_row_list,
        configuration,
    )
    formulation_metric_row_list = [
        metric_row
        for formulation_result in formulation_result_list
        for metric_row in formulation_result["metric_row_list"]
    ]

    # Build Entry-Gate Evidence
    support_payload = _build_support_payload(
        condition_audit_row_list,
        configuration,
    )
    identifiability_payload = _build_identifiability_payload(
        formulation_result_list,
        configuration,
    )
    entry_gate_payload = _build_entry_gate_payload(
        support_payload,
        identifiability_payload,
    )
    summary_payload = {
        "schema_version": 1,
        "audit_id": configuration["metadata"]["audit_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_configuration": {
            "path": _project_relative_path(_resolve_project_path(config_path)),
            "sha256": _sha256_file(_resolve_project_path(config_path)),
        },
        "source_evidence": {
            "phase0_curve_audit_csv": {
                "path": _project_relative_path(phase0_curve_audit_path),
                "sha256": _sha256_file(phase0_curve_audit_path),
            },
            "common_split_manifest_csv": {
                "path": _project_relative_path(common_split_manifest_csv_path),
                "sha256": _sha256_file(common_split_manifest_csv_path),
            },
            "common_split_manifest_yaml": {
                "path": _project_relative_path(common_split_manifest_yaml_path),
                "sha256": _sha256_file(common_split_manifest_yaml_path),
                "assignment_sha256": manifest_payload["split"][
                    "assignment_sha256"
                ],
            },
        },
        "support": support_payload,
        "identifiability": identifiability_payload,
        "observability_limitations": {
            "repeated_directional_conditions_available": False,
            "ordered_load_unload_trajectories_available": False,
            "reversal_state_available": False,
            "decision": (
                "Do not infer hysteresis, friction, or load-unload state in "
                "Phase 3; retain those mechanisms for Phase 4."
            ),
        },
        "entry_gate": entry_gate_payload,
        "output_identity": {},
    }

    # Persist Tables Before Declaring Their Identity
    output_directory = _resolve_project_path(
        configuration["outputs"]["output_directory"]
    )
    output_directory.mkdir(parents=True, exist_ok=True)
    condition_audit_csv_path = (
        output_directory / configuration["outputs"]["condition_audit_csv"]
    )
    formulation_metrics_csv_path = (
        output_directory / configuration["outputs"]["formulation_metrics_csv"]
    )
    _write_csv_rows(
        condition_audit_csv_path,
        CONDITION_AUDIT_FIELD_NAME_LIST,
        condition_audit_row_list,
    )
    _write_csv_rows(
        formulation_metrics_csv_path,
        FORMULATION_METRIC_FIELD_NAME_LIST,
        formulation_metric_row_list,
    )
    summary_payload["output_identity"] = {
        "condition_audit_csv": {
            "path": _project_relative_path(condition_audit_csv_path),
            "sha256": _sha256_file(condition_audit_csv_path),
            "row_count": len(condition_audit_row_list),
        },
        "formulation_metrics_csv": {
            "path": _project_relative_path(formulation_metrics_csv_path),
            "sha256": _sha256_file(formulation_metrics_csv_path),
            "row_count": len(formulation_metric_row_list),
        },
    }

    # Write Canonical Summary And Report
    summary_yaml_path = (
        output_directory / configuration["outputs"]["summary_yaml"]
    )
    summary_yaml_path.write_text(
        yaml.safe_dump(summary_payload, sort_keys=False, width=100),
        encoding="utf-8",
    )
    report_markdown_path = _resolve_project_path(
        configuration["outputs"]["report_markdown"]
    )
    report_markdown_path.parent.mkdir(parents=True, exist_ok=True)
    report_markdown_path.write_text(
        _build_markdown_report(summary_payload, formulation_metric_row_list),
        encoding="utf-8",
    )
    print(
        "PHASE3_COMPLIANCE_AUDIT_OK "
        f"curves={len(condition_audit_row_list)} "
        f"metrics={len(formulation_metric_row_list)} "
        f"entry_gate={entry_gate_payload['status']}"
    )
    return summary_payload


def validate_written_outputs(
    configuration: dict[str, Any],
) -> dict[str, int]:

    """Validate Phase 3 persisted hashes, row counts, and exit gate.

    Args:
        configuration: Validated Phase 3 audit configuration.

    Returns:
        Validated output row counts keyed by artifact role.
    """

    # Load Summary And Resolve Outputs
    output_directory = _resolve_project_path(
        configuration["outputs"]["output_directory"]
    )
    summary_yaml_path = (
        output_directory / configuration["outputs"]["summary_yaml"]
    )
    assert summary_yaml_path.is_file(), (
        f"Missing Phase 3 summary | {summary_yaml_path}"
    )
    summary_payload = yaml.safe_load(
        summary_yaml_path.read_text(encoding="utf-8")
    )
    assert summary_payload["entry_gate"]["status"] == "pass", (
        "Phase 3 compliance entry gate did not pass"
    )

    # Verify Content Identity
    validated_row_count_map: dict[str, int] = {}
    for artifact_role, identity_payload in summary_payload[
        "output_identity"
    ].items():
        artifact_path = _resolve_project_path(identity_payload["path"])
        assert artifact_path.is_file(), (
            f"Missing Phase 3 output | {artifact_role} | {artifact_path}"
        )
        assert _sha256_file(artifact_path) == identity_payload["sha256"], (
            f"Phase 3 output hash mismatch | {artifact_role}"
        )
        row_count = len(_read_csv_rows(artifact_path))
        assert row_count == int(identity_payload["row_count"]), (
            f"Phase 3 output row-count mismatch | {artifact_role}"
        )
        validated_row_count_map[artifact_role] = row_count

    # Verify Canonical Contract
    expected_curve_count = (
        int(configuration["analysis"]["expected_eligible_condition_count"]) * 2
    )
    assert (
        validated_row_count_map["condition_audit_csv"]
        == expected_curve_count
    ), "Phase 3 eligible directional curve count changed"
    assert summary_payload["support"]["paired_direction_contract_pass"] is True
    assert summary_payload["support"]["zero_torque_support_pass"] is True
    assert summary_payload["identifiability"]["c1_linear"]["full_rank"] is True
    assert summary_payload["identifiability"]["c5_shared"]["full_rank"] is True
    return validated_row_count_map


def _build_condition_audit_rows(
    phase0_row_list: list[dict[str, str]],
    manifest_row_by_condition_id: dict[str, dict[str, str]],
    configuration: dict[str, Any],
) -> list[dict[str, Any]]:

    """Build one compact compliance-audit row per eligible directional curve."""

    condition_audit_row_list: list[dict[str, Any]] = []
    low_torque_threshold_nm = float(
        configuration["analysis"]["low_torque_threshold_nm"]
    )
    for phase0_row in phase0_row_list:
        condition_id = phase0_row["condition_id"]
        if condition_id not in manifest_row_by_condition_id:
            continue
        manifest_row = manifest_row_by_condition_id[condition_id]
        direction = phase0_row["direction"]
        measured_torque_nm = float(phase0_row["mean_torque_nm"])
        nominal_torque_nm = float(manifest_row["output_torque_nm"])
        direction_torque_sign_pass = (
            abs(nominal_torque_nm) <= low_torque_threshold_nm
            or (direction == "Fw" and measured_torque_nm < 0.0)
            or (direction == "Bw" and measured_torque_nm > 0.0)
        )
        condition_audit_row_list.append(
            {
                "condition_id": condition_id,
                "split": manifest_row["split"],
                "direction": direction,
                "nominal_speed_rpm": float(
                    manifest_row["input_speed_rpm"]
                ),
                "nominal_torque_nm": nominal_torque_nm,
                "measured_signed_torque_nm": measured_torque_nm,
                "measured_temperature_deg_c": float(
                    phase0_row["mean_temperature_deg_c"]
                ),
                "measured_curve_mean_te_deg": float(
                    phase0_row["mean_te_deg"]
                ),
                "measured_curve_peak_to_peak_te_deg": float(
                    phase0_row["te_peak_to_peak_deg"]
                ),
                "low_torque_condition": (
                    abs(nominal_torque_nm) <= low_torque_threshold_nm
                ),
                "direction_torque_sign_pass": direction_torque_sign_pass,
            }
        )
    condition_audit_row_list.sort(
        key=lambda row: (
            SPLIT_NAME_LIST.index(row["split"]),
            row["condition_id"],
            DIRECTION_NAME_LIST.index(row["direction"]),
        )
    )
    return condition_audit_row_list


def _validate_condition_contract(
    condition_audit_row_list: list[dict[str, Any]],
    configuration: dict[str, Any],
) -> None:

    """Validate exact split and paired-direction row counts."""

    expected_split_count_map = configuration["analysis"][
        "expected_curve_count_per_direction"
    ]
    row_count_map: dict[tuple[str, str], int] = defaultdict(int)
    direction_set_by_condition_id: dict[str, set[str]] = defaultdict(set)
    for row in condition_audit_row_list:
        row_count_map[(row["split"], row["direction"])] += 1
        direction_set_by_condition_id[row["condition_id"]].add(row["direction"])
    for split_name in SPLIT_NAME_LIST:
        for direction_name in DIRECTION_NAME_LIST:
            assert row_count_map[(split_name, direction_name)] == int(
                expected_split_count_map[split_name]
            ), (
                "Phase 3 exact split count mismatch | "
                f"{split_name} | {direction_name}"
            )
    assert all(
        direction_set == set(DIRECTION_NAME_LIST)
        for direction_set in direction_set_by_condition_id.values()
    ), "Every Phase 3 condition must retain both directions"


def _build_formulation_results(
    condition_audit_row_list: list[dict[str, Any]],
    configuration: dict[str, Any],
) -> list[dict[str, Any]]:

    """Fit training-only analytical probes and evaluate every split."""

    formulation_result_list: list[dict[str, Any]] = []
    for direction_name in DIRECTION_NAME_LIST:
        direction_row_list = [
            row
            for row in condition_audit_row_list
            if row["direction"] == direction_name
        ]
        for formulation_name in ("C0", "C1", "C2", "C3"):
            formulation_result_list.append(
                _fit_formulation(
                    formulation_name,
                    direction_name,
                    direction_row_list,
                    configuration,
                )
            )
    formulation_result_list.append(
        _fit_formulation(
            "C5",
            "global",
            condition_audit_row_list,
            configuration,
        )
    )
    return formulation_result_list


def _fit_formulation(
    formulation_name: str,
    surface_name: str,
    row_list: list[dict[str, Any]],
    configuration: dict[str, Any],
) -> dict[str, Any]:

    """Fit one analytical mean-surface probe on training rows only."""

    training_row_list = [
        row for row in row_list if row["split"] == "train"
    ]
    training_design_matrix = _build_design_matrix(
        formulation_name,
        training_row_list,
        configuration,
    )
    training_target_array = np.asarray(
        [row["measured_curve_mean_te_deg"] for row in training_row_list],
        dtype=np.float64,
    )
    coefficient_array, _, design_rank, singular_value_array = np.linalg.lstsq(
        training_design_matrix,
        training_target_array,
        rcond=None,
    )
    assert np.all(np.isfinite(coefficient_array)), (
        f"Non-finite analytical coefficients | {formulation_name} | "
        f"{surface_name}"
    )
    design_condition_number = _condition_number(singular_value_array)
    physical_payload = _evaluate_physical_properties(
        formulation_name,
        coefficient_array,
        row_list,
        configuration,
    )

    metric_row_list: list[dict[str, Any]] = []
    for split_name in SPLIT_NAME_LIST:
        split_row_list = [
            row for row in row_list if row["split"] == split_name
        ]
        split_design_matrix = _build_design_matrix(
            formulation_name,
            split_row_list,
            configuration,
        )
        target_array = np.asarray(
            [row["measured_curve_mean_te_deg"] for row in split_row_list],
            dtype=np.float64,
        )
        prediction_array = split_design_matrix @ coefficient_array
        error_array = prediction_array - target_array
        metric_row_list.append(
            {
                "formulation": formulation_name,
                "surface": surface_name,
                "split": split_name,
                "curve_count": len(split_row_list),
                "mae_deg": float(np.mean(np.abs(error_array))),
                "rmse_deg": float(np.sqrt(np.mean(error_array**2))),
                "signed_bias_deg": float(np.mean(error_array)),
                "design_rank": int(design_rank),
                "design_column_count": training_design_matrix.shape[1],
                "design_condition_number": design_condition_number,
                **physical_payload,
            }
        )
    return {
        "formulation": formulation_name,
        "surface": surface_name,
        "coefficient_list": coefficient_array.tolist(),
        "design_rank": int(design_rank),
        "design_column_count": training_design_matrix.shape[1],
        "design_condition_number": design_condition_number,
        "physical": physical_payload,
        "metric_row_list": metric_row_list,
    }


def _build_design_matrix(
    formulation_name: str,
    row_list: list[dict[str, Any]],
    configuration: dict[str, Any],
) -> np.ndarray:

    """Build one explicit analytical compliance design matrix."""

    torque_array = np.asarray(
        [row["measured_signed_torque_nm"] for row in row_list],
        dtype=np.float64,
    )
    temperature_array = np.asarray(
        [row["measured_temperature_deg_c"] for row in row_list],
        dtype=np.float64,
    )
    if formulation_name == "C0":
        return np.ones((len(row_list), 1), dtype=np.float64)
    if formulation_name == "C1":
        return np.column_stack(
            [np.ones(len(row_list), dtype=np.float64), torque_array]
        )
    if formulation_name == "C2":
        reference_temperature_deg_c = float(
            configuration["analysis"]["reference_temperature_deg_c"]
        )
        temperature_scale_deg_c = float(
            configuration["analysis"]["temperature_scale_deg_c"]
        )
        normalized_temperature_array = (
            temperature_array - reference_temperature_deg_c
        ) / temperature_scale_deg_c
        return np.column_stack(
            [
                np.ones(len(row_list), dtype=np.float64),
                torque_array,
                torque_array * normalized_temperature_array,
            ]
        )
    if formulation_name == "C3":
        nonlinear_torque_scale_nm = float(
            configuration["analysis"]["nonlinear_torque_scale_nm"]
        )
        return np.column_stack(
            [
                np.ones(len(row_list), dtype=np.float64),
                torque_array,
                np.tanh(torque_array / nonlinear_torque_scale_nm),
            ]
        )
    assert formulation_name == "C5", (
        f"Unsupported compliance formulation | {formulation_name}"
    )
    forward_indicator_array = np.asarray(
        [row["direction"] == "Fw" for row in row_list],
        dtype=np.float64,
    )
    backward_indicator_array = 1.0 - forward_indicator_array
    return np.column_stack(
        [forward_indicator_array, backward_indicator_array, torque_array]
    )


def _evaluate_physical_properties(
    formulation_name: str,
    coefficient_array: np.ndarray,
    row_list: list[dict[str, Any]],
    configuration: dict[str, Any],
) -> dict[str, Any]:

    """Evaluate sign, stiffness, and monotonicity of fitted mean laws."""

    if formulation_name == "C0":
        return {
            "linear_compliance_deg_per_nm": 0.0,
            "effective_stiffness_nm_per_deg": 0.0,
            "minimum_compliance_derivative_deg_per_nm": 0.0,
            "positive_stiffness_pass": False,
            "monotonicity_pass": False,
        }

    linear_coefficient_index = 2 if formulation_name == "C5" else 1
    linear_compliance = float(coefficient_array[linear_coefficient_index])
    minimum_derivative = linear_compliance
    if formulation_name == "C2":
        temperature_value_array = np.asarray(
            [row["measured_temperature_deg_c"] for row in row_list],
            dtype=np.float64,
        )
        reference_temperature_deg_c = float(
            configuration["analysis"]["reference_temperature_deg_c"]
        )
        temperature_scale_deg_c = float(
            configuration["analysis"]["temperature_scale_deg_c"]
        )
        compliance_array = (
            linear_compliance
            + float(coefficient_array[2])
            * (
                temperature_value_array - reference_temperature_deg_c
            )
            / temperature_scale_deg_c
        )
        minimum_derivative = float(np.min(compliance_array))
    elif formulation_name == "C3":
        torque_value_array = np.linspace(
            min(row["measured_signed_torque_nm"] for row in row_list),
            max(row["measured_signed_torque_nm"] for row in row_list),
            1024,
            dtype=np.float64,
        )
        nonlinear_torque_scale_nm = float(
            configuration["analysis"]["nonlinear_torque_scale_nm"]
        )
        normalized_torque_array = (
            torque_value_array / nonlinear_torque_scale_nm
        )
        nonlinear_derivative_array = (
            float(coefficient_array[2])
            / nonlinear_torque_scale_nm
            / np.cosh(normalized_torque_array) ** 2
        )
        minimum_derivative = float(
            np.min(linear_compliance + nonlinear_derivative_array)
        )

    positive_stiffness_pass = minimum_derivative > 0.0
    effective_stiffness = (
        1.0 / linear_compliance if linear_compliance > 0.0 else 0.0
    )
    return {
        "linear_compliance_deg_per_nm": linear_compliance,
        "effective_stiffness_nm_per_deg": effective_stiffness,
        "minimum_compliance_derivative_deg_per_nm": minimum_derivative,
        "positive_stiffness_pass": positive_stiffness_pass,
        "monotonicity_pass": positive_stiffness_pass,
    }


def _build_support_payload(
    condition_audit_row_list: list[dict[str, Any]],
    configuration: dict[str, Any],
) -> dict[str, Any]:

    """Summarize split, sign, temperature, and low-torque support."""

    support_by_direction: dict[str, Any] = {}
    for direction_name in DIRECTION_NAME_LIST:
        direction_row_list = [
            row
            for row in condition_audit_row_list
            if row["direction"] == direction_name
        ]
        training_row_list = [
            row for row in direction_row_list if row["split"] == "train"
        ]
        training_torque_array = np.asarray(
            [row["measured_signed_torque_nm"] for row in training_row_list],
            dtype=np.float64,
        )
        training_temperature_array = np.asarray(
            [
                row["measured_temperature_deg_c"]
                for row in training_row_list
            ],
            dtype=np.float64,
        )
        training_curve_mean_array = np.asarray(
            [row["measured_curve_mean_te_deg"] for row in training_row_list],
            dtype=np.float64,
        )
        correlation_matrix = np.corrcoef(
            np.column_stack(
                [
                    training_torque_array,
                    training_temperature_array,
                    training_curve_mean_array,
                ]
            ),
            rowvar=False,
        )
        support_by_direction[direction_name] = {
            "curve_count_by_split": {
                split_name: sum(
                    row["split"] == split_name
                    for row in direction_row_list
                )
                for split_name in SPLIT_NAME_LIST
            },
            "signed_torque_range_nm": [
                float(np.min(training_torque_array)),
                float(np.max(training_torque_array)),
            ],
            "temperature_range_deg_c": [
                float(np.min(training_temperature_array)),
                float(np.max(training_temperature_array)),
            ],
            "unique_nominal_torque_count": len(
                {
                    row["nominal_torque_nm"]
                    for row in training_row_list
                }
            ),
            "unique_temperature_count": len(
                {
                    round(row["measured_temperature_deg_c"], 1)
                    for row in training_row_list
                }
            ),
            "low_torque_curve_count_by_split": {
                split_name: sum(
                    row["split"] == split_name
                    and row["low_torque_condition"]
                    for row in direction_row_list
                )
                for split_name in SPLIT_NAME_LIST
            },
            "direction_torque_sign_pass_rate": float(
                np.mean(
                    [
                        row["direction_torque_sign_pass"]
                        for row in direction_row_list
                    ]
                )
            ),
            "training_correlation": {
                "torque_temperature": float(correlation_matrix[0, 1]),
                "torque_curve_mean": float(correlation_matrix[0, 2]),
                "temperature_curve_mean": float(correlation_matrix[1, 2]),
            },
            "curve_mean_quantile_deg": {
                quantile_name: float(quantile_value)
                for quantile_name, quantile_value in zip(
                    ("q05", "q50", "q95"),
                    np.quantile(
                        training_curve_mean_array,
                        [0.05, 0.50, 0.95],
                        method="linear",
                    ),
                    strict=True,
                )
            },
        }
    expected_curve_count = (
        int(configuration["analysis"]["expected_eligible_condition_count"]) * 2
    )
    return {
        "eligible_directional_curve_count": len(condition_audit_row_list),
        "expected_directional_curve_count": expected_curve_count,
        "paired_direction_contract_pass": (
            len(condition_audit_row_list) == expected_curve_count
        ),
        "zero_torque_support_pass": all(
            support_by_direction[direction_name][
                "low_torque_curve_count_by_split"
            ]["train"]
            > 0
            for direction_name in DIRECTION_NAME_LIST
        ),
        "direction_torque_sign_contract_pass": all(
            support_by_direction[direction_name][
                "direction_torque_sign_pass_rate"
            ]
            == 1.0
            for direction_name in DIRECTION_NAME_LIST
        ),
        "by_direction": support_by_direction,
    }


def _build_identifiability_payload(
    formulation_result_list: list[dict[str, Any]],
    configuration: dict[str, Any],
) -> dict[str, Any]:

    """Summarize matrix rank and transfer evidence by formulation."""

    maximum_condition_number = float(
        configuration["analysis"]["maximum_design_condition_number"]
    )
    identifiability_payload: dict[str, Any] = {}
    formulation_key_map = {
        "C0": "c0_control",
        "C1": "c1_linear",
        "C2": "c2_temperature",
        "C3": "c3_nonlinear",
        "C5": "c5_shared",
    }
    for formulation_name, payload_key in formulation_key_map.items():
        matching_result_list = [
            result
            for result in formulation_result_list
            if result["formulation"] == formulation_name
        ]
        full_rank = all(
            result["design_rank"] == result["design_column_count"]
            for result in matching_result_list
        )
        condition_number_pass = all(
            result["design_condition_number"] <= maximum_condition_number
            for result in matching_result_list
        )
        identifiability_payload[payload_key] = {
            "surface_count": len(matching_result_list),
            "full_rank": full_rank,
            "condition_number_pass": condition_number_pass,
            "maximum_condition_number": max(
                result["design_condition_number"]
                for result in matching_result_list
            ),
            "all_unconstrained_physical_sign_pass": all(
                result["physical"]["positive_stiffness_pass"]
                for result in matching_result_list
            ),
            "surface_result_list": [
                {
                    "surface": result["surface"],
                    "coefficient_list": result["coefficient_list"],
                    "design_rank": result["design_rank"],
                    "design_column_count": result["design_column_count"],
                    "design_condition_number": result[
                        "design_condition_number"
                    ],
                    "physical": result["physical"],
                    "validation_mae_deg": next(
                        row["mae_deg"]
                        for row in result["metric_row_list"]
                        if row["split"] == "validation"
                    ),
                    "test_mae_deg": next(
                        row["mae_deg"]
                        for row in result["metric_row_list"]
                        if row["split"] == "test"
                    ),
                }
                for result in matching_result_list
            ],
        }
    identifiability_payload["c4_hard_decomposition"] = {
        "mean_surface_law": "same bounded linear compliance basis as C1",
        "periodic_zero_mean_constraint_testable": True,
        "full_rank": identifiability_payload["c1_linear"]["full_rank"],
        "condition_number_pass": identifiability_payload["c1_linear"][
            "condition_number_pass"
        ],
    }
    return identifiability_payload


def _build_entry_gate_payload(
    support_payload: dict[str, Any],
    identifiability_payload: dict[str, Any],
) -> dict[str, Any]:

    """Apply the Phase 3 pre-training entry gate."""

    required_boolean_map = {
        "paired_direction_contract": support_payload[
            "paired_direction_contract_pass"
        ],
        "zero_torque_support": support_payload["zero_torque_support_pass"],
        "direction_torque_sign_contract": support_payload[
            "direction_torque_sign_contract_pass"
        ],
        "c1_full_rank": identifiability_payload["c1_linear"]["full_rank"],
        "c2_full_rank": identifiability_payload["c2_temperature"]["full_rank"],
        "c3_full_rank": identifiability_payload["c3_nonlinear"]["full_rank"],
        "c5_full_rank": identifiability_payload["c5_shared"]["full_rank"],
        "c1_condition_number": identifiability_payload["c1_linear"][
            "condition_number_pass"
        ],
        "c2_condition_number": identifiability_payload["c2_temperature"][
            "condition_number_pass"
        ],
        "c3_condition_number": identifiability_payload["c3_nonlinear"][
            "condition_number_pass"
        ],
        "c5_condition_number": identifiability_payload["c5_shared"][
            "condition_number_pass"
        ],
    }
    status = (
        "pass" if all(required_boolean_map.values()) else "blocked"
    )
    return {
        "status": status,
        "required_check_map": required_boolean_map,
        "training_allowed": status == "pass",
        "authorized_formulation_list": (
            ["C0", "C1", "C2", "C3", "C4", "C5"]
            if status == "pass"
            else []
        ),
        "non_authorized_mechanism_list": [
            "hysteresis",
            "friction_state",
            "load_unload_memory",
            "contact_state",
            "wear",
            "mmt_parameter_estimation",
        ],
    }


def _build_markdown_report(
    summary_payload: dict[str, Any],
    formulation_metric_row_list: list[dict[str, Any]],
) -> str:

    """Render the canonical Phase 3 audit report."""

    support_payload = summary_payload["support"]
    identifiability_payload = summary_payload["identifiability"]
    test_metric_row_list = [
        row
        for row in formulation_metric_row_list
        if row["split"] == "test"
    ]
    test_metric_row_list.sort(
        key=lambda row: (row["surface"], row["mae_deg"])
    )

    report_line_list = [
        "# Phase 3 Compliance Identifiability Audit",
        "",
        "## Executive Decision",
        "",
        f"- Entry gate: `{summary_payload['entry_gate']['status']}`.",
        (
            "- Eligible directional curves: "
            f"`{support_payload['eligible_directional_curve_count']}`."
        ),
        "- Training targets were used only by training-split analytical probes.",
        "- Validation and test curve means were evaluation-only.",
        (
            "- Ordered load-unload, reversal, hysteresis, and friction state "
            "remain unavailable and are excluded from Phase 3."
        ),
        "",
        "## Physical Scope",
        "",
        "Phase 3 tests the bounded algebraic relation:",
        "",
        "```text",
        "elastic_TE = signed_torque / positive_effective_stiffness",
        "```",
        "",
        "Temperature-conditioned, nonlinear, hard-decomposition, and shared-",
        "stiffness variants remain isolated ablations. No Phase 2 nonzero physics",
        "weight is inherited.",
        "",
        "## Directional Support",
        "",
        "| Direction | Train / Val / Test | Signed Torque Range (Nm) | Temperature Range (C) | Train Low-Torque Curves | Torque-Temperature Correlation | Torque-Mean Correlation |",
        "| --- | --- | --- | --- | ---: | ---: | ---: |",
    ]
    for direction_name in DIRECTION_NAME_LIST:
        direction_payload = support_payload["by_direction"][direction_name]
        count_map = direction_payload["curve_count_by_split"]
        torque_range = direction_payload["signed_torque_range_nm"]
        temperature_range = direction_payload["temperature_range_deg_c"]
        correlation_map = direction_payload["training_correlation"]
        report_line_list.append(
            f"| `{direction_name}` | "
            f"{count_map['train']} / {count_map['validation']} / "
            f"{count_map['test']} | "
            f"{torque_range[0]:.3f} to {torque_range[1]:.3f} | "
            f"{temperature_range[0]:.3f} to "
            f"{temperature_range[1]:.3f} | "
            f"{direction_payload['low_torque_curve_count_by_split']['train']} | "
            f"{correlation_map['torque_temperature']:.6f} | "
            f"{correlation_map['torque_curve_mean']:.6f} |"
        )

    report_line_list.extend(
        [
            "",
            "## Training-Only Analytical Probe Results",
            "",
            "| Formulation | Surface | Test Mean MAE (deg) | Test Mean RMSE (deg) | Compliance (deg/Nm) | Stiffness (Nm/deg) | Positive / Monotonic |",
            "| --- | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for metric_row in test_metric_row_list:
        report_line_list.append(
            f"| `{metric_row['formulation']}` | "
            f"`{metric_row['surface']}` | "
            f"{metric_row['mae_deg']:.9f} | "
            f"{metric_row['rmse_deg']:.9f} | "
            f"{metric_row['linear_compliance_deg_per_nm']:.9e} | "
            f"{metric_row['effective_stiffness_nm_per_deg']:.3f} | "
            f"`{metric_row['positive_stiffness_pass']}` / "
            f"`{metric_row['monotonicity_pass']}` |"
        )

    report_line_list.extend(
        [
            "",
            "## Identifiability",
            "",
            "| Formulation | Full Rank | Condition Number Pass | Unconstrained Physical Sign Pass |",
            "| --- | --- | --- | --- |",
        ]
    )
    for payload_key in (
        "c1_linear",
        "c2_temperature",
        "c3_nonlinear",
        "c5_shared",
    ):
        formulation_payload = identifiability_payload[payload_key]
        report_line_list.append(
            f"| `{payload_key}` | "
            f"`{formulation_payload['full_rank']}` | "
            f"`{formulation_payload['condition_number_pass']}` | "
            f"`{formulation_payload['all_unconstrained_physical_sign_pass']}` |"
        )

    report_line_list.extend(
        [
            "",
            "A full-rank design only authorizes a bounded campaign test. It does",
            "not establish a causal stiffness law. Any unconstrained negative",
            "slope is evidence that positive stiffness must be enforced by",
            "construction and judged on held-out transfer rather than fitted",
            "training error.",
            "",
            "## Entry Gate",
            "",
        ]
    )
    for check_name, check_value in summary_payload["entry_gate"][
        "required_check_map"
    ].items():
        report_line_list.append(f"- `{check_name}`: `{check_value}`.")
    report_line_list.extend(
        [
            "",
            "## Decision Boundary",
            "",
            "The audit authorizes only `C0` through `C5`. It does not authorize",
            "hysteresis, friction state, load-unload memory, contact state, wear,",
            "or MMT parameter estimation. Phase 3 training may start only after",
            "the deterministic equation tests and every queue-item preflight pass.",
            "",
        ]
    )
    return "\n".join(report_line_list)


def _condition_number(singular_value_array: np.ndarray) -> float:

    """Return a finite singular-value condition number."""

    assert singular_value_array.size > 0, "Empty singular-value array"
    minimum_singular_value = float(np.min(singular_value_array))
    assert minimum_singular_value > 0.0, "Rank-deficient design matrix"
    return float(np.max(singular_value_array) / minimum_singular_value)


def _read_csv_rows(csv_path: Path) -> list[dict[str, str]]:

    """Read one UTF-8 CSV into dictionaries."""

    assert csv_path.is_file(), f"CSV input does not exist | {csv_path}"
    with csv_path.open("r", encoding="utf-8", newline="") as csv_file:
        return list(csv.DictReader(csv_file))


def _write_csv_rows(
    csv_path: Path,
    field_name_list: list[str],
    row_list: list[dict[str, Any]],
) -> None:

    """Write deterministic CSV rows with the declared field order."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        csv_writer.writeheader()
        csv_writer.writerows(row_list)


def _resolve_project_path(path_value: str | Path) -> Path:

    """Resolve a repository-relative or absolute path."""

    path = Path(path_value)
    return path.resolve() if path.is_absolute() else (PROJECT_ROOT / path).resolve()


def _project_relative_path(path: Path) -> str:

    """Return one POSIX repository-relative path."""

    return path.resolve().relative_to(PROJECT_ROOT).as_posix()


def _sha256_file(file_path: Path) -> str:

    """Return the SHA-256 digest for one file."""

    digest = hashlib.sha256()
    with file_path.open("rb") as input_file:
        for block in iter(lambda: input_file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:

    """Build the Phase 3 compliance entry-gate package."""

    arguments = parse_arguments()
    configuration = load_configuration(arguments.config)
    build_phase3_compliance_audit(configuration, arguments.config)


if __name__ == "__main__":
    main()
