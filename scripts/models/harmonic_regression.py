"""Harmonic regression baseline for TE prediction over angular position."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

class HarmonicRegression(nn.Module):

    """Structured harmonic regressor for periodic TE components."""

    def __init__(
        self,
        input_size: int,
        output_size: int = 1,
        harmonic_order: int = 12,
        coefficient_mode: str = "static",
    ) -> None:
        """Initialize the harmonic regression baseline.

        Args:
            input_size: Total input feature count including angular position and
                operating-condition features.
            output_size: Regression target count. The current implementation
                supports scalar TE output only.
            harmonic_order: Highest harmonic order used in the Fourier-style
                expansion of the angular position.
            coefficient_mode: Coefficient parameterization mode. Supported
                values are `static` and `linear_conditioned`.
        """

        super().__init__()

        # Validate Architecture Parameters
        assert input_size >= 5, f"Input Size must expose the TE operating-condition features | {input_size}"
        assert output_size == 1, f"Harmonic Regression currently supports scalar TE output only | {output_size}"
        assert harmonic_order > 0, f"Harmonic Order must be positive | {harmonic_order}"

        # Save Architecture Parameters
        self.input_size = input_size
        self.output_size = output_size
        self.harmonic_order = harmonic_order
        self.coefficient_mode = coefficient_mode.strip().lower()
        self.harmonic_feature_count = 1 + (2 * self.harmonic_order)

        # Validate Coefficient Mode
        supported_coefficient_mode_list = ["static", "linear_conditioned"]
        assert self.coefficient_mode in supported_coefficient_mode_list, (
            f"Unsupported Coefficient Mode | {coefficient_mode} | Supported: {supported_coefficient_mode_list}"
        )

        # Initialize Coefficient Parameterization
        self.base_coefficient_tensor = nn.Parameter(torch.zeros(self.harmonic_feature_count, dtype=torch.float32))
        self.conditioning_projection = None

        # Initialize Linear Conditioning Projection
        if self.coefficient_mode == "linear_conditioned":
            self.conditioning_projection = nn.Linear(input_size - 1, self.harmonic_feature_count)

    def build_harmonic_feature_tensor(self, angular_position_deg: torch.Tensor) -> torch.Tensor:

        """Build the harmonic basis evaluated at the given angular positions.

        Args:
            angular_position_deg: Angular position tensor in degrees with shape
                `(batch_size, 1)`.

        Returns:
            torch.Tensor: Harmonic design matrix containing the bias term plus
            sine and cosine features for each configured harmonic order.
        """

        # Convert Angular Position To Radians
        angular_position_rad = torch.deg2rad(angular_position_deg)
        harmonic_feature_tensor_list = [torch.ones_like(angular_position_rad)]

        # Append Sine And Cosine Features For Each Harmonic Order
        for harmonic_index in range(1, self.harmonic_order + 1):
            harmonic_multiplier = float(harmonic_index)
            harmonic_feature_tensor_list.append(torch.sin(harmonic_multiplier * angular_position_rad))
            harmonic_feature_tensor_list.append(torch.cos(harmonic_multiplier * angular_position_rad))

        # Concatenate Harmonic Features
        return torch.cat(harmonic_feature_tensor_list, dim=-1)

    def resolve_coefficient_tensor(self, normalized_condition_tensor: torch.Tensor) -> torch.Tensor:

        """Resolve the harmonic coefficient tensor for each batch item.

        Args:
            normalized_condition_tensor: Normalized operating-condition feature
                tensor excluding the raw angle column.

        Returns:
            torch.Tensor: Batch-aligned coefficient tensor used to weight the
            harmonic basis.
        """

        # Use Shared Global Coefficients In Static Mode
        if self.conditioning_projection is None:
            return self.base_coefficient_tensor.unsqueeze(0).expand(normalized_condition_tensor.shape[0], -1)

        # Add Linear Condition-Dependent Coefficient Adjustment
        return self.base_coefficient_tensor.unsqueeze(0) + self.conditioning_projection(normalized_condition_tensor)

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Predict TE using raw angle context plus normalized conditions.

        Args:
            input_tensor: Raw input tensor whose first column is the physical
                angular position in degrees.
            normalized_input_tensor: Normalized input tensor used for the
                conditioning features.

        Returns:
            torch.Tensor: Scalar TE prediction tensor with shape
            `(batch_size, 1)`.
        """

        # Extract Angular Position And Condition
        angular_position_deg = input_tensor[:, 0:1]
        normalized_condition_tensor = normalized_input_tensor[:, 1:]

        # Build Harmonic Feature Tensor
        harmonic_feature_tensor = self.build_harmonic_feature_tensor(angular_position_deg)

        # Resolve Harmonic Coefficients
        coefficient_tensor = self.resolve_coefficient_tensor(normalized_condition_tensor)

        # Compute Harmonic Regression
        return torch.sum(harmonic_feature_tensor * coefficient_tensor, dim=-1, keepdim=True)
