"""Prepare, validate, and run the Wave 5.2R Stage 7 campaign."""

from __future__ import annotations

# Import Python Utilities
import argparse
import copy
import csv
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
import random
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific And PyTorch Utilities
import numpy as np
import torch
import yaml

# Import Frozen Campaign And Model Utilities
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage6_spectral_sobolev_guidance as stage6,
)
from scripts.models.mean_centered_shape_multi_head_network import (
    MeanCenteredShapeMultiHeadNetwork,
)


# Define Frozen Stage Contract
STAGE_NAME = "wave52r_stage7_mean_centered_shape_multi_head"
CAMPAIGN_NAME = f"{STAGE_NAME}_2026_07_29"
SPLIT_SIGNATURE = stage5.SPLIT_SIGNATURE
ANGULAR_SAMPLE_COUNT = stage5.ANGULAR_SAMPLE_COUNT
CORE_ORDER_LIST = stage5.CORE_ORDER_LIST
FIRST_SCREEN_SEED = 314159
STABILITY_SEED_LIST = [271828, 161803]
DERIVATIVE_WINDOW_LENGTH = 5
MAX_EPOCH_COUNT = 64
PATIENCE_EPOCH_COUNT = 12
H04_CHECKPOINT_PATH = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "complex_harmonic_coefficient_residuals"
    / "2026-07-28-16-17-13__stage5_h04"
    / "best_model.pt"
)
H04_TEST_PREDICTION_PATH = H04_CHECKPOINT_PATH.parent / "test_predictions.npz"
CONFIG_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "mean_centered_shape_multi_head"
    / "campaigns"
    / "2026-07-29_wave52r_stage7_mean_centered_shape_multi_head"
)
QUEUE_DIRECTORY = CONFIG_DIRECTORY / "queue"
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage7_mean_centered_shape_multi_head"
)
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-29/"
    "2026-07-29-15-52-21_wave52r_stage7_mean_and_centered_shape_"
    "multi_head.md"
)
CAMPAIGN_PLAN_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "mean_centered_shape_multi_head/"
    "2026-07-29-15-52-21_wave52r_stage7_mean_centered_shape_"
    "multi_head_campaign_plan_report.md"
)
MODEL_REPORT_PATH = (
    "doc/reports/analysis/model_development_waves/wave_5_2/"
    "physics_guided_pinn_reassessment/[2026-07-29]/"
    "stage7_mean_centered_shape_multi_head/"
    "stage7_mean_centered_shape_multi_head_model_report.md"
)
LAUNCHER_PATH = (
    "scripts/campaigns/wave_5_2/"
    "run_wave52r_stage7_mean_centered_shape_multi_head.ps1"
)
LAUNCHER_NOTE_PATH = (
    "doc/scripts/campaigns/wave_5_2/"
    "run_wave52r_stage7_mean_centered_shape_multi_head.md"
)


@dataclass(frozen=True)
class CandidateSpecification:

    """Describe one immutable Stage 7 candidate."""

    queue_index: int
    candidate_id: str
    architecture: str
    training_mode: str
    shared_hidden_size_list: tuple[int, ...]
    branch_hidden_size_list: tuple[int, ...]
    learning_rate: float
    promotion_eligible: bool
    matched_control_id: str


def now_iso() -> str:

    """Return one timezone-aware local timestamp."""

    return datetime.now().astimezone().isoformat(timespec="seconds")


def now_timestamp() -> str:

    """Return one sortable local timestamp."""

    return datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")


