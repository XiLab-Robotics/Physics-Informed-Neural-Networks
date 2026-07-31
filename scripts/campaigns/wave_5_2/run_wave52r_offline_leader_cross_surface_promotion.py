"""Prepare and run the K01/H08 cross-surface promotion campaign."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from dataclasses import replace
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
import torch
import yaml

# Import Repository Models And Campaign Utilities
from scripts.analysis.polynomial_fourier_benchmark.polynomial_fourier_models import (
    fit_quadratic_coefficient_surface,
)
from scripts.analysis.polynomial_fourier_benchmark.polynomial_fourier_models import (
    project_fourier_coefficients,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage9_temporal_analytical_residual_models as stage9,
)


# Define The Approved Campaign Contract
CAMPAIGN_NAME = (
    "wave52r_offline_leader_cross_surface_promotion_2026_07_30"
)
CAMPAIGN_CONFIGURATION_PATH = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "wave52r_offline_leader_cross_surface_promotion"
    / "campaigns"
    / "2026-07-30_wave52r_offline_leader_cross_surface_promotion"
    / "campaign.yaml"
)
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)
LOCAL_GATE_SUMMARY_PATH = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "wave52r_offline_leader_promotion"
    / "2026-07-30-19-24-35__wave52r_offline_leader_promotion"
    / "promotion_gate_summary.yaml"
)
PREFLIGHT_OUTPUT_PATH = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "wave52r_offline_leader_cross_surface_promotion"
    / "campaign_preflight_summary.yaml"
)
CAMPAIGN_OUTPUT_ROOT = PROJECT_ROOT / "output" / "training_campaigns"
SURFACE_LIST = ["Fw", "Bw", "global"]
RANDOM_SEED_LIST = [314159, 271828, 161803]
EXPECTED_PROMOTION_RUN_COUNT = 18
EXPECTED_INTERNAL_ANCHOR_RUN_COUNT = 9
EXPECTED_TOTAL_RUN_COUNT = (
    EXPECTED_PROMOTION_RUN_COUNT + EXPECTED_INTERNAL_ANCHOR_RUN_COUNT
)
DIRECTION_FLAG_MAP = {
    "Fw": 1.0,
    "Bw": -1.0,
}


def now_timestamp() -> str:
    """Return one sortable local timestamp."""

    return datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")


def now_iso() -> str:
    """Return one timezone-aware local timestamp."""

    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_yaml(input_path: Path) -> dict[str, Any]:
    """Read one YAML mapping."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def write_yaml(output_path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def write_csv(
    output_path: Path,
    row_list: list[dict[str, Any]],
) -> None:
    """Write one stable CSV table."""

    assert row_list
    field_name_list = []
    for row in row_list:
        for field_name in row:
            if field_name not in field_name_list:
                field_name_list.append(field_name)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)


def compute_file_sha256(input_path: Path) -> str:
    """Return the lowercase SHA-256 digest for one file."""

    sha256_digest = hashlib.sha256()
    with input_path.open("rb") as input_file:
        while byte_chunk := input_file.read(1024 * 1024):
            sha256_digest.update(byte_chunk)
    return sha256_digest.hexdigest()


def surface_record_list(
    all_record_list: list[Any],
    surface_name: str,
) -> list[Any]:
    """Return the eligible records for one declared campaign surface."""

    excluded_condition_id_set = set(stage5.EXCLUDED_CONDITION_ID_LIST)
    eligible_record_list = [
        record
        for record in all_record_list
        if record.condition_id not in excluded_condition_id_set
    ]
    if surface_name == "global":
        result_record_list = eligible_record_list
    else:
        result_record_list = [
            record
            for record in eligible_record_list
            if record.direction == surface_name
        ]
    expected_count = 1932 if surface_name == "global" else 966
    assert len(result_record_list) == expected_count
    return result_record_list


