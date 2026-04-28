"""Run the recovered-original RCIM workflow through one canonical three-stage surface."""

from __future__ import annotations

# Import Python Utilities
import argparse
import contextlib
import importlib.util
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path
from types import ModuleType
from typing import Any

# Import Scientific Python Utilities
import pandas as pd

# Import Scikit-Learn Utilities
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor

try:
    from xgboost.sklearn import XGBRegressor
except ImportError:  # pragma: no cover - runtime dependency check
    XGBRegressor = None

try:
    from lightgbm import LGBMRegressor
except ImportError:  # pragma: no cover - runtime dependency check
    LGBMRegressor = None

PROJECT_PATH = Path(__file__).resolve().parents[4]
WORKFLOW_ROOT = Path(__file__).resolve().parent
DATAFRAME_CREATION_ROOT = WORKFLOW_ROOT / "dataframe_creation"
TRAINING_ROOT = WORKFLOW_ROOT / "training"
EVALUATION_ROOT = WORKFLOW_ROOT / "evaluation"
OUTPUT_ROOT = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "paper_reimplementation_rcim_recovered_original_workflow"
)
TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"
FORWARD_DIRECTION = "forward"
BACKWARD_DIRECTION = "backward"
DIRECTION_PREFIX_MAP = {
    FORWARD_DIRECTION: "Fw",
    BACKWARD_DIRECTION: "Bw",
}
LATEST_V17_FAMILY_ORDER = [
    "DT",
    "ET",
    "ERT",
    "RF",
    "GBM",
    "HGBM",
    "XGBM",
    "LGBM",
    "MLP",
]


def emit_log(message: str) -> None:

    """Emit one flushed progress line."""

    print(f"[INFO] {message}", flush=True)


@contextlib.contextmanager
def temporary_working_directory(target_directory: Path):

    """Temporarily switch the process working directory."""

    current_working_directory = Path.cwd()
    os.chdir(target_directory)
    try:
        yield
    finally:
        os.chdir(current_working_directory)


@contextlib.contextmanager
def temporary_sys_path(target_directory: Path):

    """Temporarily prepend one directory to ``sys.path``."""

    target_directory_text = str(target_directory)
    sys.path.insert(0, target_directory_text)
    try:
        yield
    finally:
        if target_directory_text in sys.path:
            sys.path.remove(target_directory_text)


def load_python_module(module_name: str, module_path: Path) -> ModuleType:

    """Load one Python module from an arbitrary file path."""

    module_specification = importlib.util.spec_from_file_location(module_name, module_path)
    assert module_specification is not None, f"Unable to create module specification | {module_path}"
    assert module_specification.loader is not None, f"Unable to create module loader | {module_path}"
    loaded_module = importlib.util.module_from_spec(module_specification)
    sys.modules[module_name] = loaded_module
    module_specification.loader.exec_module(loaded_module)
    return loaded_module


def load_stage_module(
    module_name: str,
    module_path: Path,
    dependency_alias_path_map: dict[str, Path] | None = None,
) -> ModuleType:

    """Load one copied original-stage module with optional import aliases."""

    dependency_alias_path_map = dependency_alias_path_map or {}
    with temporary_sys_path(module_path.parent):
        for alias_name, alias_path in dependency_alias_path_map.items():
            load_python_module(alias_name, alias_path)
        return load_python_module(module_name, module_path)


def create_output_directory(stage_label: str, direction_label: str, output_suffix: str) -> Path:

    """Create one immutable output directory for the recovered-original run."""

    timestamp_text = datetime.now().strftime(TIMESTAMP_FORMAT)
    safe_output_suffix = output_suffix.strip().replace(" ", "_")
    output_directory = OUTPUT_ROOT / f"{timestamp_text}_{stage_label}_{direction_label}_{safe_output_suffix}"
    output_directory.mkdir(parents=True, exist_ok=False)
    return output_directory


def format_summary_path(path: Path) -> str:

    """Format one path for JSON summaries without assuming it lives in the repo."""

    try:
        return str(path.relative_to(PROJECT_PATH))
    except ValueError:
        return str(path)


def normalize_direction_label(direction_label: str) -> str:

    """Normalize one direction label."""

    normalized_direction_label = str(direction_label).strip().lower()
    assert normalized_direction_label in DIRECTION_PREFIX_MAP, (
        "Unsupported recovered-original direction label | "
        f"{direction_label}"
    )
    return normalized_direction_label


def resolve_dataframe_name(direction_label: str) -> str:

    """Build the original-style dataframe filename for one direction."""

    direction_prefix = DIRECTION_PREFIX_MAP[normalize_direction_label(direction_label)]
    return f"dataFrame_prediction_{direction_prefix}_v14_newFreq.csv"


