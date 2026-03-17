from __future__ import annotations

# Import Python Utilities
import sys, shutil, logging, warnings, argparse
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]

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

# Import Project Models And Training Utilities
from scripts.models.model_factory import create_model
from scripts.training import shared_training_infrastructure
from scripts.training.transmission_error_datamodule import TransmissionErrorDataModule
from scripts.training.transmission_error_regression_module import TransmissionErrorRegressionModule

DEFAULT_CONFIG_PATH = shared_training_infrastructure.DEFAULT_CONFIG_PATH
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
    runtime_config      = resolve_runtime_config(training_config)

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
    print_key_value("Model Family", experiment_config.get("model_family", experiment_config["model_type"]), value_color=Fore.YELLOW)
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

    # Print Runtime Configuration
    print_subsection_header("Runtime")
    print_key_value("Accelerator", runtime_config["accelerator"], value_color=Fore.YELLOW)
    print_key_value("Devices", runtime_config["devices"], value_color=Fore.YELLOW)
    print_key_value("Precision", runtime_config["precision"], value_color=Fore.YELLOW)
    print_key_value("Benchmark", runtime_config["benchmark"], value_color=Fore.YELLOW)
    print_key_value("Non-Blocking Transfer", runtime_config["use_non_blocking_transfer"], value_color=Fore.YELLOW)

def print_dataset_summary(datamodule: TransmissionErrorDataModule, input_feature_dim: int, target_feature_dim: int) -> None:

    """ Print Dataset Summary """

    # Get Dataset Split Summary From The DataModule
    dataset_split_summary = datamodule.get_dataset_split_summary()

    # Print Dataset Summary Statistics
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

def print_runtime_summary(runtime_config: dict[str, object]) -> None:

    """ Print Runtime Summary """

    # Print Runtime Configuration Summary
    print_section_header("Runtime Summary")
    print_key_value("Configured Accelerator", runtime_config["accelerator"], value_color=Fore.YELLOW)
    print_key_value("Configured Devices", runtime_config["devices"], value_color=Fore.YELLOW)
    print_key_value("Configured Precision", runtime_config["precision"], value_color=Fore.YELLOW)
    print_key_value("cuDNN Benchmark", runtime_config["benchmark"], value_color=Fore.YELLOW)
    print_key_value("Non-Blocking Transfer", runtime_config["use_non_blocking_transfer"], value_color=Fore.YELLOW)
    print_key_value("CUDA Available", torch.cuda.is_available(), value_color=Fore.YELLOW)
    print_key_value("CUDA Device Count", torch.cuda.device_count(), value_color=Fore.YELLOW)

    # Print CUDA Device Name If Available, Otherwise Print Warning About CPU Training
    if torch.cuda.is_available(): print_key_value("CUDA Device Name", torch.cuda.get_device_name(0), value_color=Fore.YELLOW)
    else: print_warning_message("CUDA is not available -> training will run on CPU")

def print_output_artifact_summary(output_directory: Path, logger: TensorBoardLogger, best_model_path: str) -> None:

    """ Print Output Artifact Summary """

    # Print Output Artifact Summary
    print_section_header("Output Artifacts")
    print_key_value("Output Directory", output_directory, value_color=Fore.YELLOW)
    print_key_value("Checkpoint Directory", output_directory / "checkpoints", value_color=Fore.YELLOW)
    print_key_value("Config Snapshot", output_directory / shared_training_infrastructure.COMMON_TRAINING_CONFIG_FILENAME, value_color=Fore.YELLOW)
    print_key_value("Metrics Snapshot", output_directory / shared_training_infrastructure.COMMON_METRICS_FILENAME, value_color=Fore.YELLOW)
    print_key_value("Run Metadata", output_directory / shared_training_infrastructure.COMMON_RUN_METADATA_FILENAME, value_color=Fore.YELLOW)
    print_key_value("Run Report", output_directory / shared_training_infrastructure.COMMON_RUN_REPORT_FILENAME, value_color=Fore.YELLOW)
    print_key_value(
        "Family Best Registry",
        shared_training_infrastructure.build_family_registry_directory(output_directory.parent.name) / shared_training_infrastructure.FAMILY_BEST_FILENAME,
        value_color=Fore.YELLOW,
    )
    print_key_value(
        "Program Best Registry",
        shared_training_infrastructure.PROGRAM_REGISTRY_OUTPUT_ROOT / shared_training_infrastructure.PROGRAM_BEST_FILENAME,
        value_color=Fore.YELLOW,
    )

    # Print Logger Artifact Summary
    if logger.log_dir: print_key_value("TensorBoard Log Directory", logger.log_dir, value_color=Fore.YELLOW)
    print_key_value("Best Checkpoint", best_model_path, value_color=Fore.YELLOW)