def directional_setpoint_feature_array(record: Any) -> np.ndarray:
    """Return direction-aware causal setpoints for analytical anchors."""

    torque_sign = -1.0 if record.direction == "Fw" else 1.0
    return np.asarray(
        [
            torque_sign * abs(float(record.nominal_torque_nm)),
            abs(float(record.nominal_speed_rpm)),
            float(record.nominal_temperature_deg_c),
        ],
        dtype=np.float64,
    )


def model_condition_feature_array(
    record: Any,
    surface_name: str,
) -> np.ndarray:
    """Return the directional or explicit-global model feature vector."""

    base_feature_array = directional_setpoint_feature_array(record)
    if surface_name != "global":
        return base_feature_array
    return np.concatenate(
        [
            base_feature_array,
            np.asarray(
                [DIRECTION_FLAG_MAP[record.direction]],
                dtype=np.float64,
            ),
        ]
    )


def select_training_only_order_list(
    training_curve_matrix: np.ndarray,
    training_anchor_curve_matrix: np.ndarray,
) -> list[int]:
    """Select the Stage 5 residual harmonics without writing legacy outputs."""

    residual_matrix = (
        training_curve_matrix - training_anchor_curve_matrix
    )
    spectrum_matrix = np.fft.rfft(residual_matrix, axis=1)
    amplitude_matrix = (
        2.0 * np.abs(spectrum_matrix) / residual_matrix.shape[1]
    )
    mean_amplitude = np.mean(amplitude_matrix, axis=0)
    candidate_order_list = [
        order
        for order in range(1, min(241, amplitude_matrix.shape[1]))
        if order not in set(stage5.CORE_ORDER_LIST)
    ]
    ranked_order_list = sorted(
        candidate_order_list,
        key=lambda order: (-mean_amplitude[order], order),
    )
    return sorted(
        set(stage5.CORE_ORDER_LIST + ranked_order_list[:8])
    )


