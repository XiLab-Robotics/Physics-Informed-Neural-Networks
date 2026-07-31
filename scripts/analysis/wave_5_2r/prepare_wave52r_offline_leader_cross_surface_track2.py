"""Prepare the K01/H08 cross-surface TE Curve Verification package."""

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


# Define Package Paths
CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_campaigns"
    / "2026-07-31-10-39-08_wave52r_offline_leader_cross_surface_promotion_2026_07_30"
)
CAMPAIGN_RESULTS_PATH = CAMPAIGN_OUTPUT_DIRECTORY / "campaign_results.csv"
OUTPUT_ROOT = PROJECT_ROOT / "output" / "analysis" / "wave_5_2r" / "offline_leader_cross_surface_track2"
CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "wave52r_offline_leader_cross_surface_promotion_matrix.yaml"
)
INVENTORY_PATH = OUTPUT_ROOT / "candidate_inventory.yaml"
REMOTE_SOURCE_PATH_LIST_PATH = OUTPUT_ROOT / "remote_source_path_list.txt"
SPLIT_MANIFEST_PATH = PROJECT_ROOT / "output" / "analysis" / "polynomial_fourier_benchmark" / "common_split_manifest.yaml"
SURFACE_DIRECTION_LIST_MAP = {
    "Fw": ["forward"],
    "Bw": ["backward"],
    "global": ["forward", "backward"],
}
SURFACE_ARCHIVE_FOLDER_MAP = {
    "Fw": "forward",
    "Bw": "backward",
    "global": "global",
}
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
    """Compute one artifact digest."""

    digest = hashlib.sha256()
    with input_path.open("rb") as input_file:
        for chunk in iter(lambda: input_file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_campaign_rows() -> list[dict[str, str]]:
    """Load and validate the completed campaign result rows."""

    with CAMPAIGN_RESULTS_PATH.open("r", encoding="utf-8", newline="") as input_file:
        rows = list(csv.DictReader(input_file))
    assert len(rows) == 27
    assert all(row["status"] == "completed" for row in rows)
    return rows


def build_precomputed_candidate(
    result_row: dict[str, str],
    condition_reference_row: dict[str, str],
) -> dict[str, Any]:
    """Build one immutable precomputed-candidate declaration."""

    surface = result_row["surface"]
    candidate_id = result_row["candidate_id"]
    seed = int(result_row["random_seed"])
    run_directory = PROJECT_ROOT / result_row["run_directory"]
    reference_run_directory = PROJECT_ROOT / condition_reference_row["run_directory"]
    prediction_archive_path = run_directory / "test_predictions.npz"
    condition_reference_path = reference_run_directory / "test_predictions.npz"
    promotion_metadata = read_yaml(run_directory / "promotion_metadata.yaml")
    return {
        "candidate_id": f"wave52r_promotion_{candidate_id.lower()}_{surface.lower()}_seed_{seed}",
        "candidate_family": f"wave52r_promotion_{candidate_id.lower()}",
        "candidate_kind": "wave52r_precomputed_full_curve",
        "candidate_source_label": "wave52r_offline_leader_cross_surface_promotion",
        "candidate_surface": surface,
        "wave52r_stage": 9 if candidate_id == "K01" else 5,
        "candidate_lane": "temporal" if candidate_id == "K01" else "non_temporal",
        "run_instance_id": result_row["run_instance_id"],
        "random_seed": seed,
        "prediction_archive_path": prediction_archive_path.relative_to(PROJECT_ROOT).as_posix(),
        "condition_reference_archive_path": condition_reference_path.relative_to(PROJECT_ROOT).as_posix(),
        "expected_prediction_archive_sha256": compute_file_sha256(prediction_archive_path),
        "expected_condition_reference_sha256": compute_file_sha256(condition_reference_path),
        "expected_split_signature": promotion_metadata["split_signature"],
        "expected_curve_count": 194 if surface == "global" else 97,
        "expected_angular_sample_count": 2048,
        "allowed_direction_list": SURFACE_DIRECTION_LIST_MAP[surface],
    }


def build_incumbent_candidate(model_family: str, surface: str) -> dict[str, Any]:
    """Build one frozen non-PINN incumbent declaration."""

    archive_folder = SURFACE_ARCHIVE_FOLDER_MAP[surface]
    return {
        "candidate_id": f"accepted_{model_family}_{surface}",
        "candidate_family": model_family,
        "candidate_kind": "wave1_exported_model",
        "candidate_source_label": "accepted_non_pinn_incumbent",
        "candidate_surface": surface,
        "reference_inventory_path": (
            f"models/polished_dataset/setpoints/{model_family}/"
            f"{archive_folder}/reference_inventory.yaml"
        ),
        "allowed_direction_list": SURFACE_DIRECTION_LIST_MAP[surface],
    }


def build_candidate_list(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    """Build 18 promotion candidates and six incumbent controls."""

    h04_lookup = {
        (row["surface"], row["random_seed"]): row
        for row in rows
        if row["candidate_id"] == "H04"
    }
    candidate_list = []
    for row in rows:
        if row["candidate_id"] not in {"K01", "H08"}:
            continue
        reference_row = h04_lookup[(row["surface"], row["random_seed"])]
        candidate_list.append(build_precomputed_candidate(row, reference_row))
    for surface in ("Fw", "Bw", "global"):
        for model_family in ("periodic_gru_sequence", "periodic_mlp_harmonic"):
            candidate_list.append(build_incumbent_candidate(model_family, surface))
    assert len(candidate_list) == 24
    return candidate_list


def build_config(candidate_list: list[dict[str, Any]]) -> dict[str, Any]:
    """Build the bounded directional matrix configuration."""

    split_manifest = read_yaml(SPLIT_MANIFEST_PATH)
    split_entry_by_condition_id = {
        str(entry["condition_id"]): entry
        for entry in split_manifest["entry_list"]
    }
    for excluded_condition_id in EXCLUDED_CONDITION_ID_LIST:
        assert excluded_condition_id in split_entry_by_condition_id, (
            "Wave 5.2R excluded condition is absent from the common split "
            f"manifest: {excluded_condition_id}"
        )
        assert split_entry_by_condition_id[excluded_condition_id]["split"] == "train", (
            "Wave 5.2R excluded condition unexpectedly changed split: "
            f"{excluded_condition_id}"
        )

    expected_curve_count_by_split = {
        split_name: int(curve_count)
        for split_name, curve_count in split_manifest["split"][
            "directional_file_count_by_split"
        ].items()
    }
    expected_curve_count_by_split["train"] -= 2 * len(EXCLUDED_CONDITION_ID_LIST)
    assert expected_curve_count_by_split == {
        "train": 1350,
        "validation": 388,
        "test": 194,
    }
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
            "run_name": "wave52r_offline_leader_cross_surface_track2",
            "model_family": "track2_reference_comparison",
            "model_type": "reference_family_vs_feedforward",
        },
        "comparison": {
            "comparison_mode": "wave52r_offline_leader_cross_surface_curve_first",
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
            "expected_candidate_count": 24,
            "expected_promotion_candidate_count": 18,
            "expected_incumbent_count": 6,
            "official_te_curve_verification_pipeline_refresh": True,
            "acceptance_policy_path": "doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md",
            "registry_updates_before_acceptance": "prohibited",
        },
    }


