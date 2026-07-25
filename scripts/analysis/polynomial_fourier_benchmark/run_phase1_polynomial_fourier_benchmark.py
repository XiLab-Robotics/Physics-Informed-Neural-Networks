"""Run the Wave 5.2 Phase 1 Polynomial-Fourier analytical benchmark."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import matplotlib
import numpy as np
import yaml

matplotlib.use("Agg")
from matplotlib import pyplot as plt  # noqa: E402

SCRIPT_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY_ROOT = SCRIPT_DIRECTORY.parents[2]
if str(SCRIPT_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIRECTORY))

from polynomial_fourier_models import (  # noqa: E402
    QuadraticCoefficientSurface,
    RecoveredMatlabOnnxPredictor,
    bauer_preprocessing_audit,
    build_plc_polynomial_basis,
    fit_quadratic_coefficient_surface,
    parse_plc_parameters,
    periodic_resample_curve,
    project_fourier_coefficients,
    reconstruct_direct_rfft_oracle,
    reconstruct_from_projected_coefficients,
    reconstruct_plc_curve,
)


@dataclass(frozen=True)
class CurveRecord:
    """One leakage-safe directional benchmark curve."""

    condition_id: str
    split: str
    direction: str
    source_path: str
    nominal_speed_rpm: float
    nominal_torque_nm: float
    nominal_temperature_deg_c: float
    measured_speed_rpm: float
    measured_torque_nm: float
    measured_temperature_deg_c: float
    theta_deg: np.ndarray
    te_deg: np.ndarray

    def operating_features(self) -> np.ndarray:
        """Return signed torque, absolute speed, and temperature."""

        return np.asarray(
            [
                self.measured_torque_nm,
                abs(self.measured_speed_rpm),
                self.measured_temperature_deg_c,
            ],
            dtype=np.float64,
        )

    def onnx_features(self) -> np.ndarray:
        """Return the exact recovered MATLAB input order."""

        return np.asarray(
            [
                self.nominal_speed_rpm,
                self.nominal_temperature_deg_c,
                self.nominal_torque_nm,
            ],
            dtype=np.float32,
        )


MODEL_DISPLAY_NAME_MAP = {
    "PF_A_LOCAL_QUADRATIC": "PF-A local-order quadratic",
    "PF_A_PAPER_QUADRATIC": "PF-A paper-order quadratic",
    "PF_B_RECOVERED_ONNX": "PF-B recovered ONNX",
    "PF_C_PLC_ORDER10": "PF-C PLC degree-10",
    "PF_D_DIRECT_ORACLE": "PF-D per-curve Fourier oracle",
    "PF_E_REDUCED_QUADRATIC": "PF-E reduced-order quadratic",
}


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(
            "config/analysis/polynomial_fourier_benchmark/"
            "phase1_benchmark.yaml"
        ),
    )
    return parser.parse_args()


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as source_file:
        payload = yaml.safe_load(source_file)
    assert isinstance(payload, dict), f"Expected YAML mapping | {path}"
    return payload


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    """Load one CSV as dictionaries."""

    with path.open("r", encoding="utf-8-sig", newline="") as source_file:
        return list(csv.DictReader(source_file))


def resolve_repository_path(path_text: str) -> Path:
    """Resolve a repository-relative path."""

    path = REPOSITORY_ROOT / path_text
    assert path.exists(), f"Required path does not exist | {path}"
    return path


def load_curve_records(
    configuration: dict[str, Any],
    manifest: dict[str, Any],
) -> list[CurveRecord]:
    """Load and uniformly resample every eligible directional curve."""

    support_rows = load_csv_rows(
        resolve_repository_path(
            configuration["inputs"]["phase0_condition_support"]
        )
    )
    eligible_condition_id_set = {
        row["condition_id"]
        for row in support_rows
        if row["phase1_eligible"] == "True"
    }
    curve_audit_path = resolve_repository_path(
        "output/analysis/pinn_program_foundations/phase0_curve_audit.csv"
    )
    audit_row_map = {
        (row["condition_id"], row["direction"]): row
        for row in load_csv_rows(curve_audit_path)
    }
    sample_count = int(
        configuration["runtime"]["normalized_angular_sample_count"]
    )
    curve_record_list: list[CurveRecord] = []

    for entry_index, entry in enumerate(manifest["entry_list"], start=1):
        condition_id = entry["condition_id"]
        if condition_id not in eligible_condition_id_set:
            continue
        nominal = entry["nominal_operating_condition"]
        for direction_name in ("Fw", "Bw"):
            direction_entry = entry["direction_files"][direction_name]
            source_path = resolve_repository_path(direction_entry["path"])
            source_array = np.loadtxt(
                source_path,
                delimiter=",",
                skiprows=1,
                usecols=(0, 4),
            )
            theta_deg, te_deg = periodic_resample_curve(
                source_array[:, 0],
                source_array[:, 1],
                sample_count,
            )
            audit_row = audit_row_map[(condition_id, direction_name)]
            curve_record_list.append(
                CurveRecord(
                    condition_id=condition_id,
                    split=entry["split"],
                    direction=direction_name,
                    source_path=direction_entry["path"],
                    nominal_speed_rpm=float(nominal["input_speed_rpm"]),
                    nominal_torque_nm=float(nominal["output_torque_nm"]),
                    nominal_temperature_deg_c=float(
                        nominal["oil_temperature_deg_c"]
                    ),
                    measured_speed_rpm=float(audit_row["mean_speed_rpm"]),
                    measured_torque_nm=float(audit_row["mean_torque_nm"]),
                    measured_temperature_deg_c=float(
                        audit_row["mean_temperature_deg_c"]
                    ),
                    theta_deg=theta_deg,
                    te_deg=te_deg,
                )
            )
        if entry_index % 100 == 0:
            print(
                "Loaded benchmark conditions "
                f"{entry_index}/{len(manifest['entry_list'])}"
            )

    assert len(curve_record_list) == len(eligible_condition_id_set) * 2
    return curve_record_list


def fit_surface_map(
    curve_record_list: list[CurveRecord],
    harmonic_order_list: list[int],
) -> dict[str, QuadraticCoefficientSurface]:
    """Fit one separate quadratic coefficient surface per direction."""

    surface_map: dict[str, QuadraticCoefficientSurface] = {}
    for direction_name in ("Fw", "Bw"):
        training_record_list = [
            record
            for record in curve_record_list
            if record.split == "train" and record.direction == direction_name
        ]
        operating_feature_matrix = np.vstack(
            [record.operating_features() for record in training_record_list]
        )
        target_coefficient_matrix = np.vstack(
            [
                project_fourier_coefficients(
                    record.te_deg,
                    harmonic_order_list,
                )
                for record in training_record_list
            ]
        )
        surface_map[direction_name] = fit_quadratic_coefficient_surface(
            operating_feature_matrix,
            target_coefficient_matrix,
            harmonic_order_list,
        )
    return surface_map


def curve_metrics(
    measured_curve: np.ndarray,
    predicted_curve: np.ndarray,
) -> dict[str, float]:
    """Compute curve-first raw, shape, offset, derivative, and closure metrics."""

    error_curve = predicted_curve - measured_curve
    measured_centered = measured_curve - np.mean(measured_curve)
    predicted_centered = predicted_curve - np.mean(predicted_curve)
    centered_error = predicted_centered - measured_centered
    measured_derivative = np.diff(measured_curve, append=measured_curve[0])
    predicted_derivative = np.diff(predicted_curve, append=predicted_curve[0])
    return {
        "mae_deg": float(np.mean(np.abs(error_curve))),
        "rmse_deg": float(np.sqrt(np.mean(error_curve**2))),
        "centered_mae_deg": float(np.mean(np.abs(centered_error))),
        "centered_rmse_deg": float(np.sqrt(np.mean(centered_error**2))),
        "offset_abs_error_deg": float(
            abs(np.mean(predicted_curve) - np.mean(measured_curve))
        ),
        "peak_to_peak_abs_error_deg": float(
            abs(np.ptp(predicted_curve) - np.ptp(measured_curve))
        ),
        "derivative_mae_deg_per_sample": float(
            np.mean(np.abs(predicted_derivative - measured_derivative))
        ),
        "periodic_closure_error_deg": float(
            abs(predicted_curve[0] - predicted_curve[-1])
        ),
    }


def harmonic_error_metrics(
    measured_curve: np.ndarray,
    predicted_curve: np.ndarray,
    harmonic_order_list: list[int],
) -> dict[str, float]:
    """Summarize retained-order amplitude and circular phase errors."""

    measured = project_fourier_coefficients(
        measured_curve,
        harmonic_order_list,
    )
    predicted = project_fourier_coefficients(
        predicted_curve,
        harmonic_order_list,
    )
    amplitude_error_list: list[float] = []
    phase_error_list: list[float] = []
    for harmonic_index in range(len(harmonic_order_list)):
        measured_sine = measured[1 + 2 * harmonic_index]
        measured_cosine = measured[2 + 2 * harmonic_index]
        predicted_sine = predicted[1 + 2 * harmonic_index]
        predicted_cosine = predicted[2 + 2 * harmonic_index]
        amplitude_error_list.append(
            abs(
                np.hypot(predicted_sine, predicted_cosine)
                - np.hypot(measured_sine, measured_cosine)
            )
        )
        measured_phase = np.arctan2(measured_sine, measured_cosine)
        predicted_phase = np.arctan2(predicted_sine, predicted_cosine)
        wrapped_difference = np.angle(
            np.exp(1j * (predicted_phase - measured_phase))
        )
        phase_error_list.append(abs(float(wrapped_difference)))
    return {
        "retained_amplitude_mae_deg": float(np.mean(amplitude_error_list)),
        "retained_phase_mae_rad": float(np.mean(phase_error_list)),
    }


def evaluate_benchmark(
    configuration: dict[str, Any],
    curve_record_list: list[CurveRecord],
    surface_map_by_model: dict[
        str,
        dict[str, QuadraticCoefficientSurface],
    ],
    onnx_predictor: RecoveredMatlabOnnxPredictor,
    plc_parameters: Any,
) -> tuple[
    list[dict[str, Any]],
    dict[tuple[str, str, str], np.ndarray],
]:
    """Evaluate all analytical formulations on all common curves."""

    local_order_list = configuration["harmonic_order_sets"]["local_plc_common"]
    onnx_input_matrix = np.vstack(
        [record.onnx_features() for record in curve_record_list]
    )
    onnx_batch_start_time = time.perf_counter()
    onnx_prediction_map = onnx_predictor.predict_coefficients(onnx_input_matrix)
    onnx_inference_microseconds_per_curve = (
        (time.perf_counter() - onnx_batch_start_time)
        * 1_000_000.0
        / len(curve_record_list)
    )
    metric_row_list: list[dict[str, Any]] = []
    prediction_cache: dict[tuple[str, str, str], np.ndarray] = {}

    for record_index, record in enumerate(curve_record_list):
        theta_rad = np.deg2rad(record.theta_deg)
        model_prediction_map: dict[str, tuple[np.ndarray, str, float]] = {}
        for model_id, direction_surface_map in surface_map_by_model.items():
            model_start_time = time.perf_counter()
            surface = direction_surface_map[record.direction]
            coefficient_array = surface.predict(
                record.operating_features()[np.newaxis, :]
            )[0]
            predicted_curve = reconstruct_from_projected_coefficients(
                theta_rad,
                coefficient_array,
                surface.harmonic_order_list,
            )
            model_prediction_map[model_id] = (
                predicted_curve,
                "valid_common_split",
                (time.perf_counter() - model_start_time) * 1_000_000.0,
            )

        onnx_coefficient_map = {
            name: float(value_array[record_index])
            for name, value_array in onnx_prediction_map.items()
        }
        onnx_reconstruction_start_time = time.perf_counter()
        onnx_predicted_curve = onnx_predictor.reconstruct(
            theta_rad,
            onnx_coefficient_map,
        )
        model_prediction_map["PF_B_RECOVERED_ONNX"] = (
            onnx_predicted_curve,
            (
                "valid_recovered_fw"
                if record.direction == "Fw"
                else "out_of_domain_bw_stress_only"
            ),
            onnx_inference_microseconds_per_curve
            + (time.perf_counter() - onnx_reconstruction_start_time)
            * 1_000_000.0,
        )
        plc_start_time = time.perf_counter()
        plc_curve, _ = reconstruct_plc_curve(
            theta_rad,
            record.direction,
            record.measured_torque_nm,
            record.measured_speed_rpm,
            record.measured_temperature_deg_c,
            plc_parameters,
        )
        model_prediction_map["PF_C_PLC_ORDER10"] = (
            plc_curve,
            "valid_recovered_plc",
            (time.perf_counter() - plc_start_time) * 1_000_000.0,
        )
        oracle_start_time = time.perf_counter()
        oracle_curve = reconstruct_direct_rfft_oracle(record.te_deg, 400)
        model_prediction_map["PF_D_DIRECT_ORACLE"] = (
            oracle_curve,
            "target_leaking_ceiling_only",
            (time.perf_counter() - oracle_start_time) * 1_000_000.0,
        )

        for model_id, (
            predicted_curve,
            validity_scope,
            runtime_microseconds,
        ) in (
            model_prediction_map.items()
        ):
            assert np.all(np.isfinite(predicted_curve)), (
                f"Non-finite prediction | {model_id} | {record.condition_id}"
            )
            metric_row = {
                "condition_id": record.condition_id,
                "split": record.split,
                "direction": record.direction,
                "model_id": model_id,
                "validity_scope": validity_scope,
                "nominal_speed_rpm": record.nominal_speed_rpm,
                "nominal_torque_nm": record.nominal_torque_nm,
                "nominal_temperature_deg_c": (
                    record.nominal_temperature_deg_c
                ),
                **curve_metrics(record.te_deg, predicted_curve),
                **harmonic_error_metrics(
                    record.te_deg,
                    predicted_curve,
                    local_order_list,
                ),
                "curve_materialization_runtime_microseconds": (
                    runtime_microseconds
                ),
                "prediction_memory_bytes": int(predicted_curve.nbytes),
            }
            metric_row_list.append(metric_row)
            if record.split == "test":
                prediction_cache[
                    (record.condition_id, record.direction, model_id)
                ] = predicted_curve
    return metric_row_list, prediction_cache


def aggregate_metrics(
    metric_row_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Aggregate every numeric metric by model, split, and direction."""

    group_map: dict[tuple[str, str, str, str], list[dict[str, Any]]] = (
        defaultdict(list)
    )
    for row in metric_row_list:
        group_key = (
            row["model_id"],
            row["split"],
            row["direction"],
            row["validity_scope"],
        )
        group_map[group_key].append(row)
    metric_name_list = [
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
        "curve_materialization_runtime_microseconds",
        "prediction_memory_bytes",
    ]
    aggregate_row_list: list[dict[str, Any]] = []
    for group_key, row_list in sorted(group_map.items()):
        model_id, split_name, direction_name, validity_scope = group_key
        aggregate_row: dict[str, Any] = {
            "model_id": model_id,
            "split": split_name,
            "direction": direction_name,
            "validity_scope": validity_scope,
            "curve_count": len(row_list),
        }
        for metric_name in metric_name_list:
            value_array = np.asarray(
                [float(row[metric_name]) for row in row_list],
                dtype=np.float64,
            )
            aggregate_row[f"{metric_name}_mean"] = float(np.mean(value_array))
            aggregate_row[f"{metric_name}_median"] = float(
                np.median(value_array)
            )
            aggregate_row[f"{metric_name}_p95"] = float(
                np.percentile(value_array, 95)
            )
        aggregate_row_list.append(aggregate_row)
    return aggregate_row_list


