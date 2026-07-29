"""Prepare, validate, and run Wave 5.2R Stage 8 weak compliance priors."""

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

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
import torch
import yaml

# Import Qualified Models And Campaign Utilities
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage6_spectral_sobolev_guidance as stage6,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage7_mean_centered_shape_multi_head as stage7,
)
from scripts.models.complex_harmonic_coefficient_residual_network import (
    ComplexHarmonicCoefficientResidualNetwork,
)
from scripts.models.weak_forward_compliance_residual_network import (
    WeakForwardComplianceResidualNetwork,
)


# Define Frozen Stage Contract
STAGE_NAME = "wave52r_stage8_weak_forward_compliance_priors"
CAMPAIGN_NAME = f"{STAGE_NAME}_2026_07_29"
SPLIT_SIGNATURE = stage5.SPLIT_SIGNATURE
ANGULAR_SAMPLE_COUNT = stage5.ANGULAR_SAMPLE_COUNT
FIRST_SCREEN_SEED = 314159
STABILITY_SEED_LIST = [271828, 161803]
MAXIMUM_EPOCH_COUNT = 64
MINIMUM_EPOCH_COUNT = 16
EARLY_STOPPING_PATIENCE = 12
H04_CHECKPOINT_PATH = stage6.STAGE5_CHECKPOINT_PATH_MAP["H04"]
H04_TEST_PREDICTION_PATH = stage6.STAGE5_H04_PREDICTION_PATH
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage8_weak_forward_compliance_priors"
)
CONFIG_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "weak_forward_compliance_priors"
    / "campaigns"
    / "2026-07-29_wave52r_stage8_weak_forward_compliance_priors"
)
QUEUE_DIRECTORY = CONFIG_DIRECTORY / "queue"
RUN_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "weak_forward_compliance_priors"
)
CAMPAIGN_ROOT_DIRECTORY = PROJECT_ROOT / "output" / "training_campaigns"
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-29/"
    "2026-07-29-18-00-37_wave52r_stage8_weak_forward_compliance_priors.md"
)
CAMPAIGN_PLAN_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "weak_forward_compliance_priors/"
    "2026-07-29-18-00-37_wave52r_stage8_weak_forward_compliance_"
    "priors_campaign_plan_report.md"
)


@dataclass(frozen=True)
class CandidateSpecification:

    """Describe one immutable Stage 8 candidate."""

    queue_index: int
    candidate_id: str
    formulation: str
    compliance_weight: float
    delayed_activation: bool = False
    adaptive_weight: bool = False
    hard_equation: bool = False


@dataclass
class ComplianceBootstrap:

    """Hold train-only weak-compliance calibration quantities."""

    lower_derivative_deg_per_nm: float
    upper_derivative_deg_per_nm: float
    median_derivative_deg_per_nm: float
    sign_support_fraction: float
    shuffled_lower_derivative_deg_per_nm: float
    shuffled_upper_derivative_deg_per_nm: float
    shuffled_sign_support_fraction: float
    temperature_edge_array: np.ndarray
    temperature_lower_array: np.ndarray
    temperature_upper_array: np.ndarray
    condition_confidence_array: np.ndarray
    bootstrap_row_list: list[dict[str, Any]]


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
        CandidateSpecification(1, "D00", "frozen_diagnostic", 0.0),
        CandidateSpecification(2, "C00", "data_only", 0.0),
        CandidateSpecification(3, "S01", "sign_only", 0.10),
        CandidateSpecification(4, "B01", "broad_interval", 0.10),
        CandidateSpecification(
            5,
            "W01",
            "confidence_interval",
            0.10,
        ),
        CandidateSpecification(
            6,
            "T01",
            "temperature_interval",
            0.10,
        ),
        CandidateSpecification(
            7,
            "A01",
            "delayed_interval",
            0.10,
            delayed_activation=True,
        ),
        CandidateSpecification(
            8,
            "R01",
            "adaptive_interval",
            0.10,
            adaptive_weight=True,
        ),
        CandidateSpecification(
            9,
            "N01",
            "shuffled_interval",
            0.10,
        ),
        CandidateSpecification(
            10,
            "H01",
            "hard_equation",
            0.0,
            hard_equation=True,
        ),
    ]


def regression_torque_slope(
    condition_matrix: np.ndarray,
    curve_mean_array: np.ndarray,
    sample_index_array: np.ndarray,
    *,
    shuffle_torque: bool,
    random_generator: np.random.Generator,
) -> float:

    """Fit one controlled train-only torque slope."""

    selected_condition_matrix = condition_matrix[sample_index_array].copy()
    selected_target_array = curve_mean_array[sample_index_array]
    if shuffle_torque:
        selected_condition_matrix[:, 0] = random_generator.permutation(
            selected_condition_matrix[:, 0]
        )
    centered_speed = (
        selected_condition_matrix[:, 1]
        - np.mean(selected_condition_matrix[:, 1])
    )
    centered_temperature = (
        selected_condition_matrix[:, 2]
        - np.mean(selected_condition_matrix[:, 2])
    )
    design_matrix = np.column_stack(
        [
            np.ones(len(sample_index_array)),
            selected_condition_matrix[:, 0],
            centered_speed,
            centered_temperature,
        ]
    )
    coefficient_array, _, rank, _ = np.linalg.lstsq(
        design_matrix,
        selected_target_array,
        rcond=None,
    )
    assert rank >= 3
    return float(coefficient_array[1])