def infer_direction_label_from_dataframe_path(dataframe_path: Path) -> str:

    """Infer the direction label from one dataframe filename."""

    dataframe_name = dataframe_path.name
    if "_Bw_" in dataframe_name:
        return BACKWARD_DIRECTION
    return FORWARD_DIRECTION


def resolve_default_training_dataframe_path(direction_label: str) -> Path:

    """Resolve the shipped recovered training CSV for one direction."""

    return TRAINING_ROOT / resolve_dataframe_name(direction_label)


def load_prediction_dataframe(dataframe_path: Path) -> pd.DataFrame:

    """Load one recovered prediction dataframe using the original CSV format."""

    dataframe = pd.read_csv(
        dataframe_path,
        sep=";",
        decimal=",",
        index_col=[0],
    )
    dataframe = dataframe[dataframe["deg"] <= 35].copy()
    dataframe.reset_index(inplace=True)
    return dataframe


def resolve_target_column_name_list(dataframe: pd.DataFrame) -> list[str]:

    """Resolve the original recovered target list from the dataframe header."""

    return [
        column_name
        for column_name in dataframe.columns.tolist()
        if ("ampl" in column_name) or ("phase" in column_name)
    ]


def build_latest_snapshot_v17_family_builder_map() -> dict[str, Any]:

    """Build the family registry used by the recovered ``main_prediction_v17.py``."""

    assert XGBRegressor is not None, "xgboost is required for the recovered-original training stage"
    assert LGBMRegressor is not None, "lightgbm is required for the recovered-original training stage"
    return {
        "DT": lambda: DecisionTreeRegressor(),
        "ET": lambda: ExtraTreeRegressor(),
        "ERT": lambda: ExtraTreesRegressor(),
        "RF": lambda: RandomForestRegressor(),
        "GBM": lambda: GradientBoostingRegressor(),
        "HGBM": lambda: HistGradientBoostingRegressor(),
        "XGBM": lambda: XGBRegressor(),
        "LGBM": lambda: LGBMRegressor(),
        "MLP": lambda: MLPRegressor(),
    }


def normalize_family_selection_argument(family_selection_argument: str | None) -> list[str]:

    """Normalize one optional comma-separated family selection list."""

    if not family_selection_argument:
        return list(LATEST_V17_FAMILY_ORDER)

    selected_family_code_list = [
        family_code.strip().upper()
        for family_code in family_selection_argument.split(",")
        if family_code.strip()
    ]
    invalid_family_code_list = [
        family_code
        for family_code in selected_family_code_list
        if family_code not in LATEST_V17_FAMILY_ORDER
    ]
    assert not invalid_family_code_list, (
        "Unsupported recovered-original family selection | "
        f"{', '.join(invalid_family_code_list)}"
    )
    return selected_family_code_list


def copy_generated_onnx_files(
    workspace_model_output_directory: Path,
    export_stem: str,
    artifact_model_output_directory: Path,
) -> list[str]:

    """Copy one original-style ONNX family export set into the immutable artifact."""

    copied_file_list: list[str] = []
    artifact_model_output_directory.mkdir(parents=True, exist_ok=True)
    for workspace_onnx_path in sorted(workspace_model_output_directory.glob(f"{export_stem}_*.onnx")):
        artifact_onnx_path = artifact_model_output_directory / workspace_onnx_path.name
        shutil.copy2(workspace_onnx_path, artifact_onnx_path)
        copied_file_list.append(str(artifact_onnx_path.relative_to(PROJECT_PATH)))
    return copied_file_list


def run_dataframe_creation_stage(
    instances_path: Path,
    direction_label: str,
    output_directory: Path,
) -> dict[str, Any]:

    """Run the recovered-original dataframe-creation stage."""

    normalized_direction_label = normalize_direction_label(direction_label)
    direction_prefix = DIRECTION_PREFIX_MAP[normalized_direction_label]
    dataframe_output_directory = output_directory / "dataframe_creation"
    dataframe_output_directory.mkdir(parents=True, exist_ok=True)

    emit_log(
        "Running recovered-original dataframe creation | "
        f"direction={normalized_direction_label} "
        f"instances={instances_path}"
    )
    statistic_module = load_stage_module(
        "recovered_original_dataframe_creation_statistic",
        DATAFRAME_CREATION_ROOT / "0-statistic.py",
    )
    with temporary_working_directory(DATAFRAME_CREATION_ROOT):
        statistics_object = statistic_module.Statistics()
        statistics_object.read_all_fft(str(instances_path))
        output_dataframe = statistics_object.genDfWithAmplEPhase(direction_prefix)

    dataframe_path = dataframe_output_directory / resolve_dataframe_name(normalized_direction_label)
    output_dataframe.to_csv(
        dataframe_path,
        sep=";",
        decimal=",",
    )
    return {
        "stage_name": "dataframe_creation",
        "direction_label": normalized_direction_label,
        "instances_path": format_summary_path(instances_path),
        "dataframe_path": format_summary_path(dataframe_path),
        "row_count": int(len(output_dataframe)),
        "column_count": int(len(output_dataframe.columns)),
    }


