"""Export the canonical dataset split manifests for colleague handoff.

This script reproduces the repository-owned dataset split exactly using the
same configuration values, file-level randomization, and seed currently used
by the training pipeline, while staying standalone enough to run without the
full training stack.
"""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import random
import re
import sys
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import yaml

# Ensure direct script execution can resolve the repository package root.
SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

PACKAGE_PATH = PROJECT_ROOT / "scripts" / "datasets"
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config" / "datasets" / "transmission_error_dataset.yaml"

FORWARD_DIRECTION = "forward"
BACKWARD_DIRECTION = "backward"
FORWARD_DIRECTION_FLAG = 1.0
BACKWARD_DIRECTION_FLAG = -1.0

FILENAME_PATTERN = re.compile(
    r"(?P<speed_rpm>[0-9.]+)rpm(?P<torque_nm>[0-9.]+)Nm(?P<temperature_deg>[0-9.]+)deg\.csv$"
)


def resolve_project_relative_path(path_value: str | Path) -> Path:

    """Resolve one path against the repository root."""

    # Convert To Path
    resolved_path = Path(path_value)

    # Preserve Absolute Paths
    if resolved_path.is_absolute():
        return resolved_path.resolve()

    # Resolve Repository-Relative Path
    return (PROJECT_ROOT / resolved_path).resolve()


def load_dataset_processing_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:

    """Load the repository dataset processing YAML configuration."""

    # Resolve Config Path
    resolved_config_path = resolve_project_relative_path(config_path)
    assert resolved_config_path.exists(), f"Dataset Config Path does not exist | {resolved_config_path}"

    # Load YAML Configuration
    with resolved_config_path.open("r", encoding="utf-8") as config_file:
        dataset_processing_config = yaml.safe_load(config_file)

    # Validate Configuration
    assert isinstance(dataset_processing_config, dict), "Dataset Processing Config must be a dictionary"
    return dataset_processing_config


def resolve_dataset_root_from_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> Path:

    """Resolve the dataset root from the canonical dataset config."""

    # Load Configuration
    dataset_processing_config = load_dataset_processing_config(config_path)

    # Resolve Dataset Root
    return resolve_project_relative_path(dataset_processing_config["paths"]["dataset_root"])


def collect_dataset_csv_paths(dataset_root: str | Path) -> list[Path]:

    """Collect and sort all dataset CSV files below the dataset root."""

    # Resolve Dataset Root
    dataset_root_path = Path(dataset_root).resolve()
    assert dataset_root_path.exists(), f"Dataset Root Path does not exist | {dataset_root_path}"

    # Collect CSV Paths
    csv_file_path_list = sorted(dataset_root_path.rglob("*.csv"))
    assert len(csv_file_path_list) > 0, f"No CSV files found inside Dataset Root | {dataset_root_path}"

    return csv_file_path_list


def build_directional_file_manifest(
    dataset_root: str | Path,
    use_forward_direction: bool = True,
    use_backward_direction: bool = True,
) -> list[tuple[Path, str]]:

    """Build the same directional file manifest used by the training pipeline."""

    # Validate Direction Configuration
    assert use_forward_direction or use_backward_direction, "At least one direction must be enabled"

    # Collect CSV Paths
    csv_file_path_list = collect_dataset_csv_paths(dataset_root)

    # Build Manifest
    directional_file_manifest: list[tuple[Path, str]] = []
    for csv_file_path in csv_file_path_list:
        if use_forward_direction:
            directional_file_manifest.append((csv_file_path, FORWARD_DIRECTION))
        if use_backward_direction:
            directional_file_manifest.append((csv_file_path, BACKWARD_DIRECTION))

    return directional_file_manifest


