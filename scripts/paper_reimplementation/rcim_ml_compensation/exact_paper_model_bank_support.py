"""Support utilities for the exact RCIM paper model-bank reimplementation."""

from __future__ import annotations

# Import Python Utilities
import contextlib
import importlib.metadata
import os
import pickle
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import numpy as np
import pandas as pd

# Import Scikit-Learn Utilities
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor
from threadpoolctl import threadpool_limits

# Import Project Utilities
from scripts.training import shared_training_infrastructure

try:
    from lightgbm import LGBMRegressor
except ImportError:  # pragma: no cover - runtime dependency check
    LGBMRegressor = None

try:
    from onnxconverter_common.data_types import FloatTensorType as ONNX_FLOAT_TENSOR_TYPE
    from onnxmltools.convert import convert_lightgbm
    from onnxmltools.convert import convert_xgboost
except ImportError:  # pragma: no cover - runtime dependency check
    ONNX_FLOAT_TENSOR_TYPE = None
    convert_lightgbm = None
    convert_xgboost = None

try:
    from skl2onnx import convert_sklearn
    from skl2onnx.common.data_types import FloatTensorType
    from skl2onnx.common import tree_ensemble as skl2onnx_tree_ensemble
    from skl2onnx.operator_converters import random_forest as skl2onnx_random_forest_converter
except ImportError:  # pragma: no cover - runtime dependency check
    FloatTensorType = None
    convert_sklearn = None
    skl2onnx_tree_ensemble = None
    skl2onnx_random_forest_converter = None

try:
    from xgboost import XGBRegressor
except ImportError:  # pragma: no cover - runtime dependency check
    XGBRegressor = None

EXACT_MODEL_BANK_FILENAME = "paper_family_model_bank.pkl"
EXACT_MODEL_REPORT_ROOT = shared_training_infrastructure.PROJECT_PATH / "doc" / "reports" / "analysis" / "validation_checks"
EXACT_MODEL_REPORT_TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"
EXACT_FAMILY_ORDER = [
    "SVR",
    "MLP",
    "RF",
    "DT",
    "ET",
    "ERT",
    "GBM",
    "HGBM",
    "XGBM",
    "LGBM",
]
EXACT_FAMILY_DISPLAY_NAME_MAP = {
    "SVR": "Support Vector Regressor",
    "MLP": "Multi-Layer Perceptron",
    "RF": "Random Forest",
    "DT": "Decision Tree",
    "ET": "Extra Tree",
    "ERT": "Extra Trees",
    "GBM": "Gradient Boosting",
    "HGBM": "HistGradientBoosting",
    "XGBM": "XGBoost",
    "LGBM": "LightGBM",
}
EXACT_FAMILY_ESTIMATOR_NAME_MAP = {
    "SVR": "SVR",
    "MLP": "MLPRegressor",
    "RF": "RandomForestRegressor",
    "DT": "DecisionTreeRegressor",
    "ET": "ExtraTreeRegressor",
    "ERT": "ExtraTreesRegressor",
    "GBM": "GradientBoostingRegressor",
    "HGBM": "HistGradientBoostingRegressor",
    "XGBM": "XGBRegressor",
    "LGBM": "LGBMRegressor",
}


@dataclass
class ExactPaperDatasetBundle:

    """One prepared dataframe split bundle for the exact paper bank."""

    feature_name_list: list[str]
    target_name_list: list[str]
    train_feature_matrix: pd.DataFrame
    test_feature_matrix: pd.DataFrame
    train_target_matrix: pd.DataFrame
    test_target_matrix: pd.DataFrame
    full_dataframe: pd.DataFrame


def load_exact_model_bank_config(config_path: str | Path) -> dict[str, Any]:

    """Load one exact paper model-bank configuration file."""

    return shared_training_infrastructure.load_training_config(config_path)


def resolve_enabled_family_list(training_config: dict[str, Any]) -> list[str]:

    """Resolve the enabled paper family list from configuration."""

    # Read Enabled Family Names
    configured_family_list = training_config["training"]["enabled_families"]
    enabled_family_list = [str(family_name).strip().upper() for family_name in configured_family_list]

    # Validate Enabled Family Names
    unsupported_family_list = [family_name for family_name in enabled_family_list if family_name not in EXACT_FAMILY_ORDER]
    assert not unsupported_family_list, (
        "Unsupported exact paper family names requested | "
        f"{', '.join(unsupported_family_list)}"
    )
    return enabled_family_list


def resolve_paper_input_feature_name_list(training_config: dict[str, Any]) -> list[str]:

    """Resolve the ordered paper input feature names."""

    # Read Configured Input Features
    input_feature_name_list = [
        str(feature_name).strip()
        for feature_name in training_config["data"]["input_feature_names"]
    ]
    assert input_feature_name_list == ["rpm", "deg", "tor"], (
        "Exact paper input features must remain ['rpm', 'deg', 'tor']"
    )
    return input_feature_name_list