def build_surface_dataset(
    all_record_list: list[Any],
    surface_name: str,
) -> tuple[stage5.Stage5Dataset, dict[str, Any]]:
    """Build one leakage-safe Fw, Bw, or global promotion dataset."""

    record_list = surface_record_list(all_record_list, surface_name)
    condition_matrix = np.vstack(
        [
            model_condition_feature_array(record, surface_name)
            for record in record_list
        ]
    )
    anchor_feature_matrix = np.vstack(
        [
            directional_setpoint_feature_array(record)
            for record in record_list
        ]
    )
    curve_matrix = np.vstack(
        [record.te_deg for record in record_list]
    )
    split_array = np.asarray(
        [record.split for record in record_list]
    )
    direction_array = np.asarray(
        [record.direction for record in record_list]
    )
    training_mask = split_array == "train"
    assert int(np.sum(split_array == "train")) == (
        1350 if surface_name == "global" else 675
    )
    assert int(np.sum(split_array == "validation")) == (
        388 if surface_name == "global" else 194
    )
    assert int(np.sum(split_array == "test")) == (
        194 if surface_name == "global" else 97
    )

    # Fit Separate Training-Only PF-A Anchors For Each Direction
    core_anchor_coefficient_matrix = np.zeros(
        (
            len(record_list),
            1 + (2 * len(stage5.CORE_ORDER_LIST)),
        ),
        dtype=np.float64,
    )
    anchor_surface_digest_dictionary = {}
    for direction_name in ("Fw", "Bw"):
        direction_mask = direction_array == direction_name
        if not np.any(direction_mask):
            continue
        direction_training_mask = training_mask & direction_mask
        target_coefficient_matrix = np.vstack(
            [
                project_fourier_coefficients(
                    curve,
                    stage5.CORE_ORDER_LIST,
                )
                for curve in curve_matrix[direction_training_mask]
            ]
        )
        fitted_surface = fit_quadratic_coefficient_surface(
            anchor_feature_matrix[direction_training_mask],
            target_coefficient_matrix,
            stage5.CORE_ORDER_LIST,
        )
        core_anchor_coefficient_matrix[direction_mask] = (
            fitted_surface.predict(
                anchor_feature_matrix[direction_mask]
            )
        )
        surface_digest_payload = np.concatenate(
            [
                fitted_surface.feature_mean.ravel(),
                fitted_surface.feature_scale.ravel(),
                fitted_surface.coefficient_matrix.ravel(),
            ]
        )
        anchor_surface_digest_dictionary[direction_name] = (
            hashlib.sha256(
                np.asarray(
                    surface_digest_payload,
                    dtype="<f8",
                ).tobytes()
            ).hexdigest()
        )

    core_anchor_curve_matrix = np.vstack(
        [
            stage5._reconstruct_numpy_curve(
                coefficient_array,
                stage5.CORE_ORDER_LIST,
            )
            for coefficient_array in core_anchor_coefficient_matrix
        ]
    )
    data_selected_order_list = select_training_only_order_list(
        curve_matrix[training_mask],
        core_anchor_curve_matrix[training_mask],
    )
    order_set_map = {
        "core": list(stage5.CORE_ORDER_LIST),
        "core_plus_residual": list(
            stage5.CORE_PLUS_RESIDUAL_ORDER_LIST
        ),
        "data_selected": data_selected_order_list,
    }

    # Project Targets And Training-Only Scales For Every Order Set
    anchor_coefficient_map: dict[str, np.ndarray] = {}
    target_coefficient_map: dict[str, np.ndarray] = {}
    coefficient_scale_map: dict[str, np.ndarray] = {}
    correction_bound_map: dict[str, np.ndarray] = {}
    for order_set_name, order_list in order_set_map.items():
        anchor_matrix = stage5.map_anchor_coefficients(
            core_anchor_coefficient_matrix,
            order_list,
        )
        target_matrix = np.vstack(
            [
                project_fourier_coefficients(curve, order_list)
                for curve in curve_matrix
            ]
        )
        training_target_matrix = target_matrix[training_mask]
        training_correction_matrix = (
            target_matrix[training_mask]
            - anchor_matrix[training_mask]
        )
        coefficient_scale_map[order_set_name] = np.maximum(
            np.std(training_target_matrix, axis=0),
            1.0e-5,
        )
        correction_bound_map[order_set_name] = np.maximum(
            np.quantile(
                np.abs(training_correction_matrix),
                0.995,
                axis=0,
            ),
            1.0e-5,
        )
        anchor_coefficient_map[order_set_name] = anchor_matrix
        target_coefficient_map[order_set_name] = target_matrix

    feature_mean = np.mean(
        condition_matrix[training_mask],
        axis=0,
    )
    feature_scale = np.std(
        condition_matrix[training_mask],
        axis=0,
    )
    assert np.all(feature_scale > 0.0)
    curve_scale = float(
        np.std(curve_matrix[training_mask])
    )
    assert curve_scale > 0.0
    condition_id_list = [
        (
            f"{record.condition_id}__{record.direction}"
            if surface_name == "global"
            else record.condition_id
        )
        for record in record_list
    ]
    dataset = stage5.Stage5Dataset(
        condition_matrix=condition_matrix,
        curve_matrix=curve_matrix,
        split_array=split_array,
        condition_id_list=condition_id_list,
        anchor_coefficient_map=anchor_coefficient_map,
        target_coefficient_map=target_coefficient_map,
        order_set_map=order_set_map,
        feature_mean=feature_mean,
        feature_scale=feature_scale,
        curve_scale=curve_scale,
        coefficient_scale_map=coefficient_scale_map,
        correction_bound_map=correction_bound_map,
    )
    dataset_contract = {
        "surface": surface_name,
        "condition_feature_order": (
            [
                "signed_setpoint_torque_nm",
                "absolute_setpoint_speed_rpm",
                "setpoint_temperature_deg_c",
                "direction_flag",
            ]
            if surface_name == "global"
            else [
                "signed_setpoint_torque_nm",
                "absolute_setpoint_speed_rpm",
                "setpoint_temperature_deg_c",
            ]
        ),
        "curve_count": len(record_list),
        "curve_count_by_split": {
            split_name: int(np.sum(split_array == split_name))
            for split_name in ("train", "validation", "test")
        },
        "direction_count": {
            direction_name: int(
                np.sum(direction_array == direction_name)
            )
            for direction_name in ("Fw", "Bw")
        },
        "data_selected_order_list": data_selected_order_list,
        "anchor_surface_sha256_by_direction": (
            anchor_surface_digest_dictionary
        ),
        "split_signature": stage5.SPLIT_SIGNATURE,
        "target_derived_runtime_input_count": 0,
    }
    return dataset, dataset_contract


