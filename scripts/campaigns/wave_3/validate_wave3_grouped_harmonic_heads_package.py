"""Validate the Wave 3 grouped harmonic-heads skeleton package."""

from __future__ import annotations

# Import Standard Libraries
import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Import PyTorch Utilities
import torch

# Import YAML Utilities
import yaml


PROJECT_PATH = Path(__file__).resolve().parents[3]
TEMPLATE_PATH = Path("config/training/wave3_embryonic_skeleton/wave3_grouped_harmonic_heads_template.yaml")
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "wave3_grouped_harmonic_heads"
SUMMARY_FILENAME = "wave3_grouped_harmonic_heads_validation_summary.yaml"

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
    assert metadata.get("skeleton_name") == "wave3_grouped_harmonic_heads"
    assert metadata.get("implementation_status") == "implementation_ready"
    assert metadata.get("campaign_readiness") == "not_campaign_ready"
    assert training_policy.get("launch_allowed") is False
    assert training_policy.get("queue_allowed") is False
    assert "blocked_on_track2h_results" in metadata.get("blocker_list", [])


def run_forward_smoke(template_payload: dict[str, Any]) -> dict[str, Any]:

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

    expected_auxiliary_key_list = [
        "low_order_prediction_tensor",
        "stable_middle_prediction_tensor",
        "high_order_prediction_tensor",
        "grouped_harmonic_prediction_tensor",
        "residual_prediction_tensor",
        "wave3_grouped_residual_prediction_tensor",
        "prediction_tensor",
    ]

    assert tuple(point_output_tensor.shape) == (4, 1), f"Unexpected point output shape | {tuple(point_output_tensor.shape)}"
    assert tuple(sequence_output_tensor.shape) == (4, 1), f"Unexpected sequence output shape | {tuple(sequence_output_tensor.shape)}"
    for auxiliary_key in expected_auxiliary_key_list:
        assert auxiliary_key in auxiliary_dictionary, f"Missing auxiliary output | {auxiliary_key}"
        assert tuple(auxiliary_dictionary[auxiliary_key].shape) == (4, 1)
        assert torch.isfinite(auxiliary_dictionary[auxiliary_key]).all(), f"Non-finite auxiliary output | {auxiliary_key}"

    return {
        "point_output_shape": list(point_output_tensor.shape),
        "sequence_output_shape": list(sequence_output_tensor.shape),
        "auxiliary_key_list": expected_auxiliary_key_list,
        "low_order_harmonic_index_list": model.low_order_harmonic_index_tensor.cpu().tolist(),
        "stable_middle_harmonic_index_list": model.stable_middle_harmonic_index_tensor.cpu().tolist(),
        "high_order_harmonic_index_list": model.high_order_harmonic_index_tensor.cpu().tolist(),
    }


def write_summary(output_directory: Path, summary_dictionary: dict[str, Any]) -> None:

    """Write validation summary YAML."""

    output_directory.mkdir(parents=True, exist_ok=True)
    with (output_directory / SUMMARY_FILENAME).open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(summary_dictionary, output_file, sort_keys=False)


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--template-path",
        default=TEMPLATE_PATH,
        type=Path,
        help="Repository-relative Wave 3 grouped-head template path.",
    )
    parser.add_argument("--output-root", default=DEFAULT_OUTPUT_ROOT, type=Path)
    parser.add_argument("--run-id", default="", type=str)
    return parser.parse_args()


def main() -> int:

    """Validate the Wave 3 grouped harmonic-heads skeleton."""

    argument_namespace = parse_arguments()
    template_path = PROJECT_PATH / argument_namespace.template_path
    run_id = argument_namespace.run_id
    if not run_id:
        run_id = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}__wave3_grouped_harmonic_heads"

    template_payload = read_yaml_file(template_path)
    validate_template_payload(template_payload)
    smoke_summary_dictionary = run_forward_smoke(template_payload)

    output_directory = argument_namespace.output_root / run_id
    summary_dictionary = {
        "run_id": run_id,
        "implementation_status": "implementation_ready",
        "campaign_readiness": "not_campaign_ready",
        "template_path": argument_namespace.template_path.as_posix(),
        "output_directory": output_directory.relative_to(PROJECT_PATH).as_posix(),
        **smoke_summary_dictionary,
    }
    write_summary(output_directory, summary_dictionary)

    print(
        "Wave 3 grouped harmonic-heads skeleton validated | "
        "implementation_status=implementation_ready | "
        "campaign_readiness=not_campaign_ready | "
        f"output_directory={output_directory}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
