"""Direct entrypoint for the recovered original RCIM training and export stage."""

import argparse
import json
import os
import shutil
import sys
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

import pandas as pd


SCRIPT_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = SCRIPT_ROOT.parents[3]
UTILITIES_ROOT = SCRIPT_ROOT / "utilities"
REFERENCE_ROOT = REPOSITORY_ROOT / "reference" / "rcim_ml_compensation_recovered_assets" / "code" / "original_pipeline"
DEFAULT_VALIDATION_ROOT = REPOSITORY_ROOT / "output" / "validation_checks" / "paper_reimplementation_rcim_recovered_original_workflow"


def _ensure_utilities_on_path():
    """Expose the copied original utility modules to Python imports."""
    if str(UTILITIES_ROOT) not in sys.path:
        sys.path.insert(0, str(UTILITIES_ROOT))


def _normalize_direction(direction):
    """Map CLI direction aliases to the original RCIM suffixes."""
    normalized_direction = direction.strip().lower()
    if normalized_direction in {"fw", "forward"}:
        return "Fw", "forward"
    if normalized_direction in {"bw", "backward"}:
        return "Bw", "backward"
    raise ValueError(f"Unsupported direction: {direction}")


def _normalize_mode(mode):
    """Normalize training mode aliases."""
    normalized_mode = mode.strip().lower()
    if normalized_mode in {"export", "v17_export"}:
        return "export"
    if normalized_mode in {"retune", "v17_retune", "crossval"}:
        return "retune"
    if normalized_mode in {"paper_eval", "v18", "paper"}:
        return "paper_eval"
    raise ValueError(f"Unsupported training mode: {mode}")


def _build_default_output_root(mode_name, direction_label, output_suffix):
    """Create the default repository-owned runtime root for this stage."""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    suffix = f"_{output_suffix}" if output_suffix else ""
    return DEFAULT_VALIDATION_ROOT / f"{timestamp}__training_{mode_name}_{direction_label}{suffix}"


def _write_summary(summary_path, payload):
    """Persist a minimal JSON summary for reproducibility."""
    with open(summary_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


@contextmanager
def _pushd(target_directory_path):
    """Temporarily change the working directory."""
    original_directory = Path.cwd()
    os.chdir(target_directory_path)
    try:
        yield
    finally:
        os.chdir(original_directory)


def _build_argument_parser():
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        default="paper_eval",
        help="Training mode: export, retune, or paper_eval.",
    )
    parser.add_argument(
        "--direction",
        default="forward",
        help="Direction to train: forward/Fw or backward/Bw.",
    )
    parser.add_argument(
        "--dataframe-path",
        type=Path,
        default=None,
        help="Optional dataframe CSV path. Defaults to the shipped recovered CSV for the selected direction.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=None,
        help="Repository-owned runtime root. Defaults under output/validation_checks/.",
    )
    parser.add_argument(
        "--output-suffix",
        default="",
        help="Optional suffix appended to the default runtime root name.",
    )
    parser.add_argument(
        "--families",
        default="",
        help="Comma-separated family subset. Supports acronyms such as DT, RF, SVR, XGBM, ELM.",
    )
    parser.add_argument(
        "--test-size",
        type=float,
        default=0.20,
        help="Held-out test fraction for v18 and retuning flows.",
    )
    parser.add_argument(
        "--disable-deg-filter",
        action="store_true",
        help="Disable the original deg <= 35 oil-temperature filter.",
    )
    return parser


def _build_family_factory_map():
    """Build the family registry used by the recovered original training stage."""
    return {
        "DT": lambda: __import__("sklearn.tree", fromlist=["DecisionTreeRegressor"]).DecisionTreeRegressor(),
        "ET": lambda: __import__("sklearn.tree", fromlist=["ExtraTreeRegressor"]).ExtraTreeRegressor(),
        "ERT": lambda: __import__("sklearn.ensemble", fromlist=["ExtraTreesRegressor"]).ExtraTreesRegressor(),
        "RF": lambda: __import__("sklearn.ensemble", fromlist=["RandomForestRegressor"]).RandomForestRegressor(),
        "GBM": lambda: __import__("sklearn.ensemble", fromlist=["GradientBoostingRegressor"]).GradientBoostingRegressor(),
        "HGBM": lambda: __import__("sklearn.ensemble", fromlist=["HistGradientBoostingRegressor"]).HistGradientBoostingRegressor(),
        "XGBM": lambda: __import__("xgboost.sklearn", fromlist=["XGBRegressor"]).XGBRegressor(),
        "LGBM": lambda: __import__("lightgbm", fromlist=["LGBMRegressor"]).LGBMRegressor(),
        "MLP": lambda: __import__("sklearn.neural_network", fromlist=["MLPRegressor"]).MLPRegressor(),
        "SVR": lambda: __import__("sklearn.svm", fromlist=["SVR"]).SVR(),
        "SVM": lambda: __import__("sklearn.svm", fromlist=["SVR"]).SVR(),
        "ELM": lambda: __import__("skelm", fromlist=["ELMRegressor"]).ELMRegressor(),
    }


