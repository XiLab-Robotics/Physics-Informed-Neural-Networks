"""Periodic temporal sequence networks for harmonic-aware TE windows."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Models
from scripts.models.harmonic_regression import HarmonicRegression
from scripts.models.temporal_sequence_network import RecurrentSequenceNetwork
from scripts.models.temporal_sequence_network import TemporalConvolutionNetwork

class PeriodicTemporalSequenceNetwork(nn.Module):

    """Temporal TE sequence model with per-timestep harmonic angle features."""

    def __init__(
        self,
        temporal_model_type: str,
        input_size: int,
        output_size: int = 1,
        harmonic_order: int = 8,
        harmonic_index_list: list[int] | None = None,
        include_raw_angle_feature: bool = True,
        channel_size: list[int] | None = None,
        kernel_size: int = 5,
        activation_name: str = "GELU",
        hidden_size: int = 128,
        num_layers: int = 2,
        dropout_probability: float = 0.10,
        bidirectional: bool = False,
        readout_position: str = "center",
    ) -> None:
        """Initialize one periodic temporal TE sequence backbone.

        Args:
            temporal_model_type: Temporal backbone selector. Supported values
                are `temporal_convolution`, `gru_sequence`, and
                `lstm_sequence`.
            input_size: Raw sequence feature count, including angular position
                as the first feature.
            output_size: Regression target count.
            harmonic_order: Contiguous harmonic order used when no explicit
                harmonic index list is provided.
            harmonic_index_list: Optional explicit non-negative harmonic list.
                Positive indices create sine/cosine pairs and `0` follows the
                existing DC/bias convention.
            include_raw_angle_feature: Whether to keep the normalized raw
                angle alongside the harmonic feature expansion.
            channel_size: Temporal convolution channel widths.
            kernel_size: Temporal convolution kernel size.
            activation_name: Temporal convolution activation name.
            hidden_size: Recurrent hidden size for `GRU` and `LSTM`.
            num_layers: Recurrent layer count.
            dropout_probability: Dropout probability used by the temporal
                backbone.
            bidirectional: Whether recurrent backbones are bidirectional.
            readout_position: Sequence readout position passed to the temporal
                backbone.
        """

        super().__init__()

        # Validate Feature Parameters
        normalized_temporal_model_type = temporal_model_type.strip().lower()
        supported_temporal_type_list = ["temporal_convolution", "gru_sequence", "lstm_sequence"]
        assert normalized_temporal_model_type in supported_temporal_type_list, (
            f"Unsupported Periodic Temporal Model Type | {temporal_model_type}"
        )
        assert input_size >= 5, f"Input Size must expose the TE operating-condition features | {input_size}"
        assert output_size > 0, f"Output Size must be positive | {output_size}"
        assert harmonic_order > 0, f"Harmonic Order must be positive | {harmonic_order}"

        # Resolve Harmonic Basis
        resolved_harmonic_index_list = HarmonicRegression.resolve_harmonic_index_list(harmonic_order, harmonic_index_list)
        positive_harmonic_index_list = [harmonic_index for harmonic_index in resolved_harmonic_index_list if harmonic_index > 0]

        # Save Feature Parameters
        self.temporal_model_type = normalized_temporal_model_type
        self.input_size = input_size
        self.output_size = output_size
        self.harmonic_order = harmonic_order
        self.harmonic_index_list = resolved_harmonic_index_list
        self.positive_harmonic_index_list = positive_harmonic_index_list
        self.include_raw_angle_feature = include_raw_angle_feature

        # Register Device-Aware Harmonic Index Buffer
        positive_harmonic_index_tensor = torch.tensor(self.positive_harmonic_index_list, dtype=torch.float32)
        self.register_buffer("positive_harmonic_index_tensor", positive_harmonic_index_tensor, persistent=False)

        # Resolve Expanded Sequence Feature Size
        harmonic_feature_count = 2 * len(self.positive_harmonic_index_list)
        raw_angle_feature_count = 1 if self.include_raw_angle_feature else 0
        conditioning_feature_count = input_size - 1
        self.expanded_input_size = raw_angle_feature_count + harmonic_feature_count + conditioning_feature_count

        # Build Requested Temporal Backbone
        if self.temporal_model_type == "temporal_convolution":
            assert channel_size is not None, "Channel Size is required for periodic temporal convolution"
            self.temporal_backbone = TemporalConvolutionNetwork(
                input_size=self.expanded_input_size,
                channel_size=list(channel_size),
                output_size=output_size,
                kernel_size=kernel_size,
                activation_name=activation_name,
                dropout_probability=dropout_probability,
                readout_position=readout_position,
            )
        else:
            recurrent_type = "gru" if self.temporal_model_type == "gru_sequence" else "lstm"
            self.temporal_backbone = RecurrentSequenceNetwork(
                recurrent_type=recurrent_type,
                input_size=self.expanded_input_size,
                hidden_size=hidden_size,
                output_size=output_size,
                num_layers=num_layers,
                dropout_probability=dropout_probability,
                bidirectional=bidirectional,
                readout_position=readout_position,
            )

    def build_periodic_feature_tensor(self, angular_position_deg: torch.Tensor) -> torch.Tensor:

        """Build sine/cosine harmonic features for rank-2 or rank-3 angles."""

        # Convert Angular Position To Radians
        angular_position_rad = angular_position_deg * (torch.pi / 180.0)
        periodic_feature_tensor_list: list[torch.Tensor] = []

        # Return An Empty Feature Block When Only The DC Convention Is Requested
        if len(self.positive_harmonic_index_list) == 0:
            return angular_position_deg.new_empty((*angular_position_deg.shape[:-1], 0))

        # Append Sine And Cosine Features For Each Harmonic Index
        for harmonic_multiplier in self.positive_harmonic_index_tensor:
            periodic_feature_tensor_list.append(torch.sin(harmonic_multiplier * angular_position_rad))
            periodic_feature_tensor_list.append(torch.cos(harmonic_multiplier * angular_position_rad))

        return torch.cat(periodic_feature_tensor_list, dim=-1)

    def build_expanded_sequence_tensor(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Build the expanded per-timestep feature tensor for the backbone."""

        # Validate Sequence Inputs
        assert input_tensor.ndim == 3, f"Input Tensor must be rank-3 | {tuple(input_tensor.shape)}"
        assert normalized_input_tensor.ndim == 3, (
            f"Normalized Input Tensor must be rank-3 | {tuple(normalized_input_tensor.shape)}"
        )
        assert input_tensor.shape == normalized_input_tensor.shape, (
            f"Raw and normalized sequence shapes must match | {tuple(input_tensor.shape)} vs "
            f"{tuple(normalized_input_tensor.shape)}"
        )
        assert input_tensor.shape[-1] == self.input_size, (
            f"Input feature mismatch | {input_tensor.shape[-1]} vs {self.input_size}"
        )

        # Extract Angular Position And Build Feature List
        angular_position_deg = input_tensor[..., 0:1]
        feature_tensor_list: list[torch.Tensor] = []

        if self.include_raw_angle_feature:
            feature_tensor_list.append(normalized_input_tensor[..., 0:1])

        feature_tensor_list.append(self.build_periodic_feature_tensor(angular_position_deg))
        feature_tensor_list.append(normalized_input_tensor[..., 1:])

        # Concatenate Expanded Per-Timestep Features
        return torch.cat(feature_tensor_list, dim=-1)

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Predict normalized TE from harmonic-aware sequence windows."""

        expanded_sequence_tensor = self.build_expanded_sequence_tensor(input_tensor, normalized_input_tensor)
        return self.temporal_backbone(expanded_sequence_tensor)
