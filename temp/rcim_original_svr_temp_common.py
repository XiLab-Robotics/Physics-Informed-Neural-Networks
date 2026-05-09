""" Temporary diagnostics for the recovered-original RCIM SVR branch. """

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVR
from sklearn.svm import SVR

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts.paper_reimplementation.rcim_ml_compensation.recovered_original_workflow.workflow_runtime import REFERENCE_ROOT
from scripts.paper_reimplementation.rcim_ml_compensation.recovered_original_workflow.workflow_runtime import normalize_direction

TEMP_OUTPUT_ROOT = Path(__file__).resolve().parent / "output"
TARGET_COLUMN_COUNT = 20


class TimedSVR(SVR):

    """ Temporary SVR wrapper that prints one timing line per base fit. """

    FIT_SEQUENCE = 0

    def fit(self, X, y, sample_weight=None):

        """ Time one underlying libsvm fit call. """

        TimedSVR.FIT_SEQUENCE += 1
        fit_index = TimedSVR.FIT_SEQUENCE
        print(
            "[TEMP_FIT_START] "
            f"BaseFit {fit_index} | Kernel {self.kernel} | C {self.C} | "
            f"Epsilon {self.epsilon} | Gamma {self.gamma} | Samples {len(X)}",
            flush=True,
        )
        start_time = time.perf_counter()
        fitted_model = super().fit(X, y, sample_weight=sample_weight)
        elapsed_seconds = time.perf_counter() - start_time
        print(
            "[TEMP_FIT_DONE] "
            f"BaseFit {fit_index} | Kernel {self.kernel} | C {self.C} | "
            f"Epsilon {self.epsilon} | Gamma {self.gamma} | "
            f"ElapsedSeconds {elapsed_seconds:.3f}",
            flush=True,
        )
        return fitted_model


class TimedLinearSVR(LinearSVR):

    """ Temporary LinearSVR wrapper that prints one timing line per base fit. """

    FIT_SEQUENCE = 0

    def fit(self, X, y, sample_weight=None):

        """ Time one underlying liblinear fit call. """

        TimedLinearSVR.FIT_SEQUENCE += 1
        fit_index = TimedLinearSVR.FIT_SEQUENCE
        print(
            "[TEMP_FIT_START] "
            f"BaseFit {fit_index} | Model LinearSVR | C {self.C} | "
            f"Epsilon {self.epsilon} | Tol {self.tol} | MaxIter {self.max_iter} | "
            f"Samples {len(X)}",
            flush=True,
        )
        start_time = time.perf_counter()
        fitted_model = super().fit(X, y, sample_weight=sample_weight)
        elapsed_seconds = time.perf_counter() - start_time
        print(
            "[TEMP_FIT_DONE] "
            f"BaseFit {fit_index} | Model LinearSVR | C {self.C} | "
            f"Epsilon {self.epsilon} | Tol {self.tol} | MaxIter {self.max_iter} | "
            f"ElapsedSeconds {elapsed_seconds:.3f}",
            flush=True,
        )
        return fitted_model


def build_hybrid_rbf_plus_linear_svr_param_grid() -> list[dict[str, object]]:

    """ Build one temporary mixed search with SVR RBF and scaled LinearSVR. """

    return [
        {
            "estimator": [TimedSVR(kernel="rbf")],
            "estimator__C": [1],
            "estimator__epsilon": [1e-4, 1e-6],
            "estimator__gamma": [1.1e-6],
        },
        {
            "estimator": [
                Pipeline(
                    steps=[
                        ("scaler", StandardScaler()),
                        (
                            "model",
                            TimedLinearSVR(
                                C=1.0,
                                epsilon=0.0,
                                tol=1e-4,
                                max_iter=5000,
                                random_state=0,
                            ),
                        ),
                    ]
                )
            ],
            "estimator__model__C": [1],
            "estimator__model__epsilon": [0.0],
            "estimator__model__tol": [1e-4],
            "estimator__model__max_iter": [5000],
        },
    ]


def parse_float_csv(csv_payload: str) -> list[float]:

    """ Parse one comma-separated float list for temporary CLI knobs. """

    return [float(token.strip()) for token in csv_payload.split(",") if token.strip()]


def parse_int_csv(csv_payload: str) -> list[int]:

    """ Parse one comma-separated integer list for temporary CLI knobs. """

    return [int(token.strip()) for token in csv_payload.split(",") if token.strip()]