def split_directional_file_manifest(
    directional_file_manifest: list[tuple[Path, str]],
    validation_split: float = 0.2,
    test_split: float = 0.0,
    random_seed: int = 42,
) -> tuple[list[tuple[Path, str]], list[tuple[Path, str]], list[tuple[Path, str]]]:

    """Split the directional manifest with the canonical repository logic."""

    # Validate Split Configuration
    assert 0.0 < validation_split < 1.0, f"Validation Split must be between 0 and 1 | {validation_split}"
    assert 0.0 <= test_split < 1.0, f"Test Split must be between 0 and 1 | {test_split}"
    assert (validation_split + test_split) < 1.0, (
        f"Validation Split + Test Split must stay below 1 | {validation_split} + {test_split}"
    )

    # Collect And Shuffle Unique CSV Paths
    unique_csv_file_path_list = sorted({csv_file_path for csv_file_path, _ in directional_file_manifest})
    assert len(unique_csv_file_path_list) >= 2, "At least two CSV files are required to build train and validation splits"
    random_generator = random.Random(random_seed)
    random_generator.shuffle(unique_csv_file_path_list)

    # Build Split Indices
    validation_file_count = max(1, int(round(len(unique_csv_file_path_list) * validation_split)))
    if validation_file_count >= len(unique_csv_file_path_list):
        validation_file_count = len(unique_csv_file_path_list) - 1
    remaining_file_count_after_validation = len(unique_csv_file_path_list) - validation_file_count

    test_file_count = int(round(len(unique_csv_file_path_list) * test_split))
    if test_split > 0.0:
        test_file_count = max(1, test_file_count)
    if test_file_count >= remaining_file_count_after_validation:
        test_file_count = remaining_file_count_after_validation - 1

    # Resolve Split CSV Sets
    validation_csv_file_path_set = set(unique_csv_file_path_list[:validation_file_count])
    test_csv_file_path_set = set(
        unique_csv_file_path_list[validation_file_count:(validation_file_count + test_file_count)]
    )

    # Split Directional Manifest
    train_directional_file_manifest = [
        (csv_file_path, direction_label)
        for csv_file_path, direction_label in directional_file_manifest
        if csv_file_path not in validation_csv_file_path_set
    ]
    validation_directional_file_manifest = [
        (csv_file_path, direction_label)
        for csv_file_path, direction_label in directional_file_manifest
        if csv_file_path in validation_csv_file_path_set
    ]
    if len(test_csv_file_path_set) > 0:
        train_directional_file_manifest = [
            (csv_file_path, direction_label)
            for csv_file_path, direction_label in train_directional_file_manifest
            if csv_file_path not in test_csv_file_path_set
        ]
    test_directional_file_manifest = [
        (csv_file_path, direction_label)
        for csv_file_path, direction_label in directional_file_manifest
        if csv_file_path in test_csv_file_path_set
    ]

    # Validate Split Results
    assert len(train_directional_file_manifest) > 0, "Train Directional File Manifest is empty"
    assert len(validation_directional_file_manifest) > 0, "Validation Directional File Manifest is empty"
    if test_split > 0.0:
        assert len(test_directional_file_manifest) > 0, "Test Directional File Manifest is empty"

    return (
        train_directional_file_manifest,
        validation_directional_file_manifest,
        test_directional_file_manifest,
    )


def parse_operating_condition_metadata(csv_file_path: str | Path) -> dict[str, float]:

    """Parse speed, torque, and temperature metadata from one dataset path."""

    # Resolve CSV Path
    resolved_csv_file_path = Path(csv_file_path).resolve()

    # Parse File Name Metadata
    filename_match = FILENAME_PATTERN.search(resolved_csv_file_path.name)
    assert filename_match is not None, (
        f"Unable to parse Operating Conditions from file name | {resolved_csv_file_path.name}"
    )

    # Parse Parent Folder Temperature
    parent_folder_match = re.search(
        r"Test_(?P<temperature_deg>[0-9.]+)degree",
        resolved_csv_file_path.as_posix(),
    )
    assert parent_folder_match is not None, (
        f"Unable to parse Test Temperature from folder path | {resolved_csv_file_path}"
    )

    return {
        "speed_rpm": float(filename_match.group("speed_rpm")),
        "torque_nm": float(filename_match.group("torque_nm")),
        "oil_temperature_deg": float(parent_folder_match.group("temperature_deg")),
    }


