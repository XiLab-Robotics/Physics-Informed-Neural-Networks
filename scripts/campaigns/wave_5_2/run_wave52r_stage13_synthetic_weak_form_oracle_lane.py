"""Run Wave 5.2R Stage 13 synthetic weak-form oracle certification."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from datetime import datetime
import hashlib
from pathlib import Path
import sys
from typing import Any

# Import Numerical And Serialization Utilities
import numpy as np
import yaml

# Make Direct Script Execution Resolve The Repository Package
PROJECT_IMPORT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_IMPORT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_IMPORT_ROOT))

# Import Frozen Stage And Oracle Utilities
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.models.synthetic_weak_form_oracle import (
    add_normalized_gaussian_noise,
    build_periodic_angle_array,
    fit_linear_parameter_model,
    normalized_root_mean_square_error,
    pointwise_oscillator_residual,
    project_fourier_coefficients,
    reconstruct_fourier_curve,
    weak_oscillator_residual,
)


# Define Campaign Constants
PROJECT_ROOT = Path(__file__).resolve().parents[3]
STAGE_NAME = "wave52r_stage13_synthetic_weak_form_oracle_lane"
CAMPAIGN_NAME = f"{STAGE_NAME}_2026_07_29"
ORACLE_SEED = 314159
ORACLE_CONDITION_COUNT = 64
DENSITY_LIST = [2048, 1024, 512, 256, 128]
NOISE_LEVEL_LIST = [0.0, 0.001, 0.005, 0.01]
CONFIG_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "synthetic_weak_form_oracle_lane"
    / "campaigns"
    / "2026-07-29_wave52r_stage13_synthetic_weak_form_oracle_lane"
)
QUEUE_DIRECTORY = CONFIG_DIRECTORY / "queue"
ANALYSIS_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage13_synthetic_weak_form_oracle_lane"
)
CAMPAIGN_ROOT_DIRECTORY = PROJECT_ROOT / "output" / "training_campaigns"
VALIDATION_ROOT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "synthetic_weak_form_oracle_lane"
)
ACTIVE_CAMPAIGN_PATH = (
    PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
)
TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-29/"
    "2026-07-29-23-21-24_wave52r_stage13_synthetic_weak_form_oracle_lane.md"
)
CAMPAIGN_PLAN_PATH = (
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/"
    "synthetic_weak_form_oracle_lane/"
    "2026-07-29-23-21-24_wave52r_stage13_synthetic_weak_form_oracle_"
    "lane_campaign_plan_report.md"
)
MODEL_REPORT_PATH = (
    "doc/reports/analysis/model_development_waves/wave_5_2/"
    "physics_guided_pinn_reassessment/[2026-07-29]/"
    "stage13_synthetic_weak_form_oracle_lane/"
    "stage13_synthetic_weak_form_oracle_model_report.md"
)
LAUNCHER_PATH = (
    "scripts/campaigns/wave_5_2/"
    "run_wave52r_stage13_synthetic_weak_form_oracle_lane.ps1"
)
LAUNCHER_NOTE_PATH = (
    "doc/scripts/campaigns/wave_5_2/"
    "run_wave52r_stage13_synthetic_weak_form_oracle_lane.md"
)


def now_iso() -> str:
    """Return one timezone-aware local timestamp."""

    return datetime.now().astimezone().isoformat(timespec="seconds")


def now_timestamp() -> str:
    """Return one sortable local timestamp."""

    return datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")


def to_windows_command_path(path_text: str) -> str:
    """Convert one repository-relative path for a PowerShell command."""

    return path_text.replace("/", "\\")


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def write_csv(path: Path, row_list: list[dict[str, Any]]) -> None:
    """Write one stable CSV table."""

    assert row_list
    path.parent.mkdir(parents=True, exist_ok=True)
    field_name_list: list[str] = []
    for row in row_list:
        for field_name in row:
            if field_name not in field_name_list:
                field_name_list.append(field_name)
    with path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)


def select_oracle_indices(dataset: stage5.Stage5Dataset) -> np.ndarray:
    """Select an immutable evenly spaced training-domain condition subset."""

    training_index_array = np.flatnonzero(dataset.split_array == "train")
    selection_position_array = np.linspace(
        0,
        training_index_array.size - 1,
        ORACLE_CONDITION_COUNT,
        dtype=np.int64,
    )
    oracle_index_array = training_index_array[selection_position_array]
    assert np.unique(oracle_index_array).size == ORACLE_CONDITION_COUNT
    return oracle_index_array


def build_residual_grid(
    seed: int,
    harmonic_order: int,
) -> list[dict[str, Any]]:
    """Evaluate matched pointwise and weak residuals across corruption levels."""

    row_list: list[dict[str, Any]] = []
    for density in DENSITY_LIST:
        theta_array = build_periodic_angle_array(density)
        clean_signal = (
            0.8 * np.sin(harmonic_order * theta_array)
            - 0.35 * np.cos(harmonic_order * theta_array)
        )
        for noise_index, noise_level in enumerate(NOISE_LEVEL_LIST):
            random_generator = np.random.default_rng(
                seed + (density * 17) + noise_index
            )
            noisy_signal = add_normalized_gaussian_noise(
                clean_signal,
                noise_level,
                random_generator,
            )
            row_list.append(
                {
                    "density": density,
                    "noise_level": noise_level,
                    "pointwise_residual": pointwise_oscillator_residual(
                        noisy_signal,
                        theta_array,
                        harmonic_order,
                    ),
                    "weak_residual": weak_oscillator_residual(
                        noisy_signal,
                        theta_array,
                        harmonic_order,
                    ),
                }
            )
    return row_list


def run_oracle_matrix(
    dataset: stage5.Stage5Dataset | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Execute the ten deterministic Stage 13 oracle experiments."""

    if dataset is None:
        dataset = stage5.build_stage5_dataset()
    oracle_index_array = select_oracle_indices(dataset)
    core_order_list = list(dataset.order_set_map["core"])
    core_coefficient_matrix = dataset.anchor_coefficient_map["core"][
        oracle_index_array
    ]
    condition_matrix = dataset.condition_matrix[oracle_index_array]
    theta_array = build_periodic_angle_array(stage5.ANGULAR_SAMPLE_COUNT)
    result_row_list: list[dict[str, Any]] = []
    detail_payload: dict[str, Any] = {}

    # C00: certify exact H04 synthesis and projection.
    reconstruction_error_list: list[float] = []
    coefficient_error_list: list[float] = []
    for coefficient_array in core_coefficient_matrix:
        curve_array = reconstruct_fourier_curve(
            coefficient_array,
            core_order_list,
            theta_array,
        )
        recovered_coefficient_array = project_fourier_coefficients(
            curve_array,
            core_order_list,
            theta_array,
        )
        recovered_curve_array = reconstruct_fourier_curve(
            recovered_coefficient_array,
            core_order_list,
            theta_array,
        )
        reconstruction_error_list.append(
            float(np.max(np.abs(recovered_curve_array - curve_array)))
        )
        coefficient_error_list.append(
            normalized_root_mean_square_error(
                recovered_coefficient_array,
                coefficient_array,
            )
        )
    c00_metric = float(max(reconstruction_error_list))
    c00_pass = c00_metric <= 1.0e-10
    result_row_list.append(
        build_result_row(
            "C00",
            "exact_h04_reconstruction",
            c00_metric,
            1.0e-10,
            "maximum_absolute_curve_error",
            c00_pass,
        )
    )
    detail_payload["C00"] = {
        "maximum_absolute_curve_error": c00_metric,
        "maximum_normalized_coefficient_error": float(
            max(coefficient_error_list)
        ),
    }

    # H01 and H02: inject one omitted harmonic and compare complete/incomplete bases.
    extended_order = next(
        (
            order
            for order in dataset.order_set_map["core_plus_residual"]
            if order not in core_order_list
        ),
        max(core_order_list) + 1,
    )
    extended_order_list = core_order_list + [extended_order]
    injected_sine = 0.20 * dataset.curve_scale
    injected_cosine = -0.08 * dataset.curve_scale
    injected_truth = np.asarray([injected_sine, injected_cosine])
    injected_recovery_list: list[np.ndarray] = []
    omitted_error_list: list[float] = []
    complete_error_list: list[float] = []
    for coefficient_array in core_coefficient_matrix:
        extended_coefficient_array = np.concatenate(
            [coefficient_array, injected_truth]
        )
        curve_array = reconstruct_fourier_curve(
            extended_coefficient_array,
            extended_order_list,
            theta_array,
        )
        recovered_extended = project_fourier_coefficients(
            curve_array,
            extended_order_list,
            theta_array,
        )
        injected_recovery_list.append(recovered_extended[-2:])
        omitted_coefficient = project_fourier_coefficients(
            curve_array,
            core_order_list,
            theta_array,
        )
        omitted_curve = reconstruct_fourier_curve(
            omitted_coefficient,
            core_order_list,
            theta_array,
        )
        complete_curve = reconstruct_fourier_curve(
            recovered_extended,
            extended_order_list,
            theta_array,
        )
        omitted_error_list.append(
            float(np.sqrt(np.mean(np.square(curve_array - omitted_curve))))
        )
        complete_error_list.append(
            float(np.sqrt(np.mean(np.square(curve_array - complete_curve))))
        )
    injected_recovery_matrix = np.vstack(injected_recovery_list)
    h01_metric = normalized_root_mean_square_error(
        injected_recovery_matrix,
        np.tile(injected_truth, (ORACLE_CONDITION_COUNT, 1)),
    )
    h01_pass = h01_metric <= 0.02
    result_row_list.append(
        build_result_row(
            "H01",
            "controlled_harmonic_injection",
            h01_metric,
            0.02,
            "normalized_injected_coefficient_rmse",
            h01_pass,
        )
    )
    omission_ratio = float(
        np.mean(omitted_error_list)
        / max(np.mean(complete_error_list), 1.0e-15)
    )
    h02_pass = omission_ratio >= 5.0
    result_row_list.append(
        build_result_row(
            "H02",
            "controlled_harmonic_omission",
            omission_ratio,
            5.0,
            "omitted_to_complete_curve_error_ratio",
            h02_pass,
            higher_is_better=True,
        )
    )
    detail_payload["H01"] = {
        "injected_order": extended_order,
        "injected_sine": injected_sine,
        "injected_cosine": injected_cosine,
    }
    detail_payload["H02"] = {
        "mean_omitted_rmse": float(np.mean(omitted_error_list)),
        "mean_complete_rmse": float(np.mean(complete_error_list)),
    }

    # C01: recover a known condition-dependent coefficient correction.
    standardized_condition_matrix = (
        condition_matrix - dataset.feature_mean
    ) / dataset.feature_scale
    coefficient_bound = float(dataset.correction_bound_map["core"][1])
    correction_truth = coefficient_bound * (
        0.40 * standardized_condition_matrix[:, 0]
        - 0.20 * standardized_condition_matrix[:, 1]
    )
    recovered_correction_list: list[float] = []
    for row_index, coefficient_array in enumerate(core_coefficient_matrix):
        perturbed_coefficient = coefficient_array.copy()
        perturbed_coefficient[1] += correction_truth[row_index]
        curve_array = reconstruct_fourier_curve(
            perturbed_coefficient,
            core_order_list,
            theta_array,
        )
        recovered = project_fourier_coefficients(
            curve_array,
            core_order_list,
            theta_array,
        )
        recovered_correction_list.append(
            float(recovered[1] - coefficient_array[1])
        )
    c01_metric = normalized_root_mean_square_error(
        np.asarray(recovered_correction_list),
        correction_truth,
    )
    result_row_list.append(
        build_result_row(
            "C01",
            "coefficient_surface_perturbation",
            c01_metric,
            0.02,
            "normalized_correction_rmse",
            c01_metric <= 0.02,
        )
    )

    # M01: recover a deliberately misspecified anchor.
    anchor_bias = 0.35 * coefficient_bound
    recovered_bias_list: list[float] = []
    for coefficient_array in core_coefficient_matrix:
        biased_anchor = coefficient_array.copy()
        biased_anchor[1] -= anchor_bias
        truth_curve = reconstruct_fourier_curve(
            coefficient_array,
            core_order_list,
            theta_array,
        )
        recovered_truth = project_fourier_coefficients(
            truth_curve,
            core_order_list,
            theta_array,
        )
        recovered_bias_list.append(
            float(recovered_truth[1] - biased_anchor[1])
        )
    m01_metric = normalized_root_mean_square_error(
        np.asarray(recovered_bias_list),
        np.full(ORACLE_CONDITION_COUNT, anchor_bias),
    )
    result_row_list.append(
        build_result_row(
            "M01",
            "misspecified_anchor_recovery",
            m01_metric,
            0.02,
            "normalized_anchor_correction_rmse",
            m01_metric <= 0.02,
        )
    )

    # Q01: identify one known torque-dependent compliance nonlinearity.
    torque_like = standardized_condition_matrix[:, 1]
    compliance_design = np.column_stack(
        [
            np.ones(ORACLE_CONDITION_COUNT),
            torque_like,
            torque_like * np.abs(torque_like),
        ]
    )
    compliance_truth = np.asarray(
        [0.02, -0.10, 0.18],
        dtype=np.float64,
    ) * dataset.curve_scale
    compliance_target = compliance_design @ compliance_truth
    recovered_compliance = fit_linear_parameter_model(
        compliance_design,
        compliance_target,
    )
    q01_metric = normalized_root_mean_square_error(
        recovered_compliance,
        compliance_truth,
    )
    result_row_list.append(
        build_result_row(
            "Q01",
            "synthetic_compliance_nonlinearity",
            q01_metric,
            0.05,
            "normalized_compliance_parameter_rmse",
            q01_metric <= 0.05,
        )
    )

    # P01 and W01: matched residual grid.
    oscillator_order = 5
    residual_grid = build_residual_grid(ORACLE_SEED, oscillator_order)
    pointwise_finite = all(
        np.isfinite(row["pointwise_residual"]) for row in residual_grid
    )
    p01_metric = float(
        max(row["pointwise_residual"] for row in residual_grid)
    )
    result_row_list.append(
        build_result_row(
            "P01",
            "pointwise_oscillator_residual",
            p01_metric,
            float("inf"),
            "maximum_normalized_pointwise_residual",
            pointwise_finite,
        )
    )
    matched_row_list = [
        row
        for row in residual_grid
        if row["density"] >= 256 and row["noise_level"] > 0.0
    ]
    weak_better_count = sum(
        row["weak_residual"] < row["pointwise_residual"]
        for row in matched_row_list
    )
    target_weak_row = next(
        row
        for row in residual_grid
        if row["density"] == 256 and row["noise_level"] == 0.01
    )
    w01_metric = float(target_weak_row["weak_residual"])
    w01_pass = (
        weak_better_count == len(matched_row_list)
        and w01_metric <= 0.02
    )
    result_row_list.append(
        build_result_row(
            "W01",
            "weak_form_oscillator_residual",
            w01_metric,
            0.02,
            "weak_residual_density256_noise001",
            w01_pass,
        )
    )
    detail_payload["residual_grid"] = residual_grid
    detail_payload["W01"] = {
        "weak_better_comparison_count": weak_better_count,
        "required_comparison_count": len(matched_row_list),
    }

    # D01: determine the minimum useful density at maximum declared noise.
    passing_density_list = [
        int(row["density"])
        for row in residual_grid
        if row["noise_level"] == 0.01 and row["weak_residual"] <= 0.02
    ]
    minimum_passing_density = (
        min(passing_density_list) if passing_density_list else 0
    )
    d01_pass = minimum_passing_density > 0
    result_row_list.append(
        build_result_row(
            "D01",
            "sampling_density_stress",
            float(minimum_passing_density),
            256.0,
            "minimum_passing_angular_sample_count",
            d01_pass and minimum_passing_density <= 256,
        )
    )

    # N01: correct law must reject wrong order and shuffled angular order.
    control_theta = build_periodic_angle_array(256)
    control_signal = (
        0.8 * np.sin(oscillator_order * control_theta)
        - 0.35 * np.cos(oscillator_order * control_theta)
    )
    control_random_generator = np.random.default_rng(ORACLE_SEED + 991)
    control_signal = add_normalized_gaussian_noise(
        control_signal,
        0.001,
        control_random_generator,
    )
    correct_residual = weak_oscillator_residual(
        control_signal,
        control_theta,
        oscillator_order,
    )
    wrong_order_residual = weak_oscillator_residual(
        control_signal,
        control_theta,
        oscillator_order + 1,
    )
    shuffled_signal = control_signal[
        np.random.default_rng(ORACLE_SEED + 992).permutation(
            control_signal.size
        )
    ]
    shuffled_residual = weak_oscillator_residual(
        shuffled_signal,
        control_theta,
        oscillator_order,
    )
    wrong_ratio = wrong_order_residual / max(correct_residual, 1.0e-15)
    shuffled_ratio = shuffled_residual / max(correct_residual, 1.0e-15)
    n01_metric = float(min(wrong_ratio, shuffled_ratio))
    n01_pass = n01_metric >= 10.0
    result_row_list.append(
        build_result_row(
            "N01",
            "wrong_law_and_shuffled_controls",
            n01_metric,
            10.0,
            "minimum_negative_control_rejection_ratio",
            n01_pass,
            higher_is_better=True,
        )
    )
    detail_payload["N01"] = {
        "correct_residual": correct_residual,
        "wrong_order_residual": wrong_order_residual,
        "shuffled_residual": shuffled_residual,
        "wrong_order_rejection_ratio": wrong_ratio,
        "shuffled_rejection_ratio": shuffled_ratio,
    }

    detail_payload["provenance"] = {
        "split_signature": stage5.SPLIT_SIGNATURE,
        "oracle_seed": ORACLE_SEED,
        "oracle_condition_count": ORACLE_CONDITION_COUNT,
        "oracle_condition_id_sha256": hashlib.sha256(
            "\n".join(
                dataset.condition_id_list[index]
                for index in oracle_index_array
            ).encode("utf-8")
        ).hexdigest(),
        "core_order_list": core_order_list,
        "curve_scale": dataset.curve_scale,
        "test_curve_count_checked_only": int(
            np.sum(dataset.split_array == "test")
        ),
        "test_label_dependence": False,
        "real_data_promotion_allowed": False,
    }
    return result_row_list, detail_payload


