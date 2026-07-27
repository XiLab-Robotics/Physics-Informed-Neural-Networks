"""Reusable loss-interaction instrumentation for physics-guided TE training."""

from __future__ import annotations

# Import Python Utilities
import hashlib
import math
import os
import random
from dataclasses import dataclass
from typing import Any
from typing import Iterable
from typing import Mapping
from typing import Sequence

# Import PyTorch Utilities
import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset

SUPPORTED_WEIGHT_ADAPTER_NAME_SET = {
    "fixed",
    "gradient_statistics",
    "relobralo_style",
    "conflict_aware",
}
LOSS_COMPONENT_ROLE_SET = {"main", "auxiliary"}
DEFAULT_EPSILON = 1.0e-12


@dataclass(frozen=True)
class LossActivationSchedule:

    """Describe the staged activation interval for one loss component.

    Attributes:
        start_step: First optimization step with a non-zero multiplier.
        full_weight_step: First step at which the multiplier reaches one.
        end_step: Optional first step at which the component becomes inactive.
    """

    start_step: int = 0
    full_weight_step: int = 0
    end_step: int | None = None

    def __post_init__(self) -> None:

        """Validate the activation interval."""

        assert self.start_step >= 0, (
            f"Loss start step must be non-negative | {self.start_step}"
        )
        assert self.full_weight_step >= self.start_step, (
            "Loss full-weight step must not precede the start step | "
            f"{self.full_weight_step} vs {self.start_step}"
        )
        if self.end_step is not None:
            assert self.end_step > self.full_weight_step, (
                "Loss end step must follow the full-weight step | "
                f"{self.end_step} vs {self.full_weight_step}"
            )

    def resolve_multiplier(self, optimization_step: int) -> float:

        """Resolve the deterministic activation multiplier for one step.

        Args:
            optimization_step: Zero-based optimizer-step index.

        Returns:
            Component multiplier inside the closed interval from zero to one.
        """

        # Validate Step
        assert optimization_step >= 0, (
            f"Optimization step must be non-negative | {optimization_step}"
        )

        # Resolve Inactive Intervals
        if optimization_step < self.start_step:
            return 0.0
        if self.end_step is not None and optimization_step >= self.end_step:
            return 0.0

        # Resolve Immediate Or Completed Activation
        if self.full_weight_step == self.start_step:
            return 1.0
        if optimization_step >= self.full_weight_step:
            return 1.0

        # Resolve Linear Warm-Up
        warmup_step_count = self.full_weight_step - self.start_step
        active_step_count = optimization_step - self.start_step
        return float(active_step_count) / float(warmup_step_count)


@dataclass(frozen=True)
class LossComponentConfiguration:

    """Define one named, normalized, and scheduled loss component.

    Attributes:
        name: Stable machine-facing component name.
        unit_label: Human-readable raw unit, such as normalized TE squared.
        normalization_scale: Positive divisor that maps the raw loss to an
            order-one comparison scale.
        fixed_weight: Baseline coefficient used by fixed controls and as the
            reference coefficient for adaptive adapters.
        role: Either `main` for the protected data loss or `auxiliary`.
        activation_schedule: Optional staged activation contract.
    """

    name: str
    unit_label: str
    normalization_scale: float = 1.0
    fixed_weight: float = 1.0
    role: str = "auxiliary"
    activation_schedule: LossActivationSchedule = LossActivationSchedule()

    def __post_init__(self) -> None:

        """Validate the component contract."""

        assert self.name.strip(), "Loss component name must not be empty"
        assert self.unit_label.strip(), (
            f"Loss component unit label must not be empty | {self.name}"
        )
        assert self.normalization_scale > 0.0, (
            "Loss component normalization scale must be positive | "
            f"{self.name} | {self.normalization_scale}"
        )
        assert self.fixed_weight >= 0.0, (
            "Loss component fixed weight must be non-negative | "
            f"{self.name} | {self.fixed_weight}"
        )
        assert self.role in LOSS_COMPONENT_ROLE_SET, (
            f"Unsupported loss component role | {self.name} | {self.role}"
        )


