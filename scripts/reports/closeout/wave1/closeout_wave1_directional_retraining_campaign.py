"""Close out the completed Wave 1 directional retraining campaign."""

from __future__ import annotations

# Import Python Utilities
import argparse
import shutil
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Third-Party Utilities
import torch
import torch.nn as nn
import yaml

PROJECT_PATH = Path(__file__).resolve().parents[4]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.models.model_factory import create_model
from scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank import (
    exact_paper_model_bank_support,
)
from scripts.training import shared_training_infrastructure
from scripts.training import tree_regression_support
from scripts.training.transmission_error_regression_module import TransmissionErrorRegressionModule

CAMPAIGN_NAME = "wave1_directional_retraining_campaign_2026_05_06_16_07_16"
CAMPAIGN_OUTPUT_ROOT = PROJECT_PATH / "output" / "training_campaigns"
CAMPAIGN_RESULTS_ROOT = PROJECT_PATH / "doc" / "reports" / "campaign_results" / "wave1"
MASTER_SUMMARY_PATH = PROJECT_PATH / "doc" / "reports" / "analysis" / "Training Results Master Summary.md"
WAVE1_CLOSEOUT_STATUS_PATH = PROJECT_PATH / "doc" / "reports" / "analysis" / "Wave 1 - Closeout Status.md"
DOC_INDEX_PATH = PROJECT_PATH / "doc" / "README.md"
MODELS_ROOT_README_PATH = PROJECT_PATH / "models" / "README.md"
EXPORTED_MODELS_ROOT = PROJECT_PATH / "models" / "exported"
EXPORTED_MODELS_README_PATH = EXPORTED_MODELS_ROOT / "README.md"
EXPORTED_MODELS_INVENTORY_PATH = EXPORTED_MODELS_ROOT / "wave1_directional_retraining_export_inventory.yaml"
FAMILY_REGISTRY_ROOT = PROJECT_PATH / "output" / "registries" / "families"
PROGRAM_REGISTRY_PATH = PROJECT_PATH / "output" / "registries" / "program" / "current_best_solution.yaml"
TREE_MODEL_TYPE_SET = {"random_forest", "hist_gradient_boosting"}
WAVE1_BASE_FAMILY_LIST = [
    "tree",
    "residual_harmonic_mlp",
    "feedforward",
    "periodic_mlp",
    "harmonic_regression",
]
SCOPE_CONFIGURATION_LIST = [
    {
        "scope_name": "global",
        "training_variant": "global",
        "family_suffix": "",
    },
    {
        "scope_name": "forward",
        "training_variant": "Fw",
        "family_suffix": "_fw",
    },
    {
        "scope_name": "backward",
        "training_variant": "Bw",
        "family_suffix": "_bw",
    },
]
TARGET_ONNX_OPSET = 17


class RawInputPredictionExportWrapper(nn.Module):

    """Export wrapper that preserves the raw-input contract for neural models."""

    def __init__(self, regression_module: TransmissionErrorRegressionModule) -> None:
        super().__init__()
        self.regression_module = regression_module

    def forward(self, input_tensor: torch.Tensor) -> torch.Tensor:

        """Predict denormalized TE from raw five-feature input rows."""

        raw_input_tensor = input_tensor.float()
        normalized_input_tensor = self.regression_module.normalize_input_tensor(raw_input_tensor)
        normalized_prediction_tensor, _ = self.regression_module.forward_regression_model(
            raw_input_tensor,
            normalized_input_tensor,
        )
        return self.regression_module.denormalize_target_tensor(normalized_prediction_tensor)


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the closeout workflow."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Close out the completed Wave 1 directional retraining campaign, "
            "repair directional registry metadata, refresh the analysis "
            "surfaces, and archive Python plus ONNX model exports."
        )
    )
    argument_parser.add_argument(
        "--campaign-name",
        default=CAMPAIGN_NAME,
        help="Canonical campaign name whose output directory should be closed out.",
    )
    return argument_parser.parse_args()


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | path={input_path}"
    return payload


