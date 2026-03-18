from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Models
from scripts.models.feedforward_network import FeedForwardNetwork
from scripts.models.harmonic_regression import HarmonicRegression

class ResidualHarmonicNetwork(nn.Module):

    """ Residual Harmonic Network """

    def __init__(
        self,
        input_size: int,
        output_size: int = 1,
        harmonic_order: int = 12,
        coefficient_mode: str = "static",
        residual_hidden_size: list[int] | None = None,
        residual_activation_name: str = "GELU",
        residual_dropout_probability: float = 0.10,
        residual_use_layer_norm: bool = True,
        freeze_structured_branch: bool = False,
    ) -> None:

        super().__init__()

        # Resolve Default Residual Widths
        residual_hidden_size = residual_hidden_size or [64, 64]

        # Initialize Structured Harmonic Branch
        self.structured_branch = HarmonicRegression(
            input_size=input_size,
            output_size=output_size,
            harmonic_order=harmonic_order,
            coefficient_mode=coefficient_mode,
        )

        # Initialize Residual Neural Branch
        self.residual_branch = FeedForwardNetwork(
            input_size=input_size,
            hidden_size=residual_hidden_size,
            output_size=output_size,
            activation_name=residual_activation_name,
            dropout_probability=residual_dropout_probability,
            use_layer_norm=residual_use_layer_norm,
        )

        # Optionally Freeze Structured Parameters
        self.freeze_structured_branch = freeze_structured_branch
        if self.freeze_structured_branch:

            # Disable Structured Gradients
            for structured_parameter in self.structured_branch.parameters():
                structured_parameter.requires_grad = False

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """ Forward With Input Context """

        # Forward Pass Through Structured Harmonic Branch
        structured_prediction_tensor = self.structured_branch.forward_with_input_context(input_tensor, normalized_input_tensor)

        # Forward Pass Through Residual Neural Branch
        residual_prediction_tensor = self.residual_branch(normalized_input_tensor)

        # Combine Structured And Residual Predictions
        return structured_prediction_tensor + residual_prediction_tensor

    def compute_auxiliary_output_dictionary(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> dict[str, torch.Tensor]:

        """ Compute Auxiliary Output Dictionary """

        # Forward Pass Through Structured Harmonic Branch
        structured_prediction_tensor = self.structured_branch.forward_with_input_context(input_tensor, normalized_input_tensor)

        # Forward Pass Through Residual Neural Branch
        residual_prediction_tensor = self.residual_branch(normalized_input_tensor)

        # Return Branch-Level Diagnostics
        return {
            "structured_prediction_tensor": structured_prediction_tensor,
            "residual_prediction_tensor": residual_prediction_tensor,
            "prediction_tensor": structured_prediction_tensor + residual_prediction_tensor,
        }
