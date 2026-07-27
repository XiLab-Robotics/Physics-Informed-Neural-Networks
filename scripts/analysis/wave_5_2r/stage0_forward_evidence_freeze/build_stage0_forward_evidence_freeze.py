"""Build the Wave 5.2R Stage 0 forward-only evidence freeze."""

from __future__ import annotations

import argparse
import csv
import hashlib
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml


# Repository Paths
PROJECT_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "analysis"
    / "wave_5_2r"
    / "stage0_forward_evidence_freeze"
    / "freeze_contract.yaml"
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Build the immutable Wave 5.2R Stage 0 forward evidence contract."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the Stage 0 freeze-contract configuration.",
    )
    return parser.parse_args()


def load_configuration(config_path: Path) -> dict[str, Any]:
    """Load and validate the Stage 0 configuration."""

    resolved_path = config_path.resolve()
    assert resolved_path.is_file(), f"Missing Stage 0 config | {resolved_path}"
    configuration = yaml.safe_load(resolved_path.read_text(encoding="utf-8"))
    assert configuration["schema_version"] == 1, "Unsupported Stage 0 schema"
    assert configuration["metadata"]["training_allowed"] is False
    assert configuration["metadata"]["dataset_id"] == "polished_dataset"
    assert configuration["metadata"]["input_mode"] == "setpoints"
    assert configuration["metadata"]["surface"] == "Fw"
    return configuration


