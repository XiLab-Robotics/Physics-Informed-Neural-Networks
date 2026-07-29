"""Bounded coordinate residual models for Wave 5.2R Stage 6."""

from __future__ import annotations

# Import Standard Utilities
import math

# Import PyTorch Utilities
import torch
import torch.nn as nn


class SineLayer(nn.Module):
    """Apply one SIREN-compatible affine layer and sine activation."""

    def __init__(
        self,
        input_size: int,
        output_size: int,
        *,
        omega_0: float,
        first_layer: bool,
    ) -> None:
        """Initialize one periodic layer with the prescribed weight scale."""

        super().__init__()
        assert input_size > 0
        assert output_size > 0
        assert omega_0 > 0.0

        self.input_size = int(input_size)
        self.omega_0 = float(omega_0)
        self.linear = nn.Linear(input_size, output_size)

        # Use The SIREN Initialization Envelope
        if first_layer:
            bound = 1.0 / float(input_size)
        else:
            bound = math.sqrt(6.0 / float(input_size)) / self.omega_0
        nn.init.uniform_(self.linear.weight, -bound, bound)
        nn.init.zeros_(self.linear.bias)

    def forward(self, input_tensor: torch.Tensor) -> torch.Tensor:
        """Return the sinusoidally activated affine output."""

        return torch.sin(self.omega_0 * self.linear(input_tensor))