def build_custom_hybrid_param_grid(
    rbf_c_values: list[float],
    rbf_epsilon_values: list[float],
    rbf_gamma_values: list[float],
    linear_c_values: list[float],
    linear_epsilon_values: list[float],
    linear_tol_values: list[float],
    linear_max_iter_values: list[int],
) -> list[dict[str, object]]:

    """ Build one wider temporary hybrid search grid. """

    return [
        {
            "estimator": [TimedSVR(kernel="rbf")],
            "estimator__C": rbf_c_values,
            "estimator__epsilon": rbf_epsilon_values,
            "estimator__gamma": rbf_gamma_values,
        },
        {
            "estimator": [
                Pipeline(
                    steps=[
                        ("scaler", StandardScaler()),
                        (
                            "model",
                            TimedLinearSVR(
                                random_state=0,
                            ),
                        ),
                    ]
                )
            ],
            "estimator__model__C": linear_c_values,
            "estimator__model__epsilon": linear_epsilon_values,
            "estimator__model__tol": linear_tol_values,
            "estimator__model__max_iter": linear_max_iter_values,
        },
    ]


@dataclass
class SearchInputs:

    """ One resolved dataset surface for the temporary probes. """

    dataframe_path: Path
    direction_code: str
    direction_label: str
    feature_dataframe: pd.DataFrame
    target_dataframe: pd.DataFrame


def build_shared_argument_parser(description: str) -> argparse.ArgumentParser:

    """ Build one common parser for the temporary diagnostic scripts. """

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--direction", default="backward", help="Direction to test: forward/Fw or backward/Bw.")
    parser.add_argument("--dataframe-path", type=Path, default=None, help="Optional dataframe CSV path.")
    parser.add_argument("--test-size", type=float, default=0.20, help="Held-out split fraction copied from the workflow.")
    parser.add_argument("--cv-folds", type=int, default=5, help="GridSearchCV fold count for temporary probes.")
    parser.add_argument("--n-jobs", type=int, default=1, help="GridSearchCV n_jobs value for temporary probes.")
    parser.add_argument("--verbose", type=int, default=10, help="GridSearchCV verbose value for temporary probes.")
    parser.add_argument("--output-json", type=Path, default=None, help="Optional JSON summary output path.")
    return parser


def ensure_temp_output_root() -> Path:

    """ Ensure the temporary output root exists. """

    TEMP_OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    return TEMP_OUTPUT_ROOT


def resolve_dataframe_inputs(direction: str, dataframe_path: Path | None) -> SearchInputs:

    """ Load the same dataframe surface used by the canonical workflow. """

    direction_code, direction_label = normalize_direction(direction)
    resolved_dataframe_path = (dataframe_path or (REFERENCE_ROOT / f"dataFrame_prediction_{direction_code}_v14_newFreq.csv")).resolve()
    dataframe = pd.read_csv(resolved_dataframe_path, sep=";", decimal=",", index_col=[0])
    dataframe.reset_index(inplace=True)
    feature_dataframe = dataframe[["rpm", "deg", "tor"]]
    target_column_list = [
        column_name
        for column_name in dataframe.columns
        if "ampl" in column_name or "phase" in column_name
    ]
    target_dataframe = dataframe[target_column_list]
    return SearchInputs(
        dataframe_path=resolved_dataframe_path,
        direction_code=direction_code,
        direction_label=direction_label,
        feature_dataframe=feature_dataframe,
        target_dataframe=target_dataframe,
    )


def build_tiny_mixed_param_grid() -> list[dict[str, object]]:

    """ Build a tiny explicit mixed RBF plus linear search grid. """

    return [
        {
            "estimator__kernel": ["rbf"],
            "estimator__C": [1],
            "estimator__epsilon": [1e-4, 1e-6],
            "estimator__gamma": [1.1e-6],
        },
        {
            "estimator__kernel": ["linear"],
            "estimator__C": [1],
            "estimator__epsilon": [1e-4, 1e-6],
            "estimator__gamma": [1.1e-6],
        },
    ]


def build_original_svr_param_grid() -> dict[str, list[object]]:

    """ Build the canonical recovered-original SVR retune grid. """

    return {
        "estimator__kernel": ["rbf", "linear"],
        "estimator__C": [1, 2, 3, 5, 6, 7],
        "estimator__epsilon": [1e-4, 1e-5, 1e-6, 1e-7],
        "estimator__gamma": [1.1e-6],
    }


def build_prefixed_candidate_list(parameter_grid: dict[str, list[object]], kernel_name: str, candidate_count: int) -> list[dict[str, object]]:

    """ Select the first N candidates for one kernel from the canonical grid. """

    filtered_candidate_list = [
        candidate
        for candidate in ParameterGrid(parameter_grid)
        if candidate["estimator__kernel"] == kernel_name
    ]
    return [
        {parameter_name: [parameter_value] for parameter_name, parameter_value in candidate.items()}
        for candidate in filtered_candidate_list[:candidate_count]
    ]


