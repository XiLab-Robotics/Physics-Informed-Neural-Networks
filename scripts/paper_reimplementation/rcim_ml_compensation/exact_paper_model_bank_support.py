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
}
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
            "export_failure_mode": export_failure_mode,
            "enable_empty_svr_constant_surrogate": enable_empty_svr_constant_surrogate,
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
        "paper_alignment": {
            "input_feature_schema": ["rpm", "deg", "tor"],
            "target_schema_kind": "ampl_phase_exact_paper",
            "harmonic_order_list": [0, 1, 3, 39, 40, 78, 81, 156, 162, 240],
            "enabled_family_list": resolve_enabled_family_list(training_config),
            "recovered_reference_onnx_root": training_config["paths"].get("exact_onnx_reference_root", ""),
            "harmonic_expected_family_map": EXACT_PAPER_HARMONIC_EXPECTED_FAMILY_MAP,
            "paper_table_replication_scope": "tables_3_4_5_6_numeric_targets_serialized",
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
    paper_target_comparison_registry = validation_summary["paper_target_comparison_registry"]
    paper_harmonic_comparison_registry = validation_summary["paper_harmonic_comparison_registry"]
    paper_numeric_target_comparison_registry = validation_summary["paper_numeric_target_comparison_registry"]
    paper_numeric_harmonic_summary = validation_summary["paper_numeric_harmonic_summary"]
    onnx_export_summary = validation_summary["onnx_export_summary"]

    # Build Numeric Comparison Lookups
    numeric_target_lookup = {
        str(entry["target_name"]): entry
        for entry in paper_numeric_target_comparison_registry
    }

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
    for paper_family_name in EXACT_FAMILY_ORDER:
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
        numeric_entry = numeric_target_lookup[target_name]
        table3_repo_family_row.append(f"`{numeric_entry['repository_best_rmse_family']}`")
        table3_repo_rmse_row.append(format_exact_paper_metric_value(numeric_entry["repository_best_rmse_value"]))
        table3_paper_best_family_row.append(f"`{numeric_entry['paper_best_rmse_family']}`")
        table3_paper_target_row.append(format_exact_paper_metric_value(numeric_entry["paper_best_rmse_value"]))
        table3_gap_row.append(format_exact_paper_metric_value(numeric_entry["rmse_gap_vs_paper_best"]))
        table3_status_row.append(f"`{numeric_entry['rmse_target_status']}`")

    # Build Canonical Table 4 Comparison Rows
    table4_row_list: list[str] = []
    for paper_family_name in EXACT_FAMILY_ORDER:
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
        numeric_entry = numeric_target_lookup[target_name]
        table4_repo_family_row.append(f"`{numeric_entry['repository_best_mae_family']}`")
        table4_repo_mae_row.append(format_exact_paper_metric_value(numeric_entry["repository_best_mae_value"]))
        table4_paper_best_family_row.append(f"`{numeric_entry['paper_best_mae_family']}`")
        table4_paper_target_row.append(format_exact_paper_metric_value(numeric_entry["paper_best_mae_value"]))
        table4_gap_row.append(format_exact_paper_metric_value(numeric_entry["mae_gap_vs_paper_best"]))
        table4_status_row.append(f"`{numeric_entry['mae_target_status']}`")

    # Build Canonical Table 5 Comparison Rows
    table5_row_list: list[str] = []
    for paper_family_name in EXACT_FAMILY_ORDER:
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
        numeric_entry = numeric_target_lookup[target_name]
        table5_repo_family_row.append(f"`{numeric_entry['repository_best_rmse_family']}`")
        table5_repo_rmse_row.append(format_exact_paper_metric_value(numeric_entry["repository_best_rmse_value"]))
        table5_paper_best_family_row.append(f"`{numeric_entry['paper_best_rmse_family']}`")
        table5_paper_target_row.append(format_exact_paper_metric_value(numeric_entry["paper_best_rmse_value"]))
        table5_gap_row.append(format_exact_paper_metric_value(numeric_entry["rmse_gap_vs_paper_best"]))
        table5_status_row.append(f"`{numeric_entry['rmse_target_status']}`")

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
        "harmonic-facing status so `Track 1` closure can later be tied to a",
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
        "At the current repository state, the workflow now serializes the numeric",
        "targets from paper Tables 3, 4, 5, and the selected-model targets from",
        "Table 6. The repository can therefore show both the paper thresholds and",
        "the current exact-paper results side by side. `Track 1` still remains",
        "open until those gaps are actually closed on the repository side.",
        "",
    ])