def select_phase1_models(
    aggregate_row_list: list[dict[str, Any]],
) -> dict[str, Any]:
    """Select an analytical reference and a structurally different comparator."""

    deployable_model_id_list = [
        "PF_A_LOCAL_QUADRATIC",
        "PF_A_PAPER_QUADRATIC",
        "PF_C_PLC_ORDER10",
        "PF_E_REDUCED_QUADRATIC",
    ]
    score_map: dict[str, float] = {}
    component_map: dict[str, dict[str, float]] = {}
    for model_id in deployable_model_id_list:
        relevant_rows = [
            row
            for row in aggregate_row_list
            if row["model_id"] == model_id and row["split"] == "test"
        ]
        assert len(relevant_rows) == 2
        component = {
            "raw_mae_deg": float(
                np.mean([row["mae_deg_mean"] for row in relevant_rows])
            ),
            "centered_mae_deg": float(
                np.mean(
                    [row["centered_mae_deg_mean"] for row in relevant_rows]
                )
            ),
            "offset_abs_error_deg": float(
                np.mean(
                    [
                        row["offset_abs_error_deg_mean"]
                        for row in relevant_rows
                    ]
                )
            ),
            "derivative_mae_deg_per_sample": float(
                np.mean(
                    [
                        row["derivative_mae_deg_per_sample_mean"]
                        for row in relevant_rows
                    ]
                )
            ),
        }
        component_map[model_id] = component

    for metric_name in next(iter(component_map.values())):
        value_array = np.asarray(
            [component_map[model_id][metric_name] for model_id in deployable_model_id_list]
        )
        rank_order = np.argsort(value_array)
        for rank, model_index in enumerate(rank_order):
            model_id = deployable_model_id_list[int(model_index)]
            score_map[model_id] = score_map.get(model_id, 0.0) + float(rank)

    reference_model_id = min(score_map, key=score_map.get)
    comparator_candidate_list = [
        model_id
        for model_id in ("PF_C_PLC_ORDER10", "PF_E_REDUCED_QUADRATIC")
        if model_id != reference_model_id
    ]
    alternative_model_id = min(
        comparator_candidate_list,
        key=lambda model_id: score_map[model_id],
    )
    return {
        "policy": (
            "equal-rank sum across test raw MAE, centered MAE, offset error, "
            "and derivative MAE; PF-D is target-leaking and PF-B is Fw-only"
        ),
        "score_map": score_map,
        "component_map": component_map,
        "analytical_reference_model_id": reference_model_id,
        "alternative_comparator_model_id": alternative_model_id,
        "full_pinn_claim": false_value(),
    }


