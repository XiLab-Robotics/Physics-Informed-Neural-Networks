"""Run repository-owned copies of the recovered RCIM original workflow."""

from __future__ import annotations

# Import Python Utilities
import argparse
import contextlib
import importlib.util
import json
import os
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import pandas as pd

# Import Scikit-Learn Utilities
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
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

try:
    from skelm import ELMRegressor
except ImportError:  # pragma: no cover - runtime dependency check
    ELMRegressor = None

PROJECT_PATH = Path(__file__).resolve().parents[4]
WORKFLOW_ROOT = Path(__file__).resolve().parent
LATEST_SNAPSHOT_ROOT = WORKFLOW_ROOT / "latest_snapshot"
ORIGINAL_PIPELINE_ROOT = WORKFLOW_ROOT / "original_pipeline"
OUTPUT_ROOT = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "paper_reimplementation_rcim_recovered_original_workflow"
)
TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"
PROFILE_LATEST_SNAPSHOT_V17 = "latest_snapshot_v17"
PROFILE_ORIGINAL_V18_PAPER = "original_v18_paper_family_bank"
PROFILE_ORIGINAL_V18_FULL = "original_v18_full"
AVAILABLE_PROFILE_LIST = [
    PROFILE_LATEST_SNAPSHOT_V17,
    PROFILE_ORIGINAL_V18_PAPER,
    PROFILE_ORIGINAL_V18_FULL,
]


@dataclass(frozen=True)
class PredictionProfileDefinition:

    """One runnable recovered prediction profile."""

    profile_name: str
    workspace_root: Path
    predictor_module_path: Path
    default_dataframe_path: Path
    original_style_output_folder_name: str
    run_mode: str
    description: str


PREDICTION_PROFILE_DEFINITION_MAP = {
    PROFILE_LATEST_SNAPSHOT_V17: PredictionProfileDefinition(
        profile_name=PROFILE_LATEST_SNAPSHOT_V17,
        workspace_root=LATEST_SNAPSHOT_ROOT,
        predictor_module_path=LATEST_SNAPSHOT_ROOT / "predictorML_v7.py",
        default_dataframe_path=LATEST_SNAPSHOT_ROOT / "dataFrame_prediction_Fw_v14_newFreq.csv",
        original_style_output_folder_name="instV3.2_Fw",
        run_mode="all_for_export",
        description="Recovered later snapshot with default-family export workflow.",
    ),
    PROFILE_ORIGINAL_V18_PAPER: PredictionProfileDefinition(
        profile_name=PROFILE_ORIGINAL_V18_PAPER,
        workspace_root=ORIGINAL_PIPELINE_ROOT / "1-prediction",
        predictor_module_path=ORIGINAL_PIPELINE_ROOT / "1-prediction" / "1-predictorML_v7.py",
        default_dataframe_path=LATEST_SNAPSHOT_ROOT / "dataFrame_prediction_Fw_v14_newFreq.csv",
        original_style_output_folder_name="instV3.8_Fw_allFreq_def",
        run_mode="evaluation_on_train",
        description="Recovered original v18 prediction surface restricted to the paper family bank.",
    ),
    PROFILE_ORIGINAL_V18_FULL: PredictionProfileDefinition(
        profile_name=PROFILE_ORIGINAL_V18_FULL,
        workspace_root=ORIGINAL_PIPELINE_ROOT / "1-prediction",
        predictor_module_path=ORIGINAL_PIPELINE_ROOT / "1-prediction" / "1-predictorML_v7.py",
        default_dataframe_path=LATEST_SNAPSHOT_ROOT / "dataFrame_prediction_Fw_v14_newFreq.csv",
        original_style_output_folder_name="instV3.8_Fw_allFreq_def",
        run_mode="evaluation_on_train",
        description="Recovered original v18 prediction surface including the code-only ELM branch.",
    ),
}


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


def load_predictor_module(module_path: Path, module_name: str) -> Any:

    """Load one copied predictor module from an arbitrary filesystem path."""

    module_specification = importlib.util.spec_from_file_location(module_name, module_path)
    assert module_specification is not None, f"Unable to create module specification | {module_path}"
    assert module_specification.loader is not None, f"Unable to create module loader | {module_path}"
    predictor_module = importlib.util.module_from_spec(module_specification)
    module_specification.loader.exec_module(predictor_module)
    return predictor_module


