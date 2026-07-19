"""Prepare dataset/input-mode retraining campaign packages."""

from __future__ import annotations

# Import Python Utilities
import argparse
import os
import re
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(os.path.abspath(__file__)).parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

from scripts.datasets import transmission_error_dataset

TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-07/2026-07-07/"
    "2026-07-07-01-46-06_dataset_input_mode_retraining_campaigns.md"
)
PLANNING_REPORT_PATH = (
    "doc/reports/campaign_plans/cross_wave/input_modes/"
    "2026-07-07-01-46-06_dataset_input_mode_retraining_campaign_plan_report.md"
)
CAMPAIGN_ROOT = "config/training/dataset_input_mode_retraining/campaigns"
QUEUE_ROOT = "config/training/queue/dataset_input_mode_retraining"
SOURCE_QUEUE_ROOT = "config/training/queue/polished_dataset_full_wave_retraining/completed"
INPUT_MODE_VERSION_DICTIONARY = {
    "simplified_setpoints": {
        "dataset_name": transmission_error_dataset.SIMPLIFIED_DATASET,
        "input_mode": transmission_error_dataset.SETPOINT_INPUT_MODE,
        "dataset_schema": "simplified_curve_v1",
        "source_dataset_root": "data/simplified_dataset",
        "model_archive_root": "models/simplified_dataset/setpoints",
    },
    "polished_setpoints": {
        "dataset_name": transmission_error_dataset.POLISHED_DATASET,
        "input_mode": transmission_error_dataset.SETPOINT_INPUT_MODE,
        "dataset_schema": "polished_setpoint_curve_v1",
        "source_dataset_root": "data/polished_dataset",
        "model_archive_root": "models/polished_dataset/setpoints",
    },
    "polished_actual_values": {
        "dataset_name": transmission_error_dataset.POLISHED_DATASET,
        "input_mode": transmission_error_dataset.ACTUAL_VALUES_INPUT_MODE,
        "dataset_schema": "polished_point_v1",
        "source_dataset_root": "data/polished_dataset",
        "model_archive_root": "models/polished_dataset/actual_values",
    },
}
SURFACE_NAME_LIST = ["global", "fw", "bw"]
SURFACE_CONFIGURATION = {
    "global": {
        "training_variant": "global",
        "direction_scope_label": "bidirectional",
        "use_forward_direction": True,
        "use_backward_direction": True,
    },
    "fw": {
        "training_variant": "fw",
        "direction_scope_label": "forward_only",
        "use_forward_direction": True,
        "use_backward_direction": False,
    },
    "bw": {
        "training_variant": "bw",
        "direction_scope_label": "backward_only",
        "use_forward_direction": False,
        "use_backward_direction": True,
    },
}
SOURCE_QUEUE_STEM_PATTERN = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}_[0-9]{3}_[0-9]{3}_(?P<run_stem>.+)$"
)


def read_yaml_dictionary(path_value: str | Path) -> dict[str, Any]:

    """Read one YAML dictionary."""

    input_path = PROJECT_PATH / Path(path_value)
    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def write_yaml_dictionary(path_value: str | Path, payload: dict[str, Any]) -> None:

    """Write one YAML dictionary."""

    output_path = PROJECT_PATH / Path(path_value)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False)


def apply_dataset_and_input_mode_override(
    source_config: dict[str, Any],
    dataset_name: str,
    input_mode: str,
) -> dict[str, Any]:

    """Apply dataset and input-mode selectors without importing training modules."""

    config = deepcopy(source_config)
    dataset = config.setdefault("dataset", {})
    dataset["name"] = transmission_error_dataset.normalize_dataset_name(dataset_name)
    dataset["input_mode"] = transmission_error_dataset.normalize_input_mode(dataset_name, input_mode)
    config.setdefault("model", {})["input_size"] = "auto"
    return config


def build_campaign_name(family_name: str, version_name: str) -> str:

    """Build the stable family-version campaign name."""

    return f"dataset_input_mode_retraining__{family_name}__{version_name}"


def build_model_development_config(
    family_name: str,
    version_name: str,
    surface_name: str,
    source_config_path: str,
    queue_index: int,
) -> dict[str, Any]:

    """Build one model-development retraining config."""

    version_dictionary = INPUT_MODE_VERSION_DICTIONARY[version_name]
    source_config = read_yaml_dictionary(source_config_path)
    config = apply_dataset_and_input_mode_override(
        source_config,
        version_dictionary["dataset_name"],
        version_dictionary["input_mode"],
    )
    campaign_name = build_campaign_name(family_name, version_name)
    canonical_id = f"{family_name}_{surface_name}"
    surface_configuration = SURFACE_CONFIGURATION[surface_name]

    config.setdefault("paths", {})["dataset_config_path"] = "config/datasets/transmission_error_dataset.yaml"
    config["paths"]["output_root"] = f"output/training_runs/{family_name}"
    config.setdefault("experiment", {})["run_name"] = f"te_{canonical_id}__{version_name}"
    config["experiment"]["model_family"] = canonical_id
    config.setdefault("model", {})["input_size"] = "auto"

    metadata = config.setdefault("metadata", {})
    metadata["campaign_name"] = campaign_name
    metadata["planning_report_path"] = PLANNING_REPORT_PATH
    metadata["technical_document_path"] = TECHNICAL_DOCUMENT_PATH
    metadata["phase_name"] = "dataset_input_mode_retraining"
    metadata["campaign_config_id"] = canonical_id
    metadata["base_model_family"] = family_name
    metadata["source_config_path"] = source_config_path.replace("\\", "/")
    metadata["dataset_name"] = version_dictionary["dataset_name"]
    metadata["input_mode"] = version_dictionary["input_mode"]
    metadata["dataset_schema"] = version_dictionary["dataset_schema"]
    metadata["source_dataset_root"] = version_dictionary["source_dataset_root"]
    metadata["expected_model_archive_root"] = version_dictionary["model_archive_root"]
    metadata["queue_index"] = queue_index
    metadata.pop("run_instance_id", None)
    metadata.update(surface_configuration)
    metadata["output_run_name"] = f"te_{canonical_id}__{version_name}"
    return config


