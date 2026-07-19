"""Promote RCIM Track 1 input-mode exports into the official model archive."""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_VALIDATION_ROOT = PROJECT_ROOT / "output" / "validation_checks" / "rcim_track1"
DEFAULT_TARGET_ROOT = (
    PROJECT_ROOT
    / "models"
    / "polished_dataset"
    / "paper_reference"
    / "rcim_track1"
)

SURFACE_OUTPUT_TOKEN_MAP = {
    "global": "_global_",
    "forward": "_fw_",
    "backward": "_bw_",
}
SURFACE_SHORT_NAME_MAP = {
    "global": "global",
    "forward": "fw",
    "backward": "bw",
}
FAMILY_ARCHIVE_FOLDER_MAP = {
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


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Promote completed RCIM Track 1 polished input-mode validation exports "
            "into models/polished_dataset/paper_reference/rcim_track1/<input_mode>."
        )
    )
    parser.add_argument(
        "--input-mode",
        choices=("setpoints", "actual_values"),
        required=True,
        help="Input-mode archive branch to populate.",
    )
    parser.add_argument(
        "--validation-root",
        type=Path,
        default=DEFAULT_VALIDATION_ROOT,
        help="Root containing completed RCIM Track 1 validation output directories.",
    )
    parser.add_argument(
        "--target-root",
        type=Path,
        default=DEFAULT_TARGET_ROOT,
        help="Official RCIM Track 1 archive root before the input-mode subfolder.",
    )
    parser.add_argument(
        "--campaign-name",
        default="dataset_input_mode_retraining__rcim_track1__polished_setpoints",
        help="Campaign name recorded in promoted archive inventories.",
    )
    parser.add_argument(
        "--execution-environment",
        default="local Windows workstation",
        help="Human-readable execution environment recorded in generated README files.",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Replace an existing target input-mode archive after path safety checks.",
    )
    return parser.parse_args()


def resolve_project_path(input_path: Path) -> Path:
    if input_path.is_absolute():
        return input_path.resolve()
    return (PROJECT_ROOT / input_path).resolve()


def resolve_manifest_path(path_value: Any) -> Path:
    return resolve_project_path(Path(str(path_value).replace("\\", "/")))


def assert_within_project(resolved_path: Path) -> None:
    try:
        resolved_path.relative_to(PROJECT_ROOT)
    except ValueError as exc:
        raise AssertionError(f"Path escapes project root | path={resolved_path}") from exc


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:
    with input_path.open("r", encoding="utf-8") as input_file:
        loaded_dictionary = yaml.safe_load(input_file)
    assert isinstance(loaded_dictionary, dict), f"Expected YAML dictionary | path={input_path}"
    return loaded_dictionary


def save_yaml_dictionary(output_path: Path, payload: dict[str, Any]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=False)


def calculate_sha256(input_path: Path) -> str:
    digest = hashlib.sha256()
    with input_path.open("rb") as input_file:
        for chunk in iter(lambda: input_file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def format_project_relative_path(input_path: Path) -> str:
    return str(input_path.resolve().relative_to(PROJECT_ROOT)).replace("\\", "/")


def resolve_latest_surface_directory(validation_root: Path, input_mode: str, surface: str) -> Path:
    token = SURFACE_OUTPUT_TOKEN_MAP[surface]
    candidate_list = [
        candidate
        for candidate in validation_root.iterdir()
        if candidate.is_dir()
        and f"rcim_track1_polished_{input_mode}" in candidate.name
        and token in candidate.name
    ]
    assert candidate_list, (
        "Missing completed validation directory | "
        f"input_mode={input_mode} surface={surface} root={validation_root}"
    )
    candidate_list.sort(key=lambda path: path.stat().st_mtime, reverse=True)
    return candidate_list[0]


def parse_target_kind_and_harmonic(export_target_name: str) -> tuple[str, int]:
    if export_target_name.startswith("ampl"):
        return "amplitude", int(export_target_name.removeprefix("ampl"))
    if export_target_name.startswith("phase"):
        return "phase", int(export_target_name.removeprefix("phase"))
    raise AssertionError(f"Unsupported export target name | {export_target_name}")


def copy_file_with_parent(source_path: Path, target_path: Path) -> dict[str, Any]:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target_path)
    return {
        "path": format_project_relative_path(target_path),
        "sha256": calculate_sha256(target_path),
        "size_bytes": target_path.stat().st_size,
    }