def save_yaml_dictionary(output_path: Path, payload: dict[str, Any]) -> None:

    """Persist one YAML dictionary with repository-normalized formatting."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=True)


def write_text_file(output_path: Path, text: str) -> None:

    """Write one UTF-8 text file with a normal single final newline."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    output_path.write_text(text, encoding="utf-8", newline="\n")


def format_relative_path(path_value: Path | str) -> str:

    """Format one path relative to the repository root when possible."""

    return shared_training_infrastructure.format_project_relative_path(path_value)


def resolve_campaign_output_directory(campaign_name: str) -> Path:

    """Resolve the immutable campaign output directory for one campaign name."""

    matching_path_list = sorted(CAMPAIGN_OUTPUT_ROOT.glob(f"*_{campaign_name}"))
    assert len(matching_path_list) == 1, (
        "Expected exactly one campaign output directory | "
        f"campaign_name={campaign_name} | matches={len(matching_path_list)}"
    )
    return matching_path_list[0].resolve()


def normalize_scope_name(training_variant: str) -> str:

    """Map one training variant token to the exported scope label."""

    if training_variant == "Fw":
        return "forward"
    if training_variant == "Bw":
        return "backward"
    return "global"


def build_scope_record_list() -> list[dict[str, str]]:

    """Build the canonical Wave 1 family/scope registry mapping."""

    scope_record_list: list[dict[str, str]] = []
    for base_family in WAVE1_BASE_FAMILY_LIST:
        for scope_configuration in SCOPE_CONFIGURATION_LIST:
            family_key = f"{base_family}{scope_configuration['family_suffix']}"
            scope_record_list.append(
                {
                    "base_family": base_family,
                    "scope_name": str(scope_configuration["scope_name"]),
                    "training_variant": str(scope_configuration["training_variant"]),
                    "family_key": family_key,
                }
            )
    return scope_record_list


def repair_tree_metrics_snapshot(metrics_path: Path, training_config_path: Path) -> bool:

    """Repair one tree metrics snapshot so directional metadata matches the config."""

    metrics_snapshot_dictionary = load_yaml_dictionary(metrics_path)
    training_config = shared_training_infrastructure.load_training_config(training_config_path)
    expected_training_variant_details = shared_training_infrastructure.resolve_training_variant_details(
        training_config
    )
    experiment_dictionary = metrics_snapshot_dictionary.setdefault("experiment", {})
    changed = False
    for metadata_key, expected_value in expected_training_variant_details.items():
        if experiment_dictionary.get(metadata_key) != expected_value:
            experiment_dictionary[metadata_key] = expected_value
            changed = True
    if changed:
        save_yaml_dictionary(metrics_path, metrics_snapshot_dictionary)
    return changed


def refresh_family_registries_from_manifest(manifest_dictionary: dict[str, Any]) -> list[dict[str, Any]]:

    """Rebuild family registries from the completed campaign manifest."""

    completed_registry_entry_list: list[dict[str, Any]] = []
    for run_dictionary in manifest_dictionary["run_list"]:
        if str(run_dictionary.get("queue_status", "")).strip().lower() != "completed":
            continue
        metrics_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
            str(run_dictionary["metrics_path"])
        )
        metrics_snapshot_dictionary = shared_training_infrastructure.load_yaml_snapshot(metrics_path)
        shared_training_infrastructure.update_family_registry(metrics_snapshot_dictionary)
        completed_registry_entry_list.append(
            shared_training_infrastructure.build_registry_entry(metrics_snapshot_dictionary)
        )
    return shared_training_infrastructure.sort_registry_entries(completed_registry_entry_list)


