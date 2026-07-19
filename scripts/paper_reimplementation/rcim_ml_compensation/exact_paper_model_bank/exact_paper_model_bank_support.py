"""Support utilities for the exact RCIM paper model-bank reimplementation."""

from __future__ import annotations

# Import Python Utilities
import contextlib
import importlib.metadata
import os
import pickle
import time
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
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import LinearSVR
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
    from skelm import ELMRegressor
    from skelm.utils import HiddenLayerType
except ImportError:  # pragma: no cover - runtime dependency check
    ELMRegressor = None
    HiddenLayerType = None

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
    from skl2onnx import update_registered_converter
    from skl2onnx.algebra.onnx_ops import OnnxConcat
    from skl2onnx.algebra.onnx_ops import OnnxGemm
    from skl2onnx.algebra.onnx_ops import OnnxIdentity
    from skl2onnx.algebra.onnx_ops import OnnxMatMul
    from skl2onnx.algebra.onnx_ops import OnnxRelu
    from skl2onnx.algebra.onnx_ops import OnnxSigmoid
    from skl2onnx.algebra.onnx_ops import OnnxTanh
    from skl2onnx.common.data_types import FloatTensorType
    from skl2onnx.common import tree_ensemble as skl2onnx_tree_ensemble
    from skl2onnx.common.data_types import guess_numpy_type
    from skl2onnx.common.shape_calculator import calculate_linear_regressor_output_shapes
    from skl2onnx.operator_converters import random_forest as skl2onnx_random_forest_converter
except ImportError:  # pragma: no cover - runtime dependency check
    FloatTensorType = None
    convert_sklearn = None
    update_registered_converter = None
    OnnxConcat = None
    OnnxGemm = None
    OnnxIdentity = None
    OnnxMatMul = None
    OnnxRelu = None
    OnnxSigmoid = None
    OnnxTanh = None
    skl2onnx_tree_ensemble = None
    skl2onnx_random_forest_converter = None
    guess_numpy_type = None
    calculate_linear_regressor_output_shapes = None

try:
    from xgboost import XGBRegressor
except ImportError:  # pragma: no cover - runtime dependency check
    XGBRegressor = None

EXACT_MODEL_BANK_FILENAME = "paper_family_model_bank.pkl"
EXACT_PAPER_BEST_PARAMETER_SUMMARY_FILENAME = "best_parameter_summary.yaml"
EXACT_PYTHON_EXPORT_ROOTNAME = "python_export"
EXACT_ONNX_EXPORT_ROOTNAME = "onnx_export"
EXACT_MODEL_REPORT_ROOT = shared_training_infrastructure.PROJECT_PATH / "doc" / "reports" / "analysis" / "validation_checks"
EXACT_MODEL_REPORT_TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"
EXACT_PAPER_BEST_PARAMETER_REGISTRY_PATH = (
    shared_training_infrastructure.PROJECT_PATH
    / "output"
    / "registries"
    / "program"
    / "track1_exact_paper_best_hyperparameters.yaml"
)
EXACT_PAPER_HISTORICAL_SCORING_NAME_LIST = [
    "neg_mean_squared_error",
    "neg_root_mean_squared_error",
    "neg_mean_absolute_error",
    "neg_mean_absolute_percentage_error",
]
EXACT_PAPER_HISTORICAL_SCORE_OUTPUT_KEY_MAP = {
    "neg_mean_squared_error": "mean_squared_error",
    "neg_root_mean_squared_error": "root_mean_squared_error",
    "neg_mean_absolute_error": "mean_absolute_error",
    "neg_mean_absolute_percentage_error": "mean_absolute_percentage_error",
}
EXACT_PAPER_HISTORICAL_CROSS_VALIDATE_FOLD_COUNT = 10
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
    "ELM",
]
EXACT_PAPER_REFERENCE_FAMILY_ORDER = [
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
    "ELM": "Extreme Learning Machine",
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
    "ELM": "ELMRegressor",
}
EXACT_SVR_VARIANT_KEY = "__rcim_svr_variant__"
EXACT_SVR_VARIANT_PARAMETERS_KEY = "__rcim_svr_parameters__"
EXACT_SVR_VARIANT_RBF = "paper_faithful_rbf"
EXACT_SVR_VARIANT_LINEAR_FALLBACK = "pragmatic_linear_fallback"
EXACT_PAPER_HARMONIC_EXPECTED_FAMILY_MAP = {
    0: ["SVR"],
    1: ["RF", "LGBM"],
    3: ["HGBM"],
    39: ["HGBM"],
    40: ["ERT", "GBM"],
    78: ["HGBM", "RF"],
    81: ["RF"],
    156: ["ERT", "RF"],
    162: ["ERT"],
    240: ["ERT"],
}
EXACT_PAPER_FAMILY_NAME_ALIAS_MAP = {
    "SVM": "SVR",
    "SVR": "SVR",
    "MLP": "MLP",
    "RF": "RF",
    "DT": "DT",
    "ET": "ET",
    "ERT": "ERT",
    "GBM": "GBM",
    "HGBM": "HGBM",
    "XGBM": "XGBM",
    "LGBM": "LGBM",
    "ELM": "ELM",
}
ELM_ONNX_CONVERTER_REGISTERED = False
EXACT_PAPER_TABLE3_HARMONIC_ORDER_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
EXACT_PAPER_TABLE45_HARMONIC_ORDER_LIST = [1, 3, 39, 40, 78, 81, 156, 162, 240]
EXACT_PAPER_TABLE3_RMSE_AMPLITUDE_MAP = {
    "SVM": {0: 3.3e-3, 1: 7.4e-5, 3: 1.8e-4, 39: 1.8e-4, 40: 9.5e-5, 78: 3.3e-4, 81: 1.0e-4, 156: 8.8e-4, 162: 2.2e-3, 240: 4.7e-4},
    "MLP": {0: 1.4e-2, 1: 1.2e-2, 3: 1.2e-2, 39: 1.0e-2, 40: 1.4e-2, 78: 1.3e-2, 81: 1.5e-2, 156: 1.3e-2, 162: 1.6e-2, 240: 1.0e-2},
    "RF": {0: 4.1e-3, 1: 3.5e-5, 3: 3.0e-5, 39: 3.8e-5, 40: 3.7e-5, 78: 5.6e-5, 81: 1.5e-5, 156: 1.7e-4, 162: 2.2e-4, 240: 5.4e-5},
    "DT": {0: 4.9e-3, 1: 4.0e-5, 3: 3.3e-5, 39: 5.3e-5, 40: 4.5e-5, 78: 8.2e-5, 81: 1.8e-5, 156: 2.0e-4, 162: 1.7e-4, 240: 1.1e-4},
    "ET": {0: 4.5e-3, 1: 4.2e-5, 3: 3.5e-5, 39: 5.1e-5, 40: 4.3e-5, 78: 8.5e-5, 81: 2.7e-5, 156: 1.9e-4, 162: 3.8e-4, 240: 1.8e-4},
    "ERT": {0: 4.0e-3, 1: 3.7e-5, 3: 3.4e-5, 39: 4.0e-5, 40: 3.6e-5, 78: 5.7e-5, 81: 1.6e-5, 156: 1.3e-4, 162: 1.6e-4, 240: 4.2e-5},
    "GBM": {0: 4.0e-3, 1: 3.6e-5, 3: 3.1e-5, 39: 3.9e-5, 40: 3.9e-5, 78: 5.5e-5, 81: 1.6e-5, 156: 1.7e-4, 162: 2.2e-4, 240: 4.7e-5},
    "HGBM": {0: 3.4e-3, 1: 3.6e-5, 3: 2.5e-5, 39: 3.2e-5, 40: 3.8e-5, 78: 4.5e-5, 81: 1.6e-5, 156: 2.5e-4, 162: 5.0e-4, 240: 7.4e-5},
    "XGBM": {0: 3.5e-3, 1: 7.1e-5, 3: 1.0e-4, 39: 1.3e-4, 40: 8.7e-5, 78: 1.5e-4, 81: 6.0e-5, 156: 5.4e-4, 162: 7.5e-4, 240: 2.1e-4},
    "LGBM": {0: 3.5e-3, 1: 3.7e-5, 3: 2.6e-5, 39: 3.3e-5, 40: 3.8e-5, 78: 4.6e-5, 81: 1.6e-5, 156: 2.2e-4, 162: 4.7e-4, 240: 6.2e-5},
}
EXACT_PAPER_TABLE4_MAE_PHASE_MAP = {
    "SVM": {1: 2.2e-3, 3: 3.3e-2, 39: 2.7e-2, 40: 6.1e-2, 78: 1.9e-1, 81: 1.3e-1, 156: 1.2, 162: 4.9e-1, 240: 4.9e-1},
    "MLP": {1: 7.2e-3, 3: 6.5e-2, 39: 6.2e-2, 40: 8.0e-2, 78: 1.6e-1, 81: 1.5e-1, 156: 1.9, 162: 7.8e-1, 240: 7.0e-1},
    "RF": {1: 2.0e-3, 3: 2.4e-2, 39: 2.8e-2, 40: 3.7e-2, 78: 7.4e-2, 81: 5.3e-2, 156: 5.1e-1, 162: 2.3e-1, 240: 2.5e-1},
    "DT": {1: 2.1e-3, 3: 3.0e-2, 39: 3.6e-2, 40: 4.3e-2, 78: 9.0e-2, 81: 6.6e-2, 156: 5.2e-1, 162: 2.0e-1, 240: 2.3e-1},
    "ET": {1: 2.4e-3, 3: 3.1e-2, 39: 3.5e-2, 40: 5.1e-2, 78: 9.4e-2, 81: 8.7e-2, 156: 7.1e-1, 162: 2.8e-1, 240: 2.6e-1},
    "ERT": {1: 2.2e-3, 3: 2.7e-2, 39: 2.8e-2, 40: 4.0e-2, 78: 7.6e-2, 81: 5.6e-2, 156: 5.3e-1, 162: 2.0e-1, 240: 2.3e-1},
    "GBM": {1: 2.0e-3, 3: 2.4e-2, 39: 3.0e-2, 40: 3.6e-2, 78: 7.4e-2, 81: 5.3e-2, 156: 5.4e-1, 162: 2.5e-1, 240: 2.9e-1},
    "HGBM": {1: 1.9e-3, 3: 2.0e-2, 39: 2.1e-2, 40: 4.0e-2, 78: 9.1e-2, 81: 5.7e-2, 156: 7.4e-1, 162: 3.5e-1, 240: 3.6e-1},
    "XGBM": {1: 1.9e-3, 3: 2.4e-2, 39: 3.2e-2, 40: 6.1e-2, 78: 1.4e-1, 81: 9.1e-2, 156: 9.6e-1, 162: 5.4e-1, 240: 3.9e-1},
    "LGBM": {1: 1.8e-3, 3: 2.1e-2, 39: 2.1e-2, 40: 4.0e-2, 78: 9.5e-2, 81: 5.5e-2, 156: 7.4e-1, 162: 3.5e-1, 240: 3.4e-1},
}
EXACT_PAPER_TABLE5_RMSE_PHASE_MAP = {
    "SVM": {1: 3.1e-3, 3: 4.2e-2, 39: 4.4e-2, 40: 9.7e-2, 78: 3.2e-1, 81: 2.0e-1, 156: 1.8, 162: 1.1, 240: 1.1},
    "MLP": {1: 1.3e-2, 3: 8.4e-2, 39: 7.7e-2, 40: 1.1e-1, 78: 2.4e-1, 81: 2.2e-1, 156: 2.2, 162: 1.2, 240: 1.1},
    "RF": {1: 2.8e-3, 3: 3.3e-2, 39: 4.3e-2, 40: 5.5e-2, 78: 1.6e-1, 81: 8.2e-2, 156: 1.2, 162: 6.8e-1, 240: 6.3e-1},
    "DT": {1: 2.8e-3, 3: 4.2e-2, 39: 6.1e-2, 40: 6.1e-2, 78: 2.0e-1, 81: 1.0e-1, 156: 1.3, 162: 7.3e-1, 240: 6.7e-1},
    "ET": {1: 3.3e-3, 3: 4.6e-2, 39: 6.2e-2, 40: 7.4e-2, 78: 2.3e-1, 81: 1.5e-1, 156: 1.5, 162: 9.3e-1, 240: 6.8e-1},
    "ERT": {1: 3.6e-3, 3: 4.0e-2, 39: 4.4e-2, 40: 6.0e-2, 78: 1.8e-1, 81: 1.1e-1, 156: 1.2, 162: 6.4e-1, 240: 5.8e-1},
    "GBM": {1: 2.6e-3, 3: 3.4e-2, 39: 4.5e-2, 40: 5.5e-2, 78: 1.8e-1, 81: 8.4e-2, 156: 1.3, 162: 7.1e-1, 240: 7.1e-1},
    "HGBM": {1: 2.5e-3, 3: 2.9e-2, 39: 2.7e-2, 40: 6.0e-2, 78: 1.9e-1, 81: 8.5e-2, 156: 1.3, 162: 7.0e-1, 240: 7.4e-1},
    "XGBM": {1: 2.8e-3, 3: 3.3e-2, 39: 4.3e-2, 40: 8.9e-2, 78: 2.3e-1, 81: 1.3e-1, 156: 1.4, 162: 8.1e-1, 240: 7.6e-1},
    "LGBM": {1: 2.5e-3, 3: 3.0e-2, 39: 2.8e-2, 40: 6.0e-2, 78: 1.9e-1, 81: 8.2e-2, 156: 1.3, 162: 7.0e-1, 240: 7.1e-1},
}
EXACT_PAPER_TABLE6_SELECTED_MODEL_MAP = {
    0: {"ampl": "SVM", "phase": None},
    1: {"ampl": "RF", "phase": "LGBM"},
    3: {"ampl": "HGBM", "phase": "HGBM"},
    39: {"ampl": "HGBM", "phase": "HGBM"},
    40: {"ampl": "ERT", "phase": "GBM"},
    78: {"ampl": "HGBM", "phase": "RF"},
    81: {"ampl": "RF", "phase": "RF"},
    156: {"ampl": "ERT", "phase": "RF"},
    162: {"ampl": "ERT", "phase": "ERT"},
    240: {"ampl": "ERT", "phase": "ERT"},
}
EXACT_PAPER_HYPERPARAMETER_SEARCH_MODE_LIST = [
    "disabled",
    "paper_reference_grid_search",
]
EXACT_PAPER_WORKFLOW_STAGE_LIST = [
    "search",
    "eval",
    "export",
    "loadbest",
]


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


def emit_exact_paper_progress_log(level: str, message: str) -> None:

    """Emit one flushed exact-paper progress line for live campaign logs."""

    print(f"[{level}] {message}", flush=True)


def format_exact_elapsed_seconds(elapsed_seconds: float) -> str:

    """Format one elapsed duration for compact progress logs."""

    return f"{float(elapsed_seconds):.2f}s"


def build_exact_target_name_preview(target_name_list: list[str]) -> str:

    """Build one compact target-name preview string for progress logs."""

    if not target_name_list:
        return "<empty>"
    if len(target_name_list) <= 6:
        return ", ".join(target_name_list)
    return ", ".join(target_name_list[:3] + ["..."] + target_name_list[-2:])


