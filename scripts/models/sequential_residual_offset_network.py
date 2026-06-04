"""Sequential residual-offset network for Track 2F TE probes."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Models
from scripts.models.feedforward_network import FeedForwardNetwork
from scripts.models.temporal_sequence_network import RecurrentSequenceNetwork
from scripts.models.temporal_sequence_network import resolve_sequence_readout_tensor


class SequentialResidualOffsetNetwork(nn.Module):

    """Causal-input TE model with point base prediction plus residual offset."""

    def __init__(
        self,
        input_size: int,
        output_size: int = 1,
        base_hidden_size: list[int] | None = None,
        base_activation_name: str = "GELU",
        base_dropout_probability: float = 0.05,
        base_use_layer_norm: bool = True,
        offset_hidden_size: int = 96,
        offset_num_layers: int = 2,
        offset_dropout_probability: float = 0.10,
        offset_bidirectional: bool = False,
        offset_readout_position: str = "center",
        offset_scale: float = 1.0,
    ) -> None:
        """Initialize the sequential residual-offset probe.

        Args:
            input_size: Raw point/sequence feature count.
            output_size: Regression target count.
            base_hidden_size: Hidden layers for the point readout branch.
            base_activation_name: Activation used by the point branch.
            base_dropout_probability: Dropout probability used by the point
                branch.
            base_use_layer_norm: Whether the point branch uses layer norm.
            offset_hidden_size: Recurrent hidden size for the residual-offset
                branch.
            offset_num_layers: Recurrent layer count for the offset branch.
            offset_dropout_probability: Dropout probability used by the offset
                branch.
            offset_bidirectional: Whether the offset branch is bidirectional.
                Track 2F campaign YAML should keep this disabled for causal
                deployment discipline.
            offset_readout_position: Sequence readout position for both
                branches.
            offset_scale: Multiplicative scale applied to the residual-offset
                branch before summing with the base prediction.
        """

        super().__init__()

        # Validate Architecture Parameters
        assert input_size >= 5, f"Input Size must expose TE operating features | {input_size}"
        assert output_size > 0, f"Output Size must be positive | {output_size}"
        assert offset_hidden_size > 0, f"Offset Hidden Size must be positive | {offset_hidden_size}"
        assert offset_num_layers > 0, f"Offset Num Layers must be positive | {offset_num_layers}"
        assert offset_scale > 0.0, f"Offset Scale must be positive | {offset_scale}"

        # Save Architecture Parameters
        self.input_size = input_size
        self.output_size = output_size
        self.base_hidden_size = list(base_hidden_size or [96, 64])
        self.offset_hidden_size = offset_hidden_size
        self.offset_num_layers = offset_num_layers
        self.offset_dropout_probability = offset_dropout_probability
        self.offset_bidirectional = offset_bidirectional
        self.offset_readout_position = offset_readout_position
        self.offset_scale = float(offset_scale)

        # Build Point-Level Base Branch At The Sequence Readout Position
        self.base_branch = FeedForwardNetwork(
            input_size=input_size,
            hidden_size=self.base_hidden_size,
            output_size=output_size,
            activation_name=base_activation_name,
            dropout_probability=base_dropout_probability,
            use_layer_norm=base_use_layer_norm,
        )

        # Build Sequential Residual-Offset Branch
        self.residual_offset_branch = RecurrentSequenceNetwork(
            recurrent_type="gru",
            input_size=input_size,
            hidden_size=offset_hidden_size,
            output_size=output_size,
            num_layers=offset_num_layers,
            dropout_probability=offset_dropout_probability,
            bidirectional=offset_bidirectional,
            readout_position=offset_readout_position,
        )

    def resolve_readout_feature_tensor(self, sequence_tensor: torch.Tensor) -> torch.Tensor:

        """Extract the point feature tensor used by the base branch."""

        # Validate Sequence Tensor
        assert sequence_tensor.ndim == 3, f"Sequence Tensor must be rank-3 | {tuple(sequence_tensor.shape)}"
        assert sequence_tensor.shape[-1] == self.input_size, (
            f"Input feature mismatch | {sequence_tensor.shape[-1]} vs {self.input_size}"
        )

        return resolve_sequence_readout_tensor(sequence_tensor, self.offset_readout_position)

    def compute_auxiliary_output_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:

        """Expose base, residual-offset, and final prediction tensors."""

        # Validate Sequence Inputs
        assert input_tensor.ndim == 3, f"Input Tensor must be rank-3 | {tuple(input_tensor.shape)}"
        assert normalized_input_tensor.ndim == 3, (
            f"Normalized Input Tensor must be rank-3 | {tuple(normalized_input_tensor.shape)}"
        )
        assert input_tensor.shape == normalized_input_tensor.shape, (
            f"Raw and normalized sequence shapes must match | {tuple(input_tensor.shape)} vs "
            f"{tuple(normalized_input_tensor.shape)}"
        )

        # Compute Base Prediction From The Current Readout State
        readout_normalized_input_tensor = self.resolve_readout_feature_tensor(normalized_input_tensor)
        base_prediction_tensor = self.base_branch(readout_normalized_input_tensor)

        # Compute Residual Offset From The Causal Sequence Window
        residual_offset_prediction_tensor = self.residual_offset_branch(normalized_input_tensor) * self.offset_scale
        final_prediction_tensor = base_prediction_tensor + residual_offset_prediction_tensor

        return {
            "base_prediction_tensor": base_prediction_tensor,
            "residual_offset_prediction_tensor": residual_offset_prediction_tensor,
            "prediction_tensor": final_prediction_tensor,
        }

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Predict normalized TE from point base plus sequential offset."""

        return self.compute_auxiliary_output_dictionary(input_tensor, normalized_input_tensor)["prediction_tensor"]

    def forward(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Run inference from normalized sequence inputs."""

        return self.compute_auxiliary_output_dictionary(
            normalized_input_tensor,
            normalized_input_tensor,
        )["prediction_tensor"]