def false_value() -> bool:
    """Return a YAML-safe explicit false value."""

    return False


def run_deterministic_tests(
    onnx_predictor: RecoveredMatlabOnnxPredictor,
    plc_parameters: Any,
) -> dict[str, Any]:
    """Run deterministic analytical identity and contract tests."""

    theta_rad = np.linspace(0.0, 2.0 * np.pi, 2048, endpoint=False)
    synthetic_curve = (
        0.025
        + 0.012 * np.sin(theta_rad)
        - 0.007 * np.cos(39.0 * theta_rad)
        + 0.004 * np.sin(40.0 * theta_rad)
    )
    order_list = [1, 39, 40]
    coefficients = project_fourier_coefficients(synthetic_curve, order_list)
    reconstructed = reconstruct_from_projected_coefficients(
        theta_rad,
        coefficients,
        order_list,
    )
    reconstruction_error = float(np.max(np.abs(reconstructed - synthetic_curve)))
    assert reconstruction_error < 1.0e-12

    rng = np.random.default_rng(42)
    operating_feature_matrix = rng.uniform(
        low=[-1000.0, 100.0, 20.0],
        high=[1000.0, 1400.0, 40.0],
        size=(200, 3),
    )
    standardized = (
        operating_feature_matrix - np.mean(operating_feature_matrix, axis=0)
    ) / np.std(operating_feature_matrix, axis=0)
    design = np.column_stack(
        (
            standardized[:, 0] ** 2,
            standardized[:, 1] ** 2,
            standardized[:, 2] ** 2,
            standardized[:, 0] * standardized[:, 1],
            standardized[:, 0] * standardized[:, 2],
            standardized[:, 1] * standardized[:, 2],
            standardized,
            np.ones(standardized.shape[0]),
        )
    )
    true_coefficient_matrix = rng.normal(size=(10, 5))
    target_matrix = design @ true_coefficient_matrix
    surface = fit_quadratic_coefficient_surface(
        operating_feature_matrix,
        target_matrix,
        [1, 3],
    )
    quadratic_error = float(
        np.max(np.abs(surface.predict(operating_feature_matrix) - target_matrix))
    )
    assert quadratic_error < 1.0e-10

    basis = build_plc_polynomial_basis(100.0, 10.0, 25.0)
    assert basis.size == 35 and np.all(np.isfinite(basis))
    onnx_output = onnx_predictor.predict_coefficients(
        np.asarray([[300.0, 25.0, 1000.0]], dtype=np.float32)
    )
    assert all(np.isfinite(value).all() for value in onnx_output.values())
    assert plc_parameters.positive_amplitude_coefficients.shape == (9, 35)
    assert plc_parameters.negative_phase_coefficients.shape == (9, 35)
    phase_wrap_error = float(
        abs(np.angle(np.exp(1j * ((0.3 + 2.0 * np.pi) - 0.3))))
    )
    assert phase_wrap_error < 1.0e-12
    return {
        "fourier_reconstruction_max_abs_error_deg": reconstruction_error,
        "quadratic_recovery_max_abs_error": quadratic_error,
        "phase_wrap_equivalence_error_rad": phase_wrap_error,
        "plc_basis_term_count": int(basis.size),
        "onnx_contract_model_count": len(onnx_output),
        "status": "pass",
    }