def _build_paper_tuned_family_factory_map():
    """Build the tuned v18 family registry from the recovered original file."""
    return {
        "SVR": lambda: __import__("sklearn.svm", fromlist=["SVR"]).SVR(C=1, epsilon=0.0001, gamma=1.1e-06, kernel="rbf"),
        "MLP": lambda: __import__("sklearn.neural_network", fromlist=["MLPRegressor"]).MLPRegressor(
            activation="tanh",
            early_stopping=True,
            hidden_layer_sizes=(200, 50),
            learning_rate="adaptive",
            solver="adam",
            random_state=0,
        ),
        "RF": lambda: __import__("sklearn.ensemble", fromlist=["RandomForestRegressor"]).RandomForestRegressor(
            criterion="squared_error",
            max_depth=14,
            min_samples_split=3,
            n_estimators=90,
            random_state=0,
        ),
        "DT": lambda: __import__("sklearn.tree", fromlist=["DecisionTreeRegressor"]).DecisionTreeRegressor(
            criterion="squared_error",
            max_depth=16,
            min_samples_split=6,
            random_state=0,
        ),
        "ET": lambda: __import__("sklearn.tree", fromlist=["ExtraTreeRegressor"]).ExtraTreeRegressor(
            criterion="squared_error",
            max_depth=15,
            min_samples_split=5,
            random_state=0,
        ),
        "ERT": lambda: __import__("sklearn.ensemble", fromlist=["ExtraTreesRegressor"]).ExtraTreesRegressor(
            criterion="squared_error",
            max_depth=15,
            min_samples_split=3,
            n_estimators=60,
            random_state=0,
        ),
        "GBM": lambda: __import__("sklearn.ensemble", fromlist=["GradientBoostingRegressor"]).GradientBoostingRegressor(
            criterion="squared_error",
            learning_rate=0.1,
            max_depth=14,
            min_samples_split=14,
            n_estimators=36,
            random_state=0,
        ),
        "HGBM": lambda: __import__("sklearn.ensemble", fromlist=["HistGradientBoostingRegressor"]).HistGradientBoostingRegressor(
            random_state=0,
            learning_rate=0.21,
            max_depth=11,
            max_leaf_nodes=27,
        ),
        "LGBM": lambda: __import__("lightgbm", fromlist=["LGBMRegressor"]).LGBMRegressor(
            learning_rate=0.39,
            max_depth=12,
            subsample=0.1,
            random_state=0,
        ),
        "XGBM": lambda: __import__("xgboost.sklearn", fromlist=["XGBRegressor"]).XGBRegressor(
            reg_lambda=20,
            alpha=0.01,
            max_depth=16,
            colsample_bytree=0.8,
            random_state=0,
        ),
        "ELM": lambda: __import__("skelm", fromlist=["ELMRegressor"]).ELMRegressor(n_neurons=250, random_state=0),
    }


def _resolve_family_code_list(mode_name, families_argument):
    """Resolve the family order for the selected mode."""
    if families_argument:
        return [family_code.strip().upper() for family_code in families_argument.split(",") if family_code.strip()]
    if mode_name == "paper_eval":
        return ["SVR", "MLP", "RF", "DT", "ET", "ERT", "GBM", "HGBM", "LGBM", "XGBM", "ELM"]
    return ["DT", "ET", "ERT", "RF", "GBM", "HGBM", "XGBM", "LGBM", "MLP"]


def _select_family_list(mode_name, families_argument):
    """Instantiate the selected family list for the chosen mode."""
    default_factory_map = _build_family_factory_map()
    paper_factory_map = _build_paper_tuned_family_factory_map()
    family_code_list = _resolve_family_code_list(mode_name, families_argument)

    instantiated_family_list = []
    resolved_family_code_list = []
    for family_code in family_code_list:
        if mode_name == "paper_eval":
            factory = paper_factory_map.get(family_code)
        else:
            factory = default_factory_map.get(family_code)
        if factory is None:
            raise ValueError(f"Unsupported family code for mode {mode_name}: {family_code}")
        instantiated_family_list.append(factory())
        resolved_family_code_list.append(family_code)
    return resolved_family_code_list, instantiated_family_list


