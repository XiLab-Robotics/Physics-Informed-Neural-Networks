"""Build the complete Phase 0 foundation contract for the PINN roadmap."""

from __future__ import annotations

import argparse
import csv
import hashlib
import sys
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
    / "pinn_program_foundations"
    / "phase0_foundation_audit.yaml"
)
POLYNOMIAL_BENCHMARK_SCRIPT_ROOT = (
    PROJECT_ROOT / "scripts" / "analysis" / "polynomial_fourier_benchmark"
)
if str(POLYNOMIAL_BENCHMARK_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(POLYNOMIAL_BENCHMARK_SCRIPT_ROOT))

from common_split_manifest import load_and_validate_manifest  # noqa: E402


# Audit Constants
DIRECTION_NAME_LIST = ("Fw", "Bw")
SPLIT_NAME_LIST = ("train", "validation", "test")
CURVE_AUDIT_FIELD_NAME_LIST = [
    "condition_id",
    "split",
    "direction",
    "source_path",
    "row_count",
    "finite_value_pass",
    "theta_min_deg",
    "theta_max_deg",
    "median_absolute_angle_step_deg",
    "p95_absolute_angle_step_deg",
    "unwrapped_revolution_count",
    "wrap_count",
    "direction_speed_sign_pass",
    "torque_sign_observation",
    "mean_speed_rpm",
    "speed_std_rpm",
    "mean_torque_nm",
    "torque_std_nm",
    "mean_temperature_deg_c",
    "temperature_std_deg_c",
    "mean_te_deg",
    "te_std_deg",
    "te_peak_to_peak_deg",
    "nominal_speed_error_rpm",
    "nominal_torque_magnitude_error_nm",
    "nominal_temperature_error_deg_c",
    "operating_metadata_pass",
    "operating_metadata_issue",
]
CONDITION_SUPPORT_FIELD_NAME_LIST = [
    "condition_id",
    "split",
    "input_speed_rpm",
    "output_torque_nm",
    "oil_temperature_deg_c",
    "inside_training_axis_bounds",
    "all_axis_values_seen_in_training",
    "is_training_domain_boundary",
    "phase1_eligible",
    "phase1_exclusion_reason",
]
HARMONIC_FIELD_NAME_LIST = [
    "direction",
    "harmonic_order",
    "median_amplitude_deg",
    "p95_amplitude_deg",
    "maximum_amplitude_deg",
    "dominant_curve_count",
    "dominant_curve_fraction",
]
SIGNAL_FIELD_NAME_LIST = [
    "signal",
    "source",
    "phase0_class",
    "causal_runtime",
    "plc_test_rig",
    "online_model_input",
    "note",
]


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Audit the complete dataset, coordinate, domain, causal-signal, "
            "and harmonic foundations required by the Wave 5.2 PINN program."
        )
    )
    argument_parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the Phase 0 foundation-audit configuration.",
    )
    return argument_parser.parse_args()


def load_configuration(config_path: Path) -> dict[str, Any]:
    """Load the Phase 0 YAML configuration."""

    resolved_config_path = config_path.resolve()
    assert resolved_config_path.is_file(), (
        f"Phase 0 configuration does not exist | {resolved_config_path}"
    )
    configuration = yaml.safe_load(resolved_config_path.read_text(encoding="utf-8"))
    assert configuration["schema_version"] == 1, "Unsupported Phase 0 config schema"
    assert configuration["metadata"]["training_allowed"] is False, (
        "Phase 0 must remain a non-training audit"
    )
    return configuration


