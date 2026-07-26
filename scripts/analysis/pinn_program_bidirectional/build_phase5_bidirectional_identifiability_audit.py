"""Build the Wave 5.2 Phase 5 bidirectional identifiability audit."""

from __future__ import annotations

import argparse
import csv
import hashlib
import math
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
    / "pinn_program_bidirectional"
    / "phase5_bidirectional_identifiability_audit.yaml"
)

CONDITION_FIELD_NAME_LIST = [
    "condition_id",
    "split",
    "input_speed_rpm",
    "output_torque_nm",
    "oil_temperature_deg_c",
    "source_path",
    "source_row_count",
    "finite_value_pass",
    "forward_mean_te_deg",
    "backward_mean_te_deg",
    "signed_mean_gap_deg",
    "absolute_mean_gap_deg",
    "absolute_mean_gap_arcmin",
    "raw_pair_rmse_deg",
    "centered_pair_rmse_deg",
    "centered_pair_correlation",
    "forward_peak_to_peak_deg",
    "backward_peak_to_peak_deg",
    "peak_to_peak_difference_deg",
    "slope_pair_rmse_deg_per_deg",
    "gap_zero_crossing_count",
    "target_derived_best_shift_deg",
    "target_derived_aligned_centered_rmse_deg",
    "harmonic_1_phase_gap_rad",
    "harmonic_3_phase_gap_rad",
    "harmonic_39_phase_gap_rad",
    "harmonic_40_phase_gap_rad",
    "harmonic_78_phase_gap_rad",
    "harmonic_81_phase_gap_rad",
    "offline_gap_proxy_only",
]

SPLIT_FIELD_NAME_LIST = [
    "split",
    "condition_count",
    "median_absolute_mean_gap_arcmin",
    "p95_absolute_mean_gap_arcmin",
    "median_raw_pair_rmse_deg",
    "median_centered_pair_rmse_deg",
    "median_centered_pair_correlation",
    "median_absolute_target_derived_shift_deg",
    "median_target_derived_aligned_centered_rmse_deg",
    "median_slope_pair_rmse_deg_per_deg",
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
        help="Phase 5 audit YAML configuration.",
    )
    return parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:
    """Resolve a repository-relative path."""

    path = Path(path_value)
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def project_relative_path(path: Path) -> str:
    """Return a forward-slash repository-relative path."""

    return path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix()


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    """Load a YAML file and require a mapping root."""

    with path.open("r", encoding="utf-8") as stream:
        payload = yaml.safe_load(stream)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected a YAML mapping: {path}")
    return payload


def sha256_file(path: Path) -> str:
    """Return the SHA-256 digest of one file."""

    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_simplified_path(
    dataset_root: Path,
    speed_rpm: float,
    torque_nm: float,
    temperature_deg_c: float,
) -> Path:
    """Build the canonical paired simplified-dataset path."""

    temperature_token = f"{int(round(temperature_deg_c))}degree"
    speed_token = f"{int(round(speed_rpm))}rpm"
    file_name = (
        f"{speed_rpm:.1f}rpm"
        f"{torque_nm:.1f}Nm"
        f"{temperature_deg_c:.1f}deg.csv"
    )
    return dataset_root / f"Test_{temperature_token}" / speed_token / file_name


def normalize_periodic_curve(
    angle_deg: np.ndarray,
    te_deg: np.ndarray,
    sample_count: int,
) -> np.ndarray:
    """Interpolate a directional curve onto a common periodic angle grid."""

    wrapped_angle_deg = np.mod(np.asarray(angle_deg, dtype=np.float64), 360.0)
    te_value_deg = np.asarray(te_deg, dtype=np.float64)
    finite_mask = np.isfinite(wrapped_angle_deg) & np.isfinite(te_value_deg)
    wrapped_angle_deg = wrapped_angle_deg[finite_mask]
    te_value_deg = te_value_deg[finite_mask]
    if wrapped_angle_deg.size < 3:
        raise ValueError("A directional curve has fewer than three finite rows")

    sort_index = np.argsort(wrapped_angle_deg, kind="mergesort")
    sorted_angle_deg = wrapped_angle_deg[sort_index]
    sorted_te_deg = te_value_deg[sort_index]
    unique_angle_deg, unique_index = np.unique(
        sorted_angle_deg,
        return_index=True,
    )
    unique_te_deg = sorted_te_deg[unique_index]
    if unique_angle_deg.size < 3:
        raise ValueError("A directional curve has fewer than three unique angles")

    extended_angle_deg = np.concatenate(
        (
            unique_angle_deg[-1:] - 360.0,
            unique_angle_deg,
            unique_angle_deg[:1] + 360.0,
        )
    )
    extended_te_deg = np.concatenate(
        (unique_te_deg[-1:], unique_te_deg, unique_te_deg[:1])
    )
    target_angle_deg = np.linspace(
        0.0,
        360.0,
        sample_count,
        endpoint=False,
        dtype=np.float64,
    )
    return np.interp(target_angle_deg, extended_angle_deg, extended_te_deg)