def write_campaign_registry_artifacts(
    campaign_output_directory: Path,
    campaign_name: str,
    campaign_registry_entry_list: list[dict[str, Any]],
) -> dict[str, Any]:

    """Rewrite the campaign leaderboard, best-run YAML, and best-run Markdown."""

    assert campaign_registry_entry_list, "Campaign registry entry list is empty"
    best_registry_entry = campaign_registry_entry_list[0]
    leaderboard_path = campaign_output_directory / "campaign_leaderboard.yaml"
    best_run_path = campaign_output_directory / "campaign_best_run.yaml"
    best_run_markdown_path = campaign_output_directory / "campaign_best_run.md"

    save_yaml_dictionary(
        leaderboard_path,
        {
            "schema_version": 1,
            "campaign_name": campaign_name,
            "selection_policy": dict(shared_training_infrastructure.SELECTION_POLICY_DICTIONARY),
            "updated_at": datetime.now().isoformat(timespec="seconds"),
            "entry_count": len(campaign_registry_entry_list),
            "entry_list": campaign_registry_entry_list,
        },
    )
    save_yaml_dictionary(
        best_run_path,
        {
            "schema_version": 1,
            "campaign_name": campaign_name,
            "selection_policy": dict(shared_training_infrastructure.SELECTION_POLICY_DICTIONARY),
            "updated_at": datetime.now().isoformat(timespec="seconds"),
            "best_entry": best_registry_entry,
        },
    )
    write_text_file(
        best_run_markdown_path,
        "\n".join(
            [
                "# Campaign Best Run",
                "",
                "## Overview",
                "",
                f"- Campaign Name: `{campaign_name}`",
                f"- Run Name: `{best_registry_entry['run_name']}`",
                f"- Run Instance Id: `{best_registry_entry['run_instance_id']}`",
                f"- Model Family: `{best_registry_entry['model_family']}`",
                f"- Base Model Family: `{best_registry_entry['base_model_family']}`",
                f"- Training Variant: `{best_registry_entry['training_variant']}`",
                f"- Model Type: `{best_registry_entry['model_type']}`",
                f"- Test MAE: `{best_registry_entry['test_mae']}`",
                f"- Test RMSE: `{best_registry_entry['test_rmse']}`",
                f"- Validation MAE: `{best_registry_entry['val_mae']}`",
                f"- Output Directory: `{best_registry_entry['output_directory']}`",
                f"- Metrics Snapshot: `{best_registry_entry['metrics_path']}`",
                f"- Report Path: `{best_registry_entry['report_path']}`",
                f"- Best Checkpoint Path: `{best_registry_entry['best_checkpoint_path']}`",
                "",
                "## Selection Policy",
                "",
                f"- Primary Metric: `{shared_training_infrastructure.SELECTION_POLICY_DICTIONARY['primary_metric']}`",
                f"- First Tie Breaker: `{shared_training_infrastructure.SELECTION_POLICY_DICTIONARY['first_tie_breaker']}`",
                f"- Second Tie Breaker: `{shared_training_infrastructure.SELECTION_POLICY_DICTIONARY['second_tie_breaker']}`",
                f"- Third Tie Breaker: `{shared_training_infrastructure.SELECTION_POLICY_DICTIONARY['third_tie_breaker']}`",
            ]
        ),
    )
    shared_training_infrastructure.update_program_registry(best_registry_entry)
    return best_registry_entry


def load_family_best_entry(family_key: str) -> dict[str, Any]:

    """Load the best registry entry for one canonical family key."""

    registry_path = FAMILY_REGISTRY_ROOT / family_key / shared_training_infrastructure.FAMILY_BEST_FILENAME
    registry_dictionary = load_yaml_dictionary(registry_path)
    best_entry = registry_dictionary.get("best_entry")
    assert isinstance(best_entry, dict), f"Expected best_entry dictionary | path={registry_path}"
    return best_entry


def load_training_config_from_registry_entry(registry_entry: dict[str, Any]) -> dict[str, Any]:

    """Load the immutable training config snapshot for one registry entry."""

    output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(
        str(registry_entry["output_directory"])
    )
    return shared_training_infrastructure.load_training_config(
        output_directory / shared_training_infrastructure.COMMON_TRAINING_CONFIG_FILENAME
    )


