"""Close out the completed Wave 1 directional HPO campaign."""

from __future__ import annotations

# Import Python Utilities
import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

PROJECT_PATH = Path(__file__).resolve().parents[4]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.reports.closeout.wave1 import closeout_wave1_directional_retraining_campaign as wave1_export_support
from scripts.tooling import repository_path_support
from scripts.training import shared_training_infrastructure

CAMPAIGN_NAME = "wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11"
GRID_CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "training_campaigns"
    / "2026-05-11-20-07-44_wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_1"
)
OPTUNA_CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "training_campaigns"
    / "wave1"
    / "directional_best_hyperparameter_search"
    / CAMPAIGN_NAME
)
OPTUNA_STUDY_ROOT = OPTUNA_CAMPAIGN_OUTPUT_DIRECTORY / "optuna_studies"
CAMPAIGN_RESULTS_ROOT = PROJECT_PATH / "doc" / "reports" / "campaign_results" / "wave1"
CAMPAIGN_RESULTS_REPORT_PATH = (
    CAMPAIGN_RESULTS_ROOT
    / "2026-05-17-11-40-42_wave1_directional_best_hyperparameter_search_campaign_results_report.md"
)
MASTER_SUMMARY_PATH = PROJECT_PATH / "doc" / "reports" / "analysis" / "Training Results Master Summary.md"
WAVE1_CLOSEOUT_STATUS_PATH = PROJECT_PATH / "doc" / "reports" / "analysis" / "Wave 1 - Closeout Status.md"
DOC_INDEX_PATH = PROJECT_PATH / "doc" / "README.md"
MODELS_ROOT_README_PATH = PROJECT_PATH / "models" / "README.md"
EXPORTED_MODELS_ROOT = PROJECT_PATH / "models" / "exported"
EXPORTED_MODELS_README_PATH = EXPORTED_MODELS_ROOT / "README.md"
EXPORTED_MODELS_INVENTORY_PATH = EXPORTED_MODELS_ROOT / "wave1_directional_hpo_export_inventory.yaml"
TREE_MODEL_TYPE_SET = {"random_forest", "hist_gradient_boosting"}
NATIVE_TREE_EXTENSION = ".pkl"
NATIVE_TORCH_EXTENSION = ".ckpt"

SURFACE_LIST = [
    {"base_family": "tree", "family_key": "tree", "scope_name": "global", "variant": "global", "engine": "bounded_grid"},
    {"base_family": "tree", "family_key": "tree_fw", "scope_name": "forward", "variant": "Fw", "engine": "bounded_grid"},
    {"base_family": "tree", "family_key": "tree_bw", "scope_name": "backward", "variant": "Bw", "engine": "bounded_grid"},
    {"base_family": "harmonic_regression", "family_key": "harmonic_regression", "scope_name": "global", "variant": "global", "engine": "bounded_grid"},
    {"base_family": "harmonic_regression", "family_key": "harmonic_regression_fw", "scope_name": "forward", "variant": "Fw", "engine": "bounded_grid"},
    {"base_family": "harmonic_regression", "family_key": "harmonic_regression_bw", "scope_name": "backward", "variant": "Bw", "engine": "bounded_grid"},
    {"base_family": "feedforward", "family_key": "feedforward", "scope_name": "global", "variant": "global", "engine": "optuna"},
    {"base_family": "feedforward", "family_key": "feedforward_fw", "scope_name": "forward", "variant": "Fw", "engine": "optuna"},
    {"base_family": "feedforward", "family_key": "feedforward_bw", "scope_name": "backward", "variant": "Bw", "engine": "optuna"},
    {"base_family": "periodic_mlp", "family_key": "periodic_mlp", "scope_name": "global", "variant": "global", "engine": "optuna"},
    {"base_family": "periodic_mlp", "family_key": "periodic_mlp_fw", "scope_name": "forward", "variant": "Fw", "engine": "optuna"},
    {"base_family": "periodic_mlp", "family_key": "periodic_mlp_bw", "scope_name": "backward", "variant": "Bw", "engine": "optuna"},
    {"base_family": "residual_harmonic_mlp", "family_key": "residual_harmonic_mlp", "scope_name": "global", "variant": "global", "engine": "optuna"},
    {"base_family": "residual_harmonic_mlp", "family_key": "residual_harmonic_mlp_fw", "scope_name": "forward", "variant": "Fw", "engine": "optuna"},
    {"base_family": "residual_harmonic_mlp", "family_key": "residual_harmonic_mlp_bw", "scope_name": "backward", "variant": "Bw", "engine": "optuna"},
]


