"""Complex harmonic coefficient residual models for Wave 5.2R Stage 5."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn


class ComplexHarmonicCoefficientResidualNetwork(nn.Module):
    """Predict uniform TE curves directly or through inspectable coefficients.

    The coefficient contract is ``offset, sin(h_1), cos(h_1), ...``. Anchored
    formulations receive the causal PF-A coefficients from the campaign
    dataset, predict a correction in the same coordinates, and reconstruct the
    full curve through one immutable Fourier basis.
    """

    SUPPORTED_FORMULATION_SET = {
        "direct_curve",
        "direct_coefficient",
        "anchored_coefficient",
        "bounded_coefficient",
        "banded_coefficient",
    }

    def __init__(
        self,
        condition_input_size: int,
        hidden_size_list: list[int],
        harmonic_order_list: list[int],
        angular_sample_count: int,
        formulation: str,
        coefficient_correction_bound_list: list[float] | None = None,
        activation_name: str = "Tanh",
        zero_initialize_correction: bool = True,
    ) -> None:
        """Initialize one representation-aligned Stage 5 candidate.

        Args:
            condition_input_size: Causal setpoint feature count.
            hidden_size_list: Hidden layer widths.
            harmonic_order_list: Ordered positive Fourier orders.
            angular_sample_count: Shared uniform samples per curve.
            formulation: Direct-curve, direct-coefficient, or anchored variant.
            coefficient_correction_bound_list: Physical-unit correction bounds.
            activation_name: PyTorch activation class name.
            zero_initialize_correction: Replay PF-A exactly at initialization.
        """

        super().__init__()

        # Validate The Frozen Representation Contract
        normalized_formulation = str(formulation).strip().lower()
        resolved_order_list = [int(value) for value in harmonic_order_list]
        assert condition_input_size > 0
        assert hidden_size_list
        assert angular_sample_count >= 512
        assert normalized_formulation in self.SUPPORTED_FORMULATION_SET
        assert resolved_order_list
        assert len(set(resolved_order_list)) == len(resolved_order_list)
        assert all(value > 0 for value in resolved_order_list)

        self.condition_input_size = int(condition_input_size)
        self.hidden_size_list = [int(value) for value in hidden_size_list]
        self.harmonic_order_list = resolved_order_list
        self.angular_sample_count = int(angular_sample_count)
        self.formulation = normalized_formulation
        self.coefficient_count = 1 + (2 * len(self.harmonic_order_list))

        # Build One Deterministic Periodic Reconstruction Matrix
        theta_tensor = torch.linspace(
            0.0,
            2.0 * torch.pi,
            steps=self.angular_sample_count + 1,
            dtype=torch.float32,
        )[:-1]
        basis_column_list = [
            torch.ones_like(theta_tensor),
        ]
        for harmonic_order in self.harmonic_order_list:
            basis_column_list.extend(
                [
                    torch.sin(float(harmonic_order) * theta_tensor),
                    torch.cos(float(harmonic_order) * theta_tensor),
                ]
            )
        reconstruction_matrix = torch.stack(basis_column_list, dim=0)
        assert tuple(reconstruction_matrix.shape) == (
            self.coefficient_count,
            self.angular_sample_count,
        )
        self.register_buffer(
            "reconstruction_matrix",
            reconstruction_matrix,
            persistent=True,
        )

        # Register Physical-Unit Correction Bounds
        resolved_bound_list = coefficient_correction_bound_list or (
            [1.0] * self.coefficient_count
        )
        correction_bound_tensor = torch.as_tensor(
            resolved_bound_list,
            dtype=torch.float32,
        )
        assert tuple(correction_bound_tensor.shape) == (
            self.coefficient_count,
        )
        assert bool(torch.all(correction_bound_tensor > 0.0))
        self.register_buffer(
            "coefficient_correction_bound",
            correction_bound_tensor,
            persistent=True,
        )

        # Build The Explicit Condition-To-Output Network
        output_size = (
            self.angular_sample_count
            if self.formulation == "direct_curve"
            else self.coefficient_count
        )
        activation_class = getattr(nn, activation_name)
        layer_list: list[nn.Module] = []
        previous_width = self.condition_input_size
        for hidden_width in self.hidden_size_list:
            assert hidden_width > 0
            layer_list.extend(
                [
                    nn.Linear(previous_width, hidden_width),
                    activation_class(),
                ]
            )
            previous_width = hidden_width
        layer_list.append(nn.Linear(previous_width, output_size))
        self.condition_network = nn.Sequential(*layer_list)

        # Guarantee Exact PF-A Replay At Anchored Initialization
        if zero_initialize_correction:
            output_layer = self.condition_network[-1]
            assert isinstance(output_layer, nn.Linear)
            nn.init.zeros_(output_layer.weight)
            nn.init.zeros_(output_layer.bias)

    def reconstruct_curve(
        self,
        coefficient_tensor: torch.Tensor,
    ) -> torch.Tensor:
        """Reconstruct uniform curves from sine/cosine coefficients."""

        assert coefficient_tensor.shape[-1] == self.coefficient_count
        return coefficient_tensor @ self.reconstruction_matrix

    def forward(
        self,
        condition_tensor: torch.Tensor,
        anchor_coefficient_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        """Return every inspectable Stage 5 prediction component."""

        assert condition_tensor.ndim == 2
        assert condition_tensor.shape[-1] == self.condition_input_size
        assert anchor_coefficient_tensor.ndim == 2
        assert anchor_coefficient_tensor.shape == (
            condition_tensor.shape[0],
            self.coefficient_count,
        )

        raw_output_tensor = self.condition_network(condition_tensor)
        zero_coefficient_tensor = torch.zeros_like(
            anchor_coefficient_tensor
        )

        if self.formulation == "direct_curve":
            prediction_curve_tensor = raw_output_tensor
            prediction_coefficient_tensor = zero_coefficient_tensor
            correction_tensor = zero_coefficient_tensor
            analytical_contribution_tensor = torch.zeros_like(
                prediction_curve_tensor
            )
        else:
            if self.formulation == "direct_coefficient":
                prediction_coefficient_tensor = raw_output_tensor
                correction_tensor = zero_coefficient_tensor
                analytical_coefficient_tensor = zero_coefficient_tensor
            else:
                correction_tensor = raw_output_tensor
                if self.formulation == "bounded_coefficient":
                    correction_tensor = (
                        self.coefficient_correction_bound.unsqueeze(0)
                        * torch.tanh(correction_tensor)
                    )
                prediction_coefficient_tensor = (
                    anchor_coefficient_tensor + correction_tensor
                )
                analytical_coefficient_tensor = anchor_coefficient_tensor

            prediction_curve_tensor = self.reconstruct_curve(
                prediction_coefficient_tensor
            )
            analytical_contribution_tensor = self.reconstruct_curve(
                analytical_coefficient_tensor
            )

        return {
            "prediction_curve": prediction_curve_tensor,
            "prediction_coefficients": prediction_coefficient_tensor,
            "analytical_anchor_coefficients": anchor_coefficient_tensor,
            "analytical_contribution_curve": (
                analytical_contribution_tensor
            ),
            "coefficient_correction": correction_tensor,
        }