def build_h04_anchor_bundle(
    dataset: stage5.Stage5Dataset,
    h04_checkpoint_path: Path,
) -> stage9.AnchorBundle:
    """Build the K01 anchor bundle from one newly trained H04."""

    h04_specification = next(
        candidate
        for candidate in stage5.build_candidate_list()
        if candidate.candidate_id == "H04"
    )
    h04_model = stage5.build_model(
        h04_specification,
        dataset,
    )
    checkpoint_payload = torch.load(
        h04_checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
    h04_model.load_state_dict(
        checkpoint_payload["state_dict"],
        strict=True,
    )
    h04_model.eval()
    normalized_condition_tensor = torch.as_tensor(
        (
            dataset.condition_matrix - dataset.feature_mean
        )
        / dataset.feature_scale,
        dtype=torch.float32,
    )
    pf_a_coefficient_tensor = torch.as_tensor(
        dataset.anchor_coefficient_map["core"],
        dtype=torch.float32,
    )
    with torch.inference_mode():
        h04_output = h04_model(
            normalized_condition_tensor,
            pf_a_coefficient_tensor,
        )
    h04_curve_matrix = (
        h04_output["prediction_curve"].numpy().astype(np.float64)
    )
    h04_coefficient_matrix = (
        h04_output["prediction_coefficients"]
        .numpy()
        .astype(np.float64)
    )
    pf_a_curve_matrix = np.vstack(
        [
            stage5._reconstruct_numpy_curve(
                coefficient_array,
                stage5.CORE_ORDER_LIST,
            )
            for coefficient_array in dataset.anchor_coefficient_map[
                "core"
            ]
        ]
    )
    return stage9.AnchorBundle(
        pf_a_curve_matrix=pf_a_curve_matrix,
        pf_a_coefficient_matrix=dataset.anchor_coefficient_map[
            "core"
        ],
        h04_curve_matrix=h04_curve_matrix,
        h04_coefficient_matrix=h04_coefficient_matrix,
        h04_mean_curve_matrix=np.repeat(
            h04_coefficient_matrix[:, :1],
            stage5.ANGULAR_SAMPLE_COUNT,
            axis=1,
        ),
    )


def annotate_run_artifacts(
    result_payload: dict[str, Any],
    surface_name: str,
    model_role: str,
    random_seed: int,
) -> Path:
    """Add campaign and surface metadata to one new immutable run."""

    checkpoint_path_text = result_payload.get("checkpoint_path")
    if checkpoint_path_text:
        checkpoint_path = PROJECT_ROOT / checkpoint_path_text
        run_directory = checkpoint_path.parent
    else:
        run_directory = (
            PROJECT_ROOT / result_payload["run_directory"]
        )
        checkpoint_path = run_directory / "best_model.pt"
    checkpoint_payload = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
    checkpoint_payload.update(
        {
            "campaign_name": CAMPAIGN_NAME,
            "dataset_id": "polished_dataset",
            "input_mode": "setpoints",
            "surface": surface_name,
            "model_role": model_role,
            "random_seed": random_seed,
            "split_signature": stage5.SPLIT_SIGNATURE,
        }
    )
    torch.save(checkpoint_payload, checkpoint_path)

    metadata_path = run_directory / "promotion_metadata.yaml"
    write_yaml(
        metadata_path,
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "dataset_id": "polished_dataset",
            "input_mode": "setpoints",
            "surface": surface_name,
            "model_role": model_role,
            "random_seed": random_seed,
            "split_signature": stage5.SPLIT_SIGNATURE,
            "checkpoint_path": checkpoint_path.relative_to(
                PROJECT_ROOT
            ).as_posix(),
            "checkpoint_sha256": compute_file_sha256(
                checkpoint_path
            ),
        },
    )
    return run_directory


