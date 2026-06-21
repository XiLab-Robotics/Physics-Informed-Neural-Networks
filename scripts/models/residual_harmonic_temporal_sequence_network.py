"""Residual harmonic temporal sequence networks for Wave 2.3 TE candidates."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Models
from scripts.models.harmonic_regression import HarmonicRegression
from scripts.models.temporal_sequence_network import RecurrentSequenceNetwork
from scripts.models.temporal_sequence_network import resolve_sequence_readout_tensor

class ResidualHarmonicTemporalSequenceNetwork(nn.Module):

    """Sequence TE model with harmonic base prediction plus temporal residual."""

    def __init__(
        self,
        temporal_model_type: str,
        input_size: int,
        output_size: int = 1,
        harmonic_order: int = 12,
        coefficient_mode: str = "static",
        harmonic_index_list: list[int] | None = None,
        hidden_size: int = 128,
        num_layers: int = 2,
        dropout_probability: float = 0.10,
        bidirectional: bool = False,
        readout_position: str = "center",
        freeze_structured_branch: bool = False,
    ) -> None:
        """Initialize one residual harmonic recurrent sequence model.

        Args:
            temporal_model_type: Temporal residual selector. Supported values
                are `gru_sequence` and `lstm_sequence`.
            input_size: Raw sequence feature count, including angular position
                as the first feature.
            output_size: Regression target count.
            harmonic_order: Contiguous harmonic order used when no explicit
                harmonic index list is provided.
            coefficient_mode: Harmonic coefficient parameterization mode passed
                to the structured branch.
            harmonic_index_list: Optional explicit non-negative harmonic list.
            hidden_size: Recurrent hidden size for the residual branch.
            num_layers: Recurrent layer count.
            dropout_probability: Dropout probability used by the recurrent
                residual branch.
            bidirectional: Whether the recurrent residual branch is
                bidirectional.
            readout_position: Sequence readout position used by both the
                residual branch and center-vector extraction.
            freeze_structured_branch: Whether to freeze the structured
                harmonic branch parameters during optimization.
        """

        super().__init__()

        # Validate Architecture Parameters
        normalized_temporal_model_type = temporal_model_type.strip().lower()
        supported_temporal_type_list = ["gru_sequence", "lstm_sequence"]
        assert normalized_temporal_model_type in supported_temporal_type_list, (
            f"Unsupported Residual Harmonic Temporal Model Type | {temporal_model_type}"
        )
        assert input_size >= 4, f"Input Size must expose angle and TE operating-condition features | {input_size}"
        assert output_size > 0, f"Output Size must be positive | {output_size}"
        assert harmonic_order > 0, f"Harmonic Order must be positive | {harmonic_order}"

        # Save Architecture Parameters
        self.temporal_model_type = normalized_temporal_model_type
        self.input_size = input_size
        self.output_size = output_size
        self.harmonic_order = harmonic_order
        self.coefficient_mode = coefficient_mode
        self.readout_position = readout_position
        self.freeze_structured_branch = freeze_structured_branch

        # Initialize Structured Harmonic Branch
        self.structured_branch = HarmonicRegression(
            input_size=input_size,
            output_size=output_size,
            harmonic_order=harmonic_order,
            coefficient_mode=coefficient_mode,
            harmonic_index_list=harmonic_index_list,
        )
        self.harmonic_index_list = self.structured_branch.harmonic_index_list
        self.positive_harmonic_index_list = self.structured_branch.positive_harmonic_index_list

        # Optionally Freeze Structured Parameters
        if self.freeze_structured_branch:

            # Disable Structured Gradients
            for structured_parameter in self.structured_branch.parameters():
                structured_parameter.requires_grad = False

        # Initialize Temporal Residual Branch
        recurrent_type = "gru" if self.temporal_model_type == "gru_sequence" else "lstm"
        self.residual_branch = RecurrentSequenceNetwork(
            recurrent_type=recurrent_type,
            input_size=input_size,
            hidden_size=hidden_size,
            output_size=output_size,
            num_layers=num_layers,
            dropout_probability=dropout_probability,
            bidirectional=bidirectional,
            readout_position=readout_position,
        )

    def resolve_readout_feature_tensor(self, sequence_tensor: torch.Tensor) -> torch.Tensor:

        """Extract the rank-2 feature tensor used by the structured branch."""

        # Validate Sequence Tensor
        assert sequence_tensor.ndim == 3, f"Sequence Tensor must be rank-3 | {tuple(sequence_tensor.shape)}"
        assert sequence_tensor.shape[-1] == self.input_size, (
            f"Input feature mismatch | {sequence_tensor.shape[-1]} vs {self.input_size}"
        )

        return resolve_sequence_readout_tensor(sequence_tensor, self.readout_position)

    def compute_auxiliary_output_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:

        """Expose branch-level outputs for diagnostics and metric logging.

        Args:
            input_tensor: Raw rank-3 sequence tensor whose first feature is
                physical angular position in degrees.
            normalized_input_tensor: Normalized rank-3 sequence tensor used by
                the temporal residual branch.

        Returns:
            dict[str, torch.Tensor]: Structured branch output, residual branch
            output, and final combined prediction tensor.
        """

        # Validate Sequence Inputs
        assert input_tensor.ndim == 3, f"Input Tensor must be rank-3 | {tuple(input_tensor.shape)}"
        assert normalized_input_tensor.ndim == 3, (
            f"Normalized Input Tensor must be rank-3 | {tuple(normalized_input_tensor.shape)}"
        )
        assert input_tensor.shape == normalized_input_tensor.shape, (
            f"Raw and normalized sequence shapes must match | {tuple(input_tensor.shape)} vs "
            f"{tuple(normalized_input_tensor.shape)}"
        )

        # Extract Structured Branch Inputs At The Configured Readout Position
        readout_input_tensor = self.resolve_readout_feature_tensor(input_tensor)
        readout_normalized_input_tensor = self.resolve_readout_feature_tensor(normalized_input_tensor)

        # Forward Pass Through Structured Harmonic Branch
        structured_prediction_tensor = self.structured_branch.forward_with_input_context(
            readout_input_tensor,
            readout_normalized_input_tensor,
        )

        # Forward Pass Through Temporal Residual Branch
        residual_prediction_tensor = self.residual_branch(normalized_input_tensor)

        # Return Branch-Level Diagnostics
        return {
            "structured_prediction_tensor": structured_prediction_tensor,
            "residual_prediction_tensor": residual_prediction_tensor,
            "prediction_tensor": structured_prediction_tensor + residual_prediction_tensor,
        }

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Predict TE from a harmonic base plus recurrent residual correction."""

        return self.compute_auxiliary_output_dictionary(input_tensor, normalized_input_tensor)["prediction_tensor"]
