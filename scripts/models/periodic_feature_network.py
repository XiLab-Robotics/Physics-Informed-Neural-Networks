from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Models
from scripts.models.feedforward_network import FeedForwardNetwork

class PeriodicFeatureNetwork(nn.Module):

    """ Periodic Feature Network """

    def __init__(
        self,
        input_size: int,
        hidden_size: list[int],
        output_size: int = 1,
        activation_name: str = "GELU",
        dropout_probability: float = 0.10,
        use_layer_norm: bool = True,
        harmonic_order: int = 8,
        include_raw_angle_feature: bool = True,
    ) -> None:

        super().__init__()

        # Validate Feature Parameters
        assert input_size >= 5, f"Input Size must expose the TE operating-condition features | {input_size}"
        assert harmonic_order > 0, f"Harmonic Order must be positive | {harmonic_order}"

        # Save Feature Parameters
        self.input_size = input_size
        self.output_size = output_size
        self.harmonic_order = harmonic_order
        self.include_raw_angle_feature = include_raw_angle_feature

        # Resolve Expanded Input Size
        harmonic_feature_count = 2 * self.harmonic_order
        raw_angle_feature_count = 1 if self.include_raw_angle_feature else 0
        conditioning_feature_count = input_size - 1
        expanded_input_size = raw_angle_feature_count + harmonic_feature_count + conditioning_feature_count

        # Initialize Expanded Feedforward Backbone
        self.feature_network = FeedForwardNetwork(
            input_size=expanded_input_size,
            hidden_size=hidden_size,
            output_size=output_size,
            activation_name=activation_name,
            dropout_probability=dropout_probability,
            use_layer_norm=use_layer_norm,
        )

    def build_periodic_feature_tensor(self, angular_position_deg: torch.Tensor) -> torch.Tensor:

        """ Build Periodic Feature Tensor """

        # Convert Angular Position To Radians
        angular_position_rad = torch.deg2rad(angular_position_deg)
        periodic_feature_tensor_list: list[torch.Tensor] = []

        # Append Sine And Cosine Features For Each Harmonic Order
        for harmonic_index in range(1, self.harmonic_order + 1):
            harmonic_multiplier = float(harmonic_index)
            periodic_feature_tensor_list.append(torch.sin(harmonic_multiplier * angular_position_rad))
            periodic_feature_tensor_list.append(torch.cos(harmonic_multiplier * angular_position_rad))

        return torch.cat(periodic_feature_tensor_list, dim=-1)

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """ Forward With Input Context """

        # Extract Angular Position And Condition
        angular_position_deg = input_tensor[:, 0:1]
        feature_tensor_list: list[torch.Tensor] = []

        # Optionally Keep The Normalized Raw Angle Feature Together With The Periodic Expansion
        if self.include_raw_angle_feature:
            feature_tensor_list.append(normalized_input_tensor[:, 0:1])

        # Build Periodic Feature Tensor
        feature_tensor_list.append(self.build_periodic_feature_tensor(angular_position_deg))
        feature_tensor_list.append(normalized_input_tensor[:, 1:])

        # Concatenate Features
        expanded_feature_tensor = torch.cat(feature_tensor_list, dim=-1)
        return self.feature_network(expanded_feature_tensor)
