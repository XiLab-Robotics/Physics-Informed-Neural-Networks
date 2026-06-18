"""Validate the Wave 4B MMT feature-generator skeleton package."""

from __future__ import annotations

# Import Standard Libraries
import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Serialization Libraries
import yaml


PROJECT_PATH = Path(__file__).resolve().parents[3]
TEMPLATE_PATH = Path("config/training/wave4_embryonic_skeleton/wave4b_mmt_feature_generator_template.yaml")
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "wave4b_mmt_feature_generator"
SCHEMA_FILENAME = "wave4b_mmt_feature_schema.csv"
SAMPLE_FEATURE_FILENAME = "wave4b_mmt_sample_features.csv"
HARMONIC_FEATURE_FILENAME = "wave4b_mmt_harmonic_features.csv"
SUMMARY_FILENAME = "wave4b_mmt_feature_generator_summary.yaml"

if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.features.wave4b_mmt_feature_generator import DIAGNOSTIC_ONLY
from scripts.features.wave4b_mmt_feature_generator import INFERENCE_SAFE
from scripts.features.wave4b_mmt_feature_generator import TRAIN_ONLY_CALIBRATION
from scripts.features.wave4b_mmt_feature_generator import generate_wave4b_feature_payload
from scripts.features.wave4b_mmt_feature_generator import write_csv


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read one YAML file as a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def validate_template_payload(template_payload: dict[str, Any]) -> None:

    """Validate Wave 4B metadata and campaign blockers."""

    metadata = template_payload.get("metadata", {})
    feature_generation = template_payload.get("feature_generation", {})
    training_policy = template_payload.get("training_policy", {})

    assert metadata.get("skeleton_name") == "wave4b_mmt_feature_generator"
    assert metadata.get("implementation_status") == "implementation_ready"
    assert metadata.get("campaign_readiness") == "not_campaign_ready"
    assert training_policy.get("launch_allowed") is False
    assert training_policy.get("queue_allowed") is False
    assert feature_generation.get("inference_safe_only") is True
    assert "requires_track2h_quantile_probabilistic_closeout" in metadata.get("blocker_list", [])


def validate_payload_leakage_boundaries(payload_dictionary: dict[str, Any]) -> None:

    """Validate feature usage labels and dry-run inference exposure."""

    schema_row_list = payload_dictionary["schema_row_list"]
    sample_row_list = payload_dictionary["sample_row_list"]
    harmonic_row_list = payload_dictionary["harmonic_row_list"]
    status_dictionary = payload_dictionary["status_dictionary"]

    allowed_policy_set = {INFERENCE_SAFE, TRAIN_ONLY_CALIBRATION, DIAGNOSTIC_ONLY}
    assert schema_row_list, "Feature schema must not be empty"
    assert sample_row_list, "Sample feature rows must not be empty"
    assert harmonic_row_list, "Harmonic feature rows must not be empty"
    assert status_dictionary["campaign_readiness"] == "not_campaign_ready"
    assert any(row["usage_policy"] == DIAGNOSTIC_ONLY for row in schema_row_list)
    assert any(row["usage_policy"] == TRAIN_ONLY_CALIBRATION for row in schema_row_list)

    for schema_row in schema_row_list:
        assert schema_row["usage_policy"] in allowed_policy_set, schema_row
        if schema_row["usage_policy"] != INFERENCE_SAFE:
            assert "measured" in schema_row["source_boundary"] or "subsystem" in schema_row["feature_group"]

    for sample_row in sample_row_list:
        assert sample_row["usage_policy"] == INFERENCE_SAFE
        assert "measured_minus_mmt_mean_offset_arcsec" not in sample_row
        assert "measured_minus_mmt_centered_residual_arcsec" not in sample_row

    for harmonic_row in harmonic_row_list:
        assert harmonic_row["usage_policy"] == INFERENCE_SAFE


def write_validation_artifacts(output_directory: Path, payload_dictionary: dict[str, Any]) -> None:

    """Write dry-run validation artifacts."""

    output_directory.mkdir(parents=True, exist_ok=True)
    write_csv(output_directory / SCHEMA_FILENAME, payload_dictionary["schema_row_list"])
    write_csv(output_directory / SAMPLE_FEATURE_FILENAME, payload_dictionary["sample_row_list"])
    write_csv(output_directory / HARMONIC_FEATURE_FILENAME, payload_dictionary["harmonic_row_list"])
    with (output_directory / SUMMARY_FILENAME).open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload_dictionary["status_dictionary"], output_file, sort_keys=False)


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--template-path",
        default=TEMPLATE_PATH,
        type=Path,
        help="Repository-relative Wave 4B embryonic template path.",
    )
    parser.add_argument("--output-root", default=DEFAULT_OUTPUT_ROOT, type=Path)
    parser.add_argument("--run-id", default="", type=str)
    parser.add_argument("--sample-count", default=720, type=int)
    return parser.parse_args()


def main() -> int:

    """Validate the Wave 4B MMT feature-generator skeleton."""

    argument_namespace = parse_arguments()
    template_path = PROJECT_PATH / argument_namespace.template_path
    run_id = argument_namespace.run_id
    if not run_id:
        run_id = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}__wave4b_mmt_feature_generator"

    template_payload = read_yaml_file(template_path)
    validate_template_payload(template_payload)

    feature_generation = template_payload.get("feature_generation", {})
    harmonic_index_list = [int(value) for value in feature_generation.get("harmonic_index_list", [])]
    sample_count = int(argument_namespace.sample_count or feature_generation.get("sample_count", 720))
    payload = generate_wave4b_feature_payload(
        sample_count=sample_count,
        harmonic_index_list=harmonic_index_list,
    )
    payload_dictionary = {
        "schema_row_list": payload.schema_row_list,
        "sample_row_list": payload.sample_row_list,
        "harmonic_row_list": payload.harmonic_row_list,
        "status_dictionary": {
            **payload.status_dictionary,
            "run_id": run_id,
            "template_path": argument_namespace.template_path.as_posix(),
            "output_directory": (argument_namespace.output_root / run_id).relative_to(PROJECT_PATH).as_posix(),
        },
    }
    validate_payload_leakage_boundaries(payload_dictionary)
    write_validation_artifacts(argument_namespace.output_root / run_id, payload_dictionary)

    print(
        "Wave 4B MMT feature-generator skeleton validated | "
        "implementation_status=implementation_ready | "
        "campaign_readiness=not_campaign_ready | "
        f"output_directory={argument_namespace.output_root / run_id}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
