""" Direct entrypoint for the recovered original RCIM training and export stage. """

import argparse, ast, re, sys
from pathlib import Path

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVR
from sklearn.svm import SVR

try:

    # Import shared runtime helpers for the recovered original workflow.
    from workflow_runtime import REFERENCE_ROOT
    from workflow_runtime import build_default_output_root
    from workflow_runtime import build_prediction_output_folder_name
    from workflow_runtime import copy_dataframe_to_runtime
    from workflow_runtime import ensure_utilities_on_path
    from workflow_runtime import normalize_direction
    from workflow_runtime import pushd
    from workflow_runtime import write_summary

except ModuleNotFoundError:

    # Pragma: no cover - import compatibility for Sphinx
    from .workflow_runtime import REFERENCE_ROOT
    from .workflow_runtime import build_default_output_root
    from .workflow_runtime import build_prediction_output_folder_name
    from .workflow_runtime import copy_dataframe_to_runtime
    from .workflow_runtime import ensure_utilities_on_path
    from .workflow_runtime import normalize_direction
    from .workflow_runtime import pushd
    from .workflow_runtime import write_summary

def _normalize_mode(mode):

    """ Normalize training mode aliases. """

    # Map CLI Mode Aliases To The Original RCIM Training Modes
    normalized_mode = mode.strip().lower()
    if normalized_mode in {"export", "v17_export"}: return "export"
    if normalized_mode in {"retune", "v17_retune", "crossval"}: return "retune"
    if normalized_mode in {"paper_export", "v18_export", "paperexport", "export_tuned"}: return "paper_export"
    if normalized_mode in {"paper_eval", "v18", "paper", "eval", "original"}: return "paper_eval"
    raise ValueError(f"Unsupported training mode: {mode}")

PAPER_REFERENCE_FAMILY_CODE_LIST = ["SVR", "MLP", "RF", "DT", "ET", "ERT", "GBM", "HGBM", "LGBM", "XGBM", "ELM"]
SVR_VARIANT_KEY = "__rcim_svr_variant__"
SVR_VARIANT_PARAMETERS_KEY = "__rcim_svr_parameters__"
SVR_VARIANT_RBF = "paper_faithful_rbf"
SVR_VARIANT_LINEAR_FALLBACK = "pragmatic_linear_fallback"

def _tag_family_display_name(estimator, family_display_name):

    """ Tag one estimator so the legacy wrappers keep the family-facing name. """

    # Tag the Estimator so the Legacy Wrappers Keep the Family-Facing Name.
    setattr(estimator, "_rcim_display_name", family_display_name)
    return estimator

def _build_pragmatic_linear_svr_pipeline(C=1.0, epsilon=0.0001, tol=1e-4, max_iter=5000):

    """ Build the repository-owned pragmatic linear fallback for the SVR family. """

    # Pragmatic Linear SVR Pipeline
    linear_pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "model",
                LinearSVR(
                    C=C,
                    epsilon=epsilon,
                    tol=tol,
                    max_iter=max_iter,
                    random_state=0,
                ),
            ),
        ]
    )
    return _tag_family_display_name(linear_pipeline, "SVR")

def _build_paper_faithful_rbf_svr(C=1.0, epsilon=0.0001, gamma=1.1e-06, kernel="rbf"):

    """ Build the paper-faithful tuned SVR RBF estimator. """

    # Paper-Faithful SVR RBF Estimator
    return _tag_family_display_name(
        SVR(
            C=C,
            epsilon=epsilon,
            gamma=gamma,
            kernel=kernel,
        ),
        "SVR",
    )

def _build_repo_quiet_lgbm_regressor(**parameter_payload):

    """Build one repo-owned LGBMRegressor with suppressed native log flooding."""

    # Keep the Native LightGBM Console Chatter Under Control During Long Retune Runs.
    base_parameter_payload = {
        "verbosity": -1,
        "force_col_wise": True,
    }
    base_parameter_payload.update(parameter_payload)
    return __import__("lightgbm", fromlist=["LGBMRegressor"]).LGBMRegressor(**base_parameter_payload)

def _configure_stream_buffering():

    """ Force line-buffered output for long-running redirected training stages. """

    # Keep the Stage Observable Even When the Launcher Redirects Output to Log Files.
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(line_buffering=True, write_through=True)
        except Exception:
            # Best-effort Only; Older Python Surfaces May Reject Runtime Reconfiguration.
            pass

