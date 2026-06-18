"""Validate Wave 3 skeleton readiness for one-batch training-stack execution."""

from __future__ import annotations

# Import Standard Libraries
import argparse
import sys
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml


PROJECT_PATH = Path(__file__).resolve().parents[3]
BASE_CONFIG_PATH = Path(
    "config/training/track2g_curve_aware_training/campaigns/"
    "2026-06-08_track2g_curve_aware_training_campaign/queue/01_pointwise_control_global.yaml"
)
TEMPLATE_PATH = Path("config/training/wave3_embryonic_skeleton/wave3_harmonic_prior_residual_template.yaml")
GENERATED_CONFIG_ROOT = PROJECT_PATH / "output" / "validation_checks" / "wave3_training_smoke_ready" / "generated_configs"

if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.training.validate_training_setup import validate_training_setup


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read one YAML file as a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def write_yaml_file(output_path: Path, payload: dict[str, Any]) -> None:

    """Write one YAML file."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False)


def resolve_project_path(path_value: Path) -> Path:

    """Resolve a repository-relative or absolute path."""

    return path_value if path_value.is_absolute() else PROJECT_PATH / path_value


def build_training_smoke_ready_config(base_config: dict[str, Any], template_config: dict[str, Any]) -> dict[str, Any]:

    """Build a complete validation-only Wave 3 training config."""

    wave3_model_config = dict(template_config["model"])
    wave3_model_config.pop("model_type", None)
    wave3_model_family = str(template_config["model"].get("model_family", "wave3_harmonic_prior_residual"))
    harmonic_index_list = list(wave3_model_config.get("harmonic_index_list", []))

    training_config = dict(base_config)
    training_config["paths"] = dict(base_config["paths"])
    training_config["experiment"] = {
        "run_name": "te_wave3_harmonic_prior_residual_training_smoke_ready",
        "model_family": wave3_model_family,
        "model_type": "wave3_harmonic_prior_residual",
    }
    training_config["metadata"] = {
        "phase_name": "wave3_parallel_hardening",
        "implementation_status": "training_smoke_ready",
        "campaign_readiness": "not_campaign_ready",
        "source_template_path": TEMPLATE_PATH.as_posix(),
        "source_base_config_path": BASE_CONFIG_PATH.as_posix(),
        "blocked_by": [
            "track2h_loss_policy",
            "real_wave3_campaign_plan",
            "active_campaign_state_gate",
        ],
        "training_variant": "global",
        "direction_scope_label": "bidirectional",
        "use_forward_direction": True,
        "use_backward_direction": True,
    }
    training_config["dataset"] = dict(base_config["dataset"])
    training_config["dataset"]["num_workers"] = 0
    training_config["dataset"]["pin_memory"] = False
    training_config["model"] = wave3_model_config
    training_config["training"] = dict(base_config["training"])
    training_config["training"]["learning_rate"] = 5.0e-4
    training_config["training"]["fast_dev_run"] = False
    training_config["training"]["deterministic"] = True
    training_config["training"]["loss"] = {
        "profile": "pointwise_control",
        "weights": {
            "point": 1.0,
            "centered": 0.0,
            "offset": 0.0,
            "amplitude": 0.0,
            "harmonic": 0.0,
        },
        "harmonic_index_list": harmonic_index_list,
    }
    training_config["runtime"] = dict(base_config.get("runtime", {}))
    training_config["runtime"]["accelerator"] = "cpu"
    training_config["runtime"]["devices"] = 1
    training_config["runtime"]["precision"] = "32"
    training_config["runtime"]["benchmark"] = False
    return training_config


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-config-path", type=Path, default=BASE_CONFIG_PATH)
    parser.add_argument("--template-path", type=Path, default=TEMPLATE_PATH)
    parser.add_argument("--generated-config-root", type=Path, default=GENERATED_CONFIG_ROOT)
    parser.add_argument("--output-suffix", type=str, default="wave3_training_smoke_ready")
    return parser.parse_args()


def main() -> int:

    """Run the Wave 3 training-smoke-ready validation."""

    argument_namespace = parse_arguments()
    base_config_path = resolve_project_path(argument_namespace.base_config_path)
    template_path = resolve_project_path(argument_namespace.template_path)
    generated_config_root = argument_namespace.generated_config_root
    generated_config_root = resolve_project_path(generated_config_root)

    base_config = read_yaml_file(base_config_path)
    template_config = read_yaml_file(template_path)
    training_config = build_training_smoke_ready_config(base_config, template_config)
    generated_config_path = generated_config_root / "wave3_harmonic_prior_residual_training_smoke_ready.yaml"
    write_yaml_file(generated_config_path, training_config)

    validation_summary_path, validation_report_path = validate_training_setup(
        generated_config_path,
        output_suffix=argument_namespace.output_suffix,
    )

    print(f"Prepared Wave 3 generated validation config | {generated_config_path}")
    print(f"Prepared Wave 3 training-smoke-ready summary | {validation_summary_path}")
    print(f"Prepared Wave 3 training-smoke-ready report | {validation_report_path}")
    print("Wave 3 skeleton is training-smoke-ready and still not campaign-ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