def prepare_target_root(target_root: Path, target_input_root: Path, replace: bool) -> None:
    expected_parent = target_root.resolve()
    try:
        target_input_root.resolve().relative_to(expected_parent)
    except ValueError as exc:
        raise AssertionError(
            "Refusing to write outside the official RCIM Track 1 polished archive root | "
            f"path={target_input_root}"
        ) from exc

    if not target_input_root.exists():
        target_input_root.mkdir(parents=True)
        return

    if not replace:
        raise AssertionError(
            "Target input-mode archive already exists; pass --replace only after "
            f"reviewing the current target | path={target_input_root}"
        )

    for surface_name in SURFACE_OUTPUT_TOKEN_MAP:
        surface_root = target_input_root / surface_name
        if surface_root.exists():
            shutil.rmtree(surface_root)
    for metadata_name in ("README.md", "promotion_inventory.yaml"):
        metadata_path = target_input_root / metadata_name
        if metadata_path.exists():
            metadata_path.unlink()


def build_family_inventory(
    *,
    family_export: dict[str, Any],
    validation_summary: dict[str, Any],
    source_validation_directory: Path,
    family_archive_root: Path,
    surface: str,
    input_mode: str,
    campaign_name: str,
    execution_environment: str,
) -> dict[str, Any]:
    family_name = str(family_export["family_name"])
    reference_model_list: list[dict[str, Any]] = []

    for export_target in family_export["exported_targets"]:
        export_target_name = str(export_target["export_target_name"])
        target_kind, harmonic_order = parse_target_kind_and_harmonic(export_target_name)
        source_onnx_path = resolve_manifest_path(export_target["onnx_export_path"])
        source_python_path = resolve_manifest_path(export_target["python_export_path"])
        archived_onnx_path = (
            family_archive_root
            / "onnx"
            / target_kind
            / source_onnx_path.name
        )
        archived_python_path = (
            family_archive_root
            / "python"
            / target_kind
            / source_python_path.name
        )
        archived_onnx = copy_file_with_parent(source_onnx_path, archived_onnx_path)
        archived_python = copy_file_with_parent(source_python_path, archived_python_path)
        reference_model_list.append(
            {
                "target_name": str(export_target["target_name"]),
                "target_kind": target_kind,
                "harmonic_order": harmonic_order,
                "direction_label": surface,
                "source_onnx_export_path": format_project_relative_path(source_onnx_path),
                "source_python_export_path": format_project_relative_path(source_python_path),
                "archived_model_path": archived_onnx["path"],
                "archived_model_sha256": archived_onnx["sha256"],
                "python_model_path": archived_python["path"],
                "python_model_sha256": archived_python["sha256"],
                "export_estimator_name": str(export_target["export_estimator_name"]),
                "surrogate_strategy": str(export_target["surrogate_strategy"]),
                "onnx_file_size_bytes": archived_onnx["size_bytes"],
                "python_file_size_bytes": archived_python["size_bytes"],
            }
        )

    source_run_root = family_archive_root / "source_runs" / source_validation_directory.name
    for source_name, target_name in (
        ("validation_summary.yaml", "validation_summary.snapshot.yaml"),
        ("training_config.yaml", "training_config.snapshot.yaml"),
        ("run_metadata.yaml", "run_metadata.snapshot.yaml"),
        ("best_parameter_summary.yaml", "best_parameter_summary.snapshot.yaml"),
    ):
        source_path = source_validation_directory / source_name
        if source_path.exists():
            copy_file_with_parent(source_path, source_run_root / target_name)

    inventory = {
        "schema_version": 1,
        "topic": "rcim_track1_polished_input_mode_reference_archive",
        "campaign_name": campaign_name,
        "dataset_name": "polished_dataset",
        "dataset_root": validation_summary["dataset"]["dataset_root"],
        "input_mode": input_mode,
        "execution_environment": execution_environment,
        "direction_label": surface,
        "input_feature_names": validation_summary["dataset"]["feature_name_list"],
        "paper_family_name": family_name,
        "implementation_family_name": family_name,
        "source_validation_directory": format_project_relative_path(source_validation_directory),
        "source_validation_summary_path": format_project_relative_path(
            source_validation_directory / "validation_summary.yaml"
        ),
        "python_exported_file_count": int(family_export["python_exported_target_count"]),
        "onnx_exported_file_count": int(family_export["onnx_exported_target_count"]),
        "failed_onnx_target_count": int(family_export["failed_onnx_target_count"]),
        "reference_models": reference_model_list,
    }
    save_yaml_dictionary(family_archive_root / "reference_inventory.yaml", inventory)
    return inventory


