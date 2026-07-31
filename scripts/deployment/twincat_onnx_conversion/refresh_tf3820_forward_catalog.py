"""Refresh the maintained TF3820 catalog from canonical forward models."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

import yaml

from build_tf3820_standalone_harness import discover_models, wrap_tc_dut


PROJECT_PATH = Path(__file__).resolve().parents[3]
DEFAULT_SOURCE_ROOT = PROJECT_PATH / "models" / "polished_dataset" / "setpoints"
DEFAULT_MATRIX_ROOT = (
    PROJECT_PATH
    / "output"
    / "deployment"
    / "twincat_onnx_conversion"
    / "forward_polished_setpoints_20260731"
)
DEFAULT_TARGET_ROOT = (
    PROJECT_PATH
    / "reference"
    / "codes"
    / "TwinCAT_TF3820_StandaloneModelTest"
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    argument_parser.add_argument("--matrix-root", type=Path, default=DEFAULT_MATRIX_ROOT)
    argument_parser.add_argument("--target-root", type=Path, default=DEFAULT_TARGET_ROOT)
    argument_parser.add_argument("--surface", default="forward")
    return argument_parser.parse_args()


def resolve_path(path: Path) -> Path:
    """Resolve a path relative to the repository root."""

    return path.resolve() if path.is_absolute() else (PROJECT_PATH / path).resolve()


def compute_sha256(path: Path) -> str:
    """Return the SHA-256 digest of one file."""

    hash_object = hashlib.sha256()
    with path.open("rb") as file_handle:
        for chunk in iter(lambda: file_handle.read(1024 * 1024), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()


def project_relative(path: Path) -> str:
    """Return a stable repository-relative path."""

    return str(path.resolve().relative_to(PROJECT_PATH)).replace("\\", "/")


def load_catalog(path: Path) -> dict:
    """Load and validate the maintained model catalog."""

    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("model_list"), list):
        raise ValueError(f"Invalid model catalog: {path}")
    return payload


def load_conversion_manifest(model_source_directory: Path) -> dict:
    """Load the converter manifest associated with one prepared family."""

    manifest_path = model_source_directory / "conversion_manifest.yaml"
    payload = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Invalid conversion manifest: {manifest_path}")
    return payload


def patch_temporal_direction_input(runner_path: Path, tensor_name: str) -> bool:
    """Add the fifth temporal direction feature when the refreshed model needs it."""

    runner_text = runner_path.read_text(encoding="utf-8")
    direction_history_line = (
        f"stModelInput.{tensor_name}[0,nSequenceIndex,4]:= "
        "stTemporalHistory.aDirectionFlag[nSequenceIndex];"
    )
    direction_point_line = f"stModelInput.{tensor_name}[0,nSequenceIndex,4] := fDirectionFlag;"
    if direction_history_line in runner_text and direction_point_line in runner_text:
        return False

    temperature_history_line = (
        f"stModelInput.{tensor_name}[0,nSequenceIndex,3]:= "
        "stTemporalHistory.aTemperature[nSequenceIndex];"
    )
    temperature_point_line = f"stModelInput.{tensor_name}[0,nSequenceIndex,3] := fTemperature;"
    if runner_text.count(temperature_history_line) != 1:
        raise ValueError(f"Expected one temporal-history temperature assignment in {runner_path}")
    if runner_text.count(temperature_point_line) != 1:
        raise ValueError(f"Expected one fallback temperature assignment in {runner_path}")

    runner_text = runner_text.replace(
        temperature_history_line,
        temperature_history_line + "\n\t\t\t\t\t" + direction_history_line,
    )
    runner_text = runner_text.replace(
        temperature_point_line,
        temperature_point_line + "\n\t\t\t\t\t" + direction_point_line,
    )
    runner_path.write_text(runner_text, encoding="utf-8", newline="")
    return True


def refresh_catalog(source_root: Path, matrix_root: Path, target_root: Path, surface: str) -> None:
    """Validate, copy, and synchronize the maintained TF3820 family catalog."""

    source_root = resolve_path(source_root)
    matrix_root = resolve_path(matrix_root)
    target_root = resolve_path(target_root)
    expected_target_root = DEFAULT_TARGET_ROOT.resolve()
    if target_root != expected_target_root:
        raise ValueError(f"Refusing unexpected maintained target root: {target_root}")

    model_entry_list = discover_models(matrix_root)
    source_family_list = sorted(path.name for path in source_root.iterdir() if path.is_dir())
    prepared_family_list = sorted(model.family_id for model in model_entry_list)
    if source_family_list != prepared_family_list:
        raise ValueError(
            "Prepared TF3820 families do not match the canonical source inventory: "
            f"source={source_family_list}, prepared={prepared_family_list}"
        )

    catalog_path = target_root / "model_catalog.json"
    catalog_payload = load_catalog(catalog_path)
    existing_record_map = {record["family_id"]: record for record in catalog_payload["model_list"]}
    missing_plc_family_list = sorted(set(prepared_family_list) - set(existing_record_map))
    if missing_plc_family_list:
        raise ValueError(
            "New canonical families require explicit PLC enum and dispatch design before refresh: "
            + ", ".join(missing_plc_family_list)
        )

    removed_family_list = sorted(set(existing_record_map) - set(prepared_family_list))
    model_root = target_root / "ML_models"
    dut_root = target_root / "PLC_project" / "DUTs"
    runner_root = target_root / "PLC_project" / "POUs" / "Model Runners"
    refreshed_record_list = []
    patched_runner_list = []

    for model in model_entry_list:
        source_onnx_path = source_root / model.family_id / surface / "onnx" / "model.onnx"
        if not source_onnx_path.is_file():
            raise FileNotFoundError(f"Missing canonical source ONNX: {source_onnx_path}")
        source_onnx_sha256 = compute_sha256(source_onnx_path)
        conversion_manifest = load_conversion_manifest(model.source_directory)
        if conversion_manifest.get("source_onnx_sha256") != source_onnx_sha256:
            raise ValueError(f"Conversion manifest source hash mismatch: {model.family_id}")
        if conversion_manifest.get("onnxruntime_smoke_status") != "passed":
            raise ValueError(f"ONNX Runtime smoke did not pass: {model.family_id}")
        tf3820_payload = conversion_manifest.get("tf3820", {})
        if not isinstance(tf3820_payload, dict) or tf3820_payload.get("status") != "completed":
            raise ValueError(f"TF3820 preparation did not complete: {model.family_id}")

        destination_model_root = model_root / model.family_id
        destination_model_root.mkdir(parents=True, exist_ok=True)
        shutil.copy2(model.model_onnx_path, destination_model_root / "model.onnx")
        shutil.copy2(model.model_json_path, destination_model_root / "model.json")
        shutil.copy2(model.model_plcopen_path, destination_model_root / "model_plcopen.xml")

        (dut_root / f"{model.input_type_name}.TcDUT").write_text(
            wrap_tc_dut(model.input_type_name, model.input_type_declaration).rstrip() + "\n",
            encoding="utf-8",
            newline="",
        )
        (dut_root / f"{model.output_type_name}.TcDUT").write_text(
            wrap_tc_dut(model.output_type_name, model.output_type_declaration).rstrip() + "\n",
            encoding="utf-8",
            newline="",
        )

        runner_path = runner_root / f"{model.runner_name}.TcPOU"
        if not runner_path.is_file():
            raise FileNotFoundError(f"Missing maintained PLC runner: {runner_path}")
        if model.input_shape == (1, 33, 5):
            if patch_temporal_direction_input(runner_path, model.input_tensor_name):
                patched_runner_list.append(model.runner_name)

        record = dict(existing_record_map[model.family_id])
        record["input_shape"] = list(model.input_shape)
        record["output_shape"] = list(model.output_shape)
        record["source_onnx_path"] = project_relative(source_onnx_path)
        record["source_onnx_sha256"] = source_onnx_sha256
        record["prepared_onnx_sha256"] = compute_sha256(model.model_onnx_path)
        record["target_json_path"] = (
            "C:\\Users\\Administrator\\Documents\\ML_Models\\"
            + model.family_id
            + "\\model.json"
        )
        refreshed_record_list.append(record)

    for family_id in removed_family_list:
        record = existing_record_map[family_id]
        destination_model_root = model_root / family_id
        if destination_model_root.is_dir():
            shutil.rmtree(destination_model_root)
        for type_suffix in ("Input", "Output"):
            dut_path = dut_root / f"ST_{record['runner_name'].removeprefix('FB_').removesuffix('Tf3820Runner')}{type_suffix}.TcDUT"
            if dut_path.is_file():
                dut_path.unlink()
        runner_path = runner_root / f"{record['runner_name']}.TcPOU"
        if runner_path.is_file():
            runner_path.unlink()

    catalog_payload["schema_version"] = 2
    catalog_payload["model_count"] = len(refreshed_record_list)
    catalog_payload["source_root"] = project_relative(source_root)
    catalog_payload["surface"] = surface
    catalog_payload["model_list"] = refreshed_record_list
    catalog_path.write_text(json.dumps(catalog_payload, indent=2) + "\n", encoding="utf-8", newline="")

    print(f"[DONE] Refreshed TF3820 families: {len(refreshed_record_list)}")
    print(f"[DONE] Removed destination-only families: {removed_family_list}")
    print(f"[DONE] Patched five-feature temporal runners: {len(patched_runner_list)}")


def main() -> None:
    """Run the maintained-catalog refresh."""

    arguments = parse_arguments()
    refresh_catalog(
        source_root=arguments.source_root,
        matrix_root=arguments.matrix_root,
        target_root=arguments.target_root,
        surface=arguments.surface,
    )


if __name__ == "__main__":
    main()
