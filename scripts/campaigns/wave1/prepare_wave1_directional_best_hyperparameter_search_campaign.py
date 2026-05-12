"""Prepare the mixed Wave 1 directional best-hyperparameter search campaign."""

from __future__ import annotations

import itertools
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

PROJECT_PATH = Path(__file__).resolve().parents[3]

if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

from scripts.campaigns.infrastructure.directional_training_variant_support import (
    BACKWARD_ONLY_TRAINING_VARIANT,
    FORWARD_ONLY_TRAINING_VARIANT,
    GLOBAL_TRAINING_VARIANT,
    TRAINING_VARIANT_SEQUENCE,
    build_dataset_config_for_variant,
    build_variant_model_family,
    load_yaml_file,
    resolve_variant_specification,
    save_yaml_file,
    strip_completed_run_artifact_metadata,
)

PLANNING_REPORT_RELATIVE_PATH = (
    "doc/reports/campaign_plans/wave1/"
    "2026-05-11-19-41-11_wave1_directional_best_hyperparameter_search_campaign_plan_report.md"
)
CAMPAIGN_NAME = "wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11"
CAMPAIGN_ROOT = (
    PROJECT_PATH
    / "config"
    / "training"
    / "wave1_directional_best_hyperparameter_search"
    / "campaigns"
    / "2026-05-11_wave1_directional_best_hyperparameter_search_campaign"
)
DATASET_VARIANT_ROOT = CAMPAIGN_ROOT / "dataset_variants"
GRID_QUEUE_ROOT = CAMPAIGN_ROOT / "grid_queue"
OPTUNA_STUDY_ROOT = CAMPAIGN_ROOT / "optuna_studies"
SOURCE_CONFIG_ROOT = CAMPAIGN_ROOT / "source_training_configs"
CANONICAL_DATASET_CONFIG_PATH = PROJECT_PATH / "config" / "datasets" / "transmission_error_dataset.yaml"
DIRECTIONAL_SOURCE_CAMPAIGN_NAME = "wave1_directional_retraining_campaign_2026_05_06_16_07_16"
FAMILY_ORDER = [
    "tree",
    "residual_harmonic_mlp",
    "feedforward",
    "periodic_mlp",
    "harmonic_regression",
]
NEURAL_BASE_FAMILY_SET = {
    "feedforward",
    "periodic_mlp",
    "residual_harmonic_mlp",
}
OPTUNA_TRIAL_BUDGET = 18
TREE_GRID_PARAMETER_DICTIONARY = {
    "model.max_depth": [6, 8, 10],
    "model.learning_rate": [0.03, 0.05, 0.08],
    "model.min_samples_leaf": [10, 20],
}
HARMONIC_REGRESSION_GRID_PARAMETER_DICTIONARY = {
    "model.harmonic_order": [8, 12],
    "training.learning_rate": [0.0005, 0.0010, 0.0020],
    "dataset.point_stride": [1, 5],
}
OPTUNA_SEARCH_SPACE_BY_MODEL_TYPE = {
    "feedforward": {
        "training.learning_rate": {"type": "float", "low": 0.0003, "high": 0.0030, "log": True},
        "training.weight_decay": {"type": "float", "low": 1.0e-06, "high": 5.0e-04, "log": True},
        "dataset.curve_batch_size": {"type": "categorical", "choices": [2, 4, 8]},
        "model.dropout_probability": {"type": "categorical", "choices": [0.0, 0.05, 0.10, 0.15]},
        "model.hidden_size": {
            "type": "categorical",
            "choices": [
                [256, 256, 128, 64],
                [384, 256, 128, 64],
                [256, 256, 256, 128],
                [256, 128, 64],
            ],
        },
    },
    "periodic_mlp": {
        "training.learning_rate": {"type": "float", "low": 0.0003, "high": 0.0030, "log": True},
        "training.weight_decay": {"type": "float", "low": 1.0e-06, "high": 5.0e-04, "log": True},
        "dataset.curve_batch_size": {"type": "categorical", "choices": [2, 4, 8]},
        "model.dropout_probability": {"type": "categorical", "choices": [0.0, 0.05, 0.10, 0.15]},
        "model.hidden_size": {
            "type": "categorical",
            "choices": [
                [128, 128, 64],
                [192, 128, 64],
                [128, 128, 128, 64],
                [256, 128, 64],
            ],
        },
        "model.harmonic_order": {"type": "categorical", "choices": [4, 6, 8]},
    },
    "residual_harmonic_mlp": {
        "training.learning_rate": {"type": "float", "low": 0.0003, "high": 0.0030, "log": True},
        "training.weight_decay": {"type": "float", "low": 1.0e-06, "high": 5.0e-04, "log": True},
        "dataset.curve_batch_size": {"type": "categorical", "choices": [2, 4, 8]},
        "model.residual_dropout_probability": {"type": "categorical", "choices": [0.0, 0.05, 0.10, 0.15]},
        "model.residual_hidden_size": {
            "type": "categorical",
            "choices": [
                [128, 128, 64],
                [192, 128, 64],
                [128, 128, 128, 64],
                [256, 128, 64],
            ],
        },
        "model.harmonic_order": {"type": "categorical", "choices": [8, 12, 16]},
    },
}


