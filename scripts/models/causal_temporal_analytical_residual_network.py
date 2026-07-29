"""Causal temporal analytical-residual networks for Wave 5.2R Stage 9."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn


class CausalTemporalAnalyticalResidualNetwork(nn.Module):

    """Predict causal point or coefficient residuals above one frozen anchor.

    Args:
        condition_feature_mean: Training-only mean for speed, torque, and
            temperature.
        condition_feature_scale: Training-only standard deviation for speed,
            torque, and temperature.
        harmonic_order_list: Positive angular orders exposed to the GRU.
        hidden_size: GRU hidden width.
        num_layers: Number of stacked unidirectional GRU layers.
        residual_mode: `point` or `coefficient`.
        point_residual_bound_deg: Absolute point-residual bound.
        coefficient_residual_bound: Optional per-coefficient bounds.
        use_bounded_output: Whether to apply a hyperbolic-tangent bound.
    """

    def __init__(
        self,
        condition_feature_mean: torch.Tensor,
        condition_feature_scale: torch.Tensor,
        harmonic_order_list: list[int],
        hidden_size: int = 48,
        num_layers: int = 1,
        residual_mode: str = "point",
        point_residual_bound_deg: float = 0.025,
        coefficient_residual_bound: torch.Tensor | None = None,
        use_bounded_output: bool = True,
    ) -> None:
        """Initialize one causal analytical-residual GRU."""

        super().__init__()

        # Validate Architecture Inputs
        normalized_residual_mode = residual_mode.strip().lower()
        assert normalized_residual_mode in {"point", "coefficient"}, (
            f"Unsupported residual mode | {residual_mode}"
        )
        assert condition_feature_mean.ndim == 1
        assert condition_feature_scale.shape == condition_feature_mean.shape
        assert condition_feature_mean.numel() == 3
        assert torch.all(condition_feature_scale > 0.0)
        assert hidden_size > 0
        assert num_layers > 0
        assert harmonic_order_list
        assert all(order > 0 for order in harmonic_order_list)
        assert point_residual_bound_deg > 0.0

        # Save Immutable Architecture Fields
        self.harmonic_order_list = list(harmonic_order_list)
        self.hidden_size = int(hidden_size)
        self.num_layers = int(num_layers)
        self.residual_mode = normalized_residual_mode
        self.point_residual_bound_deg = float(point_residual_bound_deg)
        self.use_bounded_output = bool(use_bounded_output)

        # Register Training-Only Normalization And Harmonic Buffers
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

        # Resolve Output Contract
        if self.residual_mode == "coefficient":
            assert coefficient_residual_bound is not None
            assert coefficient_residual_bound.ndim == 1
            expected_coefficient_count = 1 + (2 * len(harmonic_order_list))
            assert coefficient_residual_bound.numel() == (
                expected_coefficient_count
            )
            assert torch.all(coefficient_residual_bound > 0.0)
            self.register_buffer(
                "coefficient_residual_bound",
                coefficient_residual_bound.detach().clone().float(),
            )
            output_size = expected_coefficient_count
        else:
            self.register_buffer(
                "coefficient_residual_bound",
                torch.empty(0, dtype=torch.float32),
            )
            output_size = 1

        # Build Explicit Unidirectional GRU
        angular_feature_count = 1 + (2 * len(harmonic_order_list))
        input_size = angular_feature_count + condition_feature_mean.numel()
        self.input_size = int(input_size)
        self.output_size = int(output_size)
        self.recurrent_network = nn.GRU(
            input_size=self.input_size,
            hidden_size=self.hidden_size,
            num_layers=self.num_layers,
            batch_first=True,
            dropout=0.0,
            bidirectional=False,
        )
        self.output_layer = nn.Linear(self.hidden_size, self.output_size)
        nn.init.zeros_(self.output_layer.weight)
        nn.init.zeros_(self.output_layer.bias)

    def initial_hidden_state(
        self,
        batch_size: int,
        reference_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Return an explicit zero hidden state for one curve batch."""

        assert batch_size > 0
        return reference_tensor.new_zeros(
            (self.num_layers, batch_size, self.hidden_size)
        )

    def build_angular_feature_tensor(
        self,
        angular_position_deg: torch.Tensor,
    ) -> torch.Tensor:
        """Build raw and periodic causal angular features."""

        assert angular_position_deg.ndim == 2
        angle_rad = angular_position_deg.unsqueeze(-1) * (
            torch.pi / 180.0
        )
        order_tensor = self.harmonic_order_tensor.view(1, 1, -1)
        harmonic_angle_tensor = angle_rad * order_tensor
        normalized_angle = (
            angular_position_deg.unsqueeze(-1) / 180.0
        ) - 1.0
        return torch.cat(
            [
                normalized_angle,
                torch.sin(harmonic_angle_tensor),
                torch.cos(harmonic_angle_tensor),
            ],
            dim=-1,
        )

    def build_input_feature_tensor(
        self,
        angular_position_deg: torch.Tensor,
        condition_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Combine causal angular features and repeated setpoints."""

        assert angular_position_deg.ndim == 2
        assert condition_tensor.ndim == 2
        assert condition_tensor.shape[0] == angular_position_deg.shape[0]
        assert condition_tensor.shape[1] == 3
        normalized_condition = (
            condition_tensor - self.condition_feature_mean
        ) / self.condition_feature_scale
        repeated_condition = normalized_condition.unsqueeze(1).expand(
            -1,
            angular_position_deg.shape[1],
            -1,
        )
        return torch.cat(
            [
                self.build_angular_feature_tensor(angular_position_deg),
                repeated_condition,
            ],
            dim=-1,
        )

    def reconstruct_current_harmonic_value(
        self,
        coefficient_tensor: torch.Tensor,
        angular_position_deg: torch.Tensor,
    ) -> torch.Tensor:
        """Reconstruct current values from causal coefficient estimates."""

        assert coefficient_tensor.ndim == 3
        assert angular_position_deg.shape == coefficient_tensor.shape[:2]
        angle_rad = angular_position_deg.unsqueeze(-1) * (
            torch.pi / 180.0
        )
        order_tensor = self.harmonic_order_tensor.view(1, 1, -1)
        harmonic_angle_tensor = angle_rad * order_tensor
        sine_coefficient = coefficient_tensor[..., 1::2]
        cosine_coefficient = coefficient_tensor[..., 2::2]
        reconstruction = coefficient_tensor[..., 0:1]
        reconstruction = reconstruction + torch.sum(
            sine_coefficient * torch.sin(harmonic_angle_tensor)
            + cosine_coefficient * torch.cos(harmonic_angle_tensor),
            dim=-1,
            keepdim=True,
        )
        return reconstruction

    def forward_sequence(
        self,
        angular_position_deg: torch.Tensor,
        condition_tensor: torch.Tensor,
        anchor_curve_tensor: torch.Tensor,
        anchor_coefficient_tensor: torch.Tensor | None = None,
        hidden_state_tensor: torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:
        """Predict one contiguous causal sequence and final hidden state."""

        assert anchor_curve_tensor.shape == angular_position_deg.shape
        batch_size = angular_position_deg.shape[0]
        if hidden_state_tensor is None:
            hidden_state_tensor = self.initial_hidden_state(
                batch_size,
                angular_position_deg,
            )
        input_feature_tensor = self.build_input_feature_tensor(
            angular_position_deg,
            condition_tensor,
        )
        recurrent_output, final_hidden_state = self.recurrent_network(
            input_feature_tensor,
            hidden_state_tensor,
        )
        raw_output = self.output_layer(recurrent_output)

        if self.residual_mode == "coefficient":
            assert anchor_coefficient_tensor is not None
            assert anchor_coefficient_tensor.ndim == 2
            assert anchor_coefficient_tensor.shape == (
                batch_size,
                self.output_size,
            )
            if self.use_bounded_output:
                coefficient_correction = torch.tanh(raw_output) * (
                    self.coefficient_residual_bound.view(1, 1, -1)
                )
            else:
                coefficient_correction = raw_output
            predicted_coefficient = (
                anchor_coefficient_tensor.unsqueeze(1)
                + coefficient_correction
            )
            prediction = self.reconstruct_current_harmonic_value(
                predicted_coefficient,
                angular_position_deg,
            )
            residual = prediction - anchor_curve_tensor.unsqueeze(-1)
        else:
            if self.use_bounded_output:
                residual = torch.tanh(raw_output) * (
                    self.point_residual_bound_deg
                )
            else:
                residual = raw_output
            prediction = anchor_curve_tensor.unsqueeze(-1) + residual
            coefficient_correction = raw_output.new_empty(
                (*raw_output.shape[:2], 0)
            )
            predicted_coefficient = coefficient_correction

        return {
            "prediction_curve": prediction.squeeze(-1),
            "residual_curve": residual.squeeze(-1),
            "coefficient_correction": coefficient_correction,
            "predicted_coefficient": predicted_coefficient,
            "final_hidden_state": final_hidden_state,
            "hidden_sequence": recurrent_output,
        }

    def forward_in_chunks(
        self,
        angular_position_deg: torch.Tensor,
        condition_tensor: torch.Tensor,
        anchor_curve_tensor: torch.Tensor,
        anchor_coefficient_tensor: torch.Tensor | None = None,
        chunk_length: int = 33,
        detach_hidden_between_chunks: bool = False,
    ) -> dict[str, torch.Tensor]:
        """Predict a curve in contiguous chunks with explicit state carry."""

        assert chunk_length > 0
        hidden_state = self.initial_hidden_state(
            angular_position_deg.shape[0],
            angular_position_deg,
        )
        output_list: list[dict[str, torch.Tensor]] = []
        for start_index in range(
            0,
            angular_position_deg.shape[1],
            chunk_length,
        ):
            end_index = min(
                start_index + chunk_length,
                angular_position_deg.shape[1],
            )
            chunk_output = self.forward_sequence(
                angular_position_deg[:, start_index:end_index],
                condition_tensor,
                anchor_curve_tensor[:, start_index:end_index],
                anchor_coefficient_tensor,
                hidden_state,
            )
            output_list.append(chunk_output)
            hidden_state = chunk_output["final_hidden_state"]
            if detach_hidden_between_chunks:
                hidden_state = hidden_state.detach()

        return {
            "prediction_curve": torch.cat(
                [item["prediction_curve"] for item in output_list],
                dim=1,
            ),
            "residual_curve": torch.cat(
                [item["residual_curve"] for item in output_list],
                dim=1,
            ),
            "coefficient_correction": torch.cat(
                [item["coefficient_correction"] for item in output_list],
                dim=1,
            ),
            "predicted_coefficient": torch.cat(
                [item["predicted_coefficient"] for item in output_list],
                dim=1,
            ),
            "final_hidden_state": hidden_state,
            "hidden_sequence": torch.cat(
                [item["hidden_sequence"] for item in output_list],
                dim=1,
            ),
        }

    def forward(
        self,
        angular_position_deg: torch.Tensor,
        condition_tensor: torch.Tensor,
        anchor_curve_tensor: torch.Tensor,
        anchor_coefficient_tensor: torch.Tensor | None = None,
    ) -> torch.Tensor:
        """Predict one full causal sequence from an explicit zero state."""

        return self.forward_sequence(
            angular_position_deg,
            condition_tensor,
            anchor_curve_tensor,
            anchor_coefficient_tensor,
        )["prediction_curve"]
