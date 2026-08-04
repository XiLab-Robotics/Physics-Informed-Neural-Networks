"""Validate the integrated-specialist Track 2 package without running it."""

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
    / "config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward"
    / "wave52r_integrated_specialist_track2_matrix.yaml"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "output/analysis/wave_5_2r/integrated_specialist_track2/package_preflight_summary.yaml"
)
EXPECTED_ABLATION_ID_LIST = ["A02", "A03", "A04", "A05", "A06", "A07", "A08"]
EXPECTED_SEED_LIST = [161803, 271828, 314159]
EXPECTED_EXCLUDED_CONDITION_ID_LIST = [
    "speed_500rpm__torque_600Nm__temperature_35degC",
    "speed_800rpm__torque_200Nm__temperature_25degC",
    "speed_1400rpm__torque_800Nm__temperature_35degC",
]
EXPECTED_CURVE_COUNT_BY_SPLIT = {"train": 1350, "validation": 388, "test": 194}


def read_yaml(input_path: Path) -> dict[str, Any]:
    """Read one YAML mapping."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def write_yaml(output_path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping."""

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=False, width=120)


def validate_package(config_path: Path) -> dict[str, Any]:
    """Load every candidate and validate package invariants."""

    config = track2_support.load_reference_family_comparison_config(config_path)
    dataset_configuration = config["dataset"]
    assert dataset_configuration["excluded_condition_id_list"] == EXPECTED_EXCLUDED_CONDITION_ID_LIST
    assert dataset_configuration["expected_curve_count_by_split"] == EXPECTED_CURVE_COUNT_BY_SPLIT

    candidate_configurations = track2_support.resolve_track2_candidate_configuration_list(config)
    assert len(candidate_configurations) == 29
    candidate_ids = [str(candidate["candidate_id"]) for candidate in candidate_configurations]
    assert len(candidate_ids) == len(set(candidate_ids))

    surface_count = {"Fw": 0, "Bw": 0, "global": 0}
    source_count: dict[str, int] = {}
    candidate_kind_count: dict[str, int] = {}
    observed_trained_pair_set: set[tuple[str, int]] = set()
    gate_passed_candidate_id_list = []
    for candidate_configuration in candidate_configurations:
        surface = str(candidate_configuration["candidate_surface"])
        surface_count[surface] += 1
        source_label = str(candidate_configuration["candidate_source_label"])
        source_count[source_label] = source_count.get(source_label, 0) + 1
        loaded_candidate = track2_support.load_track2_candidate(candidate_configuration)
        candidate_kind_count[loaded_candidate.candidate_kind] = (
            candidate_kind_count.get(loaded_candidate.candidate_kind, 0) + 1
        )
        if source_label == "wave52r_integrated_specialist_trained":
            observed_trained_pair_set.add(
                (str(candidate_configuration["ablation_id"]), int(candidate_configuration["random_seed"]))
            )
            if bool(candidate_configuration["campaign_gate_passed"]):
                gate_passed_candidate_id_list.append(str(candidate_configuration["candidate_id"]))

    expected_trained_pair_set = {
        (ablation_id, seed)
        for ablation_id in EXPECTED_ABLATION_ID_LIST
        for seed in EXPECTED_SEED_LIST
    }
    assert observed_trained_pair_set == expected_trained_pair_set
    assert surface_count == {"Fw": 3, "Bw": 2, "global": 24}
    assert source_count == {
        "wave52r_integrated_specialist_trained": 21,
        "wave52r_offline_leader_cross_surface_promotion": 2,
        "accepted_non_pinn_incumbent": 6,
    }
    assert len(gate_passed_candidate_id_list) == 3
    assert all("_a02_" in candidate_id for candidate_id in gate_passed_candidate_id_list)

    summary = {
        "schema_version": 1,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "passed",
        "config_path": config_path.relative_to(PROJECT_ROOT).as_posix(),
        "candidate_count": len(candidate_configurations),
        "trained_candidate_count": 21,
        "ingredient_control_count": 2,
        "incumbent_count": 6,
        "surface_candidate_count": surface_count,
        "candidate_source_count": source_count,
        "candidate_kind_count": candidate_kind_count,
        "campaign_gate_passed_candidate_id_list": sorted(gate_passed_candidate_id_list),
        "excluded_condition_id_list": EXPECTED_EXCLUDED_CONDITION_ID_LIST,
        "curve_count_by_split": EXPECTED_CURVE_COUNT_BY_SPLIT,
        "heavy_matrix_executed": False,
        "promotion_authorized": False,
    }
    write_yaml(OUTPUT_PATH, summary)
    print("[PASS] Integrated-specialist Track 2 preflight | surfaces=3 | candidates=29 | heavy_matrix=false")
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