def seed_everything(random_seed: int) -> None:

    """Seed Python, NumPy, and PyTorch deterministically."""

    random.seed(random_seed)
    np.random.seed(random_seed)
    torch.manual_seed(random_seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(random_seed)
    torch.use_deterministic_algorithms(True, warn_only=True)


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

    """Return the frozen seven-run first-screen matrix."""

    row_list = [
        (
            "C01",
            "monolithic",
            "joint",
            (64, 64, 32),
            (48,),
            2.0e-4,
            False,
            "",
        ),
        (
            "S01",
            "shared",
            "joint",
            (64, 64, 32),
            (48,),
            5.0e-4,
            True,
            "I01",
        ),
        (
            "P01",
            "partial",
            "joint",
            (64,),
            (48, 32),
            5.0e-4,
            True,
            "I01",
        ),
        (
            "I01",
            "independent",
            "joint",
            (64, 64, 32),
            (48,),
            5.0e-4,
            False,
            "",
        ),
        (
            "G01",
            "shared",
            "pcgrad",
            (64, 64, 32),
            (48,),
            5.0e-4,
            True,
            "I01",
        ),
        (
            "A01",
            "analytical_mean",
            "joint",
            (64, 64, 32),
            (48,),
            5.0e-4,
            False,
            "C01",
        ),
        (
            "A02",
            "analytical_shape",
            "joint",
            (64, 64, 32),
            (48,),
            5.0e-4,
            False,
            "C01",
        ),
    ]
    return [
        CandidateSpecification(
            queue_index=queue_index,
            candidate_id=candidate_id,
            architecture=architecture,
            training_mode=training_mode,
            shared_hidden_size_list=shared_hidden_size_list,
            branch_hidden_size_list=branch_hidden_size_list,
            learning_rate=learning_rate,
            promotion_eligible=promotion_eligible,
            matched_control_id=matched_control_id,
        )
        for queue_index, (
            candidate_id,
            architecture,
            training_mode,
            shared_hidden_size_list,
            branch_hidden_size_list,
            learning_rate,
            promotion_eligible,
            matched_control_id,
        ) in enumerate(row_list, start=1)
    ]


def build_model(
    specification: CandidateSpecification,
    dataset: stage5.Stage5Dataset,
) -> MeanCenteredShapeMultiHeadNetwork:

    """Construct one Stage 7 candidate."""

    model = MeanCenteredShapeMultiHeadNetwork(
        condition_input_size=3,
        harmonic_order_list=CORE_ORDER_LIST,
        angular_sample_count=ANGULAR_SAMPLE_COUNT,
        coefficient_correction_bound_list=(
            dataset.correction_bound_map["core"].tolist()
        ),
        architecture=specification.architecture,
        shared_hidden_size_list=list(
            specification.shared_hidden_size_list
        ),
        branch_hidden_size_list=list(
            specification.branch_hidden_size_list
        ),
    )
    if specification.candidate_id == "C01":
        checkpoint_payload = torch.load(
            H04_CHECKPOINT_PATH,
            map_location="cpu",
            weights_only=False,
        )
        checkpoint_state = checkpoint_payload["state_dict"]
        translated_state = {
            key.replace("condition_network.", "monolithic_network."): value
            for key, value in checkpoint_state.items()
            if key.startswith("condition_network.")
        }
        missing_key_list, unexpected_key_list = model.load_state_dict(
            translated_state,
            strict=False,
        )
        allowed_missing_key_set = {
            "coefficient_correction_bound",
            "shape_reconstruction_matrix",
        }
        assert set(missing_key_list) == allowed_missing_key_set
        assert unexpected_key_list == []
    return model


def parameter_count(model: torch.nn.Module) -> int:

    """Return the number of trainable parameters."""

    return int(
        sum(
            parameter.numel()
            for parameter in model.parameters()
            if parameter.requires_grad
        )
    )


def prepare_campaign(dataset: stage5.Stage5Dataset) -> None:

    """Write queue configurations and protected campaign state."""

    candidate_list = build_candidate_list()
    QUEUE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    queue_path_list: list[str] = []
    for specification in candidate_list:
        queue_path = (
            QUEUE_DIRECTORY
            / f"{specification.queue_index:03d}_"
            f"{specification.candidate_id.lower()}.yaml"
        )
        model = build_model(specification, dataset)
        payload = asdict(specification)
        payload["shared_hidden_size_list"] = list(
            specification.shared_hidden_size_list
        )
        payload["branch_hidden_size_list"] = list(
            specification.branch_hidden_size_list
        )
        payload.update(
            {
                "random_seed": FIRST_SCREEN_SEED,
                "parameter_count": parameter_count(model),
                "dataset": "polished_dataset",
                "input_mode": "setpoints",
                "surface": "Fw",
                "split_signature": SPLIT_SIGNATURE,
                "angular_sample_count": ANGULAR_SAMPLE_COUNT,
            }
        )
        write_yaml(queue_path, payload)
        queue_path_list.append(
            queue_path.relative_to(PROJECT_ROOT).as_posix()
        )

    manifest_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "stage": STAGE_NAME,
        "dataset": "polished_dataset",
        "input_mode": "setpoints",
        "surface": "Fw",
        "split_signature": SPLIT_SIGNATURE,
        "first_screen_seed": FIRST_SCREEN_SEED,
        "stability_seed_list": STABILITY_SEED_LIST,
        "expected_first_screen_run_count": len(candidate_list),
        "candidate_id_list": [
            specification.candidate_id
            for specification in candidate_list
        ],
        "queue_path_list": queue_path_list,
    }
    write_yaml(CONFIG_DIRECTORY / "campaign.yaml", manifest_payload)

    active_payload = {
        "status": "prepared",
        "prepared_at": now_iso(),
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": STAGE_NAME,
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
            CONFIG_DIRECTORY / "campaign.yaml"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "campaign_config_root": CONFIG_DIRECTORY.relative_to(
            PROJECT_ROOT
        ).as_posix(),
        "launcher_path": LAUNCHER_PATH,
        "launcher_note_path": LAUNCHER_NOTE_PATH,
        "planning_report_path": CAMPAIGN_PLAN_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "model_report_path": MODEL_REPORT_PATH,
        "local_preflight_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage7_mean_centered_shape_multi_head.ps1 "
            "-PreflightOnly"
        ),
        "local_launch_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage7_mean_centered_shape_multi_head.ps1 -Run"
        ),
        "remote_preflight_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage7_mean_centered_shape_multi_head.ps1 "
            "-Remote -PreflightOnly"
        ),
        "remote_launch_command": (
            ".\\scripts\\campaigns\\wave_5_2\\"
            "run_wave52r_stage7_mean_centered_shape_multi_head.ps1 "
            "-Remote -Run"
        ),
        "launch_command_list": [
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage7_mean_centered_shape_multi_head.ps1 "
                "-PreflightOnly"
            ),
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage7_mean_centered_shape_multi_head.ps1 "
                "-Run"
            ),
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage7_mean_centered_shape_multi_head.ps1 "
                "-Remote -PreflightOnly"
            ),
            (
                ".\\scripts\\campaigns\\wave_5_2\\"
                "run_wave52r_stage7_mean_centered_shape_multi_head.ps1 "
                "-Remote -Run"
            ),
        ],
        "approval": {
            "technical_document_status": "approved",
            "campaign_plan_status": "approved",
            "approval_source": "user blanket approval for twenty-four hours",
            "approval_recorded_at": "2026-07-29T15:30:41+02:00",
            "approval_expires_at": "2026-07-30T15:30:41+02:00",
        },
        "protected_file_list": [
            "doc/running/active_training_campaign.yaml",
            CONFIG_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
            LAUNCHER_PATH,
            (
                "scripts/campaigns/wave_5_2/"
                "run_wave52r_stage7_mean_centered_shape_multi_head.py"
            ),
            "scripts/models/mean_centered_shape_multi_head_network.py",
            ANALYSIS_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
        ],
    }
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)


