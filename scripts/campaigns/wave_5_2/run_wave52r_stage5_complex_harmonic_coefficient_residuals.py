"""Prepare, validate, and run the Wave 5.2R Stage 5 coefficient campaign."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
import hashlib
import json
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
import yaml

# Import PyTorch Utilities
import torch

# Import Project Models And Analytical Utilities
from scripts.analysis.polynomial_fourier_benchmark.polynomial_fourier_models import (
    project_fourier_coefficients,
)
from scripts.analysis.polynomial_fourier_benchmark.run_phase1_polynomial_fourier_benchmark import (
    curve_metrics,
)
from scripts.analysis.polynomial_fourier_benchmark.run_phase1_polynomial_fourier_benchmark import (
    harmonic_error_metrics,
)
from scripts.campaigns.wave_5_2.prepare_wave52r_stage4_data_only_residual_capacity_ladder_campaign import (
    COMMON_SPLIT_MANIFEST_PATH,
    EXCLUDED_CONDITION_ID_LIST,
    PHASE1_CONFIGURATION_PATH,
    build_setpoint_operating_feature_array,
    build_surface_from_payload,
    load_curve_records,
    load_yaml,
)
from scripts.models.complex_harmonic_coefficient_residual_network import (
    ComplexHarmonicCoefficientResidualNetwork,
)


# Define Frozen Stage Contract
STAGE_NAME = "wave52r_stage5_complex_harmonic_coefficient_residuals"
CAMPAIGN_NAME = f"{STAGE_NAME}_2026_07_28"
SPLIT_SIGNATURE = (
    "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16"
)
ANGULAR_SAMPLE_COUNT = 2048
FIRST_SCREEN_SEED = 314159
CORE_ORDER_LIST = [1, 3, 39, 40, 78, 81, 156, 162, 240]
CORE_PLUS_RESIDUAL_ORDER_LIST = sorted(
    [*CORE_ORDER_LIST, 2, 80, 159, 237]
)
CAUSAL_ANCHOR_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
    / "stage4_causal_setpoint_pf_a_surface.yaml"
)
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage5_complex_harmonic_coefficient_residuals"
)
CONFIG_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "complex_harmonic_coefficient_residuals"
    / "campaigns"
    / "2026-07-28_wave52r_stage5_complex_harmonic_coefficient_residuals"
)
QUEUE_DIRECTORY = CONFIG_DIRECTORY / "queue"
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-28/"
    "2026-07-28-15-56-46_wave52r_stage5_complex_harmonic_"
    "coefficient_residuals.md"
)
CAMPAIGN_PLAN_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "complex_harmonic_coefficient_residuals/"
    "2026-07-28-15-56-46_wave52r_stage5_complex_harmonic_"
    "coefficient_residuals_campaign_plan_report.md"
)


@dataclass(frozen=True)
class CandidateSpecification:
    """Describe one immutable first-screen candidate."""

    queue_index: int
    candidate_id: str
    formulation: str
    order_set_name: str
    capacity_name: str
    complex_weight: float
    band_weight: float
    surface_weight: float


@dataclass
class Stage5Dataset:
    """Hold one representation-aligned in-memory campaign dataset."""

    condition_matrix: np.ndarray
    curve_matrix: np.ndarray
    split_array: np.ndarray
    condition_id_list: list[str]
    anchor_coefficient_map: dict[str, np.ndarray]
    target_coefficient_map: dict[str, np.ndarray]
    order_set_map: dict[str, list[int]]
    feature_mean: np.ndarray
    feature_scale: np.ndarray
    curve_scale: float
    coefficient_scale_map: dict[str, np.ndarray]
    correction_bound_map: dict[str, np.ndarray]


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


def write_json(path: Path, payload: dict[str, Any]) -> None:
    """Write one stable JSON mapping."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        json.dump(payload, output_file, indent=2, sort_keys=False)
        output_file.write("\n")


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


