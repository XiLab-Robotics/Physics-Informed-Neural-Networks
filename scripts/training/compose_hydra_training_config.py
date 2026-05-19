"""Compose Hydra Training Configs Without Launching Training."""

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys

sys.dont_write_bytecode = True

# Import Python Utilities
import argparse
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.tooling import repository_path_support

DEFAULT_CONFIG_DIR = PROJECT_PATH / "config" / "training" / "hydra" / "wave1"
DEFAULT_CONFIG_NAME = "config"
HYDRA_INTERNAL_KEY_LIST = [
    "dataset_profile",
    "model_family",
    "direction",
    "trainer_profile",
    "export_profile",
    "campaign_profile",
    "_hydra_transition",
]
REQUIRED_TRAINING_TOP_LEVEL_KEY_LIST = [
    "paths",
    "experiment",
    "metadata",
    "dataset",
    "model",
    "training",
    "runtime",
]


@dataclass(frozen=True)
class MaterializedConfigBundle:

    """Store the resolved training and dataset configuration payloads."""

    training_config: dict[str, Any]
    dataset_config: dict[str, Any]


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(description=__doc__)

    # Configure Hydra Composition Inputs
    argument_parser.add_argument(
        "--config-dir",
        default=str(DEFAULT_CONFIG_DIR),
        help="Hydra configuration directory to compose from.",
    )
    argument_parser.add_argument(
        "--config-name",
        default=DEFAULT_CONFIG_NAME,
        help="Hydra root config name without the .yaml suffix.",
    )
    argument_parser.add_argument(
        "--override",
        action="append",
        default=[],
        help="Hydra override. Repeat for multiple overrides.",
    )

    # Configure Materialized Outputs
    argument_parser.add_argument(
        "--output-path",
        default=None,
        help=(
            "Repository-relative or absolute output path for the resolved training YAML. "
            "Defaults to materialized/training_configs/<campaign_config_id>.yaml."
        ),
    )
    argument_parser.add_argument(
        "--dataset-output-path",
        default=None,
        help=(
            "Repository-relative or absolute output path for the resolved dataset YAML. "
            "Defaults to paths.dataset_config_path from the composed config."
        ),
    )
    argument_parser.add_argument(
        "--print-yaml",
        action="store_true",
        help="Print the materialized training YAML after writing it.",
    )

    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    # Build Argument Parser
    argument_parser = build_argument_parser()

    # Parse Command-Line Arguments
    parsed_arguments = argument_parser.parse_args()
    return parsed_arguments


def import_hydra_dependencies():

    """Import Hydra dependencies with a repository-specific error message.

    Returns:
        Tuple containing `compose`, `initialize_config_dir`, and `OmegaConf`.

    Raises:
        RuntimeError: If `hydra-core` or `omegaconf` is not installed.
    """

    try:

        from hydra import compose, initialize_config_dir
        from omegaconf import OmegaConf

    except ImportError as import_error:

        raise RuntimeError(
            "Hydra configuration composition requires `hydra-core` and "
            "`omegaconf`. Install the repository dependencies with "
            "`python -m pip install -r requirements.txt`."
        ) from import_error

    return compose, initialize_config_dir, OmegaConf


def resolve_path_argument(path_value: str) -> Path:

    """Resolve one repository-relative or absolute path argument.

    Args:
        path_value: Path supplied by the command line or default settings.

    Returns:
        Absolute path resolved against the repository root when needed.
    """

    # Resolve Repository Relative Paths
    path = Path(path_value)
    if path.is_absolute():
        return path
    return PROJECT_PATH / path