def wrap_phase_difference(phase_a_rad: float, phase_b_rad: float) -> float:
    """Return the absolute wrapped phase difference in radians."""

    difference = phase_a_rad - phase_b_rad
    return abs(math.atan2(math.sin(difference), math.cos(difference)))


def harmonic_phase_gap(
    forward_centered_deg: np.ndarray,
    backward_centered_deg: np.ndarray,
    harmonic_order: int,
) -> float:
    """Compute the paired phase gap for one harmonic order."""

    forward_spectrum = np.fft.rfft(forward_centered_deg)
    backward_spectrum = np.fft.rfft(backward_centered_deg)
    return wrap_phase_difference(
        float(np.angle(forward_spectrum[harmonic_order])),
        float(np.angle(backward_spectrum[harmonic_order])),
    )


def target_derived_alignment(
    forward_centered_deg: np.ndarray,
    backward_centered_deg: np.ndarray,
) -> tuple[float, float]:
    """Find an offline-only circular alignment from the measured TE targets."""

    sample_count = int(forward_centered_deg.size)
    correlation = np.fft.irfft(
        np.fft.rfft(forward_centered_deg)
        * np.conj(np.fft.rfft(backward_centered_deg)),
        n=sample_count,
    )
    unsigned_lag = int(np.argmax(correlation))
    signed_lag = (
        unsigned_lag
        if unsigned_lag <= sample_count // 2
        else unsigned_lag - sample_count
    )

    candidate_list: list[tuple[int, float]] = []
    for lag in {signed_lag, -signed_lag}:
        aligned_backward_deg = np.roll(backward_centered_deg, lag)
        rmse_deg = float(
            np.sqrt(np.mean((forward_centered_deg - aligned_backward_deg) ** 2))
        )
        candidate_list.append((lag, rmse_deg))
    best_lag, best_rmse_deg = min(candidate_list, key=lambda item: item[1])
    best_shift_deg = best_lag * 360.0 / sample_count
    return float(best_shift_deg), best_rmse_deg


def count_zero_crossings(value_array: np.ndarray) -> int:
    """Count sign transitions after replacing exact zeros deterministically."""

    sign_array = np.sign(np.asarray(value_array, dtype=np.float64))
    nonzero_index_array = np.flatnonzero(sign_array)
    if nonzero_index_array.size == 0:
        return 0
    first_nonzero_index = int(nonzero_index_array[0])
    sign_array[:first_nonzero_index] = sign_array[first_nonzero_index]
    for index in range(first_nonzero_index + 1, sign_array.size):
        if sign_array[index] == 0:
            sign_array[index] = sign_array[index - 1]
    return int(np.count_nonzero(np.diff(sign_array) != 0))


