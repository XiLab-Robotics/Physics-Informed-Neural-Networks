"""Harmonic regression baseline for TE prediction over angular position."""

from __future__ import annotations

# Import Typing Utilities
from collections.abc import Sequence

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
        harmonic_index_list: Sequence[int] | None = None,
    ) -> None:
        """Initialize the harmonic regression baseline.

        Args:
            input_size: Total input feature count including angular position and
                operating-condition features.
            output_size: Regression target count. Scalar output keeps the
                legacy parameter layout for checkpoint compatibility; larger
                values use one harmonic coefficient set per output channel.
            harmonic_order: Highest harmonic order used in the Fourier-style
                expansion of the angular position.
            coefficient_mode: Coefficient parameterization mode. Supported
                values are `static` and `linear_conditioned`.
            harmonic_index_list: Optional explicit harmonic list. When omitted,
                the model uses the backward-compatible contiguous basis
                `1..harmonic_order`. When provided, `0` represents the DC/bias
                term and positive values create sine/cosine feature pairs.
        """

        super().__init__()

        # Validate Architecture Parameters
        assert input_size >= 5, f"Input Size must expose the TE operating-condition features | {input_size}"
        assert output_size > 0, f"Output Size must be positive | {output_size}"
        assert harmonic_order > 0, f"Harmonic Order must be positive | {harmonic_order}"
        resolved_harmonic_index_list = self.resolve_harmonic_index_list(harmonic_order, harmonic_index_list)
        positive_harmonic_index_list = [harmonic_index for harmonic_index in resolved_harmonic_index_list if harmonic_index > 0]

        # Save Architecture Parameters
        self.input_size = input_size
        self.output_size = output_size
        self.harmonic_order = harmonic_order
        self.coefficient_mode = coefficient_mode.strip().lower()
        self.harmonic_index_list = resolved_harmonic_index_list
        self.positive_harmonic_index_list = positive_harmonic_index_list
        self.harmonic_feature_count = 1 + (2 * len(self.positive_harmonic_index_list))

        # Validate Coefficient Mode
        supported_coefficient_mode_list = ["static", "linear_conditioned"]
        assert self.coefficient_mode in supported_coefficient_mode_list, (
            f"Unsupported Coefficient Mode | {coefficient_mode} | Supported: {supported_coefficient_mode_list}"
        )

        # Register Device-Aware Harmonic Index Buffer
        positive_harmonic_index_tensor = torch.tensor(self.positive_harmonic_index_list, dtype=torch.float32)
        self.register_buffer("positive_harmonic_index_tensor", positive_harmonic_index_tensor, persistent=False)

        # Initialize Coefficient Parameterization
        if self.output_size == 1:
            self.base_coefficient_tensor = nn.Parameter(torch.zeros(self.harmonic_feature_count, dtype=torch.float32))
        else:
            self.base_coefficient_tensor = nn.Parameter(
                torch.zeros(self.harmonic_feature_count, self.output_size, dtype=torch.float32)
            )
        self.conditioning_projection = None

        # Initialize Linear Conditioning Projection
        if self.coefficient_mode == "linear_conditioned":
            self.conditioning_projection = nn.Linear(input_size - 1, self.harmonic_feature_count * self.output_size)

    @staticmethod
    def resolve_harmonic_index_list(harmonic_order: int, harmonic_index_list: Sequence[int] | None) -> list[int]:

        """Resolve and validate the configured harmonic basis indices.

        Args:
            harmonic_order: Contiguous harmonic order used when no explicit
                harmonic index list is provided.
            harmonic_index_list: Optional explicit harmonic index sequence.

        Returns:
            list[int]: Sorted unique harmonic indices used by the model.
        """

        # Preserve Current Contiguous Harmonic Basis When No Explicit List Is Provided
        if harmonic_index_list is None:
            return list(range(1, harmonic_order + 1))

        # Validate Explicit Harmonic List
        assert len(harmonic_index_list) > 0, "Harmonic index list must not be empty"

        resolved_harmonic_index_list: list[int] = []
        for harmonic_index in harmonic_index_list:
            resolved_harmonic_index = int(harmonic_index)
            assert resolved_harmonic_index >= 0, f"Harmonic index must be non-negative | {resolved_harmonic_index}"
            resolved_harmonic_index_list.append(resolved_harmonic_index)

        unique_harmonic_index_list = sorted(set(resolved_harmonic_index_list))
        assert len(unique_harmonic_index_list) == len(resolved_harmonic_index_list), (
            f"Harmonic index list contains duplicate entries | {harmonic_index_list}"
        )
        assert any(harmonic_index > 0 for harmonic_index in unique_harmonic_index_list), (
            f"Harmonic index list must contain at least one positive harmonic | {harmonic_index_list}"
        )

        return unique_harmonic_index_list

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
        angular_position_rad = angular_position_deg * (torch.pi / 180.0)
        harmonic_feature_tensor_list = [torch.ones_like(angular_position_rad)]

        # Append Sine And Cosine Features For Each Harmonic Order
        for harmonic_multiplier in self.positive_harmonic_index_tensor:
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
            if self.output_size == 1:
                return self.base_coefficient_tensor.unsqueeze(0).expand(normalized_condition_tensor.shape[0], -1)
            return self.base_coefficient_tensor.unsqueeze(0).expand(normalized_condition_tensor.shape[0], -1, -1)

        # Add Linear Condition-Dependent Coefficient Adjustment
        projected_coefficient_tensor = self.conditioning_projection(normalized_condition_tensor)
        if self.output_size == 1:
            return self.base_coefficient_tensor.unsqueeze(0) + projected_coefficient_tensor

        projected_coefficient_tensor = projected_coefficient_tensor.reshape(
            normalized_condition_tensor.shape[0],
            self.harmonic_feature_count,
            self.output_size,
        )
        return self.base_coefficient_tensor.unsqueeze(0) + projected_coefficient_tensor

    def forward_with_input_context(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Predict TE using raw angle context plus normalized conditions.

        Args:
            input_tensor: Raw input tensor whose first column is the physical
                angular position in degrees.
            normalized_input_tensor: Normalized input tensor used for the
                conditioning features.

        Returns:
            torch.Tensor: TE prediction tensor with shape
            `(batch_size, output_size)`.
        """

        # Extract Angular Position And Condition
        angular_position_deg = input_tensor[:, 0:1]
        normalized_condition_tensor = normalized_input_tensor[:, 1:]

        # Build Harmonic Feature Tensor
        harmonic_feature_tensor = self.build_harmonic_feature_tensor(angular_position_deg)

        # Resolve Harmonic Coefficients
        coefficient_tensor = self.resolve_coefficient_tensor(normalized_condition_tensor)

        # Compute Harmonic Regression
        if self.output_size == 1:
            return torch.sum(harmonic_feature_tensor * coefficient_tensor, dim=-1, keepdim=True)

        return torch.sum(harmonic_feature_tensor.unsqueeze(-1) * coefficient_tensor, dim=1)
