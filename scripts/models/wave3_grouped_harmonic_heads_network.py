"""Embryonic Wave 5.1 grouped harmonic-heads TE model."""

from __future__ import annotations

# Import Typing Utilities
from collections.abc import Sequence

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Models
from scripts.models.feedforward_network import FeedForwardNetwork
from scripts.models.harmonic_regression import HarmonicRegression
from scripts.models.temporal_sequence_network import resolve_sequence_readout_tensor


class Wave3GroupedHarmonicHeadsNetwork(nn.Module):

    """Grouped harmonic heads plus residual correction skeleton."""

    def __init__(
        self,
        input_size: int,
        output_size: int = 1,
        harmonic_order: int = 240,
        coefficient_mode: str = "linear_conditioned",
        low_order_harmonic_index_list: Sequence[int] | None = None,
        stable_middle_harmonic_index_list: Sequence[int] | None = None,
        high_order_harmonic_index_list: Sequence[int] | None = None,
        residual_hidden_size: list[int] | None = None,
        residual_activation_name: str = "GELU",
        residual_dropout_probability: float = 0.05,
        residual_use_layer_norm: bool = True,
        low_order_scale: float = 1.0,
        stable_middle_scale: float = 1.0,
        high_order_scale: float = 1.0,
        residual_scale: float = 1.0,
        readout_position: str = "center",
        freeze_harmonic_heads: bool = False,
    ) -> None:
        """Initialize the embryonic grouped-head Wave 5.1 model.

        Args:
            input_size: Input feature count, with angular position in the
                first feature column.
            output_size: Regression target count. The skeleton supports the
                repository's scalar TE target.
            harmonic_order: Contiguous fallback harmonic order.
            coefficient_mode: Harmonic branch coefficient mode.
            low_order_harmonic_index_list: Low-order / offset harmonic group.
            stable_middle_harmonic_index_list: Stable middle harmonic group.
            high_order_harmonic_index_list: High-order fragile harmonic group.
            residual_hidden_size: Residual branch hidden widths.
            residual_activation_name: Residual branch activation name.
            residual_dropout_probability: Residual branch dropout.
            residual_use_layer_norm: Whether the residual branch uses layer
                normalization.
            low_order_scale: Scale applied to the low-order harmonic head.
            stable_middle_scale: Scale applied to the stable middle head.
            high_order_scale: Scale applied to the high-order harmonic head.
            residual_scale: Scale applied to the residual correction head.
            readout_position: Readout position for sequence batches.
            freeze_harmonic_heads: Whether all harmonic heads are frozen.
        """

        super().__init__()

        # Resolve Defaults
        low_order_harmonic_index_list = list(low_order_harmonic_index_list or [0, 1])
        stable_middle_harmonic_index_list = list(stable_middle_harmonic_index_list or [3, 39, 40, 78, 81])
        high_order_harmonic_index_list = list(high_order_harmonic_index_list or [156, 162, 240])
        residual_hidden_size = residual_hidden_size or [96, 64]

        # Validate Parameters
        assert input_size >= 5, f"Input Size must expose TE operating features | {input_size}"
        assert output_size == 1, f"Wave 5.1 grouped heads support scalar TE output only | {output_size}"
        assert harmonic_order > 0, f"Harmonic Order must be positive | {harmonic_order}"
        assert low_order_scale >= 0.0, f"Low Order Scale must be non-negative | {low_order_scale}"
        assert stable_middle_scale >= 0.0, f"Stable Middle Scale must be non-negative | {stable_middle_scale}"
        assert high_order_scale >= 0.0, f"High Order Scale must be non-negative | {high_order_scale}"
        assert residual_scale >= 0.0, f"Residual Scale must be non-negative | {residual_scale}"

        # Save Parameters
        self.input_size = int(input_size)
        self.output_size = int(output_size)
        self.harmonic_order = int(harmonic_order)
        self.coefficient_mode = str(coefficient_mode)
        self.low_order_scale = float(low_order_scale)
        self.stable_middle_scale = float(stable_middle_scale)
        self.high_order_scale = float(high_order_scale)
        self.residual_scale = float(residual_scale)
        self.readout_position = str(readout_position)
        self.freeze_harmonic_heads = bool(freeze_harmonic_heads)

        # Register Harmonic Group Buffers For Stable Diagnostics
        self.register_buffer(
            "low_order_harmonic_index_tensor",
            torch.as_tensor(low_order_harmonic_index_list, dtype=torch.long),
            persistent=True,
        )
        self.register_buffer(
            "stable_middle_harmonic_index_tensor",
            torch.as_tensor(stable_middle_harmonic_index_list, dtype=torch.long),
            persistent=True,
        )
        self.register_buffer(
            "high_order_harmonic_index_tensor",
            torch.as_tensor(high_order_harmonic_index_list, dtype=torch.long),
            persistent=True,
        )

        # Initialize Grouped Harmonic Heads
        self.low_order_head = HarmonicRegression(
            input_size=input_size,
            output_size=output_size,
            harmonic_order=harmonic_order,
            coefficient_mode=coefficient_mode,
            harmonic_index_list=low_order_harmonic_index_list,
        )
        self.stable_middle_head = HarmonicRegression(
            input_size=input_size,
            output_size=output_size,
            harmonic_order=harmonic_order,
            coefficient_mode=coefficient_mode,
            harmonic_index_list=stable_middle_harmonic_index_list,
        )
        self.high_order_head = HarmonicRegression(
            input_size=input_size,
            output_size=output_size,
            harmonic_order=harmonic_order,
            coefficient_mode=coefficient_mode,
            harmonic_index_list=high_order_harmonic_index_list,
        )

        # Optionally Freeze Harmonic Heads
        if self.freeze_harmonic_heads:
            for harmonic_head in [self.low_order_head, self.stable_middle_head, self.high_order_head]:
                for harmonic_parameter in harmonic_head.parameters():
                    harmonic_parameter.requires_grad = False

        # Initialize Residual Shape Head
        self.residual_branch = FeedForwardNetwork(
            input_size=input_size,
            hidden_size=residual_hidden_size,
            output_size=output_size,
            activation_name=residual_activation_name,
            dropout_probability=residual_dropout_probability,
            use_layer_norm=residual_use_layer_norm,
        )

    def resolve_readout_tensor(self, input_tensor: torch.Tensor) -> torch.Tensor:

        """Return point-level features from point or sequence input."""

        if input_tensor.ndim == 2:
            assert input_tensor.shape[-1] == self.input_size, (
                f"Input feature mismatch | {input_tensor.shape[-1]} vs {self.input_size}"
            )
            return input_tensor

        assert input_tensor.ndim == 3, f"Input Tensor must be rank-2 or rank-3 | {tuple(input_tensor.shape)}"
        assert input_tensor.shape[-1] == self.input_size, (
            f"Input feature mismatch | {input_tensor.shape[-1]} vs {self.input_size}"
        )
        return resolve_sequence_readout_tensor(input_tensor, self.readout_position)

    def compute_auxiliary_output_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:

        """Expose grouped harmonic, residual, and combined prediction tensors."""

        # Resolve Point-Level Views
        readout_input_tensor = self.resolve_readout_tensor(input_tensor)
        readout_normalized_input_tensor = self.resolve_readout_tensor(normalized_input_tensor)

        # Compute Grouped Harmonic Heads
        low_order_prediction_tensor = self.low_order_head.forward_with_input_context(
            readout_input_tensor,
            readout_normalized_input_tensor,
        ) * self.low_order_scale
        stable_middle_prediction_tensor = self.stable_middle_head.forward_with_input_context(
            readout_input_tensor,
            readout_normalized_input_tensor,
        ) * self.stable_middle_scale
        high_order_prediction_tensor = self.high_order_head.forward_with_input_context(
            readout_input_tensor,
            readout_normalized_input_tensor,
        ) * self.high_order_scale

        # Compute Residual Shape Correction
        residual_prediction_tensor = self.residual_branch(readout_normalized_input_tensor) * self.residual_scale
        grouped_harmonic_prediction_tensor = (
            low_order_prediction_tensor
            + stable_middle_prediction_tensor
            + high_order_prediction_tensor
        )
        prediction_tensor = grouped_harmonic_prediction_tensor + residual_prediction_tensor

        return {
            "low_order_prediction_tensor": low_order_prediction_tensor,
            "stable_middle_prediction_tensor": stable_middle_prediction_tensor,
            "high_order_prediction_tensor": high_order_prediction_tensor,
            "grouped_harmonic_prediction_tensor": grouped_harmonic_prediction_tensor,
            "residual_prediction_tensor": residual_prediction_tensor,
            "wave3_grouped_residual_prediction_tensor": residual_prediction_tensor,
            "prediction_tensor": prediction_tensor,
        }

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Predict normalized TE using raw angle context and normalized features."""

        return self.compute_auxiliary_output_dictionary(input_tensor, normalized_input_tensor)["prediction_tensor"]

    def forward(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Run inference from normalized inputs when raw context is unavailable."""

        return self.compute_auxiliary_output_dictionary(
            normalized_input_tensor,
            normalized_input_tensor,
        )["prediction_tensor"]