@dataclass(frozen=True)
class ParameterFreezeSchedule:

    """Define a name-matched parameter freeze-unfreeze interval.

    Attributes:
        parameter_name_token_list: Tokens matched against model parameter names.
        freeze_before_step: Parameters are frozen before this optimizer step.
    """

    parameter_name_token_list: tuple[str, ...]
    freeze_before_step: int

    def __post_init__(self) -> None:

        """Validate the parameter schedule."""

        assert self.parameter_name_token_list, (
            "Parameter freeze schedule requires at least one name token"
        )
        assert all(token.strip() for token in self.parameter_name_token_list), (
            "Parameter freeze schedule contains an empty name token"
        )
        assert self.freeze_before_step >= 0, (
            f"Freeze-before step must be non-negative | {self.freeze_before_step}"
        )

    def apply(
        self,
        named_parameter_iterable: Iterable[tuple[str, torch.nn.Parameter]],
        optimization_step: int,
    ) -> list[str]:

        """Apply the freeze state and return the matched parameter names.

        Args:
            named_parameter_iterable: Model parameter names and tensors.
            optimization_step: Zero-based optimizer-step index.

        Returns:
            Names of parameters matched by the schedule.
        """

        # Resolve Desired State
        assert optimization_step >= 0, (
            f"Optimization step must be non-negative | {optimization_step}"
        )
        requires_gradient = optimization_step >= self.freeze_before_step

        # Apply State To Matching Parameters
        matched_parameter_name_list: list[str] = []
        for parameter_name, parameter in named_parameter_iterable:
            if not any(
                token in parameter_name
                for token in self.parameter_name_token_list
            ):
                continue
            parameter.requires_grad_(requires_gradient)
            matched_parameter_name_list.append(parameter_name)

        assert matched_parameter_name_list, (
            "Parameter freeze schedule did not match any parameter | "
            f"{self.parameter_name_token_list}"
        )
        return matched_parameter_name_list


