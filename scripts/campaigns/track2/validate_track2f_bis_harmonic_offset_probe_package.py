"""Validate the prepared Track 2F-bis harmonic-offset probe package."""

from __future__ import annotations

# Import Python Utilities
import argparse
import sys
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Paths
PROJECT_PATH = Path(__file__).resolve().parents[3]
ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
CAMPAIGN_NAME = "track2f_bis_harmonic_offset_probe_campaign_2026_06_04"
EXPECTED_SURFACE_LIST = ["global", "fw", "bw"]
EXPECTED_INTERVENTION_LIST = [
    "clean_sequential_residual_offset_control",
    "harmonic_residual_offset_probe",
]
EXPECTED_MODEL_TYPE_BY_INTERVENTION = {
    "clean_sequential_residual_offset_control": "sequential_residual_offset_probe",
    "harmonic_residual_offset_probe": "harmonic_residual_offset_probe",
}


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read a YAML file as a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def load_queue_config_list(queue_root: Path) -> list[dict[str, Any]]:

    """Load all queue YAML files from the prepared package."""

    queue_path_list = sorted(queue_root.glob("*.yaml"))
    assert queue_path_list, f"No queue YAML files found | {queue_root}"

    queue_config_list: list[dict[str, Any]] = []
    for queue_path in queue_path_list:
        queue_config = read_yaml_file(queue_path)
        queue_config["queue_path"] = queue_path.as_posix()
        queue_config_list.append(queue_config)
    return queue_config_list


def validate_queue_matrix(queue_config_list: list[dict[str, Any]]) -> None:

    """Validate the Track 2F-bis queue matrix."""

    assert len(queue_config_list) == 6, f"Expected 6 queue configs | found={len(queue_config_list)}"

    observed_pair_set: set[tuple[str, str]] = set()
    for queue_config in queue_config_list:
        metadata = queue_config.get("metadata", {})
        experiment = queue_config.get("experiment", {})
        model = queue_config.get("model", {})
        dataset = queue_config.get("dataset", {})

        assert isinstance(metadata, dict), "Queue metadata must be a dictionary"
        assert isinstance(experiment, dict), "Queue experiment must be a dictionary"
        assert isinstance(model, dict), "Queue model must be a dictionary"
        assert isinstance(dataset, dict), "Queue dataset must be a dictionary"
        assert metadata.get("campaign_name") == CAMPAIGN_NAME

        intervention_name = str(metadata.get("intervention", ""))
        direction_variant = str(metadata.get("training_variant", "")).lower()
        surface_key = "fw" if direction_variant == "fw" else "bw" if direction_variant == "bw" else "global"
        observed_pair_set.add((surface_key, intervention_name))

        expected_model_type = EXPECTED_MODEL_TYPE_BY_INTERVENTION.get(intervention_name)
        assert expected_model_type is not None, f"Unexpected intervention | {intervention_name}"
        assert experiment.get("model_type") == expected_model_type, (
            f"Model type mismatch | intervention={intervention_name} | "
            f"observed={experiment.get('model_type')} | expected={expected_model_type}"
        )
        assert dataset.get("collate_mode") == "sequence", "Track 2F-bis entries must use sequence batches"
        assert int(dataset.get("sequence_length", 0)) == 33, "Unexpected sequence length"
        assert bool(model.get("offset_bidirectional", False)) is False, "Offset branch must remain unidirectional"

        if intervention_name == "harmonic_residual_offset_probe":
            assert model.get("harmonic_index_list") == [0, 1, 3, 39, 40, 78, 81, 156, 162, 240], (
                "Harmonic-offset probe must use the sparse RCIM harmonic list"
            )

    expected_pair_set = {
        (surface_name, intervention_name)
        for intervention_name in EXPECTED_INTERVENTION_LIST
        for surface_name in EXPECTED_SURFACE_LIST
    }
    missing_pair_set = expected_pair_set.difference(observed_pair_set)
    unexpected_pair_set = observed_pair_set.difference(expected_pair_set)
    assert not missing_pair_set, f"Missing Track 2F-bis queue pairs | {sorted(missing_pair_set)}"
    assert not unexpected_pair_set, f"Unexpected Track 2F-bis queue pairs | {sorted(unexpected_pair_set)}"


def validate_active_campaign_state() -> None:

    """Validate that the persistent active-campaign state points at Track 2F-bis."""

    active_state_path = PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH
    active_state = read_yaml_file(active_state_path)
    assert active_state.get("status") == "prepared", "Track 2F-bis campaign state is not prepared."
    assert active_state.get("campaign_name") == CAMPAIGN_NAME, (
        "Active campaign state does not point at Track 2F-bis."
    )
    queue_config_path_list = active_state.get("queue_config_path_list", [])
    assert isinstance(queue_config_path_list, list), "queue_config_path_list must be a list"
    assert len(queue_config_path_list) == 6, "Active state must record six queue configs"


def parse_arguments() -> argparse.Namespace:

    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--queue-root",
        required=True,
        type=Path,
        help="Repository-relative directory containing Track 2F-bis queue configs.",
    )
    parser.add_argument(
        "--require-prepared-state",
        action="store_true",
        help="Require doc/running/active_training_campaign.yaml to point at Track 2F-bis.",
    )
    return parser.parse_args()


def main() -> int:

    """Validate the Track 2F-bis package."""

    argument_namespace = parse_arguments()
    queue_root = PROJECT_PATH / argument_namespace.queue_root
    queue_config_list = load_queue_config_list(queue_root)
    validate_queue_matrix(queue_config_list)
    if argument_namespace.require_prepared_state:
        validate_active_campaign_state()

    print(
        "Track 2F-bis package validated | "
        f"queue_entries={len(queue_config_list)} | "
        f"interventions={len(EXPECTED_INTERVENTION_LIST)} | surfaces={len(EXPECTED_SURFACE_LIST)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
