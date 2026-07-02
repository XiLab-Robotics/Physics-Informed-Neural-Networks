"""Validate the prepared Wave 5.2B offset and harmonic guided package."""

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
CAMPAIGN_NAME = "wave52b_offset_harmonic_guided_campaign_2026_07_01"
EXPECTED_MODEL_TYPE = "wave52b_offset_harmonic_guided"
EXPECTED_DATASET_NAME = "polished_dataset"
EXPECTED_DATASET_SCHEMA = "polished_point_v1"
EXPECTED_SURFACE_LIST = ["global", "fw", "bw"]
EXPECTED_ABLATION_PROFILE_LIST = [
    "pointwise_control",
    "offset_head",
    "offset_centered_shape",
    "offset_centered_shape_harmonic",
]
EXPECTED_AUXILIARY_OUTPUT_KEY_LIST = [
    "base_prediction_tensor",
    "residual_offset_prediction_tensor",
    "structured_prediction_tensor",
    "wave52b_harmonic_prediction_tensor",
    "prediction_tensor",
]


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read one YAML file as a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def load_campaign_manifest(campaign_manifest_path: Path) -> dict[str, Any]:

    """Load the campaign manifest."""

    resolved_manifest_path = PROJECT_PATH / campaign_manifest_path
    assert resolved_manifest_path.exists(), f"Missing campaign manifest | {campaign_manifest_path}"
    return read_yaml_file(resolved_manifest_path)


def load_queue_config_list(campaign_manifest: dict[str, Any]) -> list[dict[str, Any]]:

    """Load all queue configs from the manifest."""

    queue_config_path_list = campaign_manifest.get("queue_config_path_list", [])
    assert isinstance(queue_config_path_list, list), "Manifest queue_config_path_list must be a list"
    assert len(queue_config_path_list) == 12, f"Expected 12 queue configs | found={len(queue_config_path_list)}"

    queue_config_list: list[dict[str, Any]] = []
    for queue_config_path_value in queue_config_path_list:
        queue_config_path = Path(str(queue_config_path_value))
        resolved_queue_config_path = PROJECT_PATH / queue_config_path
        assert resolved_queue_config_path.exists(), f"Missing queue config | {queue_config_path}"
        queue_config = read_yaml_file(resolved_queue_config_path)
        queue_config["queue_path"] = queue_config_path.as_posix()
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


def validate_manifest(campaign_manifest: dict[str, Any]) -> None:

    """Validate campaign-level manifest fields."""

    assert campaign_manifest.get("campaign_name") == CAMPAIGN_NAME, "Unexpected campaign name"
    assert campaign_manifest.get("dataset_name") == EXPECTED_DATASET_NAME, "Unexpected dataset name"
    assert campaign_manifest.get("dataset_schema") == EXPECTED_DATASET_SCHEMA, "Unexpected dataset schema"
    assert campaign_manifest.get("expected_run_count") == 12, "Manifest expected run count must be 12"
    assert campaign_manifest.get("expected_ablation_profile_list") == EXPECTED_ABLATION_PROFILE_LIST, (
        "Unexpected ablation profile list"
    )
    assert campaign_manifest.get("expected_surface_list") == EXPECTED_SURFACE_LIST, "Unexpected surface list"

    for required_path_key in [
        "planning_report_path",
        "technical_document_path",
        "model_report_path",
        "launcher_path",
        "launcher_note_path",
        "validator_path",
    ]:
        required_path = PROJECT_PATH / str(campaign_manifest.get(required_path_key, ""))
        assert required_path.exists(), f"Manifest path does not exist | {required_path_key}={required_path}"

    execution_policy = campaign_manifest.get("execution_policy", {})
    assert isinstance(execution_policy, dict), "execution_policy must be a dictionary"
    assert execution_policy.get("operator_run_required") is True, "Operator launch gate must remain explicit"
    assert execution_policy.get("run_te_curve_verification_pipeline") is False, "CVP must not run during campaign launch"
    assert execution_policy.get("preserve_external_full_wave_polished_campaign") is True, (
        "Manifest must preserve the external full-wave polished campaign boundary"
    )