class PhysicsGuidedOptimizationInstrumentation:

    """Measure and adapt named loss interactions on shared parameters.

    The class keeps scalar history only. Per-loss gradients are computed with
    functional autograd and therefore do not populate or overwrite parameter
    `.grad` buffers.
    """

    def __init__(
        self,
        component_configuration_list: Sequence[LossComponentConfiguration],
        ema_decay: float = 0.95,
        epsilon: float = DEFAULT_EPSILON,
        random_seed: int = 314159,
    ) -> None:

        """Initialize the loss-interaction instrumentation.

        Args:
            component_configuration_list: Complete named component contract.
            ema_decay: Exponential moving-average retention coefficient.
            epsilon: Positive numerical-stability floor.
            random_seed: Seed used by deterministic ReLoBRaLo-style lookbacks.
        """

        # Validate Global Configuration
        assert component_configuration_list, (
            "At least one loss component configuration is required"
        )
        assert 0.0 <= ema_decay < 1.0, (
            f"EMA decay must be inside [0, 1) | {ema_decay}"
        )
        assert epsilon > 0.0, f"Epsilon must be positive | {epsilon}"

        # Index Components And Main Loss
        self.component_configuration_dictionary = {
            component_configuration.name: component_configuration
            for component_configuration in component_configuration_list
        }
        assert len(self.component_configuration_dictionary) == len(
            component_configuration_list
        ), "Loss component names must be unique"
        main_component_name_list = [
            component_configuration.name
            for component_configuration in component_configuration_list
            if component_configuration.role == "main"
        ]
        assert len(main_component_name_list) == 1, (
            "Exactly one protected main loss component is required | "
            f"{main_component_name_list}"
        )

        # Initialize State
        self.main_component_name = main_component_name_list[0]
        self.ema_decay = float(ema_decay)
        self.epsilon = float(epsilon)
        self.random_generator = random.Random(int(random_seed))
        self.loss_ema_dictionary: dict[str, float] = {}
        self.initial_normalized_loss_dictionary: dict[str, float] = {}
        self.previous_normalized_loss_dictionary: dict[str, float] = {}
        self.previous_weight_dictionary: dict[str, float] = {}

    def validate_loss_dictionary(
        self,
        raw_loss_dictionary: Mapping[str, torch.Tensor],
    ) -> None:

        """Validate exact component coverage and scalar tensor structure."""

        # Validate Exact Names
        observed_name_set = set(raw_loss_dictionary)
        expected_name_set = set(self.component_configuration_dictionary)
        assert observed_name_set == expected_name_set, (
            "Raw loss dictionary does not match the component contract | "
            f"missing={sorted(expected_name_set - observed_name_set)} | "
            f"unexpected={sorted(observed_name_set - expected_name_set)}"
        )

        # Validate Scalar Finite Tensors
        for component_name, raw_loss_tensor in raw_loss_dictionary.items():
            assert isinstance(raw_loss_tensor, torch.Tensor), (
                f"Loss component must be a tensor | {component_name}"
            )
            assert raw_loss_tensor.numel() == 1, (
                f"Loss component must be scalar | {component_name} | "
                f"shape={tuple(raw_loss_tensor.shape)}"
            )
            assert bool(torch.isfinite(raw_loss_tensor.detach()).all()), (
                f"Loss component must be finite | {component_name}"
            )

    def normalize_loss_dictionary(
        self,
        raw_loss_dictionary: Mapping[str, torch.Tensor],
    ) -> dict[str, torch.Tensor]:

        """Normalize all loss components into declared comparison units."""

        # Validate Component Coverage
        self.validate_loss_dictionary(raw_loss_dictionary)

        # Apply Explicit Scales
        return {
            component_name: (
                raw_loss_tensor
                / self.component_configuration_dictionary[
                    component_name
                ].normalization_scale
            )
            for component_name, raw_loss_tensor in raw_loss_dictionary.items()
        }

    def update_loss_ema_dictionary(
        self,
        normalized_loss_dictionary: Mapping[str, torch.Tensor],
    ) -> dict[str, float]:

        """Update and return normalized per-component loss EMAs."""

        # Update Each Component Independently
        for component_name, normalized_loss_tensor in (
            normalized_loss_dictionary.items()
        ):
            normalized_loss_value = float(
                normalized_loss_tensor.detach().cpu().item()
            )
            previous_ema = self.loss_ema_dictionary.get(
                component_name,
                normalized_loss_value,
            )
            updated_ema = (
                self.ema_decay * previous_ema
                + (1.0 - self.ema_decay) * normalized_loss_value
            )
            self.loss_ema_dictionary[component_name] = updated_ema

        return dict(self.loss_ema_dictionary)

    def resolve_activation_multiplier_dictionary(
        self,
        optimization_step: int,
    ) -> dict[str, float]:

        """Resolve the activation multiplier of every component."""

        return {
            component_name: (
                component_configuration.activation_schedule.resolve_multiplier(
                    optimization_step
                )
            )
            for component_name, component_configuration in (
                self.component_configuration_dictionary.items()
            )
        }

    def compute_component_gradient_dictionary(
        self,
        normalized_loss_dictionary: Mapping[str, torch.Tensor],
        shared_parameter_sequence: Sequence[torch.nn.Parameter],
    ) -> dict[str, torch.Tensor]:

        """Compute one flattened gradient vector per normalized loss.

        Args:
            normalized_loss_dictionary: Scalar normalized losses.
            shared_parameter_sequence: Declared shared trainable parameters.

        Returns:
            Component names mapped to flattened detached gradient vectors.
        """

        # Freeze Active Parameter Layout
        active_parameter_list = [
            parameter
            for parameter in shared_parameter_sequence
            if parameter.requires_grad
        ]
        assert active_parameter_list, (
            "At least one shared parameter must require gradients"
        )

        # Compute Functional Gradients Without Touching .grad Buffers
        component_gradient_dictionary: dict[str, torch.Tensor] = {}
        for component_name, normalized_loss_tensor in (
            normalized_loss_dictionary.items()
        ):
            if normalized_loss_tensor.requires_grad:
                gradient_tuple = torch.autograd.grad(
                    normalized_loss_tensor,
                    tuple(active_parameter_list),
                    retain_graph=True,
                    create_graph=False,
                    allow_unused=True,
                )
            else:
                gradient_tuple = tuple(None for _ in active_parameter_list)

            flattened_gradient_list = []
            for parameter, parameter_gradient in zip(
                active_parameter_list,
                gradient_tuple,
                strict=True,
            ):
                if parameter_gradient is None:
                    flattened_gradient_list.append(
                        torch.zeros_like(parameter).reshape(-1)
                    )
                else:
                    flattened_gradient_list.append(
                        parameter_gradient.detach().reshape(-1)
                    )
            component_gradient_dictionary[component_name] = torch.cat(
                flattened_gradient_list
            )

        return component_gradient_dictionary

    def compute_gradient_norm_dictionary(
        self,
        component_gradient_dictionary: Mapping[str, torch.Tensor],
    ) -> dict[str, float]:

        """Compute the L2 norm of each component gradient."""

        return {
            component_name: float(
                torch.linalg.vector_norm(component_gradient_tensor).cpu().item()
            )
            for component_name, component_gradient_tensor in (
                component_gradient_dictionary.items()
            )
        }

    def compute_pairwise_gradient_cosine_dictionary(
        self,
        component_gradient_dictionary: Mapping[str, torch.Tensor],
    ) -> dict[str, float]:

        """Compute every unique pairwise gradient cosine similarity."""

        # Enumerate Stable Component Pairs
        component_name_list = list(component_gradient_dictionary)
        pairwise_cosine_dictionary: dict[str, float] = {}
        for left_index, left_component_name in enumerate(component_name_list):
            left_gradient = component_gradient_dictionary[left_component_name]
            left_norm = torch.linalg.vector_norm(left_gradient)
            for right_component_name in component_name_list[left_index + 1 :]:
                right_gradient = component_gradient_dictionary[
                    right_component_name
                ]
                right_norm = torch.linalg.vector_norm(right_gradient)
                denominator = left_norm * right_norm
                if float(denominator.detach().cpu().item()) <= self.epsilon:
                    cosine_value = 0.0
                else:
                    cosine_tensor = torch.dot(
                        left_gradient,
                        right_gradient,
                    ) / denominator
                    cosine_value = float(cosine_tensor.cpu().item())

                pair_name = (
                    f"{left_component_name}__vs__{right_component_name}"
                )
                pairwise_cosine_dictionary[pair_name] = cosine_value

        return pairwise_cosine_dictionary

    def resolve_weight_dictionary(
        self,
        adapter_name: str,
        normalized_loss_dictionary: Mapping[str, torch.Tensor],
        gradient_norm_dictionary: Mapping[str, float],
        optimization_step: int,
        gradient_weight_minimum: float = 0.05,
        gradient_weight_maximum: float = 20.0,
        relobralo_temperature: float = 0.25,
        relobralo_lookback_probability: float = 0.95,
        relobralo_previous_weight_retention: float = 0.90,
    ) -> dict[str, float]:

        """Resolve component weights for one supported adapter.

        Args:
            adapter_name: Registered adapter name.
            normalized_loss_dictionary: Current normalized scalar losses.
            gradient_norm_dictionary: Current per-component gradient norms.
            optimization_step: Zero-based optimizer-step index.
            gradient_weight_minimum: Lower adaptive-weight clamp.
            gradient_weight_maximum: Upper adaptive-weight clamp.
            relobralo_temperature: Positive relative-progress softmax scale.
            relobralo_lookback_probability: Probability of comparing with the
                initial rather than immediately previous loss state.
            relobralo_previous_weight_retention: Previous-weight blend factor.

        Returns:
            Component names mapped to finite non-negative weights.
        """

        # Validate Adapter Parameters
        normalized_adapter_name = adapter_name.strip().lower()
        assert normalized_adapter_name in SUPPORTED_WEIGHT_ADAPTER_NAME_SET, (
            f"Unsupported loss-weight adapter | {adapter_name}"
        )
        assert 0.0 < gradient_weight_minimum <= gradient_weight_maximum, (
            "Gradient weight clamps must be positive and ordered"
        )
        assert relobralo_temperature > 0.0, (
            "ReLoBRaLo-style temperature must be positive"
        )
        assert 0.0 <= relobralo_lookback_probability <= 1.0, (
            "ReLoBRaLo-style lookback probability must be inside [0, 1]"
        )
        assert 0.0 <= relobralo_previous_weight_retention < 1.0, (
            "ReLoBRaLo-style retention must be inside [0, 1)"
        )

        # Resolve Baseline Scheduled Weights
        activation_multiplier_dictionary = (
            self.resolve_activation_multiplier_dictionary(optimization_step)
        )
        fixed_weight_dictionary = {
            component_name: (
                component_configuration.fixed_weight
                * activation_multiplier_dictionary[component_name]
            )
            for component_name, component_configuration in (
                self.component_configuration_dictionary.items()
            )
        }
        if normalized_adapter_name in {"fixed", "conflict_aware"}:
            return fixed_weight_dictionary

        # Resolve Gradient-Statistics Weights
        if normalized_adapter_name == "gradient_statistics":
            main_gradient_norm = max(
                gradient_norm_dictionary[self.main_component_name],
                self.epsilon,
            )
            gradient_weight_dictionary: dict[str, float] = {}
            for component_name, fixed_weight in fixed_weight_dictionary.items():
                if fixed_weight == 0.0:
                    gradient_weight_dictionary[component_name] = 0.0
                    continue
                if component_name == self.main_component_name:
                    gradient_weight_dictionary[component_name] = fixed_weight
                    continue
                component_gradient_norm = max(
                    gradient_norm_dictionary[component_name],
                    self.epsilon,
                )
                gradient_ratio = main_gradient_norm / component_gradient_norm
                clamped_gradient_ratio = min(
                    max(gradient_ratio, gradient_weight_minimum),
                    gradient_weight_maximum,
                )
                gradient_weight_dictionary[component_name] = (
                    fixed_weight * clamped_gradient_ratio
                )
            return gradient_weight_dictionary

        # Resolve ReLoBRaLo-Style Relative-Progress Weights
        normalized_loss_value_dictionary = {
            component_name: float(
                normalized_loss_tensor.detach().cpu().item()
            )
            for component_name, normalized_loss_tensor in (
                normalized_loss_dictionary.items()
            )
        }
        if not self.initial_normalized_loss_dictionary:
            self.initial_normalized_loss_dictionary = dict(
                normalized_loss_value_dictionary
            )
            self.previous_normalized_loss_dictionary = dict(
                normalized_loss_value_dictionary
            )
            self.previous_weight_dictionary = dict(fixed_weight_dictionary)
            return fixed_weight_dictionary

        use_initial_lookback = (
            self.random_generator.random() < relobralo_lookback_probability
        )
        reference_loss_dictionary = (
            self.initial_normalized_loss_dictionary
            if use_initial_lookback
            else self.previous_normalized_loss_dictionary
        )
        active_component_name_list = [
            component_name
            for component_name, fixed_weight in fixed_weight_dictionary.items()
            if fixed_weight > 0.0
        ]
        relative_progress_dictionary = {
            component_name: (
                normalized_loss_value_dictionary[component_name]
                / (
                    abs(reference_loss_dictionary[component_name])
                    + self.epsilon
                )
            )
            for component_name in active_component_name_list
        }
        maximum_progress = max(relative_progress_dictionary.values())
        exponential_score_dictionary = {
            component_name: math.exp(
                (
                    relative_progress_dictionary[component_name]
                    - maximum_progress
                )
                / relobralo_temperature
            )
            for component_name in active_component_name_list
        }
        exponential_score_sum = sum(exponential_score_dictionary.values())
        balanced_weight_dictionary = {
            component_name: (
                len(active_component_name_list)
                * exponential_score_dictionary[component_name]
                / exponential_score_sum
            )
            for component_name in active_component_name_list
        }

        # Blend With Previous Weights And Preserve Inactive Components
        relobralo_weight_dictionary: dict[str, float] = {}
        for component_name, fixed_weight in fixed_weight_dictionary.items():
            if fixed_weight == 0.0:
                relobralo_weight_dictionary[component_name] = 0.0
                continue
            previous_weight = self.previous_weight_dictionary.get(
                component_name,
                fixed_weight,
            )
            balanced_weight = (
                fixed_weight * balanced_weight_dictionary[component_name]
            )
            relobralo_weight_dictionary[component_name] = (
                relobralo_previous_weight_retention * previous_weight
                + (1.0 - relobralo_previous_weight_retention)
                * balanced_weight
            )

        self.previous_normalized_loss_dictionary = dict(
            normalized_loss_value_dictionary
        )
        self.previous_weight_dictionary = dict(relobralo_weight_dictionary)
        return relobralo_weight_dictionary

    def compose_weighted_loss(
        self,
        normalized_loss_dictionary: Mapping[str, torch.Tensor],
        weight_dictionary: Mapping[str, float],
    ) -> torch.Tensor:

        """Compose a scalar weighted loss without gradient surgery."""

        # Validate Exact Weight Coverage
        assert set(weight_dictionary) == set(normalized_loss_dictionary), (
            "Weight dictionary must cover every normalized loss exactly"
        )

        # Compose Explicit Weighted Sum
        weighted_loss_list = [
            normalized_loss_dictionary[component_name]
            * float(weight_dictionary[component_name])
            for component_name in normalized_loss_dictionary
        ]
        return torch.stack(weighted_loss_list).sum()

    def compose_main_loss_preserving_gradient(
        self,
        component_gradient_dictionary: Mapping[str, torch.Tensor],
        weight_dictionary: Mapping[str, float],
    ) -> tuple[torch.Tensor, dict[str, dict[str, float | bool]]]:

        """Project conflicting auxiliary gradients while preserving the main.

        Each auxiliary gradient with a negative dot product against the main
        gradient is projected onto the main-gradient normal plane. The protected
        main gradient is never altered.

        Args:
            component_gradient_dictionary: Flattened component gradients.
            weight_dictionary: Scalar component coefficients.

        Returns:
            Combined flattened gradient and per-auxiliary projection records.
        """

        # Resolve Protected Main Gradient
        assert set(component_gradient_dictionary) == set(weight_dictionary), (
            "Gradient and weight dictionaries must cover identical components"
        )
        main_gradient = component_gradient_dictionary[self.main_component_name]
        main_gradient_squared_norm = torch.dot(main_gradient, main_gradient)
        combined_gradient = (
            float(weight_dictionary[self.main_component_name]) * main_gradient
        ).clone()

        # Project Only Conflicting Auxiliary Gradients
        projection_record_dictionary: dict[
            str,
            dict[str, float | bool],
        ] = {}
        for component_name, component_gradient in (
            component_gradient_dictionary.items()
        ):
            if component_name == self.main_component_name:
                continue

            gradient_dot_product = torch.dot(component_gradient, main_gradient)
            component_norm = torch.linalg.vector_norm(component_gradient)
            main_norm = torch.linalg.vector_norm(main_gradient)
            denominator = component_norm * main_norm
            if float(denominator.cpu().item()) <= self.epsilon:
                cosine_before = 0.0
            else:
                cosine_before = float(
                    (gradient_dot_product / denominator).cpu().item()
                )

            projected_gradient = component_gradient
            projection_applied = (
                float(gradient_dot_product.cpu().item()) < 0.0
                and float(main_gradient_squared_norm.cpu().item())
                > self.epsilon
            )
            if projection_applied:
                projected_gradient = component_gradient - (
                    gradient_dot_product
                    / (main_gradient_squared_norm + self.epsilon)
                ) * main_gradient

            projected_norm = torch.linalg.vector_norm(projected_gradient)
            projected_denominator = projected_norm * main_norm
            if float(projected_denominator.cpu().item()) <= self.epsilon:
                cosine_after = 0.0
            else:
                cosine_after = float(
                    (
                        torch.dot(projected_gradient, main_gradient)
                        / projected_denominator
                    )
                    .cpu()
                    .item()
                )

            combined_gradient = combined_gradient + (
                float(weight_dictionary[component_name])
                * projected_gradient
            )
            projection_record_dictionary[component_name] = {
                "projection_applied": projection_applied,
                "cosine_before": cosine_before,
                "cosine_after": cosine_after,
            }

        return combined_gradient, projection_record_dictionary

    def build_diagnostic_record(
        self,
        raw_loss_dictionary: Mapping[str, torch.Tensor],
        shared_parameter_sequence: Sequence[torch.nn.Parameter],
        adapter_name: str,
        optimization_step: int,
    ) -> dict[str, Any]:

        """Build one complete scalar loss-interaction diagnostic record."""

        # Compute Normalized Loss And Functional Gradients
        normalized_loss_dictionary = self.normalize_loss_dictionary(
            raw_loss_dictionary
        )
        loss_ema_dictionary = self.update_loss_ema_dictionary(
            normalized_loss_dictionary
        )
        component_gradient_dictionary = (
            self.compute_component_gradient_dictionary(
                normalized_loss_dictionary,
                shared_parameter_sequence,
            )
        )
        gradient_norm_dictionary = self.compute_gradient_norm_dictionary(
            component_gradient_dictionary
        )
        pairwise_cosine_dictionary = (
            self.compute_pairwise_gradient_cosine_dictionary(
                component_gradient_dictionary
            )
        )
        weight_dictionary = self.resolve_weight_dictionary(
            adapter_name=adapter_name,
            normalized_loss_dictionary=normalized_loss_dictionary,
            gradient_norm_dictionary=gradient_norm_dictionary,
            optimization_step=optimization_step,
        )

        # Convert Tensor Values To Serializable Scalars
        raw_loss_value_dictionary = {
            component_name: float(raw_loss_tensor.detach().cpu().item())
            for component_name, raw_loss_tensor in raw_loss_dictionary.items()
        }
        normalized_loss_value_dictionary = {
            component_name: float(
                normalized_loss_tensor.detach().cpu().item()
            )
            for component_name, normalized_loss_tensor in (
                normalized_loss_dictionary.items()
            )
        }
        activation_multiplier_dictionary = (
            self.resolve_activation_multiplier_dictionary(optimization_step)
        )
        return {
            "optimization_step": int(optimization_step),
            "adapter_name": adapter_name,
            "raw_loss_dictionary": raw_loss_value_dictionary,
            "normalized_loss_dictionary": normalized_loss_value_dictionary,
            "loss_ema_dictionary": loss_ema_dictionary,
            "activation_multiplier_dictionary": (
                activation_multiplier_dictionary
            ),
            "weight_dictionary": weight_dictionary,
            "gradient_norm_dictionary": gradient_norm_dictionary,
            "pairwise_gradient_cosine_dictionary": (
                pairwise_cosine_dictionary
            ),
        }


