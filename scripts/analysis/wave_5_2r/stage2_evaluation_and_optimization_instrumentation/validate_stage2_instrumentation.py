"""Validate Wave 5.2R Stage 2 loss and gradient instrumentation."""

from __future__ import annotations

# Import Python Utilities
import csv
import json
import os
import sys
from pathlib import Path
from typing import Any

# Import PyTorch Utilities
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset

# Import YAML Utilities
import yaml

PROJECT_PATH = Path(os.path.abspath(__file__)).parents[4]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.training.physics_guided_optimization_instrumentation import (  # noqa: E402
    LossActivationSchedule,
)
from scripts.training.physics_guided_optimization_instrumentation import (  # noqa: E402
    LossComponentConfiguration,
)
from scripts.training.physics_guided_optimization_instrumentation import (  # noqa: E402
    ParameterFreezeSchedule,
)
from scripts.training.physics_guided_optimization_instrumentation import (  # noqa: E402
    PhysicsGuidedOptimizationInstrumentation,
)
from scripts.training.physics_guided_optimization_instrumentation import (  # noqa: E402
    assign_flat_gradient_to_parameters,
)
from scripts.training.physics_guided_optimization_instrumentation import (  # noqa: E402
    build_deterministic_dataloader,
)
from scripts.training.physics_guided_optimization_instrumentation import (  # noqa: E402
    capture_trainable_parameter_vector,
)
from scripts.training.physics_guided_optimization_instrumentation import (  # noqa: E402
    compute_dataloader_fingerprint,
)
from scripts.training.physics_guided_optimization_instrumentation import (  # noqa: E402
    compute_update_to_parameter_ratio,
)
from scripts.training.physics_guided_optimization_instrumentation import (  # noqa: E402
    configure_deterministic_execution,
)

OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage2_evaluation_and_optimization_instrumentation"
)
CONTROL_MATRIX_PATH = OUTPUT_DIRECTORY / "stage2_control_matrix.yaml"
DIAGNOSTIC_RECORD_PATH = OUTPUT_DIRECTORY / "stage2_diagnostic_records.csv"
GRADIENT_MATRIX_PATH = OUTPUT_DIRECTORY / "stage2_gradient_interaction_matrix.csv"
EXIT_GATE_SUMMARY_PATH = OUTPUT_DIRECTORY / "stage2_exit_gate_summary.json"
RANDOM_SEED = 314159
FLOAT_TOLERANCE = 1.0e-6