def load_exact_paper_dataframe(training_config: dict[str, Any]) -> pd.DataFrame:

    """Load the recovered paper dataframe with the configured CSV settings."""

    # Resolve Input CSV Path
    source_dataframe_path = shared_training_infrastructure.resolve_project_relative_path(
        training_config["paths"]["source_dataframe_path"]
    )
    assert source_dataframe_path.exists(), f"Recovered paper dataframe not found | {source_dataframe_path}"

    # Read The Recovered CSV
    csv_separator = str(training_config["data"].get("csv_separator", ";"))
    csv_decimal = str(training_config["data"].get("csv_decimal", ","))
    dataframe = pd.read_csv(
        source_dataframe_path,
        sep=csv_separator,
        decimal=csv_decimal,
        index_col=0,
    )
    assert isinstance(dataframe, pd.DataFrame), "Recovered paper dataframe must load as a pandas DataFrame"

    # Apply The Paper Temperature Filter
    maximum_deg = float(training_config["data"]["maximum_deg"])
    filtered_dataframe = dataframe[dataframe["deg"] <= maximum_deg].copy()
    filtered_dataframe.reset_index(drop=True, inplace=True)
    assert not filtered_dataframe.empty, "Recovered paper dataframe becomes empty after configured filtering"
    return filtered_dataframe


def resolve_target_name_list(dataframe: pd.DataFrame) -> list[str]:

    """Resolve the ordered exact paper target list from the dataframe."""

    # Collect Harmonic Targets In Dataframe Order
    target_name_list = [
        column_name
        for column_name in dataframe.columns
        if ("ampl" in column_name) or ("phase" in column_name)
    ]

    # Validate Harmonic Target Count
    assert len(target_name_list) == 20, (
        "Exact paper dataframe must expose 20 harmonic targets | "
        f"found {len(target_name_list)}"
    )
    return target_name_list


def build_exact_paper_dataset_bundle(training_config: dict[str, Any]) -> ExactPaperDatasetBundle:

    """Build the exact paper dataframe split bundle."""

    # Load The Recovered Dataframe
    dataframe = load_exact_paper_dataframe(training_config)
    feature_name_list = resolve_paper_input_feature_name_list(training_config)
    target_name_list = resolve_target_name_list(dataframe)

    # Prepare Train/Test Split
    test_size = float(training_config["training"]["test_size"])
    random_seed = int(training_config["training"]["random_seed"])
    feature_matrix = dataframe[feature_name_list].copy()
    target_matrix = dataframe[target_name_list].copy()
    train_feature_matrix, test_feature_matrix, train_target_matrix, test_target_matrix = train_test_split(
        feature_matrix,
        target_matrix,
        test_size=test_size,
        random_state=random_seed,
    )

    return ExactPaperDatasetBundle(
        feature_name_list=feature_name_list,
        target_name_list=target_name_list,
        train_feature_matrix=train_feature_matrix,
        test_feature_matrix=test_feature_matrix,
        train_target_matrix=train_target_matrix,
        test_target_matrix=test_target_matrix,
        full_dataframe=dataframe,
    )


def _assert_optional_dependency(value: object, dependency_name: str) -> None:

    """Raise a clear dependency error when one optional dependency is missing."""

    assert value is not None, (
        f"Required dependency is missing for exact paper reimplementation | {dependency_name}. "
        "Install the repository requirements before running this workflow."
    )


def create_exact_paper_base_estimator(family_name: str) -> object:

    """Create one exact paper base estimator with recovered hyperparameters."""

    # Create Recovered Family Estimators
    if family_name == "SVR":
        return SVR(C=1, epsilon=0.0001, gamma=1.1e-06, kernel="rbf")

    if family_name == "MLP":
        return MLPRegressor(
            activation="tanh",
            early_stopping=True,
            hidden_layer_sizes=(200, 50),
            learning_rate="adaptive",
            solver="adam",
            random_state=0,
        )

    if family_name == "RF":
        return RandomForestRegressor(
            criterion="squared_error",
            max_depth=14,
            min_samples_split=3,
            n_estimators=90,
            random_state=0,
        )

    if family_name == "DT":
        return DecisionTreeRegressor(
            criterion="squared_error",
            max_depth=16,
            min_samples_split=6,
            random_state=0,
        )

    if family_name == "ET":
        return ExtraTreeRegressor(
            criterion="squared_error",
            max_depth=15,
            min_samples_split=5,
            random_state=0,
        )

    if family_name == "ERT":
        return ExtraTreesRegressor(
            criterion="squared_error",
            max_depth=15,
            min_samples_split=3,
            n_estimators=60,
            random_state=0,
        )

    if family_name == "GBM":
        return GradientBoostingRegressor(
            criterion="squared_error",
            learning_rate=0.1,
            max_depth=14,
            min_samples_split=14,
            n_estimators=36,
            random_state=0,
        )

    if family_name == "HGBM":
        return HistGradientBoostingRegressor(
            random_state=0,
            learning_rate=0.21,
            max_depth=11,
            max_leaf_nodes=27,
        )

    if family_name == "XGBM":
        _assert_optional_dependency(XGBRegressor, "xgboost")
        return XGBRegressor(
            reg_lambda=20,
            reg_alpha=0.01,
            max_depth=16,
            colsample_bytree=0.8,
            random_state=0,
            objective="reg:squarederror",
        )

    if family_name == "LGBM":
        _assert_optional_dependency(LGBMRegressor, "lightgbm")
        return LGBMRegressor(
            learning_rate=0.39,
            max_depth=12,
            subsample=0.1,
            random_state=0,
            objective="regression",
            verbosity=-1,
        )

    raise ValueError(f"Unsupported exact paper family | {family_name}")


