"""Temporal sequence networks for Wave 2.1 TE regression candidates."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Model Utilities
from scripts.models.feedforward_network import get_activation_module

def resolve_sequence_readout_tensor(sequence_tensor: torch.Tensor, readout_position: str) -> torch.Tensor:

    """Select one timestep representation from a batched sequence tensor."""

    # Validate Sequence Tensor
    assert sequence_tensor.ndim == 3, f"Sequence Tensor must be rank-3 | {tuple(sequence_tensor.shape)}"

    # Resolve Readout Position
    normalized_readout_position = readout_position.strip().lower()
    assert normalized_readout_position in ["center", "last"], f"Unsupported Readout Position | {readout_position}"

    if normalized_readout_position == "center":
        center_index = sequence_tensor.shape[1] // 2
        return sequence_tensor[:, center_index, :]

    return sequence_tensor[:, -1, :]

class TemporalConvolutionNetwork(nn.Module):

    """Causal-free temporal convolutional regressor for TE sequence windows."""

    def __init__(
        self,
        input_size: int,
        channel_size: list[int],
        output_size: int = 1,
        kernel_size: int = 5,
        activation_name: str = "GELU",
        dropout_probability: float = 0.10,
        readout_position: str = "center",
    ) -> None:
        """Initialize the temporal convolutional regression backbone."""

        super().__init__()

        # Validate Architecture Parameters
        assert input_size > 0, f"Input Size must be positive | {input_size}"
        assert output_size > 0, f"Output Size must be positive | {output_size}"
        assert len(channel_size) > 0, "Channel Size list must contain at least one layer"
        assert kernel_size > 0 and kernel_size % 2 == 1, f"Kernel Size must be a positive odd integer | {kernel_size}"
        assert dropout_probability >= 0.0, f"Dropout Probability must be non-negative | {dropout_probability}"

        # Save Architecture Parameters
        self.input_size = input_size
        self.channel_size = list(channel_size)
        self.output_size = output_size
        self.kernel_size = kernel_size
        self.activation_name = activation_name
        self.dropout_probability = dropout_probability
        self.readout_position = readout_position

        # Build Temporal Convolution Stack
        convolution_layer_list: list[nn.Module] = []
        previous_channel_size = input_size
        padding_size = kernel_size // 2

        for current_channel_size in self.channel_size:
            assert current_channel_size > 0, f"Channel Size must be positive | {current_channel_size}"
            convolution_layer_list.append(nn.Conv1d(previous_channel_size, current_channel_size, kernel_size, padding=padding_size))
            convolution_layer_list.append(get_activation_module(self.activation_name))
            if self.dropout_probability > 0.0: convolution_layer_list.append(nn.Dropout(self.dropout_probability))
            previous_channel_size = current_channel_size

        self.temporal_network = nn.Sequential(*convolution_layer_list)
        self.output_layer = nn.Linear(previous_channel_size, output_size)

    def forward(self, input_tensor: torch.Tensor) -> torch.Tensor:

        """Run the temporal convolutional network on rank-3 input windows."""

        # Validate Input Tensor
        assert input_tensor.ndim == 3, f"Temporal Convolution input must be rank-3 | {tuple(input_tensor.shape)}"
        assert input_tensor.shape[-1] == self.input_size, (
            f"Input feature mismatch | {input_tensor.shape[-1]} vs {self.input_size}"
        )

        # Conv1d Expects Batch, Channel, Sequence
        channel_first_input_tensor = input_tensor.transpose(1, 2)
        channel_first_output_tensor = self.temporal_network(channel_first_input_tensor)
        sequence_output_tensor = channel_first_output_tensor.transpose(1, 2)
        readout_tensor = resolve_sequence_readout_tensor(sequence_output_tensor, self.readout_position)

        return self.output_layer(readout_tensor)

class RecurrentSequenceNetwork(nn.Module):

    """GRU or LSTM sequence regressor with an explicit temporal readout."""

    def __init__(
        self,
        recurrent_type: str,
        input_size: int,
        hidden_size: int,
        output_size: int = 1,
        num_layers: int = 2,
        dropout_probability: float = 0.10,
        bidirectional: bool = False,
        readout_position: str = "center",
    ) -> None:
        """Initialize a recurrent sequence regression backbone."""

        super().__init__()

        # Validate Architecture Parameters
        normalized_recurrent_type = recurrent_type.strip().lower()
        assert normalized_recurrent_type in ["gru", "lstm"], f"Unsupported Recurrent Type | {recurrent_type}"
        assert input_size > 0, f"Input Size must be positive | {input_size}"
        assert hidden_size > 0, f"Hidden Size must be positive | {hidden_size}"
        assert output_size > 0, f"Output Size must be positive | {output_size}"
        assert num_layers > 0, f"Num Layers must be positive | {num_layers}"
        assert dropout_probability >= 0.0, f"Dropout Probability must be non-negative | {dropout_probability}"

        # Save Architecture Parameters
        self.recurrent_type = normalized_recurrent_type
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.num_layers = num_layers
        self.dropout_probability = dropout_probability
        self.bidirectional = bidirectional
        self.readout_position = readout_position

        # PyTorch applies recurrent dropout only between stacked layers.
        recurrent_dropout_probability = dropout_probability if num_layers > 1 else 0.0
        recurrent_class = nn.GRU if self.recurrent_type == "gru" else nn.LSTM
        self.recurrent_network = recurrent_class(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=recurrent_dropout_probability,
            bidirectional=bidirectional,
        )

        recurrent_output_size = hidden_size * (2 if bidirectional else 1)
        self.output_dropout = nn.Dropout(dropout_probability) if dropout_probability > 0.0 else nn.Identity()
        self.output_layer = nn.Linear(recurrent_output_size, output_size)

    def forward(self, input_tensor: torch.Tensor) -> torch.Tensor:

        """Run the recurrent sequence network on rank-3 input windows."""

        # Validate Input Tensor
        assert input_tensor.ndim == 3, f"Recurrent input must be rank-3 | {tuple(input_tensor.shape)}"
        assert input_tensor.shape[-1] == self.input_size, (
            f"Input feature mismatch | {input_tensor.shape[-1]} vs {self.input_size}"
        )

        # Read Recurrent Output Sequence
        recurrent_output_tensor, _ = self.recurrent_network(input_tensor)
        readout_tensor = resolve_sequence_readout_tensor(recurrent_output_tensor, self.readout_position)
        dropped_readout_tensor = self.output_dropout(readout_tensor)

        return self.output_layer(dropped_readout_tensor)