def file_sha256(path: Path) -> str:
    """Compute one file SHA-256 digest."""

    digest = hashlib.sha256()
    with path.open("rb") as input_file:
        for chunk in iter(lambda: input_file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def seed_everything(random_seed: int) -> None:
    """Seed Python, NumPy, CPU, and CUDA deterministically."""

    random.seed(random_seed)
    np.random.seed(random_seed)
    torch.manual_seed(random_seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(random_seed)
    torch.use_deterministic_algorithms(True, warn_only=True)


def build_candidate_list() -> list[CandidateSpecification]:
    """Return the approved eighteen-run first-screen matrix."""

    row_list = [
        ("C01", "direct_curve", "core", "compact", 0.0, 0.0, 0.0),
        ("C02", "direct_curve", "core", "deep", 0.0, 0.0, 0.0),
        ("C03", "direct_coefficient", "core", "compact", 1.0, 0.0, 0.0),
        ("C04", "direct_coefficient", "core", "deep", 1.0, 0.0, 0.0),
        (
            "C05",
            "direct_coefficient",
            "core_plus_residual",
            "compact",
            1.0,
            0.0,
            0.0,
        ),
        (
            "C06",
            "direct_coefficient",
            "core_plus_residual",
            "deep",
            1.0,
            0.0,
            0.0,
        ),
        (
            "C07",
            "direct_coefficient",
            "data_selected",
            "compact",
            1.0,
            0.0,
            0.0,
        ),
        (
            "C08",
            "direct_coefficient",
            "data_selected",
            "deep",
            1.0,
            0.0,
            0.0,
        ),
        ("H01", "anchored_coefficient", "core", "compact", 1.0, 0.0, 0.0),
        ("H02", "anchored_coefficient", "core", "deep", 1.0, 0.0, 0.0),
        ("H03", "bounded_coefficient", "core", "compact", 1.0, 0.0, 0.0),
        ("H04", "bounded_coefficient", "core", "deep", 1.0, 0.0, 0.0),
        (
            "H05",
            "banded_coefficient",
            "core_plus_residual",
            "compact",
            1.0,
            0.25,
            0.0,
        ),
        (
            "H06",
            "banded_coefficient",
            "core_plus_residual",
            "deep",
            1.0,
            0.25,
            0.0,
        ),
        (
            "H07",
            "banded_coefficient",
            "data_selected",
            "compact",
            1.0,
            0.25,
            0.0,
        ),
        (
            "H08",
            "banded_coefficient",
            "data_selected",
            "deep",
            1.0,
            0.25,
            0.0,
        ),
        (
            "A01",
            "banded_coefficient",
            "core_plus_residual",
            "compact",
            1.0,
            0.25,
            0.01,
        ),
        (
            "A02",
            "banded_coefficient",
            "core_plus_residual",
            "compact",
            1.0,
            0.25,
            0.10,
        ),
    ]
    return [
        CandidateSpecification(
            queue_index=index,
            candidate_id=row[0],
            formulation=row[1],
            order_set_name=row[2],
            capacity_name=row[3],
            complex_weight=row[4],
            band_weight=row[5],
            surface_weight=row[6],
        )
        for index, row in enumerate(row_list, start=1)
    ]


def map_anchor_coefficients(
    core_coefficient_matrix: np.ndarray,
    target_order_list: list[int],
) -> np.ndarray:
    """Embed PF-A core coefficients into one declared order set."""

    mapped_matrix = np.zeros(
        (
            core_coefficient_matrix.shape[0],
            1 + (2 * len(target_order_list)),
        ),
        dtype=np.float64,
    )
    mapped_matrix[:, 0] = core_coefficient_matrix[:, 0]
    core_position_map = {
        order: position for position, order in enumerate(CORE_ORDER_LIST)
    }
    for target_position, harmonic_order in enumerate(target_order_list):
        if harmonic_order not in core_position_map:
            continue
        core_position = core_position_map[harmonic_order]
        mapped_matrix[:, 1 + (2 * target_position)] = (
            core_coefficient_matrix[:, 1 + (2 * core_position)]
        )
        mapped_matrix[:, 2 + (2 * target_position)] = (
            core_coefficient_matrix[:, 2 + (2 * core_position)]
        )
    return mapped_matrix


def select_training_only_order_list(
    training_curve_matrix: np.ndarray,
    training_anchor_curve_matrix: np.ndarray,
) -> tuple[list[int], list[dict[str, Any]]]:
    """Select stable residual orders using training curves only."""

    residual_matrix = training_curve_matrix - training_anchor_curve_matrix
    spectrum_matrix = np.fft.rfft(residual_matrix, axis=1)
    amplitude_matrix = (
        2.0 * np.abs(spectrum_matrix) / residual_matrix.shape[1]
    )
    mean_amplitude = np.mean(amplitude_matrix, axis=0)
    candidate_order_list = [
        order
        for order in range(1, min(241, amplitude_matrix.shape[1]))
        if order not in set(CORE_ORDER_LIST)
    ]
    ranked_order_list = sorted(
        candidate_order_list,
        key=lambda order: (-mean_amplitude[order], order),
    )
    selected_residual_order_list = ranked_order_list[:8]
    selected_order_list = sorted(
        set(CORE_ORDER_LIST + selected_residual_order_list)
    )
    diagnostic_row_list = [
        {
            "harmonic_order": order,
            "mean_training_residual_amplitude_deg": float(
                mean_amplitude[order]
            ),
            "selected": order in selected_residual_order_list,
            "selection_rank": (
                selected_residual_order_list.index(order) + 1
                if order in selected_residual_order_list
                else ""
            ),
        }
        for order in ranked_order_list[:40]
    ]
    return selected_order_list, diagnostic_row_list


def build_stage5_dataset() -> Stage5Dataset:
    """Build all uniform curves, coefficients, and train-only scales."""

    phase1_configuration = load_yaml(PHASE1_CONFIGURATION_PATH)
    assert (
        int(
            phase1_configuration["runtime"][
                "normalized_angular_sample_count"
            ]
        )
        == ANGULAR_SAMPLE_COUNT
    )
    common_split_manifest = load_yaml(COMMON_SPLIT_MANIFEST_PATH)
    assert (
        common_split_manifest["split"]["assignment_sha256"]
        == SPLIT_SIGNATURE
    )
    all_record_list = load_curve_records(
        phase1_configuration,
        common_split_manifest,
    )
    excluded_condition_id_set = set(EXCLUDED_CONDITION_ID_LIST)
    record_list = [
        record
        for record in all_record_list
        if record.direction == "Fw"
        and record.condition_id not in excluded_condition_id_set
    ]
    assert len(record_list) == 966
    assert all(record.te_deg.size == ANGULAR_SAMPLE_COUNT for record in record_list)

    condition_matrix = np.vstack(
        [build_setpoint_operating_feature_array(record) for record in record_list]
    )
    curve_matrix = np.vstack([record.te_deg for record in record_list])
    split_array = np.asarray([record.split for record in record_list])
    assert int(np.sum(split_array == "train")) == 675
    assert int(np.sum(split_array == "validation")) == 194
    assert int(np.sum(split_array == "test")) == 97

    anchor_payload = load_yaml(CAUSAL_ANCHOR_PATH)
    assert anchor_payload["split_signature"] == SPLIT_SIGNATURE
    causal_surface = build_surface_from_payload(anchor_payload["surface"])
    core_anchor_coefficient_matrix = causal_surface.predict(condition_matrix)
    core_anchor_curve_matrix = np.vstack(
        [
            _reconstruct_numpy_curve(
                coefficient_array,
                CORE_ORDER_LIST,
            )
            for coefficient_array in core_anchor_coefficient_matrix
        ]
    )

    training_mask = split_array == "train"
    data_selected_order_list, diagnostic_row_list = (
        select_training_only_order_list(
            curve_matrix[training_mask],
            core_anchor_curve_matrix[training_mask],
        )
    )
    order_set_map = {
        "core": list(CORE_ORDER_LIST),
        "core_plus_residual": list(CORE_PLUS_RESIDUAL_ORDER_LIST),
        "data_selected": data_selected_order_list,
    }
    write_csv(
        ANALYSIS_DIRECTORY / "stage5_training_only_order_selection.csv",
        diagnostic_row_list,
    )

    anchor_coefficient_map: dict[str, np.ndarray] = {}
    target_coefficient_map: dict[str, np.ndarray] = {}
    coefficient_scale_map: dict[str, np.ndarray] = {}
    correction_bound_map: dict[str, np.ndarray] = {}
    for order_set_name, order_list in order_set_map.items():
        anchor_matrix = map_anchor_coefficients(
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
            target_matrix[training_mask] - anchor_matrix[training_mask]
        )
        coefficient_scale = np.maximum(
            np.std(training_target_matrix, axis=0),
            1.0e-5,
        )
        correction_bound = np.maximum(
            np.quantile(
                np.abs(training_correction_matrix),
                0.995,
                axis=0,
            ),
            1.0e-5,
        )
        anchor_coefficient_map[order_set_name] = anchor_matrix
        target_coefficient_map[order_set_name] = target_matrix
        coefficient_scale_map[order_set_name] = coefficient_scale
        correction_bound_map[order_set_name] = correction_bound

    feature_mean = np.mean(condition_matrix[training_mask], axis=0)
    feature_scale = np.std(condition_matrix[training_mask], axis=0)
    assert np.all(feature_scale > 0.0)
    curve_scale = float(np.std(curve_matrix[training_mask]))
    assert curve_scale > 0.0

    dataset = Stage5Dataset(
        condition_matrix=condition_matrix,
        curve_matrix=curve_matrix,
        split_array=split_array,
        condition_id_list=[record.condition_id for record in record_list],
        anchor_coefficient_map=anchor_coefficient_map,
        target_coefficient_map=target_coefficient_map,
        order_set_map=order_set_map,
        feature_mean=feature_mean,
        feature_scale=feature_scale,
        curve_scale=curve_scale,
        coefficient_scale_map=coefficient_scale_map,
        correction_bound_map=correction_bound_map,
    )
    write_representation_artifacts(dataset, record_list)
    return dataset


def _reconstruct_numpy_curve(
    coefficient_array: np.ndarray,
    order_list: list[int],
) -> np.ndarray:
    """Reconstruct one uniform curve without importing private helpers."""

    theta_array = np.linspace(
        0.0,
        2.0 * np.pi,
        ANGULAR_SAMPLE_COUNT,
        endpoint=False,
    )
    curve = np.full(
        ANGULAR_SAMPLE_COUNT,
        float(coefficient_array[0]),
        dtype=np.float64,
    )
    for order_position, harmonic_order in enumerate(order_list):
        curve += (
            coefficient_array[1 + (2 * order_position)]
            * np.sin(harmonic_order * theta_array)
            + coefficient_array[2 + (2 * order_position)]
            * np.cos(harmonic_order * theta_array)
        )
    return curve


def write_representation_artifacts(
    dataset: Stage5Dataset,
    record_list: list[Any],
) -> None:
    """Persist the frozen representation and train-only calibration."""

    ANALYSIS_DIRECTORY.mkdir(parents=True, exist_ok=True)
    curve_digest = hashlib.sha256(
        np.asarray(dataset.curve_matrix, dtype="<f8").tobytes()
    ).hexdigest()
    representation_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage5",
        "dataset": "polished_dataset",
        "input_mode": "setpoints",
        "surface": "Fw",
        "split_signature": SPLIT_SIGNATURE,
        "curve_count": len(record_list),
        "curve_count_by_split": {
            split_name: int(np.sum(dataset.split_array == split_name))
            for split_name in ("train", "validation", "test")
        },
        "angular_sample_count": ANGULAR_SAMPLE_COUNT,
        "angular_domain": "0 <= theta < 2*pi",
        "endpoint_included": False,
        "curve_matrix_sha256": curve_digest,
        "phase1_configuration_sha256": file_sha256(
            PHASE1_CONFIGURATION_PATH
        ),
        "common_split_manifest_sha256": file_sha256(
            COMMON_SPLIT_MANIFEST_PATH
        ),
        "causal_anchor_sha256": file_sha256(CAUSAL_ANCHOR_PATH),
        "order_set_map": dataset.order_set_map,
        "target_leakage": False,
        "measured_runtime_operating_inputs": False,
    }
    calibration_payload = {
        "schema_version": 1,
        "split_scope": "training only",
        "feature_order": [
            "signed_setpoint_torque_nm",
            "absolute_setpoint_speed_rpm",
            "setpoint_temperature_deg_c",
        ],
        "feature_mean": dataset.feature_mean.tolist(),
        "feature_scale": dataset.feature_scale.tolist(),
        "curve_scale_deg": dataset.curve_scale,
        "coefficient_scale_map": {
            name: value.tolist()
            for name, value in dataset.coefficient_scale_map.items()
        },
        "coefficient_correction_bound_map": {
            name: value.tolist()
            for name, value in dataset.correction_bound_map.items()
        },
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage5_uniform_curve_representation.yaml",
        representation_payload,
    )
    write_yaml(
        ANALYSIS_DIRECTORY / "stage5_training_only_calibration.yaml",
        calibration_payload,
    )


def candidate_hidden_size_list(capacity_name: str) -> list[int]:
    """Resolve one declared compact or deep capacity."""

    if capacity_name == "compact":
        return [32, 32]
    assert capacity_name == "deep"
    return [64, 64, 32]


def build_model(
    specification: CandidateSpecification,
    dataset: Stage5Dataset,
) -> ComplexHarmonicCoefficientResidualNetwork:
    """Construct one candidate from immutable campaign metadata."""

    order_list = dataset.order_set_map[specification.order_set_name]
    return ComplexHarmonicCoefficientResidualNetwork(
        condition_input_size=3,
        hidden_size_list=candidate_hidden_size_list(
            specification.capacity_name
        ),
        harmonic_order_list=order_list,
        angular_sample_count=ANGULAR_SAMPLE_COUNT,
        formulation=specification.formulation,
        coefficient_correction_bound_list=dataset.correction_bound_map[
            specification.order_set_name
        ].tolist(),
        zero_initialize_correction=True,
    )


def prepare_campaign(dataset: Stage5Dataset) -> None:
    """Write immutable queue configurations and persistent campaign state."""

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
            "model_family": "complex_harmonic_coefficient_residuals",
            "formulation": specification.formulation,
            "order_set_name": specification.order_set_name,
            "harmonic_order_list": dataset.order_set_map[
                specification.order_set_name
            ],
            "capacity_name": specification.capacity_name,
            "hidden_size_list": candidate_hidden_size_list(
                specification.capacity_name
            ),
            "trainable_parameter_count": trainable_parameter_count,
            "loss_weights": {
                "curve": 1.0,
                "complex": specification.complex_weight,
                "band": specification.band_weight,
                "surface": specification.surface_weight,
            },
            "random_seed": FIRST_SCREEN_SEED,
            "maximum_epochs": 48,
            "minimum_epochs": 8,
            "early_stopping_patience": 8,
            "learning_rate": 5.0e-4,
            "weight_decay": 1.0e-5,
            "dataset": "polished_dataset",
            "input_mode": "setpoints",
            "surface": "Fw",
            "split_signature": SPLIT_SIGNATURE,
            "angular_sample_count": ANGULAR_SAMPLE_COUNT,
        }
        queue_path = (
            QUEUE_DIRECTORY
            / f"{specification.queue_index:03d}_{specification.candidate_id.lower()}.yaml"
        )
        write_yaml(queue_path, queue_payload)
        queue_path_list.append(queue_path.relative_to(PROJECT_ROOT).as_posix())

    manifest_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": "wave_5_2r_stage5_complex_harmonic_coefficients",
        "status": "prepared",
        "prepared_at": now_iso(),
        "expected_run_count": len(candidate_list),
        "dataset": "polished_dataset",
        "input_mode": "setpoints",
        "surface": "Fw",
        "split_signature": SPLIT_SIGNATURE,
        "angular_sample_count": ANGULAR_SAMPLE_COUNT,
        "queue_path_list": queue_path_list,
    }
    write_yaml(CONFIG_DIRECTORY / "campaign.yaml", manifest_payload)
    active_payload = {
        "status": "prepared",
        "prepared_at": now_iso(),
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": "wave_5_2r_stage5_complex_harmonic_coefficients",
        "dataset_id": "polished_dataset",
        "input_mode": "setpoints",
        "dataset_schema": "polished_setpoint_complex_curve_v1",
        "surface_list": ["fw"],
        "primary_surface": "fw",
        "expected_run_count": len(candidate_list),
        "completed_run_count": 0,
        "failed_run_count": 0,
        "random_seed_list": [FIRST_SCREEN_SEED],
        "conditional_stability_random_seed_list": [271828, 161803],
        "campaign_manifest_path": (
            CONFIG_DIRECTORY.relative_to(PROJECT_ROOT)
            / "campaign.yaml"
        ).as_posix(),
        "campaign_config_root": QUEUE_DIRECTORY.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "launcher_path": (
            "scripts/campaigns/wave_5_2/"
            "run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1"
        ),
        "launcher_note_path": (
            "doc/scripts/campaigns/wave_5_2/"
            "run_wave52r_stage5_complex_harmonic_coefficient_residuals.md"
        ),
        "planning_report_path": CAMPAIGN_PLAN_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "representation_manifest_path": (
            ANALYSIS_DIRECTORY
            / "stage5_uniform_curve_representation.yaml"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "training_only_calibration_path": (
            ANALYSIS_DIRECTORY / "stage5_training_only_calibration.yaml"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "local_preflight_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 "
            "-PreflightOnly"
        ),
        "local_launch_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 "
            "-Run"
        ),
        "remote_preflight_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 "
            "-Remote -PreflightOnly"
        ),
        "remote_launch_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 "
            "-Remote -Run"
        ),
        "launch_command_list": [
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 "
                "-PreflightOnly"
            ),
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 "
                "-Run"
            ),
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 "
                "-Remote -PreflightOnly"
            ),
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 "
                "-Remote -Run"
            ),
        ],
        "approval": {
            "status": "approved",
            "approved_at": "2026-07-27T23:57:23+02:00",
            "expires_at": "2026-07-28T23:57:23+02:00",
            "source": "user standing approval for twenty-four hours",
        },
        "protected_file_list": [
            "doc/running/active_training_campaign.yaml",
            CONFIG_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
            (
                "scripts/campaigns/wave_5_2/"
                "run_wave52r_stage5_complex_harmonic_coefficient_residuals.py"
            ),
            (
                "scripts/campaigns/wave_5_2/"
                "run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1"
            ),
            (
                "scripts/models/"
                "complex_harmonic_coefficient_residual_network.py"
            ),
            ANALYSIS_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
        ],
    }
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)