def load_neural_regression_module(
    registry_entry: dict[str, Any],
    training_config: dict[str, Any],
) -> TransmissionErrorRegressionModule:

    """Load one Lightning checkpoint plus its normalization contract."""

    datamodule, _, _, normalization_statistics = shared_training_infrastructure.initialize_training_components(
        training_config
    )
    checkpoint_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        str(registry_entry["best_checkpoint_path"])
    )
    regression_module = TransmissionErrorRegressionModule.load_from_checkpoint(
        checkpoint_path=checkpoint_path,
        regression_model=create_model(
            model_type=str(training_config["experiment"]["model_type"]),
            model_configuration=training_config["model"],
        ),
        input_feature_dim=datamodule.get_input_feature_dim(),
        target_feature_dim=datamodule.get_target_feature_dim(),
        normalization_statistics=normalization_statistics,
        map_location=torch.device("cpu"),
    )
    regression_module.to(torch.device("cpu"))
    regression_module.eval()
    return regression_module


def export_tree_model_to_onnx(
    registry_entry: dict[str, Any],
    training_config: dict[str, Any],
    onnx_output_path: Path,
) -> None:

    """Export one fitted tree estimator into ONNX format."""

    python_model_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        str(registry_entry["best_checkpoint_path"])
    )
    estimator = tree_regression_support.load_tree_model(python_model_path)
    onnx_model = exact_paper_model_bank_support._convert_estimator_to_onnx(
        estimator=estimator,
        feature_count=int(training_config["model"]["input_size"]),
        estimator_name=estimator.__class__.__name__,
        target_opset=TARGET_ONNX_OPSET,
    )
    onnx_output_path.parent.mkdir(parents=True, exist_ok=True)
    with onnx_output_path.open("wb") as output_file:
        output_file.write(onnx_model.SerializeToString())


def export_neural_model_to_onnx(
    registry_entry: dict[str, Any],
    training_config: dict[str, Any],
    onnx_output_path: Path,
) -> None:

    """Export one neural or structured-neural checkpoint into ONNX format."""

    regression_module = load_neural_regression_module(registry_entry, training_config)
    export_wrapper = RawInputPredictionExportWrapper(regression_module)
    export_wrapper.eval()

    dummy_input_tensor = regression_module.input_feature_mean.unsqueeze(0).detach().clone()
    onnx_output_path.parent.mkdir(parents=True, exist_ok=True)
    with torch.no_grad():
        export_keyword_arguments = {
            "input_names": ["input_tensor"],
            "output_names": ["prediction_tensor"],
            "dynamic_axes": {
                "input_tensor": {0: "batch_size"},
                "prediction_tensor": {0: "batch_size"},
            },
            "opset_version": TARGET_ONNX_OPSET,
            "export_params": True,
            "do_constant_folding": True,
        }
        try:
            torch.onnx.export(
                export_wrapper,
                dummy_input_tensor,
                str(onnx_output_path),
                dynamo=True,
                **export_keyword_arguments,
            )
        except ModuleNotFoundError as export_error:
            if "onnxscript" not in str(export_error):
                raise
            torch.onnx.export(
                export_wrapper,
                dummy_input_tensor,
                str(onnx_output_path),
                dynamo=False,
                **export_keyword_arguments,
            )