def audit_condition(
    entry: dict[str, Any],
    dataset_root: Path,
    sample_count: int,
    harmonic_order_list: list[int],
    degree_to_arcmin: float,
) -> dict[str, Any]:
    """Audit one paired operating condition."""

    nominal = entry["nominal_operating_condition"]
    speed_rpm = float(nominal["input_speed_rpm"])
    torque_nm = float(nominal["output_torque_nm"])
    temperature_deg_c = float(nominal["oil_temperature_deg_c"])
    source_path = build_simplified_path(
        dataset_root,
        speed_rpm,
        torque_nm,
        temperature_deg_c,
    )
    if not source_path.is_file():
        raise FileNotFoundError(source_path)

    value_matrix = np.loadtxt(
        source_path,
        delimiter=",",
        skiprows=1,
        usecols=(0, 1, 2, 3),
        dtype=np.float64,
    )
    if value_matrix.ndim != 2 or value_matrix.shape[1] != 4:
        raise ValueError(f"Unexpected paired curve shape: {source_path}")

    forward_te_deg = normalize_periodic_curve(
        value_matrix[:, 0],
        value_matrix[:, 1],
        sample_count,
    )
    backward_te_deg = normalize_periodic_curve(
        value_matrix[:, 2],
        value_matrix[:, 3],
        sample_count,
    )
    finite_value_pass = bool(
        np.all(np.isfinite(forward_te_deg))
        and np.all(np.isfinite(backward_te_deg))
    )
    if not finite_value_pass:
        raise ValueError(f"Non-finite normalized values: {source_path}")

    forward_mean_te_deg = float(np.mean(forward_te_deg))
    backward_mean_te_deg = float(np.mean(backward_te_deg))
    forward_centered_deg = forward_te_deg - forward_mean_te_deg
    backward_centered_deg = backward_te_deg - backward_mean_te_deg
    signed_mean_gap_deg = forward_mean_te_deg - backward_mean_te_deg
    absolute_mean_gap_deg = abs(signed_mean_gap_deg)
    gap_curve_deg = forward_te_deg - backward_te_deg

    centered_denominator = float(
        np.linalg.norm(forward_centered_deg)
        * np.linalg.norm(backward_centered_deg)
    )
    centered_pair_correlation = (
        float(
            np.dot(forward_centered_deg, backward_centered_deg)
            / centered_denominator
        )
        if centered_denominator > 0.0
        else 0.0
    )
    angular_step_deg = 360.0 / sample_count
    forward_slope = np.gradient(forward_te_deg, angular_step_deg)
    backward_slope = np.gradient(backward_te_deg, angular_step_deg)
    target_shift_deg, aligned_centered_rmse_deg = target_derived_alignment(
        forward_centered_deg,
        backward_centered_deg,
    )

    harmonic_gap_map = {
        harmonic_order: harmonic_phase_gap(
            forward_centered_deg,
            backward_centered_deg,
            harmonic_order,
        )
        for harmonic_order in harmonic_order_list
    }
    return {
        "condition_id": entry["condition_id"],
        "split": entry["split"],
        "input_speed_rpm": speed_rpm,
        "output_torque_nm": torque_nm,
        "oil_temperature_deg_c": temperature_deg_c,
        "source_path": project_relative_path(source_path),
        "source_row_count": int(value_matrix.shape[0]),
        "finite_value_pass": finite_value_pass,
        "forward_mean_te_deg": forward_mean_te_deg,
        "backward_mean_te_deg": backward_mean_te_deg,
        "signed_mean_gap_deg": signed_mean_gap_deg,
        "absolute_mean_gap_deg": absolute_mean_gap_deg,
        "absolute_mean_gap_arcmin": absolute_mean_gap_deg * degree_to_arcmin,
        "raw_pair_rmse_deg": float(
            np.sqrt(np.mean((forward_te_deg - backward_te_deg) ** 2))
        ),
        "centered_pair_rmse_deg": float(
            np.sqrt(
                np.mean((forward_centered_deg - backward_centered_deg) ** 2)
            )
        ),
        "centered_pair_correlation": centered_pair_correlation,
        "forward_peak_to_peak_deg": float(np.ptp(forward_te_deg)),
        "backward_peak_to_peak_deg": float(np.ptp(backward_te_deg)),
        "peak_to_peak_difference_deg": float(
            np.ptp(forward_te_deg) - np.ptp(backward_te_deg)
        ),
        "slope_pair_rmse_deg_per_deg": float(
            np.sqrt(np.mean((forward_slope - backward_slope) ** 2))
        ),
        "gap_zero_crossing_count": count_zero_crossings(gap_curve_deg),
        "target_derived_best_shift_deg": target_shift_deg,
        "target_derived_aligned_centered_rmse_deg": aligned_centered_rmse_deg,
        "harmonic_1_phase_gap_rad": harmonic_gap_map[1],
        "harmonic_3_phase_gap_rad": harmonic_gap_map[3],
        "harmonic_39_phase_gap_rad": harmonic_gap_map[39],
        "harmonic_40_phase_gap_rad": harmonic_gap_map[40],
        "harmonic_78_phase_gap_rad": harmonic_gap_map[78],
        "harmonic_81_phase_gap_rad": harmonic_gap_map[81],
        "offline_gap_proxy_only": True,
    }


