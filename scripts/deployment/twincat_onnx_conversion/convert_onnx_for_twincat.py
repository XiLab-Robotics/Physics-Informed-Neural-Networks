"""Convert exported ONNX models into TwinCAT-facing Beckhoff artifacts."""

from __future__ import annotations

import argparse, hashlib, json, shutil, subprocess, sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import onnx
import yaml
from onnx import TensorProto, numpy_helper

try: import onnxruntime as ort
except ImportError as import_error: ort, ONNXRUNTIME_IMPORT_ERROR = None, import_error
else: ONNXRUNTIME_IMPORT_ERROR = None


PROJECT_PATH = Path(__file__).resolve().parents[3]
DEFAULT_TOOLBOX_ROOT = Path(__file__).resolve().parent / "ModelManagerAPI"
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "deployment" / "twincat_onnx_conversion"
DEFAULT_MODEL_PATH = (
    PROJECT_PATH
    / "models"
    / "polished_dataset"
    / "actual_values"
    / "exported"
    / "feedforward"
    / "forward"
    / "2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values"
    / "onnx"
    / "model.onnx"
)
INT64_MAX_VALUE = np.iinfo(np.int64).max
REQUIRED_BECKHOFF_RUNTIME_FILE_LIST = ["mllib_um.dll"]
KNOWN_BECKHOFF_RUNTIME_FILE_LIST = [
    "MLAIPlugin.dll",
    "mllib_um.dll",
    "mllib_um32.dll",
    "ML_TcCOM_Extension.dll",
    "ML_TcCOM_Extension.dll.config",
]
FLOAT_TENSOR_TYPES = {
    TensorProto.FLOAT: np.float32,
    TensorProto.DOUBLE: np.float64,
    TensorProto.FLOAT16: np.float16,
}
INTEGER_TENSOR_TYPES = {
    TensorProto.INT64: np.int64,
    TensorProto.INT32: np.int32,
    TensorProto.INT16: np.int16,
    TensorProto.INT8: np.int8,
    TensorProto.UINT64: np.uint64,
    TensorProto.UINT32: np.uint32,
    TensorProto.UINT16: np.uint16,
    TensorProto.UINT8: np.uint8,
}


@dataclass(frozen=True)
class CommandResult:

    """Store one Beckhoff command execution result."""

    name: str
    command: list[str]
    return_code: int
    stdout_path: Path
    stderr_path: Path

    @property
    def succeeded(self) -> bool:

        """Return whether the command completed successfully."""

        return self.return_code == 0


def parse_arguments() -> argparse.Namespace:

    """Parse command line arguments."""

    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("--onnx", type=Path, default=DEFAULT_MODEL_PATH, help="Source ONNX model path.")
    argument_parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT, help="Root directory for conversion runs.")
    argument_parser.add_argument("--toolbox-root", type=Path, default=DEFAULT_TOOLBOX_ROOT, help="Directory containing mllib_toolbox.exe.")
    argument_parser.add_argument("--run-name", default=None, help="Optional explicit conversion run directory name.")
    argument_parser.add_argument("--skip-tf38x0", action="store_true", help="Skip XML/BML generation for the TF38x0 runtime.")
    argument_parser.add_argument("--prepare-tf3820", action="store_true", help="Also run Beckhoff onnxprep for TF3820 Machine Learning Server artifacts.")
    argument_parser.add_argument("--run-onnxruntime-smoke", action="store_true", help="Run a CPU ONNX Runtime smoke inference before Beckhoff conversion.")
    argument_parser.add_argument("--copy-source-onnx", action="store_true", help="Copy the source ONNX into the conversion output directory.")
    argument_parser.add_argument("--fail-fast", action="store_true", help="Stop after the first failed Beckhoff command.")
    return argument_parser.parse_args()


def resolve_path(path: Path) -> Path:

    """Resolve a path relative to the project root when needed."""

    if path.is_absolute(): return path
    return (PROJECT_PATH / path).resolve()


def project_relative(path: Path) -> str:

    """Return a stable project-relative path string when possible."""

    resolved_path = path.resolve()
    try: return str(resolved_path.relative_to(PROJECT_PATH)).replace("\\", "/")
    except ValueError: return str(resolved_path)