def build_result_row(
    candidate_id: str,
    experiment: str,
    primary_metric: float,
    gate_threshold: float,
    metric_name: str,
    passed: bool,
    higher_is_better: bool = False,
) -> dict[str, Any]:
    """Build one stable certification result row."""

    return {
        "candidate_id": candidate_id,
        "experiment": experiment,
        "primary_metric_name": metric_name,
        "primary_metric": float(primary_metric),
        "gate_threshold": float(gate_threshold),
        "higher_is_better": higher_is_better,
        "gate_passed": bool(passed),
        "decision": (
            "certified_for_synthetic_use" if passed else "rejected"
        ),
        "real_data_promotion_allowed": False,
    }


def validate_preflight(
    dataset: stage5.Stage5Dataset | None = None,
) -> dict[str, Any]:
    """Validate configuration, provenance, determinism, and analytical gates."""

    manifest_payload = load_yaml(CONFIG_DIRECTORY / "campaign.yaml")
    queue_path_list = sorted(QUEUE_DIRECTORY.glob("*.yaml"))
    assert manifest_payload["candidate_count"] == 10
    assert len(queue_path_list) == 10
    candidate_id_list = [
        load_yaml(path)["candidate_id"] for path in queue_path_list
    ]
    assert candidate_id_list == [
        "C00",
        "H01",
        "H02",
        "C01",
        "M01",
        "Q01",
        "P01",
        "W01",
        "D01",
        "N01",
    ]
    for required_path in [
        PROJECT_ROOT / TECHNICAL_DOCUMENT_PATH,
        PROJECT_ROOT / CAMPAIGN_PLAN_PATH,
        PROJECT_ROOT / MODEL_REPORT_PATH,
        PROJECT_ROOT / LAUNCHER_PATH,
    ]:
        assert required_path.exists(), required_path

    if dataset is None:
        dataset = stage5.build_stage5_dataset()
    first_row_list, first_detail = run_oracle_matrix(dataset)
    second_row_list, second_detail = run_oracle_matrix(dataset)
    assert first_row_list == second_row_list
    assert first_detail == second_detail
    preflight_payload = {
        "schema_version": 1,
        "stage": STAGE_NAME,
        "checked_at": now_iso(),
        "status": "passed",
        "candidate_count": len(first_row_list),
        "deterministic_replay_exact": True,
        "split_signature": stage5.SPLIT_SIGNATURE,
        "test_label_dependence": False,
        "real_data_promotion_allowed": False,
        "preflight_result_list": first_row_list,
    }
    write_yaml(
        ANALYSIS_DIRECTORY / "stage13_preflight_summary.yaml",
        preflight_payload,
    )
    return preflight_payload


