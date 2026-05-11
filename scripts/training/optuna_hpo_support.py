"""Reusable Optuna helpers for repository-owned neural HPO studies."""

from __future__ import annotations

# Import Python Utilities
from copy import deepcopy
from pathlib import Path
from typing import Any
import json

# Import Optuna Utilities
import optuna

# Import YAML Utilities
import yaml


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"YAML file must contain a dictionary | {input_path}"
    return payload


def save_yaml_dictionary(payload: dict[str, Any], output_path: Path) -> None:

    """Persist one YAML dictionary to disk."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False)


def clone_dictionary(payload: dict[str, Any]) -> dict[str, Any]:

    """Clone one nested dictionary payload."""

    return deepcopy(payload)


def resolve_nested_dictionary_value(payload: dict[str, Any], dotted_key: str) -> Any:

    """Resolve one nested dictionary value from a dotted key."""

    current_value: Any = payload
    for key_token in dotted_key.split("."):
        assert isinstance(current_value, dict), f"Cannot traverse non-dictionary payload | {dotted_key}"
        assert key_token in current_value, f"Missing nested key | {dotted_key}"
        current_value = current_value[key_token]
    return current_value


def set_nested_dictionary_value(payload: dict[str, Any], dotted_key: str, value: Any) -> None:

    """Set one nested dictionary value from a dotted key."""

    key_token_list = dotted_key.split(".")
    current_value: dict[str, Any] = payload
    for key_token in key_token_list[:-1]:
        nested_value = current_value.setdefault(key_token, {})
        assert isinstance(nested_value, dict), f"Cannot traverse non-dictionary payload | {dotted_key}"
        current_value = nested_value
    current_value[key_token_list[-1]] = value


def build_sqlite_storage_url(storage_path: Path) -> str:

    """Build one SQLite storage URL for Optuna."""

    storage_path.parent.mkdir(parents=True, exist_ok=True)
    return f"sqlite:///{storage_path.resolve().as_posix()}"


def build_optuna_sampler(sampler_dictionary: dict[str, Any]) -> optuna.samplers.BaseSampler:

    """Build one Optuna sampler from a small config dictionary."""

    sampler_type = str(sampler_dictionary.get("type", "TPESampler")).strip()
    if sampler_type == "TPESampler":
        return optuna.samplers.TPESampler(
            seed=int(sampler_dictionary.get("seed", 42)),
            n_startup_trials=int(sampler_dictionary.get("n_startup_trials", 5)),
        )
    if sampler_type == "RandomSampler":
        return optuna.samplers.RandomSampler(
            seed=int(sampler_dictionary.get("seed", 42)),
        )
    raise ValueError(f"Unsupported Optuna sampler type | {sampler_type}")


def sample_parameter_dictionary(
    trial: optuna.trial.Trial,
    search_space_dictionary: dict[str, dict[str, Any]],
) -> dict[str, Any]:

    """Sample one parameter dictionary from the configured search space."""

    sampled_parameter_dictionary: dict[str, Any] = {}

    for dotted_key, parameter_specification in search_space_dictionary.items():
        parameter_type = str(parameter_specification.get("type", "categorical")).strip()
        parameter_name = str(parameter_specification.get("name", dotted_key)).strip()

        if parameter_type == "float":
            sampled_parameter_dictionary[dotted_key] = trial.suggest_float(
                parameter_name,
                float(parameter_specification["low"]),
                float(parameter_specification["high"]),
                log=bool(parameter_specification.get("log", False)),
                step=parameter_specification.get("step"),
            )
            continue

        if parameter_type == "int":
            sampled_parameter_dictionary[dotted_key] = trial.suggest_int(
                parameter_name,
                int(parameter_specification["low"]),
                int(parameter_specification["high"]),
                log=bool(parameter_specification.get("log", False)),
                step=int(parameter_specification.get("step", 1)),
            )
            continue

        if parameter_type == "categorical":
            sampled_parameter_dictionary[dotted_key] = trial.suggest_categorical(
                parameter_name,
                list(parameter_specification["choices"]),
            )
            continue

        raise ValueError(f"Unsupported Optuna parameter type | {parameter_type} | {dotted_key}")

    return sampled_parameter_dictionary


def apply_sampled_parameter_dictionary(
    base_training_config: dict[str, Any],
    sampled_parameter_dictionary: dict[str, Any],
) -> dict[str, Any]:

    """Apply one sampled parameter dictionary to a cloned training config."""

    prepared_training_config = clone_dictionary(base_training_config)
    for dotted_key, sampled_value in sampled_parameter_dictionary.items():
        set_nested_dictionary_value(prepared_training_config, dotted_key, sampled_value)
    return prepared_training_config


def build_trial_suffix(trial_number: int) -> str:

    """Build one compact trial suffix."""

    return f"optuna_t{trial_number:04d}"


def serialize_trial_parameter_dictionary(sampled_parameter_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Convert one sampled parameter dictionary into YAML-safe scalar payloads."""

    serialized_dictionary: dict[str, Any] = {}
    for dotted_key, sampled_value in sampled_parameter_dictionary.items():
        if isinstance(sampled_value, (str, int, float, bool)) or sampled_value is None:
            serialized_dictionary[dotted_key] = sampled_value
            continue
        serialized_dictionary[dotted_key] = json.loads(json.dumps(sampled_value))
    return serialized_dictionary