def build_dataset_variant_relative_path(training_variant: str) -> str:
    variant_specification = resolve_variant_specification(training_variant)
    dataset_filename = f"transmission_error_dataset_{variant_specification['dataset_suffix']}.yaml"
    return str(
        (
            Path("config")
            / "training"
            / "wave1_directional_best_hyperparameter_search"
            / "campaigns"
            / "2026-05-11_wave1_directional_best_hyperparameter_search_campaign"
            / "dataset_variants"
            / dataset_filename
        ).as_posix()
    )


def build_surface_registry_relative_path(base_model_family: str, training_variant: str) -> str:
    surface_model_family = build_variant_model_family(base_model_family, training_variant)
    return f"output/registries/families/{surface_model_family}/latest_family_best.yaml"


def load_surface_source_training_config(base_model_family: str, training_variant: str) -> dict[str, Any]:
    surface_model_family = build_variant_model_family(base_model_family, training_variant)
    candidate_training_config_path_list = sorted(
        (PROJECT_PATH / "output" / "training_runs" / surface_model_family).glob("*/training_config.yaml"),
        key=lambda path_value: path_value.stat().st_mtime,
        reverse=True,
    )

    for candidate_training_config_path in candidate_training_config_path_list:
        candidate_training_config = load_yaml_file(candidate_training_config_path)
        metadata_dictionary = candidate_training_config.get("metadata", {})
        if not isinstance(metadata_dictionary, dict):
            continue
        if str(metadata_dictionary.get("campaign_name", "")).strip() != DIRECTIONAL_SOURCE_CAMPAIGN_NAME:
            continue
        if str(metadata_dictionary.get("training_variant", "")).strip() != training_variant:
            continue
        return candidate_training_config

    family_registry_path = PROJECT_PATH / build_surface_registry_relative_path(base_model_family, training_variant)
    family_registry_dictionary = load_yaml_file(family_registry_path)
    best_entry_dictionary = family_registry_dictionary["best_entry"]
    output_directory = PROJECT_PATH / str(best_entry_dictionary["output_directory"])
    return load_yaml_file(output_directory / "training_config.yaml")


def build_source_training_config_relative_path(surface_model_family: str) -> str:
    return str(
        (
            Path("config")
            / "training"
            / "wave1_directional_best_hyperparameter_search"
            / "campaigns"
            / "2026-05-11_wave1_directional_best_hyperparameter_search_campaign"
            / "source_training_configs"
            / f"{surface_model_family}.yaml"
        ).as_posix()
    )


def build_campaign_output_root_relative_path() -> str:
    return f"output/training_campaigns/wave1/directional_best_hyperparameter_search/{CAMPAIGN_NAME}"


def build_grid_parameter_combinations(parameter_dictionary: dict[str, list[Any]]) -> list[dict[str, Any]]:
    dotted_key_list = list(parameter_dictionary.keys())
    candidate_value_matrix = [parameter_dictionary[dotted_key] for dotted_key in dotted_key_list]
    parameter_combination_list: list[dict[str, Any]] = []
    for parameter_value_tuple in itertools.product(*candidate_value_matrix):
        parameter_combination_list.append(
            {dotted_key: parameter_value for dotted_key, parameter_value in zip(dotted_key_list, parameter_value_tuple)}
        )
    return parameter_combination_list


def set_nested_dictionary_value(payload: dict[str, Any], dotted_key: str, value: Any) -> None:
    key_token_list = dotted_key.split(".")
    current_dictionary = payload
    for key_token in key_token_list[:-1]:
        current_dictionary = current_dictionary.setdefault(key_token, {})
    current_dictionary[key_token_list[-1]] = value


def build_grid_candidate_token(candidate_parameter_dictionary: dict[str, Any]) -> str:
    token_list: list[str] = []
    for dotted_key, parameter_value in candidate_parameter_dictionary.items():
        key_suffix = dotted_key.split(".")[-1]
        compact_key = (
            key_suffix.replace("learning_rate", "lr")
            .replace("min_samples_leaf", "leaf")
            .replace("max_depth", "depth")
            .replace("harmonic_order", "order")
            .replace("point_stride", "stride")
        )
        compact_value = str(parameter_value).replace(".", "").replace("[", "").replace("]", "").replace(", ", "-")
        token_list.append(f"{compact_key}{compact_value}")
    return "_".join(token_list)