def build_exact_target_scope_log_summary(target_name_list: list[str]) -> str:

    """Build one compact target-scope summary for runner logs."""

    target_kind_list = sorted({
        parse_exact_target_name(target_name)[0]
        for target_name in target_name_list
    })
    harmonic_order_list = sorted({
        parse_exact_target_name(target_name)[1]
        for target_name in target_name_list
    })
    harmonic_text = ",".join(str(harmonic_order) for harmonic_order in harmonic_order_list)
    kind_text = ",".join(target_kind_list)
    preview_text = build_exact_target_name_preview(target_name_list)
    return (
        f"kinds={kind_text} "
        f"harmonics={harmonic_text} "
        f"preview={preview_text}"
    )


def count_exact_parameter_grid_candidates(
    parameter_grid: dict[str, list[Any]] | list[dict[str, list[Any]]],
) -> int:

    """Count one full Cartesian parameter-grid candidate surface."""

    if isinstance(parameter_grid, list):
        return int(sum(count_exact_parameter_grid_candidates(grid_entry) for grid_entry in parameter_grid))

    candidate_count = 1
    for parameter_value_list in parameter_grid.values():
        candidate_count *= int(len(parameter_value_list))
    return int(candidate_count)


def count_exact_parameter_grid_dimensions(
    parameter_grid: dict[str, list[Any]] | list[dict[str, list[Any]]],
) -> int:

    """Count one readable parameter-dimension summary for progress logs."""

    if isinstance(parameter_grid, list):
        return int(sum(len(grid_entry) for grid_entry in parameter_grid))
    return int(len(parameter_grid))


def build_exact_paper_faithful_rbf_svr() -> SVR:

    """Build the paper-faithful exact-paper SVR RBF estimator."""

    return SVR(C=1, epsilon=0.0001, gamma=1.1e-06, kernel="rbf")


