"""Validate RCIM track1 polished input-mode campaign packages."""

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

EXPECTED_INPUT_FEATURE_NAME_LIST = [
    "angular_position_deg",
    "input_speed_rpm",
    "input_torque_nm",
    "oil_temperature_deg",
    "direction_flag",
]
EXPECTED_SURFACE_SET = {"global", "fw", "bw"}
SURFACE_DIRECTION_DICTIONARY = {
    "global": "global",
    "fw": transmission_error_dataset.FORWARD_DIRECTION,
    "bw": transmission_error_dataset.BACKWARD_DIRECTION,
}


def read_yaml_dictionary(path_value: str | Path) -> dict[str, Any]:

    """Read one YAML dictionary."""

    input_path = Path(path_value)
    if not input_path.is_absolute():
        input_path = PROJECT_PATH / input_path
    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def validate_queue_config(queue_config_path: str, manifest: dict[str, Any]) -> str:

    """Validate one RCIM track1 queue config."""

    queue_config = read_yaml_dictionary(queue_config_path)
    dataset = queue_config.get("dataset", {})
    data = queue_config.get("data", {})
    metadata = queue_config.get("metadata", {})
    experiment = queue_config.get("experiment", {})
    assert isinstance(dataset, dict)
    assert isinstance(data, dict)
    assert isinstance(metadata, dict)
    assert isinstance(experiment, dict)

    assert dataset.get("name") == manifest["dataset_name"]
    assert dataset.get("input_mode") == manifest["input_mode"]
    assert metadata.get("dataset_name") == manifest["dataset_name"]
    assert metadata.get("input_mode") == manifest["input_mode"]
    assert metadata.get("dataset_schema") == manifest["dataset_schema"]
    assert metadata.get("source_dataset_root") == manifest["source_dataset_root"]
    assert metadata.get("expected_model_archive_root") == manifest["expected_model_archive_root"]
    assert data.get("input_feature_names") == EXPECTED_INPUT_FEATURE_NAME_LIST
    assert metadata.get("expected_input_feature_names") == EXPECTED_INPUT_FEATURE_NAME_LIST

    surface = str(metadata.get("training_variant", "")).strip().lower()
    assert surface in EXPECTED_SURFACE_SET, f"Invalid RCIM track1 surface | {surface}"
    assert data.get("direction_label") == SURFACE_DIRECTION_DICTIONARY[surface]
    assert experiment.get("model_family") == "rcim_track1"
    assert str(experiment.get("run_name", "")).endswith(f"_{surface}")
    assert str(metadata.get("campaign_config_id", "")) == f"rcim_track1_{surface}"
    return surface


def validate_campaign_package(campaign_manifest_path: Path) -> None:

    """Validate one RCIM track1 input-mode campaign manifest."""

    manifest = read_yaml_dictionary(campaign_manifest_path)
    assert manifest["campaign_type"] == "rcim_track1_input_mode_retraining"
    assert manifest["family_name"] == "rcim_track1"
    assert manifest["dataset_name"] == transmission_error_dataset.POLISHED_DATASET
    assert manifest["input_mode"] in {
        transmission_error_dataset.SETPOINT_INPUT_MODE,
        transmission_error_dataset.ACTUAL_VALUES_INPUT_MODE,
    }

    resolved_schema = transmission_error_dataset.resolve_dataset_schema(
        manifest["dataset_name"],
        manifest["input_mode"],
    )
    assert resolved_schema.schema_name == manifest["dataset_schema"]
    assert resolved_schema.input_feature_name_list == EXPECTED_INPUT_FEATURE_NAME_LIST
    assert resolved_schema.input_feature_dim == 5

    queue_path_list = manifest.get("queue_config_path_list", [])
    assert len(queue_path_list) == int(manifest["expected_run_count"]) == 3
    observed_surface_set = {validate_queue_config(queue_path, manifest) for queue_path in queue_path_list}
    assert observed_surface_set == EXPECTED_SURFACE_SET, f"Missing surfaces | {observed_surface_set}"
    assert str(manifest["expected_model_archive_root"]).startswith(
        "models/polished_dataset/paper_reference/rcim_track1/"
    )
    print(
        "[DONE] RCIM track1 input-mode campaign package validated | "
        f"{manifest['campaign_name']}"
    )


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign-manifest-path", type=Path, required=True)
    return parser.parse_args()


def main() -> None:

    """Run validator."""

    arguments = parse_command_line_arguments()
    validate_campaign_package(arguments.campaign_manifest_path)


if __name__ == "__main__":
    main()