def capture_trainable_parameter_vector(
    parameter_sequence: Sequence[torch.nn.Parameter],
) -> torch.Tensor:

    """Capture one detached flattened vector of trainable parameters."""

    # Select Trainable Parameters
    active_parameter_list = [
        parameter
        for parameter in parameter_sequence
        if parameter.requires_grad
    ]
    assert active_parameter_list, (
        "At least one parameter must require gradients for vector capture"
    )

    # Flatten Stable Parameter Layout
    return torch.cat(
        [parameter.detach().reshape(-1) for parameter in active_parameter_list]
    ).clone()


def assign_flat_gradient_to_parameters(
    flattened_gradient_tensor: torch.Tensor,
    parameter_sequence: Sequence[torch.nn.Parameter],
) -> None:

    """Assign one flattened gradient vector to trainable parameters.

    Args:
        flattened_gradient_tensor: Gradient vector following parameter order.
        parameter_sequence: Parameters whose `.grad` buffers will be assigned.
    """

    # Select Trainable Parameters And Validate Length
    active_parameter_list = [
        parameter
        for parameter in parameter_sequence
        if parameter.requires_grad
    ]
    expected_element_count = sum(
        parameter.numel() for parameter in active_parameter_list
    )
    assert flattened_gradient_tensor.numel() == expected_element_count, (
        "Flattened gradient length differs from the active parameter layout | "
        f"{flattened_gradient_tensor.numel()} vs {expected_element_count}"
    )

    # Assign Per-Parameter Views
    element_offset = 0
    for parameter in active_parameter_list:
        next_element_offset = element_offset + parameter.numel()
        parameter_gradient = flattened_gradient_tensor[
            element_offset:next_element_offset
        ].reshape_as(parameter)
        parameter.grad = parameter_gradient.detach().clone()
        element_offset = next_element_offset