def build_exact_pragmatic_linear_svr_pipeline(
    C: float = 1.0,
    epsilon: float = 0.0001,
    tol: float = 1e-4,
    max_iter: int = 5000,
) -> Pipeline:

    """Build the exact-paper pragmatic linear fallback for the SVR family."""

    return Pipeline(
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


def build_repo_quiet_lgbm_regressor(**parameter_payload: Any) -> LGBMRegressor:

    """Build one repo-owned quiet `LGBMRegressor` for exact-paper training."""

    _assert_optional_dependency(LGBMRegressor, "lightgbm")
    base_parameter_payload = {
        "verbosity": -1,
        "force_col_wise": True,
    }
    base_parameter_payload.update(parameter_payload)
    return LGBMRegressor(**base_parameter_payload)


def is_exact_svr_variant_payload(best_parameter_dictionary: dict[str, Any]) -> bool:

    """Return whether one exact-paper best-parameter dictionary encodes an SVR variant."""

    return (
        isinstance(best_parameter_dictionary, dict)
        and EXACT_SVR_VARIANT_KEY in best_parameter_dictionary
        and EXACT_SVR_VARIANT_PARAMETERS_KEY in best_parameter_dictionary
    )


def build_exact_svr_estimator_from_serialized_payload(
    best_parameter_dictionary: dict[str, Any],
) -> object:

    """Rebuild one exact-paper SVR-family estimator from serialized variant metadata."""

    svr_variant = str(best_parameter_dictionary[EXACT_SVR_VARIANT_KEY]).strip()
    svr_parameter_dictionary = dict(best_parameter_dictionary[EXACT_SVR_VARIANT_PARAMETERS_KEY])

    if svr_variant == EXACT_SVR_VARIANT_RBF:
        return build_exact_paper_faithful_rbf_svr().set_params(**svr_parameter_dictionary)

    if svr_variant == EXACT_SVR_VARIANT_LINEAR_FALLBACK:
        return build_exact_pragmatic_linear_svr_pipeline(**svr_parameter_dictionary)

    raise ValueError(f"Unsupported exact-paper SVR variant payload | {svr_variant}")


def serialize_exact_best_parameter_payload(
    family_name: str,
    best_parameter_dictionary: dict[str, Any],
) -> dict[str, Any]:

    """Serialize one exact-paper best-parameter payload into a YAML-safe shape."""

    if family_name != "SVR":
        return dict(best_parameter_dictionary)

    selected_estimator = best_parameter_dictionary.get("estimator")
    if isinstance(selected_estimator, Pipeline):
        return {
            EXACT_SVR_VARIANT_KEY: EXACT_SVR_VARIANT_LINEAR_FALLBACK,
            EXACT_SVR_VARIANT_PARAMETERS_KEY: {
                "C": float(best_parameter_dictionary["estimator__model__C"]),
                "epsilon": float(best_parameter_dictionary["estimator__model__epsilon"]),
                "tol": float(best_parameter_dictionary["estimator__model__tol"]),
                "max_iter": int(best_parameter_dictionary["estimator__model__max_iter"]),
            },
        }

    return {
        EXACT_SVR_VARIANT_KEY: EXACT_SVR_VARIANT_RBF,
        EXACT_SVR_VARIANT_PARAMETERS_KEY: {
            "C": float(best_parameter_dictionary["estimator__C"]),
            "epsilon": float(best_parameter_dictionary["estimator__epsilon"]),
            "gamma": float(best_parameter_dictionary["estimator__gamma"]),
            "kernel": "rbf",
        },
    }


def serialize_exact_search_summary_payload(search_summary_payload: Any) -> Any:

    """Convert exact-paper search-summary metadata into a YAML-safe payload."""

    if search_summary_payload is None or isinstance(search_summary_payload, (str, int, float, bool)):
        return search_summary_payload

    if isinstance(search_summary_payload, np.generic):
        return search_summary_payload.item()

    if isinstance(search_summary_payload, np.ndarray):
        return [
            serialize_exact_search_summary_payload(search_summary_entry)
            for search_summary_entry in search_summary_payload.tolist()
        ]

    if isinstance(search_summary_payload, Path):
        return str(search_summary_payload)

    if isinstance(search_summary_payload, tuple):
        return [
            serialize_exact_search_summary_payload(search_summary_entry)
            for search_summary_entry in search_summary_payload
        ]

    if isinstance(search_summary_payload, list):
        return [
            serialize_exact_search_summary_payload(search_summary_entry)
            for search_summary_entry in search_summary_payload
        ]

    if isinstance(search_summary_payload, dict):
        return {
            str(search_summary_key): serialize_exact_search_summary_payload(search_summary_value)
            for search_summary_key, search_summary_value in search_summary_payload.items()
        }

    if callable(getattr(search_summary_payload, "get_params", None)):
        return {
            "estimator_class": search_summary_payload.__class__.__name__,
            "estimator_repr": repr(search_summary_payload),
        }

    return repr(search_summary_payload)


def resolve_exact_export_feature_count(
    estimator: object,
    fallback_feature_count: int | None = None,
) -> int:

    """Resolve one fitted estimator feature-count for exact-paper ONNX export."""

    if hasattr(estimator, "n_features_in_"):
        return int(getattr(estimator, "n_features_in_"))

    if hasattr(estimator, "n_features_"):
        return int(getattr(estimator, "n_features_"))

    assert fallback_feature_count is not None, (
        f"{type(estimator).__name__} does not expose one fitted feature-count attribute "
        "and no fallback feature count was provided."
    )
    return int(fallback_feature_count)


def build_exact_elm_hidden_layer_node(
    input_node: Any,
    hidden_layer: Any,
    dtype: Any,
    op_version: int,
) -> Any:

    """Build one ONNX hidden-layer node for the supported fitted ELM surface."""

    if HiddenLayerType is not None and hidden_layer.hidden_layer_ == HiddenLayerType.PAIRWISE:
        raise NotImplementedError(
            "Pairwise ELM hidden layers are not supported by the repo-owned exact-paper ONNX converter."
        )

    projection_components = hidden_layer.projection_.components_
    if hasattr(projection_components, "toarray"):
        projection_components = projection_components.toarray()
    projection_components = np.asarray(projection_components, dtype=dtype)

    projected_node = OnnxMatMul(
        input_node,
        projection_components.T,
        op_version=op_version,
    )

    hidden_ufunc = getattr(hidden_layer, "ufunc", None)
    if hidden_ufunc == "tanh":
        return OnnxTanh(projected_node, op_version=op_version)
    if hidden_ufunc == "sigm":
        return OnnxSigmoid(projected_node, op_version=op_version)
    if hidden_ufunc == "relu":
        return OnnxRelu(projected_node, op_version=op_version)
    if hidden_ufunc in ("lin", None):
        return OnnxIdentity(projected_node, op_version=op_version)

    raise NotImplementedError(f"Unsupported ELM activation for exact-paper ONNX export | {hidden_ufunc}")


def convert_exact_elm_regressor_to_onnx(
    scope: Any,
    operator: Any,
    container: Any,
) -> None:

    """Convert one fitted `ELMRegressor` into the repo-owned exact-paper ONNX graph."""

    fitted_estimator = operator.raw_operator
    input_node = operator.inputs[0]
    op_version = container.target_opset
    dtype = guess_numpy_type(input_node.type)

    hidden_layer_node_list = [
        build_exact_elm_hidden_layer_node(input_node, hidden_layer, dtype, op_version)
        for hidden_layer in fitted_estimator.hidden_layers_
    ]

    if fitted_estimator.include_original_features:
        hidden_layer_node_list = [input_node] + hidden_layer_node_list

    if len(hidden_layer_node_list) == 1:
        hidden_representation_node = hidden_layer_node_list[0]
    else:
        hidden_representation_node = OnnxConcat(*hidden_layer_node_list, axis=1, op_version=op_version)

    coefficient_matrix = np.asarray(fitted_estimator.solver_.coef_, dtype=dtype)
    if coefficient_matrix.ndim == 1:
        coefficient_matrix = coefficient_matrix.reshape((-1, 1))
    intercept_vector = np.asarray(fitted_estimator.solver_.intercept_, dtype=dtype)

    output_node = OnnxGemm(
        hidden_representation_node,
        coefficient_matrix,
        intercept_vector,
        alpha=1.0,
        beta=1.0,
        transB=0,
        op_version=op_version,
        output_names=operator.outputs[:1],
    )
    output_node.add_to(scope, container)


def register_exact_elm_onnx_converter_if_needed() -> None:

    """Register the repo-owned exact-paper `ELMRegressor` ONNX converter once."""

    global ELM_ONNX_CONVERTER_REGISTERED

    if ELMRegressor is None or ELM_ONNX_CONVERTER_REGISTERED:
        return

    _assert_optional_dependency(update_registered_converter, "skl2onnx")
    _assert_optional_dependency(calculate_linear_regressor_output_shapes, "skl2onnx")
    update_registered_converter(
        ELMRegressor,
        "RCIMELMRegressor",
        calculate_linear_regressor_output_shapes,
        convert_exact_elm_regressor_to_onnx,
    )
    ELM_ONNX_CONVERTER_REGISTERED = True


def resolve_exact_paper_workflow_stage(stage_name: str | None) -> str:

    """Normalize one exact-paper operator stage."""

    normalized_stage_name = str(stage_name or "search").strip().lower()
    assert normalized_stage_name in EXACT_PAPER_WORKFLOW_STAGE_LIST, (
        "Unsupported exact-paper workflow stage | "
        f"{normalized_stage_name}"
    )
    return normalized_stage_name


def _build_historical_cross_validate_metric_dictionary(
    score_dictionary: dict[str, np.ndarray],
) -> dict[str, float]:

    """Convert one sklearn `cross_validate` score dictionary into stable means."""

    # Recover Mean Metrics Using The Historical Absolute-Value Convention
    metric_dictionary: dict[str, float] = {}
    for scoring_name in EXACT_PAPER_HISTORICAL_SCORING_NAME_LIST:
        score_key = f"test_{scoring_name}"
        metric_name = EXACT_PAPER_HISTORICAL_SCORE_OUTPUT_KEY_MAP[scoring_name]
        metric_dictionary[metric_name] = float(abs(np.asarray(score_dictionary[score_key], dtype=np.float64).mean()))
    return metric_dictionary


def _build_historical_search_protocol_summary(
    family_name: str,
    dataset_bundle: "ExactPaperDatasetBundle",
    fitted_grid_search_estimator: GridSearchCV,
    threadpool_limit: int,
    cross_validate_verbose: int,
) -> dict[str, Any]:

    """Replay the recovered historical search-plus-cross-validation protocol."""

    # Resolve The Full Historical Validation Surface
    full_feature_matrix: pd.DataFrame | np.ndarray = dataset_bundle.full_dataframe[
        dataset_bundle.feature_name_list
    ].copy()
    full_target_matrix = dataset_bundle.full_dataframe[dataset_bundle.target_name_list].copy()
    if family_name == "XGBM":
        full_feature_matrix = full_feature_matrix.to_numpy(dtype=np.float32)

    emit_exact_paper_progress_log(
        "INFO",
        "Historical search protocol plan | "
        f"family={family_name} "
        f"wrapper_cv_folds={EXACT_PAPER_HISTORICAL_CROSS_VALIDATE_FOLD_COUNT} "
        f"target_count={len(dataset_bundle.target_name_list)} "
        f"target_cv_folds_total={EXACT_PAPER_HISTORICAL_CROSS_VALIDATE_FOLD_COUNT * len(dataset_bundle.target_name_list)}",
    )

    # Re-Run The Historical Global Cross-Validation On The Search Wrapper
    wrapper_cross_validate_start_time = time.perf_counter()
    emit_exact_paper_progress_log(
        "INFO",
        "Historical wrapper cross-validate started | "
        f"family={family_name} "
        f"cv={EXACT_PAPER_HISTORICAL_CROSS_VALIDATE_FOLD_COUNT} "
        f"targets={len(dataset_bundle.target_name_list)} "
        f"verbose={cross_validate_verbose}",
    )
    with threadpool_limits(limits=threadpool_limit):
        global_score_dictionary = cross_validate(
            fitted_grid_search_estimator,
            full_feature_matrix,
            full_target_matrix,
            cv=EXACT_PAPER_HISTORICAL_CROSS_VALIDATE_FOLD_COUNT,
            scoring=EXACT_PAPER_HISTORICAL_SCORING_NAME_LIST,
            verbose=cross_validate_verbose,
        )
    global_metric_dictionary = _build_historical_cross_validate_metric_dictionary(global_score_dictionary)
    emit_exact_paper_progress_log(
        "DONE",
        "Historical wrapper cross-validate complete | "
        f"family={family_name} "
        f"elapsed={format_exact_elapsed_seconds(time.perf_counter() - wrapper_cross_validate_start_time)} "
        f"mean_mae={global_metric_dictionary['mean_absolute_error']:.6f} "
        f"mean_rmse={global_metric_dictionary['root_mean_squared_error']:.6f}",
    )

    # Re-Run The Historical Per-Target Cross-Validation On The Best Estimators
    per_target_metric_dictionary: dict[str, dict[str, float]] = {}
    for target_index, target_name in enumerate(dataset_bundle.target_name_list):
        per_target_estimator = fitted_grid_search_estimator.best_estimator_.estimators_[target_index]
        target_score_input = full_target_matrix[full_target_matrix.columns[target_index:target_index + 1]]
        target_kind, harmonic_order = parse_exact_target_name(target_name)
        target_cross_validate_start_time = time.perf_counter()
        emit_exact_paper_progress_log(
            "INFO",
            "Historical target cross-validate started | "
            f"family={family_name} "
            f"target={target_index + 1}/{len(dataset_bundle.target_name_list)} "
            f"name={target_name} "
            f"kind={target_kind} "
            f"harmonic={harmonic_order} "
            f"cv={EXACT_PAPER_HISTORICAL_CROSS_VALIDATE_FOLD_COUNT} "
            f"verbose={cross_validate_verbose}",
        )
        with threadpool_limits(limits=threadpool_limit):
            target_score_dictionary = cross_validate(
                per_target_estimator,
                full_feature_matrix,
                target_score_input,
                cv=EXACT_PAPER_HISTORICAL_CROSS_VALIDATE_FOLD_COUNT,
                scoring=EXACT_PAPER_HISTORICAL_SCORING_NAME_LIST,
                verbose=cross_validate_verbose,
            )
        per_target_metric_dictionary[target_name] = _build_historical_cross_validate_metric_dictionary(
            target_score_dictionary
        )
        emit_exact_paper_progress_log(
            "DONE",
            "Historical target cross-validate complete | "
            f"family={family_name} "
            f"target={target_index + 1}/{len(dataset_bundle.target_name_list)} "
            f"name={target_name} "
            f"elapsed={format_exact_elapsed_seconds(time.perf_counter() - target_cross_validate_start_time)} "
            f"mean_mae={per_target_metric_dictionary[target_name]['mean_absolute_error']:.6f} "
            f"mean_rmse={per_target_metric_dictionary[target_name]['root_mean_squared_error']:.6f}",
        )

    return {
        "executed": True,
        "cv_fold_count": EXACT_PAPER_HISTORICAL_CROSS_VALIDATE_FOLD_COUNT,
        "scoring_name_list": list(EXACT_PAPER_HISTORICAL_SCORING_NAME_LIST),
        "global_wrapper_metric_mean_dictionary": global_metric_dictionary,
        "per_target_best_estimator_metric_mean_dictionary": per_target_metric_dictionary,
    }


def parse_exact_target_name(target_name: str) -> tuple[str, int]:

    """Parse one recovered target name into target kind and harmonic order."""

    # Parse The Recovered Target Suffix
    target_tokens = target_name.split("_")
    target_kind = str(target_tokens[-2]).strip()
    harmonic_order = int(target_tokens[-1])
    assert target_kind in ["ampl", "phase"], f"Unsupported exact target kind | {target_kind}"
    return target_kind, harmonic_order


def normalize_exact_paper_family_name(family_name: str | None) -> str | None:

    """Normalize one paper-facing family label to the repository family code."""

    if family_name is None:
        return None
    normalized_family_name = EXACT_PAPER_FAMILY_NAME_ALIAS_MAP.get(family_name, family_name)
    return str(normalized_family_name)


def format_exact_paper_metric_value(metric_value: float | None) -> str:

    """Format one paper or repository metric value for compact Markdown tables."""

    if metric_value is None:
        return "-"
    absolute_metric_value = abs(float(metric_value))
    if absolute_metric_value == 0.0:
        return "0.0"
    if absolute_metric_value < 1e-3:
        return f"{float(metric_value):.2e}"
    if absolute_metric_value < 1e-2:
        return f"{float(metric_value):.6f}"
    if absolute_metric_value < 1.0:
        return f"{float(metric_value):.4f}"
    return f"{float(metric_value):.3f}"


def format_exact_paper_report_value(metric_value: Any) -> str:

    """Format one optional report cell for partial-scope validation tables."""

    if metric_value in [None, ""]:
        return "-"
    if isinstance(metric_value, str):
        return f"`{metric_value}`"
    return format_exact_paper_metric_value(float(metric_value))


def resolve_exact_paper_table_metric_map(target_kind: str, metric_name: str) -> dict[str, dict[int, float]]:

    """Resolve the canonical paper table metric map for one target kind."""

    if target_kind == "ampl" and metric_name == "rmse":
        return EXACT_PAPER_TABLE3_RMSE_AMPLITUDE_MAP
    if target_kind == "phase" and metric_name == "mae":
        return EXACT_PAPER_TABLE4_MAE_PHASE_MAP
    if target_kind == "phase" and metric_name == "rmse":
        return EXACT_PAPER_TABLE5_RMSE_PHASE_MAP
    raise AssertionError(f"Unsupported paper table metric request | target_kind={target_kind} metric_name={metric_name}")


def resolve_best_entry_for_metric(
    ranking_list: list[dict[str, Any]],
    metric_name: str,
) -> dict[str, Any]:

    """Resolve the best repository entry for one target and one metric."""

    return min(
        ranking_list,
        key=lambda entry: (
            float(entry[metric_name]),
            float(entry["mae"]),
            float(entry["rmse"]),
            str(entry["family_name"]),
        ),
    )


def resolve_paper_best_family_for_metric(
    target_kind: str,
    harmonic_order: int,
    metric_name: str,
) -> tuple[str | None, float | None]:

    """Resolve the best paper-side family and metric value for one target."""

    paper_metric_map = resolve_exact_paper_table_metric_map(target_kind, metric_name)
    candidate_value_list: list[tuple[float, str]] = []
    for family_name, harmonic_metric_dictionary in paper_metric_map.items():
        if harmonic_order not in harmonic_metric_dictionary:
            continue
        candidate_value_list.append((float(harmonic_metric_dictionary[harmonic_order]), str(family_name)))

    if not candidate_value_list:
        return None, None

    best_metric_value, best_family_name = min(candidate_value_list, key=lambda item: (item[0], item[1]))
    return best_family_name, float(best_metric_value)


def build_exact_paper_numeric_target_comparison_registry(
    per_target_ranking_dictionary: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:

    """Build the canonical numeric paper-vs-repository comparison per target."""

    numeric_target_comparison_list: list[dict[str, Any]] = []
    for target_name in sorted(per_target_ranking_dictionary.keys(), key=lambda name: (parse_exact_target_name(name)[1], parse_exact_target_name(name)[0])):
        target_kind, harmonic_order = parse_exact_target_name(target_name)
        ranking_list = per_target_ranking_dictionary[target_name]
        table6_family_name = EXACT_PAPER_TABLE6_SELECTED_MODEL_MAP[harmonic_order][target_kind]
        normalized_table6_family_name = normalize_exact_paper_family_name(table6_family_name)

        best_repository_mae_entry = resolve_best_entry_for_metric(ranking_list, "mae")
        best_repository_rmse_entry = resolve_best_entry_for_metric(ranking_list, "rmse")

        paper_best_mae_family_name, paper_best_mae_value = (None, None)
        if target_kind == "phase":
            paper_best_mae_family_name, paper_best_mae_value = resolve_paper_best_family_for_metric(target_kind, harmonic_order, "mae")

        paper_best_rmse_family_name, paper_best_rmse_value = resolve_paper_best_family_for_metric(target_kind, harmonic_order, "rmse")

        if normalized_table6_family_name is None:
            table6_family_status = "paper_not_defined"
        else:
            family_match_list = [
                str(best_repository_rmse_entry["family_name"]) == normalized_table6_family_name,
            ]
            if target_kind == "phase":
                family_match_list.append(str(best_repository_mae_entry["family_name"]) == normalized_table6_family_name)
            table6_family_status = "matched_table6_family" if all(family_match_list) else "not_matched_table6_family"

        mae_target_status = "not_applicable"
        mae_gap = None
        if paper_best_mae_value is not None:
            mae_gap = float(best_repository_mae_entry["mae"]) - float(paper_best_mae_value)
            mae_target_status = "met_paper_target" if mae_gap <= 0.0 else "above_paper_target"

        rmse_gap = None
        rmse_target_status = "not_applicable"
        if paper_best_rmse_value is not None:
            rmse_gap = float(best_repository_rmse_entry["rmse"]) - float(paper_best_rmse_value)
            rmse_target_status = "met_paper_target" if rmse_gap <= 0.0 else "above_paper_target"

        numeric_target_comparison_list.append(
            {
                "target_name": target_name,
                "target_kind": target_kind,
                "harmonic_order": harmonic_order,
                "paper_table6_selected_family": table6_family_name,
                "paper_table6_selected_family_normalized": normalized_table6_family_name,
                "paper_best_mae_family": paper_best_mae_family_name,
                "paper_best_mae_value": paper_best_mae_value,
                "paper_best_rmse_family": paper_best_rmse_family_name,
                "paper_best_rmse_value": paper_best_rmse_value,
                "repository_best_mae_family": str(best_repository_mae_entry["family_name"]),
                "repository_best_mae_value": float(best_repository_mae_entry["mae"]),
                "repository_best_rmse_family": str(best_repository_rmse_entry["family_name"]),
                "repository_best_rmse_value": float(best_repository_rmse_entry["rmse"]),
                "table6_family_status": table6_family_status,
                "mae_gap_vs_paper_best": mae_gap,
                "mae_target_status": mae_target_status,
                "rmse_gap_vs_paper_best": rmse_gap,
                "rmse_target_status": rmse_target_status,
            }
        )
    return numeric_target_comparison_list


def build_exact_paper_numeric_harmonic_summary(
    numeric_target_comparison_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    """Build one harmonic-level numeric summary for paper tables 3-6."""

    harmonic_summary_list: list[dict[str, Any]] = []
    harmonic_order_list = sorted({int(entry["harmonic_order"]) for entry in numeric_target_comparison_list})
    for harmonic_order in harmonic_order_list:
        amplitude_entry = next((entry for entry in numeric_target_comparison_list if entry["harmonic_order"] == harmonic_order and entry["target_kind"] == "ampl"), None)
        phase_entry = next((entry for entry in numeric_target_comparison_list if entry["harmonic_order"] == harmonic_order and entry["target_kind"] == "phase"), None)

        status_token_list: list[str] = []
        if amplitude_entry is not None:
            status_token_list.append(str(amplitude_entry["rmse_target_status"]))
            status_token_list.append(str(amplitude_entry["table6_family_status"]))
        if phase_entry is not None:
            status_token_list.append(str(phase_entry["mae_target_status"]))
            status_token_list.append(str(phase_entry["rmse_target_status"]))
            status_token_list.append(str(phase_entry["table6_family_status"]))

        if status_token_list and all(status_token == "met_paper_target" or status_token == "matched_table6_family" for status_token in status_token_list):
            harmonic_status = "fully_matched_tables_3_6"
        elif any(status_token == "met_paper_target" or status_token == "matched_table6_family" for status_token in status_token_list):
            harmonic_status = "partially_matched_tables_3_6"
        else:
            harmonic_status = "not_yet_matched_tables_3_6"

        harmonic_summary_list.append(
            {
                "harmonic_order": harmonic_order,
                "amplitude_paper_family": None if amplitude_entry is None else amplitude_entry["paper_table6_selected_family"],
                "amplitude_repository_family": None if amplitude_entry is None else amplitude_entry["repository_best_rmse_family"],
                "amplitude_rmse_status": None if amplitude_entry is None else amplitude_entry["rmse_target_status"],
                "phase_paper_family": None if phase_entry is None else phase_entry["paper_table6_selected_family"],
                "phase_repository_mae_family": None if phase_entry is None else phase_entry["repository_best_mae_family"],
                "phase_repository_rmse_family": None if phase_entry is None else phase_entry["repository_best_rmse_family"],
                "phase_mae_status": None if phase_entry is None else phase_entry["mae_target_status"],
                "phase_rmse_status": None if phase_entry is None else phase_entry["rmse_target_status"],
                "harmonic_numeric_status": harmonic_status,
            }
        )
    return harmonic_summary_list

def build_exact_paper_target_comparison_registry(
    target_winner_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    """Build the canonical paper-vs-repository comparison per target."""

    # Compare Repository Winners Against Harmonic-Level Paper Expectations
    target_comparison_list: list[dict[str, Any]] = []
    for target_winner_entry in target_winner_list:
        target_name = str(target_winner_entry["target_name"])
        target_kind, harmonic_order = parse_exact_target_name(target_name)
        expected_family_list = EXACT_PAPER_HARMONIC_EXPECTED_FAMILY_MAP[harmonic_order]
        repository_winning_family = str(target_winner_entry["winning_family"])
        family_direction_match = repository_winning_family in expected_family_list
        target_comparison_list.append(
            {
                "target_name": target_name,
                "target_kind": target_kind,
                "harmonic_order": harmonic_order,
                "paper_expected_family_list": expected_family_list,
                "paper_expected_family_text": " / ".join(expected_family_list),
                "paper_metric_reference_status": "not_yet_serialized_from_table",
                "paper_numeric_target_available": False,
                "repository_winning_family": repository_winning_family,
                "repository_winning_estimator_name": str(target_winner_entry["winning_estimator_name"]),
                "repository_winning_mape_percent": float(target_winner_entry["winning_mape_percent"]),
                "repository_winning_mae": float(target_winner_entry["winning_mae"]),
                "repository_winning_rmse": float(target_winner_entry["winning_rmse"]),
                "family_direction_match": family_direction_match,
                "family_direction_status": (
                    "matched_expected_family_direction"
                    if family_direction_match
                    else "not_matched_expected_family_direction"
                ),
            }
        )
    target_comparison_list.sort(
        key=lambda entry: (
            int(entry["harmonic_order"]),
            str(entry["target_kind"]),
        )
    )
    return target_comparison_list


def build_exact_paper_harmonic_comparison_registry(
    target_comparison_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    """Build the canonical harmonic-level paper-vs-repository comparison."""

    # Group Target Comparisons By Harmonic Order
    harmonic_target_dictionary: dict[int, list[dict[str, Any]]] = {}
    for target_comparison_entry in target_comparison_list:
        harmonic_order = int(target_comparison_entry["harmonic_order"])
        harmonic_target_dictionary.setdefault(harmonic_order, []).append(target_comparison_entry)

    # Build One Harmonic-Level Closure View
    harmonic_comparison_list: list[dict[str, Any]] = []
    for harmonic_order in sorted(harmonic_target_dictionary.keys()):
        harmonic_target_list = sorted(
            harmonic_target_dictionary[harmonic_order],
            key=lambda entry: str(entry["target_kind"]),
        )
        expected_family_list = EXACT_PAPER_HARMONIC_EXPECTED_FAMILY_MAP[harmonic_order]
        matching_target_count = int(sum(1 for entry in harmonic_target_list if bool(entry["family_direction_match"])))
        if matching_target_count == len(harmonic_target_list):
            harmonic_match_status = "full_family_direction_match"
        elif matching_target_count > 0:
            harmonic_match_status = "partial_family_direction_match"
        else:
            harmonic_match_status = "no_family_direction_match"

        amplitude_entry = next((entry for entry in harmonic_target_list if entry["target_kind"] == "ampl"), None)
        phase_entry = next((entry for entry in harmonic_target_list if entry["target_kind"] == "phase"), None)
        harmonic_comparison_list.append(
            {
                "harmonic_order": harmonic_order,
                "paper_expected_family_list": expected_family_list,
                "paper_expected_family_text": " / ".join(expected_family_list),
                "paper_metric_reference_status": "not_yet_serialized_from_table",
                "paper_numeric_target_available": False,
                "repository_target_count": len(harmonic_target_list),
                "matching_target_count": matching_target_count,
                "harmonic_match_status": harmonic_match_status,
                "amplitude_winning_family": (
                    None if amplitude_entry is None else str(amplitude_entry["repository_winning_family"])
                ),
                "phase_winning_family": (
                    None if phase_entry is None else str(phase_entry["repository_winning_family"])
                ),
            }
        )
    return harmonic_comparison_list


def load_exact_model_bank_config(config_path: str | Path) -> dict[str, Any]:

    """Load one exact paper model-bank configuration file."""

    return shared_training_infrastructure.load_training_config(config_path)


def resolve_enabled_family_list(training_config: dict[str, Any]) -> list[str]:

    """Resolve the enabled paper family list from configuration."""

    # Read Enabled Family Names
    configured_family_list = training_config["training"]["enabled_families"]
    enabled_family_list = []
    unsupported_family_list = []

    for configured_family_name in configured_family_list:
        normalized_family_name = str(configured_family_name).strip().upper()
        canonical_family_name = EXACT_PAPER_FAMILY_NAME_ALIAS_MAP.get(normalized_family_name)

        if canonical_family_name is None:
            unsupported_family_list.append(normalized_family_name)
            continue

        enabled_family_list.append(canonical_family_name)

    # Validate Enabled Family Names
    unsupported_family_list.extend(
        family_name
        for family_name in enabled_family_list
        if family_name not in EXACT_FAMILY_ORDER
    )
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
    supported_feature_name_list = [
        ["rpm", "deg", "tor"],
        [
            "angular_position_deg",
            "input_speed_rpm",
            "input_torque_nm",
            "oil_temperature_deg",
            "direction_flag",
        ],
    ]
    assert input_feature_name_list in supported_feature_name_list, (
        "Exact paper input features must use the legacy curve-level schema "
        "or the five-feature dataset input-mode schema"
    )
    return input_feature_name_list


def resolve_exact_target_scope(training_config: dict[str, Any]) -> dict[str, Any]:

    """Resolve the configured target-scope controls for one exact-paper run."""

    # Read Optional Target-Scope Configuration
    target_scope_dictionary = training_config.get("target_scope", {})
    if not isinstance(target_scope_dictionary, dict):
        target_scope_dictionary = {}

    scope_mode = str(target_scope_dictionary.get("mode", "all")).strip().lower()
    assert scope_mode in ["all", "amplitudes_only", "phases_only"], (
        "Unsupported exact target scope mode | "
        f"{scope_mode}"
    )

    include_phase_zero = bool(target_scope_dictionary.get("include_phase_zero", True))
    harmonic_order_filter = target_scope_dictionary.get("harmonic_order_filter", [])
    assert isinstance(harmonic_order_filter, list), (
        "Exact target harmonic_order_filter must be a list when provided"
    )
    resolved_harmonic_order_filter = sorted({int(harmonic_order) for harmonic_order in harmonic_order_filter})

    return {
        "mode": scope_mode,
        "include_phase_zero": include_phase_zero,
        "harmonic_order_filter": resolved_harmonic_order_filter,
    }


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


def resolve_target_name_list(
    dataframe: pd.DataFrame,
    training_config: dict[str, Any],
) -> list[str]:

    """Resolve the ordered exact paper target list from the dataframe."""

    # Collect Full Harmonic Target Surface In Dataframe Order
    full_target_name_list = [
        column_name
        for column_name in dataframe.columns
        if ("ampl" in column_name) or ("phase" in column_name)
    ]

    # Validate Full Harmonic Target Count
    assert len(full_target_name_list) == 20, (
        "Exact paper dataframe must expose 20 harmonic targets | "
        f"found {len(full_target_name_list)}"
    )

    # Apply Configured Target-Scope Filtering
    target_scope = resolve_exact_target_scope(training_config)
    target_name_list: list[str] = []
    for target_name in full_target_name_list:
        target_kind, harmonic_order = parse_exact_target_name(target_name)

        if target_scope["mode"] == "amplitudes_only" and target_kind != "ampl":
            continue
        if target_scope["mode"] == "phases_only" and target_kind != "phase":
            continue
        if (
            target_kind == "phase"
            and harmonic_order == 0
            and not bool(target_scope["include_phase_zero"])
        ):
            continue
        if (
            target_scope["harmonic_order_filter"]
            and harmonic_order not in target_scope["harmonic_order_filter"]
        ):
            continue
        target_name_list.append(target_name)

    assert target_name_list, "Configured exact target scope produced an empty target list"
    return target_name_list


def build_exact_paper_dataset_bundle(training_config: dict[str, Any]) -> ExactPaperDatasetBundle:

    """Build the exact paper dataframe split bundle."""

    # Load The Recovered Dataframe
    dataframe = load_exact_paper_dataframe(training_config)
    feature_name_list = resolve_paper_input_feature_name_list(training_config)
    target_name_list = resolve_target_name_list(dataframe, training_config)

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


def _generate_uniform_integer_sequence(
    count: int,
    minimum_value: int,
    maximum_value: int,
) -> list[int]:

    """Reproduce the recovered integer-grid helper used in the paper code."""

    assert count > 0, "Uniform integer sequence requires a positive count"
    step = max(1, (maximum_value - minimum_value) // count)
    value_array = np.arange(minimum_value, maximum_value + 1, step, dtype=np.int64)
    return [int(value) for value in value_array[:count]]


def _resolve_float_grid_value(
    estimator_parameters: dict[str, Any],
    parameter_name: str,
    fallback_value: float,
) -> float:

    """Resolve one float parameter for the grid with a safe fallback."""

    parameter_value = estimator_parameters.get(parameter_name)
    if parameter_value is None:
        return float(fallback_value)

    return float(parameter_value)


def _resolve_int_grid_value(
    estimator_parameters: dict[str, Any],
    parameter_name: str,
    fallback_value: int,
) -> int:

    """Resolve one integer parameter for the grid with a safe fallback."""

    parameter_value = estimator_parameters.get(parameter_name)
    if parameter_value is None:
        return int(fallback_value)

    return int(parameter_value)


def resolve_exact_paper_hyperparameter_search_settings(
    training_config: dict[str, Any] | None,
) -> dict[str, Any]:

    """Resolve the exact-paper hyperparameter-search settings."""

    training_section = dict((training_config or {}).get("training", {}))
    search_config = dict(training_section.get("hyperparameter_search", {}))
    configured_disabled_family_list = training_section.get("grid_search_disabled_families", [])
    if not isinstance(configured_disabled_family_list, list):
        configured_disabled_family_list = []
    normalized_disabled_family_list = [
        str(family_name).strip().upper()
        for family_name in configured_disabled_family_list
        if str(family_name).strip()
    ]
    search_mode = str(search_config.get("mode", "paper_reference_grid_search")).strip()
    assert search_mode in EXACT_PAPER_HYPERPARAMETER_SEARCH_MODE_LIST, (
        f"Unsupported exact-paper hyperparameter search mode | {search_mode}"
    )
    grid_search_n_jobs = int(search_config.get("grid_search_n_jobs", -1))
    grid_search_verbose = int(search_config.get("grid_search_verbose", 2))
    historical_cross_validate_verbose = int(search_config.get("historical_cross_validate_verbose", 1))
    grid_search_pre_dispatch = str(search_config.get("grid_search_pre_dispatch", "2*n_jobs")).strip()
    return {
        "mode": search_mode,
        "grid_search_n_jobs": grid_search_n_jobs,
        "grid_search_verbose": grid_search_verbose,
        "historical_cross_validate_verbose": historical_cross_validate_verbose,
        "grid_search_pre_dispatch": grid_search_pre_dispatch,
        "grid_search_disabled_families": normalized_disabled_family_list,
    }


def resolve_exact_paper_estimator_runtime_parameters(
    training_config: dict[str, Any] | None,
    family_name: str,
) -> dict[str, Any]:

    """Resolve non-search estimator parameters used only for runtime control."""

    training_section = dict((training_config or {}).get("training", {}))
    runtime_section = training_section.get("estimator_runtime_parameters", {})
    if not isinstance(runtime_section, dict):
        return {}

    normalized_family_name = str(family_name).strip().upper()
    for configured_family_name, runtime_parameter_dictionary in runtime_section.items():
        if str(configured_family_name).strip().upper() != normalized_family_name:
            continue
        if not isinstance(runtime_parameter_dictionary, dict):
            return {}
        return dict(runtime_parameter_dictionary)
    return {}


def create_exact_paper_base_estimator(
    family_name: str,
    runtime_parameter_dictionary: dict[str, Any] | None = None,
) -> object:

    """Create one exact-paper base estimator matching the recovered workflow."""

    resolved_runtime_parameter_dictionary = dict(runtime_parameter_dictionary or {})

    # Create Recovered Original Family Estimators
    if family_name == "SVR":
        return build_exact_paper_faithful_rbf_svr()

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
            alpha=0.01,
            max_depth=16,
            colsample_bytree=0.8,
            random_state=0,
        )

    if family_name == "LGBM":
        return build_repo_quiet_lgbm_regressor(
            learning_rate=0.39,
            max_depth=12,
            subsample=0.1,
            random_state=0,
            **resolved_runtime_parameter_dictionary,
        )

    if family_name == "ELM":
        _assert_optional_dependency(ELMRegressor, "skelm")
        return ELMRegressor(
            n_neurons=250,
            random_state=0,
        )

    raise ValueError(f"Unsupported exact paper family | {family_name}")


def build_exact_paper_scope_descriptor(
    training_config: dict[str, Any],
    dataset_bundle: ExactPaperDatasetBundle,
    workflow_variant: str,
) -> dict[str, Any]:

    """Build one stable scope descriptor for best-parameter reuse."""

    direction_label = str(
        ((training_config or {}).get("data", {}) or {}).get("direction_label", "forward")
    ).strip().lower()
    target_scope_dictionary = resolve_exact_target_scope(training_config)
    selected_harmonic_list = list(((training_config or {}).get("evaluation", {}) or {}).get("selected_harmonics", []))
    enabled_family_list = resolve_enabled_family_list(training_config)
    return {
        "workflow_variant": str(workflow_variant),
        "direction_label": direction_label,
        "target_scope_mode": str(target_scope_dictionary["mode"]),
        "include_phase_zero": bool(target_scope_dictionary["include_phase_zero"]),
        "selected_harmonic_list": [int(harmonic_order) for harmonic_order in selected_harmonic_list],
        "feature_name_list": list(dataset_bundle.feature_name_list),
        "target_name_list": list(dataset_bundle.target_name_list),
        "enabled_family_list": list(enabled_family_list),
    }


def build_exact_paper_best_parameter_summary(
    workflow_variant: str,
    training_config: dict[str, Any],
    dataset_bundle: ExactPaperDatasetBundle,
    family_summary_list: list[dict[str, Any]],
    family_search_summary_dictionary: dict[str, dict[str, Any]],
    validation_summary_path: Path | None = None,
    output_directory: Path | None = None,
) -> dict[str, Any]:

    """Build one run-local exact-paper best-parameter summary payload."""

    scope_descriptor = build_exact_paper_scope_descriptor(
        training_config=training_config,
        dataset_bundle=dataset_bundle,
        workflow_variant=workflow_variant,
    )
    family_metric_map = {
        family_entry["family_name"]: family_entry
        for family_entry in family_summary_list
    }
    family_entry_list: list[dict[str, Any]] = []
    for family_name, family_search_entry in family_search_summary_dictionary.items():
        best_params_dictionary = family_search_entry.get("best_params")
        if best_params_dictionary is None:
            continue
        family_metric_entry = family_metric_map.get(family_name, {})
        family_entry_list.append(
            {
                "family_name": family_name,
                "best_params": dict(best_params_dictionary),
                "best_score": family_search_entry.get("best_score"),
                "search_mode": family_search_entry.get("search_mode"),
                "used_grid_search": bool(family_search_entry.get("used_grid_search", False)),
                "best_parameter_source": str(family_search_entry.get("best_parameter_source", "grid_search")),
                "mean_component_mape_percent": (
                    float(family_metric_entry["mean_component_mape_percent"])
                    if "mean_component_mape_percent" in family_metric_entry
                    else None
                ),
                "mean_component_mae": (
                    float(family_metric_entry["mean_component_mae"])
                    if "mean_component_mae" in family_metric_entry
                    else None
                ),
                "mean_component_rmse": (
                    float(family_metric_entry["mean_component_rmse"])
                    if "mean_component_rmse" in family_metric_entry
                    else None
                ),
            }
        )

    family_entry_list.sort(key=lambda entry: str(entry["family_name"]))
    return {
        "schema_version": 1,
        "generated_at": datetime.now().isoformat(),
        "scope_descriptor": scope_descriptor,
        "validation_summary_path": shared_training_infrastructure.format_project_relative_path(validation_summary_path),
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "family_entries": family_entry_list,
    }


def save_exact_paper_best_parameter_summary(
    best_parameter_summary: dict[str, Any],
    output_directory: Path,
) -> Path:

    """Persist one exact-paper best-parameter summary into the run artifact root."""

    best_parameter_summary_path = output_directory / EXACT_PAPER_BEST_PARAMETER_SUMMARY_FILENAME
    shared_training_infrastructure.save_yaml_snapshot(best_parameter_summary, best_parameter_summary_path)
    return best_parameter_summary_path


def load_exact_paper_best_parameter_summary(
    best_parameter_summary_path: str | Path,
) -> dict[str, Any]:

    """Load one exact-paper best-parameter summary payload."""

    return shared_training_infrastructure.load_training_config(best_parameter_summary_path)


def build_exact_paper_best_parameter_override_map(
    best_parameter_summary: dict[str, Any],
    enabled_family_list: list[str],
) -> dict[str, dict[str, Any]]:

    """Extract one family-name to best-parameter map from a saved summary."""

    family_entry_map = {
        str(family_entry["family_name"]).strip().upper(): dict(family_entry["best_params"])
        for family_entry in list(best_parameter_summary.get("family_entries", []))
        if family_entry.get("best_params") is not None
    }
    missing_family_list = [
        family_name for family_name in enabled_family_list
        if family_name not in family_entry_map
    ]
    assert not missing_family_list, (
        "Best-parameter summary does not cover the requested exact-paper families | "
        f"{','.join(missing_family_list)}"
    )
    return {
        family_name: family_entry_map[family_name]
        for family_name in enabled_family_list
    }


def _exact_paper_registry_entries_match_scope(
    registry_entry: dict[str, Any],
    scope_descriptor: dict[str, Any],
    family_name: str,
) -> bool:

    """Return whether one registry entry matches the requested workflow scope."""

    return (
        str(registry_entry.get("workflow_variant", "")).strip() == str(scope_descriptor["workflow_variant"])
        and str(registry_entry.get("direction_label", "")).strip().lower() == str(scope_descriptor["direction_label"])
        and str(registry_entry.get("target_scope_mode", "")).strip() == str(scope_descriptor["target_scope_mode"])
        and bool(registry_entry.get("include_phase_zero", False)) == bool(scope_descriptor["include_phase_zero"])
        and list(registry_entry.get("selected_harmonic_list", [])) == list(scope_descriptor["selected_harmonic_list"])
        and list(registry_entry.get("target_name_list", [])) == list(scope_descriptor["target_name_list"])
        and str(registry_entry.get("family_name", "")).strip().upper() == str(family_name).strip().upper()
    )


def load_exact_paper_best_parameter_registry(
    registry_path: str | Path | None = None,
) -> dict[str, Any]:

    """Load the repo-owned exact-paper best-parameter registry."""

    resolved_registry_path = Path(registry_path or EXACT_PAPER_BEST_PARAMETER_REGISTRY_PATH)
    if not resolved_registry_path.exists():
        return {
            "schema_version": 1,
            "updated_at": None,
            "entries": [],
        }
    return shared_training_infrastructure.load_training_config(resolved_registry_path)


def update_exact_paper_best_parameter_registry(
    best_parameter_summary: dict[str, Any],
    registry_path: str | Path | None = None,
) -> Path:

    """Update the repo-owned exact-paper best-parameter registry."""

    resolved_registry_path = Path(registry_path or EXACT_PAPER_BEST_PARAMETER_REGISTRY_PATH)
    registry_payload = load_exact_paper_best_parameter_registry(resolved_registry_path)
    existing_entry_list = list(registry_payload.get("entries", []))
    scope_descriptor = dict(best_parameter_summary["scope_descriptor"])

    for family_entry in list(best_parameter_summary.get("family_entries", [])):
        family_name = str(family_entry["family_name"]).strip().upper()
        replacement_entry = {
            "workflow_variant": scope_descriptor["workflow_variant"],
            "direction_label": scope_descriptor["direction_label"],
            "target_scope_mode": scope_descriptor["target_scope_mode"],
            "include_phase_zero": scope_descriptor["include_phase_zero"],
            "selected_harmonic_list": list(scope_descriptor["selected_harmonic_list"]),
            "target_name_list": list(scope_descriptor["target_name_list"]),
            "family_name": family_name,
            "best_params": dict(family_entry["best_params"]),
            "best_score": family_entry.get("best_score"),
            "search_mode": family_entry.get("search_mode"),
            "best_parameter_source": family_entry.get("best_parameter_source"),
            "mean_component_mape_percent": family_entry.get("mean_component_mape_percent"),
            "mean_component_mae": family_entry.get("mean_component_mae"),
            "mean_component_rmse": family_entry.get("mean_component_rmse"),
            "source_validation_summary_path": best_parameter_summary.get("validation_summary_path"),
            "source_best_parameter_summary_path": best_parameter_summary.get("best_parameter_summary_path"),
            "updated_at": datetime.now().isoformat(),
        }

        replacement_index = None
        for existing_index, existing_entry in enumerate(existing_entry_list):
            if _exact_paper_registry_entries_match_scope(existing_entry, scope_descriptor, family_name):
                replacement_index = existing_index
                break

        if replacement_index is None:
            existing_entry_list.append(replacement_entry)
            continue

        existing_entry = existing_entry_list[replacement_index]
        replacement_key = (
            float(replacement_entry["mean_component_mape_percent"]) if replacement_entry["mean_component_mape_percent"] is not None else float("inf"),
            float(replacement_entry["mean_component_mae"]) if replacement_entry["mean_component_mae"] is not None else float("inf"),
            float(replacement_entry["mean_component_rmse"]) if replacement_entry["mean_component_rmse"] is not None else float("inf"),
            str(replacement_entry["family_name"]),
        )
        existing_key = (
            float(existing_entry.get("mean_component_mape_percent", float("inf"))) if existing_entry.get("mean_component_mape_percent") is not None else float("inf"),
            float(existing_entry.get("mean_component_mae", float("inf"))) if existing_entry.get("mean_component_mae") is not None else float("inf"),
            float(existing_entry.get("mean_component_rmse", float("inf"))) if existing_entry.get("mean_component_rmse") is not None else float("inf"),
            str(existing_entry.get("family_name", "")),
        )
        if replacement_key <= existing_key:
            existing_entry_list[replacement_index] = replacement_entry

    resolved_registry_path.parent.mkdir(parents=True, exist_ok=True)
    shared_training_infrastructure.save_yaml_snapshot(
        {
            "schema_version": 1,
            "updated_at": datetime.now().isoformat(),
            "entries": existing_entry_list,
        },
        resolved_registry_path,
    )
    return resolved_registry_path


def resolve_exact_paper_best_parameter_summary_from_registry(
    training_config: dict[str, Any],
    dataset_bundle: ExactPaperDatasetBundle,
    workflow_variant: str,
    enabled_family_list: list[str],
    registry_path: str | Path | None = None,
) -> dict[str, Any]:

    """Materialize one summary-like payload from the repo-owned registry."""

    scope_descriptor = build_exact_paper_scope_descriptor(
        training_config=training_config,
        dataset_bundle=dataset_bundle,
        workflow_variant=workflow_variant,
    )
    registry_payload = load_exact_paper_best_parameter_registry(registry_path)
    matched_family_entry_list: list[dict[str, Any]] = []
    for family_name in enabled_family_list:
        matching_entry = None
        for registry_entry in list(registry_payload.get("entries", [])):
            if _exact_paper_registry_entries_match_scope(registry_entry, scope_descriptor, family_name):
                matching_entry = registry_entry
                break
        assert matching_entry is not None, (
            "Exact-paper best-parameter registry does not cover the requested family scope | "
            f"family={family_name} workflow_variant={workflow_variant} direction={scope_descriptor['direction_label']}"
        )
        matched_family_entry_list.append(
            {
                "family_name": family_name,
                "best_params": dict(matching_entry["best_params"]),
                "best_score": matching_entry.get("best_score"),
                "search_mode": matching_entry.get("search_mode"),
                "used_grid_search": False,
                "best_parameter_source": "stored_registry",
                "mean_component_mape_percent": matching_entry.get("mean_component_mape_percent"),
                "mean_component_mae": matching_entry.get("mean_component_mae"),
                "mean_component_rmse": matching_entry.get("mean_component_rmse"),
            }
        )

    return {
        "schema_version": 1,
        "generated_at": datetime.now().isoformat(),
        "scope_descriptor": scope_descriptor,
        "validation_summary_path": None,
        "output_directory": None,
        "family_entries": matched_family_entry_list,
    }


def build_exact_paper_reference_parameter_grid(
    family_name: str,
    base_estimator: object,
) -> dict[str, list[Any]] | list[dict[str, list[Any]]]:

    """Build the recovered original `predictorML.py` grid for one family."""

    estimator_parameters = base_estimator.get_params()

    if family_name == "DT":
        return {
            "estimator__criterion": list(dict.fromkeys(["squared_error", "absolute_error", base_estimator.get_params()["criterion"]])),
            "estimator__max_depth": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 14, 21) + [int(base_estimator.get_params()["max_depth"])])),
            "estimator__max_leaf_nodes": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 23, 28) + [base_estimator.get_params()["max_leaf_nodes"]])),
            "estimator__min_samples_split": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 2, 10) + [int(base_estimator.get_params()["min_samples_split"])])),
        }

    if family_name == "ET":
        return {
            "estimator__criterion": list(dict.fromkeys(["squared_error", "absolute_error", base_estimator.get_params()["criterion"]])),
            "estimator__max_depth": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 14, 21) + [int(base_estimator.get_params()["max_depth"])])),
            "estimator__max_leaf_nodes": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 27, 35) + [base_estimator.get_params()["max_leaf_nodes"]])),
            "estimator__min_samples_split": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 2, 10) + [int(base_estimator.get_params()["min_samples_split"])])),
        }

    if family_name == "ERT":
        return {
            "estimator__n_estimators": list(dict.fromkeys([20, 40, 60, 80, 100, int(base_estimator.get_params()["n_estimators"])])),
            "estimator__criterion": list(dict.fromkeys(["squared_error", "absolute_error", base_estimator.get_params()["criterion"]])),
            "estimator__max_depth": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 14, 21) + [int(base_estimator.get_params()["max_depth"])])),
            "estimator__max_leaf_nodes": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 27, 35) + [base_estimator.get_params()["max_leaf_nodes"]])),
            "estimator__min_samples_split": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 2, 10) + [int(base_estimator.get_params()["min_samples_split"])])),
        }

    if family_name == "RF":
        return {
            "estimator__n_estimators": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 20, 100) + [int(base_estimator.get_params()["n_estimators"])])),
            "estimator__criterion": list(dict.fromkeys(["squared_error", "absolute_error", base_estimator.get_params()["criterion"]])),
            "estimator__max_features": list(dict.fromkeys(["log2", "sqrt", base_estimator.get_params()["max_features"]])),
            "estimator__max_depth": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 14, 21) + [int(base_estimator.get_params()["max_depth"])])),
            "estimator__min_samples_split": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 2, 10) + [int(base_estimator.get_params()["min_samples_split"])])),
        }

    if family_name == "GBM":
        # Keep the recovered search surface, but constrain criterion to the
        # modern scikit-learn value that still executes on current versions.
        return {
            "estimator__n_estimators": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 20, 100) + [int(base_estimator.get_params()["n_estimators"])])),
            "estimator__criterion": ["squared_error"],
            "estimator__max_features": list(dict.fromkeys(["log2", "sqrt", base_estimator.get_params()["max_features"]])),
            "estimator__max_depth": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 14, 21) + [int(base_estimator.get_params()["max_depth"])])),
            "estimator__min_samples_split": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 2, 10) + [int(base_estimator.get_params()["min_samples_split"])])),
            "estimator__learning_rate": list(dict.fromkeys([0.0001, 0.001, 0.01, 0.1, 1.0, base_estimator.get_params()["learning_rate"]])),
        }

    if family_name == "XGBM":
        # The recovered workflow uses the intended n_estimators candidate list,
        # but the historical parameter key is misspelled. Normalize the key to
        # the executable current XGBoost API while keeping the same values.
        return {
            "estimator__learning_rate": list(
                dict.fromkeys(
                    [
                        0.01,
                        0.2,
                        0.5,
                        _resolve_float_grid_value(estimator_parameters, "learning_rate", 0.3),
                    ]
                )
            ),
            "estimator__n_estimators": list(
                dict.fromkeys(
                    _generate_uniform_integer_sequence(5, 20, 100)
                    + [_resolve_int_grid_value(estimator_parameters, "n_estimators", 100)]
                )
            ),
            "estimator__max_depth": list(
                dict.fromkeys(
                    _generate_uniform_integer_sequence(5, 14, 21)
                    + [_resolve_int_grid_value(estimator_parameters, "max_depth", 16)]
                )
            ),
            "estimator__colsample_bytree": list(
                dict.fromkeys(
                    [
                        0.3,
                        0.5,
                        _resolve_float_grid_value(estimator_parameters, "colsample_bytree", 0.8),
                    ]
                )
            ),
        }

    if family_name == "HGBM":
        return {
            "estimator__max_iter": list(dict.fromkeys([10, 100, 1000, int(base_estimator.get_params()["max_iter"])])),
            "estimator__max_depth": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 14, 21) + [int(base_estimator.get_params()["max_depth"])])),
            "estimator__learning_rate": list(dict.fromkeys(([value / 100 for value in _generate_uniform_integer_sequence(5, 1, 100)] + [float(base_estimator.get_params()["learning_rate"])]))),
            "estimator__max_leaf_nodes": list(dict.fromkeys(_generate_uniform_integer_sequence(5, 27, 35) + [int(base_estimator.get_params()["max_leaf_nodes"])])),
        }

    if family_name == "LGBM":
        return {
            "estimator__learning_rate": list(
                dict.fromkeys(
                    ([value / 100 for value in _generate_uniform_integer_sequence(5, 1, 100)]
                     + [_resolve_float_grid_value(estimator_parameters, "learning_rate", 0.39)])
                )
            ),
            "estimator__max_depth": list(
                dict.fromkeys(
                    _generate_uniform_integer_sequence(5, 14, 21)
                    + [_resolve_int_grid_value(estimator_parameters, "max_depth", 12)]
                )
            ),
            "estimator__num_leaves": list(
                dict.fromkeys(
                    _generate_uniform_integer_sequence(5, 10, 100)
                    + [_resolve_int_grid_value(estimator_parameters, "num_leaves", 31)]
                )
            ),
            "estimator__subsample": list(
                dict.fromkeys(
                    [0.1, 0.3, 0.5, 0.8, _resolve_float_grid_value(estimator_parameters, "subsample", 0.1)]
                )
            ),
        }

    if family_name == "ELM":
        return {
            "estimator__n_neurons": list(
                dict.fromkeys(
                    [100, 250, 500]
                    + (
                        [int(estimator_parameters["n_neurons"])]
                        if estimator_parameters.get("n_neurons") is not None
                        else []
                    )
                )
            ),
            "estimator__alpha": list(
                dict.fromkeys([1e-7, 1e-5, 1e-3, float(estimator_parameters["alpha"])])
            ),
            "estimator__ufunc": list(
                dict.fromkeys(["tanh", str(estimator_parameters["ufunc"])])
            ),
        }

    if family_name == "MLP":
        mlp_parameter_dictionary = base_estimator.get_params()
        return {
            "estimator__hidden_layer_sizes": list(
                dict.fromkeys(
                    [
                        (100,),
                        (50,),
                        (100, 50),
                        (200,),
                        (200, 50),
                        tuple(mlp_parameter_dictionary["hidden_layer_sizes"]),
                    ]
                )
            ),
            "estimator__activation": list(
                dict.fromkeys(["tanh", "relu", str(mlp_parameter_dictionary["activation"])])
            ),
            "estimator__solver": list(
                dict.fromkeys(["sgd", "adam", str(mlp_parameter_dictionary["solver"])])
            ),
            "estimator__alpha": list(
                dict.fromkeys([1e-4, float(mlp_parameter_dictionary["alpha"])])
            ),
            "estimator__learning_rate": list(
                dict.fromkeys(["adaptive", str(mlp_parameter_dictionary["learning_rate"])])
            ),
            "estimator__early_stopping": list(
                dict.fromkeys([True, bool(mlp_parameter_dictionary["early_stopping"])])
            ),
            "estimator__tol": list(
                dict.fromkeys([1e-4, float(mlp_parameter_dictionary["tol"])])
            ),
            "estimator__max_iter": list(
                dict.fromkeys([600, int(mlp_parameter_dictionary["max_iter"])])
            ),
        }

    if family_name == "SVR":
        return [
            {
                "estimator": [build_exact_paper_faithful_rbf_svr()],
                "estimator__C": list(dict.fromkeys([1, 2, 3, 5, 6, 7, float(base_estimator.get_params()["C"])])),
                "estimator__epsilon": list(dict.fromkeys([0.0001, 0.00001, 0.000001, 0.0000001])),
                "estimator__gamma": list(dict.fromkeys([0.0000011])),
            },
            {
                "estimator": [build_exact_pragmatic_linear_svr_pipeline()],
                "estimator__model__C": list(dict.fromkeys([1, 2, 3, 5, 6, 7, float(base_estimator.get_params()["C"])])),
                "estimator__model__epsilon": list(dict.fromkeys([0.0001, 0.00001, 0.000001, 0.0000001])),
                "estimator__model__tol": [1e-4],
                "estimator__model__max_iter": [5000],
            },
        ]

    raise ValueError(f"Unsupported exact paper family grid search | {family_name}")


