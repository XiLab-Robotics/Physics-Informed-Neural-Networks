"""Build the Wave 5.2 Phase 4 hysteresis feasibility audit."""

from __future__ import annotations

# Import Standard Library Utilities
import argparse
import csv
import hashlib
import sys
from datetime import datetime
from datetime import timezone
from pathlib import Path
from typing import Any

# Expose The Repository Root For Dataset-Lineage Imports
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific And Configuration Utilities
import numpy as np
import yaml

# Import Canonical Dataset-Lineage Utilities
from data.generate_polished_dataset import input_file_records
from data.generate_polished_dataset import input_files
from data.generate_polished_dataset import unique_condition_records


DEFAULT_CONFIGURATION_PATH = (
    PROJECT_ROOT
    / "config"
    / "analysis"
    / "pinn_program_hysteresis"
    / "phase4_hysteresis_feasibility_audit.yaml"
)

RAW_TRAJECTORY_FIELD_NAME_LIST = [
    "condition_id",
    "split",
    "source_path",
    "row_count",
    "source_size_bytes",
    "filesystem_modified_at_utc",
    "filesystem_timestamp_is_acquisition_evidence",
    "forward_valid_row_count",
    "backward_valid_row_count",
    "forward_valid_segment_count",
    "backward_valid_segment_count",
    "valid_overlap_row_count",
    "direction_window_order",
    "inter_window_gap_row_count",
    "inter_window_gap_duration_s",
    "pre_valid_row_count",
    "post_valid_row_count",
    "controlled_warmup_label_available",
    "deterministic_reset_marker_available",
    "minimum_speed_rpm",
    "maximum_speed_rpm",
    "forward_valid_median_speed_rpm",
    "backward_valid_median_speed_rpm",
    "valid_window_direction_sign_pass",
    "sustained_motion_segment_count",
    "sustained_direction_reversal_count",
    "single_reversal_pair_available",
    "repeated_reversal_cycle_pass",
    "repeated_major_loop_pass",
    "minor_loop_marker_available",
    "offline_reversal_oracle_available",
    "real_hysteresis_training_eligible",
]

DATASET_CONTRACT_FIELD_NAME_LIST = [
    "evidence_surface",
    "source_file_count",
    "row_order_preserved",
    "explicit_timestamp_available",
    "direction_pairing",
    "reversal_transition_preserved",
    "repeated_reversal_cycles",
    "minor_loop_labels",
    "controlled_warmup_labels",
    "deterministic_reset_marker",
    "te_target_status",
    "causal_use_boundary",
    "feasibility_class",
]

FORMULATION_FIELD_NAME_LIST = [
    "formulation_id",
    "name",
    "feasibility_class",
    "real_data_training_authorized",
    "synthetic_oracle_test_authorized",
    "offline_oracle_test_authorized",
    "reason",
]


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Build the Phase 4 hysteresis feasibility audit.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIGURATION_PATH,
        help="Phase 4 audit configuration path.",
    )
    return parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:
    """Resolve one project-relative path."""

    path = Path(path_value)
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def project_relative_path(path: Path) -> str:
    """Return one normalized project-relative path."""

    return path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix()


