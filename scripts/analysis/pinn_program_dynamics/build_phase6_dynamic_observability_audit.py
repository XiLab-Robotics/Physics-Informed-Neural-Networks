"""Build the Wave 5.2 Phase 6 dynamic observability audit."""

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


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONFIGURATION_PATH = (
    PROJECT_ROOT
    / "config"
    / "analysis"
    / "pinn_program_dynamics"
    / "phase6_dynamic_observability_audit.yaml"
)

CONDITION_FIELD_NAME_LIST = [
    "condition_id",
    "split",
    "source_path",
    "row_count",
    "nominal_speed_rpm",
    "direction_window_order",
    "valid_row_count",
    "transition_row_count",
    "transition_duration_s",
    "finite_value_pass",
    "raw_speed_outlier_count",
    "raw_speed_outlier_fraction",
    "forward_valid_median_speed_rpm",
    "backward_valid_median_speed_rpm",
    "forward_valid_speed_mad_rpm",
    "backward_valid_speed_mad_rpm",
    "valid_raw_acceleration_p95_rpm_per_s",
    "transition_raw_acceleration_p95_rpm_per_s",
    "valid_causal_5_acceleration_p95_rpm_per_s",
    "transition_causal_5_acceleration_p95_rpm_per_s",
    "valid_causal_21_acceleration_p95_rpm_per_s",
    "transition_causal_21_acceleration_p95_rpm_per_s",
    "valid_causal_101_acceleration_p95_rpm_per_s",
    "transition_causal_101_acceleration_p95_rpm_per_s",
    "causal_101_valid_to_transition_p95_ratio",
    "valid_speed_stability_pass",
    "robust_transition_excitation_pass",
    "validated_transient_te_target_available",
    "load_inertia_available",
    "commanded_drive_law_available",
]

SPLIT_FIELD_NAME_LIST = [
    "split",
    "condition_count",
    "median_raw_speed_outlier_fraction",
    "median_forward_valid_speed_mad_rpm",
    "median_backward_valid_speed_mad_rpm",
    "median_valid_causal_101_acceleration_p95_rpm_per_s",
    "median_transition_causal_101_acceleration_p95_rpm_per_s",
    "median_causal_101_valid_to_transition_p95_ratio",
    "valid_speed_stability_pass_count",
    "robust_transition_excitation_pass_count",
]

FORMULATION_FIELD_NAME_LIST = [
    "formulation_id",
    "name",
    "feasibility_class",
    "full_pinn_eligible",
    "reason",
]


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIGURATION_PATH,
        help="Phase 6 audit YAML configuration.",
    )
    return parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:
    """Resolve one repository-relative path."""

    path = Path(path_value)
    return path if path.is_absolute() else PROJECT_ROOT / path