def fit_exact_family_model_bank(
    dataset_bundle: ExactPaperDatasetBundle,
    enabled_family_list: list[str],
    training_config: dict[str, Any] | None = None,
    best_parameter_override_map: dict[str, dict[str, Any]] | None = None,
    workflow_stage: str = "search",
) -> tuple[dict[str, MultiOutputRegressor], dict[str, dict[str, Any]]]:

    """Fit the recovered family bank using the configured paper-side strategy."""

    # Fit Each Family Bank
    fitted_family_model_dictionary: dict[str, MultiOutputRegressor] = {}
    family_search_summary_dictionary: dict[str, dict[str, Any]] = {}
    threadpool_limit = int((training_config or {}).get("training", {}).get("threadpool_limit", 1))
    joblib_cpu_limit = int((training_config or {}).get("training", {}).get("joblib_cpu_limit", 0))
    smoke_enabled = bool((training_config or {}).get("smoke", {}).get("enabled", False))
    search_settings = resolve_exact_paper_hyperparameter_search_settings(training_config)
    resolved_workflow_stage = resolve_exact_paper_workflow_stage(workflow_stage)
    if joblib_cpu_limit > 0:
        os.environ["LOKY_MAX_CPU_COUNT"] = str(joblib_cpu_limit)
    elif "LOKY_MAX_CPU_COUNT" in os.environ:
        del os.environ["LOKY_MAX_CPU_COUNT"]
    for family_name in enabled_family_list:
        family_fit_start_time = time.perf_counter()
        loaded_best_parameter_dictionary = None
        estimator_runtime_parameter_dictionary = resolve_exact_paper_estimator_runtime_parameters(
            training_config,
            family_name,
        )
        base_estimator = create_exact_paper_base_estimator(
            family_name,
            runtime_parameter_dictionary=estimator_runtime_parameter_dictionary,
        )
        if best_parameter_override_map is not None and family_name in best_parameter_override_map:
            stored_best_parameter_dictionary = dict(best_parameter_override_map[family_name])
            if family_name == "SVR" and is_exact_svr_variant_payload(stored_best_parameter_dictionary):
                loaded_best_parameter_dictionary = stored_best_parameter_dictionary
                base_estimator = build_exact_svr_estimator_from_serialized_payload(
                    loaded_best_parameter_dictionary
                )
            else:
                loaded_best_parameter_dictionary = normalize_loaded_exact_best_parameter_dictionary(
                    stored_best_parameter_dictionary
                )
                base_estimator.set_params(**loaded_best_parameter_dictionary)
        if family_name == "MLP" and smoke_enabled:
            base_estimator.set_params(
                max_iter=min(int(base_estimator.get_params()["max_iter"]), 50),
            )
        train_feature_matrix: pd.DataFrame | np.ndarray = dataset_bundle.train_feature_matrix
        if family_name == "XGBM":
            train_feature_matrix = dataset_bundle.train_feature_matrix.to_numpy(dtype=np.float32)
        wrapped_estimator = MultiOutputRegressor(base_estimator)
        grid_search_disabled_for_family = family_name in search_settings["grid_search_disabled_families"]
        emit_exact_paper_progress_log(
            "INFO",
            "Family fit started | "
            f"family={family_name} "
            f"stage={resolved_workflow_stage} "
            f"estimator={type(base_estimator).__name__} "
            f"targets={len(dataset_bundle.target_name_list)} "
            f"threadpool_limit={threadpool_limit} "
            f"joblib_cpu_limit={joblib_cpu_limit if joblib_cpu_limit > 0 else 'system_default'} "
            f"estimator_runtime_parameters={estimator_runtime_parameter_dictionary or '{}'} "
            f"os_cpu_count={os.cpu_count()}",
        )
        emit_exact_paper_progress_log(
            "INFO",
            "Family target scope | "
            f"family={family_name} "
            f"{build_exact_target_scope_log_summary(dataset_bundle.target_name_list)}",
        )

        use_grid_search = (
            search_settings["mode"] == "paper_reference_grid_search"
            and not grid_search_disabled_for_family
            and loaded_best_parameter_dictionary is None
        )
        if loaded_best_parameter_dictionary is not None:
            emit_exact_paper_progress_log(
                "INFO",
                "Loaded stored best parameters | "
                f"family={family_name} "
                f"parameter_source=loaded_summary_or_registry "
                f"best_params={loaded_best_parameter_dictionary}",
            )
        if use_grid_search:
            parameter_grid = build_exact_paper_reference_parameter_grid(family_name, base_estimator)
            parameter_grid_candidate_count = count_exact_parameter_grid_candidates(parameter_grid)
            estimated_grid_search_cv_fit_count = int(parameter_grid_candidate_count * 5)
            emit_exact_paper_progress_log(
                "INFO",
                "Grid search configured | "
                f"family={family_name} "
                f"stage={resolved_workflow_stage} "
                f"candidates={parameter_grid_candidate_count} "
                f"estimated_cv_fits={estimated_grid_search_cv_fit_count} "
                f"parameter_count={count_exact_parameter_grid_dimensions(parameter_grid)} "
                f"n_jobs={int(search_settings['grid_search_n_jobs'])} "
                f"verbose={int(search_settings['grid_search_verbose'])} "
                f"historical_cross_validate_verbose={int(search_settings['historical_cross_validate_verbose'])} "
                f"pre_dispatch={search_settings['grid_search_pre_dispatch']}",
            )
            grid_search_estimator = GridSearchCV(
                wrapped_estimator,
                parameter_grid,
                n_jobs=int(search_settings["grid_search_n_jobs"]),
                verbose=int(search_settings["grid_search_verbose"]),
                pre_dispatch=search_settings["grid_search_pre_dispatch"],
            )
            with threadpool_limits(limits=threadpool_limit):
                grid_search_estimator.fit(
                    train_feature_matrix,
                    dataset_bundle.train_target_matrix,
                )
            emit_exact_paper_progress_log(
                "INFO",
                "Historical search protocol replay started | "
                f"family={family_name} "
                f"cv={EXACT_PAPER_HISTORICAL_CROSS_VALIDATE_FOLD_COUNT} "
                f"targets={len(dataset_bundle.target_name_list)}",
            )
            historical_protocol_summary = _build_historical_search_protocol_summary(
                family_name=family_name,
                dataset_bundle=dataset_bundle,
                fitted_grid_search_estimator=grid_search_estimator,
                threadpool_limit=threadpool_limit,
                cross_validate_verbose=int(search_settings["historical_cross_validate_verbose"]),
            )
            serialized_best_parameter_dictionary = serialize_exact_best_parameter_payload(
                family_name=family_name,
                best_parameter_dictionary=dict(grid_search_estimator.best_params_),
            )
            elapsed_seconds = time.perf_counter() - family_fit_start_time
            best_wrapped_estimator = grid_search_estimator.best_estimator_
            fitted_family_model_dictionary[family_name] = best_wrapped_estimator
            family_search_summary_dictionary[family_name] = {
                "search_mode": search_settings["mode"],
                "used_grid_search": True,
                "grid_search_disabled_for_family": False,
                "workflow_stage": resolved_workflow_stage,
                "grid_search_n_jobs": int(search_settings["grid_search_n_jobs"]),
                "grid_search_verbose": int(search_settings["grid_search_verbose"]),
                "historical_cross_validate_verbose": int(search_settings["historical_cross_validate_verbose"]),
                "grid_search_pre_dispatch": search_settings["grid_search_pre_dispatch"],
                "estimator_runtime_parameters": dict(estimator_runtime_parameter_dictionary),
                "grid_search_cv": (
                    int(grid_search_estimator.n_splits_)
                    if hasattr(grid_search_estimator, "n_splits_")
                    else None
                ),
                "parameter_grid": serialize_exact_search_summary_payload(parameter_grid),
                "best_params": serialized_best_parameter_dictionary,
                "best_parameter_source": "grid_search",
                "best_score": (
                    float(grid_search_estimator.best_score_)
                    if getattr(grid_search_estimator, "best_score_", None) is not None
                    else None
                ),
                "historical_protocol_summary": historical_protocol_summary,
            }
            emit_exact_paper_progress_log(
                "DONE",
                "Family fit complete | "
                f"family={family_name} "
                f"elapsed={format_exact_elapsed_seconds(elapsed_seconds)} "
                f"best_score={family_search_summary_dictionary[family_name]['best_score']} "
                f"best_params={family_search_summary_dictionary[family_name]['best_params']}",
            )
            continue

        if grid_search_disabled_for_family:
            emit_exact_paper_progress_log(
            "INFO",
            "Grid search bypassed for family | "
            f"family={family_name} "
            f"stage={resolved_workflow_stage} "
            f"configured_disabled_families={','.join(search_settings['grid_search_disabled_families'])}",
        )
        with threadpool_limits(limits=threadpool_limit):
            wrapped_estimator.fit(
                train_feature_matrix,
                dataset_bundle.train_target_matrix,
            )
        elapsed_seconds = time.perf_counter() - family_fit_start_time
        fitted_family_model_dictionary[family_name] = wrapped_estimator
        family_search_summary_dictionary[family_name] = {
            "search_mode": search_settings["mode"],
            "used_grid_search": False,
            "grid_search_disabled_for_family": bool(grid_search_disabled_for_family),
            "workflow_stage": resolved_workflow_stage,
            "grid_search_n_jobs": None,
            "grid_search_verbose": None,
            "historical_cross_validate_verbose": None,
            "grid_search_pre_dispatch": None,
            "estimator_runtime_parameters": dict(estimator_runtime_parameter_dictionary),
            "grid_search_cv": None,
            "parameter_grid": None,
            "best_params": (
                dict(loaded_best_parameter_dictionary)
                if loaded_best_parameter_dictionary is not None
                else None
            ),
            "best_parameter_source": (
                "loaded_summary_or_registry"
                if loaded_best_parameter_dictionary is not None
                else "direct_fit"
            ),
            "best_score": None,
            "historical_protocol_summary": None,
        }
        emit_exact_paper_progress_log(
            "DONE",
            "Family fit complete | "
            f"family={family_name} "
            f"elapsed={format_exact_elapsed_seconds(elapsed_seconds)} "
            f"search_mode={search_settings['mode']} "
            f"grid_search_disabled_for_family={grid_search_disabled_for_family} "
            f"best_parameter_source={family_search_summary_dictionary[family_name]['best_parameter_source']}",
        )

    return fitted_family_model_dictionary, family_search_summary_dictionary


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
        family_evaluation_start_time = time.perf_counter()
        emit_exact_paper_progress_log(
            "INFO",
            "Family evaluation started | "
            f"family={family_name} "
            f"targets={len(dataset_bundle.target_name_list)}",
        )
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
        emit_exact_paper_progress_log(
            "DONE",
            "Family evaluation complete | "
            f"family={family_name} "
            f"elapsed={format_exact_elapsed_seconds(time.perf_counter() - family_evaluation_start_time)} "
            f"mean_component_mape={family_summary_list[-1]['mean_component_mape_percent']:.3f}% "
            f"mean_component_mae={family_summary_list[-1]['mean_component_mae']:.6f}",
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


def normalize_loaded_exact_best_parameter_dictionary(
    loaded_best_parameter_dictionary: dict[str, Any],
) -> dict[str, Any]:

    """Normalize one stored exact-paper best-parameter dictionary for replay."""

    if is_exact_svr_variant_payload(loaded_best_parameter_dictionary):
        return dict(loaded_best_parameter_dictionary)

    # Strip The GridSearchCV `estimator__` Prefix Before Rebuilding The Base Estimator
    normalized_best_parameter_dictionary: dict[str, Any] = {}
    for parameter_name, parameter_value in loaded_best_parameter_dictionary.items():
        normalized_parameter_name = str(parameter_name)
        if normalized_parameter_name.startswith("estimator__"):
            normalized_parameter_name = normalized_parameter_name.split("estimator__", 1)[1]
        normalized_best_parameter_dictionary[normalized_parameter_name] = parameter_value
    return normalized_best_parameter_dictionary


def _convert_estimator_to_onnx(
    estimator: object,
    feature_count: int,
    estimator_name: str,
    target_opset: int,
) -> Any:

    """Convert one fitted estimator into an ONNX model."""

    # Convert HistGradientBoosting Through A Sanitized Temporary Converter Patch
    if estimator_name == "HistGradientBoostingRegressor":
        _assert_optional_dependency(convert_sklearn, "skl2onnx")
        _assert_optional_dependency(FloatTensorType, "skl2onnx")
        initial_types = [("float_input", FloatTensorType([None, feature_count]))]
        with _patched_hist_gradient_boosting_onnx_converter():
            return convert_sklearn(estimator, initial_types=initial_types, target_opset=target_opset)

    # Convert Standard Scikit-Learn Estimators
    if estimator_name not in ["XGBRegressor", "LGBMRegressor"]:
        _assert_optional_dependency(convert_sklearn, "skl2onnx")
        _assert_optional_dependency(FloatTensorType, "skl2onnx")
        if ELMRegressor is not None and isinstance(estimator, ELMRegressor):
            register_exact_elm_onnx_converter_if_needed()
        initial_types = [("float_input", FloatTensorType([None, feature_count]))]
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


def export_exact_family_python_and_onnx_bank(
    dataset_bundle: ExactPaperDatasetBundle,
    fitted_family_model_dictionary: dict[str, MultiOutputRegressor],
    training_config: dict[str, Any],
    output_directory: Path,
) -> dict[str, Any]:

    """Export one Python plus ONNX model bank per family and target when enabled.

    Args:
        dataset_bundle: Prepared paper-faithful train/test bundle.
        fitted_family_model_dictionary: Fitted family bank keyed by short family
            name.
        training_config: Effective exact-paper configuration.
        output_directory: Immutable validation artifact directory.

    Returns:
        Dictionary summarizing Python and ONNX export status, generated files,
        and comparison against the recovered ONNX release when configured.
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
    python_export_root = output_directory / EXACT_PYTHON_EXPORT_ROOTNAME
    onnx_export_root = output_directory / EXACT_ONNX_EXPORT_ROOTNAME
    python_export_root.mkdir(parents=True, exist_ok=True)
    onnx_export_root.mkdir(parents=True, exist_ok=True)

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
            "export_failure_mode": export_failure_mode,
            "enable_empty_svr_constant_surrogate": enable_empty_svr_constant_surrogate,
            "python_export_root": shared_training_infrastructure.format_project_relative_path(python_export_root),
            "python_exported_file_count": 0,
            "onnx_export_root": shared_training_infrastructure.format_project_relative_path(onnx_export_root),
            "onnx_exported_file_count": 0,
            "recovered_reference_root": shared_training_infrastructure.format_project_relative_path(recovered_reference_root),
            "recovered_reference_file_count": len(recovered_relative_path_set),
            "matched_reference_relative_paths": [],
            "missing_against_reference_relative_paths": sorted(recovered_relative_path_set),
            "extra_export_relative_paths": [],
            "family_exports": [],
        }

    # Export Each Family Target Estimator
    family_export_list: list[dict[str, Any]] = []
    exported_onnx_relative_path_set: set[str] = set()
    exported_python_relative_path_set: set[str] = set()
    for family_name in EXACT_FAMILY_ORDER:
        if family_name not in fitted_family_model_dictionary:
            continue

        # Resolve Output Family Folder
        family_export_start_time = time.perf_counter()
        wrapped_estimator = fitted_family_model_dictionary[family_name]
        family_python_directory = python_export_root / family_name
        family_onnx_directory = onnx_export_root / family_name
        family_python_directory.mkdir(parents=True, exist_ok=True)
        family_onnx_directory.mkdir(parents=True, exist_ok=True)
        estimator_name = EXACT_FAMILY_ESTIMATOR_NAME_MAP[family_name]
        exported_target_list: list[dict[str, Any]] = []
        emit_exact_paper_progress_log(
            "INFO",
            "Family Python+ONNX export started | "
            f"family={family_name} "
            f"targets={len(dataset_bundle.target_name_list)} "
            f"estimator={estimator_name}",
        )

        # Export Per-Target Estimator Files
        for target_index, target_name in enumerate(dataset_bundle.target_name_list):
            per_target_estimator = wrapped_estimator.estimators_[target_index]
            export_target_name = build_exact_target_export_name(target_name)
            python_export_filename = f"{estimator_name}_{export_target_name}.pkl"
            python_export_path = family_python_directory / python_export_filename
            onnx_export_filename = f"{estimator_name}_{export_target_name}.onnx"
            onnx_export_path = family_onnx_directory / onnx_export_filename

            # Mirror The Recovered Original Workflow By Persisting The Python Artifact First
            with python_export_path.open("wb") as output_file:
                pickle.dump(per_target_estimator, output_file)
            exported_python_relative_path = python_export_path.relative_to(python_export_root).as_posix()
            exported_python_relative_path_set.add(exported_python_relative_path)
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
                export_feature_count = resolve_exact_export_feature_count(
                    export_estimator,
                    fallback_feature_count=len(dataset_bundle.feature_name_list),
                )
                onnx_model = _convert_estimator_to_onnx(
                    export_estimator,
                    feature_count=export_feature_count,
                    estimator_name=export_estimator_name,
                    target_opset=target_opset,
                )
                with onnx_export_path.open("wb") as output_file:
                    output_file.write(onnx_model.SerializeToString())

                exported_onnx_relative_path = onnx_export_path.relative_to(onnx_export_root).as_posix()
                exported_onnx_relative_path_set.add(exported_onnx_relative_path)
                exported_target_list.append(
                    {
                        "target_name": target_name,
                        "export_target_name": export_target_name,
                        "python_export_path": shared_training_infrastructure.format_project_relative_path(python_export_path),
                        "python_file_size_bytes": int(python_export_path.stat().st_size),
                        "python_export_status": "exported",
                        "onnx_export_path": shared_training_infrastructure.format_project_relative_path(onnx_export_path),
                        "onnx_file_size_bytes": int(onnx_export_path.stat().st_size),
                        "onnx_export_status": "exported",
                        "surrogate_strategy": surrogate_strategy,
                        "export_estimator_name": export_estimator_name,
                    }
                )
            except Exception as export_error:  # pragma: no cover - exercised in real runtime
                exported_target_list.append(
                    {
                        "target_name": target_name,
                        "export_target_name": export_target_name,
                        "python_export_path": shared_training_infrastructure.format_project_relative_path(python_export_path),
                        "python_file_size_bytes": int(python_export_path.stat().st_size),
                        "python_export_status": "exported",
                        "onnx_export_path": shared_training_infrastructure.format_project_relative_path(onnx_export_path),
                        "onnx_file_size_bytes": 0,
                        "onnx_export_status": "failed",
                        "surrogate_strategy": "none",
                        "export_estimator_name": estimator_name,
                        "error_message": _build_compact_export_error_message(export_error),
                    }
                )
                emit_exact_paper_progress_log(
                    "WARN",
                    "Target ONNX export failed after Python export succeeded | "
                    f"family={family_name} "
                    f"target={target_name} "
                    f"error={_build_compact_export_error_message(export_error)}",
                )
                if export_failure_mode == "strict":
                    raise RuntimeError(
                        "Exact paper ONNX export failed | "
                        f"family={family_name} target={target_name}"
                    ) from export_error

        python_exported_target_count = int(
            sum(1 for entry in exported_target_list if entry["python_export_status"] == "exported")
        )
        onnx_exported_target_count = int(
            sum(1 for entry in exported_target_list if entry["onnx_export_status"] == "exported")
        )
        failed_onnx_target_count = int(
            sum(1 for entry in exported_target_list if entry["onnx_export_status"] == "failed")
        )
        family_export_list.append(
            {
                "family_name": family_name,
                "display_name": EXACT_FAMILY_DISPLAY_NAME_MAP[family_name],
                "estimator_name": estimator_name,
                "python_export_directory": shared_training_infrastructure.format_project_relative_path(family_python_directory),
                "onnx_export_directory": shared_training_infrastructure.format_project_relative_path(family_onnx_directory),
                "python_exported_target_count": python_exported_target_count,
                "onnx_exported_target_count": onnx_exported_target_count,
                "failed_onnx_target_count": failed_onnx_target_count,
                "exported_targets": exported_target_list,
            }
        )
        emit_exact_paper_progress_log(
            "DONE",
            "Family Python+ONNX export complete | "
            f"family={family_name} "
            f"elapsed={format_exact_elapsed_seconds(time.perf_counter() - family_export_start_time)} "
            f"python_exported={python_exported_target_count} "
            f"onnx_exported={onnx_exported_target_count} "
            f"onnx_failed={failed_onnx_target_count}",
        )

    # Compare Export Surface Against The Recovered ONNX Release
    matched_reference_relative_path_list = sorted(exported_onnx_relative_path_set.intersection(recovered_relative_path_set))
    missing_against_reference_relative_path_list = sorted(recovered_relative_path_set.difference(exported_onnx_relative_path_set))
    extra_export_relative_path_list = sorted(exported_onnx_relative_path_set.difference(recovered_relative_path_set))

    return {
        "enabled": True,
        "target_opset": target_opset,
        "export_failure_mode": export_failure_mode,
        "enable_empty_svr_constant_surrogate": enable_empty_svr_constant_surrogate,
        "python_export_root": shared_training_infrastructure.format_project_relative_path(python_export_root),
        "python_exported_file_count": len(exported_python_relative_path_set),
        "onnx_export_root": shared_training_infrastructure.format_project_relative_path(onnx_export_root),
        "onnx_exported_file_count": len(exported_onnx_relative_path_set),
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
    family_search_summary_dictionary: dict[str, dict[str, Any]],
    per_target_ranking_dictionary: dict[str, list[dict[str, Any]]],
    onnx_export_summary: dict[str, Any],
    model_bundle_path: Path,
) -> dict[str, Any]:

    """Build the canonical validation summary for one exact-paper run."""

    # Resolve Experiment And Dataset Identity
    experiment_identity = shared_training_infrastructure.resolve_experiment_identity(training_config)
    run_artifact_identity = shared_training_infrastructure.resolve_run_artifact_identity(training_config)
    winner_family_summary = family_summary_list[0]
    target_scope = resolve_exact_target_scope(training_config)
    search_settings = resolve_exact_paper_hyperparameter_search_settings(training_config)
    harmonic_order_list = sorted({
        parse_exact_target_name(target_name)[1]
        for target_name in dataset_bundle.target_name_list
    })
    target_kind_list = sorted({
        parse_exact_target_name(target_name)[0]
        for target_name in dataset_bundle.target_name_list
    })

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
    target_comparison_list = build_exact_paper_target_comparison_registry(target_winner_list)
    harmonic_comparison_list = build_exact_paper_harmonic_comparison_registry(target_comparison_list)
    numeric_target_comparison_list = build_exact_paper_numeric_target_comparison_registry(per_target_ranking_dictionary)
    numeric_harmonic_summary_list = build_exact_paper_numeric_harmonic_summary(numeric_target_comparison_list)

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
        "training_strategy": {
            "hyperparameter_search_mode": search_settings["mode"],
            "grid_search_n_jobs": int(search_settings["grid_search_n_jobs"]),
            "grid_search_verbose": int(search_settings["grid_search_verbose"]),
            "grid_search_pre_dispatch": search_settings["grid_search_pre_dispatch"],
            "family_search_summary": family_search_summary_dictionary,
        },
        "paper_alignment": {
            "input_feature_schema": ["rpm", "deg", "tor"],
            "target_schema_kind": "_".join(target_kind_list) + "_exact_paper",
            "target_scope_mode": target_scope["mode"],
            "include_phase_zero": bool(target_scope["include_phase_zero"]),
            "harmonic_order_list": harmonic_order_list,
            "harmonic_order_filter": target_scope["harmonic_order_filter"],
            "enabled_family_list": resolve_enabled_family_list(training_config),
            "recovered_reference_onnx_root": training_config["paths"].get("exact_onnx_reference_root", ""),
            "harmonic_expected_family_map": EXACT_PAPER_HARMONIC_EXPECTED_FAMILY_MAP,
            "paper_table_replication_scope": (
                "tables_3_4_5_6_numeric_targets_serialized"
                if target_scope["mode"] == "all"
                else f"{target_scope['mode']}_partial_table_replication"
            ),
        },
        "dependency_versions": resolve_dependency_version_dictionary(),
        "winner_summary": {
            "winning_family": winner_family_summary["family_name"],
            "winning_display_name": winner_family_summary["display_name"],
            "winning_estimator_name": winner_family_summary["estimator_name"],
            "winning_mean_component_mape_percent": float(winner_family_summary["mean_component_mape_percent"]),
            "winning_mean_component_mae": float(winner_family_summary["mean_component_mae"]),
            "winning_mean_component_rmse": float(winner_family_summary["mean_component_rmse"]),
            "winning_search_mode": family_search_summary_dictionary[winner_family_summary["family_name"]]["search_mode"],
            "winning_best_params": family_search_summary_dictionary[winner_family_summary["family_name"]]["best_params"],
        },
        "family_ranking": family_summary_list,
        "target_winner_registry": target_winner_list,
        "paper_target_comparison_registry": target_comparison_list,
        "paper_harmonic_comparison_registry": harmonic_comparison_list,
        "paper_numeric_target_comparison_registry": numeric_target_comparison_list,
        "paper_numeric_harmonic_summary": numeric_harmonic_summary_list,
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
    validation_report_root = (
        shared_training_infrastructure.resolve_runtime_project_path()
        / "doc"
        / "reports"
        / "analysis"
        / "validation_checks"
    )
    validation_report_filename = shared_training_infrastructure.build_safe_validation_report_filename(
        report_root=validation_report_root,
        timestamp_string=timestamp_string,
        model_family=experiment_identity.model_family,
        output_run_name=output_run_name,
        report_suffix="exact_paper_model_bank_report.md",
    )
    validation_report_path = validation_report_root / validation_report_filename
    validation_report_path.parent.mkdir(parents=True, exist_ok=True)
    return validation_report_path


def build_exact_model_report_markdown(validation_summary: dict[str, Any]) -> str:

    """Build the human-readable Markdown report for one exact-paper run."""

    # Resolve Summary Sections
    experiment_dictionary = validation_summary["experiment"]
    dataset_dictionary = validation_summary["dataset"]
    training_strategy_dictionary = validation_summary["training_strategy"]
    paper_alignment_dictionary = validation_summary["paper_alignment"]
    dependency_version_dictionary = validation_summary["dependency_versions"]
    winner_summary = validation_summary["winner_summary"]
    family_ranking = validation_summary["family_ranking"]
    target_winner_registry = validation_summary["target_winner_registry"]
    paper_target_comparison_registry = validation_summary["paper_target_comparison_registry"]
    paper_harmonic_comparison_registry = validation_summary["paper_harmonic_comparison_registry"]
    paper_numeric_target_comparison_registry = validation_summary["paper_numeric_target_comparison_registry"]
    paper_numeric_harmonic_summary = validation_summary["paper_numeric_harmonic_summary"]
    onnx_export_summary = validation_summary["onnx_export_summary"]
    family_search_summary_dictionary = training_strategy_dictionary["family_search_summary"]
    winner_historical_protocol_summary = family_search_summary_dictionary[
        winner_summary["winning_family"]
    ].get("historical_protocol_summary")
    winner_best_parameter_source = family_search_summary_dictionary[
        winner_summary["winning_family"]
    ].get("best_parameter_source")
    winner_workflow_stage = family_search_summary_dictionary[
        winner_summary["winning_family"]
    ].get("workflow_stage")

    # Build Numeric Comparison Lookups
    numeric_target_lookup = {
        str(entry["target_name"]): entry
        for entry in paper_numeric_target_comparison_registry
    }
    target_scope_mode = str(paper_alignment_dictionary.get("target_scope_mode", "all"))
    include_phase_zero = bool(paper_alignment_dictionary.get("include_phase_zero", True))

    # Build Family Ranking Rows
    family_row_list: list[str] = []
    for ranking_index, family_entry in enumerate(family_ranking, start=1):
        family_search_entry = family_search_summary_dictionary[family_entry["family_name"]]
        family_row_list.append(
            f"| {ranking_index} | `{family_entry['family_name']}` | "
            f"`{family_entry['estimator_name']}` | "
            f"`{family_search_entry['search_mode']}` | "
            f"{family_entry['mean_component_mape_percent']:.3f} | "
            f"{family_entry['mean_component_mae']:.6f} | "
            f"{family_entry['mean_component_rmse']:.6f} |"
        )

    # Build Family Search Rows
    family_search_row_list: list[str] = []
    for family_name in EXACT_FAMILY_ORDER:
        if family_name not in family_search_summary_dictionary:
            continue
        family_search_entry = family_search_summary_dictionary[family_name]
        best_score_text = (
            f"{float(family_search_entry['best_score']):.6f}"
            if family_search_entry["best_score"] is not None
            else "-"
        )
        best_params_text = (
            f"`{family_search_entry['best_params']}`"
            if family_search_entry["best_params"] is not None
            else "-"
        )
        family_search_row_list.append(
            f"| `{family_name}` | "
            f"`{family_search_entry['search_mode']}` | "
            f"{family_search_entry['grid_search_cv'] if family_search_entry['grid_search_cv'] is not None else '-'} | "
            f"{best_score_text} | "
            f"{best_params_text} |"
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

    # Build Paper Comparison Rows
    paper_target_row_list: list[str] = []
    for target_comparison_entry in paper_target_comparison_registry:
        paper_target_row_list.append(
            f"| `{target_comparison_entry['target_name']}` | "
            f"`{target_comparison_entry['paper_expected_family_text']}` | "
            f"`{target_comparison_entry['repository_winning_family']}` | "
            f"{target_comparison_entry['repository_winning_mape_percent']:.3f} | "
            f"`{target_comparison_entry['family_direction_status']}` |"
        )
    paper_harmonic_row_list: list[str] = []
    for harmonic_comparison_entry in paper_harmonic_comparison_registry:
        amplitude_winning_family = harmonic_comparison_entry["amplitude_winning_family"] or "-"
        phase_winning_family = harmonic_comparison_entry["phase_winning_family"] or "-"
        paper_harmonic_row_list.append(
            f"| `{harmonic_comparison_entry['harmonic_order']}` | "
            f"`{harmonic_comparison_entry['paper_expected_family_text']}` | "
            f"`{amplitude_winning_family}` | "
            f"`{phase_winning_family}` | "
            f"{harmonic_comparison_entry['matching_target_count']}/{harmonic_comparison_entry['repository_target_count']} | "
            f"`{harmonic_comparison_entry['harmonic_match_status']}` |"
        )

    # Build Canonical Table 3 Comparison Rows
    table3_row_list: list[str] = []
    for paper_family_name in EXACT_PAPER_REFERENCE_FAMILY_ORDER:
        paper_display_family_name = "SVM" if paper_family_name == "SVR" else paper_family_name
        paper_metric_dictionary = EXACT_PAPER_TABLE3_RMSE_AMPLITUDE_MAP[paper_display_family_name]
        metric_cell_list = [format_exact_paper_metric_value(paper_metric_dictionary[harmonic_order]) for harmonic_order in EXACT_PAPER_TABLE3_HARMONIC_ORDER_LIST]
        table3_row_list.append(f"| `{paper_display_family_name}` | " + " | ".join(metric_cell_list) + " |")
    table3_repo_family_row = []
    table3_repo_rmse_row = []
    table3_paper_best_family_row = []
    table3_paper_target_row = []
    table3_gap_row = []
    table3_status_row = []
    for harmonic_order in EXACT_PAPER_TABLE3_HARMONIC_ORDER_LIST:
        target_name = f"fft_y_Fw_filtered_ampl_{harmonic_order}"
        numeric_entry = numeric_target_lookup.get(target_name)
        table3_repo_family_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["repository_best_rmse_family"]))
        table3_repo_rmse_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["repository_best_rmse_value"]))
        table3_paper_best_family_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["paper_best_rmse_family"]))
        table3_paper_target_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["paper_best_rmse_value"]))
        table3_gap_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["rmse_gap_vs_paper_best"]))
        table3_status_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["rmse_target_status"]))

    # Build Canonical Table 4 Comparison Rows
    table4_row_list: list[str] = []
    for paper_family_name in EXACT_PAPER_REFERENCE_FAMILY_ORDER:
        paper_display_family_name = "SVM" if paper_family_name == "SVR" else paper_family_name
        paper_metric_dictionary = EXACT_PAPER_TABLE4_MAE_PHASE_MAP[paper_display_family_name]
        metric_cell_list = [format_exact_paper_metric_value(paper_metric_dictionary[harmonic_order]) for harmonic_order in EXACT_PAPER_TABLE45_HARMONIC_ORDER_LIST]
        table4_row_list.append(f"| `{paper_display_family_name}` | " + " | ".join(metric_cell_list) + " |")
    table4_repo_family_row = []
    table4_repo_mae_row = []
    table4_paper_best_family_row = []
    table4_paper_target_row = []
    table4_gap_row = []
    table4_status_row = []
    for harmonic_order in EXACT_PAPER_TABLE45_HARMONIC_ORDER_LIST:
        target_name = f"fft_y_Fw_filtered_phase_{harmonic_order}"
        numeric_entry = numeric_target_lookup.get(target_name)
        table4_repo_family_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["repository_best_mae_family"]))
        table4_repo_mae_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["repository_best_mae_value"]))
        table4_paper_best_family_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["paper_best_mae_family"]))
        table4_paper_target_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["paper_best_mae_value"]))
        table4_gap_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["mae_gap_vs_paper_best"]))
        table4_status_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["mae_target_status"]))

    # Build Canonical Table 5 Comparison Rows
    table5_row_list: list[str] = []
    for paper_family_name in EXACT_PAPER_REFERENCE_FAMILY_ORDER:
        paper_display_family_name = "SVM" if paper_family_name == "SVR" else paper_family_name
        paper_metric_dictionary = EXACT_PAPER_TABLE5_RMSE_PHASE_MAP[paper_display_family_name]
        metric_cell_list = [format_exact_paper_metric_value(paper_metric_dictionary[harmonic_order]) for harmonic_order in EXACT_PAPER_TABLE45_HARMONIC_ORDER_LIST]
        table5_row_list.append(f"| `{paper_display_family_name}` | " + " | ".join(metric_cell_list) + " |")
    table5_repo_family_row = []
    table5_repo_rmse_row = []
    table5_paper_best_family_row = []
    table5_paper_target_row = []
    table5_gap_row = []
    table5_status_row = []
    for harmonic_order in EXACT_PAPER_TABLE45_HARMONIC_ORDER_LIST:
        target_name = f"fft_y_Fw_filtered_phase_{harmonic_order}"
        numeric_entry = numeric_target_lookup.get(target_name)
        table5_repo_family_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["repository_best_rmse_family"]))
        table5_repo_rmse_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["repository_best_rmse_value"]))
        table5_paper_best_family_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["paper_best_rmse_family"]))
        table5_paper_target_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["paper_best_rmse_value"]))
        table5_gap_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["rmse_gap_vs_paper_best"]))
        table5_status_row.append(format_exact_paper_report_value(None if numeric_entry is None else numeric_entry["rmse_target_status"]))

    # Build Canonical Table 6 Comparison Rows
    table6_row_list: list[str] = []
    for harmonic_summary_entry in paper_numeric_harmonic_summary:
        table6_row_list.append(
            f"| `{harmonic_summary_entry['harmonic_order']}` | "
            f"`{harmonic_summary_entry['amplitude_paper_family'] or '-'}` | "
            f"`{harmonic_summary_entry['amplitude_repository_family'] or '-'}` | "
            f"`{harmonic_summary_entry['amplitude_rmse_status'] or '-'}` | "
            f"`{harmonic_summary_entry['phase_paper_family'] or '-'}` | "
            f"`{harmonic_summary_entry['phase_repository_mae_family'] or '-'}` | "
            f"`{harmonic_summary_entry['phase_repository_rmse_family'] or '-'}` | "
            f"`{harmonic_summary_entry['phase_mae_status'] or '-'}` | "
            f"`{harmonic_summary_entry['phase_rmse_status'] or '-'}` | "
            f"`{harmonic_summary_entry['harmonic_numeric_status']}` |"
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
            family_entry["failed_onnx_target_count"]
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
        f"- target scope mode: `{target_scope_mode}`;",
        "",
        "## Dataset Scope",
        "",
        f"- filtered row count: `{dataset_dictionary['filtered_row_count']}`;",
        f"- feature schema: `{', '.join(dataset_dictionary['feature_name_list'])}`;",
        f"- target count: `{dataset_dictionary['target_count']}`;",
        f"- target schema kind: `{paper_alignment_dictionary['target_schema_kind']}`;",
        f"- included phase `0`: `{include_phase_zero}`;",
        f"- train rows: `{dataset_dictionary['train_row_count']}`;",
        f"- test rows: `{dataset_dictionary['test_row_count']}`;",
        f"- maximum `deg` filter: `{dataset_dictionary['maximum_deg']}`;",
        "",
        "## Winner Summary",
        "",
        f"- winning family: `{winner_summary['winning_family']}`;",
        f"- winning estimator: `{winner_summary['winning_estimator_name']}`;",
        f"- winning search mode: `{winner_summary['winning_search_mode']}`;",
        f"- winning best params: `{winner_summary['winning_best_params']}`;",
        f"- winning mean component MAPE: `{winner_summary['winning_mean_component_mape_percent']:.3f}%`;",
        f"- winning mean component MAE: `{winner_summary['winning_mean_component_mae']:.6f}`;",
        f"- winning mean component RMSE: `{winner_summary['winning_mean_component_rmse']:.6f}`;",
        "",
        "## Training Strategy",
        "",
        f"- hyperparameter search mode: `{training_strategy_dictionary['hyperparameter_search_mode']}`;",
        f"- grid-search `n_jobs`: `{training_strategy_dictionary['grid_search_n_jobs']}`;",
        f"- grid-search `pre_dispatch`: `{training_strategy_dictionary['grid_search_pre_dispatch']}`;",
        f"- workflow stage: `{winner_workflow_stage}`;",
        f"- best-parameter source: `{winner_best_parameter_source}`;",
        f"- historical wrapper `cross_validate(...)` replay: `{bool(winner_historical_protocol_summary)}`;",
        "",
        "### Family Search Summary",
        "",
        "| Family | Search Mode | CV Folds | Best Score | Best Params |",
        "| --- | --- | ---: | ---: | --- |",
        *family_search_row_list,
        "",
        "## Family Ranking",
        "",
        "| Rank | Family | Estimator | Search Mode | Mean Component MAPE [%] | Mean Component MAE | Mean Component RMSE |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: |",
        *family_row_list,
        "",
        "## Target-Winner Registry",
        "",
        "| Target | Winning Family | Estimator | MAPE [%] | MAE | RMSE |",
        "| --- | --- | --- | ---: | ---: | ---: |",
        *target_winner_row_list,
        "",
        "## Paper-Target Comparison",
        "",
        "This section serializes the current `paper vs repository` comparison",
        "for each exact-paper target at the family-direction level. The stricter",
        "numeric table replication is reported in the canonical table sections",
        "below.",
        "",
        "| Target | Paper Expected Family | Repository Winner | Repo MAPE [%] | Family Direction Status |",
        "| --- | --- | --- | ---: | --- |",
        *paper_target_row_list,
        "",
        "## Paper-Harmonic Comparison",
        "",
        "This section collapses the amplitude and phase target evidence into one",
        "harmonic-facing status so `RCIM Model-Bank Reproduction` closure can later be tied to a",
        "single inspectable harmonic table.",
        "",
        "| Harmonic | Paper Expected Family | Ampl Winner | Phase Winner | Matching Targets | Harmonic Status |",
        "| ---: | --- | --- | --- | ---: | --- |",
        *paper_harmonic_row_list,
        "",
        "## Canonical Table 3 Comparison",
        "",
        "This table mirrors paper Table 3 for amplitude RMSE and adds the",
        "repository best-achieved RMSE per harmonic together with the remaining",
        "numeric gap against the paper target.",
        "",
        "| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        *table3_row_list,
        f"| `Repo Best Family` | {' | '.join(table3_repo_family_row)} |",
        f"| `Repo Best RMSE` | {' | '.join(table3_repo_rmse_row)} |",
        f"| `Paper Best Family` | {' | '.join(table3_paper_best_family_row)} |",
        f"| `Paper Target RMSE` | {' | '.join(table3_paper_target_row)} |",
        f"| `Gap Vs Paper` | {' | '.join(table3_gap_row)} |",
        f"| `Status` | {' | '.join(table3_status_row)} |",
        "",
        "## Canonical Table 4 Comparison",
        "",
        "This table mirrors paper Table 4 for phase MAE and adds the repository",
        "best-achieved MAE per harmonic together with the remaining numeric gap",
        "against the paper target.",
        "",
        "| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        *table4_row_list,
        f"| `Repo Best Family` | {' | '.join(table4_repo_family_row)} |",
        f"| `Repo Best MAE` | {' | '.join(table4_repo_mae_row)} |",
        f"| `Paper Best Family` | {' | '.join(table4_paper_best_family_row)} |",
        f"| `Paper Target MAE` | {' | '.join(table4_paper_target_row)} |",
        f"| `Gap Vs Paper` | {' | '.join(table4_gap_row)} |",
        f"| `Status` | {' | '.join(table4_status_row)} |",
        "",
        "## Canonical Table 5 Comparison",
        "",
        "This table mirrors paper Table 5 for phase RMSE and adds the repository",
        "best-achieved RMSE per harmonic together with the remaining numeric gap",
        "against the paper target.",
        "",
        "| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        *table5_row_list,
        f"| `Repo Best Family` | {' | '.join(table5_repo_family_row)} |",
        f"| `Repo Best RMSE` | {' | '.join(table5_repo_rmse_row)} |",
        f"| `Paper Best Family` | {' | '.join(table5_paper_best_family_row)} |",
        f"| `Paper Target RMSE` | {' | '.join(table5_paper_target_row)} |",
        f"| `Gap Vs Paper` | {' | '.join(table5_gap_row)} |",
        f"| `Status` | {' | '.join(table5_status_row)} |",
        "",
        "## Canonical Table 6 Comparison",
        "",
        "This table compares the paper-selected top-performing models from Table 6",
        "against the repository best families measured on the current exact-paper",
        "validation split.",
        "",
        "| `k` | Paper `A*_k` | Repo Best Ampl RMSE Family | Ampl RMSE Status | Paper `phi*_k` | Repo Best Phase MAE Family | Repo Best Phase RMSE Family | Phase MAE Status | Phase RMSE Status | Harmonic Status |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        *table6_row_list,
        "",
        "## Python And ONNX Export Surface",
        "",
        f"- export enabled: `{onnx_export_summary['enabled']}`;",
        f"- python export root: `{onnx_export_summary['python_export_root']}`;",
        f"- python exported file count: `{onnx_export_summary['python_exported_file_count']}`;",
        f"- ONNX export root: `{onnx_export_summary['onnx_export_root']}`;",
        f"- ONNX exported file count: `{onnx_export_summary['onnx_exported_file_count']}`;",
        f"- export failure mode: `{onnx_export_summary['export_failure_mode']}`;",
        f"- recovered reference file count: `{onnx_export_summary['recovered_reference_file_count']}`;",
        f"- matched relative paths: `{matched_reference_count}`;",
        f"- missing against recovered ONNX reference: `{missing_reference_count}`;",
        f"- extra exported ONNX relative paths: `{extra_export_count}`;",
        f"- failed ONNX exports: `{failed_export_count}`;",
        f"- surrogate ONNX exports: `{surrogate_export_count}`;",
        "",
        "## Runtime Dependencies",
        "",
        "| Dependency | Version |",
        "| --- | --- |",
        *dependency_row_list,
        "",
        "## Interpretation",
        "",
        "This validation run is the strict paper-faithful branch of `RCIM Model-Bank Reproduction`.",
        "Its role is to reproduce the original RCIM family bank with the exact",
        "recovered input schema, target schema, and export surface before any",
        "repository-specific simplification or target-wise winner assembly.",
        "",
        "At the current repository state, the workflow now serializes the numeric",
        "targets from paper Tables 3, 4, 5, and the selected-model targets from",
        "Table 6. The training path can also reproduce the recovered paper-side",
        "`GridSearchCV` strategy instead of only fitting the recovered base",
        "estimators directly. The repository can therefore show both the paper thresholds and",
        "the current exact-paper results side by side. `RCIM Model-Bank Reproduction` still remains",
        "open until those gaps are actually closed on the repository side.",
        "",
    ])