def write_family_readme(family_archive_root: Path, inventory: dict[str, Any]) -> None:
    family_name = inventory["paper_family_name"]
    readme_text = "\n".join(
        [
            f"# {family_name} RCIM Track 1 Polished {inventory['input_mode']} Archive",
            "",
            "This archive contains the promoted ONNX and Python fitted-estimator",
            "exports from the completed RCIM Track 1 input-mode campaign.",
            f"Execution environment: {inventory['execution_environment']}.",
            "",
            "Archive contract:",
            "",
            "- dataset: `polished_dataset`",
            f"- input mode: `{inventory['input_mode']}`",
            f"- direction: `{inventory['direction_label']}`",
            "- input features: `angular_position_deg`, `input_speed_rpm`,",
            "  `input_torque_nm`, `oil_temperature_deg`, `direction_flag`",
            "- ONNX exports: `onnx/amplitude/` and `onnx/phase/`",
            "- Python exports: `python/amplitude/` and `python/phase/`",
            "- machine-readable provenance: `reference_inventory.yaml`",
            "",
        ]
    )
    (family_archive_root / "README.md").write_text(readme_text, encoding="utf-8", newline="\n")


def promote_surface(
    *,
    validation_root: Path,
    target_input_root: Path,
    input_mode: str,
    surface: str,
    campaign_name: str,
    execution_environment: str,
) -> dict[str, Any]:
    source_validation_directory = resolve_latest_surface_directory(validation_root, input_mode, surface)
    validation_summary_path = source_validation_directory / "validation_summary.yaml"
    validation_summary = load_yaml_dictionary(validation_summary_path)

    dataset_summary = validation_summary["dataset"]
    assert dataset_summary["dataset_root"] == "data\\polished_dataset"
    assert dataset_summary["input_mode"] == input_mode
    assert dataset_summary["direction_label"] == surface
    assert dataset_summary["feature_name_list"] == [
        "angular_position_deg",
        "input_speed_rpm",
        "input_torque_nm",
        "oil_temperature_deg",
        "direction_flag",
    ]

    surface_root = target_input_root / surface
    surface_root.mkdir(parents=True, exist_ok=True)
    family_inventory_list: list[dict[str, Any]] = []
    for family_export in validation_summary["onnx_export_summary"]["family_exports"]:
        family_name = str(family_export["family_name"])
        assert int(family_export["python_exported_target_count"]) == 19
        assert int(family_export["onnx_exported_target_count"]) == 19
        assert int(family_export["failed_onnx_target_count"]) == 0
        family_archive_folder = FAMILY_ARCHIVE_FOLDER_MAP[family_name]
        family_archive_root = surface_root / family_archive_folder
        inventory = build_family_inventory(
            family_export=family_export,
            validation_summary=validation_summary,
            source_validation_directory=source_validation_directory,
            family_archive_root=family_archive_root,
            surface=surface,
            input_mode=input_mode,
            campaign_name=campaign_name,
            execution_environment=execution_environment,
        )
        write_family_readme(family_archive_root, inventory)
        family_inventory_list.append(
            {
                "family_name": family_name,
                "archive_root": format_project_relative_path(family_archive_root),
                "reference_inventory_path": format_project_relative_path(
                    family_archive_root / "reference_inventory.yaml"
                ),
                "python_exported_file_count": inventory["python_exported_file_count"],
                "onnx_exported_file_count": inventory["onnx_exported_file_count"],
                "failed_onnx_target_count": inventory["failed_onnx_target_count"],
            }
        )

    copied_python_count = len(list((surface_root).glob("**/python/**/*.pkl")))
    copied_onnx_count = len(list((surface_root).glob("**/onnx/**/*.onnx")))
    assert copied_python_count == 190, f"Unexpected Python count | surface={surface}"
    assert copied_onnx_count == 190, f"Unexpected ONNX count | surface={surface}"

    return {
        "surface": surface,
        "surface_short_name": SURFACE_SHORT_NAME_MAP[surface],
        "source_validation_directory": format_project_relative_path(source_validation_directory),
        "surface_archive_root": format_project_relative_path(surface_root),
        "family_count": len(family_inventory_list),
        "python_exported_file_count": copied_python_count,
        "onnx_exported_file_count": copied_onnx_count,
        "family_archives": family_inventory_list,
    }


