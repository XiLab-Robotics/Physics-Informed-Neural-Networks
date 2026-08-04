"""Prepare the trained integrated-specialist TE Curve Verification package."""

from __future__ import annotations

# Import Python Utilities
import csv
import hashlib
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import YAML Utilities
import yaml


# Define Package Paths And Frozen Contracts
CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output/training_campaigns/2026-08-03-17-49-23_wave52r_integrated_specialist_model_2026_08_02"
)
CAMPAIGN_RESULTS_PATH = CAMPAIGN_OUTPUT_DIRECTORY / "campaign_results.csv"
OUTPUT_ROOT = PROJECT_ROOT / "output/analysis/wave_5_2r/integrated_specialist_track2"
CONFIG_PATH = (
    PROJECT_ROOT
    / "config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward"
    / "wave52r_integrated_specialist_track2_matrix.yaml"
)
INVENTORY_PATH = OUTPUT_ROOT / "candidate_inventory.yaml"
REMOTE_SOURCE_PATH_LIST_PATH = OUTPUT_ROOT / "remote_source_path_list.txt"
SPLIT_MANIFEST_PATH = PROJECT_ROOT / "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml"
CONTROL_CONFIG_PATH = (
    PROJECT_ROOT
    / "config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward"
    / "wave52r_offline_leader_cross_surface_promotion_matrix.yaml"
)
CONDITION_REFERENCE_ARCHIVE_PATH = (
    PROJECT_ROOT
    / "output/training_runs/complex_harmonic_coefficient_residuals"
    / "2026-07-31-11-05-16__stage5_h04__seed_271828/test_predictions.npz"
)
EXPECTED_SPLIT_SIGNATURE = "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16"
TRAINED_ABLATION_ID_LIST = ["A02", "A03", "A04", "A05", "A06", "A07", "A08"]
TRAINED_SEED_LIST = [161803, 271828, 314159]
CONTROL_CANDIDATE_ID_LIST = [
    "wave52r_promotion_h08_fw_seed_161803",
    "wave52r_promotion_k01_global_seed_271828",
    "accepted_periodic_gru_sequence_Fw",
    "accepted_periodic_mlp_harmonic_Fw",
    "accepted_periodic_gru_sequence_Bw",
    "accepted_periodic_mlp_harmonic_Bw",
    "accepted_periodic_gru_sequence_global",
    "accepted_periodic_mlp_harmonic_global",
]
EXCLUDED_CONDITION_ID_LIST = [
    "speed_500rpm__torque_600Nm__temperature_35degC",
    "speed_800rpm__torque_200Nm__temperature_25degC",
    "speed_1400rpm__torque_800Nm__temperature_35degC",
]