def build_compliance_bootstrap(
    dataset: stage5.Stage5Dataset,
) -> ComplianceBootstrap:

    """Build deterministic train-only support and negative controls."""

    training_mask = dataset.split_array == "train"
    condition_matrix = dataset.condition_matrix[training_mask]
    curve_mean_array = np.mean(
        dataset.curve_matrix[training_mask],
        axis=1,
    )
    sample_count = condition_matrix.shape[0]
    random_generator = np.random.default_rng(FIRST_SCREEN_SEED)
    bootstrap_row_list: list[dict[str, Any]] = []
    slope_list: list[float] = []
    shuffled_slope_list: list[float] = []
    for bootstrap_index in range(512):
        sample_index_array = random_generator.integers(
            0,
            sample_count,
            size=sample_count,
        )
        slope = regression_torque_slope(
            condition_matrix,
            curve_mean_array,
            sample_index_array,
            shuffle_torque=False,
            random_generator=random_generator,
        )
        shuffled_slope = regression_torque_slope(
            condition_matrix,
            curve_mean_array,
            sample_index_array,
            shuffle_torque=True,
            random_generator=random_generator,
        )
        slope_list.append(slope)
        shuffled_slope_list.append(shuffled_slope)
        bootstrap_row_list.append(
            {
                "bootstrap_index": bootstrap_index,
                "torque_slope_deg_per_nm": slope,
                "shuffled_torque_slope_deg_per_nm": shuffled_slope,
            }
        )

    # Build Broad Global And Temperature-Stratified Intervals
    slope_array = np.asarray(slope_list)
    shuffled_slope_array = np.asarray(shuffled_slope_list)
    temperature_array = condition_matrix[:, 2]
    unique_temperature_array = np.unique(temperature_array)
    temperature_group_list = np.array_split(
        unique_temperature_array,
        3,
    )
    assert all(len(group) > 0 for group in temperature_group_list)
    temperature_edge_array = np.asarray(
        [
            float(unique_temperature_array[0] - 0.5),
            float(
                (
                    temperature_group_list[0][-1]
                    + temperature_group_list[1][0]
                )
                / 2.0
            ),
            float(
                (
                    temperature_group_list[1][-1]
                    + temperature_group_list[2][0]
                )
                / 2.0
            ),
            float(unique_temperature_array[-1] + 0.5),
        ]
    )
    temperature_lower_list: list[float] = []
    temperature_upper_list: list[float] = []
    for band_index in range(3):
        band_mask = np.isin(
            temperature_array,
            temperature_group_list[band_index],
        )
        band_index_array = np.flatnonzero(band_mask)
        band_slope_list = []
        for _ in range(256):
            sampled_band_indices = random_generator.choice(
                band_index_array,
                size=len(band_index_array),
                replace=True,
            )
            band_slope_list.append(
                regression_torque_slope(
                    condition_matrix,
                    curve_mean_array,
                    sampled_band_indices,
                    shuffle_torque=False,
                    random_generator=random_generator,
                )
            )
        temperature_lower_list.append(
            float(np.quantile(band_slope_list, 0.005))
        )
        temperature_upper_list.append(
            float(np.quantile(band_slope_list, 0.995))
        )

    # Convert Training-Condition Density Into A Conservative Confidence
    normalized_condition_matrix = (
        condition_matrix - dataset.feature_mean
    ) / dataset.feature_scale
    distance_matrix = np.linalg.norm(
        normalized_condition_matrix[:, np.newaxis, :]
        - normalized_condition_matrix[np.newaxis, :, :],
        axis=2,
    )
    sorted_distance_matrix = np.sort(distance_matrix, axis=1)
    tenth_neighbor_distance = sorted_distance_matrix[:, 10]
    distance_scale = float(np.median(tenth_neighbor_distance))
    confidence_array = np.exp(
        -tenth_neighbor_distance / max(distance_scale, 1.0e-8)
    )
    confidence_array /= np.max(confidence_array)

    return ComplianceBootstrap(
        lower_derivative_deg_per_nm=float(
            max(0.0, np.quantile(slope_array, 0.005))
        ),
        upper_derivative_deg_per_nm=float(
            np.quantile(slope_array, 0.995)
        ),
        median_derivative_deg_per_nm=float(np.median(slope_array)),
        sign_support_fraction=float(np.mean(slope_array > 0.0)),
        shuffled_lower_derivative_deg_per_nm=float(
            np.quantile(shuffled_slope_array, 0.005)
        ),
        shuffled_upper_derivative_deg_per_nm=float(
            np.quantile(shuffled_slope_array, 0.995)
        ),
        shuffled_sign_support_fraction=float(
            np.mean(shuffled_slope_array > 0.0)
        ),
        temperature_edge_array=temperature_edge_array,
        temperature_lower_array=np.asarray(temperature_lower_list),
        temperature_upper_array=np.asarray(temperature_upper_list),
        condition_confidence_array=confidence_array,
        bootstrap_row_list=bootstrap_row_list,
    )


def build_model(
    specification: CandidateSpecification,
    dataset: stage5.Stage5Dataset,
) -> WeakForwardComplianceResidualNetwork:

    """Build one H04-initialized Stage 8 candidate."""

    base_network = ComplexHarmonicCoefficientResidualNetwork(
        condition_input_size=3,
        hidden_size_list=[64, 64, 32],
        harmonic_order_list=stage5.CORE_ORDER_LIST,
        angular_sample_count=ANGULAR_SAMPLE_COUNT,
        formulation="bounded_coefficient",
        coefficient_correction_bound_list=(
            dataset.correction_bound_map["core"].tolist()
        ),
        zero_initialize_correction=True,
    )
    checkpoint_payload = torch.load(
        H04_CHECKPOINT_PATH,
        map_location="cpu",
        weights_only=False,
    )
    state_dictionary = checkpoint_payload["state_dict"]
    assert isinstance(state_dictionary, dict)
    base_network.load_state_dict(state_dictionary, strict=True)
    model = WeakForwardComplianceResidualNetwork(
        coefficient_network=base_network,
        torque_feature_mean_nm=float(dataset.feature_mean[0]),
        torque_feature_scale_nm=float(dataset.feature_scale[0]),
        use_hard_compliance_mean=specification.hard_equation,
    )
    if not specification.hard_equation:
        model.raw_stiffness_logit.requires_grad_(False)
        model.zero_torque_intercept_deg.requires_grad_(False)
    return model


