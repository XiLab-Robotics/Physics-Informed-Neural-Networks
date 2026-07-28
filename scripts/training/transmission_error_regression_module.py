"""Lightning regression module for normalized TE prediction workflows."""

from __future__ import annotations

# Import PyTorch Lightning Utilities
from lightning.pytorch import LightningModule

# Import PyTorch Utilities
import torch
import torch.nn as nn
import torch.nn.functional as torch_functional

# Import DataModule Utilities
from scripts.training.transmission_error_datamodule import NormalizationStatistics
from scripts.training.physics_guided_optimization_instrumentation import (
    LossComponentConfiguration,
)
from scripts.training.physics_guided_optimization_instrumentation import (
    PhysicsGuidedOptimizationInstrumentation,
)
from scripts.training.physics_guided_optimization_instrumentation import (
    capture_trainable_parameter_vector,
)
from scripts.training.physics_guided_optimization_instrumentation import (
    compute_update_to_parameter_ratio,
)

class TransmissionErrorRegressionModule(LightningModule):

    """LightningModule that wraps TE backbones, normalization, and metrics."""

    def __init__(
        self,
        regression_model: nn.Module,
        input_feature_dim: int,
        target_feature_dim: int,
        learning_rate: float = 1.0e-3,
        weight_decay: float = 1.0e-4,
        normalization_statistics: NormalizationStatistics | None = None,
        loss_configuration: dict | None = None,
    ) -> None:
        """Initialize the TE regression LightningModule.

        Args:
            regression_model: Backbone model operating on normalized inputs.
            input_feature_dim: Number of model input features.
            target_feature_dim: Number of regression targets.
            learning_rate: AdamW learning rate.
            weight_decay: AdamW weight decay.
            normalization_statistics: Optional normalization tensors loaded at
                construction time.
            loss_configuration: Optional composite loss configuration used by
                curve-aware campaign branches.
        """

        super().__init__()

        # Validate Optimization Parameters
        assert input_feature_dim > 0, f"Input Feature Dim must be positive | {input_feature_dim}"
        assert target_feature_dim > 0, f"Target Feature Dim must be positive | {target_feature_dim}"
        assert learning_rate > 0.0, f"Learning Rate must be positive | {learning_rate}"
        assert weight_decay >= 0.0, f"Weight Decay must be non-negative | {weight_decay}"

        # Save Hyperparameters
        self.save_hyperparameters(ignore=["regression_model", "normalization_statistics"])

        # Save Model And Loss
        self.regression_model = regression_model
        self.loss_configuration = self._normalize_loss_configuration(loss_configuration or {})
        self.optimization_instrumentation = (
            self._build_optimization_instrumentation()
        )
        self._parameter_vector_before_step: torch.Tensor | None = None

        # Register Normalization Buffers
        self.register_buffer("input_feature_mean", torch.zeros(input_feature_dim, dtype=torch.float32))
        self.register_buffer("input_feature_std", torch.ones(input_feature_dim, dtype=torch.float32))
        self.register_buffer("target_mean", torch.zeros(target_feature_dim, dtype=torch.float32))
        self.register_buffer("target_std", torch.ones(target_feature_dim, dtype=torch.float32))

        # Initialize Normalization State
        self.normalization_statistics_initialized = False

        # Load Normalization Statistics If Available At Construction Time
        if normalization_statistics is not None: self.set_normalization_statistics(normalization_statistics)

    def _normalize_loss_configuration(self, loss_configuration: dict) -> dict[str, object]:

        """Normalize optional curve-aware loss settings."""

        # Resolve Loss Profile And Weights
        loss_profile = str(loss_configuration.get("profile", "pointwise_control")).strip().lower()
        pointwise_loss_name = str(loss_configuration.get("pointwise_loss", "mse")).strip().lower()
        weight_dictionary = dict(loss_configuration.get("weights", {}))
        harmonic_index_list = list(loss_configuration.get("harmonic_index_list", []))
        enable_physics_diagnostics = bool(
            loss_configuration.get("enable_physics_diagnostics", False)
        )
        physics_maximum_collocation_points = int(
            loss_configuration.get("physics_maximum_collocation_points", 256)
        )
        physics_maximum_boundary_conditions = int(
            loss_configuration.get("physics_maximum_boundary_conditions", 16)
        )
        huber_delta = float(loss_configuration.get("huber_delta", loss_configuration.get("smooth_l1_beta", 1.0)))
        quantile_level_list = [
            float(quantile_level)
            for quantile_level in loss_configuration.get("quantile_level_list", [0.1, 0.5, 0.9])
        ]
        deterministic_output_index = int(loss_configuration.get("deterministic_output_index", 0))
        gaussian_log_sigma_min = float(loss_configuration.get("gaussian_log_sigma_min", -7.0))
        gaussian_log_sigma_max = float(loss_configuration.get("gaussian_log_sigma_max", 5.0))
        gaussian_sigma_min = float(loss_configuration.get("gaussian_sigma_min", 1.0e-4))
        mixture_component_count = int(loss_configuration.get("mixture_component_count", 1))
        mixture_log_sigma_min = float(loss_configuration.get("mixture_log_sigma_min", -7.0))
        mixture_log_sigma_max = float(loss_configuration.get("mixture_log_sigma_max", 5.0))
        mixture_sigma_min = float(loss_configuration.get("mixture_sigma_min", 1.0e-4))
        quantile_crossing_penalty_weight = float(loss_configuration.get("quantile_crossing_penalty_weight", 0.0))
        enable_optimization_instrumentation = bool(
            loss_configuration.get(
                "enable_optimization_instrumentation",
                False,
            )
        )
        optimization_instrumentation_ema_decay = float(
            loss_configuration.get(
                "optimization_instrumentation_ema_decay",
                0.95,
            )
        )
        optimization_instrumentation_seed = int(
            loss_configuration.get(
                "optimization_instrumentation_seed",
                314159,
            )
        )

        assert deterministic_output_index >= 0, f"Deterministic Output Index must be non-negative | {deterministic_output_index}"
        assert gaussian_log_sigma_min < gaussian_log_sigma_max, (
            f"Gaussian log-sigma bounds must be ordered | {gaussian_log_sigma_min} vs {gaussian_log_sigma_max}"
        )
        assert gaussian_sigma_min > 0.0, f"Gaussian Sigma Min must be positive | {gaussian_sigma_min}"
        assert mixture_component_count > 0, f"Mixture Component Count must be positive | {mixture_component_count}"
        assert mixture_log_sigma_min < mixture_log_sigma_max, (
            f"Mixture log-sigma bounds must be ordered | {mixture_log_sigma_min} vs {mixture_log_sigma_max}"
        )
        assert mixture_sigma_min > 0.0, f"Mixture Sigma Min must be positive | {mixture_sigma_min}"
        assert all(0.0 < quantile_level < 1.0 for quantile_level in quantile_level_list), (
            f"Quantile levels must be inside (0, 1) | {quantile_level_list}"
        )
        assert physics_maximum_collocation_points > 0
        assert physics_maximum_boundary_conditions > 0
        assert 0.0 <= optimization_instrumentation_ema_decay < 1.0

        return {
            "profile": loss_profile,
            "pointwise_loss": pointwise_loss_name,
            "huber_delta": huber_delta,
            "quantile_level_list": quantile_level_list,
            "deterministic_output_index": deterministic_output_index,
            "gaussian_log_sigma_min": gaussian_log_sigma_min,
            "gaussian_log_sigma_max": gaussian_log_sigma_max,
            "gaussian_sigma_min": gaussian_sigma_min,
            "mixture_component_count": mixture_component_count,
            "mixture_log_sigma_min": mixture_log_sigma_min,
            "mixture_log_sigma_max": mixture_log_sigma_max,
            "mixture_sigma_min": mixture_sigma_min,
            "quantile_crossing_penalty_weight": quantile_crossing_penalty_weight,
            "point_weight": float(weight_dictionary.get("point", 1.0)),
            "centered_weight": float(weight_dictionary.get("centered", 0.0)),
            "offset_weight": float(weight_dictionary.get("offset", 0.0)),
            "amplitude_weight": float(weight_dictionary.get("amplitude", 0.0)),
            "harmonic_weight": float(weight_dictionary.get("harmonic", 0.0)),
            "derivative_weight": float(weight_dictionary.get("derivative", 0.0)),
            "residual_energy_weight": float(
                weight_dictionary.get("residual_energy", 0.0)
            ),
            "physics_oscillator_weight": float(
                weight_dictionary.get("physics_oscillator", 0.0)
            ),
            "physics_periodic_value_weight": float(
                weight_dictionary.get("physics_periodic_value", 0.0)
            ),
            "physics_periodic_slope_weight": float(
                weight_dictionary.get("physics_periodic_slope", 0.0)
            ),
            "physics_analytical_anchor_weight": float(
                weight_dictionary.get("physics_analytical_anchor", 0.0)
            ),
            "physics_compliance_equation_weight": float(
                weight_dictionary.get("physics_compliance_equation", 0.0)
            ),
            "physics_zero_torque_boundary_weight": float(
                weight_dictionary.get("physics_zero_torque_boundary", 0.0)
            ),
            "physics_compliance_monotonicity_weight": float(
                weight_dictionary.get(
                    "physics_compliance_monotonicity",
                    0.0,
                )
            ),
            "physics_stiffness_bounds_weight": float(
                weight_dictionary.get("physics_stiffness_bounds", 0.0)
            ),
            "physics_periodic_mean_weight": float(
                weight_dictionary.get("physics_periodic_mean", 0.0)
            ),
            "enable_physics_diagnostics": enable_physics_diagnostics,
            "physics_maximum_collocation_points": (
                physics_maximum_collocation_points
            ),
            "physics_maximum_boundary_conditions": (
                physics_maximum_boundary_conditions
            ),
            "enable_optimization_instrumentation": (
                enable_optimization_instrumentation
            ),
            "optimization_instrumentation_ema_decay": (
                optimization_instrumentation_ema_decay
            ),
            "optimization_instrumentation_seed": (
                optimization_instrumentation_seed
            ),
            "harmonic_index_list": [int(harmonic_index) for harmonic_index in harmonic_index_list if int(harmonic_index) > 0],
        }

    def _build_optimization_instrumentation(
        self,
    ) -> PhysicsGuidedOptimizationInstrumentation | None:
        """Build fixed-weight Stage 2 diagnostics when explicitly enabled."""

        if not bool(
            self.loss_configuration[
                "enable_optimization_instrumentation"
            ]
        ):
            return None

        component_configuration_list = [
            LossComponentConfiguration(
                name="data_fit",
                unit_label="normalized_te_squared",
                normalization_scale=1.0,
                fixed_weight=float(
                    self.loss_configuration["point_weight"]
                ),
                role="main",
            )
        ]
        stage4_formulation = str(
            getattr(self.regression_model, "formulation", "")
        ).upper()
        if stage4_formulation in {"R2", "R3", "R4", "R5"}:
            component_configuration_list.append(
                LossComponentConfiguration(
                    name="residual_energy",
                    unit_label="normalized_residual_squared",
                    normalization_scale=1.0,
                    fixed_weight=float(
                        self.loss_configuration["residual_energy_weight"]
                    ),
                    role="auxiliary",
                )
            )
        return PhysicsGuidedOptimizationInstrumentation(
            component_configuration_list=component_configuration_list,
            ema_decay=float(
                self.loss_configuration[
                    "optimization_instrumentation_ema_decay"
                ]
            ),
            random_seed=int(
                self.loss_configuration[
                    "optimization_instrumentation_seed"
                ]
            ),
        )

    def compute_pointwise_prediction_loss(self, prediction_tensor: torch.Tensor, target_tensor: torch.Tensor) -> torch.Tensor:

        """Compute the configured normalized-space pointwise regression loss."""

        # Resolve Pointwise Loss Name
        pointwise_loss_name = str(self.loss_configuration["pointwise_loss"])
        error_tensor = prediction_tensor - target_tensor

        # Dispatch Supported Losses
        if pointwise_loss_name in ["mse", "l2", "mean_squared_error"]:
            return torch.mean(torch.square(error_tensor))

        if pointwise_loss_name in ["mae", "l1", "mean_absolute_error"]:
            return torch.mean(torch.abs(error_tensor))

        if pointwise_loss_name in ["smooth_l1", "huber"]:
            huber_delta = float(self.loss_configuration["huber_delta"])
            assert huber_delta > 0.0, f"Huber Delta must be positive | {huber_delta}"
            return torch_functional.huber_loss(prediction_tensor, target_tensor, reduction="mean", delta=huber_delta)

        if pointwise_loss_name in ["log_cosh", "logcosh"]:
            absolute_error_tensor = torch.abs(error_tensor)
            return torch.mean(absolute_error_tensor + torch_functional.softplus(-2.0 * absolute_error_tensor) - torch.log(torch.tensor(2.0, device=absolute_error_tensor.device)))

        if pointwise_loss_name in ["quantile_pinball", "pinball", "quantile"]:
            return self.compute_quantile_pinball_loss(prediction_tensor, target_tensor)

        if pointwise_loss_name in ["gaussian_nll", "gaussian_negative_log_likelihood"]:
            return self.compute_gaussian_negative_log_likelihood_loss(prediction_tensor, target_tensor)

        if pointwise_loss_name in ["mixture_density_nll", "mdn_nll", "mixture_gaussian_nll"]:
            return self.compute_mixture_density_negative_log_likelihood_loss(prediction_tensor, target_tensor)

        raise ValueError(f"Unsupported pointwise loss | {pointwise_loss_name}")

    def compute_quantile_pinball_loss(self, prediction_tensor: torch.Tensor, target_tensor: torch.Tensor) -> torch.Tensor:

        """Compute multi-quantile pinball loss in normalized target space."""

        quantile_level_list = list(self.loss_configuration["quantile_level_list"])
        assert prediction_tensor.shape[-1] == len(quantile_level_list), (
            f"Quantile output size mismatch | {prediction_tensor.shape[-1]} vs {len(quantile_level_list)}"
        )

        quantile_level_tensor = torch.as_tensor(
            quantile_level_list,
            device=prediction_tensor.device,
            dtype=prediction_tensor.dtype,
        ).reshape(1, -1)
        error_tensor = target_tensor - prediction_tensor
        pinball_loss_tensor = torch.maximum(
            quantile_level_tensor * error_tensor,
            (quantile_level_tensor - 1.0) * error_tensor,
        )
        pinball_loss = torch.mean(pinball_loss_tensor)

        crossing_penalty_weight = float(self.loss_configuration["quantile_crossing_penalty_weight"])
        if crossing_penalty_weight > 0.0 and prediction_tensor.shape[-1] > 1:
            quantile_delta_tensor = prediction_tensor[:, :-1] - prediction_tensor[:, 1:]
            crossing_penalty = torch.mean(torch_functional.relu(quantile_delta_tensor))
            pinball_loss = pinball_loss + crossing_penalty_weight * crossing_penalty

        return pinball_loss

    def compute_gaussian_negative_log_likelihood_loss(
        self,
        prediction_tensor: torch.Tensor,
        target_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Compute guarded Gaussian NLL in normalized target space."""

        assert prediction_tensor.shape[-1] == 2, f"Gaussian output must contain mu and log_sigma | {prediction_tensor.shape[-1]}"
        mu_tensor = prediction_tensor[:, 0:1]
        raw_log_sigma_tensor = prediction_tensor[:, 1:2]
        log_sigma_tensor = torch.clamp(
            raw_log_sigma_tensor,
            min=float(self.loss_configuration["gaussian_log_sigma_min"]),
            max=float(self.loss_configuration["gaussian_log_sigma_max"]),
        )
        sigma_tensor = torch.clamp(torch.exp(log_sigma_tensor), min=float(self.loss_configuration["gaussian_sigma_min"]))
        normalized_residual_tensor = (target_tensor - mu_tensor) / sigma_tensor
        log_two_pi_tensor = torch.log(torch.as_tensor(2.0 * torch.pi, device=prediction_tensor.device, dtype=prediction_tensor.dtype))
        return torch.mean(0.5 * torch.square(normalized_residual_tensor) + log_sigma_tensor + 0.5 * log_two_pi_tensor)

    def split_mixture_density_output_tensor(
        self,
        prediction_tensor: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:

        """Split MDN output into logits, means, and guarded log-sigmas."""

        component_count = int(self.loss_configuration["mixture_component_count"])
        expected_output_size = component_count * 3
        assert prediction_tensor.shape[-1] == expected_output_size, (
            f"MDN output size mismatch | {prediction_tensor.shape[-1]} vs {expected_output_size}"
        )

        mixture_logit_tensor = prediction_tensor[:, 0:component_count]
        component_mean_tensor = prediction_tensor[:, component_count:2 * component_count]
        raw_log_sigma_tensor = prediction_tensor[:, 2 * component_count:3 * component_count]
        log_sigma_tensor = torch.clamp(
            raw_log_sigma_tensor,
            min=float(self.loss_configuration["mixture_log_sigma_min"]),
            max=float(self.loss_configuration["mixture_log_sigma_max"]),
        )
        return mixture_logit_tensor, component_mean_tensor, log_sigma_tensor

    def compute_mixture_density_negative_log_likelihood_loss(
        self,
        prediction_tensor: torch.Tensor,
        target_tensor: torch.Tensor,
    ) -> torch.Tensor:

        """Compute stable Gaussian-mixture NLL in normalized target space."""

        mixture_logit_tensor, component_mean_tensor, log_sigma_tensor = self.split_mixture_density_output_tensor(
            prediction_tensor
        )
        sigma_tensor = torch.clamp(
            torch.exp(log_sigma_tensor),
            min=float(self.loss_configuration["mixture_sigma_min"]),
        )
        normalized_residual_tensor = (target_tensor - component_mean_tensor) / sigma_tensor
        log_two_pi_tensor = torch.log(
            torch.as_tensor(2.0 * torch.pi, device=prediction_tensor.device, dtype=prediction_tensor.dtype)
        )
        component_log_probability_tensor = (
            -0.5 * torch.square(normalized_residual_tensor)
            - log_sigma_tensor
            - 0.5 * log_two_pi_tensor
        )
        mixture_log_weight_tensor = torch_functional.log_softmax(mixture_logit_tensor, dim=-1)
        sample_log_probability_tensor = torch.logsumexp(
            mixture_log_weight_tensor + component_log_probability_tensor,
            dim=-1,
        )
        return torch.mean(-sample_log_probability_tensor)

    def compute_mixture_expectation_tensor(self, model_output_tensor: torch.Tensor) -> torch.Tensor:

        """Compute deterministic MDN playback as the mixture expectation."""

        mixture_logit_tensor, component_mean_tensor, _log_sigma_tensor = self.split_mixture_density_output_tensor(
            model_output_tensor
        )
        mixture_weight_tensor = torch.softmax(mixture_logit_tensor, dim=-1)
        return torch.sum(mixture_weight_tensor * component_mean_tensor, dim=-1, keepdim=True)

    def extract_deterministic_prediction_tensor(self, model_output_tensor: torch.Tensor) -> torch.Tensor:

        """Select the deterministic channel used for MAE/RMSE and TE curve-verification playback."""

        pointwise_loss_name = str(self.loss_configuration["pointwise_loss"])
        if pointwise_loss_name in ["gaussian_nll", "gaussian_negative_log_likelihood"]:
            assert model_output_tensor.shape[-1] >= 1, "Gaussian output must expose mu at index 0"
            return model_output_tensor[:, 0:1]

        if pointwise_loss_name in ["quantile_pinball", "pinball", "quantile"]:
            deterministic_output_index = int(self.loss_configuration["deterministic_output_index"])
            assert deterministic_output_index < model_output_tensor.shape[-1], (
                f"Deterministic Output Index out of range | {deterministic_output_index} vs {model_output_tensor.shape[-1]}"
            )
            return model_output_tensor[:, deterministic_output_index:deterministic_output_index + 1]

        if pointwise_loss_name in ["mixture_density_nll", "mdn_nll", "mixture_gaussian_nll"]:
            return self.compute_mixture_expectation_tensor(model_output_tensor)

        assert model_output_tensor.shape[-1] == self.target_mean.numel(), (
            f"Deterministic output size mismatch | {model_output_tensor.shape[-1]} vs {self.target_mean.numel()}"
        )
        return model_output_tensor

    def compute_probabilistic_metric_dictionary(
        self,
        model_output_tensor: torch.Tensor,
        normalized_target_tensor: torch.Tensor,
    ) -> dict[str, torch.Tensor]:

        """Compute optional uncertainty diagnostics from raw model outputs."""

        pointwise_loss_name = str(self.loss_configuration["pointwise_loss"])
        metric_dictionary: dict[str, torch.Tensor] = {}

        if pointwise_loss_name in ["quantile_pinball", "pinball", "quantile"]:
            assert model_output_tensor.shape[-1] >= 3, "Quantile diagnostics require lower, median, and upper channels"
            lower_quantile_tensor = model_output_tensor[:, 0:1]
            upper_quantile_tensor = model_output_tensor[:, -1:]
            interval_width_tensor = self.denormalize_target_tensor(upper_quantile_tensor) - self.denormalize_target_tensor(lower_quantile_tensor)
            coverage_tensor = (
                (normalized_target_tensor >= lower_quantile_tensor)
                & (normalized_target_tensor <= upper_quantile_tensor)
            ).float()
            crossing_tensor = (lower_quantile_tensor > upper_quantile_tensor).float()
            metric_dictionary["interval_coverage"] = torch.mean(coverage_tensor)
            metric_dictionary["interval_width"] = torch.mean(torch.abs(interval_width_tensor))
            metric_dictionary["quantile_crossing_rate"] = torch.mean(crossing_tensor)

        if pointwise_loss_name in ["gaussian_nll", "gaussian_negative_log_likelihood"]:
            mu_tensor = model_output_tensor[:, 0:1]
            log_sigma_tensor = torch.clamp(
                model_output_tensor[:, 1:2],
                min=float(self.loss_configuration["gaussian_log_sigma_min"]),
                max=float(self.loss_configuration["gaussian_log_sigma_max"]),
            )
            sigma_tensor = torch.clamp(torch.exp(log_sigma_tensor), min=float(self.loss_configuration["gaussian_sigma_min"]))
            z80_value = 1.2815515655446004
            lower_tensor = mu_tensor - z80_value * sigma_tensor
            upper_tensor = mu_tensor + z80_value * sigma_tensor
            interval_width_tensor = self.denormalize_target_tensor(upper_tensor) - self.denormalize_target_tensor(lower_tensor)
            coverage_tensor = ((normalized_target_tensor >= lower_tensor) & (normalized_target_tensor <= upper_tensor)).float()
            metric_dictionary["interval_coverage"] = torch.mean(coverage_tensor)
            metric_dictionary["interval_width"] = torch.mean(torch.abs(interval_width_tensor))
            metric_dictionary["mean_sigma"] = torch.mean(sigma_tensor * self.target_std)

        if pointwise_loss_name in ["mixture_density_nll", "mdn_nll", "mixture_gaussian_nll"]:
            mixture_logit_tensor, component_mean_tensor, log_sigma_tensor = self.split_mixture_density_output_tensor(
                model_output_tensor
            )
            mixture_weight_tensor = torch.softmax(mixture_logit_tensor, dim=-1)
            log_mixture_weight_tensor = torch_functional.log_softmax(mixture_logit_tensor, dim=-1)
            sigma_tensor = torch.clamp(
                torch.exp(log_sigma_tensor),
                min=float(self.loss_configuration["mixture_sigma_min"]),
            )
            entropy_tensor = -torch.sum(mixture_weight_tensor * log_mixture_weight_tensor, dim=-1)
            effective_component_tensor = torch.exp(entropy_tensor)
            component_mean_physical_tensor = self.denormalize_target_tensor(component_mean_tensor)
            component_scale_physical_tensor = sigma_tensor * self.target_std
            component_separation_tensor = (
                torch.max(component_mean_physical_tensor, dim=-1).values
                - torch.min(component_mean_physical_tensor, dim=-1).values
            )
            metric_dictionary["mixture_weight_entropy"] = torch.mean(entropy_tensor)
            metric_dictionary["mixture_effective_components"] = torch.mean(effective_component_tensor)
            metric_dictionary["mixture_mean_sigma"] = torch.mean(component_scale_physical_tensor)
            metric_dictionary["mixture_component_separation"] = torch.mean(torch.abs(component_separation_tensor))

        return metric_dictionary

    def compute_curve_aware_loss_dictionary(
        self,
        batch_dictionary: dict[str, torch.Tensor],
        batch_output_dictionary: dict[str, torch.Tensor],
        pointwise_loss: torch.Tensor,
    ) -> dict[str, torch.Tensor]:

        """Compute optional curve-aware loss terms from collated curve groups."""

        # Extract Configured Weights
        point_weight = float(self.loss_configuration["point_weight"])
        centered_weight = float(self.loss_configuration["centered_weight"])
        offset_weight = float(self.loss_configuration["offset_weight"])
        amplitude_weight = float(self.loss_configuration["amplitude_weight"])
        harmonic_weight = float(self.loss_configuration["harmonic_weight"])
        derivative_weight = float(self.loss_configuration["derivative_weight"])
        residual_energy_weight = float(
            self.loss_configuration["residual_energy_weight"]
        )
        physics_oscillator_weight = float(
            self.loss_configuration["physics_oscillator_weight"]
        )
        physics_periodic_value_weight = float(
            self.loss_configuration["physics_periodic_value_weight"]
        )
        physics_periodic_slope_weight = float(
            self.loss_configuration["physics_periodic_slope_weight"]
        )
        physics_analytical_anchor_weight = float(
            self.loss_configuration["physics_analytical_anchor_weight"]
        )
        physics_compliance_equation_weight = float(
            self.loss_configuration["physics_compliance_equation_weight"]
        )
        physics_zero_torque_boundary_weight = float(
            self.loss_configuration["physics_zero_torque_boundary_weight"]
        )
        physics_compliance_monotonicity_weight = float(
            self.loss_configuration[
                "physics_compliance_monotonicity_weight"
            ]
        )
        physics_stiffness_bounds_weight = float(
            self.loss_configuration["physics_stiffness_bounds_weight"]
        )
        physics_periodic_mean_weight = float(
            self.loss_configuration["physics_periodic_mean_weight"]
        )
        harmonic_index_list = list(self.loss_configuration["harmonic_index_list"])

        # Initialize Loss Terms
        zero_loss = pointwise_loss * 0.0
        centered_shape_loss = zero_loss
        curve_offset_loss = zero_loss
        curve_amplitude_loss = zero_loss
        sparse_harmonic_shape_loss = zero_loss
        curve_derivative_shape_loss = zero_loss
        residual_energy_loss = zero_loss
        physics_oscillator_residual_loss = zero_loss
        physics_periodic_value_loss = zero_loss
        physics_periodic_slope_loss = zero_loss
        physics_analytical_anchor_loss = zero_loss
        physics_compliance_equation_loss = zero_loss
        physics_zero_torque_boundary_loss = zero_loss
        physics_compliance_monotonicity_loss = zero_loss
        physics_stiffness_bounds_loss = zero_loss
        physics_periodic_mean_loss = zero_loss
        physics_collocation_point_count = zero_loss
        physics_boundary_condition_count = zero_loss

        # Compute The Only Stage 4 Auxiliary Objective When Available
        residual_prediction_tensor = batch_output_dictionary.get(
            "residual_prediction_tensor"
        )
        if isinstance(residual_prediction_tensor, torch.Tensor):
            residual_energy_loss = torch.mean(
                torch.square(residual_prediction_tensor)
            )

        curve_count_tensor = batch_dictionary.get("curve_count", None)
        count_per_curve_tensor = batch_dictionary.get("sequence_count_per_curve", batch_dictionary.get("point_count_per_curve", None))
        can_compute_curve_terms = isinstance(count_per_curve_tensor, torch.Tensor) and int(count_per_curve_tensor.numel()) > 0

        # Compute Curve Terms Only When The Collate Function Preserved Per-Curve Counts
        if can_compute_curve_terms:
            prediction_tensor = batch_output_dictionary["prediction_tensor"]
            target_tensor = batch_output_dictionary["target_tensor"]
            angular_position_tensor = batch_dictionary["angular_position_deg"].to(prediction_tensor.device).float()
            count_per_curve_tensor = count_per_curve_tensor.to(prediction_tensor.device).long()

            centered_loss_list: list[torch.Tensor] = []
            offset_loss_list: list[torch.Tensor] = []
            amplitude_loss_list: list[torch.Tensor] = []
            harmonic_loss_list: list[torch.Tensor] = []
            derivative_loss_list: list[torch.Tensor] = []
            start_index = 0

            # Walk Contiguous Per-Curve Segments In The Collated Batch
            for curve_count in count_per_curve_tensor.tolist():
                end_index = start_index + int(curve_count)
                curve_prediction_tensor = prediction_tensor[start_index:end_index]
                curve_target_tensor = target_tensor[start_index:end_index]
                curve_angle_tensor = angular_position_tensor[start_index:end_index]
                start_index = end_index

                if int(curve_prediction_tensor.numel()) == 0:
                    continue

                prediction_mean_tensor = torch.mean(curve_prediction_tensor, dim=0, keepdim=True)
                target_mean_tensor = torch.mean(curve_target_tensor, dim=0, keepdim=True)
                centered_prediction_tensor = curve_prediction_tensor - prediction_mean_tensor
                centered_target_tensor = curve_target_tensor - target_mean_tensor

                centered_loss_list.append(torch.mean(torch.square(centered_prediction_tensor - centered_target_tensor)))
                offset_loss_list.append(torch.mean(torch.square(prediction_mean_tensor - target_mean_tensor)))

                prediction_amplitude_tensor = torch.max(curve_prediction_tensor, dim=0).values - torch.min(curve_prediction_tensor, dim=0).values
                target_amplitude_tensor = torch.max(curve_target_tensor, dim=0).values - torch.min(curve_target_tensor, dim=0).values
                amplitude_loss_list.append(torch.mean(torch.square(prediction_amplitude_tensor - target_amplitude_tensor)))

                if int(curve_prediction_tensor.shape[0]) > 1:
                    prediction_derivative_tensor = curve_prediction_tensor[1:] - curve_prediction_tensor[:-1]
                    target_derivative_tensor = curve_target_tensor[1:] - curve_target_tensor[:-1]
                    derivative_loss_list.append(torch.mean(torch.square(prediction_derivative_tensor - target_derivative_tensor)))

                if harmonic_index_list:
                    harmonic_loss_list.append(
                        self.compute_sparse_harmonic_shape_loss(
                            curve_angle_tensor,
                            centered_prediction_tensor,
                            centered_target_tensor,
                            harmonic_index_list,
                        )
                    )

            if centered_loss_list:
                centered_shape_loss = torch.stack(centered_loss_list).mean()
                curve_offset_loss = torch.stack(offset_loss_list).mean()
                curve_amplitude_loss = torch.stack(amplitude_loss_list).mean()
                if harmonic_loss_list:
                    sparse_harmonic_shape_loss = torch.stack(harmonic_loss_list).mean()
                if derivative_loss_list:
                    curve_derivative_shape_loss = torch.stack(derivative_loss_list).mean()

        # Compute Target-Free PINN Residuals Through The Model Contract
        physics_weight_sum = (
            physics_oscillator_weight
            + physics_periodic_value_weight
            + physics_periodic_slope_weight
            + physics_analytical_anchor_weight
            + physics_compliance_equation_weight
            + physics_zero_torque_boundary_weight
            + physics_compliance_monotonicity_weight
            + physics_stiffness_bounds_weight
            + physics_periodic_mean_weight
        )
        should_compute_physics = bool(
            self.loss_configuration["enable_physics_diagnostics"]
        ) or physics_weight_sum > 0.0
        if should_compute_physics:
            assert hasattr(
                self.regression_model,
                "compute_physics_residual_dictionary",
            ), (
                "Configured physics diagnostics require a model physics "
                "residual contract"
            )
            raw_input_tensor = batch_dictionary["input_tensor"].float()
            normalized_input_tensor = self.normalize_input_tensor(
                raw_input_tensor
            )
            physics_loss_dictionary = (
                self.regression_model.compute_physics_residual_dictionary(
                    raw_input_tensor,
                    normalized_input_tensor,
                    maximum_collocation_points=int(
                        self.loss_configuration[
                            "physics_maximum_collocation_points"
                        ]
                    ),
                    maximum_boundary_conditions=int(
                        self.loss_configuration[
                            "physics_maximum_boundary_conditions"
                        ]
                    ),
                    target_mean_tensor=self.target_mean,
                    target_std_tensor=self.target_std,
                )
            )
            physics_oscillator_residual_loss = physics_loss_dictionary[
                "physics_oscillator_residual_loss"
            ]
            physics_periodic_value_loss = physics_loss_dictionary[
                "physics_periodic_value_loss"
            ]
            physics_periodic_slope_loss = physics_loss_dictionary[
                "physics_periodic_slope_loss"
            ]
            physics_analytical_anchor_loss = physics_loss_dictionary[
                "physics_analytical_anchor_loss"
            ]
            physics_compliance_equation_loss = physics_loss_dictionary.get(
                "physics_compliance_equation_loss",
                zero_loss,
            )
            physics_zero_torque_boundary_loss = physics_loss_dictionary.get(
                "physics_zero_torque_boundary_loss",
                zero_loss,
            )
            physics_compliance_monotonicity_loss = (
                physics_loss_dictionary.get(
                    "physics_compliance_monotonicity_loss",
                    zero_loss,
                )
            )
            physics_stiffness_bounds_loss = physics_loss_dictionary.get(
                "physics_stiffness_bounds_loss",
                zero_loss,
            )
            physics_periodic_mean_loss = physics_loss_dictionary.get(
                "physics_periodic_mean_loss",
                zero_loss,
            )
            physics_collocation_point_count = physics_loss_dictionary[
                "physics_collocation_point_count"
            ]
            physics_boundary_condition_count = physics_loss_dictionary[
                "physics_boundary_condition_count"
            ]

        # Combine Weighted Terms
        total_loss = (
            point_weight * pointwise_loss
            + centered_weight * centered_shape_loss
            + offset_weight * curve_offset_loss
            + amplitude_weight * curve_amplitude_loss
            + harmonic_weight * sparse_harmonic_shape_loss
            + derivative_weight * curve_derivative_shape_loss
            + residual_energy_weight * residual_energy_loss
            + physics_oscillator_weight * physics_oscillator_residual_loss
            + physics_periodic_value_weight * physics_periodic_value_loss
            + physics_periodic_slope_weight * physics_periodic_slope_loss
            + physics_analytical_anchor_weight * physics_analytical_anchor_loss
            + physics_compliance_equation_weight
            * physics_compliance_equation_loss
            + physics_zero_torque_boundary_weight
            * physics_zero_torque_boundary_loss
            + physics_compliance_monotonicity_weight
            * physics_compliance_monotonicity_loss
            + physics_stiffness_bounds_weight
            * physics_stiffness_bounds_loss
            + physics_periodic_mean_weight * physics_periodic_mean_loss
        )

        return {
            "loss": total_loss,
            "pointwise_loss": pointwise_loss,
            "centered_curve_shape_loss": centered_shape_loss,
            "curve_offset_loss": curve_offset_loss,
            "curve_amplitude_loss": curve_amplitude_loss,
            "sparse_harmonic_shape_loss": sparse_harmonic_shape_loss,
            "curve_derivative_shape_loss": curve_derivative_shape_loss,
            "residual_energy_loss": residual_energy_loss,
            "physics_oscillator_residual_loss": (
                physics_oscillator_residual_loss
            ),
            "physics_periodic_value_loss": physics_periodic_value_loss,
            "physics_periodic_slope_loss": physics_periodic_slope_loss,
            "physics_analytical_anchor_loss": physics_analytical_anchor_loss,
            "physics_compliance_equation_loss": (
                physics_compliance_equation_loss
            ),
            "physics_zero_torque_boundary_loss": (
                physics_zero_torque_boundary_loss
            ),
            "physics_compliance_monotonicity_loss": (
                physics_compliance_monotonicity_loss
            ),
            "physics_stiffness_bounds_loss": physics_stiffness_bounds_loss,
            "physics_periodic_mean_loss": physics_periodic_mean_loss,
            "physics_collocation_point_count": physics_collocation_point_count,
            "physics_boundary_condition_count": (
                physics_boundary_condition_count
            ),
            "curve_aware_curve_count": torch.as_tensor(
                int(curve_count_tensor) if isinstance(curve_count_tensor, int) else int(count_per_curve_tensor.numel()) if can_compute_curve_terms else 0,
                device=pointwise_loss.device,
                dtype=torch.float32,
            ),
        }

    def compute_sparse_harmonic_shape_loss(
        self,
        angular_position_tensor: torch.Tensor,
        centered_prediction_tensor: torch.Tensor,
        centered_target_tensor: torch.Tensor,
        harmonic_index_list: list[int],
    ) -> torch.Tensor:

        """Compare centered prediction and truth on sparse sine/cosine terms."""

        # Prepare Angle Tensor In Radians
        angle_radian_tensor = torch.deg2rad(angular_position_tensor.reshape(-1, 1))
        prediction_vector = centered_prediction_tensor.reshape(-1, 1)
        target_vector = centered_target_tensor.reshape(-1, 1)
        harmonic_loss_list: list[torch.Tensor] = []

        # Compare Projection Coefficients For Each Harmonic
        for harmonic_index in harmonic_index_list:
            sine_basis_tensor = torch.sin(float(harmonic_index) * angle_radian_tensor)
            cosine_basis_tensor = torch.cos(float(harmonic_index) * angle_radian_tensor)
            prediction_sine_coefficient = torch.mean(prediction_vector * sine_basis_tensor, dim=0)
            target_sine_coefficient = torch.mean(target_vector * sine_basis_tensor, dim=0)
            prediction_cosine_coefficient = torch.mean(prediction_vector * cosine_basis_tensor, dim=0)
            target_cosine_coefficient = torch.mean(target_vector * cosine_basis_tensor, dim=0)
            harmonic_loss_list.append(torch.mean(torch.square(prediction_sine_coefficient - target_sine_coefficient)))
            harmonic_loss_list.append(torch.mean(torch.square(prediction_cosine_coefficient - target_cosine_coefficient)))

        return torch.stack(harmonic_loss_list).mean()

    def set_normalization_statistics(self, normalization_statistics: NormalizationStatistics) -> None:

        """Load normalization tensors into the module buffers.

        Args:
            normalization_statistics: Input and target statistics computed from
                the training split.
        """

        # Validate Statistics Shapes
        assert normalization_statistics.input_feature_mean.shape == self.input_feature_mean.shape, (
            f"Input Feature Mean shape mismatch | {tuple(normalization_statistics.input_feature_mean.shape)} "
            f"vs {tuple(self.input_feature_mean.shape)}"
        )
        assert normalization_statistics.input_feature_std.shape == self.input_feature_std.shape, (
            f"Input Feature Std shape mismatch | {tuple(normalization_statistics.input_feature_std.shape)} "
            f"vs {tuple(self.input_feature_std.shape)}"
        )
        assert normalization_statistics.target_mean.shape == self.target_mean.shape, (
            f"Target Mean shape mismatch | {tuple(normalization_statistics.target_mean.shape)} "
            f"vs {tuple(self.target_mean.shape)}"
        )
        assert normalization_statistics.target_std.shape == self.target_std.shape, (
            f"Target Std shape mismatch | {tuple(normalization_statistics.target_std.shape)} "
            f"vs {tuple(self.target_std.shape)}"
        )

        # Copy Statistics Into Buffers
        self.input_feature_mean.copy_(normalization_statistics.input_feature_mean.float())
        self.input_feature_std.copy_(torch.clamp(normalization_statistics.input_feature_std.float(), min=1.0e-8))
        self.target_mean.copy_(normalization_statistics.target_mean.float())
        self.target_std.copy_(torch.clamp(normalization_statistics.target_std.float(), min=1.0e-8))

        # Propagate Statistics To Physics-Embedded Backbones
        if hasattr(self.regression_model, "set_normalization_statistics"):
            self.regression_model.set_normalization_statistics(
                normalization_statistics
            )

        # Mark Statistics As Ready
        self.normalization_statistics_initialized = True

    def normalize_input_tensor(self, input_tensor: torch.Tensor) -> torch.Tensor:

        """Normalize model inputs with the registered training statistics."""

        # Ensure Normalization Statistics Are Initialized Before Normalizing
        assert self.normalization_statistics_initialized, "Normalization Statistics must be initialized before training"
        return (input_tensor - self.input_feature_mean) / self.input_feature_std

    def normalize_target_tensor(self, target_tensor: torch.Tensor) -> torch.Tensor:

        """Normalize regression targets with the registered statistics."""

        # Ensure Normalization Statistics Are Initialized Before Normalizing
        assert self.normalization_statistics_initialized, "Normalization Statistics must be initialized before training"
        return (target_tensor - self.target_mean) / self.target_std

    def denormalize_target_tensor(self, normalized_target_tensor: torch.Tensor) -> torch.Tensor:

        """Map normalized target predictions back to physical TE units."""

        # Ensure Normalization Statistics Are Initialized Before Denormalizing
        assert self.normalization_statistics_initialized, "Normalization Statistics must be initialized before training"
        return (normalized_target_tensor * self.target_std) + self.target_mean

    def forward(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """Run the backbone on normalized inputs only."""

        # Forward Pass Through Regression Model In Normalized Space
        return self.regression_model(normalized_input_tensor)

    def forward_regression_model(self, input_tensor: torch.Tensor, normalized_input_tensor: torch.Tensor) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:

        """Run the backbone while supporting structured auxiliary outputs.

        Args:
            input_tensor: Raw input tensor before normalization-aware routing.
            normalized_input_tensor: Normalized model input tensor.

        Returns:
            tuple[torch.Tensor, dict[str, torch.Tensor]]: Prediction tensor in
            normalized space plus any auxiliary structured outputs emitted by
            the backbone.
        """

        auxiliary_output_dictionary: dict[str, torch.Tensor] = {}

        # Prefer Context-Aware Model Forward When The Backbone Needs Raw And Normalized Views Together
        if hasattr(self.regression_model, "compute_auxiliary_output_dictionary"):

            # Compute Auxiliary Output Dictionary
            computed_auxiliary_output_dictionary = self.regression_model.compute_auxiliary_output_dictionary(input_tensor, normalized_input_tensor)
            assert isinstance(computed_auxiliary_output_dictionary, dict), "Auxiliary Output Dictionary must be a dictionary"
            assert "prediction_tensor" in computed_auxiliary_output_dictionary, "Auxiliary Output Dictionary must contain prediction_tensor"

            # Extract Prediction And Auxiliary Output Tensors
            prediction_tensor = computed_auxiliary_output_dictionary["prediction_tensor"]
            auxiliary_output_dictionary = {
                key: value
                for key, value in computed_auxiliary_output_dictionary.items()
                if key != "prediction_tensor" and isinstance(value, torch.Tensor)
            }
            return prediction_tensor, auxiliary_output_dictionary

        # Fallback To A Simpler Context-Aware Forward Signature
        if hasattr(self.regression_model, "forward_with_input_context"):
            return self.regression_model.forward_with_input_context(input_tensor, normalized_input_tensor), auxiliary_output_dictionary

        return self(normalized_input_tensor), auxiliary_output_dictionary

    def compute_batch_outputs(self, batch_dictionary: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]:

        """Compute normalized loss terms and denormalized TE metrics.

        Args:
            batch_dictionary: Point-level batch emitted by the datamodule.

        Returns:
            dict[str, torch.Tensor]: Batch outputs including normalized
            predictions, denormalized predictions, and metric tensors.
        """

        # Extract Batch Tensors
        input_tensor = batch_dictionary["input_tensor"].float()
        target_tensor = batch_dictionary["target_tensor"].float()

        # Normalize Input And Target
        normalized_input_tensor = self.normalize_input_tensor(input_tensor)
        normalized_target_tensor = self.normalize_target_tensor(target_tensor)

        # Forward Pass
        normalized_model_output_tensor, auxiliary_output_dictionary = self.forward_regression_model(input_tensor, normalized_input_tensor)
        normalized_prediction_tensor = self.extract_deterministic_prediction_tensor(normalized_model_output_tensor)

        # Denormalize Predictions For Interpretable Metrics
        prediction_tensor = self.denormalize_target_tensor(normalized_prediction_tensor)
        mae = torch.mean(torch.abs(prediction_tensor - target_tensor))
        rmse = torch.sqrt(torch.mean(torch.square(prediction_tensor - target_tensor)))

        # Compute Pointwise And Optional Curve-Aware Loss Terms
        pointwise_loss = self.compute_pointwise_prediction_loss(normalized_model_output_tensor, normalized_target_tensor)
        loss_dictionary = self.compute_curve_aware_loss_dictionary(
            batch_dictionary=batch_dictionary,
            batch_output_dictionary={
                "prediction_tensor": normalized_prediction_tensor,
                "target_tensor": normalized_target_tensor,
                **auxiliary_output_dictionary,
            },
            pointwise_loss=pointwise_loss,
        )

        # Create Batch Output Dictionary
        batch_output_dictionary = {
            "input_tensor": input_tensor,
            "target_tensor": target_tensor,
            "normalized_input_tensor": normalized_input_tensor,
            "normalized_target_tensor": normalized_target_tensor,
            "normalized_model_output_tensor": normalized_model_output_tensor,
            "normalized_prediction_tensor": normalized_prediction_tensor,
            "prediction_tensor": prediction_tensor,
            "mae": mae,
            "rmse": rmse,
        }

        # Merge Optional Auxiliary Prediction Tensors Returned By Structured Models
        batch_output_dictionary.update(auxiliary_output_dictionary)
        batch_output_dictionary.update(loss_dictionary)
        batch_output_dictionary.update(self.compute_probabilistic_metric_dictionary(normalized_model_output_tensor, normalized_target_tensor))
        return batch_output_dictionary

    def compute_loss(
        self,
        batch_dictionary: dict[str, torch.Tensor],
        log_prefix: str,
        batch_idx: int | None = None,
    ) -> torch.Tensor:

        """Compute and log one split-specific loss bundle.

        Args:
            batch_dictionary: Point-level batch emitted by the datamodule.
            log_prefix: Prefix used for Lightning metric names such as
                `train`, `val`, or `test`.

        Returns:
            torch.Tensor: Scalar normalized-space MSE loss.
        """

        # Compute Batch Outputs And Metrics
        batch_output_dictionary = self.compute_batch_outputs(batch_dictionary)
        input_tensor = batch_output_dictionary["input_tensor"]
        loss = batch_output_dictionary["loss"]
        mae = batch_output_dictionary["mae"]
        rmse = batch_output_dictionary["rmse"]

        # Log Metrics
        batch_size = int(input_tensor.shape[0])
        self.log(f"{log_prefix}_loss", loss, on_step=False, on_epoch=True, prog_bar=True, batch_size=batch_size)
        self.log(f"{log_prefix}_mae", mae, on_step=False, on_epoch=True, prog_bar=(log_prefix != "train"), batch_size=batch_size)
        self.log(f"{log_prefix}_rmse", rmse, on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)
        self.log(f"{log_prefix}_pointwise_loss", batch_output_dictionary["pointwise_loss"], on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)
        self.log(
            f"{log_prefix}_residual_energy_loss",
            batch_output_dictionary["residual_energy_loss"],
            on_step=False,
            on_epoch=True,
            prog_bar=False,
            batch_size=batch_size,
        )
        self.log(f"{log_prefix}_centered_curve_shape_loss", batch_output_dictionary["centered_curve_shape_loss"], on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)
        self.log(f"{log_prefix}_curve_offset_loss", batch_output_dictionary["curve_offset_loss"], on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)
        self.log(f"{log_prefix}_curve_amplitude_loss", batch_output_dictionary["curve_amplitude_loss"], on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)
        self.log(f"{log_prefix}_sparse_harmonic_shape_loss", batch_output_dictionary["sparse_harmonic_shape_loss"], on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)
        self.log(
            f"{log_prefix}_physics_oscillator_residual_loss",
            batch_output_dictionary["physics_oscillator_residual_loss"],
            on_step=False,
            on_epoch=True,
            prog_bar=False,
            batch_size=batch_size,
        )
        self.log(
            f"{log_prefix}_physics_periodic_value_loss",
            batch_output_dictionary["physics_periodic_value_loss"],
            on_step=False,
            on_epoch=True,
            prog_bar=False,
            batch_size=batch_size,
        )
        self.log(
            f"{log_prefix}_physics_periodic_slope_loss",
            batch_output_dictionary["physics_periodic_slope_loss"],
            on_step=False,
            on_epoch=True,
            prog_bar=False,
            batch_size=batch_size,
        )
        self.log(
            f"{log_prefix}_physics_analytical_anchor_loss",
            batch_output_dictionary["physics_analytical_anchor_loss"],
            on_step=False,
            on_epoch=True,
            prog_bar=False,
            batch_size=batch_size,
        )
        for compliance_metric_name in [
            "physics_compliance_equation_loss",
            "physics_zero_torque_boundary_loss",
            "physics_compliance_monotonicity_loss",
            "physics_stiffness_bounds_loss",
            "physics_periodic_mean_loss",
        ]:
            self.log(
                f"{log_prefix}_{compliance_metric_name}",
                batch_output_dictionary[compliance_metric_name],
                on_step=False,
                on_epoch=True,
                prog_bar=False,
                batch_size=batch_size,
            )

        # Log Phase 3 Inspectable Physical Quantities
        effective_stiffness_tensor = batch_output_dictionary.get(
            "effective_stiffness_nm_per_deg"
        )
        if isinstance(effective_stiffness_tensor, torch.Tensor):
            self.log(
                f"{log_prefix}_effective_stiffness_nm_per_deg",
                torch.mean(effective_stiffness_tensor),
                on_step=False,
                on_epoch=True,
                prog_bar=False,
                batch_size=batch_size,
            )
        elastic_prediction_deg = batch_output_dictionary.get(
            "elastic_prediction_deg"
        )
        if isinstance(elastic_prediction_deg, torch.Tensor):
            self.log(
                f"{log_prefix}_elastic_prediction_mean_abs_deg",
                torch.mean(torch.abs(elastic_prediction_deg)),
                on_step=False,
                on_epoch=True,
                prog_bar=False,
                batch_size=batch_size,
            )
        for probabilistic_metric_name in [
            "interval_coverage",
            "interval_width",
            "quantile_crossing_rate",
            "mean_sigma",
            "mixture_weight_entropy",
            "mixture_effective_components",
            "mixture_mean_sigma",
            "mixture_component_separation",
        ]:
            probabilistic_metric_value = batch_output_dictionary.get(probabilistic_metric_name)
            if isinstance(probabilistic_metric_value, torch.Tensor):
                self.log(f"{log_prefix}_{probabilistic_metric_name}", probabilistic_metric_value, on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)

        # Log Structured-Only Diagnostics When Available
        structured_prediction_tensor = batch_output_dictionary.get("structured_prediction_tensor")
        if isinstance(structured_prediction_tensor, torch.Tensor):
            structured_prediction_denormalized = self.denormalize_target_tensor(structured_prediction_tensor)
            structured_mae = torch.mean(torch.abs(structured_prediction_denormalized - batch_output_dictionary["target_tensor"]))
            structured_rmse = torch.sqrt(torch.mean(torch.square(structured_prediction_denormalized - batch_output_dictionary["target_tensor"])))
            self.log(f"{log_prefix}_structured_mae", structured_mae, on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)
            self.log(f"{log_prefix}_structured_rmse", structured_rmse, on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)

        # Log Wave 3.1 Branch Diagnostics When Available
        base_prediction_tensor = batch_output_dictionary.get("base_prediction_tensor")
        if isinstance(base_prediction_tensor, torch.Tensor):
            base_prediction_denormalized = self.denormalize_target_tensor(base_prediction_tensor)
            base_mae = torch.mean(torch.abs(base_prediction_denormalized - batch_output_dictionary["target_tensor"]))
            base_rmse = torch.sqrt(torch.mean(torch.square(base_prediction_denormalized - batch_output_dictionary["target_tensor"])))
            self.log(f"{log_prefix}_base_mae", base_mae, on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)
            self.log(f"{log_prefix}_base_rmse", base_rmse, on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)

        residual_offset_prediction_tensor = batch_output_dictionary.get("residual_offset_prediction_tensor")
        if isinstance(residual_offset_prediction_tensor, torch.Tensor):
            residual_offset_denormalized = residual_offset_prediction_tensor * self.target_std
            residual_offset_mean_abs = torch.mean(torch.abs(residual_offset_denormalized))
            self.log(f"{log_prefix}_residual_offset_mean_abs", residual_offset_mean_abs, on_step=False, on_epoch=True, prog_bar=False, batch_size=batch_size)

        # Log Stage 4 Physical-Unit Decomposition When Available
        for auxiliary_name in [
            "analytical_prediction_deg",
            "frozen_analytical_prediction_deg",
            "residual_prediction_deg",
            "direct_prediction_deg",
        ]:
            auxiliary_tensor = batch_output_dictionary.get(auxiliary_name)
            if isinstance(auxiliary_tensor, torch.Tensor):
                self.log(
                    f"{log_prefix}_{auxiliary_name}_mean_abs",
                    torch.mean(torch.abs(auxiliary_tensor)),
                    on_step=False,
                    on_epoch=True,
                    prog_bar=False,
                    batch_size=batch_size,
                )

        # Record Per-Loss Gradients On The First Training Batch Of Each Epoch
        if (
            log_prefix == "train"
            and batch_idx == 0
            and self.optimization_instrumentation is not None
        ):
            raw_loss_dictionary = {
                "data_fit": batch_output_dictionary["pointwise_loss"],
            }
            if "residual_energy" in (
                self.optimization_instrumentation
                .component_configuration_dictionary
            ):
                raw_loss_dictionary["residual_energy"] = (
                    batch_output_dictionary["residual_energy_loss"]
                )
            diagnostic_record = (
                self.optimization_instrumentation.build_diagnostic_record(
                    raw_loss_dictionary=raw_loss_dictionary,
                    shared_parameter_sequence=list(
                        self.regression_model.parameters()
                    ),
                    adapter_name="fixed",
                    optimization_step=int(self.global_step),
                )
            )
            for component_name, component_value in diagnostic_record[
                "raw_loss_dictionary"
            ].items():
                self.log(
                    f"train_instrumentation_raw_{component_name}",
                    float(component_value),
                    on_step=True,
                    on_epoch=False,
                    prog_bar=False,
                    batch_size=batch_size,
                )
            for component_name, component_value in diagnostic_record[
                "loss_ema_dictionary"
            ].items():
                self.log(
                    f"train_instrumentation_ema_{component_name}",
                    float(component_value),
                    on_step=True,
                    on_epoch=False,
                    prog_bar=False,
                    batch_size=batch_size,
                )
            for component_name, component_value in diagnostic_record[
                "gradient_norm_dictionary"
            ].items():
                self.log(
                    f"train_instrumentation_gradient_norm_{component_name}",
                    float(component_value),
                    on_step=True,
                    on_epoch=False,
                    prog_bar=False,
                    batch_size=batch_size,
                )
            for pair_name, cosine_value in diagnostic_record[
                "pairwise_gradient_cosine_dictionary"
            ].items():
                self.log(
                    f"train_instrumentation_gradient_cosine_{pair_name}",
                    float(cosine_value),
                    on_step=True,
                    on_epoch=False,
                    prog_bar=False,
                    batch_size=batch_size,
                )

        return loss

    def training_step(self, batch_dictionary: dict[str, torch.Tensor], batch_idx: int) -> torch.Tensor:

        """Run one Lightning training step and return the loss tensor."""

        # Compute Loss And Metrics For Training Step
        return self.compute_loss(
            batch_dictionary,
            "train",
            batch_idx=batch_idx,
        )

    def validation_step(self, batch_dictionary: dict[str, torch.Tensor], batch_idx: int) -> torch.Tensor:

        """Run one Lightning validation step and return the loss tensor."""

        # Compute Loss And Metrics For Validation Step
        return self.compute_loss(batch_dictionary, "val")

    def test_step(self, batch_dictionary: dict[str, torch.Tensor], batch_idx: int) -> torch.Tensor:

        """Run one Lightning test step and return the loss tensor."""

        # Compute Loss And Metrics For Test Step
        return self.compute_loss(batch_dictionary, "test")

    def configure_optimizers(self):

        """Configure the AdamW optimizer for TE regression training."""

        # Exclude Explicitly Frozen Parameters From Optimizer State
        trainable_parameter_list = [
            parameter
            for parameter in self.parameters()
            if parameter.requires_grad
        ]
        assert trainable_parameter_list, (
            "At least one trainable parameter is required"
        )
        return torch.optim.AdamW(
            trainable_parameter_list,
            lr=float(self.hparams.learning_rate),
            weight_decay=float(self.hparams.weight_decay),
        )

    def optimizer_step(
        self,
        epoch: int,
        batch_idx: int,
        optimizer: torch.optim.Optimizer,
        optimizer_closure,
    ) -> None:
        """Execute the normal optimizer step and record its relative size."""

        if self.optimization_instrumentation is None:
            return super().optimizer_step(
                epoch,
                batch_idx,
                optimizer,
                optimizer_closure,
            )

        self._parameter_vector_before_step = (
            capture_trainable_parameter_vector(
                list(self.regression_model.parameters())
            )
        )
        super().optimizer_step(
            epoch,
            batch_idx,
            optimizer,
            optimizer_closure,
        )
        parameter_vector_after_step = capture_trainable_parameter_vector(
            list(self.regression_model.parameters())
        )
        update_ratio = compute_update_to_parameter_ratio(
            self._parameter_vector_before_step,
            parameter_vector_after_step,
        )
        self.log(
            "train_instrumentation_update_to_parameter_ratio",
            update_ratio,
            on_step=True,
            on_epoch=False,
            prog_bar=False,
        )
