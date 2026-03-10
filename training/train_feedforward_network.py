from __future__ import annotations

# Import Python Utilities
from pathlib import Path
from pprint import pformat
import shutil

# Import PyTorch Lightning Utilities
from lightning.pytorch import Trainer
from lightning.pytorch.callbacks import Callback
from lightning.pytorch.callbacks import EarlyStopping
from lightning.pytorch.callbacks import ModelCheckpoint
from lightning.pytorch.loggers import TensorBoardLogger

# Import PyTorch Utilities
import torch

# Import YAML Utilities
import yaml

# Import Project Models And Training Utilities
from models.model_factory import create_model
from scripts.datasets.transmission_error_dataset import resolve_project_relative_path
from training.transmission_error_datamodule import TransmissionErrorDataModule
from training.transmission_error_regression_module import TransmissionErrorRegressionModule


PROJECT_PATH = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = PROJECT_PATH / "config" / "feedforward_network_training.yaml"

# Set Torch Matmul Precision
torch.set_float32_matmul_precision("high")


class StartTrainingCallback(Callback):
    """ Start Training Callback """

    def on_train_start(self, trainer, pl_module) -> None:
        """ On Train Start """

        print("\nStart Training Process\n")

    def on_train_end(self, trainer, pl_module) -> None:
        """ On Train End """

        print("\nTraining Done\n")


class StartValidationCallback(Callback):
    """ Start Validation Callback """

    def on_validation_start(self, trainer, pl_module) -> None:
        """ On Validation Start """

        print("\nStart Validation Process\n")

    def on_validation_end(self, trainer, pl_module) -> None:
        """ On Validation End """

        print("\nValidation Done\n")


def load_training_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict:
    """ Load Training Config """

    # Resolve Config Path
    resolved_config_path = resolve_project_relative_path(config_path)
    assert resolved_config_path.exists(), f"Training Config Path does not exist | {resolved_config_path}"

    # Load YAML Configuration
    with resolved_config_path.open("r", encoding="utf-8") as config_file:
        training_config = yaml.safe_load(config_file)

    # Validate Configuration
    assert isinstance(training_config, dict), "Training Config must be a dictionary"

    return training_config


def save_training_config_snapshot(training_config: dict, output_directory: Path) -> None:
    """ Save Training Config Snapshot """

    # Create Output Directory
    output_directory.mkdir(parents=True, exist_ok=True)

    # Save Config Snapshot
    with (output_directory / "feedforward_network_training.yaml").open("w", encoding="utf-8") as config_file:
        yaml.safe_dump(training_config, config_file, sort_keys=False)


