"""Run a representative TwinCAT ONNX compatibility matrix."""

from __future__ import annotations

import argparse, json, subprocess, sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


PROJECT_PATH = Path(__file__).resolve().parents[3]
CONVERTER_PATH = Path(__file__).resolve().with_name("convert_onnx_for_twincat.py")
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "deployment" / "twincat_onnx_conversion"
DEFAULT_MATRIX_ROOT = DEFAULT_OUTPUT_ROOT / "family_matrix"
SURFACE_PRIORITY_LIST = ["forward", "global", "backward"]
DATASET_BRANCH_PRIORITY_LIST = [
    PROJECT_PATH / "models" / "polished_dataset" / "actual_values" / "exported",
    PROJECT_PATH / "models" / "polished_dataset" / "setpoints" / "exported",
    PROJECT_PATH / "models" / "simplified_dataset" / "setpoints" / "exported",
    PROJECT_PATH / "models" / "polished_dataset" / "exported",
    PROJECT_PATH / "models" / "simplified_dataset" / "exported",
]
MODEL_FAMILY_LIST = [
    "rcim_track1",
    "tree",
    "residual_harmonic_mlp",
    "feedforward",
    "periodic_mlp",
    "harmonic_regression",
    "periodic_mlp_harmonic",
    "temporal_convolution",
    "gru_sequence",
    "lstm_sequence",
    "periodic_temporal_convolution",
    "periodic_gru_sequence",
    "periodic_lstm_sequence",
    "residual_harmonic_gru_sequence_sparse_rcim",
    "residual_harmonic_gru_sequence_dense240",
    "residual_harmonic_gru_sequence_dense360",
    "residual_harmonic_lstm_sequence_sparse_rcim",
    "residual_harmonic_lstm_sequence_dense240",
    "residual_harmonic_lstm_sequence_dense360",
    "wave3_1_sequential_residual_offset_probe",
    "wave3_2_clean_sequential_residual_offset",
    "wave3_2_harmonic_residual_offset",
    "wave3_3_curve_aware_pointwise_control",
    "wave3_3_raw_centered_shape_curve_aware",
    "wave3_3_raw_offset_curve_aware",
    "wave3_3_full_curve_composite",
    "wave4_1_mae_robust_loss",
    "wave4_1_smooth_l1_robust_loss",
    "wave4_1_log_cosh_robust_loss",
    "wave4_2_quantile_p10_p50_p90",
    "wave4_2_gaussian_nll",
    "wave4_3_mixture_density_k2",
    "wave4_3_mixture_density_k3",
    "wave4_4_gru_latent_offset_residual",
    "wave4_4_causal_tcn_latent_offset_residual",
    "wave5_1_harmonic_prior_pointwise_control",
    "wave5_1_harmonic_prior_smooth_l1_structured",
]
RCIM_REPRESENTATIVE_ROOT = PROJECT_PATH / "output" / "validation_checks" / "rcim_model_bank_reproduction"


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("--output-root", type=Path, default=DEFAULT_MATRIX_ROOT)
    argument_parser.add_argument("--family", action="append", default=[], help="Limit execution to one family. Repeatable.")
    argument_parser.add_argument("--skip-onnxruntime-smoke", action="store_true")
    argument_parser.add_argument("--skip-tf3820-fallback", action="store_true")
    argument_parser.add_argument("--continue-existing", action="store_true")
    return argument_parser.parse_args()


def project_relative(path: Path) -> str:

    """Return a project-relative path when possible."""

    resolved_path = path.resolve()
    try:
        return str(resolved_path.relative_to(PROJECT_PATH)).replace("\\", "/")
    except ValueError:
        return str(resolved_path)


def select_newest_model_path(path_list: list[Path]) -> Path | None:

    """Select the newest path by parent run folder name."""

    if not path_list:
        return None
    return sorted(path_list, key=lambda path: str(path.parent.parent), reverse=True)[0]


def find_family_representative(family_name: str) -> Path | None:

    """Find one ONNX representative for a model family."""

    if family_name == "rcim_track1":
        candidate_list = list(RCIM_REPRESENTATIVE_ROOT.glob("*/onnx_export/MLP/MLPRegressor_ampl0.onnx"))
        return select_newest_model_path(candidate_list)

    for dataset_branch in DATASET_BRANCH_PRIORITY_LIST:
        family_root = dataset_branch / family_name
        for surface_name in SURFACE_PRIORITY_LIST:
            surface_root = family_root / surface_name
            candidate_list = list(surface_root.glob("*/onnx/model.onnx"))
            selected_path = select_newest_model_path(candidate_list)
            if selected_path is not None:
                return selected_path
            direct_path = surface_root / "onnx" / "model.onnx"
            if direct_path.exists():
                return direct_path
    return None