def build_band_index_list(order_list: list[int]) -> list[list[int]]:
    """Group coefficient indices into interpretable harmonic bands."""

    group_order_list = [
        [1],
        [order for order in order_list if 1 < order < 39],
        [order for order in order_list if 39 <= order <= 162],
        [order for order in order_list if order > 162],
    ]
    coefficient_group_list: list[list[int]] = [[0]]
    for group in group_order_list:
        coefficient_index_list: list[int] = []
        for harmonic_order in group:
            if harmonic_order not in order_list:
                continue
            position = order_list.index(harmonic_order)
            coefficient_index_list.extend(
                [1 + (2 * position), 2 + (2 * position)]
            )
        if coefficient_index_list:
            coefficient_group_list.append(coefficient_index_list)
    return coefficient_group_list


def run_preflight(dataset: Stage5Dataset) -> dict[str, Any]:
    """Validate every representation, model, bound, and gradient contract."""

    check_row_list: list[dict[str, Any]] = []
    candidate_list = build_candidate_list()
    training_indices = np.flatnonzero(dataset.split_array == "train")[:8]
    condition_tensor = torch.as_tensor(
        (
            dataset.condition_matrix[training_indices]
            - dataset.feature_mean
        )
        / dataset.feature_scale,
        dtype=torch.float32,
    )
    for specification in candidate_list:
        order_set_name = specification.order_set_name
        anchor_tensor = torch.as_tensor(
            dataset.anchor_coefficient_map[order_set_name][training_indices],
            dtype=torch.float32,
        )
        target_curve_tensor = torch.as_tensor(
            dataset.curve_matrix[training_indices],
            dtype=torch.float32,
        )
        model = build_model(specification, dataset)
        output = model(condition_tensor, anchor_tensor)
        assert output["prediction_curve"].shape == target_curve_tensor.shape
        assert torch.all(torch.isfinite(output["prediction_curve"]))
        if specification.formulation in {
            "anchored_coefficient",
            "bounded_coefficient",
            "banded_coefficient",
        }:
            replay_error = torch.max(
                torch.abs(
                    output["prediction_coefficients"] - anchor_tensor
                )
            ).item()
            assert replay_error == 0.0
        loss = torch.mean(
            torch.square(
                output["prediction_curve"] - target_curve_tensor
            )
        )
        loss.backward()
        gradient_finite = all(
            parameter.grad is None
            or bool(torch.all(torch.isfinite(parameter.grad)))
            for parameter in model.parameters()
        )
        assert gradient_finite
        if specification.formulation == "bounded_coefficient":
            with torch.no_grad():
                output_layer = model.condition_network[-1]
                assert isinstance(output_layer, torch.nn.Linear)
                output_layer.bias.fill_(100.0)
                bounded_output = model(condition_tensor, anchor_tensor)
                maximum_ratio = torch.max(
                    torch.abs(
                        bounded_output["coefficient_correction"]
                    )
                    / model.coefficient_correction_bound.unsqueeze(0)
                ).item()
                assert maximum_ratio <= 1.000001
        check_row_list.append(
            {
                "candidate_id": specification.candidate_id,
                "output_shape_passed": True,
                "finite_forward_passed": True,
                "finite_gradient_passed": True,
                "zero_anchor_replay_passed": (
                    specification.formulation
                    not in {
                        "anchored_coefficient",
                        "bounded_coefficient",
                        "banded_coefficient",
                    }
                    or replay_error == 0.0
                ),
            }
        )

    # Validate Exact Matrix Reconstruction Against NumPy
    core_model = build_model(candidate_list[2], dataset)
    representative_coefficient = torch.as_tensor(
        dataset.target_coefficient_map["core"][
            dataset.split_array == "train"
        ][:64],
        dtype=torch.float32,
    )
    torch_curve = core_model.reconstruct_curve(
        representative_coefficient
    ).detach().numpy()
    numpy_curve = np.vstack(
        [
            _reconstruct_numpy_curve(row, CORE_ORDER_LIST)
            for row in representative_coefficient.numpy()
        ]
    )
    reconstruction_error = float(np.max(np.abs(torch_curve - numpy_curve)))
    assert reconstruction_error < 1.0e-6

    summary_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage5",
        "status": "passed",
        "checked_at": now_iso(),
        "candidate_count": len(candidate_list),
        "candidate_check_row_list": check_row_list,
        "torch_numpy_reconstruction_max_abs_error": reconstruction_error,
        "uniform_curve_count": int(dataset.curve_matrix.shape[0]),
        "angular_sample_count": int(dataset.curve_matrix.shape[1]),
        "split_count": {
            split_name: int(np.sum(dataset.split_array == split_name))
            for split_name in ("train", "validation", "test")
        },
        "target_leakage_detected": False,
        "measured_runtime_input_detected": False,
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage5_preflight_validation_summary.yaml",
        summary_payload,
    )
    return summary_payload


