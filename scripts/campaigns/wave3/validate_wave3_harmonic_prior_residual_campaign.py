"""Validate the prepared Wave 3 harmonic-prior residual campaign package."""

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
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.models.model_factory import create_model
from scripts.training import shared_training_infrastructure

ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
CAMPAIGN_NAME = "wave3_harmonic_prior_residual_campaign_2026_06_14"
EXPECTED_SURFACE_LIST = ["global", "fw", "bw"]
EXPECTED_LOSS_PROFILE_DICTIONARY = {
    "pointwise_control": "mse",
    "smooth_l1_structured": "smooth_l1",
}
EXPECTED_HARMONIC_INDEX_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
EXPECTED_AUXILIARY_OUTPUT_KEY_LIST = [
    "structured_prediction_tensor",
    "residual_prediction_tensor",
    "wave3_residual_prediction_tensor",
    "prediction_tensor",
]


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read one YAML file as a dictionary."""

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


def resolve_surface_key(training_variant: str) -> str:

    """Resolve canonical surface key from config metadata."""

    normalized_training_variant = training_variant.strip().lower()
    if normalized_training_variant == "fw":
        return "fw"
    if normalized_training_variant == "bw":
        return "bw"
    return "global"


def validate_queue_matrix(queue_config_list: list[dict[str, Any]]) -> None:

    """Validate the 2 by 3 Wave 3 queue matrix."""

    assert len(queue_config_list) == 6, f"Expected 6 queue configs | found={len(queue_config_list)}"

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
        assert metadata.get("probe_group") == "wave3_harmonic_prior_residual"
        assert experiment.get("model_type") == "wave3_harmonic_prior_residual"
        assert model.get("output_size") == 1, "Wave 3 package must produce one deterministic TE target"

        loss_profile = str(metadata.get("loss_profile", ""))
        assert loss_profile in EXPECTED_LOSS_PROFILE_DICTIONARY, f"Unexpected Wave 3 profile | {loss_profile}"
        assert loss.get("profile") == loss_profile, "Loss profile mismatch between metadata and training block"
        assert loss.get("pointwise_loss") == EXPECTED_LOSS_PROFILE_DICTIONARY[loss_profile], "Pointwise loss mismatch"
        if loss_profile == "smooth_l1_structured":
            assert float(loss.get("huber_delta", 0.0)) > 0.0, "Smooth L1 profile requires positive huber_delta"

        training_variant = str(metadata.get("training_variant", ""))
        surface_key = resolve_surface_key(training_variant)
        observed_pair_set.add((loss_profile, surface_key))

        assert metadata.get("harmonic_index_list") == EXPECTED_HARMONIC_INDEX_LIST, "Unexpected metadata harmonic list"
        assert loss.get("harmonic_index_list") == EXPECTED_HARMONIC_INDEX_LIST, "Unexpected loss harmonic list"
        assert model.get("harmonic_index_list") == EXPECTED_HARMONIC_INDEX_LIST, "Unexpected model harmonic list"
        assert dataset.get("collate_mode") == "sequence", "Wave 3 entries must use sequence batches"
        assert dataset.get("shuffle_training_batch_elements") is False, "Wave 3 package keeps ordered per-curve batches"
        assert int(dataset.get("sequence_length", 0)) == 33, "Unexpected sequence length"
        assert str(model.get("readout_position", "")) == "center", "Wave 3 sequence readout must use the center point"
        assert bool(model.get("freeze_structured_branch", True)) is False, "First Wave 3 campaign trains the structured branch"
        assert "not_campaign_ready" not in str(metadata).lower(), "Queue config still carries not_campaign_ready metadata"

    expected_pair_set = {
        (profile_name, surface_name)
        for profile_name in EXPECTED_LOSS_PROFILE_DICTIONARY
        for surface_name in EXPECTED_SURFACE_LIST
    }
    missing_pair_set = expected_pair_set.difference(observed_pair_set)
    unexpected_pair_set = observed_pair_set.difference(expected_pair_set)
    assert not missing_pair_set, f"Missing Wave 3 queue pairs | {sorted(missing_pair_set)}"
    assert not unexpected_pair_set, f"Unexpected Wave 3 queue pairs | {sorted(unexpected_pair_set)}"


def validate_model_instantiation(queue_config_list: list[dict[str, Any]]) -> None:

    """Validate that every queue config can instantiate its configured model."""

    for queue_config in queue_config_list:
        experiment = queue_config["experiment"]
        model = queue_config["model"]
        created_model = create_model(str(experiment["model_type"]), model)
        assert getattr(created_model, "output_size", None) == int(model["output_size"]), (
            f"Created model output size mismatch | {queue_config['queue_path']}"
        )
        for auxiliary_buffer_name in [
            "harmonic_index_tensor",
            "low_order_harmonic_index_tensor",
            "stable_middle_harmonic_index_tensor",
            "high_order_harmonic_index_tensor",
        ]:
            assert hasattr(created_model, auxiliary_buffer_name), (
                f"Missing Wave 3 diagnostic buffer | {auxiliary_buffer_name} | {queue_config['queue_path']}"
            )


def validate_one_batch_outputs(queue_config_list: list[dict[str, Any]]) -> None:

    """Run lightweight one-batch output and loss checks for every candidate."""

    for queue_config in queue_config_list:
        validation_queue_config = dict(queue_config)
        validation_queue_config["dataset"] = dict(queue_config["dataset"])
        validation_queue_config["dataset"]["maximum_sequences_per_curve"] = 8
        validation_queue_config["dataset"]["num_workers"] = 0
        validation_queue_config["dataset"]["pin_memory"] = False
        validation_queue_config["training"] = dict(queue_config["training"])
        validation_queue_config["training"]["deterministic"] = True
        validation_queue_config["runtime"] = dict(queue_config.get("runtime", {}))
        validation_queue_config["runtime"]["accelerator"] = "cpu"
        validation_queue_config["runtime"]["devices"] = 1
        validation_queue_config["runtime"]["benchmark"] = False
        prepared_config = shared_training_infrastructure.prepare_output_artifact_training_config(
            validation_queue_config,
            artifact_kind=shared_training_infrastructure.VALIDATION_OUTPUT_ARTIFACT_KIND,
            run_name_suffix="wave3_harmonic_prior_residual_validation",
        )
        datamodule, _regression_backbone, regression_module, _normalization_statistics = (
            shared_training_infrastructure.initialize_training_components(prepared_config)
        )
        batch_dictionary = shared_training_infrastructure.fetch_first_batch(datamodule, split_name="train")
        batch_output_dictionary = regression_module.compute_batch_outputs(batch_dictionary)
        deterministic_prediction_tensor = batch_output_dictionary["normalized_prediction_tensor"]
        raw_output_tensor = batch_output_dictionary["normalized_model_output_tensor"]
        target_tensor = batch_output_dictionary["normalized_target_tensor"]
        assert deterministic_prediction_tensor.shape == target_tensor.shape, (
            f"Deterministic prediction shape mismatch | {queue_config['queue_path']}"
        )
        assert raw_output_tensor.shape[-1] == 1, f"Raw output size mismatch | {queue_config['queue_path']}"
        for auxiliary_key in EXPECTED_AUXILIARY_OUTPUT_KEY_LIST:
            assert auxiliary_key in batch_output_dictionary, (
                f"Missing Wave 3 auxiliary output | {auxiliary_key} | {queue_config['queue_path']}"
            )
            assert batch_output_dictionary[auxiliary_key].shape == target_tensor.shape, (
                f"Wave 3 auxiliary output shape mismatch | {auxiliary_key} | {queue_config['queue_path']}"
            )
        assert bool(batch_output_dictionary["loss"].isfinite().detach().cpu().item()), (
            f"Non-finite loss | {queue_config['queue_path']}"
        )


def validate_active_campaign_state() -> None:

    """Validate persistent active campaign state."""

    active_state = read_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH)
    assert active_state.get("status") == "prepared", "Wave 3 campaign state is not prepared."
    assert active_state.get("campaign_name") == CAMPAIGN_NAME, "Active state does not point at Wave 3."
    queue_config_path_list = active_state.get("queue_config_path_list", [])
    assert isinstance(queue_config_path_list, list), "queue_config_path_list must be a list"
    assert len(queue_config_path_list) == 6, "Active state must record 6 queue configs"
    launch_command_list = active_state.get("launch_command_list", [])
    assert any("-Remote" in str(command) for command in launch_command_list), "Remote command missing from active state"


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue-root", required=True, type=Path, help="Repository-relative directory containing queue configs.")
    parser.add_argument("--require-prepared-state", action="store_true", help="Require active campaign state to point at this package.")
    parser.add_argument("--run-one-batch", action="store_true", help="Run one-batch output/loss checks for every candidate.")
    return parser.parse_args()


def main() -> int:

    """Validate the prepared package."""

    argument_namespace = parse_arguments()
    queue_root = PROJECT_PATH / argument_namespace.queue_root
    queue_config_list = load_queue_config_list(queue_root)
    validate_queue_matrix(queue_config_list)
    validate_model_instantiation(queue_config_list)
    if argument_namespace.run_one_batch:
        validate_one_batch_outputs(queue_config_list)
    if argument_namespace.require_prepared_state:
        validate_active_campaign_state()

    print(
        "Wave 3 harmonic-prior residual package validated | "
        f"queue_entries={len(queue_config_list)} | "
        f"profiles={len(EXPECTED_LOSS_PROFILE_DICTIONARY)} | surfaces={len(EXPECTED_SURFACE_LIST)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