def tensor_batch_for_split(
    dataset: stage5.Stage5Dataset,
    split_name: str,
    device: torch.device,
) -> dict[str, torch.Tensor]:

    """Materialize one complete Stage 8 split."""

    return stage5.tensor_dataset_for_split(
        dataset,
        "core",
        split_name,
        device,
    )


def temperature_interval_tensor(
    raw_temperature_tensor: torch.Tensor,
    bootstrap: ComplianceBootstrap,
) -> tuple[torch.Tensor, torch.Tensor]:

    """Select train-only derivative bounds by temperature band."""

    edge_tensor = torch.as_tensor(
        bootstrap.temperature_edge_array,
        dtype=raw_temperature_tensor.dtype,
        device=raw_temperature_tensor.device,
    )
    lower_tensor = torch.as_tensor(
        bootstrap.temperature_lower_array,
        dtype=raw_temperature_tensor.dtype,
        device=raw_temperature_tensor.device,
    )
    upper_tensor = torch.as_tensor(
        bootstrap.temperature_upper_array,
        dtype=raw_temperature_tensor.dtype,
        device=raw_temperature_tensor.device,
    )
    band_index_tensor = torch.bucketize(
        raw_temperature_tensor.reshape(-1),
        edge_tensor[1:-1],
    )
    return (
        lower_tensor[band_index_tensor].unsqueeze(1),
        upper_tensor[band_index_tensor].unsqueeze(1),
    )


def interval_penalty(
    derivative_tensor: torch.Tensor,
    lower_tensor: torch.Tensor,
    upper_tensor: torch.Tensor,
    confidence_tensor: torch.Tensor,
) -> torch.Tensor:

    """Penalize only response derivatives outside one broad interval."""

    interval_width_tensor = torch.clamp(
        upper_tensor - lower_tensor,
        min=1.0e-7,
    )
    normalized_violation_tensor = (
        torch.relu(lower_tensor - derivative_tensor)
        + torch.relu(derivative_tensor - upper_tensor)
    ) / interval_width_tensor
    return torch.sum(
        confidence_tensor * torch.square(normalized_violation_tensor)
    ) / torch.clamp(torch.sum(confidence_tensor), min=1.0)


def flattened_gradient_cosine(
    first_loss: torch.Tensor,
    second_loss: torch.Tensor,
    parameter_list: list[torch.nn.Parameter],
) -> tuple[float, float, float]:

    """Return cosine and norms for two loss gradients."""

    first_gradient_list = torch.autograd.grad(
        first_loss,
        parameter_list,
        retain_graph=True,
        allow_unused=True,
    )
    second_gradient_list = torch.autograd.grad(
        second_loss,
        parameter_list,
        retain_graph=True,
        allow_unused=True,
    )
    first_vector_list = []
    second_vector_list = []
    for parameter, first_gradient, second_gradient in zip(
        parameter_list,
        first_gradient_list,
        second_gradient_list,
        strict=True,
    ):
        first_vector_list.append(
            torch.zeros_like(parameter).reshape(-1)
            if first_gradient is None
            else first_gradient.reshape(-1)
        )
        second_vector_list.append(
            torch.zeros_like(parameter).reshape(-1)
            if second_gradient is None
            else second_gradient.reshape(-1)
        )
    first_vector = torch.cat(first_vector_list)
    second_vector = torch.cat(second_vector_list)
    first_norm = torch.linalg.vector_norm(first_vector)
    second_norm = torch.linalg.vector_norm(second_vector)
    cosine = torch.sum(first_vector * second_vector) / torch.clamp(
        first_norm * second_norm,
        min=1.0e-12,
    )
    return (
        float(cosine.detach().cpu()),
        float(first_norm.detach().cpu()),
        float(second_norm.detach().cpu()),
    )


