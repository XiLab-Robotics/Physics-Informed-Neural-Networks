"""Build TE Curve Verification Pipeline inventories for polished RCIM exports."""

from __future__ import annotations

# Import Python Utilities
import argparse
import sys
from pathlib import Path
from typing import Any

# Import Third-Party Utilities
import yaml

# Configure Import Path
PROJECT_PATH = Path(__file__).resolve().parents[4]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.training import shared_training_infrastructure

FAMILY_DIRECTORY_DICTIONARY = {
    "SVR": "svm_reference_models",
    "MLP": "mlp_reference_models",
    "RF": "rf_reference_models",
    "DT": "dt_reference_models",
    "ET": "et_reference_models",
    "ERT": "ert_reference_models",
    "GBM": "gbm_reference_models",
    "HGBM": "hgbm_reference_models",
    "XGBM": "xgbm_reference_models",
    "LGBM": "lgbm_reference_models",
}

FAMILY_LABEL_DICTIONARY = {
    "SVR": "SVM",
    "MLP": "MLP",
    "RF": "RF",
    "DT": "DT",
    "ET": "ET",
    "ERT": "ERT",
    "GBM": "GBM",
    "HGBM": "HGBM",
    "XGBM": "XGBM",
    "LGBM": "LGBM",
}


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Build reference inventories from polished RCIM validation summaries.",
    )
    argument_parser.add_argument(
        "--forward-summary-path",
        type=Path,
        default=Path(
            "output/validation_checks/rcim_model_bank_reproduction/"
            "2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation/"
            "validation_summary.yaml"
        ),
        help="Polished forward RCIM validation summary.",
    )
    argument_parser.add_argument(
        "--backward-summary-path",
        type=Path,
        default=Path(
            "output/validation_checks/rcim_model_bank_reproduction/"
            "2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation/"
            "validation_summary.yaml"
        ),
        help="Polished backward RCIM validation summary.",
    )
    argument_parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("output/validation_checks/rcim_model_bank_reproduction/reference_inventories"),
        help="Output root for generated reference inventories.",
    )
    return argument_parser.parse_args()