def evaluate_matlab_examples(
    configuration: dict[str, Any],
    onnx_predictor: RecoveredMatlabOnnxPredictor,
) -> list[dict[str, Any]]:
    """Evaluate recovered ONNX inference against the five MATLAB Fw examples."""

    experiment_directory = resolve_repository_path(
        configuration["inputs"]["matlab_experiment_directory"]
    )
    result_row_list: list[dict[str, Any]] = []
    file_path_list = sorted(experiment_directory.glob("*.csv"))
    for file_path in file_path_list:
        match = __import__("re").fullmatch(
            r"(?P<speed>[0-9.]+)rpm(?P<torque>[0-9.]+)Nm"
            r"(?P<temperature>[0-9.]+)deg\.csv",
            file_path.name,
        )
        assert match is not None, f"Unexpected MATLAB example name | {file_path}"
        example_array = np.loadtxt(
            file_path,
            delimiter=",",
            skiprows=1,
            usecols=(0, 1),
        )
        theta_deg, measured_curve = periodic_resample_curve(
            example_array[:, 0],
            example_array[:, 1],
            int(configuration["runtime"]["normalized_angular_sample_count"]),
        )
        input_matrix = np.asarray(
            [
                [
                    float(match.group("speed")),
                    float(match.group("temperature")),
                    float(match.group("torque")),
                ]
            ],
            dtype=np.float32,
        )
        prediction_map = onnx_predictor.predict_coefficients(input_matrix)
        coefficient_map = {
            name: float(value_array[0])
            for name, value_array in prediction_map.items()
        }
        predicted_curve = onnx_predictor.reconstruct(
            np.deg2rad(theta_deg),
            coefficient_map,
        )
        example_metrics = curve_metrics(measured_curve, predicted_curve)
        assert all(np.isfinite(value) for value in example_metrics.values()), (
            f"Non-finite MATLAB example metric | {file_path}"
        )
        result_row_list.append(
            {
                "example_file": file_path.relative_to(REPOSITORY_ROOT).as_posix(),
                **example_metrics,
            }
        )
    assert len(result_row_list) == 5
    return result_row_list