def campaign_active_state(
    status: str,
    campaign_output_directory: Path | None = None,
    completed_run_count: int = 0,
    failed_run_count: int = 0,
) -> dict[str, Any]:
    """Build the persistent active-campaign state."""

    configuration = read_yaml(CAMPAIGN_CONFIGURATION_PATH)
    state_payload = {
        "status": status,
        "prepared_at": configuration["prepared_at"],
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": (
            "wave52r_offline_leader_cross_surface_promotion"
        ),
        "dataset_id": "polished_dataset",
        "input_mode": "setpoints",
        "surface_list": ["fw", "bw", "global"],
        "primary_surface": "global",
        "expected_run_count": EXPECTED_TOTAL_RUN_COUNT,
        "promotion_candidate_run_count": (
            EXPECTED_PROMOTION_RUN_COUNT
        ),
        "internal_anchor_run_count": (
            EXPECTED_INTERNAL_ANCHOR_RUN_COUNT
        ),
        "completed_run_count": completed_run_count,
        "failed_run_count": failed_run_count,
        "random_seed_list": RANDOM_SEED_LIST,
        "campaign_manifest_path": (
            CAMPAIGN_CONFIGURATION_PATH.relative_to(
                PROJECT_ROOT
            ).as_posix()
        ),
        "launcher_path": (
            "scripts/campaigns/wave_5_2/"
            "run_wave52r_offline_leader_cross_surface_promotion.ps1"
        ),
        "launcher_note_path": (
            "doc/scripts/campaigns/wave_5_2/"
            "run_wave52r_offline_leader_cross_surface_promotion.md"
        ),
        "planning_report_path": configuration[
            "planning_report_path"
        ],
        "technical_document_path": configuration[
            "technical_document_path"
        ],
        "local_preflight_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_offline_leader_cross_surface_promotion.ps1 "
            "-PreflightOnly"
        ),
        "local_launch_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_offline_leader_cross_surface_promotion.ps1 "
            "-Run"
        ),
        "remote_preflight_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_offline_leader_cross_surface_promotion.ps1 "
            "-Remote -PreflightOnly"
        ),
        "remote_launch_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_offline_leader_cross_surface_promotion.ps1 "
            "-Remote -Run"
        ),
        "approval": {
            "technical_document_status": "approved",
            "campaign_plan_status": "approved",
            "approval_source": "explicit user approval",
            "approval_recorded_at": configuration[
                "approval_recorded_at"
            ],
        },
        "protected_file_list": configuration[
            "protected_file_list"
        ],
        "incumbent_preservation": {
            "periodic_gru_sequence": "frozen_control",
            "periodic_mlp_harmonic": "frozen_control",
            "automatic_replacement_allowed": False,
        },
    }
    if campaign_output_directory is not None:
        state_payload["campaign_output_directory"] = (
            campaign_output_directory.relative_to(
                PROJECT_ROOT
            ).as_posix()
        )
    return state_payload


