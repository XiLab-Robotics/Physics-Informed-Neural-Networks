"""Prepare the Wave 5.2R Stage 4 data-only residual capacity campaign."""

from __future__ import annotations

# Import Python Utilities
from copy import deepcopy
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
import yaml

# Import Polynomial-Fourier Benchmark Utilities
from scripts.analysis.polynomial_fourier_benchmark.polynomial_fourier_models import (
    QuadraticCoefficientSurface,
    fit_quadratic_coefficient_surface,
    project_fourier_coefficients,
    reconstruct_from_projected_coefficients,
)
from scripts.analysis.polynomial_fourier_benchmark.run_phase1_polynomial_fourier_benchmark import (
    CurveRecord,
    curve_metrics,
    load_curve_records,
    load_yaml,
)


# Define Campaign Constants
CAMPAIGN_NAME = "wave52r_stage4_data_only_residual_capacity_2026_07_28"
CAMPAIGN_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "data_only_residual_capacity"
    / "campaigns"
    / "2026-07-28_wave52r_stage4_data_only_residual_capacity"
)
QUEUE_DIRECTORY = CAMPAIGN_DIRECTORY / "queue"
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage4_data_only_residual_capacity_ladder"
)
CAUSAL_ANCHOR_PATH = (
    ANALYSIS_DIRECTORY / "stage4_causal_setpoint_pf_a_surface.yaml"
)
CALIBRATION_PATH = (
    ANALYSIS_DIRECTORY / "stage4_training_only_calibration.yaml"
)
PHASE1_CONFIGURATION_PATH = (
    PROJECT_ROOT
    / "config"
    / "analysis"
    / "polynomial_fourier_benchmark"
    / "phase1_benchmark.yaml"
)
COMMON_SPLIT_MANIFEST_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "polynomial_fourier_benchmark"
    / "common_split_manifest.yaml"
)
LEGACY_STAGE3_ANCHOR_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage3_analytical_anchor_reproduction_and_stress_tests"
    / "stage3_pf_a_refit_surface.yaml"
)
PLANNING_REPORT_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "data_only_residual_capacity_ladder/"
    "2026-07-27-22-39-42_wave52r_stage4_data_only_residual_capacity_"
    "ladder_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-27/"
    "2026-07-27-22-37-41_wave52r_stage4_data_only_residual_capacity_"
    "ladder.md"
)
MODEL_REPORT_PATH = (
    "doc/reports/analysis/model_development_waves/wave_5_2/"
    "physics_guided_pinn_reassessment/[2026-07-28]/"
    "stage4_data_only_residual_capacity_ladder/"
    "stage4_data_only_residual_capacity_model_report.md"
)
COMMON_SPLIT_SIGNATURE = (
    "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f"
    "4376aa64f8e16"
)
HARMONIC_INDEX_LIST = [1, 3, 39, 40, 78, 81, 156, 162, 240]
EXCLUDED_CONDITION_ID_LIST = [
    "speed_500rpm__torque_600Nm__temperature_35degC",
    "speed_800rpm__torque_200Nm__temperature_25degC",
    "speed_1400rpm__torque_800Nm__temperature_35degC",
]


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping with a normal final newline."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def build_setpoint_operating_feature_array(
    record: CurveRecord,
) -> np.ndarray:
    """Return the causal torque, speed, and temperature setpoint vector."""

    signed_torque_nm = -abs(record.nominal_torque_nm)
    return np.asarray(
        [
            signed_torque_nm,
            abs(record.nominal_speed_rpm),
            record.nominal_temperature_deg_c,
        ],
        dtype=np.float64,
    )