def load_yaml(path: Path) -> dict[str, Any]:

    """Load a YAML mapping from disk."""

    if not path.exists():
        return {}
    loaded_payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    return loaded_payload if isinstance(loaded_payload, dict) else {}


def load_json(path: Path) -> dict[str, Any]:

    """Load a JSON mapping from disk."""

    if not path.exists():
        return {}
    loaded_payload = json.loads(path.read_text(encoding="utf-8"))
    return loaded_payload if isinstance(loaded_payload, dict) else {}


def run_converter(command_argument_list: list[str]) -> subprocess.CompletedProcess[str]:

    """Run the converter and capture its terminal output."""

    return subprocess.run(
        [sys.executable, "-B", str(CONVERTER_PATH), *command_argument_list],
        cwd=PROJECT_PATH,
        text=True,
        capture_output=True,
        check=False,
    )


def build_run_name(prefix: str, family_name: str) -> str:

    """Build a stable run directory name for one matrix route."""

    return f"{prefix}_{family_name}"


def resolve_manifest_path(output_root: Path, run_name: str) -> Path:

    """Resolve a converter manifest path from a run name."""

    return output_root / run_name / "conversion_manifest.yaml"


def run_family_conversion(
    family_name: str,
    onnx_path: Path,
    output_root: Path,
    run_onnxruntime_smoke: bool,
    continue_existing: bool,
) -> dict[str, Any]:

    """Run TF38x0 first and TF3820 fallback for one family."""

    route_result_map: dict[str, Any] = {}
    tf38x0_run_name = build_run_name("tf38x0", family_name)
    tf38x0_manifest_path = resolve_manifest_path(output_root, tf38x0_run_name)
    common_argument_list = [
        "--output-root",
        str(output_root),
        "--onnx",
        str(onnx_path),
        "--freeze-nonbatch-dynamic-dims",
    ]
    if run_onnxruntime_smoke:
        common_argument_list.append("--run-onnxruntime-smoke")

    if continue_existing and tf38x0_manifest_path.exists():
        tf38x0_completed_process = None
    else:
        tf38x0_completed_process = run_converter([*common_argument_list, "--run-name", tf38x0_run_name])
    tf38x0_manifest = load_yaml(tf38x0_manifest_path)
    tf38x0_payload = tf38x0_manifest.get("tf38x0", {}) if isinstance(tf38x0_manifest, dict) else {}
    route_result_map["tf38x0"] = {
        "return_code": tf38x0_completed_process.returncode if tf38x0_completed_process is not None else None,
        "manifest_path": project_relative(tf38x0_manifest_path),
        "status": tf38x0_payload.get("status", "missing_manifest"),
    }

    tf3820_run_name = build_run_name("tf3820", family_name)
    tf3820_manifest_path = resolve_manifest_path(output_root, tf3820_run_name)
    if continue_existing and tf3820_manifest_path.exists():
        tf3820_completed_process = None
    else:
        tf3820_completed_process = run_converter(
            [*common_argument_list, "--run-name", tf3820_run_name, "--skip-tf38x0", "--prepare-tf3820"]
        )
    tf3820_manifest = load_yaml(tf3820_manifest_path)
    tf3820_payload = tf3820_manifest.get("tf3820", {}) if isinstance(tf3820_manifest, dict) else {}
    route_result_map["tf3820"] = {
        "return_code": tf3820_completed_process.returncode if tf3820_completed_process is not None else None,
        "manifest_path": project_relative(tf3820_manifest_path),
        "status": tf3820_payload.get("status", "missing_manifest"),
        "json_output_path": tf3820_payload.get("json_output_path"),
        "plcopen_output_path": tf3820_payload.get("plcopen_output_path"),
    }
    inspection_summary_path = tf38x0_manifest.get("inspection_summary_path") or tf3820_manifest.get("inspection_summary_path")
    inspection_summary = load_json(PROJECT_PATH / inspection_summary_path) if inspection_summary_path else {}
    return {
        "family": family_name,
        "representative_onnx_path": project_relative(onnx_path),
        "inspection_summary_path": inspection_summary_path,
        "operator_histogram": inspection_summary.get("operator_histogram", {}),
        "dynamic_shape_count": inspection_summary.get("dynamic_shape_count"),
        "int64_max_constant_count": inspection_summary.get("int64_max_constant_count"),
        "routes": route_result_map,
        "classification": classify_family_result(route_result_map, inspection_summary),
    }


