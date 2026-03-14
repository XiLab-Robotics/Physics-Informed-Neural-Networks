from __future__ import annotations

# Import Python Utilities
import sys, argparse, yaml
from pathlib import Path

# Define Package And Project Paths
PACKAGE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = PACKAGE_PATH.parents[1]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import Plotting Utilities
import matplotlib
import matplotlib.pyplot as plt

# Use Non-Interactive Backend When The Figure Will Be Written To Disk
if "--save-path" in sys.argv: matplotlib.use("Agg")

# Import Dataset Utilities
from scripts.datasets.transmission_error_dataset import build_validated_directional_samples
from scripts.datasets.transmission_error_dataset import collect_dataset_csv_paths
from scripts.datasets.transmission_error_dataset import load_dataset_processing_config
from scripts.datasets.transmission_error_dataset import resolve_project_relative_path

# Define Default Visualization Config Path
DEFAULT_VISUALIZATION_CONFIG_PATH = PROJECT_PATH / "config" / "visualization" / "transmission_error_visualization.yaml"

def load_visualization_config(config_path: str | Path = DEFAULT_VISUALIZATION_CONFIG_PATH) -> dict:

    """ Load Visualization Config """

    # Resolve Config Path
    resolved_config_path = resolve_project_relative_path(config_path)

    # Validate Config Path
    assert resolved_config_path.exists(), f"Visualization Config Path does not exist | {resolved_config_path}"

    # Load YAML Configuration
    with resolved_config_path.open("r", encoding="utf-8") as config_file:
        visualization_config = yaml.safe_load(config_file)

    # Validate Configuration
    assert isinstance(visualization_config, dict), "Visualization Config must be a dictionary"

    return visualization_config

def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command Line Arguments """

    # Initialize Parser
    argument_parser = argparse.ArgumentParser(description="Visualize processed Transmission Error curves.")

    # Add Configuration Arguments
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_VISUALIZATION_CONFIG_PATH,
        help="Path to the visualization YAML configuration file.",
    )

    argument_parser.add_argument(
        "--csv-path",
        type=Path,
        default=None,
        help="Optional path to a specific CSV file to visualize.",
    )

    argument_parser.add_argument(
        "--file-index",
        type=int,
        default=None,
        help="Dataset CSV index used when --csv-path is not provided.",
    )

    argument_parser.add_argument(
        "--save-path",
        type=Path,
        default=None,
        help="Optional path used to save the plot instead of opening it interactively.",
    )

    return argument_parser.parse_args()

def resolve_csv_file_path(dataset_root: Path, csv_path: Path | None, file_index: int) -> Path:

    """ Resolve CSV File Path """

    # Return Explicit CSV Path
    if csv_path is not None:

        resolved_csv_path = csv_path.resolve()
        assert resolved_csv_path.exists(), f"CSV Path does not exist | {resolved_csv_path}"
        return resolved_csv_path

    # Collect Dataset CSV Paths
    csv_file_paths = collect_dataset_csv_paths(dataset_root=dataset_root)

    # Validate File Index
    assert 0 <= file_index < len(csv_file_paths), f"File Index out of range | {file_index} | Dataset size: {len(csv_file_paths)}"

    return csv_file_paths[file_index]

def visualize_transmission_error_curves(
    csv_file_path: Path,
    save_path: Path | None = None,
    figure_width: float = 12.0,
    figure_height: float = 6.0,
    figure_dpi: int = 200,
) -> None:

    """ Visualize Transmission Error Curves """

    # Load Directional Samples
    directional_sample_list = build_validated_directional_samples(csv_file_path)
    forward_sample = directional_sample_list[0]

    # Initialize Figure
    plt.figure(figsize=(figure_width, figure_height))

    # Plot Directional Curves
    for transmission_error_curve_sample in directional_sample_list:

        # Select Direction-Specific Plot Style
        if transmission_error_curve_sample.direction_label == "forward":

            line_color = "tab:blue"
            line_label = "Forward TE"

        else:

            line_color = "tab:orange"
            line_label = "Backward TE"

        plt.plot(
            transmission_error_curve_sample.angular_position_deg,
            transmission_error_curve_sample.transmission_error_deg,
            color=line_color,
            linewidth=1.0,
            label=line_label,
        )

    # Configure Figure
    plt.title(
        f"Transmission Error | {forward_sample.speed_rpm:.0f} rpm | "
        f"{forward_sample.torque_nm:.0f} Nm | "
        f"{forward_sample.oil_temperature_deg:.0f} degC"
    )
    plt.xlabel("Output Position [deg]")
    plt.ylabel("Transmission Error [deg]")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    # Save Or Show Figure
    if save_path is not None:
        resolved_save_path = save_path.resolve()
        resolved_save_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(resolved_save_path, dpi=figure_dpi)
        print(f"Saved Transmission Error plot | {resolved_save_path}")

    else: plt.show()

    plt.close()

def main() -> None:

    """ Main Function """

    # Parse Command Line Arguments
    command_line_arguments = parse_command_line_arguments()

    # Load Configurations
    visualization_config = load_visualization_config(config_path=command_line_arguments.config_path)
    dataset_processing_config = load_dataset_processing_config(
        config_path=resolve_project_relative_path(visualization_config["paths"]["dataset_config_path"])
    )

    # Resolve Runtime Parameters
    dataset_root = resolve_project_relative_path(dataset_processing_config["paths"]["dataset_root"])
    file_index = (int(command_line_arguments.file_index) if command_line_arguments.file_index is not None else int(visualization_config["selection"]["file_index"]))
    save_path = command_line_arguments.save_path

    if save_path is None:

        # Resolve Save Path From Config
        configured_save_path = visualization_config["output"]["save_path"]
        save_path = None if configured_save_path in ["", None] else Path(configured_save_path)

    # Resolve CSV Path
    csv_file_path = resolve_csv_file_path(
        dataset_root=dataset_root,
        csv_path=command_line_arguments.csv_path,
        file_index=file_index,
    )

    # Visualize Curves
    visualize_transmission_error_curves(
        csv_file_path=csv_file_path,
        save_path=save_path,
        figure_width=float(visualization_config["plot"]["figure_width"]),
        figure_height=float(visualization_config["plot"]["figure_height"]),
        figure_dpi=int(visualization_config["plot"]["figure_dpi"]),
    )

if __name__ == "__main__":

    main()
