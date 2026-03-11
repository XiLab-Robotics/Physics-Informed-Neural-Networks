from __future__ import annotations

# Import Python Utilities
import sys, shutil, logging, warnings
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[1]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import PyTorch Lightning Utilities
from lightning.pytorch import Trainer
from lightning.pytorch.callbacks import EarlyStopping
from lightning.pytorch.callbacks import ModelCheckpoint
from lightning.pytorch.callbacks import TQDMProgressBar
from lightning.pytorch.loggers import TensorBoardLogger

# Import PyTorch Utilities
import torch

# Import Terminal Formatting Utilities
try:

    from colorama import Fore
    from colorama import Style
    from colorama import init as colorama_init

except ImportError:

    class _PlainTerminalColor:
        BLACK = ""
        BLUE = ""
        CYAN = ""
        GREEN = ""
        MAGENTA = ""
        RED = ""
        RESET = ""
        WHITE = ""
        YELLOW = ""
        BRIGHT = ""
        NORMAL = ""
        RESET_ALL = ""

    Fore = _PlainTerminalColor()
    Style = _PlainTerminalColor()

    def colorama_init(*args, **kwargs) -> None:

        """ Fallback Colorama Init """

        return None

# Import YAML Utilities
import yaml

# Import Project Models And Training Utilities
from models.model_factory import create_model
from scripts.datasets.transmission_error_dataset import resolve_project_relative_path
from training.transmission_error_datamodule import TransmissionErrorDataModule
from training.transmission_error_regression_module import TransmissionErrorRegressionModule

DEFAULT_CONFIG_PATH = PROJECT_PATH / "config" / "feedforward_network_training.yaml"
SECTION_DIVIDER_WIDTH = 96
KEY_LABEL_WIDTH = 34
PROGRESS_BAR_REFRESH_RATE = 10
LIGHTNING_INFO_LOGGER_NAME_LIST = ["lightning.pytorch.utilities.rank_zero", "lightning.fabric.utilities.rank_zero"]
INPUT_FEATURE_NAME_LIST = ["angular_position_deg", "input_speed_rpm", "input_torque_nm", "oil_temperature_deg", "direction_flag"]
TARGET_FEATURE_NAME_LIST = ["transmission_error_deg"]

# Set Torch Matmul Precision
torch.set_float32_matmul_precision("high")

# Initialize Terminal Colors
colorama_init(autoreset=True)

# Suppress Known Lightning Internal Warning
warnings.filterwarnings("ignore", message=r"`isinstance\(treespec, LeafSpec\)` is deprecated.*", category=FutureWarning, module=r"lightning\.pytorch\.utilities\._pytree")

def format_terminal_value(value: object) -> str:

    """ Format Terminal Value """

    if isinstance(value, float):

        # Format Float With 6 Decimal Places If Not Too Small, Otherwise Use Scientific Notation
        if abs(value) >= 1.0e-4:return f"{value:.6f}"
        return f"{value:.6e}"

    if isinstance(value, Path):
        return str(value)

    if isinstance(value, (list, tuple)):

        # Recursively Format Each Item In The List Or Tuple
        formatted_value_list = [format_terminal_value(item) for item in value]
        return "[" + ", ".join(formatted_value_list) + "]"

    if value is None:
        return "None"

    return str(value)

def print_section_header(section_title: str) -> None:

    """ Print Section Header """

    print()
    print(Fore.CYAN + Style.BRIGHT + "=" * SECTION_DIVIDER_WIDTH)
    print(Fore.CYAN + Style.BRIGHT + section_title)
    print(Fore.CYAN + Style.BRIGHT + "=" * SECTION_DIVIDER_WIDTH)

def print_subsection_header(subsection_title: str) -> None:

    """ Print Subsection Header """

    print()
    print(Fore.MAGENTA + Style.BRIGHT + subsection_title)
    print(Fore.MAGENTA + "-" * len(subsection_title))

def print_key_value(label: str, value: object, value_color: str = Fore.WHITE) -> None:

    """ Print Key Value """

    formatted_label = f"{label:<{KEY_LABEL_WIDTH}}"
    formatted_value = format_terminal_value(value)
    print(f"{Fore.WHITE}{Style.BRIGHT}{formatted_label}{Style.RESET_ALL}{value_color}{formatted_value}{Style.RESET_ALL}")

