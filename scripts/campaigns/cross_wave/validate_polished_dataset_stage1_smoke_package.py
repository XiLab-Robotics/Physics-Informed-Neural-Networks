"""Validate the polished-dataset Stage 1 smoke campaign package."""

from __future__ import annotations

# Import Python Utilities
import argparse, os, sys
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

PROJECT_PATH = Path(os.path.abspath(__file__)).parents[3]
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.datasets import transmission_error_dataset
from scripts.training import shared_training_infrastructure

DEFAULT_CAMPAIGN_MANIFEST_PATH = (
    PROJECT_PATH
    / "config"
    / "training"
    / "polished_dataset_retraining"
    / "campaigns"
    / "2026-06-21_polished_dataset_stage1_smoke"
    / "campaign.yaml"
)
EXPECTED_DATASET_NAME = transmission_error_dataset.POLISHED_DATASET
EXCLUDED_PATH_TOKEN_LIST = ["paper_original", "paper_retuned", "rcim_original", "rcim_retuned"]


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:

    """Load and validate one YAML dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        yaml_dictionary = yaml.safe_load(input_file)
    assert isinstance(yaml_dictionary, dict), f"YAML file must contain a dictionary | {input_path}"
    return yaml_dictionary


def validate_campaign_package(campaign_manifest_path: Path, run_one_batch: bool) -> None:

    """Validate campaign paths, schema overrides, and optional model batches."""

    resolved_manifest_path = campaign_manifest_path.resolve()
    assert resolved_manifest_path.exists(), f"Campaign manifest does not exist | {resolved_manifest_path}"
    campaign_manifest = load_yaml_dictionary(resolved_manifest_path)
    assert campaign_manifest["dataset_name"] == EXPECTED_DATASET_NAME

    source_config_path_list = campaign_manifest.get("source_config_path_list", [])
    assert isinstance(source_config_path_list, list) and source_config_path_list, "Campaign source config list is empty"

    # Validate Shared Polished Dataset Contract
    dataset_schema = transmission_error_dataset.resolve_dataset_schema(EXPECTED_DATASET_NAME)
    assert dataset_schema.input_feature_name_list == ["theta", "theta_dot", "tau_load", "T", "direction_flag"]
    assert dataset_schema.target_feature_name_list == ["theta_TE"]
    assert dataset_schema.input_feature_dim == 5
    assert transmission_error_dataset.resolve_dataset_root(EXPECTED_DATASET_NAME).exists()

    # Validate Every Source Configuration
    for source_config_path_value in source_config_path_list:
        normalized_path_value = str(source_config_path_value).replace("\\", "/").lower()
        assert not any(path_token in normalized_path_value for path_token in EXCLUDED_PATH_TOKEN_LIST), (
            f"Excluded paper surface entered campaign | {source_config_path_value}"
        )

        source_config_path = shared_training_infrastructure.resolve_project_relative_path(source_config_path_value)
        assert source_config_path.exists(), f"Source training config does not exist | {source_config_path}"
        training_config = shared_training_infrastructure.apply_dataset_override(
            shared_training_infrastructure.load_training_config(source_config_path),
            EXPECTED_DATASET_NAME,
        )
        assert training_config["dataset"]["name"] == EXPECTED_DATASET_NAME
        assert training_config["model"]["input_size"] == "auto"

        if run_one_batch:
            training_config["dataset"]["num_workers"] = 0
            training_config["dataset"]["pin_memory"] = False
            training_config["dataset"]["point_stride"] = max(
                int(training_config["dataset"].get("point_stride", 1)),
                100,
            )
            training_config["dataset"]["maximum_points_per_curve"] = 64
            if training_config["dataset"].get("collate_mode") == "sequence":
                training_config["dataset"]["maximum_sequences_per_curve"] = 32

            model_type = str(training_config["experiment"]["model_type"]).strip().lower()
            if model_type in {"hist_gradient_boosting", "random_forest"}:
                datamodule = shared_training_infrastructure.create_datamodule_from_training_config(training_config)
                datamodule.setup(stage="fit")
                regression_backbone = None
            else:
                datamodule, regression_backbone, _, _ = shared_training_infrastructure.initialize_training_components(
                    training_config
                )
            batch_dictionary = shared_training_infrastructure.fetch_first_batch(datamodule)
            shared_training_infrastructure.validate_batch_dictionary(
                batch_dictionary,
                input_feature_dim=dataset_schema.input_feature_dim,
                target_feature_dim=1,
            )
            if model_type not in {"hist_gradient_boosting", "random_forest"}:
                assert regression_backbone is not None
                reloaded_backbone = shared_training_infrastructure.create_regression_backbone_from_training_config(
                    training_config,
                    datamodule.get_input_feature_dim(),
                )
                assert getattr(reloaded_backbone, "input_size", None) == dataset_schema.input_feature_dim, (
                    f"Reload backbone input_size mismatch | {source_config_path_value}"
                )

        print(f"[PASS] {source_config_path_value}")

    print(f"[DONE] Polished Stage 1 package validated | configs={len(source_config_path_list)}")


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse package validation arguments."""

    argument_parser = argparse.ArgumentParser(description="Validate the polished-dataset Stage 1 smoke package.")
    argument_parser.add_argument("--campaign-manifest-path", type=Path, default=DEFAULT_CAMPAIGN_MANIFEST_PATH)
    argument_parser.add_argument("--run-one-batch", action="store_true")
    return argument_parser.parse_args()


def main() -> None:

    """Run package validation."""

    command_line_arguments = parse_command_line_arguments()
    validate_campaign_package(
        command_line_arguments.campaign_manifest_path,
        command_line_arguments.run_one_batch,
    )


if __name__ == "__main__":
    main()