def compute_update_to_parameter_ratio(
    parameter_vector_before_step: torch.Tensor,
    parameter_vector_after_step: torch.Tensor,
    epsilon: float = DEFAULT_EPSILON,
) -> float:

    """Compute the optimizer update norm divided by parameter norm."""

    # Validate Stable Parameter Layout
    assert parameter_vector_before_step.shape == parameter_vector_after_step.shape, (
        "Before and after parameter vectors must have identical shapes | "
        f"{tuple(parameter_vector_before_step.shape)} vs "
        f"{tuple(parameter_vector_after_step.shape)}"
    )
    assert epsilon > 0.0, f"Epsilon must be positive | {epsilon}"

    # Compute Dimensionless Update Ratio
    update_norm = torch.linalg.vector_norm(
        parameter_vector_after_step - parameter_vector_before_step
    )
    parameter_norm = torch.linalg.vector_norm(parameter_vector_before_step)
    ratio = update_norm / torch.clamp(parameter_norm, min=epsilon)
    return float(ratio.detach().cpu().item())


def configure_deterministic_execution(random_seed: int) -> torch.Generator:

    """Configure deterministic PyTorch execution and return a data generator.

    Notes:
        PyTorch does not guarantee identical results across releases,
        platforms, or CPU/GPU devices. This helper establishes reproducibility
        inside one frozen execution environment.
    """

    # Seed Python And PyTorch
    resolved_random_seed = int(random_seed)
    random.seed(resolved_random_seed)
    torch.manual_seed(resolved_random_seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(resolved_random_seed)

    # Enable Deterministic Kernels
    os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
    torch.use_deterministic_algorithms(True)
    if hasattr(torch.backends, "cudnn"):
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True

    # Return Dedicated Dataloader Generator
    dataloader_generator = torch.Generator()
    dataloader_generator.manual_seed(resolved_random_seed)
    return dataloader_generator


def seed_dataloader_worker(worker_id: int) -> None:

    """Seed Python state for one deterministic dataloader worker."""

    worker_seed = int(torch.initial_seed() % (2**32))
    random.seed(worker_seed + int(worker_id))


def build_deterministic_dataloader(
    dataset: Dataset,
    batch_size: int,
    random_seed: int,
    shuffle: bool = True,
    num_workers: int = 0,
) -> DataLoader:

    """Build a seeded dataloader with an explicit generator.

    Args:
        dataset: PyTorch dataset.
        batch_size: Positive batch size.
        random_seed: Seed assigned to the dataloader generator.
        shuffle: Whether to shuffle the dataset.
        num_workers: Non-negative worker count.

    Returns:
        Deterministically configured dataloader.
    """

    # Validate Loader Configuration
    assert batch_size > 0, f"Batch size must be positive | {batch_size}"
    assert num_workers >= 0, (
        f"Dataloader worker count must be non-negative | {num_workers}"
    )

    # Build Seeded Loader
    dataloader_generator = torch.Generator()
    dataloader_generator.manual_seed(int(random_seed))
    return DataLoader(
        dataset,
        batch_size=int(batch_size),
        shuffle=bool(shuffle),
        num_workers=int(num_workers),
        generator=dataloader_generator,
        worker_init_fn=seed_dataloader_worker,
    )


def _update_fingerprint_from_value(
    fingerprint_hash: Any,
    value: Any,
) -> None:

    """Update a batch fingerprint from nested tensor-compatible values."""

    # Encode Tensor Metadata And Exact Bytes
    if isinstance(value, torch.Tensor):
        detached_tensor = value.detach().cpu().contiguous()
        fingerprint_hash.update(str(detached_tensor.dtype).encode("utf-8"))
        fingerprint_hash.update(str(tuple(detached_tensor.shape)).encode("utf-8"))
        byte_value_list = detached_tensor.view(torch.uint8).reshape(-1).tolist()
        fingerprint_hash.update(bytes(byte_value_list))
        return

    # Encode Nested Containers In Stable Order
    if isinstance(value, Mapping):
        for key in sorted(value):
            fingerprint_hash.update(str(key).encode("utf-8"))
            _update_fingerprint_from_value(fingerprint_hash, value[key])
        return
    if isinstance(value, (list, tuple)):
        for nested_value in value:
            _update_fingerprint_from_value(fingerprint_hash, nested_value)
        return

    # Encode Scalar Fallback
    fingerprint_hash.update(repr(value).encode("utf-8"))


def compute_dataloader_fingerprint(dataloader: DataLoader) -> str:

    """Compute an exact ordered-batch SHA-256 fingerprint."""

    # Hash Every Batch In Iteration Order
    fingerprint_hash = hashlib.sha256()
    for batch_index, batch_value in enumerate(dataloader):
        fingerprint_hash.update(str(batch_index).encode("utf-8"))
        _update_fingerprint_from_value(fingerprint_hash, batch_value)
    return fingerprint_hash.hexdigest()