def load_prediction_dataframe(dataframe_path: Path) -> pd.DataFrame:

    """Load the recovered prediction dataframe using the original CSV format."""

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


def _build_latest_snapshot_family_builder_map() -> dict[str, Any]:

    """Build the family registry used by the recovered latest snapshot."""

    assert XGBRegressor is not None, "xgboost is required for the latest snapshot workflow"
    assert LGBMRegressor is not None, "lightgbm is required for the latest snapshot workflow"
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


def _build_original_v18_family_builder_map(include_elm_branch: bool) -> dict[str, Any]:

    """Build the family registry used by the recovered original v18 script."""

    assert XGBRegressor is not None, "xgboost is required for the original v18 workflow"
    assert LGBMRegressor is not None, "lightgbm is required for the original v18 workflow"
    family_builder_map: dict[str, Any] = {
        "SVR": lambda: SVR(C=1, epsilon=0.0001, gamma=1.1e-06, kernel="rbf"),
        "MLP": lambda: MLPRegressor(
            activation="tanh",
            early_stopping=True,
            hidden_layer_sizes=(200, 50),
            learning_rate="adaptive",
            solver="adam",
            random_state=0,
        ),
        "RF": lambda: RandomForestRegressor(
            criterion="squared_error",
            max_depth=14,
            min_samples_split=3,
            n_estimators=90,
            random_state=0,
        ),
        "DT": lambda: DecisionTreeRegressor(
            criterion="squared_error",
            max_depth=16,
            min_samples_split=6,
            random_state=0,
        ),
        "ET": lambda: ExtraTreeRegressor(
            criterion="squared_error",
            max_depth=15,
            min_samples_split=5,
            random_state=0,
        ),
        "ERT": lambda: ExtraTreesRegressor(
            criterion="squared_error",
            max_depth=15,
            min_samples_split=3,
            n_estimators=60,
            random_state=0,
        ),
        "GBM": lambda: GradientBoostingRegressor(
            criterion="squared_error",
            learning_rate=0.1,
            max_depth=14,
            min_samples_split=14,
            n_estimators=36,
            random_state=0,
        ),
        "HGBM": lambda: HistGradientBoostingRegressor(
            random_state=0,
            learning_rate=0.21,
            max_depth=11,
            max_leaf_nodes=27,
        ),
        "XGBM": lambda: XGBRegressor(
            reg_lambda=20,
            alpha=0.01,
            max_depth=16,
            colsample_bytree=0.8,
            random_state=0,
        ),
        "LGBM": lambda: LGBMRegressor(
            learning_rate=0.39,
            max_depth=12,
            subsample=0.1,
            random_state=0,
        ),
    }
    if include_elm_branch:
        assert ELMRegressor is not None, (
            "scikit-elm is required for the original_v18_full workflow because it includes ELM"
        )
        family_builder_map["ELM"] = lambda: ELMRegressor(n_neurons=250, random_state=0)
    return family_builder_map


def build_family_builder_map(profile_name: str) -> dict[str, Any]:

    """Resolve the family registry for one recovered prediction profile."""

    if profile_name == PROFILE_LATEST_SNAPSHOT_V17:
        return _build_latest_snapshot_family_builder_map()
    if profile_name == PROFILE_ORIGINAL_V18_PAPER:
        return _build_original_v18_family_builder_map(include_elm_branch=False)
    if profile_name == PROFILE_ORIGINAL_V18_FULL:
        return _build_original_v18_family_builder_map(include_elm_branch=True)
    raise ValueError(f"Unsupported profile | {profile_name}")


def normalize_family_selection_argument(
    family_selection_argument: str | None,
    family_builder_map: dict[str, Any],
) -> list[str]:

    """Normalize one optional comma-separated family selection list."""

    if not family_selection_argument:
        return list(family_builder_map.keys())
    selected_family_code_list = [
        family_code.strip().upper()
        for family_code in family_selection_argument.split(",")
        if family_code.strip()
    ]
    invalid_family_code_list = [
        family_code
        for family_code in selected_family_code_list
        if family_code not in family_builder_map
    ]
    assert not invalid_family_code_list, (
        "Unsupported family selection for recovered profile | "
        f"{', '.join(invalid_family_code_list)}"
    )
    return selected_family_code_list