def run_preflight() -> dict[str, Any]:
    """Validate the complete approved cross-surface package."""

    assert CAMPAIGN_CONFIGURATION_PATH.exists()
    local_gate_summary = read_yaml(LOCAL_GATE_SUMMARY_PATH)
    assert (
        local_gate_summary["overall_status"]
        == "qualified_for_conditional_cross_surface_campaign"
    )
    phase1_configuration = stage5.load_yaml(
        stage5.PHASE1_CONFIGURATION_PATH
    )
    common_split_manifest = stage5.load_yaml(
        stage5.COMMON_SPLIT_MANIFEST_PATH
    )
    all_record_list = stage5.load_curve_records(
        phase1_configuration,
        common_split_manifest,
    )
    dataset_contract_dictionary = {}
    for surface_name in SURFACE_LIST:
        dataset, dataset_contract = build_surface_dataset(
            all_record_list,
            surface_name,
        )
        h08_specification = next(
            candidate
            for candidate in stage5.build_candidate_list()
            if candidate.candidate_id == "H08"
        )
        k01_specification = next(
            candidate
            for candidate in stage9.build_candidate_list()
            if candidate.candidate_id == "K01"
        )
        h08_model = stage5.build_model(
            h08_specification,
            dataset,
        )
        k01_model = stage9.build_model(
            k01_specification,
            dataset,
        )
        assert sum(
            parameter.numel()
            for parameter in h08_model.parameters()
        ) > 0
        assert sum(
            parameter.numel()
            for parameter in k01_model.parameters()
        ) > 0
        dataset_contract_dictionary[surface_name] = (
            dataset_contract
        )
    preflight_payload = {
        "schema_version": 1,
        "generated_at": now_iso(),
        "status": "passed",
        "campaign_name": CAMPAIGN_NAME,
        "local_gate_summary_path": (
            LOCAL_GATE_SUMMARY_PATH.relative_to(
                PROJECT_ROOT
            ).as_posix()
        ),
        "local_gate_summary_sha256": compute_file_sha256(
            LOCAL_GATE_SUMMARY_PATH
        ),
        "surface_list": SURFACE_LIST,
        "random_seed_list": RANDOM_SEED_LIST,
        "expected_total_run_count": EXPECTED_TOTAL_RUN_COUNT,
        "expected_promotion_run_count": (
            EXPECTED_PROMOTION_RUN_COUNT
        ),
        "expected_internal_anchor_run_count": (
            EXPECTED_INTERNAL_ANCHOR_RUN_COUNT
        ),
        "dataset_contract_dictionary": (
            dataset_contract_dictionary
        ),
        "incumbent_artifact_mutation_allowed": False,
        "training_execution_started": False,
    }
    write_yaml(PREFLIGHT_OUTPUT_PATH, preflight_payload)
    print(
        "[PASS] Cross-surface promotion campaign preflight | "
        f"surfaces={len(SURFACE_LIST)} | "
        f"seeds={len(RANDOM_SEED_LIST)} | "
        f"runs={EXPECTED_TOTAL_RUN_COUNT}",
        flush=True,
    )
    return preflight_payload


