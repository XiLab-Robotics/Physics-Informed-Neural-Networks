"""Prepare the full-candidate Wave 5.2R Track 2 analysis package."""

from __future__ import annotations

# Import Python Utilities
import hashlib
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


# Define Canonical Paths
CAMPAIGN_OUTPUT_ROOT = PROJECT_ROOT / "output" / "training_campaigns"
TRAINING_RUN_ROOT = PROJECT_ROOT / "output" / "training_runs"
MATRIX_CONFIG_ROOT = (
    PROJECT_ROOT
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
)
STAGE4_MATRIX_PATH = (
    MATRIX_CONFIG_ROOT
    / "wave52r_stage4_data_only_residual_common_test_matrix.yaml"
)
STAGE15_MATRIX_PATH = (
    MATRIX_CONFIG_ROOT
    / "wave52r_stage15_official_forward_verification_matrix.yaml"
)
OUTPUT_MATRIX_PATH = (
    MATRIX_CONFIG_ROOT
    / "wave52r_full_candidate_parallel_temporal_non_temporal_matrix.yaml"
)
ANALYSIS_OUTPUT_ROOT = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "full_candidate_track2_analysis"
)
CANDIDATE_INVENTORY_PATH = (
    ANALYSIS_OUTPUT_ROOT / "candidate_inventory.yaml"
)
REMOTE_SOURCE_PATH_LIST_PATH = (
    ANALYSIS_OUTPUT_ROOT / "remote_source_path_list.txt"
)
CONDITION_REFERENCE_ARCHIVE_PATH = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "complex_harmonic_coefficient_residuals"
    / "2026-07-28-16-17-13__stage5_h04"
    / "test_predictions.npz"
)
COMMON_SPLIT_SIGNATURE = (
    "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16"
)
EXPECTED_FORWARD_TEST_CURVE_COUNT = 97
EXPECTED_ANGULAR_SAMPLE_COUNT = 2048
SELECTED_HARMONIC_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]

STAGE_CAMPAIGN_NAME_FRAGMENT = {
    5: "wave52r_stage5_complex_harmonic_coefficient_residuals",
    6: "wave52r_stage6_spectral_sobolev_guidance",
    7: "wave52r_stage7_mean_centered_shape_multi_head",
    8: "wave52r_stage8_weak_forward_compliance_priors",
    9: "wave52r_stage9_temporal_analytical_residual_models",
    10: "wave52r_stage10_sparse_symbolic_discovery",
    11: "wave52r_stage11_uncertainty_trust_calibration",
    12: "wave52r_stage12_advanced_constraint_optimization",
    13: "wave52r_stage13_synthetic_weak_form_oracle_lane",
}
STAGE_TRAINING_FAMILY_DIRECTORY = {
    5: "complex_harmonic_coefficient_residuals",
    6: "spectral_sobolev_guidance",
    7: "mean_centered_shape_multi_head",
    8: "weak_forward_compliance_priors",
    9: "temporal_analytical_residual_models",
    10: "sparse_symbolic_formulation_discovery",
    12: "advanced_constraint_optimization",
}
TEMPORAL_STAGE_SET = {9, 12}


def read_yaml(yaml_path: Path) -> dict[str, Any]:
    """Read one required YAML mapping."""

    assert yaml_path.is_file(), f"Required YAML path is missing | {yaml_path}"
    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        payload = yaml.safe_load(yaml_file)
    assert isinstance(payload, dict), f"YAML root must be a mapping | {yaml_path}"
    return payload