class BoundedCoordinateResidualNetwork(nn.Module):
    """Add one bounded low-rank angular residual to a PF-A curve.

    The network factorizes the residual into condition weights and shared
    angular basis functions. This evaluates a complete uniform curve with one
    matrix multiplication while keeping the analytical PF-A contribution and
    learned correction separately inspectable.
    """

    SUPPORTED_ANGULAR_ARCHITECTURE_SET = {
        "raw_circular_tanh",
        "fourier_feature_tanh",
        "coordinate_tanh",
        "siren",
    }

    def __init__(
        self,
        condition_input_size: int,
        harmonic_order_list: list[int],
        angular_sample_count: int,
        angular_architecture: str,
        residual_bound_list: list[float],
        *,
        rank: int = 12,
        condition_hidden_size: int = 64,
        angular_hidden_size: int = 64,
        fourier_feature_order_list: list[int] | None = None,
        siren_omega_0: float = 30.0,
    ) -> None:
        """Initialize one low-rank bounded coordinate residual.

        Args:
            condition_input_size: Number of causal normalized setpoint inputs.
            harmonic_order_list: PF-A coefficient reconstruction orders.
            angular_sample_count: Uniform samples in one complete cycle.
            angular_architecture: Angular basis implementation.
            residual_bound_list: Training-only physical-unit bounds per angle.
            rank: Shared low-rank residual dimension.
            condition_hidden_size: Condition-network hidden width.
            angular_hidden_size: Angular-network hidden width.
            fourier_feature_order_list: Frozen angular feature orders.
            siren_omega_0: SIREN activation frequency scale.
        """

        super().__init__()

        # Validate The Immutable Curve Contract
        normalized_architecture = str(angular_architecture).strip().lower()
        resolved_order_list = [int(value) for value in harmonic_order_list]
        resolved_feature_order_list = [
            int(value)
            for value in (
                fourier_feature_order_list
                or [1, 3, 39, 40, 78, 81, 156, 162, 240]
            )
        ]
        assert condition_input_size > 0
        assert resolved_order_list
        assert angular_sample_count >= 512
        assert normalized_architecture in (
            self.SUPPORTED_ANGULAR_ARCHITECTURE_SET
        )
        assert rank > 0
        assert condition_hidden_size > 0
        assert angular_hidden_size > 0
        assert resolved_feature_order_list

        self.condition_input_size = int(condition_input_size)
        self.harmonic_order_list = resolved_order_list
        self.angular_sample_count = int(angular_sample_count)
        self.angular_architecture = normalized_architecture
        self.rank = int(rank)
        self.coefficient_count = 1 + (2 * len(resolved_order_list))

        # Register The PF-A Reconstruction Basis
        theta_tensor = torch.linspace(
            0.0,
            2.0 * torch.pi,
            steps=self.angular_sample_count + 1,
            dtype=torch.float32,
        )[:-1]
        reconstruction_column_list = [torch.ones_like(theta_tensor)]
        for harmonic_order in resolved_order_list:
            reconstruction_column_list.extend(
                [
                    torch.sin(float(harmonic_order) * theta_tensor),
                    torch.cos(float(harmonic_order) * theta_tensor),
                ]
            )
        reconstruction_matrix = torch.stack(
            reconstruction_column_list,
            dim=0,
        )
        self.register_buffer(
            "reconstruction_matrix",
            reconstruction_matrix,
            persistent=True,
        )

        # Register The Physical Residual Envelope
        residual_bound_tensor = torch.as_tensor(
            residual_bound_list,
            dtype=torch.float32,
        )
        assert tuple(residual_bound_tensor.shape) == (
            self.angular_sample_count,
        )
        assert bool(torch.all(residual_bound_tensor > 0.0))
        self.register_buffer(
            "residual_bound",
            residual_bound_tensor,
            persistent=True,
        )

        # Build The Condition-Specific Low-Rank Weights
        self.condition_network = nn.Sequential(
            nn.Linear(self.condition_input_size, condition_hidden_size),
            nn.Tanh(),
            nn.Linear(condition_hidden_size, condition_hidden_size),
            nn.Tanh(),
            nn.Linear(condition_hidden_size, self.rank),
        )
        condition_output_layer = self.condition_network[-1]
        assert isinstance(condition_output_layer, nn.Linear)
        nn.init.zeros_(condition_output_layer.weight)
        nn.init.zeros_(condition_output_layer.bias)

        # Freeze The Angular Coordinate Inputs
        normalized_theta_tensor = (
            theta_tensor / torch.pi
        ) - 1.0
        if normalized_architecture == "raw_circular_tanh":
            angular_input_tensor = torch.stack(
                [torch.sin(theta_tensor), torch.cos(theta_tensor)],
                dim=1,
            )
        elif normalized_architecture == "fourier_feature_tanh":
            angular_feature_list = []
            for harmonic_order in resolved_feature_order_list:
                angular_feature_list.extend(
                    [
                        torch.sin(float(harmonic_order) * theta_tensor),
                        torch.cos(float(harmonic_order) * theta_tensor),
                    ]
                )
            angular_input_tensor = torch.stack(
                angular_feature_list,
                dim=1,
            )
        else:
            angular_input_tensor = normalized_theta_tensor.unsqueeze(1)
        self.register_buffer(
            "angular_input_tensor",
            angular_input_tensor,
            persistent=True,
        )

        # Build One Matched Angular Basis Network
        angular_input_size = int(angular_input_tensor.shape[1])
        if normalized_architecture == "siren":
            self.angular_network = nn.Sequential(
                SineLayer(
                    angular_input_size,
                    angular_hidden_size,
                    omega_0=siren_omega_0,
                    first_layer=True,
                ),
                nn.Linear(angular_hidden_size, self.rank),
            )
            final_angular_layer = self.angular_network[-1]
            assert isinstance(final_angular_layer, nn.Linear)
            final_bound = (
                math.sqrt(6.0 / float(angular_hidden_size))
                / float(siren_omega_0)
            )
            nn.init.uniform_(
                final_angular_layer.weight,
                -final_bound,
                final_bound,
            )
            nn.init.zeros_(final_angular_layer.bias)
        else:
            self.angular_network = nn.Sequential(
                nn.Linear(angular_input_size, angular_hidden_size),
                nn.Tanh(),
                nn.Linear(angular_hidden_size, self.rank),
            )

    def reconstruct_anchor_curve(
        self,
        anchor_coefficient_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Reconstruct PF-A on the immutable angular grid."""

        assert anchor_coefficient_tensor.shape[-1] == self.coefficient_count
        return anchor_coefficient_tensor @ self.reconstruction_matrix

    def forward(
        self,
        condition_tensor: torch.Tensor,
        anchor_coefficient_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        """Return PF-A, bounded residual, and complete curve prediction."""

        assert condition_tensor.ndim == 2
        assert condition_tensor.shape[-1] == self.condition_input_size
        assert anchor_coefficient_tensor.shape == (
            condition_tensor.shape[0],
            self.coefficient_count,
        )

        # Evaluate And Normalize The Shared Angular Basis
        angular_basis_tensor = self.angular_network(
            self.angular_input_tensor
        )
        angular_basis_scale = torch.sqrt(
            torch.mean(
                torch.square(angular_basis_tensor),
                dim=0,
                keepdim=True,
            )
            + 1.0e-8
        )
        normalized_angular_basis_tensor = (
            angular_basis_tensor / angular_basis_scale
        )

        # Form One Bounded Condition-Dependent Residual
        condition_weight_tensor = self.condition_network(condition_tensor)
        raw_residual_tensor = (
            condition_weight_tensor
            @ normalized_angular_basis_tensor.transpose(0, 1)
        ) / math.sqrt(float(self.rank))
        bounded_residual_tensor = (
            self.residual_bound.unsqueeze(0)
            * torch.tanh(raw_residual_tensor)
        )

        analytical_curve_tensor = self.reconstruct_anchor_curve(
            anchor_coefficient_tensor
        )
        prediction_curve_tensor = (
            analytical_curve_tensor + bounded_residual_tensor
        )
        zero_coefficient_tensor = torch.zeros_like(
            anchor_coefficient_tensor
        )
        return {
            "prediction_curve": prediction_curve_tensor,
            "prediction_coefficients": anchor_coefficient_tensor,
            "analytical_anchor_coefficients": anchor_coefficient_tensor,
            "analytical_contribution_curve": analytical_curve_tensor,
            "coefficient_correction": zero_coefficient_tensor,
            "coordinate_residual_curve": bounded_residual_tensor,
            "condition_weight_tensor": condition_weight_tensor,
            "angular_basis_tensor": normalized_angular_basis_tensor,
        }
