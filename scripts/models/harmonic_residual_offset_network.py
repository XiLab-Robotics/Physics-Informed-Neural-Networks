"""Harmonic shape plus causal residual-offset network for Track 2F-bis."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Models
from scripts.models.harmonic_regression import HarmonicRegression
from scripts.models.temporal_sequence_network import RecurrentSequenceNetwork
from scripts.models.temporal_sequence_network import resolve_sequence_readout_tensor


class HarmonicResidualOffsetNetwork(nn.Module):

    """TE model with structured harmonic shape plus causal offset correction."""

    def __init__(
        self,
        input_size: int,
        output_size: int = 1,
        harmonic_order: int = 12,
        coefficient_mode: str = "linear_conditioned",
        harmonic_index_list: list[int] | None = None,
        offset_hidden_size: int = 96,
        offset_num_layers: int = 2,
        offset_dropout_probability: float = 0.10,
        offset_bidirectional: bool = False,
        offset_readout_position: str = "center",
        offset_scale: float = 1.0,
        freeze_structured_branch: bool = False,
    ) -> None:
        """Initialize the harmonic residual-offset probe.

        Args:
            input_size: Raw sequence feature count, including angular position
                as the first feature.
            output_size: Regression target count.
            harmonic_order: Contiguous harmonic order used when no explicit
                harmonic index list is provided.
            coefficient_mode: Harmonic coefficient parameterization mode.
            harmonic_index_list: Optional explicit harmonic list. `0` keeps
                the existing `DC` convention and positive entries create
                sine/cosine pairs.
            offset_hidden_size: Recurrent hidden size for the residual-offset
                branch.
            offset_num_layers: Recurrent layer count for the residual-offset
                branch.
            offset_dropout_probability: Dropout probability used by the
                residual-offset branch.
            offset_bidirectional: Whether the residual-offset branch is
                bidirectional. Deployable Track 2F-bis runs should keep this
                disabled.
            offset_readout_position: Sequence readout position used by both
                branches.
            offset_scale: Multiplicative scale applied to the residual-offset
                branch before summing with the harmonic prediction.
            freeze_structured_branch: Whether to freeze the harmonic branch
                parameters during optimization.
        """

        super().__init__()

        # Validate Architecture Parameters
        assert input_size >= 5, f"Input Size must expose TE operating features | {input_size}"
        assert output_size == 1, f"Harmonic residual-offset supports scalar TE output only | {output_size}"
        assert harmonic_order > 0, f"Harmonic Order must be positive | {harmonic_order}"
        assert offset_hidden_size > 0, f"Offset Hidden Size must be positive | {offset_hidden_size}"
        assert offset_num_layers > 0, f"Offset Num Layers must be positive | {offset_num_layers}"
        assert offset_scale > 0.0, f"Offset Scale must be positive | {offset_scale}"

        # Save Architecture Parameters
        self.input_size = input_size
        self.output_size = output_size
        self.harmonic_order = harmonic_order
        self.coefficient_mode = coefficient_mode
        self.offset_hidden_size = offset_hidden_size
        self.offset_num_layers = offset_num_layers
        self.offset_dropout_probability = offset_dropout_probability
        self.offset_bidirectional = offset_bidirectional
        self.offset_readout_position = offset_readout_position
        self.offset_scale = float(offset_scale)
        self.freeze_structured_branch = freeze_structured_branch

        # Initialize Structured Harmonic Shape Branch
        self.structured_branch = HarmonicRegression(
            input_size=input_size,
            output_size=output_size,
            harmonic_order=harmonic_order,
            coefficient_mode=coefficient_mode,
            harmonic_index_list=harmonic_index_list,
        )
        self.harmonic_index_list = self.structured_branch.harmonic_index_list
        self.positive_harmonic_index_list = self.structured_branch.positive_harmonic_index_list

        # Optionally Freeze Structured Branch
        if self.freeze_structured_branch:
            for structured_parameter in self.structured_branch.parameters():
                structured_parameter.requires_grad = False

        # Initialize Causal Residual-Offset Branch
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

        """Extract the point feature tensor used by the harmonic branch."""

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

        """Expose harmonic, residual-offset, and final prediction tensors."""

        # Validate Sequence Inputs
        assert input_tensor.ndim == 3, f"Input Tensor must be rank-3 | {tuple(input_tensor.shape)}"
        assert normalized_input_tensor.ndim == 3, (
            f"Normalized Input Tensor must be rank-3 | {tuple(normalized_input_tensor.shape)}"
        )
        assert input_tensor.shape == normalized_input_tensor.shape, (
            f"Raw and normalized sequence shapes must match | {tuple(input_tensor.shape)} vs "
            f"{tuple(normalized_input_tensor.shape)}"
        )

        # Compute Structured Harmonic Shape At The Readout Position
        readout_input_tensor = self.resolve_readout_feature_tensor(input_tensor)
        readout_normalized_input_tensor = self.resolve_readout_feature_tensor(normalized_input_tensor)
        structured_prediction_tensor = self.structured_branch.forward_with_input_context(
            readout_input_tensor,
            readout_normalized_input_tensor,
        )

        # Compute Causal Residual Offset From The Sequence Window
        residual_offset_prediction_tensor = self.residual_offset_branch(normalized_input_tensor) * self.offset_scale
        final_prediction_tensor = structured_prediction_tensor + residual_offset_prediction_tensor

        return {
            "structured_prediction_tensor": structured_prediction_tensor,
            "residual_offset_prediction_tensor": residual_offset_prediction_tensor,
            "prediction_tensor": final_prediction_tensor,
        }

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Predict normalized TE from harmonic shape plus causal offset."""

        return self.compute_auxiliary_output_dictionary(input_tensor, normalized_input_tensor)["prediction_tensor"]

    def forward(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Run inference from normalized sequence inputs only."""

        return self.compute_auxiliary_output_dictionary(
            normalized_input_tensor,
            normalized_input_tensor,
        )["prediction_tensor"]