def fit_exact_family_model_bank(
    dataset_bundle: ExactPaperDatasetBundle,
    enabled_family_list: list[str],
    training_config: dict[str, Any] | None = None,
) -> dict[str, MultiOutputRegressor]:

    """Fit the recovered family bank using MultiOutputRegressor wrappers."""

    # Fit Each Family Bank
    fitted_family_model_dictionary: dict[str, MultiOutputRegressor] = {}
    threadpool_limit = int((training_config or {}).get("training", {}).get("threadpool_limit", 1))
    os.environ.setdefault("LOKY_MAX_CPU_COUNT", str(threadpool_limit))
    for family_name in enabled_family_list:
        base_estimator = create_exact_paper_base_estimator(family_name)
        wrapped_estimator = MultiOutputRegressor(base_estimator)
        train_feature_matrix: pd.DataFrame | np.ndarray = dataset_bundle.train_feature_matrix
        if family_name == "XGBM":
            train_feature_matrix = dataset_bundle.train_feature_matrix.to_numpy(dtype=np.float32)
        with threadpool_limits(limits=threadpool_limit):
            wrapped_estimator.fit(
                train_feature_matrix,
                dataset_bundle.train_target_matrix,
            )
        fitted_family_model_dictionary[family_name] = wrapped_estimator

    return fitted_family_model_dictionary


def _safe_mape(truth_vector: np.ndarray, prediction_vector: np.ndarray) -> float:

    """Compute one guarded mean absolute percentage error."""

    # Avoid Instability Around Exact Zeros
    denominator_vector = np.where(np.abs(truth_vector) < 1e-12, 1e-12, truth_vector)
    return float(np.mean(np.abs((truth_vector - prediction_vector) / denominator_vector)) * 100.0)


def evaluate_exact_family_model_bank(
    dataset_bundle: ExactPaperDatasetBundle,
    fitted_family_model_dictionary: dict[str, MultiOutputRegressor],
) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:

    """Evaluate the recovered family bank on the held-out test split."""

    # Evaluate Each Family On The Held-Out Split
    family_summary_list: list[dict[str, Any]] = []
    per_target_ranking_dictionary: dict[str, list[dict[str, Any]]] = {
        target_name: []
        for target_name in dataset_bundle.target_name_list
    }

    for family_name in EXACT_FAMILY_ORDER:
        if family_name not in fitted_family_model_dictionary:
            continue

        wrapped_estimator = fitted_family_model_dictionary[family_name]
        test_feature_matrix: pd.DataFrame | np.ndarray = dataset_bundle.test_feature_matrix
        if family_name == "XGBM":
            test_feature_matrix = dataset_bundle.test_feature_matrix.to_numpy(dtype=np.float32)
        prediction_matrix = wrapped_estimator.predict(test_feature_matrix)
        truth_matrix = dataset_bundle.test_target_matrix.to_numpy(dtype=np.float64)
        prediction_matrix = np.asarray(prediction_matrix, dtype=np.float64)

        # Accumulate Per-Target Metrics
        target_metric_list: list[dict[str, Any]] = []
        for target_index, target_name in enumerate(dataset_bundle.target_name_list):
            truth_vector = truth_matrix[:, target_index]
            prediction_vector = prediction_matrix[:, target_index]
            mse_value = float(mean_squared_error(truth_vector, prediction_vector))
            rmse_value = float(np.sqrt(mse_value))
            mae_value = float(mean_absolute_error(truth_vector, prediction_vector))
            mape_value = _safe_mape(truth_vector, prediction_vector)

            target_metric_dictionary = {
                "target_name": target_name,
                "family_name": family_name,
                "mse": mse_value,
                "rmse": rmse_value,
                "mae": mae_value,
                "mape_percent": mape_value,
            }
            target_metric_list.append(target_metric_dictionary)
            per_target_ranking_dictionary[target_name].append(target_metric_dictionary)

        # Build Family-Level Aggregate Summary
        family_summary_list.append(
            {
                "family_name": family_name,
                "display_name": EXACT_FAMILY_DISPLAY_NAME_MAP[family_name],
                "estimator_name": EXACT_FAMILY_ESTIMATOR_NAME_MAP[family_name],
                "component_count": len(target_metric_list),
                "mean_component_mse": float(np.mean([entry["mse"] for entry in target_metric_list])),
                "mean_component_rmse": float(np.mean([entry["rmse"] for entry in target_metric_list])),
                "mean_component_mae": float(np.mean([entry["mae"] for entry in target_metric_list])),
                "mean_component_mape_percent": float(np.mean([entry["mape_percent"] for entry in target_metric_list])),
                "target_metrics": target_metric_list,
            }
        )

    # Sort Family And Per-Target Rankings
    family_summary_list.sort(
        key=lambda entry: (
            float(entry["mean_component_mape_percent"]),
            float(entry["mean_component_mae"]),
            str(entry["family_name"]),
        )
    )
    for target_name, ranking_list in per_target_ranking_dictionary.items():
        ranking_list.sort(
            key=lambda entry: (
                float(entry["mape_percent"]),
                float(entry["mae"]),
                str(entry["family_name"]),
            )
        )

    return family_summary_list, per_target_ranking_dictionary


def save_exact_family_model_bundle(
    fitted_family_model_dictionary: dict[str, MultiOutputRegressor],
    output_directory: Path,
) -> Path:

    """Persist the fitted family model bank to one artifact bundle."""

    # Save The Complete Family Model Dictionary
    bundle_path = output_directory / EXACT_MODEL_BANK_FILENAME
    with bundle_path.open("wb") as output_file:
        pickle.dump(fitted_family_model_dictionary, output_file)
    return bundle_path