def create_output_directory(profile_name: str, output_suffix: str) -> Path:

    """Create one immutable output directory for a recovered run."""

    timestamp_text = datetime.now().strftime(TIMESTAMP_FORMAT)
    safe_output_suffix = output_suffix.strip().replace(" ", "_")
    output_directory = OUTPUT_ROOT / f"{timestamp_text}_{profile_name}_{safe_output_suffix}"
    output_directory.mkdir(parents=True, exist_ok=False)
    return output_directory


def run_recovered_prediction_profile(
    profile_name: str,
    dataframe_path: Path,
    selected_family_code_list: list[str],
    output_directory: Path,
    export_onnx: bool,
    test_size: float,
) -> dict[str, Any]:

    """Run one recovered prediction profile and persist the outputs."""

    profile_definition = PREDICTION_PROFILE_DEFINITION_MAP[profile_name]
    predictor_module = load_predictor_module(
        profile_definition.predictor_module_path,
        module_name=f"recovered_original_{profile_name}_predictor",
    )
    dataframe = load_prediction_dataframe(dataframe_path)
    target_column_name_list = resolve_target_column_name_list(dataframe)
    family_builder_map = build_family_builder_map(profile_name)
    original_style_output_directory = output_directory / "original_style_output" / profile_definition.original_style_output_folder_name
    original_style_output_directory.mkdir(parents=True, exist_ok=True)
    workspace_output_prediction_directory = profile_definition.workspace_root / "output_prediction"
    workspace_output_prediction_directory.mkdir(parents=True, exist_ok=True)
    workspace_model_output_directory = profile_definition.workspace_root / "model_output_dir"
    workspace_model_output_directory.mkdir(parents=True, exist_ok=True)

    run_summary_dictionary: dict[str, Any] = {
        "profile_name": profile_name,
        "description": profile_definition.description,
        "dataframe_path": str(dataframe_path.relative_to(PROJECT_PATH)),
        "row_count": int(len(dataframe)),
        "target_column_count": int(len(target_column_name_list)),
        "selected_family_code_list": selected_family_code_list,
        "export_onnx": bool(export_onnx),
        "test_size": float(test_size),
        "generated_prediction_files": [],
        "generated_onnx_roots": [],
        "workspace_root": str(profile_definition.workspace_root.relative_to(PROJECT_PATH)),
    }

    with temporary_working_directory(profile_definition.workspace_root):
        for family_code in selected_family_code_list:
            emit_log(f"Running recovered profile {profile_name} | family={family_code}")
            estimator_instance = family_builder_map[family_code]()
            ml_model = predictor_module.MLModelMultipleOutput(estimator_instance, "", "tot")
            if profile_definition.run_mode == "all_for_export":
                prediction_dataframe = ml_model.predictorML_allForExport(dataframe)
            elif profile_definition.run_mode == "evaluation_on_train":
                prediction_dataframe = ml_model.predictorMLEvalutationOnTrain(dataframe, test_size)
            else:
                raise ValueError(f"Unsupported recovered run mode | {profile_definition.run_mode}")

            prediction_output_path = (
                original_style_output_directory
                / f"dfOutTot_prediction_{ml_model.name}.csv"
            )
            prediction_dataframe.to_csv(
                prediction_output_path,
                sep=";",
                decimal=",",
            )
            run_summary_dictionary["generated_prediction_files"].append(
                str(prediction_output_path.relative_to(PROJECT_PATH))
            )

            if export_onnx:
                onnx_output_root = original_style_output_directory / f"{ml_model.name}_MultiOutput_tot"
                if profile_definition.run_mode == "all_for_export":
                    onnx_output_root.mkdir(parents=True, exist_ok=True)
                    workspace_export_stem = f"{ml_model.name}_MultiOutput_tot"
                    for stale_export_path in workspace_model_output_directory.glob(f"{workspace_export_stem}_*.onnx"):
                        stale_export_path.unlink()
                    ml_model.exportModel(workspace_export_stem, target_column_name_list)
                    for exported_onnx_path in workspace_model_output_directory.glob(f"{workspace_export_stem}_*.onnx"):
                        shutil.copy2(
                            exported_onnx_path,
                            onnx_output_root / exported_onnx_path.name,
                        )
                else:
                    ml_model.exportModel(str(onnx_output_root), target_column_name_list)
                run_summary_dictionary["generated_onnx_roots"].append(
                    str(onnx_output_root.relative_to(PROJECT_PATH))
                )

    return run_summary_dictionary