def remove_hydra_internal_keys(configuration_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Remove Hydra-only composition keys from the training payload.

    Args:
        configuration_dictionary: Resolved Hydra configuration dictionary.

    Returns:
        Training configuration dictionary without composition helper keys.
    """

    # Drop Composition-Only Sections
    training_config = dict(configuration_dictionary)
    for internal_key in HYDRA_INTERNAL_KEY_LIST:
        training_config.pop(internal_key, None)

    return training_config


def validate_materialized_training_config(training_config: dict[str, Any]) -> None:

    """Validate the minimum repository training-config contract.

    Args:
        training_config: Materialized training configuration payload.

    Raises:
        AssertionError: If the materialized config is missing required fields.
    """

    # Validate Top-Level Sections
    for required_key in REQUIRED_TRAINING_TOP_LEVEL_KEY_LIST:
        assert required_key in training_config, f"Missing training config section | {required_key}"
        assert isinstance(training_config[required_key], dict), (
            f"Training config section must be a dictionary | {required_key}"
        )

    # Validate Repository Execution Contract
    paths_dictionary = training_config["paths"]
    experiment_dictionary = training_config["experiment"]
    metadata_dictionary = training_config["metadata"]

    assert str(paths_dictionary.get("dataset_config_path", "")).strip(), (
        "paths.dataset_config_path must not be empty"
    )
    assert str(paths_dictionary.get("output_root", "")).strip().startswith(
        "output/training_runs/"
    ), "paths.output_root must stay under output/training_runs/"
    assert str(experiment_dictionary.get("run_name", "")).strip(), (
        "experiment.run_name must not be empty"
    )
    assert str(experiment_dictionary.get("model_family", "")).strip(), (
        "experiment.model_family must not be empty"
    )
    assert str(experiment_dictionary.get("model_type", "")).strip(), (
        "experiment.model_type must not be empty"
    )
    assert metadata_dictionary.get("hydra_transition_policy") == (
        "wave1_future_waves_materialization_pilot"
    ), "metadata.hydra_transition_policy must identify the pilot policy"


def validate_materialized_dataset_config(
    dataset_config: dict[str, Any],
    training_config: dict[str, Any],
) -> None:

    """Validate the minimum dataset-config contract.

    Args:
        dataset_config: Materialized dataset configuration payload.
        training_config: Materialized training configuration payload.

    Raises:
        AssertionError: If required dataset sections are missing.
    """

    # Validate Dataset Sections
    for required_key in ["paths", "dataset", "directions", "split", "dataloader"]:
        assert required_key in dataset_config, f"Missing dataset config section | {required_key}"
        assert isinstance(dataset_config[required_key], dict), (
            f"Dataset config section must be a dictionary | {required_key}"
        )

    direction_dictionary = dataset_config["directions"]
    metadata_dictionary = training_config["metadata"]
    assert direction_dictionary.get("use_forward_direction") == metadata_dictionary.get(
        "use_forward_direction"
    ), "Dataset and training metadata must agree on forward-direction usage"
    assert direction_dictionary.get("use_backward_direction") == metadata_dictionary.get(
        "use_backward_direction"
    ), "Dataset and training metadata must agree on backward-direction usage"


def build_default_training_output_path(training_config: dict[str, Any]) -> Path:

    """Build the default materialized training-config output path.

    Args:
        training_config: Materialized training configuration payload.

    Returns:
        Absolute default output path for the materialized training config.
    """

    # Build Deterministic Materialization Path
    campaign_config_id = str(training_config["metadata"].get("campaign_config_id", "")).strip()
    assert campaign_config_id, "metadata.campaign_config_id must not be empty"
    return (
        PROJECT_PATH
        / "config"
        / "training"
        / "hydra"
        / "wave1"
        / "materialized"
        / "training_configs"
        / f"{campaign_config_id}.yaml"
    )


def build_default_dataset_output_path(training_config: dict[str, Any]) -> Path:

    """Build the default materialized dataset-config output path.

    Args:
        training_config: Materialized training configuration payload.

    Returns:
        Absolute default output path for the materialized dataset config.
    """

    # Use The Resolved Training Config Reference
    dataset_config_path = str(training_config["paths"].get("dataset_config_path", "")).strip()
    assert dataset_config_path, "paths.dataset_config_path must not be empty"
    assert not Path(dataset_config_path).is_absolute(), (
        "paths.dataset_config_path must remain repository-relative"
    )
    return PROJECT_PATH / dataset_config_path


def compose_hydra_training_config(
    config_dir: Path,
    config_name: str,
    override_list: Sequence[str],
) -> MaterializedConfigBundle:

    """Compose the Hydra config and extract repository payloads.

    Args:
        config_dir: Hydra config directory.
        config_name: Hydra config name.
        override_list: Hydra command-line override list.

    Returns:
        Materialized config bundle containing training and dataset payloads.
    """

    # Import Hydra Lazily For Clear Dependency Errors
    compose, initialize_config_dir, OmegaConf = import_hydra_dependencies()

    # Compose Full Hydra Configuration
    with initialize_config_dir(version_base=None, config_dir=str(config_dir.resolve())):
        composed_config = compose(config_name=config_name, overrides=list(override_list))

    composed_dictionary = OmegaConf.to_container(composed_config, resolve=True)
    assert isinstance(composed_dictionary, dict), "Composed Hydra config must be a dictionary."

    # Extract Repository Payloads
    dataset_profile_dictionary = composed_dictionary.get("dataset_profile")
    assert isinstance(dataset_profile_dictionary, dict), "dataset_profile must be a dictionary."
    dataset_config = dataset_profile_dictionary.get("dataset_variant")
    assert isinstance(dataset_config, dict), "dataset_profile.dataset_variant must be a dictionary."

    training_config = remove_hydra_internal_keys(composed_dictionary)
    validate_materialized_training_config(training_config)
    validate_materialized_dataset_config(dataset_config, training_config)

    return MaterializedConfigBundle(
        training_config=training_config,
        dataset_config=dataset_config,
    )


def write_yaml_file(payload: dict[str, Any], output_path: Path) -> None:

    """Write one YAML payload with repository-standard formatting.

    Args:
        payload: YAML-serializable dictionary payload.
        output_path: Absolute output path.
    """

    # Persist YAML Payload
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False)


def main() -> None:

    """Run the Hydra materialization workflow."""

    # Parse Arguments And Configure Platform
    parsed_arguments = parse_command_line_arguments()
    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(parsed_arguments)
    )

    # Resolve Inputs And Outputs
    config_dir = resolve_path_argument(parsed_arguments.config_dir)
    # Compose And Materialize Configs
    materialized_bundle = compose_hydra_training_config(
        config_dir=config_dir,
        config_name=parsed_arguments.config_name,
        override_list=parsed_arguments.override,
    )

    # Resolve Materialized Output Paths
    if parsed_arguments.output_path is None:
        output_path = build_default_training_output_path(materialized_bundle.training_config)
    else:
        output_path = resolve_path_argument(parsed_arguments.output_path)

    if parsed_arguments.dataset_output_path is None:
        dataset_output_path = build_default_dataset_output_path(materialized_bundle.training_config)
    else:
        dataset_output_path = resolve_path_argument(parsed_arguments.dataset_output_path)

    write_yaml_file(materialized_bundle.dataset_config, dataset_output_path)
    write_yaml_file(materialized_bundle.training_config, output_path)

    print(f"[DONE] Materialized Hydra training config | {output_path.relative_to(PROJECT_PATH)}")
    print(f"[DONE] Materialized Hydra dataset config | {dataset_output_path.relative_to(PROJECT_PATH)}")

    if parsed_arguments.print_yaml:
        print()
        print(yaml.safe_dump(materialized_bundle.training_config, sort_keys=False))


if __name__ == "__main__":

    main()