def build_exact_target_export_name(target_name: str) -> str:

    """Convert one dataframe target name into the paper export suffix."""

    # Convert `fft_y_Fw_filtered_ampl_39` -> `ampl39`
    target_tokens = target_name.split("_")
    target_kind = target_tokens[-2]
    harmonic_order = target_tokens[-1]
    return f"{target_kind}{harmonic_order}"


def _convert_estimator_to_onnx(
    estimator: object,
    feature_count: int,
    estimator_name: str,
    target_opset: int,
) -> Any:

    """Convert one fitted estimator into an ONNX model."""

    # Build The Shared Input Signature
    initial_types = [("float_input", FloatTensorType([None, feature_count]))]

    # Convert HistGradientBoosting Through A Sanitized Temporary Converter Patch
    if estimator_name == "HistGradientBoostingRegressor":
        _assert_optional_dependency(convert_sklearn, "skl2onnx")
        with _patched_hist_gradient_boosting_onnx_converter():
            return convert_sklearn(estimator, initial_types=initial_types, target_opset=target_opset)

    # Convert Standard Scikit-Learn Estimators
    if estimator_name not in ["XGBRegressor", "LGBMRegressor"]:
        _assert_optional_dependency(convert_sklearn, "skl2onnx")
        return convert_sklearn(estimator, initial_types=initial_types, target_opset=target_opset)

    # Convert XGBoost Estimators
    if estimator_name == "XGBRegressor":
        _assert_optional_dependency(convert_xgboost, "onnxmltools")
        _assert_optional_dependency(ONNX_FLOAT_TENSOR_TYPE, "onnxconverter-common")
        xgb_initial_types = [("float_input", ONNX_FLOAT_TENSOR_TYPE([None, feature_count]))]
        return convert_xgboost(estimator, initial_types=xgb_initial_types, target_opset=target_opset)

    # Convert LightGBM Estimators
    _assert_optional_dependency(convert_lightgbm, "onnxmltools")
    _assert_optional_dependency(ONNX_FLOAT_TENSOR_TYPE, "onnxconverter-common")
    lgbm_initial_types = [("float_input", ONNX_FLOAT_TENSOR_TYPE([None, feature_count]))]
    return convert_lightgbm(estimator, initial_types=lgbm_initial_types, target_opset=target_opset)


@contextlib.contextmanager
def _patched_hist_gradient_boosting_onnx_converter():

    """Temporarily sanitize the local skl2onnx HGBM converter for sklearn 1.8.

    Notes:
        The currently installed `scikit-learn=1.8.0` exposes histogram-tree node
        metadata such as `left`, `right`, and `missing_go_to_left` as NumPy
        scalar types. The local `skl2onnx=1.20.0` converter forwards those raw
        values into ONNX node attributes, but ONNX helper validation expects
        plain Python `int` values for the integer attribute lists.

        This patch only affects the temporary in-process conversion of
        `HistGradientBoostingRegressor` and restores the original converter
        functions immediately afterwards.
    """

    # Validate Optional Runtime Dependencies
    _assert_optional_dependency(skl2onnx_tree_ensemble, "skl2onnx")
    _assert_optional_dependency(skl2onnx_random_forest_converter, "skl2onnx")

    # Capture Original Converter Functions
    original_hist_converter = (
        skl2onnx_tree_ensemble.add_tree_to_attribute_pairs_hist_gradient_boosting
    )
    original_random_forest_hist_converter = (
        skl2onnx_random_forest_converter.add_tree_to_attribute_pairs_hist_gradient_boosting
    )

    def _sanitized_hist_gradient_boosting_converter(
        attr_pairs: dict[str, Any],
        is_classifier: bool,
        tree: Any,
        tree_id: int,
        tree_weight: float,
        weight_id_bias: int,
        leaf_weights_are_counts: bool,
        adjust_threshold_for_sklearn: bool = False,
        dtype: Any = None,
    ) -> None:

        """Add one HGBM tree to ONNX attributes with plain Python integers."""

        # Serialize Every HGBM Node Through Stable Python Scalar Types
        for node_index, node in enumerate(tree.nodes):
            node_id = int(node_index)
            weight = node["value"]

            if bool(node["is_leaf"]):
                mode = "LEAF"
                feature_id = 0
                threshold = 0.0
                left_child_id = 0
                right_child_id = 0
                missing_tracks_true = 0
            else:
                mode = "BRANCH_LEQ"
                feature_id = int(node["feature_idx"])
                try:
                    threshold = node["threshold"]
                except ValueError:
                    threshold = node["num_threshold"]
                left_child_id = int(node["left"])
                right_child_id = int(node["right"])
                missing_tracks_true = int(node["missing_go_to_left"])

            skl2onnx_tree_ensemble.add_node(
                attr_pairs,
                is_classifier,
                tree_id,
                tree_weight,
                node_id,
                feature_id,
                mode,
                threshold,
                left_child_id,
                right_child_id,
                weight,
                weight_id_bias,
                leaf_weights_are_counts,
                adjust_threshold_for_sklearn=adjust_threshold_for_sklearn,
                dtype=dtype,
                nodes_missing_value_tracks_true=missing_tracks_true,
            )

    # Install Temporary Converter Patch
    skl2onnx_tree_ensemble.add_tree_to_attribute_pairs_hist_gradient_boosting = (
        _sanitized_hist_gradient_boosting_converter
    )
    skl2onnx_random_forest_converter.add_tree_to_attribute_pairs_hist_gradient_boosting = (
        _sanitized_hist_gradient_boosting_converter
    )

    try:
        yield
    finally:
        # Restore Original skl2onnx Converter Functions
        skl2onnx_tree_ensemble.add_tree_to_attribute_pairs_hist_gradient_boosting = (
            original_hist_converter
        )
        skl2onnx_random_forest_converter.add_tree_to_attribute_pairs_hist_gradient_boosting = (
            original_random_forest_hist_converter
        )