def build_stage_status_dictionary() -> dict[str, Any]:

    """Build one honest status summary for the copied recovered stages."""

    return {
        "dataframe_creation": {
            "copied": True,
            "directly_runnable": False,
            "blocking_reason": (
                "The recovered creation stage imports instance_v5 via copied statistic.py, "
                "but no recovered instance_v5.py exists in the archived source trees."
            ),
        },
        "prediction": {
            "copied": True,
            "directly_runnable": True,
            "notes": (
                "The repository-owned wrapper can run the copied predictorML_v7 logic "
                "against the shipped recovered dataframe."
            ),
        },
        "evaluation": {
            "copied": True,
            "directly_runnable": False,
            "blocking_reason": (
                "The recovered evaluation stage imports instance_v4 and instance_v5, "
                "which are not present in the recovered original_pipeline tree."
            ),
        },
    }


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the recovered original runner."""

    parser = argparse.ArgumentParser(
        description="Run repository-owned copies of the recovered RCIM original workflow."
    )
    parser.add_argument(
        "--profile",
        choices=AVAILABLE_PROFILE_LIST,
        default=PROFILE_LATEST_SNAPSHOT_V17,
        help="Recovered prediction profile to run.",
    )
    parser.add_argument(
        "--families",
        type=str,
        default="",
        help="Optional comma-separated family-code filter.",
    )
    parser.add_argument(
        "--dataframe-path",
        type=Path,
        default=None,
        help="Optional explicit dataframe CSV path. Defaults to the selected profile input.",
    )
    parser.add_argument(
        "--output-suffix",
        type=str,
        default="manual_run",
        help="Suffix appended to the immutable recovered-workflow output directory.",
    )
    parser.add_argument(
        "--test-size",
        type=float,
        default=0.20,
        help="Test fraction used by the recovered original v18 evaluation-on-train path.",
    )
    parser.add_argument(
        "--skip-onnx-export",
        action="store_true",
        help="Disable ONNX export even for profiles that normally support it.",
    )
    parser.add_argument(
        "--print-stage-status",
        action="store_true",
        help="Print the recovered stage availability summary and exit.",
    )
    return parser.parse_args()


def main() -> None:

    """Run the recovered original workflow entry point."""

    arguments = parse_command_line_arguments()
    if arguments.print_stage_status:
        print(json.dumps(build_stage_status_dictionary(), indent=2))
        return

    profile_definition = PREDICTION_PROFILE_DEFINITION_MAP[arguments.profile]
    dataframe_path = (
        arguments.dataframe_path
        if arguments.dataframe_path is not None
        else profile_definition.default_dataframe_path
    )
    dataframe_path = dataframe_path.resolve()
    assert dataframe_path.is_file(), f"Recovered dataframe CSV not found | {dataframe_path}"

    family_builder_map = build_family_builder_map(arguments.profile)
    selected_family_code_list = normalize_family_selection_argument(
        arguments.families,
        family_builder_map,
    )
    output_directory = create_output_directory(arguments.profile, arguments.output_suffix)
    emit_log(f"Recovered output directory | {output_directory.relative_to(PROJECT_PATH)}")
    run_summary_dictionary = run_recovered_prediction_profile(
        profile_name=arguments.profile,
        dataframe_path=dataframe_path,
        selected_family_code_list=selected_family_code_list,
        output_directory=output_directory,
        export_onnx=not arguments.skip_onnx_export,
        test_size=float(arguments.test_size),
    )
    run_summary_dictionary["stage_status"] = build_stage_status_dictionary()
    run_summary_path = output_directory / "run_summary.json"
    run_summary_path.write_text(
        json.dumps(run_summary_dictionary, indent=2),
        encoding="utf-8",
    )
    emit_log(f"Recovered run summary | {run_summary_path.relative_to(PROJECT_PATH)}")


if __name__ == "__main__":

    main()
