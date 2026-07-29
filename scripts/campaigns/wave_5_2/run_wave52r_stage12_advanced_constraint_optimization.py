"""Run Wave 5.2R Stage 12 advanced constraint optimization."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from dataclasses import asdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
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

# Import Prior Stage Contracts
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage9_temporal_analytical_residual_models as stage9,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage11_uncertainty_trust_calibration as stage11,
)

# Import Optimization Utilities
from scripts.training.advanced_constraint_optimization import (
    AdaptiveCurveWeightState,
)
from scripts.training.advanced_constraint_optimization import (
    AugmentedLagrangianState,
)
from scripts.training.advanced_constraint_optimization import (
    build_loss_component_dictionary,
)
from scripts.training.physics_guided_optimization_instrumentation import (
    LossActivationSchedule,
)
from scripts.training.physics_guided_optimization_instrumentation import (
    LossComponentConfiguration,
)
from scripts.training.physics_guided_optimization_instrumentation import (
    PhysicsGuidedOptimizationInstrumentation,
)
from scripts.training.physics_guided_optimization_instrumentation import (
    assign_flat_gradient_to_parameters,
)


# Define Campaign Constants
PROJECT_ROOT = Path(__file__).resolve().parents[3]
STAGE_NAME = "wave52r_stage12_advanced_constraint_optimization"
CAMPAIGN_NAME = f"{STAGE_NAME}_2026_07_29"
FIRST_SCREEN_SEED = 314159
STABILITY_SEED_LIST = [271828, 161803]
MAXIMUM_EPOCH_COUNT = 36
MINIMUM_EPOCH_COUNT = 12
EARLY_STOPPING_PATIENCE = 7
CURVE_BATCH_SIZE = 16
LEARNING_RATE = 5.0e-4
CORRECTION_BUDGET = 0.004
SPLIT_SIGNATURE = stage9.SPLIT_SIGNATURE
FROZEN_K01_CHECKPOINT_PATH = stage11.PRIMARY_K01_CHECKPOINT_PATH
CONFIG_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "advanced_constraint_optimization"
    / "campaigns"
    / "2026-07-29_wave52r_stage12_advanced_constraint_optimization"
)
QUEUE_DIRECTORY = CONFIG_DIRECTORY / "queue"
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage12_advanced_constraint_optimization"
)
RUN_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "advanced_constraint_optimization"
)
CAMPAIGN_ROOT_DIRECTORY = PROJECT_ROOT / "output" / "training_campaigns"
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-29/"
    "2026-07-29-21-38-21_wave52r_stage12_advanced_constraint_optimization.md"
)
CAMPAIGN_PLAN_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "advanced_constraint_optimization/"
    "2026-07-29-21-38-21_wave52r_stage12_advanced_constraint_"
    "optimization_campaign_plan_report.md"
)
LAUNCHER_PATH = (
    "scripts/campaigns/wave_5_2/"
    "run_wave52r_stage12_advanced_constraint_optimization.ps1"
)
LAUNCHER_NOTE_PATH = (
    "doc/scripts/campaigns/wave_5_2/"
    "run_wave52r_stage12_advanced_constraint_optimization.md"
)


@dataclass(frozen=True)
class CandidateSpecification:
    """Describe one immutable Stage 12 candidate."""

    queue_index: int
    candidate_id: str
    optimization_profile: str
    diagnostic_only: bool = False


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
    field_name_list: list[str] = []
    for row in row_list:
        for field_name in row:
            if field_name not in field_name_list:
                field_name_list.append(field_name)
    with path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)


def build_candidate_list() -> list[CandidateSpecification]:
    """Return the approved ten-entry matrix."""

    return [
        CandidateSpecification(1, "C00", "frozen_k01_replay", True),
        CandidateSpecification(2, "C01", "standard_adamw"),
        CandidateSpecification(3, "G01", "gradient_statistics"),
        CandidateSpecification(4, "R01", "relobralo_style"),
        CandidateSpecification(5, "P01", "main_loss_preserving_projection"),
        CandidateSpecification(6, "S01", "self_adaptive_curve_weighting"),
        CandidateSpecification(7, "A01", "augmented_lagrangian"),
        CandidateSpecification(8, "U01", "curriculum_regularization"),
        CandidateSpecification(9, "F01", "failure_informed_resampling"),
        CandidateSpecification(10, "L01", "adamw_lbfgs_refinement"),
    ]


def find_k01_specification() -> stage9.CandidateSpecification:
    """Resolve the frozen Stage 9 K01 architecture contract."""

    return next(
        specification
        for specification in stage9.build_candidate_list()
        if specification.candidate_id == "K01"
    )


def build_instrumentation(
    profile_name: str,
    random_seed: int,
) -> PhysicsGuidedOptimizationInstrumentation:
    """Build the declared five-component optimizer instrumentation."""

    curriculum = profile_name == "curriculum_regularization"
    delayed_schedule = LossActivationSchedule(
        start_step=150 if curriculum else 0,
        full_weight_step=500 if curriculum else 0,
    )
    return PhysicsGuidedOptimizationInstrumentation(
        [
            LossComponentConfiguration(
                "raw",
                "deg",
                normalization_scale=1.0,
                fixed_weight=1.0,
                role="main",
            ),
            LossComponentConfiguration(
                "mean",
                "deg",
                normalization_scale=1.0,
                fixed_weight=0.50,
            ),
            LossComponentConfiguration(
                "shape",
                "deg",
                normalization_scale=1.0,
                fixed_weight=0.25,
            ),
            LossComponentConfiguration(
                "closure",
                "deg",
                normalization_scale=1.0,
                fixed_weight=0.05,
                activation_schedule=delayed_schedule,
            ),
            LossComponentConfiguration(
                "correction",
                "deg",
                normalization_scale=1.0,
                fixed_weight=1.0e-4,
                activation_schedule=delayed_schedule,
            ),
        ],
        random_seed=random_seed,
    )


def prepare_campaign(dataset: stage9.stage5.Stage5Dataset) -> None:
    """Prepare queue configuration and persistent campaign state."""

    QUEUE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    queue_path_list: list[str] = []
    for specification in build_candidate_list():
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
                "candidate": asdict(specification),
                "dataset": {
                    "dataset_id": "polished_dataset",
                    "input_mode": "setpoints",
                    "surface": "fw",
                    "curve_count": int(dataset.curve_matrix.shape[0]),
                    "split_signature": SPLIT_SIGNATURE,
                },
                "training": {
                    "first_screen_seed": FIRST_SCREEN_SEED,
                    "conditional_stability_seed_list": STABILITY_SEED_LIST,
                    "maximum_epoch_count": MAXIMUM_EPOCH_COUNT,
                    "curve_batch_size": CURVE_BATCH_SIZE,
                    "chunk_length": stage9.DEFAULT_CHUNK_LENGTH,
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
            "stage": "wave_5_2r_stage12",
            "candidate_count": len(build_candidate_list()),
            "expected_first_screen_run_count": len(build_candidate_list()),
            "queue_path_list": queue_path_list,
            "conditional_stability_seed_list": STABILITY_SEED_LIST,
            "technical_document_path": TECHNICAL_DOCUMENT_PATH,
            "campaign_plan_path": CAMPAIGN_PLAN_PATH,
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
            "expected_run_count": len(build_candidate_list()),
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
                    "run_wave52r_stage12_advanced_constraint_optimization.py"
                ),
                (
                    "scripts/training/"
                    "advanced_constraint_optimization.py"
                ),
                ANALYSIS_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
            ],
        },
    )


def run_preflight(
    dataset: stage9.stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
) -> dict[str, Any]:
    """Validate split, replay, losses, gradients, and adaptive states."""

    assert dataset.curve_matrix.shape == (966, stage9.ANGULAR_SAMPLE_COUNT)
    assert int(np.sum(dataset.split_array == "train")) == 675
    assert int(np.sum(dataset.split_array == "validation")) == 194
    assert int(np.sum(dataset.split_array == "test")) == 97
    assert FROZEN_K01_CHECKPOINT_PATH.is_file()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    specification = find_k01_specification()
    model = stage9.build_model(specification, dataset).to(device)
    train_batch = stage9.build_split_tensors(
        dataset,
        anchor_bundle.h04_curve_matrix,
        anchor_bundle.h04_coefficient_matrix,
        "train",
        device,
    )
    batch_index = torch.arange(2, device=device)
    output = model.forward_in_chunks(
        torch.as_tensor(train_batch["angle"]).index_select(0, batch_index),
        torch.as_tensor(train_batch["condition"]).index_select(0, batch_index),
        torch.as_tensor(train_batch["anchor"]).index_select(0, batch_index),
        torch.as_tensor(train_batch["anchor_coefficient"]).index_select(
            0,
            batch_index,
        ),
        chunk_length=stage9.DEFAULT_CHUNK_LENGTH,
        detach_hidden_between_chunks=True,
    )
    component_dictionary, per_curve_loss = (
        build_loss_component_dictionary(
            output["prediction_curve"],
            torch.as_tensor(train_batch["target"]).index_select(
                0,
                batch_index,
            ),
            output["residual_curve"],
            output["coefficient_correction"],
        )
    )
    instrumentation = build_instrumentation("gradient_statistics", 314159)
    normalized_dictionary = instrumentation.normalize_loss_dictionary(
        component_dictionary
    )
    gradient_dictionary = (
        instrumentation.compute_component_gradient_dictionary(
            normalized_dictionary,
            list(model.parameters()),
        )
    )
    gradient_norm_dictionary = (
        instrumentation.compute_gradient_norm_dictionary(
            gradient_dictionary
        )
    )
    assert all(np.isfinite(value) for value in gradient_norm_dictionary.values())
    adaptive_state = AdaptiveCurveWeightState(675)
    adaptive_state.update(batch_index.cpu(), per_curve_loss)
    generator = torch.Generator().manual_seed(314159)
    sampled_index = adaptive_state.deterministic_sample_indices(675, generator)
    repeated_index = AdaptiveCurveWeightState(
        675
    ).deterministic_sample_indices(
        675,
        torch.Generator().manual_seed(314159),
    )
    assert torch.equal(sampled_index, repeated_index)
    lagrangian_state = AugmentedLagrangianState()
    lagrangian_loss = lagrangian_state.compose_loss(
        torch.relu(component_dictionary["closure"] - 0.002),
        torch.relu(component_dictionary["correction"] - CORRECTION_BUDGET),
    )
    assert bool(torch.isfinite(lagrangian_loss))

    checkpoint_payload = torch.load(
        FROZEN_K01_CHECKPOINT_PATH,
        map_location=device,
        weights_only=False,
    )
    model.load_state_dict(checkpoint_payload["state_dict"])
    test_batch = stage9.build_split_tensors(
        dataset,
        anchor_bundle.h04_curve_matrix,
        anchor_bundle.h04_coefficient_matrix,
        "test",
        device,
    )
    test_mask = dataset.split_array == "test"
    shuffled_index_array = np.random.default_rng(
        FIRST_SCREEN_SEED + 901
    ).permutation(stage9.ANGULAR_SAMPLE_COUNT)
    replay_metrics, _, _ = stage9.evaluate_trained_candidate(
        model,
        test_batch,
        dataset.curve_matrix[test_mask],
        shuffled_index_array,
    )
    summary_payload = {
        "status": "pass",
        "checked_at": now_iso(),
        "split_signature": SPLIT_SIGNATURE,
        "curve_count": 966,
        "train_curve_count": 675,
        "validation_curve_count": 194,
        "test_curve_count": 97,
        "candidate_count": len(build_candidate_list()),
        "frozen_k01_checkpoint_path": (
            FROZEN_K01_CHECKPOINT_PATH.relative_to(PROJECT_ROOT).as_posix()
        ),
        "frozen_k01_mae_deg": replay_metrics["mae_deg"],
        "finite_gradient_component_count": len(gradient_norm_dictionary),
        "deterministic_weighted_sampling_passed": True,
        "runtime_target_derived_input_count": 0,
        "device": str(device),
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage12_preflight_validation_summary.yaml",
        summary_payload,
    )
    return summary_payload


def load_split_batch(
    batch: dict[str, torch.Tensor | None],
    index_tensor: torch.Tensor,
) -> tuple[torch.Tensor, ...]:
    """Select one complete K01 batch."""

    coefficient_source = batch["anchor_coefficient"]
    assert isinstance(coefficient_source, torch.Tensor)
    return (
        torch.as_tensor(batch["condition"]).index_select(0, index_tensor),
        torch.as_tensor(batch["target"]).index_select(0, index_tensor),
        torch.as_tensor(batch["anchor"]).index_select(0, index_tensor),
        torch.as_tensor(batch["angle"]).index_select(0, index_tensor),
        coefficient_source.index_select(0, index_tensor),
    )


def standard_validation_score(
    model: torch.nn.Module,
    validation_batch: dict[str, torch.Tensor | None],
) -> tuple[float, float]:
    """Evaluate the unchanged Stage 9 checkpoint-selection score."""

    model.eval()
    with torch.no_grad():
        output = model.forward_in_chunks(
            torch.as_tensor(validation_batch["angle"]),
            torch.as_tensor(validation_batch["condition"]),
            torch.as_tensor(validation_batch["anchor"]),
            torch.as_tensor(validation_batch["anchor_coefficient"]),
            chunk_length=stage9.DEFAULT_CHUNK_LENGTH,
        )
        score, component_payload = stage9.curve_first_loss(
            output["prediction_curve"],
            torch.as_tensor(validation_batch["target"]),
            output["residual_curve"],
        )
    return float(score.cpu()), component_payload["raw_loss_deg"]


def run_lbfgs_refinement(
    model: torch.nn.Module,
    training_batch: dict[str, torch.Tensor | None],
) -> int:
    """Apply a bounded deterministic single-device L-BFGS refinement."""

    device = next(model.parameters()).device
    subset_index = torch.arange(0, 64, device=device)
    condition, target, anchor, angle, coefficient = load_split_batch(
        training_batch,
        subset_index,
    )
    optimizer = torch.optim.LBFGS(
        model.parameters(),
        lr=0.20,
        max_iter=5,
        max_eval=7,
        history_size=10,
        line_search_fn="strong_wolfe",
    )
    evaluation_count = 0

    def closure() -> torch.Tensor:
        nonlocal evaluation_count
        evaluation_count += 1
        model.train()
        optimizer.zero_grad(set_to_none=True)
        output = model.forward_in_chunks(
            angle,
            condition,
            anchor,
            coefficient,
            chunk_length=stage9.DEFAULT_CHUNK_LENGTH,
            detach_hidden_between_chunks=True,
        )
        loss, _ = stage9.curve_first_loss(
            output["prediction_curve"],
            target,
            output["residual_curve"],
        )
        loss.backward()
        return loss

    optimizer.step(closure)
    return evaluation_count


def train_candidate(
    specification: CandidateSpecification,
    dataset: stage9.stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
    random_seed: int,
) -> dict[str, Any]:
    """Train one Stage 12 optimizer profile and persist immutable artifacts."""

    stage9.seed_everything(random_seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = stage9.build_model(find_k01_specification(), dataset).to(device)
    training_batch = stage9.build_split_tensors(
        dataset,
        anchor_bundle.h04_curve_matrix,
        anchor_bundle.h04_coefficient_matrix,
        "train",
        device,
    )
    validation_batch = stage9.build_split_tensors(
        dataset,
        anchor_bundle.h04_curve_matrix,
        anchor_bundle.h04_coefficient_matrix,
        "validation",
        device,
    )
    test_batch = stage9.build_split_tensors(
        dataset,
        anchor_bundle.h04_curve_matrix,
        anchor_bundle.h04_coefficient_matrix,
        "test",
        device,
    )
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=LEARNING_RATE,
        weight_decay=1.0e-5,
    )
    instrumentation = build_instrumentation(
        specification.optimization_profile,
        random_seed,
    )
    adaptive_state = AdaptiveCurveWeightState(675)
    lagrangian_state = AugmentedLagrangianState()
    random_generator = torch.Generator().manual_seed(random_seed + 1200)
    parameter_list = list(model.parameters())
    best_validation_score = float("inf")
    best_validation_mae = float("inf")
    best_epoch = 0
    best_state_dictionary: dict[str, torch.Tensor] | None = None
    patience_count = 0
    optimization_step = 0
    history_row_list: list[dict[str, Any]] = []
    gradient_record_list: list[dict[str, Any]] = []

    for epoch_index in range(MAXIMUM_EPOCH_COUNT):
        model.train()
        if specification.optimization_profile == "failure_informed_resampling":
            epoch_index_cpu = adaptive_state.deterministic_sample_indices(
                675,
                random_generator,
            )
            epoch_index_tensor = epoch_index_cpu.to(device)
        else:
            epoch_index_tensor = torch.randperm(
                675,
                generator=random_generator,
            ).to(device)
        epoch_loss_list: list[float] = []

        for batch_start in range(0, 675, CURVE_BATCH_SIZE):
            batch_index = epoch_index_tensor[
                batch_start : batch_start + CURVE_BATCH_SIZE
            ]
            condition, target, anchor, angle, coefficient = load_split_batch(
                training_batch,
                batch_index,
            )
            curve_weights = (
                adaptive_state.batch_weights(batch_index, device)
                if specification.optimization_profile
                == "self_adaptive_curve_weighting"
                else None
            )
            optimizer.zero_grad(set_to_none=True)
            output = model.forward_in_chunks(
                angle,
                condition,
                anchor,
                coefficient,
                chunk_length=stage9.DEFAULT_CHUNK_LENGTH,
                detach_hidden_between_chunks=True,
            )
            component_dictionary, per_curve_loss = (
                build_loss_component_dictionary(
                    output["prediction_curve"],
                    target,
                    output["residual_curve"],
                    output["coefficient_correction"],
                    curve_weights,
                )
            )
            normalized_dictionary = (
                instrumentation.normalize_loss_dictionary(
                    component_dictionary
                )
            )
            needs_component_gradients = (
                specification.optimization_profile
                in {
                    "gradient_statistics",
                    "main_loss_preserving_projection",
                }
                or optimization_step % 100 == 0
            )
            if needs_component_gradients:
                gradient_dictionary = (
                    instrumentation.compute_component_gradient_dictionary(
                        normalized_dictionary,
                        parameter_list,
                    )
                )
                gradient_norm_dictionary = (
                    instrumentation.compute_gradient_norm_dictionary(
                        gradient_dictionary
                    )
                )
            else:
                gradient_dictionary = {}
                gradient_norm_dictionary = {
                    component_name: 1.0
                    for component_name in normalized_dictionary
                }
            adapter_name = {
                "gradient_statistics": "gradient_statistics",
                "relobralo_style": "relobralo_style",
                "main_loss_preserving_projection": "conflict_aware",
            }.get(specification.optimization_profile, "fixed")
            weight_dictionary = instrumentation.resolve_weight_dictionary(
                adapter_name,
                normalized_dictionary,
                gradient_norm_dictionary,
                optimization_step,
            )

            if (
                specification.optimization_profile
                == "main_loss_preserving_projection"
            ):
                assert gradient_dictionary
                combined_gradient, projection_record = (
                    instrumentation.compose_main_loss_preserving_gradient(
                        gradient_dictionary,
                        weight_dictionary,
                    )
                )
                assign_flat_gradient_to_parameters(
                    combined_gradient,
                    parameter_list,
                )
            else:
                total_loss = instrumentation.compose_weighted_loss(
                    normalized_dictionary,
                    weight_dictionary,
                )
                projection_record = {}
                if (
                    specification.optimization_profile
                    == "augmented_lagrangian"
                ):
                    closure_violation = torch.relu(
                        component_dictionary["closure"] - 0.002
                    )
                    correction_violation = torch.relu(
                        component_dictionary["correction"]
                        - CORRECTION_BUDGET
                    )
                    total_loss = total_loss + lagrangian_state.compose_loss(
                        closure_violation,
                        correction_violation,
                    )
                total_loss.backward()

            torch.nn.utils.clip_grad_norm_(parameter_list, 5.0)
            optimizer.step()
            if specification.optimization_profile in {
                "self_adaptive_curve_weighting",
                "failure_informed_resampling",
            }:
                adaptive_state.update(batch_index, per_curve_loss)
            if (
                specification.optimization_profile == "augmented_lagrangian"
                and optimization_step > 0
                and optimization_step % 50 == 0
            ):
                lagrangian_state.update(
                    float(
                        torch.relu(
                            component_dictionary["closure"] - 0.002
                        )
                        .detach()
                        .cpu()
                    ),
                    float(
                        torch.relu(
                            component_dictionary["correction"]
                            - CORRECTION_BUDGET
                        )
                        .detach()
                        .cpu()
                    ),
                )
            epoch_loss_list.append(
                float(component_dictionary["raw"].detach().cpu())
            )
            if optimization_step % 100 == 0:
                gradient_record_list.append(
                    {
                        "optimization_step": optimization_step,
                        "raw_gradient_norm": gradient_norm_dictionary["raw"],
                        "mean_gradient_norm": gradient_norm_dictionary["mean"],
                        "shape_gradient_norm": gradient_norm_dictionary["shape"],
                        "closure_gradient_norm": (
                            gradient_norm_dictionary["closure"]
                        ),
                        "correction_gradient_norm": (
                            gradient_norm_dictionary["correction"]
                        ),
                        "projection_count": sum(
                            bool(item["projection_applied"])
                            for item in projection_record.values()
                        ),
                    }
                )
            optimization_step += 1

        validation_score, validation_mae = standard_validation_score(
            model,
            validation_batch,
        )
        history_row_list.append(
            {
                "epoch": epoch_index + 1,
                "training_raw_mae_deg": float(np.mean(epoch_loss_list)),
                "validation_score": validation_score,
                "validation_curve_mae_deg": validation_mae,
                "adaptive_effective_sample_size": (
                    adaptive_state.effective_sample_size()
                ),
                **lagrangian_state.to_payload(),
            }
        )
        if validation_score < best_validation_score - 1.0e-9:
            best_validation_score = validation_score
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
    lbfgs_evaluation_count = 0
    if specification.optimization_profile == "adamw_lbfgs_refinement":
        pre_refinement_state = {
            name: value.detach().cpu().clone()
            for name, value in model.state_dict().items()
        }
        pre_refinement_score, _ = standard_validation_score(
            model,
            validation_batch,
        )
        lbfgs_evaluation_count = run_lbfgs_refinement(model, training_batch)
        post_refinement_score, post_refinement_mae = (
            standard_validation_score(model, validation_batch)
        )
        if post_refinement_score <= pre_refinement_score:
            best_validation_score = post_refinement_score
            best_validation_mae = post_refinement_mae
            best_state_dictionary = {
                name: value.detach().cpu().clone()
                for name, value in model.state_dict().items()
            }
        else:
            model.load_state_dict(pre_refinement_state)
    else:
        model.load_state_dict(best_state_dictionary)

    test_mask = dataset.split_array == "test"
    shuffled_index_array = np.random.default_rng(
        FIRST_SCREEN_SEED + 901
    ).permutation(stage9.ANGULAR_SAMPLE_COUNT)
    metrics, predicted_curve_matrix, residual_curve_matrix = (
        stage9.evaluate_trained_candidate(
            model,
            test_batch,
            dataset.curve_matrix[test_mask],
            shuffled_index_array,
        )
    )
    seed_suffix = (
        "" if random_seed == FIRST_SCREEN_SEED else f"__seed_{random_seed}"
    )
    run_instance_id = (
        f"{now_timestamp()}__stage12_"
        f"{specification.candidate_id.lower()}{seed_suffix}"
    )
    run_directory = RUN_ROOT_DIRECTORY / run_instance_id
    run_directory.mkdir(parents=True, exist_ok=False)
    checkpoint_path = run_directory / "best_model.pt"
    torch.save(
        {
            "state_dict": best_state_dictionary,
            "candidate": asdict(specification),
            "split_signature": SPLIT_SIGNATURE,
            "feature_mean": dataset.feature_mean,
            "feature_scale": dataset.feature_scale,
        },
        checkpoint_path,
    )
    write_csv(run_directory / "training_history.csv", history_row_list)
    write_csv(
        run_directory / "gradient_diagnostics.csv",
        gradient_record_list
        or [
            {
                "optimization_step": 0,
                "raw_gradient_norm": 0.0,
                "mean_gradient_norm": 0.0,
                "shape_gradient_norm": 0.0,
                "closure_gradient_norm": 0.0,
                "correction_gradient_norm": 0.0,
                "projection_count": 0,
            }
        ],
    )
    np.savez_compressed(
        run_directory / "test_predictions.npz",
        measured_curve=dataset.curve_matrix[test_mask],
        predicted_curve=predicted_curve_matrix,
        anchor_curve=anchor_bundle.h04_curve_matrix[test_mask],
        residual_curve=residual_curve_matrix,
    )
    optimizer_state_payload = {
        "optimization_profile": specification.optimization_profile,
        "optimization_step_count": optimization_step,
        "lbfgs_evaluation_count": lbfgs_evaluation_count,
        "adaptive_curve_state": adaptive_state.to_payload(),
        "augmented_lagrangian_state": lagrangian_state.to_payload(),
    }
    write_yaml(
        run_directory / "optimizer_state_summary.yaml",
        optimizer_state_payload,
    )
    result_payload = {
        "candidate_id": specification.candidate_id,
        "optimization_profile": specification.optimization_profile,
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
        "adaptive_effective_sample_size": (
            adaptive_state.effective_sample_size()
        ),
        "lbfgs_evaluation_count": lbfgs_evaluation_count,
        **metrics,
    }
    write_yaml(run_directory / "metrics_summary.yaml", result_payload)
    return result_payload


def frozen_k01_result(
    dataset: stage9.stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
) -> dict[str, Any]:
    """Replay the frozen Stage 9 K01 checkpoint as C00."""

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = stage9.build_model(find_k01_specification(), dataset).to(device)
    checkpoint_payload = torch.load(
        FROZEN_K01_CHECKPOINT_PATH,
        map_location=device,
        weights_only=False,
    )
    model.load_state_dict(checkpoint_payload["state_dict"])
    test_batch = stage9.build_split_tensors(
        dataset,
        anchor_bundle.h04_curve_matrix,
        anchor_bundle.h04_coefficient_matrix,
        "test",
        device,
    )
    test_mask = dataset.split_array == "test"
    metrics, prediction_matrix, residual_matrix = (
        stage9.evaluate_trained_candidate(
            model,
            test_batch,
            dataset.curve_matrix[test_mask],
            np.random.default_rng(
                FIRST_SCREEN_SEED + 901
            ).permutation(stage9.ANGULAR_SAMPLE_COUNT),
        )
    )
    ANALYSIS_DIRECTORY.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        ANALYSIS_DIRECTORY / "stage12_frozen_k01_replay.npz",
        measured_curve=dataset.curve_matrix[test_mask],
        predicted_curve=prediction_matrix,
        anchor_curve=anchor_bundle.h04_curve_matrix[test_mask],
        residual_curve=residual_matrix,
    )
    return {
        "candidate_id": "C00",
        "optimization_profile": "frozen_k01_replay",
        "random_seed": FIRST_SCREEN_SEED,
        "run_instance_id": "frozen_stage9_k01",
        "best_epoch": 0,
        "best_validation_score": float("nan"),
        "best_validation_mae_deg": float("nan"),
        "checkpoint_path": (
            FROZEN_K01_CHECKPOINT_PATH.relative_to(PROJECT_ROOT).as_posix()
        ),
        "parameter_count": sum(
            parameter.numel() for parameter in model.parameters()
        ),
        "runtime_target_derived_input_count": 0,
        "adaptive_effective_sample_size": 675.0,
        "lbfgs_evaluation_count": 0,
        **metrics,
    }


def candidate_gate_row(
    candidate: dict[str, Any],
    frozen_control: dict[str, Any],
    trained_control: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate the complete predeclared Stage 12 first-screen gate."""

    raw_improved = (
        candidate["mae_deg"] <= 0.99 * trained_control["mae_deg"]
    )
    shape_improved = (
        candidate["centered_shape_mae_deg"]
        <= 0.99 * trained_control["centered_shape_mae_deg"]
    )
    raw_preserved = (
        candidate["mae_deg"] <= 1.005 * trained_control["mae_deg"]
    )
    shape_preserved = (
        candidate["centered_shape_mae_deg"]
        <= 1.005 * trained_control["centered_shape_mae_deg"]
    )
    gate_row = {
        "candidate_id": candidate["candidate_id"],
        "accuracy_improved": (
            (raw_improved and shape_preserved)
            or (shape_improved and raw_preserved)
        ),
        "mean_preserved": (
            candidate["mean_mae_deg"]
            <= 1.01 * trained_control["mean_mae_deg"]
        ),
        "p95_preserved": (
            candidate["per_curve_mae_p95"]
            <= 1.01 * trained_control["per_curve_mae_p95"]
        ),
        "closure_improved": (
            candidate["periodic_closure_error_deg"]
            <= 0.90 * trained_control["periodic_closure_error_deg"]
        ),
        "reset_reproducible": (
            candidate["reset_reproducibility_max_abs_deg"] <= 1.0e-8
        ),
        "chunk_equivalent": (
            candidate["chunk_equivalence_max_abs_deg"] <= 1.0e-6
        ),
        "bounded_correction": (
            candidate["residual_abs_max_deg"]
            <= 1.01 * max(
                trained_control["residual_abs_max_deg"],
                frozen_control["residual_abs_max_deg"],
            )
        ),
        "beats_frozen_k01": (
            candidate["mae_deg"] < frozen_control["mae_deg"]
            and candidate["centered_shape_mae_deg"]
            <= 1.005 * frozen_control["centered_shape_mae_deg"]
        ),
        "runtime_contract_passed": (
            candidate["runtime_target_derived_input_count"] == 0
        ),
        "deployment_cost_preserved": (
            candidate["parameter_count"] == trained_control["parameter_count"]
        ),
    }
    gate_row["all_first_screen_gates_passed"] = all(
        value
        for key, value in gate_row.items()
        if key not in {"candidate_id", "all_first_screen_gates_passed"}
    )
    return gate_row