def compute_sha256(path: Path) -> str:
    """Compute the SHA-256 digest of one file."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle)
    assert isinstance(payload, dict), f"Expected YAML mapping | {path}"
    return payload


def load_phase0_split_map(path: Path) -> dict[str, str]:
    """Load the unique Phase 0 split assignment per operating condition."""

    split_map: dict[str, str] = {}
    direction_set_map: dict[str, set[str]] = {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            condition_id = row["condition_id"]
            split_name = row["split"]
            previous_split = split_map.setdefault(condition_id, split_name)
            assert previous_split == split_name, (
                f"Inconsistent split assignment | {condition_id}"
            )
            direction_set_map.setdefault(condition_id, set()).add(row["direction"])

    for condition_id, direction_set in direction_set_map.items():
        assert direction_set == {"Fw", "Bw"}, (
            f"Missing direction in Phase 0 audit | {condition_id} | {direction_set}"
        )
    return split_map


def format_condition_number(value: float) -> str:
    """Format a nominal condition value for a stable identifier."""

    return f"{value:g}"


def build_condition_id(conditions: dict[str, float]) -> str:
    """Build the canonical condition identifier."""

    return (
        f"speed_{format_condition_number(conditions['speed_rpm'])}rpm"
        f"__torque_{format_condition_number(conditions['torque_nm'])}Nm"
        f"__temperature_{format_condition_number(conditions['temperature_deg'])}degC"
    )


def detect_delimiter(path: Path) -> str:
    """Detect the single-character delimiter used by one raw CSV."""

    with path.open("r", encoding="utf-8-sig") as handle:
        first_line = handle.readline()
    if ";" in first_line:
        return ";"
    if "," in first_line:
        return ","
    raise ValueError(f"Could not detect raw delimiter | {path}")


def count_boolean_segments(mask: np.ndarray) -> int:
    """Count contiguous true segments in one Boolean mask."""

    assert mask.ndim == 1, f"Expected rank-1 mask | {mask.shape}"
    if mask.size == 0:
        return 0
    segment_starts = mask & np.concatenate(
        [np.asarray([True], dtype=bool), ~mask[:-1]]
    )
    return int(np.count_nonzero(segment_starts))


def build_sustained_motion_runs(
    speed_rpm: np.ndarray,
    minimum_motion_speed_rpm: float,
    minimum_sustained_direction_rows: int,
) -> list[tuple[int, int, int]]:
    """Build debounced positive and negative motion runs."""

    motion_code = np.zeros(speed_rpm.shape, dtype=np.int8)
    motion_code[speed_rpm > minimum_motion_speed_rpm] = 1
    motion_code[speed_rpm < -minimum_motion_speed_rpm] = -1

    change_index_array = np.flatnonzero(np.diff(motion_code) != 0) + 1
    boundary_index_array = np.concatenate(
        [
            np.asarray([0], dtype=np.int64),
            change_index_array,
            np.asarray([motion_code.size], dtype=np.int64),
        ]
    )

    sustained_run_list: list[tuple[int, int, int]] = []
    for boundary_index in range(boundary_index_array.size - 1):
        start_index = int(boundary_index_array[boundary_index])
        end_index = int(boundary_index_array[boundary_index + 1])
        direction_code = int(motion_code[start_index])
        if direction_code == 0:
            continue
        if end_index - start_index < minimum_sustained_direction_rows:
            continue
        sustained_run_list.append((direction_code, start_index, end_index))

    collapsed_run_list: list[tuple[int, int, int]] = []
    for direction_code, start_index, end_index in sustained_run_list:
        if (
            collapsed_run_list
            and collapsed_run_list[-1][0] == direction_code
        ):
            previous_direction, previous_start, _previous_end = (
                collapsed_run_list[-1]
            )
            collapsed_run_list[-1] = (
                previous_direction,
                previous_start,
                end_index,
            )
        else:
            collapsed_run_list.append(
                (direction_code, start_index, end_index)
            )
    return collapsed_run_list


def resolve_window_order(
    forward_index_array: np.ndarray,
    backward_index_array: np.ndarray,
) -> tuple[str, int, int, int]:
    """Resolve directional window order and surrounding row counts."""

    assert forward_index_array.size > 0, "Forward validity window is empty"
    assert backward_index_array.size > 0, "Backward validity window is empty"

    forward_first = int(forward_index_array[0])
    forward_last = int(forward_index_array[-1])
    backward_first = int(backward_index_array[0])
    backward_last = int(backward_index_array[-1])

    if forward_last < backward_first:
        return (
            "Fw_then_Bw",
            backward_first - forward_last - 1,
            forward_first,
            backward_last,
        )
    if backward_last < forward_first:
        return (
            "Bw_then_Fw",
            forward_first - backward_last - 1,
            backward_first,
            forward_last,
        )
    return (
        "overlapping_or_interleaved",
        0,
        min(forward_first, backward_first),
        max(forward_last, backward_last),
    )


def audit_raw_trajectory(
    source_path: Path,
    conditions: dict[str, float],
    split_name: str,
    configuration: dict[str, Any],
) -> dict[str, Any]:
    """Audit one raw bidirectional operating-condition trajectory."""

    column_indices = configuration["raw_column_indices"]
    selected_column_index_tuple = (
        int(column_indices["theta_encoder_deg"]),
        int(column_indices["load_torque_nm"]),
        int(column_indices["valid_forward"]),
        int(column_indices["valid_backward"]),
        int(column_indices["oil_temperature_deg_c"]),
    )
    value_matrix = np.loadtxt(
        source_path,
        delimiter=detect_delimiter(source_path),
        usecols=selected_column_index_tuple,
        ndmin=2,
    )
    assert value_matrix.ndim == 2 and value_matrix.shape[1] == 5, (
        f"Unexpected raw matrix shape | {source_path} | {value_matrix.shape}"
    )
    assert np.all(np.isfinite(value_matrix)), (
        f"Non-finite raw value | {source_path}"
    )

    theta_encoder_deg = value_matrix[:, 0]
    forward_mask = value_matrix[:, 2] != 0.0
    backward_mask = value_matrix[:, 3] != 0.0
    forward_index_array = np.flatnonzero(forward_mask)
    backward_index_array = np.flatnonzero(backward_mask)
    assert forward_index_array.size > 0 and backward_index_array.size > 0, (
        f"Missing direction validity window | {source_path}"
    )

    direction_window_order, gap_row_count, first_valid_index, last_valid_index = (
        resolve_window_order(forward_index_array, backward_index_array)
    )
    sample_interval_s = float(configuration["constants"]["sample_interval_s"])
    angular_step_deg = np.diff(
        theta_encoder_deg,
        prepend=theta_encoder_deg[0],
    )
    speed_rpm = angular_step_deg / 360.0 * 60.0 / sample_interval_s

    thresholds = configuration["thresholds"]
    sustained_run_list = build_sustained_motion_runs(
        speed_rpm=speed_rpm,
        minimum_motion_speed_rpm=float(
            thresholds["minimum_motion_speed_rpm"]
        ),
        minimum_sustained_direction_rows=int(
            thresholds["minimum_sustained_direction_rows"]
        ),
    )
    sustained_reversal_count = sum(
        sustained_run_list[index][0] != sustained_run_list[index - 1][0]
        for index in range(1, len(sustained_run_list))
    )

    forward_segment_count = count_boolean_segments(forward_mask)
    backward_segment_count = count_boolean_segments(backward_mask)
    repeated_reversal_cycle_pass = sustained_reversal_count >= int(
        thresholds["minimum_reversal_count_for_repeated_cycle"]
    )
    repeated_major_loop_pass = (
        forward_segment_count
        >= int(thresholds["minimum_valid_segments_per_direction_for_repeated_loop"])
        and backward_segment_count
        >= int(thresholds["minimum_valid_segments_per_direction_for_repeated_loop"])
    )

    forward_median_speed_rpm = float(np.median(speed_rpm[forward_mask]))
    backward_median_speed_rpm = float(np.median(speed_rpm[backward_mask]))
    minimum_motion_speed_rpm = float(thresholds["minimum_motion_speed_rpm"])
    direction_sign_pass = (
        forward_median_speed_rpm > minimum_motion_speed_rpm
        and backward_median_speed_rpm < -minimum_motion_speed_rpm
    )
    single_reversal_pair_available = (
        direction_window_order in {"Fw_then_Bw", "Bw_then_Fw"}
        and sustained_reversal_count >= 1
        and direction_sign_pass
    )
    offline_reversal_oracle_available = (
        single_reversal_pair_available
        and forward_segment_count == 1
        and backward_segment_count == 1
        and int(np.count_nonzero(forward_mask & backward_mask)) == 0
    )

    source_stat = source_path.stat()
    minor_loop_marker_available = False
    controlled_warmup_label_available = False
    deterministic_reset_marker_available = False
    real_hysteresis_training_eligible = (
        repeated_reversal_cycle_pass
        and repeated_major_loop_pass
        and minor_loop_marker_available
        and controlled_warmup_label_available
        and deterministic_reset_marker_available
    )

    return {
        "condition_id": build_condition_id(conditions),
        "split": split_name,
        "source_path": project_relative_path(source_path),
        "row_count": int(value_matrix.shape[0]),
        "source_size_bytes": int(source_stat.st_size),
        "filesystem_modified_at_utc": datetime.fromtimestamp(
            source_stat.st_mtime,
            tz=timezone.utc,
        ).isoformat(),
        "filesystem_timestamp_is_acquisition_evidence": False,
        "forward_valid_row_count": int(forward_index_array.size),
        "backward_valid_row_count": int(backward_index_array.size),
        "forward_valid_segment_count": forward_segment_count,
        "backward_valid_segment_count": backward_segment_count,
        "valid_overlap_row_count": int(
            np.count_nonzero(forward_mask & backward_mask)
        ),
        "direction_window_order": direction_window_order,
        "inter_window_gap_row_count": gap_row_count,
        "inter_window_gap_duration_s": gap_row_count * sample_interval_s,
        "pre_valid_row_count": first_valid_index,
        "post_valid_row_count": int(value_matrix.shape[0] - last_valid_index - 1),
        "controlled_warmup_label_available": controlled_warmup_label_available,
        "deterministic_reset_marker_available": deterministic_reset_marker_available,
        "minimum_speed_rpm": float(np.min(speed_rpm)),
        "maximum_speed_rpm": float(np.max(speed_rpm)),
        "forward_valid_median_speed_rpm": forward_median_speed_rpm,
        "backward_valid_median_speed_rpm": backward_median_speed_rpm,
        "valid_window_direction_sign_pass": direction_sign_pass,
        "sustained_motion_segment_count": len(sustained_run_list),
        "sustained_direction_reversal_count": sustained_reversal_count,
        "single_reversal_pair_available": single_reversal_pair_available,
        "repeated_reversal_cycle_pass": repeated_reversal_cycle_pass,
        "repeated_major_loop_pass": repeated_major_loop_pass,
        "minor_loop_marker_available": minor_loop_marker_available,
        "offline_reversal_oracle_available": offline_reversal_oracle_available,
        "real_hysteresis_training_eligible": real_hysteresis_training_eligible,
    }


def write_csv(
    path: Path,
    field_name_list: list[str],
    row_list: list[dict[str, Any]],
) -> None:
    """Write one deterministic CSV artifact."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)