def train_feedforward_network(config_path: str | Path = DEFAULT_CONFIG_PATH) -> None:
    """ Train Feedforward Network """

    # Load Training Configuration
    training_config = load_training_config(config_path=config_path)

    # Resolve Output Directory
    output_root = resolve_project_relative_path(training_config["paths"]["output_root"])
    output_directory = output_root / training_config["experiment"]["run_name"]
    output_directory.mkdir(parents=True, exist_ok=True)

    # Save Configuration Snapshot
    save_training_config_snapshot(training_config=training_config, output_directory=output_directory)

    # Initialize DataModule
    datamodule = TransmissionErrorDataModule(
        dataset_config_path=training_config["paths"]["dataset_config_path"],
        curve_batch_size=int(training_config["dataset"]["curve_batch_size"]),
        point_stride=int(training_config["dataset"]["point_stride"]),
        maximum_points_per_curve=training_config["dataset"]["maximum_points_per_curve"],
        num_workers=int(training_config["dataset"]["num_workers"]),
        pin_memory=bool(training_config["dataset"]["pin_memory"]),
    )
    datamodule.setup(stage="fit")

    # Read Dataset Statistics
    input_feature_dim = datamodule.get_input_feature_dim()
    target_feature_dim = datamodule.get_target_feature_dim()
    normalization_statistics = datamodule.get_normalization_statistics()

    # Validate Model Input Size
    configured_input_size = int(training_config["model"]["input_size"])
    assert configured_input_size == input_feature_dim, (
        f"Configured Input Size and Dataset Input Feature Dim mismatch | "
        f"{configured_input_size} vs {input_feature_dim}"
    )

    # Create Regression Model
    regression_backbone = create_model(
        model_type=str(training_config["experiment"]["model_type"]),
        model_configuration=training_config["model"],
    )
    regression_module = TransmissionErrorRegressionModule(
        regression_model=regression_backbone,
        input_feature_dim=input_feature_dim,
        target_feature_dim=target_feature_dim,
        learning_rate=float(training_config["training"]["learning_rate"]),
        weight_decay=float(training_config["training"]["weight_decay"]),
        normalization_statistics=normalization_statistics,
    )

    # Print Training Summary
    print("\nFeedforward Training Configuration:\n")
    print(pformat(training_config, sort_dicts=False))
    print("\nDataset Summary:\n")
    print(f"    Input Feature Dim: {input_feature_dim}")
    print(f"    Target Feature Dim: {target_feature_dim}")
    print(f"    Train Curves: {len(datamodule.train_dataset)}")
    print(f"    Validation Curves: {len(datamodule.validation_dataset)}")
    print(f"    Point Stride: {datamodule.point_stride}")
    print(f"    Maximum Points Per Curve: {datamodule.maximum_points_per_curve}")
    print("\nNormalization Statistics:\n")
    print(f"    Input Feature Mean: {normalization_statistics.input_feature_mean.tolist()}")
    print(f"    Input Feature Std: {normalization_statistics.input_feature_std.tolist()}")
    print(f"    Target Mean: {normalization_statistics.target_mean.tolist()}")
    print(f"    Target Std: {normalization_statistics.target_std.tolist()}")

    # Create Logger And Callbacks
    logger = TensorBoardLogger(save_dir=str(output_directory / "logs"), name="", version="")
    checkpoint_callback = ModelCheckpoint(
        dirpath=str(output_directory / "checkpoints"),
        filename="feedforward-{epoch:03d}-{val_mae:.8f}",
        monitor="val_mae",
        mode="min",
        save_top_k=1,
        save_last=True,
    )
    early_stopping_callback = EarlyStopping(
        monitor="val_mae",
        mode="min",
        patience=int(training_config["training"]["patience"]),
        min_delta=float(training_config["training"]["min_delta"]),
        verbose=True,
    )

    # Create Trainer
    trainer = Trainer(
        accelerator="auto",
        devices="auto",
        min_epochs=int(training_config["training"]["min_epochs"]),
        max_epochs=int(training_config["training"]["max_epochs"]),
        log_every_n_steps=int(training_config["training"]["log_every_n_steps"]),
        deterministic=bool(training_config["training"]["deterministic"]),
        fast_dev_run=bool(training_config["training"]["fast_dev_run"]),
        logger=logger,
        callbacks=[
            StartTrainingCallback(),
            StartValidationCallback(),
            checkpoint_callback,
            early_stopping_callback,
        ],
    )

    # Start Training
    trainer.fit(regression_module, datamodule=datamodule)
    trainer.validate(regression_module, datamodule=datamodule)

    # Save Best Checkpoint Path
    best_model_path = checkpoint_callback.best_model_path
    if not best_model_path:
        best_model_path = "Best checkpoint not available | fast_dev_run or checkpointing disabled"

    best_model_path_file = output_directory / "best_checkpoint_path.txt"
    best_model_path_file.write_text(best_model_path, encoding="utf-8")

    # Save Last Logger Configuration
    if logger.log_dir:
        logger_directory = Path(logger.log_dir)
        if logger_directory.exists():
            shutil.copyfile(best_model_path_file, logger_directory / "best_checkpoint_path.txt")

    print("\nBest Checkpoint:\n")
    print(f"    {best_model_path}")


if __name__ == "__main__":

    train_feedforward_network()