def _build_compact_export_error_message(export_error: Exception) -> str:

    """Build one compact export error string for YAML/report serialization."""

    # Normalize Whitespace For Stable Reporting
    compact_message = " ".join(str(export_error).split())
    if len(compact_message) > 400:
        compact_message = compact_message[:397] + "..."
    return compact_message


def _is_empty_support_vector_regressor(estimator: object) -> bool:

    """Return whether one fitted SVR has degenerated to a constant predictor."""

    # Resolve Support-Vector Attributes Conservatively
    if not isinstance(estimator, SVR):
        return False

    support_vector_array = getattr(estimator, "support_vectors_", None)
    dual_coefficient_array = getattr(estimator, "dual_coef_", None)
    if support_vector_array is None or dual_coefficient_array is None:
        return False

    return int(np.size(support_vector_array)) == 0 or int(np.size(dual_coefficient_array)) == 0


def _build_constant_linear_regression_export_surrogate(
    estimator: object,
    feature_count: int,
) -> LinearRegression:

    """Create one ONNX-convertible constant regressor surrogate.

    Args:
        estimator: Fitted source estimator whose predictions are constant.
        feature_count: Input feature count for the exported model.

    Returns:
        One fitted `LinearRegression` surrogate with zero coefficients and an
        intercept equal to the constant prediction level.
    """

    # Fit One Simple Constant Linear Model
    constant_prediction = float(np.ravel(getattr(estimator, "intercept_", [0.0]))[0])
    surrogate_feature_matrix = np.zeros((2, feature_count), dtype=np.float64)
    surrogate_target_vector = np.array([constant_prediction, constant_prediction], dtype=np.float64)
    surrogate_estimator = LinearRegression()
    surrogate_estimator.fit(surrogate_feature_matrix, surrogate_target_vector)
    return surrogate_estimator