def _build_argument_parser():

    """ Build the CLI argument parser. """

    # Argument Parser
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", default="paper_eval", help="Training mode: export, retune, paper_eval, or paper_export.")
    parser.add_argument("--direction", default="forward", help="Direction to train: forward/Fw or backward/Bw.")
    parser.add_argument("--dataframe-path", type=Path, default=None, help="Optional dataframe CSV path. Defaults to the shipped recovered CSV for the selected direction.")
    parser.add_argument("--output-root", type=Path, default=None, help="Repository-owned runtime root. Defaults under output/validation_checks/.")
    parser.add_argument("--output-suffix", default="", help="Optional suffix appended to the default runtime root name.")
    parser.add_argument("--families", default="", help="Comma-separated family subset. Supports acronyms such as DT, RF, SVR, XGBM, ELM.")
    parser.add_argument("--test-size", type=float, default=0.20, help="Held-out test fraction for v18 and retuning flows.")
    parser.add_argument("--best-parameter-summary-path", type=Path, default=None, help="Optional semicolon-delimited summaryBestParameter CSV exported by the retune path.")
    parser.add_argument("--retune-grid-search-verbose", type=int, default=10, help="GridSearchCV verbosity used by the retune path.")
    parser.add_argument("--retune-cross-validate-verbose", type=int, default=10, help="cross_validate verbosity used by the retune path.")
    return parser

def _build_family_factory_map():

    """ Build the family registry used by the recovered original training stage. """

    return {
        "DT": lambda: __import__("sklearn.tree", fromlist=["DecisionTreeRegressor"]).DecisionTreeRegressor(),
        "ET": lambda: __import__("sklearn.tree", fromlist=["ExtraTreeRegressor"]).ExtraTreeRegressor(),
        "ERT": lambda: __import__("sklearn.ensemble", fromlist=["ExtraTreesRegressor"]).ExtraTreesRegressor(),
        "RF": lambda: __import__("sklearn.ensemble", fromlist=["RandomForestRegressor"]).RandomForestRegressor(),
        "GBM": lambda: __import__("sklearn.ensemble", fromlist=["GradientBoostingRegressor"]).GradientBoostingRegressor(),
        "HGBM": lambda: __import__("sklearn.ensemble", fromlist=["HistGradientBoostingRegressor"]).HistGradientBoostingRegressor(),
        "XGBM": lambda: __import__("xgboost.sklearn", fromlist=["XGBRegressor"]).XGBRegressor(),
        "LGBM": lambda: _build_repo_quiet_lgbm_regressor(),
        "MLP": lambda: __import__("sklearn.neural_network", fromlist=["MLPRegressor"]).MLPRegressor(),
        "SVR": lambda: _tag_family_display_name(SVR(), "SVR"),
        "SVM": lambda: _tag_family_display_name(SVR(), "SVR"),
        "ELM": lambda: __import__("skelm", fromlist=["ELMRegressor"]).ELMRegressor(),
    }

