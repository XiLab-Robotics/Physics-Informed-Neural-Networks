"""Close out recovered-original RCIM retuned reference archives.

This script promotes validated retuned recovered-original RCIM model exports
into ``models/paper_reference/rcim_retuned`` and regenerates the benchmark
report surface used to compare paper-original, paper-retuned, and Track 1
results.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[3]
RCIM_OUTPUT_ROOT = PROJECT_ROOT / "output" / "training_campaigns" / "rcim_original"
ARCHIVE_ROOT = PROJECT_ROOT / "models" / "paper_reference" / "rcim_retuned"
BENCHMARK_MARKDOWN_PATH = (
    PROJECT_ROOT / "doc" / "reports" / "analysis" / "RCIM Paper Reference Benchmark.md"
)
REPORT_ROOT = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "analysis"
    / "rcim_retuned_reference_closeout"
    / "[2026-05-13]"
)
REPORT_MARKDOWN_PATH = REPORT_ROOT / "rcim_retuned_reference_closeout_report.md"

HARMONIC_ORDER_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
PHASE_TABLE_HARMONIC_ORDER_LIST = [1, 3, 39, 40, 78, 81, 156, 162, 240]
FEATURE_NAME_LIST = ["rpm", "deg", "tor"]


@dataclass(frozen=True)
class FamilyDefinition:
    """Repository naming metadata for a recovered-original RCIM family."""

    family_code: str
    paper_family_name: str
    archive_folder_name: str
    estimator_name: str


@dataclass(frozen=True)
class SourceSelection:
    """Accepted source-stage bundle mapping for a family and direction."""

    direction: str
    family_code: str
    retune_bundle: str
    eval_bundle: str
    export_bundle: str


@dataclass
class PromotedFamilyArchive:
    """Summary of one promoted family archive."""

    direction: str
    family_code: str
    paper_family_name: str
    archive_root: Path
    retune_bundle: str
    eval_bundle: str
    export_bundle: str
    onnx_count: int
    pkl_count: int
    export_error_count: int
    mean_mse: float | None
    mean_rmse: float | None
    mean_mae: float | None
    mean_mape: float | None


FAMILY_DEFINITION_LIST = [
    FamilyDefinition("SVR", "SVM", "svm_reference_models", "SVR"),
    FamilyDefinition("MLP", "MLP", "mlp_reference_models", "MLP"),
    FamilyDefinition("RF", "RF", "rf_reference_models", "RandomForestRegressor"),
    FamilyDefinition("DT", "DT", "dt_reference_models", "DecisionTreeRegressor"),
    FamilyDefinition("ET", "ET", "et_reference_models", "ExtraTreesRegressor"),
    FamilyDefinition("ERT", "ERT", "ert_reference_models", "ExtraTreeRegressor"),
    FamilyDefinition("GBM", "GBM", "gbm_reference_models", "GradientBoostingRegressor"),
    FamilyDefinition("HGBM", "HGBM", "hgbm_reference_models", "HistGradientBoostingRegressor"),
    FamilyDefinition("XGBM", "XGBM", "xgbm_reference_models", "XGBRegressor"),
    FamilyDefinition("LGBM", "LGBM", "lgbm_reference_models", "LGBMRegressor"),
    FamilyDefinition("ELM", "ELM", "elm_reference_models", "ELMRegressor"),
]
FAMILY_BY_CODE = {definition.family_code: definition for definition in FAMILY_DEFINITION_LIST}

SOURCE_SELECTION_LIST = [
    SourceSelection("forward", "SVR", "2026-05-09-23-52-16__fw_retune_bundle", "2026-05-09-23-52-16__fw_retune_bundle", "2026-05-09-23-52-16__fw_retune_bundle"),
    SourceSelection("forward", "MLP", "2026-05-11-16-55-11__fw_retune_bundle", "2026-05-11-16-55-11__fw_retune_bundle", "2026-05-11-16-55-11__fw_retune_bundle"),
    SourceSelection("forward", "RF", "2026-05-09-10-02-19__fw_retune_bundle", "2026-05-09-13-01-21__fw_eval_bundle", "2026-05-09-13-01-34__fw_export_bundle"),
    SourceSelection("forward", "DT", "2026-05-13-15-40-16__fw_retune_bundle", "2026-05-13-15-40-16__fw_retune_bundle", "2026-05-13-15-40-16__fw_retune_bundle"),
    SourceSelection("forward", "ET", "2026-05-11-18-27-16__fw_retune_bundle", "2026-05-11-18-27-16__fw_retune_bundle", "2026-05-11-18-27-16__fw_retune_bundle"),
    SourceSelection("forward", "ERT", "2026-05-11-18-27-16__fw_retune_bundle", "2026-05-11-18-27-16__fw_retune_bundle", "2026-05-11-18-27-16__fw_retune_bundle"),
    SourceSelection("forward", "GBM", "2026-05-11-18-27-16__fw_retune_bundle", "2026-05-12-18-16-50__fw_eval_bundle", "2026-05-12-18-20-41__fw_export_bundle"),
    SourceSelection("forward", "HGBM", "2026-05-11-18-27-16__fw_retune_bundle", "2026-05-12-18-16-50__fw_eval_bundle", "2026-05-12-18-20-41__fw_export_bundle"),
    SourceSelection("forward", "XGBM", "2026-05-11-16-55-11__fw_retune_bundle", "2026-05-11-16-55-11__fw_retune_bundle", "2026-05-11-16-55-11__fw_retune_bundle"),
    SourceSelection("forward", "LGBM", "2026-05-12-11-20-54__fw_retune_bundle", "2026-05-12-11-20-54__fw_retune_bundle", "2026-05-12-11-20-54__fw_retune_bundle"),
    SourceSelection("forward", "ELM", "2026-05-11-18-21-23__fw_retune_bundle", "2026-05-11-18-21-23__fw_retune_bundle", "2026-05-11-18-21-23__fw_retune_bundle"),
    SourceSelection("backward", "SVR", "2026-05-09-23-42-54__bw_retune_bundle", "2026-05-09-23-42-54__bw_retune_bundle", "2026-05-09-23-42-54__bw_retune_bundle"),
    SourceSelection("backward", "MLP", "2026-05-11-09-19-07__bw_retune_bundle", "2026-05-11-09-19-07__bw_retune_bundle", "2026-05-11-09-19-07__bw_retune_bundle"),
    SourceSelection("backward", "RF", "2026-05-09-09-23-24__bw_retune_bundle", "2026-05-09-12-31-49__bw_eval_bundle", "2026-05-09-12-32-07__bw_export_bundle"),
    SourceSelection("backward", "DT", "2026-05-09-09-21-57__bw_retune_bundle", "2026-05-09-09-21-57__bw_retune_bundle", "2026-05-09-09-21-57__bw_retune_bundle"),
    SourceSelection("backward", "ET", "2026-05-12-11-08-07__bw_retune_bundle", "2026-05-12-11-08-07__bw_retune_bundle", "2026-05-12-11-08-07__bw_retune_bundle"),
    SourceSelection("backward", "ERT", "2026-05-12-11-08-07__bw_retune_bundle", "2026-05-12-11-08-07__bw_retune_bundle", "2026-05-12-11-08-07__bw_retune_bundle"),
    SourceSelection("backward", "GBM", "2026-05-12-11-08-07__bw_retune_bundle", "2026-05-12-18-22-07__bw_eval_bundle", "2026-05-12-18-22-27__bw_export_bundle"),
    SourceSelection("backward", "HGBM", "2026-05-12-11-08-07__bw_retune_bundle", "2026-05-12-18-22-07__bw_eval_bundle", "2026-05-12-18-22-27__bw_export_bundle"),
    SourceSelection("backward", "XGBM", "2026-05-11-09-19-07__bw_retune_bundle", "2026-05-11-09-19-07__bw_retune_bundle", "2026-05-11-09-19-07__bw_retune_bundle"),
    SourceSelection("backward", "LGBM", "2026-05-11-16-05-54__bw_retune_bundle", "2026-05-11-16-05-54__bw_retune_bundle", "2026-05-11-16-05-54__bw_retune_bundle"),
    SourceSelection("backward", "ELM", "2026-05-11-09-19-07__bw_retune_bundle", "2026-05-11-11-38-37__bw_eval_bundle", "2026-05-11-11-38-49__bw_export_bundle"),
]

TABLE_DEFINITION_LIST = [
    ("Table 2", "Amplitude MAE", "ampl", "MAE", HARMONIC_ORDER_LIST),
    ("Table 3", "Amplitude RMSE", "ampl", "RMSE", HARMONIC_ORDER_LIST),
    ("Table 4", "Phase MAE", "phase", "MAE", PHASE_TABLE_HARMONIC_ORDER_LIST),
    ("Table 5", "Phase RMSE", "phase", "RMSE", PHASE_TABLE_HARMONIC_ORDER_LIST),
]


def main() -> None:
    """Run the retuned-reference closeout."""

    original_paper_table_map = parse_paper_original_tables(BENCHMARK_MARKDOWN_PATH)
    promoted_archive_list: list[PromotedFamilyArchive] = []
    metric_map: dict[tuple[str, str], dict[str, float]] = {}

    reset_directory(ARCHIVE_ROOT)
    create_root_readme()

    for source_selection in SOURCE_SELECTION_LIST:
        promoted_archive = promote_family_archive(source_selection)
        promoted_archive_list.append(promoted_archive)
        metric_map[(source_selection.direction, source_selection.family_code)] = read_eval_metrics(
            source_selection
        )

    write_archive_indexes(promoted_archive_list)
    write_closeout_report(promoted_archive_list, metric_map)
    write_benchmark_markdown(original_paper_table_map, metric_map, promoted_archive_list)

    print(f"[DONE] Promoted archives | {len(promoted_archive_list)}")
    print(f"[DONE] Archive root | {ARCHIVE_ROOT.relative_to(PROJECT_ROOT)}")
    print(f"[DONE] Closeout report | {REPORT_MARKDOWN_PATH.relative_to(PROJECT_ROOT)}")
    print(f"[DONE] Benchmark report | {BENCHMARK_MARKDOWN_PATH.relative_to(PROJECT_ROOT)}")


def reset_directory(directory_path: Path) -> None:
    """Replace a generated directory safely."""

    if directory_path.exists():
        shutil.rmtree(directory_path)
    directory_path.mkdir(parents=True, exist_ok=True)


def create_root_readme() -> None:
    """Create the root README for the retuned archive surface."""

    readme_text = """# RCIM Retuned Paper Reference Models

