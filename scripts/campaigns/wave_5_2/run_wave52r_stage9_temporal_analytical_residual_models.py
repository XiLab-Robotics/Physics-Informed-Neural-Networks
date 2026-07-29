"""Run Wave 5.2R Stage 9 causal temporal analytical-residual models."""

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
import torch
import yaml

# Make Direct Script Execution Resolve The Repository Package
PROJECT_IMPORT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_IMPORT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_IMPORT_ROOT))

# Import Project Models
from scripts.models.causal_temporal_analytical_residual_network import (
    CausalTemporalAnalyticalResidualNetwork,
)
from scripts.models.periodic_temporal_sequence_network import (
    PeriodicTemporalSequenceNetwork,
)

# Import Prior Wave 5.2R Campaign Utilities
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage7_mean_centered_shape_multi_head as stage7,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage8_weak_forward_compliance_priors as stage8,
)


# Define Campaign Constants
PROJECT_ROOT = Path(__file__).resolve().parents[3]
STAGE_NAME = "wave52r_stage9_temporal_analytical_residual_models"
CAMPAIGN_NAME = f"{STAGE_NAME}_2026_07_29"
SPLIT_SIGNATURE = stage5.SPLIT_SIGNATURE
ANGULAR_SAMPLE_COUNT = stage5.ANGULAR_SAMPLE_COUNT
FIRST_SCREEN_SEED = 314159
STABILITY_SEED_LIST = [271828, 161803]
MAXIMUM_EPOCH_COUNT = 48
MINIMUM_EPOCH_COUNT = 12
EARLY_STOPPING_PATIENCE = 8
CURVE_BATCH_SIZE = 16
DEFAULT_CHUNK_LENGTH = 33
HIDDEN_SIZE = 128
NUM_LAYERS = 2
LEARNING_RATE = 5.0e-4
H04_CHECKPOINT_PATH = stage8.H04_CHECKPOINT_PATH
ACCEPTED_GRU_CHECKPOINT_PATH = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "periodic_gru_sequence"
    / "2026-07-08-22-57-44__te_periodic_gru_sequence_fw__polished_setpoints"
    / "checkpoints"
    / "periodic_gru_sequence-epoch=091-val_mae=0.00183161.ckpt"
)
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage9_temporal_analytical_residual_models"
)
CONFIG_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "temporal_analytical_residual_models"
    / "campaigns"
    / "2026-07-29_wave52r_stage9_temporal_analytical_residual_models"
)
QUEUE_DIRECTORY = CONFIG_DIRECTORY / "queue"
RUN_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "temporal_analytical_residual_models"
)
CAMPAIGN_ROOT_DIRECTORY = PROJECT_ROOT / "output" / "training_campaigns"
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-29/"
    "2026-07-29-18-35-28_wave52r_stage9_temporal_"
    "analytical_residual_models.md"
)
CAMPAIGN_PLAN_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "temporal_analytical_residual_models/"
    "2026-07-29-18-35-28_wave52r_stage9_temporal_"
    "analytical_residual_models_campaign_plan_report.md"
)
LAUNCHER_PATH = (
    "scripts/campaigns/wave_5_2/"
    "run_wave52r_stage9_temporal_analytical_residual_models.ps1"
)
LAUNCHER_NOTE_PATH = (
    "doc/scripts/campaigns/wave_5_2/"
    "run_wave52r_stage9_temporal_analytical_residual_models.md"
)


@dataclass(frozen=True)
class CandidateSpecification:
    """Describe one immutable Stage 9 candidate."""

    queue_index: int
    candidate_id: str
    formulation: str
    anchor_name: str
    residual_mode: str
    diagnostic_only: bool = False
    shuffled_training_order: bool = False
    curriculum_chunk_length: bool = False


@dataclass
class AnchorBundle:
    """Hold aligned PF-A and H04 anchor artifacts."""

    pf_a_curve_matrix: np.ndarray
    pf_a_coefficient_matrix: np.ndarray
    h04_curve_matrix: np.ndarray
    h04_coefficient_matrix: np.ndarray
    h04_mean_curve_matrix: np.ndarray


def now_iso() -> str:
    """Return one timezone-aware local timestamp."""

    return datetime.now().astimezone().isoformat(timespec="seconds")


