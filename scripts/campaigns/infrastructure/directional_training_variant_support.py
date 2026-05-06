"""Shared helpers for global/Fw/Bw training-variant campaign preparation."""

from __future__ import annotations

# Import Python Utilities
from copy import deepcopy
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

PROJECT_PATH = Path(__file__).resolve().parents[3]
GLOBAL_TRAINING_VARIANT = "global"
FORWARD_ONLY_TRAINING_VARIANT = "Fw"
BACKWARD_ONLY_TRAINING_VARIANT = "Bw"
TRAINING_VARIANT_SEQUENCE = [
    GLOBAL_TRAINING_VARIANT,
    FORWARD_ONLY_TRAINING_VARIANT,
    BACKWARD_ONLY_TRAINING_VARIANT,
]
TRAINING_VARIANT_SPECIFICATION = {
    GLOBAL_TRAINING_VARIANT: {
        "run_suffix": "global",
        "family_suffix": "",
        "dataset_suffix": "global",
        "direction_scope_label": "bidirectional",
        "use_forward_direction": True,
        "use_backward_direction": True,
    },
    FORWARD_ONLY_TRAINING_VARIANT: {
        "run_suffix": "Fw",
        "family_suffix": "_fw",
        "dataset_suffix": "fw",
        "direction_scope_label": "forward_only",
        "use_forward_direction": True,
        "use_backward_direction": False,
    },
    BACKWARD_ONLY_TRAINING_VARIANT: {
        "run_suffix": "Bw",
        "family_suffix": "_bw",
        "dataset_suffix": "bw",
        "direction_scope_label": "backward_only",
        "use_forward_direction": False,
        "use_backward_direction": True,
    },
}


def load_yaml_file(input_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    with input_path.open("r", encoding="utf-8") as input_file:
        yaml_dictionary = yaml.safe_load(input_file)
    assert isinstance(yaml_dictionary, dict), f"YAML file must contain a dictionary | {input_path}"
    return yaml_dictionary


def save_yaml_file(payload: dict[str, Any], output_path: Path) -> None:

    """Persist one YAML dictionary to disk."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False)


def resolve_variant_specification(training_variant: str) -> dict[str, Any]:

    """Resolve the configuration specification for one training variant."""

    assert training_variant in TRAINING_VARIANT_SPECIFICATION, (
        f"Unsupported training variant | {training_variant}"
    )
    return TRAINING_VARIANT_SPECIFICATION[training_variant]


def build_dataset_config_for_variant(
    base_dataset_config: dict[str, Any],
    training_variant: str,
) -> dict[str, Any]:

    """Clone and directionalize one dataset config payload."""

    variant_specification = resolve_variant_specification(training_variant)
    dataset_config = deepcopy(base_dataset_config)
    direction_dictionary = dataset_config.setdefault("directions", {})
    direction_dictionary["use_forward_direction"] = variant_specification["use_forward_direction"]
    direction_dictionary["use_backward_direction"] = variant_specification["use_backward_direction"]
    return dataset_config


def build_variant_model_family(base_model_family: str, training_variant: str) -> str:

    """Build the model-family key used by outputs and registries."""

    variant_specification = resolve_variant_specification(training_variant)
    base_model_family = str(base_model_family).strip().lower()
    assert base_model_family, "Base model family must not be empty"
    return f"{base_model_family}{variant_specification['family_suffix']}"


def build_variant_run_name(base_run_name: str, training_variant: str) -> str:

    """Build the run name used by one directional training variant."""

    variant_specification = resolve_variant_specification(training_variant)
    base_run_name = str(base_run_name).strip()
    assert base_run_name, "Base run name must not be empty"
    return f"{base_run_name}_{variant_specification['run_suffix']}"


def strip_completed_run_artifact_metadata(training_config: dict[str, Any]) -> dict[str, Any]:

    """Remove artifact-specific residue from a completed training config snapshot."""

    cleaned_training_config = deepcopy(training_config)
    metadata_dictionary = cleaned_training_config.setdefault("metadata", {})
    for metadata_key in ["output_artifact_kind", "output_run_name", "run_instance_id"]:
        metadata_dictionary.pop(metadata_key, None)
    return cleaned_training_config


def apply_directional_variant_to_training_config(
    base_training_config: dict[str, Any],
    training_variant: str,
    dataset_config_relative_path: str,
    planning_report_relative_path: str,
    campaign_name: str,
    phase_name: str,
    campaign_config_id: str,
    note_suffix: str,
) -> dict[str, Any]:

    """Build one training-config payload for a directional retraining variant."""

    variant_specification = resolve_variant_specification(training_variant)
    prepared_training_config = strip_completed_run_artifact_metadata(base_training_config)

    experiment_dictionary = prepared_training_config["experiment"]
    metadata_dictionary = prepared_training_config.setdefault("metadata", {})
    paths_dictionary = prepared_training_config["paths"]

    base_model_family = str(experiment_dictionary["model_family"]).strip().lower()
    base_run_name = str(experiment_dictionary["run_name"]).strip()
    variant_model_family = build_variant_model_family(base_model_family, training_variant)
    variant_run_name = build_variant_run_name(base_run_name, training_variant)

    experiment_dictionary["model_family"] = variant_model_family
    experiment_dictionary["run_name"] = variant_run_name
    paths_dictionary["dataset_config_path"] = dataset_config_relative_path.replace("\\", "/")
    paths_dictionary["output_root"] = f"output/training_runs/{variant_model_family}"

    metadata_dictionary["base_model_family"] = base_model_family
    metadata_dictionary["training_variant"] = training_variant
    metadata_dictionary["direction_scope_label"] = variant_specification["direction_scope_label"]
    metadata_dictionary["use_forward_direction"] = variant_specification["use_forward_direction"]
    metadata_dictionary["use_backward_direction"] = variant_specification["use_backward_direction"]
    metadata_dictionary["campaign_name"] = campaign_name
    metadata_dictionary["planning_report_path"] = planning_report_relative_path.replace("\\", "/")
    metadata_dictionary["phase_name"] = phase_name
    metadata_dictionary["campaign_config_id"] = campaign_config_id
    metadata_dictionary["notes"] = (
        f"{str(metadata_dictionary.get('notes', '')).strip()} {note_suffix}".strip()
    )
    return prepared_training_config