def build_surface_from_payload(
    surface_payload: dict[str, Any],
) -> QuadraticCoefficientSurface:
    """Recreate one immutable Polynomial-Fourier coefficient surface."""

    return QuadraticCoefficientSurface(
        feature_mean=np.asarray(
            surface_payload["feature_mean"],
            dtype=np.float64,
        ),
        feature_scale=np.asarray(
            surface_payload["feature_scale"],
            dtype=np.float64,
        ),
        coefficient_matrix=np.asarray(
            surface_payload["coefficient_matrix"],
            dtype=np.float64,
        ),
        harmonic_order_list=tuple(
            int(value)
            for value in surface_payload["harmonic_order_list"]
        ),
        design_condition_number=float(
            surface_payload["design_condition_number"]
        ),
    )


def predict_curve(
    surface: QuadraticCoefficientSurface,
    record: CurveRecord,
    use_setpoints: bool,
) -> np.ndarray:
    """Predict one curve from causal setpoints or legacy measured features."""

    operating_feature_array = (
        build_setpoint_operating_feature_array(record)
        if use_setpoints
        else record.operating_features()
    )
    coefficient_array = surface.predict(
        operating_feature_array[np.newaxis, :]
    )[0]
    return reconstruct_from_projected_coefficients(
        np.deg2rad(record.theta_deg),
        coefficient_array,
        list(surface.harmonic_order_list),
    )


def aggregate_curve_metrics(
    surface: QuadraticCoefficientSurface,
    record_list: list[CurveRecord],
    use_setpoints: bool,
) -> dict[str, float]:
    """Aggregate full-curve errors for one declared operating-input path."""

    metric_row_list = [
        curve_metrics(
            record.te_deg,
            predict_curve(surface, record, use_setpoints),
        )
        for record in record_list
    ]
    return {
        metric_name: float(
            np.mean([row[metric_name] for row in metric_row_list])
        )
        for metric_name in metric_row_list[0]
    }


def fit_causal_setpoint_surface(
    training_record_list: list[CurveRecord],
) -> QuadraticCoefficientSurface:
    """Fit PF-A with training-only causal setpoint operating variables."""

    operating_feature_matrix = np.vstack(
        [
            build_setpoint_operating_feature_array(record)
            for record in training_record_list
        ]
    )
    coefficient_target_matrix = np.vstack(
        [
            project_fourier_coefficients(
                record.te_deg,
                HARMONIC_INDEX_LIST,
            )
            for record in training_record_list
        ]
    )
    return fit_quadratic_coefficient_surface(
        operating_feature_matrix,
        coefficient_target_matrix,
        HARMONIC_INDEX_LIST,
    )


def select_training_only_residual_basis(
    surface: QuadraticCoefficientSurface,
    training_record_list: list[CurveRecord],
) -> tuple[list[int], float, dict[str, float]]:
    """Select four residual orders and one hard bound from training only."""

    mean_amplitude_by_order = np.zeros(241, dtype=np.float64)
    residual_value_list: list[np.ndarray] = []
    for record in training_record_list:
        residual_curve = record.te_deg - predict_curve(
            surface,
            record,
            use_setpoints=True,
        )
        residual_value_list.append(residual_curve)
        spectrum = np.fft.rfft(residual_curve)
        maximum_order = min(240, spectrum.size - 1)
        mean_amplitude_by_order[: maximum_order + 1] += (
            2.0
            * np.abs(spectrum[: maximum_order + 1])
            / residual_curve.size
        )
    mean_amplitude_by_order /= len(training_record_list)
    mean_amplitude_by_order[0] = 0.0
    mean_amplitude_by_order[HARMONIC_INDEX_LIST] = 0.0
    selected_order_list = sorted(
        np.argsort(mean_amplitude_by_order)[-4:].astype(int).tolist()
    )
    residual_value_array = np.concatenate(residual_value_list)
    residual_bound_deg = float(
        np.quantile(np.abs(residual_value_array), 0.995)
    )
    residual_statistics = {
        "training_residual_rms_deg": float(
            np.sqrt(np.mean(np.square(residual_value_array)))
        ),
        "training_residual_abs_p95_deg": float(
            np.quantile(np.abs(residual_value_array), 0.95)
        ),
        "training_residual_abs_p995_deg": residual_bound_deg,
        "training_residual_abs_max_deg": float(
            np.max(np.abs(residual_value_array))
        ),
    }
    return selected_order_list, residual_bound_deg, residual_statistics