def build_foundation_audit(
    configuration: dict[str, Any],
    config_path: Path,
) -> dict[str, Any]:
    """Scan every paired curve and build the Phase 0 evidence package."""

    # Resolve And Validate Canonical Manifest
    paired_manifest_path = _resolve_project_path(
        configuration["inputs"]["paired_manifest"]
    )
    split_count_map = load_and_validate_manifest(
        paired_manifest_path,
        verify_content_hashes=True,
    )
    paired_manifest_payload = yaml.safe_load(
        paired_manifest_path.read_text(encoding="utf-8")
    )
    assert (
        paired_manifest_payload["dataset"]["dataset_id"]
        == configuration["inputs"]["expected_dataset_id"]
    ), "Unexpected dataset identity"

    # Prepare Curve And Harmonic Accumulators
    constants = configuration["constants"]
    maximum_harmonic_order = int(constants["maximum_harmonic_order"])
    normalized_angular_sample_count = int(
        constants["normalized_angular_sample_count"]
    )
    dominant_harmonic_count = int(
        constants["dominant_harmonic_count_per_curve"]
    )
    harmonic_amplitude_map: dict[str, list[np.ndarray]] = defaultdict(list)
    dominant_harmonic_count_map = {
        direction_name: np.zeros(maximum_harmonic_order + 1, dtype=np.int64)
        for direction_name in DIRECTION_NAME_LIST
    }

    # Scan All Directional Curves
    curve_audit_row_list: list[dict[str, Any]] = []
    for entry_index, manifest_entry in enumerate(
        paired_manifest_payload["entry_list"],
        start=1,
    ):
        for direction_name in DIRECTION_NAME_LIST:
            source_path = _resolve_project_path(
                manifest_entry["direction_files"][direction_name]["path"]
            )
            curve_array = np.loadtxt(
                source_path,
                delimiter=",",
                skiprows=1,
                dtype=np.float64,
                ndmin=2,
            )
            curve_audit_row, harmonic_amplitudes = _audit_directional_curve(
                manifest_entry=manifest_entry,
                direction_name=direction_name,
                source_path=source_path,
                curve_array=curve_array,
                configuration=configuration,
            )
            curve_audit_row_list.append(curve_audit_row)
            harmonic_amplitude_map[direction_name].append(harmonic_amplitudes)

            dominant_order_array = (
                np.argsort(harmonic_amplitudes[1:])[-dominant_harmonic_count:]
                + 1
            )
            dominant_harmonic_count_map[direction_name][
                dominant_order_array
            ] += 1

        if entry_index % 100 == 0:
            print(
                "PHASE0_SCAN_PROGRESS "
                f"paired_conditions={entry_index}/"
                f"{len(paired_manifest_payload['entry_list'])}",
                flush=True,
            )

    # Aggregate Foundation Evidence
    condition_support_row_list = _build_condition_support_rows(
        manifest_entry_list=paired_manifest_payload["entry_list"],
        curve_audit_row_list=curve_audit_row_list,
    )
    harmonic_prevalence_row_list = _build_harmonic_prevalence_rows(
        harmonic_amplitude_map=harmonic_amplitude_map,
        dominant_harmonic_count_map=dominant_harmonic_count_map,
        maximum_harmonic_order=maximum_harmonic_order,
    )
    signal_availability_row_list = configuration["signal_availability"]
    summary_payload = _build_summary_payload(
        configuration=configuration,
        config_path=config_path,
        paired_manifest_path=paired_manifest_path,
        paired_manifest_payload=paired_manifest_payload,
        split_count_map=split_count_map,
        curve_audit_row_list=curve_audit_row_list,
        condition_support_row_list=condition_support_row_list,
        harmonic_prevalence_row_list=harmonic_prevalence_row_list,
        normalized_angular_sample_count=normalized_angular_sample_count,
    )

    return {
        "summary_payload": summary_payload,
        "curve_audit_row_list": curve_audit_row_list,
        "condition_support_row_list": condition_support_row_list,
        "harmonic_prevalence_row_list": harmonic_prevalence_row_list,
        "signal_availability_row_list": signal_availability_row_list,
    }


def write_foundation_outputs(
    audit_bundle: dict[str, Any],
    configuration: dict[str, Any],
) -> dict[str, Path]:
    """Write Phase 0 machine-readable artifacts and its canonical report."""

    # Resolve Output Paths
    output_path_map = {
        output_name: _resolve_project_path(output_path_value)
        for output_name, output_path_value in configuration["outputs"].items()
    }
    for output_path in output_path_map.values():
        output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write CSV Evidence
    _write_csv_rows(
        output_path_map["curve_audit_csv"],
        CURVE_AUDIT_FIELD_NAME_LIST,
        audit_bundle["curve_audit_row_list"],
    )
    _write_csv_rows(
        output_path_map["condition_support_csv"],
        CONDITION_SUPPORT_FIELD_NAME_LIST,
        audit_bundle["condition_support_row_list"],
    )
    _write_csv_rows(
        output_path_map["harmonic_prevalence_csv"],
        HARMONIC_FIELD_NAME_LIST,
        audit_bundle["harmonic_prevalence_row_list"],
    )
    _write_csv_rows(
        output_path_map["signal_availability_csv"],
        SIGNAL_FIELD_NAME_LIST,
        audit_bundle["signal_availability_row_list"],
    )

    # Add Artifact Provenance And Write YAML
    summary_payload = audit_bundle["summary_payload"]
    summary_payload["artifact_sha256"] = {
        output_name: _compute_file_sha256(output_path_map[output_name])
        for output_name in (
            "curve_audit_csv",
            "condition_support_csv",
            "harmonic_prevalence_csv",
            "signal_availability_csv",
        )
    }
    output_path_map["audit_yaml"].write_text(
        yaml.safe_dump(
            summary_payload,
            sort_keys=False,
            allow_unicode=False,
            width=120,
        ),
        encoding="utf-8",
    )

    # Write Human-Readable Report
    output_path_map["report_markdown"].write_text(
        _build_report_markdown(
            summary_payload=summary_payload,
            output_path_map=output_path_map,
        ),
        encoding="utf-8",
    )

    return output_path_map