def build_dataset_contract_rows(
    raw_row_list: list[dict[str, Any]],
    configuration: dict[str, Any],
) -> list[dict[str, Any]]:
    """Build dataset and prior-model chronology boundary rows."""

    expected_inventory = configuration["expected_inventory"]
    any_raw_reversal = any(
        bool(row["single_reversal_pair_available"]) for row in raw_row_list
    )
    any_repeated_reversal = any(
        bool(row["repeated_reversal_cycle_pass"]) for row in raw_row_list
    )

    return [
        {
            "evidence_surface": "original_dataset",
            "source_file_count": int(expected_inventory["raw_csv_file_count"]),
            "row_order_preserved": True,
            "explicit_timestamp_available": False,
            "direction_pairing": "same_file_validity_windows",
            "reversal_transition_preserved": any_raw_reversal,
            "repeated_reversal_cycles": any_repeated_reversal,
            "minor_loop_labels": False,
            "controlled_warmup_labels": False,
            "deterministic_reset_marker": False,
            "te_target_status": "offline_reconstructable_from_two_encoders",
            "causal_use_boundary": "offline_reversal_oracle",
            "feasibility_class": "offline_oracle_only",
        },
        {
            "evidence_surface": "polished_dataset",
            "source_file_count": int(
                expected_inventory["polished_directional_file_count"]
            ),
            "row_order_preserved": True,
            "explicit_timestamp_available": False,
            "direction_pairing": "separate_files_per_direction",
            "reversal_transition_preserved": False,
            "repeated_reversal_cycles": False,
            "minor_loop_labels": False,
            "controlled_warmup_labels": False,
            "deterministic_reset_marker": False,
            "te_target_status": "available_only_for_supervised_training",
            "causal_use_boundary": "single_direction_steady_revolution",
            "feasibility_class": "blocked_by_data_contract",
        },
        {
            "evidence_surface": "simplified_dataset",
            "source_file_count": int(
                expected_inventory["simplified_file_count"]
            ),
            "row_order_preserved": False,
            "explicit_timestamp_available": False,
            "direction_pairing": "paired_columns_sorted_by_angle",
            "reversal_transition_preserved": False,
            "repeated_reversal_cycles": False,
            "minor_loop_labels": False,
            "controlled_warmup_labels": False,
            "deterministic_reset_marker": False,
            "te_target_status": "paired_static_curve_columns",
            "causal_use_boundary": "static_curve_or_angular_window_only",
            "feasibility_class": "blocked_by_data_contract",
        },
        {
            "evidence_surface": "wave4_4_training_view",
            "source_file_count": 6,
            "row_order_preserved": True,
            "explicit_timestamp_available": False,
            "direction_pairing": "independent_direction_windows",
            "reversal_transition_preserved": False,
            "repeated_reversal_cycles": False,
            "minor_loop_labels": False,
            "controlled_warmup_labels": False,
            "deterministic_reset_marker": False,
            "te_target_status": "supervised_directional_curve_target",
            "causal_use_boundary": "latent_angular_history_not_physical_loop_state",
            "feasibility_class": "exploratory_comparator_only",
        },
    ]