def count_trainable_parameters(
    formulation: str,
    hidden_size: list[int],
    residual_basis_order_count: int,
) -> int:
    """Compute the learned-branch parameter count without importing PyTorch."""

    if formulation in {"R1", "R2", "R3"}:
        # 18 sine/cosine values plus speed, torque, temperature, direction.
        input_width = 22
        output_width = 1
    elif formulation == "R4":
        input_width = 4
        output_width = 1 + (2 * residual_basis_order_count)
    else:
        input_width = 4
        output_width = 1 + (2 * len(HARMONIC_INDEX_LIST))

    parameter_count = 0
    previous_width = input_width
    for current_width in hidden_size:
        parameter_count += (previous_width + 1) * current_width
        previous_width = current_width
    parameter_count += (previous_width + 1) * output_width
    return parameter_count


def build_candidate_specification_list() -> list[dict[str, Any]]:
    """Declare the immutable eighteen-run Stage 4 screening roster."""

    return [
        {"id": "C01", "formulation": "R1", "capacity": "compact", "hidden": [32, 32], "matched": "H01,H03"},
        {"id": "C02", "formulation": "R1", "capacity": "deep", "hidden": [64, 64, 32], "matched": "H02,H04"},
        {"id": "C03", "formulation": "R1", "capacity": "compact", "hidden": [28, 28], "matched": "H05"},
        {"id": "C04", "formulation": "R1", "capacity": "deep", "hidden": [60, 60, 30], "matched": "H06"},
        {"id": "C05", "formulation": "R1", "capacity": "compact", "hidden": [32, 32], "matched": "H07"},
        {"id": "C06", "formulation": "R1", "capacity": "deep", "hidden": [61, 61, 31], "matched": "H08"},
        {"id": "H01", "formulation": "R2", "capacity": "compact", "hidden": [32, 32], "matched": "C01"},
        {"id": "H02", "formulation": "R2", "capacity": "deep", "hidden": [64, 64, 32], "matched": "C02"},
        {"id": "H03", "formulation": "R3", "capacity": "compact", "hidden": [32, 32], "matched": "C01"},
        {"id": "H04", "formulation": "R3", "capacity": "deep", "hidden": [64, 64, 32], "matched": "C02"},
        {"id": "H05", "formulation": "R4", "capacity": "compact", "hidden": [32, 32], "matched": "C03"},
        {"id": "H06", "formulation": "R4", "capacity": "deep", "hidden": [64, 64, 32], "matched": "C04"},
        {"id": "H07", "formulation": "R5", "capacity": "compact", "hidden": [32, 32], "matched": "C05"},
        {"id": "H08", "formulation": "R5", "capacity": "deep", "hidden": [64, 64, 32], "matched": "C06"},
        {"id": "A01", "formulation": "R2", "capacity": "compact", "hidden": [32, 32], "matched": "H01", "energy": "weak"},
        {"id": "A02", "formulation": "R2", "capacity": "compact", "hidden": [32, 32], "matched": "H01", "energy": "moderate"},
        {"id": "A03", "formulation": "R5", "capacity": "compact", "hidden": [32, 32], "matched": "H07", "anchor_mode": "partial_low_order"},
        {"id": "A04", "formulation": "R5", "capacity": "compact", "hidden": [32, 32], "matched": "H07", "anchor_mode": "full"},
    ]


