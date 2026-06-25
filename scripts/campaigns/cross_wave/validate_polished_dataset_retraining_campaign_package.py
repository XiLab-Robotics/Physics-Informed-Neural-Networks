"""Validate polished-dataset retraining campaign manifests."""

from __future__ import annotations

# Import Python Utilities
import argparse, os, sys
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(os.path.abspath(__file__)).parents[3]
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.datasets import transmission_error_dataset
from scripts.training import shared_training_infrastructure

EXCLUDED_FULL_WAVE_PATH_TOKEN_LIST = [
    "paper_original",
    "paper_retuned",
    "rcim_original",
    "rcim_retuned",
]


def read_yaml_dictionary(input_path: Path) -> dict[str, Any]:

    """Read one YAML dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"YAML payload must be a dictionary | {input_path}"
    return payload


def resolve_relative_path(path_value: str | Path) -> Path:

    """Resolve one repository-relative path."""

    return shared_training_infrastructure.resolve_project_relative_path(path_value)


def validate_polished_dataset_contract() -> None:

    """Validate the shared polished dataset schema."""

    dataset_schema = transmission_error_dataset.resolve_dataset_schema(
        transmission_error_dataset.POLISHED_DATASET
    )
    assert dataset_schema.schema_name == "polished_point_v1"
    assert dataset_schema.input_feature_name_list == ["theta", "theta_dot", "tau_load", "T"]
    assert dataset_schema.target_feature_name_list == ["theta_TE"]
    assert dataset_schema.input_feature_dim == 4
    assert transmission_error_dataset.resolve_dataset_root(
        transmission_error_dataset.POLISHED_DATASET
    ).exists()


def validate_rcim_manifest(campaign_manifest: dict[str, Any]) -> None:

    """Validate the polished RCIM Model-Bank Reproduction campaign."""

    assert campaign_manifest["dataset_name"] == transmission_error_dataset.POLISHED_DATASET
    assert campaign_manifest["campaign_type"] == "rcim_model_bank_reproduction"

    queue_config_path_list = campaign_manifest.get("queue_config_path_list", [])
    assert len(queue_config_path_list) == 2, "RCIM polished package must contain forward and backward configs"

    observed_direction_set: set[str] = set()
    for queue_config_path_value in queue_config_path_list:
        queue_config_path = resolve_relative_path(queue_config_path_value)
        assert queue_config_path.exists(), f"Missing RCIM config | {queue_config_path}"
        queue_config = read_yaml_dictionary(queue_config_path)
        assert queue_config.get("dataset", {}).get("name") == transmission_error_dataset.POLISHED_DATASET
        direction_label = str(queue_config.get("data", {}).get("direction_label", "")).strip().lower()
        assert direction_label in {"forward", "backward"}, f"Invalid RCIM direction | {queue_config_path}"
        observed_direction_set.add(direction_label)
        run_name = str(queue_config.get("experiment", {}).get("run_name", ""))
        model_family = str(queue_config.get("experiment", {}).get("model_family", ""))
        assert "polished_dataset" in run_name
        assert model_family == "rcim_model_bank_reproduction"

    assert observed_direction_set == {"forward", "backward"}


def validate_full_wave_manifest(campaign_manifest: dict[str, Any]) -> None:

    """Validate the polished full-wave retraining campaign."""

    assert campaign_manifest["dataset_name"] == transmission_error_dataset.POLISHED_DATASET
    campaign_type = str(campaign_manifest["campaign_type"])
    assert campaign_type in {
        "full_wave_model_development_retraining",
        "early_wave_model_development_retraining",
    }

    queue_config_path_list = campaign_manifest.get("queue_config_path_list", [])
    expected_run_count = int(campaign_manifest.get("expected_run_count", 0))
    if campaign_type == "full_wave_model_development_retraining":
        assert expected_run_count == 108, f"Expected 108 full-wave configs | {expected_run_count}"
    else:
        assert expected_run_count == 36, f"Expected 36 early-wave configs | {expected_run_count}"
    assert len(queue_config_path_list) == expected_run_count

    observed_identifier_set: set[str] = set()
    observed_surface_set: set[str] = set()
    source_campaign_name = str(campaign_manifest.get("source_campaign_name", campaign_manifest["campaign_name"]))
    source_planning_report_path = str(
        campaign_manifest.get("source_planning_report_path", campaign_manifest["planning_report_path"])
    )
    for queue_config_path_value in queue_config_path_list:
        normalized_path_value = str(queue_config_path_value).replace("\\", "/").lower()
        assert not any(path_token in normalized_path_value for path_token in EXCLUDED_FULL_WAVE_PATH_TOKEN_LIST), (
            f"Excluded paper/reference path entered full-wave campaign | {queue_config_path_value}"
        )

        queue_config_path = resolve_relative_path(queue_config_path_value)
        assert queue_config_path.exists(), f"Missing full-wave config | {queue_config_path}"
        queue_config = read_yaml_dictionary(queue_config_path)

        experiment = queue_config.get("experiment", {})
        metadata = queue_config.get("metadata", {})
        dataset = queue_config.get("dataset", {})
        model = queue_config.get("model", {})
        assert isinstance(experiment, dict)
        assert isinstance(metadata, dict)
        assert isinstance(dataset, dict)
        assert isinstance(model, dict)

        assert dataset.get("name") == transmission_error_dataset.POLISHED_DATASET
        assert model.get("input_size") == "auto"
        assert metadata.get("campaign_name") == source_campaign_name
        assert metadata.get("planning_report_path") == source_planning_report_path

        canonical_id = str(metadata.get("campaign_config_id", ""))
        run_name = str(experiment.get("run_name", ""))
        model_family = str(experiment.get("model_family", ""))
        surface = str(metadata.get("training_variant", "")).strip().lower()
        assert surface in {"global", "fw", "bw"}, f"Invalid surface | {canonical_id}"
        assert canonical_id.endswith(f"_{surface}"), f"Canonical id must end with surface | {canonical_id}"
        assert model_family == canonical_id, f"Model family mismatch | {model_family} vs {canonical_id}"
        assert run_name == f"te_{canonical_id}", f"Run name mismatch | {run_name} vs te_{canonical_id}"
        assert canonical_id == canonical_id.lower(), f"Canonical id must be lowercase | {canonical_id}"

        observed_identifier_set.add(canonical_id)
        observed_surface_set.add(surface)

    assert len(observed_identifier_set) == expected_run_count
    assert observed_surface_set == {"global", "fw", "bw"}


def validate_campaign_package(campaign_manifest_path: Path) -> None:

    """Validate one polished retraining campaign package."""

    resolved_manifest_path = campaign_manifest_path.resolve()
    assert resolved_manifest_path.exists(), f"Campaign manifest does not exist | {resolved_manifest_path}"
    campaign_manifest = read_yaml_dictionary(resolved_manifest_path)
    validate_polished_dataset_contract()

    campaign_type = str(campaign_manifest.get("campaign_type", "")).strip()
    if campaign_type == "rcim_model_bank_reproduction":
        validate_rcim_manifest(campaign_manifest)
    elif campaign_type in {"full_wave_model_development_retraining", "early_wave_model_development_retraining"}:
        validate_full_wave_manifest(campaign_manifest)
    else:
        raise AssertionError(f"Unsupported polished retraining campaign type | {campaign_type}")

    print(
        "[DONE] Polished retraining campaign package validated | "
        f"campaign={campaign_manifest['campaign_name']} "
        f"type={campaign_type}"
    )


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("--campaign-manifest-path", type=Path, required=True)
    return argument_parser.parse_args()


def main() -> None:

    """Run command-line validation."""

    command_line_arguments = parse_command_line_arguments()
    validate_campaign_package(command_line_arguments.campaign_manifest_path)


if __name__ == "__main__":
    main()