def export_exact_family_onnx_bank(
    dataset_bundle: ExactPaperDatasetBundle,
    fitted_family_model_dictionary: dict[str, MultiOutputRegressor],
    training_config: dict[str, Any],
    output_directory: Path,
) -> dict[str, Any]:

    """Export one ONNX model per family and target when enabled.

    Args:
        dataset_bundle: Prepared paper-faithful train/test bundle.
        fitted_family_model_dictionary: Fitted family bank keyed by short family
            name.
        training_config: Effective exact-paper configuration.
        output_directory: Immutable validation artifact directory.

    Returns:
        Dictionary summarizing export status, generated files, and comparison
        against the recovered ONNX release when configured.
    """

    # Resolve Export Configuration
    export_config = training_config["export"]
    export_enabled = bool(export_config["enable_onnx_export"])
    target_opset = int(export_config["target_opset"])
    export_failure_mode = str(export_config.get("export_failure_mode", "strict")).strip().lower()
    assert export_failure_mode in ["strict", "continue"], (
        "Unsupported export_failure_mode for exact paper workflow | "
        f"{export_failure_mode}"
    )
    enable_empty_svr_constant_surrogate = bool(
        export_config.get("enable_empty_svr_constant_surrogate", True)
    )
    export_root = output_directory / "onnx_export"
    export_root.mkdir(parents=True, exist_ok=True)

    # Build Optional Recovered Reference File Index
    recovered_reference_root_value = str(training_config["paths"].get("exact_onnx_reference_root", "")).strip()
    recovered_reference_root = None
    recovered_relative_path_set: set[str] = set()
    if recovered_reference_root_value:
        recovered_reference_root = shared_training_infrastructure.resolve_project_relative_path(
            recovered_reference_root_value
        )
        if recovered_reference_root.exists():
            recovered_relative_path_set = {
                reference_path.relative_to(recovered_reference_root).as_posix()
                for reference_path in recovered_reference_root.rglob("*.onnx")
            }

    # Skip ONNX Export When Disabled
    if not export_enabled:
        return {
            "enabled": False,
            "target_opset": target_opset,
            "export_root": shared_training_infrastructure.format_project_relative_path(export_root),
            "exported_file_count": 0,
            "recovered_reference_root": shared_training_infrastructure.format_project_relative_path(recovered_reference_root),
            "recovered_reference_file_count": len(recovered_relative_path_set),
            "matched_reference_relative_paths": [],
            "missing_against_reference_relative_paths": sorted(recovered_relative_path_set),
            "extra_export_relative_paths": [],
            "family_exports": [],
        }

    # Export Each Family Target Estimator
    family_export_list: list[dict[str, Any]] = []
    exported_relative_path_set: set[str] = set()
    for family_name in EXACT_FAMILY_ORDER:
        if family_name not in fitted_family_model_dictionary:
            continue

        # Resolve Output Family Folder
        wrapped_estimator = fitted_family_model_dictionary[family_name]
        family_directory = export_root / family_name
        family_directory.mkdir(parents=True, exist_ok=True)
        estimator_name = EXACT_FAMILY_ESTIMATOR_NAME_MAP[family_name]
        exported_target_list: list[dict[str, Any]] = []

        # Export Per-Target Estimator Files
        for target_index, target_name in enumerate(dataset_bundle.target_name_list):
            per_target_estimator = wrapped_estimator.estimators_[target_index]
            export_target_name = build_exact_target_export_name(target_name)
            export_filename = f"{estimator_name}_{export_target_name}.onnx"
            export_path = family_directory / export_filename
            try:
                # Build An Export-Safe Estimator Representation
                export_estimator = per_target_estimator
                surrogate_strategy = "none"
                if (
                    family_name == "SVR"
                    and enable_empty_svr_constant_surrogate
                    and _is_empty_support_vector_regressor(per_target_estimator)
                ):
                    export_estimator = _build_constant_linear_regression_export_surrogate(
                        per_target_estimator,
                        feature_count=len(dataset_bundle.feature_name_list),
                    )
                    surrogate_strategy = "constant_linear_regression"

                # Convert And Persist One ONNX Target Artifact
                export_estimator_name = type(export_estimator).__name__
                onnx_model = _convert_estimator_to_onnx(
                    export_estimator,
                    feature_count=len(dataset_bundle.feature_name_list),
                    estimator_name=export_estimator_name,
                    target_opset=target_opset,
                )
                with export_path.open("wb") as output_file:
                    output_file.write(onnx_model.SerializeToString())

                exported_relative_path = export_path.relative_to(export_root).as_posix()
                exported_relative_path_set.add(exported_relative_path)
                exported_target_list.append(
                    {
                        "target_name": target_name,
                        "export_target_name": export_target_name,
                        "export_path": shared_training_infrastructure.format_project_relative_path(export_path),
                        "file_size_bytes": int(export_path.stat().st_size),
                        "export_status": "exported",
                        "surrogate_strategy": surrogate_strategy,
                        "export_estimator_name": export_estimator_name,
                    }
                )
            except Exception as export_error:  # pragma: no cover - exercised in real runtime
                exported_target_list.append(
                    {
                        "target_name": target_name,
                        "export_target_name": export_target_name,
                        "export_path": shared_training_infrastructure.format_project_relative_path(export_path),
                        "file_size_bytes": 0,
                        "export_status": "failed",
                        "surrogate_strategy": "none",
                        "export_estimator_name": estimator_name,
                        "error_message": _build_compact_export_error_message(export_error),
                    }
                )
                if export_failure_mode == "strict":
                    raise RuntimeError(
                        "Exact paper ONNX export failed | "
                        f"family={family_name} target={target_name}"
                    ) from export_error

        family_export_list.append(
            {
                "family_name": family_name,
                "display_name": EXACT_FAMILY_DISPLAY_NAME_MAP[family_name],
                "estimator_name": estimator_name,
                "export_directory": shared_training_infrastructure.format_project_relative_path(family_directory),
                "exported_target_count": int(
                    sum(1 for entry in exported_target_list if entry["export_status"] == "exported")
                ),
                "failed_target_count": int(
                    sum(1 for entry in exported_target_list if entry["export_status"] == "failed")
                ),
                "exported_targets": exported_target_list,
            }
        )

    # Compare Export Surface Against The Recovered ONNX Release
    matched_reference_relative_path_list = sorted(exported_relative_path_set.intersection(recovered_relative_path_set))
    missing_against_reference_relative_path_list = sorted(recovered_relative_path_set.difference(exported_relative_path_set))
    extra_export_relative_path_list = sorted(exported_relative_path_set.difference(recovered_relative_path_set))

    return {
        "enabled": True,
        "target_opset": target_opset,
        "export_failure_mode": export_failure_mode,
        "enable_empty_svr_constant_surrogate": enable_empty_svr_constant_surrogate,
        "export_root": shared_training_infrastructure.format_project_relative_path(export_root),
        "exported_file_count": len(exported_relative_path_set),
        "recovered_reference_root": shared_training_infrastructure.format_project_relative_path(recovered_reference_root),
        "recovered_reference_file_count": len(recovered_relative_path_set),
        "matched_reference_relative_paths": matched_reference_relative_path_list,
        "missing_against_reference_relative_paths": missing_against_reference_relative_path_list,
        "extra_export_relative_paths": extra_export_relative_path_list,
        "family_exports": family_export_list,
    }


def resolve_dependency_version_dictionary() -> dict[str, str]:

    """Resolve version strings for the runtime dependencies used here."""

    # Resolve Version String For Each Relevant Dependency
    dependency_name_list = [
        "numpy",
        "pandas",
        "scikit-learn",
        "skl2onnx",
        "onnxmltools",
        "xgboost",
        "lightgbm",
    ]
    dependency_version_dictionary: dict[str, str] = {}
    for dependency_name in dependency_name_list:
        try:
            dependency_version_dictionary[dependency_name] = importlib.metadata.version(dependency_name)
        except importlib.metadata.PackageNotFoundError:
            dependency_version_dictionary[dependency_name] = "not_installed"
    return dependency_version_dictionary


