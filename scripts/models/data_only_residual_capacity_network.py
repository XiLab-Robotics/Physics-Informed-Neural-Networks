"""Data-only analytical-residual capacity models for Wave 5.2R Stage 4."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import Project Models
from scripts.models.feedforward_network import FeedForwardNetwork
from scripts.models.periodic_feature_network import PeriodicFeatureNetwork


class DataOnlyResidualCapacityNetwork(nn.Module):
    """Expose direct and PF-A residual-learning formulations.

    The model keeps the frozen Polynomial-Fourier anchor, any trainable
    coefficient-surface adjustment, and the learned residual separately
    inspectable. All outputs returned through the training contract are in
    normalized target space unless their key ends in ``_deg``.
    """

    SUPPORTED_FORMULATION_SET = {"R1", "R2", "R3", "R4", "R5"}
    SUPPORTED_ANCHOR_MODE_SET = {"frozen", "partial_low_order", "full"}

    def __init__(
        self,
        input_size: int,
        hidden_size: list[int],
        harmonic_index_list: list[int],
        analytical_anchor_feature_mean: list[float],
        analytical_anchor_feature_scale: list[float],
        analytical_anchor_coefficient_matrix: list[list[float]],
        formulation: str,
        output_size: int = 1,
        activation_name: str = "Tanh",
        dropout_probability: float = 0.0,
        use_layer_norm: bool = False,
        residual_bound_deg: float = 0.01,
        residual_basis_order_list: list[int] | None = None,
        anchor_mode: str = "frozen",
        partial_unfreeze_harmonic_index_list: list[int] | None = None,
        zero_initialize_residual: bool = True,
        include_raw_angle_feature: bool = False,
    ) -> None:
        """Initialize one Stage 4 formulation.

        Args:
            input_size: Feature width including physical angle in column zero.
            hidden_size: Hidden widths for the learned branch.
            harmonic_index_list: Nine PF-A reconstruction orders.
            analytical_anchor_feature_mean: Training-only PF-A feature means.
            analytical_anchor_feature_scale: Training-only PF-A feature scales.
            analytical_anchor_coefficient_matrix: Complete-quadratic surface.
            formulation: One of R1 through R5.
            output_size: Scalar TE output count.
            activation_name: Learned-branch activation.
            dropout_probability: Hidden dropout probability.
            use_layer_norm: Whether hidden layers use layer normalization.
            residual_bound_deg: Hard physical-unit residual bound for R3.
            residual_basis_order_list: Fixed low-rank Fourier basis for R4.
            anchor_mode: Frozen, partial-low-order, or full surface adjustment.
            partial_unfreeze_harmonic_index_list: Orders whose base surface may
                be adjusted in partial mode.
            zero_initialize_residual: Initialize hybrid residual heads at zero.
            include_raw_angle_feature: Preserve normalized angle beside the
                periodic features for pointwise learned branches.
        """

        super().__init__()

        # Validate Global Model Contract
        normalized_formulation = str(formulation).strip().upper()
        normalized_anchor_mode = str(anchor_mode).strip().lower()
        assert input_size >= 4
        assert output_size == 1
        assert hidden_size
        assert normalized_formulation in self.SUPPORTED_FORMULATION_SET
        assert normalized_anchor_mode in self.SUPPORTED_ANCHOR_MODE_SET
        assert residual_bound_deg > 0.0
        if normalized_formulation != "R5":
            assert normalized_anchor_mode == "frozen", (
                "Only R5 may adjust the analytical coefficient surface"
            )

        resolved_harmonic_index_list = [
            int(value) for value in harmonic_index_list
        ]
        assert resolved_harmonic_index_list
        assert len(set(resolved_harmonic_index_list)) == len(
            resolved_harmonic_index_list
        )
        assert all(value > 0 for value in resolved_harmonic_index_list)

        resolved_basis_order_list = [
            int(value) for value in (residual_basis_order_list or [])
        ]
        if normalized_formulation == "R4":
            assert resolved_basis_order_list
            assert len(set(resolved_basis_order_list)) == len(
                resolved_basis_order_list
            )
            assert all(value > 0 for value in resolved_basis_order_list)

        # Save Inspectable Metadata
        self.input_size = int(input_size)
        self.condition_input_size = self.input_size - 1
        self.output_size = int(output_size)
        self.formulation = normalized_formulation
        self.anchor_mode = normalized_anchor_mode
        self.hidden_size = list(hidden_size)
        self.harmonic_index_list = resolved_harmonic_index_list
        self.residual_basis_order_list = resolved_basis_order_list
        self.residual_bound_deg = float(residual_bound_deg)

        # Register Training Normalization Buffers
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

        # Register Immutable Stage 3 PF-A Surface
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
        expected_coefficient_count = 1 + (
            2 * len(self.harmonic_index_list)
        )
        assert tuple(feature_mean_tensor.shape) == (3,)
        assert tuple(feature_scale_tensor.shape) == (3,)
        assert bool(torch.all(feature_scale_tensor > 0.0))
        assert tuple(coefficient_matrix_tensor.shape) == (
            10,
            expected_coefficient_count,
        )
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
            "frozen_analytical_anchor_coefficient_matrix",
            coefficient_matrix_tensor,
            persistent=True,
        )
        self.register_buffer(
            "harmonic_index_tensor",
            torch.as_tensor(
                self.harmonic_index_list,
                dtype=torch.float32,
            ),
            persistent=True,
        )
        self.register_buffer(
            "residual_basis_order_tensor",
            torch.as_tensor(
                self.residual_basis_order_list,
                dtype=torch.float32,
            ),
            persistent=True,
        )

        # Build Explicit Anchor-Surface Adjustment For R5 Ablations
        self.anchor_surface_delta = nn.Parameter(
            torch.zeros_like(coefficient_matrix_tensor),
            requires_grad=(self.anchor_mode != "frozen"),
        )
        anchor_surface_trainable_mask = self._build_anchor_surface_mask(
            partial_unfreeze_harmonic_index_list or [1, 3],
        )
        self.register_buffer(
            "anchor_surface_trainable_mask",
            anchor_surface_trainable_mask,
            persistent=True,
        )

        # Build One Learned Branch Per Formulation
        self.pointwise_network: PeriodicFeatureNetwork | None = None
        self.condition_coefficient_network: FeedForwardNetwork | None = None
        if self.formulation in {"R1", "R2", "R3"}:
            self.pointwise_network = PeriodicFeatureNetwork(
                input_size=self.input_size,
                hidden_size=self.hidden_size,
                output_size=1,
                activation_name=activation_name,
                dropout_probability=dropout_probability,
                use_layer_norm=use_layer_norm,
                harmonic_order=max(self.harmonic_index_list),
                harmonic_index_list=self.harmonic_index_list,
                include_raw_angle_feature=include_raw_angle_feature,
            )
        elif self.formulation == "R4":
            residual_output_count = 1 + (
                2 * len(self.residual_basis_order_list)
            )
            self.condition_coefficient_network = FeedForwardNetwork(
                input_size=self.condition_input_size,
                hidden_size=self.hidden_size,
                output_size=residual_output_count,
                activation_name=activation_name,
                dropout_probability=dropout_probability,
                use_layer_norm=use_layer_norm,
            )
        else:
            self.condition_coefficient_network = FeedForwardNetwork(
                input_size=self.condition_input_size,
                hidden_size=self.hidden_size,
                output_size=expected_coefficient_count,
                activation_name=activation_name,
                dropout_probability=dropout_probability,
                use_layer_norm=use_layer_norm,
            )

        # Guarantee Exact PF-A Initialization For Every Hybrid Arm
        if zero_initialize_residual and self.formulation != "R1":
            self._zero_initialize_learned_output_layer()

    def _build_anchor_surface_mask(
        self,
        partial_unfreeze_harmonic_index_list: list[int],
    ) -> torch.Tensor:
        """Build the declared coefficient-surface adjustment mask."""

        coefficient_count = 1 + (2 * len(self.harmonic_index_list))
        if self.anchor_mode == "full":
            return torch.ones((10, coefficient_count), dtype=torch.float32)
        if self.anchor_mode == "frozen":
            return torch.zeros((10, coefficient_count), dtype=torch.float32)

        selected_order_set = {
            int(value) for value in partial_unfreeze_harmonic_index_list
        }
        assert selected_order_set
        assert selected_order_set.issubset(set(self.harmonic_index_list))
        mask_tensor = torch.zeros(
            (10, coefficient_count),
            dtype=torch.float32,
        )
        mask_tensor[:, 0] = 1.0
        for harmonic_position, harmonic_index in enumerate(
            self.harmonic_index_list
        ):
            if harmonic_index not in selected_order_set:
                continue
            mask_tensor[:, 1 + (2 * harmonic_position)] = 1.0
            mask_tensor[:, 2 + (2 * harmonic_position)] = 1.0
        return mask_tensor

    def _zero_initialize_learned_output_layer(self) -> None:
        """Initialize the learned residual or coefficient delta at zero."""

        if self.pointwise_network is not None:
            output_layer = self.pointwise_network.feature_network.network[-1]
        else:
            assert self.condition_coefficient_network is not None
            output_layer = self.condition_coefficient_network.network[-1]
        assert isinstance(output_layer, nn.Linear)
        nn.init.zeros_(output_layer.weight)
        nn.init.zeros_(output_layer.bias)

    def set_normalization_statistics(
        self,
        normalization_statistics: object,
    ) -> None:
        """Copy training-only input and target statistics into buffers."""

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

    def _build_analytical_design_tensor(
        self,
        input_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Build the Stage 3 complete-quadratic operating basis."""

        # Convert Positive Setpoint Magnitude To Physical Signed Torque
        if self.input_size >= 5:
            signed_torque_tensor = (
                -input_tensor[:, 4:5]
                * torch.abs(input_tensor[:, 2:3])
            )
        else:
            signed_torque_tensor = -torch.abs(input_tensor[:, 2:3])
        operating_feature_tensor = torch.cat(
            (
                signed_torque_tensor,
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
        return torch.cat(
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

    def _resolve_anchor_coefficient_matrix(self) -> torch.Tensor:
        """Return frozen or explicitly adjusted PF-A surface coefficients."""

        if self.anchor_mode == "frozen":
            return self.frozen_analytical_anchor_coefficient_matrix
        return self.frozen_analytical_anchor_coefficient_matrix + (
            self.anchor_surface_delta * self.anchor_surface_trainable_mask
        )

    def _reconstruct_from_coefficient_tensor(
        self,
        input_tensor: torch.Tensor,
        coefficient_tensor: torch.Tensor,
        order_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Reconstruct one periodic curve from offset and complex coefficients."""

        expected_coefficient_count = 1 + (2 * int(order_tensor.numel()))
        assert coefficient_tensor.ndim == 2
        assert coefficient_tensor.shape[1] == expected_coefficient_count
        theta_rad_tensor = torch.deg2rad(input_tensor[:, 0:1])
        prediction_tensor = coefficient_tensor[:, 0:1]
        for order_position, order_value in enumerate(order_tensor.tolist()):
            sine_coefficient_tensor = coefficient_tensor[
                :,
                1 + (2 * order_position) : 2 + (2 * order_position),
            ]
            cosine_coefficient_tensor = coefficient_tensor[
                :,
                2 + (2 * order_position) : 3 + (2 * order_position),
            ]
            prediction_tensor = prediction_tensor + (
                sine_coefficient_tensor
                * torch.sin(float(order_value) * theta_rad_tensor)
                + cosine_coefficient_tensor
                * torch.cos(float(order_value) * theta_rad_tensor)
            )
        return prediction_tensor

    def _compute_anchor_dictionary(
        self,
        input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        """Compute frozen and optionally adjusted analytical contributions."""

        design_tensor = self._build_analytical_design_tensor(input_tensor)
        frozen_coefficient_tensor = (
            design_tensor
            @ self.frozen_analytical_anchor_coefficient_matrix
        )
        adjusted_coefficient_tensor = (
            design_tensor @ self._resolve_anchor_coefficient_matrix()
        )
        frozen_prediction_deg = self._reconstruct_from_coefficient_tensor(
            input_tensor,
            frozen_coefficient_tensor,
            self.harmonic_index_tensor,
        )
        adjusted_prediction_deg = self._reconstruct_from_coefficient_tensor(
            input_tensor,
            adjusted_coefficient_tensor,
            self.harmonic_index_tensor,
        )
        return {
            "frozen_analytical_coefficient_tensor": (
                frozen_coefficient_tensor
            ),
            "analytical_coefficient_tensor": adjusted_coefficient_tensor,
            "frozen_analytical_prediction_deg": frozen_prediction_deg,
            "analytical_prediction_deg": adjusted_prediction_deg,
            "analytical_prediction_tensor": (
                adjusted_prediction_deg - self.target_mean
            )
            / self.target_std,
        }

    def _compute_pointwise_learned_tensor(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Compute direct or pointwise residual output in normalized units."""

        assert self.pointwise_network is not None
        return self.pointwise_network.forward_with_input_context(
            input_tensor,
            normalized_input_tensor,
        )

    def _compute_basis_residual_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        """Predict and reconstruct an R4 low-rank periodic residual."""

        assert self.condition_coefficient_network is not None
        normalized_coefficient_tensor = self.condition_coefficient_network(
            normalized_input_tensor[:, 1:],
        )
        normalized_residual_tensor = self._reconstruct_from_coefficient_tensor(
            input_tensor,
            normalized_coefficient_tensor,
            self.residual_basis_order_tensor,
        )
        return {
            "residual_coefficient_tensor": (
                normalized_coefficient_tensor * self.target_std
            ),
            "residual_prediction_tensor": normalized_residual_tensor,
            "residual_prediction_deg": (
                normalized_residual_tensor * self.target_std
            ),
        }

    def _compute_coefficient_residual_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        """Predict and reconstruct the R5 coefficient correction."""

        assert self.condition_coefficient_network is not None
        normalized_delta_tensor = self.condition_coefficient_network(
            normalized_input_tensor[:, 1:],
        )
        normalized_residual_tensor = self._reconstruct_from_coefficient_tensor(
            input_tensor,
            normalized_delta_tensor,
            self.harmonic_index_tensor,
        )
        return {
            "residual_coefficient_tensor": (
                normalized_delta_tensor * self.target_std
            ),
            "residual_prediction_tensor": normalized_residual_tensor,
            "residual_prediction_deg": (
                normalized_residual_tensor * self.target_std
            ),
        }

    def compute_auxiliary_output_dictionary(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        """Expose complete Stage 4 analytical and learned decomposition."""

        assert bool(self.normalization_ready.item()), (
            "Stage 4 model normalization statistics are not initialized"
        )
        assert input_tensor.shape == normalized_input_tensor.shape
        assert input_tensor.ndim == 2
        assert input_tensor.shape[1] == self.input_size

        # Direct Data-Only Control Never Evaluates The Analytical Path
        if self.formulation == "R1":
            direct_prediction_tensor = self._compute_pointwise_learned_tensor(
                input_tensor,
                normalized_input_tensor,
            )
            return {
                "prediction_tensor": direct_prediction_tensor,
                "direct_prediction_tensor": direct_prediction_tensor,
                "direct_prediction_deg": (
                    direct_prediction_tensor * self.target_std
                    + self.target_mean
                ),
            }

        # Evaluate Frozen Or Explicitly Adjusted PF-A
        anchor_dictionary = self._compute_anchor_dictionary(input_tensor)
        analytical_prediction_tensor = anchor_dictionary[
            "analytical_prediction_tensor"
        ]

        # Resolve Learned Residual Formulation
        if self.formulation in {"R2", "R3"}:
            raw_residual_tensor = self._compute_pointwise_learned_tensor(
                input_tensor,
                normalized_input_tensor,
            )
            if self.formulation == "R3":
                residual_prediction_deg = (
                    self.residual_bound_deg * torch.tanh(raw_residual_tensor)
                )
                residual_prediction_tensor = (
                    residual_prediction_deg / self.target_std
                )
            else:
                residual_prediction_tensor = raw_residual_tensor
                residual_prediction_deg = (
                    residual_prediction_tensor * self.target_std
                )
            residual_dictionary = {
                "raw_residual_tensor": raw_residual_tensor,
                "residual_prediction_tensor": residual_prediction_tensor,
                "residual_prediction_deg": residual_prediction_deg,
            }
        elif self.formulation == "R4":
            residual_dictionary = self._compute_basis_residual_dictionary(
                input_tensor,
                normalized_input_tensor,
            )
        else:
            residual_dictionary = (
                self._compute_coefficient_residual_dictionary(
                    input_tensor,
                    normalized_input_tensor,
                )
            )

        prediction_tensor = (
            analytical_prediction_tensor
            + residual_dictionary["residual_prediction_tensor"]
        )
        return {
            **anchor_dictionary,
            **residual_dictionary,
            "prediction_tensor": prediction_tensor,
            "combined_prediction_deg": (
                prediction_tensor * self.target_std + self.target_mean
            ),
        }

    def forward_with_input_context(
        self,
        input_tensor: torch.Tensor,
        normalized_input_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Return normalized combined prediction with physical input context."""

        return self.compute_auxiliary_output_dictionary(
            input_tensor,
            normalized_input_tensor,
        )["prediction_tensor"]

    def forward(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:
        """Reject context-free use because physical angle is required."""

        raise RuntimeError(
            "Stage 4 models require raw angle context; use "
            "forward_with_input_context or compute_auxiliary_output_dictionary"
        )
