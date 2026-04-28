"""Support utilities for the original-dataset exact RCIM model-bank branch."""

from __future__ import annotations

# Import Python Utilities
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import pandas as pd

# Import Project Utilities
from scripts.datasets import transmission_error_dataset
from scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank import exact_paper_model_bank_support
from scripts.paper_reimplementation.rcim_ml_compensation.harmonic_wise_comparison import harmonic_wise_support
from scripts.training import shared_training_infrastructure

ORIGINAL_DATASET_EXACT_MODEL_REPORT_TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"
ORIGINAL_DATASET_DIRECTION_PREFIX_MAP = {
    "forward": "Fw",
    "backward": "Bw",
}


@dataclass
class OriginalDatasetExactModelBankBundle:

    """Prepared original-dataset bundle for one directional exact-model run."""

    exact_dataset_bundle: exact_paper_model_bank_support.ExactPaperDatasetBundle
    validation_feature_matrix: pd.DataFrame
    validation_target_matrix: pd.DataFrame
    dataset_root: Path
    dataset_config_path: Path
    direction_label: str
    direction_prefix: str
    selected_harmonic_list: list[int]
    decomposition_point_stride: int
    split_row_count_dictionary: dict[str, int]
    split_file_count_dictionary: dict[str, int]
    smoke_settings: dict[str, Any]


def load_original_dataset_exact_model_bank_config(config_path: str | Path) -> dict[str, Any]:

    """Load one original-dataset exact-model-bank configuration."""

    return shared_training_infrastructure.load_training_config(config_path)


def resolve_original_dataset_direction_settings(training_config: dict[str, Any]) -> tuple[str, str]:

    """Resolve the configured playback direction and its target-name prefix."""

    direction_label = str(training_config["data"]["direction_label"]).strip().lower()
    assert direction_label in ORIGINAL_DATASET_DIRECTION_PREFIX_MAP, (
        "Unsupported original-dataset exact direction label | "
        f"{direction_label}"
    )
    return direction_label, ORIGINAL_DATASET_DIRECTION_PREFIX_MAP[direction_label]


def resolve_original_dataset_smoke_settings(training_config: dict[str, Any] | None) -> dict[str, Any]:

    """Resolve optional smoke-validation limits for the original-dataset branch."""

    smoke_configuration = dict((training_config or {}).get("smoke", {}))
    smoke_enabled = bool(smoke_configuration.get("enabled", False))
    return {
        "enabled": smoke_enabled,
        "max_train_file_count": int(smoke_configuration.get("max_train_file_count", 0)),
        "max_validation_file_count": int(smoke_configuration.get("max_validation_file_count", 0)),
        "max_test_file_count": int(smoke_configuration.get("max_test_file_count", 0)),
    }


def _limit_directional_manifest_by_unique_file_count(
    directional_manifest: list[tuple[Path, str]],
    maximum_unique_file_count: int,
) -> list[tuple[Path, str]]:

    """Limit one directional manifest to the first N unique files."""

    if maximum_unique_file_count <= 0:
        return directional_manifest

    limited_manifest: list[tuple[Path, str]] = []
    selected_file_path_set: set[Path] = set()
    for csv_file_path, direction_label in directional_manifest:
        if csv_file_path not in selected_file_path_set:
            if len(selected_file_path_set) >= maximum_unique_file_count:
                continue
            selected_file_path_set.add(csv_file_path)
        limited_manifest.append((csv_file_path, direction_label))

    assert limited_manifest, "Smoke-limited directional manifest became empty"
    return limited_manifest


def _build_directional_target_name_list(
    direction_prefix: str,
    selected_harmonic_list: list[int],
) -> list[str]:

    """Build the ordered exact-paper target names for one direction."""

    target_name_list: list[str] = []
    for harmonic_order in selected_harmonic_list:
        target_name_list.append(f"fft_y_{direction_prefix}_filtered_ampl_{harmonic_order}")
        target_name_list.append(f"fft_y_{direction_prefix}_filtered_phase_{harmonic_order}")
    return target_name_list


