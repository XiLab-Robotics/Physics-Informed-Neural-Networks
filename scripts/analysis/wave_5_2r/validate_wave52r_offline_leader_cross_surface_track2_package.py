"""Validate the K01/H08 cross-surface Track 2 package without running it."""

from __future__ import annotations

# Import Python Utilities
import argparse
from datetime import datetime
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import YAML Utilities
import yaml

# Import Track 2 Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support as track2_support,
)


DEFAULT_CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "wave52r_offline_leader_cross_surface_promotion_matrix.yaml"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "offline_leader_cross_surface_track2"
    / "package_preflight_summary.yaml"
)
EXPECTED_EXCLUDED_CONDITION_ID_LIST = [
    "speed_500rpm__torque_600Nm__temperature_35degC",
    "speed_800rpm__torque_200Nm__temperature_25degC",
    "speed_1400rpm__torque_800Nm__temperature_35degC",
]
EXPECTED_CURVE_COUNT_BY_SPLIT = {
    "train": 1350,
    "validation": 388,
    "test": 194,
}


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


def validate_package(config_path: Path) -> dict[str, Any]:
    """Load every candidate and validate directional package invariants."""

    config = track2_support.load_reference_family_comparison_config(config_path)
    dataset_configuration = config["dataset"]
    assert dataset_configuration["excluded_condition_id_list"] == (
        EXPECTED_EXCLUDED_CONDITION_ID_LIST
    ), "Wave 5.2R exclusion contract is incomplete"
    assert dataset_configuration["expected_curve_count_by_split"] == (
        EXPECTED_CURVE_COUNT_BY_SPLIT
    ), "Wave 5.2R split-count contract changed unexpectedly"

    split_manifest_path = PROJECT_ROOT / dataset_configuration["split_manifest_path"]
    split_manifest = read_yaml(split_manifest_path)
    split_entry_by_condition_id = {
        str(entry["condition_id"]): entry
        for entry in split_manifest["entry_list"]
    }
    assert all(
        split_entry_by_condition_id[condition_id]["split"] == "train"
        for condition_id in EXPECTED_EXCLUDED_CONDITION_ID_LIST
    ), "Wave 5.2R exclusions no longer belong to the training split"
    observed_curve_count_by_split = {
        split_name: int(curve_count)
        for split_name, curve_count in split_manifest["split"][
            "directional_file_count_by_split"
        ].items()
    }
    observed_curve_count_by_split["train"] -= 2 * len(
        EXPECTED_EXCLUDED_CONDITION_ID_LIST
    )
    assert observed_curve_count_by_split == EXPECTED_CURVE_COUNT_BY_SPLIT

    candidate_configurations = track2_support.resolve_track2_candidate_configuration_list(config)
    assert len(candidate_configurations) == 24
    candidate_ids = [str(candidate["candidate_id"]) for candidate in candidate_configurations]
    assert len(candidate_ids) == len(set(candidate_ids))

    surface_count = {"Fw": 0, "Bw": 0, "global": 0}
    promotion_count = 0
    incumbent_count = 0
    candidate_kind_count: dict[str, int] = {}
    for candidate_configuration in candidate_configurations:
        surface = str(candidate_configuration["candidate_surface"])
        surface_count[surface] += 1
        loaded_candidate = track2_support.load_track2_candidate(candidate_configuration)
        candidate_kind_count[loaded_candidate.candidate_kind] = candidate_kind_count.get(loaded_candidate.candidate_kind, 0) + 1
        if candidate_configuration["candidate_source_label"] == "wave52r_offline_leader_cross_surface_promotion":
            promotion_count += 1
        else:
            assert candidate_configuration["candidate_source_label"] == "accepted_non_pinn_incumbent"
            incumbent_count += 1

    assert surface_count == {"Fw": 8, "Bw": 8, "global": 8}
    assert promotion_count == 18
    assert incumbent_count == 6
    summary = {
        "schema_version": 1,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "passed",
        "config_path": config_path.relative_to(PROJECT_ROOT).as_posix(),
        "candidate_count": len(candidate_configurations),
        "promotion_candidate_count": promotion_count,
        "incumbent_count": incumbent_count,
        "surface_candidate_count": surface_count,
        "candidate_kind_count": candidate_kind_count,
        "excluded_condition_id_list": EXPECTED_EXCLUDED_CONDITION_ID_LIST,
        "curve_count_by_split": observed_curve_count_by_split,
        "heavy_matrix_executed": False,
        "promotion_authorized": False,
    }
    write_yaml(OUTPUT_PATH, summary)
    print("[PASS] Cross-surface Track 2 preflight | surfaces=3 | candidates=24 | heavy_matrix=false")
    return summary


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--config-path", default=str(DEFAULT_CONFIG_PATH))
    parser.add_argument("--windows", action="store_true")
    parser.add_argument("--linux", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Validate the configured package."""

    arguments = parse_arguments()
    config_path = Path(arguments.config_path)
    if not config_path.is_absolute():
        config_path = PROJECT_ROOT / config_path
    validate_package(config_path.resolve())


if __name__ == "__main__":
    main()
