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
from scripts.models.periodic_temporal_sequence_network import PeriodicTemporalSequenceNetwork
from scripts.models.residual_harmonic_network import ResidualHarmonicNetwork
from scripts.models.residual_harmonic_temporal_sequence_network import ResidualHarmonicTemporalSequenceNetwork
from scripts.models.sequential_residual_offset_network import SequentialResidualOffsetNetwork
from scripts.models.temporal_sequence_network import RecurrentSequenceNetwork
from scripts.models.temporal_sequence_network import TemporalConvolutionNetwork

def create_model(model_type: str, model_configuration: dict[str, Any]) -> nn.Module:

    """Instantiate one supported TE model from a configuration dictionary.

    Args:
        model_type: Canonical model-type string such as `feedforward`,
            `harmonic_regression`, `periodic_mlp`,
            `residual_harmonic_mlp`, `temporal_convolution`,
            `gru_sequence`, `lstm_sequence`, or one of the periodic temporal
            sequence and residual harmonic temporal variants.
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
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
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
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
            include_raw_angle_feature=bool(model_configuration.get("include_raw_angle_feature", True)),
        )

    # Create Residual Harmonic + Feedforward Model
    if normalized_model_type == "residual_harmonic_mlp":
        return ResidualHarmonicNetwork(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration["harmonic_order"]),
            coefficient_mode=str(model_configuration.get("coefficient_mode", "static")),
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
            residual_hidden_size=list(model_configuration["residual_hidden_size"]),
            residual_activation_name=str(model_configuration.get("residual_activation_name", "GELU")),
            residual_dropout_probability=float(model_configuration.get("residual_dropout_probability", 0.10)),
            residual_use_layer_norm=bool(model_configuration.get("residual_use_layer_norm", True)),
            freeze_structured_branch=bool(model_configuration.get("freeze_structured_branch", False)),
        )

    # Create Temporal Convolution Sequence Model
    if normalized_model_type == "temporal_convolution":
        return TemporalConvolutionNetwork(
            input_size=int(model_configuration["input_size"]),
            channel_size=list(model_configuration["channel_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            kernel_size=int(model_configuration.get("kernel_size", 5)),
            activation_name=str(model_configuration.get("activation_name", "GELU")),
            dropout_probability=float(model_configuration.get("dropout_probability", 0.10)),
            readout_position=str(model_configuration.get("readout_position", "center")),
        )

    # Create Periodic Temporal Convolution Sequence Model
    if normalized_model_type == "periodic_temporal_convolution":
        return PeriodicTemporalSequenceNetwork(
            temporal_model_type="temporal_convolution",
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration["harmonic_order"]),
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
            include_raw_angle_feature=bool(model_configuration.get("include_raw_angle_feature", True)),
            channel_size=list(model_configuration["channel_size"]),
            kernel_size=int(model_configuration.get("kernel_size", 5)),
            activation_name=str(model_configuration.get("activation_name", "GELU")),
            dropout_probability=float(model_configuration.get("dropout_probability", 0.10)),
            readout_position=str(model_configuration.get("readout_position", "center")),
        )

    # Create GRU Sequence Model
    if normalized_model_type == "gru_sequence":
        return RecurrentSequenceNetwork(
            recurrent_type="gru",
            input_size=int(model_configuration["input_size"]),
            hidden_size=int(model_configuration["hidden_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            num_layers=int(model_configuration.get("num_layers", 2)),
            dropout_probability=float(model_configuration.get("dropout_probability", 0.10)),
            bidirectional=bool(model_configuration.get("bidirectional", False)),
            readout_position=str(model_configuration.get("readout_position", "center")),
        )

    # Create Residual Harmonic GRU Sequence Model
    if normalized_model_type == "residual_harmonic_gru_sequence":
        return ResidualHarmonicTemporalSequenceNetwork(
            temporal_model_type="gru_sequence",
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration["harmonic_order"]),
            coefficient_mode=str(model_configuration.get("coefficient_mode", "static")),
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
            hidden_size=int(model_configuration["hidden_size"]),
            num_layers=int(model_configuration.get("num_layers", 2)),
            dropout_probability=float(model_configuration.get("dropout_probability", 0.10)),
            bidirectional=bool(model_configuration.get("bidirectional", False)),
            readout_position=str(model_configuration.get("readout_position", "center")),
            freeze_structured_branch=bool(model_configuration.get("freeze_structured_branch", False)),
        )

    # Create Periodic GRU Sequence Model
    if normalized_model_type == "periodic_gru_sequence":
        return PeriodicTemporalSequenceNetwork(
            temporal_model_type="gru_sequence",
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration["harmonic_order"]),
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
            include_raw_angle_feature=bool(model_configuration.get("include_raw_angle_feature", True)),
            hidden_size=int(model_configuration["hidden_size"]),
            num_layers=int(model_configuration.get("num_layers", 2)),
            dropout_probability=float(model_configuration.get("dropout_probability", 0.10)),
            bidirectional=bool(model_configuration.get("bidirectional", False)),
            readout_position=str(model_configuration.get("readout_position", "center")),
        )

    # Create LSTM Sequence Model
    if normalized_model_type == "lstm_sequence":
        return RecurrentSequenceNetwork(
            recurrent_type="lstm",
            input_size=int(model_configuration["input_size"]),
            hidden_size=int(model_configuration["hidden_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            num_layers=int(model_configuration.get("num_layers", 2)),
            dropout_probability=float(model_configuration.get("dropout_probability", 0.10)),
            bidirectional=bool(model_configuration.get("bidirectional", False)),
            readout_position=str(model_configuration.get("readout_position", "center")),
        )

    # Create Residual Harmonic LSTM Sequence Model
    if normalized_model_type == "residual_harmonic_lstm_sequence":
        return ResidualHarmonicTemporalSequenceNetwork(
            temporal_model_type="lstm_sequence",
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration["harmonic_order"]),
            coefficient_mode=str(model_configuration.get("coefficient_mode", "static")),
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
            hidden_size=int(model_configuration["hidden_size"]),
            num_layers=int(model_configuration.get("num_layers", 2)),
            dropout_probability=float(model_configuration.get("dropout_probability", 0.10)),
            bidirectional=bool(model_configuration.get("bidirectional", False)),
            readout_position=str(model_configuration.get("readout_position", "center")),
            freeze_structured_branch=bool(model_configuration.get("freeze_structured_branch", False)),
        )

    # Create Track 2F Sequential Residual-Offset Probe
    if normalized_model_type == "sequential_residual_offset_probe":
        return SequentialResidualOffsetNetwork(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            base_hidden_size=list(model_configuration.get("base_hidden_size", [96, 64])),
            base_activation_name=str(model_configuration.get("base_activation_name", "GELU")),
            base_dropout_probability=float(model_configuration.get("base_dropout_probability", 0.05)),
            base_use_layer_norm=bool(model_configuration.get("base_use_layer_norm", True)),
            offset_hidden_size=int(model_configuration.get("offset_hidden_size", 96)),
            offset_num_layers=int(model_configuration.get("offset_num_layers", 2)),
            offset_dropout_probability=float(model_configuration.get("offset_dropout_probability", 0.10)),
            offset_bidirectional=bool(model_configuration.get("offset_bidirectional", False)),
            offset_readout_position=str(model_configuration.get("offset_readout_position", "center")),
            offset_scale=float(model_configuration.get("offset_scale", 1.0)),
        )

    # Create Periodic LSTM Sequence Model
    if normalized_model_type == "periodic_lstm_sequence":
        return PeriodicTemporalSequenceNetwork(
            temporal_model_type="lstm_sequence",
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration["harmonic_order"]),
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
            include_raw_angle_feature=bool(model_configuration.get("include_raw_angle_feature", True)),
            hidden_size=int(model_configuration["hidden_size"]),
            num_layers=int(model_configuration.get("num_layers", 2)),
            dropout_probability=float(model_configuration.get("dropout_probability", 0.10)),
            bidirectional=bool(model_configuration.get("bidirectional", False)),
            readout_position=str(model_configuration.get("readout_position", "center")),
        )

    raise ValueError(f"Unsupported Model Type | {model_type}")