def summarize_split(
    split: str,
    row_list: list[dict[str, Any]],
) -> dict[str, Any]:
    """Summarize paired metrics for one split."""

    def median(field_name: str) -> float:
        return float(np.median([float(row[field_name]) for row in row_list]))

    return {
        "split": split,
        "condition_count": len(row_list),
        "median_absolute_mean_gap_arcmin": median(
            "absolute_mean_gap_arcmin"
        ),
        "p95_absolute_mean_gap_arcmin": float(
            np.percentile(
                [
                    float(row["absolute_mean_gap_arcmin"])
                    for row in row_list
                ],
                95.0,
            )
        ),
        "median_raw_pair_rmse_deg": median("raw_pair_rmse_deg"),
        "median_centered_pair_rmse_deg": median("centered_pair_rmse_deg"),
        "median_centered_pair_correlation": median(
            "centered_pair_correlation"
        ),
        "median_absolute_target_derived_shift_deg": float(
            np.median(
                [
                    abs(float(row["target_derived_best_shift_deg"]))
                    for row in row_list
                ]
            )
        ),
        "median_target_derived_aligned_centered_rmse_deg": median(
            "target_derived_aligned_centered_rmse_deg"
        ),
        "median_slope_pair_rmse_deg_per_deg": median(
            "slope_pair_rmse_deg_per_deg"
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
    """Build the canonical Phase 5 Markdown report."""

    lines = [
        "# Phase 5 Bidirectional TE, Backlash, And Lost-Motion Report",
        "",
        "## Decision",
        "",
        "Phase 5 is complete as a non-training identifiability result. The",
        "paired dataset supports direct measurement of separate `Fw` and `Bw`",
        "TE surfaces and an offline directional-gap proxy. It does not contain",
        "an independent global lost-motion measurement, component-error",
        "metrology, contact clearances, or a repeated transition-state contract.",
        "No full-PINN compatibility, lost-motion, or backlash residual is",
        "therefore promoted.",
        "",
        "`PINN-B1` remains a valid empirical shared-trunk/two-head comparator,",
        "but it does not qualify as a full PINN by itself. Training it in this",
        "phase would not test a new physical law, so no campaign was prepared.",
        "",
        "## Dataset Evidence",
        "",
        f"- Paired operating conditions: `{summary['paired_condition_count']}`.",
        f"- Source rows scanned: `{summary['source_row_count']}`.",
        "- Pairing unit: one operating condition with measured `Fw` and `Bw`",
        "  curves.",
        "- The common train/validation/test assignment remains condition-level",
        "  and direction-paired.",
        "- All directional-gap and target-alignment quantities are explicitly",
        "  marked offline-only.",
        "",
        "## Split Surfaces",
        "",
        "| Split | Conditions | Median abs mean gap (arcmin) | P95 abs mean gap (arcmin) | Median raw RMSE (deg) | Median centered RMSE (deg) | Median centered correlation | Median target-derived shift (deg) |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in split_summary_row_list:
        lines.append(
            f"| {row['split']} | {row['condition_count']} | "
            f"{row['median_absolute_mean_gap_arcmin']:.6f} | "
            f"{row['p95_absolute_mean_gap_arcmin']:.6f} | "
            f"{row['median_raw_pair_rmse_deg']:.8f} | "
            f"{row['median_centered_pair_rmse_deg']:.8f} | "
            f"{row['median_centered_pair_correlation']:.6f} | "
            f"{row['median_absolute_target_derived_shift_deg']:.6f} |"
        )

    lines.extend(
        [
            "",
            "The target-derived alignment is diagnostic evidence only. It cannot",
            "be computed from TE during deployment and therefore cannot enter",
            "model inputs, latent-state initialization, or held-out parameter",
            "fitting.",
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
            "## Interpretation",
            "",
            "The measured difference between paired directional targets is real",
            "dataset evidence, but it is not an independently observed backlash",
            "state. Defining a latent lost-motion output as exactly the predicted",
            "`Fw`/`Bw` difference would be algebraically underdetermined: the",
            "latent variable could absorb any mismatch without identifying a",
            "mechanism. Likewise, enforcing shared centered shape would be an",
            "empirical regularizer unless a source-complete local compatibility",
            "equation is available.",
            "",
            "The source-faithful Wang relation remains blocked by missing",
            "component-error measurements and geometry-specific pin-gear",
            "equivalence parameters. The Xu dead-zone/contact branch remains",
            "synthetic-only because clearance, stiffness, and contact force are",
            "unobserved. The single raw reversal retained by Phase 4 remains an",
            "offline transition oracle, not a reusable state label.",
            "",
            "## Exit Gate",
            "",
            "- `full_pinn_training_authorized: false`",
            "- `physical_residual_promoted: false`",
            "- `empirical_bidirectional_comparator_retained: true`",
            "- `advance_to_phase6: true`",
            "",
            "Phase 6 may now audit acceleration, inertia, and trajectory",
            "constraints. The paired directional metrics remain available for",
            "later Wave 6 multi-head evaluation, without being relabeled as",
            "identified backlash physics.",
            "",
            "## Reproduction",
            "",
            "```powershell",
            "python -B scripts/analysis/pinn_program_bidirectional/build_phase5_bidirectional_identifiability_audit.py",
            "python -B scripts/analysis/pinn_program_bidirectional/validate_phase5_bidirectional_identifiability_audit.py",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """Execute the Phase 5 audit."""

    arguments = parse_arguments()
    configuration_path = resolve_project_path(arguments.config)
    configuration = load_yaml_mapping(configuration_path)

    input_configuration = configuration["inputs"]
    paired_manifest_path = resolve_project_path(
        input_configuration["paired_manifest"]
    )
    phase0_path = resolve_project_path(
        input_configuration["phase0_foundation_audit"]
    )
    phase4_path = resolve_project_path(
        input_configuration["phase4_hysteresis_audit"]
    )
    dataset_root = resolve_project_path(
        input_configuration["simplified_dataset_root"]
    )
    manifest = load_yaml_mapping(paired_manifest_path)
    phase0_summary = load_yaml_mapping(phase0_path)
    phase4_summary = load_yaml_mapping(phase4_path)

    constants = configuration["constants"]
    sample_count = int(constants["normalized_angular_sample_count"])
    harmonic_order_list = [
        int(value) for value in constants["harmonic_order_list"]
    ]
    degree_to_arcmin = float(constants["degree_to_arcmin"])

    condition_row_list: list[dict[str, Any]] = []
    for index, entry in enumerate(manifest["entry_list"], start=1):
        condition_row_list.append(
            audit_condition(
                entry,
                dataset_root,
                sample_count,
                harmonic_order_list,
                degree_to_arcmin,
            )
        )
        if index % 100 == 0:
            print(f"PHASE5_PROGRESS conditions={index}")

    split_row_map: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in condition_row_list:
        split_row_map[str(row["split"])].append(row)
    split_summary_row_list = [
        summarize_split(split, split_row_map[split])
        for split in ("train", "validation", "test")
    ]
    formulation_row_list = [
        dict(row) for row in configuration["candidate_formulations"]
    ]

    output_configuration = configuration["outputs"]
    output_path_map = {
        key: resolve_project_path(value)
        for key, value in output_configuration.items()
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
            "paired_manifest": {
                "path": project_relative_path(paired_manifest_path),
                "sha256": sha256_file(paired_manifest_path),
                "assignment_sha256": manifest["split"]["assignment_sha256"],
            },
            "phase0_foundation_audit": {
                "path": project_relative_path(phase0_path),
                "sha256": sha256_file(phase0_path),
                "exit_status": phase0_summary["exit_gate"]["status"],
            },
            "phase4_hysteresis_audit": {
                "path": project_relative_path(phase4_path),
                "sha256": sha256_file(phase4_path),
                "training_authorized": phase4_summary["exit_gate"][
                    "real_data_training_authorized"
                ],
            },
        },
        "paired_condition_count": len(condition_row_list),
        "source_row_count": sum(
            int(row["source_row_count"]) for row in condition_row_list
        ),
        "finite_value_pass": all(
            bool(row["finite_value_pass"]) for row in condition_row_list
        ),
        "condition_count_by_split": {
            row["split"]: row["condition_count"]
            for row in split_summary_row_list
        },
        "split_summary": split_summary_row_list,
        "observability": {
            "direction_flag_causal": True,
            "paired_directional_te_target_available_offline": True,
            "independent_global_lost_motion_measurement_available": False,
            "component_error_metrology_available": False,
            "contact_clearance_available": False,
            "contact_force_available": False,
            "repeated_transition_state_contract_available": False,
            "target_derived_alignment_online_eligible": False,
        },
        "candidate_formulations": formulation_row_list,
        "exit_gate": {
            "status": "failed_no_training_authorized",
            "full_pinn_training_authorized": full_pinn_training_authorized,
            "physical_residual_promoted": False,
            "empirical_bidirectional_comparator_retained": True,
            "campaign_preparation_required": False,
            "advance_to_phase6": bool(
                configuration["exit_gate"]["advance_to_phase6_after_closeout"]
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
        "PHASE5_BIDIRECTIONAL_IDENTIFIABILITY_AUDIT_OK "
        f"conditions={len(condition_row_list)} "
        f"rows={summary['source_row_count']} "
        "training_authorized=false"
    )


if __name__ == "__main__":
    main()