def write_inventory(candidate_list: list[dict[str, Any]]) -> None:
    """Write the auditable candidate inventory."""

    write_yaml(
        INVENTORY_PATH,
        {
            "schema_version": 1,
            "analysis_id": "wave52r_offline_leader_cross_surface_track2",
            "dataset": "polished_dataset",
            "input_mode": "setpoints",
            "candidate_count": len(candidate_list),
            "promotion_candidate_count": 18,
            "incumbent_count": 6,
            "surface_list": ["Fw", "Bw", "global"],
            "candidate_list": candidate_list,
        },
    )


def write_remote_source_manifest(candidate_list: list[dict[str, Any]]) -> None:
    """Write every immutable artifact path needed by remote execution."""

    path_set = {
        CONFIG_PATH.relative_to(PROJECT_ROOT).as_posix(),
        INVENTORY_PATH.relative_to(PROJECT_ROOT).as_posix(),
        CAMPAIGN_OUTPUT_DIRECTORY.relative_to(PROJECT_ROOT).as_posix(),
    }
    for candidate in candidate_list:
        for key in ("prediction_archive_path", "condition_reference_archive_path", "reference_inventory_path"):
            if key in candidate:
                path_set.add(str(candidate[key]))
                if key == "reference_inventory_path":
                    path_set.add(str(Path(str(candidate[key])).parent))
    REMOTE_SOURCE_PATH_LIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    REMOTE_SOURCE_PATH_LIST_PATH.write_text("\n".join(sorted(path_set)) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    """Prepare config, inventory, and remote artifact manifest."""

    rows = load_campaign_rows()
    candidate_list = build_candidate_list(rows)
    write_yaml(CONFIG_PATH, build_config(candidate_list))
    write_inventory(candidate_list)
    write_remote_source_manifest(candidate_list)
    print("[PASS] Prepared cross-surface Track 2 package | candidates=24 | promotion=18 | incumbents=6")


if __name__ == "__main__":
    main()