def _build_paper_tuned_family_factory_map():

    """ Build the tuned v18 family registry from the recovered original file. """

    return {

        # Support Vector Machine / Support Vector Regressor
        "SVR": lambda: _build_paper_faithful_rbf_svr(C=1, epsilon=0.0001, gamma=1.1e-06, kernel="rbf"),

        # Artificial Neural Network
        "MLP": lambda: __import__("sklearn.neural_network", fromlist=["MLPRegressor"]).MLPRegressor(
            activation="tanh",
            early_stopping=True,
            hidden_layer_sizes=(200, 50),
            learning_rate="adaptive",
            solver="adam",
            random_state=0,
        ),

        # Random Forest
        "RF": lambda: __import__("sklearn.ensemble", fromlist=["RandomForestRegressor"]).RandomForestRegressor(
            criterion="squared_error",
            max_depth=14,
            min_samples_split=3,
            n_estimators=90,
            random_state=0,
        ),

        # Decision Tree
        "DT": lambda: __import__("sklearn.tree", fromlist=["DecisionTreeRegressor"]).DecisionTreeRegressor(
            criterion="squared_error",
            max_depth=16,
            min_samples_split=6,
            random_state=0,
        ),

        # Extra Tree
        "ET": lambda: __import__("sklearn.tree", fromlist=["ExtraTreeRegressor"]).ExtraTreeRegressor(
            criterion="squared_error",
            max_depth=15,
            min_samples_split=5,
            random_state=0,
        ),

        # Extra Random Tree
        "ERT": lambda: __import__("sklearn.ensemble", fromlist=["ExtraTreesRegressor"]).ExtraTreesRegressor(
            criterion="squared_error",
            max_depth=15,
            min_samples_split=3,
            n_estimators=60,
            random_state=0,
        ),

        # Gradient Boosted Machine
        "GBM": lambda: __import__("sklearn.ensemble", fromlist=["GradientBoostingRegressor"]).GradientBoostingRegressor(
            criterion="squared_error",
            learning_rate=0.1,
            max_depth=14,
            min_samples_split=14,
            n_estimators=36,
            random_state=0,
        ),

        # Histogram Gradient Boosted Machine
        "HGBM": lambda: __import__("sklearn.ensemble", fromlist=["HistGradientBoostingRegressor"]).HistGradientBoostingRegressor(
            random_state=0,
            learning_rate=0.21,
            max_depth=11,
            max_leaf_nodes=27,
        ),

        # Light Gradient Boosted Machine
        "LGBM": lambda: _build_repo_quiet_lgbm_regressor(
            learning_rate=0.39,
            max_depth=12,
            subsample=0.1,
            random_state=0,
        ),

        # Extreme Gradient Boosted Machine
        "XGBM": lambda: __import__("xgboost.sklearn", fromlist=["XGBRegressor"]).XGBRegressor(
            reg_lambda=20,
            alpha=0.01,
            max_depth=16,
            colsample_bytree=0.8,
            random_state=0,
        ),

        # Extreme Learning Machine
        "ELM": lambda: __import__("skelm", fromlist=["ELMRegressor"]).ELMRegressor(n_neurons=250, random_state=0),
    }

def _resolve_family_code_list(mode_name, families_argument):

    """ Resolve the family order for the selected mode. """

    # The Family List Can Be Customized With The CLI, But Defaults To The Original Order And Composition For Each Mode.
    if families_argument: return [family_code.strip().upper() for family_code in families_argument.split(",") if family_code.strip()]
    return list(PAPER_REFERENCE_FAMILY_CODE_LIST)

def _normalize_summary_family_code(summary_family_code):

    """ Normalize the historical summary family acronym to the runtime family code. """

    normalized_family_code = summary_family_code.strip().upper()
    if normalized_family_code == "SVM": return "SVR"
    return normalized_family_code

def _sanitize_best_parameter_payload(best_parameter_payload):

    """ Parse the historical best-parameter string into one Python dictionary. """

    # The Historical Best-Parameter Payload Is Not Always Well-Formed, So We Need To Sanitize It.
    sanitized_payload = best_parameter_payload.strip()
    sanitized_payload = re.sub(r"np\.int64\(([^)]+)\)", r"\1", sanitized_payload)
    sanitized_payload = re.sub(r"np\.float64\(([^)]+)\)", r"\1", sanitized_payload)
    parsed_payload = ast.literal_eval(sanitized_payload)

    # The Payload Contains The SVR Variant Keys, We Assume It's Already Parsed.
    if (
        isinstance(parsed_payload, dict)
        and SVR_VARIANT_KEY in parsed_payload
        and SVR_VARIANT_PARAMETERS_KEY in parsed_payload
    ):
        return parsed_payload

    normalized_payload = {}

    for parameter_name, parameter_value in parsed_payload.items():

        # Normalize The Known Historical Random-Forest Typo Without Corrupting Already-Correct Keys.
        normalized_parameter_name = parameter_name
        if normalized_parameter_name == "estimator__n_estimator":
            normalized_parameter_name = "estimator__n_estimators"

        normalized_payload[normalized_parameter_name.replace("estimator__", "")] = parameter_value

    return normalized_payload

def _build_svr_model_from_serialized_payload(best_parameter_payload):

    """ Rebuild one tuned SVR-family estimator from the retune summary payload. """

    # The Payload Contains The SVR Variant Keys, We Assume It's Already Parsed.
    svr_variant = best_parameter_payload[SVR_VARIANT_KEY]
    svr_parameter_map = best_parameter_payload[SVR_VARIANT_PARAMETERS_KEY]

    # SVR Variant Paper-Faithful RBF
    if svr_variant == SVR_VARIANT_RBF:
        return _build_paper_faithful_rbf_svr(**svr_parameter_map)

    # SVR Variant Pragmatic Linear Fallback
    if svr_variant == SVR_VARIANT_LINEAR_FALLBACK:
        return _build_pragmatic_linear_svr_pipeline(**svr_parameter_map)

    raise ValueError(f"Unsupported serialized SVR variant: {svr_variant}")

