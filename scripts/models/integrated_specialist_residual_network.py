"""Bounded empirical specialist integration for Wave 5.2R."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn


class IntegratedSpecialistResidualNetwork(nn.Module):
    """Add inspectable, bounded specialist residuals to a frozen K01 curve.

    The module never reconstructs K01 internally. Its inputs are frozen model
    outputs prepared by the campaign runner, which keeps baseline provenance
    separate from the learned residual branches. Every residual is explicitly
    mean-centered, and the H08 branch is deterministically disabled for
    backward records.

    Args:
        condition_feature_mean: Training-only condition mean.
        condition_feature_scale: Training-only condition standard deviation.
        harmonic_order_list: Orders used by the learned shape residual.
        enable_h08_branch: Enable the forward H08 difference branch.
        enable_h04_branch: Enable the H04 analytical-control difference.
        enable_shape_branch: Enable a learned harmonic shape residual.
        enable_condition_branch: Enable the extended condition interaction.
        use_thresholded_condition_library: Use the compact Stage 10 control.
        branch_bound_deg: Maximum absolute contribution of each branch.
    """

    def __init__(
        self,
        condition_feature_mean: torch.Tensor,
        condition_feature_scale: torch.Tensor,
        harmonic_order_list: list[int],
        enable_h08_branch: bool = False,
        enable_h04_branch: bool = False,
        enable_shape_branch: bool = False,
        enable_condition_branch: bool = False,
        use_thresholded_condition_library: bool = False,
        branch_bound_deg: float = 0.02,
    ) -> None:
        """Initialize the explicitly routed residual branches."""

        super().__init__()

        # Validate The Frozen Runtime Contract
        assert condition_feature_mean.ndim == 1
        assert condition_feature_scale.shape == condition_feature_mean.shape
        assert condition_feature_mean.numel() == 4
        assert torch.all(condition_feature_scale > 0.0)
        assert harmonic_order_list
        assert all(order > 0 for order in harmonic_order_list)
        assert branch_bound_deg > 0.0

        # Preserve Inspectable Architecture Flags
        self.enable_h08_branch = bool(enable_h08_branch)
        self.enable_h04_branch = bool(enable_h04_branch)
        self.enable_shape_branch = bool(enable_shape_branch)
        self.enable_condition_branch = bool(enable_condition_branch)
        self.use_thresholded_condition_library = bool(
            use_thresholded_condition_library
        )
        self.branch_bound_deg = float(branch_bound_deg)
        self.harmonic_order_list = list(harmonic_order_list)

        # Register Training-Only Constants As Persistent Export Buffers
        self.register_buffer(
            "condition_feature_mean",
            condition_feature_mean.detach().clone().float(),
        )
        self.register_buffer(
            "condition_feature_scale",
            condition_feature_scale.detach().clone().float(),
        )
        self.register_buffer(
            "harmonic_order_tensor",
            torch.as_tensor(harmonic_order_list, dtype=torch.float32),
        )

        # Build Small PLC-Oriented Branch Heads
        hidden_size = 24
        self.h08_gate_head = nn.Sequential(
            nn.Linear(4, 12),
            nn.Tanh(),
            nn.Linear(12, 1),
        )
        self.h04_gate_head = nn.Sequential(
            nn.Linear(4, 12),
            nn.Tanh(),
            nn.Linear(12, 1),
        )
        self.shape_coefficient_head = nn.Sequential(
            nn.Linear(4, hidden_size),
            nn.Tanh(),
            nn.Linear(hidden_size, 2 * len(harmonic_order_list)),
        )
        condition_library_size = 8 if use_thresholded_condition_library else 16
        self.condition_coefficient_head = nn.Linear(
            condition_library_size,
            2 * len(harmonic_order_list),
        )

        # Start From Exact K01 Replay Before Training
        for module in (
            self.h08_gate_head[-1],
            self.h04_gate_head[-1],
            self.shape_coefficient_head[-1],
            self.condition_coefficient_head,
        ):
            nn.init.zeros_(module.weight)
            nn.init.zeros_(module.bias)

    @staticmethod
    def mean_center(curve_tensor: torch.Tensor) -> torch.Tensor:
        """Remove the per-curve mean without changing tensor shape."""

        assert curve_tensor.ndim == 2
        return curve_tensor - torch.mean(curve_tensor, dim=1, keepdim=True)

    def normalize_condition(
        self,
        condition_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Apply the immutable training-only condition normalization."""

        assert condition_tensor.ndim == 2
        assert condition_tensor.shape[1] == 4
        return (
            condition_tensor - self.condition_feature_mean
        ) / self.condition_feature_scale

    def build_condition_library(
        self,
        normalized_condition: torch.Tensor,
    ) -> torch.Tensor:
        """Build the explicit Stage 10-inspired causal feature library."""

        torque = normalized_condition[:, 0:1]
        speed = normalized_condition[:, 1:2]
        temperature = normalized_condition[:, 2:3]
        direction = normalized_condition[:, 3:4]
        compact_library = torch.cat(
            [
                torque,
                speed,
                temperature,
                direction,
                torque * speed,
                torque * temperature,
                speed * temperature,
                torque * direction,
            ],
            dim=1,
        )
        if self.use_thresholded_condition_library:
            return compact_library
        return torch.cat(
            [
                compact_library,
                speed * direction,
                temperature * direction,
                torque.square(),
                speed.square(),
                temperature.square(),
                torque * speed * temperature,
                torque * speed * direction,
                speed * temperature * direction,
            ],
            dim=1,
        )

    def reconstruct_centered_harmonics(
        self,
        coefficient_tensor: torch.Tensor,
        angular_position_deg: torch.Tensor,
    ) -> torch.Tensor:
        """Reconstruct a zero-mean sine/cosine residual curve."""

        assert coefficient_tensor.ndim == 2
        assert angular_position_deg.ndim == 2
        assert coefficient_tensor.shape[0] == angular_position_deg.shape[0]
        harmonic_angle = (
            angular_position_deg.unsqueeze(-1)
            * (torch.pi / 180.0)
            * self.harmonic_order_tensor.view(1, 1, -1)
        )
        sine_coefficient = coefficient_tensor[:, 0::2].unsqueeze(1)
        cosine_coefficient = coefficient_tensor[:, 1::2].unsqueeze(1)
        curve = torch.sum(
            sine_coefficient * torch.sin(harmonic_angle)
            + cosine_coefficient * torch.cos(harmonic_angle),
            dim=-1,
        )
        return self.mean_center(curve)

    def forward_components(
        self,
        condition_tensor: torch.Tensor,
        angular_position_deg: torch.Tensor,
        k01_curve_tensor: torch.Tensor,
        h08_curve_tensor: torch.Tensor,
        h04_curve_tensor: torch.Tensor,
        direction_flag_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        """Return every routed contribution and the final prediction."""

        assert k01_curve_tensor.shape == angular_position_deg.shape
        assert h08_curve_tensor.shape == k01_curve_tensor.shape
        assert h04_curve_tensor.shape == k01_curve_tensor.shape
        assert direction_flag_tensor.shape == (k01_curve_tensor.shape[0], 1)
        normalized_condition = self.normalize_condition(condition_tensor)
        forward_gate = (direction_flag_tensor > 0.0).to(k01_curve_tensor.dtype)

        # Keep H08 Mean And A0 Out Of The Candidate Path
        h08_difference = self.mean_center(h08_curve_tensor) - self.mean_center(
            k01_curve_tensor
        )
        h08_gate = torch.tanh(self.h08_gate_head(normalized_condition))
        h08_residual = forward_gate * h08_gate * h08_difference
        h08_residual = torch.clamp(
            h08_residual,
            -self.branch_bound_deg,
            self.branch_bound_deg,
        )
        if not self.enable_h08_branch:
            h08_residual = torch.zeros_like(k01_curve_tensor)

        # Expose H04 As A Separate Frozen Analytical Control
        h04_difference = self.mean_center(h04_curve_tensor) - self.mean_center(
            k01_curve_tensor
        )
        h04_gate = torch.tanh(self.h04_gate_head(normalized_condition))
        h04_residual = torch.clamp(
            h04_gate * h04_difference,
            -self.branch_bound_deg,
            self.branch_bound_deg,
        )
        if not self.enable_h04_branch:
            h04_residual = torch.zeros_like(k01_curve_tensor)

        # Reconstruct Learned Shape And Condition Residuals
        shape_coefficient = torch.tanh(
            self.shape_coefficient_head(normalized_condition)
        ) * self.branch_bound_deg
        shape_residual = self.reconstruct_centered_harmonics(
            shape_coefficient,
            angular_position_deg,
        )
        if not self.enable_shape_branch:
            shape_residual = torch.zeros_like(k01_curve_tensor)

        condition_library = self.build_condition_library(normalized_condition)
        condition_coefficient = torch.tanh(
            self.condition_coefficient_head(condition_library)
        ) * self.branch_bound_deg
        condition_residual = self.reconstruct_centered_harmonics(
            condition_coefficient,
            angular_position_deg,
        )
        if not self.enable_condition_branch:
            condition_residual = torch.zeros_like(k01_curve_tensor)

        final_prediction = (
            k01_curve_tensor
            + h08_residual
            + h04_residual
            + shape_residual
            + condition_residual
        )
        return {
            "k01_baseline_curve": k01_curve_tensor,
            "k01_mean": torch.mean(k01_curve_tensor, dim=1, keepdim=True),
            "k01_centered_curve": self.mean_center(k01_curve_tensor),
            "forward_gate": forward_gate,
            "h08_centered_residual": h08_residual,
            "h04_centered_residual": h04_residual,
            "learned_shape_residual": shape_residual,
            "condition_interaction_residual": condition_residual,
            "prediction_curve": final_prediction,
        }

    def forward(
        self,
        condition_tensor: torch.Tensor,
        angular_position_deg: torch.Tensor,
        k01_curve_tensor: torch.Tensor,
        h08_curve_tensor: torch.Tensor,
        h04_curve_tensor: torch.Tensor,
        direction_flag_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Return the tensor-only final prediction for export tooling."""

        return self.forward_components(
            condition_tensor,
            angular_position_deg,
            k01_curve_tensor,
            h08_curve_tensor,
            h04_curve_tensor,
            direction_flag_tensor,
        )["prediction_curve"]