def build_formulation_rows(
    configuration: dict[str, Any],
) -> list[dict[str, Any]]:
    """Build the formulation feasibility decision rows."""

    row_list: list[dict[str, Any]] = []
    for entry in configuration["formulation_portfolio"]:
        feasibility_class = entry["feasibility_class"]
        row_list.append(
            {
                "formulation_id": entry["formulation_id"],
                "name": entry["name"],
                "feasibility_class": feasibility_class,
                "real_data_training_authorized": (
                    feasibility_class == "real_data_trainable"
                ),
                "synthetic_oracle_test_authorized": (
                    feasibility_class == "synthetic_oracle_only"
                ),
                "offline_oracle_test_authorized": (
                    feasibility_class == "offline_oracle_only"
                ),
                "reason": " ".join(str(entry["reason"]).split()),
            }
        )
    return row_list


def markdown_boolean(value: Any) -> str:
    """Render a Boolean-like value for a Markdown table."""

    return "yes" if bool(value) else "no"


def build_markdown_report(
    report_path: Path,
    summary: dict[str, Any],
    dataset_row_list: list[dict[str, Any]],
    formulation_row_list: list[dict[str, Any]],
) -> None:
    """Write the canonical Phase 4 feasibility report."""

    inventory = summary["inventory"]
    chronology = summary["chronology_evidence"]
    exit_gate = summary["exit_gate"]

    report_line_list = [
        "# Phase 4 Hysteresis, Friction, And Memory Feasibility Report",
        "",
        "## Overview",
        "",
        "Phase 4 is complete as a feasibility-first, non-training result. The",
        "original raw files preserve one ordered forward-to-backward trajectory",
        "per operating condition, including the unvalidated transition interval.",
        "However, the repository does not contain repeated reversal cycles,",
        "minor-loop labels, controlled warm-up labels, or a deterministic state",
        "reset marker. The Phase 4 real-data training gate therefore fails.",
        "",
        "No Phase 4 physical residual is promoted and no training campaign is",
        "prepared. The raw trajectories remain useful as offline reversal",
        "oracles, while Bouc-Wen, rolling-friction, play/stop, and white-box",
        "state laws remain available for synthetic-oracle verification.",
        "",
        "## Source Inventory",
        "",
        "| Evidence | Value |",
        "| --- | ---: |",
        f"| Raw CSV files | {inventory['raw_csv_file_count']} |",
        f"| Canonical raw conditions | {inventory['canonical_raw_condition_count']} |",
        f"| Ignored duplicate or connection files | {inventory['ignored_source_file_count']} |",
        f"| Polished directional files | {inventory['polished_directional_file_count']} |",
        f"| Simplified files | {inventory['simplified_file_count']} |",
        "",
        "## Chronology And State Evidence",
        "",
        "| Check | Result |",
        "| --- | ---: |",
        f"| Raw trajectories with ordered direction windows | {chronology['ordered_direction_window_count']} |",
        f"| Raw trajectories with at least one physical reversal | {chronology['single_reversal_pair_count']} |",
        f"| Raw trajectories with repeated reversals | {chronology['repeated_reversal_cycle_count']} |",
        f"| Raw trajectories with repeated major loops | {chronology['repeated_major_loop_count']} |",
        f"| Raw trajectories with minor-loop markers | {chronology['minor_loop_marker_count']} |",
        f"| Raw trajectories with controlled warm-up labels | {chronology['controlled_warmup_label_count']} |",
        f"| Raw trajectories with deterministic reset markers | {chronology['deterministic_reset_marker_count']} |",
        f"| Offline reversal-oracle trajectories | {chronology['offline_reversal_oracle_count']} |",
        "",
        "The raw row order plus the documented `0.25 ms` sample interval is",
        "sufficient to reconstruct an offline time axis. Filesystem modification",
        "times are explicitly excluded as acquisition chronology. The forward",
        "and backward validity windows are each contiguous, with a transition",
        "interval between them, but each condition supplies only one direction",
        "pair rather than repeated major or minor loops.",
        "",
        "## Dataset And Prior-Model Boundary",
        "",
        "| Surface | Pairing | Reversal preserved | Repeated cycles | Boundary |",
        "| --- | --- | --- | --- | --- |",
    ]

    for row in dataset_row_list:
        report_line_list.append(
            "| "
            f"`{row['evidence_surface']}` | "
            f"{row['direction_pairing']} | "
            f"{markdown_boolean(row['reversal_transition_preserved'])} | "
            f"{markdown_boolean(row['repeated_reversal_cycles'])} | "
            f"`{row['feasibility_class']}` |"
        )

    report_line_list.extend(
        [
            "",
            "Wave 4.4 demonstrated that short within-direction angular history can",
            "be encoded by GRU or causal TCN models. It did not preserve the raw",
            "forward-to-backward transition and therefore does not establish an",
            "identified physical hysteresis state.",
            "",
            "## Formulation Decisions",
            "",
            "| Formulation | Model | Decision | Real-data training |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in formulation_row_list:
        report_line_list.append(
            "| "
            f"`{row['formulation_id']}` | "
            f"{row['name']} | "
            f"`{row['feasibility_class']}` | "
            f"{markdown_boolean(row['real_data_training_authorized'])} |"
        )

    report_line_list.extend(
        [
            "",
            "### Decision Interpretation",
            "",
            "- `PINN-Y1`, `PINN-Y2`, `PINN-Y3`, and `PINN-Y5` remain eligible",
            "  for equation-level and synthetic-oracle tests only.",
            "- `PINN-Y4` is blocked because condition variation cannot be separated",
            "  from unknown hysteresis initialization without matched repeats.",
            "- `PINN-Y6` may be evaluated as an offline reconstructed-trajectory",
            "  comparator, but not promoted as a real-data hysteresis model.",
            "",
            "## Exit Gate",
            "",
            f"**Status: `{exit_gate['status']}`.**",
            "",
            "| Requirement | Passed |",
            "| --- | --- |",
        ]
    )
    for check_name, check_value in exit_gate["check_map"].items():
        report_line_list.append(
            f"| `{check_name}` | {markdown_boolean(check_value)} |"
        )

    report_line_list.extend(
        [
            "",
            "The mandatory repeated-reversal and stable-state requirements are not",
            "met. Phase 4 closes without training and the sixteen-phase roadmap",
            "advances to Phase 5, where bidirectional TE and lost-motion laws can",
            "use the existing paired `Fw` and `Bw` surfaces without pretending",
            "that the missing transition-state labels are available.",
            "",
            "## Reproducibility",
            "",
            f"- Configuration: `{summary['source_configuration']['path']}`",
            f"- Raw trajectory audit: `{summary['artifact_paths']['raw_trajectory_csv']}`",
            f"- Dataset contract audit: `{summary['artifact_paths']['dataset_contract_csv']}`",
            f"- Formulation decisions: `{summary['artifact_paths']['formulation_feasibility_csv']}`",
            f"- Machine-readable summary: `{summary['artifact_paths']['summary_yaml']}`",
            "",
        ]
    )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report_line_list), encoding="utf-8")