def write_root_readme(target_input_root: Path, promotion_inventory: dict[str, Any]) -> None:
    surface_lines = [
        f"- `{surface_entry['surface']}/`: {surface_entry['family_count']} family archives, "
        f"{surface_entry['onnx_exported_file_count']} ONNX files, "
        f"{surface_entry['python_exported_file_count']} Python pickle files"
        for surface_entry in promotion_inventory["surfaces"]
    ]
    readme_text = "\n".join(
        [
            f"# RCIM Track 1 Polished {promotion_inventory['input_mode']} Archive",
            "",
            "This folder contains the official promoted RCIM Track 1 polished-dataset",
            f"{promotion_inventory['input_mode']} model bank.",
            f"Execution environment: {promotion_inventory['execution_environment']}.",
            "",
            "Input contract:",
            "",
            "- dataset: `polished_dataset`",
            f"- input mode: `{promotion_inventory['input_mode']}`",
            "- input dimension: `5`",
            "- input features: `angular_position_deg`, `input_speed_rpm`,",
            "  `input_torque_nm`, `oil_temperature_deg`, `direction_flag`",
            "",
            "Promoted surfaces:",
            "",
            *surface_lines,
            "",
            "Each family archive contains:",
            "",
            "- `onnx/amplitude/` and `onnx/phase/`",
            "- `python/amplitude/` and `python/phase/`",
            "- `reference_inventory.yaml`",
            "- `source_runs/<validation_run>/` snapshots",
            "",
        ]
    )
    (target_input_root / "README.md").write_text(readme_text, encoding="utf-8", newline="\n")


def main() -> None:
    arguments = parse_arguments()
    validation_root = resolve_project_path(arguments.validation_root)
    target_root = resolve_project_path(arguments.target_root)
    target_input_root = target_root / arguments.input_mode
    assert_within_project(validation_root)
    assert_within_project(target_input_root)

    prepare_target_root(target_root, target_input_root, arguments.replace)

    surface_inventory_list = []
    for surface in ("global", "forward", "backward"):
        surface_inventory_list.append(
            promote_surface(
                validation_root=validation_root,
                target_input_root=target_input_root,
                input_mode=arguments.input_mode,
                surface=surface,
                campaign_name=arguments.campaign_name,
                execution_environment=arguments.execution_environment,
            )
        )

    promotion_inventory = {
        "schema_version": 1,
        "campaign_name": arguments.campaign_name,
        "dataset_name": "polished_dataset",
        "input_mode": arguments.input_mode,
        "execution_environment": arguments.execution_environment,
        "target_archive_root": format_project_relative_path(target_input_root),
        "surface_count": len(surface_inventory_list),
        "total_python_exported_file_count": sum(
            surface["python_exported_file_count"] for surface in surface_inventory_list
        ),
        "total_onnx_exported_file_count": sum(
            surface["onnx_exported_file_count"] for surface in surface_inventory_list
        ),
        "surfaces": surface_inventory_list,
    }
    assert promotion_inventory["total_python_exported_file_count"] == 570
    assert promotion_inventory["total_onnx_exported_file_count"] == 570
    save_yaml_dictionary(target_input_root / "promotion_inventory.yaml", promotion_inventory)
    write_root_readme(target_input_root, promotion_inventory)

    print(
        "[DONE] Promoted RCIM Track 1 input-mode exports | "
        f"target={format_project_relative_path(target_input_root)} "
        f"onnx={promotion_inventory['total_onnx_exported_file_count']} "
        f"python={promotion_inventory['total_python_exported_file_count']}"
    )


if __name__ == "__main__":
    main()