def compute_sha256(file_path: Path) -> str:

    """Compute the SHA-256 hash of a file."""

    hash_object = hashlib.sha256()
    with file_path.open("rb") as file_handle:
        for chunk in iter(lambda: file_handle.read(1024 * 1024), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()


def create_run_directory(output_root: Path, onnx_path: Path, run_name: str | None) -> Path:

    """Create the timestamped conversion run directory."""

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    source_slug = onnx_path.parent.parent.name if onnx_path.parent.name == "onnx" else onnx_path.stem
    directory_name = run_name or f"{timestamp}_{source_slug}"
    run_directory = output_root / directory_name
    run_directory.mkdir(parents=True, exist_ok=False)
    (run_directory / "logs").mkdir(parents=True, exist_ok=True)
    return run_directory


def shape_dimension_to_value(dimension: Any) -> dict[str, Any]:

    """Convert one ONNX shape dimension into a serializable record."""

    if dimension.HasField("dim_value"): return {"kind": "static", "value": int(dimension.dim_value)}
    if dimension.HasField("dim_param"): return {"kind": "dynamic", "value": dimension.dim_param}
    return {"kind": "unknown", "value": None}


def value_info_to_record(value_info: Any) -> dict[str, Any]:

    """Convert an ONNX ValueInfoProto into a serializable record."""

    tensor_type = value_info.type.tensor_type
    return {
        "name": value_info.name,
        "element_type": int(tensor_type.elem_type),
        "element_type_name": TensorProto.DataType.Name(tensor_type.elem_type),
        "shape": [shape_dimension_to_value(dimension) for dimension in tensor_type.shape.dim],
    }


def collect_constant_records(model: Any) -> list[dict[str, Any]]:

    """Collect ONNX Constant node tensor attributes relevant to Beckhoff parsing."""

    constant_record_list: list[dict[str, Any]] = []
    for node_index, node in enumerate(model.graph.node):
        if node.op_type != "Constant": continue
        for attribute in node.attribute:
            if attribute.name != "value" or not attribute.HasField("t"): continue
            tensor = attribute.t
            try: array = numpy_helper.to_array(tensor)
            except Exception as read_error:
                constant_record_list.append({
                    "node_index": node_index,
                    "node_name": node.name,
                    "output": list(node.output),
                    "read_error": str(read_error),
                })
                continue
            flat_array = array.reshape(-1) if array.size else array
            contains_int64_max = bool(array.dtype == np.int64 and np.any(array == INT64_MAX_VALUE))
            constant_record_list.append({
                "node_index": node_index,
                "node_name": node.name,
                "output": list(node.output),
                "onnx_dtype": TensorProto.DataType.Name(tensor.data_type),
                "numpy_dtype": str(array.dtype),
                "shape": list(array.shape),
                "contains_int64_max": contains_int64_max,
                "preview": [int(value) if np.issubdtype(array.dtype, np.integer) else float(value) for value in flat_array[:12]],
            })
    return constant_record_list


def inspect_onnx_model(onnx_path: Path) -> dict[str, Any]:

    """Inspect an ONNX model and return a serializable compatibility summary."""

    model = onnx.load(str(onnx_path), load_external_data=True)
    checker_status = "passed"
    checker_error = ""
    try: onnx.checker.check_model(model)
    except onnx.checker.ValidationError as validation_error:
        checker_status = "failed"
        checker_error = str(validation_error)

    input_record_list = [value_info_to_record(value_info) for value_info in model.graph.input]
    output_record_list = [value_info_to_record(value_info) for value_info in model.graph.output]
    operator_histogram = dict(sorted(Counter(node.op_type for node in model.graph.node).items()))
    constant_record_list = collect_constant_records(model)
    dynamic_shape_count = sum(
        1
        for value_record in [*input_record_list, *output_record_list]
        for dimension_record in value_record["shape"]
        if dimension_record["kind"] != "static"
    )
    int64_max_constant_list = [record for record in constant_record_list if record.get("contains_int64_max")]
    route = "tf38x0_candidate"
    route_reason_list = []
    if checker_status != "passed":
        route = "inspection_only"
        route_reason_list.append("ONNX checker failed.")
    if dynamic_shape_count:
        route_reason_list.append("Dynamic dimensions are present; TF3820 allows only leading dynamic batch dimensions.")
    if int64_max_constant_list:
        route_reason_list.append("INT64_MAX Constant nodes detected; Beckhoff MLlib may reject open Slice sentinels.")

    return {
        "source_onnx_path": project_relative(onnx_path),
        "source_onnx_sha256": compute_sha256(onnx_path),
        "source_onnx_size_bytes": onnx_path.stat().st_size,
        "ir_version": int(model.ir_version),
        "opset_imports": [{"domain": entry.domain or "ai.onnx", "version": int(entry.version)} for entry in model.opset_import],
        "checker_status": checker_status,
        "checker_error": checker_error,
        "inputs": input_record_list,
        "outputs": output_record_list,
        "node_count": len(model.graph.node),
        "initializer_count": len(model.graph.initializer),
        "operator_histogram": operator_histogram,
        "dynamic_shape_count": dynamic_shape_count,
        "int64_max_constant_count": len(int64_max_constant_list),
        "int64_max_constant_nodes": int64_max_constant_list,
        "constant_nodes": constant_record_list,
        "recommended_route": route,
        "route_notes": route_reason_list,
    }


def resolve_numpy_dtype(element_type: int) -> np.dtype:

    """Resolve an ONNX tensor element type into a NumPy dtype for smoke input."""

    if element_type in FLOAT_TENSOR_TYPES: return np.dtype(FLOAT_TENSOR_TYPES[element_type])
    if element_type in INTEGER_TENSOR_TYPES: return np.dtype(INTEGER_TENSOR_TYPES[element_type])
    raise ValueError(f"Unsupported ONNX Runtime smoke input type: {TensorProto.DataType.Name(element_type)}")


def resolve_smoke_shape(shape_record_list: list[dict[str, Any]]) -> tuple[int, ...]:

    """Resolve a concrete smoke-test shape from ONNX input metadata."""

    resolved_shape = []
    for dimension_index, dimension_record in enumerate(shape_record_list):
        if dimension_record["kind"] == "static" and dimension_record["value"] not in (0, None):
            resolved_shape.append(int(dimension_record["value"]))
        else:
            resolved_shape.append(1 if dimension_index == 0 else 2)
    return tuple(resolved_shape)


def run_onnxruntime_smoke(onnx_path: Path, inspection_summary: dict[str, Any]) -> dict[str, Any]:

    """Run one CPU ONNX Runtime inference with synthetic inputs."""

    if ort is None:
        return {"status": "skipped", "reason": f"onnxruntime import failed: {ONNXRUNTIME_IMPORT_ERROR}"}

    session = ort.InferenceSession(str(onnx_path), providers=["CPUExecutionProvider"])
    random_generator = np.random.default_rng(seed=12345)
    input_feed = {}
    input_summary_list = []
    for input_metadata, input_record in zip(session.get_inputs(), inspection_summary["inputs"]):
        numpy_dtype = resolve_numpy_dtype(input_record["element_type"])
        smoke_shape = resolve_smoke_shape(input_record["shape"])
        if np.issubdtype(numpy_dtype, np.floating):
            input_array = random_generator.normal(size=smoke_shape).astype(numpy_dtype)
        else:
            input_array = random_generator.integers(low=0, high=3, size=smoke_shape).astype(numpy_dtype)
        input_feed[input_metadata.name] = input_array
        input_summary_list.append({"name": input_metadata.name, "shape": list(input_array.shape), "dtype": str(input_array.dtype)})

    output_list = session.run(None, input_feed)
    return {
        "status": "passed",
        "provider_list": session.get_providers(),
        "inputs": input_summary_list,
        "outputs": [
            {"index": index, "shape": list(output.shape), "dtype": str(output.dtype)}
            for index, output in enumerate(output_list)
        ],
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:

    """Write pretty JSON to disk."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_yaml(path: Path, payload: dict[str, Any]) -> None:

    """Write readable YAML to disk."""

    class NoAliasDumper(yaml.SafeDumper):

        """Disable YAML anchors for operator-facing manifests."""

        def ignore_aliases(self, data: Any) -> bool:

            """Return true so PyYAML emits repeated values inline."""

            return True

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.dump(payload, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False), encoding="utf-8")


def run_beckhoff_command(command_name: str, command: list[str], log_directory: Path) -> CommandResult:

    """Run one Beckhoff toolbox command and persist stdout and stderr."""

    stdout_path = log_directory / f"{command_name}.stdout.log"
    stderr_path = log_directory / f"{command_name}.stderr.log"
    completed_process = subprocess.run(command, cwd=Path(command[0]).parent, text=True, capture_output=True, check=False)
    stdout_path.write_text(completed_process.stdout, encoding="utf-8")
    stderr_path.write_text(completed_process.stderr, encoding="utf-8")
    return CommandResult(command_name, command, completed_process.returncode, stdout_path, stderr_path)


def command_result_to_record(command_result: CommandResult) -> dict[str, Any]:

    """Convert a command result into a manifest record."""

    return {
        "name": command_result.name,
        "command": command_result.command,
        "return_code": command_result.return_code,
        "succeeded": command_result.succeeded,
        "stdout_path": project_relative(command_result.stdout_path),
        "stderr_path": project_relative(command_result.stderr_path),
    }


def load_reference_inventory(onnx_path: Path) -> dict[str, Any] | None:

    """Load the nearest model reference inventory when available."""

    for parent_path in onnx_path.parents:
        inventory_path = parent_path / "reference_inventory.yaml"
        if inventory_path.exists():
            with inventory_path.open("r", encoding="utf-8") as file_handle:
                return yaml.safe_load(file_handle)
    return None


def inspect_beckhoff_toolbox(toolbox_root: Path) -> dict[str, Any]:

    """Inspect whether the recovered Beckhoff toolbox is runnable."""

    toolbox_executable = toolbox_root / "mllib_toolbox.exe"
    missing_file_list = [
        runtime_file_name
        for runtime_file_name in REQUIRED_BECKHOFF_RUNTIME_FILE_LIST
        if not (toolbox_root / runtime_file_name).exists()
    ]
    detected_runtime_file_list = [
        runtime_file_name
        for runtime_file_name in KNOWN_BECKHOFF_RUNTIME_FILE_LIST
        if (toolbox_root / runtime_file_name).exists()
    ]
    return {
        "toolbox_root": project_relative(toolbox_root),
        "toolbox_executable": project_relative(toolbox_executable),
        "toolbox_executable_exists": toolbox_executable.exists(),
        "required_runtime_file_list": REQUIRED_BECKHOFF_RUNTIME_FILE_LIST,
        "detected_runtime_file_list": detected_runtime_file_list,
        "missing_runtime_file_list": missing_file_list,
        "status": "ready" if toolbox_executable.exists() and not missing_file_list else "missing_runtime_dependency",
    }


def run_tf38x0_conversion(toolbox_executable: Path, onnx_path: Path, run_directory: Path, fail_fast: bool) -> dict[str, Any]:

    """Run the TF38x0 XML/BML conversion path."""

    output_directory = run_directory / "tf38x0"
    log_directory = run_directory / "logs"
    output_directory.mkdir(parents=True, exist_ok=True)
    xml_output_path = output_directory / "model.xml"
    bml_output_path = output_directory / "model.bml"
    info_output_path = output_directory / "info.txt"

    result_list = []
    command_sequence = [
        ("tf38x0_onnximport_xml", [str(toolbox_executable), "onnximport", str(onnx_path), str(xml_output_path)]),
        ("tf38x0_store_bml", [str(toolbox_executable), "store", str(xml_output_path), str(bml_output_path)]),
        ("tf38x0_info_xml", [str(toolbox_executable), "info", str(xml_output_path)]),
    ]
    for command_name, command in command_sequence:
        if command_name != "tf38x0_onnximport_xml" and not xml_output_path.exists():
            break
        command_result = run_beckhoff_command(command_name, command, log_directory)
        result_list.append(command_result)
        if command_name == "tf38x0_info_xml" and command_result.stdout_path.exists():
            info_output_path.write_text(command_result.stdout_path.read_text(encoding="utf-8"), encoding="utf-8")
        if not command_result.succeeded and fail_fast:
            break

    return {
        "status": "completed" if result_list and all(result.succeeded for result in result_list[:2]) else "failed",
        "xml_output_path": project_relative(xml_output_path) if xml_output_path.exists() else None,
        "bml_output_path": project_relative(bml_output_path) if bml_output_path.exists() else None,
        "info_output_path": project_relative(info_output_path) if info_output_path.exists() else None,
        "commands": [command_result_to_record(result) for result in result_list],
    }


def run_tf3820_preparation(toolbox_executable: Path, onnx_path: Path, run_directory: Path) -> dict[str, Any]:

    """Run the TF3820 Machine Learning Server preparation path."""

    output_directory = run_directory / "tf3820"
    output_directory.mkdir(parents=True, exist_ok=True)
    json_output_path = output_directory / "model.json"
    command = [str(toolbox_executable), "onnxprep", str(onnx_path), str(json_output_path)]
    command_result = run_beckhoff_command("tf3820_onnxprep", command, run_directory / "logs")
    generated_file_list = [project_relative(path) for path in output_directory.glob("*")]
    return {
        "status": "completed" if command_result.succeeded else "failed",
        "json_output_path": project_relative(json_output_path) if json_output_path.exists() else None,
        "generated_file_list": generated_file_list,
        "commands": [command_result_to_record(command_result)],
    }


def main() -> int:

    """Run the TwinCAT conversion workflow."""

    arguments = parse_arguments()
    onnx_path = resolve_path(arguments.onnx)
    output_root = resolve_path(arguments.output_root)
    toolbox_root = resolve_path(arguments.toolbox_root)
    toolbox_executable = toolbox_root / "mllib_toolbox.exe"

    if not onnx_path.exists():
        raise FileNotFoundError(f"ONNX model not found: {onnx_path}")
    beckhoff_toolbox_status = inspect_beckhoff_toolbox(toolbox_root)
    if not toolbox_executable.exists():
        raise FileNotFoundError(f"Beckhoff toolbox executable not found: {toolbox_executable}")

    run_directory = create_run_directory(output_root, onnx_path, arguments.run_name)
    print(f"Conversion output: {project_relative(run_directory)}")

    inspection_summary = inspect_onnx_model(onnx_path)
    write_json(run_directory / "inspection_summary.json", inspection_summary)
    beckhoff_input_path = run_directory / "source_model.onnx"
    shutil.copy2(onnx_path, beckhoff_input_path)

    onnxruntime_smoke = None
    if arguments.run_onnxruntime_smoke:
        onnxruntime_smoke = run_onnxruntime_smoke(onnx_path, inspection_summary)
        write_json(run_directory / "onnxruntime_smoke.json", onnxruntime_smoke)

    reference_inventory = load_reference_inventory(onnx_path)
    conversion_manifest: dict[str, Any] = {
        "schema_version": 1,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source_onnx_path": project_relative(onnx_path),
        "source_onnx_sha256": inspection_summary["source_onnx_sha256"],
        "beckhoff_input_onnx_path": project_relative(beckhoff_input_path),
        "output_directory": project_relative(run_directory),
        "toolbox_executable": project_relative(toolbox_executable),
        "beckhoff_toolbox_status": beckhoff_toolbox_status,
        "inspection_summary_path": project_relative(run_directory / "inspection_summary.json"),
        "onnxruntime_smoke_path": project_relative(run_directory / "onnxruntime_smoke.json") if onnxruntime_smoke else None,
        "onnxruntime_smoke_status": onnxruntime_smoke["status"] if onnxruntime_smoke else "not_requested",
        "reference_inventory": reference_inventory,
        "tf38x0": {"status": "skipped"},
        "tf3820": {"status": "skipped"},
    }

    if not arguments.skip_tf38x0 and beckhoff_toolbox_status["status"] != "ready":
        conversion_manifest["tf38x0"] = {
            "status": "missing_runtime_dependency",
            "missing_runtime_file_list": beckhoff_toolbox_status["missing_runtime_file_list"],
            "note": "Beckhoff conversion was not executed because the recovered toolbox copy is missing required runtime files.",
        }
    elif not arguments.skip_tf38x0:
        conversion_manifest["tf38x0"] = run_tf38x0_conversion(toolbox_executable, beckhoff_input_path, run_directory, arguments.fail_fast)
    if arguments.prepare_tf3820 and beckhoff_toolbox_status["status"] != "ready":
        conversion_manifest["tf3820"] = {
            "status": "missing_runtime_dependency",
            "missing_runtime_file_list": beckhoff_toolbox_status["missing_runtime_file_list"],
            "note": "TF3820 preparation was not executed because the recovered toolbox copy is missing required runtime files.",
        }
    elif arguments.prepare_tf3820:
        conversion_manifest["tf3820"] = run_tf3820_preparation(toolbox_executable, beckhoff_input_path, run_directory)

    write_yaml(run_directory / "conversion_manifest.yaml", conversion_manifest)
    print(f"Manifest: {project_relative(run_directory / 'conversion_manifest.yaml')}")

    failed_status_list = [
        route_payload["status"]
        for route_payload in [conversion_manifest["tf38x0"], conversion_manifest["tf3820"]]
        if route_payload["status"] in {"failed", "missing_runtime_dependency"}
    ]
    return 1 if failed_status_list else 0


if __name__ == "__main__":
    sys.exit(main())