def tensor_batch_for_split(
    dataset: stage5.Stage5Dataset,
    split_name: str,
    device: torch.device,
) -> dict[str, torch.Tensor]:

    """Build one complete mean/shape batch."""

    batch = stage5.tensor_dataset_for_split(
        dataset,
        "core",
        split_name,
        device,
    )
    target_mean_tensor = torch.mean(
        batch["curve"],
        dim=1,
        keepdim=True,
    )
    batch["mean"] = target_mean_tensor
    batch["shape"] = batch["curve"] - target_mean_tensor
    return batch


def compute_losses(
    output: dict[str, torch.Tensor],
    batch: dict[str, torch.Tensor],
    curve_scale: float,
    mean_scale: float,
    shape_scale: float,
) -> dict[str, torch.Tensor]:

    """Compute named normalized curve, mean, and shape losses."""

    curve_loss = torch.mean(
        torch.square(
            (output["prediction_curve"] - batch["curve"])
            / curve_scale
        )
    )
    mean_loss = torch.mean(
        torch.square(
            (output["prediction_mean"] - batch["mean"])
            / mean_scale
        )
    )
    shape_loss = torch.mean(
        torch.square(
            (
                output["prediction_centered_shape"]
                - batch["shape"]
            )
            / shape_scale
        )
    )
    return {
        "curve_loss": curve_loss,
        "mean_loss": mean_loss,
        "shape_loss": shape_loss,
        "total_loss": curve_loss + 0.5 * mean_loss + 0.5 * shape_loss,
    }


def flattened_gradient_cosine(
    first_gradient_list: tuple[torch.Tensor | None, ...],
    second_gradient_list: tuple[torch.Tensor | None, ...],
) -> tuple[float, float, float]:

    """Return cosine and norms for two parameter-gradient collections."""

    dot_product = torch.zeros((), dtype=torch.float32)
    first_norm_squared = torch.zeros((), dtype=torch.float32)
    second_norm_squared = torch.zeros((), dtype=torch.float32)
    for first_gradient, second_gradient in zip(
        first_gradient_list,
        second_gradient_list,
        strict=True,
    ):
        if first_gradient is None or second_gradient is None:
            continue
        dot_product = dot_product + torch.sum(
            first_gradient * second_gradient
        )
        first_norm_squared = first_norm_squared + torch.sum(
            torch.square(first_gradient)
        )
        second_norm_squared = second_norm_squared + torch.sum(
            torch.square(second_gradient)
        )
    first_norm = torch.sqrt(first_norm_squared)
    second_norm = torch.sqrt(second_norm_squared)
    denominator = first_norm * second_norm
    cosine = torch.where(
        denominator > 1.0e-12,
        dot_product / denominator,
        torch.zeros_like(dot_product),
    )
    return (
        float(cosine.detach().cpu()),
        float(first_norm.detach().cpu()),
        float(second_norm.detach().cpu()),
    )