def collect_family_source_entries(family_name: str) -> list[tuple[str, str, str]]:

    """Collect the source entries for one model-development family."""

    family_entry_list = []
    source_queue_root = PROJECT_PATH / SOURCE_QUEUE_ROOT
    assert source_queue_root.exists(), f"Source queue root does not exist | {source_queue_root}"
    for source_config_path in sorted(source_queue_root.glob("*.yaml")):
        source_stem_match = SOURCE_QUEUE_STEM_PATTERN.match(source_config_path.stem)
        assert source_stem_match is not None, f"Unexpected source queue file name | {source_config_path.name}"
        run_stem = source_stem_match.group("run_stem")
        surface_name = None
        for candidate_surface_name in SURFACE_NAME_LIST:
            suffix = f"_{candidate_surface_name}"
            if run_stem.endswith(suffix):
                surface_name = candidate_surface_name
                observed_family_name = run_stem[: -len(suffix)]
                break
        assert surface_name is not None, f"Unable to resolve surface from source queue | {source_config_path.name}"
        if observed_family_name == family_name:
            family_entry_list.append(
                (
                    observed_family_name,
                    surface_name,
                    source_config_path.relative_to(PROJECT_PATH).as_posix(),
                )
            )

    observed_surface_set = {entry[1] for entry in family_entry_list}
    assert observed_surface_set == set(SURFACE_NAME_LIST), (
        f"Family must provide global/fw/bw source configs | {family_name} | {observed_surface_set}"
    )
    return sorted(family_entry_list, key=lambda entry: SURFACE_NAME_LIST.index(entry[1]))


def prepare_model_development_campaign(family_name: str, version_name: str) -> Path:

    """Prepare one three-surface model-development campaign."""

    campaign_name = build_campaign_name(family_name, version_name)
    campaign_root = Path(CAMPAIGN_ROOT) / campaign_name
    queue_root = campaign_root / "queue"
    queue_path_list: list[str] = []
    for queue_index, (_, surface_name, source_config_path) in enumerate(
        collect_family_source_entries(family_name),
        start=1,
    ):
        config = build_model_development_config(
            family_name,
            version_name,
            surface_name,
            source_config_path,
            queue_index,
        )
        queue_path = queue_root / f"{queue_index:03d}_{family_name}_{surface_name}.yaml"
        write_yaml_dictionary(queue_path, config)
        queue_path_list.append(queue_path.as_posix())

    version_dictionary = INPUT_MODE_VERSION_DICTIONARY[version_name]
    manifest = {
        "schema_version": 1,
        "campaign_name": campaign_name,
        "campaign_type": "dataset_input_mode_model_development_retraining",
        "family_name": family_name,
        "dataset_name": version_dictionary["dataset_name"],
        "input_mode": version_dictionary["input_mode"],
        "dataset_schema": version_dictionary["dataset_schema"],
        "source_dataset_root": version_dictionary["source_dataset_root"],
        "expected_model_archive_root": version_dictionary["model_archive_root"],
        "expected_surface_list": SURFACE_NAME_LIST,
        "expected_run_count": len(queue_path_list),
        "planning_report_path": PLANNING_REPORT_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "queue_root": f"{QUEUE_ROOT}/{campaign_name}",
        "queue_config_path_list": queue_path_list,
        "execution_policy": {
            "operator_run_required": True,
            "stop_on_error": True,
            "run_te_curve_verification_pipeline": False,
        },
    }
    manifest_path = campaign_root / "campaign.yaml"
    write_yaml_dictionary(manifest_path, manifest)
    return PROJECT_PATH / manifest_path


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--family", required=True, choices=sorted(collect_model_development_family_set()))
    parser.add_argument("--version", required=True, choices=sorted(INPUT_MODE_VERSION_DICTIONARY))
    return parser.parse_args()


def collect_model_development_family_set() -> set[str]:

    """Collect available model-development families from completed source queues."""

    family_set: set[str] = set()
    source_queue_root = PROJECT_PATH / SOURCE_QUEUE_ROOT
    assert source_queue_root.exists(), f"Source queue root does not exist | {source_queue_root}"
    for source_config_path in sorted(source_queue_root.glob("*.yaml")):
        source_stem_match = SOURCE_QUEUE_STEM_PATTERN.match(source_config_path.stem)
        assert source_stem_match is not None, f"Unexpected source queue file name | {source_config_path.name}"
        run_stem = source_stem_match.group("run_stem")
        for candidate_surface_name in SURFACE_NAME_LIST:
            suffix = f"_{candidate_surface_name}"
            if run_stem.endswith(suffix):
                family_set.add(run_stem[: -len(suffix)])
                break
    assert family_set, f"No source families found | {source_queue_root}"
    return family_set


def main() -> None:

    """Run campaign preparation."""

    arguments = parse_command_line_arguments()
    manifest_path = prepare_model_development_campaign(arguments.family, arguments.version)
    print(f"[DONE] Prepared campaign manifest | {manifest_path.relative_to(PROJECT_PATH).as_posix()}")


if __name__ == "__main__":
    main()
