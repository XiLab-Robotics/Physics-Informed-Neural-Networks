from __future__ import annotations

# Import PyTorch Utilities
import torch.nn as nn


def get_activation_module(activation_name: str) -> nn.Module:
    """ Get Activation Module """

    # Supported Activations
    activation_module_map = {
        "relu": nn.ReLU,
        "gelu": nn.GELU,
        "silu": nn.SiLU,
        "tanh": nn.Tanh,
    }

    # Resolve Activation Module
    activation_key = activation_name.lower()
    assert activation_key in activation_module_map, f"Unsupported Activation Name | {activation_name}"

    return activation_module_map[activation_key]()


class FeedForwardNetwork(nn.Module):
    """ Feedforward Network """

    def __init__(
        self,
        input_size: int,
        hidden_size: list[int],
        output_size: int = 1,
        activation_name: str = "GELU",
        dropout_probability: float = 0.10,
        use_layer_norm: bool = True,
    ) -> None:

        super().__init__()

        # Validate Architecture Parameters
        assert input_size > 0, f"Input Size must be positive | {input_size}"
        assert output_size > 0, f"Output Size must be positive | {output_size}"
        assert len(hidden_size) > 0, "Hidden Size list must contain at least one layer"
        assert dropout_probability >= 0.0, f"Dropout Probability must be non-negative | {dropout_probability}"

        # Save Architecture Parameters
        self.input_size = input_size
        self.hidden_size = list(hidden_size)
        self.output_size = output_size
        self.activation_name = activation_name
        self.dropout_probability = dropout_probability
        self.use_layer_norm = use_layer_norm

        # Build Hidden Network
        network_layers: list[nn.Module] = []
        previous_feature_size = input_size

        for current_hidden_size in self.hidden_size:

            # Validate Hidden Layer Size
            assert current_hidden_size > 0, f"Hidden Layer Size must be positive | {current_hidden_size}"

            # Append Linear Layer
            network_layers.append(nn.Linear(previous_feature_size, current_hidden_size))

            # Append Layer Normalization
            if self.use_layer_norm:
                network_layers.append(nn.LayerNorm(current_hidden_size))

            # Append Activation Function
            network_layers.append(get_activation_module(self.activation_name))

            # Append Dropout
            if self.dropout_probability > 0.0:
                network_layers.append(nn.Dropout(self.dropout_probability))

            previous_feature_size = current_hidden_size

        # Append Output Layer
        network_layers.append(nn.Linear(previous_feature_size, output_size))

        # Create Sequential Network
        self.network = nn.Sequential(*network_layers)

    def forward(self, input_tensor):
        """ Forward Pass """

        return self.network(input_tensor)