def apply_pcgrad_step(
    model: MeanCenteredShapeMultiHeadNetwork,
    loss_map: dict[str, torch.Tensor],
    optimizer: torch.optim.Optimizer,
) -> tuple[float, bool]:

    """Backpropagate one projected shared-gradient update."""

    shared_parameter_list = model.shared_parameter_list()
    assert shared_parameter_list
    mean_gradient_list = torch.autograd.grad(
        loss_map["mean_loss"],
        shared_parameter_list,
        retain_graph=True,
        allow_unused=True,
    )
    shape_gradient_list = torch.autograd.grad(
        loss_map["shape_loss"],
        shared_parameter_list,
        retain_graph=True,
        allow_unused=True,
    )
    curve_gradient_list = torch.autograd.grad(
        loss_map["curve_loss"],
        shared_parameter_list,
        retain_graph=True,
        allow_unused=True,
    )
    cosine, _, _ = flattened_gradient_cosine(
        mean_gradient_list,
        shape_gradient_list,
    )
    conflict_detected = cosine < 0.0

    optimizer.zero_grad(set_to_none=True)
    loss_map["total_loss"].backward()
    for parameter, mean_gradient, shape_gradient, curve_gradient in zip(
        shared_parameter_list,
        mean_gradient_list,
        shape_gradient_list,
        curve_gradient_list,
        strict=True,
    ):
        zero_gradient = torch.zeros_like(parameter)
        resolved_mean_gradient = (
            zero_gradient if mean_gradient is None else mean_gradient
        )
        resolved_shape_gradient = (
            zero_gradient if shape_gradient is None else shape_gradient
        )
        resolved_curve_gradient = (
            zero_gradient if curve_gradient is None else curve_gradient
        )
        if conflict_detected:
            dot_product = torch.sum(
                resolved_mean_gradient * resolved_shape_gradient
            )
            mean_norm_squared = torch.sum(
                torch.square(resolved_mean_gradient)
            )
            shape_norm_squared = torch.sum(
                torch.square(resolved_shape_gradient)
            )
            projected_mean_gradient = (
                resolved_mean_gradient
                - dot_product
                / torch.clamp(shape_norm_squared, min=1.0e-12)
                * resolved_shape_gradient
            )
            projected_shape_gradient = (
                resolved_shape_gradient
                - dot_product
                / torch.clamp(mean_norm_squared, min=1.0e-12)
                * resolved_mean_gradient
            )
        else:
            projected_mean_gradient = resolved_mean_gradient
            projected_shape_gradient = resolved_shape_gradient
        parameter.grad = (
            resolved_curve_gradient
            + 0.5 * projected_mean_gradient
            + 0.5 * projected_shape_gradient
        )
    optimizer.step()
    return cosine, conflict_detected


def joint_step(
    model: MeanCenteredShapeMultiHeadNetwork,
    loss_map: dict[str, torch.Tensor],
    optimizer: torch.optim.Optimizer,
) -> tuple[float, bool]:

    """Backpropagate one joint update while recording shared conflict."""

    shared_parameter_list = model.shared_parameter_list()
    cosine = 0.0
    if shared_parameter_list:
        mean_gradient_list = torch.autograd.grad(
            loss_map["mean_loss"],
            shared_parameter_list,
            retain_graph=True,
            allow_unused=True,
        )
        shape_gradient_list = torch.autograd.grad(
            loss_map["shape_loss"],
            shared_parameter_list,
            retain_graph=True,
            allow_unused=True,
        )
        cosine, _, _ = flattened_gradient_cosine(
            mean_gradient_list,
            shape_gradient_list,
        )
    optimizer.zero_grad(set_to_none=True)
    loss_map["total_loss"].backward()
    optimizer.step()
    return cosine, cosine < 0.0


def evaluate_metrics(
    measured_curve_matrix: np.ndarray,
    predicted_curve_matrix: np.ndarray,
) -> dict[str, float]:

    """Evaluate full-curve and explicit decomposition metrics."""

    metric_payload = stage6.aggregate_stage6_metrics(
        measured_curve_matrix,
        predicted_curve_matrix,
        DERIVATIVE_WINDOW_LENGTH,
    )
    measured_mean_array = np.mean(
        measured_curve_matrix,
        axis=1,
        keepdims=True,
    )
    predicted_mean_array = np.mean(
        predicted_curve_matrix,
        axis=1,
        keepdims=True,
    )
    measured_shape_matrix = measured_curve_matrix - measured_mean_array
    predicted_shape_matrix = predicted_curve_matrix - predicted_mean_array
    metric_payload.update(
        {
            "mean_mae_deg": float(
                np.mean(np.abs(measured_mean_array - predicted_mean_array))
            ),
            "centered_shape_mae_deg": float(
                np.mean(
                    np.abs(
                        measured_shape_matrix - predicted_shape_matrix
                    )
                )
            ),
        }
    )
    return metric_payload