def refresh_export_archive(scope_record_list: list[dict[str, str]]) -> list[dict[str, Any]]:

    """Rebuild the `models/exported` Wave 1 directional archive surface."""

    archive_entry_list: list[dict[str, Any]] = []
    for scope_record in scope_record_list:
        base_family = scope_record["base_family"]
        scope_name = scope_record["scope_name"]
        family_key = scope_record["family_key"]
        registry_entry = load_family_best_entry(family_key)
        training_config = load_training_config_from_registry_entry(registry_entry)

        scope_root = EXPORTED_MODELS_ROOT / base_family / scope_name
        onnx_root = scope_root / "onnx"
        python_root = scope_root / "python"
        if scope_root.exists():
            shutil.rmtree(scope_root)
        onnx_root.mkdir(parents=True, exist_ok=True)
        python_root.mkdir(parents=True, exist_ok=True)

        source_python_model_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
            str(registry_entry["best_checkpoint_path"])
        )
        copied_python_model_path = python_root / source_python_model_path.name
        shutil.copy2(source_python_model_path, copied_python_model_path)

        onnx_output_path = onnx_root / "model.onnx"
        model_type = str(registry_entry["model_type"]).strip().lower()
        if model_type in TREE_MODEL_TYPE_SET:
            export_tree_model_to_onnx(registry_entry, training_config, onnx_output_path)
        else:
            export_neural_model_to_onnx(registry_entry, training_config, onnx_output_path)

        archive_entry_list.append(
            {
                "base_family": base_family,
                "scope_name": scope_name,
                "family_key": family_key,
                "training_variant": scope_record["training_variant"],
                "model_type": model_type,
                "run_name": str(registry_entry["run_name"]),
                "run_instance_id": str(registry_entry["run_instance_id"]),
                "test_mae": float(registry_entry["test_mae"]),
                "test_rmse": float(registry_entry["test_rmse"]),
                "val_mae": float(registry_entry["val_mae"]),
                "python_model_path": format_relative_path(copied_python_model_path),
                "onnx_model_path": format_relative_path(onnx_output_path),
                "source_output_directory": str(registry_entry["output_directory"]),
                "source_best_checkpoint_path": str(registry_entry["best_checkpoint_path"]),
            }
        )
    return archive_entry_list


def write_export_archive_metadata(
    campaign_output_directory: Path,
    archive_entry_list: list[dict[str, Any]],
) -> None:

    """Write the root exported-model README and inventory surfaces."""

    save_yaml_dictionary(
        EXPORTED_MODELS_INVENTORY_PATH,
        {
            "schema_version": 1,
            "topic": "wave1_directional_retraining_export_archive",
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "source_campaign_name": CAMPAIGN_NAME,
            "source_campaign_output_directory": format_relative_path(campaign_output_directory),
            "entry_count": len(archive_entry_list),
            "entry_list": archive_entry_list,
        },
    )

    readme_line_list = [
        "# Exported Model Archive",
        "",
        "This folder stores curated deployment-facing exports copied from completed",
        "training artifacts.",
        "",
        "## Wave 1 Directional Retraining Archive",
        "",
        f"- Source campaign: `{CAMPAIGN_NAME}`",
        f"- Source campaign output directory: `{format_relative_path(campaign_output_directory)}`",
        "- Surface contract: one family folder, then `global/`, `forward/`, and `backward/`.",
        "- Each scope folder exposes both `python/` and `onnx/` copies of the selected winner.",
        f"- Machine-readable inventory: `{format_relative_path(EXPORTED_MODELS_INVENTORY_PATH)}`",
        "",
        "## Family Folders",
        "",
    ]
    for base_family in WAVE1_BASE_FAMILY_LIST:
        readme_line_list.append(f"- `{base_family}/global/`")
        readme_line_list.append(f"- `{base_family}/forward/`")
        readme_line_list.append(f"- `{base_family}/backward/`")
    write_text_file(EXPORTED_MODELS_README_PATH, "\n".join(readme_line_list))


def build_campaign_ranking_table(campaign_registry_entry_list: list[dict[str, Any]]) -> list[str]:

    """Build the Markdown table for the full 15-run ranking."""

    line_list = [
        "| Rank | Family | Scope | Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] |",
        "| --- | --- | --- | --- | --- | ---: | ---: | ---: |",
    ]
    for rank_index, registry_entry in enumerate(campaign_registry_entry_list, start=1):
        line_list.append(
            f"| `{rank_index}` | "
            f"`{registry_entry['base_model_family']}` | "
            f"`{normalize_scope_name(str(registry_entry['training_variant']))}` | "
            f"`{registry_entry['run_name']}` | "
            f"`{registry_entry['model_type']}` | "
            f"{float(registry_entry['val_mae']):.6f} | "
            f"{float(registry_entry['test_mae']):.6f} | "
            f"{float(registry_entry['test_rmse']):.6f} |"
        )
    return line_list