def _copy_dataframe_to_runtime(source_dataframe_path, runtime_root, direction_code):
    """Copy the selected dataframe into the runtime root using the original filename."""
    runtime_dataframe_name = f"dataFrame_prediction_{direction_code}_v14_newFreq.csv"
    runtime_dataframe_path = runtime_root / runtime_dataframe_name
    shutil.copy2(source_dataframe_path, runtime_dataframe_path)
    return runtime_dataframe_name, runtime_dataframe_path


def _build_prediction_output_folder_name(mode_name, direction_code):
    """Resolve the original-style output folder used by the selected training mode."""
    if mode_name == "paper_eval":
        return f"output_prediction/instV3.8_{direction_code}_allFreq_def/"
    return "output_prediction/"


def main():
    """Run the recovered original training stage with repository-owned path handling."""
    parser = _build_argument_parser()
    args = parser.parse_args()

    _ensure_utilities_on_path()
    from predictorML import MLModelMultipleOutput  # pylint: disable=import-outside-toplevel

    direction_code, direction_label = _normalize_direction(args.direction)
    mode_name = _normalize_mode(args.mode)
    dataframe_path = (args.dataframe_path or (REFERENCE_ROOT / f"dataFrame_prediction_{direction_code}_v14_newFreq.csv")).resolve()
    output_root = args.output_root or _build_default_output_root(mode_name, direction_label, args.output_suffix)
    output_root = output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "output_prediction").mkdir(exist_ok=True)
    (output_root / "model_output_dir").mkdir(exist_ok=True)

    runtime_dataframe_name, runtime_dataframe_path = _copy_dataframe_to_runtime(dataframe_path, output_root, direction_code)
    output_folder_name = _build_prediction_output_folder_name(mode_name, direction_code)
    (output_root / output_folder_name).mkdir(parents=True, exist_ok=True)
    selected_family_code_list, model_list = _select_family_list(mode_name, args.families)

    with _pushd(output_root):
        df_input = pd.read_csv(runtime_dataframe_name, sep=";", decimal=",", index_col=[0])
        if not args.disable_deg_filter:
            df_input = df_input[df_input["deg"] <= 35]
        df_input.reset_index(inplace=True)
        cols_to_predict = [column_name for column_name in df_input.columns if "ampl" in column_name or "phase" in column_name]

        generated_prediction_path_list = []
        for model in model_list:
            df_output_total = pd.DataFrame()
            if mode_name == "export":
                ml_model = MLModelMultipleOutput(model, "", "tot")
                df_output = ml_model.predictorML_allForExport(df_input, args.test_size)
                ml_model.exportModel(ml_model.name + "_MultiOutput_" + "tot", cols_to_predict)
            elif mode_name == "retune":
                ml_model = MLModelMultipleOutput(model, "crossValidationWithHyperparameter_3.8_allFreq", "tot")
                df_output = ml_model.predictorMLCrossValidationWithHyperparameter(df_input, args.test_size)
            else:
                ml_model = MLModelMultipleOutput(model, "multipleOutputEvaluationOnTrain_3.8_allFreq", "tot")
                df_output = ml_model.predictorMLEvalutationOnTrain(df_input, args.test_size)

            if df_output_total.empty:
                df_output_total = df_output
            else:
                df_output_total = df_output_total.merge(df_output, on=["rpm", "deg", "tor"])

            prediction_output_path = output_root / output_folder_name / f"dfOutTot_prediction_{ml_model.name}.csv"
            df_output_total.to_csv(prediction_output_path, sep=";", decimal=",")
            generated_prediction_path_list.append(str(prediction_output_path))

    _write_summary(
        output_root / "run_summary.json",
        {
            "stage": "training_models",
            "mode": mode_name,
            "direction": direction_label,
            "input_dataframe_path": str(dataframe_path),
            "runtime_dataframe_path": str(runtime_dataframe_path),
            "deg_filter_enabled": not args.disable_deg_filter,
            "test_size": args.test_size,
            "selected_families": selected_family_code_list,
            "prediction_output_folder": str(output_root / output_folder_name),
            "model_output_dir": str(output_root / "model_output_dir"),
            "generated_prediction_paths": generated_prediction_path_list,
        },
    )
    print(output_root)


if __name__ == "__main__":
    main()
