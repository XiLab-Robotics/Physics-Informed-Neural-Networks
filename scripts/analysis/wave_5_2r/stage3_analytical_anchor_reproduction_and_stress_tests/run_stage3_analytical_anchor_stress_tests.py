"""Run Wave 5.2R Stage 3 PF-A reproduction and stress tests."""

from __future__ import annotations

# Import Python Utilities
import csv
import json
import os
import sys
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Sequence

# Import Plotting Utilities
import matplotlib

# Import Numerical Utilities
import numpy as np
import yaml

matplotlib.use("Agg")
from matplotlib import pyplot as plt  # noqa: E402

PROJECT_PATH = Path(os.path.abspath(__file__)).parents[4]
BENCHMARK_SCRIPT_DIRECTORY = (
    PROJECT_PATH / "scripts" / "analysis" / "polynomial_fourier_benchmark"
)
if str(BENCHMARK_SCRIPT_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(BENCHMARK_SCRIPT_DIRECTORY))
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Polynomial-Fourier Utilities
from polynomial_fourier_models import (  # noqa: E402
    QuadraticCoefficientSurface,
)
from polynomial_fourier_models import (  # noqa: E402
    RecoveredMatlabOnnxPredictor,
)
from polynomial_fourier_models import (  # noqa: E402
    fit_quadratic_coefficient_surface,
)
from polynomial_fourier_models import (  # noqa: E402
    project_fourier_coefficients,
)
from polynomial_fourier_models import (  # noqa: E402
    reconstruct_from_projected_coefficients,
)
from run_phase1_polynomial_fourier_benchmark import (  # noqa: E402
    CurveRecord,
)
from run_phase1_polynomial_fourier_benchmark import (  # noqa: E402
    curve_metrics,
)
from run_phase1_polynomial_fourier_benchmark import (  # noqa: E402
    harmonic_error_metrics,
)
from run_phase1_polynomial_fourier_benchmark import (  # noqa: E402
    load_curve_records,
)
from run_phase1_polynomial_fourier_benchmark import load_yaml  # noqa: E402
from run_phase1_polynomial_fourier_benchmark import (  # noqa: E402
    surface_to_payload,
)
from run_phase1_polynomial_fourier_benchmark import (  # noqa: E402
    write_csv_rows,
)

PHASE1_CONFIGURATION_PATH = (
    PROJECT_PATH
    / "config"
    / "analysis"
    / "polynomial_fourier_benchmark"
    / "phase1_benchmark.yaml"
)
PHASE1_COEFFICIENT_MODEL_PATH = (
    PROJECT_PATH
    / "output"
    / "analysis"
    / "polynomial_fourier_benchmark"
    / "phase1_coefficient_models.yaml"
)
PHASE1_AGGREGATE_METRIC_PATH = (
    PROJECT_PATH
    / "output"
    / "analysis"
    / "polynomial_fourier_benchmark"
    / "phase1_aggregate_metrics.csv"
)
STAGE0_CONTRACT_PATH = (
    PROJECT_PATH
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage0_forward_evidence_freeze"
    / "frozen_contract"
    / "stage0_forward_evidence_freeze.yaml"
)
OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage3_analytical_anchor_reproduction_and_stress_tests"
)
REPORT_ASSET_DIRECTORY = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "model_development_waves"
    / "wave_5_2"
    / "physics_guided_pinn_reassessment"
    / "[2026-07-27]"
    / "stage3_analytical_anchor_reproduction_and_stress_tests"
    / "assets"
)
REFIT_SURFACE_PATH = OUTPUT_DIRECTORY / "stage3_pf_a_refit_surface.yaml"
REFIT_COEFFICIENT_PATH = OUTPUT_DIRECTORY / "stage3_pf_a_coefficient_surfaces.csv"
REPRODUCTION_PATH = OUTPUT_DIRECTORY / "stage3_reproduction_comparison.csv"
VARIANT_PATH = OUTPUT_DIRECTORY / "stage3_forward_variant_comparison.csv"
BOOTSTRAP_REPEAT_PATH = OUTPUT_DIRECTORY / "stage3_bootstrap_repeat_diagnostics.csv"
BOOTSTRAP_TARGET_PATH = OUTPUT_DIRECTORY / "stage3_bootstrap_target_stability.csv"
HOLDOUT_PATH = OUTPUT_DIRECTORY / "stage3_train_only_holdout_diagnostics.csv"
CORRUPTION_PATH = OUTPUT_DIRECTORY / "stage3_anchor_corruption_diagnostics.csv"
ENVELOPE_CONDITION_PATH = OUTPUT_DIRECTORY / "stage3_validity_envelope_conditions.csv"
ENVELOPE_SUMMARY_PATH = OUTPUT_DIRECTORY / "stage3_validity_envelope.yaml"
EXIT_GATE_PATH = OUTPUT_DIRECTORY / "stage3_exit_gate_summary.json"
VARIANT_PLOT_PATH = REPORT_ASSET_DIRECTORY / "stage3_variant_comparison.png"
STABILITY_PLOT_PATH = REPORT_ASSET_DIRECTORY / "stage3_stability_holdouts.png"
CORRUPTION_PLOT_PATH = REPORT_ASSET_DIRECTORY / "stage3_corruption_sensitivity.png"

EXPECTED_SPLIT_SIGNATURE = (
    "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16"
)
RANDOM_SEED = 314159
BOOTSTRAP_REPEAT_COUNT = 64
REPRODUCTION_ABSOLUTE_TOLERANCE = 1.0e-12
BOOTSTRAP_CONDITION_NUMBER_P95_LIMIT = 10.0
BOOTSTRAP_RELATIVE_COEFFICIENT_DELTA_P95_LIMIT = 0.50
BOOTSTRAP_PREDICTION_DEVIATION_TO_BASE_MAE_LIMIT = 1.0
METRIC_NAME_LIST = [
    "mae_deg",
    "rmse_deg",
    "centered_mae_deg",
    "centered_rmse_deg",
    "offset_abs_error_deg",
    "peak_to_peak_abs_error_deg",
    "derivative_mae_deg_per_sample",
    "periodic_closure_error_deg",
    "retained_amplitude_mae_deg",
    "retained_phase_mae_rad",
]


@dataclass(frozen=True)
class HoldoutSpecification:

    """Describe one train-only analytical extrapolation test.

    Attributes:
        holdout_id: Stable machine-facing identifier.
        holdout_family: Axis or corner test family.
        support_class: Interpolation, edge extrapolation, or sparse corner.
        record_index_array: Frozen training-row indices held out from fitting.
        description: Human-readable holdout definition.
    """

    holdout_id: str
    holdout_family: str
    support_class: str
    record_index_array: np.ndarray
    description: str


def load_csv_row_list(path: Path) -> list[dict[str, str]]:

    """Load one UTF-8 CSV into a list of dictionaries."""

    with path.open("r", encoding="utf-8-sig", newline="") as input_file:
        return list(csv.DictReader(input_file))


def build_coefficient_label_list(
    harmonic_order_list: Sequence[int],
) -> list[str]:

    """Build offset plus ordered sine/cosine coefficient labels."""

    coefficient_label_list = ["offset"]
    for harmonic_order in harmonic_order_list:
        coefficient_label_list.extend(
            [
                f"sin_{int(harmonic_order)}",
                f"cos_{int(harmonic_order)}",
            ]
        )
    return coefficient_label_list


def build_training_matrices(
    training_record_list: Sequence[CurveRecord],
    harmonic_order_list: Sequence[int],
) -> tuple[np.ndarray, np.ndarray]:

    """Build train-only operating features and projected coefficient targets."""

    # Build Causal Operating Feature Matrix
    operating_feature_matrix = np.vstack(
        [record.operating_features() for record in training_record_list]
    )

    # Build Explicit Offset And Complex-Coefficient Targets
    target_coefficient_matrix = np.vstack(
        [
            project_fourier_coefficients(
                record.te_deg,
                list(harmonic_order_list),
            )
            for record in training_record_list
        ]
    )
    return operating_feature_matrix, target_coefficient_matrix


def fit_surface_from_records(
    training_record_list: Sequence[CurveRecord],
    harmonic_order_list: Sequence[int],
) -> QuadraticCoefficientSurface:

    """Fit one complete-quadratic surface from declared training records."""

    operating_feature_matrix, target_coefficient_matrix = (
        build_training_matrices(
            training_record_list,
            harmonic_order_list,
        )
    )
    return fit_quadratic_coefficient_surface(
        operating_feature_matrix,
        target_coefficient_matrix,
        list(harmonic_order_list),
    )


