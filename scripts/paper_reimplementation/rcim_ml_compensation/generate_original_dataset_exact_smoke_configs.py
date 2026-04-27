"""Generate per-family smoke configs for the bidirectional original-dataset branch."""

from __future__ import annotations

# Import Python Utilities
import sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import YAML Utilities
import yaml

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation import exact_paper_model_bank_support
from scripts.training import shared_training_infrastructure

CONFIG_ROOT = (
    shared_training_infrastructure.PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "original_dataset_exact_model_bank"
)
SMOKE_CONFIG_ROOT = CONFIG_ROOT / "smoke"
BASELINE_CONFIG_PATH_MAP = {
    "forward": CONFIG_ROOT / "baseline_forward.yaml",
    "backward": CONFIG_ROOT / "baseline_backward.yaml",
}
SMOKE_OUTPUT_ROOT = "output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/smoke"
SMOKE_FILE_COUNT_LIMITS = {
    "max_train_file_count": 10,
    "max_validation_file_count": 3,
    "max_test_file_count": 3,
}


def load_yaml_file(config_path: Path) -> dict:

    """Load one YAML file."""

    with config_path.open("r", encoding="utf-8") as input_file:
        return yaml.safe_load(input_file)


def save_yaml_file(payload: dict, output_path: Path) -> None:

    """Persist one YAML payload."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False)


def build_family_smoke_config(direction_label: str, family_name: str) -> dict:

    """Build one family-local smoke config."""

    baseline_payload = load_yaml_file(BASELINE_CONFIG_PATH_MAP[direction_label])
    normalized_family_name = str(family_name).strip().upper()
    family_slug = normalized_family_name.lower()

    baseline_payload["paths"]["output_root"] = SMOKE_OUTPUT_ROOT
    baseline_payload["experiment"]["run_name"] = (
        f"rcim_original_dataset_exact_model_bank_{direction_label}_{family_slug}_smoke"
    )
    baseline_payload["experiment"]["model_family"] = "paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke"
    baseline_payload["experiment"]["model_type"] = f"exact_model_bank_{direction_label}_{family_slug}_smoke"
    baseline_payload["training"]["enabled_families"] = [normalized_family_name]
    baseline_payload["training"]["grid_search_disabled_families"] = [normalized_family_name]
    baseline_payload["training"]["hyperparameter_search"]["mode"] = "disabled"
    baseline_payload["training"]["threadpool_limit"] = 1
    baseline_payload["training"]["joblib_cpu_limit"] = 0
    baseline_payload["smoke"] = {
        "enabled": True,
        **SMOKE_FILE_COUNT_LIMITS,
    }
    return baseline_payload


def main() -> None:

    """Generate the smoke-config tree."""

    generated_file_count = 0
    for direction_label in ["forward", "backward"]:
        for family_name in exact_paper_model_bank_support.EXACT_FAMILY_ORDER:
            output_path = SMOKE_CONFIG_ROOT / direction_label / f"{family_name.lower()}_smoke.yaml"
            save_yaml_file(
                build_family_smoke_config(direction_label, family_name),
                output_path,
            )
            generated_file_count += 1
            print(
                "[DONE] Smoke config written | "
                f"{shared_training_infrastructure.format_project_relative_path(output_path)}",
                flush=True,
            )

    print(f"[DONE] Generated smoke config count | {generated_file_count}", flush=True)


if __name__ == "__main__":

    main()