def train_candidate(
    specification: CandidateSpecification,
    dataset: stage5.Stage5Dataset,
    campaign_output_directory: Path,
    random_seed: int,
    run_suffix: str = "",
) -> dict[str, Any]:

    """Train one candidate and persist its immutable run."""

    seed_everything(random_seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = build_model(specification, dataset).to(device)
    train_batch = tensor_batch_for_split(dataset, "train", device)
    validation_batch = tensor_batch_for_split(
        dataset,
        "validation",
        device,
    )
    test_batch = tensor_batch_for_split(dataset, "test", device)
    training_mask = dataset.split_array == "train"
    mean_scale = max(
        float(
            np.std(
                np.mean(
                    dataset.curve_matrix[training_mask],
                    axis=1,
                )
            )
        ),
        1.0e-5,
    )
    shape_scale = max(
        float(
            np.std(
                dataset.curve_matrix[training_mask]
                - np.mean(
                    dataset.curve_matrix[training_mask],
                    axis=1,
                    keepdims=True,
                )
            )
        ),
        1.0e-5,
    )
    curve_scale = max(float(dataset.curve_scale), 1.0e-5)
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=specification.learning_rate,
    )

    best_validation_loss = float("inf")
    best_epoch = 0
    best_state_dictionary: dict[str, torch.Tensor] | None = None
    patience_counter = 0
    history_row_list: list[dict[str, Any]] = []
    negative_conflict_count = 0
    for epoch_index in range(1, MAX_EPOCH_COUNT + 1):
        model.train()
        train_output = model(
            train_batch["condition"],
            train_batch["anchor"],
        )
        train_loss_map = compute_losses(
            train_output,
            train_batch,
            curve_scale,
            mean_scale,
            shape_scale,
        )
        if specification.training_mode == "pcgrad":
            gradient_cosine, conflict_detected = apply_pcgrad_step(
                model,
                train_loss_map,
                optimizer,
            )
        else:
            gradient_cosine, conflict_detected = joint_step(
                model,
                train_loss_map,
                optimizer,
            )
        negative_conflict_count += int(conflict_detected)

        model.eval()
        with torch.no_grad():
            validation_output = model(
                validation_batch["condition"],
                validation_batch["anchor"],
            )
            validation_loss_map = compute_losses(
                validation_output,
                validation_batch,
                curve_scale,
                mean_scale,
                shape_scale,
            )
        validation_loss = float(
            validation_loss_map["total_loss"].detach().cpu()
        )
        history_row_list.append(
            {
                "epoch": epoch_index,
                "train_total_loss": float(
                    train_loss_map["total_loss"].detach().cpu()
                ),
                "train_curve_loss": float(
                    train_loss_map["curve_loss"].detach().cpu()
                ),
                "train_mean_loss": float(
                    train_loss_map["mean_loss"].detach().cpu()
                ),
                "train_shape_loss": float(
                    train_loss_map["shape_loss"].detach().cpu()
                ),
                "validation_total_loss": validation_loss,
                "mean_shape_gradient_cosine": gradient_cosine,
                "negative_gradient_conflict": conflict_detected,
            }
        )
        if validation_loss < best_validation_loss - 1.0e-8:
            best_validation_loss = validation_loss
            best_epoch = epoch_index
            best_state_dictionary = {
                key: value.detach().cpu().clone()
                for key, value in model.state_dict().items()
            }
            patience_counter = 0
        else:
            patience_counter += 1
        if patience_counter >= PATIENCE_EPOCH_COUNT:
            break
    assert best_state_dictionary is not None
    model.load_state_dict(best_state_dictionary)
    model.eval()
    with torch.no_grad():
        test_output = model(
            test_batch["condition"],
            test_batch["anchor"],
        )

    test_prediction_matrix = (
        test_output["prediction_curve"].detach().cpu().numpy()
    )
    test_measured_matrix = test_batch["curve"].detach().cpu().numpy()
    metric_payload = evaluate_metrics(
        test_measured_matrix,
        test_prediction_matrix,
    )
    shape_cycle_mean_max_abs = float(
        torch.amax(
            torch.abs(test_output["shape_cycle_mean"])
        ).detach().cpu()
    )
    reconstruction_identity_max_abs = float(
        test_output["reconstruction_identity_error"].detach().cpu()
    )
    run_instance_id = (
        f"{now_timestamp()}__stage7_"
        f"{specification.candidate_id.lower()}{run_suffix}"
    )
    run_directory = (
        PROJECT_ROOT
        / "output"
        / "training_runs"
        / "mean_centered_shape_multi_head"
        / run_instance_id
    )
    run_directory.mkdir(parents=True, exist_ok=False)
    checkpoint_path = run_directory / "best_model.pt"
    torch.save(
        {
            "state_dict": best_state_dictionary,
            "candidate": asdict(specification),
            "random_seed": random_seed,
            "best_epoch": best_epoch,
            "feature_mean": dataset.feature_mean,
            "feature_scale": dataset.feature_scale,
        },
        checkpoint_path,
    )
    split_mask = dataset.split_array == "test"
    np.savez_compressed(
        run_directory / "test_predictions.npz",
        condition_id=np.asarray(dataset.condition_id_list)[split_mask],
        measured_curve=test_measured_matrix,
        predicted_curve=test_prediction_matrix,
        predicted_mean=(
            test_output["prediction_mean"].detach().cpu().numpy()
        ),
        predicted_centered_shape=(
            test_output["prediction_centered_shape"]
            .detach()
            .cpu()
            .numpy()
        ),
        analytical_curve=(
            test_batch["anchor"].detach().cpu().numpy()
            @ torch.cat(
                [
                    torch.ones(
                        (1, ANGULAR_SAMPLE_COUNT),
                        dtype=torch.float32,
                        device=device,
                    ),
                    model.shape_reconstruction_matrix,
                ],
                dim=0,
            ).detach().cpu().numpy()
        ),
    )
    training_config_payload = asdict(specification)
    training_config_payload.update(
        {
            "random_seed": random_seed,
            "run_instance_id": run_instance_id,
            "parameter_count": parameter_count(model),
            "best_epoch": best_epoch,
            "curve_scale": curve_scale,
            "mean_scale": mean_scale,
            "shape_scale": shape_scale,
            "split_signature": SPLIT_SIGNATURE,
        }
    )
    write_yaml(run_directory / "training_config.yaml", training_config_payload)
    write_csv(run_directory / "training_history.csv", history_row_list)
    result_payload: dict[str, Any] = {
        "candidate_id": specification.candidate_id,
        "architecture": specification.architecture,
        "training_mode": specification.training_mode,
        "promotion_eligible": specification.promotion_eligible,
        "matched_control_id": specification.matched_control_id,
        "random_seed": random_seed,
        "run_instance_id": run_instance_id,
        "parameter_count": parameter_count(model),
        "best_epoch": best_epoch,
        "negative_gradient_conflict_epoch_count": (
            negative_conflict_count
        ),
        "negative_gradient_conflict_fraction": (
            negative_conflict_count / len(history_row_list)
        ),
        "shape_cycle_mean_max_abs_deg": shape_cycle_mean_max_abs,
        "reconstruction_identity_max_abs_deg": (
            reconstruction_identity_max_abs
        ),
        "checkpoint_path": checkpoint_path.relative_to(
            PROJECT_ROOT
        ).as_posix(),
    }
    result_payload.update(metric_payload)
    write_yaml(run_directory / "metrics_summary.yaml", result_payload)
    return result_payload


