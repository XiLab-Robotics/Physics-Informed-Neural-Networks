"""Validate dataset/input-mode retraining campaign packages."""

from __future__ import annotations

# Import Python Utilities
import argparse
import os
import sys
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(os.path.abspath(__file__)).parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.datasets import transmission_error_dataset

SURFACE_NAME_SET = {"global", "fw", "bw"}


def read_yaml_dictionary(path_value: str | Path) -> dict[str, Any]:

    """Read one YAML dictionary."""

    input_path = Path(path_value)
    if not input_path.is_absolute():
        input_path = PROJECT_PATH / input_path
    input_path = input_path.resolve()
    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def validate_queue_config(
    queue_config_path: str,
    manifest: dict[str, Any],
) -> str:

    """Validate one queue config and return its normalized surface."""

    queue_config = read_yaml_dictionary(queue_config_path)
    dataset = queue_config.get("dataset", {})
    metadata = queue_config.get("metadata", {})
    experiment = queue_config.get("experiment", {})
    model = queue_config.get("model", {})
    assert isinstance(dataset, dict)
    assert isinstance(metadata, dict)
    assert isinstance(experiment, dict)
    assert isinstance(model, dict)

    assert dataset.get("name") == manifest["dataset_name"]
    assert dataset.get("input_mode") == manifest["input_mode"]
    assert metadata.get("dataset_name") == manifest["dataset_name"]
    assert metadata.get("input_mode") == manifest["input_mode"]
    assert metadata.get("dataset_schema") == manifest["dataset_schema"]
    assert metadata.get("source_dataset_root") == manifest["source_dataset_root"]
    assert metadata.get("expected_model_archive_root") == manifest["expected_model_archive_root"]
    assert model.get("input_size") == "auto"

    resolved_schema = transmission_error_dataset.resolve_dataset_schema(
        dataset.get("name"),
        dataset.get("input_mode"),
    )
    assert resolved_schema.schema_name == manifest["dataset_schema"]

    surface = str(metadata.get("training_variant", "")).strip().lower()
    assert surface in SURFACE_NAME_SET, f"Invalid surface | {surface} | {queue_config_path}"
    canonical_id = str(metadata.get("campaign_config_id", ""))
    assert canonical_id.endswith(f"_{surface}"), f"Campaign id/surface mismatch | {canonical_id}"
    assert experiment.get("model_family") == canonical_id
    return surface


def validate_campaign_package(campaign_manifest_path: Path) -> None:

    """Validate one campaign manifest."""

    manifest = read_yaml_dictionary(campaign_manifest_path)
    assert manifest["campaign_type"] == "dataset_input_mode_model_development_retraining"
    assert manifest["input_mode"] in transmission_error_dataset.SUPPORTED_INPUT_MODE_LIST
    assert manifest["dataset_name"] in transmission_error_dataset.SUPPORTED_DATASET_NAME_LIST
    assert not (
        manifest["dataset_name"] == transmission_error_dataset.SIMPLIFIED_DATASET
        and manifest["input_mode"] == transmission_error_dataset.ACTUAL_VALUES_INPUT_MODE
    )

    queue_path_list = manifest.get("queue_config_path_list", [])
    assert len(queue_path_list) == int(manifest["expected_run_count"]) == 3
    surface_set = {validate_queue_config(queue_path, manifest) for queue_path in queue_path_list}
    assert surface_set == SURFACE_NAME_SET, f"Missing campaign surfaces | {surface_set}"
    print(f"[DONE] Dataset/input-mode campaign package validated | {manifest['campaign_name']}")


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign-manifest-path", type=Path, required=True)
    return parser.parse_args()


def main() -> None:

    """Run command-line validation."""

    arguments = parse_command_line_arguments()
    validate_campaign_package(arguments.campaign_manifest_path)


if __name__ == "__main__":
    main()