def run_training_stage(
    dataframe_path: Path,
    direction_label: str,
    selected_family_code_list: list[str],
    output_directory: Path,
    export_onnx: bool,
) -> dict[str, Any]:

    """Run the canonical recovered-original training stage based on ``v17``."""

    normalized_direction_label = normalize_direction_label(direction_label)
    direction_prefix = DIRECTION_PREFIX_MAP[normalized_direction_label]
    family_builder_map = build_latest_snapshot_v17_family_builder_map()
    predictor_module = load_stage_module(
        "recovered_original_training_predictor",
        TRAINING_ROOT / "predictorML_v7.py",
    )
    dataframe = load_prediction_dataframe(dataframe_path)
    target_column_name_list = resolve_target_column_name_list(dataframe)

    training_output_directory = output_directory / "training"
    training_output_directory.mkdir(parents=True, exist_ok=True)
    artifact_prediction_directory = training_output_directory / "output_prediction" / f"instV3.2_{direction_prefix}"
    artifact_prediction_directory.mkdir(parents=True, exist_ok=True)
    artifact_model_output_directory = training_output_directory / "model_output_dir"
    artifact_model_output_directory.mkdir(parents=True, exist_ok=True)

    workspace_prediction_directory = TRAINING_ROOT / "output_prediction" / f"instV3.2_{direction_prefix}"
    workspace_prediction_directory.mkdir(parents=True, exist_ok=True)
    workspace_model_output_directory = TRAINING_ROOT / "model_output_dir"
    workspace_model_output_directory.mkdir(parents=True, exist_ok=True)

    generated_prediction_file_list: list[str] = []
    generated_onnx_file_list: list[str] = []

    with temporary_working_directory(TRAINING_ROOT):
        for family_code in selected_family_code_list:
            emit_log(f"Running recovered-original training | family={family_code}")
            estimator_instance = family_builder_map[family_code]()
            ml_model = predictor_module.MLModelMultipleOutput(estimator_instance, "", "tot")
            prediction_dataframe = ml_model.predictorML_allForExport(dataframe)

            prediction_filename = f"dfOutTot_prediction_{ml_model.name}.csv"
            workspace_prediction_path = workspace_prediction_directory / prediction_filename
            artifact_prediction_path = artifact_prediction_directory / prediction_filename
            prediction_dataframe.to_csv(
                workspace_prediction_path,
                sep=";",
                decimal=",",
            )
            shutil.copy2(workspace_prediction_path, artifact_prediction_path)
            generated_prediction_file_list.append(
                str(artifact_prediction_path.relative_to(PROJECT_PATH))
            )

            if export_onnx:
                export_stem = f"{ml_model.name}_MultiOutput_tot"
                for stale_export_path in workspace_model_output_directory.glob(f"{export_stem}_*.onnx"):
                    stale_export_path.unlink()
                ml_model.exportModel(export_stem, target_column_name_list)
                generated_onnx_file_list.extend(
                    copy_generated_onnx_files(
                        workspace_model_output_directory,
                        export_stem,
                        artifact_model_output_directory,
                    )
                )

    return {
        "stage_name": "training",
        "direction_label": normalized_direction_label,
        "dataframe_path": format_summary_path(dataframe_path),
        "filtered_row_count": int(len(dataframe)),
        "target_column_count": int(len(target_column_name_list)),
        "selected_family_code_list": selected_family_code_list,
        "generated_prediction_files": generated_prediction_file_list,
        "generated_onnx_files": generated_onnx_file_list,
        "artifact_prediction_directory": str(artifact_prediction_directory.relative_to(PROJECT_PATH)),
    }


def prepare_evaluation_runtime_directories(runtime_root: Path) -> None:

    """Create the hardcoded original-style folders expected by the evaluation scripts."""

    (runtime_root / "evaluation" / "instV2.1" / "details").mkdir(parents=True, exist_ok=True)
    (runtime_root / "evaluation" / "instV2.1" / "perPaper").mkdir(parents=True, exist_ok=True)
    (runtime_root / "20240130_evaluationSignal").mkdir(parents=True, exist_ok=True)


