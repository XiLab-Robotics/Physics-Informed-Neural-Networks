"""Validate the full-candidate Wave 5.2R Track 2 package without running it."""

from __future__ import annotations

# Import Python Utilities
import argparse
from datetime import datetime
import hashlib
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
import yaml

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)


# Define Package Paths
DEFAULT_CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "wave52r_full_candidate_parallel_temporal_non_temporal_matrix.yaml"
)
DEFAULT_OUTPUT_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "full_candidate_track2_analysis"
    / "package_preflight_summary.yaml"
)
REMOTE_SOURCE_PATH_LIST_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "full_candidate_track2_analysis"
    / "remote_source_path_list.txt"
)


def read_yaml(yaml_path: Path) -> dict[str, Any]:
    """Read one required YAML mapping."""

    assert yaml_path.is_file(), f"Required YAML path is missing | {yaml_path}"
    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        payload = yaml.safe_load(yaml_file)
    assert isinstance(payload, dict), f"YAML root must be a mapping | {yaml_path}"
    return payload


def write_yaml(yaml_path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping with a normal final newline."""

    yaml_path.parent.mkdir(parents=True, exist_ok=True)
    with yaml_path.open("w", encoding="utf-8", newline="\n") as yaml_file:
        yaml.safe_dump(
            payload,
            yaml_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def compute_prediction_fingerprint(
    candidate: reference_family_vs_feedforward_support.Track2Candidate,
) -> str | None:
    """Compute one stable fingerprint for a precomputed prediction matrix."""

    if (
        candidate.candidate_kind
        != reference_family_vs_feedforward_support
        .PRECOMPUTED_FULL_CURVE_CANDIDATE_KIND
    ):
        return None
    assert candidate.model_dictionary is not None
    prediction_lookup = candidate.model_dictionary[
        "prediction_by_condition_key"
    ]
    ordered_prediction_matrix = np.vstack(
        [
            np.asarray(
                prediction_lookup[condition_key],
                dtype=np.float32,
            )
            for condition_key in sorted(prediction_lookup)
        ]
    )
    return hashlib.sha256(
        ordered_prediction_matrix.tobytes(order="C")
    ).hexdigest()


def validate_remote_source_list() -> list[str]:
    """Validate every declared remote source path."""

    assert REMOTE_SOURCE_PATH_LIST_PATH.is_file()
    source_path_list = [
        source_path_text.strip()
        for source_path_text in REMOTE_SOURCE_PATH_LIST_PATH.read_text(
            encoding="utf-8"
        ).splitlines()
        if source_path_text.strip()
    ]
    assert source_path_list == sorted(set(source_path_list))
    missing_source_path_list = [
        source_path_text
        for source_path_text in source_path_list
        if not (PROJECT_ROOT / source_path_text).exists()
    ]
    assert not missing_source_path_list, (
        "Remote source list contains missing paths | "
        f"paths={missing_source_path_list[:5]}"
    )
    return source_path_list


def validate_package(config_path: Path) -> dict[str, Any]:
    """Validate inventory, candidate loading, and immutable prediction inputs."""

    training_config = (
        reference_family_vs_feedforward_support
        .load_reference_family_comparison_config(config_path)
    )
    metadata = training_config["metadata"]
    inventory_path = (
        reference_family_vs_feedforward_support
        .shared_training_infrastructure
        .resolve_runtime_project_relative_path(
            metadata["candidate_inventory_path"]
        )
    )
    inventory_payload = read_yaml(inventory_path)
    candidate_configuration_list = (
        reference_family_vs_feedforward_support
        .resolve_track2_candidate_configuration_list(training_config)
    )
    candidate_id_list = [
        str(candidate_configuration["candidate_id"])
        for candidate_configuration in candidate_configuration_list
    ]
    expected_candidate_count = int(
        metadata["expected_candidate_count"]
    )
    assert len(candidate_id_list) == expected_candidate_count
    assert len(candidate_id_list) == len(set(candidate_id_list))
    assert (
        int(inventory_payload["matrix_eligible_candidate_count"])
        == expected_candidate_count
    )
    inventory_eligible_candidate_id_set = {
        str(inventory_entry["candidate_id"])
        for inventory_entry in inventory_payload["candidate_list"]
        if bool(inventory_entry["matrix_eligible"])
    }
    assert set(candidate_id_list) == inventory_eligible_candidate_id_set

    loaded_candidate_list = []
    prediction_fingerprint_by_candidate_id: dict[str, str] = {}
    candidate_kind_count: dict[str, int] = {}
    for candidate_configuration in candidate_configuration_list:
        candidate = (
            reference_family_vs_feedforward_support
            .load_track2_candidate(candidate_configuration)
        )
        loaded_candidate_list.append(candidate)
        candidate_kind_count[candidate.candidate_kind] = (
            candidate_kind_count.get(candidate.candidate_kind, 0) + 1
        )
        prediction_fingerprint = compute_prediction_fingerprint(
            candidate
        )
        if prediction_fingerprint is not None:
            prediction_fingerprint_by_candidate_id[
                candidate.candidate_id
            ] = prediction_fingerprint

    # Exercise the immutable archive adapter against the real Track 2 dataset
    # records. This proves condition-key resolution and archived-truth identity
    # without computing the heavy comparison matrix or its reports.
    selected_harmonic_list = [
        int(value)
        for value in training_config["evaluation"]["selected_harmonics"]
    ]
    curve_record_list, _, _, _ = (
        reference_family_vs_feedforward_support.build_curve_record_list(
            training_config,
            selected_harmonic_list,
        )
    )
    forward_curve_record_list = [
        curve_record
        for curve_record in curve_record_list
        if str(curve_record.direction_label).strip().lower() == "forward"
    ]
    assert len(forward_curve_record_list) == 97
    precomputed_adapter_replay_count = 0
    archived_truth_max_abs_difference_deg = 0.0
    archived_truth_absolute_difference_sum_deg = 0.0
    archived_truth_sample_count = 0
    for candidate in loaded_candidate_list:
        if (
            candidate.candidate_kind
            != reference_family_vs_feedforward_support
            .PRECOMPUTED_FULL_CURVE_CANDIDATE_KIND
        ):
            continue
        for curve_record in forward_curve_record_list:
            predicted_curve_deg = (
                reference_family_vs_feedforward_support
                .predict_wave52r_precomputed_full_curve(
                    candidate,
                    curve_record,
                )
            )
            assert np.all(np.isfinite(predicted_curve_deg))
            condition_key = (
                reference_family_vs_feedforward_support
                .build_wave52r_condition_key_from_curve_record(
                    curve_record
                )
            )
            archived_truth_curve_deg = (
                reference_family_vs_feedforward_support
                .interpolate_wave52r_uniform_curve_to_track2_grid(
                    candidate.model_dictionary[
                        "truth_by_condition_key"
                    ][condition_key],
                    curve_record.angular_position_deg,
                )
            )
            archived_truth_absolute_difference_deg = np.abs(
                archived_truth_curve_deg
                - curve_record.transmission_error_deg.astype(np.float32)
            )
            archived_truth_max_abs_difference_deg = max(
                archived_truth_max_abs_difference_deg,
                float(np.max(archived_truth_absolute_difference_deg)),
            )
            archived_truth_absolute_difference_sum_deg += float(
                np.sum(archived_truth_absolute_difference_deg)
            )
            archived_truth_sample_count += int(
                archived_truth_absolute_difference_deg.size
            )
            precomputed_adapter_replay_count += 1

    candidate_id_list_by_fingerprint: dict[str, list[str]] = {}
    for (
        candidate_id,
        prediction_fingerprint,
    ) in prediction_fingerprint_by_candidate_id.items():
        candidate_id_list_by_fingerprint.setdefault(
            prediction_fingerprint,
            [],
        ).append(candidate_id)
    duplicate_prediction_group_list = [
        {
            "prediction_sha256": prediction_fingerprint,
            "candidate_id_list": sorted(
                fingerprint_candidate_id_list
            ),
        }
        for (
            prediction_fingerprint,
            fingerprint_candidate_id_list,
        ) in sorted(candidate_id_list_by_fingerprint.items())
        if len(fingerprint_candidate_id_list) > 1
    ]

    temporal_candidate_count = int(
        inventory_payload["temporal_candidate_count"]
    )
    non_temporal_candidate_count = int(
        inventory_payload["non_temporal_candidate_count"]
    )
    assert temporal_candidate_count == int(
        metadata["expected_temporal_candidate_count"]
    )
    assert non_temporal_candidate_count == int(
        metadata["expected_non_temporal_candidate_count"]
    )
    required_candidate_id_set = {
        "wave52r_stage15_pf_a_setpoint_quadratic_Fw",
        "accepted_periodic_mlp_harmonic_Fw",
        "accepted_periodic_gru_sequence_Fw",
        "wave52r_stage5_h04_seed_314159",
        "wave52r_stage9_k01",
    }
    assert required_candidate_id_set.issubset(set(candidate_id_list))

    remote_source_path_list = validate_remote_source_list()
    return {
        "schema_version": 1,
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": "passed",
        "config_path": config_path.resolve().relative_to(
            PROJECT_ROOT.resolve()
        ).as_posix(),
        "inventory_path": inventory_path.resolve().relative_to(
            PROJECT_ROOT.resolve()
        ).as_posix(),
        "candidate_count": len(loaded_candidate_list),
        "temporal_candidate_count": temporal_candidate_count,
        "non_temporal_candidate_count": non_temporal_candidate_count,
        "candidate_kind_count": candidate_kind_count,
        "precomputed_prediction_candidate_count": len(
            prediction_fingerprint_by_candidate_id
        ),
        "real_forward_curve_record_count": len(
            forward_curve_record_list
        ),
        "precomputed_adapter_replay_count": (
            precomputed_adapter_replay_count
        ),
        "archived_truth_grid_replay_max_abs_difference_deg": (
            archived_truth_max_abs_difference_deg
        ),
        "archived_truth_grid_replay_mae_deg": (
            archived_truth_absolute_difference_sum_deg
            / archived_truth_sample_count
        ),
        "duplicate_prediction_group_count": len(
            duplicate_prediction_group_list
        ),
        "duplicate_prediction_group_list": (
            duplicate_prediction_group_list
        ),
        "remote_source_path_count": len(remote_source_path_list),
        "heavy_matrix_executed": False,
    }


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Validate the full-candidate Wave 5.2R Track 2 package "
            "without executing the heavy matrix."
        )
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
    )
    argument_parser.add_argument(
        "--output-path",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
    )
    return argument_parser.parse_args()


def main() -> None:
    """Run package validation and persist the result."""

    arguments = parse_arguments()
    config_path = arguments.config_path
    if not config_path.is_absolute():
        config_path = PROJECT_ROOT / config_path
    output_path = arguments.output_path
    if not output_path.is_absolute():
        output_path = PROJECT_ROOT / output_path

    validation_payload = validate_package(config_path)
    write_yaml(output_path, validation_payload)
    print(
        "WAVE52R_FULL_CANDIDATE_TRACK2_PREFLIGHT_PASSED "
        f"candidates={validation_payload['candidate_count']} "
        f"duplicates={validation_payload['duplicate_prediction_group_count']}"
    )
    print(output_path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix())


if __name__ == "__main__":
    main()