def _build_directional_exact_dataframe(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    direction_prefix: str,
    selected_harmonic_list: list[int],
) -> pd.DataFrame:

    """Build one dataframe matching the exact-paper target schema."""

    dataframe_row_list: list[dict[str, float]] = []
    for curve_record in curve_record_list:
        row_dictionary: dict[str, float] = {
            "rpm": float(curve_record.speed_rpm),
            "deg": float(curve_record.oil_temperature_deg),
            "tor": float(curve_record.torque_nm),
        }
        for harmonic_order in selected_harmonic_list:
            row_dictionary[f"fft_y_{direction_prefix}_filtered_ampl_{harmonic_order}"] = float(
                curve_record.amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"]
            )
            row_dictionary[f"fft_y_{direction_prefix}_filtered_phase_{harmonic_order}"] = float(
                curve_record.amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"]
            )
        dataframe_row_list.append(row_dictionary)

    directional_dataframe = pd.DataFrame(dataframe_row_list)
    assert not directional_dataframe.empty, "Directional exact dataframe must not be empty"
    return directional_dataframe


def build_original_dataset_exact_model_bank_bundle(
    training_config: dict[str, Any],
) -> OriginalDatasetExactModelBankBundle:

    """Build the original-dataset exact-model-bank split bundle."""

    # Resolve Dataset And Direction
    dataset_config_path = shared_training_infrastructure.resolve_project_relative_path(
        training_config["paths"]["dataset_config_path"]
    )
    dataset_configuration = transmission_error_dataset.load_dataset_processing_config(dataset_config_path)
    dataset_root = transmission_error_dataset.resolve_project_relative_path(
        dataset_configuration["paths"]["dataset_root"]
    )
    direction_label, direction_prefix = resolve_original_dataset_direction_settings(training_config)

    # Build A Single-Direction Manifest And File-Level Split
    directional_file_manifest = transmission_error_dataset.build_directional_file_manifest(
        dataset_root=dataset_root,
        use_forward_direction=(direction_label == transmission_error_dataset.FORWARD_DIRECTION),
        use_backward_direction=(direction_label == transmission_error_dataset.BACKWARD_DIRECTION),
    )
    validation_split = float(training_config["training"]["validation_split"])
    test_size = float(training_config["training"]["test_size"])
    random_seed = int(training_config["training"]["random_seed"])
    train_manifest, validation_manifest, test_manifest = (
        transmission_error_dataset.split_directional_file_manifest(
            directional_file_manifest,
            validation_split=validation_split,
            test_split=test_size,
            random_seed=random_seed,
        )
    )
    smoke_settings = resolve_original_dataset_smoke_settings(training_config)
    if smoke_settings["enabled"]:
        train_manifest = _limit_directional_manifest_by_unique_file_count(
            train_manifest,
            smoke_settings["max_train_file_count"],
        )
        validation_manifest = _limit_directional_manifest_by_unique_file_count(
            validation_manifest,
            smoke_settings["max_validation_file_count"],
        )
        test_manifest = _limit_directional_manifest_by_unique_file_count(
            test_manifest,
            smoke_settings["max_test_file_count"],
        )

    # Build Harmonic Curve Records
    selected_harmonic_list = harmonic_wise_support.resolve_selected_harmonic_list(training_config)
    decomposition_point_stride = int(training_config["evaluation"]["decomposition_point_stride"])
    train_record_list = harmonic_wise_support.build_curve_record_list(
        train_manifest,
        selected_harmonic_list,
        decomposition_point_stride,
    )
    validation_record_list = harmonic_wise_support.build_curve_record_list(
        validation_manifest,
        selected_harmonic_list,
        decomposition_point_stride,
    )
    test_record_list = harmonic_wise_support.build_curve_record_list(
        test_manifest,
        selected_harmonic_list,
        decomposition_point_stride,
    )

    # Build Paper-Compatible Directional Dataframes
    train_dataframe = _build_directional_exact_dataframe(
        train_record_list,
        direction_prefix,
        selected_harmonic_list,
    )
    validation_dataframe = _build_directional_exact_dataframe(
        validation_record_list,
        direction_prefix,
        selected_harmonic_list,
    )
    test_dataframe = _build_directional_exact_dataframe(
        test_record_list,
        direction_prefix,
        selected_harmonic_list,
    )
    full_dataframe = pd.concat(
        [train_dataframe, validation_dataframe, test_dataframe],
        axis=0,
        ignore_index=True,
    )

    # Resolve Exact-Paper Feature And Target Surface
    feature_name_list = exact_paper_model_bank_support.resolve_paper_input_feature_name_list(training_config)
    full_target_name_list = _build_directional_target_name_list(direction_prefix, selected_harmonic_list)
    assert set(full_target_name_list).issubset(set(full_dataframe.columns.tolist())), (
        "Original-dataset exact dataframe is missing required harmonic targets"
    )
    target_name_list = exact_paper_model_bank_support.resolve_target_name_list(
        full_dataframe,
        training_config,
    )

    exact_dataset_bundle = exact_paper_model_bank_support.ExactPaperDatasetBundle(
        feature_name_list=feature_name_list,
        target_name_list=target_name_list,
        train_feature_matrix=train_dataframe[feature_name_list].copy(),
        test_feature_matrix=test_dataframe[feature_name_list].copy(),
        train_target_matrix=train_dataframe[target_name_list].copy(),
        test_target_matrix=test_dataframe[target_name_list].copy(),
        full_dataframe=full_dataframe,
    )
    split_row_count_dictionary = {
        "train": int(len(train_dataframe)),
        "validation": int(len(validation_dataframe)),
        "test": int(len(test_dataframe)),
    }
    split_file_count_dictionary = {
        "train": int(len({csv_file_path for csv_file_path, _ in train_manifest})),
        "validation": int(len({csv_file_path for csv_file_path, _ in validation_manifest})),
        "test": int(len({csv_file_path for csv_file_path, _ in test_manifest})),
    }
    return OriginalDatasetExactModelBankBundle(
        exact_dataset_bundle=exact_dataset_bundle,
        validation_feature_matrix=validation_dataframe[feature_name_list].copy(),
        validation_target_matrix=validation_dataframe[target_name_list].copy(),
        dataset_root=dataset_root,
        dataset_config_path=dataset_config_path,
        direction_label=direction_label,
        direction_prefix=direction_prefix,
        selected_harmonic_list=selected_harmonic_list,
        decomposition_point_stride=decomposition_point_stride,
        split_row_count_dictionary=split_row_count_dictionary,
        split_file_count_dictionary=split_file_count_dictionary,
        smoke_settings=smoke_settings,
    )


