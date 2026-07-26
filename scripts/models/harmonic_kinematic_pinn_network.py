"""Harmonic and kinematic PINN components for Wave 5.2 Phase 2."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Models
from scripts.models.feedforward_network import FeedForwardNetwork


class HarmonicKinematicPinnNetwork(nn.Module):
    """Direction-specific angular-oscillator PINN for TE curves.

    The model separates an angle-independent offset from one component per
    configured output order. In ``explicit_fourier`` mode, condition-dependent
    sine and cosine coefficients form the parameter-matched non-PINN control.
    In ``implicit_pinn`` mode, each component head may depart from the exact
    harmonic law and is regularized through a differentiable angular
    oscillator residual.
    """

    SUPPORTED_HEAD_MODE_SET = {"explicit_fourier", "implicit_pinn"}

    def __init__(
        self,
        input_size: int,
        harmonic_index_list: list[int],
        condition_hidden_size: list[int],
        condition_latent_size: int,
        component_hidden_size: list[int],
        output_size: int = 1,
        head_mode: str = "implicit_pinn",
        activation_name: str = "Tanh",
        dropout_probability: float = 0.0,
        use_layer_norm: bool = False,
        analytical_anchor_feature_mean: list[float] | None = None,
        analytical_anchor_feature_scale: list[float] | None = None,
        analytical_anchor_coefficient_matrix: list[list[float]] | None = None,
    ) -> None:
        """Initialize the Phase 2 harmonic-kinematic model.

        Args:
            input_size: Input width including output angle in column zero.
            harmonic_index_list: Positive output orders represented explicitly.
            condition_hidden_size: Hidden widths of the condition encoder.
            condition_latent_size: Width of the causal condition embedding.
            component_hidden_size: Hidden widths of each implicit component.
            output_size: Scalar TE output count. Phase 2 requires one.
            head_mode: ``explicit_fourier`` control or ``implicit_pinn``.
            activation_name: Activation used in the condition and component
                networks.
            dropout_probability: Hidden dropout probability.
            use_layer_norm: Whether hidden layers use layer normalization.
            analytical_anchor_feature_mean: Optional three-variable Bauer
                surface normalization mean.
            analytical_anchor_feature_scale: Optional three-variable Bauer
                surface normalization scale.
            analytical_anchor_coefficient_matrix: Optional complete-quadratic
                coefficient surface with offset and sine/cosine columns.
        """

        super().__init__()

        # Validate Model Contract
        assert input_size >= 4, (
            "Phase 2 PINN requires angle, speed, torque, and temperature"
        )
        assert output_size == 1, "Phase 2 currently supports scalar TE only"
        assert condition_latent_size > 0
        assert len(condition_hidden_size) > 0
        assert len(component_hidden_size) > 0
        normalized_head_mode = str(head_mode).strip().lower()
        assert normalized_head_mode in self.SUPPORTED_HEAD_MODE_SET, (
            f"Unsupported Phase 2 head mode | {head_mode}"
        )
        resolved_harmonic_index_list = sorted(
            {int(value) for value in harmonic_index_list}
        )
        assert resolved_harmonic_index_list
        assert all(value > 0 for value in resolved_harmonic_index_list)

        # Save Inspectable Model Metadata
        self.input_size = int(input_size)
        self.condition_input_size = self.input_size - 1
        self.output_size = int(output_size)
        self.head_mode = normalized_head_mode
        self.harmonic_index_list = resolved_harmonic_index_list
        self.condition_latent_size = int(condition_latent_size)

        # Register Device-Aware Harmonic Orders
        harmonic_index_tensor = torch.as_tensor(
            self.harmonic_index_list,
            dtype=torch.float32,
        )
        self.register_buffer(
            "harmonic_index_tensor",
            harmonic_index_tensor,
            persistent=True,
        )

        # Register The Optional Frozen Phase 1 Analytical Surface
        analytical_anchor_value_list = [
            analytical_anchor_feature_mean,
            analytical_anchor_feature_scale,
            analytical_anchor_coefficient_matrix,
        ]
        self.has_analytical_anchor = all(
            value is not None for value in analytical_anchor_value_list
        )
        assert self.has_analytical_anchor or all(
            value is None for value in analytical_anchor_value_list
        ), "Analytical anchor payload must be either complete or absent"
        if self.has_analytical_anchor:
            feature_mean_tensor = torch.as_tensor(
                analytical_anchor_feature_mean,
                dtype=torch.float32,
            )
            feature_scale_tensor = torch.as_tensor(
                analytical_anchor_feature_scale,
                dtype=torch.float32,
            )
            coefficient_matrix_tensor = torch.as_tensor(
                analytical_anchor_coefficient_matrix,
                dtype=torch.float32,
            )
            expected_coefficient_count = 1 + (2 * len(self.harmonic_index_list))
            assert tuple(feature_mean_tensor.shape) == (3,)
            assert tuple(feature_scale_tensor.shape) == (3,)
            assert torch.all(feature_scale_tensor > 0.0)
            assert tuple(coefficient_matrix_tensor.shape) == (
                10,
                expected_coefficient_count,
            )
        else:
            feature_mean_tensor = torch.empty(0, dtype=torch.float32)
            feature_scale_tensor = torch.empty(0, dtype=torch.float32)
            coefficient_matrix_tensor = torch.empty((0, 0), dtype=torch.float32)
        self.register_buffer(
            "analytical_anchor_feature_mean",
            feature_mean_tensor,
            persistent=True,
        )
        self.register_buffer(
            "analytical_anchor_feature_scale",
            feature_scale_tensor,
            persistent=True,
        )
        self.register_buffer(
            "analytical_anchor_coefficient_matrix",
            coefficient_matrix_tensor,
            persistent=True,
        )

        # Build The Causal Operating-Condition Encoder
        self.condition_encoder = FeedForwardNetwork(
            input_size=self.condition_input_size,
            hidden_size=condition_hidden_size,
            output_size=self.condition_latent_size,
            activation_name=activation_name,
            dropout_probability=dropout_probability,
            use_layer_norm=use_layer_norm,
        )
        self.offset_head = nn.Linear(self.condition_latent_size, 1)

        # Build The Parameter-Matched Fourier Control Or Implicit PINN Heads
        harmonic_count = len(self.harmonic_index_list)
        self.explicit_coefficient_head: nn.Module | None = None
        self.implicit_component_head_map = nn.ModuleDict()
        if self.head_mode == "explicit_fourier":
            self.explicit_coefficient_head = nn.Linear(
                self.condition_latent_size,
                2 * harmonic_count,
            )
        else:
            component_input_size = self.condition_latent_size + 3
            for harmonic_index in self.harmonic_index_list:
                self.implicit_component_head_map[str(harmonic_index)] = (
                    FeedForwardNetwork(
                        input_size=component_input_size,
                        hidden_size=component_hidden_size,
                        output_size=1,
                        activation_name=activation_name,
                        dropout_probability=dropout_probability,
                        use_layer_norm=use_layer_norm,
                    )
                )

    def _compute_condition_latent_tensor(
        self,
        normalized_condition_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Encode causal condition features without target information."""

        assert normalized_condition_tensor.ndim == 2
        assert normalized_condition_tensor.shape[1] == self.condition_input_size
        return self.condition_encoder(normalized_condition_tensor)

    def _compute_component_tensor(
        self,
        theta_rad_tensor: torch.Tensor,
        condition_latent_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Compute one component column per configured output order."""

        assert theta_rad_tensor.ndim == 2
        assert theta_rad_tensor.shape[1] == 1
        assert condition_latent_tensor.shape[0] == theta_rad_tensor.shape[0]

        component_tensor_list: list[torch.Tensor] = []
        if self.head_mode == "explicit_fourier":
            assert self.explicit_coefficient_head is not None
            coefficient_tensor = self.explicit_coefficient_head(
                condition_latent_tensor
            )
            sine_coefficient_tensor, cosine_coefficient_tensor = torch.chunk(
                coefficient_tensor,
                chunks=2,
                dim=-1,
            )
            order_tensor = self.harmonic_index_tensor.to(
                dtype=theta_rad_tensor.dtype
            ).reshape(1, -1)
            component_tensor = (
                sine_coefficient_tensor * torch.sin(theta_rad_tensor * order_tensor)
                + cosine_coefficient_tensor
                * torch.cos(theta_rad_tensor * order_tensor)
            )
            return component_tensor

        # Permit Angular Departures That The Governing Residual Must Constrain
        normalized_theta_tensor = (theta_rad_tensor / torch.pi) - 1.0
        for harmonic_index in self.harmonic_index_list:
            harmonic_value = float(harmonic_index)
            component_input_tensor = torch.cat(
                (
                    condition_latent_tensor,
                    normalized_theta_tensor,
                    torch.sin(harmonic_value * theta_rad_tensor),
                    torch.cos(harmonic_value * theta_rad_tensor),
                ),
                dim=-1,
            )
            component_tensor_list.append(
                self.implicit_component_head_map[str(harmonic_index)](
                    component_input_tensor
                )
            )
        return torch.cat(component_tensor_list, dim=-1)

    def _compute_from_theta_and_condition(
        self,
        theta_rad_tensor: torch.Tensor,
        normalized_condition_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        """Compute offset, harmonic components, and total prediction."""

        condition_latent_tensor = self._compute_condition_latent_tensor(
            normalized_condition_tensor
        )
        offset_prediction_tensor = self.offset_head(condition_latent_tensor)
        harmonic_component_tensor = self._compute_component_tensor(
            theta_rad_tensor,
            condition_latent_tensor,
        )
        harmonic_prediction_tensor = torch.sum(
            harmonic_component_tensor,
            dim=-1,
            keepdim=True,
        )
        prediction_tensor = offset_prediction_tensor + harmonic_prediction_tensor
        return {
            "condition_latent_tensor": condition_latent_tensor,
            "offset_prediction_tensor": offset_prediction_tensor,
            "harmonic_component_tensor": harmonic_component_tensor,
            "harmonic_prediction_tensor": harmonic_prediction_tensor,
            "prediction_tensor": prediction_tensor,
        }

    def compute_auxiliary_output_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        """Expose inspectable offset and harmonic component predictions."""

        assert input_tensor.ndim == 2
        assert normalized_input_tensor.ndim == 2
        assert input_tensor.shape == normalized_input_tensor.shape
        assert input_tensor.shape[1] == self.input_size
        theta_rad_tensor = torch.deg2rad(input_tensor[:, 0:1])
        normalized_condition_tensor = normalized_input_tensor[:, 1:]
        return self._compute_from_theta_and_condition(
            theta_rad_tensor,
            normalized_condition_tensor,
        )

    def compute_analytical_anchor_prediction_tensor(
        self,
        input_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Evaluate the frozen Phase 1 Bauer surface in physical TE degrees."""

        assert self.has_analytical_anchor, "Analytical anchor is not configured"
        assert input_tensor.ndim == 2
        assert input_tensor.shape[1] == self.input_size

        # Recreate The Phase 1 Signed-Torque, Absolute-Speed, Temperature Basis
        operating_feature_tensor = torch.cat(
            (
                input_tensor[:, 2:3],
                torch.abs(input_tensor[:, 1:2]),
                input_tensor[:, 3:4],
            ),
            dim=-1,
        )
        standardized_feature_tensor = (
            operating_feature_tensor - self.analytical_anchor_feature_mean
        ) / self.analytical_anchor_feature_scale
        torque_tensor = standardized_feature_tensor[:, 0:1]
        speed_tensor = standardized_feature_tensor[:, 1:2]
        temperature_tensor = standardized_feature_tensor[:, 2:3]
        design_tensor = torch.cat(
            (
                torch.square(torque_tensor),
                torch.square(speed_tensor),
                torch.square(temperature_tensor),
                torque_tensor * speed_tensor,
                torque_tensor * temperature_tensor,
                speed_tensor * temperature_tensor,
                torque_tensor,
                speed_tensor,
                temperature_tensor,
                torch.ones_like(torque_tensor),
            ),
            dim=-1,
        )
        coefficient_tensor = (
            design_tensor @ self.analytical_anchor_coefficient_matrix
        )

        # Reconstruct The Direction-Specific Polynomial-Fourier Curve
        theta_rad_tensor = torch.deg2rad(input_tensor[:, 0:1])
        analytical_prediction_tensor = coefficient_tensor[:, 0:1]
        for harmonic_position, harmonic_index in enumerate(
            self.harmonic_index_list
        ):
            sine_coefficient_tensor = coefficient_tensor[
                :,
                1 + (2 * harmonic_position) : 2 + (2 * harmonic_position),
            ]
            cosine_coefficient_tensor = coefficient_tensor[
                :,
                2 + (2 * harmonic_position) : 3 + (2 * harmonic_position),
            ]
            analytical_prediction_tensor = analytical_prediction_tensor + (
                sine_coefficient_tensor
                * torch.sin(float(harmonic_index) * theta_rad_tensor)
                + cosine_coefficient_tensor
                * torch.cos(float(harmonic_index) * theta_rad_tensor)
            )
        return analytical_prediction_tensor

    @staticmethod
    def compute_normalized_oscillator_residual(
        component_tensor: torch.Tensor,
        theta_rad_tensor: torch.Tensor,
        harmonic_index: int,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Compute first derivative, second derivative, and normalized residual."""

        assert component_tensor.shape == theta_rad_tensor.shape
        assert theta_rad_tensor.requires_grad
        first_derivative_tensor = torch.autograd.grad(
            outputs=component_tensor,
            inputs=theta_rad_tensor,
            grad_outputs=torch.ones_like(component_tensor),
            create_graph=True,
            retain_graph=True,
            allow_unused=False,
        )[0]
        second_derivative_tensor = torch.autograd.grad(
            outputs=first_derivative_tensor,
            inputs=theta_rad_tensor,
            grad_outputs=torch.ones_like(first_derivative_tensor),
            create_graph=True,
            retain_graph=True,
            allow_unused=False,
        )[0]
        harmonic_index_squared = float(harmonic_index * harmonic_index)
        normalized_residual_tensor = (
            second_derivative_tensor / harmonic_index_squared
            + component_tensor
        )
        return (
            first_derivative_tensor,
            second_derivative_tensor,
            normalized_residual_tensor,
        )

    def compute_physics_residual_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
        maximum_collocation_points: int = 256,
        maximum_boundary_conditions: int = 16,
        target_mean_tensor: torch.Tensor | None = None,
        target_std_tensor: torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:
        """Compute target-free oscillator and periodic-boundary losses."""

        assert maximum_collocation_points > 0
        assert maximum_boundary_conditions > 0
        assert input_tensor.ndim == normalized_input_tensor.ndim == 2
        assert input_tensor.shape == normalized_input_tensor.shape

        # Higher-Order Derivatives Must Remain Enabled During Validation Too
        with torch.inference_mode(False), torch.enable_grad():
            collocation_count = min(
                int(input_tensor.shape[0]),
                int(maximum_collocation_points),
            )
            collocation_index_tensor = torch.linspace(
                0,
                input_tensor.shape[0] - 1,
                steps=collocation_count,
                device=input_tensor.device,
            ).round().long()
            selected_input_tensor = input_tensor.index_select(
                0,
                collocation_index_tensor,
            )
            selected_normalized_input_tensor = normalized_input_tensor.index_select(
                0,
                collocation_index_tensor,
            )
            theta_rad_tensor = torch.deg2rad(
                selected_input_tensor[:, 0:1]
            ).detach().clone().requires_grad_(True)
            normalized_condition_tensor = (
                selected_normalized_input_tensor[:, 1:].detach().clone()
            )
            physics_output_dictionary = (
                self._compute_from_theta_and_condition(
                    theta_rad_tensor,
                    normalized_condition_tensor,
                )
            )
            harmonic_component_tensor = physics_output_dictionary[
                "harmonic_component_tensor"
            ]

            # Evaluate One Governing Residual Per Interpretable Component Head
            oscillator_loss_list: list[torch.Tensor] = []
            for harmonic_position, harmonic_index in enumerate(
                self.harmonic_index_list
            ):
                component_tensor = harmonic_component_tensor[
                    :,
                    harmonic_position : harmonic_position + 1,
                ]
                _, _, residual_tensor = (
                    self.compute_normalized_oscillator_residual(
                        component_tensor,
                        theta_rad_tensor,
                        harmonic_index,
                    )
                )
                oscillator_loss_list.append(torch.mean(torch.square(residual_tensor)))
            oscillator_residual_loss = torch.stack(
                oscillator_loss_list
            ).mean()

            # Evaluate Periodic Value And Slope Closure At Matched Conditions
            boundary_count = min(
                int(normalized_condition_tensor.shape[0]),
                int(maximum_boundary_conditions),
            )
            boundary_condition_tensor = normalized_condition_tensor[
                :boundary_count
            ]
            theta_zero_tensor = torch.zeros(
                (boundary_count, 1),
                device=input_tensor.device,
                dtype=input_tensor.dtype,
                requires_grad=True,
            )
            theta_period_tensor = torch.full(
                (boundary_count, 1),
                fill_value=2.0 * torch.pi,
                device=input_tensor.device,
                dtype=input_tensor.dtype,
                requires_grad=True,
            )
            zero_prediction_tensor = self._compute_from_theta_and_condition(
                theta_zero_tensor,
                boundary_condition_tensor,
            )["prediction_tensor"]
            period_prediction_tensor = self._compute_from_theta_and_condition(
                theta_period_tensor,
                boundary_condition_tensor,
            )["prediction_tensor"]
            zero_slope_tensor = torch.autograd.grad(
                zero_prediction_tensor,
                theta_zero_tensor,
                grad_outputs=torch.ones_like(zero_prediction_tensor),
                create_graph=True,
                retain_graph=True,
                allow_unused=False,
            )[0]
            period_slope_tensor = torch.autograd.grad(
                period_prediction_tensor,
                theta_period_tensor,
                grad_outputs=torch.ones_like(period_prediction_tensor),
                create_graph=True,
                retain_graph=True,
                allow_unused=False,
            )[0]
            periodic_value_loss = torch.mean(
                torch.square(zero_prediction_tensor - period_prediction_tensor)
            )
            periodic_slope_loss = torch.mean(
                torch.square(zero_slope_tensor - period_slope_tensor)
            )

            # Compare Against The Frozen Direction-Specific Bauer Surface
            analytical_anchor_loss = torch.zeros_like(oscillator_residual_loss)
            if self.has_analytical_anchor:
                assert target_mean_tensor is not None
                assert target_std_tensor is not None
                analytical_anchor_prediction_tensor = (
                    self.compute_analytical_anchor_prediction_tensor(
                        selected_input_tensor
                    )
                )
                normalized_analytical_anchor_tensor = (
                    analytical_anchor_prediction_tensor - target_mean_tensor
                ) / target_std_tensor
                analytical_anchor_loss = torch.mean(
                    torch.square(
                        physics_output_dictionary["prediction_tensor"]
                        - normalized_analytical_anchor_tensor
                    )
                )

        return {
            "physics_oscillator_residual_loss": oscillator_residual_loss,
            "physics_periodic_value_loss": periodic_value_loss,
            "physics_periodic_slope_loss": periodic_slope_loss,
            "physics_analytical_anchor_loss": analytical_anchor_loss,
            "physics_collocation_point_count": torch.as_tensor(
                collocation_count,
                device=input_tensor.device,
                dtype=input_tensor.dtype,
            ),
            "physics_boundary_condition_count": torch.as_tensor(
                boundary_count,
                device=input_tensor.device,
                dtype=input_tensor.dtype,
            ),
        }

    def forward_with_input_context(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Predict normalized TE with raw angular context."""

        return self.compute_auxiliary_output_dictionary(
            input_tensor,
            normalized_input_tensor,
        )["prediction_tensor"]

    def forward(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:
        """Fallback forward path when raw context is unavailable."""

        return self.compute_auxiliary_output_dictionary(
            normalized_input_tensor,
            normalized_input_tensor,
        )["prediction_tensor"]