def print_info_message(message: str) -> None:

    """ Print Info Message """

    print(f"{Fore.BLUE}{Style.BRIGHT}[INFO]{Style.RESET_ALL} {message}")

def print_success_message(message: str) -> None:

    """ Print Success Message """

    print(f"{Fore.GREEN}{Style.BRIGHT}[DONE]{Style.RESET_ALL} {message}")

def print_warning_message(message: str) -> None:

    """ Print Warning Message """

    print(f"{Fore.YELLOW}{Style.BRIGHT}[WARN]{Style.RESET_ALL} {message}")

@contextmanager
def suppress_lightning_info_logs() -> Iterator[None]:

    """ Suppress Lightning Info Logs """

    # Store Current Logger Levels
    logger_state_list: list[tuple[logging.Logger, int]] = []

    # Set Lightning Loggers To Warning Level To Suppress Info Logs
    for logger_name in LIGHTNING_INFO_LOGGER_NAME_LIST:
        lightning_logger = logging.getLogger(logger_name)
        logger_state_list.append((lightning_logger, lightning_logger.level))
        lightning_logger.setLevel(logging.WARNING)

    try:

        yield

    finally:

        # Restore Previous Logger Levels
        for lightning_logger, previous_log_level in logger_state_list:
            lightning_logger.setLevel(previous_log_level)

def print_feature_statistics(feature_name_list: list[str], mean_value_list: list[float], std_value_list: list[float]) -> None:

    """ Print Feature Statistics """

    for feature_name, feature_mean, feature_std in zip(feature_name_list, mean_value_list, std_value_list):

        print_key_value(label=f"{feature_name} | mean", value=feature_mean, value_color=Fore.YELLOW)
        print_key_value(label=f"{feature_name} | std", value=feature_std, value_color=Fore.YELLOW)

def print_training_configuration_summary(training_config: dict) -> None:

    """ Print Training Configuration Summary """

    # Read Config Sections
    path_config         = training_config["paths"]
    experiment_config   = training_config["experiment"]
    dataset_config      = training_config["dataset"]
    model_config        = training_config["model"]
    optimization_config = training_config["training"]

    # Print Config Overview
    print_section_header("Feedforward Training Configuration")
    print_info_message("Resolved YAML configuration for the current training run")

    # Print Path Configuration
    print_subsection_header("Paths")
    print_key_value("Dataset Config Path", path_config["dataset_config_path"], value_color=Fore.YELLOW)
    print_key_value("Output Root", path_config["output_root"], value_color=Fore.YELLOW)

    # Print Experiment Configuration
    print_subsection_header("Experiment")
    print_key_value("Run Name", experiment_config["run_name"], value_color=Fore.YELLOW)
    print_key_value("Model Type", experiment_config["model_type"], value_color=Fore.YELLOW)

    # Print Dataset Configuration
    print_subsection_header("Dataset")
    print_key_value("Curve Batch Size", dataset_config["curve_batch_size"], value_color=Fore.YELLOW)
    print_key_value("Point Stride", dataset_config["point_stride"], value_color=Fore.YELLOW)
    print_key_value("Maximum Points Per Curve", dataset_config["maximum_points_per_curve"], value_color=Fore.YELLOW)
    print_key_value("Num Workers", dataset_config["num_workers"], value_color=Fore.YELLOW)
    print_key_value("Pin Memory", dataset_config["pin_memory"], value_color=Fore.YELLOW)

    # Print Model Configuration
    print_subsection_header("Model")
    print_key_value("Input Size", model_config["input_size"], value_color=Fore.YELLOW)
    print_key_value("Hidden Layers", model_config["hidden_size"], value_color=Fore.YELLOW)
    print_key_value("Output Size", model_config["output_size"], value_color=Fore.YELLOW)
    print_key_value("Activation", model_config["activation_name"], value_color=Fore.YELLOW)
    print_key_value("Dropout Probability", model_config["dropout_probability"], value_color=Fore.YELLOW)
    print_key_value("Use Layer Norm", model_config["use_layer_norm"], value_color=Fore.YELLOW)

    # Print Optimization Configuration
    print_subsection_header("Optimization")
    print_key_value("Learning Rate", optimization_config["learning_rate"], value_color=Fore.YELLOW)
    print_key_value("Weight Decay", optimization_config["weight_decay"], value_color=Fore.YELLOW)
    print_key_value("Min Epochs", optimization_config["min_epochs"], value_color=Fore.YELLOW)
    print_key_value("Max Epochs", optimization_config["max_epochs"], value_color=Fore.YELLOW)
    print_key_value("Patience", optimization_config["patience"], value_color=Fore.YELLOW)
    print_key_value("Min Delta", optimization_config["min_delta"], value_color=Fore.YELLOW)
    print_key_value("Log Every N Steps", optimization_config["log_every_n_steps"], value_color=Fore.YELLOW)
    print_key_value("Fast Dev Run", optimization_config["fast_dev_run"], value_color=Fore.YELLOW)
    print_key_value("Deterministic", optimization_config["deterministic"], value_color=Fore.YELLOW)

