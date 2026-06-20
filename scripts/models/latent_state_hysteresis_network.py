"""Latent-state hysteresis-aware network for Wave 4.4 TE probes."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn
import torch.nn.functional as torch_functional

# Import Project Model Utilities
from scripts.models.feedforward_network import FeedForwardNetwork
from scripts.models.feedforward_network import get_activation_module
from scripts.models.temporal_sequence_network import resolve_sequence_readout_tensor


class CausalTemporalStateEncoder(nn.Module):

    """Compact causal temporal convolution state encoder."""

    def __init__(
        self,
        input_size: int,
        hidden_size: int,
        channel_size: list[int] | None = None,
        kernel_size: int = 5,
        activation_name: str = "GELU",
        dropout_probability: float = 0.10,
    ) -> None:
        """Initialize the causal temporal state encoder."""

        super().__init__()

        # Validate Architecture Parameters
        assert input_size > 0, f"Input Size must be positive | {input_size}"
        assert hidden_size > 0, f"Hidden Size must be positive | {hidden_size}"
        assert kernel_size > 0, f"Kernel Size must be positive | {kernel_size}"
        assert dropout_probability >= 0.0, f"Dropout Probability must be non-negative | {dropout_probability}"

        # Save Architecture Parameters
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.channel_size = list(channel_size or [hidden_size, hidden_size])
        self.kernel_size = kernel_size
        self.activation_name = activation_name
        self.dropout_probability = dropout_probability

        # Build Causal Convolution Stack
        convolution_layer_list: list[nn.Module] = []
        previous_channel_size = input_size
        for current_channel_size in self.channel_size:
            assert current_channel_size > 0, f"Channel Size must be positive | {current_channel_size}"
            convolution_layer_list.append(nn.Conv1d(previous_channel_size, current_channel_size, kernel_size))
            convolution_layer_list.append(get_activation_module(self.activation_name))
            if self.dropout_probability > 0.0:
                convolution_layer_list.append(nn.Dropout(self.dropout_probability))
            previous_channel_size = current_channel_size

        self.temporal_network = nn.ModuleList(convolution_layer_list)
        self.output_projection = nn.Linear(previous_channel_size, hidden_size)

    def forward(self, input_tensor: torch.Tensor) -> torch.Tensor:

        """Encode a batch-first causal sequence into one latent state."""

        # Validate Input Tensor
        assert input_tensor.ndim == 3, f"Causal TCN input must be rank-3 | {tuple(input_tensor.shape)}"
        assert input_tensor.shape[-1] == self.input_size, (
            f"Input feature mismatch | {input_tensor.shape[-1]} vs {self.input_size}"
        )

        # Run Conv1d Layers With Left Padding Only
        channel_first_tensor = input_tensor.transpose(1, 2)
        for layer in self.temporal_network:
            if isinstance(layer, nn.Conv1d):
                channel_first_tensor = torch_functional.pad(
                    channel_first_tensor,
                    (self.kernel_size - 1, 0),
                )
            channel_first_tensor = layer(channel_first_tensor)

        sequence_output_tensor = channel_first_tensor.transpose(1, 2)
        last_state_tensor = sequence_output_tensor[:, -1, :]
        return self.output_projection(last_state_tensor)


class LatentStateHysteresisNetwork(nn.Module):

    """Causal latent-state model with base, offset, and residual TE heads."""

    def __init__(
        self,
        input_size: int,
        output_size: int = 1,
        latent_encoder_type: str = "gru",
        latent_hidden_size: int = 96,
        latent_num_layers: int = 2,
        latent_dropout_probability: float = 0.10,
        latent_channel_size: list[int] | None = None,
        latent_kernel_size: int = 5,
        latent_activation_name: str = "GELU",
        readout_position: str = "last",
        base_hidden_size: list[int] | None = None,
        head_hidden_size: list[int] | None = None,
        head_activation_name: str = "GELU",
        head_dropout_probability: float = 0.05,
        use_layer_norm: bool = True,
        offset_scale: float = 1.0,
        residual_scale: float = 1.0,
    ) -> None:
        """Initialize the latent-state hysteresis-aware TE probe."""

        super().__init__()

        # Validate Architecture Parameters
        normalized_encoder_type = latent_encoder_type.strip().lower()
        assert normalized_encoder_type in ["gru", "causal_tcn"], f"Unsupported Latent Encoder Type | {latent_encoder_type}"
        assert input_size >= 5, f"Input Size must expose TE operating features | {input_size}"
        assert output_size > 0, f"Output Size must be positive | {output_size}"
        assert latent_hidden_size > 0, f"Latent Hidden Size must be positive | {latent_hidden_size}"
        assert latent_num_layers > 0, f"Latent Num Layers must be positive | {latent_num_layers}"
        assert offset_scale > 0.0, f"Offset Scale must be positive | {offset_scale}"
        assert residual_scale > 0.0, f"Residual Scale must be positive | {residual_scale}"

        # Save Architecture Parameters
        self.input_size = input_size
        self.output_size = output_size
        self.latent_encoder_type = normalized_encoder_type
        self.latent_hidden_size = latent_hidden_size
        self.latent_num_layers = latent_num_layers
        self.readout_position = readout_position
        self.offset_scale = float(offset_scale)
        self.residual_scale = float(residual_scale)

        # Build Causal Latent-State Encoder
        recurrent_dropout_probability = latent_dropout_probability if latent_num_layers > 1 else 0.0
        if self.latent_encoder_type == "gru":
            self.latent_encoder = nn.GRU(
                input_size=input_size,
                hidden_size=latent_hidden_size,
                num_layers=latent_num_layers,
                batch_first=True,
                dropout=recurrent_dropout_probability,
                bidirectional=False,
            )
        else:
            self.latent_encoder = CausalTemporalStateEncoder(
                input_size=input_size,
                hidden_size=latent_hidden_size,
                channel_size=latent_channel_size,
                kernel_size=latent_kernel_size,
                activation_name=latent_activation_name,
                dropout_probability=latent_dropout_probability,
            )

        # Build Point Base And Latent Heads
        self.base_branch = FeedForwardNetwork(
            input_size=input_size,
            hidden_size=list(base_hidden_size or [96, 64]),
            output_size=output_size,
            activation_name=head_activation_name,
            dropout_probability=head_dropout_probability,
            use_layer_norm=use_layer_norm,
        )
        head_input_size = input_size + latent_hidden_size
        self.offset_head = FeedForwardNetwork(
            input_size=head_input_size,
            hidden_size=list(head_hidden_size or [96, 64]),
            output_size=output_size,
            activation_name=head_activation_name,
            dropout_probability=head_dropout_probability,
            use_layer_norm=use_layer_norm,
        )
        self.residual_head = FeedForwardNetwork(
            input_size=head_input_size,
            hidden_size=list(head_hidden_size or [96, 64]),
            output_size=output_size,
            activation_name=head_activation_name,
            dropout_probability=head_dropout_probability,
            use_layer_norm=use_layer_norm,
        )

    def resolve_readout_feature_tensor(self, sequence_tensor: torch.Tensor) -> torch.Tensor:

        """Extract the current operating-state feature tensor."""

        # Validate Sequence Tensor
        assert sequence_tensor.ndim == 3, f"Sequence Tensor must be rank-3 | {tuple(sequence_tensor.shape)}"
        assert sequence_tensor.shape[-1] == self.input_size, (
            f"Input feature mismatch | {sequence_tensor.shape[-1]} vs {self.input_size}"
        )
        return resolve_sequence_readout_tensor(sequence_tensor, self.readout_position)

    def encode_latent_state(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Encode the causal operating-history window into one latent state."""

        # Dispatch Encoder Type
        if self.latent_encoder_type == "gru":
            _sequence_tensor, hidden_state_tensor = self.latent_encoder(normalized_input_tensor)
            return hidden_state_tensor[-1]

        return self.latent_encoder(normalized_input_tensor)

    def compute_auxiliary_output_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:

        """Expose base, latent, offset, residual, and final prediction tensors."""

        # Validate Sequence Inputs
        assert input_tensor.ndim == 3, f"Input Tensor must be rank-3 | {tuple(input_tensor.shape)}"
        assert normalized_input_tensor.ndim == 3, (
            f"Normalized Input Tensor must be rank-3 | {tuple(normalized_input_tensor.shape)}"
        )
        assert input_tensor.shape == normalized_input_tensor.shape, (
            f"Raw and normalized sequence shapes must match | {tuple(input_tensor.shape)} vs "
            f"{tuple(normalized_input_tensor.shape)}"
        )

        # Compute Causal Readout And Latent State
        readout_normalized_input_tensor = self.resolve_readout_feature_tensor(normalized_input_tensor)
        latent_state_tensor = self.encode_latent_state(normalized_input_tensor)
        head_input_tensor = torch.cat([readout_normalized_input_tensor, latent_state_tensor], dim=-1)

        # Predict Base, Offset, Residual, And Final TE
        base_prediction_tensor = self.base_branch(readout_normalized_input_tensor)
        offset_prediction_tensor = self.offset_head(head_input_tensor) * self.offset_scale
        residual_prediction_tensor = self.residual_head(head_input_tensor) * self.residual_scale
        final_prediction_tensor = base_prediction_tensor + offset_prediction_tensor + residual_prediction_tensor

        return {
            "base_prediction_tensor": base_prediction_tensor,
            "latent_state_tensor": latent_state_tensor,
            "residual_offset_prediction_tensor": offset_prediction_tensor,
            "hysteresis_residual_prediction_tensor": residual_prediction_tensor,
            "prediction_tensor": final_prediction_tensor,
        }

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Predict normalized TE using raw context and normalized model input."""

        return self.compute_auxiliary_output_dictionary(input_tensor, normalized_input_tensor)["prediction_tensor"]

    def forward(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Run inference from normalized sequence inputs."""

        return self.compute_auxiliary_output_dictionary(
            normalized_input_tensor,
            normalized_input_tensor,
        )["prediction_tensor"]
