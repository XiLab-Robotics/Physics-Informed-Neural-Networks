"""Benchmark RCIM Track1 LGBM search scaling on Aries."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

from sklearn.model_selection import GridSearchCV, ParameterGrid
from sklearn.multioutput import MultiOutputRegressor
from threadpoolctl import threadpool_limits

PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

from scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank import (  # noqa: E402
    exact_paper_model_bank_support,
)
from scripts.paper_reimplementation.rcim_ml_compensation.original_dataset_exact_model_bank import (  # noqa: E402
    original_dataset_exact_model_bank_support,
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config-path", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--candidate-limit", type=int, default=16)
    parser.add_argument("--candidate-offset", type=int, default=0)
    parser.add_argument("--candidate-stride", type=int, default=1)
    parser.add_argument("--grid-search-n-jobs", type=int, required=True)
    parser.add_argument("--threadpool-limit", type=int, required=True)
    parser.add_argument("--pre-dispatch", type=str, default="n_jobs")
    parser.add_argument("--lgbm-n-jobs", type=int, default=0)
    parser.add_argument("--device-type", type=str, default="cpu", choices=["cpu", "gpu"])
    parser.add_argument("--gpu-platform-id", type=int, default=0)
    parser.add_argument("--gpu-device-id", type=int, default=0)
    return parser.parse_args()


def build_lgbm_estimator(arguments: argparse.Namespace) -> Any:
    parameter_payload: dict[str, Any] = {
        "learning_rate": 0.39,
        "max_depth": 12,
        "subsample": 0.1,
        "random_state": 0,
    }
    if int(arguments.lgbm_n_jobs) > 0:
        parameter_payload["n_jobs"] = int(arguments.lgbm_n_jobs)
    if arguments.device_type == "gpu":
        parameter_payload.update(
            {
                "device_type": "gpu",
                "gpu_platform_id": int(arguments.gpu_platform_id),
                "gpu_device_id": int(arguments.gpu_device_id),
            }
        )
    return exact_paper_model_bank_support.build_repo_quiet_lgbm_regressor(**parameter_payload)


def main() -> None:
    arguments = parse_arguments()
    started_at = time.perf_counter()

    os.environ["LOKY_MAX_CPU_COUNT"] = str(max(1, int(arguments.grid_search_n_jobs)))
    config = original_dataset_exact_model_bank_support.load_original_dataset_exact_model_bank_config(
        arguments.config_path
    )
    config.setdefault("training", {})
    config["training"]["enabled_families"] = ["LGBM"]
    config["training"]["threadpool_limit"] = int(arguments.threadpool_limit)
    config["training"]["joblib_cpu_limit"] = int(arguments.grid_search_n_jobs)
    bundle = original_dataset_exact_model_bank_support.build_original_dataset_exact_model_bank_bundle(config)
    exact_bundle = bundle.exact_dataset_bundle

    base_estimator = build_lgbm_estimator(arguments)
    full_grid = list(
        ParameterGrid(
            exact_paper_model_bank_support.build_exact_paper_reference_parameter_grid(
                "LGBM",
                base_estimator,
            )
        )
    )
    candidate_offset = max(0, int(arguments.candidate_offset))
    candidate_stride = max(1, int(arguments.candidate_stride))
    selected_full_grid = full_grid[candidate_offset::candidate_stride][: max(1, int(arguments.candidate_limit))]
    candidate_grid = [
        {parameter_name: [parameter_value] for parameter_name, parameter_value in candidate.items()}
        for candidate in selected_full_grid
    ]
    wrapped_estimator = MultiOutputRegressor(base_estimator)
    grid_search = GridSearchCV(
        wrapped_estimator,
        candidate_grid,
        n_jobs=int(arguments.grid_search_n_jobs),
        pre_dispatch=str(arguments.pre_dispatch),
        verbose=1,
    )

    fit_started_at = time.perf_counter()
    with threadpool_limits(limits=int(arguments.threadpool_limit)):
        grid_search.fit(
            exact_bundle.train_feature_matrix,
            exact_bundle.train_target_matrix,
        )
    fit_elapsed_seconds = time.perf_counter() - fit_started_at
    elapsed_seconds = time.perf_counter() - started_at

    result = {
        "schema_version": 1,
        "config_path": str(arguments.config_path),
        "direction_label": bundle.direction_label,
        "dataset_name": config.get("dataset", {}).get("name"),
        "input_mode": config.get("dataset", {}).get("input_mode"),
        "train_rows": int(bundle.split_row_count_dictionary["train"]),
        "targets": len(exact_bundle.target_name_list),
        "features": list(exact_bundle.feature_name_list),
        "full_candidate_count": len(full_grid),
        "candidate_offset": candidate_offset,
        "candidate_stride": candidate_stride,
        "candidate_limit": len(candidate_grid),
        "estimated_cv_fits": len(candidate_grid) * int(grid_search.n_splits_),
        "grid_search_n_jobs": int(arguments.grid_search_n_jobs),
        "threadpool_limit": int(arguments.threadpool_limit),
        "pre_dispatch": str(arguments.pre_dispatch),
        "lgbm_n_jobs": int(arguments.lgbm_n_jobs),
        "device_type": str(arguments.device_type),
        "fit_elapsed_seconds": fit_elapsed_seconds,
        "elapsed_seconds": elapsed_seconds,
        "seconds_per_cv_fit": fit_elapsed_seconds / (len(candidate_grid) * int(grid_search.n_splits_)),
        "best_score": float(grid_search.best_score_),
        "best_params": dict(grid_search.best_params_),
        "hostname": os.uname().nodename,
    }
    arguments.output_json.parent.mkdir(parents=True, exist_ok=True)
    arguments.output_json.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
