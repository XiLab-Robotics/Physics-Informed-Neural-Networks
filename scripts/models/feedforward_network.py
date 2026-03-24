"""Feedforward network components for TE regression baselines."""

from __future__ import annotations

# Import PyTorch Utilities
import torch.nn as nn

def get_activation_module(activation_name: str) -> nn.Module:

    """Return the activation layer instance for one configured activation name.

    Args:
        activation_name: Case-insensitive activation identifier supported by the
            repository feedforward baselines.

    Returns:
        A newly instantiated PyTorch activation module.

    Raises:
        AssertionError: If the requested activation name is not supported by
            the repository activation map.
    """

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

    # Instantiate Activation Module
    return activation_module_map[activation_key]()

class FeedForwardNetwork(nn.Module):

    """Dense multilayer perceptron used by the static TE regression baselines.

    The network builds a stack of linear layers followed by optional layer
    normalization, one activation per hidden layer, and optional dropout.
    The final layer maps the last hidden representation to the scalar or vector
    regression output configured by ``output_size``.
    """

    def __init__(
        self,
        input_size: int,
        hidden_size: list[int],
        output_size: int = 1,
        activation_name: str = "GELU",
        dropout_probability: float = 0.10,
        use_layer_norm: bool = True,
    ) -> None:
        """Initialize the feedforward regression backbone.

        Args:
            input_size: Number of scalar input features provided to the model.
            hidden_size: Hidden-layer widths in execution order.
            output_size: Number of regression outputs produced by the final
                linear layer.
            activation_name: Activation identifier resolved through
                :func:`get_activation_module`.
            dropout_probability: Dropout probability applied after each hidden
                activation when greater than zero.
            use_layer_norm: Whether to insert ``LayerNorm`` after each hidden
                linear layer.

        Raises:
            AssertionError: If an invalid architecture value is provided.
        """

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

        # Build Hidden Feedforward Layers
        network_layers: list[nn.Module] = []
        previous_feature_size = input_size

        for current_hidden_size in self.hidden_size:

            # Validate Hidden Layer Size
            assert current_hidden_size > 0, f"Hidden Layer Size must be positive | {current_hidden_size}"

            # Append Linear Layer
            network_layers.append(nn.Linear(previous_feature_size, current_hidden_size))

            # Append Layer Normalization
            if self.use_layer_norm: network_layers.append(nn.LayerNorm(current_hidden_size))

            # Append Activation Function
            network_layers.append(get_activation_module(self.activation_name))

            # Append Dropout
            if self.dropout_probability > 0.0: network_layers.append(nn.Dropout(self.dropout_probability))

            # Update Previous Feature Size
            previous_feature_size = current_hidden_size

        # Append Final Output Layer
        network_layers.append(nn.Linear(previous_feature_size, output_size))

        # Create Sequential Feedforward Network
        self.network = nn.Sequential(*network_layers)

    def forward(self, input_tensor):

        """Run the dense regression backbone on one input tensor.

        Args:
            input_tensor: Batched input tensor whose last dimension matches
                ``input_size``.

        Returns:
            Output tensor produced by the sequential dense network.
        """

        # Run Dense Network
        return self.network(input_tensor)
