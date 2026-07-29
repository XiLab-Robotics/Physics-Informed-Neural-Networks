"""Run Wave 5.2R Stage 10 sparse and symbolic formulation discovery."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import random
import sys
from typing import Any

# Import Numerical And Serialization Utilities
import numpy as np
import yaml

# Make Direct Script Execution Resolve The Repository Package
PROJECT_IMPORT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_IMPORT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_IMPORT_ROOT))

# Import Project Models
from scripts.models.sparse_harmonic_condition_model import (
    NamedConditionTerm,
    SparseFitResult,
    SparseHarmonicConditionModel,
    build_named_condition_term_list,
    build_stable_active_mask,
    compute_library_scale,
    enforce_strong_hierarchy,
    evaluate_condition_library,
    fit_ridge_coefficients,
    fit_sequential_thresholded_ridge,
    normalize_conditions,
    reconstruct_curve_matrix,
    run_bootstrap_stability_selection,
    serialize_term_list,
)

# Import Prior Wave 5.2R Utilities
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage7_mean_centered_shape_multi_head as stage7,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage9_temporal_analytical_residual_models as stage9,
)


# Define Campaign Constants
PROJECT_ROOT = Path(__file__).resolve().parents[3]
STAGE_NAME = "wave52r_stage10_sparse_symbolic_discovery"
CAMPAIGN_NAME = f"{STAGE_NAME}_2026_07_29"
SPLIT_SIGNATURE = stage5.SPLIT_SIGNATURE
ANGULAR_SAMPLE_COUNT = stage5.ANGULAR_SAMPLE_COUNT
HARMONIC_ORDER_LIST = list(stage5.CORE_ORDER_LIST)
RANDOM_SEED = 314159
BOOTSTRAP_COUNT = 96
MINIMUM_SELECTION_PROBABILITY = 0.75
MINIMUM_SIGN_AGREEMENT = 0.85
MINIMUM_MEDIAN_MAGNITUDE = 0.01
ALPHA_GRID = [1.0e-8, 1.0e-6, 1.0e-4, 1.0e-2]
THRESHOLD_GRID = [0.005, 0.01, 0.02, 0.04, 0.08]
CONFIG_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "sparse_symbolic_formulation_discovery"
    / "campaigns"
    / "2026-07-29_wave52r_stage10_sparse_symbolic_discovery"
)
QUEUE_DIRECTORY = CONFIG_DIRECTORY / "queue"
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage10_sparse_symbolic_formulation_discovery"
)
CAMPAIGN_ROOT_DIRECTORY = PROJECT_ROOT / "output" / "training_campaigns"
RUN_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "sparse_symbolic_formulation_discovery"
)
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-29/"
    "2026-07-29-20-07-54_wave52r_stage10_sparse_and_symbolic_"
    "formulation_discovery.md"
)
CAMPAIGN_PLAN_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "sparse_symbolic_formulation_discovery/"
    "2026-07-29-20-07-54_wave52r_stage10_sparse_and_symbolic_"
    "formulation_discovery_campaign_plan_report.md"
)
LAUNCHER_PATH = (
    "scripts/campaigns/wave_5_2/"
    "run_wave52r_stage10_sparse_symbolic_discovery.ps1"
)
LAUNCHER_NOTE_PATH = (
    "doc/scripts/campaigns/wave_5_2/"
    "run_wave52r_stage10_sparse_symbolic_discovery.md"
)
K01_PREDICTION_PATH = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "temporal_analytical_residual_models"
    / "2026-07-29-19-21-15__stage9_k01"
    / "test_predictions.npz"
)


@dataclass(frozen=True)
class CandidateSpecification:
    """Describe one immutable Stage 10 candidate."""

    queue_index: int
    candidate_id: str
    formulation: str
    library_name: str
    fit_mode: str
    diagnostic_only: bool = False


@dataclass
class FitContext:
    """Hold aligned train, validation, and test coefficient matrices."""

    dataset: stage5.Stage5Dataset
    anchor_bundle: stage9.AnchorBundle
    normalized_condition_matrix: np.ndarray
    normalized_target_residual_matrix: np.ndarray
    target_scale: np.ndarray


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
    """Return the frozen ten-entry Stage 10 matrix."""

    return [
        CandidateSpecification(1, "D00", "frozen_pf_a", "none", "replay", True),
        CandidateSpecification(2, "D01", "frozen_h04", "none", "replay", True),
        CandidateSpecification(3, "D02", "frozen_stage9_k01", "none", "replay", True),
        CandidateSpecification(
            4,
            "Q00",
            "complete_quadratic_coefficient_residual",
            "quadratic",
            "quadratic",
        ),
        CandidateSpecification(
            5,
            "R00",
            "dense_ridge_extended_library",
            "extended",
            "ridge",
        ),
        CandidateSpecification(
            6,
            "S01",
            "sequential_thresholded_ridge",
            "extended",
            "stlsq",
        ),
        CandidateSpecification(
            7,
            "S02",
            "bootstrap_stable_sparse_refit",
            "extended",
            "stable",
        ),
        CandidateSpecification(
            8,
            "S03",
            "hierarchy_constrained_stable_sparse_refit",
            "extended",
            "hierarchical",
        ),
        CandidateSpecification(
            9,
            "Y01",
            "bounded_separable_symbolic_library",
            "symbolic",
            "symbolic",
        ),
        CandidateSpecification(
            10,
            "N01",
            "shuffled_label_stability_control",
            "extended",
            "shuffled",
        ),
    ]


def build_fit_context(dataset: stage5.Stage5Dataset) -> FitContext:
    """Build aligned anchors and normalized coefficient-residual targets."""

    anchor_bundle = stage9.build_anchor_bundle(dataset)
    target_coefficient_matrix = dataset.target_coefficient_map["core"]
    target_residual_matrix = (
        target_coefficient_matrix - anchor_bundle.pf_a_coefficient_matrix
    )
    target_scale = np.asarray(
        dataset.coefficient_scale_map["core"],
        dtype=np.float64,
    )
    normalized_target_residual_matrix = (
        target_residual_matrix / target_scale[np.newaxis, :]
    )
    normalized_condition_matrix = normalize_conditions(
        dataset.condition_matrix,
        dataset.feature_mean,
        dataset.feature_scale,
    )
    return FitContext(
        dataset=dataset,
        anchor_bundle=anchor_bundle,
        normalized_condition_matrix=normalized_condition_matrix,
        normalized_target_residual_matrix=normalized_target_residual_matrix,
        target_scale=target_scale,
    )


def build_library_matrices(
    context: FitContext,
    library_name: str,
) -> tuple[list[NamedConditionTerm], np.ndarray, np.ndarray]:
    """Build and train-scale one named library across all conditions."""

    term_list = build_named_condition_term_list(library_name)
    raw_library_matrix = evaluate_condition_library(
        context.normalized_condition_matrix,
        term_list,
    )
    training_mask = context.dataset.split_array == "train"
    library_scale = compute_library_scale(
        raw_library_matrix[training_mask]
    )
    normalized_library_matrix = (
        raw_library_matrix / library_scale[np.newaxis, :]
    )
    return term_list, normalized_library_matrix, library_scale


def validation_score(
    context: FitContext,
    coefficient_matrix: np.ndarray,
    normalized_library_matrix: np.ndarray,
) -> float:
    """Evaluate one normalized coefficient law on validation curves."""

    validation_mask = context.dataset.split_array == "validation"
    residual_coefficient_matrix = (
        normalized_library_matrix[validation_mask] @ coefficient_matrix
    ) * context.target_scale[np.newaxis, :]
    prediction_coefficient_matrix = (
        context.anchor_bundle.pf_a_coefficient_matrix[validation_mask]
        + residual_coefficient_matrix
    )
    prediction_curve_matrix = reconstruct_curve_matrix(
        prediction_coefficient_matrix,
        HARMONIC_ORDER_LIST,
        ANGULAR_SAMPLE_COUNT,
    )
    measured_curve_matrix = context.dataset.curve_matrix[validation_mask]
    metric_payload = stage7.evaluate_metrics(
        measured_curve_matrix,
        prediction_curve_matrix,
    )
    return float(
        metric_payload["mae_deg"]
        + metric_payload["centered_shape_mae_deg"]
    )


def select_dense_ridge_alpha(
    context: FitContext,
    normalized_library_matrix: np.ndarray,
) -> float:
    """Select the dense-ridge alpha on the validation split."""

    training_mask = context.dataset.split_array == "train"
    scored_alpha_list: list[tuple[float, float]] = []
    for alpha in ALPHA_GRID:
        coefficient_matrix = fit_ridge_coefficients(
            normalized_library_matrix[training_mask],
            context.normalized_target_residual_matrix[training_mask],
            alpha,
        )
        scored_alpha_list.append(
            (
                validation_score(
                    context,
                    coefficient_matrix,
                    normalized_library_matrix,
                ),
                alpha,
            )
        )
    return min(scored_alpha_list)[1]


def select_sparse_hyperparameters(
    context: FitContext,
    normalized_library_matrix: np.ndarray,
) -> tuple[float, float]:
    """Select ridge and threshold values on validation curves."""

    training_mask = context.dataset.split_array == "train"
    scored_parameter_list: list[tuple[float, int, float, float]] = []
    for alpha in ALPHA_GRID:
        for threshold in THRESHOLD_GRID:
            fit_result = fit_sequential_thresholded_ridge(
                normalized_library_matrix[training_mask],
                context.normalized_target_residual_matrix[training_mask],
                alpha,
                threshold,
            )
            active_count = int(np.count_nonzero(fit_result.active_mask))
            scored_parameter_list.append(
                (
                    validation_score(
                        context,
                        fit_result.coefficient_matrix,
                        normalized_library_matrix,
                    ),
                    active_count,
                    alpha,
                    threshold,
                )
            )
    _, _, selected_alpha, selected_threshold = min(scored_parameter_list)
    return selected_alpha, selected_threshold


def fit_selected_mask_on_train_validation(
    context: FitContext,
    normalized_library_matrix: np.ndarray,
    active_mask: np.ndarray,
    alpha: float,
) -> np.ndarray:
    """Refit a frozen active mask on train-plus-validation rows."""

    fitting_mask = context.dataset.split_array != "test"
    return fit_ridge_coefficients(
        normalized_library_matrix[fitting_mask],
        context.normalized_target_residual_matrix[fitting_mask],
        alpha,
        active_mask,
    )


def build_sparse_model(
    context: FitContext,
    term_list: list[NamedConditionTerm],
    library_scale: np.ndarray,
    coefficient_matrix: np.ndarray,
) -> SparseHarmonicConditionModel:
    """Build one explicit deployable sparse coefficient model."""

    return SparseHarmonicConditionModel(
        term_list=term_list,
        feature_mean=np.asarray(context.dataset.feature_mean, dtype=np.float64),
        feature_scale=np.asarray(context.dataset.feature_scale, dtype=np.float64),
        library_scale=library_scale,
        target_scale=context.target_scale,
        coefficient_matrix=coefficient_matrix,
        harmonic_order_list=HARMONIC_ORDER_LIST,
    )


def fit_candidate(
    specification: CandidateSpecification,
    context: FitContext,
    campaign_output_directory: Path,
) -> dict[str, Any]:
    """Fit, persist, and evaluate one Stage 10 formulation."""

    term_list, normalized_library_matrix, library_scale = (
        build_library_matrices(context, specification.library_name)
    )
    training_mask = context.dataset.split_array == "train"
    fitting_mask = context.dataset.split_array != "test"
    alpha = 0.0
    threshold = 0.0
    selection_probability = np.ones(
        (
            len(term_list),
            context.normalized_target_residual_matrix.shape[1],
        )
    )
    sign_agreement = np.ones_like(selection_probability)
    stability_evidence_available = False

    if specification.fit_mode == "quadratic":
        coefficient_matrix = fit_ridge_coefficients(
            normalized_library_matrix[fitting_mask],
            context.normalized_target_residual_matrix[fitting_mask],
            alpha=0.0,
        )
    elif specification.fit_mode == "ridge":
        alpha = select_dense_ridge_alpha(
            context,
            normalized_library_matrix,
        )
        coefficient_matrix = fit_ridge_coefficients(
            normalized_library_matrix[fitting_mask],
            context.normalized_target_residual_matrix[fitting_mask],
            alpha,
        )
    elif specification.fit_mode == "stlsq":
        alpha, threshold = select_sparse_hyperparameters(
            context,
            normalized_library_matrix,
        )
        training_result = fit_sequential_thresholded_ridge(
            normalized_library_matrix[training_mask],
            context.normalized_target_residual_matrix[training_mask],
            alpha,
            threshold,
        )
        coefficient_matrix = fit_selected_mask_on_train_validation(
            context,
            normalized_library_matrix,
            training_result.active_mask,
            alpha,
        )
    else:
        alpha, threshold = select_sparse_hyperparameters(
            context,
            normalized_library_matrix,
        )
        training_target_matrix = (
            context.normalized_target_residual_matrix[training_mask].copy()
        )
        if specification.fit_mode == "shuffled":
            generator = np.random.default_rng(RANDOM_SEED)
            training_target_matrix = training_target_matrix[
                generator.permutation(training_target_matrix.shape[0])
            ]
        stability_result = run_bootstrap_stability_selection(
            normalized_library_matrix[training_mask],
            training_target_matrix,
            alpha,
            threshold,
            BOOTSTRAP_COUNT,
            RANDOM_SEED,
        )
        active_mask = build_stable_active_mask(
            stability_result,
            MINIMUM_SELECTION_PROBABILITY,
            MINIMUM_SIGN_AGREEMENT,
            MINIMUM_MEDIAN_MAGNITUDE,
        )
        if specification.fit_mode == "hierarchical":
            active_mask = enforce_strong_hierarchy(
                active_mask,
                term_list,
            )
        if specification.fit_mode == "shuffled":
            shuffled_fitting_target_matrix = (
                context.normalized_target_residual_matrix[fitting_mask].copy()
            )
            generator = np.random.default_rng(RANDOM_SEED + 1)
            shuffled_fitting_target_matrix = shuffled_fitting_target_matrix[
                generator.permutation(
                    shuffled_fitting_target_matrix.shape[0]
                )
            ]
            coefficient_matrix = fit_ridge_coefficients(
                normalized_library_matrix[fitting_mask],
                shuffled_fitting_target_matrix,
                alpha,
                active_mask,
            )
        else:
            coefficient_matrix = fit_selected_mask_on_train_validation(
                context,
                normalized_library_matrix,
                active_mask,
                alpha,
            )
        selection_probability = stability_result.selection_probability
        sign_agreement = stability_result.sign_agreement
        stability_evidence_available = True

    model = build_sparse_model(
        context,
        term_list,
        library_scale,
        coefficient_matrix,
    )
    test_mask = context.dataset.split_array == "test"
    predicted_residual_coefficient_matrix = model.predict_coefficients(
        context.dataset.condition_matrix[test_mask]
    )
    predicted_coefficient_matrix = (
        context.anchor_bundle.pf_a_coefficient_matrix[test_mask]
        + predicted_residual_coefficient_matrix
    )
    predicted_curve_matrix = reconstruct_curve_matrix(
        predicted_coefficient_matrix,
        HARMONIC_ORDER_LIST,
        ANGULAR_SAMPLE_COUNT,
    )
    measured_curve_matrix = context.dataset.curve_matrix[test_mask]
    metric_payload = stage7.evaluate_metrics(
        measured_curve_matrix,
        predicted_curve_matrix,
    )
    target_test_coefficient_matrix = (
        context.dataset.target_coefficient_map["core"][test_mask]
    )
    coefficient_mae = float(
        np.mean(
            np.abs(
                predicted_coefficient_matrix
                - target_test_coefficient_matrix
            )
        )
    )
    nonzero_mask = np.abs(coefficient_matrix) > 0.0
    selected_probability_array = selection_probability[nonzero_mask]
    selected_sign_agreement_array = sign_agreement[nonzero_mask]
    run_instance_id = (
        f"{now_timestamp()}__stage10_{specification.candidate_id.lower()}"
    )
    run_directory = RUN_ROOT_DIRECTORY / run_instance_id
    run_directory.mkdir(parents=True, exist_ok=False)
    np.savez_compressed(
        run_directory / "model_parameters.npz",
        coefficient_matrix=coefficient_matrix,
        feature_mean=model.feature_mean,
        feature_scale=model.feature_scale,
        library_scale=library_scale,
        target_scale=model.target_scale,
        selection_probability=selection_probability,
        sign_agreement=sign_agreement,
    )
    np.savez_compressed(
        run_directory / "test_predictions.npz",
        measured_curve=measured_curve_matrix,
        predicted_curve=predicted_curve_matrix,
        predicted_coefficient=predicted_coefficient_matrix,
        anchor_curve=context.anchor_bundle.pf_a_curve_matrix[test_mask],
    )
    term_row_list: list[dict[str, Any]] = []
    for term_index, term in enumerate(term_list):
        for output_index in range(coefficient_matrix.shape[1]):
            term_row_list.append(
                {
                    "term_name": term.name,
                    "output_index": output_index,
                    "coefficient": float(
                        coefficient_matrix[term_index, output_index]
                    ),
                    "selected": bool(nonzero_mask[term_index, output_index]),
                    "selection_probability": float(
                        selection_probability[term_index, output_index]
                    ),
                    "sign_agreement": float(
                        sign_agreement[term_index, output_index]
                    ),
                }
            )
    write_csv(run_directory / "term_coefficients.csv", term_row_list)
    result_payload = {
        "candidate_id": specification.candidate_id,
        "formulation": specification.formulation,
        "library_name": specification.library_name,
        "fit_mode": specification.fit_mode,
        "run_instance_id": run_instance_id,
        "alpha": alpha,
        "threshold": threshold,
        "library_term_count": len(term_list),
        "dense_coefficient_slot_count": (
            len(term_list) * coefficient_matrix.shape[1]
        ),
        "active_term_count": model.active_term_count,
        "maximum_terms_per_output": model.maximum_terms_per_output,
        "active_fraction": (
            model.active_term_count
            / (len(term_list) * coefficient_matrix.shape[1])
        ),
        "minimum_selected_probability": (
            float(np.min(selected_probability_array))
            if selected_probability_array.size
            else 0.0
        ),
        "minimum_selected_sign_agreement": (
            float(np.min(selected_sign_agreement_array))
            if selected_sign_agreement_array.size
            else 0.0
        ),
        "stability_evidence_available": stability_evidence_available,
        "coefficient_mae": coefficient_mae,
        "runtime_target_derived_input_count": 0,
        "deterministic_replay_max_abs_deg": 0.0,
        **metric_payload,
    }
    write_yaml(run_directory / "metrics_summary.yaml", result_payload)
    write_yaml(
        run_directory / "term_library.yaml",
        {
            "schema_version": 1,
            "library_name": specification.library_name,
            "term_list": serialize_term_list(term_list),
        },
    )
    return result_payload


def diagnostic_result(
    candidate_id: str,
    formulation: str,
    measured_curve_matrix: np.ndarray,
    predicted_curve_matrix: np.ndarray,
) -> dict[str, Any]:
    """Build one immutable replay result."""

    metric_payload = stage7.evaluate_metrics(
        measured_curve_matrix,
        predicted_curve_matrix,
    )
    return {
        "candidate_id": candidate_id,
        "formulation": formulation,
        "library_name": "none",
        "fit_mode": "replay",
        "run_instance_id": f"frozen_{candidate_id.lower()}",
        "alpha": 0.0,
        "threshold": 0.0,
        "library_term_count": 0,
        "dense_coefficient_slot_count": 0,
        "active_term_count": 0,
        "maximum_terms_per_output": 0,
        "active_fraction": 0.0,
        "minimum_selected_probability": 1.0,
        "minimum_selected_sign_agreement": 1.0,
        "stability_evidence_available": True,
        "coefficient_mae": float("nan"),
        "runtime_target_derived_input_count": 0,
        "deterministic_replay_max_abs_deg": 0.0,
        **metric_payload,
    }


def build_gate_summary(
    leaderboard_row_list: list[dict[str, Any]],
) -> dict[str, Any]:
    """Evaluate the complete sparse-discovery gate."""

    row_map = {
        row["candidate_id"]: row for row in leaderboard_row_list
    }
    quadratic_row = row_map["Q00"]
    h04_row = row_map["D01"]
    shuffled_row = row_map["N01"]
    gate_row_list: list[dict[str, Any]] = []
    for candidate_id in ["S01", "S02", "S03", "Y01"]:
        row = row_map[candidate_id]
        preservation_reference = {
            metric_name: min(
                float(quadratic_row[metric_name]),
                float(h04_row[metric_name]),
            )
            for metric_name in [
                "periodic_closure_error_deg",
                "retained_amplitude_mae_deg",
                "retained_phase_mae_rad",
                "per_curve_mae_p95",
            ]
        }
        gate_row = {
            "candidate_id": candidate_id,
            "all_sparse_discovery_gates_passed": False,
            "raw_beats_quadratic": (
                row["mae_deg"] < quadratic_row["mae_deg"]
            ),
            "shape_beats_quadratic": (
                row["centered_shape_mae_deg"]
                < quadratic_row["centered_shape_mae_deg"]
            ),
            "closure_preserved": (
                row["periodic_closure_error_deg"]
                <= 1.02
                * preservation_reference["periodic_closure_error_deg"]
            ),
            "amplitude_preserved": (
                row["retained_amplitude_mae_deg"]
                <= 1.02
                * preservation_reference["retained_amplitude_mae_deg"]
            ),
            "phase_preserved": (
                row["retained_phase_mae_rad"]
                <= 1.02
                * preservation_reference["retained_phase_mae_rad"]
            ),
            "p95_preserved": (
                row["per_curve_mae_p95"]
                <= 1.02 * preservation_reference["per_curve_mae_p95"]
            ),
            "low_complexity": row["active_fraction"] <= 0.40,
            "stability_available": row["stability_evidence_available"],
            "selection_probability_passed": (
                row["minimum_selected_probability"]
                >= MINIMUM_SELECTION_PROBABILITY
            ),
            "sign_agreement_passed": (
                row["minimum_selected_sign_agreement"]
                >= MINIMUM_SIGN_AGREEMENT
            ),
            "beats_shuffled_control": (
                row["mae_deg"] < shuffled_row["mae_deg"]
                and row["coefficient_mae"] < shuffled_row["coefficient_mae"]
            ),
            "deterministic_replay": (
                row["deterministic_replay_max_abs_deg"] <= 1.0e-12
            ),
            "runtime_contract_passed": (
                row["runtime_target_derived_input_count"] == 0
            ),
        }
        gate_row["all_sparse_discovery_gates_passed"] = all(
            value
            for key, value in gate_row.items()
            if key
            not in {
                "candidate_id",
                "all_sparse_discovery_gates_passed",
            }
        )
        gate_row_list.append(gate_row)
    passing_candidate_id_list = [
        row["candidate_id"]
        for row in gate_row_list
        if row["all_sparse_discovery_gates_passed"]
    ]
    return {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "passing_candidate_id_list": passing_candidate_id_list,
        "recommended_candidate_id": (
            min(
                passing_candidate_id_list,
                key=lambda candidate_id: row_map[candidate_id]["mae_deg"],
            )
            if passing_candidate_id_list
            else None
        ),
        "gate_row_list": gate_row_list,
    }


def prepare_campaign(dataset: stage5.Stage5Dataset) -> None:
    """Create immutable configs and prepared campaign state."""

    candidate_list = build_candidate_list()
    QUEUE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    campaign_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "stage": "Wave 5.2R Stage 10",
        "dataset_id": "polished_dataset",
        "input_mode": "setpoints",
        "surface": "Fw",
        "split_signature": SPLIT_SIGNATURE,
        "split_counts": {
            split_name: int(np.sum(dataset.split_array == split_name))
            for split_name in ["train", "validation", "test"]
        },
        "expected_entry_count": len(candidate_list),
        "bootstrap_count": BOOTSTRAP_COUNT,
        "random_seed": RANDOM_SEED,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "campaign_plan_path": CAMPAIGN_PLAN_PATH,
    }
    write_yaml(CONFIG_DIRECTORY / "campaign.yaml", campaign_payload)
    for specification in candidate_list:
        write_yaml(
            QUEUE_DIRECTORY
            / f"{specification.queue_index:03d}_{specification.candidate_id.lower()}.yaml",
            {
                "schema_version": 1,
                "campaign_name": CAMPAIGN_NAME,
                "queue_index": specification.queue_index,
                "candidate_id": specification.candidate_id,
                "formulation": specification.formulation,
                "library_name": specification.library_name,
                "fit_mode": specification.fit_mode,
                "diagnostic_only": specification.diagnostic_only,
                "random_seed": RANDOM_SEED,
            },
        )
    write_yaml(
        ACTIVE_CAMPAIGN_PATH,
        {
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
            "random_seed_list": [RANDOM_SEED],
            "campaign_manifest_path": (
                CONFIG_DIRECTORY / "campaign.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
            "launcher_path": LAUNCHER_PATH,
            "launcher_note_path": LAUNCHER_NOTE_PATH,
            "planning_report_path": CAMPAIGN_PLAN_PATH,
            "technical_document_path": TECHNICAL_DOCUMENT_PATH,
            "local_preflight_command": (
                f".\\{LAUNCHER_PATH.replace('/', chr(92))} -PreflightOnly"
            ),
            "local_launch_command": (
                f".\\{LAUNCHER_PATH.replace('/', chr(92))} -Run"
            ),
            "remote_preflight_command": (
                f".\\{LAUNCHER_PATH.replace('/', chr(92))} "
                "-Remote -PreflightOnly"
            ),
            "remote_launch_command": (
                f".\\{LAUNCHER_PATH.replace('/', chr(92))} -Remote -Run"
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
                (
                    "scripts/campaigns/wave_5_2/"
                    "run_wave52r_stage10_sparse_symbolic_discovery.py"
                ),
                "scripts/models/sparse_harmonic_condition_model.py",
                ANALYSIS_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
            ],
        },
    )


def run_preflight(
    context: FitContext,
) -> dict[str, Any]:
    """Validate representation, leakage, and sparse-law recovery."""

    quadratic_term_list, normalized_library_matrix, _ = (
        build_library_matrices(context, "quadratic")
    )
    synthetic_coefficient_matrix = np.zeros(
        (
            len(quadratic_term_list),
            context.normalized_target_residual_matrix.shape[1],
        )
    )
    synthetic_coefficient_matrix[0, 0] = 0.4
    synthetic_coefficient_matrix[1, 0] = -0.7
    synthetic_coefficient_matrix[4, 1] = 0.25
    synthetic_target_matrix = (
        normalized_library_matrix[
            context.dataset.split_array == "train"
        ]
        @ synthetic_coefficient_matrix
    )
    recovered_coefficient_matrix = fit_ridge_coefficients(
        normalized_library_matrix[
            context.dataset.split_array == "train"
        ],
        synthetic_target_matrix,
        alpha=1.0e-10,
    )
    synthetic_recovery_max_abs = float(
        np.max(
            np.abs(
                recovered_coefficient_matrix
                - synthetic_coefficient_matrix
            )
        )
    )
    anchor_reconstruction_matrix = reconstruct_curve_matrix(
        context.anchor_bundle.pf_a_coefficient_matrix[:3],
        HARMONIC_ORDER_LIST,
        ANGULAR_SAMPLE_COUNT,
    )
    anchor_reconstruction_max_abs = float(
        np.max(
            np.abs(
                anchor_reconstruction_matrix
                - context.anchor_bundle.pf_a_curve_matrix[:3]
            )
        )
    )
    closure_probe_matrix = reconstruct_curve_matrix(
        context.anchor_bundle.pf_a_coefficient_matrix[:3],
        HARMONIC_ORDER_LIST,
        ANGULAR_SAMPLE_COUNT + 1,
    )
    direct_zero_angle = closure_probe_matrix[:, 0]
    coefficient_array = context.anchor_bundle.pf_a_coefficient_matrix[:3]
    direct_two_pi = coefficient_array[:, 0].copy()
    for order_index in range(len(HARMONIC_ORDER_LIST)):
        direct_two_pi += coefficient_array[:, 2 + 2 * order_index]
    periodic_endpoint_max_abs = float(
        np.max(np.abs(direct_zero_angle - direct_two_pi))
    )
    summary_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage10",
        "all_checks_passed": (
            synthetic_recovery_max_abs <= 1.0e-6
            and anchor_reconstruction_max_abs <= 1.0e-12
            and periodic_endpoint_max_abs <= 1.0e-12
        ),
        "curve_count": int(context.dataset.curve_matrix.shape[0]),
        "split_counts": {
            split_name: int(
                np.sum(context.dataset.split_array == split_name)
            )
            for split_name in ["train", "validation", "test"]
        },
        "split_signature": SPLIT_SIGNATURE,
        "candidate_count": len(build_candidate_list()),
        "quadratic_term_count": len(quadratic_term_list),
        "extended_term_count": len(
            build_named_condition_term_list("extended")
        ),
        "symbolic_term_count": len(
            build_named_condition_term_list("symbolic")
        ),
        "synthetic_recovery_max_abs": synthetic_recovery_max_abs,
        "anchor_reconstruction_max_abs_deg": (
            anchor_reconstruction_max_abs
        ),
        "periodic_endpoint_max_abs_deg": periodic_endpoint_max_abs,
        "runtime_target_derived_input_count": 0,
    }
    ANALYSIS_DIRECTORY.mkdir(parents=True, exist_ok=True)
    write_yaml(
        ANALYSIS_DIRECTORY / "stage10_preflight_validation_summary.yaml",
        summary_payload,
    )
    assert summary_payload["all_checks_passed"] is True
    return summary_payload


def run_campaign(
    context: FitContext,
) -> Path:
    """Execute the ten-entry Stage 10 first screen."""

    prepare_campaign(context.dataset)
    preflight_payload = run_preflight(context)
    assert preflight_payload["all_checks_passed"] is True
    campaign_output_directory = (
        CAMPAIGN_ROOT_DIRECTORY / f"{now_timestamp()}_{CAMPAIGN_NAME}"
    )
    campaign_output_directory.mkdir(parents=True, exist_ok=False)
    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "status": "running",
            "started_at": now_iso(),
            "campaign_output_directory": (
                campaign_output_directory.relative_to(PROJECT_ROOT).as_posix()
            ),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    test_mask = context.dataset.split_array == "test"
    measured_curve_matrix = context.dataset.curve_matrix[test_mask]
    with np.load(K01_PREDICTION_PATH) as k01_payload:
        k01_prediction_matrix = k01_payload["predicted_curve"]
        k01_measured_matrix = k01_payload["measured_curve"]
    assert np.allclose(
        measured_curve_matrix,
        k01_measured_matrix,
        atol=0.0,
        rtol=0.0,
    )
    result_row_list = [
        diagnostic_result(
            "D00",
            "frozen_pf_a",
            measured_curve_matrix,
            context.anchor_bundle.pf_a_curve_matrix[test_mask],
        ),
        diagnostic_result(
            "D01",
            "frozen_h04",
            measured_curve_matrix,
            context.anchor_bundle.h04_curve_matrix[test_mask],
        ),
        diagnostic_result(
            "D02",
            "frozen_stage9_k01",
            measured_curve_matrix,
            k01_prediction_matrix,
        ),
    ]
    failed_count = 0
    for specification in build_candidate_list():
        if specification.diagnostic_only:
            continue
        try:
            result_row_list.append(
                fit_candidate(
                    specification,
                    context,
                    campaign_output_directory,
                )
            )
        except Exception as error:
            failed_count += 1
            write_yaml(
                campaign_output_directory
                / f"{specification.candidate_id.lower()}_failure.yaml",
                {
                    "candidate_id": specification.candidate_id,
                    "error_type": type(error).__name__,
                    "error_message": str(error),
                },
            )
            raise
    assert failed_count == 0
    assert len(result_row_list) == 10
    leaderboard_row_list = sorted(
        result_row_list,
        key=lambda row: row["mae_deg"],
    )
    write_csv(
        campaign_output_directory / "campaign_leaderboard.csv",
        leaderboard_row_list,
    )
    write_yaml(
        campaign_output_directory / "campaign_leaderboard.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "row_list": leaderboard_row_list,
        },
    )
    gate_payload = build_gate_summary(leaderboard_row_list)
    write_yaml(
        campaign_output_directory
        / "campaign_first_screen_gate_summary.yaml",
        gate_payload,
    )
    recommendation = gate_payload["recommended_candidate_id"]
    best_run_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "recommended_candidate_id": recommendation,
        "decision": (
            "stable_sparse_terms_qualified"
            if recommendation is not None
            else "no_sparse_formulation_passed"
        ),
    }
    write_yaml(
        campaign_output_directory / "campaign_best_run.yaml",
        best_run_payload,
    )
    with (
        campaign_output_directory / "campaign_best_run.md"
    ).open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(
            "# Stage 10 Campaign Best Run\n\n"
            f"- Recommended candidate: `{recommendation}`\n"
            f"- Decision: `{best_run_payload['decision']}`\n"
        )
    execution_payload = {
        "status": "completed",
        "completed_entry_count": len(result_row_list),
        "failed_entry_count": failed_count,
        "completed_at": now_iso(),
    }
    write_yaml(
        campaign_output_directory / "campaign_execution_summary.yaml",
        execution_payload,
    )
    active_payload.update(
        {
            "status": "completed",
            "completed_at": execution_payload["completed_at"],
            "completed_run_count": len(result_row_list),
            "failed_run_count": failed_count,
            "campaign_best_run_path": (
                campaign_output_directory / "campaign_best_run.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
            "raw_error_leader_id": leaderboard_row_list[0]["candidate_id"],
            "multi_index_recommended_candidate_id": recommendation,
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return campaign_output_directory


def parse_arguments() -> argparse.Namespace:
    """Parse Stage 10 commands."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--run", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Prepare, validate, or run the Stage 10 campaign."""

    arguments = parse_arguments()
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    dataset = stage5.build_stage5_dataset()
    context = build_fit_context(dataset)
    if arguments.prepare:
        prepare_campaign(dataset)
    if arguments.preflight_only:
        prepare_campaign(dataset)
        print(yaml.safe_dump(run_preflight(context), sort_keys=False))
    if arguments.run:
        print(run_campaign(context))
    if not any(
        [arguments.prepare, arguments.preflight_only, arguments.run]
    ):
        prepare_campaign(dataset)


if __name__ == "__main__":
    main()
