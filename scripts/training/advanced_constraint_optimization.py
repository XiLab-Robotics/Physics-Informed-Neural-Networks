"""Advanced optimization helpers for Wave 5.2R Stage 12."""

from __future__ import annotations

# Import Python Utilities
from dataclasses import dataclass
from typing import Mapping

# Import PyTorch Utilities
import torch


@dataclass
class AugmentedLagrangianState:
    """Track bounded multipliers for two inequality constraints."""

    closure_multiplier: float = 0.0
    correction_multiplier: float = 0.0
    penalty: float = 1.0
    maximum_multiplier: float = 20.0
    maximum_penalty: float = 20.0

    def compose_loss(
        self,
        closure_violation: torch.Tensor,
        correction_violation: torch.Tensor,
    ) -> torch.Tensor:
        """Compose the differentiable augmented-Lagrangian contribution."""

        assert closure_violation.numel() == 1
        assert correction_violation.numel() == 1
        return (
            self.closure_multiplier * closure_violation
            + 0.5 * self.penalty * closure_violation.square()
            + self.correction_multiplier * correction_violation
            + 0.5 * self.penalty * correction_violation.square()
        )

    def update(
        self,
        closure_violation_value: float,
        correction_violation_value: float,
    ) -> None:
        """Update multipliers from detached training-only violations."""

        self.closure_multiplier = min(
            self.maximum_multiplier,
            max(
                0.0,
                self.closure_multiplier
                + self.penalty * closure_violation_value,
            ),
        )
        self.correction_multiplier = min(
            self.maximum_multiplier,
            max(
                0.0,
                self.correction_multiplier
                + self.penalty * correction_violation_value,
            ),
        )
        if max(closure_violation_value, correction_violation_value) > 0.0:
            self.penalty = min(self.maximum_penalty, self.penalty * 1.10)

    def to_payload(self) -> dict[str, float]:
        """Return a serialization-safe state record."""

        return {
            "closure_multiplier": self.closure_multiplier,
            "correction_multiplier": self.correction_multiplier,
            "penalty": self.penalty,
        }


class AdaptiveCurveWeightState:
    """Maintain bounded training-curve emphasis without test information."""

    def __init__(
        self,
        curve_count: int,
        minimum_weight: float = 0.50,
        maximum_weight: float = 2.00,
        update_rate: float = 0.20,
    ) -> None:
        """Initialize uniform deterministic weights."""

        assert curve_count > 0
        assert 0.0 < minimum_weight <= 1.0 <= maximum_weight
        assert 0.0 < update_rate <= 1.0
        self.minimum_weight = float(minimum_weight)
        self.maximum_weight = float(maximum_weight)
        self.update_rate = float(update_rate)
        self.weight_tensor = torch.ones(curve_count, dtype=torch.float64)

    def update(
        self,
        curve_index_tensor: torch.Tensor,
        detached_curve_loss_tensor: torch.Tensor,
    ) -> None:
        """Apply a multiplicative hard-example update to observed curves."""

        index_cpu = curve_index_tensor.detach().cpu().long()
        loss_cpu = detached_curve_loss_tensor.detach().cpu().double()
        normalized_loss = loss_cpu / max(
            float(torch.mean(loss_cpu).item()),
            1.0e-12,
        )
        target_weight = torch.clamp(
            normalized_loss,
            min=self.minimum_weight,
            max=self.maximum_weight,
        )
        old_weight = self.weight_tensor.index_select(0, index_cpu)
        updated_weight = (
            (1.0 - self.update_rate) * old_weight
            + self.update_rate * target_weight
        )
        self.weight_tensor.index_copy_(0, index_cpu, updated_weight)
        self.weight_tensor /= torch.mean(self.weight_tensor)
        self.weight_tensor.clamp_(
            min=self.minimum_weight,
            max=self.maximum_weight,
        )

    def batch_weights(
        self,
        curve_index_tensor: torch.Tensor,
        device: torch.device,
    ) -> torch.Tensor:
        """Return normalized weights for one batch."""

        weights = self.weight_tensor.index_select(
            0,
            curve_index_tensor.detach().cpu().long(),
        ).to(device=device, dtype=torch.float32)
        return weights / torch.mean(weights)

    def deterministic_sample_indices(
        self,
        sample_count: int,
        generator: torch.Generator,
    ) -> torch.Tensor:
        """Draw a deterministic weighted epoch with replacement."""

        assert sample_count > 0
        return torch.multinomial(
            self.weight_tensor,
            sample_count,
            replacement=True,
            generator=generator,
        )

    def effective_sample_size(self) -> float:
        """Return the standard importance-weight effective sample size."""

        normalized_weight = self.weight_tensor / torch.sum(self.weight_tensor)
        return float(1.0 / torch.sum(normalized_weight.square()).item())

    def to_payload(self) -> dict[str, float]:
        """Return scalar diagnostics for persistence."""

        return {
            "minimum_weight": float(torch.min(self.weight_tensor).item()),
            "maximum_weight": float(torch.max(self.weight_tensor).item()),
            "effective_sample_size": self.effective_sample_size(),
        }