def _load_best_parameter_map(best_parameter_summary_path):

    """ Load one family-to-parameter map from the retune summary CSV. """

    # Read The Historical RCIM Summaries
    summary_dataframe = pd.read_csv(best_parameter_summary_path, sep=";", decimal=",")
    best_parameter_map = {}

    # Load The Best-Parameter Map For Each Family
    for _, summary_row in summary_dataframe.iterrows():
        family_code = _normalize_summary_family_code(str(summary_row["0_method"]))
        best_parameter_map[family_code] = _sanitize_best_parameter_payload(str(summary_row["best_parameters"]))
    return best_parameter_map

def _instantiate_family_model(factory_map, family_code, best_parameter_map):

    """ Instantiate one family model, optionally overriding it with tuned parameters. """

    # Instantiate The Family Model
    family_model = factory_map[family_code]()
    if best_parameter_map is None: return family_model
    if family_code not in best_parameter_map: raise ValueError(f"Missing tuned parameter entry for family {family_code}")

    # Special Case For SVR
    if (family_code == "SVR" and isinstance(best_parameter_map[family_code], dict) and SVR_VARIANT_KEY in best_parameter_map[family_code]):
        return _build_svr_model_from_serialized_payload(best_parameter_map[family_code])

    # Apply The Tuned Parameters
    family_model.set_params(**best_parameter_map[family_code])
    return family_model

def _select_family_list(mode_name, families_argument, best_parameter_summary_path=None):

    """ Instantiate the selected family list for the chosen mode. """

    # Build Family Factory Maps And Code List
    default_factory_map = _build_family_factory_map()
    paper_factory_map = _build_paper_tuned_family_factory_map()
    family_code_list = _resolve_family_code_list(mode_name, families_argument)
    best_parameter_map = None
    if best_parameter_summary_path is not None:
        best_parameter_map = _load_best_parameter_map(best_parameter_summary_path)

    # Instantiate The Family Models
    instantiated_family_list = []
    resolved_family_code_list = []
    for family_code in family_code_list:
        if mode_name in {"paper_eval", "paper_export"} and best_parameter_map is None: factory_map = paper_factory_map
        else: factory_map = default_factory_map
        if family_code not in factory_map: raise ValueError(f"Unsupported family code for mode {mode_name}: {family_code}")
        instantiated_family_list.append(_instantiate_family_model(factory_map, family_code, best_parameter_map))
        resolved_family_code_list.append(family_code)
    return resolved_family_code_list, instantiated_family_list

