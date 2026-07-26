"""Factory helpers that map TE model-type strings to concrete modules."""

from __future__ import annotations

# Import Typing Utilities
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Import PyTorch Utilities
import torch.nn as nn

# Import Project Models
from scripts.models.feedforward_network import FeedForwardNetwork
from scripts.models.harmonic_regression import HarmonicRegression
from scripts.models.harmonic_kinematic_pinn_network import HarmonicKinematicPinnNetwork
from scripts.models.harmonic_residual_offset_network import HarmonicResidualOffsetNetwork
from scripts.models.latent_state_hysteresis_network import LatentStateHysteresisNetwork
from scripts.models.periodic_feature_network import PeriodicFeatureNetwork
from scripts.models.periodic_temporal_sequence_network import PeriodicTemporalSequenceNetwork
from scripts.models.quasi_static_compliance_pinn_network import (
    QuasiStaticCompliancePinnNetwork,
)
from scripts.models.residual_harmonic_network import ResidualHarmonicNetwork
from scripts.models.residual_harmonic_temporal_sequence_network import ResidualHarmonicTemporalSequenceNetwork
from scripts.models.sequential_residual_offset_network import SequentialResidualOffsetNetwork
from scripts.models.temporal_sequence_network import RecurrentSequenceNetwork
from scripts.models.temporal_sequence_network import TemporalConvolutionNetwork
from scripts.models.wave3_grouped_harmonic_heads_network import Wave3GroupedHarmonicHeadsNetwork
from scripts.models.wave3_harmonic_prior_residual_network import Wave3HarmonicPriorResidualNetwork
from scripts.models.wave52b_offset_harmonic_guided_network import Wave52BOffsetHarmonicGuidedNetwork