def run_evaluation_stage(
    instances_path: Path,
    prediction_directory: Path,
    output_directory: Path,
    run_prediction_v4: bool,
    run_signals: bool,
) -> dict[str, Any]:

    """Run the recovered-original evaluation stage on top of generated prediction CSVs."""

    prediction_file_path_list = sorted(prediction_directory.glob("dfOutTot_prediction_*.csv"))
    assert prediction_file_path_list, f"No recovered prediction CSVs found | {prediction_directory}"

    runtime_root = output_directory / "evaluation" / "original_style_runtime"
    runtime_root.mkdir(parents=True, exist_ok=True)
    prepare_evaluation_runtime_directories(runtime_root)

    emit_log(
        "Running recovered-original evaluation | "
        f"instances={instances_path} "
        f"predictions={prediction_directory}"
    )
    statistic_module = load_stage_module(
        "statistic",
        EVALUATION_ROOT / "0-statistic.py",
    )
    with temporary_working_directory(runtime_root):
        statistics_object = statistic_module.Statistics()
        statistics_object.read_all_fft(str(instances_path))

        if run_prediction_v4:
            evaluation_prediction_module = load_stage_module(
                "recovered_original_evaluate_prediction_v4",
                EVALUATION_ROOT / "2-main_evaluatePrediction_v4.py",
                dependency_alias_path_map={
                    "statistic": EVALUATION_ROOT / "0-statistic.py",
                },
            )
            for prediction_file_path in prediction_file_path_list:
                evaluation_prediction_module.evaluatePredictionFile(
                    statistics_object,
                    str(prediction_file_path.resolve()),
                )

        if run_signals:
            evaluation_signal_module = load_stage_module(
                "recovered_original_evaluate_signals",
                EVALUATION_ROOT / "2-main_evaluateSignals.py",
                dependency_alias_path_map={
                    "statistic": EVALUATION_ROOT / "0-statistic.py",
                },
            )
            for prediction_file_path in prediction_file_path_list:
                evaluation_signal_module.evaluatePredictionFile(
                    statistics_object,
                    str(prediction_file_path.resolve()),
                )

    generated_artifact_list = [
        str(path.relative_to(PROJECT_PATH))
        for path in sorted(runtime_root.rglob("*"))
        if path.is_file()
    ]
    return {
        "stage_name": "evaluation",
        "instances_path": format_summary_path(instances_path),
        "prediction_directory": format_summary_path(prediction_directory),
        "prediction_file_count": int(len(prediction_file_path_list)),
        "ran_evaluate_prediction_v4": bool(run_prediction_v4),
        "ran_evaluate_signals": bool(run_signals),
        "generated_artifacts": generated_artifact_list,
    }


