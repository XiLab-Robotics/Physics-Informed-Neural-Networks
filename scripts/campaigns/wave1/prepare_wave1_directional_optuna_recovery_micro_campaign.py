"""Prepare a lightweight Optuna recovery micro-campaign for Wave 1 neural HPO."""

from __future__ import annotations

# Import Python Utilities
import argparse

import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

PROJECT_PATH = Path(__file__).resolve().parents[3]

if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.tooling import repository_path_support

from scripts.campaigns.infrastructure.directional_training_variant_support import load_yaml_file, save_yaml_file

CAMPAIGN_NAME = "wave1_directional_optuna_recovery_micro_campaign_2026_05_12_10_49_02"
PLANNING_REPORT_RELATIVE_PATH = (
    "doc/reports/campaign_plans/wave1/"
    "2026-05-12-10-49-02_wave1_directional_optuna_recovery_micro_campaign_plan_report.md"
)
CAMPAIGN_ROOT = (
    PROJECT_PATH
    / "config"
    / "training"
    / "wave1_directional_optuna_recovery_micro"
    / "campaigns"
    / "2026-05-12_wave1_directional_optuna_recovery_micro_campaign"
)
SOURCE_TRAINING_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "training"
    / "wave1_directional_best_hyperparameter_search"
    / "campaigns"
    / "2026-05-11_wave1_directional_best_hyperparameter_search_campaign"
    / "source_training_configs"
    / "feedforward.yaml"
)


def build_source_training_config() -> dict[str, Any]:
    source_training_config = deepcopy(load_yaml_file(SOURCE_TRAINING_CONFIG_PATH))

    source_training_config["paths"]["output_root"] = "output/training_runs/feedforward_recovery_micro"
    source_training_config["experiment"]["run_name"] = "te_feedforward_optuna_recovery_micro_global"
    source_training_config["experiment"]["model_family"] = "feedforward_recovery_micro"

    metadata_dictionary = source_training_config.setdefault("metadata", {})
    metadata_dictionary["campaign_name"] = CAMPAIGN_NAME
    metadata_dictionary["planning_report_path"] = PLANNING_REPORT_RELATIVE_PATH
    metadata_dictionary["phase_name"] = "wave1_directional_optuna_recovery_micro"
    metadata_dictionary["campaign_config_id"] = "feedforward_recovery_micro_global"
    metadata_dictionary["notes"] = (
        f"{str(metadata_dictionary.get('notes', '')).strip()} "
        "Recovery micro-campaign source config for validating the Wave 1 neural Optuna launcher path."
    ).strip()

    dataset_dictionary = source_training_config.setdefault("dataset", {})
    dataset_dictionary["curve_batch_size"] = 8
    dataset_dictionary["point_stride"] = 20
    dataset_dictionary["num_workers"] = 2
    dataset_dictionary["pin_memory"] = False

    training_dictionary = source_training_config.setdefault("training", {})
    training_dictionary["min_epochs"] = 1
    training_dictionary["max_epochs"] = 2
    training_dictionary["patience"] = 1
    training_dictionary["fast_dev_run"] = False

    runtime_dictionary = source_training_config.setdefault("runtime", {})
    runtime_dictionary["benchmark"] = False
    runtime_dictionary["use_non_blocking_transfer"] = False
    return source_training_config


def build_study_config() -> dict[str, Any]:
    study_output_root = (
        "output/training_campaigns/wave1/directional_best_hyperparameter_search_recovery_micro/"
        f"{CAMPAIGN_NAME}/optuna_studies/feedforward_recovery_micro"
    )
    source_training_config_relative_path = str(
        (
            Path("config")
            / "training"
            / "wave1_directional_optuna_recovery_micro"
            / "campaigns"
            / "2026-05-12_wave1_directional_optuna_recovery_micro_campaign"
            / "source_training_configs"
            / "feedforward_recovery_micro.yaml"
        ).as_posix()
    )
    return {
        "study": {
            "study_name": f"{CAMPAIGN_NAME}_feedforward_recovery_micro_optuna",
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": PLANNING_REPORT_RELATIVE_PATH,
            "phase_name": "wave1_directional_optuna_recovery_micro",
            "source_training_config_path": source_training_config_relative_path,
            "study_output_root": study_output_root,
            "storage_relative_path": f"{study_output_root}/study.sqlite3",
            "model_family": "feedforward_recovery_micro",
            "base_model_family": "feedforward",
            "model_type": "feedforward",
            "training_variant": "global",
            "direction_scope_label": "bidirectional",
            "objective_metric_name": "val_mae",
            "direction": "minimize",
            "trial_budget": 1,
            "sampler": {
                "type": "TPESampler",
                "seed": 42,
                "n_startup_trials": 1,
            },
        },
        "execution": {
            "accelerator": "auto",
            "devices": 1,
            "precision": "32",
            "benchmark": False,
            "use_non_blocking_transfer": False,
        },
        "search_space": {
            "training.learning_rate": {
                "type": "categorical",
                "choices": [0.0007, 0.0010],
            },
            "training.weight_decay": {
                "type": "categorical",
                "choices": [0.0001],
            },
            "model.dropout_probability": {
                "type": "categorical",
                "choices": [0.05, 0.10],
            },
        },
    }



def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(description=__doc__)
    repository_path_support.add_platform_arguments(argument_parser)
    parsed_arguments = argument_parser.parse_args()
    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(parsed_arguments)
    )
    return parsed_arguments

def main() -> None:
    source_training_config = build_source_training_config()
    source_training_config_output_path = CAMPAIGN_ROOT / "source_training_configs" / "feedforward_recovery_micro.yaml"
    save_yaml_file(source_training_config, source_training_config_output_path)

    study_config = build_study_config()
    study_config_output_path = CAMPAIGN_ROOT / "optuna_studies" / "feedforward_recovery_micro.yaml"
    save_yaml_file(study_config, study_config_output_path)

    save_yaml_file(
        {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": PLANNING_REPORT_RELATIVE_PATH,
            "source_training_config_path": str(source_training_config_output_path.relative_to(PROJECT_PATH)).replace("\\", "/"),
            "study_config_path": str(study_config_output_path.relative_to(PROJECT_PATH)).replace("\\", "/"),
            "trial_budget": 1,
        },
        CAMPAIGN_ROOT / "campaign_manifest.yaml",
    )
    (CAMPAIGN_ROOT / "README.md").write_text(
        "\n".join(
            [
                f"# {CAMPAIGN_NAME}",
                "",
                "## Overview",
                "",
                "This package validates the recovered neural `Optuna` launcher path",
                "with one isolated `feedforward` micro study.",
                "",
                "## Search Counts",
                "",
                "- study configs: `1`",
                "- trial budget per study: `1`",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"[DONE] Prepared recovery micro-campaign | {CAMPAIGN_ROOT.relative_to(PROJECT_PATH)}", flush=True)


if __name__ == "__main__":
    main()