def main():

    """ Run the recovered original training stage with repository-owned path handling. """

    _configure_stream_buffering()

    # Parse The CLI
    parser = _build_argument_parser()
    args = parser.parse_args()

    # Ensure Utilities Are On The Path
    ensure_utilities_on_path()

    # Import The Original MLModelMultipleOutput Class After Utilities Are On The Path
    from utilities.predictorML import MLModelMultipleOutput

    # Build The Output Root
    direction_code, direction_label = normalize_direction(args.direction)
    mode_name = _normalize_mode(args.mode)
    dataframe_path = (args.dataframe_path or (REFERENCE_ROOT / f"dataFrame_prediction_{direction_code}_v14_newFreq.csv")).resolve()
    output_root = args.output_root or build_default_output_root("training", direction_label, args.output_suffix, mode_name)
    output_root = output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    # Preserve The Original Relative Output Layout Inside The Runtime Root So Copied Original Helpers Can Run Unchanged.
    (output_root / "output_prediction").mkdir(exist_ok=True)
    (output_root / "model_output_dir").mkdir(exist_ok=True)

    # Copy The Dataframe To The Runtime Root
    runtime_dataframe_name, runtime_dataframe_path = copy_dataframe_to_runtime(dataframe_path, output_root, direction_code)
    output_folder_name = build_prediction_output_folder_name(mode_name, direction_code)
    (output_root / output_folder_name).mkdir(parents=True, exist_ok=True)
    selected_family_code_list, model_list = _select_family_list(mode_name, args.families, args.best_parameter_summary_path)

    with pushd(output_root):

        # Call The Copied Original Training Logic
        print(f"[INFO] Training Output Root | {output_root}", flush=True)
        print(f"[INFO] Runtime Dataframe Path | {runtime_dataframe_path}", flush=True)
        print(f"[INFO] Mode | {mode_name}", flush=True)
        print(f"[INFO] Direction | {direction_label}", flush=True)
        print(f"[INFO] Families | {','.join(selected_family_code_list)}", flush=True)
        print(f"[INFO] Retune GridSearch Verbose | {args.retune_grid_search_verbose}", flush=True)
        print(f"[INFO] Retune CrossValidate Verbose | {args.retune_cross_validate_verbose}", flush=True)
        if args.best_parameter_summary_path is not None:
            print(f"[INFO] Best-Parameter Summary | {args.best_parameter_summary_path.resolve()}", flush=True)

        df_input = pd.read_csv(runtime_dataframe_name, sep=";", decimal=",", index_col=[0])
        df_input.reset_index(inplace=True)
        cols_to_predict = [column_name for column_name in df_input.columns if "ampl" in column_name or "phase" in column_name]

        # Initialize The Output List
        generated_prediction_path_list = []

        total_family_count = len(model_list)

        for family_index, (family_code, model) in enumerate(zip(selected_family_code_list, model_list), start=1):

            print(
                f"[PROGRESS] Family {family_index}/{total_family_count} | {family_code} | "
                f"Mode {mode_name} | Start",
                flush=True,
            )

            # Initialize The Output Dataframe
            df_output_total = pd.DataFrame()

            # Train The Models
            if mode_name == "export":

                # Mirror the shipped v17 export-oriented path on the runtime dataframe copy.
                ml_model = MLModelMultipleOutput(model, "", "tot")
                df_output = ml_model.predictorML_allForExport(df_input, args.test_size)
                ml_model.exportModel(ml_model.name + "_MultiOutput_" + "tot", cols_to_predict)

            elif mode_name == "retune":

                # Mirror the author-guided retuning path that starts from the v17 structure and re-enables hyperparameter search.
                ml_model = MLModelMultipleOutput(
                    model,
                    "crossValidationWithHyperparameter_3.8_allFreq",
                    "tot",
                    retune_grid_search_verbose=args.retune_grid_search_verbose,
                    retune_cross_validate_verbose=args.retune_cross_validate_verbose,
                )
                df_output = ml_model.predictorMLCrossValidationWithHyperparameter(df_input, args.test_size)

            elif mode_name == "paper_export":

                # Train the full-dataset export bank with the tuned paper-reference family parameters.
                ml_model = MLModelMultipleOutput(model, "paperReferenceExport_3.8_allFreq", "tot")
                df_output = ml_model.predictorML_allForExport(df_input, args.test_size)
                ml_model.exportModel(ml_model.name + "_MultiOutput_" + "tot", cols_to_predict)

            else:

                # Mirror the paper-style v18 held-out evaluation path with the recovered tuned hyperparameters.
                ml_model = MLModelMultipleOutput(model, "multipleOutputEvaluationOnTrain_3.8_allFreq", "tot")
                df_output = ml_model.predictorMLEvalutationOnTrain(df_input, args.test_size)

            # Update The Output Dataframe
            if df_output_total.empty: df_output_total = df_output
            else: df_output_total = df_output_total.merge(df_output, on=["rpm", "deg", "tor"])

            # Save The Output
            prediction_output_path = output_root / output_folder_name / f"dfOutTot_prediction_{ml_model.name}.csv"
            df_output_total.to_csv(prediction_output_path, sep=";", decimal=",")
            generated_prediction_path_list.append(str(prediction_output_path))

            print(
                f"[PROGRESS] Family {family_index}/{total_family_count} | {family_code} | "
                f"Mode {mode_name} | Done | {prediction_output_path.name}",
                flush=True,
            )

    # Write A Summary Of The Run For Reproducibility
    write_summary(
        output_root / "run_summary.json",
        {
            "stage": "training_models",
            "mode": mode_name,
            "direction": direction_label,
            "input_dataframe_path": str(dataframe_path),
            "runtime_dataframe_path": str(runtime_dataframe_path),
            "test_size": args.test_size,
            "selected_families": selected_family_code_list,
            "selected_family_count": len(selected_family_code_list),
            "best_parameter_summary_path": str(args.best_parameter_summary_path.resolve()) if args.best_parameter_summary_path else None,
            "prediction_output_folder": str(output_root / output_folder_name),
            "model_output_dir": str(output_root / "model_output_dir"),
            "generated_prediction_paths": generated_prediction_path_list,
        },
    )
    print(f"[DONE] Training Summary | {output_root / 'run_summary.json'}", flush=True)
    print(output_root)

if __name__ == "__main__":

    main()