def build_loss_component_dictionary(
    prediction_tensor: torch.Tensor,
    target_tensor: torch.Tensor,
    residual_tensor: torch.Tensor,
    coefficient_correction_tensor: torch.Tensor,
    curve_weight_tensor: torch.Tensor | None = None,
) -> tuple[dict[str, torch.Tensor], torch.Tensor]:
    """Build raw, mean, shape, closure, and correction loss components."""

    assert prediction_tensor.shape == target_tensor.shape
    point_error = torch.abs(prediction_tensor - target_tensor)
    per_curve_raw_loss = torch.mean(point_error, dim=1)
    if curve_weight_tensor is None:
        raw_loss = torch.mean(per_curve_raw_loss)
    else:
        assert curve_weight_tensor.shape == per_curve_raw_loss.shape
        raw_loss = torch.mean(per_curve_raw_loss * curve_weight_tensor)

    prediction_mean = torch.mean(prediction_tensor, dim=1, keepdim=True)
    target_mean = torch.mean(target_tensor, dim=1, keepdim=True)
    mean_loss = torch.mean(torch.abs(prediction_mean - target_mean))
    shape_loss = torch.mean(
        torch.abs(
            (prediction_tensor - prediction_mean)
            - (target_tensor - target_mean)
        )
    )

    residual_closure = residual_tensor[:, -1] - residual_tensor[:, 0]
    closure_loss = torch.mean(torch.abs(residual_closure))
    if coefficient_correction_tensor.numel() == 0:
        correction_rms = torch.sqrt(
            torch.mean(residual_tensor.square()) + 1.0e-12
        )
    else:
        correction_rms = torch.sqrt(
            torch.mean(coefficient_correction_tensor.square()) + 1.0e-12
        )

    return (
        {
            "raw": raw_loss,
            "mean": mean_loss,
            "shape": shape_loss,
            "closure": closure_loss,
            "correction": correction_rms,
        },
        per_curve_raw_loss,
    )


def summarize_gradient_conflicts(
    cosine_dictionary: Mapping[str, float],
) -> dict[str, float]:
    """Summarize the frequency and magnitude of negative gradient cosines."""

    cosine_value_list = list(cosine_dictionary.values())
    if not cosine_value_list:
        return {
            "negative_fraction": 0.0,
            "minimum_cosine": 0.0,
            "mean_cosine": 0.0,
        }
    negative_count = sum(value < 0.0 for value in cosine_value_list)
    return {
        "negative_fraction": negative_count / len(cosine_value_list),
        "minimum_cosine": min(cosine_value_list),
        "mean_cosine": sum(cosine_value_list) / len(cosine_value_list),
    }
