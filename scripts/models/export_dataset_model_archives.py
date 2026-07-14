"""Build dataset-first model export archives from completed campaign runs."""

from __future__ import annotations

# Import Python Utilities
import argparse
import multiprocessing
import os
import pickle
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml

PROJECT_PATH = Path(__file__).resolve().parents[2]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

TARGET_ONNX_OPSET = 17
TREE_MODEL_TYPE_SET = {"random_forest", "hist_gradient_boosting"}
TEMPORAL_MODEL_NAME_TOKEN_LIST = [
    "gru",
    "lstm",
    "sequence",
    "temporal",
    "latent_dynamics",
]
COMMON_TRAINING_CONFIG_FILENAME = "training_config.yaml"
COMMON_METRICS_FILENAME = "metrics_summary.yaml"
COMMON_RUN_METADATA_FILENAME = "run_metadata.yaml"
COMMON_RUN_REPORT_FILENAME = "training_test_report.md"


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Build dataset-first model export archives from completed campaign manifests."
    )
    argument_parser.add_argument(
        "--dataset-id",
        required=True,
        choices=["polished_dataset", "simplified_dataset"],
        help="Dataset archive root to build.",
    )
    argument_parser.add_argument(
        "--input-mode",
        required=True,
        choices=["setpoints", "actual_values"],
        help="Dataset input mode archive branch to build.",
    )
    argument_parser.add_argument(
        "--campaign-manifest",
        action="append",
        default=[],
        help="Campaign manifest path to read. Repeat for multiple campaigns.",
    )
    argument_parser.add_argument(
        "--output-root",
        default=None,
        help="Override output root. Defaults to models/<dataset-id>/<input-mode>/exported.",
    )
    argument_parser.add_argument(
        "--export",
        action="store_true",
        help="Write artifacts. Without this flag the script only reports inventory.",
    )
    argument_parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip run archives that already contain reference_inventory.yaml.",
    )
    argument_parser.add_argument(
        "--onnx-timeout-seconds",
        type=int,
        default=180,
        help="Per-run ONNX export timeout. Timed-out runs still keep Python/provenance artifacts.",
    )
    return argument_parser.parse_args()


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def save_yaml_dictionary(output_path: Path, payload: dict[str, Any]) -> None:

    """Save one YAML dictionary."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False)


def format_project_relative_path(path_value: Path | str) -> str:

    """Format one path relative to the repository when possible."""

    path = Path(path_value)
    if not path.is_absolute():
        return path.as_posix()
    try:
        return path.absolute().relative_to(PROJECT_PATH).as_posix()
    except ValueError:
        return path.as_posix()


def resolve_project_path(path_value: Path | str) -> Path:

    """Resolve a project-relative or absolute path."""

    path = Path(path_value)
    if path.is_absolute():
        return path.resolve()
    return (PROJECT_PATH / path).resolve()


def normalize_surface_name(run_dictionary: dict[str, Any], metrics_dictionary: dict[str, Any] | None) -> str:

    """Normalize one training run to global, forward, or backward surface."""

    for source_dictionary in [run_dictionary, metrics_dictionary or {}]:
        variant = str(source_dictionary.get("training_variant", "")).strip().lower()
        if variant in ["fw", "forward"]:
            return "forward"
        if variant in ["bw", "backward"]:
            return "backward"
        if variant == "global":
            return "global"

        experiment_dictionary = source_dictionary.get("experiment", {})
        if isinstance(experiment_dictionary, dict):
            experiment_variant = str(experiment_dictionary.get("training_variant", "")).strip().lower()
            if experiment_variant in ["fw", "forward"]:
                return "forward"
            if experiment_variant in ["bw", "backward"]:
                return "backward"
            if experiment_variant == "global":
                return "global"

    run_name = str(run_dictionary.get("run_name", "")).lower()
    if run_name.endswith("_fw"):
        return "forward"
    if run_name.endswith("_bw"):
        return "backward"
    return "global"


def read_best_checkpoint_path(run_dictionary: dict[str, Any], output_directory: Path) -> Path:

    """Resolve the best Python-side model artifact for one run."""

    raw_path = run_dictionary.get("best_checkpoint_path")
    if raw_path not in [None, ""]:
        candidate_path = resolve_project_path(str(raw_path))
        if candidate_path.exists():
            return candidate_path

    pointer_path = output_directory / "best_checkpoint_path.txt"
    if pointer_path.exists():
        pointer_text = pointer_path.read_text(encoding="utf-8").strip()
        if pointer_text:
            candidate_path = resolve_project_path(pointer_text)
            if candidate_path.exists():
                return candidate_path

    tree_model_path = output_directory / "tree_model.pkl"
    if tree_model_path.exists():
        return tree_model_path

    checkpoint_path_list = sorted((output_directory / "checkpoints").glob("*.ckpt"))
    assert checkpoint_path_list, f"Missing best checkpoint for run | {output_directory}"
    return checkpoint_path_list[-1].resolve()


def load_metrics_dictionary(output_directory: Path) -> dict[str, Any]:

    """Load metrics summary for one run."""

    metrics_path = output_directory / COMMON_METRICS_FILENAME
    assert metrics_path.exists(), f"Missing metrics summary | {metrics_path}"
    return load_yaml_dictionary(metrics_path)


def load_training_config(output_directory: Path) -> dict[str, Any]:

    """Load training config snapshot for one run."""

    training_config_path = output_directory / COMMON_TRAINING_CONFIG_FILENAME
    assert training_config_path.exists(), f"Missing training config | {training_config_path}"
    return load_yaml_dictionary(training_config_path)


def build_archive_run_list(
    manifest_path_list: list[Path],
    dataset_id: str,
    input_mode: str,
) -> list[dict[str, Any]]:

    """Build archive run records from campaign manifests."""

    archive_run_list: list[dict[str, Any]] = []
    seen_run_instance_id_set: set[str] = set()

    for manifest_path in manifest_path_list:
        manifest_dictionary = load_yaml_dictionary(manifest_path)
        raw_run_list = manifest_dictionary.get("run_list", [])
        if not isinstance(raw_run_list, list):
            raw_run_list = manifest_dictionary.get("runs", [])
        assert isinstance(raw_run_list, list), f"Expected run list in manifest | {manifest_path}"

        for run_dictionary in raw_run_list:
            assert isinstance(run_dictionary, dict), f"Expected run dictionary | {manifest_path}"
            run_instance_id = str(run_dictionary.get("run_instance_id", "")).strip()
            output_directory = resolve_project_path(str(run_dictionary["output_directory"]))
            metrics_dictionary = load_metrics_dictionary(output_directory)
            metrics_dataset_dictionary = metrics_dictionary.get("dataset", {})
            run_dataset_id = str(
                run_dictionary.get("dataset_id")
                or metrics_dataset_dictionary.get("dataset_id")
                or metrics_dictionary.get("dataset_split", {}).get("dataset_name")
            )
            if run_dataset_id != dataset_id:
                continue
            run_input_mode = str(
                run_dictionary.get("input_mode")
                or metrics_dataset_dictionary.get("input_mode")
                or metrics_dictionary.get("dataset_split", {}).get("input_mode")
                or "setpoints"
            )
            if run_input_mode != input_mode:
                continue
            if run_instance_id in seen_run_instance_id_set:
                continue
            seen_run_instance_id_set.add(run_instance_id)

            best_checkpoint_path = read_best_checkpoint_path(run_dictionary, output_directory)
            archive_run_list.append(
                {
                    "manifest_path": manifest_path,
                    "run_dictionary": run_dictionary,
                    "metrics_dictionary": metrics_dictionary,
                    "output_directory": output_directory,
                    "best_checkpoint_path": best_checkpoint_path,
                    "surface": normalize_surface_name(run_dictionary, metrics_dictionary),
                }
            )

    return archive_run_list


def load_neural_regression_module(training_config: dict[str, Any], checkpoint_path: Path):

    """Load one Lightning checkpoint for ONNX export."""

    import torch

    from scripts.training import shared_training_infrastructure
    from scripts.training.transmission_error_regression_module import TransmissionErrorRegressionModule

    datamodule, _, _, normalization_statistics = shared_training_infrastructure.initialize_training_components(
        training_config
    )
    regression_module = TransmissionErrorRegressionModule.load_from_checkpoint(
        checkpoint_path=checkpoint_path,
        regression_model=shared_training_infrastructure.create_regression_backbone_from_training_config(
            training_config,
            datamodule.get_input_feature_dim(),
        ),
        input_feature_dim=datamodule.get_input_feature_dim(),
        target_feature_dim=datamodule.get_target_feature_dim(),
        normalization_statistics=normalization_statistics,
        map_location=torch.device("cpu"),
    )
    regression_module.to(torch.device("cpu"))
    regression_module.eval()
    return regression_module


def export_tree_model_to_onnx(training_config: dict[str, Any], python_model_path: Path, onnx_output_path: Path) -> None:

    """Export one tree model to ONNX."""

    from skl2onnx import convert_sklearn
    from skl2onnx.common.data_types import FloatTensorType

    with python_model_path.open("rb") as input_file:
        estimator = pickle.load(input_file)
    configured_feature_count = training_config["model"].get("input_size")
    if str(configured_feature_count).strip().lower() == "auto":
        configured_feature_count = None
    feature_count = int(
        getattr(
            estimator,
            "n_features_in_",
            int(configured_feature_count) if configured_feature_count is not None else 0,
        )
    )
    assert feature_count > 0, f"Unable to resolve tree export feature count | {python_model_path}"
    initial_types = [("float_input", FloatTensorType([None, feature_count]))]
    onnx_model = convert_sklearn(
        estimator,
        initial_types=initial_types,
        target_opset=TARGET_ONNX_OPSET,
    )
    onnx_output_path.parent.mkdir(parents=True, exist_ok=True)
    with onnx_output_path.open("wb") as output_file:
        output_file.write(onnx_model.SerializeToString())


def build_neural_export_dummy_input(
    regression_module,
    training_config: dict[str, Any],
):

    """Build a raw-input example tensor that matches the trained model contract."""

    dataset_dictionary = training_config.get("dataset", {})
    experiment_dictionary = training_config.get("experiment", {})
    model_dictionary = training_config.get("model", {})
    assert isinstance(dataset_dictionary, dict), "Expected dataset dictionary in training config."
    assert isinstance(experiment_dictionary, dict), "Expected experiment dictionary in training config."
    assert isinstance(model_dictionary, dict), "Expected model dictionary in training config."

    base_input_tensor = regression_module.input_feature_mean.detach().clone().float()
    collate_mode = str(dataset_dictionary.get("collate_mode", "")).strip().lower()
    model_type = str(experiment_dictionary.get("model_type") or model_dictionary.get("model_type") or "").lower()
    sequence_length = int(dataset_dictionary.get("sequence_length") or model_dictionary.get("sequence_length") or 0)
    uses_temporal_input = collate_mode == "sequence" or sequence_length > 0
    uses_temporal_input = uses_temporal_input or any(token in model_type for token in TEMPORAL_MODEL_NAME_TOKEN_LIST)
    if not uses_temporal_input:
        return base_input_tensor.unsqueeze(0)

    if sequence_length <= 0:
        sequence_length = 33
    return base_input_tensor.view(1, 1, -1).repeat(1, sequence_length, 1)


def export_neural_model_to_onnx(training_config: dict[str, Any], checkpoint_path: Path, onnx_output_path: Path) -> None:

    """Export one neural model checkpoint to ONNX."""

    import torch
    import torch.nn as nn

    class RawInputPredictionExportWrapper(nn.Module):

        """Export wrapper that preserves the raw-input contract for neural models."""

        def __init__(self, regression_module) -> None:
            super().__init__()
            self.regression_module = regression_module

        def forward(self, input_tensor):

            """Predict denormalized TE from raw input rows."""

            raw_input_tensor = input_tensor.float()
            normalized_input_tensor = self.regression_module.normalize_input_tensor(raw_input_tensor)
            normalized_prediction_tensor, _ = self.regression_module.forward_regression_model(
                raw_input_tensor,
                normalized_input_tensor,
            )
            return self.regression_module.denormalize_target_tensor(normalized_prediction_tensor)

    regression_module = load_neural_regression_module(training_config, checkpoint_path)
    export_wrapper = RawInputPredictionExportWrapper(regression_module)
    export_wrapper.eval()
    dummy_input_tensor = build_neural_export_dummy_input(regression_module, training_config)
    dynamic_input_axes = {0: "batch_size"}
    if dummy_input_tensor.dim() == 3:
        dynamic_input_axes[1] = "sequence_length"
    onnx_output_path.parent.mkdir(parents=True, exist_ok=True)
    with torch.no_grad():
        export_keyword_arguments = {
            "input_names": ["input_tensor"],
            "output_names": ["prediction_tensor"],
            "dynamic_axes": {
                "input_tensor": dynamic_input_axes,
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


def export_model_to_onnx_worker(
    model_type: str,
    training_config: dict[str, Any],
    python_model_path_text: str,
    onnx_output_path_text: str,
    result_queue: multiprocessing.Queue,
) -> None:

    """Run one ONNX export in a child process."""

    try:
        python_model_path = Path(python_model_path_text)
        onnx_output_path = Path(onnx_output_path_text)
        if model_type in TREE_MODEL_TYPE_SET:
            export_tree_model_to_onnx(training_config, python_model_path, onnx_output_path)
        else:
            export_neural_model_to_onnx(training_config, python_model_path, onnx_output_path)
        result_queue.put({"status": "exported", "error": ""})
    except Exception as error:  # noqa: BLE001 - exported into machine-readable inventory.
        result_queue.put({"status": "failed", "error": f"{error.__class__.__name__}: {error}"})


def export_model_to_onnx_with_timeout(
    model_type: str,
    training_config: dict[str, Any],
    python_model_path: Path,
    onnx_output_path: Path,
    timeout_seconds: int,
) -> tuple[str, str]:

    """Export one model to ONNX with a per-run timeout."""

    result_queue: multiprocessing.Queue = multiprocessing.Queue()
    export_process = multiprocessing.Process(
        target=export_model_to_onnx_worker,
        args=(
            model_type,
            training_config,
            str(python_model_path),
            str(onnx_output_path),
            result_queue,
        ),
    )
    export_process.start()
    export_process.join(timeout=max(1, int(timeout_seconds)))
    if export_process.is_alive():
        export_process.terminate()
        export_process.join(timeout=10)
        if onnx_output_path.exists():
            onnx_output_path.unlink()
        return "timeout", f"ONNX export exceeded {timeout_seconds} seconds"

    if result_queue.empty():
        if onnx_output_path.exists():
            return "exported", ""
        return "failed", f"ONNX export process exited with code {export_process.exitcode}"

    result_dictionary = result_queue.get()
    return str(result_dictionary["status"]), str(result_dictionary["error"])


def resolve_archive_input_mode(
    run_dictionary: dict[str, Any],
    metrics_dictionary: dict[str, Any],
    training_config: dict[str, Any],
) -> str:

    """Resolve an input-mode label across old and new run metadata layouts."""

    metrics_dataset_dictionary = metrics_dictionary.get("dataset", {})
    metrics_split_dictionary = metrics_dictionary.get("dataset_split", {})
    training_dataset_dictionary = training_config.get("dataset", {})
    return str(
        metrics_dataset_dictionary.get("input_mode")
        or metrics_split_dictionary.get("input_mode")
        or training_dataset_dictionary.get("input_mode")
        or run_dictionary.get("input_mode")
        or "setpoints"
    )


def copy_run_provenance(output_directory: Path, destination_root: Path) -> dict[str, str]:

    """Reference source-run provenance without duplicating campaign artifacts."""

    source_target_map = {
        "training_config.snapshot.yaml": output_directory / COMMON_TRAINING_CONFIG_FILENAME,
        "metrics_summary.snapshot.yaml": output_directory / COMMON_METRICS_FILENAME,
        "run_metadata.snapshot.yaml": output_directory / COMMON_RUN_METADATA_FILENAME,
        "training_test_report.snapshot.md": output_directory / COMMON_RUN_REPORT_FILENAME,
    }
    optional_pointer_path = output_directory / "best_checkpoint_path.txt"
    if optional_pointer_path.exists():
        source_target_map["best_checkpoint_path.snapshot.txt"] = optional_pointer_path

    copied_path_map: dict[str, str] = {}
    for target_name, source_path in source_target_map.items():
        if not source_path.exists():
            continue
        copied_path_map[target_name] = format_project_relative_path(source_path)
    return copied_path_map


def link_or_copy_python_artifact(source_path: Path, destination_path: Path) -> None:

    """Create a repository-local checkpoint reference without duplicating large files."""

    destination_path.parent.mkdir(parents=True, exist_ok=True)
    if destination_path.exists() or destination_path.is_symlink():
        destination_path.unlink()

    try:
        relative_source_path = os.path.relpath(source_path, start=destination_path.parent)
        destination_path.symlink_to(relative_source_path)
    except OSError:
        shutil.copy2(source_path, destination_path)


def archive_one_run(
    archive_record: dict[str, Any],
    output_root: Path,
    expected_dataset_id: str,
    expected_input_mode: str,
    onnx_timeout_seconds: int,
    skip_existing: bool,
) -> dict[str, Any]:

    """Archive Python, ONNX, and provenance artifacts for one run."""

    run_dictionary = archive_record["run_dictionary"]
    metrics_dictionary = archive_record["metrics_dictionary"]
    output_directory = archive_record["output_directory"]
    best_checkpoint_path = archive_record["best_checkpoint_path"]
    surface = str(archive_record["surface"])
    training_config = load_training_config(output_directory)
    dataset_dictionary = metrics_dictionary["dataset"]
    archive_input_mode = resolve_archive_input_mode(run_dictionary, metrics_dictionary, training_config)
    assert dataset_dictionary["dataset_id"] == expected_dataset_id, (
        f"Dataset mismatch during archive | {dataset_dictionary['dataset_id']} vs {expected_dataset_id}"
    )
    assert archive_input_mode == expected_input_mode, (
        f"Input-mode mismatch during archive | {archive_input_mode} vs {expected_input_mode}"
    )
    model_family = str(metrics_dictionary["experiment"].get("base_model_family") or metrics_dictionary["comparison_payload"]["model_family"])
    run_name = str(run_dictionary.get("run_name") or metrics_dictionary["experiment"]["run_name"])
    run_instance_id = str(metrics_dictionary["experiment"]["run_instance_id"])

    archive_root = output_root / model_family / surface / run_instance_id
    existing_inventory_path = archive_root / "reference_inventory.yaml"
    if skip_existing and existing_inventory_path.exists():
        existing_inventory = load_yaml_dictionary(existing_inventory_path)
        if existing_inventory.get("onnx_export_status") == "exported":
            return dict(existing_inventory)

    if archive_root.exists():
        shutil.rmtree(archive_root)
    python_root = archive_root / "python"
    onnx_root = archive_root / "onnx"
    python_root.mkdir(parents=True, exist_ok=True)
    onnx_root.mkdir(parents=True, exist_ok=True)

    python_artifact_path = python_root / best_checkpoint_path.name
    link_or_copy_python_artifact(best_checkpoint_path, python_artifact_path)

    onnx_output_path = onnx_root / "model.onnx"
    model_type = str(metrics_dictionary["comparison_payload"]["model_type"]).strip().lower()
    export_status, export_error = export_model_to_onnx_with_timeout(
        model_type=model_type,
        training_config=training_config,
        python_model_path=best_checkpoint_path,
        onnx_output_path=onnx_output_path,
        timeout_seconds=onnx_timeout_seconds,
    )
    if export_status != "exported" and onnx_output_path.exists():
        onnx_output_path.unlink()

    source_run_snapshot_path_map = copy_run_provenance(output_directory, archive_root)
    inventory_dictionary = {
        "schema_version": 1,
        "dataset_id": metrics_dictionary["dataset"]["dataset_id"],
        "dataset_schema": metrics_dictionary["dataset"]["dataset_schema"],
        "input_mode": archive_input_mode,
        "model_family": model_family,
        "model_type": model_type,
        "surface": surface,
        "run_name": run_name,
        "run_instance_id": run_instance_id,
        "source_output_directory": format_project_relative_path(output_directory),
        "source_best_checkpoint_path": format_project_relative_path(best_checkpoint_path),
        "python_model_path": format_project_relative_path(python_artifact_path),
        "onnx_model_path": format_project_relative_path(onnx_output_path) if onnx_output_path.exists() else "N/A",
        "onnx_export_status": export_status,
        "onnx_export_error": export_error,
        "source_run_snapshot_path_map": source_run_snapshot_path_map,
        "metrics": {
            "val_mae": metrics_dictionary["comparison_payload"].get("val_mae"),
            "test_mae": metrics_dictionary["comparison_payload"].get("test_mae"),
            "test_rmse": metrics_dictionary["comparison_payload"].get("test_rmse"),
        },
    }
    save_yaml_dictionary(archive_root / "reference_inventory.yaml", inventory_dictionary)
    return inventory_dictionary


def write_dataset_export_summary(
    output_root: Path,
    dataset_id: str,
    input_mode: str,
    archive_entry_list: list[dict[str, Any]],
) -> None:

    """Write dataset export summary."""

    surface_counts: dict[str, int] = {"global": 0, "forward": 0, "backward": 0}
    status_counts: dict[str, int] = {}
    for entry in archive_entry_list:
        surface = str(entry["surface"])
        surface_counts[surface] = surface_counts.get(surface, 0) + 1
        status = str(entry["onnx_export_status"])
        status_counts[status] = status_counts.get(status, 0) + 1

    save_yaml_dictionary(
        output_root / "model_development_export_inventory.yaml",
        {
            "schema_version": 1,
            "dataset_id": dataset_id,
            "input_mode": input_mode,
            "entry_count": len(archive_entry_list),
            "surface_counts": surface_counts,
            "onnx_export_status_counts": status_counts,
            "entries": archive_entry_list,
        },
    )


def main() -> None:

    """Run the dataset-first export workflow."""

    arguments = parse_command_line_arguments()
    manifest_path_list = [resolve_project_path(path) for path in arguments.campaign_manifest]
    output_root = resolve_project_path(arguments.output_root or f"models/{arguments.dataset_id}/{arguments.input_mode}/exported")
    archive_run_list = build_archive_run_list(manifest_path_list, arguments.dataset_id, arguments.input_mode)
    surface_counts: dict[str, int] = {"global": 0, "forward": 0, "backward": 0}
    for archive_record in archive_run_list:
        surface = str(archive_record["surface"])
        surface_counts[surface] = surface_counts.get(surface, 0) + 1

    print(f"[INFO] Dataset: {arguments.dataset_id}")
    print(f"[INFO] Input mode: {arguments.input_mode}")
    print(f"[INFO] Runs: {len(archive_run_list)}")
    print(f"[INFO] Surface counts: {surface_counts}")
    if not arguments.export:
        return

    archive_entry_list = []
    for index, archive_record in enumerate(archive_run_list, start=1):
        run_name = str(archive_record["run_dictionary"].get("run_name", "unknown"))
        print(f"[INFO] Exporting {index}/{len(archive_run_list)} | {run_name}")
        archive_entry_list.append(
            archive_one_run(
                archive_record,
                output_root,
                expected_dataset_id=arguments.dataset_id,
                expected_input_mode=arguments.input_mode,
                onnx_timeout_seconds=int(arguments.onnx_timeout_seconds),
                skip_existing=bool(arguments.skip_existing),
            )
        )
    write_dataset_export_summary(output_root, arguments.dataset_id, arguments.input_mode, archive_entry_list)
    print(f"[DONE] Dataset export archive: {format_project_relative_path(output_root)}")


if __name__ == "__main__":
    main()