def build_base_configuration(
    residual_basis_order_list: list[int],
    residual_bound_deg: float,
) -> dict[str, Any]:
    """Build the common leakage-safe training configuration."""

    return {
        "paths": {
            "dataset_config_path": (
                "config/datasets/transmission_error_dataset.yaml"
            ),
            "output_root": (
                "output/training_runs/data_only_residual_capacity"
            ),
        },
        "experiment": {
            "run_name": "",
            "model_family": "",
            "model_type": "data_only_residual_capacity",
        },
        "metadata": {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": PLANNING_REPORT_PATH,
            "technical_document_path": TECHNICAL_DOCUMENT_PATH,
            "model_report_path": MODEL_REPORT_PATH,
            "phase_name": (
                "wave_5_2r_stage4_data_only_residual_capacity_ladder"
            ),
            "campaign_config_id": "",
            "queue_index": 0,
            "intervention": "",
            "probe_group": "wave52r_stage4_first_screen",
            "loss_profile": "stage4_data_only",
            "dataset_name": "polished_dataset",
            "input_mode": "setpoints",
            "dataset_schema": "polished_setpoint_curve_v1",
            "source_dataset_root": "data/polished_dataset",
            "training_variant": "fw",
            "direction_scope_label": "forward_only",
            "use_forward_direction": True,
            "use_backward_direction": False,
            "training_random_seed": 314159,
            "common_split_signature": COMMON_SPLIT_SIGNATURE,
            "analytical_anchor_contract": (
                "training-only causal setpoint PF-A refit"
            ),
        },
        "dataset": {
            "curve_batch_size": 4,
            "point_stride": 8,
            "maximum_points_per_curve": 4096,
            "num_workers": 2,
            "pin_memory": True,
            "name": "polished_dataset",
            "input_mode": "setpoints",
            "split_manifest_path": (
                "output/analysis/polynomial_fourier_benchmark/"
                "common_split_manifest.yaml"
            ),
            "excluded_condition_id_list": list(
                EXCLUDED_CONDITION_ID_LIST
            ),
            "expected_curve_count_by_split": {
                "train": 675,
                "validation": 194,
                "test": 97,
            },
        },
        "model": {
            "input_size": "auto",
            "output_size": 1,
            "hidden_size": [],
            "formulation": "",
            "harmonic_index_list": list(HARMONIC_INDEX_LIST),
            "activation_name": "Tanh",
            "dropout_probability": 0.0,
            "use_layer_norm": False,
            "analytical_anchor_path": (
                CAUSAL_ANCHOR_PATH.relative_to(PROJECT_ROOT).as_posix()
            ),
            "analytical_anchor_model_id": "PF_A_SETPOINT_QUADRATIC",
            "residual_bound_deg": residual_bound_deg,
            "residual_basis_order_list": list(
                residual_basis_order_list
            ),
            "anchor_mode": "frozen",
            "partial_unfreeze_harmonic_index_list": [1, 3],
            "zero_initialize_residual": True,
            "include_raw_angle_feature": False,
        },
        "training": {
            "learning_rate": 5.0e-4,
            "weight_decay": 1.0e-5,
            "min_epochs": 4,
            "max_epochs": 24,
            "patience": 5,
            "min_delta": 1.0e-5,
            "log_every_n_steps": 1,
            "fast_dev_run": False,
            "deterministic": True,
            "random_seed": 314159,
            "loss": {
                "profile": "stage4_data_only",
                "pointwise_loss": "mse",
                "enable_physics_diagnostics": False,
                "enable_optimization_instrumentation": True,
                "optimization_instrumentation_ema_decay": 0.95,
                "optimization_instrumentation_seed": 314159,
                "weights": {
                    "point": 1.0,
                    "centered": 0.0,
                    "offset": 0.0,
                    "amplitude": 0.0,
                    "harmonic": 0.0,
                    "derivative": 0.0,
                    "residual_energy": 0.0,
                    "physics_oscillator": 0.0,
                    "physics_periodic_value": 0.0,
                    "physics_periodic_slope": 0.0,
                    "physics_analytical_anchor": 0.0,
                    "physics_compliance_equation": 0.0,
                    "physics_zero_torque_boundary": 0.0,
                    "physics_compliance_monotonicity": 0.0,
                    "physics_stiffness_bounds": 0.0,
                    "physics_periodic_mean": 0.0,
                },
                "harmonic_index_list": list(HARMONIC_INDEX_LIST),
            },
        },
        "runtime": {
            "accelerator": "auto",
            "devices": "auto",
            "precision": "32",
            "benchmark": False,
            "use_non_blocking_transfer": True,
        },
    }