class Stage2SharedParameterToyModel(nn.Module):

    """Provide shared and auxiliary parameters for deterministic validation."""

    def __init__(self) -> None:

        """Initialize deterministic linear layers."""

        super().__init__()
        self.shared_projection = nn.Linear(2, 1, bias=False)
        self.auxiliary_head = nn.Linear(1, 1, bias=False)
        with torch.no_grad():
            self.shared_projection.weight.copy_(
                torch.tensor([[0.20, -0.15]], dtype=torch.float32)
            )
            self.auxiliary_head.weight.fill_(0.75)

    def forward(
        self,
        input_tensor: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:

        """Compute shared and auxiliary predictions."""

        shared_prediction_tensor = self.shared_projection(input_tensor)
        auxiliary_prediction_tensor = self.auxiliary_head(
            shared_prediction_tensor
        )
        return shared_prediction_tensor, auxiliary_prediction_tensor


def build_toy_batch() -> tuple[torch.Tensor, torch.Tensor]:

    """Build a deterministic batch with a known opposing physical target."""

    # Build Input Coordinates
    input_tensor = torch.tensor(
        [
            [-1.0, -0.5],
            [-0.5, 0.25],
            [0.0, 1.0],
            [0.5, -1.0],
            [1.0, 0.75],
            [1.5, -0.25],
        ],
        dtype=torch.float32,
    )

    # Build Protected Data Target
    target_weight_tensor = torch.tensor(
        [[0.90], [0.55]],
        dtype=torch.float32,
    )
    target_tensor = input_tensor @ target_weight_tensor
    return input_tensor, target_tensor


def build_component_configuration_list(
    manual_normalization_scale_dictionary: dict[str, float] | None = None,
) -> list[LossComponentConfiguration]:

    """Build the three-component Stage 2 validation contract."""

    # Resolve Optional Manual Scales
    scale_dictionary = manual_normalization_scale_dictionary or {
        "data_fit": 1.0,
        "harmonic_shape": 1.0,
        "weak_physics": 1.0,
    }

    # Declare Named Units, Roles, And Schedules
    return [
        LossComponentConfiguration(
            name="data_fit",
            unit_label="normalized_te_squared",
            normalization_scale=scale_dictionary["data_fit"],
            fixed_weight=1.0,
            role="main",
        ),
        LossComponentConfiguration(
            name="harmonic_shape",
            unit_label="normalized_complex_coefficient_squared",
            normalization_scale=scale_dictionary["harmonic_shape"],
            fixed_weight=1.0,
            role="auxiliary",
        ),
        LossComponentConfiguration(
            name="weak_physics",
            unit_label="normalized_residual_squared",
            normalization_scale=scale_dictionary["weak_physics"],
            fixed_weight=1.0,
            role="auxiliary",
            activation_schedule=LossActivationSchedule(
                start_step=2,
                full_weight_step=6,
            ),
        ),
    ]


def compute_toy_loss_dictionary(
    model: Stage2SharedParameterToyModel,
    input_tensor: torch.Tensor,
    target_tensor: torch.Tensor,
) -> dict[str, torch.Tensor]:

    """Compute aligned and conflicting scalar loss components."""

    # Compute Shared And Auxiliary Predictions
    shared_prediction_tensor, auxiliary_prediction_tensor = model(input_tensor)

    # Construct Distinct Objectives
    data_fit_loss = torch.mean(
        torch.square(shared_prediction_tensor - target_tensor)
    )
    harmonic_target_tensor = 0.80 * target_tensor
    harmonic_shape_loss = torch.mean(
        torch.square(auxiliary_prediction_tensor - harmonic_target_tensor)
    )
    weak_physics_target_tensor = -1.00 * target_tensor
    weak_physics_loss = torch.mean(
        torch.square(shared_prediction_tensor - weak_physics_target_tensor)
    )
    return {
        "data_fit": data_fit_loss,
        "harmonic_shape": harmonic_shape_loss,
        "weak_physics": weak_physics_loss,
    }


def assert_parameter_gradients_are_empty(
    parameter_sequence: list[torch.nn.Parameter],
) -> None:

    """Assert that functional diagnostics did not mutate `.grad` buffers."""

    assert all(parameter.grad is None for parameter in parameter_sequence), (
        "Functional per-loss diagnostics unexpectedly mutated .grad buffers"
    )


def build_control_matrix() -> dict[str, Any]:

    """Build the predeclared Stage 2 matched-control matrix."""

    return {
        "schema_version": 1,
        "stage": (
            "Wave 5.2R Stage 2: Evaluation And Optimization Instrumentation"
        ),
        "data_contract": {
            "dataset": "polished_dataset",
            "input_mode": "setpoints",
            "surface": "Fw",
            "split_signature": (
                "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16"
            ),
            "training_executed": False,
            "validation_scope": (
                "deterministic synthetic shared-parameter smoke harness"
            ),
        },
        "control_list": [
            {
                "control_id": "C0_FIXED_EQUAL",
                "description": "Fixed equal weights without unit rescaling.",
                "adapter": "fixed",
                "component_set": [
                    "data_fit",
                    "harmonic_shape",
                    "weak_physics",
                ],
                "normalization": "identity",
            },
            {
                "control_id": "C1_FIXED_MANUAL_NORMALIZATION",
                "description": (
                    "Fixed equal coefficients after explicit initial-loss "
                    "normalization."
                ),
                "adapter": "fixed",
                "component_set": [
                    "data_fit",
                    "harmonic_shape",
                    "weak_physics",
                ],
                "normalization": "declared_per_component_scale",
            },
            {
                "control_id": "C2_ADAPTIVE_WITHOUT_PHYSICS",
                "description": (
                    "Gradient-statistics weighting on data and harmonic losses "
                    "without a physical residual."
                ),
                "adapter": "gradient_statistics",
                "component_set": ["data_fit", "harmonic_shape"],
                "normalization": "declared_per_component_scale",
            },
            {
                "control_id": "C3_PHYSICS_IDENTICAL_FIXED",
                "description": (
                    "Weak-physics component with the same fixed coefficients "
                    "as the matched non-adaptive model."
                ),
                "adapter": "fixed",
                "component_set": [
                    "data_fit",
                    "harmonic_shape",
                    "weak_physics",
                ],
                "normalization": "declared_per_component_scale",
            },
        ],
        "adapter_list": [
            "fixed",
            "gradient_statistics",
            "relobralo_style",
            "conflict_aware",
        ],
        "exit_gate_check_list": [
            "named_loss_units_and_normalization",
            "loss_value_and_ema_tracking",
            "per_loss_gradient_norms",
            "pairwise_gradient_cosines",
            "update_to_parameter_ratio",
            "all_required_adapter_modes",
            "staged_loss_activation",
            "freeze_unfreeze_schedule",
            "deterministic_seed_and_dataloader",
            "functional_diagnostics_preserve_grad_buffers",
            "main_loss_preserving_conflict_projection",
            "all_required_controls_registered",
        ],
    }


def write_diagnostic_records(
    diagnostic_record_list: list[dict[str, Any]],
) -> None:

    """Write long-form component diagnostic records."""

    # Freeze CSV Schema
    field_name_list = [
        "record_id",
        "optimization_step",
        "adapter_name",
        "component_name",
        "raw_loss",
        "normalized_loss",
        "loss_ema",
        "activation_multiplier",
        "weight",
        "gradient_norm",
    ]

    # Write One Row Per Component
    with DIAGNOSTIC_RECORD_PATH.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_name_list)
        csv_writer.writeheader()
        for record_index, diagnostic_record in enumerate(
            diagnostic_record_list
        ):
            for component_name in diagnostic_record["raw_loss_dictionary"]:
                csv_writer.writerow(
                    {
                        "record_id": record_index,
                        "optimization_step": diagnostic_record[
                            "optimization_step"
                        ],
                        "adapter_name": diagnostic_record["adapter_name"],
                        "component_name": component_name,
                        "raw_loss": diagnostic_record[
                            "raw_loss_dictionary"
                        ][component_name],
                        "normalized_loss": diagnostic_record[
                            "normalized_loss_dictionary"
                        ][component_name],
                        "loss_ema": diagnostic_record["loss_ema_dictionary"][
                            component_name
                        ],
                        "activation_multiplier": diagnostic_record[
                            "activation_multiplier_dictionary"
                        ][component_name],
                        "weight": diagnostic_record["weight_dictionary"][
                            component_name
                        ],
                        "gradient_norm": diagnostic_record[
                            "gradient_norm_dictionary"
                        ][component_name],
                    }
                )