def build_grid_candidate_config(
    source_training_config: dict[str, Any],
    candidate_parameter_dictionary: dict[str, Any],
    candidate_index: int,
    candidate_total: int,
    campaign_config_id: str,
) -> dict[str, Any]:
    prepared_training_config = strip_completed_run_artifact_metadata(source_training_config)
    prepared_training_config = deepcopy(prepared_training_config)

    for dotted_key, parameter_value in candidate_parameter_dictionary.items():
        set_nested_dictionary_value(prepared_training_config, dotted_key, parameter_value)

    experiment_dictionary = prepared_training_config["experiment"]
    metadata_dictionary = prepared_training_config.setdefault("metadata", {})
    runtime_dictionary = prepared_training_config.setdefault("runtime", {})
    run_name_suffix = build_grid_candidate_token(candidate_parameter_dictionary)
    experiment_dictionary["run_name"] = f"{experiment_dictionary['run_name']}_grid_{run_name_suffix}"

    metadata_dictionary["campaign_name"] = CAMPAIGN_NAME
    metadata_dictionary["planning_report_path"] = PLANNING_REPORT_RELATIVE_PATH
    metadata_dictionary["phase_name"] = "wave1_directional_best_hyperparameter_search"
    metadata_dictionary["campaign_config_id"] = campaign_config_id
    metadata_dictionary["hpo_engine"] = "bounded_grid"
    metadata_dictionary["hpo_candidate_index"] = int(candidate_index)
    metadata_dictionary["hpo_candidate_total"] = int(candidate_total)
    metadata_dictionary["notes"] = (
        f"{str(metadata_dictionary.get('notes', '')).strip()} "
        f"Bounded hyperparameter-grid candidate {candidate_index}/{candidate_total}."
    ).strip()

    runtime_dictionary["accelerator"] = "cpu"
    runtime_dictionary["devices"] = 1
    runtime_dictionary["precision"] = "32"
    runtime_dictionary["benchmark"] = False
    runtime_dictionary["use_non_blocking_transfer"] = False
    return prepared_training_config


def build_optuna_study_config(
    source_training_config_relative_path: str,
    surface_model_family: str,
    source_training_config: dict[str, Any],
    study_output_root_relative_path: str,
) -> dict[str, Any]:
    experiment_dictionary = source_training_config["experiment"]
    metadata_dictionary = source_training_config.get("metadata", {})
    model_type = str(experiment_dictionary["model_type"]).strip().lower()
    return {
        "study": {
            "study_name": f"{CAMPAIGN_NAME}_{surface_model_family}_optuna",
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": PLANNING_REPORT_RELATIVE_PATH,
            "phase_name": "wave1_directional_best_hyperparameter_search",
            "source_training_config_path": source_training_config_relative_path,
            "study_output_root": study_output_root_relative_path,
            "storage_relative_path": f"{study_output_root_relative_path}/study.sqlite3",
            "model_family": surface_model_family,
            "base_model_family": str(metadata_dictionary.get("base_model_family", surface_model_family)),
            "model_type": model_type,
            "training_variant": str(metadata_dictionary.get("training_variant", "global")),
            "direction_scope_label": str(metadata_dictionary.get("direction_scope_label", "bidirectional")),
            "objective_metric_name": "val_mae",
            "direction": "minimize",
            "trial_budget": OPTUNA_TRIAL_BUDGET,
            "sampler": {
                "type": "TPESampler",
                "seed": 42,
                "n_startup_trials": 5,
            },
        },
        "execution": {
            "accelerator": "auto",
            "devices": 1,
            "precision": "32",
            "benchmark": True,
            "use_non_blocking_transfer": True,
            "dataset_num_workers": 2,
            "dataset_pin_memory": True,
        },
        "search_space": OPTUNA_SEARCH_SPACE_BY_MODEL_TYPE[model_type],
    }


def build_campaign_readme_markdown(
    grid_queue_relative_path_list: list[str],
    optuna_study_relative_path_list: list[str],
) -> str:
    markdown_line_list = [
        f"# {CAMPAIGN_NAME}",
        "",
        "## Overview",
        "",
        "This package refines the `15` directional `Wave 1` winner surfaces with",
        "a mixed search strategy.",
        "",
        "- bounded CPU-throttled grid search for `tree` and `harmonic_regression`;",
        "- persisted `Optuna` studies for the three neural families.",
        "",
        "## Search Counts",
        "",
        f"- bounded grid queue configs: `{len(grid_queue_relative_path_list)}`",
        f"- Optuna study configs: `{len(optuna_study_relative_path_list)}`",
        f"- Optuna trial budget per study: `{OPTUNA_TRIAL_BUDGET}`",
        "",
    ]
    return "\n".join(markdown_line_list) + "\n"


