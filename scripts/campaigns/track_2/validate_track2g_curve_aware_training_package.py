"""Validate the prepared Wave 3.3 curve-aware training package."""

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
CAMPAIGN_NAME = "track2g_curve_aware_training_campaign_2026_06_08"
EXPECTED_SURFACE_LIST = ["global", "fw", "bw"]
EXPECTED_LOSS_PROFILE_LIST = [
    "pointwise_control",
    "raw_centered_shape",
    "raw_offset",
    "full_curve_composite",
]
EXPECTED_HARMONIC_INDEX_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read a YAML file as a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def load_queue_config_list(queue_root: Path) -> list[dict[str, Any]]:

    """Load all queue YAML files."""

    queue_path_list = sorted(queue_root.glob("*.yaml"))
    assert queue_path_list, f"No queue YAML files found | {queue_root}"

    queue_config_list: list[dict[str, Any]] = []
    for queue_path in queue_path_list:
        queue_config = read_yaml_file(queue_path)
        queue_config["queue_path"] = queue_path.as_posix()
        queue_config_list.append(queue_config)
    return queue_config_list


def validate_queue_matrix(queue_config_list: list[dict[str, Any]]) -> None:

    """Validate the 4 by 3 Wave 3.3 queue matrix."""

    assert len(queue_config_list) == 12, f"Expected 12 queue configs | found={len(queue_config_list)}"

    observed_pair_set: set[tuple[str, str]] = set()
    for queue_config in queue_config_list:
        metadata = queue_config.get("metadata", {})
        experiment = queue_config.get("experiment", {})
        dataset = queue_config.get("dataset", {})
        model = queue_config.get("model", {})
        training = queue_config.get("training", {})
        loss = training.get("loss", {})

        assert isinstance(metadata, dict), "Queue metadata must be a dictionary"
        assert isinstance(experiment, dict), "Queue experiment must be a dictionary"
        assert isinstance(dataset, dict), "Queue dataset must be a dictionary"
        assert isinstance(model, dict), "Queue model must be a dictionary"
        assert isinstance(loss, dict), "Queue training loss must be a dictionary"
        assert metadata.get("campaign_name") == CAMPAIGN_NAME
        assert experiment.get("model_type") == "curve_aware_harmonic_residual_offset_probe"

        loss_profile = str(metadata.get("loss_profile", ""))
        training_variant = str(metadata.get("training_variant", "")).lower()
        surface_key = "fw" if training_variant == "fw" else "bw" if training_variant == "bw" else "global"
        observed_pair_set.add((loss_profile, surface_key))

        assert loss.get("profile") == loss_profile, "Loss profile mismatch between metadata and training block"
        assert loss.get("harmonic_index_list") == EXPECTED_HARMONIC_INDEX_LIST, "Unexpected loss harmonic list"
        assert model.get("harmonic_index_list") == EXPECTED_HARMONIC_INDEX_LIST, "Unexpected model harmonic list"
        assert dataset.get("collate_mode") == "sequence", "Wave 3.3 entries must use sequence batches"
        assert dataset.get("shuffle_training_batch_elements") is False, "Curve-aware loss requires ordered per-curve training batches"
        assert int(dataset.get("sequence_length", 0)) == 33, "Unexpected sequence length"
        assert bool(model.get("offset_bidirectional", False)) is False, "Offset branch must remain unidirectional"

    expected_pair_set = {
        (loss_profile, surface_name)
        for loss_profile in EXPECTED_LOSS_PROFILE_LIST
        for surface_name in EXPECTED_SURFACE_LIST
    }
    missing_pair_set = expected_pair_set.difference(observed_pair_set)
    unexpected_pair_set = observed_pair_set.difference(expected_pair_set)
    assert not missing_pair_set, f"Missing Wave 3.3 queue pairs | {sorted(missing_pair_set)}"
    assert not unexpected_pair_set, f"Unexpected Wave 3.3 queue pairs | {sorted(unexpected_pair_set)}"


def validate_active_campaign_state() -> None:

    """Validate persistent active campaign state."""

    active_state = read_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH)
    assert active_state.get("status") == "prepared", "Wave 3.3 campaign state is not prepared."
    assert active_state.get("campaign_name") == CAMPAIGN_NAME, "Active state does not point at Wave 3.3."
    queue_config_path_list = active_state.get("queue_config_path_list", [])
    assert isinstance(queue_config_path_list, list), "queue_config_path_list must be a list"
    assert len(queue_config_path_list) == 12, "Active state must record 12 queue configs"
    launch_command_list = active_state.get("launch_command_list", [])
    assert any("-Remote" in str(command) for command in launch_command_list), "Remote command missing from active state"


def parse_arguments() -> argparse.Namespace:

    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--queue-root",
        required=True,
        type=Path,
        help="Repository-relative directory containing Wave 3.3 queue configs.",
    )
    parser.add_argument(
        "--require-prepared-state",
        action="store_true",
        help="Require doc/running/active_training_campaign.yaml to point at Wave 3.3.",
    )
    return parser.parse_args()


def main() -> int:

    """Validate the prepared package."""

    argument_namespace = parse_arguments()
    queue_root = PROJECT_PATH / argument_namespace.queue_root
    queue_config_list = load_queue_config_list(queue_root)
    validate_queue_matrix(queue_config_list)
    if argument_namespace.require_prepared_state:
        validate_active_campaign_state()

    print(
        "Wave 3.3 package validated | "
        f"queue_entries={len(queue_config_list)} | "
        f"loss_profiles={len(EXPECTED_LOSS_PROFILE_LIST)} | surfaces={len(EXPECTED_SURFACE_LIST)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