def read_yaml(input_path: Path) -> dict[str, Any]:
    """Read one YAML mapping."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def write_yaml(output_path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=False, width=120)


def compute_file_sha256(input_path: Path) -> str:
    """Compute one immutable artifact digest."""

    digest = hashlib.sha256()
    with input_path.open("rb") as input_file:
        for chunk in iter(lambda: input_file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_trained_rows() -> list[dict[str, str]]:
    """Load the 21 completed trainable-arm rows."""

    with CAMPAIGN_RESULTS_PATH.open("r", encoding="utf-8", newline="") as input_file:
        all_rows = list(csv.DictReader(input_file))
    trained_rows = [
        row
        for row in all_rows
        if row["ablation_id"] in TRAINED_ABLATION_ID_LIST and row["status"] == "completed"
    ]
    observed_pair_set = {
        (row["ablation_id"], int(row["random_seed"]))
        for row in trained_rows
    }
    expected_pair_set = {
        (ablation_id, seed)
        for ablation_id in TRAINED_ABLATION_ID_LIST
        for seed in TRAINED_SEED_LIST
    }
    assert observed_pair_set == expected_pair_set
    assert len(trained_rows) == 21
    return trained_rows


def build_trained_candidate(result_row: dict[str, str]) -> dict[str, Any]:
    """Build one immutable integrated-specialist candidate declaration."""

    ablation_id = result_row["ablation_id"]
    seed = int(result_row["random_seed"])
    run_instance_id = result_row["run_instance_id"]
    run_directory = PROJECT_ROOT / "output/training_runs/integrated_specialist_models" / run_instance_id
    prediction_archive_path = run_directory / "test_predictions.npz"
    gate_passed = result_row["gate_passed"].strip().lower() == "true"
    return {
        "candidate_id": f"wave52r_integrated_{ablation_id.lower()}_seed_{seed}",
        "candidate_family": f"wave52r_integrated_specialist_{ablation_id.lower()}",
        "candidate_kind": "wave52r_precomputed_full_curve",
        "candidate_source_label": "wave52r_integrated_specialist_trained",
        "candidate_surface": "global",
        "wave52r_stage": "integrated_specialist",
        "candidate_lane": "empirical_integrated_specialist",
        "ablation_id": ablation_id,
        "run_instance_id": run_instance_id,
        "random_seed": seed,
        "campaign_gate_passed": gate_passed,
        "passed_branch_list": result_row.get("passed_branch_list", ""),
        "prediction_archive_path": prediction_archive_path.relative_to(PROJECT_ROOT).as_posix(),
        "condition_reference_archive_path": CONDITION_REFERENCE_ARCHIVE_PATH.relative_to(PROJECT_ROOT).as_posix(),
        "expected_prediction_archive_sha256": compute_file_sha256(prediction_archive_path),
        "expected_condition_reference_sha256": compute_file_sha256(CONDITION_REFERENCE_ARCHIVE_PATH),
        "expected_split_signature": EXPECTED_SPLIT_SIGNATURE,
        "expected_curve_count": 194,
        "expected_angular_sample_count": 2048,
        "allowed_direction_list": ["forward", "backward"],
    }


def load_control_candidates() -> list[dict[str, Any]]:
    """Reuse the frozen ingredient and accepted-incumbent declarations."""

    control_config = read_yaml(CONTROL_CONFIG_PATH)
    candidate_by_id = {
        str(candidate["candidate_id"]): candidate
        for candidate in control_config["comparison"]["candidate_list"]
    }
    assert all(candidate_id in candidate_by_id for candidate_id in CONTROL_CANDIDATE_ID_LIST)
    return [candidate_by_id[candidate_id] for candidate_id in CONTROL_CANDIDATE_ID_LIST]


def build_config(candidate_list: list[dict[str, Any]]) -> dict[str, Any]:
    """Build the bounded three-surface matrix configuration."""

    split_manifest = read_yaml(SPLIT_MANIFEST_PATH)
    expected_curve_count_by_split = {
        split_name: int(curve_count)
        for split_name, curve_count in split_manifest["split"]["directional_file_count_by_split"].items()
    }
    expected_curve_count_by_split["train"] -= 2 * len(EXCLUDED_CONDITION_ID_LIST)
    assert expected_curve_count_by_split == {"train": 1350, "validation": 388, "test": 194}
    return {
        "paths": {"dataset_config_path": "config/datasets/transmission_error_dataset.yaml"},
        "dataset": {
            "name": "polished_dataset",
            "input_mode": "setpoints",
            "split_manifest_path": SPLIT_MANIFEST_PATH.relative_to(PROJECT_ROOT).as_posix(),
            "excluded_condition_id_list": EXCLUDED_CONDITION_ID_LIST,
            "expected_curve_count_by_split": expected_curve_count_by_split,
        },
        "experiment": {
            "run_name": "wave52r_integrated_specialist_track2",
            "model_family": "track2_reference_comparison",
            "model_type": "reference_family_vs_feedforward",
        },
        "comparison": {
            "comparison_mode": "wave52r_integrated_specialist_curve_first",
            "lightweight_test_curve_records": True,
            "percentage_error_denominator": "peak_to_peak_truth",
            "preview_curve_count": 8,
            "candidate_list": candidate_list,
        },
        "evaluation": {
            "selected_harmonics": [0, 1, 3, 39, 40, 78, 81, 156, 162, 240],
            "decomposition_point_stride": 1,
        },
        "metadata": {
            "candidate_inventory_path": INVENTORY_PATH.relative_to(PROJECT_ROOT).as_posix(),
            "expected_candidate_count": 29,
            "expected_trained_candidate_count": 21,
            "expected_ingredient_control_count": 2,
            "expected_incumbent_count": 6,
            "official_te_curve_verification_pipeline_refresh": True,
            "acceptance_policy_path": "doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md",
            "registry_updates_before_acceptance": "prohibited",
        },
    }


def write_remote_source_manifest(candidate_list: list[dict[str, Any]]) -> None:
    """Write every immutable path required by remote execution."""

    path_set = {
        CONFIG_PATH.relative_to(PROJECT_ROOT).as_posix(),
        INVENTORY_PATH.relative_to(PROJECT_ROOT).as_posix(),
        CAMPAIGN_RESULTS_PATH.relative_to(PROJECT_ROOT).as_posix(),
        CONTROL_CONFIG_PATH.relative_to(PROJECT_ROOT).as_posix(),
    }
    for candidate in candidate_list:
        for key in ("prediction_archive_path", "condition_reference_archive_path", "reference_inventory_path"):
            if key not in candidate:
                continue
            path_set.add(str(candidate[key]))
            if key == "reference_inventory_path":
                path_set.add(str(Path(str(candidate[key])).parent))
    REMOTE_SOURCE_PATH_LIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    REMOTE_SOURCE_PATH_LIST_PATH.write_text("\n".join(sorted(path_set)) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    """Prepare the config, inventory, and remote artifact manifest."""

    trained_candidates = [build_trained_candidate(row) for row in load_trained_rows()]
    candidate_list = trained_candidates + load_control_candidates()
    assert len(candidate_list) == 29
    write_yaml(CONFIG_PATH, build_config(candidate_list))
    write_yaml(
        INVENTORY_PATH,
        {
            "schema_version": 1,
            "analysis_id": "wave52r_integrated_specialist_track2",
            "dataset": "polished_dataset",
            "input_mode": "setpoints",
            "candidate_count": 29,
            "trained_candidate_count": 21,
            "ingredient_control_count": 2,
            "incumbent_count": 6,
            "surface_list": ["Fw", "Bw", "global"],
            "candidate_list": candidate_list,
        },
    )
    write_remote_source_manifest(candidate_list)
    print("[PASS] Prepared integrated-specialist Track 2 package | candidates=29 | trained=21 | controls=8")


if __name__ == "__main__":
    main()