def compute_training_losses(
    model: WeakForwardComplianceResidualNetwork,
    batch: dict[str, torch.Tensor],
    specification: CandidateSpecification,
    dataset: stage5.Stage5Dataset,
    bootstrap: ComplianceBootstrap,
    confidence_tensor: torch.Tensor,
    epoch_index: int,
) -> tuple[torch.Tensor, dict[str, torch.Tensor], dict[str, float]]:

    """Compute data, decomposition, and weak-compliance objectives."""

    condition_tensor = batch["condition"].detach().clone()
    condition_tensor.requires_grad_(True)
    derivative_tensor, output = model.mean_compliance_derivative(
        condition_tensor,
        batch["anchor"],
        create_graph=True,
    )
    prediction_curve_tensor = output["prediction_curve"]
    measured_mean_tensor = torch.mean(
        batch["curve"],
        dim=1,
        keepdim=True,
    )
    measured_shape_tensor = batch["curve"] - measured_mean_tensor
    curve_loss = torch.mean(
        torch.square(
            (prediction_curve_tensor - batch["curve"])
            / dataset.curve_scale
        )
    )
    mean_scale = max(
        float(
            np.std(
                np.mean(
                    dataset.curve_matrix[
                        dataset.split_array == "train"
                    ],
                    axis=1,
                )
            )
        ),
        1.0e-5,
    )
    mean_loss = torch.mean(
        torch.square(
            (output["prediction_mean"] - measured_mean_tensor)
            / mean_scale
        )
    )
    shape_loss = torch.mean(
        torch.square(
            (
                output["prediction_centered_shape"]
                - measured_shape_tensor
            )
            / dataset.curve_scale
        )
    )

    # Resolve The Declared Weak Prior Without Test-Derived Quantities
    one_tensor = torch.ones_like(derivative_tensor)
    compliance_loss = torch.zeros_like(curve_loss)
    if specification.formulation == "sign_only":
        compliance_loss = torch.mean(
            torch.square(
                torch.relu(-derivative_tensor)
                / max(bootstrap.median_derivative_deg_per_nm, 1.0e-7)
            )
        )
    elif specification.formulation in {
        "broad_interval",
        "confidence_interval",
        "delayed_interval",
        "adaptive_interval",
    }:
        lower_tensor = one_tensor * (
            bootstrap.lower_derivative_deg_per_nm
        )
        upper_tensor = one_tensor * (
            bootstrap.upper_derivative_deg_per_nm
        )
        resolved_confidence_tensor = (
            confidence_tensor
            if specification.formulation == "confidence_interval"
            else one_tensor
        )
        compliance_loss = interval_penalty(
            derivative_tensor,
            lower_tensor,
            upper_tensor,
            resolved_confidence_tensor,
        )
    elif specification.formulation == "temperature_interval":
        raw_temperature_tensor = (
            condition_tensor[:, 2:3] * float(dataset.feature_scale[2])
            + float(dataset.feature_mean[2])
        )
        lower_tensor, upper_tensor = temperature_interval_tensor(
            raw_temperature_tensor,
            bootstrap,
        )
        compliance_loss = interval_penalty(
            derivative_tensor,
            lower_tensor,
            upper_tensor,
            one_tensor,
        )
    elif specification.formulation == "shuffled_interval":
        lower_value = bootstrap.shuffled_lower_derivative_deg_per_nm
        upper_value = bootstrap.shuffled_upper_derivative_deg_per_nm
        if lower_value > upper_value:
            lower_value, upper_value = upper_value, lower_value
        compliance_loss = interval_penalty(
            derivative_tensor,
            one_tensor * lower_value,
            one_tensor * upper_value,
            one_tensor,
        )

    effective_weight = float(specification.compliance_weight)
    if specification.delayed_activation and epoch_index < 16:
        effective_weight = 0.0
    component_map = {
        "curve_loss": curve_loss,
        "mean_loss": mean_loss,
        "shape_loss": shape_loss,
        "compliance_loss": compliance_loss,
    }
    parameter_list = [
        parameter
        for parameter in model.parameters()
        if parameter.requires_grad
    ]
    raw_compliance_cosine = float("nan")
    mean_compliance_cosine = float("nan")
    shape_compliance_cosine = float("nan")
    compliance_gradient_norm = 0.0
    if (
        effective_weight > 0.0
        and float(compliance_loss.detach().cpu()) > 0.0
    ):
        (
            raw_compliance_cosine,
            raw_gradient_norm,
            compliance_gradient_norm,
        ) = flattened_gradient_cosine(
            curve_loss,
            compliance_loss,
            parameter_list,
        )
        mean_compliance_cosine, _, _ = flattened_gradient_cosine(
            mean_loss,
            compliance_loss,
            parameter_list,
        )
        shape_compliance_cosine, _, _ = flattened_gradient_cosine(
            shape_loss,
            compliance_loss,
            parameter_list,
        )
        if specification.adaptive_weight:
            effective_weight *= float(
                np.clip(
                    raw_gradient_norm
                    / max(compliance_gradient_norm, 1.0e-12),
                    0.1,
                    10.0,
                )
            )
    total_loss = (
        curve_loss
        + 0.25 * mean_loss
        + 0.25 * shape_loss
        + effective_weight * compliance_loss
    )
    scalar_payload = {
        name: float(value.detach().cpu())
        for name, value in component_map.items()
    }
    scalar_payload.update(
        {
            "total_loss": float(total_loss.detach().cpu()),
            "effective_compliance_weight": effective_weight,
            "raw_compliance_gradient_cosine": raw_compliance_cosine,
            "mean_compliance_gradient_cosine": mean_compliance_cosine,
            "shape_compliance_gradient_cosine": (
                shape_compliance_cosine
            ),
            "compliance_gradient_norm": compliance_gradient_norm,
            "derivative_mean_deg_per_nm": float(
                torch.mean(derivative_tensor).detach().cpu()
            ),
            "derivative_negative_fraction": float(
                torch.mean((derivative_tensor < 0.0).float())
                .detach()
                .cpu()
            ),
        }
    )
    return total_loss, component_map, scalar_payload


