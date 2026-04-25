"""Prepare the bidirectional original-dataset Track 1 mega-campaign package."""

from __future__ import annotations

# Import Python Utilities
import sys
from datetime import datetime
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[4]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import YAML Utilities
import yaml

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation import exact_paper_model_bank_support

CONFIG_ROOT = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "original_dataset_exact_model_bank"
)
BASELINE_CONFIG_PATH_MAP = {
    "forward": CONFIG_ROOT / "baseline_forward.yaml",
    "backward": CONFIG_ROOT / "baseline_backward.yaml",
}
CAMPAIGN_CONFIG_ROOT = (
    CONFIG_ROOT
    / "campaigns"
    / "track1"
    / "exact_paper"
    / "bidirectional_original_dataset"
)
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
PLANNING_REPORT_RELATIVE_PATH = (
    "doc/reports/campaign_plans/track1/exact_paper/"
    "2026-04-26-00-43-19_track1_bidirectional_original_dataset_mega_relaunch_after_micro_gate_plan_report.md"
)
LAUNCHER_RELATIVE_PATH = "scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1"
REMOTE_WRAPPER_RELATIVE_PATH = "scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1"
LOCAL_HELPER_RELATIVE_PATH = "scripts/campaigns/track1/exact_paper/invoke_exact_paper_campaign_local.ps1"
SHARED_LAUNCHER_RELATIVE_PATH = "scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1"
LAUNCHER_NOTE_RELATIVE_PATH = "doc/scripts/campaigns/run_track1_bidirectional_original_dataset_mega_campaign.md"
CAMPAIGN_OUTPUT_DIRECTORY_TEMPLATE = (
    "output/training_campaigns/track1/exact_paper/bidirectional_original_dataset/{campaign_name}"
)
VALIDATION_OUTPUT_ROOT = "output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank"
ATTEMPT_SEED_LIST = [0, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 27, 29, 31, 37, 42, 47, 53, 59, 61]


def load_yaml_file(config_path: Path) -> dict:

    """Load one YAML file."""

    with config_path.open("r", encoding="utf-8") as input_file:
        return yaml.safe_load(input_file)