def write_gradient_matrix(
    diagnostic_record_list: list[dict[str, Any]],
) -> None:

    """Write long-form pairwise gradient cosine records."""

    # Freeze CSV Schema
    field_name_list = [
        "record_id",
        "optimization_step",
        "adapter_name",
        "component_pair",
        "gradient_cosine_similarity",
    ]

    # Write One Row Per Pair
    with GRADIENT_MATRIX_PATH.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_name_list)
        csv_writer.writeheader()
        for record_index, diagnostic_record in enumerate(
            diagnostic_record_list
        ):
            for component_pair, cosine_similarity in diagnostic_record[
                "pairwise_gradient_cosine_dictionary"
            ].items():
                csv_writer.writerow(
                    {
                        "record_id": record_index,
                        "optimization_step": diagnostic_record[
                            "optimization_step"
                        ],
                        "adapter_name": diagnostic_record["adapter_name"],
                        "component_pair": component_pair,
                        "gradient_cosine_similarity": cosine_similarity,
                    }
                )


def validate_deterministic_dataloader() -> dict[str, Any]:

    """Validate identical seed fingerprints and different shuffle orders."""

    # Build Stable Dataset
    input_tensor = torch.arange(40, dtype=torch.float32).reshape(20, 2)
    target_tensor = torch.arange(20, dtype=torch.float32).reshape(20, 1)
    dataset = TensorDataset(input_tensor, target_tensor)

    # Compare Equal And Distinct Seeds
    first_loader = build_deterministic_dataloader(
        dataset,
        batch_size=4,
        random_seed=RANDOM_SEED,
    )
    repeated_loader = build_deterministic_dataloader(
        dataset,
        batch_size=4,
        random_seed=RANDOM_SEED,
    )
    alternate_loader = build_deterministic_dataloader(
        dataset,
        batch_size=4,
        random_seed=RANDOM_SEED + 1,
    )
    first_fingerprint = compute_dataloader_fingerprint(first_loader)
    repeated_fingerprint = compute_dataloader_fingerprint(repeated_loader)
    alternate_fingerprint = compute_dataloader_fingerprint(alternate_loader)
    assert first_fingerprint == repeated_fingerprint, (
        "Identical dataloader seeds produced different ordered-batch hashes"
    )
    assert first_fingerprint != alternate_fingerprint, (
        "Distinct dataloader seeds produced the same shuffled-batch hash"
    )
    return {
        "seed": RANDOM_SEED,
        "repeated_seed_fingerprint": first_fingerprint,
        "repeated_seed_match": True,
        "alternate_seed": RANDOM_SEED + 1,
        "alternate_seed_fingerprint": alternate_fingerprint,
        "alternate_seed_differs": True,
    }