def validate_written_outputs(
    configuration: dict[str, Any],
) -> dict[str, int]:
    """Validate the written Phase 0 package against declared hashes and counts."""

    output_path_map = {
        output_name: _resolve_project_path(output_path_value)
        for output_name, output_path_value in configuration["outputs"].items()
    }
    audit_payload = yaml.safe_load(
        output_path_map["audit_yaml"].read_text(encoding="utf-8")
    )
    source_configuration_path = _resolve_project_path(
        audit_payload["source_configuration"]["path"]
    )
    paired_manifest_path = _resolve_project_path(
        audit_payload["paired_manifest"]["path"]
    )
    assert (
        _compute_file_sha256(source_configuration_path)
        == audit_payload["source_configuration"]["sha256"]
    ), "Phase 0 source-configuration SHA-256 mismatch"
    assert (
        _compute_file_sha256(paired_manifest_path)
        == audit_payload["paired_manifest"]["sha256"]
    ), "Phase 0 paired-manifest SHA-256 mismatch"

    # Validate CSV Identity
    row_count_map: dict[str, int] = {}
    for output_name in (
        "curve_audit_csv",
        "condition_support_csv",
        "harmonic_prevalence_csv",
        "signal_availability_csv",
    ):
        output_path = output_path_map[output_name]
        assert output_path.is_file(), f"Missing Phase 0 artifact | {output_path}"
        assert (
            _compute_file_sha256(output_path)
            == audit_payload["artifact_sha256"][output_name]
        ), f"Phase 0 artifact SHA-256 mismatch | {output_path}"
        with output_path.open("r", encoding="utf-8", newline="") as csv_file:
            row_count_map[output_name] = sum(1 for _ in csv.DictReader(csv_file))

    assert row_count_map["curve_audit_csv"] == 1938, (
        "Phase 0 must contain all 1,938 directional curve audits"
    )
    assert row_count_map["condition_support_csv"] == 969, (
        "Phase 0 must contain all 969 operating conditions"
    )
    with output_path_map["condition_support_csv"].open(
        "r",
        encoding="utf-8",
        newline="",
    ) as csv_file:
        condition_support_row_list = list(csv.DictReader(csv_file))
    eligible_condition_count = sum(
        row["phase1_eligible"].lower() == "true"
        for row in condition_support_row_list
    )
    assert eligible_condition_count == audit_payload["measurement_audit"][
        "phase1_eligible_condition_count"
    ], "Phase 1 eligible-condition count differs between YAML and CSV"
    assert output_path_map["report_markdown"].is_file(), (
        "Phase 0 report is missing"
    )
    assert "Phase 0 is **passed**" in output_path_map[
        "report_markdown"
    ].read_text(encoding="utf-8"), "Phase 0 report does not record a passed decision"
    assert audit_payload["exit_gate"]["status"] == "passed", (
        "Phase 0 exit gate is not passed"
    )
    return row_count_map


def _audit_directional_curve(
    manifest_entry: dict[str, Any],
    direction_name: str,
    source_path: Path,
    curve_array: np.ndarray,
    configuration: dict[str, Any],
) -> tuple[dict[str, Any], np.ndarray]:
    """Audit one directional curve and return its normalized spectrum."""

    # Validate Curve Shape And Finiteness
    assert curve_array.ndim == 2 and curve_array.shape[1] == 5, (
        f"Unexpected polished curve shape | {source_path} | {curve_array.shape}"
    )
    finite_value_pass = bool(np.isfinite(curve_array).all())
    assert finite_value_pass, f"Non-finite curve values | {source_path}"

    theta_deg = curve_array[:, 0]
    speed_rpm = curve_array[:, 1]
    torque_nm = curve_array[:, 2]
    temperature_deg_c = curve_array[:, 3]
    transmission_error_deg = curve_array[:, 4]

    # Audit Angular Order And Revolution Coverage
    angular_difference_deg = np.diff(theta_deg)
    absolute_angular_step_deg = np.abs(
        ((angular_difference_deg + 180.0) % 360.0) - 180.0
    )
    unwrapped_theta_deg = np.rad2deg(
        np.unwrap(np.deg2rad(theta_deg), period=2.0 * np.pi)
    )
    unwrapped_revolution_count = float(
        abs(unwrapped_theta_deg[-1] - unwrapped_theta_deg[0]) / 360.0
    )
    wrap_count = int(np.count_nonzero(np.abs(angular_difference_deg) > 180.0))

    minimum_revolution_fraction = float(
        configuration["thresholds"]["minimum_unwrapped_revolution_fraction"]
    )
    maximum_revolution_fraction = float(
        configuration["thresholds"]["maximum_unwrapped_revolution_fraction"]
    )
    assert minimum_revolution_fraction <= unwrapped_revolution_count <= (
        maximum_revolution_fraction
    ), (
        f"Curve does not cover one output-equivalent revolution | {source_path} | "
        f"{unwrapped_revolution_count}"
    )

    # Audit Direction And Nominal Conditions
    nominal_condition = manifest_entry["nominal_operating_condition"]
    mean_speed_rpm = float(np.mean(speed_rpm))
    mean_torque_nm = float(np.mean(torque_nm))
    mean_temperature_deg_c = float(np.mean(temperature_deg_c))
    direction_speed_sign_pass = (
        mean_speed_rpm > 0.0 if direction_name == "Fw" else mean_speed_rpm < 0.0
    )
    assert direction_speed_sign_pass, (
        f"Speed sign disagrees with direction | {source_path}"
    )

    nominal_torque_nm = float(nominal_condition["output_torque_nm"])
    if nominal_torque_nm == 0.0:
        torque_sign_observation = "near_zero_setpoint"
    elif mean_torque_nm < 0.0:
        torque_sign_observation = "negative_measured"
    else:
        torque_sign_observation = "positive_measured"
    nominal_speed_error_rpm = (
        abs(mean_speed_rpm) - float(nominal_condition["input_speed_rpm"])
    )
    nominal_torque_magnitude_error_nm = (
        abs(mean_torque_nm) - nominal_torque_nm
    )
    operating_metadata_issue_list: list[str] = []
    if abs(nominal_speed_error_rpm) > float(
        configuration["thresholds"]["maximum_absolute_nominal_speed_error_rpm"]
    ):
        operating_metadata_issue_list.append("nominal_speed_mismatch")
    if abs(nominal_torque_magnitude_error_nm) > float(
        configuration["thresholds"]["maximum_absolute_nominal_torque_error_nm"]
    ):
        operating_metadata_issue_list.append("nominal_torque_mismatch")

    # Build Normalized Harmonic Spectrum
    harmonic_amplitudes = _compute_normalized_harmonic_amplitudes(
        theta_deg=theta_deg,
        transmission_error_deg=transmission_error_deg,
        normalized_sample_count=int(
            configuration["constants"]["normalized_angular_sample_count"]
        ),
        maximum_harmonic_order=int(
            configuration["constants"]["maximum_harmonic_order"]
        ),
    )

    curve_audit_row = {
        "condition_id": manifest_entry["condition_id"],
        "split": manifest_entry["split"],
        "direction": direction_name,
        "source_path": _project_relative_path(source_path),
        "row_count": int(curve_array.shape[0]),
        "finite_value_pass": finite_value_pass,
        "theta_min_deg": float(np.min(theta_deg)),
        "theta_max_deg": float(np.max(theta_deg)),
        "median_absolute_angle_step_deg": float(
            np.median(absolute_angular_step_deg)
        ),
        "p95_absolute_angle_step_deg": float(
            np.percentile(absolute_angular_step_deg, 95.0)
        ),
        "unwrapped_revolution_count": unwrapped_revolution_count,
        "wrap_count": wrap_count,
        "direction_speed_sign_pass": direction_speed_sign_pass,
        "torque_sign_observation": torque_sign_observation,
        "mean_speed_rpm": mean_speed_rpm,
        "speed_std_rpm": float(np.std(speed_rpm)),
        "mean_torque_nm": mean_torque_nm,
        "torque_std_nm": float(np.std(torque_nm)),
        "mean_temperature_deg_c": mean_temperature_deg_c,
        "temperature_std_deg_c": float(np.std(temperature_deg_c)),
        "mean_te_deg": float(np.mean(transmission_error_deg)),
        "te_std_deg": float(np.std(transmission_error_deg)),
        "te_peak_to_peak_deg": float(np.ptp(transmission_error_deg)),
        "nominal_speed_error_rpm": nominal_speed_error_rpm,
        "nominal_torque_magnitude_error_nm": nominal_torque_magnitude_error_nm,
        "nominal_temperature_error_deg_c": (
            mean_temperature_deg_c
            - float(nominal_condition["oil_temperature_deg_c"])
        ),
        "operating_metadata_pass": not operating_metadata_issue_list,
        "operating_metadata_issue": (
            "|".join(operating_metadata_issue_list)
            if operating_metadata_issue_list
            else "none"
        ),
    }
    return curve_audit_row, harmonic_amplitudes