def save_yaml_file(payload: dict, output_path: Path) -> None:

    """Persist one YAML payload."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False)


def build_campaign_config(
    direction_label: str,
    family_name: str,
    attempt_index: int,
    split_seed: int,
    campaign_slug: str,
) -> dict:

    """Build one campaign config payload."""

    baseline_payload = load_yaml_file(BASELINE_CONFIG_PATH_MAP[direction_label])
    family_slug = family_name.lower()
    attempt_slug = f"attempt_{attempt_index:02d}"

    baseline_payload["paths"]["output_root"] = VALIDATION_OUTPUT_ROOT
    baseline_payload["experiment"]["run_name"] = (
        f"track1_original_dataset_{direction_label}_{family_slug}_{attempt_slug}"
    )
    baseline_payload["experiment"]["model_family"] = "paper_reimplementation_rcim_original_dataset_exact_model_bank"
    baseline_payload["experiment"]["model_type"] = f"exact_model_bank_{direction_label}_{family_slug}_campaign"
    baseline_payload["training"]["enabled_families"] = [family_name]
    baseline_payload["training"]["random_seed"] = int(split_seed)
    if family_name == "SVR":
        baseline_payload["training"]["grid_search_disabled_families"] = ["SVR"]
    else:
        baseline_payload["training"]["grid_search_disabled_families"] = []
    baseline_payload.pop("smoke", None)
    return baseline_payload


def build_campaign_config_path(
    direction_label: str,
    family_name: str,
    attempt_index: int,
    campaign_slug: str,
) -> Path:

    """Build one campaign config path."""

    family_slug = family_name.lower()
    campaign_directory = (
        CAMPAIGN_CONFIG_ROOT
        / direction_label
        / family_slug
        / campaign_slug
    )
    filename = (
        f"{attempt_index:03d}_track1_original_dataset_{direction_label}_{family_slug}_"
        f"attempt_{attempt_index:02d}.yaml"
    )
    return campaign_directory / filename


def build_campaign_readme_markdown(campaign_slug: str, direction_label: str, family_name: str) -> str:

    """Build one family-direction campaign README."""

    return "\n".join(
        [
            f"# {campaign_slug}",
            "",
            f"- direction: `{direction_label}`",
            f"- family: `{family_name}`",
            f"- attempt count: `{len(ATTEMPT_SEED_LIST)}`",
            f"- split seeds: `{', '.join(str(value) for value in ATTEMPT_SEED_LIST)}`",
            "",
        ]
    )


def main() -> None:

    """Prepare the complete mega-campaign package and active state."""

    timestamp_string = datetime.now().astimezone().strftime("%Y-%m-%d_%H_%M_%S")
    campaign_name = f"track1_bidirectional_original_dataset_mega_campaign_{timestamp_string}"
    queue_config_relative_path_list: list[str] = []
    protected_file_relative_path_list = [
        PLANNING_REPORT_RELATIVE_PATH.replace("/", "\\"),
        LAUNCHER_RELATIVE_PATH.replace("/", "\\"),
        REMOTE_WRAPPER_RELATIVE_PATH.replace("/", "\\"),
        LOCAL_HELPER_RELATIVE_PATH.replace("/", "\\"),
        SHARED_LAUNCHER_RELATIVE_PATH.replace("/", "\\"),
        LAUNCHER_NOTE_RELATIVE_PATH.replace("/", "\\"),
        "doc\\running\\active_training_campaign.yaml",
    ]

    for direction_label in ["forward", "backward"]:
        for family_name in exact_paper_model_bank_support.EXACT_FAMILY_ORDER:
            campaign_slug = f"{datetime.now().strftime('%Y-%m-%d')}_track1_{direction_label}_{family_name.lower()}_original_dataset_mega_campaign"
            campaign_directory = CAMPAIGN_CONFIG_ROOT / direction_label / family_name.lower() / campaign_slug
            campaign_directory.mkdir(parents=True, exist_ok=True)
            readme_path = campaign_directory / "README.md"
            readme_path.write_text(
                build_campaign_readme_markdown(campaign_slug, direction_label, family_name),
                encoding="utf-8",
            )
            protected_file_relative_path_list.append(str(readme_path.relative_to(PROJECT_PATH)).replace("/", "\\"))

            for attempt_index, split_seed in enumerate(ATTEMPT_SEED_LIST, start=1):
                config_path = build_campaign_config_path(
                    direction_label,
                    family_name,
                    attempt_index,
                    campaign_slug,
                )
                save_yaml_file(
                    build_campaign_config(direction_label, family_name, attempt_index, split_seed, campaign_slug),
                    config_path,
                )
                queue_config_relative_path_list.append(str(config_path.relative_to(PROJECT_PATH)).replace("/", "\\"))

    active_campaign_payload = {
        "campaign_name": campaign_name,
        "status": "prepared",
        "planning_report_path": PLANNING_REPORT_RELATIVE_PATH.replace("/", "\\"),
        "campaign_config_directory": str(CAMPAIGN_CONFIG_ROOT.relative_to(PROJECT_PATH)).replace("/", "\\"),
        "queue_root": None,
        "campaign_output_root": "output/training_campaigns",
        "campaign_output_directory": CAMPAIGN_OUTPUT_DIRECTORY_TEMPLATE.format(
            campaign_name=campaign_name
        ).replace("/", "\\"),
        "launch_mode": "remote_operator_launcher",
        "activation_pending_user_confirmation": False,
        "prepared_at": datetime.now().astimezone().isoformat(),
        "started_at": None,
        "finished_at": None,
        "completion_recorded_at": None,
        "results_report_path": None,
        "remote_host_alias": "xilab-remote",
        "remote_repository_path": (
            "C:\\Users\\Martina Salami\\Documents\\Davide\\Physics-Informed-Neural-Networks"
        ),
        "remote_conda_environment_name": "standard_ml_lan_node",
        "queue_config_path_list": queue_config_relative_path_list,
        "protected_file_list": protected_file_relative_path_list,
        "launch_command_list": [
            ".\\scripts\\campaigns\\track1\\exact_paper\\run_track1_bidirectional_original_dataset_mega_campaign.ps1 -Remote",
        ],
        "remote_bootstrap_contract": {
            "queue_bundle_transport": "temporary_python_script_with_json_safe_path_literals",
            "remote_preflight_transport": "temporary_python_script_with_conda_run",
            "onnx_dependency_preflight": [
                "skl2onnx",
                "onnxmltools",
                "onnxconverter-common",
                "xgboost",
                "lightgbm",
            ],
            "forbidden_patterns": [
                "python -c for queue bundle parsing",
                "raw python path literals that terminate with a backslash",
            ],
        },
        "completed_family_list": [],
        "pending_family_list": list(exact_paper_model_bank_support.EXACT_FAMILY_ORDER),
        "interruption_note": None,
    }
    save_yaml_file(active_campaign_payload, ACTIVE_CAMPAIGN_STATE_PATH)
    print(f"[DONE] Prepared mega-campaign queue count | {len(queue_config_relative_path_list)}", flush=True)
    print(f"[DONE] Active campaign state updated | {ACTIVE_CAMPAIGN_STATE_PATH}", flush=True)


if __name__ == "__main__":

    main()