def now_timestamp() -> str:
    """Return one sortable local timestamp."""

    return datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")


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


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def seed_everything(random_seed: int) -> None:
    """Seed Python, NumPy, CPU, and CUDA deterministically."""

    random.seed(random_seed)
    np.random.seed(random_seed)
    torch.manual_seed(random_seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(random_seed)
    torch.use_deterministic_algorithms(True, warn_only=True)


def build_candidate_list() -> list[CandidateSpecification]:
    """Return the approved ten-candidate first-screen matrix."""

    return [
        CandidateSpecification(
            1,
            "D00",
            "frozen_h04",
            "h04",
            "point",
            diagnostic_only=True,
        ),
        CandidateSpecification(
            2,
            "G00",
            "accepted_periodic_gru_replay",
            "none",
            "point",
            diagnostic_only=True,
        ),
        CandidateSpecification(
            3,
            "C00",
            "causal_periodic_gru",
            "zero",
            "point",
        ),
        CandidateSpecification(
            4,
            "R00",
            "parameter_matched_zero_anchor_residual_gru",
            "zero",
            "point",
        ),
        CandidateSpecification(
            5,
            "P01",
            "pf_a_causal_residual_gru",
            "pf_a",
            "point",
        ),
        CandidateSpecification(
            6,
            "H01",
            "h04_causal_residual_gru",
            "h04",
            "point",
        ),
        CandidateSpecification(
            7,
            "K01",
            "h04_coefficient_residual_gru",
            "h04",
            "coefficient",
        ),
        CandidateSpecification(
            8,
            "M01",
            "h04_static_mean_temporal_shape_gru",
            "h04_mean",
            "point",
        ),
        CandidateSpecification(
            9,
            "L01",
            "h04_context_curriculum_residual_gru",
            "h04",
            "point",
            curriculum_chunk_length=True,
        ),
        CandidateSpecification(
            10,
            "N01",
            "h04_shuffled_angular_order_residual_gru",
            "h04",
            "point",
            shuffled_training_order=True,
        ),
    ]


def build_anchor_bundle(
    dataset: stage5.Stage5Dataset,
) -> AnchorBundle:
    """Reconstruct aligned PF-A and frozen H04 anchor artifacts."""

    pf_a_coefficient_matrix = dataset.anchor_coefficient_map["core"]
    pf_a_curve_matrix = np.vstack(
        [
            stage5._reconstruct_numpy_curve(
                coefficient_array,
                stage5.CORE_ORDER_LIST,
            )
            for coefficient_array in pf_a_coefficient_matrix
        ]
    )
    diagnostic_specification = build_candidate_list()[0]
    h04_model = stage8.build_model(
        stage8.build_candidate_list()[0],
        dataset,
    )
    h04_model.eval()
    normalized_condition_tensor = torch.as_tensor(
        (
            dataset.condition_matrix - dataset.feature_mean
        )
        / dataset.feature_scale,
        dtype=torch.float32,
    )
    anchor_coefficient_tensor = torch.as_tensor(
        pf_a_coefficient_matrix,
        dtype=torch.float32,
    )
    with torch.no_grad():
        output = h04_model(
            normalized_condition_tensor,
            anchor_coefficient_tensor,
        )
    h04_curve_matrix = (
        output["prediction_curve"].detach().cpu().numpy().astype(np.float64)
    )
    h04_coefficient_matrix = (
        output["prediction_coefficients"]
        .detach()
        .cpu()
        .numpy()
        .astype(np.float64)
    )
    assert diagnostic_specification.candidate_id == "D00"
    assert h04_curve_matrix.shape == dataset.curve_matrix.shape
    assert h04_coefficient_matrix.shape == pf_a_coefficient_matrix.shape
    h04_mean_curve_matrix = np.repeat(
        h04_coefficient_matrix[:, :1],
        ANGULAR_SAMPLE_COUNT,
        axis=1,
    )
    return AnchorBundle(
        pf_a_curve_matrix=pf_a_curve_matrix,
        pf_a_coefficient_matrix=pf_a_coefficient_matrix,
        h04_curve_matrix=h04_curve_matrix,
        h04_coefficient_matrix=h04_coefficient_matrix,
        h04_mean_curve_matrix=h04_mean_curve_matrix,
    )


def anchor_arrays_for_candidate(
    specification: CandidateSpecification,
    anchor_bundle: AnchorBundle,
) -> tuple[np.ndarray, np.ndarray | None]:
    """Resolve one candidate's aligned anchor arrays."""

    if specification.anchor_name == "zero":
        return (
            np.zeros_like(anchor_bundle.h04_curve_matrix),
            None,
        )
    if specification.anchor_name == "pf_a":
        return (
            anchor_bundle.pf_a_curve_matrix,
            anchor_bundle.pf_a_coefficient_matrix,
        )
    if specification.anchor_name == "h04":
        return (
            anchor_bundle.h04_curve_matrix,
            anchor_bundle.h04_coefficient_matrix,
        )
    if specification.anchor_name == "h04_mean":
        return (
            anchor_bundle.h04_mean_curve_matrix,
            anchor_bundle.h04_coefficient_matrix,
        )
    raise AssertionError(
        f"Unsupported anchor name | {specification.anchor_name}"
    )


def build_model(
    specification: CandidateSpecification,
    dataset: stage5.Stage5Dataset,
) -> CausalTemporalAnalyticalResidualNetwork:
    """Build one Stage 9 causal GRU."""

    coefficient_bound_tensor = torch.as_tensor(
        dataset.correction_bound_map["core"],
        dtype=torch.float32,
    )
    point_bound = (
        0.12
        if specification.anchor_name == "zero"
        or specification.anchor_name == "h04_mean"
        else 0.025
    )
    return CausalTemporalAnalyticalResidualNetwork(
        condition_feature_mean=torch.as_tensor(
            dataset.feature_mean,
            dtype=torch.float32,
        ),
        condition_feature_scale=torch.as_tensor(
            dataset.feature_scale,
            dtype=torch.float32,
        ),
        harmonic_order_list=stage5.CORE_ORDER_LIST,
        hidden_size=HIDDEN_SIZE,
        num_layers=NUM_LAYERS,
        residual_mode=specification.residual_mode,
        point_residual_bound_deg=point_bound,
        coefficient_residual_bound=coefficient_bound_tensor,
        use_bounded_output=True,
    )


def load_accepted_periodic_gru(
    device: torch.device,
) -> tuple[
    PeriodicTemporalSequenceNetwork,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
]:
    """Reconstruct the accepted historical periodic GRU checkpoint."""

    checkpoint_payload = torch.load(
        ACCEPTED_GRU_CHECKPOINT_PATH,
        map_location="cpu",
        weights_only=False,
    )
    model = PeriodicTemporalSequenceNetwork(
        temporal_model_type="gru_sequence",
        input_size=5,
        output_size=1,
        harmonic_order=240,
        harmonic_index_list=[0, *stage5.CORE_ORDER_LIST],
        include_raw_angle_feature=True,
        hidden_size=128,
        num_layers=2,
        dropout_probability=0.10,
        bidirectional=False,
        readout_position="center",
    )
    model_state_dictionary = {
        key.removeprefix("regression_model."): value
        for key, value in checkpoint_payload["state_dict"].items()
        if key.startswith("regression_model.")
    }
    model.load_state_dict(model_state_dictionary, strict=True)
    model.eval()
    return (
        model.to(device),
        checkpoint_payload["state_dict"]["input_feature_mean"].to(device),
        checkpoint_payload["state_dict"]["input_feature_std"].to(device),
        checkpoint_payload["state_dict"]["target_mean"].to(device),
        checkpoint_payload["state_dict"]["target_std"].to(device),
    )


def replay_accepted_periodic_gru(
    dataset: stage5.Stage5Dataset,
    split_name: str,
    device: torch.device,
) -> np.ndarray:
    """Replay the centered-window accepted GRU on Stage 0 curves."""

    (
        model,
        input_feature_mean,
        input_feature_std,
        target_mean,
        target_std,
    ) = load_accepted_periodic_gru(device)
    split_index_array = np.flatnonzero(dataset.split_array == split_name)
    angular_position_array = np.linspace(
        0.0,
        360.0,
        ANGULAR_SAMPLE_COUNT,
        endpoint=False,
        dtype=np.float32,
    )
    centered_offset_array = np.arange(-16, 17, dtype=np.int64)
    centered_index_matrix = (
        np.arange(ANGULAR_SAMPLE_COUNT, dtype=np.int64)[:, None]
        + centered_offset_array[None, :]
    ) % ANGULAR_SAMPLE_COUNT
    prediction_curve_list: list[np.ndarray] = []
    for dataset_index in split_index_array:
        torque_nm, speed_rpm, temperature_deg_c = (
            dataset.condition_matrix[dataset_index]
        )
        raw_feature_matrix = np.column_stack(
            [
                angular_position_array,
                np.full(
                    ANGULAR_SAMPLE_COUNT,
                    abs(speed_rpm),
                    dtype=np.float32,
                ),
                np.full(
                    ANGULAR_SAMPLE_COUNT,
                    abs(torque_nm),
                    dtype=np.float32,
                ),
                np.full(
                    ANGULAR_SAMPLE_COUNT,
                    temperature_deg_c,
                    dtype=np.float32,
                ),
                np.ones(
                    ANGULAR_SAMPLE_COUNT,
                    dtype=np.float32,
                ),
            ]
        )
        raw_window_tensor = torch.as_tensor(
            raw_feature_matrix[centered_index_matrix],
            dtype=torch.float32,
            device=device,
        )
        normalized_window_tensor = (
            raw_window_tensor - input_feature_mean.view(1, 1, -1)
        ) / input_feature_std.view(1, 1, -1)
        prediction_batch_list: list[torch.Tensor] = []
        with torch.no_grad():
            for start_index in range(0, ANGULAR_SAMPLE_COUNT, 512):
                end_index = min(
                    start_index + 512,
                    ANGULAR_SAMPLE_COUNT,
                )
                normalized_prediction = model.forward_with_input_context(
                    raw_window_tensor[start_index:end_index],
                    normalized_window_tensor[start_index:end_index],
                )
                prediction_batch_list.append(
                    normalized_prediction * target_std + target_mean
                )
        prediction_curve = (
            torch.cat(prediction_batch_list, dim=0)
            .squeeze(-1)
            .detach()
            .cpu()
            .numpy()
        )
        prediction_curve_list.append(prediction_curve)
    return np.vstack(prediction_curve_list)


def curve_first_loss(
    prediction_tensor: torch.Tensor,
    target_tensor: torch.Tensor,
    residual_tensor: torch.Tensor,
) -> tuple[torch.Tensor, dict[str, float]]:
    """Compute the shared raw, mean, shape, and residual objective."""

    raw_loss = torch.mean(torch.abs(prediction_tensor - target_tensor))
    prediction_mean = torch.mean(prediction_tensor, dim=1, keepdim=True)
    target_mean = torch.mean(target_tensor, dim=1, keepdim=True)
    mean_loss = torch.mean(torch.abs(prediction_mean - target_mean))
    shape_loss = torch.mean(
        torch.abs(
            (prediction_tensor - prediction_mean)
            - (target_tensor - target_mean)
        )
    )
    residual_rms = torch.sqrt(torch.mean(residual_tensor**2) + 1.0e-12)
    total_loss = (
        raw_loss
        + 0.50 * mean_loss
        + 0.25 * shape_loss
        + 1.0e-4 * residual_rms
    )
    return total_loss, {
        "raw_loss_deg": float(raw_loss.detach().cpu()),
        "mean_loss_deg": float(mean_loss.detach().cpu()),
        "shape_loss_deg": float(shape_loss.detach().cpu()),
        "residual_rms_deg": float(residual_rms.detach().cpu()),
        "total_loss": float(total_loss.detach().cpu()),
    }


def curriculum_chunk_length(epoch_index: int) -> int:
    """Resolve the Stage 9 causal processing curriculum."""

    if epoch_index < MAXIMUM_EPOCH_COUNT // 3:
        return 9
    if epoch_index < (2 * MAXIMUM_EPOCH_COUNT) // 3:
        return 17
    return DEFAULT_CHUNK_LENGTH


def predict_model(
    model: CausalTemporalAnalyticalResidualNetwork,
    condition_tensor: torch.Tensor,
    anchor_curve_tensor: torch.Tensor,
    anchor_coefficient_tensor: torch.Tensor | None,
    angular_position_tensor: torch.Tensor,
    chunk_length: int,
) -> tuple[np.ndarray, np.ndarray, dict[str, float]]:
    """Predict one split and calculate recurrent-state diagnostics."""

    model.eval()
    prediction_list: list[np.ndarray] = []
    residual_list: list[np.ndarray] = []
    hidden_norm_list: list[float] = []
    reset_difference_list: list[float] = []
    chunk_difference_list: list[float] = []
    with torch.no_grad():
        for batch_start in range(0, condition_tensor.shape[0], 16):
            batch_end = min(batch_start + 16, condition_tensor.shape[0])
            batch_condition = condition_tensor[batch_start:batch_end]
            batch_anchor = anchor_curve_tensor[batch_start:batch_end]
            batch_coefficient = (
                None
                if anchor_coefficient_tensor is None
                else anchor_coefficient_tensor[batch_start:batch_end]
            )
            batch_angle = angular_position_tensor[batch_start:batch_end]
            chunk_output = model.forward_in_chunks(
                batch_angle,
                batch_condition,
                batch_anchor,
                batch_coefficient,
                chunk_length=chunk_length,
            )
            repeated_output = model.forward_in_chunks(
                batch_angle,
                batch_condition,
                batch_anchor,
                batch_coefficient,
                chunk_length=chunk_length,
            )
            one_pass_output = model.forward_sequence(
                batch_angle,
                batch_condition,
                batch_anchor,
                batch_coefficient,
            )
            prediction_list.append(
                chunk_output["prediction_curve"].cpu().numpy()
            )
            residual_list.append(
                chunk_output["residual_curve"].cpu().numpy()
            )
            hidden_norm_list.append(
                float(
                    torch.linalg.vector_norm(
                        chunk_output["hidden_sequence"],
                        dim=-1,
                    )
                    .mean()
                    .cpu()
                )
            )
            reset_difference_list.append(
                float(
                    torch.max(
                        torch.abs(
                            chunk_output["prediction_curve"]
                            - repeated_output["prediction_curve"]
                        )
                    ).cpu()
                )
            )
            chunk_difference_list.append(
                float(
                    torch.max(
                        torch.abs(
                            chunk_output["prediction_curve"]
                            - one_pass_output["prediction_curve"]
                        )
                    ).cpu()
                )
            )
    prediction_matrix = np.vstack(prediction_list)
    residual_matrix = np.vstack(residual_list)
    recurrent_metric_payload = {
        "hidden_state_mean_norm": float(np.mean(hidden_norm_list)),
        "hidden_state_max_batch_mean_norm": float(
            np.max(hidden_norm_list)
        ),
        "reset_reproducibility_max_abs_deg": float(
            np.max(reset_difference_list)
        ),
        "chunk_equivalence_max_abs_deg": float(
            np.max(chunk_difference_list)
        ),
    }
    return prediction_matrix, residual_matrix, recurrent_metric_payload


def build_split_tensors(
    dataset: stage5.Stage5Dataset,
    anchor_curve_matrix: np.ndarray,
    anchor_coefficient_matrix: np.ndarray | None,
    split_name: str,
    device: torch.device,
) -> dict[str, torch.Tensor | None]:
    """Materialize one full-curve split for causal GRU training."""

    split_mask = dataset.split_array == split_name
    curve_count = int(np.sum(split_mask))
    angular_position_array = np.linspace(
        0.0,
        360.0,
        ANGULAR_SAMPLE_COUNT,
        endpoint=False,
        dtype=np.float32,
    )
    return {
        "condition": torch.as_tensor(
            dataset.condition_matrix[split_mask],
            dtype=torch.float32,
            device=device,
        ),
        "target": torch.as_tensor(
            dataset.curve_matrix[split_mask],
            dtype=torch.float32,
            device=device,
        ),
        "anchor": torch.as_tensor(
            anchor_curve_matrix[split_mask],
            dtype=torch.float32,
            device=device,
        ),
        "anchor_coefficient": (
            None
            if anchor_coefficient_matrix is None
            else torch.as_tensor(
                anchor_coefficient_matrix[split_mask],
                dtype=torch.float32,
                device=device,
            )
        ),
        "angle": torch.as_tensor(
            np.repeat(
                angular_position_array[None, :],
                curve_count,
                axis=0,
            ),
            dtype=torch.float32,
            device=device,
        ),
    }


def evaluate_trained_candidate(
    model: CausalTemporalAnalyticalResidualNetwork,
    test_batch: dict[str, torch.Tensor | None],
    measured_curve_matrix: np.ndarray,
    shuffled_index_array: np.ndarray,
) -> tuple[dict[str, float], np.ndarray, np.ndarray]:
    """Evaluate full curves and temporal-specificity diagnostics."""

    condition_tensor = test_batch["condition"]
    target_tensor = test_batch["target"]
    anchor_curve_tensor = test_batch["anchor"]
    angular_position_tensor = test_batch["angle"]
    anchor_coefficient_tensor = test_batch["anchor_coefficient"]
    assert isinstance(condition_tensor, torch.Tensor)
    assert isinstance(target_tensor, torch.Tensor)
    assert isinstance(anchor_curve_tensor, torch.Tensor)
    assert isinstance(angular_position_tensor, torch.Tensor)
    assert anchor_coefficient_tensor is None or isinstance(
        anchor_coefficient_tensor,
        torch.Tensor,
    )
    (
        prediction_matrix,
        residual_matrix,
        recurrent_metric_payload,
    ) = predict_model(
        model,
        condition_tensor,
        anchor_curve_tensor,
        anchor_coefficient_tensor,
        angular_position_tensor,
        DEFAULT_CHUNK_LENGTH,
    )
    metric_payload = stage7.evaluate_metrics(
        measured_curve_matrix,
        prediction_matrix,
    )
    inverse_index_array = np.argsort(shuffled_index_array)
    shuffled_index_tensor = torch.as_tensor(
        shuffled_index_array,
        dtype=torch.long,
        device=condition_tensor.device,
    )
    with torch.no_grad():
        shuffled_output = model.forward_in_chunks(
            angular_position_tensor.index_select(1, shuffled_index_tensor),
            condition_tensor,
            anchor_curve_tensor.index_select(1, shuffled_index_tensor),
            anchor_coefficient_tensor,
            chunk_length=DEFAULT_CHUNK_LENGTH,
        )
    shuffled_prediction_matrix = (
        shuffled_output["prediction_curve"]
        .detach()
        .cpu()
        .numpy()[:, inverse_index_array]
    )
    prefix_length_list = [1, 9, 17, 33, 129, 512, ANGULAR_SAMPLE_COUNT]
    metric_payload.update(
        {
            "residual_rms_deg": float(
                np.sqrt(np.mean(residual_matrix**2))
            ),
            "residual_abs_max_deg": float(
                np.max(np.abs(residual_matrix))
            ),
            "shuffled_order_prediction_difference_mae_deg": float(
                np.mean(
                    np.abs(
                        shuffled_prediction_matrix - prediction_matrix
                    )
                )
            ),
            **recurrent_metric_payload,
        }
    )
    for prefix_length in prefix_length_list:
        metric_payload[
            f"prefix_{prefix_length}_mae_deg"
        ] = float(
            np.mean(
                np.abs(
                    prediction_matrix[:, :prefix_length]
                    - measured_curve_matrix[:, :prefix_length]
                )
            )
        )
    return metric_payload, prediction_matrix, residual_matrix


def train_candidate(
    specification: CandidateSpecification,
    dataset: stage5.Stage5Dataset,
    anchor_bundle: AnchorBundle,
    campaign_output_directory: Path,
    random_seed: int,
) -> dict[str, Any]:
    """Train one Stage 9 candidate and persist immutable artifacts."""

    seed_everything(random_seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    anchor_curve_matrix, anchor_coefficient_matrix = (
        anchor_arrays_for_candidate(specification, anchor_bundle)
    )
    training_batch = build_split_tensors(
        dataset,
        anchor_curve_matrix,
        anchor_coefficient_matrix,
        "train",
        device,
    )
    validation_batch = build_split_tensors(
        dataset,
        anchor_curve_matrix,
        anchor_coefficient_matrix,
        "validation",
        device,
    )
    test_batch = build_split_tensors(
        dataset,
        anchor_curve_matrix,
        anchor_coefficient_matrix,
        "test",
        device,
    )
    model = build_model(specification, dataset).to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=LEARNING_RATE,
        weight_decay=1.0e-5,
    )
    shuffled_index_array = np.random.default_rng(
        FIRST_SCREEN_SEED + 901
    ).permutation(ANGULAR_SAMPLE_COUNT)
    shuffled_index_tensor = torch.as_tensor(
        shuffled_index_array,
        dtype=torch.long,
        device=device,
    )

    best_validation_score = float("inf")
    best_validation_mae = float("inf")
    best_epoch = -1
    best_state_dictionary: dict[str, torch.Tensor] | None = None
    patience_count = 0
    history_row_list: list[dict[str, Any]] = []
    training_curve_count = int(
        torch.as_tensor(training_batch["condition"]).shape[0]
    )
    for epoch_index in range(MAXIMUM_EPOCH_COUNT):
        model.train()
        epoch_permutation = torch.randperm(
            training_curve_count,
            device=device,
        )
        epoch_loss_list: list[float] = []
        epoch_raw_list: list[float] = []
        epoch_mean_list: list[float] = []
        epoch_shape_list: list[float] = []
        chunk_length = (
            curriculum_chunk_length(epoch_index)
            if specification.curriculum_chunk_length
            else DEFAULT_CHUNK_LENGTH
        )
        for batch_start in range(0, training_curve_count, CURVE_BATCH_SIZE):
            batch_index = epoch_permutation[
                batch_start : batch_start + CURVE_BATCH_SIZE
            ]
            batch_condition = torch.as_tensor(
                training_batch["condition"]
            ).index_select(0, batch_index)
            batch_target = torch.as_tensor(
                training_batch["target"]
            ).index_select(0, batch_index)
            batch_anchor = torch.as_tensor(
                training_batch["anchor"]
            ).index_select(0, batch_index)
            batch_angle = torch.as_tensor(
                training_batch["angle"]
            ).index_select(0, batch_index)
            batch_coefficient_source = training_batch[
                "anchor_coefficient"
            ]
            batch_coefficient = (
                None
                if batch_coefficient_source is None
                else torch.as_tensor(
                    batch_coefficient_source
                ).index_select(0, batch_index)
            )
            if specification.shuffled_training_order:
                batch_target = batch_target.index_select(
                    1,
                    shuffled_index_tensor,
                )
                batch_anchor = batch_anchor.index_select(
                    1,
                    shuffled_index_tensor,
                )
                batch_angle = batch_angle.index_select(
                    1,
                    shuffled_index_tensor,
                )
            optimizer.zero_grad(set_to_none=True)
            output = model.forward_in_chunks(
                batch_angle,
                batch_condition,
                batch_anchor,
                batch_coefficient,
                chunk_length=chunk_length,
                detach_hidden_between_chunks=True,
            )
            total_loss, component_payload = curve_first_loss(
                output["prediction_curve"],
                batch_target,
                output["residual_curve"],
            )
            total_loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            epoch_loss_list.append(component_payload["total_loss"])
            epoch_raw_list.append(component_payload["raw_loss_deg"])
            epoch_mean_list.append(component_payload["mean_loss_deg"])
            epoch_shape_list.append(component_payload["shape_loss_deg"])

        model.eval()
        validation_condition = torch.as_tensor(
            validation_batch["condition"]
        )
        validation_target = torch.as_tensor(
            validation_batch["target"]
        )
        validation_anchor = torch.as_tensor(
            validation_batch["anchor"]
        )
        validation_angle = torch.as_tensor(validation_batch["angle"])
        validation_coefficient = validation_batch["anchor_coefficient"]
        with torch.no_grad():
            validation_output = model.forward_in_chunks(
                validation_angle,
                validation_condition,
                validation_anchor,
                (
                    None
                    if validation_coefficient is None
                    else torch.as_tensor(validation_coefficient)
                ),
                chunk_length=DEFAULT_CHUNK_LENGTH,
            )
            validation_score, validation_component_payload = (
                curve_first_loss(
                    validation_output["prediction_curve"],
                    validation_target,
                    validation_output["residual_curve"],
                )
            )
        validation_score_value = float(validation_score.cpu())
        validation_mae = validation_component_payload["raw_loss_deg"]
        history_row_list.append(
            {
                "epoch": epoch_index + 1,
                "chunk_length": chunk_length,
                "training_total_loss": float(np.mean(epoch_loss_list)),
                "training_raw_mae_deg": float(np.mean(epoch_raw_list)),
                "training_mean_mae_deg": float(np.mean(epoch_mean_list)),
                "training_shape_mae_deg": float(np.mean(epoch_shape_list)),
                "validation_score": validation_score_value,
                "validation_curve_mae_deg": validation_mae,
            }
        )
        if validation_score_value < best_validation_score - 1.0e-9:
            best_validation_score = validation_score_value
            best_validation_mae = validation_mae
            best_epoch = epoch_index + 1
            best_state_dictionary = {
                name: value.detach().cpu().clone()
                for name, value in model.state_dict().items()
            }
            patience_count = 0
        else:
            patience_count += 1
        if (
            epoch_index + 1 >= MINIMUM_EPOCH_COUNT
            and patience_count >= EARLY_STOPPING_PATIENCE
        ):
            break

    assert best_state_dictionary is not None
    model.load_state_dict(best_state_dictionary)
    test_mask = dataset.split_array == "test"
    (
        metric_payload,
        predicted_curve_matrix,
        residual_curve_matrix,
    ) = evaluate_trained_candidate(
        model,
        test_batch,
        dataset.curve_matrix[test_mask],
        shuffled_index_array,
    )
    seed_suffix = (
        ""
        if random_seed == FIRST_SCREEN_SEED
        else f"__seed_{random_seed}"
    )
    run_instance_id = (
        f"{now_timestamp()}__stage9_"
        f"{specification.candidate_id.lower()}{seed_suffix}"
    )
    run_directory = RUN_ROOT_DIRECTORY / run_instance_id
    run_directory.mkdir(parents=True, exist_ok=True)
    checkpoint_path = run_directory / "best_model.pt"
    torch.save(
        {
            "state_dict": best_state_dictionary,
            "candidate": specification.__dict__,
            "feature_mean": dataset.feature_mean,
            "feature_scale": dataset.feature_scale,
            "split_signature": SPLIT_SIGNATURE,
        },
        checkpoint_path,
    )
    write_csv(run_directory / "training_history.csv", history_row_list)
    np.savez_compressed(
        run_directory / "test_predictions.npz",
        measured_curve=dataset.curve_matrix[test_mask],
        predicted_curve=predicted_curve_matrix,
        anchor_curve=anchor_curve_matrix[test_mask],
        residual_curve=residual_curve_matrix,
    )
    result_payload = {
        "candidate_id": specification.candidate_id,
        "formulation": specification.formulation,
        "random_seed": random_seed,
        "run_instance_id": run_instance_id,
        "best_epoch": best_epoch,
        "best_validation_score": best_validation_score,
        "best_validation_mae_deg": best_validation_mae,
        "checkpoint_path": checkpoint_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "parameter_count": sum(
            parameter.numel() for parameter in model.parameters()
        ),
        "runtime_target_derived_input_count": 0,
        **metric_payload,
    }
    write_yaml(run_directory / "metrics_summary.yaml", result_payload)
    return result_payload


def diagnostic_result(
    candidate_id: str,
    formulation: str,
    measured_curve_matrix: np.ndarray,
    prediction_curve_matrix: np.ndarray,
    checkpoint_path: Path,
) -> dict[str, Any]:
    """Build one immutable diagnostic leaderboard result."""

    metric_payload = stage7.evaluate_metrics(
        measured_curve_matrix,
        prediction_curve_matrix,
    )
    metric_payload.update(
        {
            "residual_rms_deg": 0.0,
            "residual_abs_max_deg": 0.0,
            "shuffled_order_prediction_difference_mae_deg": 0.0,
            "hidden_state_mean_norm": 0.0,
            "hidden_state_max_batch_mean_norm": 0.0,
            "reset_reproducibility_max_abs_deg": 0.0,
            "chunk_equivalence_max_abs_deg": 0.0,
        }
    )
    for prefix_length in [1, 9, 17, 33, 129, 512, ANGULAR_SAMPLE_COUNT]:
        metric_payload[f"prefix_{prefix_length}_mae_deg"] = float(
            np.mean(
                np.abs(
                    prediction_curve_matrix[:, :prefix_length]
                    - measured_curve_matrix[:, :prefix_length]
                )
            )
        )
    return {
        "candidate_id": candidate_id,
        "formulation": formulation,
        "random_seed": FIRST_SCREEN_SEED,
        "run_instance_id": (
            "frozen_stage5_h04"
            if candidate_id == "D00"
            else "accepted_periodic_gru_replay"
        ),
        "best_epoch": 0,
        "best_validation_score": float("nan"),
        "best_validation_mae_deg": float("nan"),
        "checkpoint_path": checkpoint_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "parameter_count": 0 if candidate_id == "D00" else 157953,
        "runtime_target_derived_input_count": 0,
        **metric_payload,
    }


def candidate_gate_row(
    candidate_row: dict[str, Any],
    frozen_row: dict[str, Any],
    accepted_gru_row: dict[str, Any],
    control_row: dict[str, Any],
    shuffled_row: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate one complete Stage 9 first-screen gate."""

    preserved_tolerance = 1.02
    gate_row = {
        "candidate_id": candidate_row["candidate_id"],
        "all_first_screen_gates_passed": False,
        "raw_beats_h04": candidate_row["mae_deg"] < frozen_row["mae_deg"],
        "raw_beats_accepted_gru": (
            candidate_row["mae_deg"] < accepted_gru_row["mae_deg"]
        ),
        "raw_beats_control": (
            candidate_row["mae_deg"] < control_row["mae_deg"]
        ),
        "mean_beats_h04": (
            candidate_row["mean_mae_deg"]
            < frozen_row["mean_mae_deg"]
        ),
        "mean_beats_accepted_gru": (
            candidate_row["mean_mae_deg"]
            < accepted_gru_row["mean_mae_deg"]
        ),
        "mean_beats_control": (
            candidate_row["mean_mae_deg"]
            < control_row["mean_mae_deg"]
        ),
        "beats_shuffled_control": (
            candidate_row["mae_deg"] < shuffled_row["mae_deg"]
            and candidate_row["mean_mae_deg"]
            < shuffled_row["mean_mae_deg"]
        ),
        "shape_preserved": (
            candidate_row["centered_shape_mae_deg"]
            <= preserved_tolerance
            * min(
                frozen_row["centered_shape_mae_deg"],
                accepted_gru_row["centered_shape_mae_deg"],
            )
        ),
        "derivative_preserved": (
            candidate_row["sobolev_derivative_mae"]
            <= preserved_tolerance
            * min(
                frozen_row["sobolev_derivative_mae"],
                accepted_gru_row["sobolev_derivative_mae"],
            )
        ),
        "closure_preserved": (
            candidate_row["periodic_closure_error_deg"]
            <= preserved_tolerance
            * min(
                frozen_row["periodic_closure_error_deg"],
                accepted_gru_row["periodic_closure_error_deg"],
            )
        ),
        "amplitude_preserved": (
            candidate_row["retained_amplitude_mae_deg"]
            <= preserved_tolerance
            * min(
                frozen_row["retained_amplitude_mae_deg"],
                accepted_gru_row["retained_amplitude_mae_deg"],
            )
        ),
        "phase_preserved": (
            candidate_row["retained_phase_mae_rad"]
            <= preserved_tolerance
            * min(
                frozen_row["retained_phase_mae_rad"],
                accepted_gru_row["retained_phase_mae_rad"],
            )
        ),
        "p95_preserved": (
            candidate_row["per_curve_mae_p95"]
            <= preserved_tolerance
            * min(
                frozen_row["per_curve_mae_p95"],
                accepted_gru_row["per_curve_mae_p95"],
            )
        ),
        "reset_reproducible": (
            candidate_row["reset_reproducibility_max_abs_deg"] <= 1.0e-8
        ),
        "chunk_equivalent": (
            candidate_row["chunk_equivalence_max_abs_deg"] <= 1.0e-6
        ),
        "prefix_finite": all(
            np.isfinite(candidate_row[f"prefix_{length}_mae_deg"])
            for length in [1, 9, 17, 33, 129, 512, ANGULAR_SAMPLE_COUNT]
        ),
        "runtime_contract_passed": (
            candidate_row["runtime_target_derived_input_count"] == 0
        ),
    }
    gate_row["all_first_screen_gates_passed"] = all(
        value
        for key, value in gate_row.items()
        if key not in {"candidate_id", "all_first_screen_gates_passed"}
    )
    return gate_row


def build_gate_summary(
    leaderboard_row_list: list[dict[str, Any]],
) -> dict[str, Any]:
    """Build the Stage 9 first-screen gate summary."""

    row_map = {
        row["candidate_id"]: row for row in leaderboard_row_list
    }
    gate_candidate_id_list = ["P01", "H01", "K01", "M01", "L01"]
    gate_row_list = [
        candidate_gate_row(
            row_map[candidate_id],
            row_map["D00"],
            row_map["G00"],
            row_map["R00"],
            row_map["N01"],
        )
        for candidate_id in gate_candidate_id_list
    ]
    passing_candidate_id_list = [
        row["candidate_id"]
        for row in gate_row_list
        if row["all_first_screen_gates_passed"]
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
    """Prepare configs, queue, and persistent Stage 9 state."""

    candidate_list = build_candidate_list()
    QUEUE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    queue_path_list: list[str] = []
    for specification in candidate_list:
        queue_path = (
            QUEUE_DIRECTORY
            / f"{specification.queue_index:03d}_"
            f"{specification.candidate_id.lower()}.yaml"
        )
        write_yaml(
            queue_path,
            {
                "schema_version": 1,
                "campaign_name": CAMPAIGN_NAME,
                "candidate": specification.__dict__,
                "dataset": {
                    "dataset_id": "polished_dataset",
                    "input_mode": "setpoints",
                    "surface": "fw",
                    "curve_count": 966,
                    "split_counts": {
                        "train": 675,
                        "validation": 194,
                        "test": 97,
                    },
                    "split_signature": SPLIT_SIGNATURE,
                    "angular_sample_count": ANGULAR_SAMPLE_COUNT,
                },
                "training": {
                    "first_screen_seed": FIRST_SCREEN_SEED,
                    "conditional_stability_seed_list": STABILITY_SEED_LIST,
                    "maximum_epoch_count": MAXIMUM_EPOCH_COUNT,
                    "curve_batch_size": CURVE_BATCH_SIZE,
                    "processing_chunk_length": DEFAULT_CHUNK_LENGTH,
                },
            },
        )
        queue_path_list.append(
            queue_path.relative_to(PROJECT_ROOT).as_posix()
        )
    campaign_manifest_path = CONFIG_DIRECTORY / "campaign.yaml"
    write_yaml(
        campaign_manifest_path,
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "stage": "wave_5_2r_stage9",
            "candidate_count": len(candidate_list),
            "expected_first_screen_run_count": len(candidate_list),
            "queue_path_list": queue_path_list,
            "conditional_stability_seed_list": STABILITY_SEED_LIST,
            "technical_document_path": TECHNICAL_DOCUMENT_PATH,
            "campaign_plan_path": CAMPAIGN_PLAN_PATH,
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
        "random_seed_list": [FIRST_SCREEN_SEED],
        "conditional_stability_random_seed_list": STABILITY_SEED_LIST,
        "campaign_manifest_path": campaign_manifest_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
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
                "run_wave52r_stage9_temporal_analytical_residual_models.py"
            ),
            (
                "scripts/models/"
                "causal_temporal_analytical_residual_network.py"
            ),
            ANALYSIS_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
        ],
    }
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)


def run_preflight(
    dataset: stage5.Stage5Dataset,
    anchor_bundle: AnchorBundle,
) -> dict[str, Any]:
    """Run Stage 9 split, state, replay, and gradient preflight."""

    assert dataset.condition_matrix.shape == (966, 3)
    assert dataset.curve_matrix.shape == (966, ANGULAR_SAMPLE_COUNT)
    assert int(np.sum(dataset.split_array == "train")) == 675
    assert int(np.sum(dataset.split_array == "validation")) == 194
    assert int(np.sum(dataset.split_array == "test")) == 97
    assert H04_CHECKPOINT_PATH.is_file()
    assert ACCEPTED_GRU_CHECKPOINT_PATH.is_file()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    test_specification = next(
        item
        for item in build_candidate_list()
        if item.candidate_id == "H01"
    )
    model = build_model(test_specification, dataset).to(device)
    condition_tensor = torch.as_tensor(
        dataset.condition_matrix[:2],
        dtype=torch.float32,
        device=device,
    )
    angle_tensor = torch.as_tensor(
        np.repeat(
            np.linspace(
                0.0,
                360.0,
                65,
                endpoint=False,
                dtype=np.float32,
            )[None, :],
            2,
            axis=0,
        ),
        device=device,
    )
    anchor_tensor = torch.as_tensor(
        anchor_bundle.h04_curve_matrix[:2, :65],
        dtype=torch.float32,
        device=device,
    )
    coefficient_tensor = torch.as_tensor(
        anchor_bundle.h04_coefficient_matrix[:2],
        dtype=torch.float32,
        device=device,
    )
    output = model.forward_in_chunks(
        angle_tensor,
        condition_tensor,
        anchor_tensor,
        coefficient_tensor,
        chunk_length=17,
    )
    assert output["prediction_curve"].shape == (2, 65)
    assert torch.isfinite(output["prediction_curve"]).all()
    loss = torch.mean(output["prediction_curve"] ** 2)
    loss.backward()
    gradient_is_finite = all(
        parameter.grad is None
        or bool(torch.isfinite(parameter.grad).all())
        for parameter in model.parameters()
    )
    assert gradient_is_finite
    model.eval()
    with torch.no_grad():
        repeated_output = model.forward_in_chunks(
            angle_tensor,
            condition_tensor,
            anchor_tensor,
            coefficient_tensor,
            chunk_length=17,
        )
        one_pass_output = model.forward_sequence(
            angle_tensor,
            condition_tensor,
            anchor_tensor,
            coefficient_tensor,
        )
    reset_difference = float(
        torch.max(
            torch.abs(
                output["prediction_curve"].detach()
                - repeated_output["prediction_curve"]
            )
        ).cpu()
    )
    chunk_difference = float(
        torch.max(
            torch.abs(
                repeated_output["prediction_curve"]
                - one_pass_output["prediction_curve"]
            )
        ).cpu()
    )
    assert reset_difference <= 1.0e-8
    assert chunk_difference <= 1.0e-6
    accepted_replay = replay_accepted_periodic_gru(
        dataset,
        "test",
        device,
    )
    assert accepted_replay.shape == (97, ANGULAR_SAMPLE_COUNT)
    assert np.isfinite(accepted_replay).all()
    summary_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage9",
        "all_checks_passed": True,
        "curve_count": 966,
        "split_counts": {
            "train": 675,
            "validation": 194,
            "test": 97,
        },
        "split_signature": SPLIT_SIGNATURE,
        "candidate_count": len(build_candidate_list()),
        "accepted_gru_replay_shape": list(accepted_replay.shape),
        "accepted_gru_historical_split_counts": [1356, 388, 194],
        "accepted_gru_is_external_benchmark": True,
        "explicit_zero_state_shape": [
            NUM_LAYERS,
            2,
            HIDDEN_SIZE,
        ],
        "reset_reproducibility_max_abs_deg": reset_difference,
        "chunk_equivalence_max_abs_deg": chunk_difference,
        "finite_gradient_check_passed": gradient_is_finite,
        "runtime_target_derived_input_count": 0,
        "device": str(device),
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage9_preflight_validation_summary.yaml",
        summary_payload,
    )
    return summary_payload


def run_campaign(
    dataset: stage5.Stage5Dataset,
    anchor_bundle: AnchorBundle,
) -> Path:
    """Execute the bounded Stage 9 first screen and conditional stability."""

    prepare_campaign(dataset)
    preflight_payload = run_preflight(dataset, anchor_bundle)
    assert preflight_payload["all_checks_passed"] is True
    campaign_output_directory = (
        CAMPAIGN_ROOT_DIRECTORY
        / f"{now_timestamp()}_{CAMPAIGN_NAME}"
    )
    campaign_output_directory.mkdir(parents=True, exist_ok=False)
    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "status": "running",
            "started_at": now_iso(),
            "campaign_output_directory": campaign_output_directory.relative_to(
                PROJECT_ROOT
            ).as_posix(),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)

    test_mask = dataset.split_array == "test"
    measured_curve_matrix = dataset.curve_matrix[test_mask]
    h04_prediction_matrix = anchor_bundle.h04_curve_matrix[test_mask]
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    accepted_gru_prediction_matrix = replay_accepted_periodic_gru(
        dataset,
        "test",
        device,
    )
    result_row_list = [
        diagnostic_result(
            "D00",
            "frozen_h04",
            measured_curve_matrix,
            h04_prediction_matrix,
            H04_CHECKPOINT_PATH,
        ),
        diagnostic_result(
            "G00",
            "accepted_periodic_gru_replay",
            measured_curve_matrix,
            accepted_gru_prediction_matrix,
            ACCEPTED_GRU_CHECKPOINT_PATH,
        ),
    ]
    np.savez_compressed(
        ANALYSIS_DIRECTORY / "stage9_accepted_gru_replay.npz",
        measured_curve=measured_curve_matrix,
        predicted_curve=accepted_gru_prediction_matrix,
    )

    first_screen_failed_count = 0
    trainable_specification_list = [
        item
        for item in build_candidate_list()
        if not item.diagnostic_only
    ]
    for specification in trainable_specification_list:
        try:
            result_row_list.append(
                train_candidate(
                    specification,
                    dataset,
                    anchor_bundle,
                    campaign_output_directory,
                    FIRST_SCREEN_SEED,
                )
            )
        except Exception as error:
            first_screen_failed_count += 1
            write_yaml(
                campaign_output_directory
                / f"{specification.candidate_id.lower()}_failure.yaml",
                {
                    "candidate_id": specification.candidate_id,
                    "error_type": type(error).__name__,
                    "error_message": str(error),
                },
            )

    assert first_screen_failed_count == 0
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

    stability_row_list: list[dict[str, Any]] = []
    passing_candidate_id_set = set(
        gate_payload["passing_candidate_id_list"]
    )
    for specification in trainable_specification_list:
        if specification.candidate_id not in passing_candidate_id_set:
            continue
        for stability_seed in STABILITY_SEED_LIST:
            stability_row_list.append(
                train_candidate(
                    specification,
                    dataset,
                    anchor_bundle,
                    campaign_output_directory,
                    stability_seed,
                )
            )
    if stability_row_list:
        write_csv(
            campaign_output_directory / "campaign_stability_results.csv",
            stability_row_list,
        )
        write_yaml(
            campaign_output_directory / "campaign_stability_results.yaml",
            {
                "schema_version": 1,
                "row_list": stability_row_list,
            },
        )

    recommended_candidate_id = gate_payload[
        "recommended_candidate_id"
    ]
    best_run_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "recommended_candidate_id": recommended_candidate_id,
        "decision": (
            "conditional_candidate_requires_stability_review"
            if recommended_candidate_id is not None
            else "no_first_screen_candidate_passed"
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
            "# Stage 9 Campaign Best Run\n\n"
            f"- Recommended candidate: `{recommended_candidate_id}`\n"
            f"- Decision: `{best_run_payload['decision']}`\n"
        )
    execution_payload = {
        "status": "completed",
        "first_screen_completed_count": len(result_row_list),
        "first_screen_failed_count": first_screen_failed_count,
        "stability_completed_count": len(stability_row_list),
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
            "failed_run_count": first_screen_failed_count,
            "stability_completed_run_count": len(stability_row_list),
            "campaign_best_run_path": (
                campaign_output_directory / "campaign_best_run.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
            "raw_error_leader_id": leaderboard_row_list[0]["candidate_id"],
            "multi_index_recommended_candidate_id": (
                recommended_candidate_id
            ),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return campaign_output_directory


def refresh_accepted_gru_replay(
    dataset: stage5.Stage5Dataset,
) -> Path:
    """Refresh the accepted setpoint-GRU replay without retraining candidates."""

    campaign_output_directory_list = sorted(
        CAMPAIGN_ROOT_DIRECTORY.glob(f"*_{CAMPAIGN_NAME}")
    )
    assert campaign_output_directory_list, (
        f"No completed Stage 9 campaign directory found | "
        f"{CAMPAIGN_ROOT_DIRECTORY}"
    )
    campaign_output_directory = campaign_output_directory_list[-1]
    leaderboard_path = (
        campaign_output_directory / "campaign_leaderboard.yaml"
    )
    leaderboard_payload = load_yaml(leaderboard_path)
    leaderboard_row_list = leaderboard_payload["row_list"]
    measured_curve_matrix = dataset.curve_matrix[
        dataset.split_array == "test"
    ]
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    accepted_gru_prediction_matrix = replay_accepted_periodic_gru(
        dataset,
        "test",
        device,
    )
    corrected_gru_row = diagnostic_result(
        "G00",
        "accepted_setpoint_periodic_gru_replay",
        measured_curve_matrix,
        accepted_gru_prediction_matrix,
        ACCEPTED_GRU_CHECKPOINT_PATH,
    )
    leaderboard_row_list = [
        corrected_gru_row if row["candidate_id"] == "G00" else row
        for row in leaderboard_row_list
    ]
    leaderboard_row_list = sorted(
        leaderboard_row_list,
        key=lambda row: row["mae_deg"],
    )
    write_csv(
        campaign_output_directory / "campaign_leaderboard.csv",
        leaderboard_row_list,
    )
    write_yaml(
        leaderboard_path,
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "accepted_gru_replay_refreshed_at": now_iso(),
            "accepted_gru_replay_contract": (
                "polished_dataset setpoints forward archive checkpoint"
            ),
            "row_list": leaderboard_row_list,
        },
    )
    gate_payload = build_gate_summary(leaderboard_row_list)
    gate_payload["accepted_gru_replay_refreshed_at"] = now_iso()
    write_yaml(
        campaign_output_directory
        / "campaign_first_screen_gate_summary.yaml",
        gate_payload,
    )
    np.savez_compressed(
        ANALYSIS_DIRECTORY / "stage9_accepted_gru_replay.npz",
        measured_curve=measured_curve_matrix,
        predicted_curve=accepted_gru_prediction_matrix,
    )
    execution_summary_path = (
        campaign_output_directory / "campaign_execution_summary.yaml"
    )
    execution_payload = load_yaml(execution_summary_path)
    execution_payload.update(
        {
            "accepted_gru_replay_refreshed_at": now_iso(),
            "accepted_gru_replay_checkpoint_path": (
                ACCEPTED_GRU_CHECKPOINT_PATH.relative_to(
                    PROJECT_ROOT
                ).as_posix()
            ),
            "accepted_gru_replay_contract": (
                "polished_dataset setpoints forward archive checkpoint"
            ),
        }
    )
    write_yaml(execution_summary_path, execution_payload)
    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "accepted_gru_replay_refreshed_at": now_iso(),
            "accepted_gru_replay_checkpoint_path": (
                ACCEPTED_GRU_CHECKPOINT_PATH.relative_to(
                    PROJECT_ROOT
                ).as_posix()
            ),
            "raw_error_leader_id": leaderboard_row_list[0]["candidate_id"],
            "multi_index_recommended_candidate_id": gate_payload[
                "recommended_candidate_id"
            ],
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return campaign_output_directory


def parse_arguments() -> argparse.Namespace:
    """Parse Stage 9 campaign commands."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--refresh-accepted-replay", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Prepare, validate, or run the Stage 9 campaign."""

    arguments = parse_arguments()
    dataset = stage5.build_stage5_dataset()
    anchor_bundle = build_anchor_bundle(dataset)
    if arguments.prepare:
        prepare_campaign(dataset)
    if arguments.preflight_only:
        prepare_campaign(dataset)
        summary_payload = run_preflight(dataset, anchor_bundle)
        print(yaml.safe_dump(summary_payload, sort_keys=False))
    if arguments.run:
        campaign_output_directory = run_campaign(dataset, anchor_bundle)
        print(campaign_output_directory)
    if arguments.refresh_accepted_replay:
        campaign_output_directory = refresh_accepted_gru_replay(dataset)
        print(campaign_output_directory)
    if not any(
        [
            arguments.prepare,
            arguments.preflight_only,
            arguments.run,
            arguments.refresh_accepted_replay,
        ]
    ):
        prepare_campaign(dataset)


if __name__ == "__main__":
    main()