def build_exact_model_validation_summary(
    resolved_config_path: Path,
    output_directory: Path,
    training_config: dict[str, Any],
    dataset_bundle: ExactPaperDatasetBundle,
    family_summary_list: list[dict[str, Any]],
    per_target_ranking_dictionary: dict[str, list[dict[str, Any]]],
    onnx_export_summary: dict[str, Any],
    model_bundle_path: Path,
) -> dict[str, Any]:

    """Build the canonical validation summary for one exact-paper run."""

    # Resolve Experiment And Dataset Identity
    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    run_artifact_identity = shared_training_infrastructure.resolve_run_artifact_identity(training_config)
    winner_family_summary = family_summary_list[0]

    # Build One Inspectable Target-Winner Registry
    target_winner_list: list[dict[str, Any]] = []
    for target_name in dataset_bundle.target_name_list:
        winning_entry = per_target_ranking_dictionary[target_name][0]
        target_winner_list.append(
            {
                "target_name": target_name,
                "winning_family": winning_entry["family_name"],
                "winning_display_name": EXACT_FAMILY_DISPLAY_NAME_MAP[winning_entry["family_name"]],
                "winning_estimator_name": EXACT_FAMILY_ESTIMATOR_NAME_MAP[winning_entry["family_name"]],
                "winning_mape_percent": float(winning_entry["mape_percent"]),
                "winning_mae": float(winning_entry["mae"]),
                "winning_rmse": float(winning_entry["rmse"]),
            }
        )

    # Build Summary Dictionary
    return {
        "schema_version": 1,
        "workflow_name": "rcim_exact_paper_model_bank_validation",
        "reference_scope": "paper_faithful_exact_model_bank",
        "config_path": shared_training_infrastructure.format_project_relative_path(resolved_config_path),
        "experiment": {
            "model_family": experiment_identity.model_family,
            "model_type": experiment_identity.model_type,
            "run_name": experiment_identity.run_name,
            "output_run_name": run_artifact_identity.run_name,
            "run_instance_id": run_artifact_identity.run_instance_id,
            "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        },
        "dataset": {
            "source_dataframe_path": training_config["paths"]["source_dataframe_path"],
            "filtered_row_count": int(len(dataset_bundle.full_dataframe)),
            "feature_count": int(len(dataset_bundle.feature_name_list)),
            "target_count": int(len(dataset_bundle.target_name_list)),
            "feature_name_list": list(dataset_bundle.feature_name_list),
            "target_name_list": list(dataset_bundle.target_name_list),
            "maximum_deg": float(training_config["data"]["maximum_deg"]),
            "train_row_count": int(len(dataset_bundle.train_feature_matrix)),
            "test_row_count": int(len(dataset_bundle.test_feature_matrix)),
            "test_size": float(training_config["training"]["test_size"]),
            "random_seed": int(training_config["training"]["random_seed"]),
        },
        "paper_alignment": {
            "input_feature_schema": ["rpm", "deg", "tor"],
            "target_schema_kind": "ampl_phase_exact_paper",
            "harmonic_order_list": [0, 1, 3, 39, 40, 78, 81, 156, 162, 240],
            "enabled_family_list": resolve_enabled_family_list(training_config),
            "recovered_reference_onnx_root": training_config["paths"].get("exact_onnx_reference_root", ""),
        },
        "dependency_versions": resolve_dependency_version_dictionary(),
        "winner_summary": {
            "winning_family": winner_family_summary["family_name"],
            "winning_display_name": winner_family_summary["display_name"],
            "winning_estimator_name": winner_family_summary["estimator_name"],
            "winning_mean_component_mape_percent": float(winner_family_summary["mean_component_mape_percent"]),
            "winning_mean_component_mae": float(winner_family_summary["mean_component_mae"]),
            "winning_mean_component_rmse": float(winner_family_summary["mean_component_rmse"]),
        },
        "family_ranking": family_summary_list,
        "target_winner_registry": target_winner_list,
        "per_target_ranking": per_target_ranking_dictionary,
        "onnx_export_summary": onnx_export_summary,
        "artifacts": {
            "model_bundle_path": shared_training_infrastructure.format_project_relative_path(model_bundle_path),
            "validation_summary_path": shared_training_infrastructure.format_project_relative_path(
                output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME
            ),
        },
    }


def build_validation_report_path(training_config: dict[str, Any]) -> Path:

    """Build the Markdown report path for one exact-paper validation run."""

    # Build Timestamped Canonical Report Path
    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    output_run_name = shared_training_infrastructure.resolve_output_run_name(training_config)
    timestamp_string = datetime.now().strftime(EXACT_MODEL_REPORT_TIMESTAMP_FORMAT)
    validation_report_filename = (
        f"{timestamp_string}_{shared_training_infrastructure.sanitize_name(experiment_identity.model_family)}_"
        f"{shared_training_infrastructure.sanitize_name(output_run_name)}_exact_paper_model_bank_report.md"
    )
    validation_report_path = EXACT_MODEL_REPORT_ROOT / validation_report_filename
    validation_report_path.parent.mkdir(parents=True, exist_ok=True)
    return validation_report_path


def build_exact_model_report_markdown(validation_summary: dict[str, Any]) -> str:

    """Build the human-readable Markdown report for one exact-paper run."""

    # Resolve Summary Sections
    experiment_dictionary = validation_summary["experiment"]
    dataset_dictionary = validation_summary["dataset"]
    paper_alignment_dictionary = validation_summary["paper_alignment"]
    dependency_version_dictionary = validation_summary["dependency_versions"]
    winner_summary = validation_summary["winner_summary"]
    family_ranking = validation_summary["family_ranking"]
    target_winner_registry = validation_summary["target_winner_registry"]
    onnx_export_summary = validation_summary["onnx_export_summary"]

    # Build Family Ranking Rows
    family_row_list: list[str] = []
    for ranking_index, family_entry in enumerate(family_ranking, start=1):
        family_row_list.append(
            f"| {ranking_index} | `{family_entry['family_name']}` | "
            f"`{family_entry['estimator_name']}` | "
            f"{family_entry['mean_component_mape_percent']:.3f} | "
            f"{family_entry['mean_component_mae']:.6f} | "
            f"{family_entry['mean_component_rmse']:.6f} |"
        )

    # Build Target-Winner Rows
    target_winner_row_list: list[str] = []
    for target_winner_entry in target_winner_registry:
        target_winner_row_list.append(
            f"| `{target_winner_entry['target_name']}` | `{target_winner_entry['winning_family']}` | "
            f"`{target_winner_entry['winning_estimator_name']}` | "
            f"{target_winner_entry['winning_mape_percent']:.3f} | "
            f"{target_winner_entry['winning_mae']:.6f} | "
            f"{target_winner_entry['winning_rmse']:.6f} |"
        )

    # Build Dependency Rows
    dependency_row_list = [
        f"| `{dependency_name}` | `{dependency_version}` |"
        for dependency_name, dependency_version in dependency_version_dictionary.items()
    ]

    # Build ONNX Comparison Notes
    matched_reference_count = len(onnx_export_summary["matched_reference_relative_paths"])
    missing_reference_count = len(onnx_export_summary["missing_against_reference_relative_paths"])
    extra_export_count = len(onnx_export_summary["extra_export_relative_paths"])
    failed_export_count = int(
        sum(
            family_entry["failed_target_count"]
            for family_entry in onnx_export_summary["family_exports"]
        )
    )
    surrogate_export_count = int(
        sum(
            1
            for family_entry in onnx_export_summary["family_exports"]
            for target_entry in family_entry["exported_targets"]
            if target_entry.get("surrogate_strategy", "none") != "none"
        )
    )

    return "\n".join([
        "# Exact RCIM Paper Model-Bank Validation Report",
        "",
        "## Overview",
        "",
        "This report summarizes one repository-owned validation run of the",
        "exact paper-faithful RCIM family bank reconstructed from the recovered",
        "paper assets.",
        "",
        f"- model family: `{experiment_dictionary['model_family']}`;",
        f"- model type: `{experiment_dictionary['model_type']}`;",
        f"- run name: `{experiment_dictionary['run_name']}`;",
        f"- output run name: `{experiment_dictionary['output_run_name']}`;",
        f"- run instance id: `{experiment_dictionary['run_instance_id']}`;",
        f"- source dataframe: `{dataset_dictionary['source_dataframe_path']}`;",
        f"- enabled families: `{', '.join(paper_alignment_dictionary['enabled_family_list'])}`;",
        "",
        "## Dataset Scope",
        "",
        f"- filtered row count: `{dataset_dictionary['filtered_row_count']}`;",
        f"- feature schema: `{', '.join(dataset_dictionary['feature_name_list'])}`;",
        f"- target count: `{dataset_dictionary['target_count']}`;",
        f"- train rows: `{dataset_dictionary['train_row_count']}`;",
        f"- test rows: `{dataset_dictionary['test_row_count']}`;",
        f"- maximum `deg` filter: `{dataset_dictionary['maximum_deg']}`;",
        "",
        "## Winner Summary",
        "",
        f"- winning family: `{winner_summary['winning_family']}`;",
        f"- winning estimator: `{winner_summary['winning_estimator_name']}`;",
        f"- winning mean component MAPE: `{winner_summary['winning_mean_component_mape_percent']:.3f}%`;",
        f"- winning mean component MAE: `{winner_summary['winning_mean_component_mae']:.6f}`;",
        f"- winning mean component RMSE: `{winner_summary['winning_mean_component_rmse']:.6f}`;",
        "",
        "## Family Ranking",
        "",
        "| Rank | Family | Estimator | Mean Component MAPE [%] | Mean Component MAE | Mean Component RMSE |",
        "| ---: | --- | --- | ---: | ---: | ---: |",
        *family_row_list,
        "",
        "## Target-Winner Registry",
        "",
        "| Target | Winning Family | Estimator | MAPE [%] | MAE | RMSE |",
        "| --- | --- | --- | ---: | ---: | ---: |",
        *target_winner_row_list,
        "",
        "## ONNX Export Surface",
        "",
        f"- export enabled: `{onnx_export_summary['enabled']}`;",
        f"- export root: `{onnx_export_summary['export_root']}`;",
        f"- exported file count: `{onnx_export_summary['exported_file_count']}`;",
        f"- export failure mode: `{onnx_export_summary['export_failure_mode']}`;",
        f"- recovered reference file count: `{onnx_export_summary['recovered_reference_file_count']}`;",
        f"- matched relative paths: `{matched_reference_count}`;",
        f"- missing against recovered reference: `{missing_reference_count}`;",
        f"- extra exported relative paths: `{extra_export_count}`;",
        f"- failed exports: `{failed_export_count}`;",
        f"- surrogate exports: `{surrogate_export_count}`;",
        "",
        "## Runtime Dependencies",
        "",
        "| Dependency | Version |",
        "| --- | --- |",
        *dependency_row_list,
        "",
        "## Interpretation",
        "",
        "This validation run is the strict paper-faithful branch of `Track 1`.",
        "Its role is to reproduce the original RCIM family bank with the exact",
        "recovered input schema, target schema, and export surface before any",
        "repository-specific simplification or target-wise winner assembly.",
        "",
    ])
