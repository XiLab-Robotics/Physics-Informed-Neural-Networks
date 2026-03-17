from __future__ import annotations

# Import PyTorch Lightning Utilities
from lightning.pytorch import LightningModule

# Import PyTorch Utilities
import torch
import torch.nn as nn

# Import DataModule Utilities
from scripts.training.transmission_error_datamodule import NormalizationStatistics

class TransmissionErrorRegressionModule(LightningModule):

    """ Transmission Error Regression Module """

    def __init__(
        self,
        regression_model: nn.Module,
        input_feature_dim: int,
        target_feature_dim: int,
        learning_rate: float = 1.0e-3,
        weight_decay: float = 1.0e-4,
        normalization_statistics: NormalizationStatistics | None = None,
    ) -> None:

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
        self.loss_function = nn.MSELoss()

        # Register Normalization Buffers
        self.register_buffer("input_feature_mean", torch.zeros(input_feature_dim, dtype=torch.float32))
        self.register_buffer("input_feature_std", torch.ones(input_feature_dim, dtype=torch.float32))
        self.register_buffer("target_mean", torch.zeros(target_feature_dim, dtype=torch.float32))
        self.register_buffer("target_std", torch.ones(target_feature_dim, dtype=torch.float32))

        # Initialize Normalization State
        self.normalization_statistics_initialized = False

        # Load Normalization Statistics If Available At Construction Time
        if normalization_statistics is not None: self.set_normalization_statistics(normalization_statistics)

    def set_normalization_statistics(self, normalization_statistics: NormalizationStatistics) -> None:

        """ Set Normalization Statistics """

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

        # Mark Statistics As Ready
        self.normalization_statistics_initialized = True

    def normalize_input_tensor(self, input_tensor: torch.Tensor) -> torch.Tensor:

        """ Normalize Input Tensor """

        # Ensure Normalization Statistics Are Initialized Before Normalizing
        assert self.normalization_statistics_initialized, "Normalization Statistics must be initialized before training"
        return (input_tensor - self.input_feature_mean) / self.input_feature_std

    def normalize_target_tensor(self, target_tensor: torch.Tensor) -> torch.Tensor:

        """ Normalize Target Tensor """

        # Ensure Normalization Statistics Are Initialized Before Normalizing
        assert self.normalization_statistics_initialized, "Normalization Statistics must be initialized before training"
        return (target_tensor - self.target_mean) / self.target_std

    def denormalize_target_tensor(self, normalized_target_tensor: torch.Tensor) -> torch.Tensor:

        """ Denormalize Target Tensor """

        # Ensure Normalization Statistics Are Initialized Before Denormalizing
        assert self.normalization_statistics_initialized, "Normalization Statistics must be initialized before training"
        return (normalized_target_tensor * self.target_std) + self.target_mean

    def forward(self, normalized_input_tensor: torch.Tensor) -> torch.Tensor:

        """ Forward Pass """

        # Forward Pass Through Regression Model In Normalized Space
        return self.regression_model(normalized_input_tensor)

    def compute_batch_outputs(self, batch_dictionary: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]:

        """ Compute Batch Outputs """

        # Extract Batch Tensors
        input_tensor = batch_dictionary["input_tensor"].float()
        target_tensor = batch_dictionary["target_tensor"].float()

        # Normalize Input And Target
        normalized_input_tensor = self.normalize_input_tensor(input_tensor)
        normalized_target_tensor = self.normalize_target_tensor(target_tensor)

        # Forward Pass
        normalized_prediction_tensor = self(normalized_input_tensor)

        # Compute Loss In Normalized Space
        loss = self.loss_function(normalized_prediction_tensor, normalized_target_tensor)

        # Denormalize Predictions For Interpretable Metrics
        prediction_tensor = self.denormalize_target_tensor(normalized_prediction_tensor)
        mae = torch.mean(torch.abs(prediction_tensor - target_tensor))
        rmse = torch.sqrt(torch.mean(torch.square(prediction_tensor - target_tensor)))

        return {
            "input_tensor": input_tensor,
            "target_tensor": target_tensor,
            "normalized_input_tensor": normalized_input_tensor,
            "normalized_target_tensor": normalized_target_tensor,
            "normalized_prediction_tensor": normalized_prediction_tensor,
            "prediction_tensor": prediction_tensor,
            "loss": loss,
            "mae": mae,
            "rmse": rmse,
        }

    def compute_loss(self, batch_dictionary: dict[str, torch.Tensor], log_prefix: str) -> torch.Tensor:

        """ Compute Loss """

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

        return loss

    def training_step(self, batch_dictionary: dict[str, torch.Tensor], batch_idx: int) -> torch.Tensor:

        """ Training Step """

        # Compute Loss And Metrics For Training Step
        return self.compute_loss(batch_dictionary, "train")

    def validation_step(self, batch_dictionary: dict[str, torch.Tensor], batch_idx: int) -> torch.Tensor:

        """ Validation Step """

        # Compute Loss And Metrics For Validation Step
        return self.compute_loss(batch_dictionary, "val")

    def test_step(self, batch_dictionary: dict[str, torch.Tensor], batch_idx: int) -> torch.Tensor:

        """ Test Step """

        # Compute Loss And Metrics For Test Step
        return self.compute_loss(batch_dictionary, "test")

    def configure_optimizers(self):

        """ Configure Optimizers """

        # Configure AdamW Optimizer
        return torch.optim.AdamW(self.parameters(), lr=float(self.hparams.learning_rate), weight_decay=float(self.hparams.weight_decay))
