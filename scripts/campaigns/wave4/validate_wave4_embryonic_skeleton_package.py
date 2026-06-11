"""Validate the embryonic Wave 4 skeleton package."""

from __future__ import annotations

# Import Standard Libraries
import argparse
import sys
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml


PROJECT_PATH = Path(__file__).resolve().parents[3]
TEMPLATE_PATH = Path("config/training/wave4_embryonic_skeleton/wave4a_mmt_equation_diagnostic_template.yaml")

if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.models.wave4_mmt_diagnostic_adapter import Wave4MMTDiagnosticAdapter


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read one YAML file as a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def validate_template_payload(template_payload: dict[str, Any]) -> None:

    """Validate skeleton metadata and launch blockers."""

    metadata = template_payload.get("metadata", {})
    training_policy = template_payload.get("training_policy", {})
    assert metadata.get("implementation_status") == "implementation_ready"
    assert metadata.get("campaign_readiness") == "not_campaign_ready"
    assert training_policy.get("launch_allowed") is False
    assert training_policy.get("queue_allowed") is False
    assert "requires_parameter_inventory" in metadata.get("blocker_list", [])


def run_mmt_adapter_smoke(template_payload: dict[str, Any]) -> None:

    """Run the MMT diagnostic adapter smoke check."""

    diagnostic_configuration = template_payload.get("diagnostic", {})
    sample_count = int(diagnostic_configuration.get("sample_count", 720))
    top_harmonic_count = int(diagnostic_configuration.get("top_harmonic_count", 8))

    adapter = Wave4MMTDiagnosticAdapter()
    status_dictionary = adapter.to_status_dictionary()
    summary = adapter.run_demo_summary(sample_count=sample_count, top_k=top_harmonic_count)

    assert status_dictionary["implementation_status"] == "implementation_ready"
    assert status_dictionary["campaign_readiness"] == "not_campaign_ready"
    assert summary.sample_count == sample_count
    assert summary.campaign_readiness == "not_campaign_ready"
    assert len(summary.dominant_harmonic_index_list) == top_harmonic_count


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--template-path",
        default=TEMPLATE_PATH,
        type=Path,
        help="Repository-relative Wave 4 embryonic template path.",
    )
    return parser.parse_args()


def main() -> int:

    """Validate the Wave 4 embryonic skeleton."""

    argument_namespace = parse_arguments()
    template_path = PROJECT_PATH / argument_namespace.template_path
    template_payload = read_yaml_file(template_path)
    validate_template_payload(template_payload)
    run_mmt_adapter_smoke(template_payload)

    print(
        "Wave 4 embryonic skeleton validated | "
        "implementation_status=implementation_ready | "
        "campaign_readiness=not_campaign_ready"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