def write_yaml(yaml_path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping with a normal final newline."""

    yaml_path.parent.mkdir(parents=True, exist_ok=True)
    with yaml_path.open("w", encoding="utf-8", newline="\n") as yaml_file:
        yaml.safe_dump(
            payload,
            yaml_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def format_project_relative_path(path: Path) -> str:
    """Format one repository path with portable separators."""

    return path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix()


def compute_file_sha256(file_path: Path) -> str:
    """Return one lowercase SHA-256 digest."""

    sha256_digest = hashlib.sha256()
    with file_path.open("rb") as input_file:
        while byte_chunk := input_file.read(1024 * 1024):
            sha256_digest.update(byte_chunk)
    return sha256_digest.hexdigest()


def resolve_completed_campaign_directory(stage_number: int) -> Path:
    """Resolve the unique completed package for one Wave 5.2R stage."""

    campaign_fragment = STAGE_CAMPAIGN_NAME_FRAGMENT[stage_number]
    campaign_directory_list = [
        candidate_path
        for candidate_path in CAMPAIGN_OUTPUT_ROOT.iterdir()
        if candidate_path.is_dir()
        and campaign_fragment in candidate_path.name
        and (candidate_path / "campaign_leaderboard.yaml").is_file()
    ]
    assert len(campaign_directory_list) == 1, (
        "Expected one completed Wave 5.2R campaign package | "
        f"stage={stage_number} | matches={len(campaign_directory_list)}"
    )
    return campaign_directory_list[0]


def resolve_leaderboard_row_list(
    leaderboard_payload: dict[str, Any],
) -> list[dict[str, Any]]:
    """Resolve the stage-specific leaderboard row collection."""

    for row_key in [
        "row_list",
        "entry_list",
        "ranked_candidate_list",
        "result_list",
    ]:
        row_list = leaderboard_payload.get(row_key)
        if isinstance(row_list, list):
            assert all(isinstance(row, dict) for row in row_list)
            return list(row_list)
    raise AssertionError("Campaign leaderboard has no supported row list.")


def resolve_run_directory(
    stage_number: int,
    leaderboard_row: dict[str, Any],
) -> Path | None:
    """Resolve one trained run directory when the row owns one."""

    explicit_run_directory = leaderboard_row.get("run_directory")
    if explicit_run_directory:
        return PROJECT_ROOT / str(explicit_run_directory).replace("\\", "/")

    explicit_output_directory = leaderboard_row.get("output_directory")
    if explicit_output_directory:
        return PROJECT_ROOT / str(explicit_output_directory).replace("\\", "/")

    run_instance_id = str(
        leaderboard_row.get("run_instance_id", "")
    ).strip()
    family_directory_name = STAGE_TRAINING_FAMILY_DIRECTORY.get(stage_number)
    if not run_instance_id or family_directory_name is None:
        return None
    candidate_run_directory = (
        TRAINING_RUN_ROOT
        / family_directory_name
        / run_instance_id
    )
    if not candidate_run_directory.is_dir():
        return None
    return candidate_run_directory


def build_inventory_entry(
    *,
    stage_number: int | None,
    candidate_id: str,
    formulation: str,
    candidate_lane: str,
    artifact_role: str,
    run_instance_id: str,
    source_path: Path | None,
    matrix_eligible: bool,
    exclusion_reason: str | None,
    random_seed: int | None,
) -> dict[str, Any]:
    """Build one normalized candidate-inventory entry."""

    return {
        "stage": (
            f"stage_{stage_number}"
            if stage_number is not None
            else "reference"
        ),
        "candidate_id": candidate_id,
        "formulation": formulation,
        "candidate_lane": candidate_lane,
        "artifact_role": artifact_role,
        "run_instance_id": run_instance_id,
        "random_seed": random_seed,
        "source_path": (
            format_project_relative_path(source_path)
            if source_path is not None and source_path.exists()
            else None
        ),
        "matrix_eligible": bool(matrix_eligible),
        "exclusion_reason": exclusion_reason,
    }


def build_precomputed_candidate_configuration(
    *,
    stage_number: int,
    candidate_id: str,
    formulation: str,
    candidate_lane: str,
    run_instance_id: str,
    prediction_archive_path: Path,
) -> dict[str, Any]:
    """Build one immutable full-curve matrix candidate."""

    return {
        "candidate_id": candidate_id,
        "candidate_family": (
            f"wave52r_stage{stage_number}_{formulation}"
        ),
        "candidate_kind": "wave52r_precomputed_full_curve",
        "candidate_source_label": (
            f"wave52r_stage{stage_number}_{candidate_lane}"
        ),
        "candidate_surface": "Fw",
        "wave52r_stage": stage_number,
        "candidate_lane": candidate_lane,
        "run_instance_id": run_instance_id,
        "prediction_archive_path": format_project_relative_path(
            prediction_archive_path
        ),
        "condition_reference_archive_path": (
            format_project_relative_path(
                CONDITION_REFERENCE_ARCHIVE_PATH
            )
        ),
        "expected_prediction_archive_sha256": compute_file_sha256(
            prediction_archive_path
        ),
        "expected_condition_reference_sha256": compute_file_sha256(
            CONDITION_REFERENCE_ARCHIVE_PATH
        ),
        "expected_split_signature": COMMON_SPLIT_SIGNATURE,
        "expected_curve_count": EXPECTED_FORWARD_TEST_CURVE_COUNT,
        "expected_angular_sample_count": EXPECTED_ANGULAR_SAMPLE_COUNT,
        "allowed_direction_list": ["forward"],
    }


def validate_prediction_archive(
    prediction_archive_path: Path,
) -> None:
    """Validate one saved prediction archive against the frozen condition order."""

    assert prediction_archive_path.is_file()
    with np.load(
        CONDITION_REFERENCE_ARCHIVE_PATH,
        allow_pickle=False,
    ) as reference_archive:
        reference_condition_id_array = np.asarray(
            reference_archive["condition_id"]
        )
        reference_measured_curve_matrix = np.asarray(
            reference_archive["measured_curve"],
            dtype=np.float64,
        )

    with np.load(
        prediction_archive_path,
        allow_pickle=False,
    ) as prediction_archive:
        measured_curve_matrix = np.asarray(
            prediction_archive["measured_curve"],
            dtype=np.float64,
        )
        predicted_curve_matrix = np.asarray(
            prediction_archive["predicted_curve"],
            dtype=np.float64,
        )
        if "condition_id" in prediction_archive.files:
            assert np.array_equal(
                np.asarray(prediction_archive["condition_id"]),
                reference_condition_id_array,
            )

    expected_shape = (
        EXPECTED_FORWARD_TEST_CURVE_COUNT,
        EXPECTED_ANGULAR_SAMPLE_COUNT,
    )
    assert measured_curve_matrix.shape == expected_shape
    assert predicted_curve_matrix.shape == expected_shape
    assert np.all(np.isfinite(predicted_curve_matrix))
    maximum_measured_curve_difference = float(
        np.max(
            np.abs(
                measured_curve_matrix
                - reference_measured_curve_matrix
            )
        )
    )
    assert maximum_measured_curve_difference <= 1.0e-7, (
        "Prediction archive does not use the frozen Wave 5.2R test order | "
        f"path={prediction_archive_path} | "
        f"max_abs_difference_deg={maximum_measured_curve_difference:.12g}"
    )


def build_stage4_inventory_and_matrix_rows() -> tuple[
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    """Reuse the already validated eighteen-candidate Stage 4 matrix."""

    stage4_matrix_payload = read_yaml(STAGE4_MATRIX_PATH)
    stage4_candidate_configuration_list = list(
        stage4_matrix_payload["comparison"]["candidate_list"]
    )
    assert len(stage4_candidate_configuration_list) == 18

    inventory_entry_list = []
    for candidate_configuration in stage4_candidate_configuration_list:
        inventory_entry_list.append(
            build_inventory_entry(
                stage_number=4,
                candidate_id=str(
                    candidate_configuration["candidate_id"]
                ),
                formulation=str(
                    candidate_configuration["candidate_family"]
                ),
                candidate_lane="non_temporal",
                artifact_role="trained_real_data_predictor",
                run_instance_id="registry_backed_stage4_run",
                source_path=PROJECT_ROOT
                / str(
                    candidate_configuration["family_registry_path"]
                ),
                matrix_eligible=True,
                exclusion_reason=None,
                random_seed=314159,
            )
        )
    return inventory_entry_list, stage4_candidate_configuration_list


def build_stage5_inventory_and_matrix_rows() -> tuple[
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    """Build Stage 5 first-screen and stability-seed inventory rows."""

    campaign_directory = resolve_completed_campaign_directory(5)
    leaderboard_payload = read_yaml(
        campaign_directory / "campaign_leaderboard.yaml"
    )
    stability_payload = read_yaml(
        campaign_directory / "campaign_stability_summary.yaml"
    )
    stage_row_list = (
        resolve_leaderboard_row_list(leaderboard_payload)
        + resolve_leaderboard_row_list(stability_payload)
    )
    assert len(stage_row_list) == 22

    inventory_entry_list = []
    matrix_candidate_list = []
    for leaderboard_row in stage_row_list:
        candidate_id = str(leaderboard_row["candidate_id"]).lower()
        random_seed = int(leaderboard_row.get("random_seed", 314159))
        run_instance_id = str(leaderboard_row["run_instance_id"])
        run_directory = resolve_run_directory(5, leaderboard_row)
        assert run_directory is not None
        prediction_archive_path = run_directory / "test_predictions.npz"
        validate_prediction_archive(prediction_archive_path)
        matrix_candidate_id = (
            f"wave52r_stage5_{candidate_id}_seed_{random_seed}"
        )
        formulation = str(leaderboard_row["formulation"])
        inventory_entry_list.append(
            build_inventory_entry(
                stage_number=5,
                candidate_id=matrix_candidate_id,
                formulation=formulation,
                candidate_lane="non_temporal",
                artifact_role="trained_real_data_predictor",
                run_instance_id=run_instance_id,
                source_path=prediction_archive_path,
                matrix_eligible=True,
                exclusion_reason=None,
                random_seed=random_seed,
            )
        )
        matrix_candidate_list.append(
            build_precomputed_candidate_configuration(
                stage_number=5,
                candidate_id=matrix_candidate_id,
                formulation=formulation,
                candidate_lane="non_temporal",
                run_instance_id=run_instance_id,
                prediction_archive_path=prediction_archive_path,
            )
        )
    return inventory_entry_list, matrix_candidate_list


def build_later_stage_inventory_and_matrix_rows(
    stage_number: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Build inventory and matrix rows for Wave 5.2R Stages 6 through 13."""

    campaign_directory = resolve_completed_campaign_directory(stage_number)
    leaderboard_payload = read_yaml(
        campaign_directory / "campaign_leaderboard.yaml"
    )
    leaderboard_row_list = resolve_leaderboard_row_list(
        leaderboard_payload
    )
    inventory_entry_list = []
    matrix_candidate_list = []
    candidate_lane = (
        "temporal"
        if stage_number in TEMPORAL_STAGE_SET
        else "non_temporal"
    )
    if stage_number == 11:
        candidate_lane = "calibration_only"
    if stage_number == 13:
        candidate_lane = "synthetic_oracle"

    for leaderboard_row in leaderboard_row_list:
        short_candidate_id = str(
            leaderboard_row.get(
                "candidate_id",
                leaderboard_row.get("run_name", "unknown"),
            )
        ).lower()
        matrix_candidate_id = (
            f"wave52r_stage{stage_number}_{short_candidate_id}"
        )
        formulation = str(
            leaderboard_row.get(
                "formulation",
                leaderboard_row.get(
                    "fit_mode",
                    leaderboard_row.get(
                        "optimization_profile",
                        "diagnostic",
                    ),
                ),
            )
        )
        run_instance_id = str(
            leaderboard_row.get("run_instance_id", "")
        )
        random_seed_value = leaderboard_row.get("random_seed")
        random_seed = (
            int(random_seed_value)
            if random_seed_value is not None
            else None
        )
        run_directory = resolve_run_directory(
            stage_number,
            leaderboard_row,
        )
        prediction_archive_path = (
            run_directory / "test_predictions.npz"
            if run_directory is not None
            else None
        )
        has_prediction_archive = (
            prediction_archive_path is not None
            and prediction_archive_path.is_file()
        )
        matrix_eligible = (
            stage_number not in {11, 13}
            and has_prediction_archive
        )
        if stage_number == 11:
            exclusion_reason = (
                "Calibration-only trust diagnostic; the frozen K01 curve "
                "remains the prediction center."
            )
            artifact_role = "calibration_diagnostic"
        elif stage_number == 13:
            exclusion_reason = (
                "Synthetic analytical-oracle result with no measured "
                "real-data prediction payload."
            )
            artifact_role = "synthetic_oracle"
        elif not has_prediction_archive:
            exclusion_reason = (
                "Frozen replay or diagnostic row without a distinct trained "
                "full-curve prediction archive."
            )
            artifact_role = "replay_or_diagnostic"
        else:
            exclusion_reason = None
            artifact_role = "trained_real_data_predictor"
            assert prediction_archive_path is not None
            validate_prediction_archive(prediction_archive_path)

        inventory_entry_list.append(
            build_inventory_entry(
                stage_number=stage_number,
                candidate_id=matrix_candidate_id,
                formulation=formulation,
                candidate_lane=candidate_lane,
                artifact_role=artifact_role,
                run_instance_id=run_instance_id,
                source_path=prediction_archive_path,
                matrix_eligible=matrix_eligible,
                exclusion_reason=exclusion_reason,
                random_seed=random_seed,
            )
        )
        if matrix_eligible:
            assert prediction_archive_path is not None
            matrix_candidate_list.append(
                build_precomputed_candidate_configuration(
                    stage_number=stage_number,
                    candidate_id=matrix_candidate_id,
                    formulation=formulation,
                    candidate_lane=candidate_lane,
                    run_instance_id=run_instance_id,
                    prediction_archive_path=prediction_archive_path,
                )
            )
    return inventory_entry_list, matrix_candidate_list


def build_reference_inventory_and_matrix_rows() -> tuple[
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    """Add PF-A and the accepted temporal and non-temporal references."""

    stage15_payload = read_yaml(STAGE15_MATRIX_PATH)
    stage15_candidate_list = list(
        stage15_payload["comparison"]["candidate_list"]
    )
    reference_candidate_list = [
        candidate_configuration
        for candidate_configuration in stage15_candidate_list
        if str(candidate_configuration["candidate_id"])
        in {
            "wave52r_stage15_pf_a_setpoint_quadratic_Fw",
            "accepted_periodic_mlp_harmonic_Fw",
            "accepted_periodic_gru_sequence_Fw",
        }
    ]
    assert len(reference_candidate_list) == 3
    lane_by_candidate_id = {
        "wave52r_stage15_pf_a_setpoint_quadratic_Fw": "analytical",
        "accepted_periodic_mlp_harmonic_Fw": "non_temporal",
        "accepted_periodic_gru_sequence_Fw": "temporal",
    }
    inventory_entry_list = []
    for candidate_configuration in reference_candidate_list:
        candidate_id = str(candidate_configuration["candidate_id"])
        source_path_text = candidate_configuration.get(
            "reference_inventory_path",
            candidate_configuration.get("analytical_anchor_path"),
        )
        assert source_path_text is not None
        inventory_entry_list.append(
            build_inventory_entry(
                stage_number=None,
                candidate_id=candidate_id,
                formulation=str(
                    candidate_configuration["candidate_family"]
                ),
                candidate_lane=lane_by_candidate_id[candidate_id],
                artifact_role="frozen_reference",
                run_instance_id="frozen_reference",
                source_path=PROJECT_ROOT / str(source_path_text),
                matrix_eligible=True,
                exclusion_reason=None,
                random_seed=None,
            )
        )
    return inventory_entry_list, reference_candidate_list


def build_remote_source_path_list(
    matrix_candidate_list: list[dict[str, Any]],
) -> list[str]:
    """Build the exact source list required by remote matrix execution."""

    source_path_set = {
        format_project_relative_path(OUTPUT_MATRIX_PATH),
        format_project_relative_path(CANDIDATE_INVENTORY_PATH),
        format_project_relative_path(CONDITION_REFERENCE_ARCHIVE_PATH),
        "output/training_runs/data_only_residual_capacity",
        (
            "output/training_campaigns/"
            "2026-07-28-10-01-40_wave52r_stage4_data_only_"
            "residual_capacity_2026_07_28"
        ),
        (
            "output/analysis/wave_5_2r/"
            "stage4_data_only_residual_capacity_ladder/"
            "stage4_causal_setpoint_pf_a_surface.yaml"
        ),
        "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml",
        "models/polished_dataset/setpoints/periodic_mlp_harmonic/forward",
        "models/polished_dataset/setpoints/periodic_gru_sequence/forward",
    }
    for candidate_configuration in matrix_candidate_list:
        for path_key in [
            "prediction_archive_path",
            "checkpoint_path",
            "training_config_path",
            "analytical_anchor_path",
            "reference_inventory_path",
            "family_registry_path",
        ]:
            path_value = candidate_configuration.get(path_key)
            if path_value:
                source_path_set.add(str(path_value).replace("\\", "/"))
    for source_path_text in source_path_set:
        assert (PROJECT_ROOT / source_path_text).exists(), (
            f"Remote source path does not exist | {source_path_text}"
        )

    # Avoid adding a child path when an already declared directory packages
    # the same content. This keeps remote tar archives deterministic and
    # prevents duplicate entries without broadening the synchronized scope.
    minimized_source_path_list: list[str] = []
    for source_path_text in sorted(
        source_path_set,
        key=lambda value: (len(Path(value).parts), value),
    ):
        source_path = PROJECT_ROOT / source_path_text
        covered_by_existing_directory = any(
            (PROJECT_ROOT / existing_source_path_text).is_dir()
            and source_path.is_relative_to(
                PROJECT_ROOT / existing_source_path_text
            )
            for existing_source_path_text in minimized_source_path_list
        )
        if not covered_by_existing_directory:
            minimized_source_path_list.append(source_path_text)
    return sorted(minimized_source_path_list)


def main() -> None:
    """Prepare the complete eligible Wave 5.2R forward Track 2 package."""

    assert CONDITION_REFERENCE_ARCHIVE_PATH.is_file()
    inventory_entry_list: list[dict[str, Any]] = []
    matrix_candidate_list: list[dict[str, Any]] = []

    stage4_inventory, stage4_candidates = (
        build_stage4_inventory_and_matrix_rows()
    )
    inventory_entry_list.extend(stage4_inventory)
    matrix_candidate_list.extend(stage4_candidates)

    stage5_inventory, stage5_candidates = (
        build_stage5_inventory_and_matrix_rows()
    )
    inventory_entry_list.extend(stage5_inventory)
    matrix_candidate_list.extend(stage5_candidates)

    for stage_number in range(6, 14):
        stage_inventory, stage_candidates = (
            build_later_stage_inventory_and_matrix_rows(stage_number)
        )
        inventory_entry_list.extend(stage_inventory)
        matrix_candidate_list.extend(stage_candidates)

    reference_inventory, reference_candidates = (
        build_reference_inventory_and_matrix_rows()
    )
    inventory_entry_list.extend(reference_inventory)
    matrix_candidate_list.extend(reference_candidates)

    candidate_id_list = [
        str(candidate_configuration["candidate_id"])
        for candidate_configuration in matrix_candidate_list
    ]
    assert len(candidate_id_list) == len(set(candidate_id_list)), (
        "Track 2 matrix candidate identifiers must be unique."
    )

    eligible_inventory_entry_list = [
        inventory_entry
        for inventory_entry in inventory_entry_list
        if inventory_entry["matrix_eligible"]
    ]
    assert len(eligible_inventory_entry_list) == len(matrix_candidate_list)
    temporal_candidate_count = sum(
        inventory_entry["candidate_lane"] == "temporal"
        and inventory_entry["matrix_eligible"]
        for inventory_entry in inventory_entry_list
    )
    non_temporal_candidate_count = sum(
        inventory_entry["candidate_lane"] == "non_temporal"
        and inventory_entry["matrix_eligible"]
        for inventory_entry in inventory_entry_list
    )

    matrix_payload = {
        "paths": {
            "dataset_config_path": (
                "config/datasets/transmission_error_dataset.yaml"
            ),
        },
        "dataset": {
            "name": "polished_dataset",
            "input_mode": "setpoints",
            "split_manifest_path": (
                "output/analysis/polynomial_fourier_benchmark/"
                "common_split_manifest.yaml"
            ),
            "excluded_condition_id_list": [
                "speed_500rpm__torque_600Nm__temperature_35degC",
                "speed_800rpm__torque_200Nm__temperature_25degC",
                "speed_1400rpm__torque_800Nm__temperature_35degC",
            ],
            "expected_curve_count_by_split": {
                "train": 1350,
                "validation": 388,
                "test": 194,
            },
        },
        "experiment": {
            "run_name": (
                "wave52r_full_candidate_parallel_temporal_non_temporal"
            ),
            "model_family": "track2_reference_comparison",
            "model_type": "reference_family_vs_feedforward",
        },
        "comparison": {
            "comparison_mode": (
                "wave52r_full_candidate_forward_curve_first"
            ),
            "lightweight_test_curve_records": True,
            "percentage_error_denominator": "peak_to_peak_truth",
            "preview_curve_count": 6,
            "candidate_list": matrix_candidate_list,
        },
        "evaluation": {
            "selected_harmonics": list(SELECTED_HARMONIC_LIST),
            "decomposition_point_stride": 1,
        },
        "metadata": {
            "roadmap_scope": "wave52r_stages_0_through_15",
            "candidate_inventory_path": (
                format_project_relative_path(CANDIDATE_INVENTORY_PATH)
            ),
            "expected_candidate_count": len(matrix_candidate_list),
            "expected_temporal_candidate_count": temporal_candidate_count,
            "expected_non_temporal_candidate_count": (
                non_temporal_candidate_count
            ),
            "official_te_curve_verification_pipeline_refresh": True,
            "acceptance_policy_path": (
                "doc/reports/analysis/te_curve_verification_pipeline/"
                "00_overview/multi_index_curve_first_selection_policy/"
                "[2026-06-16]/"
                "track2_multi_index_curve_first_selection_policy.md"
            ),
            "registry_updates_before_acceptance": "prohibited",
        },
    }
    write_yaml(OUTPUT_MATRIX_PATH, matrix_payload)

    count_by_stage: dict[str, dict[str, int]] = {}
    for inventory_entry in inventory_entry_list:
        stage_label = str(inventory_entry["stage"])
        stage_count_dictionary = count_by_stage.setdefault(
            stage_label,
            {"inventory": 0, "matrix_eligible": 0},
        )
        stage_count_dictionary["inventory"] += 1
        stage_count_dictionary["matrix_eligible"] += int(
            inventory_entry["matrix_eligible"]
        )
    inventory_payload = {
        "schema_version": 1,
        "analysis_id": (
            "wave52r_full_candidate_parallel_temporal_non_temporal"
        ),
        "dataset": "polished_dataset",
        "input_mode": "setpoints",
        "surface": "Fw",
        "split_signature": COMMON_SPLIT_SIGNATURE,
        "expected_forward_test_curve_count": (
            EXPECTED_FORWARD_TEST_CURVE_COUNT
        ),
        "inventory_entry_count": len(inventory_entry_list),
        "matrix_eligible_candidate_count": len(matrix_candidate_list),
        "temporal_candidate_count": temporal_candidate_count,
        "non_temporal_candidate_count": non_temporal_candidate_count,
        "count_by_stage": count_by_stage,
        "candidate_list": inventory_entry_list,
    }
    write_yaml(CANDIDATE_INVENTORY_PATH, inventory_payload)

    remote_source_path_list = build_remote_source_path_list(
        matrix_candidate_list
    )
    REMOTE_SOURCE_PATH_LIST_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    REMOTE_SOURCE_PATH_LIST_PATH.write_text(
        "\n".join(remote_source_path_list) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    print(
        "WAVE52R_FULL_CANDIDATE_TRACK2_PACKAGE_PREPARED "
        f"inventory={len(inventory_entry_list)} "
        f"eligible={len(matrix_candidate_list)} "
        f"temporal={temporal_candidate_count} "
        f"non_temporal={non_temporal_candidate_count}"
    )
    print(format_project_relative_path(OUTPUT_MATRIX_PATH))
    print(format_project_relative_path(CANDIDATE_INVENTORY_PATH))
    print(format_project_relative_path(REMOTE_SOURCE_PATH_LIST_PATH))


if __name__ == "__main__":
    main()