def build_family_scope_table(scope_record_list: list[dict[str, str]]) -> list[str]:

    """Build the Wave 1 family-by-scope summary table."""

    row_map: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for scope_record in scope_record_list:
        registry_entry = load_family_best_entry(scope_record["family_key"])
        row_map[scope_record["base_family"]][scope_record["scope_name"]] = registry_entry

    line_list = [
        "| Family | Global Test MAE [deg] | Forward Test MAE [deg] | Backward Test MAE [deg] | Best Scope |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for base_family in WAVE1_BASE_FAMILY_LIST:
        global_entry = row_map[base_family]["global"]
        forward_entry = row_map[base_family]["forward"]
        backward_entry = row_map[base_family]["backward"]
        best_scope_name = min(
            ["global", "forward", "backward"],
            key=lambda scope_name: float(row_map[base_family][scope_name]["test_mae"]),
        )
        line_list.append(
            f"| `{base_family}` | "
            f"{float(global_entry['test_mae']):.6f} | "
            f"{float(forward_entry['test_mae']):.6f} | "
            f"{float(backward_entry['test_mae']):.6f} | "
            f"`{best_scope_name}` |"
        )
    return line_list


def build_export_archive_table(archive_entry_list: list[dict[str, Any]]) -> list[str]:

    """Build the exported-model archive inventory table."""

    line_list = [
        "| Family | Scope | Python Artifact | ONNX Artifact |",
        "| --- | --- | --- | --- |",
    ]
    for archive_entry in archive_entry_list:
        line_list.append(
            f"| `{archive_entry['base_family']}` | "
            f"`{archive_entry['scope_name']}` | "
            f"`{archive_entry['python_model_path']}` | "
            f"`{archive_entry['onnx_model_path']}` |"
        )
    return line_list


def build_campaign_results_report_markdown(
    report_timestamp: str,
    campaign_output_directory: Path,
    campaign_manifest_dictionary: dict[str, Any],
    campaign_registry_entry_list: list[dict[str, Any]],
    best_registry_entry: dict[str, Any],
    tree_repair_count: int,
    archive_entry_list: list[dict[str, Any]],
) -> str:

    """Build the final campaign-results Markdown report."""

    completed_run_count = sum(
        str(run_dictionary.get("queue_status", "")).strip().lower() == "completed"
        for run_dictionary in campaign_manifest_dictionary["run_list"]
    )
    failed_run_count = sum(
        str(run_dictionary.get("queue_status", "")).strip().lower() == "failed"
        for run_dictionary in campaign_manifest_dictionary["run_list"]
    )
    line_list = [
        "# Wave 1 Directional Retraining Campaign Results",
        "",
        "## Overview",
        "",
        f"- Campaign Name: `{CAMPAIGN_NAME}`",
        f"- Closeout Timestamp: `{report_timestamp}`",
        f"- Campaign Output Directory: `{format_relative_path(campaign_output_directory)}`",
        f"- Completed Runs: `{completed_run_count}`",
        f"- Failed Runs: `{failed_run_count}`",
        "- All `15` planned Wave 1 runs are now closed across `global`, `forward`, and `backward` variants.",
        "- The protected `doc/running/active_training_campaign.yaml` file was intentionally left untouched because it still tracks a separate `Track 1` campaign.",
        "",
        "## Closeout Actions",
        "",
        f"- Repaired directional metadata in `{tree_repair_count}` tree metrics snapshots so registry-facing artifacts now preserve `base_model_family`, `training_variant`, and direction flags consistently.",
        "- Rebuilt the affected family registries, the campaign leaderboard, the campaign best-run snapshots, and the program best registry from the repaired metrics.",
        "- Archived one ONNX export plus one Python artifact for every `Wave 1` family/scope winner under `models/exported/`.",
        "- Refreshed the canonical `Wave 1` closeout report and regenerated the training-results master summary from the updated registries.",
        "",
        "## Campaign Ranking",
        "",
    ]
    line_list.extend(build_campaign_ranking_table(campaign_registry_entry_list))
    line_list.extend(
        [
            "",
            "## Family Directional Surface",
            "",
            f"- Current campaign-best entry: `{best_registry_entry['run_name']}` from family `{best_registry_entry['model_family']}` with `test_mae = {float(best_registry_entry['test_mae']):.6f} deg`.",
            "",
        ]
    )
    line_list.extend(build_family_scope_table(build_scope_record_list()))
    line_list.extend(
        [
            "",
            "## Exported Model Archive",
            "",
            f"- Export root: `{format_relative_path(EXPORTED_MODELS_ROOT)}`",
            f"- Root inventory: `{format_relative_path(EXPORTED_MODELS_INVENTORY_PATH)}`",
            "- Each family now exposes `global/`, `forward/`, and `backward/` subfolders, each containing both `python/` and `onnx/` model copies.",
            "",
        ]
    )
    line_list.extend(build_export_archive_table(archive_entry_list))
    line_list.extend(
        [
            "",
            "## Canonical Follow-Through",
            "",
            f"- `Wave 1` summary refreshed: `{format_relative_path(WAVE1_CLOSEOUT_STATUS_PATH)}`",
            f"- master summary refreshed: `{format_relative_path(MASTER_SUMMARY_PATH)}`",
            f"- campaign leaderboard refreshed: `{format_relative_path(campaign_output_directory / 'campaign_leaderboard.yaml')}`",
            f"- campaign best run refreshed: `{format_relative_path(campaign_output_directory / 'campaign_best_run.yaml')}`",
            f"- program best registry: `{format_relative_path(PROGRAM_REGISTRY_PATH)}`",
        ]
    )
    return "\n".join(line_list)


def write_wave1_closeout_status(
    best_registry_entry: dict[str, Any],
    scope_record_list: list[dict[str, str]],
    campaign_results_report_path: Path,
) -> None:

    """Rewrite the canonical Wave 1 closeout status report for the new policy."""

    line_list = [
        "# Wave 1 Closeout Status And Consolidated Summary Report",
        "",
        "## Executive Summary",
        "",
        "`Wave 1` remains closed, but its canonical comparison surface is now directional.",
        "",
        "The repository now treats each `Wave 1` family as a triad of winners:",
        "",
        "- one `global` model trained on the full directional dataset;",
        "- one `forward` model trained on the forward-only split;",
        "- one `backward` model trained on the backward-only split.",
        "",
        f"The current Wave 1 directional leader is `{best_registry_entry['run_name']}` from `{best_registry_entry['model_family']}` with `test_mae = {float(best_registry_entry['test_mae']):.6f} deg`.",
        "",
        "## Family Directional Summary",
        "",
    ]
    line_list.extend(build_family_scope_table(scope_record_list))
    line_list.extend(
        [
            "",
            "## Operational Consequences",
            "",
            "- Cross-family comparisons should now use like-for-like directional scopes instead of comparing a directional paper branch against an older all-directions repository baseline.",
            "- Future model-family waves should materialize the same `global` plus `forward` plus `backward` surface and refresh `models/exported/` during closeout.",
            f"- The full closeout evidence bundle for this transition is the final campaign report `{format_relative_path(campaign_results_report_path)}`.",
        ]
    )
    write_text_file(WAVE1_CLOSEOUT_STATUS_PATH, "\n".join(line_list))


def update_doc_index_with_campaign_report(campaign_results_report_path: Path) -> None:

    """Register the new campaign-results report from the canonical doc index."""

    report_relative_path = format_relative_path(campaign_results_report_path)
    report_link_line = f"- [{report_relative_path}](./{report_relative_path.replace(' ', '%20')})"
    if report_link_line in DOC_INDEX_PATH.read_text(encoding="utf-8"):
        return

    doc_index_text = DOC_INDEX_PATH.read_text(encoding="utf-8")
    insertion_anchor = "- [reports/campaign_results/2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report.md](./reports/campaign_results/2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report.md)"
    assert insertion_anchor in doc_index_text, "Failed to locate the Wave 1 campaign-results insertion anchor in doc/README.md"
    insertion_block = (
        f"{report_link_line}\n"
        "  Final results report for the completed Wave 1 directional retraining campaign, including repaired directional registry metadata, the consolidated 15-run ranking, and the exported Python plus ONNX archive under `models/exported/`.\n"
        f"{insertion_anchor}"
    )
    doc_index_text = doc_index_text.replace(insertion_anchor, insertion_block)
    write_text_file(DOC_INDEX_PATH, doc_index_text)


def update_models_root_readme() -> None:

    """Register the new exported-model archive contract in `models/README.md`."""

    models_readme_text = MODELS_ROOT_README_PATH.read_text(encoding="utf-8")
    archive_line = "- `exported/<family>/<scope>/` for curated deployment-facing Wave 1 winner copies in both `python/` and `onnx/` form"
    if archive_line in models_readme_text:
        return
    anchor_line = "- `exported/` for ONNX, Structured Text, or other deployment-ready exports"
    assert anchor_line in models_readme_text, "Failed to locate the exported-model anchor in models/README.md"
    replacement_block = (
        f"{anchor_line}\n"
        f"{archive_line}"
    )
    models_readme_text = models_readme_text.replace(anchor_line, replacement_block)
    write_text_file(MODELS_ROOT_README_PATH, models_readme_text)


def main() -> None:

    """Run the full Wave 1 directional retraining closeout."""

    command_line_arguments = parse_command_line_arguments()
    campaign_output_directory = resolve_campaign_output_directory(command_line_arguments.campaign_name)
    campaign_manifest_path = campaign_output_directory / "campaign_manifest.yaml"
    campaign_manifest_dictionary = load_yaml_dictionary(campaign_manifest_path)

    tree_repair_count = 0
    for run_dictionary in campaign_manifest_dictionary["run_list"]:
        output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(
            str(run_dictionary["output_directory"])
        )
        metrics_path = output_directory / shared_training_infrastructure.COMMON_METRICS_FILENAME
        training_config_path = output_directory / shared_training_infrastructure.COMMON_TRAINING_CONFIG_FILENAME
        training_config = shared_training_infrastructure.load_training_config(training_config_path)
        model_family = str(training_config["experiment"]["model_family"]).strip().lower()
        if model_family not in ["tree", "tree_fw", "tree_bw"]:
            continue
        if repair_tree_metrics_snapshot(metrics_path, training_config_path):
            tree_repair_count += 1

    campaign_registry_entry_list = refresh_family_registries_from_manifest(campaign_manifest_dictionary)
    best_registry_entry = write_campaign_registry_artifacts(
        campaign_output_directory,
        command_line_arguments.campaign_name,
        campaign_registry_entry_list,
    )

    scope_record_list = build_scope_record_list()
    archive_entry_list = refresh_export_archive(scope_record_list)
    write_export_archive_metadata(campaign_output_directory, archive_entry_list)

    report_timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    campaign_results_report_path = (
        CAMPAIGN_RESULTS_ROOT
        / f"{report_timestamp}_wave1_directional_retraining_campaign_results_report.md"
    )
    campaign_results_report_markdown = build_campaign_results_report_markdown(
        report_timestamp=report_timestamp,
        campaign_output_directory=campaign_output_directory,
        campaign_manifest_dictionary=campaign_manifest_dictionary,
        campaign_registry_entry_list=campaign_registry_entry_list,
        best_registry_entry=best_registry_entry,
        tree_repair_count=tree_repair_count,
        archive_entry_list=archive_entry_list,
    )
    write_text_file(campaign_results_report_path, campaign_results_report_markdown)

    write_wave1_closeout_status(
        best_registry_entry=best_registry_entry,
        scope_record_list=scope_record_list,
        campaign_results_report_path=campaign_results_report_path,
    )
    update_doc_index_with_campaign_report(campaign_results_report_path)
    update_models_root_readme()

    from scripts.reports.analysis.generate_training_results_master_summary import (
        generate_training_results_master_summary,
    )

    generate_training_results_master_summary(MASTER_SUMMARY_PATH)
    print(f"[DONE] Wave 1 directional retraining closeout completed | report={format_relative_path(campaign_results_report_path)}", flush=True)


if __name__ == "__main__":
    main()