def load_h04_baseline_metrics() -> dict[str, float]:

    """Evaluate the frozen H04 prediction on the Stage 7 surface."""

    with np.load(H04_TEST_PREDICTION_PATH) as payload:
        measured_curve_matrix = payload["measured_curve"]
        predicted_curve_matrix = payload["predicted_curve"]
    return evaluate_metrics(measured_curve_matrix, predicted_curve_matrix)


def normalized_composite_score(
    metric_row: dict[str, Any],
    baseline_metrics: dict[str, float],
) -> float:

    """Return the declared raw, mean, and shape composite."""

    return float(
        (
            metric_row["mae_deg"] / baseline_metrics["mae_deg"]
            + metric_row["mean_mae_deg"]
            / baseline_metrics["mean_mae_deg"]
            + metric_row["centered_shape_mae_deg"]
            / baseline_metrics["centered_shape_mae_deg"]
        )
        / 3.0
    )


def build_first_screen_gate_summary(
    leaderboard_row_list: list[dict[str, Any]],
    baseline_metrics: dict[str, float],
) -> dict[str, Any]:

    """Evaluate every explicit Stage 7 first-screen gate."""

    candidate_map = {
        row["candidate_id"]: row for row in leaderboard_row_list
    }
    independent_row = candidate_map["I01"]
    independent_score = normalized_composite_score(
        independent_row,
        baseline_metrics,
    )
    gate_row_list: list[dict[str, Any]] = []
    for candidate_id in ["S01", "P01", "G01"]:
        candidate_row = candidate_map[candidate_id]
        candidate_score = normalized_composite_score(
            candidate_row,
            baseline_metrics,
        )
        parameter_ratio = (
            candidate_row["parameter_count"]
            / independent_row["parameter_count"]
        )
        shared_advantage = (
            candidate_score < independent_score
            or (
                candidate_score <= 1.005 * independent_score
                and parameter_ratio <= 0.80
            )
        )
        gate_row = {
            "candidate_id": candidate_id,
            "all_first_screen_gates_passed": False,
            "normalized_composite_score": candidate_score,
            "independent_composite_score": independent_score,
            "parameter_ratio_vs_independent": parameter_ratio,
            "raw_mae_preserved": (
                candidate_row["mae_deg"]
                <= 1.01 * baseline_metrics["mae_deg"]
            ),
            "mean_mae_improved": (
                candidate_row["mean_mae_deg"]
                <= 0.995 * baseline_metrics["mean_mae_deg"]
            ),
            "centered_shape_improved": (
                candidate_row["centered_shape_mae_deg"]
                <= 0.995
                * baseline_metrics["centered_shape_mae_deg"]
            ),
            "derivative_preserved": (
                candidate_row["sobolev_derivative_mae"]
                <= 1.01 * baseline_metrics["sobolev_derivative_mae"]
            ),
            "closure_preserved": (
                candidate_row["periodic_closure_error_deg"]
                <= 1.01
                * baseline_metrics["periodic_closure_error_deg"]
            ),
            "amplitude_preserved": (
                candidate_row["retained_amplitude_mae_deg"]
                <= 1.01
                * baseline_metrics["retained_amplitude_mae_deg"]
            ),
            "phase_preserved": (
                candidate_row["retained_phase_mae_rad"]
                <= 1.01
                * baseline_metrics["retained_phase_mae_rad"]
            ),
            "p95_preserved": (
                candidate_row["per_curve_mae_p95"]
                <= baseline_metrics["per_curve_mae_p95"]
            ),
            "shared_advantage_passed": shared_advantage,
            "shape_invariant_passed": (
                candidate_row["shape_cycle_mean_max_abs_deg"] <= 1.0e-7
            ),
            "reconstruction_invariant_passed": (
                candidate_row["reconstruction_identity_max_abs_deg"]
                <= 1.0e-7
            ),
            "gradient_conflict_reported": (
                "negative_gradient_conflict_fraction"
                in candidate_row
            ),
        }
        gate_row["all_first_screen_gates_passed"] = all(
            bool(value)
            for key, value in gate_row.items()
            if key != "all_first_screen_gates_passed"
            and (
                key.endswith("_passed")
                or key.endswith("_preserved")
                or key.endswith("_improved")
                or key == "gradient_conflict_reported"
            )
        )
        gate_row_list.append(gate_row)
    passing_candidate_id_list = [
        row["candidate_id"]
        for row in gate_row_list
        if row["all_first_screen_gates_passed"]
    ]
    recommended_candidate_id = None
    if passing_candidate_id_list:
        recommended_candidate_id = min(
            passing_candidate_id_list,
            key=lambda candidate_id: normalized_composite_score(
                candidate_map[candidate_id],
                baseline_metrics,
            ),
        )
    return {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "baseline": "stage5_h04_seed_314159",
        "baseline_metrics": baseline_metrics,
        "passing_candidate_id_list": passing_candidate_id_list,
        "recommended_candidate_id": recommended_candidate_id,
        "gate_row_list": gate_row_list,
    }