def build_run_configuration(
    queue_index: int,
    candidate_specification: dict[str, Any],
    base_configuration: dict[str, Any],
) -> dict[str, Any]:
    """Build one immutable candidate configuration."""

    configuration = deepcopy(base_configuration)
    candidate_id = str(candidate_specification["id"])
    formulation = str(candidate_specification["formulation"])
    capacity = str(candidate_specification["capacity"])
    run_slug = (
        f"stage4_{candidate_id.lower()}_{formulation.lower()}_{capacity}"
    )
    configuration["experiment"].update(
        {
            "run_name": f"te_{run_slug}__polished_setpoints_fw",
            "model_family": run_slug,
        }
    )
    configuration["metadata"].update(
        {
            "campaign_config_id": run_slug,
            "queue_index": queue_index,
            "intervention": formulation,
            "candidate_id": candidate_id,
            "capacity_level": capacity,
            "matched_candidate_id": candidate_specification["matched"],
        }
    )
    configuration["model"]["hidden_size"] = list(
        candidate_specification["hidden"]
    )
    configuration["model"]["formulation"] = formulation
    configuration["model"]["anchor_mode"] = str(
        candidate_specification.get("anchor_mode", "frozen")
    )
    energy_label = str(candidate_specification.get("energy", "none"))
    energy_weight_map = {"none": 0.0, "weak": 0.01, "moderate": 0.10}
    configuration["training"]["loss"]["weights"][
        "residual_energy"
    ] = energy_weight_map[energy_label]
    configuration["metadata"]["residual_energy_profile"] = energy_label
    configuration["metadata"]["trainable_parameter_count"] = (
        count_trainable_parameters(
            formulation,
            list(candidate_specification["hidden"]),
            len(configuration["model"]["residual_basis_order_list"]),
        )
    )
    return configuration


