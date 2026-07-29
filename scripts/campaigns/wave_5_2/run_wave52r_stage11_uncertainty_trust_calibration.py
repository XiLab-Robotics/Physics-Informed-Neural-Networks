"""Run Wave 5.2R Stage 11 uncertainty and physics-trust calibration."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import shutil
import sys
import time
from typing import Any

# Import Numerical And Serialization Utilities
import numpy as np
import torch
import yaml

# Make Direct Script Execution Resolve The Repository Package
PROJECT_IMPORT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_IMPORT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_IMPORT_ROOT))

# Import Stage 11 Trust Components
from scripts.models.sparse_harmonic_condition_model import (
    SparseHarmonicConditionModel,
    build_named_condition_term_list,
)
from scripts.models.uncertainty_physics_trust_calibrator import (
    CompositeTrustState,
    IsotonicCalibrationState,
    apply_composite_trust_estimator,
    apply_isotonic_error_calibrator,
    calculate_curve_disagreement,
    calculate_curve_error,
    calculate_ensemble_spread,
    calculate_nearest_training_distance,
    calculate_support_boundary_score,
    evaluate_conformal_intervals,
    evaluate_group_metrics,
    evaluate_localization_metrics,
    fit_composite_trust_estimator,
    fit_conformal_quantiles,
    fit_isotonic_error_calibrator,
    serialize_composite_state,
    serialize_isotonic_state,
)

# Import Prior Wave 5.2R Campaign Utilities
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage9_temporal_analytical_residual_models as stage9,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage10_sparse_symbolic_discovery as stage10,
)


# Define Campaign Constants
PROJECT_ROOT = Path(__file__).resolve().parents[3]
STAGE_NAME = "wave52r_stage11_uncertainty_trust_calibration"
CAMPAIGN_NAME = f"{STAGE_NAME}_2026_07_29"
SPLIT_SIGNATURE = stage5.SPLIT_SIGNATURE
PRIMARY_SEED = 314159
ENSEMBLE_SEED_LIST = [314159, 271828, 161803, 141421, 173205]
SUPPORT_DENSITY_THRESHOLD = 0.303207
CONFIG_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "uncertainty_physics_trust_calibration"
    / "campaigns"
    / "2026-07-29_wave52r_stage11_uncertainty_trust_calibration"
)
QUEUE_DIRECTORY = CONFIG_DIRECTORY / "queue"
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage11_uncertainty_physics_trust_calibration"
)
RUN_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "uncertainty_physics_trust_calibration"
)
CAMPAIGN_ROOT_DIRECTORY = PROJECT_ROOT / "output" / "training_campaigns"
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)
PRIMARY_K01_CHECKPOINT_PATH = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "temporal_analytical_residual_models"
    / "2026-07-29-19-21-15__stage9_k01"
    / "best_model.pt"
)
STAGE10_R00_PARAMETER_PATH = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "sparse_symbolic_formulation_discovery"
    / "2026-07-29-20-21-50__stage10_r00"
    / "model_parameters.npz"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-29/"
    "2026-07-29-20-33-38_wave52r_stage11_uncertainty_and_"
    "physics_trust_calibration.md"
)
CAMPAIGN_PLAN_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "uncertainty_physics_trust_calibration/"
    "2026-07-29-20-33-38_wave52r_stage11_uncertainty_and_"
    "physics_trust_calibration_campaign_plan_report.md"
)
LAUNCHER_PATH = (
    "scripts/campaigns/wave_5_2/"
    "run_wave52r_stage11_uncertainty_trust_calibration.ps1"
)
LAUNCHER_NOTE_PATH = (
    "doc/scripts/campaigns/wave_5_2/"
    "run_wave52r_stage11_uncertainty_trust_calibration.md"
)


@dataclass(frozen=True)
class CandidateSpecification:
    """Describe one immutable Stage 11 trust candidate."""

    queue_index: int
    candidate_id: str
    formulation: str
    diagnostic_control: bool = False
    ensemble_checkpoint_count: int = 1


@dataclass
class FrozenPredictionBundle:
    """Hold aligned full-dataset frozen predictions."""

    pf_a_curve_matrix: np.ndarray
    h04_curve_matrix: np.ndarray
    k01_curve_matrix: np.ndarray
    dense_r00_curve_matrix: np.ndarray
    k01_ensemble_prediction_tensor: np.ndarray
    ensemble_checkpoint_path_list: list[str]


def now_timestamp() -> str:
    """Return one sortable local timestamp."""

    return datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")


def now_iso() -> str:
    """Return one timezone-aware local timestamp."""

    return datetime.now().astimezone().isoformat(timespec="seconds")


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


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


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


def build_candidate_list() -> list[CandidateSpecification]:
    """Return the approved ten-entry Stage 11 matrix."""

    return [
        CandidateSpecification(
            1,
            "C00",
            "constant_conformal_control",
            diagnostic_control=True,
        ),
        CandidateSpecification(2, "S01", "condition_distance"),
        CandidateSpecification(3, "S02", "support_boundary_score"),
        CandidateSpecification(4, "A01", "pf_a_h04_disagreement"),
        CandidateSpecification(5, "A02", "h04_k01_disagreement"),
        CandidateSpecification(6, "A03", "pf_a_k01_disagreement"),
        CandidateSpecification(7, "D01", "dense_r00_k01_disagreement"),
        CandidateSpecification(
            8,
            "E01",
            "k01_five_seed_ensemble_spread",
            ensemble_checkpoint_count=5,
        ),
        CandidateSpecification(9, "M01", "composite_trust_estimator"),
        CandidateSpecification(
            10,
            "N01",
            "shuffled_composite_control",
            diagnostic_control=True,
        ),
    ]


def find_k01_specification() -> stage9.CandidateSpecification:
    """Resolve the frozen Stage 9 K01 candidate specification."""

    matching_list = [
        specification
        for specification in stage9.build_candidate_list()
        if specification.candidate_id == "K01"
    ]
    assert len(matching_list) == 1
    return matching_list[0]


def predict_checkpoint_all_curves(
    checkpoint_path: Path,
    dataset: stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
) -> np.ndarray:
    """Replay one K01 checkpoint on every frozen split."""

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    specification = find_k01_specification()
    model = stage9.build_model(specification, dataset).to(device)
    checkpoint_payload = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
    assert checkpoint_payload["split_signature"] == SPLIT_SIGNATURE
    model.load_state_dict(checkpoint_payload["state_dict"])
    prediction_by_split: dict[str, np.ndarray] = {}
    for split_name in ("train", "validation", "test"):
        batch = stage9.build_split_tensors(
            dataset,
            anchor_bundle.h04_curve_matrix,
            anchor_bundle.h04_coefficient_matrix,
            split_name,
            device,
        )
        prediction, _, _ = stage9.predict_model(
            model,
            torch.as_tensor(batch["condition"]),
            torch.as_tensor(batch["anchor"]),
            torch.as_tensor(batch["anchor_coefficient"]),
            torch.as_tensor(batch["angle"]),
            chunk_length=stage9.DEFAULT_CHUNK_LENGTH,
        )
        prediction_by_split[split_name] = prediction.astype(np.float64)
    aligned_prediction = np.empty_like(
        dataset.curve_matrix,
        dtype=np.float64,
    )
    for split_name, prediction in prediction_by_split.items():
        aligned_prediction[dataset.split_array == split_name] = prediction
    assert np.all(np.isfinite(aligned_prediction))
    return aligned_prediction


def build_dense_r00_predictions(
    dataset: stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
) -> np.ndarray:
    """Replay the Stage 10 dense R00 coefficient law on all conditions."""

    parameter_payload = np.load(STAGE10_R00_PARAMETER_PATH)
    model = SparseHarmonicConditionModel(
        term_list=build_named_condition_term_list("extended"),
        feature_mean=np.asarray(
            parameter_payload["feature_mean"],
            dtype=np.float64,
        ),
        feature_scale=np.asarray(
            parameter_payload["feature_scale"],
            dtype=np.float64,
        ),
        library_scale=np.asarray(
            parameter_payload["library_scale"],
            dtype=np.float64,
        ),
        target_scale=np.asarray(
            parameter_payload["target_scale"],
            dtype=np.float64,
        ),
        coefficient_matrix=np.asarray(
            parameter_payload["coefficient_matrix"],
            dtype=np.float64,
        ),
        harmonic_order_list=list(stage5.CORE_ORDER_LIST),
    )
    correction_coefficient_matrix = model.predict_coefficients(
        dataset.condition_matrix
    )
    prediction_coefficient_matrix = (
        anchor_bundle.pf_a_coefficient_matrix
        + correction_coefficient_matrix
    )
    prediction_curve_matrix = stage10.reconstruct_curve_matrix(
        prediction_coefficient_matrix,
        list(stage5.CORE_ORDER_LIST),
        stage5.ANGULAR_SAMPLE_COUNT,
    )
    assert prediction_curve_matrix.shape == dataset.curve_matrix.shape
    return prediction_curve_matrix


def train_additional_ensemble_members(
    dataset: stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
    campaign_output_directory: Path,
) -> list[Path]:
    """Train and persist the four additional deterministic K01 members."""

    checkpoint_path_list = [PRIMARY_K01_CHECKPOINT_PATH]
    specification = find_k01_specification()
    original_run_root = stage9.RUN_ROOT_DIRECTORY
    stage9.RUN_ROOT_DIRECTORY = RUN_ROOT_DIRECTORY
    try:
        for random_seed in ENSEMBLE_SEED_LIST[1:]:
            result_payload = stage9.train_candidate(
                specification,
                dataset,
                anchor_bundle,
                campaign_output_directory,
                random_seed,
            )
            checkpoint_path = (
                PROJECT_ROOT / result_payload["checkpoint_path"]
            )
            assert checkpoint_path.exists()
            checkpoint_path_list.append(checkpoint_path)
    finally:
        stage9.RUN_ROOT_DIRECTORY = original_run_root
    assert len(checkpoint_path_list) == len(ENSEMBLE_SEED_LIST)
    return checkpoint_path_list


def build_frozen_prediction_bundle(
    dataset: stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
    campaign_output_directory: Path,
    train_ensemble: bool,
    checkpoint_path_list: list[Path] | None = None,
) -> FrozenPredictionBundle:
    """Build all aligned prediction sources for trust calibration."""

    if checkpoint_path_list is not None:
        resolved_checkpoint_path_list = checkpoint_path_list
    elif train_ensemble:
        resolved_checkpoint_path_list = train_additional_ensemble_members(
            dataset,
            anchor_bundle,
            campaign_output_directory,
        )
    else:
        resolved_checkpoint_path_list = [PRIMARY_K01_CHECKPOINT_PATH]
    ensemble_prediction_list = [
        predict_checkpoint_all_curves(
            checkpoint_path,
            dataset,
            anchor_bundle,
        )
        for checkpoint_path in resolved_checkpoint_path_list
    ]
    return FrozenPredictionBundle(
        pf_a_curve_matrix=anchor_bundle.pf_a_curve_matrix,
        h04_curve_matrix=anchor_bundle.h04_curve_matrix,
        k01_curve_matrix=ensemble_prediction_list[0],
        dense_r00_curve_matrix=build_dense_r00_predictions(
            dataset,
            anchor_bundle,
        ),
        k01_ensemble_prediction_tensor=np.stack(
            ensemble_prediction_list,
            axis=0,
        ),
        ensemble_checkpoint_path_list=[
            path.relative_to(PROJECT_ROOT).as_posix()
            for path in resolved_checkpoint_path_list
        ],
    )


def build_condition_band_array(
    full_feature_array: np.ndarray,
    training_mask: np.ndarray,
    feature_name: str,
) -> np.ndarray:
    """Assign train-defined low, medium, and high operating bands."""

    training_value = np.asarray(
        full_feature_array[training_mask],
        dtype=np.float64,
    )
    lower, upper = np.quantile(training_value, [1.0 / 3.0, 2.0 / 3.0])
    band_array = np.full(full_feature_array.shape, "mid", dtype=object)
    band_array[full_feature_array <= lower] = "low"
    band_array[full_feature_array > upper] = "high"
    return np.asarray(
        [f"{feature_name}_{value}" for value in band_array],
        dtype=str,
    )


def build_raw_signal_map(
    dataset: stage5.Stage5Dataset,
    prediction_bundle: FrozenPredictionBundle,
) -> tuple[
    dict[str, np.ndarray],
    dict[str, np.ndarray],
    np.ndarray,
]:
    """Build curvewise and pointwise causal uncertainty signals."""

    training_mask = dataset.split_array == "train"
    condition_distance = calculate_nearest_training_distance(
        dataset.condition_matrix,
        dataset.condition_matrix[training_mask],
        dataset.feature_mean,
        dataset.feature_scale,
    )
    support_boundary_score, support_tier_array = (
        calculate_support_boundary_score(
            dataset.condition_matrix,
            dataset.condition_matrix[training_mask],
            dataset.feature_mean,
            dataset.feature_scale,
            SUPPORT_DENSITY_THRESHOLD,
        )
    )
    pf_a_h04_curve, pf_a_h04_point = calculate_curve_disagreement(
        prediction_bundle.pf_a_curve_matrix,
        prediction_bundle.h04_curve_matrix,
    )
    h04_k01_curve, h04_k01_point = calculate_curve_disagreement(
        prediction_bundle.h04_curve_matrix,
        prediction_bundle.k01_curve_matrix,
    )
    pf_a_k01_curve, pf_a_k01_point = calculate_curve_disagreement(
        prediction_bundle.pf_a_curve_matrix,
        prediction_bundle.k01_curve_matrix,
    )
    dense_k01_curve, dense_k01_point = calculate_curve_disagreement(
        prediction_bundle.dense_r00_curve_matrix,
        prediction_bundle.k01_curve_matrix,
    )
    if prediction_bundle.k01_ensemble_prediction_tensor.shape[0] >= 2:
        ensemble_curve, ensemble_point = calculate_ensemble_spread(
            prediction_bundle.k01_ensemble_prediction_tensor
        )
    else:
        ensemble_curve = np.zeros(dataset.curve_matrix.shape[0])
        ensemble_point = np.zeros_like(dataset.curve_matrix)
    curve_signal_map = {
        "C00": np.ones(dataset.curve_matrix.shape[0]),
        "S01": condition_distance,
        "S02": support_boundary_score,
        "A01": pf_a_h04_curve,
        "A02": h04_k01_curve,
        "A03": pf_a_k01_curve,
        "D01": dense_k01_curve,
        "E01": ensemble_curve,
    }
    point_signal_map = {
        "C00": np.ones_like(dataset.curve_matrix),
        "S01": np.repeat(
            condition_distance[:, np.newaxis],
            stage5.ANGULAR_SAMPLE_COUNT,
            axis=1,
        ),
        "S02": np.repeat(
            support_boundary_score[:, np.newaxis],
            stage5.ANGULAR_SAMPLE_COUNT,
            axis=1,
        ),
        "A01": pf_a_h04_point,
        "A02": h04_k01_point,
        "A03": pf_a_k01_point,
        "D01": dense_k01_point,
        "E01": ensemble_point,
    }
    return curve_signal_map, point_signal_map, support_tier_array


def build_composite_feature_matrix(
    curve_signal_map: dict[str, np.ndarray],
) -> np.ndarray:
    """Stack the declared causal scalar signals for M01."""

    return np.column_stack(
        [
            curve_signal_map[candidate_id]
            for candidate_id in (
                "S01",
                "S02",
                "A01",
                "A02",
                "A03",
                "D01",
                "E01",
            )
        ]
    )


def serialize_calibration_state(
    candidate_id: str,
    isotonic_state: IsotonicCalibrationState | None,
    composite_state: CompositeTrustState | None,
) -> dict[str, Any]:
    """Serialize the calibration mechanism for one candidate."""

    if candidate_id == "M01":
        assert composite_state is not None
        return {
            "type": "nonnegative_ridge_plus_isotonic",
            "state": serialize_composite_state(composite_state),
        }
    assert isotonic_state is not None
    return {
        "type": "isotonic",
        "state": serialize_isotonic_state(isotonic_state),
    }


def build_group_array_map(
    dataset: stage5.Stage5Dataset,
    support_tier_array: np.ndarray,
) -> dict[str, np.ndarray]:
    """Build train-defined operating bands and support groups."""

    training_mask = dataset.split_array == "train"
    return {
        "torque": build_condition_band_array(
            dataset.condition_matrix[:, 0],
            training_mask,
            "torque",
        ),
        "speed": build_condition_band_array(
            dataset.condition_matrix[:, 1],
            training_mask,
            "speed",
        ),
        "temperature": build_condition_band_array(
            dataset.condition_matrix[:, 2],
            training_mask,
            "temperature",
        ),
        "support": support_tier_array,
    }


def calculate_candidate_gate(
    specification: CandidateSpecification,
    metric_payload: dict[str, Any],
    constant_width: float,
    group_row_list: list[dict[str, Any]],
) -> dict[str, Any]:
    """Apply the frozen Stage 11 exit thresholds."""

    localization = metric_payload["localization"]
    interval = metric_payload["interval"]
    populated_band_rows = [
        row
        for row in group_row_list
        if row["group_domain"] in {"torque", "speed", "temperature"}
        and int(row["curve_count"]) >= 10
    ]
    minimum_band_coverage = min(
        (
            float(row["marginal_90_coverage"])
            for row in populated_band_rows
        ),
        default=1.0,
    )
    gate_payload = {
        "not_a_control": not specification.diagnostic_control,
        "rank_correlation_pass": (
            localization["spearman_correlation"] >= 0.30
        ),
        "average_precision_pass": (
            localization["top_quintile_average_precision"] >= 0.35
        ),
        "high_error_capture_pass": (
            localization["top_20_percent_error_capture_rate"] >= 0.40
        ),
        "selective_risk_pass": (
            localization["selective_curve_mae_80_percent_deg"]
            <= 0.90 * localization["unfiltered_curve_mae_deg"]
        ),
        "marginal_coverage_pass": (
            0.85 <= interval["marginal_90_coverage"] <= 0.95
        ),
        "interval_width_pass": (
            interval["marginal_90_mean_width_deg"]
            <= 1.05 * constant_width
        ),
        "operating_band_coverage_pass": minimum_band_coverage >= 0.75,
        "causal_runtime_input_pass": (
            metric_payload["runtime_target_derived_input_count"] == 0
        ),
        "finite_payload_pass": metric_payload["finite_payload_pass"],
        "minimum_populated_band_coverage": minimum_band_coverage,
    }
    gate_payload["qualified_trust_component"] = bool(
        all(
            value
            for key, value in gate_payload.items()
            if key.endswith("_pass")
        )
        and gate_payload["not_a_control"]
    )
    gate_payload["deployment_cost_pass"] = (
        metric_payload["checkpoint_cost_multiplier"] <= 1.25
    )
    gate_payload["deployment_ready"] = bool(
        gate_payload["qualified_trust_component"]
        and gate_payload["deployment_cost_pass"]
    )
    return gate_payload


def prepare_campaign(dataset: stage5.Stage5Dataset) -> None:
    """Create the approved Stage 11 campaign package and state."""

    CONFIG_DIRECTORY.mkdir(parents=True, exist_ok=True)
    QUEUE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    candidate_list = build_candidate_list()
    campaign_payload = {
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": STAGE_NAME,
        "status": "prepared",
        "dataset_id": "polished_dataset",
        "input_mode": "setpoints",
        "surface_list": ["fw"],
        "primary_surface": "fw",
        "expected_run_count": len(candidate_list),
        "random_seed_list": ENSEMBLE_SEED_LIST,
        "split_signature": SPLIT_SIGNATURE,
        "curve_count_by_split": {
            split_name: int(np.sum(dataset.split_array == split_name))
            for split_name in ("train", "validation", "test")
        },
        "candidate_id_list": [
            specification.candidate_id
            for specification in candidate_list
        ],
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "planning_report_path": CAMPAIGN_PLAN_PATH,
        "launcher_path": LAUNCHER_PATH,
        "launcher_note_path": LAUNCHER_NOTE_PATH,
    }
    write_yaml(CONFIG_DIRECTORY / "campaign.yaml", campaign_payload)
    for specification in candidate_list:
        write_yaml(
            QUEUE_DIRECTORY
            / (
                f"{specification.queue_index:03d}_"
                f"{specification.candidate_id.lower()}.yaml"
            ),
            {
                "queue_index": specification.queue_index,
                "candidate_id": specification.candidate_id,
                "formulation": specification.formulation,
                "diagnostic_control": specification.diagnostic_control,
                "ensemble_checkpoint_count": (
                    specification.ensemble_checkpoint_count
                ),
                "status": "prepared",
            },
        )
    active_payload = {
        "status": "prepared",
        "prepared_at": now_iso(),
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": STAGE_NAME,
        "dataset_id": "polished_dataset",
        "input_mode": "setpoints",
        "surface_list": ["fw"],
        "primary_surface": "fw",
        "expected_run_count": len(candidate_list),
        "completed_run_count": 0,
        "failed_run_count": 0,
        "random_seed_list": ENSEMBLE_SEED_LIST,
        "campaign_manifest_path": (
            CONFIG_DIRECTORY / "campaign.yaml"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "launcher_path": LAUNCHER_PATH,
        "launcher_note_path": LAUNCHER_NOTE_PATH,
        "planning_report_path": CAMPAIGN_PLAN_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "local_preflight_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage11_uncertainty_trust_calibration.ps1 "
            "-PreflightOnly"
        ),
        "local_launch_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage11_uncertainty_trust_calibration.ps1 -Run"
        ),
        "remote_preflight_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage11_uncertainty_trust_calibration.ps1 "
            "-Remote -PreflightOnly"
        ),
        "remote_launch_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage11_uncertainty_trust_calibration.ps1 "
            "-Remote -Run"
        ),
        "approval": {
            "technical_document_status": "approved",
            "campaign_plan_status": "approved",
            "approval_source": (
                "user blanket approval for twenty-four hours"
            ),
            "approval_recorded_at": "2026-07-29T15:30:41+02:00",
            "approval_expires_at": "2026-07-30T15:30:41+02:00",
        },
        "protected_file_list": [
            "doc/running/active_training_campaign.yaml",
            CONFIG_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
            LAUNCHER_PATH,
            (
                "scripts/campaigns/wave_5_2/"
                "run_wave52r_stage11_uncertainty_trust_calibration.py"
            ),
            (
                "scripts/models/"
                "uncertainty_physics_trust_calibrator.py"
            ),
            ANALYSIS_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
        ],
    }
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)


def run_preflight(
    dataset: stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
) -> dict[str, Any]:
    """Run deterministic Stage 11 preflight checks without training."""

    assert dataset.curve_matrix.shape == (966, stage5.ANGULAR_SAMPLE_COUNT)
    assert dataset.condition_matrix.shape == (966, 3)
    assert int(np.sum(dataset.split_array == "train")) == 675
    assert int(np.sum(dataset.split_array == "validation")) == 194
    assert int(np.sum(dataset.split_array == "test")) == 97
    assert PRIMARY_K01_CHECKPOINT_PATH.exists()
    assert STAGE10_R00_PARAMETER_PATH.exists()
    checkpoint_payload = torch.load(
        PRIMARY_K01_CHECKPOINT_PATH,
        map_location="cpu",
        weights_only=False,
    )
    assert checkpoint_payload["split_signature"] == SPLIT_SIGNATURE
    dense_prediction = build_dense_r00_predictions(
        dataset,
        anchor_bundle,
    )
    assert np.all(np.isfinite(dense_prediction))
    synthetic_score = np.linspace(0.0, 1.0, 64)
    synthetic_error = 0.001 + 0.004 * synthetic_score
    calibration_state = fit_isotonic_error_calibrator(
        synthetic_score,
        synthetic_error,
    )
    synthetic_prediction = apply_isotonic_error_calibrator(
        calibration_state,
        synthetic_score,
    )
    synthetic_recovery_error = float(
        np.max(np.abs(synthetic_prediction - synthetic_error))
    )
    assert synthetic_recovery_error <= 1.0e-12
    summary_payload = {
        "status": "pass",
        "checked_at": now_iso(),
        "split_signature": SPLIT_SIGNATURE,
        "curve_count": int(dataset.curve_matrix.shape[0]),
        "train_curve_count": int(
            np.sum(dataset.split_array == "train")
        ),
        "validation_curve_count": int(
            np.sum(dataset.split_array == "validation")
        ),
        "test_curve_count": int(
            np.sum(dataset.split_array == "test")
        ),
        "candidate_count": len(build_candidate_list()),
        "ensemble_seed_list": ENSEMBLE_SEED_LIST,
        "primary_k01_checkpoint_path": (
            PRIMARY_K01_CHECKPOINT_PATH.relative_to(
                PROJECT_ROOT
            ).as_posix()
        ),
        "stage10_r00_parameter_path": (
            STAGE10_R00_PARAMETER_PATH.relative_to(
                PROJECT_ROOT
            ).as_posix()
        ),
        "synthetic_isotonic_recovery_max_abs": (
            synthetic_recovery_error
        ),
        "runtime_target_derived_input_count": 0,
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage11_preflight_validation_summary.yaml",
        summary_payload,
    )
    return summary_payload


def evaluate_candidate(
    specification: CandidateSpecification,
    dataset: stage5.Stage5Dataset,
    prediction_bundle: FrozenPredictionBundle,
    curve_signal_map: dict[str, np.ndarray],
    support_tier_array: np.ndarray,
    composite_state: CompositeTrustState,
    composite_raw_score: np.ndarray,
    shuffled_raw_score: np.ndarray,
    campaign_timestamp: str,
) -> dict[str, Any]:
    """Calibrate, evaluate, and persist one Stage 11 candidate."""

    validation_mask = dataset.split_array == "validation"
    test_mask = dataset.split_array == "test"
    measured_validation = dataset.curve_matrix[validation_mask]
    measured_test = dataset.curve_matrix[test_mask]
    k01_validation = prediction_bundle.k01_curve_matrix[validation_mask]
    k01_test = prediction_bundle.k01_curve_matrix[test_mask]
    validation_curve_error = calculate_curve_error(
        measured_validation,
        k01_validation,
    )
    test_curve_error = calculate_curve_error(measured_test, k01_test)

    isotonic_state: IsotonicCalibrationState | None = None
    candidate_composite_state: CompositeTrustState | None = None
    if specification.candidate_id == "M01":
        candidate_composite_state = composite_state
        raw_score = composite_raw_score
        _, calibrated_scale = apply_composite_trust_estimator(
            composite_state,
            build_composite_feature_matrix(curve_signal_map),
        )
    elif specification.candidate_id == "N01":
        raw_score = shuffled_raw_score
        isotonic_state = fit_isotonic_error_calibrator(
            raw_score[validation_mask],
            validation_curve_error,
        )
        calibrated_scale = apply_isotonic_error_calibrator(
            isotonic_state,
            raw_score,
        )
    else:
        raw_score = curve_signal_map[specification.candidate_id]
        isotonic_state = fit_isotonic_error_calibrator(
            raw_score[validation_mask],
            validation_curve_error,
        )
        calibrated_scale = apply_isotonic_error_calibrator(
            isotonic_state,
            raw_score,
        )

    conformal_payload = fit_conformal_quantiles(
        measured_validation - k01_validation,
        calibrated_scale[validation_mask],
    )
    localization_payload = evaluate_localization_metrics(
        raw_score[test_mask],
        test_curve_error,
    )
    interval_payload = evaluate_conformal_intervals(
        measured_test,
        k01_test,
        calibrated_scale[test_mask],
        conformal_payload,
    )
    group_array_map = build_group_array_map(
        dataset,
        support_tier_array,
    )
    group_row_list: list[dict[str, Any]] = []
    for group_domain, group_array in group_array_map.items():
        domain_row_list = evaluate_group_metrics(
            group_array[test_mask],
            raw_score[test_mask],
            test_curve_error,
            measured_test,
            k01_test,
            calibrated_scale[test_mask],
            conformal_payload,
        )
        for row in domain_row_list:
            group_row_list.append(
                {
                    "group_domain": group_domain,
                    **row,
                }
            )

    checkpoint_cost_multiplier = float(
        specification.ensemble_checkpoint_count
    )
    checkpoint_size_bytes = 0
    if specification.candidate_id == "E01":
        checkpoint_size_bytes = int(
            sum(
                (PROJECT_ROOT / path).stat().st_size
                for path in (
                    prediction_bundle.ensemble_checkpoint_path_list
                )
            )
        )
    elif specification.candidate_id in {"A02", "A03", "D01", "M01", "N01"}:
        checkpoint_size_bytes = int(PRIMARY_K01_CHECKPOINT_PATH.stat().st_size)
    evaluation_start = time.perf_counter()
    for _ in range(100):
        _ = np.asarray(calibrated_scale[test_mask]) * 1.0
    evaluation_seconds_per_curve = (
        (time.perf_counter() - evaluation_start)
        / (100 * int(np.sum(test_mask)))
    )
    metric_payload: dict[str, Any] = {
        "candidate_id": specification.candidate_id,
        "formulation": specification.formulation,
        "diagnostic_control": specification.diagnostic_control,
        "localization": localization_payload,
        "interval": interval_payload,
        "runtime_target_derived_input_count": 0,
        "finite_payload_pass": bool(
            np.all(np.isfinite(raw_score[test_mask]))
            and np.all(np.isfinite(calibrated_scale[test_mask]))
        ),
        "checkpoint_cost_multiplier": checkpoint_cost_multiplier,
        "checkpoint_size_bytes": checkpoint_size_bytes,
        "uncertainty_evaluation_seconds_per_curve": (
            float(evaluation_seconds_per_curve)
        ),
    }
    run_instance_id = (
        f"{campaign_timestamp}__stage11_"
        f"{specification.candidate_id.lower()}"
    )
    run_directory = RUN_ROOT_DIRECTORY / run_instance_id
    run_directory.mkdir(parents=True, exist_ok=True)
    write_yaml(
        run_directory / "calibration_state.yaml",
        {
            "candidate_id": specification.candidate_id,
            "calibration": serialize_calibration_state(
                specification.candidate_id,
                isotonic_state,
                candidate_composite_state,
            ),
            "conformal": conformal_payload,
        },
    )
    write_yaml(run_directory / "metrics_summary.yaml", metric_payload)
    write_csv(run_directory / "group_metrics.csv", group_row_list)
    np.savez_compressed(
        run_directory / "test_uncertainty.npz",
        condition_id=np.asarray(dataset.condition_id_list)[test_mask],
        measured_curve=measured_test,
        predicted_curve=k01_test,
        raw_uncertainty_score=raw_score[test_mask],
        calibrated_curve_scale=calibrated_scale[test_mask],
        per_curve_mae=test_curve_error,
        support_tier=support_tier_array[test_mask],
    )
    return {
        **metric_payload,
        "run_instance_id": run_instance_id,
        "run_directory": run_directory.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "group_row_list": group_row_list,
    }


def build_gate_summary(
    result_list: list[dict[str, Any]],
) -> dict[str, Any]:
    """Apply candidate gates and choose the simplest passing mechanism."""

    constant_result = next(
        result
        for result in result_list
        if result["candidate_id"] == "C00"
    )
    constant_width = float(
        constant_result["interval"]["marginal_90_mean_width_deg"]
    )
    specification_map = {
        specification.candidate_id: specification
        for specification in build_candidate_list()
    }
    gate_row_list: list[dict[str, Any]] = []
    for result in result_list:
        gate_payload = calculate_candidate_gate(
            specification_map[result["candidate_id"]],
            result,
            constant_width,
            result["group_row_list"],
        )
        result["gate"] = gate_payload
        gate_row_list.append(
            {
                "candidate_id": result["candidate_id"],
                "formulation": result["formulation"],
                **gate_payload,
            }
        )
    simplicity_order = [
        "S01",
        "S02",
        "A01",
        "A02",
        "A03",
        "D01",
        "M01",
        "E01",
    ]
    qualified_id_list = [
        candidate_id
        for candidate_id in simplicity_order
        if next(
            result
            for result in result_list
            if result["candidate_id"] == candidate_id
        )["gate"]["qualified_trust_component"]
    ]
    selected_candidate_id = (
        qualified_id_list[0] if qualified_id_list else None
    )
    return {
        "status": "complete",
        "evaluated_candidate_count": len(result_list),
        "qualified_candidate_id_list": qualified_id_list,
        "selected_candidate_id": selected_candidate_id,
        "official_mean_prediction_changed": False,
        "wave6_entry_authorized": False,
        "gate_row_list": gate_row_list,
    }


def leaderboard_row(result: dict[str, Any]) -> dict[str, Any]:
    """Flatten one candidate result for campaign ranking."""

    localization = result["localization"]
    interval = result["interval"]
    gate = result["gate"]
    diagnostic_score = (
        localization["spearman_correlation"]
        + localization["top_quintile_average_precision"]
        + localization["top_20_percent_error_capture_rate"]
        - localization["normalized_area_under_risk_coverage"]
    )
    return {
        "candidate_id": result["candidate_id"],
        "formulation": result["formulation"],
        "run_instance_id": result["run_instance_id"],
        "spearman_correlation": localization["spearman_correlation"],
        "top_quintile_average_precision": (
            localization["top_quintile_average_precision"]
        ),
        "top_20_percent_error_capture_rate": (
            localization["top_20_percent_error_capture_rate"]
        ),
        "normalized_area_under_risk_coverage": (
            localization["normalized_area_under_risk_coverage"]
        ),
        "selective_curve_mae_80_percent_deg": (
            localization["selective_curve_mae_80_percent_deg"]
        ),
        "marginal_90_coverage": interval["marginal_90_coverage"],
        "marginal_90_mean_width_deg": (
            interval["marginal_90_mean_width_deg"]
        ),
        "simultaneous_90_curve_coverage": (
            interval["simultaneous_90_curve_coverage"]
        ),
        "checkpoint_cost_multiplier": (
            result["checkpoint_cost_multiplier"]
        ),
        "qualified_trust_component": (
            gate["qualified_trust_component"]
        ),
        "deployment_ready": gate["deployment_ready"],
        "diagnostic_score": float(diagnostic_score),
    }


def run_campaign(
    dataset: stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
) -> dict[str, Any]:
    """Execute the approved Stage 11 calibration campaign."""

    prepare_campaign(dataset)
    campaign_timestamp = now_timestamp()
    campaign_output_directory = (
        CAMPAIGN_ROOT_DIRECTORY
        / f"{campaign_timestamp}_{CAMPAIGN_NAME}"
    )
    campaign_output_directory.mkdir(parents=True, exist_ok=False)
    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "status": "running",
            "started_at": now_iso(),
            "campaign_output_directory": (
                campaign_output_directory.relative_to(
                    PROJECT_ROOT
                ).as_posix()
            ),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)

    try:
        prediction_bundle = build_frozen_prediction_bundle(
            dataset,
            anchor_bundle,
            campaign_output_directory,
            train_ensemble=True,
        )
        (
            curve_signal_map,
            _,
            support_tier_array,
        ) = build_raw_signal_map(dataset, prediction_bundle)
        validation_mask = dataset.split_array == "validation"
        validation_curve_error = calculate_curve_error(
            dataset.curve_matrix[validation_mask],
            prediction_bundle.k01_curve_matrix[validation_mask],
        )
        composite_feature_matrix = build_composite_feature_matrix(
            curve_signal_map
        )
        composite_state = fit_composite_trust_estimator(
            composite_feature_matrix[validation_mask],
            validation_curve_error,
            PRIMARY_SEED,
        )
        composite_raw_score, _ = apply_composite_trust_estimator(
            composite_state,
            composite_feature_matrix,
        )
        shuffled_raw_score = composite_raw_score.copy()
        random_generator = np.random.default_rng(PRIMARY_SEED + 1101)
        random_generator.shuffle(shuffled_raw_score)

        result_list: list[dict[str, Any]] = []
        for specification in build_candidate_list():
            result_list.append(
                evaluate_candidate(
                    specification,
                    dataset,
                    prediction_bundle,
                    curve_signal_map,
                    support_tier_array,
                    composite_state,
                    composite_raw_score,
                    shuffled_raw_score,
                    campaign_timestamp,
                )
            )
        gate_summary = build_gate_summary(result_list)
        leaderboard_row_list = sorted(
            [leaderboard_row(result) for result in result_list],
            key=lambda row: (
                not bool(row["qualified_trust_component"]),
                -float(row["diagnostic_score"]),
                row["candidate_id"],
            ),
        )
        diagnostic_best_row = max(
            (
                row
                for row in leaderboard_row_list
                if row["candidate_id"] not in {"C00", "N01"}
            ),
            key=lambda row: float(row["diagnostic_score"]),
        )
        selected_candidate_id = gate_summary["selected_candidate_id"]
        selected_row = (
            None
            if selected_candidate_id is None
            else next(
                row
                for row in leaderboard_row_list
                if row["candidate_id"] == selected_candidate_id
            )
        )
        write_yaml(
            campaign_output_directory / "campaign_leaderboard.yaml",
            {
                "campaign_name": CAMPAIGN_NAME,
                "ranked_candidate_list": leaderboard_row_list,
            },
        )
        write_csv(
            campaign_output_directory / "campaign_leaderboard.csv",
            leaderboard_row_list,
        )
        write_yaml(
            campaign_output_directory
            / "campaign_first_screen_gate_summary.yaml",
            gate_summary,
        )
        best_run_payload = {
            "campaign_name": CAMPAIGN_NAME,
            "qualified_winner": selected_row,
            "diagnostic_best_candidate": diagnostic_best_row,
            "official_mean_prediction_changed": False,
            "wave6_entry_authorized": False,
        }
        write_yaml(
            campaign_output_directory / "campaign_best_run.yaml",
            best_run_payload,
        )
        best_run_markdown = [
            "# Wave 5.2R Stage 11 Campaign Best Run",
            "",
            (
                f"- Qualified winner: "
                f"`{selected_candidate_id or 'none'}`."
            ),
            (
                "- Diagnostic best candidate: "
                f"`{diagnostic_best_row['candidate_id']}`."
            ),
            "- Official mean prediction changed: no.",
            "- Wave 6 entry authorized: no.",
            "",
        ]
        (
            campaign_output_directory / "campaign_best_run.md"
        ).write_text("\n".join(best_run_markdown), encoding="utf-8")
        execution_payload = {
            "status": "completed",
            "campaign_name": CAMPAIGN_NAME,
            "started_at": active_payload["started_at"],
            "completed_at": now_iso(),
            "expected_run_count": len(build_candidate_list()),
            "completed_run_count": len(result_list),
            "failed_run_count": 0,
            "ensemble_checkpoint_path_list": (
                prediction_bundle.ensemble_checkpoint_path_list
            ),
            "qualified_winner_id": selected_candidate_id,
            "diagnostic_best_candidate_id": (
                diagnostic_best_row["candidate_id"]
            ),
        }
        write_yaml(
            campaign_output_directory / "campaign_execution_summary.yaml",
            execution_payload,
        )
        active_payload.update(
            {
                "status": "completed",
                "completed_at": execution_payload["completed_at"],
                "completed_run_count": len(result_list),
                "failed_run_count": 0,
                "campaign_best_run_path": (
                    campaign_output_directory
                    / "campaign_best_run.yaml"
                ).relative_to(PROJECT_ROOT).as_posix(),
                "qualified_winner_id": selected_candidate_id,
                "diagnostic_best_candidate_id": (
                    diagnostic_best_row["candidate_id"]
                ),
            }
        )
        write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
        return {
            "campaign_output_directory": (
                campaign_output_directory.relative_to(
                    PROJECT_ROOT
                ).as_posix()
            ),
            "execution": execution_payload,
            "gate_summary": gate_summary,
            "leaderboard": leaderboard_row_list,
        }
    except Exception:
        active_payload.update(
            {
                "status": "failed",
                "completed_at": now_iso(),
                "failed_run_count": 1,
            }
        )
        write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
        raise


def recompute_completed_campaign(
    dataset: stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
) -> dict[str, Any]:
    """Recompute Stage 11 calibration metrics without retraining K01."""

    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    assert active_payload["status"] == "completed"
    campaign_output_directory = (
        PROJECT_ROOT / active_payload["campaign_output_directory"]
    )
    execution_path = (
        campaign_output_directory / "campaign_execution_summary.yaml"
    )
    execution_payload = load_yaml(execution_path)
    checkpoint_path_list = [
        PROJECT_ROOT / relative_path
        for relative_path in execution_payload[
            "ensemble_checkpoint_path_list"
        ]
    ]
    assert len(checkpoint_path_list) == len(ENSEMBLE_SEED_LIST)
    assert all(path.exists() for path in checkpoint_path_list)
    campaign_timestamp = campaign_output_directory.name.split(
        "_wave52r_stage11_",
        maxsplit=1,
    )[0]
    prediction_bundle = build_frozen_prediction_bundle(
        dataset,
        anchor_bundle,
        campaign_output_directory,
        train_ensemble=False,
        checkpoint_path_list=checkpoint_path_list,
    )
    (
        curve_signal_map,
        _,
        support_tier_array,
    ) = build_raw_signal_map(dataset, prediction_bundle)
    validation_mask = dataset.split_array == "validation"
    validation_curve_error = calculate_curve_error(
        dataset.curve_matrix[validation_mask],
        prediction_bundle.k01_curve_matrix[validation_mask],
    )
    composite_feature_matrix = build_composite_feature_matrix(
        curve_signal_map
    )
    composite_state = fit_composite_trust_estimator(
        composite_feature_matrix[validation_mask],
        validation_curve_error,
        PRIMARY_SEED,
    )
    composite_raw_score, _ = apply_composite_trust_estimator(
        composite_state,
        composite_feature_matrix,
    )
    shuffled_raw_score = composite_raw_score.copy()
    random_generator = np.random.default_rng(PRIMARY_SEED + 1101)
    random_generator.shuffle(shuffled_raw_score)
    result_list = [
        evaluate_candidate(
            specification,
            dataset,
            prediction_bundle,
            curve_signal_map,
            support_tier_array,
            composite_state,
            composite_raw_score,
            shuffled_raw_score,
            campaign_timestamp,
        )
        for specification in build_candidate_list()
    ]
    gate_summary = build_gate_summary(result_list)
    leaderboard_row_list = sorted(
        [leaderboard_row(result) for result in result_list],
        key=lambda row: (
            not bool(row["qualified_trust_component"]),
            -float(row["diagnostic_score"]),
            row["candidate_id"],
        ),
    )
    diagnostic_best_row = max(
        (
            row
            for row in leaderboard_row_list
            if row["candidate_id"] not in {"C00", "N01"}
        ),
        key=lambda row: float(row["diagnostic_score"]),
    )
    selected_candidate_id = gate_summary["selected_candidate_id"]
    selected_row = (
        None
        if selected_candidate_id is None
        else next(
            row
            for row in leaderboard_row_list
            if row["candidate_id"] == selected_candidate_id
        )
    )
    write_yaml(
        campaign_output_directory / "campaign_leaderboard.yaml",
        {
            "campaign_name": CAMPAIGN_NAME,
            "ranked_candidate_list": leaderboard_row_list,
        },
    )
    write_csv(
        campaign_output_directory / "campaign_leaderboard.csv",
        leaderboard_row_list,
    )
    write_yaml(
        campaign_output_directory
        / "campaign_first_screen_gate_summary.yaml",
        gate_summary,
    )
    write_yaml(
        campaign_output_directory / "campaign_best_run.yaml",
        {
            "campaign_name": CAMPAIGN_NAME,
            "qualified_winner": selected_row,
            "diagnostic_best_candidate": diagnostic_best_row,
            "official_mean_prediction_changed": False,
            "wave6_entry_authorized": False,
        },
    )
    best_run_markdown = [
        "# Wave 5.2R Stage 11 Campaign Best Run",
        "",
        f"- Qualified winner: `{selected_candidate_id or 'none'}`.",
        (
            "- Diagnostic best candidate: "
            f"`{diagnostic_best_row['candidate_id']}`."
        ),
        "- Official mean prediction changed: no.",
        "- Wave 6 entry authorized: no.",
        "",
    ]
    (
        campaign_output_directory / "campaign_best_run.md"
    ).write_text("\n".join(best_run_markdown), encoding="utf-8")
    execution_payload.update(
        {
            "metrics_recomputed_at": now_iso(),
            "qualified_winner_id": selected_candidate_id,
            "diagnostic_best_candidate_id": (
                diagnostic_best_row["candidate_id"]
            ),
        }
    )
    write_yaml(execution_path, execution_payload)
    active_payload.update(
        {
            "qualified_winner_id": selected_candidate_id,
            "diagnostic_best_candidate_id": (
                diagnostic_best_row["candidate_id"]
            ),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return {
        "campaign_output_directory": (
            campaign_output_directory.relative_to(PROJECT_ROOT).as_posix()
        ),
        "gate_summary": gate_summary,
        "leaderboard": leaderboard_row_list,
    }


def parse_arguments() -> argparse.Namespace:
    """Parse Stage 11 campaign arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--recompute", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Run the requested Stage 11 workflow."""

    arguments = parse_arguments()
    assert sum(
        (
            arguments.prepare,
            arguments.preflight,
            arguments.run,
            arguments.recompute,
        )
    ) == 1, "Choose exactly one of --prepare, --preflight, or --run."
    dataset = stage5.build_stage5_dataset()
    anchor_bundle = stage9.build_anchor_bundle(dataset)
    if arguments.prepare:
        prepare_campaign(dataset)
        print(f"[DONE] Prepared {CAMPAIGN_NAME}")
        return
    if arguments.preflight:
        prepare_campaign(dataset)
        summary = run_preflight(dataset, anchor_bundle)
        print(yaml.safe_dump(summary, sort_keys=False))
        return
    if arguments.recompute:
        result = recompute_completed_campaign(dataset, anchor_bundle)
        print(yaml.safe_dump(result, sort_keys=False))
        return
    run_preflight(dataset, anchor_bundle)
    result = run_campaign(dataset, anchor_bundle)
    print(yaml.safe_dump(result, sort_keys=False))


if __name__ == "__main__":
    main()