def run_multioutput_svr_search(
    inputs: SearchInputs,
    parameter_grid: list[dict[str, object]] | dict[str, list[object]],
    test_size: float,
    cv_folds: int,
    n_jobs: int,
    verbose: int,
) -> dict[str, object]:

    """ Run one temporary MultiOutputRegressor SVR grid search. """

    TimedSVR.FIT_SEQUENCE = 0
    X_train, _, y_train, _ = train_test_split(
        inputs.feature_dataframe,
        inputs.target_dataframe,
        test_size=test_size,
        random_state=0,
    )
    search = GridSearchCV(
        MultiOutputRegressor(TimedSVR()),
        parameter_grid,
        cv=cv_folds,
        n_jobs=n_jobs,
        verbose=verbose,
    )
    candidate_count = len(ParameterGrid(parameter_grid))
    expected_base_fit_count = TARGET_COLUMN_COUNT * ((candidate_count * cv_folds) + 1)
    print(
        "[TEMP_INFO] "
        f"Direction {inputs.direction_label} | Dataframe {inputs.dataframe_path} | "
        f"Samples {len(inputs.feature_dataframe)} | Train {len(X_train)} | "
        f"Targets {inputs.target_dataframe.shape[1]} | Candidates {candidate_count} | "
        f"CV {cv_folds} | ExpectedBaseFits {expected_base_fit_count} | NJobs {n_jobs}",
        flush=True,
    )
    print(f"[TEMP_INFO] ParameterGrid {list(ParameterGrid(parameter_grid))}", flush=True)
    start_time = time.perf_counter()
    search.fit(X_train, y_train)
    elapsed_seconds = time.perf_counter() - start_time
    return {
        "direction": inputs.direction_label,
        "dataframe_path": str(inputs.dataframe_path),
        "candidate_count": candidate_count,
        "cv_folds": cv_folds,
        "n_jobs": n_jobs,
        "expected_base_fit_count": expected_base_fit_count,
        "observed_base_fit_count": TimedSVR.FIT_SEQUENCE,
        "elapsed_seconds": elapsed_seconds,
        "best_params": {
            parameter_name: (
                repr(parameter_value)
                if not isinstance(parameter_value, (str, int, float, bool, type(None)))
                else parameter_value
            )
            for parameter_name, parameter_value in search.best_params_.items()
        },
        "best_score": float(search.best_score_),
    }


def run_linear_model_comparison(
    inputs: SearchInputs,
    test_size: float,
    n_jobs: int,
    verbose: int,
) -> dict[str, object]:

    """ Compare SVR linear against LinearSVR on the same dataset surface. """

    X_train, _, y_train, _ = train_test_split(
        inputs.feature_dataframe,
        inputs.target_dataframe,
        test_size=test_size,
        random_state=0,
    )
    comparison_payload = {
        "direction": inputs.direction_label,
        "dataframe_path": str(inputs.dataframe_path),
        "train_samples": len(X_train),
        "target_count": inputs.target_dataframe.shape[1],
        "n_jobs": n_jobs,
    }

    linear_svr_grid = {
        "estimator__C": [1],
        "estimator__epsilon": [1e-4, 1e-6],
        "estimator__gamma": [1.1e-6],
        "estimator__kernel": ["linear"],
    }
    comparison_payload["svr_linear"] = run_multioutput_svr_search(
        inputs=inputs,
        parameter_grid=linear_svr_grid,
        test_size=test_size,
        cv_folds=3,
        n_jobs=n_jobs,
        verbose=verbose,
    )

    TimedLinearSVR.FIT_SEQUENCE = 0
    linear_regressor = MultiOutputRegressor(
        TimedLinearSVR(
            C=1.0,
            epsilon=0.0,
            tol=1e-4,
            max_iter=5000,
            random_state=0,
        )
    )
    print("[TEMP_INFO] Starting LinearSVR comparison fit", flush=True)
    start_time = time.perf_counter()
    linear_regressor.fit(X_train, y_train)
    elapsed_seconds = time.perf_counter() - start_time
    comparison_payload["linear_svr"] = {
        "observed_base_fit_count": TimedLinearSVR.FIT_SEQUENCE,
        "elapsed_seconds": elapsed_seconds,
    }
    return comparison_payload


def resolve_output_json_path(requested_output_json: Path | None, default_stem: str) -> Path:

    """ Resolve one JSON output path under temp/output by default. """

    if requested_output_json is not None:
        return requested_output_json.resolve()
    ensure_temp_output_root()
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    return (TEMP_OUTPUT_ROOT / f"{timestamp}__{default_stem}.json").resolve()


def write_json_summary(output_json_path: Path, payload: dict[str, object]) -> None:

    """ Persist one temporary JSON summary. """

    output_json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_json_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
    print(f"[TEMP_DONE] JSON summary written to {output_json_path}", flush=True)


def initialize_temp_cli() -> None:

    """ Apply the same flush-friendly stdout behavior as the main workflow. """

    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(line_buffering=True, write_through=True)
        except Exception:
            pass