def build_stage_status_dictionary() -> dict[str, Any]:

    """Build one honest status summary for the reorganized recovered workflow."""

    return {
        "dataframe_creation": {
            "copied": True,
            "primary_code": "dataframe_creation/0-main_createDFforPrediction.py",
            "primary_support": "dataframe_creation/0-statistic.py",
            "dependency_note": "Requires an external original-style instance CSV directory.",
        },
        "training": {
            "copied": True,
            "primary_code": "training/main_prediction_v17.py",
            "primary_support": "training/predictorML_v7.py",
            "scope_note": "This is the canonical recovered-original paper training surface used by the repository wrapper.",
        },
        "evaluation": {
            "copied": True,
            "primary_codes": [
                "evaluation/2-main_evaluatePrediction_v4.py",
                "evaluation/2-main_evaluateSignals.py",
            ],
            "dependency_note": "Requires an external original-style instance CSV directory and prediction CSV outputs from the training stage.",
        },
    }


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the recovered-original runner."""

    parser = argparse.ArgumentParser(
        description="Run the reorganized recovered-original RCIM workflow."
    )
    parser.add_argument(
        "--stage",
        choices=["all", "dataframe_creation", "training", "evaluation"],
        default="training",
        help="Recovered-original stage to run.",
    )
    parser.add_argument(
        "--direction",
        choices=[FORWARD_DIRECTION, BACKWARD_DIRECTION],
        default=FORWARD_DIRECTION,
        help="Direction used for dataframe creation and training naming.",
    )
    parser.add_argument(
        "--instances-path",
        type=Path,
        default=None,
        help="Path to the original-style instance CSV directory used by dataframe creation and evaluation.",
    )
    parser.add_argument(
        "--dataframe-path",
        type=Path,
        default=None,
        help="Optional explicit recovered dataframe CSV path for the training stage.",
    )
    parser.add_argument(
        "--prediction-directory",
        type=Path,
        default=None,
        help="Optional explicit prediction-directory path for the evaluation stage.",
    )
    parser.add_argument(
        "--families",
        type=str,
        default="",
        help="Optional comma-separated family-code filter for the training stage.",
    )
    parser.add_argument(
        "--output-suffix",
        type=str,
        default="manual_run",
        help="Suffix appended to the immutable recovered-original output directory.",
    )
    parser.add_argument(
        "--skip-onnx-export",
        action="store_true",
        help="Disable ONNX export for the training stage.",
    )
    parser.add_argument(
        "--skip-evaluate-prediction-v4",
        action="store_true",
        help="Skip the copied `2-main_evaluatePrediction_v4.py` pass.",
    )
    parser.add_argument(
        "--skip-evaluate-signals",
        action="store_true",
        help="Skip the copied `2-main_evaluateSignals.py` pass.",
    )
    parser.add_argument(
        "--print-stage-status",
        action="store_true",
        help="Print the recovered-original stage summary and exit.",
    )
    return parser.parse_args()


def main() -> None:

    """Run the recovered-original workflow entry point."""

    arguments = parse_command_line_arguments()
    if arguments.print_stage_status:
        print(json.dumps(build_stage_status_dictionary(), indent=2))
        return

    normalized_direction_label = normalize_direction_label(arguments.direction)
    output_directory = create_output_directory(
        arguments.stage,
        normalized_direction_label,
        arguments.output_suffix,
    )
    emit_log(f"Recovered-original output directory | {output_directory.relative_to(PROJECT_PATH)}")

    run_summary_dictionary: dict[str, Any] = {
        "stage": arguments.stage,
        "direction_label": normalized_direction_label,
        "output_directory": str(output_directory.relative_to(PROJECT_PATH)),
        "stage_status": build_stage_status_dictionary(),
    }

    dataframe_stage_summary: dict[str, Any] | None = None
    training_stage_summary: dict[str, Any] | None = None

    if arguments.stage in {"all", "dataframe_creation"}:
        assert arguments.instances_path is not None, (
            "--instances-path is required for dataframe_creation or all"
        )
        dataframe_stage_summary = run_dataframe_creation_stage(
            arguments.instances_path.resolve(),
            normalized_direction_label,
            output_directory,
        )
        run_summary_dictionary["dataframe_creation"] = dataframe_stage_summary

    if arguments.stage in {"all", "training"}:
        dataframe_path = (
            arguments.dataframe_path.resolve()
            if arguments.dataframe_path is not None
            else None
        )
        if dataframe_path is None and dataframe_stage_summary is not None:
            dataframe_path = PROJECT_PATH / dataframe_stage_summary["dataframe_path"]
        if dataframe_path is None:
            dataframe_path = resolve_default_training_dataframe_path(normalized_direction_label)
        selected_family_code_list = normalize_family_selection_argument(arguments.families)
        training_stage_summary = run_training_stage(
            dataframe_path.resolve(),
            normalized_direction_label,
            selected_family_code_list,
            output_directory,
            export_onnx=not arguments.skip_onnx_export,
        )
        run_summary_dictionary["training"] = training_stage_summary

    if arguments.stage in {"all", "evaluation"}:
        assert arguments.instances_path is not None, (
            "--instances-path is required for evaluation or all"
        )
        assert normalized_direction_label == FORWARD_DIRECTION, (
            "The copied recovered-original evaluation scripts are forward-specific."
        )
        prediction_directory = (
            arguments.prediction_directory.resolve()
            if arguments.prediction_directory is not None
            else None
        )
        if prediction_directory is None and training_stage_summary is not None:
            prediction_directory = PROJECT_PATH / training_stage_summary["artifact_prediction_directory"]
        assert prediction_directory is not None, (
            "--prediction-directory is required for standalone evaluation runs"
        )
        evaluation_stage_summary = run_evaluation_stage(
            arguments.instances_path.resolve(),
            prediction_directory,
            output_directory,
            run_prediction_v4=not arguments.skip_evaluate_prediction_v4,
            run_signals=not arguments.skip_evaluate_signals,
        )
        run_summary_dictionary["evaluation"] = evaluation_stage_summary

    run_summary_path = output_directory / "run_summary.json"
    run_summary_path.write_text(
        json.dumps(run_summary_dictionary, indent=2),
        encoding="utf-8",
    )
    emit_log(f"Recovered-original run summary | {run_summary_path.relative_to(PROJECT_PATH)}")


if __name__ == "__main__":

    main()