def print_dataset_summary(datamodule: TransmissionErrorDataModule, input_feature_dim: int, target_feature_dim: int) -> None:

    """ Print Dataset Summary """

    dataset_split_summary = datamodule.get_dataset_split_summary()

    print_section_header("Dataset Summary")
    print_key_value("Input Feature Dim", input_feature_dim, value_color=Fore.YELLOW)
    print_key_value("Target Feature Dim", target_feature_dim, value_color=Fore.YELLOW)
    print_key_value("Train Curves", dataset_split_summary.train_curve_count, value_color=Fore.YELLOW)
    print_key_value("Validation Curves", dataset_split_summary.validation_curve_count, value_color=Fore.YELLOW)
    print_key_value("Test Curves", dataset_split_summary.test_curve_count, value_color=Fore.YELLOW)
    print_key_value("Point Stride", datamodule.point_stride, value_color=Fore.YELLOW)
    print_key_value("Maximum Points Per Curve", datamodule.maximum_points_per_curve, value_color=Fore.YELLOW)
    print_key_value("Persistent Workers", datamodule.num_workers > 0, value_color=Fore.YELLOW)

def print_model_summary(regression_backbone: torch.nn.Module) -> None:

    """ Print Model Summary """

    # Compute Parameter Counts
    trainable_parameter_count = sum(parameter.numel() for parameter in regression_backbone.parameters() if parameter.requires_grad)
    total_parameter_count = sum(parameter.numel() for parameter in regression_backbone.parameters())
    frozen_parameter_count = total_parameter_count - trainable_parameter_count

    # Print Compact Model Summary
    print_section_header("Model Summary")
    print_key_value("Backbone", regression_backbone.__class__.__name__, value_color=Fore.YELLOW)
    print_key_value("Trainable Parameters", trainable_parameter_count, value_color=Fore.YELLOW)
    print_key_value("Frozen Parameters", frozen_parameter_count, value_color=Fore.YELLOW)
    print_key_value("Total Parameters", total_parameter_count, value_color=Fore.YELLOW)

def print_normalization_statistics_summary(normalization_statistics) -> None:

    """ Print Normalization Statistics Summary """

    print_section_header("Normalization Statistics")

    # Print Input Normalization Statistics
    print_subsection_header("Input Features")
    print_feature_statistics(
        feature_name_list=INPUT_FEATURE_NAME_LIST,
        mean_value_list=normalization_statistics.input_feature_mean.tolist(),
        std_value_list=normalization_statistics.input_feature_std.tolist(),
    )

    # Print Target Normalization Statistics
    print_subsection_header("Target")
    print_feature_statistics(
        feature_name_list=TARGET_FEATURE_NAME_LIST,
        mean_value_list=normalization_statistics.target_mean.tolist(),
        std_value_list=normalization_statistics.target_std.tolist(),
    )