def run_preflight(dataset: stage5.Stage5Dataset) -> dict[str, Any]:

    """Validate data, model, component, and gradient contracts."""

    assert dataset.curve_matrix.shape == (966, ANGULAR_SAMPLE_COUNT)
    assert int(np.sum(dataset.split_array == "train")) == 675
    assert int(np.sum(dataset.split_array == "validation")) == 194
    assert int(np.sum(dataset.split_array == "test")) == 97
    assert H04_CHECKPOINT_PATH.is_file()
    device = torch.device("cpu")
    training_batch = tensor_batch_for_split(dataset, "train", device)
    sample_index = torch.arange(8)
    check_row_list: list[dict[str, Any]] = []
    parameter_count_map: dict[str, int] = {}
    for specification in build_candidate_list():
        model = build_model(specification, dataset)
        output = model(
            training_batch["condition"][sample_index],
            training_batch["anchor"][sample_index],
        )
        loss_map = compute_losses(
            output,
            {
                key: value[sample_index]
                for key, value in training_batch.items()
            },
            max(float(dataset.curve_scale), 1.0e-5),
            1.0e-3,
            1.0e-2,
        )
        loss_map["total_loss"].backward()
        gradient_finite = all(
            parameter.grad is None
            or bool(torch.isfinite(parameter.grad).all())
            for parameter in model.parameters()
        )
        parameter_count_map[specification.candidate_id] = parameter_count(
            model
        )
        check_row_list.append(
            {
                "candidate_id": specification.candidate_id,
                "output_shape_passed": tuple(
                    output["prediction_curve"].shape
                )
                == (8, ANGULAR_SAMPLE_COUNT),
                "shape_mean_max_abs_deg": float(
                    torch.amax(
                        torch.abs(output["shape_cycle_mean"])
                    ).detach()
                ),
                "reconstruction_identity_max_abs_deg": float(
                    output["reconstruction_identity_error"].detach()
                ),
                "finite_gradient_passed": gradient_finite,
                "parameter_count": parameter_count(model),
            }
        )
    assert all(
        row["output_shape_passed"]
        and row["shape_mean_max_abs_deg"] <= 1.0e-7
        and row["reconstruction_identity_max_abs_deg"] <= 1.0e-7
        and row["finite_gradient_passed"]
        for row in check_row_list
    )
    summary_payload = {
        "schema_version": 1,
        "stage_name": STAGE_NAME,
        "validated_at": now_iso(),
        "candidate_count": len(check_row_list),
        "accepted_curve_count": 966,
        "train_curve_count": 675,
        "validation_curve_count": 194,
        "test_curve_count": 97,
        "split_signature": SPLIT_SIGNATURE,
        "parameter_count_map": parameter_count_map,
        "shared_parameter_ratio_vs_independent": (
            parameter_count_map["S01"] / parameter_count_map["I01"]
        ),
        "partial_parameter_ratio_vs_independent": (
            parameter_count_map["P01"] / parameter_count_map["I01"]
        ),
        "runtime_target_input_count": 0,
        "all_checks_passed": True,
        "check_row_list": check_row_list,
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage7_preflight_validation_summary.yaml",
        summary_payload,
    )
    return summary_payload