def load_harmonic_analytical_anchor_configuration(
    model_configuration: dict[str, Any],
) -> dict[str, Any]:
    """Load one frozen Phase 1 Polynomial-Fourier surface when configured."""

    anchor_path_text = model_configuration.get("analytical_anchor_path")
    if anchor_path_text in [None, ""]:
        return {}

    anchor_path = Path(str(anchor_path_text))
    assert anchor_path.is_file(), f"Analytical Anchor does not exist | {anchor_path}"
    with anchor_path.open("r", encoding="utf-8") as source_file:
        anchor_payload = yaml.safe_load(source_file)
    assert isinstance(anchor_payload, dict)
    model_id = str(
        model_configuration.get(
            "analytical_anchor_model_id",
            "PF_A_LOCAL_QUADRATIC",
        )
    )
    direction_label = str(model_configuration["analytical_anchor_direction"])
    surface_payload = anchor_payload["surface_map"][model_id][direction_label]
    assert list(surface_payload["harmonic_order_list"]) == list(
        model_configuration["harmonic_index_list"]
    ), "Analytical Anchor harmonic orders do not match the PINN configuration"
    return {
        "analytical_anchor_feature_mean": surface_payload["feature_mean"],
        "analytical_anchor_feature_scale": surface_payload["feature_scale"],
        "analytical_anchor_coefficient_matrix": (
            surface_payload["coefficient_matrix"]
        ),
    }


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

    # Create Wave 3.1 Sequential Residual-Offset Probe
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

    # Create Wave 3.2 Harmonic Residual-Offset Probe
    if normalized_model_type in ["harmonic_residual_offset_probe", "curve_aware_harmonic_residual_offset_probe"]:
        return HarmonicResidualOffsetNetwork(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration["harmonic_order"]),
            coefficient_mode=str(model_configuration.get("coefficient_mode", "linear_conditioned")),
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
            offset_hidden_size=int(model_configuration.get("offset_hidden_size", 96)),
            offset_num_layers=int(model_configuration.get("offset_num_layers", 2)),
            offset_dropout_probability=float(model_configuration.get("offset_dropout_probability", 0.10)),
            offset_bidirectional=bool(model_configuration.get("offset_bidirectional", False)),
            offset_readout_position=str(model_configuration.get("offset_readout_position", "center")),
            offset_scale=float(model_configuration.get("offset_scale", 1.0)),
            freeze_structured_branch=bool(model_configuration.get("freeze_structured_branch", False)),
        )

    # Create Wave 4.4 Latent-State Hysteresis Probe
    if normalized_model_type == "latent_state_hysteresis_probe":
        return LatentStateHysteresisNetwork(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            latent_encoder_type=str(model_configuration.get("latent_encoder_type", "gru")),
            latent_hidden_size=int(model_configuration.get("latent_hidden_size", 96)),
            latent_num_layers=int(model_configuration.get("latent_num_layers", 2)),
            latent_dropout_probability=float(model_configuration.get("latent_dropout_probability", 0.10)),
            latent_channel_size=model_configuration.get("latent_channel_size"),
            latent_kernel_size=int(model_configuration.get("latent_kernel_size", 5)),
            latent_activation_name=str(model_configuration.get("latent_activation_name", "GELU")),
            readout_position=str(model_configuration.get("readout_position", "last")),
            base_hidden_size=list(model_configuration.get("base_hidden_size", [96, 64])),
            head_hidden_size=list(model_configuration.get("head_hidden_size", [96, 64])),
            head_activation_name=str(model_configuration.get("head_activation_name", "GELU")),
            head_dropout_probability=float(model_configuration.get("head_dropout_probability", 0.05)),
            use_layer_norm=bool(model_configuration.get("use_layer_norm", True)),
            offset_scale=float(model_configuration.get("offset_scale", 1.0)),
            residual_scale=float(model_configuration.get("residual_scale", 1.0)),
        )

    # Create Embryonic Wave 5.1 Harmonic-Prior Residual Skeleton
    if normalized_model_type == "wave3_harmonic_prior_residual":
        return Wave3HarmonicPriorResidualNetwork(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration.get("harmonic_order", 240)),
            coefficient_mode=str(model_configuration.get("coefficient_mode", "linear_conditioned")),
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
            residual_hidden_size=list(model_configuration.get("residual_hidden_size", [96, 64])),
            residual_activation_name=str(model_configuration.get("residual_activation_name", "GELU")),
            residual_dropout_probability=float(model_configuration.get("residual_dropout_probability", 0.05)),
            residual_use_layer_norm=bool(model_configuration.get("residual_use_layer_norm", True)),
            residual_scale=float(model_configuration.get("residual_scale", 1.0)),
            readout_position=str(model_configuration.get("readout_position", "center")),
            freeze_structured_branch=bool(model_configuration.get("freeze_structured_branch", False)),
            low_order_harmonic_index_list=model_configuration.get("low_order_harmonic_index_list"),
            stable_middle_harmonic_index_list=model_configuration.get("stable_middle_harmonic_index_list"),
            high_order_harmonic_index_list=model_configuration.get("high_order_harmonic_index_list"),
        )

    # Create Wave 5.2 Phase 2 Harmonic-Kinematic PINN
    if normalized_model_type == "harmonic_kinematic_pinn":
        analytical_anchor_configuration = (
            load_harmonic_analytical_anchor_configuration(
                model_configuration
            )
        )
        return HarmonicKinematicPinnNetwork(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_index_list=list(
                model_configuration["harmonic_index_list"]
            ),
            condition_hidden_size=list(
                model_configuration.get("condition_hidden_size", [96, 64])
            ),
            condition_latent_size=int(
                model_configuration.get("condition_latent_size", 48)
            ),
            component_hidden_size=list(
                model_configuration.get("component_hidden_size", [32, 32])
            ),
            head_mode=str(
                model_configuration.get("head_mode", "implicit_pinn")
            ),
            activation_name=str(
                model_configuration.get("activation_name", "Tanh")
            ),
            dropout_probability=float(
                model_configuration.get("dropout_probability", 0.0)
            ),
            use_layer_norm=bool(
                model_configuration.get("use_layer_norm", False)
            ),
            analytical_anchor_feature_mean=analytical_anchor_configuration.get(
                "analytical_anchor_feature_mean",
                model_configuration.get("analytical_anchor_feature_mean"),
            ),
            analytical_anchor_feature_scale=analytical_anchor_configuration.get(
                "analytical_anchor_feature_scale",
                model_configuration.get("analytical_anchor_feature_scale"),
            ),
            analytical_anchor_coefficient_matrix=(
                analytical_anchor_configuration.get(
                    "analytical_anchor_coefficient_matrix",
                    model_configuration.get(
                        "analytical_anchor_coefficient_matrix"
                    ),
                )
            ),
        )

    # Create Wave 5.2 Phase 3 Quasi-Static Compliance PINN
    if normalized_model_type == "quasi_static_compliance_pinn":
        return QuasiStaticCompliancePinnNetwork(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_index_list=list(
                model_configuration["harmonic_index_list"]
            ),
            condition_hidden_size=list(
                model_configuration.get("condition_hidden_size", [64, 48])
            ),
            condition_latent_size=int(
                model_configuration.get("condition_latent_size", 32)
            ),
            mean_hidden_size=list(
                model_configuration.get("mean_hidden_size", [32, 16])
            ),
            formulation=str(
                model_configuration.get("formulation", "C1")
            ),
            activation_name=str(
                model_configuration.get("activation_name", "Tanh")
            ),
            dropout_probability=float(
                model_configuration.get("dropout_probability", 0.0)
            ),
            use_layer_norm=bool(
                model_configuration.get("use_layer_norm", False)
            ),
            minimum_stiffness_nm_per_deg=float(
                model_configuration.get(
                    "minimum_stiffness_nm_per_deg",
                    5000.0,
                )
            ),
            maximum_stiffness_nm_per_deg=float(
                model_configuration.get(
                    "maximum_stiffness_nm_per_deg",
                    100000.0,
                )
            ),
            initial_stiffness_nm_per_deg=float(
                model_configuration.get(
                    "initial_stiffness_nm_per_deg",
                    27250.0,
                )
            ),
            initial_forward_intercept_deg=float(
                model_configuration.get(
                    "initial_forward_intercept_deg",
                    -0.0217,
                )
            ),
            initial_backward_intercept_deg=float(
                model_configuration.get(
                    "initial_backward_intercept_deg",
                    -0.0116,
                )
            ),
            reference_temperature_deg_c=float(
                model_configuration.get(
                    "reference_temperature_deg_c",
                    30.0,
                )
            ),
            temperature_scale_deg_c=float(
                model_configuration.get(
                    "temperature_scale_deg_c",
                    10.0,
                )
            ),
            nonlinear_torque_scale_nm=float(
                model_configuration.get(
                    "nonlinear_torque_scale_nm",
                    400.0,
                )
            ),
            maximum_nonlinear_amplitude_deg=float(
                model_configuration.get(
                    "maximum_nonlinear_amplitude_deg",
                    0.02,
                )
            ),
            torque_input_mode=str(
                model_configuration.get(
                    "torque_input_mode",
                    "nominal_magnitude",
                )
            ),
        )

    # Create Embryonic Wave 5.1 Grouped Harmonic-Heads Skeleton
    if normalized_model_type == "wave3_grouped_harmonic_heads":
        return Wave3GroupedHarmonicHeadsNetwork(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            harmonic_order=int(model_configuration.get("harmonic_order", 240)),
            coefficient_mode=str(model_configuration.get("coefficient_mode", "linear_conditioned")),
            low_order_harmonic_index_list=model_configuration.get("low_order_harmonic_index_list"),
            stable_middle_harmonic_index_list=model_configuration.get("stable_middle_harmonic_index_list"),
            high_order_harmonic_index_list=model_configuration.get("high_order_harmonic_index_list"),
            residual_hidden_size=list(model_configuration.get("residual_hidden_size", [96, 64])),
            residual_activation_name=str(model_configuration.get("residual_activation_name", "GELU")),
            residual_dropout_probability=float(model_configuration.get("residual_dropout_probability", 0.05)),
            residual_use_layer_norm=bool(model_configuration.get("residual_use_layer_norm", True)),
            low_order_scale=float(model_configuration.get("low_order_scale", 1.0)),
            stable_middle_scale=float(model_configuration.get("stable_middle_scale", 1.0)),
            high_order_scale=float(model_configuration.get("high_order_scale", 1.0)),
            residual_scale=float(model_configuration.get("residual_scale", 1.0)),
            readout_position=str(model_configuration.get("readout_position", "center")),
            freeze_harmonic_heads=bool(model_configuration.get("freeze_harmonic_heads", False)),
        )

    # Create Wave 5.2B Offset And Harmonic Guided Model
    if normalized_model_type == "wave52b_offset_harmonic_guided":
        return Wave52BOffsetHarmonicGuidedNetwork(
            input_size=int(model_configuration["input_size"]),
            output_size=int(model_configuration.get("output_size", 1)),
            base_hidden_size=model_configuration.get("base_hidden_size"),
            offset_hidden_size=model_configuration.get("offset_hidden_size"),
            activation_name=str(model_configuration.get("activation_name", "GELU")),
            dropout_probability=float(model_configuration.get("dropout_probability", 0.05)),
            use_layer_norm=bool(model_configuration.get("use_layer_norm", True)),
            offset_scale=float(model_configuration.get("offset_scale", 1.0)),
            harmonic_scale=float(model_configuration.get("harmonic_scale", 0.0)),
            harmonic_order=int(model_configuration.get("harmonic_order", 240)),
            coefficient_mode=str(model_configuration.get("coefficient_mode", "linear_conditioned")),
            harmonic_index_list=model_configuration.get("harmonic_index_list"),
            readout_position=str(model_configuration.get("readout_position", "center")),
            freeze_harmonic_branch=bool(model_configuration.get("freeze_harmonic_branch", False)),
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