This folder stores curated recovered-original RCIM models generated from the
retuned hyperparameter workflow.

Direction branches:

- `forward/`
- `backward/`

Each populated family archive follows the same structure used by
`models/paper_reference/rcim_original/`:

- `<direction>/<family>_reference_models/README.md`
- `<direction>/<family>_reference_models/reference_inventory.yaml`
- `<direction>/<family>_reference_models/onnx/amplitude/`
- `<direction>/<family>_reference_models/onnx/phase/`
- `<direction>/<family>_reference_models/python/amplitude/`
- `<direction>/<family>_reference_models/python/phase/`
- `<direction>/<family>_reference_models/data/`
- `<direction>/<family>_reference_models/dataset_snapshot_manifest.yaml`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/`

Archive acceptance rule:

- every promoted family-direction archive has `20` ONNX files;
- every promoted family-direction archive has `20` Python pickle files;
- no promoted family-direction archive contains ONNX export-error sidecars.
"""
    write_text(ARCHIVE_ROOT / "README.md", readme_text)


def promote_family_archive(source_selection: SourceSelection) -> PromotedFamilyArchive:
    """Promote one accepted family-direction source into the curated archive."""

    family_definition = FAMILY_BY_CODE[source_selection.family_code]
    family_archive_root = (
        ARCHIVE_ROOT
        / source_selection.direction
        / family_definition.archive_folder_name
    )
    reset_directory(family_archive_root)
    create_archive_directories(family_archive_root)

    export_model_dir = get_stage_root(source_selection, "export") / "model_output_dir"
    export_file_list = [
        path
        for path in export_model_dir.iterdir()
        if path.is_file() and family_definition.estimator_name in path.name
    ]
    onnx_file_list = sorted(path for path in export_file_list if path.suffix == ".onnx")
    pkl_file_list = sorted(path for path in export_file_list if path.suffix == ".pkl")
    error_file_list = sorted(
        path for path in export_file_list if path.name.endswith(".export_error.txt")
    )

    if len(onnx_file_list) != 20 or len(pkl_file_list) != 20 or error_file_list:
        raise RuntimeError(
            "Incomplete export for "
            f"{source_selection.direction}/{source_selection.family_code}: "
            f"onnx={len(onnx_file_list)} pkl={len(pkl_file_list)} "
            f"errors={len(error_file_list)}"
        )

    dataset_snapshot = copy_dataset_snapshot(source_selection, family_archive_root)
    inventory_entry_list = copy_model_exports(
        source_selection,
        family_definition,
        family_archive_root,
        dataset_snapshot,
        onnx_file_list,
        pkl_file_list,
    )
    copy_source_run_snapshots(source_selection, family_archive_root)
    write_family_readme(source_selection, family_definition, family_archive_root)
    write_family_inventory(
        source_selection,
        family_definition,
        family_archive_root,
        dataset_snapshot,
        inventory_entry_list,
    )
    write_dataset_manifest(source_selection, family_archive_root, dataset_snapshot)

    metric_row = read_eval_metrics(source_selection)
    return PromotedFamilyArchive(
        direction=source_selection.direction,
        family_code=source_selection.family_code,
        paper_family_name=family_definition.paper_family_name,
        archive_root=family_archive_root,
        retune_bundle=source_selection.retune_bundle,
        eval_bundle=source_selection.eval_bundle,
        export_bundle=source_selection.export_bundle,
        onnx_count=len(onnx_file_list),
        pkl_count=len(pkl_file_list),
        export_error_count=len(error_file_list),
        mean_mse=metric_row.get("MSE"),
        mean_rmse=metric_row.get("RMSE"),
        mean_mae=metric_row.get("MAE"),
        mean_mape=metric_row.get("MAPE"),
    )


def create_archive_directories(family_archive_root: Path) -> None:
    """Create the standard archive subdirectories."""

    for relative_path in [
        "onnx/amplitude",
        "onnx/phase",
        "python/amplitude",
        "python/phase",
        "data",
        "source_runs",
    ]:
        (family_archive_root / relative_path).mkdir(parents=True, exist_ok=True)


def copy_dataset_snapshot(
    source_selection: SourceSelection,
    family_archive_root: Path,
) -> dict[str, object]:
    """Copy the runtime dataframe snapshot and return manifest metadata."""

    export_root = get_stage_root(source_selection, "export")
    direction_token = "Fw" if source_selection.direction == "forward" else "Bw"
    dataset_source_path = export_root / f"dataFrame_prediction_{direction_token}_v14_newFreq.csv"
    if not dataset_source_path.exists():
        raise FileNotFoundError(dataset_source_path)

    dataset_destination_path = family_archive_root / "data" / dataset_source_path.name
    shutil.copy2(dataset_source_path, dataset_destination_path)
    row_count, column_name_list = read_semicolon_csv_shape(dataset_destination_path)

    return {
        "source_dataset_path": to_posix_relative(dataset_source_path),
        "archived_dataset_path": to_posix_relative(dataset_destination_path),
        "dataset_sha256": sha256_file(dataset_destination_path),
        "row_count": row_count,
        "column_count": len(column_name_list),
        "column_name_list": column_name_list,
    }


def copy_model_exports(
    source_selection: SourceSelection,
    family_definition: FamilyDefinition,
    family_archive_root: Path,
    dataset_snapshot: dict[str, object],
    onnx_file_list: list[Path],
    pkl_file_list: list[Path],
) -> list[dict[str, object]]:
    """Copy ONNX and Python model exports into target-kind subfolders."""

    onnx_by_target = {extract_target_name(path): path for path in onnx_file_list}
    pkl_by_target = {extract_target_name(path): path for path in pkl_file_list}
    expected_target_list = build_expected_target_list(source_selection.direction)
    inventory_entry_list: list[dict[str, object]] = []

    for target_name, target_kind, harmonic_order in expected_target_list:
        if target_name not in onnx_by_target or target_name not in pkl_by_target:
            raise RuntimeError(
                f"Missing target export for {source_selection.direction}/"
                f"{source_selection.family_code}/{target_name}"
            )

        model_name_prefix = pkl_by_target[target_name].name.split("_paperReferenceExport", 1)[0]
        target_short_name = f"{target_kind_short(target_kind)}{harmonic_order}"
        target_folder = "amplitude" if target_kind == "ampl" else "phase"
        onnx_destination_path = (
            family_archive_root
            / "onnx"
            / target_folder
            / f"{model_name_prefix}_{target_short_name}.onnx"
        )
        pkl_destination_path = (
            family_archive_root
            / "python"
            / target_folder
            / f"{model_name_prefix}_{target_short_name}.pkl"
        )
        shutil.copy2(onnx_by_target[target_name], onnx_destination_path)
        shutil.copy2(pkl_by_target[target_name], pkl_destination_path)

        inventory_entry_list.append(
            {
                "target_name": target_name,
                "target_kind": "amplitude" if target_kind == "ampl" else "phase",
                "harmonic_order": harmonic_order,
                "direction_label": source_selection.direction,
                "source_run_instance_id": source_selection.export_bundle,
                "export_estimator_name": model_name_prefix,
                "source_export_bundle_path": to_posix_relative(
                    get_bundle_root(source_selection.direction, source_selection.export_bundle)
                ),
                "source_export_model_output_dir": to_posix_relative(
                    get_stage_root(source_selection, "export") / "model_output_dir"
                ),
                "dataset_snapshot_path": dataset_snapshot["archived_dataset_path"],
                "dataset_snapshot_sha256": dataset_snapshot["dataset_sha256"],
                "feature_name_list": FEATURE_NAME_LIST,
                "archived_onnx_path": to_posix_relative(onnx_destination_path),
                "archived_onnx_sha256": sha256_file(onnx_destination_path),
                "python_model_path": to_posix_relative(pkl_destination_path),
                "python_model_sha256": sha256_file(pkl_destination_path),
                "python_model_serialization": "pickle",
                "python_estimator_class_name": model_name_prefix,
                "onnx_export_status": "success",
            }
        )

    return inventory_entry_list


def copy_source_run_snapshots(
    source_selection: SourceSelection,
    family_archive_root: Path,
) -> None:
    """Copy stage summaries, logs, and prediction snapshots into source_runs."""

    stage_bundle_map = {
        "retune": source_selection.retune_bundle,
        "eval": source_selection.eval_bundle,
        "export": source_selection.export_bundle,
    }
    for stage_name, bundle_name in stage_bundle_map.items():
        bundle_root = get_bundle_root(source_selection.direction, bundle_name)
        source_run_root = family_archive_root / "source_runs" / bundle_name
        source_run_root.mkdir(parents=True, exist_ok=True)

        launcher_summary_path = bundle_root / "launcher_summary.json"
        if launcher_summary_path.exists():
            shutil.copy2(
                launcher_summary_path,
                source_run_root / "launcher_summary.snapshot.json",
            )

        stage_root = bundle_root / stage_name
        stage_summary_path = stage_root / "run_summary.json"
        if stage_summary_path.exists():
            shutil.copy2(
                stage_summary_path,
                source_run_root / f"{stage_name}.run_summary.snapshot.json",
            )

        stage_dataframe_path_list = sorted(stage_root.glob("dataFrame_prediction_*.csv"))
        for dataframe_path in stage_dataframe_path_list:
            shutil.copy2(
                dataframe_path,
                source_run_root / f"{stage_name}.{dataframe_path.name}",
            )

        output_prediction_root = stage_root / "output_prediction"
        if output_prediction_root.exists():
            destination_output_root = source_run_root / f"{stage_name}_output_prediction"
            if destination_output_root.exists():
                shutil.rmtree(destination_output_root)
            shutil.copytree(output_prediction_root, destination_output_root)

        log_root = bundle_root / "logs"
        for log_path in sorted(log_root.glob(f"{stage_name}.*.log")):
            shutil.copy2(log_path, source_run_root / log_path.name)


def write_family_readme(
    source_selection: SourceSelection,
    family_definition: FamilyDefinition,
    family_archive_root: Path,
) -> None:
    """Write a human-facing family archive README."""

    readme_text = f"""# RCIM Retuned {source_selection.direction.title()} {family_definition.paper_family_name} Reference Models

This archive stores the retuned recovered-original RCIM target-level models for
the `{source_selection.direction}` branch.

Archive contents:

- `reference_inventory.yaml`
- `onnx/amplitude/`
- `onnx/phase/`
- `python/amplitude/`
- `python/phase/`
- `data/`
- `dataset_snapshot_manifest.yaml`
- `source_runs/<run_instance_id>/`

Selection rule:

- retuned hyperparameters come from the accepted `Retune` stage;
- `Eval` and `Export` stages are the accepted downstream recovery surfaces;
- every target must expose both ONNX and Python pickle artifacts;
- any source export with ONNX errors is rejected for this curated archive.

Provenance summary:

- direction label: `{source_selection.direction}`
- paper family: `{family_definition.paper_family_name}`
- implementation family: `{source_selection.family_code}`
- retune source bundle: `{source_selection.retune_bundle}`
- eval source bundle: `{source_selection.eval_bundle}`
- export source bundle: `{source_selection.export_bundle}`
- archived target count: `20`
- ONNX exported target count: `20`
- Python pickle target count: `20`
- ONNX export error count: `0`
"""
    write_text(family_archive_root / "README.md", readme_text)


def write_family_inventory(
    source_selection: SourceSelection,
    family_definition: FamilyDefinition,
    family_archive_root: Path,
    dataset_snapshot: dict[str, object],
    inventory_entry_list: list[dict[str, object]],
) -> None:
    """Write machine-readable archive inventory YAML."""

    inventory = {
        "schema_version": 1,
        "topic": (
            "rcim_retuned_"
            f"{source_selection.direction}_{source_selection.family_code.lower()}_reference_models"
        ),
        "paper_family_name": family_definition.paper_family_name,
        "implementation_family_name": source_selection.family_code,
        "archive_scope": {
            "direction_label": source_selection.direction,
            "source_stage": "RetuneEvalExport",
            "retune_bundle_run_instance_id": source_selection.retune_bundle,
            "eval_bundle_run_instance_id": source_selection.eval_bundle,
            "export_bundle_run_instance_id": source_selection.export_bundle,
            "retune_bundle_root": to_posix_relative(
                get_bundle_root(source_selection.direction, source_selection.retune_bundle)
            ),
            "eval_bundle_root": to_posix_relative(
                get_bundle_root(source_selection.direction, source_selection.eval_bundle)
            ),
            "export_bundle_root": to_posix_relative(
                get_bundle_root(source_selection.direction, source_selection.export_bundle)
            ),
            "amplitude_harmonic_order_list": HARMONIC_ORDER_LIST,
            "phase_harmonic_order_list": HARMONIC_ORDER_LIST,
            "archived_target_count": len(inventory_entry_list),
            "onnx_success_count": len(inventory_entry_list),
            "onnx_failure_count": 0,
            "python_pickle_count": len(inventory_entry_list),
        },
        "source_code": (
            "scripts/paper_reimplementation/rcim_ml_compensation/"
            "recovered_original_workflow/training_models.py"
        ),
        "source_launcher": (
            "scripts/campaigns/paper_reference/rcim_original/"
            "run_rcim_original_reference_training.ps1"
        ),
        "source_data": dataset_snapshot["source_dataset_path"],
        "notes": [
            "This archive stores accepted retuned recovered-original RCIM models.",
            "Every target has both an ONNX export and a Python pickle artifact.",
        ],
        "reference_models": inventory_entry_list,
    }
    write_yaml(family_archive_root / "reference_inventory.yaml", inventory)


def write_dataset_manifest(
    source_selection: SourceSelection,
    family_archive_root: Path,
    dataset_snapshot: dict[str, object],
) -> None:
    """Write the dataset snapshot manifest."""

    manifest = {
        "schema_version": 1,
        "archive_scope": f"rcim_retuned_{source_selection.direction}_reference_models",
        "direction_label": source_selection.direction,
        "source_bundle_run_instance_id": source_selection.export_bundle,
        **dataset_snapshot,
    }
    write_yaml(family_archive_root / "dataset_snapshot_manifest.yaml", manifest)


def write_archive_indexes(promoted_archive_list: list[PromotedFamilyArchive]) -> None:
    """Write direction-level README files."""

    for direction in ["forward", "backward"]:
        direction_archive_list = [
            archive for archive in promoted_archive_list if archive.direction == direction
        ]
        lines = [
            f"# RCIM Retuned {direction.title()} Reference Models",
            "",
            "This direction folder contains accepted retuned recovered-original",
            "RCIM family archives.",
            "",
            "Populated family archives:",
            "",
        ]
        for archive in direction_archive_list:
            lines.append(f"- `{archive.archive_root.name}/`")
        write_text(ARCHIVE_ROOT / direction / "README.md", "\n".join(lines) + "\n")


def write_closeout_report(
    promoted_archive_list: list[PromotedFamilyArchive],
    metric_map: dict[tuple[str, str], dict[str, float]],
) -> None:
    """Generate the detailed Markdown closeout report."""

    REPORT_ROOT.mkdir(parents=True, exist_ok=True)
    lines = [
        "# RCIM Retuned Reference Archive Closeout Report",
        "",
        "## Overview",
        "",
        "This report records the closeout of recovered-original RCIM retuned",
        "model exports into the curated `models/paper_reference/rcim_retuned`",
        "archive. The closeout accepts only family-direction exports with all",
        "`20` target-level ONNX artifacts and all `20` target-level Python",
        "pickle artifacts.",
        "",
        "## Archive Completeness",
        "",
        "| Direction | Family | Retune Bundle | Eval Bundle | Export Bundle | ONNX | PKL | Exported Errors |",
        "| --- | --- | --- | --- | --- | ---: | ---: | ---: |",
    ]
    for archive in promoted_archive_list:
        lines.append(
            "| "
            f"`{archive.direction}` | `{archive.paper_family_name}` | "
            f"`{archive.retune_bundle}` | `{archive.eval_bundle}` | "
            f"`{archive.export_bundle}` | `{archive.onnx_count}` | "
            f"`{archive.pkl_count}` | `{archive.export_error_count}` |"
        )

    lines.extend(
        [
            "",
            "## Mean Evaluation Metrics",
            "",
            "These values come from the accepted `Eval` stage",
            "`summaryCrossValidation+_3.8_allFreq.csv` files.",
            "",
            "| Direction | Family | MSE | RMSE | MAE | MAPE |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for archive in promoted_archive_list:
        lines.append(
            "| "
            f"`{archive.direction}` | `{archive.paper_family_name}` | "
            f"{format_metric(archive.mean_mse)} | {format_metric(archive.mean_rmse)} | "
            f"{format_metric(archive.mean_mae)} | {format_metric(archive.mean_mape)} |"
        )

    for direction in ["forward", "backward"]:
        lines.extend(["", f"## {direction.title()} Retuned Tables", ""])
        append_retuned_tables(lines, direction, metric_map)

    lines.extend(
        [
            "",
            "## Source Recovery Notes",
            "",
            "- `RF` uses separate backward `Eval` and `Export` recovery bundles after the parser fix.",
            "- `ELM` uses later recovery export bundles where the custom ONNX exporter is active.",
            "- `GBM` and `HGBM` use later recovery export bundles that removed earlier ONNX export errors.",
            "- `LGBM` uses the quieter retune factory surface so native LightGBM chatter does not bury failure evidence.",
        ]
    )

    write_text(REPORT_MARKDOWN_PATH, "\n".join(lines) + "\n")


def write_benchmark_markdown(
    original_paper_table_map: dict[str, list[list[str]]],
    metric_map: dict[tuple[str, str], dict[str, float]],
    promoted_archive_list: list[PromotedFamilyArchive],
) -> None:
    """Rewrite the canonical benchmark around the new table structure."""

    archive_count = len(promoted_archive_list)
    lines = [
        "# RCIM Paper Reference Benchmark",
        "",
        "## Scope",
        "",
        "This benchmark is the canonical repository-owned comparison surface for",
        "RCIM paper-reference model replication. It has been reset around three",
        "explicit surfaces:",
        "",
        "- `paper original`: values reconstructed from the original paper tables;",
        "- `paper retuned`: recovered-original RCIM models retuned through",
        "  `run_rcim_original_reference_training.ps1`;",
        "- `Track 1`: repository-owned exact-paper model-bank results, reset to",
        "  empty pending cells until the next Track 1 pass repopulates them.",
        "",
        "Forward Track 1 cells must compare against the better value between",
        "`paper original` and `paper retuned`. Backward Track 1 cells must",
        "compare against `paper retuned`, because the paper does not provide",
        "backward original tables.",
        "",
        "## Current Archive Status",
        "",
        f"- retuned family-direction archives promoted: `{archive_count}`",
        "- archive root: `models/paper_reference/rcim_retuned/`",
        "- accepted export contract: `20` ONNX files, `20` PKL files, `0` export errors",
        "- detailed closeout report:",
        "  `doc/reports/analysis/rcim_retuned_reference_closeout/[2026-05-13]/rcim_retuned_reference_closeout_report.md`",
        "",
    ]

    for direction in ["forward", "backward"]:
        lines.extend(["", f"## {direction.title()} Tables", ""])
        for table_name, table_label, target_kind, metric_name, harmonics in TABLE_DEFINITION_LIST:
            title = f"{table_name} - {table_label}"
            lines.extend(["", f"### {direction.title()} {title}", ""])
            if direction == "forward":
                lines.extend(
                    [
                        "#### Paper Original",
                        "",
                        "Paper original values exist only for the forward branch.",
                        "",
                    ]
                )
                append_raw_markdown_table(
                    lines,
                    original_paper_table_map.get(table_name, []),
                )
            else:
                lines.extend(
                    [
                        "#### Paper Original",
                        "",
                        "No backward paper-original table is available in the paper.",
                        "",
                    ]
                )

            lines.extend(["", "#### Paper Retuned", ""])
            append_metric_matrix(lines, direction, target_kind, metric_name, harmonics, metric_map)
            lines.extend(["", "#### Track 1", ""])
            append_pending_track1_matrix(lines, harmonics)

    lines.extend(
        [
            "",
            "## Reading Rules",
            "",
            "- `paper original` is immutable paper-side evidence and exists only for forward.",
            "- `paper retuned` is the current recovered-original retuned baseline.",
            "- `Track 1` cells are intentionally empty after this reset.",
            "- Future Track 1 closeouts must fill cells only after accepted",
            "  family-target results are available in the repository.",
            "- Future Track 1 forward status colors compare against the best of",
            "  `paper original` and `paper retuned`.",
            "- Future Track 1 backward status colors compare against `paper retuned`.",
        ]
    )

    write_text(BENCHMARK_MARKDOWN_PATH, "\n".join(lines) + "\n")


def append_retuned_tables(
    lines: list[str],
    direction: str,
    metric_map: dict[tuple[str, str], dict[str, float]],
) -> None:
    """Append all retuned metric matrices for one direction."""

    for table_name, table_label, target_kind, metric_name, harmonics in TABLE_DEFINITION_LIST:
        lines.extend(["", f"### {table_name} - {table_label}", ""])
        append_metric_matrix(lines, direction, target_kind, metric_name, harmonics, metric_map)


def append_metric_matrix(
    lines: list[str],
    direction: str,
    target_kind: str,
    metric_name: str,
    harmonics: list[int],
    metric_map: dict[tuple[str, str], dict[str, float]],
) -> None:
    """Append a Markdown matrix from eval metric rows."""

    lines.append("<!-- markdownlint-disable MD013 -->")
    lines.append("| Model | " + " | ".join(f"`{harmonic}`" for harmonic in harmonics) + " |")
    lines.append("| --- | " + " | ".join("---:" for _ in harmonics) + " |")
    for family_definition in FAMILY_DEFINITION_LIST:
        row = [f"`{family_definition.paper_family_name}`"]
        metrics = metric_map.get((direction, family_definition.family_code), {})
        for harmonic in harmonics:
            key = f"{target_kind}_{harmonic}_{metric_name}"
            row.append(format_metric(metrics.get(key)))
        lines.append("| " + " | ".join(row) + " |")
    lines.append("<!-- markdownlint-enable MD013 -->")


def append_pending_track1_matrix(lines: list[str], harmonics: list[int]) -> None:
    """Append a reset Track 1 matrix with empty pending cells."""

    lines.append("<!-- markdownlint-disable MD013 -->")
    lines.append("| Model | " + " | ".join(f"`{harmonic}`" for harmonic in harmonics) + " |")
    lines.append("| --- | " + " | ".join("---" for _ in harmonics) + " |")
    for family_definition in FAMILY_DEFINITION_LIST:
        row = [f"`{family_definition.paper_family_name}`"]
        row.extend("pending" for _ in harmonics)
        lines.append("| " + " | ".join(row) + " |")
    lines.append("<!-- markdownlint-enable MD013 -->")


def append_raw_markdown_table(lines: list[str], table_lines: list[list[str]]) -> None:
    """Append a previously parsed Markdown table."""

    if not table_lines:
        lines.append("Paper original table could not be reconstructed from the prior benchmark.")
        return
    lines.append("<!-- markdownlint-disable MD013 -->")
    for row in table_lines:
        lines.append("| " + " | ".join(row) + " |")
    lines.append("<!-- markdownlint-enable MD013 -->")


def parse_paper_original_tables(benchmark_path: Path) -> dict[str, list[list[str]]]:
    """Extract existing paper-original Tables 2-5 before the benchmark rewrite."""

    text = benchmark_path.read_text(encoding="utf-8")
    table_map: dict[str, list[list[str]]] = {}
    for table_name, _, _, _, _ in TABLE_DEFINITION_LIST:
        table_marker = f"#### {table_name} -"
        marker_index = text.find(table_marker)
        if marker_index < 0:
            continue
        paper_index = text.find("Paper-side repository-owned reconstruction:", marker_index)
        if paper_index < 0:
            continue
        table_start = text.find("| Model |", paper_index)
        if table_start < 0:
            continue
        table_lines: list[list[str]] = []
        for raw_line in text[table_start:].splitlines():
            stripped_line = raw_line.strip()
            if not stripped_line.startswith("|"):
                if table_lines:
                    break
                continue
            cells = [cell.strip() for cell in stripped_line.strip("|").split("|")]
            table_lines.append(cells)
        if table_lines:
            table_map[table_name] = table_lines
    return table_map


def read_eval_metrics(source_selection: SourceSelection) -> dict[str, float]:
    """Read the accepted eval-stage cross-validation metrics for a family."""

    eval_output_root = get_stage_root(source_selection, "eval") / "output_prediction"
    summary_path_list = sorted(eval_output_root.rglob("summaryCrossValidation+_3.8_allFreq.csv"))
    if not summary_path_list:
        raise FileNotFoundError(f"No eval summary found under {eval_output_root}")
    with summary_path_list[0].open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        row = next(reader)
    metric_map = {
        key: parse_metric_value(value)
        for key, value in row.items()
        if key != "0_method" and value not in {None, ""}
    }
    for metric_name in ["MSE", "RMSE", "MAE", "MAPE"]:
        if metric_name not in metric_map:
            metric_value_list = [
                value
                for key, value in metric_map.items()
                if key.endswith(f"_{metric_name}")
            ]
            if metric_value_list:
                metric_map[metric_name] = sum(metric_value_list) / len(metric_value_list)
    return metric_map


def read_semicolon_csv_shape(csv_path: Path) -> tuple[int, list[str]]:
    """Return row count and semicolon-delimited header columns."""

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter=";")
        header = next(reader)
        row_count = sum(1 for _ in reader)
    return row_count, header


def get_bundle_root(direction: str, bundle_name: str) -> Path:
    """Resolve a source bundle root."""

    bundle_root = RCIM_OUTPUT_ROOT / direction / bundle_name
    if not bundle_root.exists():
        raise FileNotFoundError(bundle_root)
    return bundle_root


def get_stage_root(source_selection: SourceSelection, stage_name: str) -> Path:
    """Resolve a stage root from a source selection."""

    bundle_name = {
        "retune": source_selection.retune_bundle,
        "eval": source_selection.eval_bundle,
        "export": source_selection.export_bundle,
    }[stage_name]
    stage_root = get_bundle_root(source_selection.direction, bundle_name) / stage_name
    if not stage_root.exists():
        raise FileNotFoundError(stage_root)
    return stage_root


def build_expected_target_list(direction: str) -> list[tuple[str, str, int]]:
    """Build the canonical 20 recovered-original target list."""

    direction_token = "Fw" if direction == "forward" else "Bw"
    target_list: list[tuple[str, str, int]] = []
    for target_kind in ["ampl", "phase"]:
        for harmonic_order in HARMONIC_ORDER_LIST:
            target_name = f"fft_y_{direction_token}_filtered_{target_kind}_{harmonic_order}"
            target_list.append((target_name, target_kind, harmonic_order))
    return target_list


def extract_target_name(model_path: Path) -> str:
    """Extract the recovered-original target name from an export filename."""

    match = re.search(r"(fft_y_(?:Fw|Bw)_filtered_(?:ampl|phase)_\d+)", model_path.name)
    if not match:
        raise ValueError(f"Could not extract target name from {model_path.name}")
    return match.group(1)


def target_kind_short(target_kind: str) -> str:
    """Return archive filename target-kind shorthand."""

    return "ampl" if target_kind == "ampl" else "phase"


def parse_metric_value(raw_value: str) -> float:
    """Parse recovered-original CSV decimal-comma metrics."""

    return float(raw_value.replace(",", "."))


def format_metric(value: float | None) -> str:
    """Format a report metric compactly."""

    if value is None:
        return "-"
    if value == 0:
        return "0"
    if abs(value) < 0.001:
        return f"{value:.6g}"
    return f"{value:.6f}".rstrip("0").rstrip(".")


def sha256_file(file_path: Path) -> str:
    """Return a SHA-256 digest for a file."""

    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def to_posix_relative(path: Path) -> str:
    """Return a repository-relative POSIX path."""

    return path.resolve().relative_to(PROJECT_ROOT).as_posix()


def write_text(path: Path, text: str) -> None:
    """Write UTF-8 text with parent directory creation."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalize_markdown_text(text), encoding="utf-8")


def normalize_markdown_text(text: str) -> str:
    """Collapse excessive blank lines in generated Markdown-like text."""

    normalized_text = re.sub(r"\n{3,}", "\n\n", text)
    return normalized_text.rstrip() + "\n"


def write_yaml(path: Path, payload: object) -> None:
    """Write a small YAML document without introducing a dependency."""

    write_text(path, render_yaml(payload))


def render_yaml(payload: object, indent: int = 0) -> str:
    """Render basic Python containers as deterministic YAML."""

    lines = list(iter_yaml_lines(payload, indent))
    return "\n".join(lines) + "\n"


def iter_yaml_lines(payload: object, indent: int = 0) -> Iterable[str]:
    """Yield YAML lines for simple dictionaries and lists."""

    prefix = " " * indent
    if isinstance(payload, dict):
        for key, value in payload.items():
            if isinstance(value, (dict, list)):
                yield f"{prefix}{key}:"
                yield from iter_yaml_lines(value, indent + 2)
            else:
                yield f"{prefix}{key}: {format_yaml_scalar(value)}"
    elif isinstance(payload, list):
        for item in payload:
            if isinstance(item, (dict, list)):
                yield f"{prefix}-"
                yield from iter_yaml_lines(item, indent + 2)
            else:
                yield f"{prefix}- {format_yaml_scalar(item)}"
    else:
        yield f"{prefix}{format_yaml_scalar(payload)}"


def format_yaml_scalar(value: object) -> str:
    """Format a scalar for simple YAML output."""

    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if not text:
        return "''"
    if re.fullmatch(r"[A-Za-z0-9_./:+-]+", text):
        return text
    return json.dumps(text)


if __name__ == "__main__":
    main()