def validate_dataset_variants(campaign_manifest: dict[str, Any]) -> None:

    """Validate dataset variants point at polished data."""

    dataset_variant_path_list = campaign_manifest.get("dataset_variant_path_list", [])
    assert isinstance(dataset_variant_path_list, list), "dataset_variant_path_list must be a list"
    assert len(dataset_variant_path_list) == 3, "Expected three dataset variants"

    for dataset_variant_path_value in dataset_variant_path_list:
        dataset_variant_path = PROJECT_PATH / str(dataset_variant_path_value)
        dataset_variant = read_yaml_file(dataset_variant_path)
        assert dataset_variant.get("paths", {}).get("dataset_root") == "data/polished_dataset", (
            f"Dataset variant does not target polished_dataset | {dataset_variant_path}"
        )
        dataset_dictionary = dataset_variant.get("dataset", {})
        assert dataset_dictionary.get("name") == EXPECTED_DATASET_NAME, "Dataset variant name mismatch"
        assert dataset_dictionary.get("schema") == EXPECTED_DATASET_SCHEMA, "Dataset variant schema mismatch"


def validate_queue_matrix(queue_config_list: list[dict[str, Any]]) -> None:

    """Validate the 4 by 3 Wave 5.2B queue matrix."""

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
        assert metadata.get("probe_group") == "wave52b_offset_harmonic_guided"
        assert metadata.get("dataset_id") == EXPECTED_DATASET_NAME
        assert metadata.get("dataset_schema") == EXPECTED_DATASET_SCHEMA
        assert experiment.get("model_type") == EXPECTED_MODEL_TYPE
        assert model.get("output_size") == 1, "Wave 5.2B package must produce one deterministic TE target"
        assert dataset.get("name") == EXPECTED_DATASET_NAME, "Queue dataset name mismatch"
        assert dataset.get("collate_mode") == "sequence", "Wave 5.2B entries must use sequence batches"
        assert dataset.get("shuffle_training_batch_elements") is False, "Wave 5.2B keeps ordered per-curve batches"
        assert int(dataset.get("sequence_length", 0)) == 33, "Unexpected sequence length"
        assert str(model.get("readout_position", "")) == "center", "Wave 5.2B sequence readout must use the center point"
        assert loss.get("pointwise_loss") == "mse", "Wave 5.2B package uses deterministic MSE point loss"

        ablation_profile = str(metadata.get("ablation_profile", ""))
        assert ablation_profile in EXPECTED_ABLATION_PROFILE_LIST, f"Unexpected ablation profile | {ablation_profile}"
        assert loss.get("profile") == ablation_profile, "Loss profile mismatch between metadata and training block"
        surface_key = resolve_surface_key(str(metadata.get("training_variant", "")))
        observed_pair_set.add((ablation_profile, surface_key))

        if ablation_profile == "pointwise_control":
            assert float(model.get("offset_scale", -1.0)) == 0.0, "Pointwise control must disable offset branch contribution"
            assert float(model.get("harmonic_scale", -1.0)) == 0.0, "Pointwise control must disable harmonic branch contribution"
        if ablation_profile == "offset_centered_shape_harmonic":
            assert float(model.get("harmonic_scale", 0.0)) > 0.0, "Harmonic ablation must enable harmonic branch contribution"
            assert float(loss.get("weights", {}).get("harmonic", 0.0)) > 0.0, "Harmonic ablation must enable harmonic loss"

        assert "simplified_dataset" not in str(queue_config), (
            f"Wave 5.2B queue config must not target simplified_dataset | {queue_config['queue_path']}"
        )

    expected_pair_set = {
        (profile_name, surface_name)
        for profile_name in EXPECTED_ABLATION_PROFILE_LIST
        for surface_name in EXPECTED_SURFACE_LIST
    }
    missing_pair_set = expected_pair_set.difference(observed_pair_set)
    unexpected_pair_set = observed_pair_set.difference(expected_pair_set)
    assert not missing_pair_set, f"Missing Wave 5.2B queue pairs | {sorted(missing_pair_set)}"
    assert not unexpected_pair_set, f"Unexpected Wave 5.2B queue pairs | {sorted(unexpected_pair_set)}"