def run_campaign() -> Path:
    """Run the bounded matrix and write immutable campaign artifacts."""

    dataset = stage5.build_stage5_dataset()
    validate_preflight(dataset)
    started_at = now_iso()
    campaign_directory = (
        CAMPAIGN_ROOT_DIRECTORY
        / f"{now_timestamp()}_{CAMPAIGN_NAME}"
    )
    validation_directory = (
        VALIDATION_ROOT_DIRECTORY / campaign_directory.name
    )
    result_row_list, detail_payload = run_oracle_matrix(dataset)
    write_csv(campaign_directory / "campaign_leaderboard.csv", result_row_list)
    write_csv(
        campaign_directory / "weak_form_noise_density_grid.csv",
        detail_payload["residual_grid"],
    )
    write_yaml(
        campaign_directory / "oracle_detail.yaml",
        detail_payload,
    )
    all_passed = all(row["gate_passed"] for row in result_row_list)
    certification_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "stage": STAGE_NAME,
        "started_at": started_at,
        "completed_at": now_iso(),
        "status": "completed",
        "expected_run_count": 10,
        "completed_run_count": 10,
        "failed_run_count": 0,
        "certified_case_count": sum(
            row["gate_passed"] for row in result_row_list
        ),
        "rejected_case_count": sum(
            not row["gate_passed"] for row in result_row_list
        ),
        "all_cases_certified": all_passed,
        "synthetic_oracle_lane_status": (
            "certified_for_synthetic_use"
            if all_passed
            else "implementation_valid_but_power_limited"
        ),
        "qualified_real_data_winner_id": None,
        "real_data_promotion_allowed": False,
        "result_list": result_row_list,
    }
    write_yaml(
        campaign_directory / "campaign_certification_summary.yaml",
        certification_payload,
    )
    write_yaml(
        campaign_directory / "campaign_best_run.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "best_run_id": None,
            "reason": (
                "Stage 13 certifies independent analytical cases and does not "
                "rank or promote a real-data model."
            ),
            "qualified_real_data_winner_id": None,
        },
    )
    best_run_markdown = (
        "# Stage 13 Campaign Best Run\n\n"
        "No real-data best run is declared. Stage 13 is an analytical "
        "certification lane, and synthetic success cannot promote a model.\n"
    )
    (campaign_directory / "campaign_best_run.md").write_text(
        best_run_markdown,
        encoding="utf-8",
        newline="\n",
    )
    write_yaml(
        campaign_directory / "campaign_leaderboard.yaml",
        {
            "schema_version": 1,
            "campaign_name": CAMPAIGN_NAME,
            "result_list": result_row_list,
        },
    )
    write_yaml(
        validation_directory / "stage13_validation_summary.yaml",
        certification_payload,
    )
    write_yaml(
        ACTIVE_CAMPAIGN_PATH,
        {
            "status": "completed",
            "prepared_at": "2026-07-29T23:21:24+02:00",
            "campaign_name": CAMPAIGN_NAME,
            "campaign_type": STAGE_NAME,
            "dataset_id": "polished_dataset",
            "input_mode": "setpoints",
            "surface_list": ["fw"],
            "primary_surface": "fw",
            "expected_run_count": 10,
            "completed_run_count": 10,
            "failed_run_count": 0,
            "random_seed_list": [ORACLE_SEED],
            "campaign_manifest_path": str(
                (CONFIG_DIRECTORY / "campaign.yaml").relative_to(PROJECT_ROOT)
            ).replace("\\", "/"),
            "launcher_path": LAUNCHER_PATH,
            "launcher_note_path": LAUNCHER_NOTE_PATH,
            "planning_report_path": CAMPAIGN_PLAN_PATH,
            "technical_document_path": TECHNICAL_DOCUMENT_PATH,
            "local_preflight_command": (
                f".\\{to_windows_command_path(LAUNCHER_PATH)} -PreflightOnly"
            ),
            "local_launch_command": (
                f".\\{to_windows_command_path(LAUNCHER_PATH)} -Run"
            ),
            "remote_preflight_command": (
                f".\\{to_windows_command_path(LAUNCHER_PATH)} "
                "-Remote -PreflightOnly"
            ),
            "remote_launch_command": (
                f".\\{to_windows_command_path(LAUNCHER_PATH)} -Remote -Run"
            ),
            "approval": {
                "technical_document_status": "approved",
                "campaign_plan_status": "approved",
                "approval_source": (
                    "user blanket approval for twenty-four hours"
                ),
                "approval_recorded_at": "2026-07-29T15:30:41+02:00",
                "approval_expires_at": "2026-07-30T15:30:41+02:00",
            },
            "protected_file_list": [
                "doc/running/active_training_campaign.yaml",
                str(CONFIG_DIRECTORY.relative_to(PROJECT_ROOT)).replace(
                    "\\", "/"
                ),
                LAUNCHER_PATH,
                str(Path(__file__).relative_to(PROJECT_ROOT)).replace("\\", "/"),
                "scripts/models/synthetic_weak_form_oracle.py",
                str(ANALYSIS_DIRECTORY.relative_to(PROJECT_ROOT)).replace(
                    "\\", "/"
                ),
            ],
            "started_at": started_at,
            "completed_at": certification_payload["completed_at"],
            "campaign_output_directory": str(
                campaign_directory.relative_to(PROJECT_ROOT)
            ).replace("\\", "/"),
            "campaign_best_run_path": str(
                (campaign_directory / "campaign_best_run.yaml").relative_to(
                    PROJECT_ROOT
                )
            ).replace("\\", "/"),
            "qualified_real_data_winner_id": None,
            "synthetic_oracle_lane_status": certification_payload[
                "synthetic_oracle_lane_status"
            ],
            "real_data_promotion_allowed": False,
            "previous_campaign": {
                "campaign_name": (
                    "wave52r_stage12_advanced_constraint_optimization_"
                    "2026_07_29"
                ),
                "status": "completed",
                "commit": "cb0e13d4b5618f032c8b17b04456e7eeecb63bef",
            },
        },
    )
    print(f"Stage 13 campaign completed | {campaign_directory}")
    return campaign_directory


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--run", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Run Stage 13 preflight or campaign execution."""

    argument_namespace = parse_arguments()
    if argument_namespace.run:
        run_campaign()
        return
    validate_preflight()
    print("Stage 13 preflight passed.")


if __name__ == "__main__":
    main()