def main() -> None:
    """Create causal anchor, calibration evidence, and campaign package."""

    phase1_configuration = load_yaml(PHASE1_CONFIGURATION_PATH)
    common_split_manifest = load_yaml(COMMON_SPLIT_MANIFEST_PATH)
    assert (
        common_split_manifest["split"]["assignment_sha256"]
        == COMMON_SPLIT_SIGNATURE
    )
    curve_record_list = load_curve_records(
        phase1_configuration,
        common_split_manifest,
    )
    excluded_condition_id_set = set(EXCLUDED_CONDITION_ID_LIST)
    forward_record_list = [
        record
        for record in curve_record_list
        if record.direction == "Fw"
        and record.condition_id not in excluded_condition_id_set
    ]
    training_record_list = [
        record
        for record in forward_record_list
        if record.split == "train"
    ]
    test_record_list = [
        record for record in forward_record_list if record.split == "test"
    ]
    assert len(training_record_list) == 675
    assert len(test_record_list) == 97

    # Refit A Strictly Causal Setpoint Surface
    causal_surface = fit_causal_setpoint_surface(training_record_list)
    legacy_payload = load_yaml(LEGACY_STAGE3_ANCHOR_PATH)
    legacy_surface = build_surface_from_payload(legacy_payload["surface"])
    causal_test_metrics = aggregate_curve_metrics(
        causal_surface,
        test_record_list,
        use_setpoints=True,
    )
    legacy_measured_test_metrics = aggregate_curve_metrics(
        legacy_surface,
        test_record_list,
        use_setpoints=False,
    )
    legacy_replayed_on_setpoints_test_metrics = aggregate_curve_metrics(
        legacy_surface,
        test_record_list,
        use_setpoints=True,
    )

    causal_anchor_payload = {
        "schema_version": 1,
        "model_id": "PF_A_SETPOINT_QUADRATIC",
        "fit_scope": (
            "frozen polished_dataset setpoint Fw training split only"
        ),
        "split_signature": COMMON_SPLIT_SIGNATURE,
        "training_curve_count": 675,
        "validation_curve_count": 194,
        "test_curve_count": 97,
        "source_formulation": "PF_A_LOCAL_QUADRATIC",
        "legacy_stage3_anchor_path": (
            LEGACY_STAGE3_ANCHOR_PATH.relative_to(PROJECT_ROOT).as_posix()
        ),
        "causal_input_contract": {
            "torque": "negative nominal output-torque setpoint for Fw",
            "speed": "absolute nominal input-speed setpoint",
            "temperature": "nominal oil-temperature setpoint",
            "target_derived_runtime_inputs": False,
        },
        "surface": {
            "feature_order": [
                "signed_setpoint_torque_nm",
                "absolute_setpoint_speed_rpm",
                "setpoint_temperature_deg_c",
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
            "harmonic_order_list": list(HARMONIC_INDEX_LIST),
            "feature_mean": causal_surface.feature_mean.tolist(),
            "feature_scale": causal_surface.feature_scale.tolist(),
            "design_condition_number": (
                causal_surface.design_condition_number
            ),
            "coefficient_matrix": (
                causal_surface.coefficient_matrix.tolist()
            ),
        },
        "test_metrics": causal_test_metrics,
    }
    write_yaml(CAUSAL_ANCHOR_PATH, causal_anchor_payload)

    residual_basis_order_list, residual_bound_deg, residual_statistics = (
        select_training_only_residual_basis(
            causal_surface,
            training_record_list,
        )
    )
    candidate_specification_list = build_candidate_specification_list()
    base_configuration = build_base_configuration(
        residual_basis_order_list,
        residual_bound_deg,
    )

    # Materialize Immutable Queue Configurations
    queue_path_list: list[str] = []
    parameter_count_map: dict[str, int] = {}
    for queue_index, candidate_specification in enumerate(
        candidate_specification_list,
        start=1,
    ):
        configuration = build_run_configuration(
            queue_index,
            candidate_specification,
            base_configuration,
        )
        candidate_id = str(candidate_specification["id"])
        formulation = str(candidate_specification["formulation"])
        capacity = str(candidate_specification["capacity"])
        queue_path = QUEUE_DIRECTORY / (
            f"{queue_index:03d}_{candidate_id.lower()}_"
            f"{formulation.lower()}_{capacity}.yaml"
        )
        write_yaml(queue_path, configuration)
        queue_path_list.append(
            queue_path.relative_to(PROJECT_ROOT).as_posix()
        )
        parameter_count_map[candidate_id] = int(
            configuration["metadata"]["trainable_parameter_count"]
        )

    parameter_match_row_list = []
    matched_pair_list = [
        ("C01", "H01"),
        ("C01", "H03"),
        ("C02", "H02"),
        ("C02", "H04"),
        ("C03", "H05"),
        ("C04", "H06"),
        ("C05", "H07"),
        ("C06", "H08"),
    ]
    for control_id, hybrid_id in matched_pair_list:
        control_count = parameter_count_map[control_id]
        hybrid_count = parameter_count_map[hybrid_id]
        mismatch_fraction = abs(control_count - hybrid_count) / hybrid_count
        assert mismatch_fraction <= 0.05
        parameter_match_row_list.append(
            {
                "control_id": control_id,
                "hybrid_id": hybrid_id,
                "control_parameter_count": control_count,
                "hybrid_parameter_count": hybrid_count,
                "mismatch_fraction": mismatch_fraction,
                "passes_five_percent_gate": True,
            }
        )

    calibration_payload = {
        "schema_version": 1,
        "stage": "wave_5_2r_stage4",
        "split_signature": COMMON_SPLIT_SIGNATURE,
        "causal_anchor_path": (
            CAUSAL_ANCHOR_PATH.relative_to(PROJECT_ROOT).as_posix()
        ),
        "legacy_anchor_causality_erratum": {
            "finding": (
                "Stage 3 exact Phase 1 reproduction used measured operating "
                "averages despite the declared setpoint-only scope."
            ),
            "resolution": (
                "Stage 4 uses a new training-only PF-A surface fit and "
                "evaluated exclusively with nominal setpoints."
            ),
            "legacy_measured_test_metrics": (
                legacy_measured_test_metrics
            ),
            "legacy_surface_replayed_on_setpoints_test_metrics": (
                legacy_replayed_on_setpoints_test_metrics
            ),
            "causal_setpoint_refit_test_metrics": causal_test_metrics,
        },
        "training_only_residual_statistics": residual_statistics,
        "residual_basis_order_list": residual_basis_order_list,
        "residual_bound_deg": residual_bound_deg,
        "residual_energy_weight_map": {
            "none": 0.0,
            "weak": 0.01,
            "moderate": 0.10,
        },
        "parameter_count_by_candidate": parameter_count_map,
        "parameter_match_row_list": parameter_match_row_list,
    }
    write_yaml(CALIBRATION_PATH, calibration_payload)

    campaign_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": (
            "wave_5_2r_stage4_data_only_residual_capacity_ladder"
        ),
        "family_name": "data_only_residual_capacity",
        "dataset_name": "polished_dataset",
        "input_mode": "setpoints",
        "dataset_schema": "polished_setpoint_curve_v1",
        "source_dataset_root": "data/polished_dataset",
        "primary_surface": "fw",
        "expected_surface_list": ["fw"],
        "expected_run_count": len(queue_path_list),
        "planning_report_path": PLANNING_REPORT_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "model_report_path": MODEL_REPORT_PATH,
        "common_split_manifest_path": (
            COMMON_SPLIT_MANIFEST_PATH.relative_to(PROJECT_ROOT).as_posix()
        ),
        "common_split_signature": COMMON_SPLIT_SIGNATURE,
        "causal_anchor_path": (
            CAUSAL_ANCHOR_PATH.relative_to(PROJECT_ROOT).as_posix()
        ),
        "training_only_calibration_path": (
            CALIBRATION_PATH.relative_to(PROJECT_ROOT).as_posix()
        ),
        "legacy_stage3_anchor_path": (
            LEGACY_STAGE3_ANCHOR_PATH.relative_to(PROJECT_ROOT).as_posix()
        ),
        "excluded_condition_id_list": list(
            EXCLUDED_CONDITION_ID_LIST
        ),
        "expected_curve_count_by_split": {
            "train": 675,
            "validation": 194,
            "test": 97,
        },
        "queue_root": (
            "config/training/queue/data_only_residual_capacity/"
            f"{CAMPAIGN_NAME}"
        ),
        "queue_config_path_list": queue_path_list,
        "execution_policy": {
            "operator_run_required": False,
            "standing_approval_applies": True,
            "stop_on_error": True,
            "conditional_stability_repeat": True,
            "run_te_curve_verification_pipeline": False,
            "scalar_mae_only_promotion_allowed": False,
        },
    }
    write_yaml(CAMPAIGN_DIRECTORY / "campaign.yaml", campaign_payload)
    print(
        f"Prepared {len(queue_path_list)} Stage 4 queue configurations"
    )
    print(
        "Causal PF-A test MAE | "
        f"{causal_test_metrics['mae_deg']:.9f} deg"
    )
    print(
        "Residual basis | "
        + ", ".join(str(value) for value in residual_basis_order_list)
    )
    print(f"Residual bound | {residual_bound_deg:.9f} deg")


if __name__ == "__main__":
    main()