def print_runtime_summary() -> None:

    """ Print Runtime Summary """

    print_section_header("Runtime Summary")
    print_key_value("CUDA Available", torch.cuda.is_available(), value_color=Fore.YELLOW)
    print_key_value("CUDA Device Count", torch.cuda.device_count(), value_color=Fore.YELLOW)

    if torch.cuda.is_available(): print_key_value("CUDA Device Name", torch.cuda.get_device_name(0), value_color=Fore.YELLOW)
    else: print_warning_message("CUDA is not available -> training will run on CPU")

def print_output_artifact_summary(output_directory: Path, logger: TensorBoardLogger, best_model_path: str) -> None:

    """ Print Output Artifact Summary """

    print_section_header("Output Artifacts")
    print_key_value("Output Directory", output_directory, value_color=Fore.YELLOW)
    print_key_value("Checkpoint Directory", output_directory / "checkpoints", value_color=Fore.YELLOW)
    print_key_value("Config Snapshot", output_directory / "feedforward_network_training.yaml", value_color=Fore.YELLOW)
    print_key_value("Metrics Snapshot", output_directory / "training_test_metrics.yaml", value_color=Fore.YELLOW)
    print_key_value("Run Report", output_directory / "training_test_report.md", value_color=Fore.YELLOW)

    if logger.log_dir: print_key_value("TensorBoard Log Directory", logger.log_dir, value_color=Fore.YELLOW)
    print_key_value("Best Checkpoint", best_model_path, value_color=Fore.YELLOW)

def serialize_metric_dictionary(metric_dictionary: dict[str, object]) -> dict[str, object]:

    """ Serialize Metric Dictionary """

    serialized_metric_dictionary: dict[str, object] = {}

    for metric_name, metric_value in metric_dictionary.items():

        if isinstance(metric_value, torch.Tensor):
            serialized_metric_dictionary[metric_name] = float(metric_value.detach().cpu().item())
            continue

        if isinstance(metric_value, float):
            serialized_metric_dictionary[metric_name] = float(metric_value)
            continue

        if isinstance(metric_value, int):
            serialized_metric_dictionary[metric_name] = int(metric_value)
            continue

        serialized_metric_dictionary[metric_name] = str(metric_value)

    return serialized_metric_dictionary

def save_metrics_snapshot(
    output_directory: Path,
    training_config: dict,
    datamodule: TransmissionErrorDataModule,
    best_model_path: str,
    validation_metric_list: list[dict[str, object]],
    test_metric_list: list[dict[str, object]],
) -> dict[str, object]:

    """ Save Metrics Snapshot """

    dataset_split_summary = datamodule.get_dataset_split_summary()
    normalization_statistics = datamodule.get_normalization_statistics()

    validation_metric_dictionary = serialize_metric_dictionary(validation_metric_list[0] if len(validation_metric_list) > 0 else {})
    test_metric_dictionary = serialize_metric_dictionary(test_metric_list[0] if len(test_metric_list) > 0 else {})

    metrics_snapshot_dictionary: dict[str, object] = {
        "run_name": training_config["experiment"]["run_name"],
        "best_checkpoint_path": best_model_path,
        "dataset_split": {
            "train_curves": dataset_split_summary.train_curve_count,
            "validation_curves": dataset_split_summary.validation_curve_count,
            "test_curves": dataset_split_summary.test_curve_count,
        },
        "normalization_statistics": {
            "input_feature_mean": [float(value) for value in normalization_statistics.input_feature_mean.tolist()],
            "input_feature_std": [float(value) for value in normalization_statistics.input_feature_std.tolist()],
            "target_mean": [float(value) for value in normalization_statistics.target_mean.tolist()],
            "target_std": [float(value) for value in normalization_statistics.target_std.tolist()],
        },
        "validation_metrics": validation_metric_dictionary,
        "test_metrics": test_metric_dictionary,
    }

    metrics_snapshot_path = output_directory / "training_test_metrics.yaml"
    with metrics_snapshot_path.open("w", encoding="utf-8") as metrics_file:
        yaml.safe_dump(metrics_snapshot_dictionary, metrics_file, sort_keys=False)

    return metrics_snapshot_dictionary