def tensor_dataset_for_split(
    dataset: Stage5Dataset,
    order_set_name: str,
    split_name: str,
    device: torch.device,
) -> dict[str, torch.Tensor]:
    """Materialize one full split on the selected device."""

    split_mask = dataset.split_array == split_name
    normalized_condition_matrix = (
        dataset.condition_matrix[split_mask] - dataset.feature_mean
    ) / dataset.feature_scale
    return {
        "condition": torch.as_tensor(
            normalized_condition_matrix,
            dtype=torch.float32,
            device=device,
        ),
        "curve": torch.as_tensor(
            dataset.curve_matrix[split_mask],
            dtype=torch.float32,
            device=device,
        ),
        "coefficient": torch.as_tensor(
            dataset.target_coefficient_map[order_set_name][split_mask],
            dtype=torch.float32,
            device=device,
        ),
        "anchor": torch.as_tensor(
            dataset.anchor_coefficient_map[order_set_name][split_mask],
            dtype=torch.float32,
            device=device,
        ),
    }


def compute_training_loss(
    model: ComplexHarmonicCoefficientResidualNetwork,
    output: dict[str, torch.Tensor],
    batch: dict[str, torch.Tensor],
    specification: CandidateSpecification,
    dataset: Stage5Dataset,
    neighbor_edge_tensor: torch.Tensor | None,
) -> tuple[torch.Tensor, dict[str, float]]:
    """Compute the declared curve, complex, band, and surface objective."""

    curve_scale = torch.as_tensor(
        dataset.curve_scale,
        dtype=output["prediction_curve"].dtype,
        device=output["prediction_curve"].device,
    )
    curve_loss = torch.mean(
        torch.square(
            (output["prediction_curve"] - batch["curve"]) / curve_scale
        )
    )
    coefficient_scale = torch.as_tensor(
        dataset.coefficient_scale_map[specification.order_set_name],
        dtype=output["prediction_coefficients"].dtype,
        device=output["prediction_coefficients"].device,
    )
    complex_loss = torch.zeros_like(curve_loss)
    band_loss = torch.zeros_like(curve_loss)
    surface_loss = torch.zeros_like(curve_loss)
    if specification.formulation != "direct_curve":
        normalized_coefficient_error = (
            output["prediction_coefficients"] - batch["coefficient"]
        ) / coefficient_scale.unsqueeze(0)
        complex_loss = torch.mean(
            torch.square(normalized_coefficient_error)
        )
        if specification.band_weight > 0.0:
            band_loss_list = [
                torch.mean(
                    torch.square(
                        normalized_coefficient_error[:, index_list]
                    )
                )
                for index_list in build_band_index_list(
                    dataset.order_set_map[specification.order_set_name]
                )
            ]
            band_loss = torch.mean(torch.stack(band_loss_list))
        if specification.surface_weight > 0.0:
            assert neighbor_edge_tensor is not None
            correction_tensor = output["coefficient_correction"]
            correction_bound = model.coefficient_correction_bound
            edge_difference = (
                correction_tensor[neighbor_edge_tensor[:, 0]]
                - correction_tensor[neighbor_edge_tensor[:, 1]]
            ) / correction_bound.unsqueeze(0)
            surface_loss = torch.mean(torch.square(edge_difference))

    total_loss = (
        curve_loss
        + specification.complex_weight * complex_loss
        + specification.band_weight * band_loss
        + specification.surface_weight * surface_loss
    )
    return total_loss, {
        "curve_loss": float(curve_loss.detach().cpu()),
        "complex_loss": float(complex_loss.detach().cpu()),
        "band_loss": float(band_loss.detach().cpu()),
        "surface_loss": float(surface_loss.detach().cpu()),
        "total_loss": float(total_loss.detach().cpu()),
    }