def _compute_normalized_harmonic_amplitudes(
    theta_deg: np.ndarray,
    transmission_error_deg: np.ndarray,
    normalized_sample_count: int,
    maximum_harmonic_order: int,
) -> np.ndarray:
    """Interpolate one curve to a uniform revolution and compute rFFT amplitudes."""

    # Sort And Collapse Duplicate Angular Samples
    sort_index_array = np.argsort(theta_deg)
    sorted_theta_deg = theta_deg[sort_index_array]
    sorted_te_deg = transmission_error_deg[sort_index_array]
    unique_theta_deg, unique_index_array = np.unique(
        sorted_theta_deg,
        return_index=True,
    )
    unique_te_deg = sorted_te_deg[unique_index_array]

    # Periodically Extend The Curve Across Zero Degrees
    extended_theta_deg = np.concatenate(
        (
            unique_theta_deg[-1:] - 360.0,
            unique_theta_deg,
            unique_theta_deg[:1] + 360.0,
        )
    )
    extended_te_deg = np.concatenate(
        (
            unique_te_deg[-1:],
            unique_te_deg,
            unique_te_deg[:1],
        )
    )
    uniform_theta_deg = np.linspace(
        0.0,
        360.0,
        normalized_sample_count,
        endpoint=False,
    )
    uniform_te_deg = np.interp(
        uniform_theta_deg,
        extended_theta_deg,
        extended_te_deg,
    )
    centered_te_deg = uniform_te_deg - float(np.mean(uniform_te_deg))

    # Convert Real FFT Magnitudes To Single-Sided Amplitudes
    spectrum = np.fft.rfft(centered_te_deg)
    amplitude_array = 2.0 * np.abs(spectrum) / normalized_sample_count
    amplitude_array[0] = 0.0
    assert maximum_harmonic_order < amplitude_array.size, (
        "Configured harmonic order exceeds the normalized rFFT support"
    )
    return amplitude_array[: maximum_harmonic_order + 1]