def build_metric_interpretation(metric_dictionary: dict[str, object], metric_prefix: str) -> str:

    """ Build Metric Interpretation """

    metric_mae = metric_dictionary.get(f"{metric_prefix}_mae")
    metric_rmse = metric_dictionary.get(f"{metric_prefix}_rmse")

    if isinstance(metric_mae, (int, float)) and isinstance(metric_rmse, (int, float)):
        return (
            f"The held-out {metric_prefix} error stayed finite with MAE={metric_mae:.6f} deg and "
            f"RMSE={metric_rmse:.6f} deg, which indicates a numerically stable baseline run."
        )

    return f"The held-out {metric_prefix} metrics were not fully available in serialized form, so only raw metric files should be trusted."

def save_training_test_report(
    output_directory: Path,
    training_config: dict,
    metrics_snapshot_dictionary: dict[str, object],
) -> None:

    """ Save Training Test Report """

    dataset_split_dictionary = metrics_snapshot_dictionary["dataset_split"]
    validation_metric_dictionary = metrics_snapshot_dictionary["validation_metrics"]
    test_metric_dictionary = metrics_snapshot_dictionary["test_metrics"]

    report_line_list = [
        "# Feedforward Training And Testing Report",
        "",
        "## Overview",
        "",
        f"- Run Name: `{training_config['experiment']['run_name']}`",
        f"- Model Type: `{training_config['experiment']['model_type']}`",
        f"- Best Checkpoint: `{metrics_snapshot_dictionary['best_checkpoint_path']}`",
        "",
        "## Dataset Split",
        "",
        f"- Train Curves: `{dataset_split_dictionary['train_curves']}`",
        f"- Validation Curves: `{dataset_split_dictionary['validation_curves']}`",
        f"- Test Curves: `{dataset_split_dictionary['test_curves']}`",
        "",
        "## Validation Metrics",
        "",
    ]

    for metric_name, metric_value in validation_metric_dictionary.items():
        report_line_list.append(f"- {metric_name}: `{format_terminal_value(metric_value)}`")

    report_line_list.extend([
        "",
        "## Test Metrics",
        "",
    ])

    for metric_name, metric_value in test_metric_dictionary.items():
        report_line_list.append(f"- {metric_name}: `{format_terminal_value(metric_value)}`")

    report_line_list.extend([
        "",
        "## Interpretation",
        "",
        build_metric_interpretation(validation_metric_dictionary, "val"),
        build_metric_interpretation(test_metric_dictionary, "test"),
    ])

    report_path = output_directory / "training_test_report.md"
    report_path.write_text("\n".join(report_line_list) + "\n", encoding="utf-8")

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
    assert configured_input_size == input_feature_dim, (f"Configured Input Size and Dataset Input Feature Dim mismatch | {configured_input_size} vs {input_feature_dim}")

    # Create Regression Backbone Model
    regression_backbone = create_model(
        model_type=str(training_config["experiment"]["model_type"]),
        model_configuration=training_config["model"],
    )

    # Create Regression Lightning Module
    regression_module = TransmissionErrorRegressionModule(
        regression_model=regression_backbone,
        input_feature_dim=input_feature_dim,
        target_feature_dim=target_feature_dim,
        learning_rate=float(training_config["training"]["learning_rate"]),
        weight_decay=float(training_config["training"]["weight_decay"]),
        normalization_statistics=normalization_statistics,
    )

    # Print Training Summary
    print_training_configuration_summary(training_config=training_config)
    print_dataset_summary(datamodule=datamodule, input_feature_dim=input_feature_dim, target_feature_dim=target_feature_dim)
    print_model_summary(regression_backbone=regression_backbone)
    print_normalization_statistics_summary(normalization_statistics=normalization_statistics)
    print_runtime_summary()

    # Create Logger
    logger = TensorBoardLogger(save_dir=str(output_directory / "logs"), name="", version="")

    # Checkpoint Callback To Save Best Model Based On Validation MAE, As Well As The Last Model For Resuming Training If Needed
    checkpoint_callback = ModelCheckpoint(
        dirpath=str(output_directory / "checkpoints"),
        filename="feedforward-{epoch:03d}-{val_mae:.8f}",
        monitor="val_mae",
        mode="min",
        save_top_k=1,
        save_last=True,
    )

    # Early Stopping Callback To Stop Training If Validation MAE Does Not Improve For A Certain Number Of Epochs
    early_stopping_callback = EarlyStopping(
        monitor="val_mae",
        mode="min",
        patience=int(training_config["training"]["patience"]),
        min_delta=float(training_config["training"]["min_delta"]),
        verbose=True,
    )

    # Progress Bar Callback To Display Training Progress
    progress_bar_callback = TQDMProgressBar(
        refresh_rate=PROGRESS_BAR_REFRESH_RATE,
        leave=True,
    )

    # Create Trainer - Suppress Lightning Internal Info Logs To Reduce Terminal Clutter During Training
    with suppress_lightning_info_logs():

        trainer = Trainer(
            accelerator="auto",
            devices="auto",
            min_epochs=int(training_config["training"]["min_epochs"]),
            max_epochs=int(training_config["training"]["max_epochs"]),
            log_every_n_steps=int(training_config["training"]["log_every_n_steps"]),
            deterministic=bool(training_config["training"]["deterministic"]),
            fast_dev_run=bool(training_config["training"]["fast_dev_run"]),
            enable_model_summary=False,
            enable_progress_bar=True,
            logger=logger,
            callbacks=[
                checkpoint_callback,
                early_stopping_callback,
                progress_bar_callback,
            ],
        )

    # Start Training
    print_section_header("Training Loop")
    print_info_message("Starting Lightning fit loop")
    trainer.fit(regression_module, datamodule=datamodule)
    print_success_message("Training loop completed")

    # Start Validation
    print_section_header("Validation Loop")
    print_info_message("Starting final Lightning validation loop")
    validation_metric_list = trainer.validate(regression_module, datamodule=datamodule)
    print_success_message("Validation loop completed")

    # Save Best Checkpoint Path
    best_model_path = checkpoint_callback.best_model_path
    if not best_model_path: best_model_path = "Best checkpoint not available | fast_dev_run or checkpointing disabled"

    # Load Best Checkpoint For Final Held-Out Evaluation
    best_regression_module = regression_module
    if Path(best_model_path).exists():

        print_section_header("Best Checkpoint Evaluation")
        print_info_message("Loading best checkpoint for reproducible validation and test evaluation")
        best_regression_module = TransmissionErrorRegressionModule.load_from_checkpoint(
            checkpoint_path=best_model_path,
            regression_model=create_model(
                model_type=str(training_config["experiment"]["model_type"]),
                model_configuration=training_config["model"],
            ),
            input_feature_dim=input_feature_dim,
            target_feature_dim=target_feature_dim,
            normalization_statistics=normalization_statistics,
        )
        validation_metric_list = trainer.validate(best_regression_module, datamodule=datamodule)
        print_success_message("Best-checkpoint validation loop completed")

    # Start Testing
    print_section_header("Test Loop")
    print_info_message("Starting held-out Lightning test loop")
    test_metric_list = trainer.test(best_regression_module, datamodule=datamodule)
    print_success_message("Test loop completed")

    # Save Best Checkpoint Path To File For Easy Reference
    best_model_path_file = output_directory / "best_checkpoint_path.txt"
    best_model_path_file.write_text(best_model_path, encoding="utf-8")

    # Save Machine-Readable Metrics And Human-Readable Report
    metrics_snapshot_dictionary = save_metrics_snapshot(
        output_directory=output_directory,
        training_config=training_config,
        datamodule=datamodule,
        best_model_path=best_model_path,
        validation_metric_list=validation_metric_list,
        test_metric_list=test_metric_list,
    )
    save_training_test_report(
        output_directory=output_directory,
        training_config=training_config,
        metrics_snapshot_dictionary=metrics_snapshot_dictionary,
    )

    # Save Last Logger Configuration
    if logger.log_dir:

        logger_directory = Path(logger.log_dir)
        if logger_directory.exists(): shutil.copyfile(best_model_path_file, logger_directory / "best_checkpoint_path.txt")

    print_output_artifact_summary(output_directory=output_directory, logger=logger, best_model_path=best_model_path)
    print_success_message("Feedforward training workflow completed")

if __name__ == "__main__":

    # Train Feedforward Network
    train_feedforward_network()