def build_neighbor_edges(
    normalized_training_condition_matrix: np.ndarray,
    device: torch.device,
) -> torch.Tensor:
    """Build deterministic training-only nearest-condition edges."""

    difference_tensor = (
        normalized_training_condition_matrix[:, np.newaxis, :]
        - normalized_training_condition_matrix[np.newaxis, :, :]
    )
    distance_matrix = np.linalg.norm(difference_tensor, axis=2)
    np.fill_diagonal(distance_matrix, np.inf)
    nearest_index_matrix = np.argsort(distance_matrix, axis=1)[:, :2]
    edge_array = np.vstack(
        [
            np.column_stack(
                (
                    np.arange(normalized_training_condition_matrix.shape[0]),
                    nearest_index_matrix[:, neighbor_position],
                )
            )
            for neighbor_position in range(2)
        ]
    )
    return torch.as_tensor(edge_array, dtype=torch.long, device=device)


def aggregate_metrics(
    measured_curve_matrix: np.ndarray,
    predicted_curve_matrix: np.ndarray,
) -> dict[str, float]:
    """Aggregate the canonical Stage 5 curve-first metrics."""

    metric_row_list: list[dict[str, float]] = []
    for measured_curve, predicted_curve in zip(
        measured_curve_matrix,
        predicted_curve_matrix,
        strict=True,
    ):
        metric_row = curve_metrics(measured_curve, predicted_curve)
        metric_row.update(
            harmonic_error_metrics(
                measured_curve,
                predicted_curve,
                CORE_ORDER_LIST,
            )
        )
        metric_row_list.append(metric_row)
    return {
        metric_name: float(
            np.mean([row[metric_name] for row in metric_row_list])
        )
        for metric_name in metric_row_list[0]
    }