def load_yaml_dictionary(yaml_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    resolved_path = shared_training_infrastructure.resolve_runtime_project_relative_path(yaml_path)
    if not resolved_path.is_file():
        raise FileNotFoundError(f"Missing RCIM validation summary: {resolved_path}")
    with resolved_path.open("r", encoding="utf-8") as input_stream:
        loaded_dictionary = yaml.safe_load(input_stream) or {}
    if not isinstance(loaded_dictionary, dict):
        raise TypeError(f"Expected YAML dictionary: {resolved_path}")
    return loaded_dictionary


def format_project_path(path_value: str | Path) -> str:

    """Format a repository-relative path for YAML output."""

    resolved_path = shared_training_infrastructure.resolve_runtime_project_relative_path(path_value)
    return shared_training_infrastructure.format_project_relative_path(resolved_path)


def parse_target_metadata(target_name: str) -> tuple[str, int]:

    """Parse target kind and harmonic order from an RCIM target name."""

    target_name_text = str(target_name).strip()
    if "_ampl_" in target_name_text:
        return "amplitude", int(target_name_text.rsplit("_ampl_", 1)[1])
    if "_phase_" in target_name_text:
        return "phase", int(target_name_text.rsplit("_phase_", 1)[1])
    raise ValueError(f"Unsupported RCIM target name: {target_name_text}")


def collect_family_metric_dictionary(summary_dictionary: dict[str, Any]) -> dict[str, dict[str, dict[str, float]]]:

    """Collect per-family, per-target metrics from the validation summary."""

    metric_dictionary: dict[str, dict[str, dict[str, float]]] = {}
    for family_dictionary in summary_dictionary.get("family_ranking", []):
        family_name = str(family_dictionary["family_name"]).strip()
        target_metric_dictionary: dict[str, dict[str, float]] = {}
        for target_dictionary in family_dictionary.get("target_metrics", []):
            target_name = str(target_dictionary["target_name"]).strip()
            target_metric_dictionary[target_name] = {
                "mae": float(target_dictionary["mae"]),
                "rmse": float(target_dictionary["rmse"]),
                "mape_percent": float(target_dictionary["mape_percent"]),
            }
        metric_dictionary[family_name] = target_metric_dictionary
    return metric_dictionary


def build_family_inventory(
    summary_dictionary: dict[str, Any],
    family_export_dictionary: dict[str, Any],
    family_metric_dictionary: dict[str, dict[str, dict[str, float]]],
    direction_label: str,
) -> dict[str, Any]:

    """Build one reference inventory dictionary for one RCIM family."""

    family_name = str(family_export_dictionary["family_name"]).strip()
    family_label = FAMILY_LABEL_DICTIONARY[family_name]
    dataset_dictionary = summary_dictionary["dataset"]
    experiment_dictionary = summary_dictionary["experiment"]
    feature_name_list = [str(feature_name) for feature_name in dataset_dictionary["feature_name_list"]]
    target_name_list = [str(target_name) for target_name in dataset_dictionary["target_name_list"]]
    selected_harmonic_list = [int(order) for order in dataset_dictionary["selected_harmonic_list"]]
    reference_model_list: list[dict[str, Any]] = []

    for exported_target_dictionary in family_export_dictionary["exported_targets"]:
        if str(exported_target_dictionary["python_export_status"]).strip() != "exported":
            continue
        target_name = str(exported_target_dictionary["target_name"]).strip()
        target_kind, harmonic_order = parse_target_metadata(target_name)
        target_metric_dictionary = family_metric_dictionary[family_name][target_name]
        reference_model_list.append(
            {
                "target_name": target_name,
                "target_kind": target_kind,
                "harmonic_order": harmonic_order,
                "direction_label": direction_label,
                "benchmark_mae": target_metric_dictionary["mae"],
                "benchmark_rmse": target_metric_dictionary["rmse"],
                "training_metric_mae": target_metric_dictionary["mae"],
                "training_metric_rmse": target_metric_dictionary["rmse"],
                "training_metric_mape_percent": target_metric_dictionary["mape_percent"],
                "source_run_instance_id": str(experiment_dictionary["run_instance_id"]),
                "source_config_path": str(summary_dictionary["config_path"]),
                "source_validation_summary_path": format_project_path(
                    summary_dictionary["artifacts"]["validation_summary_path"]
                ),
                "source_model_bundle_path": format_project_path(
                    summary_dictionary["artifacts"]["model_bundle_path"]
                ),
                "source_export_path": format_project_path(exported_target_dictionary["onnx_export_path"]),
                "python_model_path": format_project_path(exported_target_dictionary["python_export_path"]),
                "python_model_serialization": "pickle_protocol",
                "python_estimator_class_name": str(exported_target_dictionary["export_estimator_name"]),
                "export_estimator_name": str(exported_target_dictionary["export_estimator_name"]),
                "surrogate_strategy": str(exported_target_dictionary.get("surrogate_strategy", "none")),
                "feature_name_list": feature_name_list,
                "source_run_target_name_list": target_name_list,
                "filtered_row_count": int(dataset_dictionary["filtered_row_count"]),
                "train_row_count": int(dataset_dictionary["train_row_count"]),
                "validation_row_count": int(dataset_dictionary["validation_row_count"]),
                "test_row_count": int(dataset_dictionary["test_row_count"]),
                "train_file_count": int(dataset_dictionary["train_file_count"]),
                "validation_file_count": int(dataset_dictionary["validation_file_count"]),
                "test_file_count": int(dataset_dictionary["test_file_count"]),
                "test_size": float(dataset_dictionary["test_size"]),
                "random_seed": int(dataset_dictionary["random_seed"]),
                "selected_harmonic_list": selected_harmonic_list,
                "decomposition_point_stride": int(dataset_dictionary["decomposition_point_stride"]),
            }
        )

    expected_target_count = len(target_name_list)
    if len(reference_model_list) != expected_target_count:
        raise AssertionError(
            "Incomplete polished RCIM family export | "
            f"family={family_name} direction={direction_label} "
            f"expected={expected_target_count} found={len(reference_model_list)}"
        )

    return {
        "schema_version": 2,
        "topic": "polished_dataset_rcim_model_bank_reproduction_reference_archive",
        "paper_family_name": family_label,
        "implementation_family_name": family_name,
        "archive_scope": f"polished_dataset_{direction_label}",
        "canonical_selection_rule": (
            "Generated from the completed polished RCIM Model-Bank Reproduction "
            "validation summary for TE Curve Verification Pipeline comparison."
        ),
        "source_code": (
            "scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/"
            "build_polished_rcim_reference_inventories.py"
        ),
        "source_data": str(dataset_dictionary["dataset_config_path"]),
        "notes": [
            "This inventory is generated, not hand curated.",
            "It points to the committed Python exports from the polished RCIM campaign.",
        ],
        "reference_models": sorted(
            reference_model_list,
            key=lambda entry: (int(entry["harmonic_order"]), str(entry["target_kind"])),
        ),
    }


def write_direction_inventories(summary_path: Path, output_root: Path, direction_folder: str) -> list[Path]:

    """Write all family inventories for one RCIM direction."""

    summary_dictionary = load_yaml_dictionary(summary_path)
    direction_label = str(summary_dictionary["dataset"]["direction_label"]).strip().lower()
    family_metric_dictionary = collect_family_metric_dictionary(summary_dictionary)
    output_path_list: list[Path] = []

    for family_export_dictionary in summary_dictionary["onnx_export_summary"]["family_exports"]:
        family_name = str(family_export_dictionary["family_name"]).strip()
        if family_name not in FAMILY_DIRECTORY_DICTIONARY:
            continue
        inventory_dictionary = build_family_inventory(
            summary_dictionary,
            family_export_dictionary,
            family_metric_dictionary,
            direction_label,
        )
        inventory_directory = (
            shared_training_infrastructure.resolve_runtime_project_relative_path(output_root)
            / direction_folder
            / FAMILY_DIRECTORY_DICTIONARY[family_name]
        )
        inventory_directory.mkdir(parents=True, exist_ok=True)
        inventory_path = inventory_directory / "reference_inventory.yaml"
        with inventory_path.open("w", encoding="utf-8") as output_stream:
            yaml.safe_dump(
                inventory_dictionary,
                output_stream,
                sort_keys=False,
                allow_unicode=True,
                width=120,
            )
        output_path_list.append(inventory_path)

    if not output_path_list:
        raise AssertionError(f"No inventories generated from summary: {summary_path}")
    return output_path_list


def main() -> None:

    """Build both polished RCIM direction inventory sets."""

    arguments = parse_command_line_arguments()
    output_path_list = []
    output_path_list.extend(
        write_direction_inventories(arguments.forward_summary_path, arguments.output_root, "forward")
    )
    output_path_list.extend(
        write_direction_inventories(arguments.backward_summary_path, arguments.output_root, "backward")
    )
    print(
        "Prepared polished RCIM reference inventories | "
        f"count={len(output_path_list)} | root={arguments.output_root}"
    )


if __name__ == "__main__":
    main()