def build_metric_interpretation(metric_dictionary: dict[str, object], metric_prefix: str) -> str:

    """ Build Metric Interpretation """

    # Extract MAE And RMSE Values From The Metric Dictionary For The Given Prefix
    metric_mae = metric_dictionary.get(f"{metric_prefix}_mae")
    metric_rmse = metric_dictionary.get(f"{metric_prefix}_rmse")

    # Interpret The Metrics Based On Their Values
    if isinstance(metric_mae, (int, float)) and isinstance(metric_rmse, (int, float)):
        return (
            f"The held-out {metric_prefix} error stayed finite with MAE={metric_mae:.6f} deg and "
            f"RMSE={metric_rmse:.6f} deg, which indicates a numerically stable baseline run."
        )

    return f"The held-out {metric_prefix} metrics were not fully available in serialized form, so only raw metric files should be trusted."

def save_training_test_report(output_directory: Path, training_config: dict, metrics_snapshot_dictionary: dict[str, object]) -> None:

    """ Save Training Test Report """

    # Extract Relevant Information From The Metrics Snapshot Dictionary To Build The Report
    experiment_dictionary = metrics_snapshot_dictionary["experiment"]
    dataset_split_dictionary = metrics_snapshot_dictionary["dataset_split"]
    validation_metric_dictionary = metrics_snapshot_dictionary["validation_metrics"]
    test_metric_dictionary = metrics_snapshot_dictionary["test_metrics"]

    # Build The Report As A List Of Lines To Be Joined With Newlines For Output
    report_line_list = [
        "# Feedforward Training And Testing Report",
        "",
        "## Overview",
        "",
        f"- Run Name: `{experiment_dictionary['run_name']}`",
        f"- Model Family: `{experiment_dictionary['model_family']}`",
        f"- Model Type: `{experiment_dictionary['model_type']}`",
        f"- Best Checkpoint: `{metrics_snapshot_dictionary['artifacts']['best_checkpoint_path']}`",
        "",
        "## Dataset Split",
        "",
        f"- Train Curves: `{dataset_split_dictionary['train_curve_count']}`",
        f"- Validation Curves: `{dataset_split_dictionary['validation_curve_count']}`",
        f"- Test Curves: `{dataset_split_dictionary['test_curve_count']}`",
        "",
        "## Validation Metrics",
        "",
    ]

    # Add Each Validation Metric To The Report
    for metric_name, metric_value in validation_metric_dictionary.items():
        report_line_list.append(f"- {metric_name}: `{format_terminal_value(metric_value)}`")

    # Add Each Test Metric To The Report
    report_line_list.extend([
        "",
        "## Test Metrics",
        "",
    ])

    # Add Each Test Metric To The Report
    for metric_name, metric_value in test_metric_dictionary.items():
        report_line_list.append(f"- {metric_name}: `{format_terminal_value(metric_value)}`")

    # Add Interpretation Of The Metrics To The Report
    report_line_list.extend([
        "",
        "## Interpretation",
        "",
        build_metric_interpretation(validation_metric_dictionary, "val"),
        build_metric_interpretation(test_metric_dictionary, "test"),
    ])

    # Save The Report To The Output Directory As A Markdown File
    report_path = output_directory / shared_training_infrastructure.COMMON_RUN_REPORT_FILENAME
    report_path.write_text("\n".join(report_line_list) + "\n", encoding="utf-8")

def load_training_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict:

    """ Load Training Config """

    # Resolve Config Path
    return shared_training_infrastructure.load_training_config(config_path)