def validate_model_instantiation(queue_config_list: list[dict[str, Any]]) -> None:

    """Validate that every queue config can instantiate its configured model."""

    for queue_config in queue_config_list:
        experiment = queue_config["experiment"]
        model = dict(queue_config["model"])
        if model.get("input_size") == "auto":
            model["input_size"] = 5
        created_model = create_model(str(experiment["model_type"]), model)
        assert getattr(created_model, "output_size", None) == int(model["output_size"]), (
            f"Created model output size mismatch | {queue_config['queue_path']}"
        )
        assert hasattr(created_model, "harmonic_index_tensor"), (
            f"Missing Wave 5.2B harmonic diagnostic buffer | {queue_config['queue_path']}"
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
            run_name_suffix="wave52b_offset_harmonic_guided_validation",
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
                f"Missing Wave 5.2B auxiliary output | {auxiliary_key} | {queue_config['queue_path']}"
            )
            assert batch_output_dictionary[auxiliary_key].shape == target_tensor.shape, (
                f"Wave 5.2B auxiliary output shape mismatch | {auxiliary_key} | {queue_config['queue_path']}"
            )
        assert bool(batch_output_dictionary["loss"].isfinite().detach().cpu().item()), (
            f"Non-finite loss | {queue_config['queue_path']}"
        )


def validate_active_campaign_state(campaign_manifest: dict[str, Any]) -> None:

    """Validate persistent active campaign state."""

    active_state = read_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH)
    assert active_state.get("status") == "prepared", "Wave 5.2B campaign state is not prepared."
    assert active_state.get("campaign_name") == CAMPAIGN_NAME, "Active state does not point at Wave 5.2B."
    queue_config_path_list = active_state.get("queue_config_path_list", [])
    assert isinstance(queue_config_path_list, list), "queue_config_path_list must be a list"
    assert len(queue_config_path_list) == 12, "Active state must record 12 queue configs"
    assert queue_config_path_list == campaign_manifest.get("queue_config_path_list"), (
        "Active state queue list does not match campaign manifest"
    )
    launch_command_list = active_state.get("launch_command_list", [])
    assert any("-Remote" in str(command) for command in launch_command_list), "Remote command missing from active state"
    next_prepared_campaign = active_state.get("next_prepared_campaign", {})
    assert isinstance(next_prepared_campaign, dict), "External full-wave campaign record must remain present"
    assert next_prepared_campaign.get("campaign_name") == "polished_dataset_full_wave_retraining_2026_06_22", (
        "External full-wave polished campaign pointer was not preserved"
    )


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign-manifest-path", required=True, type=Path, help="Repository-relative campaign manifest path.")
    parser.add_argument("--require-prepared-state", action="store_true", help="Require active campaign state to point at this package.")
    parser.add_argument("--run-one-batch", action="store_true", help="Run one-batch output/loss checks for every candidate.")
    return parser.parse_args()


def main() -> int:

    """Validate the prepared package."""

    argument_namespace = parse_arguments()
    campaign_manifest = load_campaign_manifest(argument_namespace.campaign_manifest_path)
    queue_config_list = load_queue_config_list(campaign_manifest)
    validate_manifest(campaign_manifest)
    validate_dataset_variants(campaign_manifest)
    validate_queue_matrix(queue_config_list)
    validate_model_instantiation(queue_config_list)
    if argument_namespace.run_one_batch:
        validate_one_batch_outputs(queue_config_list)
    if argument_namespace.require_prepared_state:
        validate_active_campaign_state(campaign_manifest)

    print(
        "Wave 5.2B offset and harmonic guided package validated | "
        f"queue_entries={len(queue_config_list)} | "
        f"profiles={len(EXPECTED_ABLATION_PROFILE_LIST)} | surfaces={len(EXPECTED_SURFACE_LIST)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
