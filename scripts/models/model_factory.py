"""Factory helpers that map TE model-type strings to concrete modules."""

from __future__ import annotations

# Import Typing Utilities
from typing import Any

# Import PyTorch Utilities
import torch.nn as nn

# Import Project Models
from scripts.models.feedforward_network import FeedForwardNetwork
from scripts.models.harmonic_regression import HarmonicRegression
from scripts.models.periodic_feature_network import PeriodicFeatureNetwork
from scripts.models.residual_harmonic_network import ResidualHarmonicNetwork

def create_model(model_type: str, model_configuration: dict[str, Any]) -> nn.Module:

    """Instantiate one supported TE model from a configuration dictionary.

    Args:
        model_type: Canonical model-type string such as `feedforward`,
            `harmonic_regression`, `periodic_mlp`, or
            `residual_harmonic_mlp`.
        model_configuration: Model-specific configuration dictionary.

    Returns:
        nn.Module: Instantiated PyTorch module matching the requested model
        type.

    Raises:
        ValueError: If `model_type` does not match one of the supported model
            families.
    """

    # Validate Model Type
    normalized_model_type = model_type.lower()

    # Create Requested Feedforward Model
    if normalized_model_type == "feedforward":
        return FeedForwardNetwork(
            input_size=int(model_configuration["input_size"]),
            hidden_size=list(model_configuration["hidden_size"]),
            output_size=int(model_configuration["output_size"]),
            activation_name=str(model_configuration["activation_name"]),
            dropout_probability=float(model_configuration["dropout_probability"]),
            use_layer_norm=bool(model_configuration["use_layer_norm"]),
        )

    # Create Harmonic Regression Baseline
    if normalized_model_type == "harmonic_regression":
        return HarmonicRegression(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration["harmonic_order"]),
            coefficient_mode=str(model_configuration.get("coefficient_mode", "static")),
        )

    # Create Periodic-Feature Feedforward Model
    if normalized_model_type == "periodic_mlp":
        return PeriodicFeatureNetwork(
            input_size=int(model_configuration["input_size"]),
            hidden_size=list(model_configuration["hidden_size"]),
            output_size=int(model_configuration["output_size"]),
            activation_name=str(model_configuration["activation_name"]),
            dropout_probability=float(model_configuration["dropout_probability"]),
            use_layer_norm=bool(model_configuration["use_layer_norm"]),
            harmonic_order=int(model_configuration["harmonic_order"]),
            include_raw_angle_feature=bool(model_configuration.get("include_raw_angle_feature", True)),
        )

    # Create Residual Harmonic + Feedforward Model
    if normalized_model_type == "residual_harmonic_mlp":
        return ResidualHarmonicNetwork(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration["harmonic_order"]),
            coefficient_mode=str(model_configuration.get("coefficient_mode", "static")),
            residual_hidden_size=list(model_configuration["residual_hidden_size"]),
            residual_activation_name=str(model_configuration.get("residual_activation_name", "GELU")),
            residual_dropout_probability=float(model_configuration.get("residual_dropout_probability", 0.10)),
            residual_use_layer_norm=bool(model_configuration.get("residual_use_layer_norm", True)),
            freeze_structured_branch=bool(model_configuration.get("freeze_structured_branch", False)),
        )

    raise ValueError(f"Unsupported Model Type | {model_type}")