def evaluate_candidate(
    model: WeakForwardComplianceResidualNetwork,
    batch: dict[str, torch.Tensor],
    measured_curve_matrix: np.ndarray,
) -> tuple[dict[str, float], np.ndarray, np.ndarray]:

    """Evaluate full curves and predicted compliance derivatives."""

    model.eval()
    condition_tensor = batch["condition"].detach().clone()
    condition_tensor.requires_grad_(True)
    derivative_tensor, output = model.mean_compliance_derivative(
        condition_tensor,
        batch["anchor"],
        create_graph=False,
    )
    predicted_curve_matrix = (
        output["prediction_curve"].detach().cpu().numpy()
    )
    derivative_array = derivative_tensor.detach().cpu().numpy()
    metric_payload = stage7.evaluate_metrics(
        measured_curve_matrix,
        predicted_curve_matrix,
    )
    metric_payload.update(
        {
            "compliance_derivative_mean_deg_per_nm": float(
                np.mean(derivative_array)
            ),
            "compliance_derivative_min_deg_per_nm": float(
                np.min(derivative_array)
            ),
            "compliance_derivative_max_deg_per_nm": float(
                np.max(derivative_array)
            ),
            "compliance_negative_fraction": float(
                np.mean(derivative_array < 0.0)
            ),
            "effective_stiffness_nm_per_deg": float(
                model.effective_stiffness_nm_per_deg()
                .detach()
                .cpu()
            ),
        }
    )
    return metric_payload, predicted_curve_matrix, derivative_array


def train_candidate(
    specification: CandidateSpecification,
    dataset: stage5.Stage5Dataset,
    bootstrap: ComplianceBootstrap,
    campaign_output_directory: Path,
    random_seed: int,
) -> dict[str, Any]:

    """Train one Stage 8 candidate and persist immutable artifacts."""

    seed_everything(random_seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = build_model(specification, dataset).to(device)
    training_batch = tensor_batch_for_split(dataset, "train", device)
    validation_batch = tensor_batch_for_split(
        dataset,
        "validation",
        device,
    )
    test_batch = tensor_batch_for_split(dataset, "test", device)
    confidence_tensor = torch.as_tensor(
        bootstrap.condition_confidence_array,
        dtype=torch.float32,
        device=device,
    ).unsqueeze(1)
    optimizer = torch.optim.AdamW(
        [
            parameter
            for parameter in model.parameters()
            if parameter.requires_grad
        ],
        lr=2.0e-4,
        weight_decay=1.0e-5,
    )

    best_validation_mae = float("inf")
    best_epoch = -1
    best_state_dictionary: dict[str, torch.Tensor] | None = None
    patience_count = 0
    history_row_list: list[dict[str, Any]] = []
    for epoch_index in range(MAXIMUM_EPOCH_COUNT):
        model.train()
        optimizer.zero_grad(set_to_none=True)
        total_loss, _, scalar_payload = compute_training_losses(
            model,
            training_batch,
            specification,
            dataset,
            bootstrap,
            confidence_tensor,
            epoch_index,
        )
        total_loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=10.0)
        optimizer.step()

        model.eval()
        with torch.no_grad():
            validation_output = model(
                validation_batch["condition"],
                validation_batch["anchor"],
            )
            validation_mae = float(
                torch.mean(
                    torch.abs(
                        validation_output["prediction_curve"]
                        - validation_batch["curve"]
                    )
                ).cpu()
            )
        history_row_list.append(
            {
                "epoch": epoch_index + 1,
                **scalar_payload,
                "validation_curve_mae_deg": validation_mae,
            }
        )
        if validation_mae < best_validation_mae - 1.0e-9:
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
    measured_curve_matrix = dataset.curve_matrix[test_mask]
    (
        metric_payload,
        predicted_curve_matrix,
        derivative_array,
    ) = evaluate_candidate(
        model,
        test_batch,
        measured_curve_matrix,
    )
    seed_suffix = (
        ""
        if random_seed == FIRST_SCREEN_SEED
        else f"__seed_{random_seed}"
    )
    run_instance_id = (
        f"{now_timestamp()}__stage8_"
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
            "bootstrap_interval": [
                bootstrap.lower_derivative_deg_per_nm,
                bootstrap.upper_derivative_deg_per_nm,
            ],
        },
        checkpoint_path,
    )
    write_csv(run_directory / "training_history.csv", history_row_list)
    np.savez_compressed(
        run_directory / "test_predictions.npz",
        measured_curve=measured_curve_matrix,
        predicted_curve=predicted_curve_matrix,
        compliance_derivative_deg_per_nm=derivative_array,
    )
    result_payload = {
        "candidate_id": specification.candidate_id,
        "formulation": specification.formulation,
        "random_seed": random_seed,
        "run_instance_id": run_instance_id,
        "best_epoch": best_epoch,
        "best_validation_mae_deg": best_validation_mae,
        "checkpoint_path": checkpoint_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        **metric_payload,
    }
    write_yaml(run_directory / "metrics_summary.yaml", result_payload)
    return result_payload


def frozen_h04_result(
    dataset: stage5.Stage5Dataset,
    bootstrap: ComplianceBootstrap,
) -> dict[str, Any]:

    """Evaluate immutable H04 with the Stage 8 derivative diagnostics."""

    specification = build_candidate_list()[0]
    device = torch.device("cpu")
    model = build_model(specification, dataset).to(device)
    test_batch = tensor_batch_for_split(dataset, "test", device)
    test_mask = dataset.split_array == "test"
    metric_payload, _, _ = evaluate_candidate(
        model,
        test_batch,
        dataset.curve_matrix[test_mask],
    )
    return {
        "candidate_id": "D00",
        "formulation": "frozen_diagnostic",
        "random_seed": FIRST_SCREEN_SEED,
        "run_instance_id": "frozen_stage5_h04",
        "best_epoch": 0,
        "best_validation_mae_deg": float("nan"),
        "checkpoint_path": H04_CHECKPOINT_PATH.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        **metric_payload,
    }