def parse_command_line_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Close out the Wave 1 directional best-hyperparameter campaign."
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser.parse_args()


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:
    """Load one YAML dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def save_yaml_dictionary(output_path: Path, payload: dict[str, Any]) -> None:
    """Persist one YAML dictionary."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=True)


def write_text_file(output_path: Path, text: str) -> None:
    """Write one UTF-8 text file with a single final newline."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    output_path.write_text(text, encoding="utf-8", newline="\n")


def format_relative_path(path_value: Path | str) -> str:
    """Format a repository-relative path when possible."""

    return shared_training_infrastructure.format_project_relative_path(path_value)


def resolve_project_path(path_value: Path | str) -> Path:
    """Resolve one repository-relative or absolute path."""

    return shared_training_infrastructure.resolve_runtime_project_relative_path(str(path_value))


def load_metrics_entry_from_output_directory(output_directory: Path) -> dict[str, Any]:
    """Build a registry-style entry from one training output directory."""

    metrics_path = output_directory / shared_training_infrastructure.COMMON_METRICS_FILENAME
    metrics_snapshot = load_yaml_dictionary(metrics_path)
    registry_entry = shared_training_infrastructure.build_registry_entry(metrics_snapshot)
    return normalize_registry_entry_paths(registry_entry, output_directory)


def normalize_registry_entry_paths(registry_entry: dict[str, Any], output_directory: Path) -> dict[str, Any]:
    """Normalize one registry-style entry to local repository-relative paths."""

    local_output_directory = output_directory.resolve()
    registry_entry["output_directory"] = format_relative_path(local_output_directory)
    registry_entry["metrics_path"] = format_relative_path(
        local_output_directory / shared_training_infrastructure.COMMON_METRICS_FILENAME
    )
    registry_entry["report_path"] = format_relative_path(local_output_directory / "training_test_report.md")

    best_checkpoint_pointer_path = local_output_directory / "best_checkpoint_path.txt"
    if best_checkpoint_pointer_path.exists():
        checkpoint_text = best_checkpoint_pointer_path.read_text(encoding="utf-8").strip()
        checkpoint_candidate = Path(checkpoint_text)
        if not checkpoint_candidate.is_absolute():
            checkpoint_candidate = PROJECT_PATH / checkpoint_candidate
        if not checkpoint_candidate.exists():
            checkpoint_candidate = local_output_directory / "checkpoints" / checkpoint_candidate.name
        registry_entry["best_checkpoint_path"] = format_relative_path(checkpoint_candidate)
    else:
        model_type = str(registry_entry["model_type"]).strip().lower()
        if model_type in TREE_MODEL_TYPE_SET:
            registry_entry["best_checkpoint_path"] = format_relative_path(local_output_directory / "tree_model.pkl")
        else:
            checkpoint_path_list = sorted((local_output_directory / "checkpoints").glob("*.ckpt"))
            assert checkpoint_path_list, f"Missing checkpoint under {local_output_directory}"
            best_checkpoint_path = next(
                (path for path in checkpoint_path_list if path.name != "last.ckpt"),
                checkpoint_path_list[0],
            )
            registry_entry["best_checkpoint_path"] = format_relative_path(best_checkpoint_path)
    return registry_entry


def load_family_registry_best_entry(family_key: str) -> dict[str, Any]:
    """Load the canonical family-best entry for one family surface."""

    registry_entry = wave1_export_support.load_family_best_entry(family_key)
    output_directory = resolve_project_path(str(registry_entry["output_directory"]))
    return normalize_registry_entry_paths(registry_entry, output_directory)


def resolve_hpo_surface_entry(surface: dict[str, str]) -> dict[str, Any]:
    """Resolve the HPO-selected winner entry for one surface."""

    if surface["engine"] == "bounded_grid":
        return load_family_registry_best_entry(surface["family_key"])

    best_trial_path = OPTUNA_STUDY_ROOT / surface["family_key"] / "best_trial.yaml"
    best_trial_dictionary = load_yaml_dictionary(best_trial_path)
    user_attributes = best_trial_dictionary["best_user_attributes"]
    output_directory = resolve_project_path(str(user_attributes["output_directory"]))
    registry_entry = load_metrics_entry_from_output_directory(output_directory)
    registry_entry["hpo_best_trial_number"] = int(best_trial_dictionary["best_trial_number"])
    registry_entry["hpo_best_value"] = float(best_trial_dictionary["best_value"])
    registry_entry["hpo_objective_metric_name"] = str(best_trial_dictionary["objective_metric_name"])
    registry_entry["hpo_successful_trials"] = int(best_trial_dictionary["successful_trials"])
    registry_entry["hpo_completed_trials"] = int(best_trial_dictionary["completed_trials"])
    registry_entry["hpo_best_parameters"] = dict(best_trial_dictionary["best_parameters"])
    return registry_entry


def load_training_config_from_entry(registry_entry: dict[str, Any]) -> dict[str, Any]:
    """Load the immutable training config for one winner entry."""

    output_directory = resolve_project_path(str(registry_entry["output_directory"]))
    return shared_training_infrastructure.load_training_config(
        output_directory / shared_training_infrastructure.COMMON_TRAINING_CONFIG_FILENAME
    )


def load_metrics_from_entry(registry_entry: dict[str, Any]) -> dict[str, Any]:
    """Load the metrics snapshot for one winner entry."""

    return load_yaml_dictionary(resolve_project_path(str(registry_entry["metrics_path"])))


def extract_bounded_grid_hyperparameters(training_config: dict[str, Any]) -> dict[str, Any]:
    """Extract bounded-grid hyperparameters from one selected config."""

    model_dictionary = training_config.get("model", {})
    dataset_dictionary = training_config.get("dataset", {})
    training_dictionary = training_config.get("training", {})
    candidate_dictionary = {
        "model.max_depth": model_dictionary.get("max_depth"),
        "model.learning_rate": model_dictionary.get("learning_rate"),
        "model.min_samples_leaf": model_dictionary.get("min_samples_leaf"),
        "model.harmonic_order": model_dictionary.get("harmonic_order"),
        "training.learning_rate": training_dictionary.get("learning_rate"),
        "dataset.point_stride": dataset_dictionary.get("point_stride"),
    }
    return {
        key: value
        for key, value in candidate_dictionary.items()
        if value is not None
    }


def resolve_native_artifact_contract(registry_entry: dict[str, Any]) -> dict[str, Any]:
    """Verify the Python-native artifact for one selected winner."""

    model_type = str(registry_entry["model_type"]).strip().lower()
    artifact_path = resolve_project_path(str(registry_entry["best_checkpoint_path"]))
    expected_extension = NATIVE_TREE_EXTENSION if model_type in TREE_MODEL_TYPE_SET else NATIVE_TORCH_EXTENSION
    status = artifact_path.exists() and artifact_path.suffix.lower() == expected_extension
    return {
        "native_model_path": format_relative_path(artifact_path),
        "native_model_extension": artifact_path.suffix.lower(),
        "expected_native_extension": expected_extension,
        "native_model_exists": artifact_path.exists(),
        "native_model_status": "ok" if status else "mismatch",
    }


def copy_source_run_bundle(scope_root: Path, registry_entry: dict[str, Any]) -> dict[str, str]:
    """Copy source-run provenance snapshots into one export scope."""

    source_output_directory = resolve_project_path(str(registry_entry["output_directory"]))
    run_instance_id = str(registry_entry["run_instance_id"])
    source_run_root = scope_root / "source_runs" / run_instance_id
    source_run_root.mkdir(parents=True, exist_ok=True)

    copied_path_map: dict[str, str] = {}
    source_target_dictionary = {
        "training_config.snapshot.yaml": source_output_directory / "training_config.yaml",
        "metrics_summary.snapshot.yaml": source_output_directory / "metrics_summary.yaml",
        "run_metadata.snapshot.yaml": source_output_directory / "run_metadata.yaml",
        "training_test_report.snapshot.md": source_output_directory / "training_test_report.md",
    }
    optional_checkpoint_pointer = source_output_directory / "best_checkpoint_path.txt"
    if optional_checkpoint_pointer.exists():
        source_target_dictionary["best_checkpoint_path.snapshot.txt"] = optional_checkpoint_pointer

    for target_name, source_path in source_target_dictionary.items():
        assert source_path.exists(), f"Expected source snapshot | {source_path}"
        target_path = source_run_root / target_name
        if source_path.suffix.lower() in [".md", ".txt"]:
            write_text_file(target_path, source_path.read_text(encoding="utf-8"))
        else:
            shutil.copy2(source_path, target_path)
        copied_path_map[target_name] = format_relative_path(target_path)
    return copied_path_map


def write_dataset_snapshot(scope_root: Path, surface: dict[str, str], registry_entry: dict[str, Any]) -> dict[str, str]:
    """Copy dataset config and write a scope-local dataset manifest."""

    training_config = load_training_config_from_entry(registry_entry)
    metrics_snapshot = load_metrics_from_entry(registry_entry)
    data_root = scope_root / "data"
    data_root.mkdir(parents=True, exist_ok=True)
    source_dataset_config_path = resolve_project_path(str(training_config["paths"]["dataset_config_path"]))
    copied_dataset_config_path = data_root / "dataset_config.snapshot.yaml"
    shutil.copy2(source_dataset_config_path, copied_dataset_config_path)
    manifest_path = scope_root / "dataset_snapshot_manifest.yaml"
    save_yaml_dictionary(
        manifest_path,
        {
            "schema_version": 1,
            "topic": "wave1_directional_hpo_scope_dataset_snapshot",
            "base_family": surface["base_family"],
            "family_key": surface["family_key"],
            "scope_name": surface["scope_name"],
            "training_variant": surface["variant"],
            "run_name": str(registry_entry["run_name"]),
            "run_instance_id": str(registry_entry["run_instance_id"]),
            "source_dataset_config_path": format_relative_path(source_dataset_config_path),
            "copied_dataset_config_path": format_relative_path(copied_dataset_config_path),
            "dataset_split_summary": dict(metrics_snapshot["dataset_split"]),
        },
    )
    return {
        "dataset_snapshot_manifest_path": format_relative_path(manifest_path),
        "copied_dataset_config_path": format_relative_path(copied_dataset_config_path),
    }


def export_surface_model(surface: dict[str, str], registry_entry: dict[str, Any]) -> dict[str, Any]:
    """Refresh one curated exported-model scope."""

    scope_root = EXPORTED_MODELS_ROOT / surface["base_family"] / surface["scope_name"]
    if scope_root.exists():
        shutil.rmtree(scope_root)
    python_root = scope_root / "python"
    onnx_root = scope_root / "onnx"
    python_root.mkdir(parents=True, exist_ok=True)
    onnx_root.mkdir(parents=True, exist_ok=True)

    training_config = load_training_config_from_entry(registry_entry)
    native_artifact_path = resolve_project_path(str(registry_entry["best_checkpoint_path"]))
    copied_native_artifact_path = python_root / native_artifact_path.name
    shutil.copy2(native_artifact_path, copied_native_artifact_path)

    onnx_output_path = onnx_root / "model.onnx"
    model_type = str(registry_entry["model_type"]).strip().lower()
    if model_type in TREE_MODEL_TYPE_SET:
        wave1_export_support.export_tree_model_to_onnx(registry_entry, training_config, onnx_output_path)
    else:
        wave1_export_support.export_neural_model_to_onnx(registry_entry, training_config, onnx_output_path)

    source_run_snapshot_path_map = copy_source_run_bundle(scope_root, registry_entry)
    dataset_snapshot_bundle = write_dataset_snapshot(scope_root, surface, registry_entry)
    reference_inventory_path = scope_root / "reference_inventory.yaml"
    save_yaml_dictionary(
        reference_inventory_path,
        {
            "schema_version": 1,
            "topic": "wave1_directional_hpo_export_reference_inventory",
            "base_family": surface["base_family"],
            "family_key": surface["family_key"],
            "scope_name": surface["scope_name"],
            "training_variant": surface["variant"],
            "search_engine": surface["engine"],
            "run_name": str(registry_entry["run_name"]),
            "run_instance_id": str(registry_entry["run_instance_id"]),
            "model_type": str(registry_entry["model_type"]),
            "val_mae": float(registry_entry["val_mae"]),
            "test_mae": float(registry_entry["test_mae"]),
            "test_rmse": float(registry_entry["test_rmse"]),
            "python_model_path": format_relative_path(copied_native_artifact_path),
            "onnx_model_path": format_relative_path(onnx_output_path),
            "source_output_directory": str(registry_entry["output_directory"]),
            "source_best_checkpoint_path": str(registry_entry["best_checkpoint_path"]),
            "dataset_snapshot_manifest_path": dataset_snapshot_bundle["dataset_snapshot_manifest_path"],
            "source_run_snapshot_path_map": source_run_snapshot_path_map,
        },
    )

    write_text_file(
        scope_root / "README.md",
        "\n".join(
            [
                f"# {surface['base_family']} {surface['scope_name'].capitalize()} HPO Export Archive",
                "",
                "This folder stores the curated `Wave 1` directional HPO winner for",
                "one family and one training scope.",
                "",
                "## Winner Summary",
                "",
                f"- Base Family: `{surface['base_family']}`",
                f"- Family Key: `{surface['family_key']}`",
                f"- Scope: `{surface['scope_name']}`",
                f"- Search Engine: `{surface['engine']}`",
                f"- Run Name: `{registry_entry['run_name']}`",
                f"- Run Instance Id: `{registry_entry['run_instance_id']}`",
                f"- Model Type: `{registry_entry['model_type']}`",
                f"- Validation MAE: `{float(registry_entry['val_mae']):.6f} deg`",
                f"- Test MAE: `{float(registry_entry['test_mae']):.6f} deg`",
                "",
                "## Archive Contents",
                "",
                f"- Python-native artifact: `{format_relative_path(copied_native_artifact_path)}`",
                f"- ONNX artifact: `{format_relative_path(onnx_output_path)}`",
                f"- Reference inventory: `{format_relative_path(reference_inventory_path)}`",
                f"- Dataset provenance: `{dataset_snapshot_bundle['dataset_snapshot_manifest_path']}`",
            ]
        ),
    )

    onnx_status = onnx_output_path.exists() and onnx_output_path.stat().st_size > 0
    return {
        "base_family": surface["base_family"],
        "family_key": surface["family_key"],
        "scope_name": surface["scope_name"],
        "training_variant": surface["variant"],
        "search_engine": surface["engine"],
        "run_name": str(registry_entry["run_name"]),
        "run_instance_id": str(registry_entry["run_instance_id"]),
        "model_type": str(registry_entry["model_type"]),
        "val_mae": float(registry_entry["val_mae"]),
        "test_mae": float(registry_entry["test_mae"]),
        "test_rmse": float(registry_entry["test_rmse"]),
        "python_model_path": format_relative_path(copied_native_artifact_path),
        "onnx_model_path": format_relative_path(onnx_output_path),
        "onnx_model_exists": onnx_output_path.exists(),
        "onnx_model_size_bytes": onnx_output_path.stat().st_size if onnx_output_path.exists() else 0,
        "onnx_model_status": "ok" if onnx_status else "missing_or_empty",
        "reference_inventory_path": format_relative_path(reference_inventory_path),
        "dataset_snapshot_manifest_path": dataset_snapshot_bundle["dataset_snapshot_manifest_path"],
    }


def build_surface_record(surface: dict[str, str]) -> dict[str, Any]:
    """Build one closeout record for one surface."""

    registry_entry = resolve_hpo_surface_entry(surface)
    training_config = load_training_config_from_entry(registry_entry)
    native_contract = resolve_native_artifact_contract(registry_entry)
    best_hyperparameters = (
        dict(registry_entry["hpo_best_parameters"])
        if "hpo_best_parameters" in registry_entry
        else extract_bounded_grid_hyperparameters(training_config)
    )
    archive_record = export_surface_model(surface, registry_entry)
    family_best_entry = load_family_registry_best_entry(surface["family_key"])
    is_canonical_family_best = (
        str(family_best_entry["run_instance_id"]) == str(registry_entry["run_instance_id"])
    )
    return {
        **surface,
        "registry_entry": registry_entry,
        "best_hyperparameters": best_hyperparameters,
        "has_best_hyperparameters": bool(best_hyperparameters),
        "native_contract": native_contract,
        "archive_record": archive_record,
        "is_canonical_family_best": is_canonical_family_best,
        "canonical_family_best_run_instance_id": str(family_best_entry["run_instance_id"]),
    }


def build_hyperparameter_table(surface_record_list: list[dict[str, Any]]) -> list[str]:
    """Build the best-hyperparameter table."""

    line_list = [
        "| Family | Scope | Engine | Best Run | Best Hyperparameters | Canonical Family Best? |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for record in surface_record_list:
        parameter_text = "; ".join(
            f"{key}={value}" for key, value in record["best_hyperparameters"].items()
        )
        line_list.append(
            f"| `{record['family_key']}` | "
            f"`{record['scope_name']}` | "
            f"`{record['engine']}` | "
            f"`{record['registry_entry']['run_name']}` | "
            f"`{parameter_text}` | "
            f"`{record['is_canonical_family_best']}` |"
        )
    return line_list


def build_artifact_table(surface_record_list: list[dict[str, Any]]) -> list[str]:
    """Build the artifact verification table."""

    line_list = [
        "| Family | Scope | Native Format | Native Status | ONNX Status | ONNX Size [B] |",
        "| --- | --- | --- | --- | --- | ---: |",
    ]
    for record in surface_record_list:
        native_contract = record["native_contract"]
        archive_record = record["archive_record"]
        line_list.append(
            f"| `{record['family_key']}` | "
            f"`{record['scope_name']}` | "
            f"`{native_contract['expected_native_extension']}` | "
            f"`{native_contract['native_model_status']}` | "
            f"`{archive_record['onnx_model_status']}` | "
            f"{int(archive_record['onnx_model_size_bytes'])} |"
        )
    return line_list


def build_ranking_table(surface_record_list: list[dict[str, Any]]) -> list[str]:
    """Build a ranking table using test MAE."""

    ranked_record_list = sorted(
        surface_record_list,
        key=lambda record: (
            float(record["registry_entry"]["test_mae"]),
            float(record["registry_entry"]["test_rmse"]),
            float(record["registry_entry"]["val_mae"]),
        ),
    )
    line_list = [
        "| Rank | Family | Scope | Engine | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |",
        "| --- | --- | --- | --- | ---: | ---: | ---: |",
    ]
    for rank_index, record in enumerate(ranked_record_list, start=1):
        entry = record["registry_entry"]
        line_list.append(
            f"| `{rank_index}` | "
            f"`{record['family_key']}` | "
            f"`{record['scope_name']}` | "
            f"`{record['engine']}` | "
            f"{float(entry['val_mae']):.6f} | "
            f"{float(entry['test_mae']):.6f} | "
            f"{float(entry['test_rmse']):.6f} |"
        )
    return line_list


def write_export_archive_metadata(surface_record_list: list[dict[str, Any]]) -> None:
    """Write root metadata for the refreshed exported-model archive."""

    archive_entry_list = [record["archive_record"] for record in surface_record_list]
    save_yaml_dictionary(
        EXPORTED_MODELS_INVENTORY_PATH,
        {
            "schema_version": 1,
            "topic": "wave1_directional_hpo_export_archive",
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "source_campaign_name": CAMPAIGN_NAME,
            "grid_campaign_output_directory": format_relative_path(GRID_CAMPAIGN_OUTPUT_DIRECTORY),
            "optuna_campaign_output_directory": format_relative_path(OPTUNA_CAMPAIGN_OUTPUT_DIRECTORY),
            "entry_count": len(archive_entry_list),
            "entry_list": archive_entry_list,
        },
    )
    readme_line_list = [
        "# Exported Model Archive",
        "",
        "This folder stores curated deployment-facing exports copied from completed",
        "training artifacts together with provenance needed to trace each promoted",
        "winner.",
        "",
        "## Wave 1 Directional HPO Archive",
        "",
        f"- Source campaign: `{CAMPAIGN_NAME}`",
        "- Surface contract: one family folder, then `global/`, `forward/`, and `backward/`.",
        "- Each scope folder exposes both `python/` and `onnx/` copies of the HPO-selected winner.",
        f"- Machine-readable inventory: `{format_relative_path(EXPORTED_MODELS_INVENTORY_PATH)}`",
        "",
        "## Family Folders",
        "",
    ]
    for base_family in ["tree", "harmonic_regression", "feedforward", "periodic_mlp", "residual_harmonic_mlp"]:
        readme_line_list.append(f"- `{base_family}/global/`")
        readme_line_list.append(f"- `{base_family}/forward/`")
        readme_line_list.append(f"- `{base_family}/backward/`")
    write_text_file(EXPORTED_MODELS_README_PATH, "\n".join(readme_line_list))


def write_campaign_results_report(surface_record_list: list[dict[str, Any]]) -> None:
    """Write the final HPO campaign results report."""

    all_hyperparameters_available = all(record["has_best_hyperparameters"] for record in surface_record_list)
    all_native_ok = all(record["native_contract"]["native_model_status"] == "ok" for record in surface_record_list)
    all_onnx_ok = all(record["archive_record"]["onnx_model_status"] == "ok" for record in surface_record_list)
    optuna_record_list = [record for record in surface_record_list if record["engine"] == "optuna"]
    grid_record_list = [record for record in surface_record_list if record["engine"] == "bounded_grid"]

    line_list = [
        "# Wave 1 Directional Best Hyperparameter Search Campaign Results",
        "",
        "## Overview",
        "",
        f"- Campaign Name: `{CAMPAIGN_NAME}`",
        f"- Artifact Commit: `5cf40ebe2f3625f6e202237d4ed06265f5b9659c`",
        f"- Closeout Timestamp: `{datetime.now().isoformat(timespec='seconds')}`",
        f"- Bounded Grid Surfaces: `{len(grid_record_list)}`",
        f"- Optuna Surfaces: `{len(optuna_record_list)}`",
        f"- Total Surfaces: `{len(surface_record_list)}`",
        f"- Best Hyperparameters Available: `{all_hyperparameters_available}`",
        f"- Native Python Artifacts Verified: `{all_native_ok}`",
        f"- ONNX Exports Verified: `{all_onnx_ok}`",
        "",
        "The closeout combines the `6` bounded-grid `tree` and",
        "`harmonic_regression` surfaces with the `9` persisted `Optuna` neural",
        "surfaces.",
        "",
        "## Search Completion",
        "",
        "| Phase | Surface Count | Completion Evidence |",
        "| --- | ---: | --- |",
        f"| `bounded_grid` | `{len(grid_record_list)}` | `campaign_leaderboard.yaml` and family registries |",
        f"| `optuna` | `{len(optuna_record_list)}` | `best_trial.yaml`, `study_summary.yaml`, and trial result snapshots |",
        "",
        "## Best Hyperparameters",
        "",
    ]
    line_list.extend(build_hyperparameter_table(surface_record_list))
    line_list.extend(["", "## HPO Winner Ranking", ""])
    line_list.extend(build_ranking_table(surface_record_list))
    line_list.extend(["", "## Artifact Verification", ""])
    line_list.extend(build_artifact_table(surface_record_list))
    line_list.extend(
        [
            "",
            "## Export Archive",
            "",
            f"- Export Root: `{format_relative_path(EXPORTED_MODELS_ROOT)}`",
            f"- Export Inventory: `{format_relative_path(EXPORTED_MODELS_INVENTORY_PATH)}`",
            "- `tree` surfaces use `.pkl` Python artifacts.",
            "- `harmonic_regression` and neural surfaces use `.ckpt` Python artifacts.",
            "- Every surface has a refreshed `onnx/model.onnx` export in `models/exported/`.",
            "",
            "## Registry Note",
            "",
            "HPO winners and canonical family-best winners are related but not always",
            "identical. The canonical registries use the repository selection policy",
            "based on held-out test metrics, while `Optuna` selects the best trial by",
            "`val_mae`. This closeout records the HPO winners and explicitly flags",
            "whether each one is also the current canonical family-best entry.",
        ]
    )
    write_text_file(CAMPAIGN_RESULTS_REPORT_PATH, "\n".join(line_list))


def write_wave1_closeout_status(surface_record_list: list[dict[str, Any]]) -> None:
    """Refresh the canonical Wave 1 closeout status."""

    best_record = min(
        surface_record_list,
        key=lambda record: (
            float(record["registry_entry"]["test_mae"]),
            float(record["registry_entry"]["test_rmse"]),
            float(record["registry_entry"]["val_mae"]),
        ),
    )
    line_list = [
        "# Wave 1 Closeout Status And Consolidated Summary Report",
        "",
        "## Executive Summary",
        "",
        "`Wave 1` remains closed with a directional `global` / `forward` /",
        "`backward` comparison surface. The latest completed optimization pass is",
        "the directional best-hyperparameter search campaign.",
        "",
        f"- Current HPO leader: `{best_record['registry_entry']['run_name']}`",
        f"- Leader family: `{best_record['family_key']}`",
        f"- Leader scope: `{best_record['scope_name']}`",
        f"- Leader test MAE: `{float(best_record['registry_entry']['test_mae']):.6f} deg`",
        f"- Full HPO closeout report: `{format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH)}`",
        "",
        "## HPO Surface Ranking",
        "",
    ]
    line_list.extend(build_ranking_table(surface_record_list))
    write_text_file(WAVE1_CLOSEOUT_STATUS_PATH, "\n".join(line_list))


def update_doc_index() -> None:
    """Register the HPO closeout report from the doc index."""

    doc_index_text = DOC_INDEX_PATH.read_text(encoding="utf-8")
    report_relative_path = format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH)
    if report_relative_path.startswith("doc/"):
        report_relative_path = report_relative_path[4:]
    report_line = f"- [{report_relative_path}](./{report_relative_path.replace(' ', '%20')})"
    if report_line in doc_index_text:
        return
    anchor = "### Campaign Plans And Results"
    if anchor not in doc_index_text:
        write_text_file(DOC_INDEX_PATH, doc_index_text + "\n\n" + report_line + "\n")
        return
    insertion = (
        f"{anchor}\n\n"
        f"{report_line}\n"
        "  Final results report for the completed Wave 1 directional best-hyperparameter search campaign, including bounded-grid and Optuna surfaces plus refreshed Python and ONNX exports.\n"
    )
    doc_index_text = doc_index_text.replace(f"{anchor}\n", insertion, 1)
    write_text_file(DOC_INDEX_PATH, doc_index_text)


def update_models_readme() -> None:
    """Ensure models README mentions the refreshed HPO archive."""

    models_readme_text = MODELS_ROOT_README_PATH.read_text(encoding="utf-8")
    archive_line = "- `exported/<family>/<scope>/` for curated Wave 1 HPO winner archives with `python/`, `onnx/`, local inventories, and source-run provenance bundles"
    if archive_line in models_readme_text:
        return
    anchor_line = "- `exported/` for ONNX, Structured Text, or other deployment-ready exports"
    if anchor_line in models_readme_text:
        models_readme_text = models_readme_text.replace(anchor_line, f"{anchor_line}\n{archive_line}")
    else:
        models_readme_text = models_readme_text.rstrip() + "\n" + archive_line + "\n"
    write_text_file(MODELS_ROOT_README_PATH, models_readme_text)


def main() -> None:
    """Run the Wave 1 directional HPO closeout."""

    command_line_arguments = parse_command_line_arguments()
    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(command_line_arguments)
    )

    surface_record_list = [build_surface_record(surface) for surface in SURFACE_LIST]
    write_export_archive_metadata(surface_record_list)
    write_campaign_results_report(surface_record_list)
    write_wave1_closeout_status(surface_record_list)
    update_doc_index()
    update_models_readme()

    from scripts.reports.analysis.generate_training_results_master_summary import (
        generate_training_results_master_summary,
    )

    generate_training_results_master_summary(MASTER_SUMMARY_PATH)
    print(
        "[DONE] Wave 1 directional HPO closeout completed | "
        f"report={format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
