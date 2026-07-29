"""Mean and centered-shape multi-head models for Wave 5.2R Stage 7."""

from __future__ import annotations

# Import PyTorch Utilities
import torch
import torch.nn as nn


def build_tanh_network(
    input_size: int,
    hidden_size_list: list[int],
    output_size: int,
    zero_initialize_output: bool = True,
) -> nn.Sequential:

    """Build one explicit fully connected Tanh network."""

    assert input_size > 0
    assert output_size > 0
    assert hidden_size_list
    layer_list: list[nn.Module] = []
    previous_size = input_size
    for hidden_size in hidden_size_list:
        assert hidden_size > 0
        layer_list.extend(
            [
                nn.Linear(previous_size, hidden_size),
                nn.Tanh(),
            ]
        )
        previous_size = hidden_size
    output_layer = nn.Linear(previous_size, output_size)
    if zero_initialize_output:
        nn.init.zeros_(output_layer.weight)
        nn.init.zeros_(output_layer.bias)
    layer_list.append(output_layer)
    return nn.Sequential(*layer_list)


class MeanCenteredShapeMultiHeadNetwork(nn.Module):

    """Predict bounded mean and exactly centered periodic shape components."""

    SUPPORTED_ARCHITECTURE_SET = {
        "monolithic",
        "shared",
        "partial",
        "independent",
        "analytical_mean",
        "analytical_shape",
    }

    def __init__(
        self,
        condition_input_size: int,
        harmonic_order_list: list[int],
        angular_sample_count: int,
        coefficient_correction_bound_list: list[float],
        architecture: str,
        shared_hidden_size_list: list[int] | None = None,
        branch_hidden_size_list: list[int] | None = None,
    ) -> None:

        """Initialize one Stage 7 decomposition.

        Args:
            condition_input_size: Causal setpoint feature count.
            harmonic_order_list: Ordered positive Fourier orders.
            angular_sample_count: Uniform curve sample count.
            coefficient_correction_bound_list: Mean and shape bounds.
            architecture: Declared sharing or analytical ablation.
            shared_hidden_size_list: Shared or monolithic hidden widths.
            branch_hidden_size_list: Head-specific hidden widths.
        """

        super().__init__()

        # Validate The Immutable Coefficient Contract
        resolved_architecture = str(architecture).strip().lower()
        resolved_order_list = [int(value) for value in harmonic_order_list]
        coefficient_count = 1 + (2 * len(resolved_order_list))
        bound_tensor = torch.as_tensor(
            coefficient_correction_bound_list,
            dtype=torch.float32,
        )
        assert resolved_architecture in self.SUPPORTED_ARCHITECTURE_SET
        assert condition_input_size > 0
        assert angular_sample_count >= 512
        assert resolved_order_list
        assert len(set(resolved_order_list)) == len(resolved_order_list)
        assert tuple(bound_tensor.shape) == (coefficient_count,)
        assert bool(torch.all(bound_tensor > 0.0))

        self.condition_input_size = int(condition_input_size)
        self.harmonic_order_list = resolved_order_list
        self.angular_sample_count = int(angular_sample_count)
        self.coefficient_count = coefficient_count
        self.shape_coefficient_count = coefficient_count - 1
        self.architecture = resolved_architecture
        self.register_buffer(
            "coefficient_correction_bound",
            bound_tensor,
            persistent=True,
        )

        # Build The Non-Constant Periodic Reconstruction Basis
        theta_tensor = torch.linspace(
            0.0,
            2.0 * torch.pi,
            steps=self.angular_sample_count + 1,
            dtype=torch.float32,
        )[:-1]
        shape_basis_row_list: list[torch.Tensor] = []
        for harmonic_order in self.harmonic_order_list:
            shape_basis_row_list.extend(
                [
                    torch.sin(float(harmonic_order) * theta_tensor),
                    torch.cos(float(harmonic_order) * theta_tensor),
                ]
            )
        shape_reconstruction_matrix = torch.stack(
            shape_basis_row_list,
            dim=0,
        )
        assert tuple(shape_reconstruction_matrix.shape) == (
            self.shape_coefficient_count,
            self.angular_sample_count,
        )
        self.register_buffer(
            "shape_reconstruction_matrix",
            shape_reconstruction_matrix,
            persistent=True,
        )

        # Build The Declared Sharing Topology
        shared_width_list = shared_hidden_size_list or [64, 64, 32]
        branch_width_list = branch_hidden_size_list or [48]
        if self.architecture == "monolithic":
            self.monolithic_network = build_tanh_network(
                self.condition_input_size,
                shared_width_list,
                self.coefficient_count,
            )
        elif self.architecture == "shared":
            self.shared_encoder = build_tanh_network(
                self.condition_input_size,
                shared_width_list,
                shared_width_list[-1],
                zero_initialize_output=False,
            )
            self.mean_head = nn.Linear(shared_width_list[-1], 1)
            self.shape_head = nn.Linear(
                shared_width_list[-1],
                self.shape_coefficient_count,
            )
            self._zero_initialize_head(self.mean_head)
            self._zero_initialize_head(self.shape_head)
        elif self.architecture == "partial":
            first_shared_width = shared_width_list[0]
            self.shared_encoder = nn.Sequential(
                nn.Linear(self.condition_input_size, first_shared_width),
                nn.Tanh(),
            )
            self.mean_network = build_tanh_network(
                first_shared_width,
                branch_width_list,
                1,
            )
            self.shape_network = build_tanh_network(
                first_shared_width,
                branch_width_list,
                self.shape_coefficient_count,
            )
        elif self.architecture == "independent":
            self.mean_network = build_tanh_network(
                self.condition_input_size,
                shared_width_list,
                1,
            )
            self.shape_network = build_tanh_network(
                self.condition_input_size,
                shared_width_list,
                self.shape_coefficient_count,
            )
        elif self.architecture == "analytical_mean":
            self.shape_network = build_tanh_network(
                self.condition_input_size,
                shared_width_list,
                self.shape_coefficient_count,
            )
        else:
            assert self.architecture == "analytical_shape"
            self.mean_network = build_tanh_network(
                self.condition_input_size,
                shared_width_list,
                1,
            )

    @staticmethod
    def _zero_initialize_head(head: nn.Linear) -> None:

        """Initialize one correction head to exact analytical replay."""

        nn.init.zeros_(head.weight)
        nn.init.zeros_(head.bias)

    def shared_parameter_list(self) -> list[nn.Parameter]:

        """Return parameters jointly influenced by mean and shape losses."""

        if hasattr(self, "shared_encoder"):
            return list(self.shared_encoder.parameters())
        if hasattr(self, "monolithic_network"):
            return list(self.monolithic_network.parameters())
        return []

    def _raw_correction_components(
        self,
        condition_tensor: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:

        """Return unbounded mean and shape corrections."""

        batch_size = condition_tensor.shape[0]
        zero_mean_tensor = condition_tensor.new_zeros((batch_size, 1))
        zero_shape_tensor = condition_tensor.new_zeros(
            (batch_size, self.shape_coefficient_count)
        )
        if self.architecture == "monolithic":
            raw_correction_tensor = self.monolithic_network(condition_tensor)
            return (
                raw_correction_tensor[:, :1],
                raw_correction_tensor[:, 1:],
            )
        if self.architecture == "shared":
            shared_feature_tensor = self.shared_encoder(condition_tensor)
            return (
                self.mean_head(shared_feature_tensor),
                self.shape_head(shared_feature_tensor),
            )
        if self.architecture == "partial":
            shared_feature_tensor = self.shared_encoder(condition_tensor)
            return (
                self.mean_network(shared_feature_tensor),
                self.shape_network(shared_feature_tensor),
            )
        if self.architecture == "independent":
            return (
                self.mean_network(condition_tensor),
                self.shape_network(condition_tensor),
            )
        if self.architecture == "analytical_mean":
            return (
                zero_mean_tensor,
                self.shape_network(condition_tensor),
            )
        assert self.architecture == "analytical_shape"
        return (
            self.mean_network(condition_tensor),
            zero_shape_tensor,
        )

    def forward(
        self,
        condition_tensor: torch.Tensor,
        anchor_coefficient_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:

        """Return explicit mean, centered shape, and reconstructed curve."""

        assert condition_tensor.ndim == 2
        assert condition_tensor.shape[1] == self.condition_input_size
        assert anchor_coefficient_tensor.shape == (
            condition_tensor.shape[0],
            self.coefficient_count,
        )

        # Predict Bounded Corrections In Physical Coefficient Units
        raw_mean_tensor, raw_shape_tensor = (
            self._raw_correction_components(condition_tensor)
        )
        mean_correction_tensor = (
            self.coefficient_correction_bound[:1].unsqueeze(0)
            * torch.tanh(raw_mean_tensor)
        )
        shape_correction_tensor = (
            self.coefficient_correction_bound[1:].unsqueeze(0)
            * torch.tanh(raw_shape_tensor)
        )
        prediction_mean_tensor = (
            anchor_coefficient_tensor[:, :1] + mean_correction_tensor
        )
        prediction_shape_coefficient_tensor = (
            anchor_coefficient_tensor[:, 1:] + shape_correction_tensor
        )

        # Enforce Exact Zero-Mean Shape Before Reconstruction
        raw_shape_curve_tensor = (
            prediction_shape_coefficient_tensor
            @ self.shape_reconstruction_matrix
        )
        prediction_shape_curve_tensor = (
            raw_shape_curve_tensor
            - torch.mean(
                raw_shape_curve_tensor,
                dim=1,
                keepdim=True,
            )
        )
        prediction_curve_tensor = (
            prediction_mean_tensor + prediction_shape_curve_tensor
        )
        prediction_coefficient_tensor = torch.cat(
            [
                prediction_mean_tensor,
                prediction_shape_coefficient_tensor,
            ],
            dim=1,
        )

        return {
            "prediction_curve": prediction_curve_tensor,
            "prediction_mean": prediction_mean_tensor,
            "prediction_centered_shape": prediction_shape_curve_tensor,
            "prediction_coefficients": prediction_coefficient_tensor,
            "mean_correction": mean_correction_tensor,
            "shape_coefficient_correction": shape_correction_tensor,
            "shape_cycle_mean": torch.mean(
                prediction_shape_curve_tensor,
                dim=1,
                keepdim=True,
            ),
            "reconstruction_identity_error": torch.amax(
                torch.abs(
                    prediction_curve_tensor
                    - (
                        prediction_mean_tensor
                        + prediction_shape_curve_tensor
                    )
                )
            ),
        }