def candidate_gate_row(
    candidate_row: dict[str, Any],
    frozen_row: dict[str, Any],
    control_row: dict[str, Any],
    shuffled_row: dict[str, Any],
) -> dict[str, Any]:

    """Evaluate one explicit Stage 8 curve-first gate."""

    gate_row = {
        "candidate_id": candidate_row["candidate_id"],
        "all_first_screen_gates_passed": False,
        "raw_beats_frozen": (
            candidate_row["mae_deg"] < frozen_row["mae_deg"]
        ),
        "raw_beats_control": (
            candidate_row["mae_deg"] < control_row["mae_deg"]
        ),
        "mean_beats_frozen": (
            candidate_row["mean_mae_deg"]
            < frozen_row["mean_mae_deg"]
        ),
        "mean_beats_control": (
            candidate_row["mean_mae_deg"]
            < control_row["mean_mae_deg"]
        ),
        "shape_preserved": (
            candidate_row["centered_shape_mae_deg"]
            <= 1.005 * frozen_row["centered_shape_mae_deg"]
        ),
        "derivative_preserved": (
            candidate_row["sobolev_derivative_mae"]
            <= 1.005 * frozen_row["sobolev_derivative_mae"]
        ),
        "closure_preserved": (
            candidate_row["periodic_closure_error_deg"]
            <= 1.01 * frozen_row["periodic_closure_error_deg"]
        ),
        "amplitude_preserved": (
            candidate_row["retained_amplitude_mae_deg"]
            <= 1.005 * frozen_row["retained_amplitude_mae_deg"]
        ),
        "phase_preserved": (
            candidate_row["retained_phase_mae_rad"]
            <= 1.005 * frozen_row["retained_phase_mae_rad"]
        ),
        "p95_preserved": (
            candidate_row["per_curve_mae_p95"]
            <= frozen_row["per_curve_mae_p95"]
        ),
        "beats_shuffled_control": (
            candidate_row["mae_deg"] < shuffled_row["mae_deg"]
            and candidate_row["mean_mae_deg"]
            < shuffled_row["mean_mae_deg"]
        ),
        "positive_derivative_supported": (
            candidate_row["compliance_negative_fraction"] <= 0.01
        ),
        "finite_metrics": all(
            np.isfinite(float(candidate_row[field_name]))
            for field_name in (
                "mae_deg",
                "mean_mae_deg",
                "centered_shape_mae_deg",
                "compliance_derivative_mean_deg_per_nm",
            )
        ),
    }
    gate_row["all_first_screen_gates_passed"] = all(
        bool(value)
        for key, value in gate_row.items()
        if key != "candidate_id"
        and key != "all_first_screen_gates_passed"
    )
    return gate_row


