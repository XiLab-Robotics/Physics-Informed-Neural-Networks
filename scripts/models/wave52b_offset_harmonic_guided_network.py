"""Wave 5.2B offset and harmonic guided TE regression backbone."""

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


class Wave52BOffsetHarmonicGuidedNetwork(nn.Module):

    """Point-readout TE model with explicit base, offset, and harmonic heads."""

    def __init__(
        self,
        input_size: int,
        output_size: int = 1,
        base_hidden_size: Sequence[int] | None = None,
        offset_hidden_size: Sequence[int] | None = None,
        activation_name: str = "GELU",
        dropout_probability: float = 0.05,
        use_layer_norm: bool = True,
        offset_scale: float = 1.0,
        harmonic_scale: float = 0.0,
        harmonic_order: int = 240,
        coefficient_mode: str = "linear_conditioned",
        harmonic_index_list: Sequence[int] | None = None,
        readout_position: str = "center",
        freeze_harmonic_branch: bool = False,
    ) -> None:
        """Initialize the Wave 5.2B guided regression backbone.

        Args:
            input_size: Input feature count exposed by the TE datamodule.
            output_size: Regression target count. Wave 5.2B uses the scalar TE
                target.
            base_hidden_size: Hidden widths for the direct prediction branch.
            offset_hidden_size: Hidden widths for the residual offset branch.
            activation_name: Feedforward activation name.
            dropout_probability: Dropout probability for both dense branches.
            use_layer_norm: Whether dense branches use layer normalization.
            offset_scale: Multiplicative scale applied to the offset branch.
            harmonic_scale: Multiplicative scale applied to the harmonic branch.
            harmonic_order: Contiguous harmonic order fallback.
            coefficient_mode: Harmonic coefficient parameterization.
            harmonic_index_list: Optional sparse harmonic index list.
            readout_position: Sequence readout position when batches are rank-3.
            freeze_harmonic_branch: Whether the harmonic branch is frozen.
        """

        super().__init__()

        # Resolve Defaults
        base_hidden_size = list(base_hidden_size or [128, 96, 64])
        offset_hidden_size = list(offset_hidden_size or [64, 32])
        harmonic_index_list = list(harmonic_index_list or [0, 1, 3, 39, 40, 78, 81, 156, 162, 240])

        # Validate Architecture Parameters
        assert input_size >= 4, f"Input Size must expose angle and operating features | {input_size}"
        assert output_size == 1, f"Wave 5.2B supports scalar TE output only | {output_size}"
        assert offset_scale >= 0.0, f"Offset Scale must be non-negative | {offset_scale}"
        assert harmonic_scale >= 0.0, f"Harmonic Scale must be non-negative | {harmonic_scale}"
        assert harmonic_order > 0, f"Harmonic Order must be positive | {harmonic_order}"

        # Save Architecture Parameters
        self.input_size = int(input_size)
        self.output_size = int(output_size)
        self.offset_scale = float(offset_scale)
        self.harmonic_scale = float(harmonic_scale)
        self.harmonic_order = int(harmonic_order)
        self.coefficient_mode = str(coefficient_mode)
        self.readout_position = str(readout_position)
        self.freeze_harmonic_branch = bool(freeze_harmonic_branch)

        # Register Harmonic Metadata For Diagnostics
        self.register_buffer("harmonic_index_tensor", torch.as_tensor(harmonic_index_list, dtype=torch.long), persistent=True)

        # Initialize Direct And Offset Branches
        self.base_branch = FeedForwardNetwork(
            input_size=input_size,
            hidden_size=list(base_hidden_size),
            output_size=output_size,
            activation_name=activation_name,
            dropout_probability=dropout_probability,
            use_layer_norm=use_layer_norm,
        )
        self.offset_branch = FeedForwardNetwork(
            input_size=input_size,
            hidden_size=list(offset_hidden_size),
            output_size=output_size,
            activation_name=activation_name,
            dropout_probability=dropout_probability,
            use_layer_norm=use_layer_norm,
        )

        # Initialize Optional Harmonic Guidance Branch
        self.harmonic_branch = HarmonicRegression(
            input_size=input_size,
            output_size=output_size,
            harmonic_order=harmonic_order,
            coefficient_mode=coefficient_mode,
            harmonic_index_list=harmonic_index_list,
        )
        if self.freeze_harmonic_branch:
            for harmonic_parameter in self.harmonic_branch.parameters():
                harmonic_parameter.requires_grad = False

    def resolve_readout_tensor(self, input_tensor: torch.Tensor) -> torch.Tensor:

        """Resolve point-level features from point or sequence input."""

        # Return Point Batch Directly
        if input_tensor.ndim == 2:
            assert input_tensor.shape[-1] == self.input_size, (
                f"Input feature mismatch | {input_tensor.shape[-1]} vs {self.input_size}"
            )
            return input_tensor

        # Extract Configured Sequence Readout
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

        """Expose final prediction and all guided-branch diagnostics."""

        # Resolve Point-Level Views
        readout_input_tensor = self.resolve_readout_tensor(input_tensor)
        readout_normalized_input_tensor = self.resolve_readout_tensor(normalized_input_tensor)

        # Compute Branch Predictions
        base_prediction_tensor = self.base_branch(readout_normalized_input_tensor)
        residual_offset_prediction_tensor = self.offset_branch(readout_normalized_input_tensor) * self.offset_scale
        harmonic_prediction_tensor = self.harmonic_branch.forward_with_input_context(
            readout_input_tensor,
            readout_normalized_input_tensor,
        ) * self.harmonic_scale
        prediction_tensor = base_prediction_tensor + residual_offset_prediction_tensor + harmonic_prediction_tensor

        return {
            "base_prediction_tensor": base_prediction_tensor,
            "residual_offset_prediction_tensor": residual_offset_prediction_tensor,
            "structured_prediction_tensor": harmonic_prediction_tensor,
            "wave52b_harmonic_prediction_tensor": harmonic_prediction_tensor,
            "prediction_tensor": prediction_tensor,
        }

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Predict normalized TE using raw angle context and normalized inputs."""

        return self.compute_auxiliary_output_dictionary(input_tensor, normalized_input_tensor)["prediction_tensor"]

    def forward(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Run inference from normalized inputs when raw context is unavailable."""

        return self.compute_auxiliary_output_dictionary(
            normalized_input_tensor,
            normalized_input_tensor,
        )["prediction_tensor"]