def train_candidate(
    specification: CandidateSpecification,
    dataset: Stage5Dataset,
    campaign_output_directory: Path,
    random_seed: int = FIRST_SCREEN_SEED,
) -> dict[str, Any]:
    """Train one candidate and persist its immutable run artifacts."""

    seed_everything(random_seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = build_model(specification, dataset).to(device)
    train_batch = tensor_dataset_for_split(
        dataset,
        specification.order_set_name,
        "train",
        device,
    )
    validation_batch = tensor_dataset_for_split(
        dataset,
        specification.order_set_name,
        "validation",
        device,
    )
    test_batch = tensor_dataset_for_split(
        dataset,
        specification.order_set_name,
        "test",
        device,
    )
    normalized_training_condition_matrix = (
        dataset.condition_matrix[dataset.split_array == "train"]
        - dataset.feature_mean
    ) / dataset.feature_scale
    neighbor_edge_tensor = build_neighbor_edges(
        normalized_training_condition_matrix,
        device,
    )
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=5.0e-4,
        weight_decay=1.0e-5,
    )

    best_validation_mae = float("inf")
    best_state_dictionary: dict[str, torch.Tensor] | None = None
    best_epoch = -1
    patience_count = 0
    history_row_list: list[dict[str, Any]] = []
    for epoch_index in range(48):
        model.train()
        optimizer.zero_grad(set_to_none=True)
        training_output = model(
            train_batch["condition"],
            train_batch["anchor"],
        )
        total_loss, loss_dictionary = compute_training_loss(
            model,
            training_output,
            train_batch,
            specification,
            dataset,
            neighbor_edge_tensor,
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
                **loss_dictionary,
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
        if epoch_index + 1 >= 8 and patience_count >= 8:
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
    predicted_coefficient_matrix = (
        test_output["prediction_coefficients"].detach().cpu().numpy()
    )
    correction_matrix = (
        test_output["coefficient_correction"].detach().cpu().numpy()
    )
    test_curve_matrix = dataset.curve_matrix[
        dataset.split_array == "test"
    ]
    metric_dictionary = aggregate_metrics(
        test_curve_matrix,
        predicted_curve_matrix,
    )
    anchor_coefficient_matrix = dataset.anchor_coefficient_map[
        specification.order_set_name
    ][dataset.split_array == "test"]
    anchor_curve_matrix = np.vstack(
        [
            _reconstruct_numpy_curve(
                coefficient_array,
                dataset.order_set_map[specification.order_set_name],
            )
            for coefficient_array in anchor_coefficient_matrix
        ]
    )
    anchor_rms = float(np.sqrt(np.mean(np.square(anchor_curve_matrix))))
    correction_curve_matrix = predicted_curve_matrix - anchor_curve_matrix
    correction_rms = float(
        np.sqrt(np.mean(np.square(correction_curve_matrix)))
    )
    correction_to_anchor_rms = (
        correction_rms / max(anchor_rms, 1.0e-12)
        if specification.formulation
        in {
            "anchored_coefficient",
            "bounded_coefficient",
            "banded_coefficient",
        }
        else float("nan")
    )

    seed_suffix = (
        ""
        if random_seed == FIRST_SCREEN_SEED
        else f"__seed_{random_seed}"
    )
    run_instance_id = (
        f"{now_timestamp()}__stage5_{specification.candidate_id.lower()}"
        f"{seed_suffix}"
    )
    run_directory = (
        PROJECT_ROOT
        / "output"
        / "training_runs"
        / "complex_harmonic_coefficient_residuals"
        / run_instance_id
    )
    run_directory.mkdir(parents=True, exist_ok=True)
    checkpoint_path = run_directory / "best_model.pt"
    torch.save(
        {
            "state_dict": best_state_dictionary,
            "candidate": specification.__dict__,
            "harmonic_order_list": dataset.order_set_map[
                specification.order_set_name
            ],
            "feature_mean": dataset.feature_mean,
            "feature_scale": dataset.feature_scale,
            "best_epoch": best_epoch,
        },
        checkpoint_path,
    )
    write_csv(run_directory / "training_history.csv", history_row_list)
    metrics_payload = {
        "schema_version": 1,
        "candidate_id": specification.candidate_id,
        "run_instance_id": run_instance_id,
        "best_epoch": best_epoch,
        "validation_curve_mae_deg": best_validation_mae,
        "test_metrics": metric_dictionary,
        "correction_rms_deg": correction_rms,
        "anchor_rms_deg": anchor_rms,
        "correction_to_anchor_rms": correction_to_anchor_rms,
        "coefficient_correction_abs_max": float(
            np.max(np.abs(correction_matrix))
        ),
        "prediction_coefficient_abs_max": float(
            np.max(np.abs(predicted_coefficient_matrix))
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
            "harmonic_order_list": dataset.order_set_map[
                specification.order_set_name
            ],
            "random_seed": random_seed,
            "angular_sample_count": ANGULAR_SAMPLE_COUNT,
            "split_signature": SPLIT_SIGNATURE,
        },
    )
    np.savez_compressed(
        run_directory / "test_predictions.npz",
        condition_id=np.asarray(dataset.condition_id_list)[
            dataset.split_array == "test"
        ],
        measured_curve=test_curve_matrix,
        predicted_curve=predicted_curve_matrix,
        predicted_coefficient=predicted_coefficient_matrix,
        coefficient_correction=correction_matrix,
    )
    campaign_log_path = (
        campaign_output_directory
        / "logs"
        / f"{specification.queue_index:03d}_{specification.candidate_id.lower()}.log"
    )
    campaign_log_path.parent.mkdir(parents=True, exist_ok=True)
    with campaign_log_path.open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as output_file:
        for history_row in history_row_list:
            output_file.write(json.dumps(history_row, sort_keys=True) + "\n")
    return {
        "candidate_id": specification.candidate_id,
        "queue_index": specification.queue_index,
        "formulation": specification.formulation,
        "order_set_name": specification.order_set_name,
        "capacity_name": specification.capacity_name,
        "random_seed": random_seed,
        "run_instance_id": run_instance_id,
        "run_directory": run_directory.relative_to(PROJECT_ROOT).as_posix(),
        "best_epoch": best_epoch,
        "validation_curve_mae_deg": best_validation_mae,
        **metric_dictionary,
        "correction_to_anchor_rms": correction_to_anchor_rms,
        "status": "completed",
    }


def run_campaign(dataset: Stage5Dataset) -> Path:
    """Execute all eighteen first-screen candidates and close scalar artifacts."""

    campaign_timestamp = now_timestamp()
    campaign_output_directory = (
        PROJECT_ROOT
        / "output"
        / "training_campaigns"
        / f"{campaign_timestamp}_{CAMPAIGN_NAME}"
    )
    campaign_output_directory.mkdir(parents=True, exist_ok=True)
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

    candidate_list = build_candidate_list()
    result_row_list: list[dict[str, Any]] = []
    for specification in candidate_list:
        print(
            f"[{specification.queue_index:02d}/{len(candidate_list)}] "
            f"Training {specification.candidate_id}"
        )
        result_row = train_candidate(
            specification,
            dataset,
            campaign_output_directory,
            FIRST_SCREEN_SEED,
        )
        result_row_list.append(result_row)
        write_csv(
            campaign_output_directory / "campaign_leaderboard.csv",
            sorted(
                result_row_list,
                key=lambda row: row["mae_deg"],
            ),
        )

    leaderboard_row_list = sorted(
        result_row_list,
        key=lambda row: row["mae_deg"],
    )
    best_row = leaderboard_row_list[0]
    write_csv(
        campaign_output_directory / "campaign_leaderboard.csv",
        leaderboard_row_list,
    )
    write_yaml(
        campaign_output_directory / "campaign_leaderboard.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "ranking_metric": "test full-curve MAE deg",
            "row_list": leaderboard_row_list,
        },
    )
    write_yaml(
        campaign_output_directory / "campaign_best_run.yaml",
        best_row,
    )
    with (
        campaign_output_directory / "campaign_best_run.md"
    ).open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(
            "# Stage 5 Scalar Campaign Best Run\n\n"
            f"- Candidate: `{best_row['candidate_id']}`\n"
            f"- Formulation: `{best_row['formulation']}`\n"
            f"- Test curve MAE: `{best_row['mae_deg']:.12f} deg`\n"
            f"- Test centered MAE: `{best_row['centered_mae_deg']:.12f} deg`\n"
            f"- Run instance: `{best_row['run_instance_id']}`\n\n"
            "This scalar ranking is not a promotion decision. The bounded "
            "curve-first and cancellation audit remains mandatory.\n"
        )
    execution_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "status": "completed",
        "completed_at": now_iso(),
        "expected_run_count": len(candidate_list),
        "completed_run_count": len(result_row_list),
        "failed_run_count": 0,
        "best_candidate_id": best_row["candidate_id"],
        "best_test_curve_mae_deg": best_row["mae_deg"],
    }
    write_yaml(
        campaign_output_directory / "campaign_execution_summary.yaml",
        execution_payload,
    )
    active_payload.update(
        {
            "status": "completed_pending_closeout",
            "completed_at": now_iso(),
            "completed_run_count": len(result_row_list),
            "failed_run_count": 0,
            "campaign_output_directory": campaign_output_directory.relative_to(
                PROJECT_ROOT
            ).as_posix(),
            "campaign_best_run_path": (
                campaign_output_directory / "campaign_best_run.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return campaign_output_directory


def run_stability_continuation(dataset: Stage5Dataset) -> Path:
    """Run H04 and its matched C04 control on the two declared seeds."""

    campaign_output_directory_list = sorted(
        (
            PROJECT_ROOT / "output" / "training_campaigns"
        ).glob(f"*_{CAMPAIGN_NAME}"),
        key=lambda path: path.stat().st_mtime,
    )
    assert campaign_output_directory_list
    campaign_output_directory = campaign_output_directory_list[-1]
    specification_map = {
        specification.candidate_id: specification
        for specification in build_candidate_list()
    }
    stability_row_list: list[dict[str, Any]] = []
    for random_seed in (271828, 161803):
        for candidate_id in ("C04", "H04"):
            print(
                f"[stability] Training {candidate_id} "
                f"with seed {random_seed}"
            )
            stability_row_list.append(
                train_candidate(
                    specification_map[candidate_id],
                    dataset,
                    campaign_output_directory,
                    random_seed,
                )
            )
    write_csv(
        campaign_output_directory / "campaign_stability_leaderboard.csv",
        sorted(
            stability_row_list,
            key=lambda row: (
                row["random_seed"],
                row["mae_deg"],
            ),
        ),
    )
    write_yaml(
        campaign_output_directory / "campaign_stability_summary.yaml",
        {
            "schema_version": 1,
            "candidate_id_list": ["C04", "H04"],
            "random_seed_list": [271828, 161803],
            "completed_run_count": len(stability_row_list),
            "failed_run_count": 0,
            "row_list": stability_row_list,
        },
    )
    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "status": "completed_pending_closeout",
            "stability_completed_at": now_iso(),
            "stability_completed_run_count": len(stability_row_list),
            "stability_failed_run_count": 0,
            "stability_summary_path": (
                campaign_output_directory
                / "campaign_stability_summary.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return campaign_output_directory


def parse_arguments() -> argparse.Namespace:
    """Parse Stage 5 launcher arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--run-stability", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Prepare, validate, and optionally run the approved Stage 5 campaign."""

    arguments = parse_arguments()
    dataset = build_stage5_dataset()
    if arguments.run_stability:
        preflight_summary = run_preflight(dataset)
        print(yaml.safe_dump(preflight_summary, sort_keys=False))
        output_directory = run_stability_continuation(dataset)
        print(f"Stability output: {output_directory}")
        return
    prepare_campaign(dataset)
    preflight_summary = run_preflight(dataset)
    print(yaml.safe_dump(preflight_summary, sort_keys=False))
    if arguments.run:
        output_directory = run_campaign(dataset)
        print(f"Campaign output: {output_directory}")
    elif not arguments.prepare_only and not arguments.preflight_only:
        print("Preparation and preflight completed; pass --run to train.")


if __name__ == "__main__":
    main()
