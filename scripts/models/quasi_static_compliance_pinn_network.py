"""Quasi-static compliance and elastic-offset PINNs for Wave 5.2 Phase 3."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Models
from scripts.models.feedforward_network import FeedForwardNetwork


class QuasiStaticCompliancePinnNetwork(nn.Module):

    """Predict TE through periodic and quasi-static mean components.

    ``C0`` is the non-PINN learned-mean control. ``C1`` through ``C3`` expose
    a learned mean surface and a differentiable compliance residual with
    respect to signed torque. ``C4`` and ``C5`` embed the elastic equation
    directly in the forward path. Every formulation uses an explicit
    condition-dependent Fourier branch whose continuous-cycle mean is zero.
    """

    SUPPORTED_FORMULATION_SET = {"C0", "C1", "C2", "C3", "C4", "C5"}
    SOFT_RESIDUAL_FORMULATION_SET = {"C1", "C2", "C3"}
    HARD_EQUATION_FORMULATION_SET = {"C4", "C5"}

    def __init__(
        self,
        input_size: int,
        harmonic_index_list: list[int],
        condition_hidden_size: list[int],
        condition_latent_size: int,
        mean_hidden_size: list[int],
        output_size: int = 1,
        formulation: str = "C1",
        activation_name: str = "Tanh",
        dropout_probability: float = 0.0,
        use_layer_norm: bool = False,
        minimum_stiffness_nm_per_deg: float = 5000.0,
        maximum_stiffness_nm_per_deg: float = 100000.0,
        initial_stiffness_nm_per_deg: float = 27250.0,
        initial_forward_intercept_deg: float = -0.0217,
        initial_backward_intercept_deg: float = -0.0116,
        reference_temperature_deg_c: float = 30.0,
        temperature_scale_deg_c: float = 10.0,
        nonlinear_torque_scale_nm: float = 400.0,
        maximum_nonlinear_amplitude_deg: float = 0.02,
        torque_input_mode: str = "nominal_magnitude",
    ) -> None:

        """Initialize one Phase 3 compliance formulation.

        Args:
            input_size: Input width ordered as angle, speed, torque,
                temperature, and direction flag.
            harmonic_index_list: Positive output orders in the periodic branch.
            condition_hidden_size: Hidden widths of the condition encoder.
            condition_latent_size: Width of the causal condition embedding.
            mean_hidden_size: Hidden widths of the learned mean surface.
            output_size: Scalar TE output count.
            formulation: One of ``C0`` through ``C5``.
            activation_name: Activation used by learned branches.
            dropout_probability: Hidden dropout probability.
            use_layer_norm: Whether learned branches use layer normalization.
            minimum_stiffness_nm_per_deg: Strict lower stiffness bound.
            maximum_stiffness_nm_per_deg: Strict upper stiffness bound.
            initial_stiffness_nm_per_deg: Audit-backed initialization.
            initial_forward_intercept_deg: Forward zero-torque mean.
            initial_backward_intercept_deg: Backward zero-torque mean.
            reference_temperature_deg_c: Temperature-law reference.
            temperature_scale_deg_c: Temperature-law normalization scale.
            nonlinear_torque_scale_nm: Odd nonlinear compliance scale.
            maximum_nonlinear_amplitude_deg: Upper nonlinear amplitude bound.
            torque_input_mode: ``nominal_magnitude`` or ``measured_signed``.
        """

        super().__init__()

        # Validate Model Contract
        normalized_formulation = str(formulation).strip().upper()
        normalized_torque_input_mode = str(torque_input_mode).strip().lower()
        assert input_size == 5, (
            "Phase 3 requires angle, speed, torque, temperature, and direction"
        )
        assert output_size == 1, "Phase 3 supports scalar TE only"
        assert normalized_formulation in self.SUPPORTED_FORMULATION_SET
        assert normalized_torque_input_mode in {
            "nominal_magnitude",
            "measured_signed",
        }
        assert minimum_stiffness_nm_per_deg > 0.0
        assert (
            minimum_stiffness_nm_per_deg
            < initial_stiffness_nm_per_deg
            < maximum_stiffness_nm_per_deg
        )
        assert temperature_scale_deg_c > 0.0
        assert nonlinear_torque_scale_nm > 0.0
        assert maximum_nonlinear_amplitude_deg >= 0.0
        resolved_harmonic_index_list = sorted(
            {int(value) for value in harmonic_index_list}
        )
        assert resolved_harmonic_index_list
        assert all(value > 0 for value in resolved_harmonic_index_list)

        # Save Inspectable Metadata
        self.input_size = int(input_size)
        self.output_size = int(output_size)
        self.formulation = normalized_formulation
        self.torque_input_mode = normalized_torque_input_mode
        self.harmonic_index_list = resolved_harmonic_index_list
        self.condition_latent_size = int(condition_latent_size)
        self.minimum_stiffness_nm_per_deg = float(
            minimum_stiffness_nm_per_deg
        )
        self.maximum_stiffness_nm_per_deg = float(
            maximum_stiffness_nm_per_deg
        )
        self.reference_temperature_deg_c = float(
            reference_temperature_deg_c
        )
        self.temperature_scale_deg_c = float(temperature_scale_deg_c)
        self.nonlinear_torque_scale_nm = float(nonlinear_torque_scale_nm)
        self.maximum_nonlinear_amplitude_deg = float(
            maximum_nonlinear_amplitude_deg
        )

        # Register Normalization Buffers For Physical-Unit Decomposition
        self.register_buffer(
            "input_feature_mean",
            torch.zeros(self.input_size, dtype=torch.float32),
            persistent=True,
        )
        self.register_buffer(
            "input_feature_std",
            torch.ones(self.input_size, dtype=torch.float32),
            persistent=True,
        )
        self.register_buffer(
            "target_mean",
            torch.zeros(self.output_size, dtype=torch.float32),
            persistent=True,
        )
        self.register_buffer(
            "target_std",
            torch.ones(self.output_size, dtype=torch.float32),
            persistent=True,
        )
        self.register_buffer(
            "normalization_ready",
            torch.tensor(False, dtype=torch.bool),
            persistent=True,
        )

        # Build Condition Encoder And Zero-Mean Periodic Branch
        self.condition_encoder = FeedForwardNetwork(
            input_size=self.input_size - 1,
            hidden_size=condition_hidden_size,
            output_size=self.condition_latent_size,
            activation_name=activation_name,
            dropout_probability=dropout_probability,
            use_layer_norm=use_layer_norm,
        )
        self.periodic_coefficient_head = nn.Linear(
            self.condition_latent_size,
            2 * len(self.harmonic_index_list),
        )
        self.learned_mean_head: nn.Module | None = None
        if self.formulation in {"C0", "C1", "C2", "C3"}:
            self.learned_mean_head = FeedForwardNetwork(
                input_size=self.condition_latent_size,
                hidden_size=mean_hidden_size,
                output_size=1,
                activation_name=activation_name,
                dropout_probability=dropout_probability,
                use_layer_norm=use_layer_norm,
            )

        # Initialize Bounded Physical Parameters
        initial_stiffness_fraction = (
            initial_stiffness_nm_per_deg
            - self.minimum_stiffness_nm_per_deg
        ) / (
            self.maximum_stiffness_nm_per_deg
            - self.minimum_stiffness_nm_per_deg
        )
        initial_stiffness_logit = torch.logit(
            torch.tensor(initial_stiffness_fraction, dtype=torch.float32)
        )
        self.raw_direction_stiffness_logit = nn.Parameter(
            initial_stiffness_logit.repeat(2)
        )
        self.raw_shared_stiffness_logit = nn.Parameter(
            initial_stiffness_logit.reshape(1)
        )
        self.raw_temperature_slope = nn.Parameter(
            torch.zeros(2, dtype=torch.float32)
        )
        self.direction_intercept_deg = nn.Parameter(
            torch.tensor(
                [
                    initial_forward_intercept_deg,
                    initial_backward_intercept_deg,
                ],
                dtype=torch.float32,
            )
        )
        initial_nonlinear_fraction = 0.1
        self.raw_nonlinear_amplitude_logit = nn.Parameter(
            torch.logit(
                torch.full(
                    (2,),
                    initial_nonlinear_fraction,
                    dtype=torch.float32,
                )
            )
        )

        # Register Harmonic Orders
        self.register_buffer(
            "harmonic_index_tensor",
            torch.as_tensor(
                self.harmonic_index_list,
                dtype=torch.float32,
            ),
            persistent=True,
        )

    def set_normalization_statistics(self, normalization_statistics: object) -> None:

        """Copy training-only normalization statistics into model buffers."""

        input_feature_mean = getattr(
            normalization_statistics,
            "input_feature_mean",
        )
        input_feature_std = getattr(
            normalization_statistics,
            "input_feature_std",
        )
        target_mean = getattr(normalization_statistics, "target_mean")
        target_std = getattr(normalization_statistics, "target_std")
        assert input_feature_mean.shape == self.input_feature_mean.shape
        assert input_feature_std.shape == self.input_feature_std.shape
        assert target_mean.shape == self.target_mean.shape
        assert target_std.shape == self.target_std.shape
        self.input_feature_mean.copy_(input_feature_mean.float())
        self.input_feature_std.copy_(
            torch.clamp(input_feature_std.float(), min=1.0e-8)
        )
        self.target_mean.copy_(target_mean.float())
        self.target_std.copy_(torch.clamp(target_std.float(), min=1.0e-8))
        self.normalization_ready.fill_(True)

    def compute_signed_torque_tensor(
        self,
        input_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Resolve measured-convention signed torque from causal inputs."""

        torque_tensor = input_tensor[:, 2:3]
        direction_flag_tensor = input_tensor[:, 4:5]
        if self.torque_input_mode == "nominal_magnitude":
            return -direction_flag_tensor * torch.abs(torque_tensor)
        return torque_tensor

    def compute_direction_weight_tensor(
        self,
        input_tensor: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:

        """Return differentiable forward and backward selector weights."""

        direction_flag_tensor = input_tensor[:, 4:5]
        forward_weight_tensor = (direction_flag_tensor + 1.0) / 2.0
        backward_weight_tensor = 1.0 - forward_weight_tensor
        return forward_weight_tensor, backward_weight_tensor

    def compute_effective_stiffness_tensor(
        self,
        input_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Compute positive bounded stiffness for the active formulation."""

        forward_weight_tensor, backward_weight_tensor = (
            self.compute_direction_weight_tensor(input_tensor)
        )
        if self.formulation == "C5":
            raw_stiffness_logit = self.raw_shared_stiffness_logit.reshape(
                1,
                1,
            ).expand(input_tensor.shape[0], 1)
        else:
            direction_stiffness_logit_tensor = (
                self.raw_direction_stiffness_logit.reshape(1, 2)
            )
            raw_stiffness_logit = (
                forward_weight_tensor
                * direction_stiffness_logit_tensor[:, 0:1]
                + backward_weight_tensor
                * direction_stiffness_logit_tensor[:, 1:2]
            )
            if self.formulation == "C2":
                direction_temperature_slope_tensor = (
                    self.raw_temperature_slope.reshape(1, 2)
                )
                temperature_slope_tensor = (
                    forward_weight_tensor
                    * direction_temperature_slope_tensor[:, 0:1]
                    + backward_weight_tensor
                    * direction_temperature_slope_tensor[:, 1:2]
                )
                normalized_temperature_tensor = (
                    input_tensor[:, 3:4]
                    - self.reference_temperature_deg_c
                ) / self.temperature_scale_deg_c
                raw_stiffness_logit = (
                    raw_stiffness_logit
                    + temperature_slope_tensor
                    * normalized_temperature_tensor
                )

        stiffness_fraction_tensor = torch.sigmoid(raw_stiffness_logit)
        stiffness_range = (
            self.maximum_stiffness_nm_per_deg
            - self.minimum_stiffness_nm_per_deg
        )
        return (
            self.minimum_stiffness_nm_per_deg
            + stiffness_range * stiffness_fraction_tensor
        )

    def compute_direction_intercept_tensor(
        self,
        input_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Select the explicit zero-torque intercept by direction."""

        forward_weight_tensor, backward_weight_tensor = (
            self.compute_direction_weight_tensor(input_tensor)
        )
        return (
            forward_weight_tensor * self.direction_intercept_deg[0]
            + backward_weight_tensor * self.direction_intercept_deg[1]
        )

    def compute_nonlinear_amplitude_tensor(
        self,
        input_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Select a nonnegative bounded nonlinear amplitude by direction."""

        forward_weight_tensor, backward_weight_tensor = (
            self.compute_direction_weight_tensor(input_tensor)
        )
        amplitude_tensor = self.maximum_nonlinear_amplitude_deg * torch.sigmoid(
            self.raw_nonlinear_amplitude_logit
        )
        return (
            forward_weight_tensor * amplitude_tensor[0]
            + backward_weight_tensor * amplitude_tensor[1]
        )

    def compute_target_compliance_derivative_tensor(
        self,
        input_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Compute the positive derivative prescribed by the physical law."""

        effective_stiffness_tensor = (
            self.compute_effective_stiffness_tensor(input_tensor)
        )
        compliance_derivative_tensor = 1.0 / effective_stiffness_tensor
        if self.formulation == "C3":
            signed_torque_tensor = self.compute_signed_torque_tensor(
                input_tensor
            )
            normalized_torque_tensor = (
                signed_torque_tensor / self.nonlinear_torque_scale_nm
            )
            nonlinear_derivative_tensor = (
                self.compute_nonlinear_amplitude_tensor(input_tensor)
                / self.nonlinear_torque_scale_nm
                / torch.cosh(normalized_torque_tensor).square()
            )
            compliance_derivative_tensor = (
                compliance_derivative_tensor + nonlinear_derivative_tensor
            )
        return compliance_derivative_tensor

    def compute_hard_mean_prediction_deg(
        self,
        input_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Evaluate the equation-embedded C4 or C5 physical mean."""

        assert self.formulation in self.HARD_EQUATION_FORMULATION_SET
        signed_torque_tensor = self.compute_signed_torque_tensor(input_tensor)
        elastic_prediction_deg = (
            signed_torque_tensor
            / self.compute_effective_stiffness_tensor(input_tensor)
        )
        return (
            self.compute_direction_intercept_tensor(input_tensor)
            + elastic_prediction_deg
        )

    def _compute_output_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:

        """Compute mean, periodic, elastic, stiffness, and total predictions."""

        assert bool(self.normalization_ready.item()), (
            "Phase 3 model normalization statistics are not initialized"
        )
        assert input_tensor.ndim == normalized_input_tensor.ndim == 2
        assert input_tensor.shape == normalized_input_tensor.shape
        assert input_tensor.shape[1] == self.input_size

        # Encode Causal Operating Conditions
        normalized_condition_tensor = normalized_input_tensor[:, 1:]
        condition_latent_tensor = self.condition_encoder(
            normalized_condition_tensor
        )

        # Build Explicit Zero-Mean Fourier Contribution
        coefficient_tensor = self.periodic_coefficient_head(
            condition_latent_tensor
        )
        sine_coefficient_tensor, cosine_coefficient_tensor = torch.chunk(
            coefficient_tensor,
            chunks=2,
            dim=-1,
        )
        theta_rad_tensor = torch.deg2rad(input_tensor[:, 0:1])
        order_tensor = self.harmonic_index_tensor.to(
            dtype=theta_rad_tensor.dtype
        ).reshape(1, -1)
        periodic_component_tensor = (
            sine_coefficient_tensor
            * torch.sin(theta_rad_tensor * order_tensor)
            + cosine_coefficient_tensor
            * torch.cos(theta_rad_tensor * order_tensor)
        )
        periodic_prediction_tensor = torch.sum(
            periodic_component_tensor,
            dim=-1,
            keepdim=True,
        )

        # Build Learned Or Equation-Embedded Mean Surface
        if self.formulation in self.HARD_EQUATION_FORMULATION_SET:
            mean_prediction_deg = self.compute_hard_mean_prediction_deg(
                input_tensor
            )
            mean_prediction_tensor = (
                mean_prediction_deg - self.target_mean
            ) / self.target_std
        else:
            assert self.learned_mean_head is not None
            mean_prediction_tensor = self.learned_mean_head(
                condition_latent_tensor
            )
            mean_prediction_deg = (
                mean_prediction_tensor * self.target_std + self.target_mean
            )

        # Expose Physical Contribution Diagnostics
        signed_torque_tensor = self.compute_signed_torque_tensor(input_tensor)
        effective_stiffness_tensor = (
            self.compute_effective_stiffness_tensor(input_tensor)
        )
        elastic_prediction_deg = (
            signed_torque_tensor / effective_stiffness_tensor
        )
        if self.formulation == "C3":
            elastic_prediction_deg = (
                elastic_prediction_deg
                + self.compute_nonlinear_amplitude_tensor(input_tensor)
                * torch.tanh(
                    signed_torque_tensor / self.nonlinear_torque_scale_nm
                )
            )

        prediction_tensor = (
            mean_prediction_tensor + periodic_prediction_tensor
        )
        return {
            "condition_latent_tensor": condition_latent_tensor,
            "mean_prediction_tensor": mean_prediction_tensor,
            "mean_prediction_deg": mean_prediction_deg,
            "periodic_component_tensor": periodic_component_tensor,
            "periodic_prediction_tensor": periodic_prediction_tensor,
            "elastic_prediction_deg": elastic_prediction_deg,
            "effective_stiffness_nm_per_deg": effective_stiffness_tensor,
            "direction_intercept_deg": (
                self.compute_direction_intercept_tensor(input_tensor)
            ),
            "prediction_tensor": prediction_tensor,
        }

    def compute_auxiliary_output_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:

        """Expose the complete inspectable Phase 3 decomposition."""

        return self._compute_output_dictionary(
            input_tensor,
            normalized_input_tensor,
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

        """Compute target-free compliance, boundary, and periodic losses."""

        del normalized_input_tensor, target_mean_tensor, target_std_tensor
        assert maximum_collocation_points > 0
        assert maximum_boundary_conditions > 0

        # Keep A Shape-Compatible Zero For The Non-PINN Control
        zero_loss = input_tensor.sum() * 0.0
        if self.formulation == "C0":
            return self._build_physics_result_dictionary(
                zero_loss=zero_loss,
                collocation_count=0,
                boundary_count=0,
            )

        with torch.inference_mode(False), torch.enable_grad():
            # Select Deterministic Collocation Conditions
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
            ).detach()

            # Differentiate Physical Mean With Respect To Nominal Torque
            nominal_torque_tensor = (
                selected_input_tensor[:, 2:3]
                .clone()
                .requires_grad_(True)
            )
            differentiable_input_tensor = torch.cat(
                (
                    selected_input_tensor[:, 0:2],
                    nominal_torque_tensor,
                    selected_input_tensor[:, 3:5],
                ),
                dim=-1,
            )
            differentiable_normalized_input_tensor = (
                differentiable_input_tensor - self.input_feature_mean
            ) / self.input_feature_std
            output_dictionary = self._compute_output_dictionary(
                differentiable_input_tensor,
                differentiable_normalized_input_tensor,
            )
            mean_prediction_deg = output_dictionary["mean_prediction_deg"]
            mean_derivative_wrt_nominal_torque = torch.autograd.grad(
                outputs=mean_prediction_deg,
                inputs=nominal_torque_tensor,
                grad_outputs=torch.ones_like(mean_prediction_deg),
                create_graph=True,
                retain_graph=True,
                allow_unused=False,
            )[0]
            direction_flag_tensor = differentiable_input_tensor[:, 4:5]
            if self.torque_input_mode == "nominal_magnitude":
                mean_derivative_wrt_signed_torque = (
                    -direction_flag_tensor
                    * mean_derivative_wrt_nominal_torque
                )
            else:
                mean_derivative_wrt_signed_torque = (
                    mean_derivative_wrt_nominal_torque
                )
            target_compliance_derivative_tensor = (
                self.compute_target_compliance_derivative_tensor(
                    differentiable_input_tensor
                )
            )
            compliance_scale = 1.0 / self.minimum_stiffness_nm_per_deg
            compliance_equation_loss = torch.mean(
                torch.square(
                    (
                        mean_derivative_wrt_signed_torque
                        - target_compliance_derivative_tensor
                    )
                    / compliance_scale
                )
            )

            # Enforce The Explicit Zero-Torque Intercept
            zero_torque_input_tensor = (
                differentiable_input_tensor.detach().clone()
            )
            zero_torque_input_tensor[:, 2] = 0.0
            zero_torque_normalized_input_tensor = (
                zero_torque_input_tensor - self.input_feature_mean
            ) / self.input_feature_std
            zero_torque_mean_prediction_deg = self._compute_output_dictionary(
                zero_torque_input_tensor,
                zero_torque_normalized_input_tensor,
            )["mean_prediction_deg"]
            expected_intercept_tensor = self.compute_direction_intercept_tensor(
                zero_torque_input_tensor
            )
            zero_torque_boundary_loss = torch.mean(
                torch.square(
                    zero_torque_mean_prediction_deg
                    - expected_intercept_tensor
                )
            )

            # Penalize Only Violations Of The Positive Monotonic Margin
            minimum_compliance_margin = (
                0.1 / self.maximum_stiffness_nm_per_deg
            )
            monotonicity_loss = torch.mean(
                torch.square(
                    torch.relu(
                        minimum_compliance_margin
                        - mean_derivative_wrt_signed_torque
                    )
                    / compliance_scale
                )
            )
            effective_stiffness_tensor = output_dictionary[
                "effective_stiffness_nm_per_deg"
            ]
            stiffness_bounds_loss = torch.mean(
                torch.square(
                    torch.relu(
                        self.minimum_stiffness_nm_per_deg
                        - effective_stiffness_tensor
                    )
                )
                + torch.square(
                    torch.relu(
                        effective_stiffness_tensor
                        - self.maximum_stiffness_nm_per_deg
                    )
                )
            )

            # Verify Zero Mean Of The Explicit Periodic Branch
            boundary_count = min(
                int(selected_input_tensor.shape[0]),
                int(maximum_boundary_conditions),
            )
            boundary_input_tensor = selected_input_tensor[
                :boundary_count
            ].detach()
            periodic_angle_count = 64
            angle_deg_tensor = torch.arange(
                periodic_angle_count,
                device=input_tensor.device,
                dtype=input_tensor.dtype,
            ).reshape(1, -1, 1)
            angle_deg_tensor = (
                angle_deg_tensor * (360.0 / periodic_angle_count)
            )
            expanded_boundary_input_tensor = boundary_input_tensor[
                :, None, :
            ].repeat(1, periodic_angle_count, 1)
            expanded_boundary_input_tensor[:, :, 0:1] = angle_deg_tensor
            flattened_boundary_input_tensor = (
                expanded_boundary_input_tensor.reshape(-1, self.input_size)
            )
            flattened_boundary_normalized_input_tensor = (
                flattened_boundary_input_tensor - self.input_feature_mean
            ) / self.input_feature_std
            periodic_prediction_tensor = self._compute_output_dictionary(
                flattened_boundary_input_tensor,
                flattened_boundary_normalized_input_tensor,
            )["periodic_prediction_tensor"].reshape(
                boundary_count,
                periodic_angle_count,
                1,
            )
            periodic_mean_loss = torch.mean(
                torch.square(
                    torch.mean(periodic_prediction_tensor, dim=1)
                )
            )

        return self._build_physics_result_dictionary(
            zero_loss=zero_loss,
            collocation_count=collocation_count,
            boundary_count=boundary_count,
            compliance_equation_loss=compliance_equation_loss,
            zero_torque_boundary_loss=zero_torque_boundary_loss,
            monotonicity_loss=monotonicity_loss,
            stiffness_bounds_loss=stiffness_bounds_loss,
            periodic_mean_loss=periodic_mean_loss,
        )

    def _build_physics_result_dictionary(
        self,
        zero_loss: torch.Tensor,
        collocation_count: int,
        boundary_count: int,
        compliance_equation_loss: torch.Tensor | None = None,
        zero_torque_boundary_loss: torch.Tensor | None = None,
        monotonicity_loss: torch.Tensor | None = None,
        stiffness_bounds_loss: torch.Tensor | None = None,
        periodic_mean_loss: torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:

        """Build the shared Phase 2 and Phase 3 residual interface."""

        return {
            "physics_oscillator_residual_loss": zero_loss,
            "physics_periodic_value_loss": zero_loss,
            "physics_periodic_slope_loss": zero_loss,
            "physics_analytical_anchor_loss": zero_loss,
            "physics_compliance_equation_loss": (
                compliance_equation_loss
                if compliance_equation_loss is not None
                else zero_loss
            ),
            "physics_zero_torque_boundary_loss": (
                zero_torque_boundary_loss
                if zero_torque_boundary_loss is not None
                else zero_loss
            ),
            "physics_compliance_monotonicity_loss": (
                monotonicity_loss
                if monotonicity_loss is not None
                else zero_loss
            ),
            "physics_stiffness_bounds_loss": (
                stiffness_bounds_loss
                if stiffness_bounds_loss is not None
                else zero_loss
            ),
            "physics_periodic_mean_loss": (
                periodic_mean_loss
                if periodic_mean_loss is not None
                else zero_loss
            ),
            "physics_collocation_point_count": torch.as_tensor(
                collocation_count,
                device=zero_loss.device,
                dtype=zero_loss.dtype,
            ),
            "physics_boundary_condition_count": torch.as_tensor(
                boundary_count,
                device=zero_loss.device,
                dtype=zero_loss.dtype,
            ),
        }

    def forward_with_input_context(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Predict normalized TE with raw physical context."""

        return self._compute_output_dictionary(
            input_tensor,
            normalized_input_tensor,
        )["prediction_tensor"]

    def forward(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Reconstruct raw context and predict from normalized inputs."""

        assert bool(self.normalization_ready.item())
        input_tensor = (
            normalized_input_tensor * self.input_feature_std
            + self.input_feature_mean
        )
        return self.forward_with_input_context(
            input_tensor,
            normalized_input_tensor,
        )
