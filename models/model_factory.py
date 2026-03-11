from __future__ import annotations

# Import Typing Utilities
from typing import Any

# Import PyTorch Utilities
import torch.nn as nn

# Import Project Models
from models.feedforward_network import FeedForwardNetwork


def create_model(model_type: str, model_configuration: dict[str, Any]) -> nn.Module:

    """ Create Model """

    # Validate Model Type
    normalized_model_type = model_type.lower()

    # Create Feedforward Model
    if normalized_model_type == "feedforward":
        return FeedForwardNetwork(
            input_size=int(model_configuration["input_size"]),
            hidden_size=list(model_configuration["hidden_size"]),
            output_size=int(model_configuration["output_size"]),
            activation_name=str(model_configuration["activation_name"]),
            dropout_probability=float(model_configuration["dropout_probability"]),
            use_layer_norm=bool(model_configuration["use_layer_norm"]),
        )

    raise ValueError(f"Unsupported Model Type | {model_type}")