def main() -> int:

    """Run every Stage 2 exit-gate validation and write durable evidence."""

    # Prepare Deterministic Runtime And Output
    configure_deterministic_execution(RANDOM_SEED)
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    control_matrix = build_control_matrix()
    CONTROL_MATRIX_PATH.write_text(
        yaml.safe_dump(control_matrix, sort_keys=False),
        encoding="utf-8",
    )

    # Build Shared-Parameter Toy Problem
    model = Stage2SharedParameterToyModel()
    input_tensor, target_tensor = build_toy_batch()
    raw_loss_dictionary = compute_toy_loss_dictionary(
        model,
        input_tensor,
        target_tensor,
    )
    shared_parameter_list = list(model.shared_projection.parameters())
    assert_parameter_gradients_are_empty(shared_parameter_list)

    # Validate Named Raw And Manually Normalized Components
    raw_loss_value_dictionary = {
        component_name: float(raw_loss.detach().cpu().item())
        for component_name, raw_loss in raw_loss_dictionary.items()
    }
    manual_normalization_scale_dictionary = {
        component_name: max(loss_value, 1.0e-8)
        for component_name, loss_value in raw_loss_value_dictionary.items()
    }
    manually_normalized_instrumentation = (
        PhysicsGuidedOptimizationInstrumentation(
            build_component_configuration_list(
                manual_normalization_scale_dictionary
            ),
            ema_decay=0.50,
            random_seed=RANDOM_SEED,
        )
    )
    manually_normalized_loss_dictionary = (
        manually_normalized_instrumentation.normalize_loss_dictionary(
            raw_loss_dictionary
        )
    )
    for component_name, normalized_loss in (
        manually_normalized_loss_dictionary.items()
    ):
        assert abs(float(normalized_loss.detach().cpu().item()) - 1.0) < (
            FLOAT_TOLERANCE
        ), f"Manual normalization did not produce unit scale | {component_name}"

    # Validate Fixed Diagnostics And EMA State
    instrumentation = PhysicsGuidedOptimizationInstrumentation(
        build_component_configuration_list(),
        ema_decay=0.50,
        random_seed=RANDOM_SEED,
    )
    fixed_diagnostic_record = instrumentation.build_diagnostic_record(
        raw_loss_dictionary=raw_loss_dictionary,
        shared_parameter_sequence=shared_parameter_list,
        adapter_name="fixed",
        optimization_step=6,
    )
    assert_parameter_gradients_are_empty(shared_parameter_list)
    assert all(
        gradient_norm > 0.0
        for gradient_norm in fixed_diagnostic_record[
            "gradient_norm_dictionary"
        ].values()
    ), "Every toy loss must expose a non-zero shared-parameter gradient"
    assert (
        fixed_diagnostic_record["pairwise_gradient_cosine_dictionary"][
            "data_fit__vs__weak_physics"
        ]
        < 0.0
    ), "The weak-physics toy loss must conflict with the protected data loss"
    for component_name in raw_loss_dictionary:
        assert abs(
            fixed_diagnostic_record["loss_ema_dictionary"][component_name]
            - fixed_diagnostic_record["normalized_loss_dictionary"][
                component_name
            ]
        ) < FLOAT_TOLERANCE, (
            f"First EMA observation must equal the current loss | {component_name}"
        )

    # Validate Gradient-Statistics Adapter
    gradient_statistics_record = instrumentation.build_diagnostic_record(
        raw_loss_dictionary=raw_loss_dictionary,
        shared_parameter_sequence=shared_parameter_list,
        adapter_name="gradient_statistics",
        optimization_step=6,
    )
    assert_parameter_gradients_are_empty(shared_parameter_list)
    assert all(
        math_value >= 0.0
        for math_value in gradient_statistics_record[
            "weight_dictionary"
        ].values()
    ), "Gradient-statistics weights must be non-negative"

    # Validate Adaptive Control Without Physics
    adaptive_without_physics_configuration_list = [
        component_configuration
        for component_configuration in build_component_configuration_list()
        if component_configuration.name != "weak_physics"
    ]
    adaptive_without_physics_instrumentation = (
        PhysicsGuidedOptimizationInstrumentation(
            adaptive_without_physics_configuration_list,
            random_seed=RANDOM_SEED,
        )
    )
    adaptive_without_physics_loss_dictionary = {
        component_name: raw_loss_dictionary[component_name]
        for component_name in ["data_fit", "harmonic_shape"]
    }
    adaptive_without_physics_record = (
        adaptive_without_physics_instrumentation.build_diagnostic_record(
            raw_loss_dictionary=adaptive_without_physics_loss_dictionary,
            shared_parameter_sequence=shared_parameter_list,
            adapter_name="gradient_statistics",
            optimization_step=0,
        )
    )
    assert set(adaptive_without_physics_record["weight_dictionary"]) == {
        "data_fit",
        "harmonic_shape",
    }, "Adaptive-without-physics control contains an unexpected component"

    # Validate Deterministic ReLoBRaLo-Style State
    relobralo_instrumentation = PhysicsGuidedOptimizationInstrumentation(
        build_component_configuration_list(),
        ema_decay=0.50,
        random_seed=RANDOM_SEED,
    )
    relobralo_initial_record = relobralo_instrumentation.build_diagnostic_record(
        raw_loss_dictionary=raw_loss_dictionary,
        shared_parameter_sequence=shared_parameter_list,
        adapter_name="relobralo_style",
        optimization_step=6,
    )
    scaled_loss_dictionary = {
        "data_fit": raw_loss_dictionary["data_fit"] * 0.50,
        "harmonic_shape": raw_loss_dictionary["harmonic_shape"] * 0.90,
        "weak_physics": raw_loss_dictionary["weak_physics"] * 1.10,
    }
    relobralo_followup_record = relobralo_instrumentation.build_diagnostic_record(
        raw_loss_dictionary=scaled_loss_dictionary,
        shared_parameter_sequence=shared_parameter_list,
        adapter_name="relobralo_style",
        optimization_step=7,
    )
    assert relobralo_initial_record["weight_dictionary"] != (
        relobralo_followup_record["weight_dictionary"]
    ), "ReLoBRaLo-style weights did not react to relative progress"
    assert_parameter_gradients_are_empty(shared_parameter_list)

    # Validate Main-Loss-Preserving Conflict Projection And Optimizer Update
    normalized_loss_dictionary = instrumentation.normalize_loss_dictionary(
        raw_loss_dictionary
    )
    component_gradient_dictionary = (
        instrumentation.compute_component_gradient_dictionary(
            normalized_loss_dictionary,
            shared_parameter_list,
        )
    )
    conflict_weight_dictionary = instrumentation.resolve_weight_dictionary(
        adapter_name="conflict_aware",
        normalized_loss_dictionary=normalized_loss_dictionary,
        gradient_norm_dictionary=(
            instrumentation.compute_gradient_norm_dictionary(
                component_gradient_dictionary
            )
        ),
        optimization_step=6,
    )
    combined_gradient, projection_record_dictionary = (
        instrumentation.compose_main_loss_preserving_gradient(
            component_gradient_dictionary,
            conflict_weight_dictionary,
        )
    )
    weak_physics_projection_record = projection_record_dictionary[
        "weak_physics"
    ]
    assert weak_physics_projection_record["projection_applied"] is True, (
        "Conflict-aware adapter did not project the opposing physics gradient"
    )
    assert float(weak_physics_projection_record["cosine_after"]) >= (
        -FLOAT_TOLERANCE
    ), "Projected physics gradient remains negatively aligned with main loss"
    assert_parameter_gradients_are_empty(shared_parameter_list)

    optimizer = torch.optim.SGD(shared_parameter_list, lr=0.05)
    parameter_vector_before_step = capture_trainable_parameter_vector(
        shared_parameter_list
    )
    optimizer.zero_grad(set_to_none=True)
    assign_flat_gradient_to_parameters(
        combined_gradient,
        shared_parameter_list,
    )
    optimizer.step()
    parameter_vector_after_step = capture_trainable_parameter_vector(
        shared_parameter_list
    )
    update_to_parameter_ratio = compute_update_to_parameter_ratio(
        parameter_vector_before_step,
        parameter_vector_after_step,
    )
    assert update_to_parameter_ratio > 0.0, (
        "Conflict-aware optimizer smoke step produced no parameter update"
    )

    # Validate Staged Activation
    staged_activation_multiplier_dictionary = {
        optimization_step: (
            instrumentation.resolve_activation_multiplier_dictionary(
                optimization_step
            )["weak_physics"]
        )
        for optimization_step in [0, 2, 4, 6, 7]
    }
    assert staged_activation_multiplier_dictionary == {
        0: 0.0,
        2: 0.0,
        4: 0.5,
        6: 1.0,
        7: 1.0,
    }, (
        "Staged weak-physics activation differs from the declared schedule | "
        f"{staged_activation_multiplier_dictionary}"
    )

    # Validate Parameter Freeze-Unfreeze Schedule
    freeze_schedule = ParameterFreezeSchedule(
        parameter_name_token_list=("auxiliary_head",),
        freeze_before_step=5,
    )
    matched_parameter_name_list = freeze_schedule.apply(
        model.named_parameters(),
        optimization_step=0,
    )
    assert all(
        not parameter.requires_grad
        for parameter_name, parameter in model.named_parameters()
        if parameter_name in matched_parameter_name_list
    ), "Auxiliary parameters were not frozen before the release step"
    freeze_schedule.apply(model.named_parameters(), optimization_step=5)
    assert all(
        parameter.requires_grad
        for parameter_name, parameter in model.named_parameters()
        if parameter_name in matched_parameter_name_list
    ), "Auxiliary parameters were not unfrozen at the release step"

    # Validate Dataloader Determinism
    deterministic_dataloader_summary = validate_deterministic_dataloader()

    # Persist Long-Form Diagnostics
    diagnostic_record_list = [
        fixed_diagnostic_record,
        gradient_statistics_record,
        adaptive_without_physics_record,
        relobralo_initial_record,
        relobralo_followup_record,
    ]
    write_diagnostic_records(diagnostic_record_list)
    write_gradient_matrix(diagnostic_record_list)

    # Persist Exit-Gate Summary
    exit_gate_summary = {
        "schema_version": 1,
        "stage": (
            "Wave 5.2R Stage 2: Evaluation And Optimization Instrumentation"
        ),
        "status": "pass",
        "training_executed": False,
        "random_seed": RANDOM_SEED,
        "component_count": 3,
        "adapter_count": 4,
        "required_control_count": len(control_matrix["control_list"]),
        "exit_gate_check_count": len(
            control_matrix["exit_gate_check_list"]
        ),
        "exit_gate_pass_count": len(
            control_matrix["exit_gate_check_list"]
        ),
        "update_to_parameter_ratio": update_to_parameter_ratio,
        "negative_data_physics_cosine_before_projection": (
            weak_physics_projection_record["cosine_before"]
        ),
        "data_physics_cosine_after_projection": (
            weak_physics_projection_record["cosine_after"]
        ),
        "weak_physics_projection_applied": (
            weak_physics_projection_record["projection_applied"]
        ),
        "staged_activation_multiplier_dictionary": (
            staged_activation_multiplier_dictionary
        ),
        "freeze_unfreeze_parameter_name_list": (
            matched_parameter_name_list
        ),
        "deterministic_dataloader": deterministic_dataloader_summary,
        "artifact_dictionary": {
            "control_matrix": CONTROL_MATRIX_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "diagnostic_records": DIAGNOSTIC_RECORD_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "gradient_interaction_matrix": GRADIENT_MATRIX_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "exit_gate_summary": EXIT_GATE_SUMMARY_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
        },
        "conclusion": (
            "Loss interaction is observable and all Stage 2 adapters, "
            "schedules, deterministic checks, and matched controls pass the "
            "synthetic shared-parameter smoke gate."
        ),
    }
    EXIT_GATE_SUMMARY_PATH.write_text(
        json.dumps(exit_gate_summary, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        "WAVE52R_STAGE2_VALIDATION_OK "
        f"components={exit_gate_summary['component_count']} "
        f"adapters={exit_gate_summary['adapter_count']} "
        f"controls={exit_gate_summary['required_control_count']} "
        f"checks={exit_gate_summary['exit_gate_pass_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