def run_campaign() -> Path:
    """Execute all approved surface, seed, and candidate cells."""

    preflight_payload = run_preflight()
    assert preflight_payload["status"] == "passed"
    phase1_configuration = stage5.load_yaml(
        stage5.PHASE1_CONFIGURATION_PATH
    )
    common_split_manifest = stage5.load_yaml(
        stage5.COMMON_SPLIT_MANIFEST_PATH
    )
    all_record_list = stage5.load_curve_records(
        phase1_configuration,
        common_split_manifest,
    )
    dataset_dictionary = {
        surface_name: build_surface_dataset(
            all_record_list,
            surface_name,
        )
        for surface_name in SURFACE_LIST
    }

    campaign_run_instance_id = (
        f"{now_timestamp()}_{CAMPAIGN_NAME}"
    )
    campaign_output_directory = (
        CAMPAIGN_OUTPUT_ROOT / campaign_run_instance_id
    )
    campaign_output_directory.mkdir(
        parents=True,
        exist_ok=False,
    )
    write_yaml(
        ACTIVE_CAMPAIGN_PATH,
        {
            **campaign_active_state(
                "running",
                campaign_output_directory,
            ),
            "started_at": now_iso(),
        },
    )

    # Train The Internal H04 Anchor And Both Promotion Candidates
    result_row_list = []
    artifact_path_list = []
    queue_index = 0
    for surface_name in SURFACE_LIST:
        dataset, dataset_contract = dataset_dictionary[surface_name]
        write_yaml(
            campaign_output_directory
            / "dataset_contracts"
            / f"{surface_name.lower()}_dataset_contract.yaml",
            dataset_contract,
        )
        for random_seed in RANDOM_SEED_LIST:
            queue_index += 1
            h04_specification = replace(
                next(
                    candidate
                    for candidate in stage5.build_candidate_list()
                    if candidate.candidate_id == "H04"
                ),
                queue_index=(queue_index * 10) + 1,
            )
            h08_specification = replace(
                next(
                    candidate
                    for candidate in stage5.build_candidate_list()
                    if candidate.candidate_id == "H08"
                ),
                queue_index=(queue_index * 10) + 2,
            )
            k01_specification = replace(
                next(
                    candidate
                    for candidate in stage9.build_candidate_list()
                    if candidate.candidate_id == "K01"
                ),
                queue_index=(queue_index * 10) + 3,
            )

            h04_result = stage5.train_candidate(
                h04_specification,
                dataset,
                campaign_output_directory,
                random_seed,
            )
            h04_run_directory = annotate_run_artifacts(
                h04_result,
                surface_name,
                "internal_h04_anchor",
                random_seed,
            )
            h04_checkpoint_path = (
                h04_run_directory / "best_model.pt"
            )
            artifact_path_list.append(
                h04_run_directory.relative_to(
                    PROJECT_ROOT
                ).as_posix()
            )
            result_row_list.append(
                {
                    **h04_result,
                    "surface": surface_name,
                    "model_role": "internal_h04_anchor",
                }
            )

            h08_result = stage5.train_candidate(
                h08_specification,
                dataset,
                campaign_output_directory,
                random_seed,
            )
            h08_run_directory = annotate_run_artifacts(
                h08_result,
                surface_name,
                "promotion_candidate",
                random_seed,
            )
            artifact_path_list.append(
                h08_run_directory.relative_to(
                    PROJECT_ROOT
                ).as_posix()
            )
            result_row_list.append(
                {
                    **h08_result,
                    "surface": surface_name,
                    "model_role": "promotion_candidate",
                }
            )

            anchor_bundle = build_h04_anchor_bundle(
                dataset,
                h04_checkpoint_path,
            )
            k01_result = stage9.train_candidate(
                k01_specification,
                dataset,
                anchor_bundle,
                campaign_output_directory,
                random_seed,
            )
            k01_run_directory = annotate_run_artifacts(
                k01_result,
                surface_name,
                "promotion_candidate",
                random_seed,
            )
            artifact_path_list.append(
                k01_run_directory.relative_to(
                    PROJECT_ROOT
                ).as_posix()
            )
            result_row_list.append(
                {
                    **k01_result,
                    "status": "completed",
                    "surface": surface_name,
                    "model_role": "promotion_candidate",
                    "run_directory": (
                        k01_run_directory.relative_to(
                            PROJECT_ROOT
                        ).as_posix()
                    ),
                }
            )
            write_yaml(
                campaign_output_directory
                / "queue_state"
                / f"{queue_index:03d}_{surface_name.lower()}_"
                f"seed_{random_seed}.yaml",
                {
                    "status": "completed",
                    "surface": surface_name,
                    "random_seed": random_seed,
                    "h04_run_instance_id": h04_result[
                        "run_instance_id"
                    ],
                    "h08_run_instance_id": h08_result[
                        "run_instance_id"
                    ],
                    "k01_run_instance_id": k01_result[
                        "run_instance_id"
                    ],
                },
            )

    assert len(result_row_list) == EXPECTED_TOTAL_RUN_COUNT
    promotion_result_list = [
        result
        for result in result_row_list
        if result["model_role"] == "promotion_candidate"
    ]
    assert (
        len(promotion_result_list)
        == EXPECTED_PROMOTION_RUN_COUNT
    )
    promotion_result_list.sort(
        key=lambda result: (
            float(
                result.get(
                    "validation_curve_mae_deg",
                    result.get(
                        "best_validation_mae_deg",
                        float("inf"),
                    ),
                )
            ),
            result["candidate_id"],
            result["surface"],
            result["random_seed"],
        )
    )
    overall_best_result = promotion_result_list[0]

    # Persist Winner, Leaderboard, And Recoverable Artifact Inventory
    write_yaml(
        campaign_output_directory / "campaign_leaderboard.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "selection_scope": (
                "validation-only scalar ordering before official "
                "multi-index TE Curve Verification Pipeline"
            ),
            "result_list": promotion_result_list,
        },
    )
    write_yaml(
        campaign_output_directory / "campaign_best_run.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "status": "provisional_validation_winner",
            "best_run": overall_best_result,
            "promotion_authorized": False,
            "required_next_step": (
                "normal closeout followed by separate global/Fw/Bw "
                "TE Curve Verification Pipeline"
            ),
        },
    )
    best_run_markdown = f"""# Campaign Best Run

- Campaign: `{CAMPAIGN_NAME}`
- Provisional validation winner: `{overall_best_result["candidate_id"]}`
- Surface: `{overall_best_result["surface"]}`
- Random seed: `{overall_best_result["random_seed"]}`
- Run instance: `{overall_best_result["run_instance_id"]}`

This scalar validation winner does not replace the periodic GRU or periodic
harmonic MLP and does not authorize global promotion. The official decision
requires direction-separated curve-first verification.
"""
    with (
        campaign_output_directory / "campaign_best_run.md"
    ).open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(best_run_markdown)
    write_csv(
        campaign_output_directory / "campaign_results.csv",
        result_row_list,
    )
    artifact_inventory_path = (
        campaign_output_directory
        / "campaign_artifact_path_list.txt"
    )
    with artifact_inventory_path.open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as output_file:
        for artifact_path in sorted(set(artifact_path_list)):
            output_file.write(artifact_path + "\n")

    completed_state = {
        **campaign_active_state(
            "completed",
            campaign_output_directory,
            completed_run_count=EXPECTED_TOTAL_RUN_COUNT,
        ),
        "started_at": read_yaml(ACTIVE_CAMPAIGN_PATH)[
            "started_at"
        ],
        "completed_at": now_iso(),
        "campaign_best_run_path": (
            campaign_output_directory
            / "campaign_best_run.yaml"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "qualified_real_data_winner_id": None,
        "official_curve_verification_status": "pending",
    }
    write_yaml(
        campaign_output_directory / "campaign_state.yaml",
        completed_state,
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, completed_state)
    print(
        "[DONE] Cross-surface promotion campaign completed | "
        f"runs={len(result_row_list)} | "
        f"output={campaign_output_directory.relative_to(PROJECT_ROOT).as_posix()}",
        flush=True,
    )
    return campaign_output_directory


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description=(
            "Preflight or run the approved K01/H08 Fw/Bw/global "
            "promotion campaign."
        )
    )
    parser.add_argument(
        "--preflight-only",
        action="store_true",
    )
    parser.add_argument(
        "--run",
        action="store_true",
    )
    return parser.parse_args()


def main() -> None:
    """Run preflight by default or execute the approved campaign."""

    arguments = parse_arguments()
    if arguments.run:
        run_campaign()
        return
    run_preflight()


if __name__ == "__main__":
    main()
