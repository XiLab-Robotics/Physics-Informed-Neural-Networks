"""Prepare the bounded Phase 3 C1-Fw initialization-stability campaign."""

from __future__ import annotations

# Import Python Utilities
import sys
from pathlib import Path
from typing import Any

# Define Repository Root Before Importing Project Modules
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Phase 3 Campaign Construction Utilities
from scripts.campaigns.wave_5_2.prepare_phase3_quasi_static_compliance_pinn_campaign import (
    AUDIT_ARTIFACT_PATH,
    COMMON_SPLIT_MANIFEST_PATH,
    EXCLUDED_CONDITION_ID_LIST,
    MODEL_REPORT_PATH,
    PLANNING_REPORT_PATH,
    TECHNICAL_DOCUMENT_PATH,
    build_run_configuration,
    write_yaml,
)

# Define Campaign Constants
CAMPAIGN_NAME = "phase3_c1_fw_stability_repeat_2026_07_26"
CAMPAIGN_DIRECTORY = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "quasi_static_compliance_pinn"
    / "campaigns"
    / "2026-07-26_phase3_c1_fw_stability_repeat"
)
QUEUE_DIRECTORY = CAMPAIGN_DIRECTORY / "queue"
INITIAL_CAMPAIGN_NAME = "phase3_quasi_static_compliance_pinn_2026_07_26"
INITIAL_C1_FW_CONFIG_PATH = (
    "config/training/quasi_static_compliance_pinn/campaigns/"
    "2026-07-26_phase3_quasi_static_compliance_pinn/queue/"
    "004_c1_linear_compliance_soft_fw.yaml"
)
STABILITY_RANDOM_SEED_LIST = [314159, 271828]


def build_repeat_configuration(
    queue_index: int,
    random_seed: int,
) -> dict[str, Any]:
    """Build one C1-Fw repeat with a distinct reproducible initialization."""

    configuration = build_run_configuration(queue_index, "C1", "fw")
    seed_slug = f"seed_{random_seed}"
    family_name = (
        "phase3_pinn_c1_linear_compliance_soft_fw_"
        f"{seed_slug}"
    )
    configuration["experiment"].update(
        {
            "run_name": (
                "te_phase3_pinn_c1_linear_compliance_soft_fw_"
                f"{seed_slug}__polished_setpoints"
            ),
            "model_family": family_name,
        }
    )
    configuration["metadata"].update(
        {
            "campaign_name": CAMPAIGN_NAME,
            "campaign_config_id": family_name,
            "queue_index": queue_index,
            "repeat_of_campaign_name": INITIAL_CAMPAIGN_NAME,
            "repeat_of_config_path": INITIAL_C1_FW_CONFIG_PATH,
            "stability_repeat_index": queue_index,
            "training_random_seed": random_seed,
            "probe_group": "phase3_c1_fw_initialization_stability",
            "roadmap_role_coverage": [
                "linear_compliance_soft_residual",
                "initialization_stability_repeat",
            ],
        }
    )
    configuration["training"]["random_seed"] = random_seed
    return configuration


def main() -> None:
    """Create the two-run stability manifest and queue package."""

    queue_path_list: list[str] = []
    for queue_index, random_seed in enumerate(
        STABILITY_RANDOM_SEED_LIST,
        start=1,
    ):
        configuration = build_repeat_configuration(
            queue_index,
            random_seed,
        )
        queue_path = QUEUE_DIRECTORY / (
            f"{queue_index:03d}_c1_linear_compliance_soft_fw_"
            f"seed_{random_seed}.yaml"
        )
        write_yaml(queue_path, configuration)
        queue_path_list.append(
            queue_path.relative_to(PROJECT_ROOT).as_posix()
        )

    campaign_payload = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": (
            "wave_5_2_phase_3_c1_fw_initialization_stability"
        ),
        "parent_campaign_name": INITIAL_CAMPAIGN_NAME,
        "family_name": "quasi_static_compliance_pinn",
        "formulation": "C1",
        "surface": "fw",
        "dataset_name": "polished_dataset",
        "input_mode": "setpoints",
        "expected_run_count": len(queue_path_list),
        "random_seed_list": list(STABILITY_RANDOM_SEED_LIST),
        "planning_report_path": PLANNING_REPORT_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "model_report_path": MODEL_REPORT_PATH,
        "audit_artifact_path": AUDIT_ARTIFACT_PATH,
        "common_split_manifest_path": COMMON_SPLIT_MANIFEST_PATH,
        "common_split_signature": (
            "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f"
            "4376aa64f8e16"
        ),
        "excluded_condition_id_list": list(
            EXCLUDED_CONDITION_ID_LIST
        ),
        "expected_curve_count_by_split": {
            "train": 675,
            "validation": 194,
            "test": 97,
        },
        "queue_root": (
            "config/training/queue/quasi_static_compliance_pinn/"
            f"{CAMPAIGN_NAME}"
        ),
        "queue_config_path_list": queue_path_list,
        "execution_policy": {
            "operator_run_required": False,
            "standing_approval_applies": True,
            "stop_on_error": True,
            "run_te_curve_verification_pipeline": False,
            "scalar_mae_only_promotion_allowed": False,
        },
    }
    write_yaml(CAMPAIGN_DIRECTORY / "campaign.yaml", campaign_payload)
    print(
        f"Prepared {len(queue_path_list)} Phase 3 C1-Fw stability repeats"
    )
    print(CAMPAIGN_DIRECTORY.relative_to(PROJECT_ROOT).as_posix())


if __name__ == "__main__":
    main()