def build_gate_summary(
    row_list: list[dict[str, Any]],
) -> dict[str, Any]:

    """Build the first-screen decision and conditional stability roster."""

    row_map = {row["candidate_id"]: row for row in row_list}
    frozen_row = row_map["D00"]
    control_row = row_map["C00"]
    shuffled_row = row_map["N01"]
    gate_row_list = [
        candidate_gate_row(
            row_map[candidate_id],
            frozen_row,
            control_row,
            shuffled_row,
        )
        for candidate_id in (
            "S01",
            "B01",
            "W01",
            "T01",
            "A01",
            "R01",
        )
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


def prepare_campaign(
    dataset: stage5.Stage5Dataset,
    bootstrap: ComplianceBootstrap,
) -> None:

    """Write queue configurations and protected campaign state."""

    candidate_list = build_candidate_list()
    QUEUE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    queue_path_list = []
    for specification in candidate_list:
        queue_path = (
            QUEUE_DIRECTORY
            / (
                f"{specification.queue_index:03d}_"
                f"{specification.candidate_id.lower()}.yaml"
            )
        )
        write_yaml(
            queue_path,
            {
                "schema_version": 1,
                "stage": STAGE_NAME,
                "campaign_name": CAMPAIGN_NAME,
                "candidate": specification.__dict__,
                "dataset": "polished_dataset",
                "input_mode": "setpoints",
                "surface": "Fw",
                "split_signature": SPLIT_SIGNATURE,
                "random_seed": FIRST_SCREEN_SEED,
                "conditional_stability_seed_list": (
                    STABILITY_SEED_LIST
                ),
                "runtime_target_derived_input_count": 0,
            },
        )
        queue_path_list.append(
            queue_path.relative_to(PROJECT_ROOT).as_posix()
        )
    write_yaml(
        CONFIG_DIRECTORY / "campaign.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "campaign_type": STAGE_NAME,
            "model_family": "weak_forward_compliance_priors",
            "dataset": "polished_dataset",
            "input_mode": "setpoints",
            "surface": "Fw",
            "expected_first_screen_count": len(candidate_list),
            "first_screen_seed": FIRST_SCREEN_SEED,
            "conditional_stability_seed_list": STABILITY_SEED_LIST,
            "queue_path_list": queue_path_list,
            "technical_document_path": TECHNICAL_DOCUMENT_PATH,
            "campaign_plan_path": CAMPAIGN_PLAN_PATH,
        },
    )
    write_csv(
        ANALYSIS_DIRECTORY / "stage8_training_only_bootstrap.csv",
        bootstrap.bootstrap_row_list,
    )
    write_yaml(
        ANALYSIS_DIRECTORY / "stage8_training_only_bootstrap.yaml",
        {
            "schema_version": 1,
            "split_scope": "training_only",
            "split_signature": SPLIT_SIGNATURE,
            "training_curve_count": int(
                np.sum(dataset.split_array == "train")
            ),
            "bootstrap_replicate_count": len(
                bootstrap.bootstrap_row_list
            ),
            "lower_derivative_deg_per_nm": (
                bootstrap.lower_derivative_deg_per_nm
            ),
            "median_derivative_deg_per_nm": (
                bootstrap.median_derivative_deg_per_nm
            ),
            "upper_derivative_deg_per_nm": (
                bootstrap.upper_derivative_deg_per_nm
            ),
            "sign_support_fraction": bootstrap.sign_support_fraction,
            "effective_stiffness_from_median_nm_per_deg": (
                1.0 / bootstrap.median_derivative_deg_per_nm
            ),
            "shuffled_lower_derivative_deg_per_nm": (
                bootstrap.shuffled_lower_derivative_deg_per_nm
            ),
            "shuffled_upper_derivative_deg_per_nm": (
                bootstrap.shuffled_upper_derivative_deg_per_nm
            ),
            "shuffled_sign_support_fraction": (
                bootstrap.shuffled_sign_support_fraction
            ),
            "temperature_edge_array_deg_c": (
                bootstrap.temperature_edge_array.tolist()
            ),
            "temperature_lower_derivative_array_deg_per_nm": (
                bootstrap.temperature_lower_array.tolist()
            ),
            "temperature_upper_derivative_array_deg_per_nm": (
                bootstrap.temperature_upper_array.tolist()
            ),
            "validation_or_test_target_used": False,
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
            "random_seed_list": [FIRST_SCREEN_SEED],
            "conditional_stability_random_seed_list": (
                STABILITY_SEED_LIST
            ),
            "campaign_manifest_path": (
                CONFIG_DIRECTORY / "campaign.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
            "launcher_path": (
                "scripts/campaigns/wave_5_2/"
                "run_wave52r_stage8_weak_forward_compliance_priors.ps1"
            ),
            "launcher_note_path": (
                "doc/scripts/campaigns/wave_5_2/"
                "run_wave52r_stage8_weak_forward_compliance_priors.md"
            ),
            "planning_report_path": CAMPAIGN_PLAN_PATH,
            "technical_document_path": TECHNICAL_DOCUMENT_PATH,
            "local_preflight_command": (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage8_weak_forward_compliance_priors.ps1 "
                "-PreflightOnly"
            ),
            "local_launch_command": (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage8_weak_forward_compliance_priors.ps1 "
                "-Run"
            ),
            "remote_preflight_command": (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage8_weak_forward_compliance_priors.ps1 "
                "-Remote -PreflightOnly"
            ),
            "remote_launch_command": (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage8_weak_forward_compliance_priors.ps1 "
                "-Remote -Run"
            ),
            "approval": {
                "technical_document_status": "approved",
                "campaign_plan_status": "approved",
                "approval_source": (
                    "user blanket approval for twenty-four hours"
                ),
                "approval_recorded_at": (
                    "2026-07-29T15:30:41+02:00"
                ),
                "approval_expires_at": (
                    "2026-07-30T15:30:41+02:00"
                ),
            },
            "protected_file_list": [
                ACTIVE_CAMPAIGN_PATH.relative_to(PROJECT_ROOT).as_posix(),
                CONFIG_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
                (
                    "scripts/campaigns/wave_5_2/"
                    "run_wave52r_stage8_weak_forward_compliance_priors.py"
                ),
                (
                    "scripts/models/"
                    "weak_forward_compliance_residual_network.py"
                ),
                ANALYSIS_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
            ],
        },
    )


def run_preflight(
    dataset: stage5.Stage5Dataset,
    bootstrap: ComplianceBootstrap,
) -> dict[str, Any]:

    """Validate split, bootstrap, derivative, and reconstruction contracts."""

    assert dataset.curve_matrix.shape == (966, ANGULAR_SAMPLE_COUNT)
    assert int(np.sum(dataset.split_array == "train")) == 675
    assert int(np.sum(dataset.split_array == "validation")) == 194
    assert int(np.sum(dataset.split_array == "test")) == 97
    assert bootstrap.sign_support_fraction >= 0.95
    assert bootstrap.lower_derivative_deg_per_nm >= 0.0
    assert (
        bootstrap.upper_derivative_deg_per_nm
        > bootstrap.lower_derivative_deg_per_nm
    )
    assert (
        bootstrap.shuffled_sign_support_fraction
        < bootstrap.sign_support_fraction
    )
    test_specification = build_candidate_list()[2]
    model = build_model(test_specification, dataset)
    training_batch = tensor_batch_for_split(
        dataset,
        "train",
        torch.device("cpu"),
    )
    condition_tensor = (
        training_batch["condition"][:12].detach().clone()
    )
    condition_tensor.requires_grad_(True)
    derivative_tensor, output = model.mean_compliance_derivative(
        condition_tensor,
        training_batch["anchor"][:12],
        create_graph=True,
    )
    derivative_loss = torch.mean(torch.square(derivative_tensor))
    derivative_loss.backward()
    assert torch.all(torch.isfinite(output["prediction_curve"]))
    assert torch.all(torch.isfinite(derivative_tensor))
    assert tuple(output["prediction_curve"].shape) == (
        12,
        ANGULAR_SAMPLE_COUNT,
    )
    payload = {
        "schema_version": 1,
        "stage": STAGE_NAME,
        "status": "passed",
        "split_signature": SPLIT_SIGNATURE,
        "curve_count": 966,
        "split_count": {
            "train": 675,
            "validation": 194,
            "test": 97,
        },
        "candidate_count": len(build_candidate_list()),
        "bootstrap_sign_support_fraction": (
            bootstrap.sign_support_fraction
        ),
        "bootstrap_interval_deg_per_nm": [
            bootstrap.lower_derivative_deg_per_nm,
            bootstrap.upper_derivative_deg_per_nm,
        ],
        "shuffled_sign_support_fraction": (
            bootstrap.shuffled_sign_support_fraction
        ),
        "derivative_autograd_passed": True,
        "runtime_target_derived_input_count": 0,
        "all_checks_passed": True,
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage8_preflight_validation_summary.yaml",
        payload,
    )
    return payload


def run_campaign(
    dataset: stage5.Stage5Dataset,
    bootstrap: ComplianceBootstrap,
) -> Path:

    """Execute the first screen and conditional stability continuation."""

    campaign_output_directory = (
        CAMPAIGN_ROOT_DIRECTORY
        / f"{now_timestamp()}_{CAMPAIGN_NAME}"
    )
    campaign_output_directory.mkdir(parents=True, exist_ok=True)
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

    result_row_list = [frozen_h04_result(dataset, bootstrap)]
    failed_run_count = 0
    for specification in build_candidate_list()[1:]:
        try:
            result_row_list.append(
                train_candidate(
                    specification,
                    dataset,
                    bootstrap,
                    campaign_output_directory,
                    FIRST_SCREEN_SEED,
                )
            )
        except Exception as error:
            failed_run_count += 1
            result_row_list.append(
                {
                    "candidate_id": specification.candidate_id,
                    "formulation": specification.formulation,
                    "random_seed": FIRST_SCREEN_SEED,
                    "status": "failed",
                    "error": repr(error),
                }
            )
    completed_row_list = [
        row for row in result_row_list if row.get("status") != "failed"
    ]
    completed_row_list.sort(
        key=lambda row: float(row.get("mae_deg", float("inf")))
    )
    write_yaml(
        campaign_output_directory / "campaign_leaderboard.yaml",
        {"row_list": completed_row_list},
    )
    write_csv(
        campaign_output_directory / "campaign_leaderboard.csv",
        completed_row_list,
    )
    gate_summary = build_gate_summary(completed_row_list)
    write_yaml(
        campaign_output_directory
        / "campaign_first_screen_gate_summary.yaml",
        gate_summary,
    )

    # Continue Only Fully Qualified Ingredients Across Two More Seeds
    stability_result_row_list = []
    specification_map = {
        specification.candidate_id: specification
        for specification in build_candidate_list()
    }
    for candidate_id in gate_summary["passing_candidate_id_list"]:
        for random_seed in STABILITY_SEED_LIST:
            stability_result_row_list.append(
                train_candidate(
                    specification_map[candidate_id],
                    dataset,
                    bootstrap,
                    campaign_output_directory,
                    random_seed,
                )
            )
    if stability_result_row_list:
        write_yaml(
            campaign_output_directory
            / "campaign_stability_leaderboard.yaml",
            {"row_list": stability_result_row_list},
        )
        write_csv(
            campaign_output_directory
            / "campaign_stability_leaderboard.csv",
            stability_result_row_list,
        )

    raw_leader = completed_row_list[0]
    best_run_payload = {
        "candidate_id": raw_leader["candidate_id"],
        "run_instance_id": raw_leader["run_instance_id"],
        "checkpoint_path": raw_leader["checkpoint_path"],
        "mae_deg": raw_leader["mae_deg"],
        "multi_index_recommended_candidate_id": (
            gate_summary["recommended_candidate_id"]
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
            "# Stage 8 Campaign Best Run\n\n"
            f"- raw-error leader: `{raw_leader['candidate_id']}`;\n"
            f"- test MAE: `{raw_leader['mae_deg']:.9f} deg`;\n"
            "- multi-index recommendation: "
            f"`{gate_summary['recommended_candidate_id']}`.\n"
        )
    write_yaml(
        campaign_output_directory / "campaign_execution_summary.yaml",
        {
            "status": (
                "completed" if failed_run_count == 0 else "completed_with_failures"
            ),
            "first_screen_completed_count": len(completed_row_list),
            "first_screen_failed_count": failed_run_count,
            "stability_completed_count": len(stability_result_row_list),
            "completed_at": now_iso(),
        },
    )
    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "status": "completed",
            "completed_at": now_iso(),
            "completed_run_count": len(completed_row_list),
            "failed_run_count": failed_run_count,
            "stability_completed_run_count": len(
                stability_result_row_list
            ),
            "campaign_best_run_path": (
                campaign_output_directory / "campaign_best_run.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
            "raw_error_leader_id": raw_leader["candidate_id"],
            "multi_index_recommended_candidate_id": (
                gate_summary["recommended_candidate_id"]
            ),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return campaign_output_directory


def parse_arguments() -> argparse.Namespace:

    """Parse the Stage 8 command line."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--run", action="store_true")
    return parser.parse_args()


def main() -> None:

    """Prepare, preflight, and optionally execute Stage 8."""

    arguments = parse_arguments()
    dataset = stage5.build_stage5_dataset()
    bootstrap = build_compliance_bootstrap(dataset)
    prepare_campaign(dataset, bootstrap)
    preflight_payload = run_preflight(dataset, bootstrap)
    print(yaml.safe_dump(preflight_payload, sort_keys=False))
    if arguments.run:
        campaign_output_directory = run_campaign(dataset, bootstrap)
        print(
            "[DONE] Stage 8 campaign | "
            f"{campaign_output_directory.relative_to(PROJECT_ROOT)}"
        )
    elif not arguments.preflight_only:
        print("[READY] Use --run to execute the approved campaign.")


if __name__ == "__main__":
    main()
