"""Build the Stage 4 causal setpoint validity envelope."""

from __future__ import annotations

# Import Python Utilities
import csv
from itertools import product
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
import yaml

# Import Stage 4 Preparation Utilities
from scripts.campaigns.wave_5_2.prepare_wave52r_stage4_data_only_residual_capacity_ladder_campaign import (
    COMMON_SPLIT_MANIFEST_PATH,
    EXCLUDED_CONDITION_ID_LIST,
    PHASE1_CONFIGURATION_PATH,
    build_setpoint_operating_feature_array,
    build_surface_from_payload,
    load_curve_records,
    load_yaml,
    predict_curve,
)


# Define Artifact Paths
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
)
CAUSAL_ANCHOR_PATH = (
    ANALYSIS_DIRECTORY / "stage4_causal_setpoint_pf_a_surface.yaml"
)
ENVELOPE_PATH = (
    ANALYSIS_DIRECTORY / "stage4_causal_setpoint_validity_envelope.yaml"
)
CONDITION_PATH = (
    ANALYSIS_DIRECTORY
    / "stage4_causal_setpoint_validity_envelope_conditions.csv"
)


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


def compute_nearest_standardized_distance(
    query_feature_matrix: np.ndarray,
    reference_feature_matrix: np.ndarray,
    feature_scale: np.ndarray,
) -> np.ndarray:
    """Compute nearest Euclidean distance in standardized setpoint space."""

    standardized_difference_tensor = (
        query_feature_matrix[:, np.newaxis, :]
        - reference_feature_matrix[np.newaxis, :, :]
    ) / feature_scale[np.newaxis, np.newaxis, :]
    return np.min(
        np.linalg.norm(standardized_difference_tensor, axis=2),
        axis=1,
    )