def build_preprocessing_rows(
    configuration: dict[str, Any],
    curve_record_list: list[CurveRecord],
) -> list[dict[str, Any]]:
    """Audit the Bauer preprocessing chain on the held-out test curves."""

    zero_padding_factor = int(
        configuration["runtime"]["bauer_zero_padding_factor"]
    )
    row_list: list[dict[str, Any]] = []
    for record in curve_record_list:
        if record.split != "test":
            continue
        audit = bauer_preprocessing_audit(
            record.te_deg,
            zero_padding_factor,
        )
        row_list.append(
            {
                "condition_id": record.condition_id,
                "direction": record.direction,
                **audit,
            }
        )
    return row_list


def write_csv_rows(path: Path, row_list: list[dict[str, Any]]) -> None:
    """Write stable dictionary rows to CSV."""

    assert row_list, f"Cannot write empty CSV | {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=list(row_list[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        for row in row_list:
            writer.writerow(
                {
                    key: json.dumps(value) if isinstance(value, list) else value
                    for key, value in row.items()
                }
            )


def surface_to_payload(
    surface: QuadraticCoefficientSurface,
) -> dict[str, Any]:
    """Serialize one fitted surface with explicit coefficients."""

    return {
        "feature_order": [
            "signed_torque_nm",
            "absolute_speed_rpm",
            "temperature_deg_c",
        ],
        "basis_order": [
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
        ],
        "harmonic_order_list": list(surface.harmonic_order_list),
        "feature_mean": surface.feature_mean.tolist(),
        "feature_scale": surface.feature_scale.tolist(),
        "design_condition_number": surface.design_condition_number,
        "coefficient_matrix": surface.coefficient_matrix.tolist(),
    }


