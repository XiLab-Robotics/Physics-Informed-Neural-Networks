"""Prepare, validate, and run Wave 5.2R Stage 6 guidance experiments."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
from scipy.signal import savgol_coeffs
from scipy.signal import savgol_filter
import yaml

# Import PyTorch Utilities
import torch
import torch.nn.functional as torch_functional

# Import Project Models And Stage 5 Evidence Utilities
from scripts.analysis.polynomial_fourier_benchmark.run_phase1_polynomial_fourier_benchmark import (
    curve_metrics,
)
from scripts.analysis.polynomial_fourier_benchmark.run_phase1_polynomial_fourier_benchmark import (
    harmonic_error_metrics,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.models.complex_harmonic_coefficient_residual_network import (
    ComplexHarmonicCoefficientResidualNetwork,
)
from scripts.models.spectral_sobolev_guided_residual_network import (
    BoundedCoordinateResidualNetwork,
)


# Define The Immutable Stage Contract
STAGE_NAME = "wave52r_stage6_spectral_sobolev_guidance"
CAMPAIGN_NAME = f"{STAGE_NAME}_2026_07_29"
SPLIT_SIGNATURE = stage5.SPLIT_SIGNATURE
ANGULAR_SAMPLE_COUNT = stage5.ANGULAR_SAMPLE_COUNT
CORE_ORDER_LIST = stage5.CORE_ORDER_LIST
FIRST_SCREEN_SEED = 314159
STABILITY_SEED_LIST = [271828, 161803]
MAXIMUM_EPOCH_COUNT = 48
MINIMUM_EPOCH_COUNT = 8
EARLY_STOPPING_PATIENCE = 8
ANGULAR_DELTA = (2.0 * np.pi) / float(ANGULAR_SAMPLE_COUNT)

ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage6_spectral_sobolev_guidance"
)
CONFIG_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "spectral_sobolev_guidance"
    / "campaigns"
    / "2026-07-29_wave52r_stage6_spectral_sobolev_guidance"
)
QUEUE_DIRECTORY = CONFIG_DIRECTORY / "queue"
RUN_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "spectral_sobolev_guidance"
)
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-29/"
    "2026-07-29-14-41-07_wave52r_stage6_spectral_and_sobolev_"
    "guidance.md"
)
CAMPAIGN_PLAN_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "spectral_sobolev_guidance/"
    "2026-07-29-14-41-07_wave52r_stage6_spectral_sobolev_"
    "guidance_campaign_plan_report.md"
)
LAUNCHER_PATH = (
    "scripts/campaigns/wave_5_2/"
    "run_wave52r_stage6_spectral_sobolev_guidance.ps1"
)
LAUNCHER_NOTE_PATH = (
    "doc/scripts/campaigns/wave_5_2/"
    "run_wave52r_stage6_spectral_sobolev_guidance.md"
)

STAGE5_RUN_ROOT = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "complex_harmonic_coefficient_residuals"
)
STAGE5_CHECKPOINT_PATH_MAP = {
    "H04": (
        STAGE5_RUN_ROOT
        / "2026-07-28-16-17-13__stage5_h04"
        / "best_model.pt"
    ),
    "H08": (
        STAGE5_RUN_ROOT
        / "2026-07-28-16-17-15__stage5_h08"
        / "best_model.pt"
    ),
    "C04": (
        STAGE5_RUN_ROOT
        / "2026-07-28-16-17-09__stage5_c04"
        / "best_model.pt"
    ),
    "C08": (
        STAGE5_RUN_ROOT
        / "2026-07-28-16-17-11__stage5_c08"
        / "best_model.pt"
    ),
}
STAGE5_H04_PREDICTION_PATH = (
    STAGE5_RUN_ROOT
    / "2026-07-28-16-17-13__stage5_h04"
    / "test_predictions.npz"
)


@dataclass(frozen=True)
class CandidateSpecification:
    """Describe one immutable Stage 6 candidate."""

    queue_index: int
    candidate_id: str
    model_kind: str
    order_set_name: str
    initialization_id: str | None
    spectral_mode: str
    spectral_weight: float
    derivative_weight: float
    weak_weight: float
    failure_weighted: bool
    curriculum: bool
    matched_control_id: str | None
    promotion_eligible: bool


@dataclass
class Stage6Dataset:
    """Hold the canonical curves and all training-only guidance evidence."""

    base: stage5.Stage5Dataset
    derivative_target_matrix: np.ndarray
    derivative_scale: float
    derivative_window_length: int
    derivative_coefficient_array: np.ndarray
    second_derivative_gate_passed: bool
    second_derivative_sensitivity: float
    failure_weight_array: np.ndarray
    failure_effective_sample_ratio: float
    weak_basis_matrix: np.ndarray
    weak_target_matrix: np.ndarray
    weak_scale_array: np.ndarray
    coordinate_residual_bound_array: np.ndarray


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


def build_candidate_list() -> list[CandidateSpecification]:
    """Return the approved fifteen-run first-screen matrix."""

    row_list = [
        (
            "C01",
            "coefficient_bounded",
            "core",
            "H04",
            "none",
            0.0,
            0.0,
            0.0,
            False,
            False,
            None,
            False,
        ),
        (
            "C02",
            "coefficient_bounded",
            "core",
            "H04",
            "uniform",
            0.5,
            0.0,
            0.0,
            False,
            False,
            "C01",
            False,
        ),
        (
            "C03",
            "coefficient_direct",
            "core",
            "C04",
            "uniform",
            0.5,
            0.0,
            0.0,
            False,
            False,
            "C02",
            False,
        ),
        (
            "C04",
            "coefficient_direct",
            "data_selected",
            "C08",
            "fragile",
            0.5,
            0.0,
            0.0,
            False,
            False,
            None,
            False,
        ),
        (
            "D01",
            "coefficient_bounded",
            "core",
            "H04",
            "none",
            0.0,
            0.10,
            0.0,
            False,
            False,
            "C01",
            True,
        ),
        (
            "S02",
            "coefficient_bounded",
            "data_selected",
            "H08",
            "fragile",
            0.5,
            0.0,
            0.0,
            False,
            False,
            "C04",
            True,
        ),
        (
            "DS01",
            "coefficient_bounded",
            "core",
            "H04",
            "uniform",
            0.5,
            0.10,
            0.0,
            False,
            False,
            "C02",
            True,
        ),
        (
            "DS02",
            "coefficient_bounded",
            "data_selected",
            "H08",
            "fragile",
            0.5,
            0.10,
            0.0,
            False,
            False,
            "C04",
            True,
        ),
        (
            "CU01",
            "coefficient_bounded",
            "core",
            "H04",
            "uniform",
            0.5,
            0.10,
            0.0,
            False,
            True,
            "DS01",
            True,
        ),
        (
            "FI01",
            "coefficient_bounded",
            "core",
            "H04",
            "uniform",
            0.5,
            0.10,
            0.0,
            True,
            False,
            "DS01",
            True,
        ),
        (
            "FF00",
            "coordinate_raw",
            "core",
            None,
            "uniform",
            0.5,
            0.10,
            0.0,
            False,
            False,
            None,
            False,
        ),
        (
            "FF01",
            "coordinate_fourier",
            "core",
            None,
            "uniform",
            0.5,
            0.10,
            0.0,
            False,
            False,
            "FF00",
            True,
        ),
        (
            "SI00",
            "coordinate_tanh",
            "core",
            None,
            "uniform",
            0.5,
            0.10,
            0.0,
            False,
            False,
            None,
            False,
        ),
        (
            "SI01",
            "coordinate_siren",
            "core",
            None,
            "uniform",
            0.5,
            0.10,
            0.0,
            False,
            False,
            "SI00",
            True,
        ),
        (
            "W01",
            "coefficient_bounded",
            "core",
            "H04",
            "none",
            0.0,
            0.0,
            0.25,
            False,
            False,
            "C01",
            True,
        ),
    ]
    return [
        CandidateSpecification(
            queue_index=index,
            candidate_id=row[0],
            model_kind=row[1],
            order_set_name=row[2],
            initialization_id=row[3],
            spectral_mode=row[4],
            spectral_weight=row[5],
            derivative_weight=row[6],
            weak_weight=row[7],
            failure_weighted=row[8],
            curriculum=row[9],
            matched_control_id=row[10],
            promotion_eligible=row[11],
        )
        for index, row in enumerate(row_list, start=1)
    ]


def reconstruct_numpy_curve(
    coefficient_matrix: np.ndarray,
    harmonic_order_list: list[int],
) -> np.ndarray:
    """Reconstruct complete curves from Stage 5 coefficient coordinates."""

    theta_array = np.linspace(
        0.0,
        2.0 * np.pi,
        ANGULAR_SAMPLE_COUNT,
        endpoint=False,
    )
    curve_matrix = np.repeat(
        coefficient_matrix[:, :1],
        ANGULAR_SAMPLE_COUNT,
        axis=1,
    )
    for position, harmonic_order in enumerate(harmonic_order_list):
        curve_matrix += (
            coefficient_matrix[:, 1 + (2 * position), np.newaxis]
            * np.sin(float(harmonic_order) * theta_array)[np.newaxis, :]
        )
        curve_matrix += (
            coefficient_matrix[:, 2 + (2 * position), np.newaxis]
            * np.cos(float(harmonic_order) * theta_array)[np.newaxis, :]
        )
    return curve_matrix


def exact_coefficient_derivative(
    coefficient_matrix: np.ndarray,
    harmonic_order_list: list[int],
) -> np.ndarray:
    """Return the analytical first angular derivative."""

    theta_array = np.linspace(
        0.0,
        2.0 * np.pi,
        ANGULAR_SAMPLE_COUNT,
        endpoint=False,
    )
    derivative_matrix = np.zeros(
        (coefficient_matrix.shape[0], ANGULAR_SAMPLE_COUNT),
        dtype=np.float64,
    )
    for position, harmonic_order in enumerate(harmonic_order_list):
        sine_coefficient = coefficient_matrix[:, 1 + (2 * position)]
        cosine_coefficient = coefficient_matrix[:, 2 + (2 * position)]
        derivative_matrix += (
            float(harmonic_order)
            * sine_coefficient[:, np.newaxis]
            * np.cos(float(harmonic_order) * theta_array)[np.newaxis, :]
        )
        derivative_matrix -= (
            float(harmonic_order)
            * cosine_coefficient[:, np.newaxis]
            * np.sin(float(harmonic_order) * theta_array)[np.newaxis, :]
        )
    return derivative_matrix


def calibrate_derivative_estimator(
    base_dataset: stage5.Stage5Dataset,
) -> tuple[
    np.ndarray,
    float,
    int,
    np.ndarray,
    bool,
    float,
    list[dict[str, Any]],
]:
    """Select one circular derivative estimator using training evidence only."""

    training_mask = base_dataset.split_array == "train"
    training_coefficient_matrix = base_dataset.target_coefficient_map["core"][
        training_mask
    ]
    oracle_curve_matrix = reconstruct_numpy_curve(
        training_coefficient_matrix,
        CORE_ORDER_LIST,
    )
    oracle_derivative_matrix = exact_coefficient_derivative(
        training_coefficient_matrix,
        CORE_ORDER_LIST,
    )
    oracle_scale = max(
        float(np.sqrt(np.mean(np.square(oracle_derivative_matrix)))),
        1.0e-8,
    )

    calibration_row_list: list[dict[str, Any]] = []
    for window_length in [5, 7, 9, 11]:
        estimated_derivative_matrix = savgol_filter(
            oracle_curve_matrix,
            window_length=window_length,
            polyorder=3,
            deriv=1,
            delta=ANGULAR_DELTA,
            axis=1,
            mode="wrap",
        )
        normalized_oracle_error = float(
            np.sqrt(
                np.mean(
                    np.square(
                        estimated_derivative_matrix
                        - oracle_derivative_matrix
                    )
                )
            )
            / oracle_scale
        )
        calibration_row_list.append(
            {
                "window_length": window_length,
                "polyorder": 3,
                "normalized_oracle_rmse": normalized_oracle_error,
            }
        )

    selected_row = min(
        calibration_row_list,
        key=lambda row: (
            float(row["normalized_oracle_rmse"]),
            int(row["window_length"]),
        ),
    )
    selected_window_length = int(selected_row["window_length"])
    derivative_target_matrix = savgol_filter(
        base_dataset.curve_matrix,
        window_length=selected_window_length,
        polyorder=3,
        deriv=1,
        delta=ANGULAR_DELTA,
        axis=1,
        mode="wrap",
    )
    derivative_scale = max(
        float(np.std(derivative_target_matrix[training_mask])),
        1.0e-8,
    )
    derivative_coefficient_array = savgol_coeffs(
        selected_window_length,
        polyorder=3,
        deriv=1,
        delta=ANGULAR_DELTA,
        use="dot",
    ).astype(np.float64)

    # Keep Curvature Disabled Unless Adjacent Windows Agree
    comparison_window_length = min(selected_window_length + 2, 11)
    if comparison_window_length % 2 == 0:
        comparison_window_length += 1
    second_derivative_primary = savgol_filter(
        base_dataset.curve_matrix[training_mask],
        window_length=selected_window_length,
        polyorder=3,
        deriv=2,
        delta=ANGULAR_DELTA,
        axis=1,
        mode="wrap",
    )
    second_derivative_comparison = savgol_filter(
        base_dataset.curve_matrix[training_mask],
        window_length=comparison_window_length,
        polyorder=3,
        deriv=2,
        delta=ANGULAR_DELTA,
        axis=1,
        mode="wrap",
    )
    second_derivative_scale = max(
        float(np.std(second_derivative_primary)),
        1.0e-8,
    )
    second_derivative_sensitivity = float(
        np.mean(
            np.abs(
                second_derivative_primary
                - second_derivative_comparison
            )
        )
        / second_derivative_scale
    )
    second_derivative_gate_passed = (
        second_derivative_sensitivity <= 0.20
    )
    return (
        derivative_target_matrix.astype(np.float64),
        derivative_scale,
        selected_window_length,
        derivative_coefficient_array,
        second_derivative_gate_passed,
        second_derivative_sensitivity,
        calibration_row_list,
    )


def build_weak_basis_matrix() -> np.ndarray:
    """Build fixed local Fourier test functions on the complete cycle."""

    theta_array = np.linspace(
        0.0,
        2.0 * np.pi,
        ANGULAR_SAMPLE_COUNT,
        endpoint=False,
    )
    test_function_list: list[np.ndarray] = []
    center_list = np.linspace(0.0, 2.0 * np.pi, 8, endpoint=False)
    half_width = np.pi / 4.0
    for center in center_list:
        circular_distance = (
            (theta_array - center + np.pi) % (2.0 * np.pi)
        ) - np.pi
        window_array = np.zeros_like(theta_array)
        active_mask = np.abs(circular_distance) <= half_width
        window_array[active_mask] = 0.5 * (
            1.0
            + np.cos(
                np.pi
                * circular_distance[active_mask]
                / half_width
            )
        )
        for harmonic_order in [1, 40, 81, 162, 240]:
            test_function_list.extend(
                [
                    window_array
                    * np.sin(float(harmonic_order) * theta_array),
                    window_array
                    * np.cos(float(harmonic_order) * theta_array),
                ]
            )
    basis_matrix = np.stack(test_function_list, axis=1)
    basis_scale_array = np.sqrt(
        np.mean(np.square(basis_matrix), axis=0)
    )
    basis_matrix /= np.maximum(
        basis_scale_array[np.newaxis, :],
        1.0e-8,
    )
    return basis_matrix.astype(np.float64)


def build_stage6_dataset() -> tuple[Stage6Dataset, list[dict[str, Any]]]:
    """Build all Stage 6 guidance evidence from the canonical Stage 5 data."""

    base_dataset = stage5.build_stage5_dataset()
    assert base_dataset.curve_matrix.shape == (
        966,
        ANGULAR_SAMPLE_COUNT,
    )
    (
        derivative_target_matrix,
        derivative_scale,
        derivative_window_length,
        derivative_coefficient_array,
        second_derivative_gate_passed,
        second_derivative_sensitivity,
        derivative_calibration_row_list,
    ) = calibrate_derivative_estimator(base_dataset)

    training_mask = base_dataset.split_array == "train"
    anchor_curve_matrix = reconstruct_numpy_curve(
        base_dataset.anchor_coefficient_map["core"],
        CORE_ORDER_LIST,
    )
    training_residual_matrix = (
        base_dataset.curve_matrix[training_mask]
        - anchor_curve_matrix[training_mask]
    )

    # Build Bounded Failure-Informed Angular Weights
    failure_score_array = np.mean(
        np.abs(training_residual_matrix),
        axis=0,
    )
    failure_weight_array = np.clip(
        failure_score_array
        / max(float(np.mean(failure_score_array)), 1.0e-8),
        0.5,
        2.0,
    )
    failure_weight_array /= float(np.mean(failure_weight_array))
    failure_effective_sample_ratio = float(
        np.square(np.sum(failure_weight_array))
        / (
            np.sum(np.square(failure_weight_array))
            * failure_weight_array.size
        )
    )
    assert failure_effective_sample_ratio >= 0.70

    # Build Fixed Weak-Form Targets And Scales
    weak_basis_matrix = build_weak_basis_matrix()
    weak_target_matrix = (
        base_dataset.curve_matrix @ weak_basis_matrix
    ) / float(ANGULAR_SAMPLE_COUNT)
    weak_scale_array = np.std(
        weak_target_matrix[training_mask],
        axis=0,
    )
    weak_scale_array = np.maximum(weak_scale_array, 1.0e-6)

    # Build One Training-Only Physical Residual Envelope
    coordinate_residual_bound_array = 1.25 * np.quantile(
        np.abs(training_residual_matrix),
        0.995,
        axis=0,
    )
    coordinate_residual_bound_array = np.clip(
        coordinate_residual_bound_array,
        1.0e-3,
        5.0e-2,
    )

    return (
        Stage6Dataset(
            base=base_dataset,
            derivative_target_matrix=derivative_target_matrix,
            derivative_scale=derivative_scale,
            derivative_window_length=derivative_window_length,
            derivative_coefficient_array=derivative_coefficient_array,
            second_derivative_gate_passed=(
                second_derivative_gate_passed
            ),
            second_derivative_sensitivity=(
                second_derivative_sensitivity
            ),
            failure_weight_array=failure_weight_array,
            failure_effective_sample_ratio=(
                failure_effective_sample_ratio
            ),
            weak_basis_matrix=weak_basis_matrix,
            weak_target_matrix=weak_target_matrix,
            weak_scale_array=weak_scale_array,
            coordinate_residual_bound_array=(
                coordinate_residual_bound_array
            ),
        ),
        derivative_calibration_row_list,
    )


def build_model(
    specification: CandidateSpecification,
    dataset: Stage6Dataset,
) -> torch.nn.Module:
    """Construct one coefficient or coordinate candidate."""

    order_list = dataset.base.order_set_map[
        specification.order_set_name
    ]
    if specification.model_kind.startswith("coefficient_"):
        formulation = (
            "direct_coefficient"
            if specification.model_kind == "coefficient_direct"
            else "bounded_coefficient"
        )
        model: torch.nn.Module = (
            ComplexHarmonicCoefficientResidualNetwork(
                condition_input_size=3,
                hidden_size_list=[64, 64, 32],
                harmonic_order_list=order_list,
                angular_sample_count=ANGULAR_SAMPLE_COUNT,
                formulation=formulation,
                coefficient_correction_bound_list=(
                    dataset.base.correction_bound_map[
                        specification.order_set_name
                    ].tolist()
                ),
                zero_initialize_correction=True,
            )
        )
    else:
        architecture_map = {
            "coordinate_raw": ("raw_circular_tanh", 99),
            "coordinate_fourier": ("fourier_feature_tanh", 48),
            "coordinate_tanh": ("coordinate_tanh", 64),
            "coordinate_siren": ("siren", 64),
        }
        angular_architecture, angular_hidden_size = architecture_map[
            specification.model_kind
        ]
        model = BoundedCoordinateResidualNetwork(
            condition_input_size=3,
            harmonic_order_list=CORE_ORDER_LIST,
            angular_sample_count=ANGULAR_SAMPLE_COUNT,
            angular_architecture=angular_architecture,
            residual_bound_list=(
                dataset.coordinate_residual_bound_array.tolist()
            ),
            rank=12,
            condition_hidden_size=64,
            angular_hidden_size=angular_hidden_size,
            fourier_feature_order_list=CORE_ORDER_LIST,
        )

    # Start Every Fine-Tuning Arm From The Same Qualified Checkpoint
    if specification.initialization_id is not None:
        checkpoint_path = STAGE5_CHECKPOINT_PATH_MAP[
            specification.initialization_id
        ]
        checkpoint_payload = torch.load(
            checkpoint_path,
            map_location="cpu",
            weights_only=False,
        )
        state_dictionary = checkpoint_payload["state_dict"]
        assert isinstance(state_dictionary, dict)
        model.load_state_dict(state_dictionary, strict=True)
    return model


def tensor_batch_for_split(
    dataset: Stage6Dataset,
    order_set_name: str,
    split_name: str,
    device: torch.device,
) -> dict[str, torch.Tensor]:
    """Materialize one complete split and every guidance target."""

    split_mask = dataset.base.split_array == split_name
    batch = stage5.tensor_dataset_for_split(
        dataset.base,
        order_set_name,
        split_name,
        device,
    )
    batch.update(
        {
            "derivative": torch.as_tensor(
                dataset.derivative_target_matrix[split_mask],
                dtype=torch.float32,
                device=device,
            ),
            "weak_target": torch.as_tensor(
                dataset.weak_target_matrix[split_mask],
                dtype=torch.float32,
                device=device,
            ),
        }
    )
    return batch


def circular_derivative_torch(
    curve_tensor: torch.Tensor,
    derivative_coefficient_tensor: torch.Tensor,
) -> torch.Tensor:
    """Apply the calibrated periodic Savitzky-Golay derivative."""

    assert curve_tensor.ndim == 2
    assert derivative_coefficient_tensor.ndim == 1
    padding_width = int(derivative_coefficient_tensor.numel() // 2)
    padded_curve_tensor = torch_functional.pad(
        curve_tensor.unsqueeze(1),
        (padding_width, padding_width),
        mode="circular",
    )
    return torch_functional.conv1d(
        padded_curve_tensor,
        derivative_coefficient_tensor.view(1, 1, -1),
    ).squeeze(1)


def project_curve_coefficients_torch(
    curve_tensor: torch.Tensor,
    harmonic_order_list: list[int],
) -> torch.Tensor:
    """Project complete curves into Stage 5 sine/cosine coordinates."""

    theta_tensor = torch.linspace(
        0.0,
        2.0 * torch.pi,
        steps=ANGULAR_SAMPLE_COUNT + 1,
        dtype=curve_tensor.dtype,
        device=curve_tensor.device,
    )[:-1]
    coefficient_tensor_list = [
        torch.mean(curve_tensor, dim=1, keepdim=True)
    ]
    for harmonic_order in harmonic_order_list:
        sine_basis = torch.sin(float(harmonic_order) * theta_tensor)
        cosine_basis = torch.cos(float(harmonic_order) * theta_tensor)
        coefficient_tensor_list.extend(
            [
                (
                    2.0
                    * torch.mean(
                        curve_tensor * sine_basis.unsqueeze(0),
                        dim=1,
                        keepdim=True,
                    )
                ),
                (
                    2.0
                    * torch.mean(
                        curve_tensor * cosine_basis.unsqueeze(0),
                        dim=1,
                        keepdim=True,
                    )
                ),
            ]
        )
    return torch.cat(coefficient_tensor_list, dim=1)


def build_spectral_weight_tensor(
    harmonic_order_list: list[int],
    spectral_mode: str,
    device: torch.device,
) -> torch.Tensor:
    """Return fixed coefficient-coordinate spectral weights."""

    weight_list = [0.5]
    core_order_set = set(CORE_ORDER_LIST)
    for harmonic_order in harmonic_order_list:
        harmonic_weight = 1.0
        if (
            spectral_mode == "fragile"
            and harmonic_order not in core_order_set
        ):
            harmonic_weight = 2.0
        elif (
            spectral_mode == "fragile"
            and harmonic_order >= 156
        ):
            harmonic_weight = 1.5
        weight_list.extend([harmonic_weight, harmonic_weight])
    weight_tensor = torch.as_tensor(
        weight_list,
        dtype=torch.float32,
        device=device,
    )
    return weight_tensor / torch.mean(weight_tensor)


def resolve_active_loss_weights(
    specification: CandidateSpecification,
    epoch_index: int,
) -> tuple[float, float, float]:
    """Resolve deterministic curriculum or fixed secondary weights."""

    spectral_weight = specification.spectral_weight
    derivative_weight = specification.derivative_weight
    weak_weight = specification.weak_weight
    if not specification.curriculum:
        return spectral_weight, derivative_weight, weak_weight

    # Learn Curve Fit, Then Spectrum, Then Derivative Structure
    if epoch_index < MAXIMUM_EPOCH_COUNT // 3:
        return 0.0, 0.0, 0.0
    if epoch_index < (2 * MAXIMUM_EPOCH_COUNT) // 3:
        return spectral_weight, 0.0, 0.0
    return spectral_weight, derivative_weight, weak_weight


def compute_loss_components(
    output: dict[str, torch.Tensor],
    batch: dict[str, torch.Tensor],
    specification: CandidateSpecification,
    dataset: Stage6Dataset,
    derivative_coefficient_tensor: torch.Tensor,
    weak_basis_tensor: torch.Tensor,
    weak_scale_tensor: torch.Tensor,
    failure_weight_tensor: torch.Tensor,
    epoch_index: int,
) -> tuple[torch.Tensor, dict[str, torch.Tensor], dict[str, float]]:
    """Compute normalized curve, derivative, spectral, and weak objectives."""

    prediction_curve_tensor = output["prediction_curve"]
    curve_scale_tensor = torch.as_tensor(
        dataset.base.curve_scale,
        dtype=prediction_curve_tensor.dtype,
        device=prediction_curve_tensor.device,
    )
    normalized_curve_error = (
        prediction_curve_tensor - batch["curve"]
    ) / curve_scale_tensor
    if specification.failure_weighted:
        curve_loss = torch.mean(
            torch.square(normalized_curve_error)
            * failure_weight_tensor.unsqueeze(0)
        )
    else:
        curve_loss = torch.mean(torch.square(normalized_curve_error))

    derivative_loss = torch.zeros_like(curve_loss)
    if specification.derivative_weight > 0.0:
        prediction_derivative_tensor = circular_derivative_torch(
            prediction_curve_tensor,
            derivative_coefficient_tensor,
        )
        derivative_loss = torch.mean(
            torch.square(
                (
                    prediction_derivative_tensor
                    - batch["derivative"]
                )
                / float(dataset.derivative_scale)
            )
        )

    spectral_loss = torch.zeros_like(curve_loss)
    if specification.spectral_mode != "none":
        prediction_coefficient_tensor = (
            project_curve_coefficients_torch(
                prediction_curve_tensor,
                dataset.base.order_set_map[
                    specification.order_set_name
                ],
            )
        )
        coefficient_scale_tensor = torch.as_tensor(
            dataset.base.coefficient_scale_map[
                specification.order_set_name
            ],
            dtype=prediction_curve_tensor.dtype,
            device=prediction_curve_tensor.device,
        )
        spectral_weight_tensor = build_spectral_weight_tensor(
            dataset.base.order_set_map[
                specification.order_set_name
            ],
            specification.spectral_mode,
            prediction_curve_tensor.device,
        )
        normalized_coefficient_error = (
            prediction_coefficient_tensor - batch["coefficient"]
        ) / coefficient_scale_tensor.unsqueeze(0)
        spectral_loss = torch.mean(
            torch.square(normalized_coefficient_error)
            * spectral_weight_tensor.unsqueeze(0)
        )

    weak_loss = torch.zeros_like(curve_loss)
    if specification.weak_weight > 0.0:
        prediction_weak_tensor = (
            prediction_curve_tensor @ weak_basis_tensor
        ) / float(ANGULAR_SAMPLE_COUNT)
        weak_loss = torch.mean(
            torch.square(
                (
                    prediction_weak_tensor - batch["weak_target"]
                )
                / weak_scale_tensor.unsqueeze(0)
            )
        )

    (
        active_spectral_weight,
        active_derivative_weight,
        active_weak_weight,
    ) = resolve_active_loss_weights(specification, epoch_index)
    total_loss = (
        curve_loss
        + active_spectral_weight * spectral_loss
        + active_derivative_weight * derivative_loss
        + active_weak_weight * weak_loss
    )
    component_tensor_map = {
        "curve": curve_loss,
        "spectral": spectral_loss,
        "derivative": derivative_loss,
        "weak": weak_loss,
    }
    scalar_payload = {
        "curve_loss": float(curve_loss.detach().cpu()),
        "spectral_loss": float(spectral_loss.detach().cpu()),
        "derivative_loss": float(derivative_loss.detach().cpu()),
        "weak_loss": float(weak_loss.detach().cpu()),
        "active_spectral_weight": active_spectral_weight,
        "active_derivative_weight": active_derivative_weight,
        "active_weak_weight": active_weak_weight,
        "total_loss": float(total_loss.detach().cpu()),
    }
    return total_loss, component_tensor_map, scalar_payload


def gradient_norm(
    loss_tensor: torch.Tensor,
    parameter_list: list[torch.nn.Parameter],
) -> float:
    """Return one detached L2 gradient norm without mutating gradients."""

    if not loss_tensor.requires_grad:
        return 0.0
    gradient_list = torch.autograd.grad(
        loss_tensor,
        parameter_list,
        retain_graph=True,
        allow_unused=True,
    )
    squared_norm = torch.zeros(
        (),
        dtype=loss_tensor.dtype,
        device=loss_tensor.device,
    )
    for gradient_tensor in gradient_list:
        if gradient_tensor is not None:
            squared_norm = squared_norm + torch.sum(
                torch.square(gradient_tensor)
            )
    return float(torch.sqrt(squared_norm).detach().cpu())


def derivative_correlation(
    measured_derivative: np.ndarray,
    predicted_derivative: np.ndarray,
) -> float:
    """Return a stable Pearson correlation for two derivative curves."""

    measured_centered = measured_derivative - np.mean(
        measured_derivative
    )
    predicted_centered = predicted_derivative - np.mean(
        predicted_derivative
    )
    denominator = float(
        np.linalg.norm(measured_centered)
        * np.linalg.norm(predicted_centered)
    )
    if denominator <= 1.0e-12:
        return 0.0
    return float(
        np.dot(measured_centered, predicted_centered) / denominator
    )


def aggregate_stage6_metrics(
    measured_curve_matrix: np.ndarray,
    predicted_curve_matrix: np.ndarray,
    derivative_window_length: int,
) -> dict[str, float]:
    """Aggregate the complete Stage 6 curve-first decision surface."""

    measured_derivative_matrix = savgol_filter(
        measured_curve_matrix,
        window_length=derivative_window_length,
        polyorder=3,
        deriv=1,
        delta=ANGULAR_DELTA,
        axis=1,
        mode="wrap",
    )
    predicted_derivative_matrix = savgol_filter(
        predicted_curve_matrix,
        window_length=derivative_window_length,
        polyorder=3,
        deriv=1,
        delta=ANGULAR_DELTA,
        axis=1,
        mode="wrap",
    )

    metric_row_list: list[dict[str, float]] = []
    per_curve_mae_list: list[float] = []
    for row_index, (measured_curve, predicted_curve) in enumerate(
        zip(
            measured_curve_matrix,
            predicted_curve_matrix,
            strict=True,
        )
    ):
        metric_row = curve_metrics(measured_curve, predicted_curve)
        metric_row.update(
            harmonic_error_metrics(
                measured_curve,
                predicted_curve,
                CORE_ORDER_LIST,
            )
        )
        measured_derivative = measured_derivative_matrix[row_index]
        predicted_derivative = predicted_derivative_matrix[row_index]
        metric_row["sobolev_derivative_mae"] = float(
            np.mean(
                np.abs(
                    measured_derivative - predicted_derivative
                )
            )
        )
        metric_row["sobolev_derivative_correlation"] = (
            derivative_correlation(
                measured_derivative,
                predicted_derivative,
            )
        )
        metric_row_list.append(metric_row)
        per_curve_mae_list.append(
            float(np.mean(np.abs(measured_curve - predicted_curve)))
        )

    metric_payload = {
        metric_name: float(
            np.mean([row[metric_name] for row in metric_row_list])
        )
        for metric_name in metric_row_list[0]
    }
    metric_payload["per_curve_mae_p95"] = float(
        np.quantile(per_curve_mae_list, 0.95)
    )
    metric_payload["per_curve_mae_worst"] = float(
        np.max(per_curve_mae_list)
    )

    measured_spectrum = np.fft.rfft(
        measured_curve_matrix,
        axis=1,
    )
    predicted_spectrum = np.fft.rfft(
        predicted_curve_matrix,
        axis=1,
    )
    unsupported_slice = slice(241, measured_spectrum.shape[1])
    measured_high_energy = float(
        np.mean(
            np.square(
                np.abs(measured_spectrum[:, unsupported_slice])
            )
        )
    )
    predicted_high_energy = float(
        np.mean(
            np.square(
                np.abs(predicted_spectrum[:, unsupported_slice])
            )
        )
    )
    metric_payload["unsupported_high_frequency_energy_ratio"] = (
        predicted_high_energy / max(measured_high_energy, 1.0e-12)
    )
    return metric_payload


def write_guidance_artifacts(
    dataset: Stage6Dataset,
    derivative_calibration_row_list: list[dict[str, Any]],
) -> None:
    """Persist the training-only derivative and guidance contract."""

    ANALYSIS_DIRECTORY.mkdir(parents=True, exist_ok=True)
    write_csv(
        ANALYSIS_DIRECTORY / "stage6_derivative_window_calibration.csv",
        derivative_calibration_row_list,
    )
    write_yaml(
        ANALYSIS_DIRECTORY / "stage6_guidance_manifest.yaml",
        {
            "schema_version": 1,
            "stage_name": STAGE_NAME,
            "generated_at": now_iso(),
            "dataset": "polished_dataset",
            "input_mode": "setpoints",
            "surface": "Fw",
            "split_signature": SPLIT_SIGNATURE,
            "angular_sample_count": ANGULAR_SAMPLE_COUNT,
            "angular_delta_radian": ANGULAR_DELTA,
            "derivative": {
                "implementation": "scipy.signal.savgol_filter",
                "window_length": dataset.derivative_window_length,
                "polyorder": 3,
                "derivative_order": 1,
                "delta": ANGULAR_DELTA,
                "mode": "wrap",
                "scale": dataset.derivative_scale,
                "selection_scope": "training_only",
            },
            "second_derivative": {
                "sensitivity": dataset.second_derivative_sensitivity,
                "threshold": 0.20,
                "gate_passed": dataset.second_derivative_gate_passed,
                "activated": False,
                "decision": (
                    "not_in_first_screen_even_if_stable"
                    if dataset.second_derivative_gate_passed
                    else "blocked_by_window_sensitivity"
                ),
            },
            "failure_weighting": {
                "minimum_weight": float(
                    np.min(dataset.failure_weight_array)
                ),
                "maximum_weight": float(
                    np.max(dataset.failure_weight_array)
                ),
                "mean_weight": float(
                    np.mean(dataset.failure_weight_array)
                ),
                "effective_sample_ratio": (
                    dataset.failure_effective_sample_ratio
                ),
                "selection_scope": "training_only_pf_a_residual",
            },
            "weak_form": {
                "test_function_count": int(
                    dataset.weak_basis_matrix.shape[1]
                ),
                "angular_window_count": 8,
                "harmonic_order_list": [1, 40, 81, 162, 240],
                "selection_scope": "fixed_before_training",
            },
            "coordinate_residual_bound": {
                "minimum_deg": float(
                    np.min(dataset.coordinate_residual_bound_array)
                ),
                "maximum_deg": float(
                    np.max(dataset.coordinate_residual_bound_array)
                ),
                "quantile": 0.995,
                "multiplier": 1.25,
                "selection_scope": "training_only_pf_a_residual",
            },
            "runtime_target_or_derivative_input_count": 0,
        },
    )


def prepare_campaign(
    dataset: Stage6Dataset,
    derivative_calibration_row_list: list[dict[str, Any]],
) -> None:
    """Write queue configurations and the persistent campaign state."""

    write_guidance_artifacts(
        dataset,
        derivative_calibration_row_list,
    )
    candidate_list = build_candidate_list()
    QUEUE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    queue_path_list: list[str] = []
    for specification in candidate_list:
        model = build_model(specification, dataset)
        trainable_parameter_count = sum(
            parameter.numel()
            for parameter in model.parameters()
            if parameter.requires_grad
        )
        queue_payload = {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "queue_index": specification.queue_index,
            "candidate_id": specification.candidate_id,
            "model_family": "spectral_sobolev_guidance",
            "model_kind": specification.model_kind,
            "order_set_name": specification.order_set_name,
            "harmonic_order_list": dataset.base.order_set_map[
                specification.order_set_name
            ],
            "initialization_id": specification.initialization_id,
            "trainable_parameter_count": trainable_parameter_count,
            "loss": {
                "curve_weight": 1.0,
                "spectral_mode": specification.spectral_mode,
                "spectral_weight": specification.spectral_weight,
                "derivative_weight": specification.derivative_weight,
                "weak_weight": specification.weak_weight,
                "failure_weighted": specification.failure_weighted,
                "curriculum": specification.curriculum,
            },
            "matched_control_id": specification.matched_control_id,
            "promotion_eligible": specification.promotion_eligible,
            "random_seed": FIRST_SCREEN_SEED,
            "maximum_epochs": MAXIMUM_EPOCH_COUNT,
            "minimum_epochs": MINIMUM_EPOCH_COUNT,
            "early_stopping_patience": EARLY_STOPPING_PATIENCE,
            "learning_rate": (
                5.0e-4
                if specification.model_kind.startswith("coordinate_")
                else 2.0e-4
            ),
            "weight_decay": 1.0e-5,
            "dataset": "polished_dataset",
            "input_mode": "setpoints",
            "surface": "Fw",
            "split_signature": SPLIT_SIGNATURE,
            "angular_sample_count": ANGULAR_SAMPLE_COUNT,
            "derivative_window_length": (
                dataset.derivative_window_length
            ),
        }
        queue_path = (
            QUEUE_DIRECTORY
            / (
                f"{specification.queue_index:03d}_"
                f"{specification.candidate_id.lower()}.yaml"
            )
        )
        write_yaml(queue_path, queue_payload)
        queue_path_list.append(
            queue_path.relative_to(PROJECT_ROOT).as_posix()
        )

    write_yaml(
        CONFIG_DIRECTORY / "campaign.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "campaign_type": (
                "wave_5_2r_stage6_spectral_sobolev_guidance"
            ),
            "status": "prepared",
            "prepared_at": now_iso(),
            "expected_run_count": len(candidate_list),
            "dataset": "polished_dataset",
            "input_mode": "setpoints",
            "surface": "Fw",
            "split_signature": SPLIT_SIGNATURE,
            "angular_sample_count": ANGULAR_SAMPLE_COUNT,
            "queue_path_list": queue_path_list,
        },
    )

    active_payload = {
        "status": "prepared",
        "prepared_at": now_iso(),
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": (
            "wave_5_2r_stage6_spectral_sobolev_guidance"
        ),
        "dataset_id": "polished_dataset",
        "input_mode": "setpoints",
        "dataset_schema": "polished_setpoint_uniform_curve_v1",
        "surface_list": ["fw"],
        "primary_surface": "fw",
        "expected_run_count": len(candidate_list),
        "completed_run_count": 0,
        "failed_run_count": 0,
        "random_seed_list": [FIRST_SCREEN_SEED],
        "conditional_stability_random_seed_list": STABILITY_SEED_LIST,
        "campaign_manifest_path": (
            CONFIG_DIRECTORY.relative_to(PROJECT_ROOT).as_posix()
            + "/campaign.yaml"
        ),
        "campaign_config_root": (
            QUEUE_DIRECTORY.relative_to(PROJECT_ROOT).as_posix()
        ),
        "launcher_path": LAUNCHER_PATH,
        "launcher_note_path": LAUNCHER_NOTE_PATH,
        "planning_report_path": CAMPAIGN_PLAN_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "guidance_manifest_path": (
            ANALYSIS_DIRECTORY.relative_to(PROJECT_ROOT).as_posix()
            + "/stage6_guidance_manifest.yaml"
        ),
        "local_preflight_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage6_spectral_sobolev_guidance.ps1 "
            "-PreflightOnly"
        ),
        "local_launch_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage6_spectral_sobolev_guidance.ps1 "
            "-Run"
        ),
        "remote_preflight_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage6_spectral_sobolev_guidance.ps1 "
            "-Remote -PreflightOnly"
        ),
        "remote_launch_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage6_spectral_sobolev_guidance.ps1 "
            "-Remote -Run"
        ),
        "launch_command_list": [
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage6_spectral_sobolev_guidance.ps1 "
                "-PreflightOnly"
            ),
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage6_spectral_sobolev_guidance.ps1 "
                "-Run"
            ),
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage6_spectral_sobolev_guidance.ps1 "
                "-Remote -PreflightOnly"
            ),
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage6_spectral_sobolev_guidance.ps1 "
                "-Remote -Run"
            ),
        ],
        "approval": {
            "technical_document_status": "approved",
            "technical_document_approval_source": (
                "user blanket approval for twenty-four hours"
            ),
            "campaign_plan_status": "approved",
            "campaign_plan_approval_source": (
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
                "run_wave52r_stage6_spectral_sobolev_guidance.py"
            ),
            LAUNCHER_PATH,
            (
                "scripts/models/"
                "spectral_sobolev_guided_residual_network.py"
            ),
            ANALYSIS_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
        ],
    }
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)


def run_preflight(dataset: Stage6Dataset) -> dict[str, Any]:
    """Validate every model, guidance operator, and leakage boundary."""

    device = torch.device("cpu")
    derivative_coefficient_tensor = torch.as_tensor(
        dataset.derivative_coefficient_array,
        dtype=torch.float32,
        device=device,
    )
    weak_basis_tensor = torch.as_tensor(
        dataset.weak_basis_matrix,
        dtype=torch.float32,
        device=device,
    )
    weak_scale_tensor = torch.as_tensor(
        dataset.weak_scale_array,
        dtype=torch.float32,
        device=device,
    )
    failure_weight_tensor = torch.as_tensor(
        dataset.failure_weight_array,
        dtype=torch.float32,
        device=device,
    )

    # Verify Torch And SciPy Circular Derivative Parity
    parity_curve_matrix = dataset.base.curve_matrix[:4]
    scipy_derivative_matrix = savgol_filter(
        parity_curve_matrix,
        window_length=dataset.derivative_window_length,
        polyorder=3,
        deriv=1,
        delta=ANGULAR_DELTA,
        axis=1,
        mode="wrap",
    )
    torch_derivative_matrix = (
        circular_derivative_torch(
            torch.as_tensor(parity_curve_matrix, dtype=torch.float32),
            derivative_coefficient_tensor,
        )
        .detach()
        .cpu()
        .numpy()
    )
    derivative_parity_max_abs_error = float(
        np.max(
            np.abs(
                scipy_derivative_matrix - torch_derivative_matrix
            )
        )
    )
    assert derivative_parity_max_abs_error <= 1.0e-4

    candidate_row_list: list[dict[str, Any]] = []
    parameter_count_map: dict[str, int] = {}
    for specification in build_candidate_list():
        model = build_model(specification, dataset).to(device)
        model.train()
        batch = tensor_batch_for_split(
            dataset,
            specification.order_set_name,
            "train",
            device,
        )
        small_batch = {
            key: value[:4]
            for key, value in batch.items()
        }
        output = model(
            small_batch["condition"],
            small_batch["anchor"],
        )
        assert output["prediction_curve"].shape == (
            4,
            ANGULAR_SAMPLE_COUNT,
        )
        assert bool(torch.isfinite(output["prediction_curve"]).all())
        total_loss, _, _ = compute_loss_components(
            output,
            small_batch,
            specification,
            dataset,
            derivative_coefficient_tensor,
            weak_basis_tensor,
            weak_scale_tensor,
            failure_weight_tensor,
            epoch_index=MAXIMUM_EPOCH_COUNT - 1,
        )
        total_loss.backward()
        assert all(
            parameter.grad is None
            or bool(torch.isfinite(parameter.grad).all())
            for parameter in model.parameters()
        )

        trainable_parameter_count = sum(
            parameter.numel()
            for parameter in model.parameters()
            if parameter.requires_grad
        )
        parameter_count_map[specification.candidate_id] = (
            trainable_parameter_count
        )
        coordinate_bound_passed = True
        zero_replay_max_abs_error = float("nan")
        if specification.model_kind.startswith("coordinate_"):
            residual_tensor = output["coordinate_residual_curve"]
            coordinate_bound_passed = bool(
                torch.all(
                    torch.abs(residual_tensor)
                    <= model.residual_bound.unsqueeze(0) + 1.0e-7
                )
            )
            assert coordinate_bound_passed
            zero_replay_max_abs_error = float(
                torch.max(
                    torch.abs(
                        output["prediction_curve"]
                        - output["analytical_contribution_curve"]
                    )
                ).detach()
            )
            assert zero_replay_max_abs_error <= 1.0e-8

        candidate_row_list.append(
            {
                "candidate_id": specification.candidate_id,
                "model_kind": specification.model_kind,
                "trainable_parameter_count": trainable_parameter_count,
                "loss_finite": bool(torch.isfinite(total_loss)),
                "gradient_finite": True,
                "coordinate_bound_passed": coordinate_bound_passed,
                "zero_replay_max_abs_error": (
                    zero_replay_max_abs_error
                ),
            }
        )

    # Require Parameter-Matched Coordinate Architecture Pairs
    fourier_parameter_ratio = (
        parameter_count_map["FF01"] / parameter_count_map["FF00"]
    )
    siren_parameter_ratio = (
        parameter_count_map["SI01"] / parameter_count_map["SI00"]
    )
    assert 0.95 <= fourier_parameter_ratio <= 1.05
    assert 0.95 <= siren_parameter_ratio <= 1.05
    assert dataset.failure_effective_sample_ratio >= 0.70

    payload = {
        "schema_version": 1,
        "stage_name": STAGE_NAME,
        "validated_at": now_iso(),
        "candidate_count": len(candidate_row_list),
        "accepted_curve_count": int(
            dataset.base.curve_matrix.shape[0]
        ),
        "train_curve_count": int(
            np.sum(dataset.base.split_array == "train")
        ),
        "validation_curve_count": int(
            np.sum(dataset.base.split_array == "validation")
        ),
        "test_curve_count": int(
            np.sum(dataset.base.split_array == "test")
        ),
        "derivative_window_length": (
            dataset.derivative_window_length
        ),
        "derivative_parity_max_abs_error": (
            derivative_parity_max_abs_error
        ),
        "second_derivative_gate_passed": (
            dataset.second_derivative_gate_passed
        ),
        "second_derivative_sensitivity": (
            dataset.second_derivative_sensitivity
        ),
        "failure_effective_sample_ratio": (
            dataset.failure_effective_sample_ratio
        ),
        "fourier_control_parameter_ratio": fourier_parameter_ratio,
        "siren_control_parameter_ratio": siren_parameter_ratio,
        "runtime_target_or_derivative_input_count": 0,
        "all_checks_passed": True,
        "candidate_row_list": candidate_row_list,
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage6_preflight_validation_summary.yaml",
        payload,
    )
    return payload


def train_candidate(
    specification: CandidateSpecification,
    dataset: Stage6Dataset,
    campaign_output_directory: Path,
    random_seed: int,
) -> dict[str, Any]:
    """Fine-tune one candidate and persist immutable artifacts."""

    stage5.seed_everything(random_seed)
    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )
    model = build_model(specification, dataset).to(device)
    train_batch = tensor_batch_for_split(
        dataset,
        specification.order_set_name,
        "train",
        device,
    )
    validation_batch = tensor_batch_for_split(
        dataset,
        specification.order_set_name,
        "validation",
        device,
    )
    test_batch = tensor_batch_for_split(
        dataset,
        specification.order_set_name,
        "test",
        device,
    )
    derivative_coefficient_tensor = torch.as_tensor(
        dataset.derivative_coefficient_array,
        dtype=torch.float32,
        device=device,
    )
    weak_basis_tensor = torch.as_tensor(
        dataset.weak_basis_matrix,
        dtype=torch.float32,
        device=device,
    )
    weak_scale_tensor = torch.as_tensor(
        dataset.weak_scale_array,
        dtype=torch.float32,
        device=device,
    )
    failure_weight_tensor = torch.as_tensor(
        dataset.failure_weight_array,
        dtype=torch.float32,
        device=device,
    )

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=(
            5.0e-4
            if specification.model_kind.startswith("coordinate_")
            else 2.0e-4
        ),
        weight_decay=1.0e-5,
    )
    parameter_list = [
        parameter
        for parameter in model.parameters()
        if parameter.requires_grad
    ]

    best_validation_mae = float("inf")
    best_state_dictionary: dict[str, torch.Tensor] | None = None
    best_epoch = -1
    patience_count = 0
    history_row_list: list[dict[str, Any]] = []
    for epoch_index in range(MAXIMUM_EPOCH_COUNT):
        model.train()
        optimizer.zero_grad(set_to_none=True)
        training_output = model(
            train_batch["condition"],
            train_batch["anchor"],
        )
        (
            total_loss,
            component_tensor_map,
            scalar_payload,
        ) = compute_loss_components(
            training_output,
            train_batch,
            specification,
            dataset,
            derivative_coefficient_tensor,
            weak_basis_tensor,
            weak_scale_tensor,
            failure_weight_tensor,
            epoch_index,
        )

        gradient_payload = {
            "curve_gradient_norm": float("nan"),
            "spectral_gradient_norm": float("nan"),
            "derivative_gradient_norm": float("nan"),
            "weak_gradient_norm": float("nan"),
        }
        if epoch_index == 0 or (epoch_index + 1) % 8 == 0:
            for component_name, component_tensor in (
                component_tensor_map.items()
            ):
                if (
                    component_name == "curve"
                    or float(component_tensor.detach().cpu()) > 0.0
                ):
                    gradient_payload[
                        f"{component_name}_gradient_norm"
                    ] = gradient_norm(
                        component_tensor,
                        parameter_list,
                    )

        total_loss.backward()
        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=10.0,
        )
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
                **gradient_payload,
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
    model.eval()
    with torch.no_grad():
        test_output = model(
            test_batch["condition"],
            test_batch["anchor"],
        )
    predicted_curve_matrix = (
        test_output["prediction_curve"].detach().cpu().numpy()
    )
    test_mask = dataset.base.split_array == "test"
    measured_curve_matrix = dataset.base.curve_matrix[test_mask]
    metric_dictionary = aggregate_stage6_metrics(
        measured_curve_matrix,
        predicted_curve_matrix,
        dataset.derivative_window_length,
    )
    analytical_curve_matrix = (
        test_output["analytical_contribution_curve"]
        .detach()
        .cpu()
        .numpy()
    )
    correction_curve_matrix = (
        predicted_curve_matrix - analytical_curve_matrix
    )
    correction_rms = float(
        np.sqrt(np.mean(np.square(correction_curve_matrix)))
    )
    anchor_rms = float(
        np.sqrt(np.mean(np.square(analytical_curve_matrix)))
    )

    seed_suffix = (
        ""
        if random_seed == FIRST_SCREEN_SEED
        else f"__seed_{random_seed}"
    )
    run_instance_id = (
        f"{now_timestamp()}__stage6_"
        f"{specification.candidate_id.lower()}{seed_suffix}"
    )
    run_directory = RUN_ROOT_DIRECTORY / run_instance_id
    run_directory.mkdir(parents=True, exist_ok=True)
    checkpoint_path = run_directory / "best_model.pt"
    torch.save(
        {
            "state_dict": best_state_dictionary,
            "candidate": specification.__dict__,
            "harmonic_order_list": dataset.base.order_set_map[
                specification.order_set_name
            ],
            "feature_mean": dataset.base.feature_mean,
            "feature_scale": dataset.base.feature_scale,
            "derivative_window_length": (
                dataset.derivative_window_length
            ),
            "best_epoch": best_epoch,
        },
        checkpoint_path,
    )
    write_csv(run_directory / "training_history.csv", history_row_list)
    metrics_payload = {
        "schema_version": 1,
        "candidate_id": specification.candidate_id,
        "run_instance_id": run_instance_id,
        "random_seed": random_seed,
        "best_epoch": best_epoch,
        "validation_curve_mae_deg": best_validation_mae,
        "test_metrics": metric_dictionary,
        "correction_rms_deg": correction_rms,
        "anchor_rms_deg": anchor_rms,
        "correction_to_anchor_rms": (
            correction_rms / max(anchor_rms, 1.0e-12)
        ),
        "device": str(device),
        "checkpoint_path": checkpoint_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
    }
    write_yaml(run_directory / "metrics_summary.yaml", metrics_payload)
    write_yaml(
        run_directory / "training_config.yaml",
        {
            **specification.__dict__,
            "random_seed": random_seed,
            "harmonic_order_list": dataset.base.order_set_map[
                specification.order_set_name
            ],
            "maximum_epochs": MAXIMUM_EPOCH_COUNT,
            "minimum_epochs": MINIMUM_EPOCH_COUNT,
            "early_stopping_patience": EARLY_STOPPING_PATIENCE,
            "learning_rate": (
                5.0e-4
                if specification.model_kind.startswith("coordinate_")
                else 2.0e-4
            ),
            "weight_decay": 1.0e-5,
            "split_signature": SPLIT_SIGNATURE,
        },
    )
    np.savez_compressed(
        run_directory / "test_predictions.npz",
        condition_id=np.asarray(dataset.base.condition_id_list)[
            test_mask
        ],
        measured_curve=measured_curve_matrix.astype(np.float32),
        predicted_curve=predicted_curve_matrix.astype(np.float32),
        analytical_curve=analytical_curve_matrix.astype(np.float32),
        correction_curve=correction_curve_matrix.astype(np.float32),
    )

    row_payload = {
        "candidate_id": specification.candidate_id,
        "model_kind": specification.model_kind,
        "order_set_name": specification.order_set_name,
        "spectral_mode": specification.spectral_mode,
        "spectral_weight": specification.spectral_weight,
        "derivative_weight": specification.derivative_weight,
        "weak_weight": specification.weak_weight,
        "failure_weighted": specification.failure_weighted,
        "curriculum": specification.curriculum,
        "matched_control_id": specification.matched_control_id or "",
        "promotion_eligible": specification.promotion_eligible,
        "random_seed": random_seed,
        "run_instance_id": run_instance_id,
        "validation_curve_mae_deg": best_validation_mae,
        **metric_dictionary,
        "correction_to_anchor_rms": (
            correction_rms / max(anchor_rms, 1.0e-12)
        ),
        "checkpoint_path": checkpoint_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
    }
    log_path = (
        campaign_output_directory
        / "logs"
        / (
            f"{specification.queue_index:03d}_"
            f"{specification.candidate_id.lower()}"
            f"{seed_suffix}.log"
        )
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8", newline="\n") as log_file:
        yaml.safe_dump(
            row_payload,
            log_file,
            sort_keys=False,
            allow_unicode=False,
        )
    return row_payload


def load_stage5_h04_baseline_metrics(
    dataset: Stage6Dataset,
) -> dict[str, float]:
    """Recompute Stage 5 H04 on the complete Stage 6 metric surface."""

    with np.load(STAGE5_H04_PREDICTION_PATH) as payload:
        measured_curve_matrix = np.asarray(
            payload["measured_curve"],
            dtype=np.float64,
        )
        predicted_curve_matrix = np.asarray(
            payload["predicted_curve"],
            dtype=np.float64,
        )
    return aggregate_stage6_metrics(
        measured_curve_matrix,
        predicted_curve_matrix,
        dataset.derivative_window_length,
    )


def first_screen_gate(
    candidate_row: dict[str, Any],
    matched_row: dict[str, Any],
    baseline_metrics: dict[str, float],
) -> tuple[bool, dict[str, bool], float]:
    """Evaluate one promotion-eligible first-screen candidate."""

    gate_map = {
        "raw_mae_preserved": (
            float(candidate_row["mae_deg"])
            <= 1.01 * float(baseline_metrics["mae_deg"])
        ),
        "centered_mae_preserved": (
            float(candidate_row["centered_mae_deg"])
            <= 1.01 * float(baseline_metrics["centered_mae_deg"])
        ),
        "offset_preserved": (
            float(candidate_row["offset_abs_error_deg"])
            <= 1.01
            * float(baseline_metrics["offset_abs_error_deg"])
        ),
        "derivative_mae_improved": (
            float(candidate_row["sobolev_derivative_mae"])
            <= 0.995
            * float(baseline_metrics["sobolev_derivative_mae"])
        ),
        "derivative_correlation_improved": (
            float(candidate_row["sobolev_derivative_correlation"])
            >= float(
                baseline_metrics["sobolev_derivative_correlation"]
            )
        ),
        "harmonic_amplitude_improved": (
            float(candidate_row["retained_amplitude_mae_deg"])
            <= 0.995
            * float(baseline_metrics["retained_amplitude_mae_deg"])
        ),
        "harmonic_phase_improved": (
            float(candidate_row["retained_phase_mae_rad"])
            <= 0.995
            * float(baseline_metrics["retained_phase_mae_rad"])
        ),
        "p95_improved": (
            float(candidate_row["per_curve_mae_p95"])
            <= float(baseline_metrics["per_curve_mae_p95"])
        ),
        "matched_control_beaten": (
            float(candidate_row["mae_deg"])
            < float(matched_row["mae_deg"])
        ),
        "unsupported_energy_bounded": (
            float(
                candidate_row[
                    "unsupported_high_frequency_energy_ratio"
                ]
            )
            <= 1.10
        ),
    }
    normalized_score = float(
        np.mean(
            [
                float(candidate_row["mae_deg"])
                / max(float(baseline_metrics["mae_deg"]), 1.0e-12),
                float(candidate_row["sobolev_derivative_mae"])
                / max(
                    float(
                        baseline_metrics["sobolev_derivative_mae"]
                    ),
                    1.0e-12,
                ),
                float(candidate_row["retained_amplitude_mae_deg"])
                / max(
                    float(
                        baseline_metrics["retained_amplitude_mae_deg"]
                    ),
                    1.0e-12,
                ),
                float(candidate_row["retained_phase_mae_rad"])
                / max(
                    float(
                        baseline_metrics["retained_phase_mae_rad"]
                    ),
                    1.0e-12,
                ),
                float(candidate_row["per_curve_mae_p95"])
                / max(
                    float(baseline_metrics["per_curve_mae_p95"]),
                    1.0e-12,
                ),
            ]
        )
    )
    return all(gate_map.values()), gate_map, normalized_score


def run_campaign(dataset: Stage6Dataset) -> Path:
    """Execute the first screen and any qualified stability continuation."""

    campaign_output_directory = (
        PROJECT_ROOT
        / "output"
        / "training_campaigns"
        / f"{now_timestamp()}_{CAMPAIGN_NAME}"
    )
    campaign_output_directory.mkdir(parents=True, exist_ok=False)
    candidate_list = build_candidate_list()
    candidate_map = {
        specification.candidate_id: specification
        for specification in candidate_list
    }

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

    first_screen_row_list: list[dict[str, Any]] = []
    for specification in candidate_list:
        print(
            f"[stage6] Training {specification.candidate_id} "
            f"({specification.model_kind})"
        )
        first_screen_row_list.append(
            train_candidate(
                specification,
                dataset,
                campaign_output_directory,
                FIRST_SCREEN_SEED,
            )
        )

    first_screen_row_list.sort(
        key=lambda row: (
            float(row["mae_deg"]),
            str(row["candidate_id"]),
        )
    )
    write_csv(
        campaign_output_directory / "campaign_leaderboard.csv",
        first_screen_row_list,
    )
    write_yaml(
        campaign_output_directory / "campaign_leaderboard.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "completed_at": now_iso(),
            "row_list": first_screen_row_list,
        },
    )

    baseline_metrics = load_stage5_h04_baseline_metrics(dataset)
    row_map = {
        str(row["candidate_id"]): row
        for row in first_screen_row_list
    }
    gate_row_list: list[dict[str, Any]] = []
    passing_candidate_list: list[tuple[float, str]] = []
    for specification in candidate_list:
        if not specification.promotion_eligible:
            continue
        assert specification.matched_control_id is not None
        candidate_row = row_map[specification.candidate_id]
        matched_row = row_map[specification.matched_control_id]
        gate_passed, gate_map, normalized_score = first_screen_gate(
            candidate_row,
            matched_row,
            baseline_metrics,
        )
        gate_row_list.append(
            {
                "candidate_id": specification.candidate_id,
                "matched_control_id": (
                    specification.matched_control_id
                ),
                "all_first_screen_gates_passed": gate_passed,
                "normalized_score": normalized_score,
                **gate_map,
            }
        )
        if gate_passed:
            passing_candidate_list.append(
                (normalized_score, specification.candidate_id)
            )
    passing_candidate_list.sort()
    recommended_candidate_id = (
        passing_candidate_list[0][1]
        if passing_candidate_list
        else None
    )
    write_yaml(
        campaign_output_directory
        / "campaign_first_screen_gate_summary.yaml",
        {
            "schema_version": 1,
            "baseline": "stage5_h04_seed_314159",
            "baseline_metrics": baseline_metrics,
            "passing_candidate_id_list": [
                candidate_id
                for _, candidate_id in passing_candidate_list
            ],
            "recommended_candidate_id": recommended_candidate_id,
            "gate_row_list": gate_row_list,
        },
    )

    stability_row_list: list[dict[str, Any]] = []
    stability_passed = False
    if recommended_candidate_id is not None:
        selected_specification = candidate_map[
            recommended_candidate_id
        ]
        assert selected_specification.matched_control_id is not None
        matched_specification = candidate_map[
            selected_specification.matched_control_id
        ]
        for random_seed in STABILITY_SEED_LIST:
            for specification in (
                matched_specification,
                selected_specification,
            ):
                print(
                    f"[stage6 stability] Training "
                    f"{specification.candidate_id} seed {random_seed}"
                )
                stability_row_list.append(
                    train_candidate(
                        specification,
                        dataset,
                        campaign_output_directory,
                        random_seed,
                    )
                )
        write_csv(
            campaign_output_directory
            / "campaign_stability_leaderboard.csv",
            stability_row_list,
        )

        all_seed_gate_map: dict[int, bool] = {
            FIRST_SCREEN_SEED: True
        }
        stability_map = {
            (str(row["candidate_id"]), int(row["random_seed"])): row
            for row in stability_row_list
        }
        stability_gate_payload_list = []
        for random_seed in STABILITY_SEED_LIST:
            selected_row = stability_map[
                (recommended_candidate_id, random_seed)
            ]
            matched_row = stability_map[
                (
                    selected_specification.matched_control_id,
                    random_seed,
                )
            ]
            gate_passed, gate_map, normalized_score = (
                first_screen_gate(
                    selected_row,
                    matched_row,
                    baseline_metrics,
                )
            )
            all_seed_gate_map[random_seed] = gate_passed
            stability_gate_payload_list.append(
                {
                    "random_seed": random_seed,
                    "all_gates_passed": gate_passed,
                    "normalized_score": normalized_score,
                    **gate_map,
                }
            )
        stability_passed = all(all_seed_gate_map.values())
        write_yaml(
            campaign_output_directory
            / "campaign_stability_summary.yaml",
            {
                "schema_version": 1,
                "candidate_id": recommended_candidate_id,
                "matched_control_id": (
                    selected_specification.matched_control_id
                ),
                "completed_run_count": len(stability_row_list),
                "all_three_seeds_passed": stability_passed,
                "gate_payload_list": stability_gate_payload_list,
                "row_list": stability_row_list,
            },
        )

    raw_best_row = first_screen_row_list[0]
    final_recommended_candidate_id = (
        recommended_candidate_id if stability_passed else None
    )
    best_run_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "selection_basis": "first_screen_test_raw_mae",
        "candidate_id": raw_best_row["candidate_id"],
        "run_instance_id": raw_best_row["run_instance_id"],
        "test_mae_deg": raw_best_row["mae_deg"],
        "checkpoint_path": raw_best_row["checkpoint_path"],
        "multi_index_recommended_candidate_id": (
            final_recommended_candidate_id
        ),
        "stability_passed": stability_passed,
    }
    write_yaml(
        campaign_output_directory / "campaign_best_run.yaml",
        best_run_payload,
    )
    with (
        campaign_output_directory / "campaign_best_run.md"
    ).open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(
            "# Wave 5.2R Stage 6 Campaign Best Run\n\n"
            f"- Raw-error leader: `{raw_best_row['candidate_id']}`\n"
            f"- Test MAE: `{float(raw_best_row['mae_deg']):.9f} deg`\n"
            "- Multi-index recommendation: "
            f"`{final_recommended_candidate_id or 'none'}`\n"
            f"- Stability passed: `{str(stability_passed).lower()}`\n"
        )
    write_yaml(
        campaign_output_directory / "campaign_execution_summary.yaml",
        {
            "schema_version": 1,
            "status": "completed",
            "completed_at": now_iso(),
            "expected_run_count": len(candidate_list),
            "completed_run_count": len(first_screen_row_list),
            "failed_run_count": 0,
            "stability_completed_run_count": len(
                stability_row_list
            ),
            "stability_failed_run_count": 0,
            "raw_error_leader_id": raw_best_row["candidate_id"],
            "multi_index_recommended_candidate_id": (
                final_recommended_candidate_id
            ),
        },
    )

    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "status": "completed",
            "completed_at": now_iso(),
            "completed_run_count": len(first_screen_row_list),
            "failed_run_count": 0,
            "stability_completed_run_count": len(
                stability_row_list
            ),
            "stability_failed_run_count": 0,
            "campaign_best_run_path": (
                campaign_output_directory
                / "campaign_best_run.yaml"
            )
            .relative_to(PROJECT_ROOT)
            .as_posix(),
            "raw_error_leader_id": raw_best_row["candidate_id"],
            "multi_index_recommended_candidate_id": (
                final_recommended_candidate_id
            ),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return campaign_output_directory


def parse_arguments() -> argparse.Namespace:
    """Parse Stage 6 execution mode."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--run", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Prepare, validate, and optionally execute Stage 6."""

    arguments = parse_arguments()
    assert arguments.preflight_only or arguments.run
    dataset, derivative_calibration_row_list = build_stage6_dataset()
    prepare_campaign(dataset, derivative_calibration_row_list)
    preflight_payload = run_preflight(dataset)
    assert preflight_payload["all_checks_passed"]
    if arguments.preflight_only and not arguments.run:
        print(
            "[DONE] Stage 6 preflight passed for "
            f"{preflight_payload['candidate_count']} candidates."
        )
        return
    output_directory = run_campaign(dataset)
    print(
        "[DONE] Stage 6 campaign completed at "
        f"{output_directory.relative_to(PROJECT_ROOT).as_posix()}"
    )


if __name__ == "__main__":
    main()