def predict_surface_curve(
    surface: QuadraticCoefficientSurface,
    record: CurveRecord,
    operating_feature_override: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:

    """Predict one curve and return its explicit coefficient array."""

    # Resolve Causal Operating Inputs
    operating_feature_array = (
        record.operating_features()
        if operating_feature_override is None
        else np.asarray(operating_feature_override, dtype=np.float64)
    )
    assert operating_feature_array.shape == (3,), (
        "Operating feature override must contain torque, speed, temperature"
    )

    # Predict Coefficients And Reconstruct Exact Periodic Curve
    coefficient_array = surface.predict(
        operating_feature_array[np.newaxis, :]
    )[0]
    predicted_curve = reconstruct_from_projected_coefficients(
        np.deg2rad(record.theta_deg),
        coefficient_array,
        surface.harmonic_order_list,
    )
    assert np.all(np.isfinite(coefficient_array)), (
        f"Non-finite coefficient prediction | {record.condition_id}"
    )
    assert np.all(np.isfinite(predicted_curve)), (
        f"Non-finite curve prediction | {record.condition_id}"
    )
    return predicted_curve, coefficient_array


def build_curve_metric_row(
    record: CurveRecord,
    model_id: str,
    predicted_curve: np.ndarray,
    evaluation_order_list: Sequence[int],
    anchor_prediction: np.ndarray | None = None,
) -> dict[str, Any]:

    """Build one full curve-first metric row."""

    # Compute Standard And Harmonic Metrics
    metric_dictionary = {
        **curve_metrics(record.te_deg, predicted_curve),
        **harmonic_error_metrics(
            record.te_deg,
            predicted_curve,
            list(evaluation_order_list),
        ),
    }

    # Compute Optional Anchor Deviation
    if anchor_prediction is None:
        anchor_deviation_mae_deg = 0.0
        anchor_deviation_max_abs_deg = 0.0
    else:
        anchor_difference = predicted_curve - anchor_prediction
        anchor_deviation_mae_deg = float(np.mean(np.abs(anchor_difference)))
        anchor_deviation_max_abs_deg = float(
            np.max(np.abs(anchor_difference))
        )

    return {
        "condition_id": record.condition_id,
        "split": record.split,
        "model_id": model_id,
        "nominal_speed_rpm": record.nominal_speed_rpm,
        "nominal_torque_nm": record.nominal_torque_nm,
        "nominal_temperature_deg_c": (
            record.nominal_temperature_deg_c
        ),
        **metric_dictionary,
        "anchor_deviation_mae_deg": anchor_deviation_mae_deg,
        "anchor_deviation_max_abs_deg": anchor_deviation_max_abs_deg,
    }


def aggregate_metric_row_list(
    metric_row_list: Sequence[dict[str, Any]],
) -> dict[str, float]:

    """Aggregate the stable metric set over one curve population."""

    assert metric_row_list, "Cannot aggregate an empty metric population"
    aggregate_dictionary: dict[str, float] = {}
    for metric_name in [
        *METRIC_NAME_LIST,
        "anchor_deviation_mae_deg",
        "anchor_deviation_max_abs_deg",
    ]:
        metric_value_array = np.asarray(
            [float(row[metric_name]) for row in metric_row_list],
            dtype=np.float64,
        )
        aggregate_dictionary[f"{metric_name}_mean"] = float(
            np.mean(metric_value_array)
        )
        aggregate_dictionary[f"{metric_name}_median"] = float(
            np.median(metric_value_array)
        )
        aggregate_dictionary[f"{metric_name}_p95"] = float(
            np.quantile(metric_value_array, 0.95)
        )
        aggregate_dictionary[f"{metric_name}_maximum"] = float(
            np.max(metric_value_array)
        )
    return aggregate_dictionary


def evaluate_surface_on_records(
    model_id: str,
    surface: QuadraticCoefficientSurface,
    record_list: Sequence[CurveRecord],
    evaluation_order_list: Sequence[int],
    anchor_prediction_dictionary: MappingLike | None = None,
) -> tuple[list[dict[str, Any]], dict[str, np.ndarray]]:

    """Evaluate one analytical surface on a declared record population."""

    metric_row_list: list[dict[str, Any]] = []
    prediction_dictionary: dict[str, np.ndarray] = {}
    for record in record_list:
        predicted_curve, _ = predict_surface_curve(surface, record)
        anchor_prediction = (
            None
            if anchor_prediction_dictionary is None
            else anchor_prediction_dictionary[record.condition_id]
        )
        metric_row_list.append(
            build_curve_metric_row(
                record=record,
                model_id=model_id,
                predicted_curve=predicted_curve,
                evaluation_order_list=evaluation_order_list,
                anchor_prediction=anchor_prediction,
            )
        )
        prediction_dictionary[record.condition_id] = predicted_curve
    return metric_row_list, prediction_dictionary


MappingLike = dict[str, np.ndarray]


def build_reproduction_evidence(
    refit_surface: QuadraticCoefficientSurface,
    phase1_surface_payload: dict[str, Any],
    refit_test_metric_dictionary: dict[str, float],
    phase1_test_metric_row: dict[str, str],
) -> list[dict[str, Any]]:

    """Compare refit coefficients and metrics with frozen Phase 1 evidence."""

    # Compare Surface State
    phase1_feature_mean = np.asarray(
        phase1_surface_payload["feature_mean"],
        dtype=np.float64,
    )
    phase1_feature_scale = np.asarray(
        phase1_surface_payload["feature_scale"],
        dtype=np.float64,
    )
    phase1_coefficient_matrix = np.asarray(
        phase1_surface_payload["coefficient_matrix"],
        dtype=np.float64,
    )
    reproduction_row_list = [
        {
            "comparison_id": "feature_mean_max_abs",
            "refit_value": float(
                np.max(np.abs(refit_surface.feature_mean - phase1_feature_mean))
            ),
            "phase1_value": 0.0,
            "absolute_difference": float(
                np.max(np.abs(refit_surface.feature_mean - phase1_feature_mean))
            ),
            "tolerance": REPRODUCTION_ABSOLUTE_TOLERANCE,
        },
        {
            "comparison_id": "feature_scale_max_abs",
            "refit_value": float(
                np.max(
                    np.abs(refit_surface.feature_scale - phase1_feature_scale)
                )
            ),
            "phase1_value": 0.0,
            "absolute_difference": float(
                np.max(
                    np.abs(refit_surface.feature_scale - phase1_feature_scale)
                )
            ),
            "tolerance": REPRODUCTION_ABSOLUTE_TOLERANCE,
        },
        {
            "comparison_id": "coefficient_matrix_max_abs",
            "refit_value": float(
                np.max(
                    np.abs(
                        refit_surface.coefficient_matrix
                        - phase1_coefficient_matrix
                    )
                )
            ),
            "phase1_value": 0.0,
            "absolute_difference": float(
                np.max(
                    np.abs(
                        refit_surface.coefficient_matrix
                        - phase1_coefficient_matrix
                    )
                )
            ),
            "tolerance": REPRODUCTION_ABSOLUTE_TOLERANCE,
        },
        {
            "comparison_id": "design_condition_number",
            "refit_value": refit_surface.design_condition_number,
            "phase1_value": float(
                phase1_surface_payload["design_condition_number"]
            ),
            "absolute_difference": abs(
                refit_surface.design_condition_number
                - float(phase1_surface_payload["design_condition_number"])
            ),
            "tolerance": REPRODUCTION_ABSOLUTE_TOLERANCE,
        },
    ]

    # Compare Every Phase 1 Aggregate Metric
    for metric_name in METRIC_NAME_LIST:
        refit_value = float(
            refit_test_metric_dictionary[f"{metric_name}_mean"]
        )
        phase1_value = float(
            phase1_test_metric_row[f"{metric_name}_mean"]
        )
        reproduction_row_list.append(
            {
                "comparison_id": f"test_{metric_name}_mean",
                "refit_value": refit_value,
                "phase1_value": phase1_value,
                "absolute_difference": abs(refit_value - phase1_value),
                "tolerance": REPRODUCTION_ABSOLUTE_TOLERANCE,
            }
        )

    # Resolve Pass State
    for reproduction_row in reproduction_row_list:
        reproduction_row["status"] = (
            "pass"
            if float(reproduction_row["absolute_difference"])
            <= float(reproduction_row["tolerance"])
            else "fail"
        )
    return reproduction_row_list


def write_explicit_coefficient_surface_rows(
    surface: QuadraticCoefficientSurface,
) -> None:

    """Serialize every basis-to-coefficient mapping in long form."""

    basis_label_list = [
        "torque_squared",
        "speed_squared",
        "temperature_squared",
        "torque_speed",
        "torque_temperature",
        "speed_temperature",
        "torque",
        "speed",
        "temperature",
        "constant",
    ]
    coefficient_label_list = build_coefficient_label_list(
        surface.harmonic_order_list
    )
    row_list = []
    for basis_index, basis_label in enumerate(basis_label_list):
        for coefficient_index, coefficient_label in enumerate(
            coefficient_label_list
        ):
            row_list.append(
                {
                    "basis_index": basis_index,
                    "basis_label": basis_label,
                    "coefficient_index": coefficient_index,
                    "coefficient_label": coefficient_label,
                    "coefficient_value": float(
                        surface.coefficient_matrix[
                            basis_index,
                            coefficient_index,
                        ]
                    ),
                }
            )
    write_csv_rows(REFIT_COEFFICIENT_PATH, row_list)


def evaluate_forward_variant_roster(
    configuration: dict[str, Any],
    forward_record_list: Sequence[CurveRecord],
    training_record_list: Sequence[CurveRecord],
    test_record_list: Sequence[CurveRecord],
    anchor_prediction_dictionary: dict[str, np.ndarray],
) -> list[dict[str, Any]]:

    """Compare all required forward analytical formulations."""

    # Freeze Variant Order Sets
    harmonic_set_dictionary = configuration["harmonic_order_sets"]
    variant_order_dictionary = {
        "PF_A_LOCAL_QUADRATIC": harmonic_set_dictionary[
            "local_plc_common"
        ],
        "PF_E_REDUCED_QUADRATIC": harmonic_set_dictionary["reduced_common"],
        "PF_A_PAPER_QUADRATIC": harmonic_set_dictionary[
            "bauer_paper_rh380"
        ],
        "PF_G_PLC_SAFE_CORE_QUADRATIC": [1, 3, 39, 40],
        "PF_H_ONNX_ORDER_QUADRATIC": harmonic_set_dictionary[
            "recovered_onnx_sparse"
        ],
    }
    evaluation_order_list = harmonic_set_dictionary["local_plc_common"]
    variant_row_list: list[dict[str, Any]] = []

    # Fit And Evaluate Quadratic Variants
    for model_id, harmonic_order_list in variant_order_dictionary.items():
        surface = fit_surface_from_records(
            training_record_list,
            harmonic_order_list,
        )
        metric_row_list, _ = evaluate_surface_on_records(
            model_id=model_id,
            surface=surface,
            record_list=test_record_list,
            evaluation_order_list=evaluation_order_list,
            anchor_prediction_dictionary=anchor_prediction_dictionary,
        )
        aggregate_dictionary = aggregate_metric_row_list(metric_row_list)
        variant_row_list.append(
            {
                "model_id": model_id,
                "formulation": "complete_quadratic_coefficient_surface",
                "harmonic_order_list": list(harmonic_order_list),
                "harmonic_order_count": len(harmonic_order_list),
                "coefficient_output_count": 1 + 2 * len(harmonic_order_list),
                "design_condition_number": (
                    surface.design_condition_number
                ),
                "validity_scope": "frozen_forward_common_split",
                "deployment_status": (
                    "qualified_anchor"
                    if model_id == "PF_A_LOCAL_QUADRATIC"
                    else "comparator_only"
                ),
                **aggregate_dictionary,
            }
        )

    # Evaluate Recovered ONNX Sparse Comparator
    onnx_predictor = RecoveredMatlabOnnxPredictor(
        {
            model_name: PROJECT_PATH / model_path
            for model_name, model_path in configuration["onnx_models"].items()
        },
        list(configuration["runtime"]["onnx_provider_list"]),
    )
    forward_input_matrix = np.vstack(
        [record.onnx_features() for record in forward_record_list]
    )
    onnx_prediction_map = onnx_predictor.predict_coefficients(
        forward_input_matrix
    )
    forward_index_by_condition_id = {
        record.condition_id: record_index
        for record_index, record in enumerate(forward_record_list)
    }
    onnx_metric_row_list: list[dict[str, Any]] = []
    for record in test_record_list:
        record_index = forward_index_by_condition_id[record.condition_id]
        coefficient_map = {
            coefficient_name: float(coefficient_value_array[record_index])
            for coefficient_name, coefficient_value_array in (
                onnx_prediction_map.items()
            )
        }
        predicted_curve = onnx_predictor.reconstruct(
            np.deg2rad(record.theta_deg),
            coefficient_map,
        )
        assert np.all(np.isfinite(predicted_curve)), (
            f"Recovered ONNX produced non-finite curve | {record.condition_id}"
        )
        onnx_metric_row_list.append(
            build_curve_metric_row(
                record=record,
                model_id="PF_B_RECOVERED_ONNX",
                predicted_curve=predicted_curve,
                evaluation_order_list=evaluation_order_list,
                anchor_prediction=anchor_prediction_dictionary[
                    record.condition_id
                ],
            )
        )
    variant_row_list.append(
        {
            "model_id": "PF_B_RECOVERED_ONNX",
            "formulation": "recovered_sparse_onnx_coefficient_bank",
            "harmonic_order_list": [1, 39, 40],
            "harmonic_order_count": 3,
            "coefficient_output_count": 7,
            "design_condition_number": "",
            "validity_scope": "recovered_forward_only",
            "deployment_status": "comparator_only",
            **aggregate_metric_row_list(onnx_metric_row_list),
        }
    )
    return variant_row_list


def run_bootstrap_stability_analysis(
    refit_surface: QuadraticCoefficientSurface,
    training_record_list: Sequence[CurveRecord],
    test_record_list: Sequence[CurveRecord],
    base_test_prediction_dictionary: dict[str, np.ndarray],
    base_test_mae_deg: float,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, float]]:

    """Measure coefficient and prediction stability under train bootstrap."""

    # Freeze Full Training Matrices And Random Stream
    harmonic_order_list = list(refit_surface.harmonic_order_list)
    operating_feature_matrix, target_coefficient_matrix = (
        build_training_matrices(
            training_record_list,
            harmonic_order_list,
        )
    )
    random_generator = np.random.default_rng(RANDOM_SEED)
    bootstrap_surface_list: list[QuadraticCoefficientSurface] = []
    bootstrap_repeat_row_list: list[dict[str, Any]] = []

    # Fit Deterministic Bootstrap Replicates
    for bootstrap_index in range(BOOTSTRAP_REPEAT_COUNT):
        sampled_index_array = random_generator.choice(
            len(training_record_list),
            size=len(training_record_list),
            replace=True,
        )
        bootstrap_surface = fit_quadratic_coefficient_surface(
            operating_feature_matrix[sampled_index_array],
            target_coefficient_matrix[sampled_index_array],
            harmonic_order_list,
        )
        bootstrap_surface_list.append(bootstrap_surface)

        coefficient_delta = (
            bootstrap_surface.coefficient_matrix
            - refit_surface.coefficient_matrix
        )
        relative_coefficient_delta = float(
            np.linalg.norm(coefficient_delta)
            / max(np.linalg.norm(refit_surface.coefficient_matrix), 1.0e-15)
        )
        prediction_deviation_value_list: list[float] = []
        prediction_deviation_maximum_list: list[float] = []
        for record in test_record_list:
            bootstrap_prediction, _ = predict_surface_curve(
                bootstrap_surface,
                record,
            )
            anchor_prediction = base_test_prediction_dictionary[
                record.condition_id
            ]
            prediction_difference = (
                bootstrap_prediction - anchor_prediction
            )
            prediction_deviation_value_list.append(
                float(np.mean(np.abs(prediction_difference)))
            )
            prediction_deviation_maximum_list.append(
                float(np.max(np.abs(prediction_difference)))
            )
        mean_prediction_deviation = float(
            np.mean(prediction_deviation_value_list)
        )
        bootstrap_repeat_row_list.append(
            {
                "bootstrap_index": bootstrap_index,
                "random_seed": RANDOM_SEED,
                "sample_count": len(sampled_index_array),
                "unique_sample_count": int(
                    np.unique(sampled_index_array).size
                ),
                "design_condition_number": (
                    bootstrap_surface.design_condition_number
                ),
                "relative_coefficient_delta": (
                    relative_coefficient_delta
                ),
                "test_prediction_deviation_mae_deg": (
                    mean_prediction_deviation
                ),
                "test_prediction_deviation_to_base_mae_ratio": (
                    mean_prediction_deviation / base_test_mae_deg
                ),
                "test_prediction_deviation_max_abs_deg": float(
                    np.max(prediction_deviation_maximum_list)
                ),
                "finite": True,
            }
        )

    # Summarize Stability Per Explicit Coefficient Target
    bootstrap_coefficient_tensor = np.stack(
        [
            surface.coefficient_matrix
            for surface in bootstrap_surface_list
        ],
        axis=0,
    )
    coefficient_label_list = build_coefficient_label_list(
        harmonic_order_list
    )
    bootstrap_target_row_list: list[dict[str, Any]] = []
    for coefficient_index, coefficient_label in enumerate(
        coefficient_label_list
    ):
        base_coefficient_vector = refit_surface.coefficient_matrix[
            :,
            coefficient_index,
        ]
        bootstrap_delta_matrix = (
            bootstrap_coefficient_tensor[:, :, coefficient_index]
            - base_coefficient_vector[np.newaxis, :]
        )
        delta_norm_array = np.linalg.norm(
            bootstrap_delta_matrix,
            axis=1,
        )
        base_norm = float(np.linalg.norm(base_coefficient_vector))
        relative_delta_norm_array = delta_norm_array / max(
            base_norm,
            1.0e-15,
        )
        bootstrap_target_row_list.append(
            {
                "coefficient_index": coefficient_index,
                "coefficient_label": coefficient_label,
                "base_surface_norm": base_norm,
                "bootstrap_delta_norm_median": float(
                    np.median(delta_norm_array)
                ),
                "bootstrap_delta_norm_p95": float(
                    np.quantile(delta_norm_array, 0.95)
                ),
                "bootstrap_relative_delta_norm_median": float(
                    np.median(relative_delta_norm_array)
                ),
                "bootstrap_relative_delta_norm_p95": float(
                    np.quantile(relative_delta_norm_array, 0.95)
                ),
                "maximum_basis_coefficient_std": float(
                    np.max(
                        np.std(
                            bootstrap_coefficient_tensor[
                                :,
                                :,
                                coefficient_index,
                            ],
                            axis=0,
                            ddof=1,
                        )
                    )
                ),
            }
        )

    # Build Global Stability Summary
    condition_number_array = np.asarray(
        [
            row["design_condition_number"]
            for row in bootstrap_repeat_row_list
        ],
        dtype=np.float64,
    )
    relative_delta_array = np.asarray(
        [
            row["relative_coefficient_delta"]
            for row in bootstrap_repeat_row_list
        ],
        dtype=np.float64,
    )
    prediction_ratio_array = np.asarray(
        [
            row["test_prediction_deviation_to_base_mae_ratio"]
            for row in bootstrap_repeat_row_list
        ],
        dtype=np.float64,
    )
    summary_dictionary = {
        "condition_number_median": float(
            np.median(condition_number_array)
        ),
        "condition_number_p95": float(
            np.quantile(condition_number_array, 0.95)
        ),
        "condition_number_maximum": float(np.max(condition_number_array)),
        "relative_coefficient_delta_median": float(
            np.median(relative_delta_array)
        ),
        "relative_coefficient_delta_p95": float(
            np.quantile(relative_delta_array, 0.95)
        ),
        "prediction_deviation_to_base_mae_ratio_median": float(
            np.median(prediction_ratio_array)
        ),
        "prediction_deviation_to_base_mae_ratio_p95": float(
            np.quantile(prediction_ratio_array, 0.95)
        ),
    }
    return (
        bootstrap_repeat_row_list,
        bootstrap_target_row_list,
        summary_dictionary,
    )