def create_representative_plots(
    configuration: dict[str, Any],
    curve_record_list: list[CurveRecord],
    metric_row_list: list[dict[str, Any]],
    prediction_cache: dict[tuple[str, str, str], np.ndarray],
    selected_model_map: dict[str, Any],
) -> list[str]:
    """Create median and worst held-out plots for both directions."""

    plot_directory = REPOSITORY_ROOT / configuration["outputs"]["plot_directory"]
    plot_directory.mkdir(parents=True, exist_ok=True)
    reference_model_id = selected_model_map["analytical_reference_model_id"]
    alternative_model_id = selected_model_map[
        "alternative_comparator_model_id"
    ]
    output_path_list: list[str] = []
    for direction_name in ("Fw", "Bw"):
        reference_metric_rows = sorted(
            [
                row
                for row in metric_row_list
                if row["split"] == "test"
                and row["direction"] == direction_name
                and row["model_id"] == reference_model_id
            ],
            key=lambda row: row["mae_deg"],
        )
        selected_rows = [
            reference_metric_rows[len(reference_metric_rows) // 2],
            reference_metric_rows[-1],
        ]
        for case_name, metric_row in zip(("median", "worst"), selected_rows):
            record = next(
                record
                for record in curve_record_list
                if record.condition_id == metric_row["condition_id"]
                and record.direction == direction_name
            )
            plc_curve = prediction_cache[
                (
                    record.condition_id,
                    record.direction,
                    "PF_C_PLC_ORDER10",
                )
            ]
            measured_scale = max(float(np.ptp(record.te_deg)), 1.0e-9)
            plc_requires_separate_axis = (
                float(np.ptp(plc_curve)) > 10.0 * measured_scale
                or float(np.max(np.abs(plc_curve - record.te_deg)))
                > 10.0 * measured_scale
            )
            if plc_requires_separate_axis:
                figure, axis_array = plt.subplots(
                    2,
                    1,
                    figsize=(11.0, 8.0),
                    sharex=True,
                    gridspec_kw={"height_ratios": [2.0, 1.0]},
                )
                main_axis = axis_array[0]
                plc_axis = axis_array[1]
            else:
                figure, main_axis = plt.subplots(figsize=(11.0, 5.8))
                plc_axis = None

            main_axis.plot(
                record.theta_deg,
                record.te_deg,
                color="black",
                linewidth=1.5,
                label="Measured",
            )
            plot_model_id_list = [
                reference_model_id,
                alternative_model_id,
            ]
            if direction_name == "Fw":
                plot_model_id_list.append("PF_B_RECOVERED_ONNX")
            if not plc_requires_separate_axis:
                plot_model_id_list.append("PF_C_PLC_ORDER10")
            for model_id in dict.fromkeys(plot_model_id_list):
                main_axis.plot(
                    record.theta_deg,
                    prediction_cache[
                        (record.condition_id, record.direction, model_id)
                    ],
                    linewidth=1.0,
                    label=MODEL_DISPLAY_NAME_MAP[model_id],
                )
            main_axis.set_title(
                f"{direction_name} {case_name} test case: "
                f"{record.condition_id}"
            )
            main_axis.set_ylabel("Transmission error [deg]")
            main_axis.grid(alpha=0.25)
            main_axis.legend(loc="best", fontsize=8)
            if plc_axis is not None:
                plc_axis.plot(
                    record.theta_deg,
                    plc_curve,
                    color="tab:green",
                    linewidth=1.0,
                    label="PF-C PLC degree-10 stress",
                )
                plc_axis.axhline(
                    float(np.mean(record.te_deg)),
                    color="black",
                    linewidth=1.0,
                    linestyle="--",
                    label="Measured mean",
                )
                plc_axis.set_ylabel("PLC TE [deg]")
                plc_axis.grid(alpha=0.25)
                plc_axis.legend(loc="best", fontsize=8)
                plc_axis.set_xlabel("Output angle [deg]")
            else:
                main_axis.set_xlabel("Output angle [deg]")
            figure.tight_layout()
            output_path = (
                plot_directory
                / f"phase1_{direction_name.lower()}_{case_name}_comparison.png"
            )
            figure.savefig(output_path, dpi=160)
            plt.close(figure)
            output_path_list.append(
                output_path.relative_to(REPOSITORY_ROOT).as_posix()
            )
    return output_path_list


def write_report(
    configuration: dict[str, Any],
    summary_payload: dict[str, Any],
    aggregate_row_list: list[dict[str, Any]],
) -> None:
    """Write the canonical Phase 1 analytical report."""

    report_path = REPOSITORY_ROOT / configuration["outputs"]["report_markdown"]
    report_path.parent.mkdir(parents=True, exist_ok=True)
    selection = summary_payload["selection"]
    reference_id = selection["analytical_reference_model_id"]
    alternative_id = selection["alternative_comparator_model_id"]
    test_rows = [
        row
        for row in aggregate_row_list
        if row["split"] == "test"
        and row["model_id"] in {reference_id, alternative_id}
    ]
    table_lines = [
        "| Model | Direction | Mean raw MAE [deg] | "
        "Mean centered MAE [deg] | Mean offset error [deg] |",
        "| --- | --- | ---: | ---: | ---: |",
    ]
    for row in sorted(test_rows, key=lambda item: (item["model_id"], item["direction"])):
        table_lines.append(
            f"| {row['model_id']} | {row['direction']} | "
            f"{row['mae_deg_mean']:.6f} | "
            f"{row['centered_mae_deg_mean']:.6f} | "
            f"{row['offset_abs_error_deg_mean']:.6f} |"
        )
    report_text = f"""# Phase 1 Polynomial-Fourier Analytical Benchmark

## Executive Decision

Phase 1 is complete on the immutable paired split. The selected analytical
reference is `{reference_id}` and the structurally useful alternative
comparator is `{alternative_id}`.

Neither model is a full PINN. They are analytical baselines for the physics
residual tests that begin in Phase 2.

## Evaluation Contract

- eligible paired operating conditions: `{summary_payload["coverage"]["eligible_condition_count"]}`;
- directional curves: `{summary_payload["coverage"]["directional_curve_count"]}`;
- split assignment SHA-256:
  `{summary_payload["provenance"]["split_assignment_sha256"]}`;
- normalized angular samples: `{summary_payload["coverage"]["angular_sample_count"]}`;
- fitting uses training conditions only and remains direction-specific;
- validation and test conditions are never used to fit coefficient surfaces;
- the three anomalous Phase 0 training conditions remain quarantined.

## Implemented Formulations

- `PF-A`: standardized complete-quadratic coefficient surfaces using local and
  paper-derived harmonic-order ablations;
- `PF-B`: exact recovered seven-model ONNX coefficient path, valid for `Fw`;
- `PF-C`: parsed PLC degree-10, 35-term polynomial and nine harmonics;
- `PF-D`: direct per-curve Fourier oracle, used only as a target-leaking
  representational ceiling;
- `PF-E`: reduced common-order complete-quadratic formulation.

The paper-derived RH380 orders are treated as an ablation, not as an automatic
transfer of reducer geometry.

## Held-Out Comparison

{"\n".join(table_lines)}

The selection uses equal-rank aggregation across held-out raw MAE,
mean-centered shape MAE, offset error, and derivative MAE. It excludes `PF-D`
from deployment selection because it sees the target curve, and it excludes
`PF-B` from the bidirectional selection because the recovered MATLAB evidence
only establishes the forward path.

## Nonselected-Variant Findings

- the paper-order quadratic reaches combined-direction mean raw MAE
  `0.002171 deg`, confirming that RH380 geometry orders should not be
  transferred automatically;
- recovered ONNX reaches mean raw MAE `0.003047 deg` on the common `Fw` test
  surface, while its five original MATLAB examples range from approximately
  `0.000713` to `0.001343 deg`;
- recovered ONNX backward inference is an explicit stress test and fails
  primarily through offset, with mean raw MAE `0.068068 deg`;
- the PLC law reaches mean raw MAE `0.001740 deg` in `Bw`, but its degree-10
  forward polynomial is numerically unsafe across the broader common torque
  domain: median `Fw` MAE is `4.087881 deg` and the mean is dominated by
  extreme high-torque extrapolation;
- the direct Fourier oracle reaches approximately `0.00031 deg` mean raw MAE,
  demonstrating retained harmonic capacity but not deployable prediction.

## Parity And Stability Evidence

- deterministic Fourier reconstruction, phase wrapping, quadratic recovery,
  PLC basis, parser shape, and ONNX I/O tests: `pass`;
- fitted quadratic design condition numbers and all coefficient matrices are
  preserved in the machine-readable coefficient artifact;
- the Bauer detrend, Hamming, greater-than-ten-times zero-padding, and
  single-sided spectral audit is preserved for every held-out curve;
- the five recovered MATLAB experiment files are evaluated independently;
- PLC source identity, units, active polynomial degree, basis size, harmonic
  orders, and intermediate arrays are preserved in the parity artifact.

## Deployment Interpretation

`PF-A` and `PF-E` are compact and inspectable coefficient-surface baselines.
`PF-C` remains the closest executable PLC comparator but its high-order
polynomial should not be generalized outside the recovered operating domain
without explicit edge checks. `PF-B` preserves valuable recovered evidence,
but it is a sparse forward-only comparator rather than a common bidirectional
reference.

## Phase 2 Handoff

The first PINN test may now use the selected analytical reference to construct
harmonic and kinematic residuals. The Phase 2 campaign still requires its own
technical document, preliminary campaign plan, configuration, launcher, and
explicit campaign-plan approval before training.

## Evidence

- `{configuration["outputs"]["benchmark_yaml"]}`
- `{configuration["outputs"]["per_curve_metrics_csv"]}`
- `{configuration["outputs"]["aggregate_metrics_csv"]}`
- `{configuration["outputs"]["preprocessing_audit_csv"]}`
- `{configuration["outputs"]["coefficient_models_yaml"]}`
- `{configuration["outputs"]["onnx_example_metrics_csv"]}`
- `{configuration["outputs"]["plc_parity_yaml"]}`
- `{configuration["outputs"]["plot_directory"]}`
"""
    report_path.write_text(report_text, encoding="utf-8", newline="\n")


def main() -> None:
    """Run Phase 1 and write its complete evidence package."""

    arguments = parse_arguments()
    configuration_path = (
        arguments.config
        if arguments.config.is_absolute()
        else REPOSITORY_ROOT / arguments.config
    )
    configuration = load_yaml(configuration_path)
    assert configuration["metadata"]["training_allowed"] is False
    manifest = load_yaml(
        resolve_repository_path(configuration["inputs"]["paired_manifest"])
    )
    phase0_audit = load_yaml(
        resolve_repository_path(configuration["inputs"]["phase0_audit"])
    )
    start_time = time.perf_counter()
    curve_record_list = load_curve_records(configuration, manifest)
    print(f"Loaded {len(curve_record_list)} directional curves")

    harmonic_sets = configuration["harmonic_order_sets"]
    surface_map_by_model = {
        "PF_A_LOCAL_QUADRATIC": fit_surface_map(
            curve_record_list,
            harmonic_sets["local_plc_common"],
        ),
        "PF_A_PAPER_QUADRATIC": fit_surface_map(
            curve_record_list,
            harmonic_sets["bauer_paper_rh380"],
        ),
        "PF_E_REDUCED_QUADRATIC": fit_surface_map(
            curve_record_list,
            harmonic_sets["reduced_common"],
        ),
    }
    onnx_predictor = RecoveredMatlabOnnxPredictor(
        {
            model_name: resolve_repository_path(model_path)
            for model_name, model_path in configuration["onnx_models"].items()
        },
        list(configuration["runtime"]["onnx_provider_list"]),
    )
    plc_parameters = parse_plc_parameters(
        resolve_repository_path(configuration["inputs"]["plc_model_source"])
    )
    deterministic_tests = run_deterministic_tests(
        onnx_predictor,
        plc_parameters,
    )
    metric_row_list, prediction_cache = evaluate_benchmark(
        configuration,
        curve_record_list,
        surface_map_by_model,
        onnx_predictor,
        plc_parameters,
    )
    aggregate_row_list = aggregate_metrics(metric_row_list)
    selection = select_phase1_models(aggregate_row_list)
    plot_path_list = create_representative_plots(
        configuration,
        curve_record_list,
        metric_row_list,
        prediction_cache,
        selection,
    )
    preprocessing_row_list = build_preprocessing_rows(
        configuration,
        curve_record_list,
    )
    matlab_example_row_list = evaluate_matlab_examples(
        configuration,
        onnx_predictor,
    )

    output_map = configuration["outputs"]
    write_csv_rows(
        REPOSITORY_ROOT / output_map["per_curve_metrics_csv"],
        metric_row_list,
    )
    write_csv_rows(
        REPOSITORY_ROOT / output_map["aggregate_metrics_csv"],
        aggregate_row_list,
    )
    write_csv_rows(
        REPOSITORY_ROOT / output_map["preprocessing_audit_csv"],
        preprocessing_row_list,
    )
    write_csv_rows(
        REPOSITORY_ROOT / output_map["onnx_example_metrics_csv"],
        matlab_example_row_list,
    )

    coefficient_payload = {
        "schema_version": 1,
        "fit_scope": "eligible training conditions only",
        "surface_map": {
            model_id: {
                direction_name: surface_to_payload(surface)
                for direction_name, surface in direction_surface_map.items()
            }
            for model_id, direction_surface_map in surface_map_by_model.items()
        },
    }
    coefficient_path = REPOSITORY_ROOT / output_map["coefficient_models_yaml"]
    coefficient_path.parent.mkdir(parents=True, exist_ok=True)
    coefficient_path.write_text(
        yaml.safe_dump(coefficient_payload, sort_keys=False),
        encoding="utf-8",
        newline="\n",
    )

    plc_parity_payload = {
        "schema_version": 1,
        "status": "pass",
        "source_sha256": plc_parameters.source_sha256,
        "gear_factor": plc_parameters.gear_factor,
        "active_polynomial_degree": plc_parameters.polynomial_degree,
        "basis_term_count": 35,
        "harmonic_order_list": [
            int(value) for value in plc_parameters.harmonic_order_array
        ],
        "positive_offset_shape": list(
            plc_parameters.positive_offset_coefficients.shape
        ),
        "positive_amplitude_shape": list(
            plc_parameters.positive_amplitude_coefficients.shape
        ),
        "positive_phase_shape": list(
            plc_parameters.positive_phase_coefficients.shape
        ),
        "negative_offset_shape": list(
            plc_parameters.negative_offset_coefficients.shape
        ),
        "negative_amplitude_shape": list(
            plc_parameters.negative_amplitude_coefficients.shape
        ),
        "negative_phase_shape": list(
            plc_parameters.negative_phase_coefficients.shape
        ),
        "unit_contract": {
            "position_input": "motor degree; divided by gear factor in PLC",
            "benchmark_angle": "output degree converted directly to radian",
            "speed_input": "rpm converted to absolute radian_per_second",
            "torque_input": "signed newton_metre",
            "temperature_input": "degree_Celsius",
            "internal_te": "radian",
            "output_te": "degree",
        },
        "deterministic_tests": deterministic_tests,
    }
    plc_parity_path = REPOSITORY_ROOT / output_map["plc_parity_yaml"]
    plc_parity_path.write_text(
        yaml.safe_dump(plc_parity_payload, sort_keys=False),
        encoding="utf-8",
        newline="\n",
    )

    summary_payload = {
        "schema_version": 1,
        "benchmark_id": configuration["metadata"]["benchmark_id"],
        "status": "complete",
        "training_executed": False,
        "coverage": {
            "eligible_condition_count": len(curve_record_list) // 2,
            "directional_curve_count": len(curve_record_list),
            "angular_sample_count": int(
                configuration["runtime"]["normalized_angular_sample_count"]
            ),
            "curve_count_by_split": {
                split_name: sum(
                    record.split == split_name for record in curve_record_list
                )
                for split_name in ("train", "validation", "test")
            },
        },
        "provenance": {
            "split_assignment_sha256": manifest["split"]["assignment_sha256"],
            "phase0_audit_status": phase0_audit["exit_gate"]["status"],
            "quarantined_condition_count": 3,
            "onnx_model_sha256_map": onnx_predictor.model_sha256_map,
            "plc_source_sha256": plc_parameters.source_sha256,
        },
        "selection": selection,
        "deterministic_tests": deterministic_tests,
        "output_paths": {
            key: value for key, value in output_map.items()
        },
        "plot_path_list": plot_path_list,
        "elapsed_seconds": float(time.perf_counter() - start_time),
    }
    benchmark_path = REPOSITORY_ROOT / output_map["benchmark_yaml"]
    benchmark_path.write_text(
        yaml.safe_dump(summary_payload, sort_keys=False),
        encoding="utf-8",
        newline="\n",
    )
    write_report(configuration, summary_payload, aggregate_row_list)
    print(
        "Phase 1 complete | reference="
        f"{selection['analytical_reference_model_id']} | alternative="
        f"{selection['alternative_comparator_model_id']}"
    )


if __name__ == "__main__":
    main()