def main() -> None:
    """Classify every eligible forward condition using training setpoints."""

    phase1_configuration = load_yaml(PHASE1_CONFIGURATION_PATH)
    common_split_manifest = load_yaml(COMMON_SPLIT_MANIFEST_PATH)
    curve_record_list = load_curve_records(
        phase1_configuration,
        common_split_manifest,
    )
    excluded_condition_id_set = set(EXCLUDED_CONDITION_ID_LIST)
    forward_record_list = [
        record
        for record in curve_record_list
        if record.direction == "Fw"
        and record.condition_id not in excluded_condition_id_set
    ]
    training_record_list = [
        record
        for record in forward_record_list
        if record.split == "train"
    ]
    assert len(forward_record_list) == 966
    assert len(training_record_list) == 675

    causal_anchor_payload = load_yaml(CAUSAL_ANCHOR_PATH)
    causal_surface = build_surface_from_payload(
        causal_anchor_payload["surface"]
    )
    training_feature_matrix = np.vstack(
        [
            build_setpoint_operating_feature_array(record)
            for record in training_record_list
        ]
    )
    forward_feature_matrix = np.vstack(
        [
            build_setpoint_operating_feature_array(record)
            for record in forward_record_list
        ]
    )
    feature_minimum = np.min(training_feature_matrix, axis=0)
    feature_maximum = np.max(training_feature_matrix, axis=0)
    feature_scale = causal_surface.feature_scale

    # Derive A Training-Only Leave-One-Out Density Threshold
    standardized_training_difference_tensor = (
        training_feature_matrix[:, np.newaxis, :]
        - training_feature_matrix[np.newaxis, :, :]
    ) / feature_scale[np.newaxis, np.newaxis, :]
    training_distance_matrix = np.linalg.norm(
        standardized_training_difference_tensor,
        axis=2,
    )
    np.fill_diagonal(training_distance_matrix, np.inf)
    training_leave_one_out_distance_array = np.min(
        training_distance_matrix,
        axis=1,
    )
    supported_distance_threshold = float(
        np.quantile(training_leave_one_out_distance_array, 0.95)
    )
    nearest_distance_array = compute_nearest_standardized_distance(
        forward_feature_matrix,
        training_feature_matrix,
        feature_scale,
    )
    inside_axis_box_mask = np.all(
        (forward_feature_matrix >= feature_minimum[np.newaxis, :])
        & (forward_feature_matrix <= feature_maximum[np.newaxis, :]),
        axis=1,
    )

    # Classify Every Eligible Forward Condition
    tier_count_by_split = {
        split_name: {
            "supported_core": 0,
            "supported_sparse_or_corner": 0,
            "unsupported_extrapolation": 0,
        }
        for split_name in ("train", "validation", "test")
    }
    condition_row_list: list[dict[str, Any]] = []
    finite_prediction_count = 0
    for record_index, record in enumerate(forward_record_list):
        predicted_curve = predict_curve(
            causal_surface,
            record,
            use_setpoints=True,
        )
        finite_prediction = bool(np.all(np.isfinite(predicted_curve)))
        finite_prediction_count += int(finite_prediction)
        nearest_distance = float(nearest_distance_array[record_index])
        if not bool(inside_axis_box_mask[record_index]):
            support_tier = "unsupported_extrapolation"
        elif nearest_distance <= supported_distance_threshold:
            support_tier = "supported_core"
        else:
            support_tier = "supported_sparse_or_corner"
        tier_count_by_split[record.split][support_tier] += 1
        operating_feature_array = forward_feature_matrix[record_index]
        condition_row_list.append(
            {
                "condition_id": record.condition_id,
                "split": record.split,
                "signed_setpoint_torque_nm": float(
                    operating_feature_array[0]
                ),
                "absolute_setpoint_speed_rpm": float(
                    operating_feature_array[1]
                ),
                "setpoint_temperature_deg_c": float(
                    operating_feature_array[2]
                ),
                "inside_training_axis_box": bool(
                    inside_axis_box_mask[record_index]
                ),
                "nearest_standardized_training_distance": (
                    nearest_distance
                ),
                "supported_distance_threshold": (
                    supported_distance_threshold
                ),
                "support_tier": support_tier,
                "prediction_finite": finite_prediction,
            }
        )

    # Stress Every Center, Face, Edge, And Corner Combination
    stress_level_matrix = np.column_stack(
        (
            feature_minimum,
            causal_surface.feature_mean,
            feature_maximum,
        )
    )
    envelope_grid_feature_matrix = np.vstack(
        [
            np.asarray(
                [
                    stress_level_matrix[feature_index, level_index]
                    for feature_index, level_index in enumerate(
                        level_index_tuple
                    )
                ],
                dtype=np.float64,
            )
            for level_index_tuple in product(range(3), repeat=3)
        ]
    )
    envelope_grid_coefficient_matrix = causal_surface.predict(
        envelope_grid_feature_matrix
    )
    assert np.all(np.isfinite(envelope_grid_coefficient_matrix))
    assert finite_prediction_count == len(forward_record_list)

    feature_name_list = [
        "signed_setpoint_torque_nm",
        "absolute_setpoint_speed_rpm",
        "setpoint_temperature_deg_c",
    ]
    envelope_payload = {
        "schema_version": 1,
        "dataset": "polished_dataset",
        "input_mode": "setpoints",
        "surface": "Fw",
        "fit_scope": "frozen training split only",
        "feature_order": feature_name_list,
        "axis_bound_dictionary": {
            feature_name: {
                "minimum": float(feature_minimum[feature_index]),
                "mean": float(
                    causal_surface.feature_mean[feature_index]
                ),
                "maximum": float(feature_maximum[feature_index]),
                "scale": float(feature_scale[feature_index]),
            }
            for feature_index, feature_name in enumerate(
                feature_name_list
            )
        },
        "supported_distance_threshold": supported_distance_threshold,
        "supported_distance_derivation": (
            "training-only P95 leave-one-out nearest standardized distance"
        ),
        "tier_definition_dictionary": {
            "supported_core": (
                "inside every training setpoint-axis bound and no farther "
                "than the train-only density threshold"
            ),
            "supported_sparse_or_corner": (
                "inside every setpoint-axis bound but farther than the "
                "train-only density threshold"
            ),
            "unsupported_extrapolation": (
                "outside at least one training setpoint-axis bound"
            ),
        },
        "tier_count_by_split": tier_count_by_split,
        "eligible_forward_condition_count": len(forward_record_list),
        "finite_prediction_count": finite_prediction_count,
        "envelope_grid_point_count": int(
            envelope_grid_feature_matrix.shape[0]
        ),
        "envelope_grid_finite": True,
        "deployment_rule": (
            "Use the causal PF-A anchor as qualified only in supported_core. "
            "Treat supported_sparse_or_corner as low-trust and route "
            "unsupported_extrapolation to fallback or review."
        ),
    }
    write_csv(CONDITION_PATH, condition_row_list)
    write_yaml(ENVELOPE_PATH, envelope_payload)
    print(yaml.safe_dump(envelope_payload, sort_keys=False))


if __name__ == "__main__":
    main()