def main() -> None:
    base_dataset_config = load_yaml_file(CANONICAL_DATASET_CONFIG_PATH)
    grid_queue_relative_path_list: list[str] = []
    optuna_study_relative_path_list: list[str] = []

    for training_variant in TRAINING_VARIANT_SEQUENCE:
        dataset_variant_payload = build_dataset_config_for_variant(base_dataset_config, training_variant)
        dataset_variant_relative_path = build_dataset_variant_relative_path(training_variant)
        save_yaml_file(dataset_variant_payload, PROJECT_PATH / dataset_variant_relative_path)

    grid_queue_index = 1
    for base_model_family in FAMILY_ORDER:
        for training_variant in TRAINING_VARIANT_SEQUENCE:
            surface_model_family = build_variant_model_family(base_model_family, training_variant)
            source_training_config = load_surface_source_training_config(base_model_family, training_variant)
            source_training_config["paths"]["dataset_config_path"] = build_dataset_variant_relative_path(training_variant)
            source_training_config_relative_path = build_source_training_config_relative_path(surface_model_family)
            save_yaml_file(source_training_config, PROJECT_PATH / source_training_config_relative_path)

            if base_model_family in NEURAL_BASE_FAMILY_SET:
                study_relative_path = (
                    Path("config")
                    / "training"
                    / "wave1_directional_best_hyperparameter_search"
                    / "campaigns"
                    / "2026-05-11_wave1_directional_best_hyperparameter_search_campaign"
                    / "optuna_studies"
                    / f"{surface_model_family}.yaml"
                )
                study_output_root_relative_path = f"{build_campaign_output_root_relative_path()}/optuna_studies/{surface_model_family}"
                study_payload = build_optuna_study_config(
                    source_training_config_relative_path,
                    surface_model_family,
                    source_training_config,
                    study_output_root_relative_path,
                )
                save_yaml_file(study_payload, PROJECT_PATH / study_relative_path)
                optuna_study_relative_path_list.append(str(study_relative_path).replace("\\", "/"))
                continue

            if base_model_family == "tree":
                parameter_combination_list = build_grid_parameter_combinations(TREE_GRID_PARAMETER_DICTIONARY)
            else:
                parameter_combination_list = build_grid_parameter_combinations(HARMONIC_REGRESSION_GRID_PARAMETER_DICTIONARY)

            candidate_total = len(parameter_combination_list)
            for candidate_index, candidate_parameter_dictionary in enumerate(parameter_combination_list, start=1):
                campaign_config_id = f"{surface_model_family}_grid_{candidate_index:03d}"
                candidate_payload = build_grid_candidate_config(
                    source_training_config,
                    candidate_parameter_dictionary,
                    candidate_index,
                    candidate_total,
                    campaign_config_id,
                )
                candidate_filename = (
                    f"{grid_queue_index:03d}_{surface_model_family}_{build_grid_candidate_token(candidate_parameter_dictionary)}.yaml"
                )
                candidate_output_path = GRID_QUEUE_ROOT / candidate_filename
                save_yaml_file(candidate_payload, candidate_output_path)
                grid_queue_relative_path_list.append(str(candidate_output_path.relative_to(PROJECT_PATH)).replace("\\", "/"))
                grid_queue_index += 1

    save_yaml_file(
        {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": PLANNING_REPORT_RELATIVE_PATH,
            "campaign_output_root": build_campaign_output_root_relative_path(),
            "grid_queue_relative_path_list": grid_queue_relative_path_list,
            "optuna_study_relative_path_list": optuna_study_relative_path_list,
            "optuna_trial_budget_per_study": OPTUNA_TRIAL_BUDGET,
        },
        CAMPAIGN_ROOT / "campaign_manifest.yaml",
    )
    (CAMPAIGN_ROOT / "README.md").write_text(
        build_campaign_readme_markdown(grid_queue_relative_path_list, optuna_study_relative_path_list),
        encoding="utf-8",
    )
    print(
        "[DONE] Prepared Wave 1 directional best-hyperparameter search campaign | "
        f"grid_configs={len(grid_queue_relative_path_list)} | optuna_studies={len(optuna_study_relative_path_list)}",
        flush=True,
    )
    print(f"[DONE] Campaign root | {CAMPAIGN_ROOT.relative_to(PROJECT_PATH)}", flush=True)


if __name__ == "__main__":
    main()