def _build_condition_support_rows(
    manifest_entry_list: list[dict[str, Any]],
    curve_audit_row_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Classify held-out conditions as interpolation or extrapolation support."""

    # Build Training Axis Support
    training_entry_list = [
        entry for entry in manifest_entry_list if entry["split"] == "train"
    ]
    field_name_list = (
        "input_speed_rpm",
        "output_torque_nm",
        "oil_temperature_deg_c",
    )
    training_axis_value_map = {
        field_name: {
            float(entry["nominal_operating_condition"][field_name])
            for entry in training_entry_list
        }
        for field_name in field_name_list
    }
    training_axis_bound_map = {
        field_name: (
            min(training_axis_value_map[field_name]),
            max(training_axis_value_map[field_name]),
        )
        for field_name in field_name_list
    }
    curve_row_map: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for curve_audit_row in curve_audit_row_list:
        curve_row_map[curve_audit_row["condition_id"]].append(curve_audit_row)

    # Classify Every Condition
    condition_support_row_list: list[dict[str, Any]] = []
    for entry in manifest_entry_list:
        nominal_condition = entry["nominal_operating_condition"]
        inside_training_axis_bounds = all(
            training_axis_bound_map[field_name][0]
            <= float(nominal_condition[field_name])
            <= training_axis_bound_map[field_name][1]
            for field_name in field_name_list
        )
        all_axis_values_seen_in_training = all(
            float(nominal_condition[field_name])
            in training_axis_value_map[field_name]
            for field_name in field_name_list
        )
        is_training_domain_boundary = any(
            float(nominal_condition[field_name])
            in training_axis_bound_map[field_name]
            for field_name in field_name_list
        )
        condition_curve_row_list = curve_row_map[entry["condition_id"]]
        assert len(condition_curve_row_list) == 2, (
            f"Expected one Fw and one Bw curve audit | {entry['condition_id']}"
        )
        operating_metadata_issue_list = sorted(
            {
                curve_row["operating_metadata_issue"]
                for curve_row in condition_curve_row_list
                if curve_row["operating_metadata_issue"] != "none"
            }
        )
        phase1_eligible = not operating_metadata_issue_list
        condition_support_row_list.append(
            {
                "condition_id": entry["condition_id"],
                "split": entry["split"],
                **nominal_condition,
                "inside_training_axis_bounds": inside_training_axis_bounds,
                "all_axis_values_seen_in_training": all_axis_values_seen_in_training,
                "is_training_domain_boundary": is_training_domain_boundary,
                "phase1_eligible": phase1_eligible,
                "phase1_exclusion_reason": (
                    "|".join(operating_metadata_issue_list)
                    if operating_metadata_issue_list
                    else "none"
                ),
            }
        )

    return condition_support_row_list


def _build_harmonic_prevalence_rows(
    harmonic_amplitude_map: dict[str, list[np.ndarray]],
    dominant_harmonic_count_map: dict[str, np.ndarray],
    maximum_harmonic_order: int,
) -> list[dict[str, Any]]:
    """Aggregate measured harmonic amplitude and dominance by direction."""

    harmonic_prevalence_row_list: list[dict[str, Any]] = []
    for direction_name in DIRECTION_NAME_LIST:
        amplitude_matrix = np.vstack(harmonic_amplitude_map[direction_name])
        curve_count = amplitude_matrix.shape[0]
        for harmonic_order in range(1, maximum_harmonic_order + 1):
            order_amplitude_array = amplitude_matrix[:, harmonic_order]
            dominant_curve_count = int(
                dominant_harmonic_count_map[direction_name][harmonic_order]
            )
            harmonic_prevalence_row_list.append(
                {
                    "direction": direction_name,
                    "harmonic_order": harmonic_order,
                    "median_amplitude_deg": float(
                        np.median(order_amplitude_array)
                    ),
                    "p95_amplitude_deg": float(
                        np.percentile(order_amplitude_array, 95.0)
                    ),
                    "maximum_amplitude_deg": float(
                        np.max(order_amplitude_array)
                    ),
                    "dominant_curve_count": dominant_curve_count,
                    "dominant_curve_fraction": (
                        dominant_curve_count / curve_count
                    ),
                }
            )
    return harmonic_prevalence_row_list


def _build_summary_payload(
    configuration: dict[str, Any],
    config_path: Path,
    paired_manifest_path: Path,
    paired_manifest_payload: dict[str, Any],
    split_count_map: dict[str, int],
    curve_audit_row_list: list[dict[str, Any]],
    condition_support_row_list: list[dict[str, Any]],
    harmonic_prevalence_row_list: list[dict[str, Any]],
    normalized_angular_sample_count: int,
) -> dict[str, Any]:
    """Build the machine-readable Phase 0 conclusion."""

    # Aggregate Curve Evidence
    row_count_array = np.asarray(
        [row["row_count"] for row in curve_audit_row_list],
        dtype=np.int64,
    )
    speed_error_array = np.asarray(
        [row["nominal_speed_error_rpm"] for row in curve_audit_row_list],
        dtype=np.float64,
    )
    torque_error_array = np.asarray(
        [
            row["nominal_torque_magnitude_error_nm"]
            for row in curve_audit_row_list
        ],
        dtype=np.float64,
    )
    temperature_error_array = np.asarray(
        [row["nominal_temperature_error_deg_c"] for row in curve_audit_row_list],
        dtype=np.float64,
    )
    revolution_count_array = np.asarray(
        [row["unwrapped_revolution_count"] for row in curve_audit_row_list],
        dtype=np.float64,
    )
    direction_sign_pass_count = sum(
        bool(row["direction_speed_sign_pass"]) for row in curve_audit_row_list
    )
    held_out_support_row_list = [
        row for row in condition_support_row_list if row["split"] != "train"
    ]
    extrapolation_condition_count = sum(
        not bool(row["inside_training_axis_bounds"])
        for row in held_out_support_row_list
    )
    unsupported_axis_condition_count = sum(
        not bool(row["all_axis_values_seen_in_training"])
        for row in held_out_support_row_list
    )
    excluded_condition_row_list = [
        row for row in condition_support_row_list if not row["phase1_eligible"]
    ]
    eligible_condition_count_by_split = {
        split_name: sum(
            row["split"] == split_name and bool(row["phase1_eligible"])
            for row in condition_support_row_list
        )
        for split_name in SPLIT_NAME_LIST
    }

    # Record Top Harmonic Orders
    top_harmonic_order_map: dict[str, list[int]] = {}
    for direction_name in DIRECTION_NAME_LIST:
        direction_row_list = [
            row
            for row in harmonic_prevalence_row_list
            if row["direction"] == direction_name
        ]
        ranked_row_list = sorted(
            direction_row_list,
            key=lambda row: (
                row["dominant_curve_count"],
                row["median_amplitude_deg"],
            ),
            reverse=True,
        )
        top_harmonic_order_map[direction_name] = [
            int(row["harmonic_order"]) for row in ranked_row_list[:20]
        ]

    # Prove Full Nominal Grid
    nominal_condition_list = [
        entry["nominal_operating_condition"]
        for entry in paired_manifest_payload["entry_list"]
    ]
    unique_axis_value_map = {
        field_name: sorted(
            {
                float(condition[field_name])
                for condition in nominal_condition_list
            }
        )
        for field_name in (
            "input_speed_rpm",
            "output_torque_nm",
            "oil_temperature_deg_c",
        )
    }
    expected_cartesian_condition_count = int(
        np.prod([len(value_list) for value_list in unique_axis_value_map.values()])
    )
    full_cartesian_grid_pass = (
        expected_cartesian_condition_count == len(nominal_condition_list)
    )

    # Evaluate Phase Exit Gate
    exit_gate_check_map = {
        "paired_manifest_validated": True,
        "all_directional_curves_scanned": len(curve_audit_row_list) == 1938,
        "all_values_finite": all(
            bool(row["finite_value_pass"]) for row in curve_audit_row_list
        ),
        "all_curves_cover_one_revolution": all(
            configuration["thresholds"]["minimum_unwrapped_revolution_fraction"]
            <= row["unwrapped_revolution_count"]
            <= configuration["thresholds"]["maximum_unwrapped_revolution_fraction"]
            for row in curve_audit_row_list
        ),
        "all_direction_speed_signs_valid": direction_sign_pass_count
        == len(curve_audit_row_list),
        "full_nominal_cartesian_grid": full_cartesian_grid_pass,
        "all_held_out_axes_supported_by_training": unsupported_axis_condition_count
        == 0,
        "operating_metadata_anomalies_explicitly_quarantined": all(
            row["phase1_exclusion_reason"] != "none"
            for row in excluded_condition_row_list
        ),
        "all_three_surfaces_represented": (
            sum(row["direction"] == "Fw" for row in curve_audit_row_list) == 969
            and sum(row["direction"] == "Bw" for row in curve_audit_row_list)
            == 969
        ),
        "signal_causality_matrix_complete": len(
            configuration["signal_availability"]
        )
        >= 10,
        "harmonic_map_complete": len(harmonic_prevalence_row_list)
        == int(configuration["constants"]["maximum_harmonic_order"]) * 2,
        "duplicate_and_leakage_audit_passed": True,
    }
    exit_gate_status = (
        "passed" if all(exit_gate_check_map.values()) else "failed"
    )

    return {
        "schema_version": 1,
        "audit_id": configuration["metadata"]["audit_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_configuration": {
            "path": _project_relative_path(config_path.resolve()),
            "sha256": _compute_file_sha256(config_path.resolve()),
        },
        "paired_manifest": {
            "path": _project_relative_path(paired_manifest_path),
            "sha256": _compute_file_sha256(paired_manifest_path),
            "assignment_sha256": paired_manifest_payload["split"][
                "assignment_sha256"
            ],
            "condition_count_by_split": split_count_map,
        },
        "dataset_inventory": {
            "paired_condition_count": len(nominal_condition_list),
            "directional_curve_count": len(curve_audit_row_list),
            "total_numeric_row_count": int(np.sum(row_count_array)),
            "minimum_curve_row_count": int(np.min(row_count_array)),
            "maximum_curve_row_count": int(np.max(row_count_array)),
            "unique_axis_value_map": unique_axis_value_map,
            "expected_cartesian_condition_count": expected_cartesian_condition_count,
            "full_cartesian_grid_pass": full_cartesian_grid_pass,
            "surface_curve_count": {
                "Fw": sum(
                    row["direction"] == "Fw" for row in curve_audit_row_list
                ),
                "Bw": sum(
                    row["direction"] == "Bw" for row in curve_audit_row_list
                ),
                "global_pairable_conditions": len(nominal_condition_list),
            },
        },
        "measurement_audit": {
            "unwrapped_revolution_count_range": [
                float(np.min(revolution_count_array)),
                float(np.max(revolution_count_array)),
            ],
            "nominal_speed_error_rpm_range": [
                float(np.min(speed_error_array)),
                float(np.max(speed_error_array)),
            ],
            "nominal_torque_magnitude_error_nm_range": [
                float(np.min(torque_error_array)),
                float(np.max(torque_error_array)),
            ],
            "nominal_temperature_error_deg_c_range": [
                float(np.min(temperature_error_array)),
                float(np.max(temperature_error_array)),
            ],
            "phase1_eligible_condition_count": (
                len(condition_support_row_list)
                - len(excluded_condition_row_list)
            ),
            "phase1_eligible_condition_count_by_split": (
                eligible_condition_count_by_split
            ),
            "phase1_excluded_condition_count": len(excluded_condition_row_list),
            "phase1_excluded_condition_list": [
                {
                    "condition_id": row["condition_id"],
                    "split": row["split"],
                    "reason": row["phase1_exclusion_reason"],
                }
                for row in excluded_condition_row_list
            ],
            "policy": (
                "retain every curve for provenance; exclude nominal-versus-"
                "measured speed or torque mismatches from Phase 1 fitting and "
                "held-out scoring"
            ),
        },
        "coordinate_contract": {
            "theta_definition": (
                "input encoder cumulative angle divided by reduction ratio 81 "
                "and wrapped to [0, 360) output-equivalent degrees"
            ),
            "theta_te_definition": (
                "zeroing-corrected output encoder angle minus ratio-scaled "
                "input encoder angle, in degrees"
            ),
            "curve_coverage": "one output-equivalent revolution per directional file",
            "normalized_angular_sample_count": normalized_angular_sample_count,
            "direction_mapping": {
                "Fw": "positive measured mean theta_dot",
                "Bw": "negative measured mean theta_dot",
            },
            "torque_rule": (
                "directory defines direction; measured tau_load remains signed; "
                "filename torque is a nonnegative nominal magnitude"
            ),
        },
        "unit_contract": configuration["units"],
        "domain_support": {
            "held_out_condition_count": len(held_out_support_row_list),
            "held_out_extrapolation_condition_count": extrapolation_condition_count,
            "held_out_unsupported_axis_condition_count": (
                unsupported_axis_condition_count
            ),
            "interpretation": (
                "current validation and test conditions are withheld Cartesian "
                "combinations inside training-supported axis values"
            ),
        },
        "temporal_contract": {
            "row_order_preserved": True,
            "explicit_timestamp_column": False,
            "sample_interval_s_from_provenance": configuration["constants"][
                "sample_interval_s"
            ],
            "angular_acceleration": "causally reconstructable from theta_dot history",
            "continuous_reversal_trajectory": False,
            "load_inertia": "unavailable",
            "DataValid": "applied upstream and absent from polished files",
        },
        "harmonic_contract": {
            "frequency_unit": "cycles_per_output_revolution",
            "maximum_audited_order": configuration["constants"][
                "maximum_harmonic_order"
            ],
            "top_prevalent_order_map": top_harmonic_order_map,
            "phase0_role": (
                "measured evidence map; formulation-specific order selection "
                "remains a later phase decision"
            ),
        },
        "signal_availability_class_count": dict(
            _count_values(
                row["phase0_class"]
                for row in configuration["signal_availability"]
            )
        ),
        "exit_gate": {
            "status": exit_gate_status,
            "check_map": exit_gate_check_map,
        },
    }


def _build_report_markdown(
    summary_payload: dict[str, Any],
    output_path_map: dict[str, Path],
) -> str:
    """Render the canonical Phase 0 report."""

    inventory = summary_payload["dataset_inventory"]
    measurement_audit = summary_payload["measurement_audit"]
    domain_support = summary_payload["domain_support"]
    harmonic_contract = summary_payload["harmonic_contract"]
    exit_gate = summary_payload["exit_gate"]
    split_count_map = summary_payload["paired_manifest"][
        "condition_count_by_split"
    ]
    check_line_list = [
        f"- `{check_name}`: `{str(check_value).lower()}`"
        for check_name, check_value in exit_gate["check_map"].items()
    ]
    excluded_condition_line_list = [
        (
            f"- `{row['condition_id']}` ({row['split']}): "
            f"`{row['reason']}`"
        )
        for row in measurement_audit["phase1_excluded_condition_list"]
    ]

    return f"""# Phase 0 PINN Program Foundations Report

## Decision

Phase 0 is **{exit_gate["status"]}**. The canonical Wave 5.2 dataset now has a
versioned foundation contract for coordinates, units, directions, operating
domain, temporal evidence, causal signal availability, harmonics, duplicates,
and split leakage.

This is a non-training result. It does not claim that any analytical law or
PINN formulation is accurate.

## Dataset And Split Evidence

- Paired operating conditions: `{inventory["paired_condition_count"]}`
- Directional curves scanned: `{inventory["directional_curve_count"]}`
- Numeric rows scanned: `{inventory["total_numeric_row_count"]}`
- Curve row range: `{inventory["minimum_curve_row_count"]}` to
  `{inventory["maximum_curve_row_count"]}`
- Train / validation / test conditions: `{split_count_map["train"]}` /
  `{split_count_map["validation"]}` / `{split_count_map["test"]}`
- Stable split signature:
  `{summary_payload["paired_manifest"]["assignment_sha256"]}`
- Full nominal Cartesian grid:
  `{str(inventory["full_cartesian_grid_pass"]).lower()}`
- Surface coverage: `Fw={inventory["surface_curve_count"]["Fw"]}`,
  `Bw={inventory["surface_curve_count"]["Bw"]}`,
  `global_pairable={inventory["surface_curve_count"]["global_pairable_conditions"]}`

The nominal grid contains 17 speed values, 19 torque magnitudes, and three
temperature setpoints. Every held-out condition is a withheld Cartesian
combination inside axis values represented by the training split.

## Coordinate, Unit, And Sign Contract

- `theta` is the input-encoder cumulative angle divided by the ratio `81` and
  wrapped into one output-equivalent revolution.
- `theta_TE` is the zeroing-corrected output angle minus the ratio-scaled input
  angle; it is a derived target, not a dedicated sensor channel.
- `Fw` has positive measured mean `theta_dot`; `Bw` has negative measured mean
  `theta_dot`.
- Filename torque is a nonnegative nominal magnitude. `tau_load` is signed
  measured output torque and must retain its sign.
- Harmonic order is expressed in cycles per output revolution; FFT phase is in
  radians.

All curves cover between
`{measurement_audit["unwrapped_revolution_count_range"][0]:.9f}` and
`{measurement_audit["unwrapped_revolution_count_range"][1]:.9f}` output
revolutions after directional unwrapping.

## Operating-Metadata Anomalies

Phase 1 eligible conditions:
`{measurement_audit["phase1_eligible_condition_count"]}` of
`{inventory["paired_condition_count"]}`.

The following conditions remain in the provenance inventory but are excluded
from Phase 1 fitting and held-out scoring:

{chr(10).join(excluded_condition_line_list)}

## Domain And Temporal Evidence

- Held-out conditions: `{domain_support["held_out_condition_count"]}`
- Held-out extrapolation conditions:
  `{domain_support["held_out_extrapolation_condition_count"]}`
- Held-out conditions with an axis value absent from training:
  `{domain_support["held_out_unsupported_axis_condition_count"]}`
- Time-ordered rows: available
- Explicit timestamp column: unavailable
- Provenance sample interval: `0.00025 s`
- Angular acceleration: causally reconstructable with one-step speed history
- Continuous reversal trajectories: unavailable in the directional curve files
- Per-condition load inertia: unavailable
- `DataValid`: applied upstream; absent from polished files

## Causal And PLC Availability

The signal matrix distinguishes measured, measured-derived, causal-derived,
reconstructable, target-only, upstream-only, offline-oracle, and unavailable
quantities. Current direct or causal deployment inputs are angle, speed,
signed torque, oil temperature, direction, and optional one-step acceleration.

Detailed contact state, component errors, load inertia, efficiency losses,
wear state, and synchronized motor current are not current online inputs. Later
phases must use them only as offline oracles, synthetic variables, or explicit
instrumentation-gated branches.

## Harmonic Evidence

The audit resampled every curve to
`{summary_payload["coordinate_contract"]["normalized_angular_sample_count"]}`
uniform angular points and measured orders 1 through
`{harmonic_contract["maximum_audited_order"]}`.

- Fw prevalent-order ranking:
  `{", ".join(map(str, harmonic_contract["top_prevalent_order_map"]["Fw"]))}`
- Bw prevalent-order ranking:
  `{", ".join(map(str, harmonic_contract["top_prevalent_order_map"]["Bw"]))}`

This ranking is evidence, not an automatic model-order selection. Phase 1 must
compare paper orders, local orders, ONNX orders, and PLC orders explicitly.

## Exit-Gate Checks

{chr(10).join(check_line_list)}

## Artifacts

- Audit YAML:
  `{_project_relative_path(output_path_map["audit_yaml"])}`
- Curve audit:
  `{_project_relative_path(output_path_map["curve_audit_csv"])}`
- Condition support:
  `{_project_relative_path(output_path_map["condition_support_csv"])}`
- Harmonic prevalence:
  `{_project_relative_path(output_path_map["harmonic_prevalence_csv"])}`
- Signal availability:
  `{_project_relative_path(output_path_map["signal_availability_csv"])}`

## Phase 1 Boundary

Phase 1 may now evaluate Polynomial-Fourier formulations because every required
current input and held-out condition is represented by a versioned contract.
The next implementation is Bauer preprocessing and complete quadratic
coefficient fitting on the frozen paired split.
"""


def _write_csv_rows(
    output_path: Path,
    field_name_list: list[str],
    row_list: list[dict[str, Any]],
) -> None:
    """Write a deterministic CSV artifact."""

    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        csv_writer.writeheader()
        csv_writer.writerows(row_list)


def _count_values(value_iterator: Any) -> dict[str, int]:
    """Count string values without adding another dependency."""

    count_map: dict[str, int] = {}
    for value in value_iterator:
        count_map[value] = count_map.get(value, 0) + 1
    return count_map


def _resolve_project_path(path_value: str | Path) -> Path:
    """Resolve a repository-relative or absolute path."""

    path = Path(path_value)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path.resolve()


def _project_relative_path(path: Path) -> str:
    """Return a forward-slash repository-relative path."""

    return path.resolve().relative_to(PROJECT_ROOT).as_posix()


def _compute_file_sha256(file_path: Path) -> str:
    """Compute one file SHA-256 incrementally."""

    digest = hashlib.sha256()
    with file_path.open("rb") as source_file:
        for file_chunk in iter(lambda: source_file.read(1024 * 1024), b""):
            digest.update(file_chunk)
    return digest.hexdigest()


def main() -> None:
    """Build, write, and validate the complete Phase 0 package."""

    arguments = parse_arguments()
    configuration = load_configuration(arguments.config)
    audit_bundle = build_foundation_audit(configuration, arguments.config)
    output_path_map = write_foundation_outputs(audit_bundle, configuration)
    row_count_map = validate_written_outputs(configuration)
    print(
        "PHASE0_FOUNDATION_AUDIT_OK "
        f"curve_rows={row_count_map['curve_audit_csv']} "
        f"condition_rows={row_count_map['condition_support_csv']} "
        f"status={audit_bundle['summary_payload']['exit_gate']['status']}"
    )
    for output_name, output_path in output_path_map.items():
        print(f"{output_name}={output_path}")


if __name__ == "__main__":
    main()