def resolve_runtime_config(training_config: dict) -> dict[str, object]:

    """ Resolve Runtime Config """

    # Initialize Default Runtime Configuration
    runtime_config = shared_training_infrastructure.resolve_runtime_config(training_config)

    # Disable Benchmark In Deterministic Mode
    if bool(training_config["training"]["deterministic"]) and bool(runtime_config["benchmark"]):

        print_warning_message("Deterministic mode is enabled -> disabling cuDNN benchmark to avoid conflicting runtime behavior")
        runtime_config["benchmark"] = False

    # Warn If Non-Blocking Transfer Has Limited Value
    if bool(runtime_config["use_non_blocking_transfer"]) and not bool(training_config["dataset"]["pin_memory"]):
        print_warning_message("Non-blocking transfer is enabled but pin_memory is disabled -> host-to-device copy overlap may be limited")

    return runtime_config

def train_feedforward_network(config_path: str | Path = DEFAULT_CONFIG_PATH) -> None:

    """ Train Feedforward Network """

    # Load Training Configuration
    training_config = shared_training_infrastructure.prepare_output_artifact_training_config(load_training_config(config_path))
    runtime_config = resolve_runtime_config(training_config)

    # Resolve Output Directory
    output_directory = shared_training_infrastructure.resolve_output_directory(training_config)
    output_directory.mkdir(parents=True, exist_ok=True)

    # Save Configuration Snapshot
    shared_training_infrastructure.save_training_config_snapshot(training_config, output_directory)
    shared_training_infrastructure.save_run_metadata_snapshot(training_config, output_directory)

    # Initialize Shared Training Components
    datamodule, regression_backbone, regression_module, normalization_statistics = shared_training_infrastructure.initialize_training_components(training_config)
    input_feature_dim = datamodule.get_input_feature_dim()
    target_feature_dim = datamodule.get_target_feature_dim()
    parameter_summary = shared_training_infrastructure.summarize_model_parameters(regression_backbone)

    # Print Training Summary
    print_training_configuration_summary(training_config)
    print_dataset_summary(datamodule, input_feature_dim, target_feature_dim)
    print_model_summary(regression_backbone)
    print_normalization_statistics_summary(normalization_statistics)
    print_runtime_summary(runtime_config)

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
            accelerator=runtime_config["accelerator"],
            devices=runtime_config["devices"],
            precision=runtime_config["precision"],
            benchmark=bool(runtime_config["benchmark"]),
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

        # Load The Best Checkpoint For Reproducible Validation And Test Evaluation
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
    metrics_snapshot_dictionary = shared_training_infrastructure.build_common_metrics_snapshot(
        training_config,
        config_path,
        output_directory,
        datamodule,
        parameter_summary,
        runtime_config,
        best_model_path,
        validation_metric_list,
        test_metric_list,
    )

    # Save Metrics Snapshot
    shared_training_infrastructure.save_common_metrics_snapshot(
        metrics_snapshot_dictionary,
        output_directory,
    )

    # Save Training/Test Report
    save_training_test_report(
        output_directory,
        training_config,
        metrics_snapshot_dictionary,
    )

    # Update Best-Result Registries
    family_best_entry = shared_training_infrastructure.update_family_registry(metrics_snapshot_dictionary)
    shared_training_infrastructure.update_program_registry(family_best_entry)

    # Save Last Logger Configuration
    if logger.log_dir:

        logger_directory = Path(logger.log_dir)
        if logger_directory.exists(): shutil.copyfile(best_model_path_file, logger_directory / "best_checkpoint_path.txt")

    # Print Output Artifact Summary
    print_output_artifact_summary(output_directory, logger, best_model_path)
    print_success_message("Feedforward training workflow completed")

def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command Line Arguments """

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(description="Train the feedforward Transmission Error baseline.")

    # Add Config Path Argument
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the YAML training configuration file.",
    )

    return argument_parser.parse_args()

def main() -> None:

    """ Main Function """

    # Parse Command Line Arguments
    command_line_arguments = parse_command_line_arguments()

    # Train Feedforward Network
    train_feedforward_network(command_line_arguments.config_path)

if __name__ == "__main__":

    main()