def parse_cli_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the dataset split export helper."""

    # Build Argument Parser
    argument_parser = argparse.ArgumentParser(
        description=(
            "Export the canonical dataset split using the repository seed and "
            "file-based randomization logic."
        )
    )

    # Add Dataset Configuration Inputs
    argument_parser.add_argument(
        "--config-path",
        type=str,
        default=str(DEFAULT_CONFIG_PATH),
        help="Path to the dataset processing YAML configuration.",
    )
    argument_parser.add_argument(
        "--output-directory",
        type=str,
        required=True,
        help="Directory where the exported split manifests will be written.",
    )

    return argument_parser.parse_args()


def resolve_direction_flag(direction_label: str) -> float:

    """Resolve the numeric direction flag used by the repository dataset logic.

    Args:
        direction_label: Direction string stored inside the directional
            manifest.

    Returns:
        Numeric direction flag aligned with the repository convention.

    Raises:
        AssertionError: If the direction label is not recognized.
    """

    # Resolve Forward Direction
    if direction_label == FORWARD_DIRECTION:
        return FORWARD_DIRECTION_FLAG

    # Resolve Backward Direction
    if direction_label == BACKWARD_DIRECTION:
        return BACKWARD_DIRECTION_FLAG

    # Reject Unknown Labels
    raise AssertionError(f"Unsupported direction label | {direction_label}")


def format_project_relative_path(path_value: str | Path) -> str:

    """Format one path as a project-relative POSIX-like string."""

    # Resolve Absolute Path
    resolved_path = Path(path_value).resolve()

    # Convert To Project-Relative Path
    try:
        relative_path = resolved_path.relative_to(PROJECT_ROOT.resolve())
        return relative_path.as_posix()
    except ValueError:
        return resolved_path.as_posix()


def build_directional_manifest_row(csv_file_path: Path, direction_label: str) -> dict[str, Any]:

    """Build one exported row for the directional split manifest."""

    # Parse Operating Metadata
    operating_condition_metadata = parse_operating_condition_metadata(csv_file_path)

    # Build Export Row
    return {
        "source_file_path": format_project_relative_path(csv_file_path),
        "direction_label": direction_label,
        "direction_flag": resolve_direction_flag(direction_label),
        "speed_rpm": operating_condition_metadata["speed_rpm"],
        "torque_nm": operating_condition_metadata["torque_nm"],
        "oil_temperature_deg": operating_condition_metadata["oil_temperature_deg"],
    }


def build_unique_file_manifest_rows(directional_file_manifest: list[tuple[Path, str]]) -> list[dict[str, Any]]:

    """Build the unique-file export rows for one split.

    Args:
        directional_file_manifest: Split subset including direction labels.

    Returns:
        Sorted export rows with one entry per unique CSV file.
    """

    # Collect Unique CSV Paths
    unique_csv_file_paths = sorted({csv_file_path.resolve() for csv_file_path, _ in directional_file_manifest})

    # Build Export Rows
    unique_file_manifest_rows: list[dict[str, Any]] = []
    for csv_file_path in unique_csv_file_paths:

        # Parse Operating Metadata
        operating_condition_metadata = parse_operating_condition_metadata(csv_file_path)

        # Append Export Row
        unique_file_manifest_rows.append(
            {
                "source_file_path": format_project_relative_path(csv_file_path),
                "speed_rpm": operating_condition_metadata["speed_rpm"],
                "torque_nm": operating_condition_metadata["torque_nm"],
                "oil_temperature_deg": operating_condition_metadata["oil_temperature_deg"],
            }
        )

    return unique_file_manifest_rows


def write_csv_manifest(output_path: Path, row_dictionary_list: list[dict[str, Any]]) -> None:

    """Write one CSV manifest from a list of row dictionaries."""

    # Resolve Empty Export Case
    assert len(row_dictionary_list) > 0, f"Refusing to write empty manifest | {output_path}"

    # Create Parent Directory
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write CSV Rows
    field_name_list = list(row_dictionary_list[0].keys())
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=field_name_list)
        csv_writer.writeheader()
        csv_writer.writerows(row_dictionary_list)


def write_yaml_summary(output_path: Path, summary_dictionary: dict[str, Any]) -> None:

    """Write the dataset split summary YAML."""

    # Create Parent Directory
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write YAML Summary
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(summary_dictionary, output_file, sort_keys=False, allow_unicode=False)


def build_split_summary_dictionary(
    config_path: Path,
    dataset_root: Path,
    dataset_processing_config: dict[str, Any],
    train_manifest: list[tuple[Path, str]],
    validation_manifest: list[tuple[Path, str]],
    test_manifest: list[tuple[Path, str]],
) -> dict[str, Any]:

    """Build the colleague-facing summary for the exported dataset split."""

    # Resolve Split Configuration
    split_configuration = dataset_processing_config["split"]

    # Count Unique Files
    train_unique_file_count = len({csv_file_path.resolve() for csv_file_path, _ in train_manifest})
    validation_unique_file_count = len({csv_file_path.resolve() for csv_file_path, _ in validation_manifest})
    test_unique_file_count = len({csv_file_path.resolve() for csv_file_path, _ in test_manifest})
    total_unique_file_count = train_unique_file_count + validation_unique_file_count + test_unique_file_count

    # Count Directional Entries
    train_directional_entry_count = len(train_manifest)
    validation_directional_entry_count = len(validation_manifest)
    test_directional_entry_count = len(test_manifest)
    total_directional_entry_count = (
        train_directional_entry_count
        + validation_directional_entry_count
        + test_directional_entry_count
    )

    # Build Summary Dictionary
    return {
        "schema_version": 1,
        "export_name": "dataset_split_export",
        "project_root": str(PROJECT_ROOT.resolve()),
        "dataset_root": str(dataset_root.resolve()),
        "dataset_root_relative": format_project_relative_path(dataset_root),
        "dataset_config_path": format_project_relative_path(config_path),
        "split_strategy": {
            "scope": "unique_csv_file_paths",
            "randomization": "python_random_shuffle",
            "random_seed": int(split_configuration["random_seed"]),
            "validation_split": float(split_configuration["validation_split"]),
            "test_split": float(split_configuration["test_split"]),
            "implied_train_split": 1.0 - float(split_configuration["validation_split"]) - float(split_configuration["test_split"]),
            "assignment_order": ["validation", "test", "train_remaining"],
        },
        "direction_configuration": {
            "use_forward_direction": bool(dataset_processing_config["directions"]["use_forward_direction"]),
            "use_backward_direction": bool(dataset_processing_config["directions"]["use_backward_direction"]),
        },
        "counts": {
            "unique_csv_files": {
                "train": train_unique_file_count,
                "validation": validation_unique_file_count,
                "test": test_unique_file_count,
                "total": total_unique_file_count,
            },
            "directional_entries": {
                "train": train_directional_entry_count,
                "validation": validation_directional_entry_count,
                "test": test_directional_entry_count,
                "total": total_directional_entry_count,
            },
        },
    }


def export_split_manifests(
    output_directory: Path,
    train_manifest: list[tuple[Path, str]],
    validation_manifest: list[tuple[Path, str]],
    test_manifest: list[tuple[Path, str]],
) -> None:

    """Export the directional and unique-file manifests for every split."""

    # Define Split Registry
    split_registry = {
        "train": train_manifest,
        "validation": validation_manifest,
        "test": test_manifest,
    }

    # Export Per-Split Files
    for split_name, directional_manifest in split_registry.items():

        # Build Directional Rows
        directional_row_dictionary_list = [
            build_directional_manifest_row(csv_file_path, direction_label)
            for csv_file_path, direction_label in directional_manifest
        ]

        # Build Unique-File Rows
        unique_file_row_dictionary_list = build_unique_file_manifest_rows(directional_manifest)

        # Write Directional CSV
        write_csv_manifest(
            output_directory / f"{split_name}_directional_manifest.csv",
            directional_row_dictionary_list,
        )

        # Write Unique-File CSV
        write_csv_manifest(
            output_directory / f"{split_name}_unique_files.csv",
            unique_file_row_dictionary_list,
        )


def main() -> None:

    """Export the canonical dataset split manifests using the repository config."""

    # Parse CLI Arguments
    cli_arguments = parse_cli_arguments()

    # Resolve Paths
    config_path = Path(cli_arguments.config_path).resolve()
    output_directory = Path(cli_arguments.output_directory).resolve()

    # Load Dataset Configuration
    dataset_processing_config = load_dataset_processing_config(config_path)
    dataset_root = resolve_dataset_root_from_config(config_path)

    # Build Canonical Directional Manifest
    directional_file_manifest = build_directional_file_manifest(
        dataset_root=dataset_root,
        use_forward_direction=bool(dataset_processing_config["directions"]["use_forward_direction"]),
        use_backward_direction=bool(dataset_processing_config["directions"]["use_backward_direction"]),
    )

    # Reproduce Canonical Dataset Split
    train_manifest, validation_manifest, test_manifest = split_directional_file_manifest(
        directional_file_manifest=directional_file_manifest,
        validation_split=float(dataset_processing_config["split"]["validation_split"]),
        test_split=float(dataset_processing_config["split"]["test_split"]),
        random_seed=int(dataset_processing_config["split"]["random_seed"]),
    )

    # Export CSV Manifests
    export_split_manifests(
        output_directory=output_directory,
        train_manifest=train_manifest,
        validation_manifest=validation_manifest,
        test_manifest=test_manifest,
    )

    # Export YAML Summary
    split_summary_dictionary = build_split_summary_dictionary(
        config_path=config_path,
        dataset_root=dataset_root,
        dataset_processing_config=dataset_processing_config,
        train_manifest=train_manifest,
        validation_manifest=validation_manifest,
        test_manifest=test_manifest,
    )
    write_yaml_summary(output_directory / "dataset_split_summary.yaml", split_summary_dictionary)

    # Emit Final Status
    print(f"[DONE] Dataset split exported | {output_directory}")


if __name__ == "__main__":
    main()
