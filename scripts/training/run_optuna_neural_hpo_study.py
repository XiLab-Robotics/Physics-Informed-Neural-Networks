"""Execute one persisted Optuna study against the repository neural trainers."""

from __future__ import annotations

# Import Python Utilities
import argparse
import gc
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Optuna Utilities
import optuna

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities That Do Not Pull Torch Before GPU Pinning
from scripts.tooling import repository_path_support
from scripts.training import optuna_hpo_support


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Run one persisted Optuna study for a repository neural family."
    )
    argument_parser.add_argument(
        "--study-config-path",
        type=Path,
        required=True,
        help="Path to the Optuna study YAML configuration.",
    )
    argument_parser.add_argument(
        "--gpu-id",
        default="",
        help="Optional single GPU id exposed through CUDA_VISIBLE_DEVICES.",
    )
    argument_parser.add_argument(
        "--dataset",
        choices=["polished_dataset", "simplified_dataset"],
        default="polished_dataset",
        help="Dataset selector applied to every generated trial config.",
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser.parse_args()


def configure_gpu_visibility(gpu_id_text: str) -> None:

    """Pin the current process to one requested GPU before importing torch."""

    normalized_gpu_id_text = str(gpu_id_text).strip()
    if normalized_gpu_id_text == "":
        return
    os.environ["CUDA_VISIBLE_DEVICES"] = normalized_gpu_id_text


def resolve_objective_metric(
    metrics_snapshot_dictionary: dict[str, Any],
    metric_name: str,
) -> float:

    """Resolve one scalar objective metric from the saved metrics snapshot."""

    validation_metric_dictionary = metrics_snapshot_dictionary.get("validation_metrics", {})
    test_metric_dictionary = metrics_snapshot_dictionary.get("test_metrics", {})
    comparison_payload = metrics_snapshot_dictionary.get("comparison_payload", {})

    for candidate_dictionary in [
        validation_metric_dictionary,
        test_metric_dictionary,
        comparison_payload,
    ]:
        if isinstance(candidate_dictionary, dict) and metric_name in candidate_dictionary:
            return float(candidate_dictionary[metric_name])

    raise KeyError(f"Objective metric not found in metrics snapshot | {metric_name}")


def build_trial_training_config(
    base_training_config: dict[str, Any],
    study_config_dictionary: dict[str, Any],
    sampled_parameter_dictionary: dict[str, Any],
    trial_number: int,
    shared_training_infrastructure: Any,
) -> dict[str, Any]:

    """Build one prepared training configuration for a single Optuna trial."""

    study_dictionary = study_config_dictionary["study"]
    execution_dictionary = study_config_dictionary.get("execution", {})
    metadata_dictionary = base_training_config.setdefault("metadata", {})

    trial_training_config = optuna_hpo_support.apply_sampled_parameter_dictionary(
        base_training_config,
        sampled_parameter_dictionary,
    )

    # Preserve The Canonical Family Scope But Make The Trial Identity Explicit
    trial_suffix = optuna_hpo_support.build_trial_suffix(trial_number)
    experiment_dictionary = trial_training_config["experiment"]
    trial_run_name = f"{experiment_dictionary['run_name']}_{trial_suffix}"
    experiment_dictionary["run_name"] = trial_run_name

    # Apply Explicit Runtime Overrides for GPU-Preferred Neural Trials
    runtime_dictionary = trial_training_config.setdefault("runtime", {})
    if "accelerator" in execution_dictionary:
        runtime_dictionary["accelerator"] = execution_dictionary["accelerator"]
    if "devices" in execution_dictionary:
        runtime_dictionary["devices"] = execution_dictionary["devices"]
    if "precision" in execution_dictionary:
        runtime_dictionary["precision"] = execution_dictionary["precision"]
    if "benchmark" in execution_dictionary:
        runtime_dictionary["benchmark"] = execution_dictionary["benchmark"]
    if "use_non_blocking_transfer" in execution_dictionary:
        runtime_dictionary["use_non_blocking_transfer"] = execution_dictionary["use_non_blocking_transfer"]

    dataset_dictionary = trial_training_config.setdefault("dataset", {})
    if "dataset_num_workers" in execution_dictionary:
        dataset_dictionary["num_workers"] = int(execution_dictionary["dataset_num_workers"])
    if "dataset_pin_memory" in execution_dictionary:
        dataset_dictionary["pin_memory"] = bool(execution_dictionary["dataset_pin_memory"])

    # Attach Study Metadata Before Preparing Immutable Artifact Identity
    trial_metadata_dictionary = trial_training_config.setdefault("metadata", {})
    trial_metadata_dictionary["campaign_name"] = study_dictionary["campaign_name"]
    trial_metadata_dictionary["planning_report_path"] = study_dictionary["planning_report_path"]
    trial_metadata_dictionary["phase_name"] = study_dictionary["phase_name"]
    trial_metadata_dictionary["hpo_engine"] = "optuna"
    trial_metadata_dictionary["hpo_study_name"] = study_dictionary["study_name"]
    trial_metadata_dictionary["hpo_trial_number"] = int(trial_number)
    trial_metadata_dictionary["hpo_objective_metric"] = study_dictionary["objective_metric_name"]
    trial_metadata_dictionary["notes"] = (
        f"{str(metadata_dictionary.get('notes', '')).strip()} "
        f"Optuna trial {trial_number} under study `{study_dictionary['study_name']}`."
    ).strip()

    return shared_training_infrastructure.prepare_output_artifact_training_config(
        trial_training_config,
    )


def save_trial_result_snapshot(
    study_output_root: Path,
    trial_number: int,
    payload: dict[str, Any],
) -> None:

    """Persist one per-trial result snapshot under the study output root."""

    trial_result_path = study_output_root / "trial_results" / f"trial_{trial_number:04d}.yaml"
    optuna_hpo_support.save_yaml_dictionary(payload, trial_result_path)


def main() -> None:

    """Run the Optuna study execution entry point."""

    command_line_arguments = parse_command_line_arguments()
    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(command_line_arguments)
    )
    configure_gpu_visibility(command_line_arguments.gpu_id)

    # Import Torch-Dependent Repository Modules Only After GPU Pinning
    from scripts.training import shared_training_infrastructure
    from scripts.training import train_feedforward_network

    study_config_path = command_line_arguments.study_config_path.resolve()
    study_config_dictionary = optuna_hpo_support.load_yaml_dictionary(study_config_path)
    study_dictionary = study_config_dictionary["study"]
    search_space_dictionary = study_config_dictionary["search_space"]
    source_training_config_path = (PROJECT_PATH / study_dictionary["source_training_config_path"]).resolve()
    base_training_config = optuna_hpo_support.load_yaml_dictionary(source_training_config_path)
    base_training_config = shared_training_infrastructure.apply_dataset_override(
        base_training_config,
        command_line_arguments.dataset,
    )
    study_output_root = (PROJECT_PATH / study_dictionary["study_output_root"]).resolve()
    study_output_root.mkdir(parents=True, exist_ok=True)

    storage_path = (PROJECT_PATH / study_dictionary["storage_relative_path"]).resolve()
    storage_url = optuna_hpo_support.build_sqlite_storage_url(storage_path)
    sampler = optuna_hpo_support.build_optuna_sampler(study_dictionary.get("sampler", {}))
    study = optuna.create_study(
        study_name=str(study_dictionary["study_name"]),
        storage=storage_url,
        sampler=sampler,
        direction=str(study_dictionary.get("direction", "minimize")),
        load_if_exists=True,
    )

    objective_metric_name = str(study_dictionary["objective_metric_name"])
    trial_budget = int(study_dictionary["trial_budget"])
    completed_or_failed_trial_count = len(study.trials)
    remaining_trial_budget = max(trial_budget - completed_or_failed_trial_count, 0)

    def objective(trial: optuna.trial.Trial) -> float:

        sampled_parameter_dictionary = optuna_hpo_support.sample_parameter_dictionary(
            trial,
            search_space_dictionary,
        )
        prepared_training_config = build_trial_training_config(
            optuna_hpo_support.clone_dictionary(base_training_config),
            study_config_dictionary,
            sampled_parameter_dictionary,
            trial.number,
            shared_training_infrastructure,
        )
        run_instance_id = shared_training_infrastructure.resolve_run_instance_id(prepared_training_config)
        output_directory = shared_training_infrastructure.resolve_output_directory(prepared_training_config)
        trial_config_path = study_output_root / "trial_configs" / f"trial_{trial.number:04d}.yaml"
        optuna_hpo_support.save_yaml_dictionary(prepared_training_config, trial_config_path)

        print(
            f"[HPO] Study {study_dictionary['study_name']} | Trial {trial.number} | "
            f"Run {prepared_training_config['experiment']['run_name']}",
            flush=True,
        )
        train_feedforward_network.train_feedforward_network(trial_config_path)

        metrics_snapshot_path = output_directory / shared_training_infrastructure.COMMON_METRICS_FILENAME
        metrics_snapshot_dictionary = optuna_hpo_support.load_yaml_dictionary(metrics_snapshot_path)
        objective_value = resolve_objective_metric(metrics_snapshot_dictionary, objective_metric_name)
        serialized_parameter_dictionary = optuna_hpo_support.serialize_trial_parameter_dictionary(
            sampled_parameter_dictionary
        )

        trial.set_user_attr("run_instance_id", run_instance_id)
        trial.set_user_attr("run_name", prepared_training_config["experiment"]["run_name"])
        trial.set_user_attr("trial_config_path", str(trial_config_path.relative_to(PROJECT_PATH)).replace("\\", "/"))
        trial.set_user_attr("output_directory", str(output_directory.relative_to(PROJECT_PATH)).replace("\\", "/"))
        trial.set_user_attr("val_mae", float(metrics_snapshot_dictionary["validation_metrics"]["val_mae"]))
        trial.set_user_attr("test_mae", float(metrics_snapshot_dictionary["test_metrics"]["test_mae"]))
        trial.set_user_attr("sampled_parameters", serialized_parameter_dictionary)

        save_trial_result_snapshot(
            study_output_root,
            trial.number,
            {
                "study_name": study_dictionary["study_name"],
                "trial_number": int(trial.number),
                "completed_at": datetime.now().isoformat(timespec="seconds"),
                "objective_metric_name": objective_metric_name,
                "objective_value": float(objective_value),
                "run_instance_id": run_instance_id,
                "run_name": prepared_training_config["experiment"]["run_name"],
                "trial_config_path": str(trial_config_path.relative_to(PROJECT_PATH)).replace("\\", "/"),
                "output_directory": str(output_directory.relative_to(PROJECT_PATH)).replace("\\", "/"),
                "sampled_parameters": serialized_parameter_dictionary,
            },
        )

        gc.collect()
        return float(objective_value)

    if remaining_trial_budget > 0:
        study.optimize(
            objective,
            n_trials=remaining_trial_budget,
            gc_after_trial=True,
            show_progress_bar=False,
            catch=(Exception,),
        )

    completed_trial_list = [trial for trial in study.trials if trial.state == optuna.trial.TrialState.COMPLETE]
    if len(completed_trial_list) == 0:
        raise RuntimeError(
            f"Optuna study finished without any completed trials | {study.study_name}"
        )

    best_trial = study.best_trial
    optuna_hpo_support.save_yaml_dictionary(
        {
            "study_name": study.study_name,
            "storage_relative_path": str(storage_path.relative_to(PROJECT_PATH)).replace("\\", "/"),
            "direction": study.direction.name.lower(),
            "trial_budget": trial_budget,
            "completed_trials": len(study.trials),
            "successful_trials": len(completed_trial_list),
            "best_trial_number": int(best_trial.number),
            "best_value": float(best_trial.value),
            "objective_metric_name": objective_metric_name,
            "best_parameters": optuna_hpo_support.serialize_trial_parameter_dictionary(best_trial.params),
            "best_user_attributes": dict(best_trial.user_attrs),
        },
        study_output_root / "best_trial.yaml",
    )
    optuna_hpo_support.save_yaml_dictionary(
        {
            "study_name": study.study_name,
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "trial_budget": trial_budget,
            "completed_trials": len(study.trials),
            "successful_trials": len(completed_trial_list),
            "best_trial_number": int(best_trial.number),
            "best_value": float(best_trial.value),
            "objective_metric_name": objective_metric_name,
            "study_output_root": str(study_output_root.relative_to(PROJECT_PATH)).replace("\\", "/"),
            "storage_relative_path": str(storage_path.relative_to(PROJECT_PATH)).replace("\\", "/"),
        },
        study_output_root / "study_summary.yaml",
    )
    print(f"[DONE] Optuna study completed | {study.study_name}", flush=True)


if __name__ == "__main__":

    main()