def project_relative_path(path: Path) -> str:
    """Return a forward-slash repository-relative path."""

    return path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix()


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    """Load a YAML document with a mapping root."""

    with path.open("r", encoding="utf-8") as stream:
        payload = yaml.safe_load(stream)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected YAML mapping: {path}")
    return payload


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    """Load a CSV artifact into row mappings."""

    with path.open("r", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def sha256_file(path: Path) -> str:
    """Return the SHA-256 digest of one file."""

    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def detect_delimiter(path: Path) -> str:
    """Detect the raw delimiter from the first nonempty line."""

    with path.open("r", encoding="utf-8", errors="replace") as stream:
        for line in stream:
            if line.strip():
                return ";" if line.count(";") > line.count(",") else ","
    raise ValueError(f"Empty raw source file: {path}")


def causal_moving_average(value_array: np.ndarray, window_rows: int) -> np.ndarray:
    """Compute a trailing moving average without future samples."""

    if window_rows <= 1:
        return np.asarray(value_array, dtype=np.float64).copy()
    value_array = np.asarray(value_array, dtype=np.float64)
    cumulative_sum = np.cumsum(value_array, dtype=np.float64)
    result = cumulative_sum.copy()
    result[window_rows:] = (
        cumulative_sum[window_rows:] - cumulative_sum[:-window_rows]
    )
    denominator = np.minimum(
        np.arange(1, value_array.size + 1, dtype=np.float64),
        float(window_rows),
    )
    return result / denominator


def median_absolute_deviation(value_array: np.ndarray) -> float:
    """Return the unscaled median absolute deviation."""

    median_value = float(np.median(value_array))
    return float(np.median(np.abs(value_array - median_value)))


def percentile_absolute(
    value_array: np.ndarray,
    mask: np.ndarray,
    percentile: float,
) -> float:
    """Return an absolute-value percentile over one nonempty region."""

    selected = np.abs(value_array[mask])
    if selected.size == 0:
        raise ValueError("Cannot compute a percentile over an empty region")
    return float(np.percentile(selected, percentile))


def build_transition_mask(
    forward_mask: np.ndarray,
    backward_mask: np.ndarray,
) -> tuple[np.ndarray, str]:
    """Build the exclusive inter-window transition region."""

    forward_index = np.flatnonzero(forward_mask)
    backward_index = np.flatnonzero(backward_mask)
    if forward_index.size == 0 or backward_index.size == 0:
        raise ValueError("Missing forward or backward validity region")

    transition_mask = np.zeros(forward_mask.shape, dtype=bool)
    if int(forward_index[-1]) < int(backward_index[0]):
        transition_mask[
            int(forward_index[-1]) + 1 : int(backward_index[0])
        ] = True
        return transition_mask, "Fw_then_Bw"
    if int(backward_index[-1]) < int(forward_index[0]):
        transition_mask[
            int(backward_index[-1]) + 1 : int(forward_index[0])
        ] = True
        return transition_mask, "Bw_then_Fw"
    raise ValueError("Directional validity regions overlap or interleave")


def audit_condition(
    phase4_row: dict[str, str],
    configuration: dict[str, Any],
) -> dict[str, Any]:
    """Audit causal derivatives and excitation for one raw trajectory."""

    source_path = resolve_project_path(phase4_row["source_path"])
    column_indices = configuration["raw_column_indices"]
    value_matrix = np.loadtxt(
        source_path,
        delimiter=detect_delimiter(source_path),
        usecols=(
            int(column_indices["theta_encoder_deg"]),
            int(column_indices["valid_forward"]),
            int(column_indices["valid_backward"]),
        ),
        ndmin=2,
        dtype=np.float64,
    )
    if value_matrix.ndim != 2 or value_matrix.shape[1] != 3:
        raise ValueError(f"Unexpected raw matrix shape: {source_path}")
    finite_value_pass = bool(np.all(np.isfinite(value_matrix)))
    if not finite_value_pass:
        raise ValueError(f"Non-finite raw values: {source_path}")

    theta_encoder_deg = value_matrix[:, 0]
    forward_mask = value_matrix[:, 1] != 0.0
    backward_mask = value_matrix[:, 2] != 0.0
    valid_mask = forward_mask | backward_mask
    transition_mask, direction_window_order = build_transition_mask(
        forward_mask,
        backward_mask,
    )
    if not np.any(transition_mask):
        raise ValueError(f"Empty inter-window transition: {source_path}")

    sample_interval_s = float(configuration["constants"]["sample_interval_s"])
    angular_step_deg = np.diff(
        theta_encoder_deg,
        prepend=theta_encoder_deg[0],
    )
    raw_speed_rpm = angular_step_deg / 360.0 * 60.0 / sample_interval_s
    raw_acceleration_rpm_per_s = np.diff(
        raw_speed_rpm,
        prepend=raw_speed_rpm[0],
    ) / sample_interval_s

    nominal_speed_rpm = abs(
        float(phase4_row["forward_valid_median_speed_rpm"])
    )
    constants = configuration["constants"]
    speed_outlier_threshold_rpm = (
        float(constants["speed_outlier_multiplier"]) * nominal_speed_rpm
        + float(constants["speed_outlier_margin_rpm"])
    )
    raw_speed_outlier_mask = np.abs(raw_speed_rpm) > speed_outlier_threshold_rpm

    acceleration_map: dict[int, np.ndarray] = {}
    for window_rows_value in constants["causal_smoothing_window_rows"]:
        window_rows = int(window_rows_value)
        smoothed_speed_rpm = causal_moving_average(
            raw_speed_rpm,
            window_rows,
        )
        acceleration_map[window_rows] = np.diff(
            smoothed_speed_rpm,
            prepend=smoothed_speed_rpm[0],
        ) / sample_interval_s

    forward_valid_speed = raw_speed_rpm[forward_mask]
    backward_valid_speed = raw_speed_rpm[backward_mask]
    valid_p95_101 = percentile_absolute(
        acceleration_map[101],
        valid_mask,
        95.0,
    )
    transition_p95_101 = percentile_absolute(
        acceleration_map[101],
        transition_mask,
        95.0,
    )
    excitation_ratio = (
        valid_p95_101 / transition_p95_101
        if transition_p95_101 > 0.0
        else float("inf")
    )
    forward_speed_mad_rpm = median_absolute_deviation(forward_valid_speed)
    backward_speed_mad_rpm = median_absolute_deviation(backward_valid_speed)
    valid_speed_stability_pass = (
        forward_speed_mad_rpm <= max(1.0, nominal_speed_rpm * 0.01)
        and backward_speed_mad_rpm <= max(1.0, nominal_speed_rpm * 0.01)
    )
    robust_transition_excitation_pass = (
        transition_p95_101 > valid_p95_101 * 4.0
    )

    return {
        "condition_id": phase4_row["condition_id"],
        "split": phase4_row["split"],
        "source_path": project_relative_path(source_path),
        "row_count": int(value_matrix.shape[0]),
        "nominal_speed_rpm": nominal_speed_rpm,
        "direction_window_order": direction_window_order,
        "valid_row_count": int(np.count_nonzero(valid_mask)),
        "transition_row_count": int(np.count_nonzero(transition_mask)),
        "transition_duration_s": float(
            np.count_nonzero(transition_mask) * sample_interval_s
        ),
        "finite_value_pass": finite_value_pass,
        "raw_speed_outlier_count": int(
            np.count_nonzero(raw_speed_outlier_mask)
        ),
        "raw_speed_outlier_fraction": float(
            np.mean(raw_speed_outlier_mask)
        ),
        "forward_valid_median_speed_rpm": float(
            np.median(forward_valid_speed)
        ),
        "backward_valid_median_speed_rpm": float(
            np.median(backward_valid_speed)
        ),
        "forward_valid_speed_mad_rpm": forward_speed_mad_rpm,
        "backward_valid_speed_mad_rpm": backward_speed_mad_rpm,
        "valid_raw_acceleration_p95_rpm_per_s": percentile_absolute(
            raw_acceleration_rpm_per_s,
            valid_mask,
            95.0,
        ),
        "transition_raw_acceleration_p95_rpm_per_s": percentile_absolute(
            raw_acceleration_rpm_per_s,
            transition_mask,
            95.0,
        ),
        "valid_causal_5_acceleration_p95_rpm_per_s": percentile_absolute(
            acceleration_map[5],
            valid_mask,
            95.0,
        ),
        "transition_causal_5_acceleration_p95_rpm_per_s": percentile_absolute(
            acceleration_map[5],
            transition_mask,
            95.0,
        ),
        "valid_causal_21_acceleration_p95_rpm_per_s": percentile_absolute(
            acceleration_map[21],
            valid_mask,
            95.0,
        ),
        "transition_causal_21_acceleration_p95_rpm_per_s": percentile_absolute(
            acceleration_map[21],
            transition_mask,
            95.0,
        ),
        "valid_causal_101_acceleration_p95_rpm_per_s": valid_p95_101,
        "transition_causal_101_acceleration_p95_rpm_per_s": transition_p95_101,
        "causal_101_valid_to_transition_p95_ratio": excitation_ratio,
        "valid_speed_stability_pass": valid_speed_stability_pass,
        "robust_transition_excitation_pass": robust_transition_excitation_pass,
        "validated_transient_te_target_available": False,
        "load_inertia_available": False,
        "commanded_drive_law_available": False,
    }


def summarize_split(
    split_name: str,
    row_list: list[dict[str, Any]],
) -> dict[str, Any]:
    """Summarize dynamic evidence for one split."""

    def median(field_name: str) -> float:
        return float(np.median([float(row[field_name]) for row in row_list]))

    return {
        "split": split_name,
        "condition_count": len(row_list),
        "median_raw_speed_outlier_fraction": median(
            "raw_speed_outlier_fraction"
        ),
        "median_forward_valid_speed_mad_rpm": median(
            "forward_valid_speed_mad_rpm"
        ),
        "median_backward_valid_speed_mad_rpm": median(
            "backward_valid_speed_mad_rpm"
        ),
        "median_valid_causal_101_acceleration_p95_rpm_per_s": median(
            "valid_causal_101_acceleration_p95_rpm_per_s"
        ),
        "median_transition_causal_101_acceleration_p95_rpm_per_s": median(
            "transition_causal_101_acceleration_p95_rpm_per_s"
        ),
        "median_causal_101_valid_to_transition_p95_ratio": median(
            "causal_101_valid_to_transition_p95_ratio"
        ),
        "valid_speed_stability_pass_count": sum(
            bool(row["valid_speed_stability_pass"]) for row in row_list
        ),
        "robust_transition_excitation_pass_count": sum(
            bool(row["robust_transition_excitation_pass"])
            for row in row_list
        ),
    }


def write_csv(
    path: Path,
    field_name_list: list[str],
    row_list: list[dict[str, Any]],
) -> None:
    """Write one deterministic CSV artifact."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)


def build_report(
    summary: dict[str, Any],
    split_summary_row_list: list[dict[str, Any]],
    formulation_row_list: list[dict[str, Any]],
) -> str:
    """Build the canonical Phase 6 Markdown report."""

    lines = [
        "# Phase 6 Dynamic Acceleration, Inertia, And Trajectory Report",
        "",
        "## Decision",
        "",
        "Phase 6 is complete as a non-training observability result. Causal",
        "acceleration is mathematically reconstructable from the raw input",
        "encoder, and every condition contains a forward-to-backward",
        "transition. After a 101-row causal filter, however, transition",
        "acceleration is not robustly separated from valid-window derivative",
        "noise at P95. Load inertia, commanded drive law, and a validated",
        "transient TE target are also unavailable. No dynamic full-PINN",
        "residual is therefore promoted.",
        "",
        "`PINN-D4` remains a trainable empirical periodic-plus-temporal",
        "comparator, but the current steady-speed target windows do not turn it",
        "into a dynamic PINN. No campaign was prepared.",
        "",
        "## Dataset Evidence",
        "",
        f"- Canonical raw conditions: `{summary['condition_count']}`.",
        f"- Raw rows scanned: `{summary['raw_row_count']}`.",
        "- Derivative convention: strictly causal backward difference.",
        "- Causal smoothing windows: `5`, `21`, and `101` rows.",
        "- `DataValid` directional windows and the inter-window transition are",
        "  reported separately.",
        "",
        "## Split Surfaces",
        "",
        "| Split | Conditions | Median valid speed MAD Fw/Bw (rpm) | Median valid accel P95, causal 101 (rpm/s) | Median transition accel P95, causal 101 (rpm/s) | Median valid/transition ratio | Stable valid speed | Robust transition excitation |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in split_summary_row_list:
        lines.append(
            f"| {row['split']} | {row['condition_count']} | "
            f"{row['median_forward_valid_speed_mad_rpm']:.6f} / "
            f"{row['median_backward_valid_speed_mad_rpm']:.6f} | "
            f"{row['median_valid_causal_101_acceleration_p95_rpm_per_s']:.3f} | "
            f"{row['median_transition_causal_101_acceleration_p95_rpm_per_s']:.3f} | "
            f"{row['median_causal_101_valid_to_transition_p95_ratio']:.6f} | "
            f"{row['valid_speed_stability_pass_count']} | "
            f"{row['robust_transition_excitation_pass_count']} |"
        )

    lines.extend(
        [
            "",
            "The raw one-step derivative includes encoder discontinuities and",
            "large isolated spikes, so it cannot be used as a physical target",
            "without a stated causal filtering and outlier policy. Rare upper",
            "tail transition samples are dominated by those discontinuities;",
            "the robust P95 comparison does not separate transition excitation",
            "from valid-window derivative noise. The transition is also outside",
            "the validated steady-direction TE curve contract.",
            "",
            "## Candidate Decisions",
            "",
            "| Candidate | Feasibility | Full PINN eligible | Decision basis |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in formulation_row_list:
        lines.append(
            f"| `{row['formulation_id']}` | "
            f"`{row['feasibility_class']}` | "
            f"`{str(bool(row['full_pinn_eligible'])).lower()}` | "
            f"{row['reason']} |"
        )

    lines.extend(
        [
            "",
            "## Exit Gate",
            "",
            "- `full_pinn_training_authorized: false`",
            "- `physical_residual_promoted: false`",
            "- `empirical_temporal_comparator_retained: true`",
            "- `advance_to_phase7: true`",
            "",
            "Phase 7 may now audit contact, mesh stiffness, and load sharing.",
            "Phase 6 dynamic trajectories remain offline evidence until a",
            "validated transient target, drive-law label, and inertia contract",
            "are available.",
            "",
            "## Reproduction",
            "",
            "```powershell",
            "python -B scripts/analysis/pinn_program_dynamics/build_phase6_dynamic_observability_audit.py",
            "python -B scripts/analysis/pinn_program_dynamics/validate_phase6_dynamic_observability_audit.py",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """Execute the Phase 6 dynamic observability audit."""

    arguments = parse_arguments()
    configuration_path = resolve_project_path(arguments.config)
    configuration = load_yaml_mapping(configuration_path)
    input_configuration = configuration["inputs"]

    phase0_path = resolve_project_path(
        input_configuration["phase0_foundation_audit"]
    )
    phase4_csv_path = resolve_project_path(
        input_configuration["phase4_raw_trajectory_audit"]
    )
    phase4_summary_path = resolve_project_path(
        input_configuration["phase4_hysteresis_audit"]
    )
    phase0_summary = load_yaml_mapping(phase0_path)
    phase4_summary = load_yaml_mapping(phase4_summary_path)
    phase4_row_list = load_csv_rows(phase4_csv_path)

    condition_row_list: list[dict[str, Any]] = []
    for index, phase4_row in enumerate(phase4_row_list, start=1):
        condition_row_list.append(
            audit_condition(phase4_row, configuration)
        )
        if index % 100 == 0:
            print(f"PHASE6_PROGRESS conditions={index}")

    split_row_map: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in condition_row_list:
        split_row_map[str(row["split"])].append(row)
    split_summary_row_list = [
        summarize_split(split_name, split_row_map[split_name])
        for split_name in ("train", "validation", "test")
    ]
    formulation_row_list = [
        dict(row) for row in configuration["candidate_formulations"]
    ]

    output_path_map = {
        key: resolve_project_path(value)
        for key, value in configuration["outputs"].items()
    }
    write_csv(
        output_path_map["condition_audit_csv"],
        CONDITION_FIELD_NAME_LIST,
        condition_row_list,
    )
    write_csv(
        output_path_map["split_summary_csv"],
        SPLIT_FIELD_NAME_LIST,
        split_summary_row_list,
    )
    write_csv(
        output_path_map["formulation_feasibility_csv"],
        FORMULATION_FIELD_NAME_LIST,
        formulation_row_list,
    )

    full_pinn_training_authorized = any(
        row["feasibility_class"] == "real_data_trainable"
        and bool(row["full_pinn_eligible"])
        for row in formulation_row_list
    )
    summary = {
        "schema_version": 1,
        "audit_id": configuration["metadata"]["audit_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_configuration": {
            "path": project_relative_path(configuration_path),
            "sha256": sha256_file(configuration_path),
        },
        "input_evidence": {
            "phase0_foundation_audit": {
                "path": project_relative_path(phase0_path),
                "sha256": sha256_file(phase0_path),
                "load_inertia_class": next(
                    row["phase0_class"]
                    for row in load_yaml_mapping(
                        resolve_project_path(
                            "config/analysis/pinn_program_foundations/"
                            "phase0_foundation_audit.yaml"
                        )
                    )["signal_availability"]
                    if row["signal"] == "load_inertia"
                ),
                "exit_status": phase0_summary["exit_gate"]["status"],
            },
            "phase4_raw_trajectory_audit": {
                "path": project_relative_path(phase4_csv_path),
                "sha256": sha256_file(phase4_csv_path),
                "row_count": len(phase4_row_list),
            },
            "phase4_hysteresis_audit": {
                "path": project_relative_path(phase4_summary_path),
                "sha256": sha256_file(phase4_summary_path),
                "single_reversal_count": phase4_summary["chronology_evidence"][
                    "single_reversal_pair_count"
                ],
            },
        },
        "condition_count": len(condition_row_list),
        "raw_row_count": sum(int(row["row_count"]) for row in condition_row_list),
        "condition_count_by_split": {
            row["split"]: row["condition_count"]
            for row in split_summary_row_list
        },
        "split_summary": split_summary_row_list,
        "observability": {
            "causal_acceleration_reconstructable": True,
            "causal_filter_policy_required": True,
            "validated_transient_te_target_available": False,
            "load_inertia_available": False,
            "commanded_drive_law_available": False,
            "repeated_dynamic_trajectory_available": False,
            "steady_directional_te_windows_available": True,
            "single_reversal_transition_available": True,
        },
        "candidate_formulations": formulation_row_list,
        "exit_gate": {
            "status": "failed_no_training_authorized",
            "full_pinn_training_authorized": full_pinn_training_authorized,
            "physical_residual_promoted": False,
            "empirical_temporal_comparator_retained": True,
            "campaign_preparation_required": False,
            "advance_to_phase7": bool(
                configuration["exit_gate"]["advance_to_phase7_after_closeout"]
            ),
        },
    }
    output_path_map["audit_yaml"].parent.mkdir(parents=True, exist_ok=True)
    with output_path_map["audit_yaml"].open("w", encoding="utf-8") as stream:
        yaml.safe_dump(summary, stream, sort_keys=False)

    report_text = build_report(
        summary,
        split_summary_row_list,
        formulation_row_list,
    )
    output_path_map["report_markdown"].parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    output_path_map["report_markdown"].write_text(
        report_text,
        encoding="utf-8",
    )

    print(
        "PHASE6_DYNAMIC_OBSERVABILITY_AUDIT_OK "
        f"conditions={len(condition_row_list)} "
        f"rows={summary['raw_row_count']} "
        "training_authorized=false"
    )


if __name__ == "__main__":
    main()