def build_evidence_freeze(
    configuration: dict[str, Any],
    config_path: Path,
) -> dict[str, Any]:
    """Build all Stage 0 frozen artifacts and return the summary."""

    input_paths = {
        key: _resolve_project_path(value)
        for key, value in configuration["inputs"].items()
    }
    for input_name, input_path in input_paths.items():
        assert input_path.is_file(), f"Missing Stage 0 input {input_name} | {input_path}"

    output_root = _resolve_project_path(configuration["outputs"]["root"])
    output_root.mkdir(parents=True, exist_ok=True)

    # Verify Dataset Identity And Materialize Forward Manifest
    split_manifest = _read_yaml(input_paths["split_manifest_yaml"])
    phase0_audit = _read_yaml(input_paths["phase0_audit"])
    expected_signature = configuration["contract"][
        "expected_split_assignment_sha256"
    ]
    assert split_manifest["split"]["assignment_sha256"] == expected_signature
    assert phase0_audit["paired_manifest"]["assignment_sha256"] == expected_signature
    assert split_manifest["dataset"]["dataset_id"] == "polished_dataset"

    excluded_condition_id_set = {
        row["condition_id"]
        for row in phase0_audit["measurement_audit"][
            "phase1_excluded_condition_list"
        ]
    }
    forward_manifest_rows = _build_forward_manifest_rows(
        split_manifest["entry_list"],
        excluded_condition_id_set,
    )
    _write_csv(
        output_root
        / configuration["outputs"]["forward_condition_manifest_csv"],
        forward_manifest_rows,
    )

    # Build Comparable Baseline And Per-Cell Tables
    pf_aggregate_rows = _read_csv(
        input_paths["reproduced_pf_aggregate_metrics"]
    )
    pf_per_curve_rows = _read_csv(
        input_paths["reproduced_pf_per_curve_metrics"]
    )
    neural_candidate_rows = _read_csv(
        input_paths["neural_candidate_diagnostics"]
    )
    neural_curve_rows = _read_csv(input_paths["neural_curve_diagnostics"])
    neural_harmonic_rows = _read_csv(
        input_paths["neural_harmonic_diagnostics"]
    )

    baseline_rows = _build_baseline_rows(
        pf_aggregate_rows,
        neural_candidate_rows,
        neural_curve_rows,
    )
    _write_csv(
        output_root / configuration["outputs"]["baseline_metrics_csv"],
        baseline_rows,
    )

    operating_cell_rows = _build_operating_cell_rows(
        pf_per_curve_rows,
        neural_curve_rows,
    )
    _write_csv(
        output_root / configuration["outputs"]["operating_cell_metrics_csv"],
        operating_cell_rows,
    )

    harmonic_band_rows = _build_harmonic_band_rows(neural_harmonic_rows)
    _write_csv(
        output_root / configuration["outputs"]["harmonic_band_metrics_csv"],
        harmonic_band_rows,
    )

    # Verify Reproduction Against Frozen Historical Evidence
    reproduction_rows = _build_reproduction_rows(
        canonical_pf_rows=_read_csv(
            input_paths["canonical_pf_aggregate_metrics"]
        ),
        reproduced_pf_rows=pf_aggregate_rows,
        historical_neural_rows=_read_csv(
            input_paths["historical_neural_candidate_diagnostics"]
        ),
        reproduced_neural_rows=neural_candidate_rows,
        tolerance_map=configuration["contract"]["reproduction_tolerance"],
    )
    _write_csv(
        output_root / configuration["outputs"]["reproduction_comparison_csv"],
        reproduction_rows,
    )

    # Freeze Source And Model Provenance
    provenance_path_list = list(input_paths.values())
    neural_replay_summary = _read_yaml(input_paths["neural_replay_summary"])
    pf_replay_summary = _read_yaml(input_paths["reproduced_pf_summary"])
    pf_coefficient_payload = _read_yaml(
        input_paths["reproduced_pf_coefficients"]
    )
    for candidate in neural_replay_summary["candidate_list"]:
        provenance_path_list.append(_resolve_project_path(candidate["source_path"]))
        provenance_path_list.append(
            _resolve_project_path(candidate["model_file_path"])
        )
    provenance_rows = _build_provenance_rows(provenance_path_list)
    _write_csv(
        output_root / configuration["outputs"]["provenance_csv"],
        provenance_rows,
    )

    # Write Machine-Readable Exit-Gate Decision
    expected_count_map = configuration["contract"][
        "expected_eligible_condition_count_by_split"
    ]
    actual_count_map = _count_manifest_rows_by_split(forward_manifest_rows)
    candidate_id_list = [row["candidate_id"] for row in baseline_rows]
    expected_candidate_id_list = configuration["contract"][
        "expected_candidate_id_list"
    ]
    exit_gate = {
        "split_identity_pass": (
            split_manifest["split"]["assignment_sha256"] == expected_signature
            and phase0_audit["paired_manifest"]["assignment_sha256"]
            == expected_signature
        ),
        "eligible_condition_count_pass": actual_count_map == expected_count_map,
        "test_curve_count_pass": (
            actual_count_map["test"]
            == configuration["contract"]["expected_test_curve_count"]
        ),
        "candidate_roster_pass": candidate_id_list == expected_candidate_id_list,
        "forward_only_pass": all(
            row["direction"] == "Fw" for row in operating_cell_rows
        ),
        "finite_metric_pass": _all_numeric_metrics_finite(
            baseline_rows,
            {
                "curve_mae_deg",
                "curve_rmse_deg",
                "centered_curve_mae_deg",
                "absolute_curve_mean_error_deg",
            },
        ),
        "reproduction_tolerance_pass": all(
            row["within_tolerance"] == "true" for row in reproduction_rows
        ),
        "no_test_fit_pass": (
            pf_replay_summary["training_executed"] is False
            and pf_coefficient_payload["fit_scope"]
            == "eligible training conditions only"
            and all(
                candidate["candidate_kind"] == "wave1_exported_model"
                for candidate in neural_replay_summary["candidate_list"]
            )
        ),
    }
    summary = {
        "schema_version": 1,
        "stage_id": configuration["metadata"]["stage_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": {
            "dataset_id": "polished_dataset",
            "input_mode": "setpoints",
            "surface": "Fw",
            "angular_unit": "degree",
            "test_condition_count": actual_count_map["test"],
        },
        "split_contract": {
            "assignment_sha256": expected_signature,
            "eligible_condition_count_by_split": actual_count_map,
            "excluded_condition_id_list": sorted(excluded_condition_id_set),
        },
        "candidate_id_list": candidate_id_list,
        "artifact_map": {
            key: str(
                Path(configuration["outputs"]["root"])
                / configuration["outputs"][key]
            ).replace("\\", "/")
            for key in (
                "forward_condition_manifest_csv",
                "baseline_metrics_csv",
                "operating_cell_metrics_csv",
                "harmonic_band_metrics_csv",
                "provenance_csv",
                "reproduction_comparison_csv",
            )
        },
        "exit_gate": {
            "status": (
                "passed" if all(exit_gate.values()) else "failed"
            ),
            "check_map": exit_gate,
        },
        "decision": (
            "Stage 0 evidence freeze accepted. Stage 1 may begin."
            if all(exit_gate.values())
            else "Stage 0 evidence freeze rejected. Repair provenance."
        ),
    }
    summary_path = (
        output_root / configuration["outputs"]["summary_yaml"]
    )
    summary_path.write_text(
        yaml.safe_dump(summary, sort_keys=False, allow_unicode=False),
        encoding="utf-8",
    )
    return summary


def validate_written_outputs(
    configuration: dict[str, Any],
) -> dict[str, int]:
    """Validate the Stage 0 outputs after serialization."""

    output_root = _resolve_project_path(configuration["outputs"]["root"])
    summary_path = output_root / configuration["outputs"]["summary_yaml"]
    assert summary_path.is_file(), f"Missing Stage 0 summary | {summary_path}"
    summary = _read_yaml(summary_path)
    assert summary["exit_gate"]["status"] == "passed"
    assert all(summary["exit_gate"]["check_map"].values())

    expected_count_map = configuration["contract"][
        "expected_eligible_condition_count_by_split"
    ]
    manifest_rows = _read_csv(
        output_root
        / configuration["outputs"]["forward_condition_manifest_csv"]
    )
    assert _count_manifest_rows_by_split(manifest_rows) == expected_count_map
    assert len(manifest_rows) == sum(expected_count_map.values())
    assert len({row["condition_id"] for row in manifest_rows}) == len(
        manifest_rows
    )
    assert all(row["direction"] == "Fw" for row in manifest_rows)

    baseline_rows = _read_csv(
        output_root / configuration["outputs"]["baseline_metrics_csv"]
    )
    assert [row["candidate_id"] for row in baseline_rows] == configuration[
        "contract"
    ]["expected_candidate_id_list"]
    assert all(int(row["curve_count"]) == 97 for row in baseline_rows)

    operating_rows = _read_csv(
        output_root / configuration["outputs"]["operating_cell_metrics_csv"]
    )
    candidate_count_map = defaultdict(int)
    for row in operating_rows:
        assert row["direction"] == "Fw"
        candidate_count_map[row["candidate_id"]] += 1
    assert dict(candidate_count_map) == {
        candidate_id: 97
        for candidate_id in configuration["contract"][
            "expected_candidate_id_list"
        ]
    }

    reproduction_rows = _read_csv(
        output_root
        / configuration["outputs"]["reproduction_comparison_csv"]
    )
    assert reproduction_rows
    assert all(row["within_tolerance"] == "true" for row in reproduction_rows)

    provenance_rows = _read_csv(
        output_root / configuration["outputs"]["provenance_csv"]
    )
    assert provenance_rows
    assert all(len(row["sha256"]) == 64 for row in provenance_rows)

    return {
        "manifest_rows": len(manifest_rows),
        "baseline_rows": len(baseline_rows),
        "operating_cell_rows": len(operating_rows),
        "reproduction_rows": len(reproduction_rows),
        "provenance_rows": len(provenance_rows),
    }


def _build_forward_manifest_rows(
    entry_list: list[dict[str, Any]],
    excluded_condition_id_set: set[str],
) -> list[dict[str, Any]]:
    """Build the eligible forward condition manifest."""

    row_list: list[dict[str, Any]] = []
    for entry in entry_list:
        if entry["condition_id"] in excluded_condition_id_set:
            continue
        operating_condition = entry["nominal_operating_condition"]
        forward_file = entry["direction_files"]["Fw"]
        row_list.append(
            {
                "condition_id": entry["condition_id"],
                "split": entry["split"],
                "direction": "Fw",
                "input_speed_rpm": operating_condition["input_speed_rpm"],
                "output_torque_nm": operating_condition["output_torque_nm"],
                "oil_temperature_deg_c": operating_condition[
                    "oil_temperature_deg_c"
                ],
                "source_path": forward_file["path"],
                "source_size_bytes": forward_file["size_bytes"],
                "source_sha256": forward_file["sha256"],
            }
        )
    return row_list


def _build_baseline_rows(
    pf_aggregate_rows: list[dict[str, str]],
    neural_candidate_rows: list[dict[str, str]],
    neural_curve_rows: list[dict[str, str]],
) -> list[dict[str, Any]]:
    """Build one comparable forward baseline row per candidate."""

    pf_row = _find_unique_row(
        pf_aggregate_rows,
        model_id="PF_A_LOCAL_QUADRATIC",
        split="test",
        direction="Fw",
    )
    row_list: list[dict[str, Any]] = [
        {
            "candidate_id": "PF_A_LOCAL_QUADRATIC",
            "candidate_family": "polynomial_fourier",
            "candidate_kind": "analytical_anchor",
            "curve_count": pf_row["curve_count"],
            "curve_mae_deg": pf_row["mae_deg_mean"],
            "curve_mae_p95_deg": pf_row["mae_deg_p95"],
            "curve_rmse_deg": pf_row["rmse_deg_mean"],
            "centered_curve_mae_deg": pf_row["centered_mae_deg_mean"],
            "absolute_curve_mean_error_deg": pf_row[
                "offset_abs_error_deg_mean"
            ],
            "peak_to_peak_abs_error_deg": pf_row[
                "peak_to_peak_abs_error_deg_mean"
            ],
            "peak_to_peak_error_pct": "",
            "derivative_error": pf_row[
                "derivative_mae_deg_per_sample_mean"
            ],
            "derivative_error_unit": "degree_per_sample_mae",
            "closure_mismatch_deg": pf_row[
                "periodic_closure_error_deg_mean"
            ],
            "harmonic_amplitude_error": pf_row[
                "retained_amplitude_mae_deg_mean"
            ],
            "harmonic_amplitude_error_unit": "degree_mae",
            "harmonic_phase_error": pf_row["retained_phase_mae_rad_mean"],
            "harmonic_phase_error_unit": "radian_mae",
            "metric_contract": "phase1_full_resolution_degree",
        }
    ]
    neural_kind_map = {
        "accepted_periodic_mlp_harmonic_Fw": "accepted_harmonic_mlp",
        "accepted_periodic_gru_sequence_Fw": "accepted_sequence_gru",
    }
    for candidate_id in neural_kind_map:
        row = _find_unique_row(
            neural_candidate_rows,
            candidate_id=candidate_id,
        )
        candidate_curve_rows = [
            curve_row
            for curve_row in neural_curve_rows
            if curve_row["candidate_id"] == candidate_id
        ]
        assert len(candidate_curve_rows) == 97
        row_list.append(
            {
                "candidate_id": candidate_id,
                "candidate_family": row["candidate_family"],
                "candidate_kind": neural_kind_map[candidate_id],
                "curve_count": row["curve_count"],
                "curve_mae_deg": row["mean_curve_mae_deg"],
                "curve_mae_p95_deg": _percentile(
                    [
                        float(curve_row["curve_mae_deg"])
                        for curve_row in candidate_curve_rows
                    ],
                    95.0,
                ),
                "curve_rmse_deg": _mean(
                    [
                        float(curve_row["curve_rmse_deg"])
                        for curve_row in candidate_curve_rows
                    ]
                ),
                "centered_curve_mae_deg": row[
                    "mean_centered_curve_mae_deg"
                ],
                "absolute_curve_mean_error_deg": row[
                    "mean_absolute_curve_mean_error_deg"
                ],
                "peak_to_peak_abs_error_deg": "",
                "peak_to_peak_error_pct": row[
                    "mean_peak_to_peak_error_pct"
                ],
                "derivative_error": row[
                    "mean_derivative_rmse_deg_per_deg"
                ],
                "derivative_error_unit": "degree_per_degree_rmse",
                "closure_mismatch_deg": row[
                    "mean_closure_mismatch_deg"
                ],
                "harmonic_amplitude_error": row[
                    "mean_harmonic_amplitude_error_pct"
                ],
                "harmonic_amplitude_error_unit": "percent",
                "harmonic_phase_error": row[
                    "mean_harmonic_phase_error_deg"
                ],
                "harmonic_phase_error_unit": "degree",
                "metric_contract": "cvp1.2_full_resolution_degree",
            }
        )
    return row_list


def _build_operating_cell_rows(
    pf_per_curve_rows: list[dict[str, str]],
    neural_curve_rows: list[dict[str, str]],
) -> list[dict[str, Any]]:
    """Normalize per-operating-cell metrics across all three baselines."""

    row_list: list[dict[str, Any]] = []
    for row in pf_per_curve_rows:
        if not (
            row["model_id"] == "PF_A_LOCAL_QUADRATIC"
            and row["split"] == "test"
            and row["direction"] == "Fw"
        ):
            continue
        row_list.append(
            {
                "candidate_id": row["model_id"],
                "direction": "Fw",
                "input_speed_rpm": row["nominal_speed_rpm"],
                "output_torque_nm": row["nominal_torque_nm"],
                "oil_temperature_deg_c": row[
                    "nominal_temperature_deg_c"
                ],
                "curve_mae_deg": row["mae_deg"],
                "curve_rmse_deg": row["rmse_deg"],
                "centered_curve_mae_deg": row["centered_mae_deg"],
                "absolute_curve_mean_error_deg": row[
                    "offset_abs_error_deg"
                ],
                "metric_contract": "phase1_full_resolution_degree",
            }
        )
    for row in neural_curve_rows:
        row_list.append(
            {
                "candidate_id": row["candidate_id"],
                "direction": "Fw",
                "input_speed_rpm": row["speed_rpm"],
                "output_torque_nm": row["torque_nm"],
                "oil_temperature_deg_c": row["oil_temperature_deg"],
                "curve_mae_deg": row["curve_mae_deg"],
                "curve_rmse_deg": row["curve_rmse_deg"],
                "centered_curve_mae_deg": row[
                    "centered_curve_mae_deg"
                ],
                "absolute_curve_mean_error_deg": row[
                    "absolute_curve_mean_error_deg"
                ],
                "metric_contract": "cvp1.2_full_resolution_degree",
            }
        )
    return row_list


def _build_harmonic_band_rows(
    harmonic_rows: list[dict[str, str]],
) -> list[dict[str, Any]]:
    """Aggregate harmonic errors per neural candidate and harmonic order."""

    value_map: dict[tuple[str, int], dict[str, list[float]]] = defaultdict(
        lambda: {"amplitude": [], "phase": []}
    )
    for row in harmonic_rows:
        key = (row["candidate_id"], int(row["harmonic_order"]))
        if row["amplitude_error_pct"]:
            value_map[key]["amplitude"].append(
                float(row["amplitude_error_pct"])
            )
        if row["phase_error_deg"]:
            value_map[key]["phase"].append(float(row["phase_error_deg"]))

    row_list: list[dict[str, Any]] = []
    for (candidate_id, harmonic_order), value_map_entry in sorted(
        value_map.items()
    ):
        row_list.append(
            {
                "candidate_id": candidate_id,
                "harmonic_order": harmonic_order,
                "curve_count_with_amplitude": len(
                    value_map_entry["amplitude"]
                ),
                "mean_amplitude_error_pct": _mean(
                    value_map_entry["amplitude"]
                ),
                "curve_count_with_phase": len(value_map_entry["phase"]),
                "mean_phase_error_deg": _mean(value_map_entry["phase"]),
            }
        )
    return row_list


def _build_reproduction_rows(
    *,
    canonical_pf_rows: list[dict[str, str]],
    reproduced_pf_rows: list[dict[str, str]],
    historical_neural_rows: list[dict[str, str]],
    reproduced_neural_rows: list[dict[str, str]],
    tolerance_map: dict[str, float],
) -> list[dict[str, Any]]:
    """Compare fresh metrics with their frozen canonical counterparts."""

    row_list: list[dict[str, Any]] = []
    canonical_pf = _find_unique_row(
        canonical_pf_rows,
        model_id="PF_A_LOCAL_QUADRATIC",
        split="test",
        direction="Fw",
    )
    reproduced_pf = _find_unique_row(
        reproduced_pf_rows,
        model_id="PF_A_LOCAL_QUADRATIC",
        split="test",
        direction="Fw",
    )
    for metric_name in (
        "mae_deg_mean",
        "rmse_deg_mean",
        "centered_mae_deg_mean",
        "offset_abs_error_deg_mean",
    ):
        row_list.append(
            _comparison_row(
                candidate_id="PF_A_LOCAL_QUADRATIC",
                metric_name=metric_name,
                canonical_value=float(canonical_pf[metric_name]),
                reproduced_value=float(reproduced_pf[metric_name]),
                tolerance=float(tolerance_map["pf_absolute_deg"]),
            )
        )

    neural_metric_tolerance_map = {
        "mean_curve_mae_deg": float(
            tolerance_map["neural_absolute_deg"]
        ),
        "mean_percentage_error_pct": float(
            tolerance_map["neural_percentage_point"]
        ),
        "mean_harmonic_amplitude_error_pct": float(
            tolerance_map["neural_percentage_point"]
        ),
        "mean_harmonic_phase_error_deg": float(
            tolerance_map["neural_percentage_point"]
        ),
    }
    for candidate_id in (
        "accepted_periodic_mlp_harmonic_Fw",
        "accepted_periodic_gru_sequence_Fw",
    ):
        canonical_row = _find_unique_row(
            historical_neural_rows,
            candidate_id=candidate_id,
        )
        reproduced_row = _find_unique_row(
            reproduced_neural_rows,
            candidate_id=candidate_id,
        )
        for metric_name, tolerance in neural_metric_tolerance_map.items():
            row_list.append(
                _comparison_row(
                    candidate_id=candidate_id,
                    metric_name=metric_name,
                    canonical_value=float(canonical_row[metric_name]),
                    reproduced_value=float(reproduced_row[metric_name]),
                    tolerance=tolerance,
                )
            )
    return row_list


def _comparison_row(
    *,
    candidate_id: str,
    metric_name: str,
    canonical_value: float,
    reproduced_value: float,
    tolerance: float,
) -> dict[str, Any]:
    """Build one explicit reproduction comparison row."""

    absolute_difference = abs(canonical_value - reproduced_value)
    return {
        "candidate_id": candidate_id,
        "metric_name": metric_name,
        "canonical_value": canonical_value,
        "reproduced_value": reproduced_value,
        "absolute_difference": absolute_difference,
        "absolute_tolerance": tolerance,
        "within_tolerance": str(absolute_difference <= tolerance).lower(),
    }


def _build_provenance_rows(path_list: Iterable[Path]) -> list[dict[str, Any]]:
    """Hash every unique source artifact used by the freeze."""

    unique_paths = sorted({path.resolve() for path in path_list})
    return [
        {
            "path": str(path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            "size_bytes": path.stat().st_size,
            "sha256": _sha256(path),
        }
        for path in unique_paths
    ]


def _all_numeric_metrics_finite(
    row_list: list[dict[str, Any]],
    field_name_set: set[str],
) -> bool:
    """Return whether every populated selected metric is finite."""

    for row in row_list:
        for field_name in field_name_set:
            value = row[field_name]
            if value != "" and not math.isfinite(float(value)):
                return False
    return True


def _count_manifest_rows_by_split(
    row_list: list[dict[str, Any]],
) -> dict[str, int]:
    """Count forward manifest rows by split."""

    count_map = {"train": 0, "validation": 0, "test": 0}
    for row in row_list:
        count_map[row["split"]] += 1
    return count_map


def _find_unique_row(
    row_list: list[dict[str, str]],
    **filter_map: str,
) -> dict[str, str]:
    """Find exactly one CSV row matching all requested fields."""

    matching_rows = [
        row
        for row in row_list
        if all(row.get(key) == value for key, value in filter_map.items())
    ]
    assert len(matching_rows) == 1, (
        f"Expected one row for {filter_map}, found {len(matching_rows)}"
    )
    return matching_rows[0]


def _mean(value_list: list[float]) -> float | str:
    """Return the arithmetic mean or an empty marker."""

    if not value_list:
        return ""
    return sum(value_list) / len(value_list)


def _percentile(value_list: list[float], percentile: float) -> float:
    """Return a linearly interpolated percentile for a non-empty list."""

    assert value_list
    assert 0.0 <= percentile <= 100.0
    sorted_values = sorted(value_list)
    position = (len(sorted_values) - 1) * percentile / 100.0
    lower_index = math.floor(position)
    upper_index = math.ceil(position)
    if lower_index == upper_index:
        return sorted_values[lower_index]
    upper_weight = position - lower_index
    return (
        sorted_values[lower_index] * (1.0 - upper_weight)
        + sorted_values[upper_index] * upper_weight
    )


def _read_csv(path: Path) -> list[dict[str, str]]:
    """Read a CSV file into dictionaries."""

    with path.open("r", encoding="utf-8", newline="") as csv_file:
        return list(csv.DictReader(csv_file))


def _read_yaml(path: Path) -> dict[str, Any]:
    """Read one YAML mapping."""

    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict), f"Expected YAML mapping | {path}"
    return payload


def _write_csv(path: Path, row_list: list[dict[str, Any]]) -> None:
    """Write dictionaries to a CSV file with stable headers."""

    assert row_list, f"Refusing to write empty CSV | {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list(row_list[0]))
        writer.writeheader()
        writer.writerows(row_list)


def _sha256(path: Path) -> str:
    """Compute the SHA-256 digest of one file."""

    digest = hashlib.sha256()
    with path.open("rb") as source_file:
        while chunk := source_file.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def _resolve_project_path(path_value: str | Path) -> Path:
    """Resolve a repository-relative path."""

    path = Path(path_value)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path.resolve()


def main() -> None:
    """Build and immediately validate the Stage 0 freeze."""

    arguments = parse_arguments()
    configuration = load_configuration(arguments.config)
    summary = build_evidence_freeze(configuration, arguments.config)
    row_count_map = validate_written_outputs(configuration)
    print(
        "WAVE52R_STAGE0_BUILD_OK "
        f"status={summary['exit_gate']['status']} "
        f"manifest_rows={row_count_map['manifest_rows']} "
        f"operating_cell_rows={row_count_map['operating_cell_rows']} "
        f"reproduction_rows={row_count_map['reproduction_rows']}"
    )


if __name__ == "__main__":
    main()