def classify_family_result(route_result_map: dict[str, Any], inspection_summary: dict[str, Any]) -> str:

    """Classify one family from route statuses and graph features."""

    if route_result_map["tf38x0"]["status"] == "completed":
        return "compatible_tf38x0_xml_bml"
    if route_result_map["tf3820"]["status"] == "completed":
        return "tf3820_plcopen_candidate"
    operator_set = set(inspection_summary.get("operator_histogram", {}))
    if {"LayerNormalization", "ReduceMean"} & operator_set:
        return "requires_model_variant_without_normalization_for_tf38x0"
    if {"GRU", "LSTM"} & operator_set:
        return "sequence_runtime_requires_tf3820_or_model_variant"
    if inspection_summary.get("int64_max_constant_count"):
        return "requires_slice_constant_postprocess"
    return "failed_needs_manual_review"


def write_markdown_summary(summary_path: Path, summary_payload: dict[str, Any]) -> None:

    """Write a compact Markdown compatibility table."""

    line_list = [
        "# TwinCAT ONNX Family Compatibility Matrix",
        "",
        f"- Created at: `{summary_payload['created_at']}`",
        f"- Families requested: `{summary_payload['family_count']}`",
        f"- Families with representative ONNX: `{summary_payload['represented_family_count']}`",
        "",
        "| Family | Classification | TF38x0 | TF3820 | Representative |",
        "| --- | --- | --- | --- | --- |",
    ]
    for family_result in summary_payload["family_results"]:
        route_map = family_result.get("routes", {})
        tf38x0_status = route_map.get("tf38x0", {}).get("status", "missing")
        tf3820_status = route_map.get("tf3820", {}).get("status", "missing")
        representative_path = family_result.get("representative_onnx_path", "")
        if representative_path is None:
            representative_path = ""
        line_list.append(
            "| "
            + " | ".join(
                [
                    family_result["family"],
                    family_result.get("classification", ""),
                    tf38x0_status,
                    tf3820_status,
                    representative_path,
                ]
            )
            + " |"
        )
    summary_path.write_text("\n".join(line_list) + "\n", encoding="utf-8")


def main() -> int:

    """Run the compatibility matrix."""

    arguments = parse_arguments()
    output_root = (PROJECT_PATH / arguments.output_root).resolve() if not arguments.output_root.is_absolute() else arguments.output_root
    output_root.mkdir(parents=True, exist_ok=True)
    selected_family_list = arguments.family or MODEL_FAMILY_LIST
    family_result_list: list[dict[str, Any]] = []
    missing_family_list: list[str] = []

    for family_name in selected_family_list:
        representative_path = find_family_representative(family_name)
        if representative_path is None:
            missing_family_list.append(family_name)
            family_result_list.append({
                "family": family_name,
                "representative_onnx_path": None,
                "classification": "missing_representative_export",
                "routes": {},
            })
            continue
        print(f"[INFO] {family_name}: {project_relative(representative_path)}", flush=True)
        family_result = run_family_conversion(
            family_name,
            representative_path,
            output_root,
            run_onnxruntime_smoke=not arguments.skip_onnxruntime_smoke,
            continue_existing=arguments.continue_existing,
        )
        family_result_list.append(family_result)
        print(
            f"[INFO] {family_name}: {family_result['classification']} "
            f"(TF38x0={family_result['routes']['tf38x0']['status']}, "
            f"TF3820={family_result['routes']['tf3820']['status']})",
            flush=True,
        )

    classification_counter = Counter(result["classification"] for result in family_result_list)
    summary_payload = {
        "schema_version": 1,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "output_root": project_relative(output_root),
        "family_count": len(selected_family_list),
        "represented_family_count": len(selected_family_list) - len(missing_family_list),
        "missing_family_list": missing_family_list,
        "classification_counts": dict(sorted(classification_counter.items())),
        "family_results": family_result_list,
    }
    summary_yaml_path = output_root / "family_compatibility_matrix_summary.yaml"
    summary_json_path = output_root / "family_compatibility_matrix_summary.json"
    summary_markdown_path = output_root / "family_compatibility_matrix_summary.md"
    summary_yaml_path.write_text(yaml.safe_dump(summary_payload, sort_keys=False), encoding="utf-8")
    summary_json_path.write_text(json.dumps(summary_payload, indent=2), encoding="utf-8")
    write_markdown_summary(summary_markdown_path, summary_payload)
    print(f"[DONE] Summary: {project_relative(summary_yaml_path)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