def run_campaign(
    dataset: stage9.stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
) -> Path:
    """Execute first screen and conditional stability."""

    prepare_campaign(dataset)
    run_preflight(dataset, anchor_bundle)
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
            "campaign_output_directory": (
                campaign_output_directory.relative_to(PROJECT_ROOT).as_posix()
            ),
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)

    result_row_list = [frozen_k01_result(dataset, anchor_bundle)]
    failure_count = 0
    for specification in build_candidate_list()[1:]:
        try:
            result_row_list.append(
                train_candidate(
                    specification,
                    dataset,
                    anchor_bundle,
                    FIRST_SCREEN_SEED,
                )
            )
        except Exception as error:
            failure_count += 1
            write_yaml(
                campaign_output_directory
                / f"{specification.candidate_id.lower()}_failure.yaml",
                {
                    "candidate_id": specification.candidate_id,
                    "error_type": type(error).__name__,
                    "error_message": str(error),
                },
            )

    row_map = {row["candidate_id"]: row for row in result_row_list}
    gate_row_list = [
        candidate_gate_row(row, row_map["C00"], row_map["C01"])
        for row in result_row_list
        if row["candidate_id"] not in {"C00", "C01"}
    ]
    passing_candidate_id_list = [
        row["candidate_id"]
        for row in gate_row_list
        if row["all_first_screen_gates_passed"]
    ]
    recommended_candidate_id = (
        min(
            passing_candidate_id_list,
            key=lambda candidate_id: row_map[candidate_id]["mae_deg"],
        )
        if passing_candidate_id_list
        else None
    )

    stability_row_list: list[dict[str, Any]] = []
    if recommended_candidate_id is not None:
        specification = next(
            item
            for item in build_candidate_list()
            if item.candidate_id == recommended_candidate_id
        )
        for stability_seed in STABILITY_SEED_LIST:
            stability_row_list.append(
                train_candidate(
                    specification,
                    dataset,
                    anchor_bundle,
                    stability_seed,
                )
            )

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
    gate_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "gate_row_list": gate_row_list,
        "passing_candidate_id_list": passing_candidate_id_list,
        "recommended_candidate_id": recommended_candidate_id,
        "conditional_stability_executed": bool(stability_row_list),
        "stability_row_list": stability_row_list,
    }
    write_yaml(
        campaign_output_directory / "campaign_first_screen_gate_summary.yaml",
        gate_payload,
    )
    best_row = leaderboard_row_list[0]
    qualified_winner = (
        row_map[recommended_candidate_id]
        if recommended_candidate_id is not None
        else None
    )
    best_payload = {
        "campaign_name": CAMPAIGN_NAME,
        "raw_error_leader_id": best_row["candidate_id"],
        "raw_error_leader_mae_deg": best_row["mae_deg"],
        "qualified_winner_id": recommended_candidate_id,
        "qualified_winner": qualified_winner,
    }
    write_yaml(
        campaign_output_directory / "campaign_best_run.yaml",
        best_payload,
    )
    with (
        campaign_output_directory / "campaign_best_run.md"
    ).open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(
            "# Stage 12 Campaign Best Run\n\n"
            f"- Raw-error leader: `{best_row['candidate_id']}`.\n"
            f"- Qualified winner: `{recommended_candidate_id}`.\n"
            f"- Conditional stability executed: "
            f"`{bool(stability_row_list)}`.\n"
        )
    write_yaml(
        campaign_output_directory / "campaign_execution_summary.yaml",
        {
            "campaign_name": CAMPAIGN_NAME,
            "status": "completed" if failure_count == 0 else "completed_with_failures",
            "completed_first_screen_count": len(result_row_list),
            "failed_first_screen_count": failure_count,
            "conditional_stability_run_count": len(stability_row_list),
            "completed_at": now_iso(),
        },
    )
    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "status": "completed" if failure_count == 0 else "completed_with_failures",
            "completed_at": now_iso(),
            "completed_run_count": len(result_row_list),
            "failed_run_count": failure_count,
            "campaign_best_run_path": (
                campaign_output_directory
                / "campaign_best_run.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
            "qualified_winner_id": recommended_candidate_id,
            "raw_error_leader_id": best_row["candidate_id"],
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return campaign_output_directory


def resume_failed_campaign(
    dataset: stage9.stage5.Stage5Dataset,
    anchor_bundle: stage9.AnchorBundle,
) -> Path:
    """Recover failed first-screen entries in the latest Stage 12 campaign."""

    candidate_directory_list = sorted(
        [
            path
            for path in CAMPAIGN_ROOT_DIRECTORY.iterdir()
            if path.is_dir() and CAMPAIGN_NAME in path.name
        ],
        key=lambda path: path.stat().st_mtime,
    )
    assert candidate_directory_list, "No Stage 12 campaign output was found"
    campaign_output_directory = candidate_directory_list[-1]
    leaderboard_payload = load_yaml(
        campaign_output_directory / "campaign_leaderboard.yaml"
    )
    result_row_list = list(leaderboard_payload["row_list"])
    completed_id_set = {
        row["candidate_id"] for row in result_row_list
    }
    missing_specification_list = [
        specification
        for specification in build_candidate_list()
        if specification.candidate_id not in completed_id_set
    ]
    assert missing_specification_list, (
        "The latest Stage 12 campaign has no failed entries to recover"
    )
    recovered_id_list: list[str] = []
    recovery_failure_list: list[dict[str, str]] = []
    for specification in missing_specification_list:
        try:
            result_row_list.append(
                train_candidate(
                    specification,
                    dataset,
                    anchor_bundle,
                    FIRST_SCREEN_SEED,
                )
            )
            recovered_id_list.append(specification.candidate_id)
        except Exception as error:
            recovery_failure_list.append(
                {
                    "candidate_id": specification.candidate_id,
                    "error_type": type(error).__name__,
                    "error_message": str(error),
                }
            )

    row_map = {row["candidate_id"]: row for row in result_row_list}
    assert "C00" in row_map and "C01" in row_map
    gate_row_list = [
        candidate_gate_row(row, row_map["C00"], row_map["C01"])
        for row in result_row_list
        if row["candidate_id"] not in {"C00", "C01"}
    ]
    passing_candidate_id_list = [
        row["candidate_id"]
        for row in gate_row_list
        if row["all_first_screen_gates_passed"]
    ]
    recommended_candidate_id = (
        min(
            passing_candidate_id_list,
            key=lambda candidate_id: row_map[candidate_id]["mae_deg"],
        )
        if passing_candidate_id_list
        else None
    )
    stability_row_list: list[dict[str, Any]] = []
    if recommended_candidate_id is not None:
        specification = next(
            item
            for item in build_candidate_list()
            if item.candidate_id == recommended_candidate_id
        )
        for stability_seed in STABILITY_SEED_LIST:
            stability_row_list.append(
                train_candidate(
                    specification,
                    dataset,
                    anchor_bundle,
                    stability_seed,
                )
            )

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
    write_yaml(
        campaign_output_directory / "campaign_first_screen_gate_summary.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "gate_row_list": gate_row_list,
            "passing_candidate_id_list": passing_candidate_id_list,
            "recommended_candidate_id": recommended_candidate_id,
            "conditional_stability_executed": bool(stability_row_list),
            "stability_row_list": stability_row_list,
        },
    )
    best_row = leaderboard_row_list[0]
    write_yaml(
        campaign_output_directory / "campaign_best_run.yaml",
        {
            "campaign_name": CAMPAIGN_NAME,
            "raw_error_leader_id": best_row["candidate_id"],
            "raw_error_leader_mae_deg": best_row["mae_deg"],
            "qualified_winner_id": recommended_candidate_id,
            "qualified_winner": (
                row_map[recommended_candidate_id]
                if recommended_candidate_id is not None
                else None
            ),
        },
    )
    with (
        campaign_output_directory / "campaign_best_run.md"
    ).open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(
            "# Stage 12 Campaign Best Run\n\n"
            f"- Raw-error leader: `{best_row['candidate_id']}`.\n"
            f"- Qualified winner: `{recommended_candidate_id}`.\n"
            f"- Conditional stability executed: "
            f"`{bool(stability_row_list)}`.\n"
        )
    completed_count = len(result_row_list)
    remaining_failure_count = len(recovery_failure_list)
    write_yaml(
        campaign_output_directory / "campaign_execution_summary.yaml",
        {
            "campaign_name": CAMPAIGN_NAME,
            "status": (
                "completed"
                if remaining_failure_count == 0
                else "completed_with_failures"
            ),
            "completed_first_screen_count": completed_count,
            "failed_first_screen_count": remaining_failure_count,
            "initial_failure_count": len(missing_specification_list),
            "recovered_candidate_id_list": recovered_id_list,
            "recovery_failure_list": recovery_failure_list,
            "conditional_stability_run_count": len(stability_row_list),
            "completed_at": now_iso(),
        },
    )
    active_payload = load_yaml(ACTIVE_CAMPAIGN_PATH)
    active_payload.update(
        {
            "status": (
                "completed"
                if remaining_failure_count == 0
                else "completed_with_failures"
            ),
            "completed_at": now_iso(),
            "completed_run_count": completed_count,
            "failed_run_count": remaining_failure_count,
            "campaign_output_directory": (
                campaign_output_directory.relative_to(
                    PROJECT_ROOT
                ).as_posix()
            ),
            "campaign_best_run_path": (
                campaign_output_directory
                / "campaign_best_run.yaml"
            ).relative_to(PROJECT_ROOT).as_posix(),
            "qualified_winner_id": recommended_candidate_id,
            "raw_error_leader_id": best_row["candidate_id"],
            "recovered_candidate_id_list": recovered_id_list,
        }
    )
    write_yaml(ACTIVE_CAMPAIGN_PATH, active_payload)
    return campaign_output_directory


def parse_arguments() -> argparse.Namespace:
    """Parse Stage 12 campaign commands."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--resume-failed", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Prepare, validate, or run Stage 12."""

    arguments = parse_arguments()
    dataset = stage9.stage5.build_stage5_dataset()
    anchor_bundle = stage9.build_anchor_bundle(dataset)
    if arguments.prepare:
        prepare_campaign(dataset)
    if arguments.preflight_only:
        prepare_campaign(dataset)
        print(
            yaml.safe_dump(
                run_preflight(dataset, anchor_bundle),
                sort_keys=False,
            )
        )
    if arguments.run:
        print(run_campaign(dataset, anchor_bundle))
    if arguments.resume_failed:
        print(resume_failed_campaign(dataset, anchor_bundle))
    if not any(
        [
            arguments.prepare,
            arguments.preflight_only,
            arguments.run,
            arguments.resume_failed,
        ]
    ):
        prepare_campaign(dataset)


if __name__ == "__main__":
    main()
