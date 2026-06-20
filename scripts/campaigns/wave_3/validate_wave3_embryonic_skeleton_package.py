"""Validate the embryonic Wave 5.1 skeleton package."""

from __future__ import annotations

# Import Standard Libraries
import argparse
import sys
from pathlib import Path
from typing import Any

# Import PyTorch Utilities
import torch

# Import YAML Utilities
import yaml


PROJECT_PATH = Path(__file__).resolve().parents[3]
TEMPLATE_PATH = Path("config/training/wave3_embryonic_skeleton/wave3_harmonic_prior_residual_template.yaml")

if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.models.model_factory import create_model


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
    assert "blocked_on_track2h_results" in metadata.get("blocker_list", [])


def run_forward_smoke(template_payload: dict[str, Any]) -> None:

    """Instantiate the model and run point and sequence forward smoke checks."""

    model_configuration = dict(template_payload["model"])
    model_type = str(model_configuration.pop("model_type"))
    model_configuration.pop("model_family", None)
    model = create_model(model_type, model_configuration)
    model.eval()

    input_size = int(model_configuration["input_size"])
    point_input_tensor = torch.randn(4, input_size)
    point_input_tensor[:, 0] = torch.linspace(0.0, 360.0, 4)
    sequence_input_tensor = torch.randn(4, 33, input_size)
    sequence_input_tensor[:, :, 0] = torch.linspace(0.0, 360.0, 33).reshape(1, 33)

    with torch.no_grad():
        point_output_tensor = model(point_input_tensor)
        sequence_output_tensor = model(sequence_input_tensor)
        auxiliary_dictionary = model.compute_auxiliary_output_dictionary(sequence_input_tensor, sequence_input_tensor)

    assert tuple(point_output_tensor.shape) == (4, 1), f"Unexpected point output shape | {tuple(point_output_tensor.shape)}"
    assert tuple(sequence_output_tensor.shape) == (4, 1), f"Unexpected sequence output shape | {tuple(sequence_output_tensor.shape)}"
    assert "structured_prediction_tensor" in auxiliary_dictionary
    assert "wave3_residual_prediction_tensor" in auxiliary_dictionary


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--template-path",
        default=TEMPLATE_PATH,
        type=Path,
        help="Repository-relative Wave 5.1 embryonic template path.",
    )
    return parser.parse_args()


def main() -> int:

    """Validate the Wave 5.1 embryonic skeleton."""

    argument_namespace = parse_arguments()
    template_path = PROJECT_PATH / argument_namespace.template_path
    template_payload = read_yaml_file(template_path)
    validate_template_payload(template_payload)
    run_forward_smoke(template_payload)

    print(
        "Wave 5.1 embryonic skeleton validated | "
        "implementation_status=implementation_ready | "
        "campaign_readiness=not_campaign_ready"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