def build_original_dataset_validation_summary(
    resolved_config_path: Path,
    output_directory: Path,
    training_config: dict[str, Any],
    original_dataset_bundle: OriginalDatasetExactModelBankBundle,
    family_summary_list: list[dict[str, Any]],
    family_search_summary_dictionary: dict[str, dict[str, Any]],
    per_target_ranking_dictionary: dict[str, list[dict[str, Any]]],
    onnx_export_summary: dict[str, Any],
    model_bundle_path: Path,
) -> dict[str, Any]:

    """Build the canonical validation summary for the original-dataset branch."""

    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    run_artifact_identity = shared_training_infrastructure.resolve_run_artifact_identity(training_config)
    winner_family_summary = family_summary_list[0]
    target_winner_list: list[dict[str, Any]] = []
    for target_name in original_dataset_bundle.exact_dataset_bundle.target_name_list:
        winning_entry = per_target_ranking_dictionary[target_name][0]
        target_winner_list.append(
            {
                "target_name": target_name,
                "winning_family": winning_entry["family_name"],
                "winning_display_name": exact_paper_model_bank_support.EXACT_FAMILY_DISPLAY_NAME_MAP[
                    winning_entry["family_name"]
                ],
                "winning_estimator_name": exact_paper_model_bank_support.EXACT_FAMILY_ESTIMATOR_NAME_MAP[
                    winning_entry["family_name"]
                ],
                "winning_mape_percent": float(winning_entry["mape_percent"]),
                "winning_mae": float(winning_entry["mae"]),
                "winning_rmse": float(winning_entry["rmse"]),
            }
        )

    return {
        "schema_version": 1,
        "workflow_name": "rcim_original_dataset_exact_model_bank_validation",
        "reference_scope": "original_dataset_directional_exact_model_bank",
        "config_path": shared_training_infrastructure.format_project_relative_path(resolved_config_path),
        "experiment": {
            "model_family": experiment_identity.model_family,
            "model_type": experiment_identity.model_type,
            "run_name": experiment_identity.run_name,
            "output_run_name": run_artifact_identity.run_name,
            "run_instance_id": run_artifact_identity.run_instance_id,
            "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        },
        "dataset": {
            "dataset_root": shared_training_infrastructure.format_project_relative_path(
                original_dataset_bundle.dataset_root
            ),
            "dataset_config_path": shared_training_infrastructure.format_project_relative_path(
                original_dataset_bundle.dataset_config_path
            ),
            "direction_label": original_dataset_bundle.direction_label,
            "direction_prefix": original_dataset_bundle.direction_prefix,
            "filtered_row_count": int(len(original_dataset_bundle.exact_dataset_bundle.full_dataframe)),
            "feature_count": int(len(original_dataset_bundle.exact_dataset_bundle.feature_name_list)),
            "target_count": int(len(original_dataset_bundle.exact_dataset_bundle.target_name_list)),
            "feature_name_list": list(original_dataset_bundle.exact_dataset_bundle.feature_name_list),
            "target_name_list": list(original_dataset_bundle.exact_dataset_bundle.target_name_list),
            "selected_harmonic_list": [int(harmonic_order) for harmonic_order in original_dataset_bundle.selected_harmonic_list],
            "decomposition_point_stride": int(original_dataset_bundle.decomposition_point_stride),
            "train_row_count": int(original_dataset_bundle.split_row_count_dictionary["train"]),
            "validation_row_count": int(original_dataset_bundle.split_row_count_dictionary["validation"]),
            "test_row_count": int(original_dataset_bundle.split_row_count_dictionary["test"]),
            "train_file_count": int(original_dataset_bundle.split_file_count_dictionary["train"]),
            "validation_file_count": int(original_dataset_bundle.split_file_count_dictionary["validation"]),
            "test_file_count": int(original_dataset_bundle.split_file_count_dictionary["test"]),
            "validation_split": float(training_config["training"]["validation_split"]),
            "test_size": float(training_config["training"]["test_size"]),
            "random_seed": int(training_config["training"]["random_seed"]),
            "smoke_settings": dict(original_dataset_bundle.smoke_settings),
        },
        "training_strategy": {
            "hyperparameter_search_mode": exact_paper_model_bank_support.resolve_exact_paper_hyperparameter_search_settings(
                training_config
            )["mode"],
            "family_search_summary": family_search_summary_dictionary,
            "validation_usage_note": (
                "Validation split is reserved for future campaign-level tuning. "
                "The current stabilization branch fits on the train split and reports held-out test metrics."
            ),
        },
        "paper_alignment": {
            "input_feature_schema": ["rpm", "deg", "tor"],
            "feature_origin_mapping": {
                "rpm": "speed_rpm",
                "deg": "oil_temperature_deg",
                "tor": "torque_nm",
            },
            "separate_direction_models": True,
            "published_paper_tables_reference_scope": "forward_only",
        },
        "dependency_versions": exact_paper_model_bank_support.resolve_dependency_version_dictionary(),
        "winner_summary": {
            "winning_family": winner_family_summary["family_name"],
            "winning_display_name": winner_family_summary["display_name"],
            "winning_estimator_name": winner_family_summary["estimator_name"],
            "winning_mean_component_mape_percent": float(winner_family_summary["mean_component_mape_percent"]),
            "winning_mean_component_mae": float(winner_family_summary["mean_component_mae"]),
            "winning_mean_component_rmse": float(winner_family_summary["mean_component_rmse"]),
            "winning_best_params": family_search_summary_dictionary[winner_family_summary["family_name"]]["best_params"],
        },
        "family_ranking": family_summary_list,
        "target_winner_registry": target_winner_list,
        "per_target_ranking": per_target_ranking_dictionary,
        "onnx_export_summary": onnx_export_summary,
        "artifacts": {
            "model_bundle_path": shared_training_infrastructure.format_project_relative_path(model_bundle_path),
            "validation_summary_path": shared_training_infrastructure.format_project_relative_path(
                output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME
            ),
        },
    }


def build_original_dataset_validation_report_path(training_config: dict[str, Any]) -> Path:

    """Build the Markdown report path for the original-dataset branch."""

    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    output_run_name = shared_training_infrastructure.resolve_output_run_name(training_config)
    timestamp_string = datetime.now().strftime(ORIGINAL_DATASET_EXACT_MODEL_REPORT_TIMESTAMP_FORMAT)
    report_filename = (
        f"{timestamp_string}_{shared_training_infrastructure.sanitize_name(experiment_identity.model_family)}_"
        f"{shared_training_infrastructure.sanitize_name(output_run_name)}_original_dataset_exact_model_bank_report.md"
    )
    report_root = (
        shared_training_infrastructure.resolve_runtime_project_path()
        / "doc"
        / "reports"
        / "analysis"
        / "validation_checks"
    )
    report_path = report_root / report_filename
    report_path.parent.mkdir(parents=True, exist_ok=True)
    return report_path


def build_original_dataset_validation_report_markdown(validation_summary: dict[str, Any]) -> str:

    """Build the human-readable Markdown report for the original-dataset branch."""

    experiment_dictionary = validation_summary["experiment"]
    dataset_dictionary = validation_summary["dataset"]
    training_strategy_dictionary = validation_summary["training_strategy"]
    winner_summary = validation_summary["winner_summary"]
    family_ranking = validation_summary["family_ranking"]
    target_winner_registry = validation_summary["target_winner_registry"]
    family_search_summary_dictionary = training_strategy_dictionary["family_search_summary"]

    family_row_list: list[str] = []
    for ranking_index, family_entry in enumerate(family_ranking, start=1):
        family_search_entry = family_search_summary_dictionary[family_entry["family_name"]]
        best_params_text = (
            f"`{family_search_entry['best_params']}`"
            if family_search_entry["best_params"] is not None
            else "-"
        )
        family_row_list.append(
            f"| {ranking_index} | `{family_entry['family_name']}` | "
            f"`{family_entry['estimator_name']}` | "
            f"{family_entry['mean_component_mape_percent']:.3f} | "
            f"{family_entry['mean_component_mae']:.6f} | "
            f"{family_entry['mean_component_rmse']:.6f} | "
            f"{best_params_text} |"
        )

    target_winner_row_list: list[str] = []
    for target_winner_entry in target_winner_registry:
        target_winner_row_list.append(
            f"| `{target_winner_entry['target_name']}` | "
            f"`{target_winner_entry['winning_family']}` | "
            f"{target_winner_entry['winning_mae']:.6f} | "
            f"{target_winner_entry['winning_rmse']:.6f} | "
            f"{target_winner_entry['winning_mape_percent']:.3f} |"
        )

    return "\n".join(
        [
            "# Original-Dataset Exact RCIM Model Bank Validation Report",
            "",
            "## Overview",
            "",
            "This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.",
            "",
            f"- direction label: `{dataset_dictionary['direction_label']}`",
            f"- dataset root: `{dataset_dictionary['dataset_root']}`",
            f"- dataset config: `{dataset_dictionary['dataset_config_path']}`",
            f"- selected harmonics: `{', '.join(str(value) for value in dataset_dictionary['selected_harmonic_list'])}`",
            f"- decomposition point stride: `{dataset_dictionary['decomposition_point_stride']}`",
            f"- feature schema: `{', '.join(dataset_dictionary['feature_name_list'])}`",
            f"- target count: `{dataset_dictionary['target_count']}`",
            "",
            "## Split Summary",
            "",
            f"- train rows / files: `{dataset_dictionary['train_row_count']}` / `{dataset_dictionary['train_file_count']}`",
            f"- validation rows / files: `{dataset_dictionary['validation_row_count']}` / `{dataset_dictionary['validation_file_count']}`",
            f"- test rows / files: `{dataset_dictionary['test_row_count']}` / `{dataset_dictionary['test_file_count']}`",
            f"- validation split: `{dataset_dictionary['validation_split']}`",
            f"- test split: `{dataset_dictionary['test_size']}`",
            f"- random seed: `{dataset_dictionary['random_seed']}`",
            f"- validation usage note: {training_strategy_dictionary['validation_usage_note']}",
            "",
            "## Winner Summary",
            "",
            f"- winning family: `{winner_summary['winning_family']}`",
            f"- winning estimator: `{winner_summary['winning_estimator_name']}`",
            f"- winning mean component MAPE: `{winner_summary['winning_mean_component_mape_percent']:.3f}%`",
            f"- winning mean component MAE: `{winner_summary['winning_mean_component_mae']:.6f}`",
            f"- winning mean component RMSE: `{winner_summary['winning_mean_component_rmse']:.6f}`",
            "",
            "## Family Ranking",
            "",
            "| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |",
            "| --- | --- | --- | ---: | ---: | ---: | --- |",
            *family_row_list,
            "",
            "## Per-Target Winners",
            "",
            "| Target | Winning Family | MAE | RMSE | MAPE % |",
            "| --- | --- | ---: | ---: | ---: |",
            *target_winner_row_list,
            "",
            "## Artifact Paths",
            "",
            f"- config path: `{validation_summary['config_path']}`",
            f"- output directory: `{experiment_dictionary['output_directory']}`",
            f"- model bundle: `{validation_summary['artifacts']['model_bundle_path']}`",
            f"- validation summary: `{validation_summary['artifacts']['validation_summary_path']}`",
            "",
        ]
    )
