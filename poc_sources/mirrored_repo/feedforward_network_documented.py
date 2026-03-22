from __future__ import annotations

# Import Python Utilities
from collections.abc import Sequence


ACTIVATION_MODULE_MAP = {
    "relu": "ReLU",
    "gelu": "GELU",
    "silu": "SiLU",
    "tanh": "Tanh",
}


def get_activation_module(activation_name: str) -> str:

    """Resolve the activation function used by the feedforward backbone.

    This helper mirrors the activation-selection logic from the canonical
    feedforward module while staying lightweight enough for isolated
    documentation generation. The real repository implementation returns a
    PyTorch activation module; this proof-of-concept mirror returns the
    activation display name so the documentation can be generated without a
    runtime PyTorch dependency.

    Args:
        activation_name: User-facing activation identifier. Supported values are
            ``relu``, ``gelu``, ``silu``, and ``tanh``.

    Returns:
        Canonical activation display name associated with the requested
        activation key.

    Raises:
        AssertionError: If ``activation_name`` does not match one of the
            supported activation identifiers.

    Examples:
        >>> get_activation_module("gelu")
        'GELU'

    Notes:
        The canonical repository implementation instantiates the real neural
        activation module. This isolated mirror keeps only the semantic mapping
        so the documentation site can focus on API readability.
    """

    # Resolve Activation Key
    activation_key = activation_name.lower()
    assert activation_key in ACTIVATION_MODULE_MAP, f"Unsupported Activation Name | {activation_name}"

    # Return Canonical Activation Label
    return ACTIVATION_MODULE_MAP[activation_key]


class FeedForwardNetwork:

    """Represent the configurable dense baseline used for static TE regression.

    The real repository model builds a stack of linear layers, optional layer
    normalization blocks, non-linear activations, and optional dropout. This
    isolated mirror preserves the same constructor contract and architectural
    intent while replacing the heavy runtime dependency with a documentation-
    friendly pure-Python representation.

    Attributes:
        input_size: Number of input features presented to the first dense layer.
        hidden_size: Width of each hidden dense layer in the backbone.
        output_size: Number of output channels predicted by the network.
        activation_name: User-facing activation identifier resolved by
            :func:`get_activation_module`.
        dropout_probability: Dropout probability applied after each hidden
            activation when positive.
        use_layer_norm: Whether each hidden block conceptually includes layer
            normalization.
        layer_description_list: Human-readable description of the internal block
            sequence built from the constructor arguments.

    Notes:
        This class exists only for documentation prototyping. It is intentionally
        lighter than the canonical ``torch.nn.Module`` implementation so both
        MkDocs and Sphinx can render it without importing the full ML stack.
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
        """Initialize the documented mirror of the feedforward architecture.

        Args:
            input_size: Input feature count consumed by the first dense layer.
            hidden_size: Ordered list of hidden-layer widths.
            output_size: Output feature count produced by the last dense layer.
            activation_name: Non-linear activation identifier used in each
                hidden block.
            dropout_probability: Dropout probability applied after each hidden
                activation when larger than zero.
            use_layer_norm: Whether the hidden blocks should include conceptual
                layer-normalization stages.

        Raises:
            AssertionError: If any size is invalid or if
                ``dropout_probability`` is negative.
        """

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

        # Build Human-Readable Layer Summary
        self.layer_description_list: list[str] = []
        previous_feature_size = input_size

        for current_hidden_size in self.hidden_size:
            assert current_hidden_size > 0, f"Hidden Layer Size must be positive | {current_hidden_size}"
            self.layer_description_list.append(f"Linear({previous_feature_size} -> {current_hidden_size})")
            if self.use_layer_norm:
                self.layer_description_list.append(f"LayerNorm({current_hidden_size})")
            self.layer_description_list.append(get_activation_module(self.activation_name))
            if self.dropout_probability > 0.0:
                self.layer_description_list.append(f"Dropout(p={self.dropout_probability:.2f})")
            previous_feature_size = current_hidden_size

        self.layer_description_list.append(f"Linear({previous_feature_size} -> {output_size})")

    def forward(self, input_tensor: Sequence[float] | Sequence[Sequence[float]]) -> Sequence[float] | Sequence[Sequence[float]]:
        """Describe the conceptual forward pass of the dense baseline.

        Args:
            input_tensor: One sample or batch of samples expressed as numeric
                feature vectors. The mirror accepts generic sequences because it
                is meant for documentation, not numerical execution.

        Returns:
            The same value received in ``input_tensor``. The mirror does not
            perform real numerical inference; it only preserves the public API
            shape required for the documentation proof of concept.

        Notes:
            In the canonical repository implementation this method delegates to a
            ``torch.nn.Sequential`` network and returns the predicted
            transmission-error values.
        """

        # Return Placeholder Output
        return input_tensor
