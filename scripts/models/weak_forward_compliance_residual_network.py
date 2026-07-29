"""Weak forward-compliance residual model for Wave 5.2R Stage 8."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import The Qualified Coefficient Model
from scripts.models.complex_harmonic_coefficient_residual_network import (
    ComplexHarmonicCoefficientResidualNetwork,
)


class WeakForwardComplianceResidualNetwork(nn.Module):

    """Expose weak response derivatives above one bounded H04-style model.

    The standard path delegates coefficient prediction and periodic
    reconstruction to the Stage 5 network. The hard-equation path replaces
    only the predicted constant coefficient with a bounded algebraic
    torque-response law, leaving the learned centered harmonic shape
    inspectable.

    Args:
        coefficient_network: Initialized bounded coefficient network.
        torque_feature_mean_nm: Training-only torque normalization mean.
        torque_feature_scale_nm: Training-only torque normalization scale.
        use_hard_compliance_mean: Whether to replace the learned mean.
        minimum_stiffness_nm_per_deg: Lower hard-equation stiffness bound.
        maximum_stiffness_nm_per_deg: Upper hard-equation stiffness bound.
        initial_stiffness_nm_per_deg: Initial effective stiffness.
        initial_intercept_deg: Initial zero-torque intercept.
    """

    def __init__(
        self,
        coefficient_network: ComplexHarmonicCoefficientResidualNetwork,
        torque_feature_mean_nm: float,
        torque_feature_scale_nm: float,
        *,
        use_hard_compliance_mean: bool = False,
        minimum_stiffness_nm_per_deg: float = 5_000.0,
        maximum_stiffness_nm_per_deg: float = 100_000.0,
        initial_stiffness_nm_per_deg: float = 28_164.36,
        initial_intercept_deg: float = -0.0200,
    ) -> None:

        """Initialize one weak or hard forward-compliance candidate."""

        super().__init__()

        # Validate The Observable Forward Contract
        assert torque_feature_scale_nm > 0.0
        assert minimum_stiffness_nm_per_deg > 0.0
        assert maximum_stiffness_nm_per_deg > minimum_stiffness_nm_per_deg
        assert (
            minimum_stiffness_nm_per_deg
            < initial_stiffness_nm_per_deg
            < maximum_stiffness_nm_per_deg
        )
        self.coefficient_network = coefficient_network
        self.use_hard_compliance_mean = bool(use_hard_compliance_mean)
        self.minimum_stiffness_nm_per_deg = float(
            minimum_stiffness_nm_per_deg
        )
        self.maximum_stiffness_nm_per_deg = float(
            maximum_stiffness_nm_per_deg
        )
        self.register_buffer(
            "torque_feature_mean_nm",
            torch.tensor(float(torque_feature_mean_nm), dtype=torch.float32),
            persistent=True,
        )
        self.register_buffer(
            "torque_feature_scale_nm",
            torch.tensor(float(torque_feature_scale_nm), dtype=torch.float32),
            persistent=True,
        )

        # Parameterize The Hard Negative Control Inside Physical Bounds
        initial_fraction = (
            float(initial_stiffness_nm_per_deg)
            - self.minimum_stiffness_nm_per_deg
        ) / (
            self.maximum_stiffness_nm_per_deg
            - self.minimum_stiffness_nm_per_deg
        )
        self.raw_stiffness_logit = nn.Parameter(
            torch.logit(
                torch.tensor(initial_fraction, dtype=torch.float32)
            )
        )
        self.zero_torque_intercept_deg = nn.Parameter(
            torch.tensor(float(initial_intercept_deg), dtype=torch.float32)
        )

    def signed_torque_from_normalized(
        self,
        normalized_condition_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Recover causal signed setpoint torque in Newton-metres."""

        assert normalized_condition_tensor.ndim == 2
        assert normalized_condition_tensor.shape[1] >= 1
        return (
            normalized_condition_tensor[:, :1]
            * self.torque_feature_scale_nm
            + self.torque_feature_mean_nm
        )

    def effective_stiffness_nm_per_deg(self) -> torch.Tensor:

        """Return the positive bounded hard-control stiffness."""

        stiffness_fraction = torch.sigmoid(self.raw_stiffness_logit)
        return self.minimum_stiffness_nm_per_deg + (
            self.maximum_stiffness_nm_per_deg
            - self.minimum_stiffness_nm_per_deg
        ) * stiffness_fraction

    def forward(
        self,
        normalized_condition_tensor: torch.Tensor,
        anchor_coefficient_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:

        """Return curve, mean, centered shape, and compliance quantities."""

        coefficient_output = self.coefficient_network(
            normalized_condition_tensor,
            anchor_coefficient_tensor,
        )
        prediction_coefficient_tensor = coefficient_output[
            "prediction_coefficients"
        ]
        learned_curve_tensor = coefficient_output["prediction_curve"]
        learned_mean_tensor = prediction_coefficient_tensor[:, :1]
        learned_centered_shape_tensor = (
            learned_curve_tensor - learned_mean_tensor
        )
        signed_torque_tensor = self.signed_torque_from_normalized(
            normalized_condition_tensor
        )
        effective_stiffness_tensor = (
            self.effective_stiffness_nm_per_deg()
        )
        hard_mean_tensor = (
            self.zero_torque_intercept_deg
            + signed_torque_tensor / effective_stiffness_tensor
        )

        # Replace Only The Constant Coefficient For The Hard Control
        if self.use_hard_compliance_mean:
            prediction_mean_tensor = hard_mean_tensor
            prediction_curve_tensor = (
                hard_mean_tensor + learned_centered_shape_tensor
            )
            prediction_coefficient_tensor = torch.cat(
                [
                    hard_mean_tensor,
                    prediction_coefficient_tensor[:, 1:],
                ],
                dim=1,
            )
        else:
            prediction_mean_tensor = learned_mean_tensor
            prediction_curve_tensor = learned_curve_tensor

        return {
            **coefficient_output,
            "prediction_curve": prediction_curve_tensor,
            "prediction_coefficients": prediction_coefficient_tensor,
            "prediction_mean": prediction_mean_tensor,
            "prediction_centered_shape": (
                prediction_curve_tensor - prediction_mean_tensor
            ),
            "signed_torque_nm": signed_torque_tensor,
            "hard_compliance_mean": hard_mean_tensor,
            "effective_stiffness_nm_per_deg": (
                effective_stiffness_tensor.reshape(1)
            ),
        }

    def mean_compliance_derivative(
        self,
        normalized_condition_tensor: torch.Tensor,
        anchor_coefficient_tensor: torch.Tensor,
        *,
        create_graph: bool,
    ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:

        """Differentiate predicted mean with respect to signed torque.

        The input tensor must require gradients. The derivative is converted
        from normalized-feature units to `deg / Nm`. `create_graph=True`
        preserves the derivative graph so a weak compliance penalty can
        participate in the subsequent optimization backward pass.
        """

        assert normalized_condition_tensor.requires_grad
        output = self.forward(
            normalized_condition_tensor,
            anchor_coefficient_tensor,
        )
        normalized_gradient_tensor = torch.autograd.grad(
            outputs=output["prediction_mean"],
            inputs=normalized_condition_tensor,
            grad_outputs=torch.ones_like(output["prediction_mean"]),
            create_graph=create_graph,
            retain_graph=create_graph,
            allow_unused=False,
        )[0]
        compliance_derivative_tensor = (
            normalized_gradient_tensor[:, :1]
            / self.torque_feature_scale_nm
        )
        return compliance_derivative_tensor, output