def build_train_only_holdout_specification_list(
    training_record_list: Sequence[CurveRecord],
) -> list[HoldoutSpecification]:

    """Build axis-level and geometric corner holdouts inside training data."""

    holdout_specification_list: list[HoldoutSpecification] = []
    nominal_axis_dictionary: dict[
        str,
        tuple[str, Callable[[CurveRecord], float]],
    ] = {
        "torque": (
            "nominal_torque_nm",
            lambda record: record.nominal_torque_nm,
        ),
        "speed": (
            "nominal_speed_rpm",
            lambda record: record.nominal_speed_rpm,
        ),
        "temperature": (
            "nominal_temperature_deg_c",
            lambda record: record.nominal_temperature_deg_c,
        ),
    }

    # Build Low, Median, And High Axis-Level Holdouts
    for axis_name, (_, value_getter) in nominal_axis_dictionary.items():
        axis_value_array = np.asarray(
            [value_getter(record) for record in training_record_list],
            dtype=np.float64,
        )
        unique_level_array = np.unique(axis_value_array)
        selected_level_dictionary = {
            "low": float(unique_level_array[0]),
            "median": float(
                unique_level_array[len(unique_level_array) // 2]
            ),
            "high": float(unique_level_array[-1]),
        }
        for level_role, level_value in selected_level_dictionary.items():
            record_index_array = np.flatnonzero(
                np.isclose(axis_value_array, level_value)
            )
            support_class = (
                "interpolation"
                if level_role == "median"
                else "axis_edge_extrapolation"
            )
            holdout_specification_list.append(
                HoldoutSpecification(
                    holdout_id=(
                        f"{axis_name}_{level_role}_"
                        f"{level_value:g}"
                    ),
                    holdout_family=axis_name,
                    support_class=support_class,
                    record_index_array=record_index_array,
                    description=(
                        f"Hold out every train curve at {axis_name} "
                        f"{level_value:g} ({level_role} observed level)."
                    ),
                )
            )

    # Build Eight Fixed-Size Geometric Corner Holdouts
    operating_feature_matrix = np.vstack(
        [record.operating_features() for record in training_record_list]
    )
    feature_mean = np.mean(operating_feature_matrix, axis=0)
    feature_scale = np.std(operating_feature_matrix, axis=0)
    standardized_feature_matrix = (
        operating_feature_matrix - feature_mean
    ) / feature_scale
    corner_holdout_count = max(
        24,
        int(np.ceil(0.05 * len(training_record_list))),
    )
    for corner_sign_tuple in product((-1.0, 1.0), repeat=3):
        corner_sign_array = np.asarray(
            corner_sign_tuple,
            dtype=np.float64,
        )
        corner_score_array = (
            standardized_feature_matrix @ corner_sign_array
        )
        record_index_array = np.argsort(corner_score_array)[
            -corner_holdout_count:
        ]
        corner_label = "_".join(
            "high" if sign_value > 0.0 else "low"
            for sign_value in corner_sign_tuple
        )
        holdout_specification_list.append(
            HoldoutSpecification(
                holdout_id=f"corner_{corner_label}",
                holdout_family="corner",
                support_class="sparse_corner_extrapolation",
                record_index_array=np.sort(record_index_array),
                description=(
                    "Hold out the five-percent training population nearest "
                    f"the standardized {corner_label} corner."
                ),
            )
        )
    return holdout_specification_list


def run_train_only_holdout_analysis(
    refit_surface: QuadraticCoefficientSurface,
    training_record_list: Sequence[CurveRecord],
) -> list[dict[str, Any]]:

    """Refit PF-A after each train-only axis and corner holdout."""

    harmonic_order_list = list(refit_surface.harmonic_order_list)
    holdout_specification_list = (
        build_train_only_holdout_specification_list(training_record_list)
    )
    holdout_row_list: list[dict[str, Any]] = []
    all_record_index_array = np.arange(len(training_record_list))

    # Evaluate Every Predeclared Holdout
    for holdout_specification in holdout_specification_list:
        retained_index_array = np.setdiff1d(
            all_record_index_array,
            holdout_specification.record_index_array,
            assume_unique=True,
        )
        retained_record_list = [
            training_record_list[int(record_index)]
            for record_index in retained_index_array
        ]
        holdout_record_list = [
            training_record_list[int(record_index)]
            for record_index in holdout_specification.record_index_array
        ]
        holdout_surface = fit_surface_from_records(
            retained_record_list,
            harmonic_order_list,
        )

        # Compare Holdout Refit With Full-Train Anchor
        holdout_metric_row_list: list[dict[str, Any]] = []
        base_metric_row_list: list[dict[str, Any]] = []
        prediction_deviation_value_list: list[float] = []
        for record in holdout_record_list:
            holdout_prediction, _ = predict_surface_curve(
                holdout_surface,
                record,
            )
            base_prediction, _ = predict_surface_curve(
                refit_surface,
                record,
            )
            holdout_metric_row_list.append(
                build_curve_metric_row(
                    record,
                    holdout_specification.holdout_id,
                    holdout_prediction,
                    harmonic_order_list,
                    base_prediction,
                )
            )
            base_metric_row_list.append(
                build_curve_metric_row(
                    record,
                    "PF_A_FULL_TRAIN",
                    base_prediction,
                    harmonic_order_list,
                )
            )
            prediction_deviation_value_list.append(
                float(
                    np.mean(
                        np.abs(holdout_prediction - base_prediction)
                    )
                )
            )
        holdout_aggregate = aggregate_metric_row_list(
            holdout_metric_row_list
        )
        base_aggregate = aggregate_metric_row_list(base_metric_row_list)
        holdout_row_list.append(
            {
                "holdout_id": holdout_specification.holdout_id,
                "holdout_family": holdout_specification.holdout_family,
                "support_class": holdout_specification.support_class,
                "description": holdout_specification.description,
                "fit_curve_count": len(retained_record_list),
                "holdout_curve_count": len(holdout_record_list),
                "design_condition_number": (
                    holdout_surface.design_condition_number
                ),
                "holdout_mae_deg": holdout_aggregate[
                    "mae_deg_mean"
                ],
                "full_train_anchor_mae_deg": base_aggregate[
                    "mae_deg_mean"
                ],
                "mae_ratio_to_full_train_anchor": (
                    holdout_aggregate["mae_deg_mean"]
                    / max(base_aggregate["mae_deg_mean"], 1.0e-15)
                ),
                "centered_mae_deg": holdout_aggregate[
                    "centered_mae_deg_mean"
                ],
                "offset_abs_error_deg": holdout_aggregate[
                    "offset_abs_error_deg_mean"
                ],
                "derivative_mae_deg_per_sample": holdout_aggregate[
                    "derivative_mae_deg_per_sample_mean"
                ],
                "prediction_deviation_from_full_anchor_mae_deg": float(
                    np.mean(prediction_deviation_value_list)
                ),
                "finite": True,
            }
        )
    return holdout_row_list


def rotate_harmonic_coefficients(
    coefficient_array: np.ndarray,
    phase_shift_rad: float,
) -> np.ndarray:

    """Apply one common circular phase shift to all retained harmonics."""

    rotated_coefficient_array = coefficient_array.copy()
    cosine_shift = float(np.cos(phase_shift_rad))
    sine_shift = float(np.sin(phase_shift_rad))
    harmonic_count = (coefficient_array.size - 1) // 2
    for harmonic_index in range(harmonic_count):
        sine_index = 1 + 2 * harmonic_index
        cosine_index = sine_index + 1
        sine_coefficient = coefficient_array[sine_index]
        cosine_coefficient = coefficient_array[cosine_index]
        rotated_coefficient_array[sine_index] = (
            sine_coefficient * cosine_shift
            - cosine_coefficient * sine_shift
        )
        rotated_coefficient_array[cosine_index] = (
            cosine_coefficient * cosine_shift
            + sine_coefficient * sine_shift
        )
    return rotated_coefficient_array


def run_anchor_corruption_analysis(
    refit_surface: QuadraticCoefficientSurface,
    test_record_list: Sequence[CurveRecord],
    base_test_prediction_dictionary: dict[str, np.ndarray],
) -> list[dict[str, Any]]:

    """Measure sensitivity to coefficient, phase, order, and input corruption."""

    harmonic_order_list = list(refit_surface.harmonic_order_list)
    corruption_row_list: list[dict[str, Any]] = []

    def evaluate_corruption_arm(
        corruption_id: str,
        corruption_family: str,
        severity_value: float,
        coefficient_transform: Callable[
            [np.ndarray, CurveRecord],
            np.ndarray,
        ],
    ) -> None:

        """Evaluate one deterministic corruption arm."""

        arm_metric_row_list: list[dict[str, Any]] = []
        for record in test_record_list:
            base_coefficient_array = refit_surface.predict(
                record.operating_features()[np.newaxis, :]
            )[0]
            corrupted_coefficient_array = coefficient_transform(
                base_coefficient_array,
                record,
            )
            corrupted_prediction = reconstruct_from_projected_coefficients(
                np.deg2rad(record.theta_deg),
                corrupted_coefficient_array,
                harmonic_order_list,
            )
            assert np.all(np.isfinite(corrupted_prediction)), (
                f"Non-finite corruption prediction | {corruption_id} | "
                f"{record.condition_id}"
            )
            arm_metric_row_list.append(
                build_curve_metric_row(
                    record=record,
                    model_id=corruption_id,
                    predicted_curve=corrupted_prediction,
                    evaluation_order_list=harmonic_order_list,
                    anchor_prediction=base_test_prediction_dictionary[
                        record.condition_id
                    ],
                )
            )
        aggregate_dictionary = aggregate_metric_row_list(
            arm_metric_row_list
        )
        corruption_row_list.append(
            {
                "corruption_id": corruption_id,
                "corruption_family": corruption_family,
                "severity_value": severity_value,
                "curve_count": len(arm_metric_row_list),
                **aggregate_dictionary,
                "finite": True,
            }
        )

    # Scale All Or Harmonic-Only Coefficients
    for coefficient_scope in ("all", "harmonic_only"):
        for scale_factor in (0.90, 0.95, 1.05, 1.10):
            def scale_transform(
                coefficient_array: np.ndarray,
                _record: CurveRecord,
                resolved_scope: str = coefficient_scope,
                resolved_scale: float = scale_factor,
            ) -> np.ndarray:

                """Scale the declared coefficient scope."""

                corrupted_array = coefficient_array.copy()
                start_index = 0 if resolved_scope == "all" else 1
                corrupted_array[start_index:] *= resolved_scale
                return corrupted_array

            evaluate_corruption_arm(
                corruption_id=(
                    f"scale_{coefficient_scope}_{scale_factor:.2f}"
                ),
                corruption_family="coefficient_scale",
                severity_value=scale_factor - 1.0,
                coefficient_transform=scale_transform,
            )

    # Rotate Every Retained Harmonic Phase
    for phase_shift_deg in (-15.0, -5.0, -1.0, 1.0, 5.0, 15.0):
        evaluate_corruption_arm(
            corruption_id=f"phase_shift_{phase_shift_deg:+g}deg",
            corruption_family="phase_perturbation",
            severity_value=phase_shift_deg,
            coefficient_transform=(
                lambda coefficient_array, _record, shift=phase_shift_deg: (
                    rotate_harmonic_coefficients(
                        coefficient_array,
                        np.deg2rad(shift),
                    )
                )
            ),
        )

    # Omit Individual And Grouped Harmonic Orders
    omission_group_dictionary: dict[str, list[int]] = {
        **{
            f"order_{harmonic_order}": [harmonic_order]
            for harmonic_order in harmonic_order_list
        },
        "low_orders": [1, 3],
        "mesh_orders": [39, 40, 78, 81],
        "high_orders": [156, 162, 240],
    }
    for omission_label, omitted_order_list in (
        omission_group_dictionary.items()
    ):
        omitted_index_list = [
            harmonic_order_list.index(harmonic_order)
            for harmonic_order in omitted_order_list
            if harmonic_order in harmonic_order_list
        ]

        def omission_transform(
            coefficient_array: np.ndarray,
            _record: CurveRecord,
            resolved_index_list: list[int] = omitted_index_list,
        ) -> np.ndarray:

            """Zero the declared sine/cosine coefficient pairs."""

            corrupted_array = coefficient_array.copy()
            for harmonic_index in resolved_index_list:
                corrupted_array[1 + 2 * harmonic_index] = 0.0
                corrupted_array[2 + 2 * harmonic_index] = 0.0
            return corrupted_array

        evaluate_corruption_arm(
            corruption_id=f"omit_{omission_label}",
            corruption_family="order_omission",
            severity_value=float(len(omitted_index_list)),
            coefficient_transform=omission_transform,
        )

    # Shift One Operating Input Before Coefficient Evaluation
    operating_axis_name_list = ["torque", "speed", "temperature"]
    for feature_index, feature_name in enumerate(operating_axis_name_list):
        for standard_deviation_shift in (-0.50, -0.25, 0.25, 0.50):
            def input_shift_transform(
                _coefficient_array: np.ndarray,
                record: CurveRecord,
                resolved_feature_index: int = feature_index,
                resolved_shift: float = standard_deviation_shift,
            ) -> np.ndarray:

                """Re-evaluate coefficients after a standardized input shift."""

                shifted_feature_array = record.operating_features().copy()
                shifted_feature_array[resolved_feature_index] += (
                    resolved_shift
                    * refit_surface.feature_scale[resolved_feature_index]
                )
                return refit_surface.predict(
                    shifted_feature_array[np.newaxis, :]
                )[0]

            evaluate_corruption_arm(
                corruption_id=(
                    f"input_shift_{feature_name}_"
                    f"{standard_deviation_shift:+.2f}std"
                ),
                corruption_family="operating_input_shift",
                severity_value=standard_deviation_shift,
                coefficient_transform=input_shift_transform,
            )
    return corruption_row_list


def compute_nearest_standardized_distance(
    query_feature_matrix: np.ndarray,
    reference_feature_matrix: np.ndarray,
    feature_scale: np.ndarray,
) -> np.ndarray:

    """Compute nearest Euclidean distance in standardized operating space."""

    standardized_difference_tensor = (
        query_feature_matrix[:, np.newaxis, :]
        - reference_feature_matrix[np.newaxis, :, :]
    ) / feature_scale[np.newaxis, np.newaxis, :]
    distance_matrix = np.linalg.norm(
        standardized_difference_tensor,
        axis=2,
    )
    return np.min(distance_matrix, axis=1)


def build_validity_envelope(
    refit_surface: QuadraticCoefficientSurface,
    forward_record_list: Sequence[CurveRecord],
    training_record_list: Sequence[CurveRecord],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:

    """Define supported, sparse, and unsupported operating-state tiers."""

    # Freeze Train-Support Geometry
    training_feature_matrix = np.vstack(
        [record.operating_features() for record in training_record_list]
    )
    feature_minimum = np.min(training_feature_matrix, axis=0)
    feature_maximum = np.max(training_feature_matrix, axis=0)
    feature_scale = refit_surface.feature_scale

    # Derive Train-Only Leave-One-Out Density Threshold
    standardized_training_difference_tensor = (
        training_feature_matrix[:, np.newaxis, :]
        - training_feature_matrix[np.newaxis, :, :]
    ) / feature_scale[np.newaxis, np.newaxis, :]
    training_distance_matrix = np.linalg.norm(
        standardized_training_difference_tensor,
        axis=2,
    )
    np.fill_diagonal(training_distance_matrix, np.inf)
    training_leave_one_out_distance_array = np.min(
        training_distance_matrix,
        axis=1,
    )
    supported_distance_threshold = float(
        np.quantile(training_leave_one_out_distance_array, 0.95)
    )

    # Classify Every Eligible Forward Condition
    forward_feature_matrix = np.vstack(
        [record.operating_features() for record in forward_record_list]
    )
    nearest_distance_array = compute_nearest_standardized_distance(
        forward_feature_matrix,
        training_feature_matrix,
        feature_scale,
    )
    inside_axis_box_mask = np.all(
        (forward_feature_matrix >= feature_minimum[np.newaxis, :])
        & (forward_feature_matrix <= feature_maximum[np.newaxis, :]),
        axis=1,
    )
    condition_row_list: list[dict[str, Any]] = []
    tier_count_dictionary: dict[str, dict[str, int]] = {
        split_name: {
            "supported_core": 0,
            "supported_sparse_or_corner": 0,
            "unsupported_extrapolation": 0,
        }
        for split_name in ("train", "validation", "test")
    }
    finite_prediction_count = 0
    for record_index, record in enumerate(forward_record_list):
        predicted_curve, _ = predict_surface_curve(refit_surface, record)
        finite_prediction = bool(np.all(np.isfinite(predicted_curve)))
        finite_prediction_count += int(finite_prediction)
        nearest_distance = float(nearest_distance_array[record_index])
        if not bool(inside_axis_box_mask[record_index]):
            support_tier = "unsupported_extrapolation"
        elif nearest_distance <= supported_distance_threshold:
            support_tier = "supported_core"
        else:
            support_tier = "supported_sparse_or_corner"
        tier_count_dictionary[record.split][support_tier] += 1
        condition_row_list.append(
            {
                "condition_id": record.condition_id,
                "split": record.split,
                "measured_torque_nm": record.measured_torque_nm,
                "absolute_measured_speed_rpm": abs(
                    record.measured_speed_rpm
                ),
                "measured_temperature_deg_c": (
                    record.measured_temperature_deg_c
                ),
                "inside_training_axis_box": bool(
                    inside_axis_box_mask[record_index]
                ),
                "nearest_standardized_training_distance": (
                    nearest_distance
                ),
                "supported_distance_threshold": (
                    supported_distance_threshold
                ),
                "support_tier": support_tier,
                "prediction_finite": finite_prediction,
            }
        )

    # Stress Every Envelope Center/Face/Corner Grid Point
    stress_level_matrix = np.column_stack(
        (
            feature_minimum,
            refit_surface.feature_mean,
            feature_maximum,
        )
    )
    envelope_grid_feature_list = []
    for level_index_tuple in product(range(3), repeat=3):
        envelope_grid_feature_list.append(
            np.asarray(
                [
                    stress_level_matrix[feature_index, level_index]
                    for feature_index, level_index in enumerate(
                        level_index_tuple
                    )
                ],
                dtype=np.float64,
            )
        )
    envelope_grid_feature_matrix = np.vstack(envelope_grid_feature_list)
    envelope_grid_coefficient_matrix = refit_surface.predict(
        envelope_grid_feature_matrix
    )
    assert np.all(np.isfinite(envelope_grid_coefficient_matrix)), (
        "PF-A produced non-finite coefficients inside the deployment envelope"
    )

    # Build Deployable Envelope Summary
    feature_name_list = [
        "signed_torque_nm",
        "absolute_speed_rpm",
        "temperature_deg_c",
    ]
    envelope_summary = {
        "schema_version": 1,
        "dataset": "polished_dataset",
        "input_mode": "setpoints",
        "surface": "Fw",
        "fit_scope": "frozen training split only",
        "feature_order": feature_name_list,
        "axis_bound_dictionary": {
            feature_name: {
                "minimum": float(feature_minimum[feature_index]),
                "mean": float(
                    refit_surface.feature_mean[feature_index]
                ),
                "maximum": float(feature_maximum[feature_index]),
                "scale": float(feature_scale[feature_index]),
            }
            for feature_index, feature_name in enumerate(feature_name_list)
        },
        "supported_distance_threshold": supported_distance_threshold,
        "supported_distance_derivation": (
            "training-only P95 leave-one-out nearest standardized distance"
        ),
        "tier_definition_dictionary": {
            "supported_core": (
                "inside every training axis bound and no farther than the "
                "train-only density threshold"
            ),
            "supported_sparse_or_corner": (
                "inside every axis bound but farther than the train-only "
                "density threshold"
            ),
            "unsupported_extrapolation": (
                "outside at least one measured training axis bound"
            ),
        },
        "tier_count_by_split": tier_count_dictionary,
        "eligible_forward_condition_count": len(forward_record_list),
        "finite_prediction_count": finite_prediction_count,
        "envelope_grid_point_count": len(envelope_grid_feature_list),
        "envelope_grid_finite": True,
        "deployment_rule": (
            "Use PF-A as a qualified anchor only in supported_core. Treat "
            "supported_sparse_or_corner as low-trust and route "
            "unsupported_extrapolation to fallback or explicit review."
        ),
    }
    return condition_row_list, envelope_summary


def create_variant_plot(variant_row_list: Sequence[dict[str, Any]]) -> None:

    """Create a compact forward-variant metric comparison."""

    # Resolve Stable Plot Order
    sorted_variant_row_list = sorted(
        variant_row_list,
        key=lambda row: float(row["mae_deg_mean"]),
    )
    model_label_list = [
        str(row["model_id"]).replace("_QUADRATIC", "").replace("PF_", "PF-")
        for row in sorted_variant_row_list
    ]
    raw_mae_array = np.asarray(
        [row["mae_deg_mean"] for row in sorted_variant_row_list],
        dtype=np.float64,
    )
    centered_mae_array = np.asarray(
        [row["centered_mae_deg_mean"] for row in sorted_variant_row_list],
        dtype=np.float64,
    )
    offset_error_array = np.asarray(
        [
            row["offset_abs_error_deg_mean"]
            for row in sorted_variant_row_list
        ],
        dtype=np.float64,
    )

    # Draw Grouped Metric Bars
    figure, axis = plt.subplots(figsize=(12.0, 6.4))
    x_position_array = np.arange(len(model_label_list))
    bar_width = 0.25
    axis.bar(
        x_position_array - bar_width,
        raw_mae_array,
        width=bar_width,
        label="Raw MAE",
        color="#274690",
    )
    axis.bar(
        x_position_array,
        centered_mae_array,
        width=bar_width,
        label="Centered MAE",
        color="#4F80C1",
    )
    axis.bar(
        x_position_array + bar_width,
        offset_error_array,
        width=bar_width,
        label="Offset error",
        color="#72B7B2",
    )
    axis.set_xticks(x_position_array)
    axis.set_xticklabels(model_label_list, rotation=25, ha="right")
    axis.set_ylabel("Held-out error [deg]")
    axis.set_title("Stage 3 Forward Analytical Variant Comparison")
    axis.grid(axis="y", alpha=0.25)
    axis.legend()
    figure.tight_layout()
    figure.savefig(VARIANT_PLOT_PATH, dpi=180)
    plt.close(figure)


def create_stability_plot(
    bootstrap_repeat_row_list: Sequence[dict[str, Any]],
    holdout_row_list: Sequence[dict[str, Any]],
) -> None:

    """Create bootstrap and holdout stability panels."""

    # Prepare Bootstrap Panel
    bootstrap_ratio_array = np.asarray(
        [
            row["test_prediction_deviation_to_base_mae_ratio"]
            for row in bootstrap_repeat_row_list
        ],
        dtype=np.float64,
    )
    sorted_holdout_row_list = sorted(
        holdout_row_list,
        key=lambda row: float(row["mae_ratio_to_full_train_anchor"]),
    )
    holdout_label_list = [
        str(row["holdout_id"]).replace("_", " ")
        for row in sorted_holdout_row_list
    ]
    holdout_ratio_array = np.asarray(
        [
            row["mae_ratio_to_full_train_anchor"]
            for row in sorted_holdout_row_list
        ],
        dtype=np.float64,
    )

    # Draw Complementary Stability Panels
    figure, axis_array = plt.subplots(1, 2, figsize=(14.0, 7.2))
    axis_array[0].hist(
        bootstrap_ratio_array,
        bins=14,
        color="#4F80C1",
        edgecolor="white",
    )
    axis_array[0].axvline(
        np.quantile(bootstrap_ratio_array, 0.95),
        color="#C44E52",
        linestyle="--",
        label="P95",
    )
    axis_array[0].set_xlabel("Prediction deviation / base test MAE")
    axis_array[0].set_ylabel("Bootstrap count")
    axis_array[0].set_title("Deterministic Bootstrap Stability")
    axis_array[0].legend()
    y_position_array = np.arange(len(holdout_label_list))
    axis_array[1].barh(
        y_position_array,
        holdout_ratio_array,
        color="#72B7B2",
    )
    axis_array[1].axvline(
        1.0,
        color="#274690",
        linestyle="--",
        label="Full-train anchor",
    )
    axis_array[1].set_yticks(y_position_array)
    axis_array[1].set_yticklabels(holdout_label_list, fontsize=7)
    axis_array[1].set_xlabel("Holdout MAE / full-train anchor MAE")
    axis_array[1].set_title("Train-Only Axis And Corner Holdouts")
    axis_array[1].legend()
    figure.tight_layout()
    figure.savefig(STABILITY_PLOT_PATH, dpi=180)
    plt.close(figure)


def create_corruption_plot(
    corruption_row_list: Sequence[dict[str, Any]],
) -> None:

    """Create a ranked anchor-corruption sensitivity plot."""

    # Retain Most Material Corruptions
    sorted_corruption_row_list = sorted(
        corruption_row_list,
        key=lambda row: float(row["anchor_deviation_mae_deg_mean"]),
        reverse=True,
    )[:20]
    corruption_label_list = [
        str(row["corruption_id"]).replace("_", " ")
        for row in sorted_corruption_row_list
    ][::-1]
    deviation_array = np.asarray(
        [
            row["anchor_deviation_mae_deg_mean"]
            for row in sorted_corruption_row_list
        ],
        dtype=np.float64,
    )[::-1]
    family_color_map = {
        "coefficient_scale": "#274690",
        "phase_perturbation": "#4F80C1",
        "order_omission": "#72B7B2",
        "operating_input_shift": "#C44E52",
    }
    color_list = [
        family_color_map[str(row["corruption_family"])]
        for row in sorted_corruption_row_list
    ][::-1]

    # Draw Ranked Horizontal Bars
    figure, axis = plt.subplots(figsize=(12.0, 8.0))
    y_position_array = np.arange(len(corruption_label_list))
    axis.barh(
        y_position_array,
        deviation_array,
        color=color_list,
    )
    axis.set_yticks(y_position_array)
    axis.set_yticklabels(corruption_label_list, fontsize=8)
    axis.set_xlabel("Mean absolute deviation from uncorrupted PF-A [deg]")
    axis.set_title("Stage 3 Analytical Anchor Corruption Sensitivity")
    axis.grid(axis="x", alpha=0.25)
    figure.tight_layout()
    figure.savefig(CORRUPTION_PLOT_PATH, dpi=180)
    plt.close(figure)


def main() -> int:

    """Run the complete Stage 3 analytical-anchor qualification workflow."""

    # Prepare Stable Output Directories
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    REPORT_ASSET_DIRECTORY.mkdir(parents=True, exist_ok=True)

    # Load Frozen Configuration, Manifest, And Curves
    configuration = load_yaml(PHASE1_CONFIGURATION_PATH)
    manifest = load_yaml(
        PROJECT_PATH / configuration["inputs"]["paired_manifest"]
    )
    stage0_contract = load_yaml(STAGE0_CONTRACT_PATH)
    split_signature = str(manifest["split"]["assignment_sha256"])
    assert split_signature == EXPECTED_SPLIT_SIGNATURE
    assert stage0_contract["split_contract"]["assignment_sha256"] == (
        EXPECTED_SPLIT_SIGNATURE
    )
    curve_record_list = load_curve_records(configuration, manifest)
    forward_record_list = [
        record
        for record in curve_record_list
        if record.direction == "Fw"
    ]
    training_record_list = [
        record
        for record in forward_record_list
        if record.split == "train"
    ]
    validation_record_list = [
        record
        for record in forward_record_list
        if record.split == "validation"
    ]
    test_record_list = [
        record
        for record in forward_record_list
        if record.split == "test"
    ]
    assert (
        len(training_record_list),
        len(validation_record_list),
        len(test_record_list),
    ) == (675, 194, 97)

    # Refit Canonical PF-A On Frozen Training Only
    local_order_list = configuration["harmonic_order_sets"][
        "local_plc_common"
    ]
    refit_surface = fit_surface_from_records(
        training_record_list,
        local_order_list,
    )
    all_refit_metric_row_list, all_prediction_dictionary = (
        evaluate_surface_on_records(
            model_id="PF_A_LOCAL_QUADRATIC",
            surface=refit_surface,
            record_list=forward_record_list,
            evaluation_order_list=local_order_list,
        )
    )
    test_refit_metric_row_list = [
        row
        for row in all_refit_metric_row_list
        if row["split"] == "test"
    ]
    refit_test_metric_dictionary = aggregate_metric_row_list(
        test_refit_metric_row_list
    )
    test_prediction_dictionary = {
        record.condition_id: all_prediction_dictionary[record.condition_id]
        for record in test_record_list
    }

    # Reproduce Frozen Phase 1 Surface And Metrics
    phase1_coefficient_payload = load_yaml(PHASE1_COEFFICIENT_MODEL_PATH)
    phase1_surface_payload = phase1_coefficient_payload["surface_map"][
        "PF_A_LOCAL_QUADRATIC"
    ]["Fw"]
    phase1_test_metric_row_list = [
        row
        for row in load_csv_row_list(PHASE1_AGGREGATE_METRIC_PATH)
        if row["model_id"] == "PF_A_LOCAL_QUADRATIC"
        and row["split"] == "test"
        and row["direction"] == "Fw"
    ]
    assert len(phase1_test_metric_row_list) == 1
    reproduction_row_list = build_reproduction_evidence(
        refit_surface,
        phase1_surface_payload,
        refit_test_metric_dictionary,
        phase1_test_metric_row_list[0],
    )
    assert all(row["status"] == "pass" for row in reproduction_row_list)

    # Serialize Explicit Refit State
    refit_surface_payload = {
        "schema_version": 1,
        "model_id": "PF_A_LOCAL_QUADRATIC",
        "fit_scope": "frozen Fw training split only",
        "split_signature": split_signature,
        "training_curve_count": len(training_record_list),
        "validation_curve_count": len(validation_record_list),
        "test_curve_count": len(test_record_list),
        "coefficient_label_list": build_coefficient_label_list(
            local_order_list
        ),
        "surface": surface_to_payload(refit_surface),
    }
    REFIT_SURFACE_PATH.write_text(
        yaml.safe_dump(refit_surface_payload, sort_keys=False),
        encoding="utf-8",
        newline="\n",
    )
    write_explicit_coefficient_surface_rows(refit_surface)
    write_csv_rows(REPRODUCTION_PATH, reproduction_row_list)

    # Compare Required Forward Analytical Variants
    variant_row_list = evaluate_forward_variant_roster(
        configuration,
        forward_record_list,
        training_record_list,
        test_record_list,
        test_prediction_dictionary,
    )
    write_csv_rows(VARIANT_PATH, variant_row_list)

    # Run Coefficient And Prediction Stability Tests
    (
        bootstrap_repeat_row_list,
        bootstrap_target_row_list,
        bootstrap_summary,
    ) = run_bootstrap_stability_analysis(
        refit_surface,
        training_record_list,
        test_record_list,
        test_prediction_dictionary,
        float(refit_test_metric_dictionary["mae_deg_mean"]),
    )
    write_csv_rows(BOOTSTRAP_REPEAT_PATH, bootstrap_repeat_row_list)
    write_csv_rows(BOOTSTRAP_TARGET_PATH, bootstrap_target_row_list)

    # Run Train-Only Holdouts And Anchor Corruptions
    holdout_row_list = run_train_only_holdout_analysis(
        refit_surface,
        training_record_list,
    )
    write_csv_rows(HOLDOUT_PATH, holdout_row_list)
    corruption_row_list = run_anchor_corruption_analysis(
        refit_surface,
        test_record_list,
        test_prediction_dictionary,
    )
    write_csv_rows(CORRUPTION_PATH, corruption_row_list)

    # Build Deployment Validity Envelope
    envelope_condition_row_list, envelope_summary = build_validity_envelope(
        refit_surface,
        forward_record_list,
        training_record_list,
    )
    write_csv_rows(ENVELOPE_CONDITION_PATH, envelope_condition_row_list)
    ENVELOPE_SUMMARY_PATH.write_text(
        yaml.safe_dump(envelope_summary, sort_keys=False),
        encoding="utf-8",
        newline="\n",
    )

    # Create Report-Local Visual Evidence
    create_variant_plot(variant_row_list)
    create_stability_plot(
        bootstrap_repeat_row_list,
        holdout_row_list,
    )
    create_corruption_plot(corruption_row_list)

    # Resolve Exit Gates
    finite_forward_prediction_pass = (
        envelope_summary["finite_prediction_count"]
        == envelope_summary["eligible_forward_condition_count"]
    )
    reproduction_pass = all(
        row["status"] == "pass" for row in reproduction_row_list
    )
    condition_number_pass = (
        refit_surface.design_condition_number
        < BOOTSTRAP_CONDITION_NUMBER_P95_LIMIT
        and bootstrap_summary["condition_number_p95"]
        < BOOTSTRAP_CONDITION_NUMBER_P95_LIMIT
    )
    coefficient_stability_pass = (
        bootstrap_summary["relative_coefficient_delta_p95"]
        < BOOTSTRAP_RELATIVE_COEFFICIENT_DELTA_P95_LIMIT
    )
    prediction_stability_pass = (
        bootstrap_summary[
            "prediction_deviation_to_base_mae_ratio_p95"
        ]
        < BOOTSTRAP_PREDICTION_DEVIATION_TO_BASE_MAE_LIMIT
    )
    holdout_finite_pass = all(
        bool(row["finite"]) for row in holdout_row_list
    )
    corruption_finite_pass = all(
        bool(row["finite"]) for row in corruption_row_list
    )
    variant_finite_pass = all(
        np.isfinite(float(row["mae_deg_mean"]))
        for row in variant_row_list
    )
    gate_dictionary = {
        "split_signature_match": split_signature
        == EXPECTED_SPLIT_SIGNATURE,
        "training_only_refit": True,
        "phase1_reproduction": reproduction_pass,
        "explicit_offset_and_complex_coefficients": (
            len(build_coefficient_label_list(local_order_list))
            == 1 + 2 * len(local_order_list)
        ),
        "condition_number_stability": condition_number_pass,
        "bootstrap_coefficient_stability": coefficient_stability_pass,
        "bootstrap_prediction_stability": prediction_stability_pass,
        "required_forward_variant_roster": len(variant_row_list) == 6,
        "train_only_axis_and_corner_holdouts": (
            len(holdout_row_list) == 17 and holdout_finite_pass
        ),
        "all_corruption_families": (
            {
                row["corruption_family"]
                for row in corruption_row_list
            }
            == {
                "coefficient_scale",
                "phase_perturbation",
                "order_omission",
                "operating_input_shift",
            }
            and corruption_finite_pass
        ),
        "deployable_validity_envelope": bool(
            envelope_summary["envelope_grid_finite"]
        ),
        "finite_all_valid_forward_conditions": (
            finite_forward_prediction_pass and variant_finite_pass
        ),
    }
    assert all(gate_dictionary.values()), (
        "Stage 3 exit gate failed | "
        f"{[name for name, passed in gate_dictionary.items() if not passed]}"
    )

    # Persist Final Summary
    ranked_variant_row_list = sorted(
        variant_row_list,
        key=lambda row: float(row["mae_deg_mean"]),
    )
    worst_holdout_row = max(
        holdout_row_list,
        key=lambda row: float(row["mae_ratio_to_full_train_anchor"]),
    )
    most_sensitive_corruption_row = max(
        corruption_row_list,
        key=lambda row: float(row["anchor_deviation_mae_deg_mean"]),
    )
    exit_gate_summary = {
        "schema_version": 1,
        "stage": (
            "Wave 5.2R Stage 3: Analytical Anchor Reproduction And "
            "Stress Tests"
        ),
        "status": "pass",
        "training_executed": False,
        "split_signature": split_signature,
        "forward_curve_count_by_split": {
            "train": len(training_record_list),
            "validation": len(validation_record_list),
            "test": len(test_record_list),
        },
        "canonical_anchor": "PF_A_LOCAL_QUADRATIC",
        "canonical_anchor_status": "qualified_analytical_component",
        "design_condition_number": (
            refit_surface.design_condition_number
        ),
        "test_mae_deg": refit_test_metric_dictionary["mae_deg_mean"],
        "test_centered_mae_deg": refit_test_metric_dictionary[
            "centered_mae_deg_mean"
        ],
        "test_offset_abs_error_deg": refit_test_metric_dictionary[
            "offset_abs_error_deg_mean"
        ],
        "bootstrap_repeat_count": BOOTSTRAP_REPEAT_COUNT,
        "bootstrap_summary": bootstrap_summary,
        "variant_rank_by_raw_mae": [
            {
                "rank": rank_index,
                "model_id": row["model_id"],
                "mae_deg": row["mae_deg_mean"],
                "deployment_status": row["deployment_status"],
            }
            for rank_index, row in enumerate(
                ranked_variant_row_list,
                start=1,
            )
        ],
        "holdout_count": len(holdout_row_list),
        "worst_holdout": {
            "holdout_id": worst_holdout_row["holdout_id"],
            "mae_deg": worst_holdout_row["holdout_mae_deg"],
            "mae_ratio_to_full_train_anchor": worst_holdout_row[
                "mae_ratio_to_full_train_anchor"
            ],
        },
        "corruption_arm_count": len(corruption_row_list),
        "most_sensitive_corruption": {
            "corruption_id": most_sensitive_corruption_row[
                "corruption_id"
            ],
            "anchor_deviation_mae_deg": (
                most_sensitive_corruption_row[
                    "anchor_deviation_mae_deg_mean"
                ]
            ),
        },
        "validity_envelope": {
            "supported_distance_threshold": (
                envelope_summary["supported_distance_threshold"]
            ),
            "tier_count_by_split": (
                envelope_summary["tier_count_by_split"]
            ),
            "finite_prediction_count": (
                envelope_summary["finite_prediction_count"]
            ),
        },
        "gate_dictionary": gate_dictionary,
        "gate_count": len(gate_dictionary),
        "gate_pass_count": sum(gate_dictionary.values()),
        "artifact_dictionary": {
            "refit_surface": REFIT_SURFACE_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "coefficient_surfaces": REFIT_COEFFICIENT_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "reproduction": REPRODUCTION_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "variant_comparison": VARIANT_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "bootstrap_repeats": BOOTSTRAP_REPEAT_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "bootstrap_targets": BOOTSTRAP_TARGET_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "holdouts": HOLDOUT_PATH.relative_to(PROJECT_PATH).as_posix(),
            "corruptions": CORRUPTION_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "envelope_conditions": ENVELOPE_CONDITION_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "envelope_summary": ENVELOPE_SUMMARY_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "variant_plot": VARIANT_PLOT_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "stability_plot": STABILITY_PLOT_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
            "corruption_plot": CORRUPTION_PLOT_PATH.relative_to(
                PROJECT_PATH
            ).as_posix(),
        },
        "conclusion": (
            "PF-A exactly reproduces Phase 1, remains finite across every "
            "eligible forward condition, and is qualified as a bounded "
            "analytical component inside the declared support envelope. "
            "Alternative and corrupted formulations remain comparators."
        ),
    }
    EXIT_GATE_PATH.write_text(
        json.dumps(exit_gate_summary, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    print(
        "WAVE52R_STAGE3_RUN_OK "
        f"forward_curves={len(forward_record_list)} "
        f"variants={len(variant_row_list)} "
        f"holdouts={len(holdout_row_list)} "
        f"corruptions={len(corruption_row_list)} "
        f"gates={sum(gate_dictionary.values())}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