def main() -> None:
    """Build all Phase 4 audit artifacts and the decision report."""

    arguments = parse_arguments()
    configuration_path = resolve_project_path(arguments.config)
    configuration = load_yaml(configuration_path)

    # Resolve Source And Output Paths
    source_paths = configuration["source_paths"]
    output_paths = configuration["output_paths"]
    raw_dataset_root = resolve_project_path(source_paths["raw_dataset_root"])
    polished_dataset_root = resolve_project_path(
        source_paths["polished_dataset_root"]
    )
    simplified_dataset_root = resolve_project_path(
        source_paths["simplified_dataset_root"]
    )
    phase0_curve_audit_path = resolve_project_path(
        source_paths["phase0_curve_audit"]
    )
    phase0_foundation_audit_path = resolve_project_path(
        source_paths["phase0_foundation_audit"]
    )
    wave4_4_closeout_report_path = resolve_project_path(
        source_paths["wave4_4_closeout_report"]
    )
    output_directory = resolve_project_path(output_paths["output_directory"])
    raw_trajectory_csv_path = output_directory / output_paths["raw_trajectory_csv"]
    dataset_contract_csv_path = (
        output_directory / output_paths["dataset_contract_csv"]
    )
    formulation_feasibility_csv_path = (
        output_directory / output_paths["formulation_feasibility_csv"]
    )
    summary_yaml_path = output_directory / output_paths["summary_yaml"]
    report_path = resolve_project_path(output_paths["report_markdown"])

    required_path_list = [
        raw_dataset_root,
        polished_dataset_root,
        simplified_dataset_root,
        phase0_curve_audit_path,
        phase0_foundation_audit_path,
        wave4_4_closeout_report_path,
    ]
    for required_path in required_path_list:
        assert required_path.exists(), f"Missing Phase 4 input | {required_path}"

    # Build Canonical Raw Inventory
    raw_csv_path_list = sorted(raw_dataset_root.rglob("*.csv"))
    record_list, parser_skip_count = input_file_records(
        input_files(raw_dataset_root, polished_dataset_root)
    )
    selected_record_list = unique_condition_records(record_list)
    split_map = load_phase0_split_map(phase0_curve_audit_path)
    expected_inventory = configuration["expected_inventory"]
    assert len(raw_csv_path_list) == int(
        expected_inventory["raw_csv_file_count"]
    ), f"Raw inventory drift | {len(raw_csv_path_list)}"
    assert len(selected_record_list) == int(
        expected_inventory["canonical_raw_condition_count"]
    ), f"Canonical condition drift | {len(selected_record_list)}"
    assert parser_skip_count == 0, f"Unexpected parser skips | {parser_skip_count}"

    # Scan Every Canonical Raw Trajectory
    raw_row_list: list[dict[str, Any]] = []
    total_record_count = len(selected_record_list)
    for record_index, (source_path, conditions) in enumerate(
        selected_record_list,
        start=1,
    ):
        condition_id = build_condition_id(conditions)
        assert condition_id in split_map, (
            f"Raw condition absent from Phase 0 split | {condition_id}"
        )
        raw_row_list.append(
            audit_raw_trajectory(
                source_path=source_path,
                conditions=conditions,
                split_name=split_map[condition_id],
                configuration=configuration,
            )
        )
        if record_index % 50 == 0 or record_index == total_record_count:
            print(
                "PHASE4_RAW_AUDIT_PROGRESS "
                f"{record_index}/{total_record_count}"
            )

    # Build Aggregate Evidence And Decisions
    dataset_row_list = build_dataset_contract_rows(
        raw_row_list,
        configuration,
    )
    formulation_row_list = build_formulation_rows(configuration)
    assert len(formulation_row_list) == int(
        expected_inventory["formulation_count"]
    ), f"Unexpected formulation count | {len(formulation_row_list)}"

    polished_file_count = len(list(polished_dataset_root.rglob("*.csv")))
    simplified_file_count = len(list(simplified_dataset_root.rglob("*.csv")))
    ignored_source_file_count = len(raw_csv_path_list) - len(selected_record_list)
    assert polished_file_count == int(
        expected_inventory["polished_directional_file_count"]
    ), f"Polished inventory drift | {polished_file_count}"
    assert simplified_file_count == int(
        expected_inventory["simplified_file_count"]
    ), f"Simplified inventory drift | {simplified_file_count}"
    assert ignored_source_file_count == int(
        expected_inventory["ignored_duplicate_or_connection_file_count"]
    ), f"Ignored raw inventory drift | {ignored_source_file_count}"

    chronology_evidence = {
        "ordered_direction_window_count": sum(
            row["direction_window_order"] in {"Fw_then_Bw", "Bw_then_Fw"}
            for row in raw_row_list
        ),
        "single_reversal_pair_count": sum(
            bool(row["single_reversal_pair_available"]) for row in raw_row_list
        ),
        "repeated_reversal_cycle_count": sum(
            bool(row["repeated_reversal_cycle_pass"]) for row in raw_row_list
        ),
        "repeated_major_loop_count": sum(
            bool(row["repeated_major_loop_pass"]) for row in raw_row_list
        ),
        "minor_loop_marker_count": sum(
            bool(row["minor_loop_marker_available"]) for row in raw_row_list
        ),
        "controlled_warmup_label_count": sum(
            bool(row["controlled_warmup_label_available"])
            for row in raw_row_list
        ),
        "deterministic_reset_marker_count": sum(
            bool(row["deterministic_reset_marker_available"])
            for row in raw_row_list
        ),
        "offline_reversal_oracle_count": sum(
            bool(row["offline_reversal_oracle_available"])
            for row in raw_row_list
        ),
        "real_hysteresis_training_eligible_count": sum(
            bool(row["real_hysteresis_training_eligible"])
            for row in raw_row_list
        ),
        "minimum_inter_window_gap_duration_s": min(
            float(row["inter_window_gap_duration_s"]) for row in raw_row_list
        ),
        "maximum_inter_window_gap_duration_s": max(
            float(row["inter_window_gap_duration_s"]) for row in raw_row_list
        ),
        "minimum_sustained_direction_reversal_count": min(
            int(row["sustained_direction_reversal_count"])
            for row in raw_row_list
        ),
        "maximum_sustained_direction_reversal_count": max(
            int(row["sustained_direction_reversal_count"])
            for row in raw_row_list
        ),
    }

    exit_check_map = {
        "all_canonical_raw_files_scanned": (
            len(raw_row_list)
            == int(expected_inventory["canonical_raw_condition_count"])
        ),
        "ordered_acquisition_available": (
            chronology_evidence["ordered_direction_window_count"]
            == len(raw_row_list)
        ),
        "single_reversal_transition_available": (
            chronology_evidence["single_reversal_pair_count"] > 0
        ),
        "repeated_reversal_cycles_available": (
            chronology_evidence["repeated_reversal_cycle_count"] > 0
        ),
        "repeated_major_and_minor_loops_available": (
            chronology_evidence["repeated_major_loop_count"] > 0
            and chronology_evidence["minor_loop_marker_count"] > 0
        ),
        "controlled_warmup_state_available": (
            chronology_evidence["controlled_warmup_label_count"] > 0
        ),
        "deterministic_reset_evidence_available": (
            chronology_evidence["deterministic_reset_marker_count"] > 0
        ),
        "stable_causal_state_evolution_testable": (
            chronology_evidence["real_hysteresis_training_eligible_count"] > 0
        ),
    }
    training_authorized = all(exit_check_map.values())
    assert not training_authorized, (
        "Unexpected Phase 4 training authorization; review the campaign gate"
    )

    # Persist Machine-Readable Artifacts
    write_csv(
        raw_trajectory_csv_path,
        RAW_TRAJECTORY_FIELD_NAME_LIST,
        raw_row_list,
    )
    write_csv(
        dataset_contract_csv_path,
        DATASET_CONTRACT_FIELD_NAME_LIST,
        dataset_row_list,
    )
    write_csv(
        formulation_feasibility_csv_path,
        FORMULATION_FIELD_NAME_LIST,
        formulation_row_list,
    )

    summary = {
        "schema_version": 1,
        "audit_id": configuration["audit_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_configuration": {
            "path": project_relative_path(configuration_path),
            "sha256": compute_sha256(configuration_path),
        },
        "source_evidence": {
            "phase0_foundation_audit": {
                "path": project_relative_path(phase0_foundation_audit_path),
                "sha256": compute_sha256(phase0_foundation_audit_path),
            },
            "phase0_curve_audit": {
                "path": project_relative_path(phase0_curve_audit_path),
                "sha256": compute_sha256(phase0_curve_audit_path),
            },
            "wave4_4_closeout_report": {
                "path": project_relative_path(wave4_4_closeout_report_path),
                "sha256": compute_sha256(wave4_4_closeout_report_path),
            },
        },
        "inventory": {
            "raw_csv_file_count": len(raw_csv_path_list),
            "canonical_raw_condition_count": len(raw_row_list),
            "ignored_source_file_count": ignored_source_file_count,
            "polished_directional_file_count": polished_file_count,
            "simplified_file_count": simplified_file_count,
        },
        "chronology_evidence": chronology_evidence,
        "dataset_contract_class_count": {
            feasibility_class: sum(
                row["feasibility_class"] == feasibility_class
                for row in dataset_row_list
            )
            for feasibility_class in sorted(
                {row["feasibility_class"] for row in dataset_row_list}
            )
        },
        "formulation_class_count": {
            feasibility_class: sum(
                row["feasibility_class"] == feasibility_class
                for row in formulation_row_list
            )
            for feasibility_class in sorted(
                {row["feasibility_class"] for row in formulation_row_list}
            )
        },
        "exit_gate": {
            "status": "failed_no_training_authorized",
            "real_data_training_authorized": False,
            "phase4_physical_residual_promoted": False,
            "advance_to_phase5": True,
            "check_map": exit_check_map,
            "decision": (
                "Close Phase 4 as a valid feasibility result. Preserve raw "
                "trajectories as offline reversal oracles and physical state "
                "laws as synthetic-oracle tests; do not train a promotable "
                "hysteresis PINN on the current data contract."
            ),
        },
        "artifact_paths": {
            "raw_trajectory_csv": project_relative_path(
                raw_trajectory_csv_path
            ),
            "dataset_contract_csv": project_relative_path(
                dataset_contract_csv_path
            ),
            "formulation_feasibility_csv": project_relative_path(
                formulation_feasibility_csv_path
            ),
            "summary_yaml": project_relative_path(summary_yaml_path),
            "report_markdown": project_relative_path(report_path),
        },
    }

    output_directory.mkdir(parents=True, exist_ok=True)
    with summary_yaml_path.open("w", encoding="utf-8", newline="\n") as handle:
        yaml.safe_dump(
            summary,
            handle,
            sort_keys=False,
            allow_unicode=True,
        )
    build_markdown_report(
        report_path=report_path,
        summary=summary,
        dataset_row_list=dataset_row_list,
        formulation_row_list=formulation_row_list,
    )

    print(
        "PHASE4_HYSTERESIS_FEASIBILITY_AUDIT_OK "
        f"raw_conditions={len(raw_row_list)} "
        f"single_reversal={chronology_evidence['single_reversal_pair_count']} "
        f"repeated_reversal={chronology_evidence['repeated_reversal_cycle_count']} "
        "training_authorized=false"
    )


if __name__ == "__main__":
    main()