def run_campaign(dataset: stage5.Stage5Dataset) -> Path:

    """Execute the first screen and conditional stability continuation."""

    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    campaign_output_directory = (
        PROJECT_ROOT
        / "output"
        / "training_campaigns"
        / f"{now_timestamp()}_{CAMPAIGN_NAME}"
    )
    campaign_output_directory.mkdir(parents=True, exist_ok=False)
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

    result_row_list: list[dict[str, Any]] = []
    failed_run_count = 0
    log_directory = campaign_output_directory / "logs"
    log_directory.mkdir(parents=True, exist_ok=True)
    for specification in build_candidate_list():
        try:
            result_row = train_candidate(
                specification,
                dataset,
                campaign_output_directory,
                FIRST_SCREEN_SEED,
            )
            result_row_list.append(result_row)
            log_text = (
                f"candidate_id={specification.candidate_id}\n"
                f"status=completed\n"
                f"test_mae_deg={result_row['mae_deg']:.12f}\n"
                f"mean_mae_deg={result_row['mean_mae_deg']:.12f}\n"
                f"centered_shape_mae_deg="
                f"{result_row['centered_shape_mae_deg']:.12f}\n"
            )
        except Exception as error:
            failed_run_count += 1
            log_text = (
                f"candidate_id={specification.candidate_id}\n"
                f"status=failed\nerror={error!r}\n"
            )
        log_path = (
            log_directory
            / f"{specification.queue_index:03d}_"
            f"{specification.candidate_id.lower()}.log"
        )
        log_path.write_text(log_text, encoding="utf-8", newline="\n")
    assert failed_run_count == 0
    assert len(result_row_list) == len(build_candidate_list())
    result_row_list.sort(key=lambda row: float(row["mae_deg"]))
    write_csv(
        campaign_output_directory / "campaign_leaderboard.csv",
        result_row_list,
    )
    write_yaml(
        campaign_output_directory / "campaign_leaderboard.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "completed_at": now_iso(),
            "row_list": result_row_list,
        },
    )
    baseline_metrics = load_h04_baseline_metrics()
    gate_payload = build_first_screen_gate_summary(
        result_row_list,
        baseline_metrics,
    )
    write_yaml(
        campaign_output_directory
        / "campaign_first_screen_gate_summary.yaml",
        gate_payload,
    )

    stability_row_list: list[dict[str, Any]] = []
    recommended_candidate_id = gate_payload[
        "recommended_candidate_id"
    ]
    if recommended_candidate_id is not None:
        specification_map = {
            specification.candidate_id: specification
            for specification in build_candidate_list()
        }
        for random_seed in STABILITY_SEED_LIST:
            for candidate_id in [recommended_candidate_id, "I01"]:
                stability_row_list.append(
                    train_candidate(
                        specification_map[candidate_id],
                        dataset,
                        campaign_output_directory,
                        random_seed,
                        run_suffix=f"_stability_seed_{random_seed}",
                    )
                )
        write_csv(
            campaign_output_directory
            / "campaign_stability_leaderboard.csv",
            stability_row_list,
        )
        write_yaml(
            campaign_output_directory
            / "campaign_stability_leaderboard.yaml",
            {
                "schema_version": 1,
                "recommended_candidate_id": recommended_candidate_id,
                "row_list": stability_row_list,
            },
        )

    raw_best_row = result_row_list[0]
    best_run_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "selection_basis": "first_screen_test_raw_mae",
        "candidate_id": raw_best_row["candidate_id"],
        "run_instance_id": raw_best_row["run_instance_id"],
        "test_mae_deg": raw_best_row["mae_deg"],
        "checkpoint_path": raw_best_row["checkpoint_path"],
        "multi_index_recommended_candidate_id": (
            recommended_candidate_id
        ),
        "stability_run_count": len(stability_row_list),
    }
    write_yaml(
        campaign_output_directory / "campaign_best_run.yaml",
        best_run_payload,
    )
    (
        campaign_output_directory / "campaign_best_run.md"
    ).write_text(
        "# Campaign Best Run\n\n"
        f"- raw-error leader: `{raw_best_row['candidate_id']}`;\n"
        f"- test MAE: `{raw_best_row['mae_deg']:.9f} deg`;\n"
        "- multi-index recommendation: "
        f"`{recommended_candidate_id}`.\n",
        encoding="utf-8",
        newline="\n",
    )
    execution_payload = {
        "schema_version": 1,
        "status": "completed",
        "completed_at": now_iso(),
        "expected_run_count": len(build_candidate_list()),
        "completed_run_count": len(result_row_list),
        "failed_run_count": failed_run_count,
        "stability_completed_run_count": len(stability_row_list),
        "raw_error_leader_id": raw_best_row["candidate_id"],
        "multi_index_recommended_candidate_id": (
            recommended_candidate_id
        ),
    }
    write_yaml(
        campaign_output_directory / "campaign_execution_summary.yaml",
        execution_payload,
    )
    active_payload.update(
        {
            "status": "completed",
            "completed_at": now_iso(),
            "completed_run_count": len(result_row_list),
            "failed_run_count": failed_run_count,
            "stability_completed_run_count": len(stability_row_list),
            "campaign_best_run_path": (
                campaign_output_directory / "campaign_best_run.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
            "raw_error_leader_id": raw_best_row["candidate_id"],
            "multi_index_recommended_candidate_id": (
                recommended_candidate_id
            ),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return campaign_output_directory


def parse_arguments() -> argparse.Namespace:

    """Parse the Stage 7 command line."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--run", action="store_true")
    return parser.parse_args()


def main() -> None:

    """Prepare, preflight, and optionally execute Stage 7."""

    arguments = parse_arguments()
    dataset = stage5.build_stage5_dataset()
    prepare_campaign(dataset)
    summary_payload = run_preflight(dataset)
    assert summary_payload["all_checks_passed"]
    print(
        "[DONE] Stage 7 preflight passed for "
        f"{summary_payload['candidate_count']} candidates."
    )
    if arguments.run:
        output_directory = run_campaign(dataset)
        print(
            "[DONE] Stage 7 campaign completed | "
            f"{output_directory.relative_to(PROJECT_ROOT).as_posix()}"
        )
    elif arguments.preflight_only:
        print("[DONE] Stage 7 preflight-only mode completed.")


if __name__ == "__main__":
    main()
