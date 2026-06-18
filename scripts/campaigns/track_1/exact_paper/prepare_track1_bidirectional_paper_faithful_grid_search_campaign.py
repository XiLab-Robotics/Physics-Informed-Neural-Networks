"""Prepare the Track 1 bidirectional paper-faithful grid-search campaign."""

from __future__ import annotations

# Import Python Utilities
import argparse
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
from scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank import (
    exact_paper_model_bank_support,
)
from scripts.tooling import repository_path_support

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
    / "bidirectional_paper_faithful_grid_search"
)
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
PLANNING_REPORT_RELATIVE_PATH = (
    "doc/reports/campaign_plans/track_1/exact_paper/"
    "2026-05-04-12-13-07_track1_paper_faithful_search_protocol_and_campaign_replacement_plan_report.md"
)
LAUNCHER_RELATIVE_PATH = (
    "scripts/campaigns/track_1/exact_paper/"
    "run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1"
)
REMOTE_WRAPPER_RELATIVE_PATH = "scripts/campaigns/track_1/exact_paper/run_exact_paper_campaign_remote.ps1"
LOCAL_HELPER_RELATIVE_PATH = "scripts/campaigns/track_1/exact_paper/invoke_exact_paper_campaign_local.ps1"
BASH_LAUNCHER_RELATIVE_PATH = (
    "scripts/campaigns/track_1/exact_paper/"
    "run_track1_bidirectional_paper_faithful_grid_search_campaign.sh"
)
SHARED_LAUNCHER_RELATIVE_PATH = "scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1"
LAUNCHER_NOTE_RELATIVE_PATH = (
    "doc/scripts/campaigns/"
    "run_track1_bidirectional_paper_faithful_grid_search_campaign.md"
)
CAMPAIGN_OUTPUT_DIRECTORY_TEMPLATE = (
    "output/training_campaigns/track1/exact_paper/"
    "bidirectional_paper_faithful_grid_search/{campaign_name}"
)
VALIDATION_OUTPUT_ROOT = "output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank"
PAPER_FAITHFUL_SPLIT_SEED = 0


def load_yaml_file(config_path: Path) -> dict:

    """Load one YAML file."""

    with config_path.open("r", encoding="utf-8") as input_file:
        return yaml.safe_load(input_file)


def save_yaml_file(payload: dict, output_path: Path) -> None:

    """Persist one YAML payload."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False)


def format_repository_path(path_value: str | Path, platform_name: str) -> str:

    """Format one repository-relative path for the selected platform."""

    if isinstance(path_value, Path):
        return repository_path_support.format_repository_relative_path(
            path_value,
            PROJECT_PATH,
            platform_name,
        )

    normalized_path_text = repository_path_support.normalize_repository_relative_path_text(path_value)
    if platform_name == repository_path_support.WINDOWS_PLATFORM_NAME:
        return normalized_path_text.replace("/", "\\")
    return normalized_path_text


def build_campaign_config(
    direction_label: str,
    family_name: str,
) -> dict:

    """Build one campaign config payload."""

    baseline_payload = load_yaml_file(BASELINE_CONFIG_PATH_MAP[direction_label])
    family_slug = family_name.lower()

    baseline_payload["paths"]["output_root"] = VALIDATION_OUTPUT_ROOT
    baseline_payload["experiment"]["run_name"] = (
        f"track1_paper_faithful_grid_search_{direction_label}_{family_slug}"
    )
    baseline_payload["experiment"]["model_family"] = "paper_reimplementation_rcim_original_dataset_exact_model_bank"
    baseline_payload["experiment"]["model_type"] = (
        f"exact_model_bank_{direction_label}_{family_slug}_paper_faithful_grid_search_campaign"
    )
    baseline_payload["training"]["enabled_families"] = [family_name]
    baseline_payload["training"]["random_seed"] = PAPER_FAITHFUL_SPLIT_SEED
    baseline_payload["training"]["grid_search_disabled_families"] = []
    baseline_payload.pop("smoke", None)
    return baseline_payload


def build_campaign_config_path(
    direction_label: str,
    family_name: str,
    campaign_slug: str,
) -> Path:

    """Build one campaign config path."""

    family_slug = family_name.lower()
    campaign_directory = CAMPAIGN_CONFIG_ROOT / direction_label / family_slug / campaign_slug
    filename = f"001_track1_paper_faithful_grid_search_{direction_label}_{family_slug}.yaml"
    return campaign_directory / filename


def build_campaign_readme_markdown(
    campaign_slug: str,
    direction_label: str,
    family_name: str,
) -> str:

    """Build one family-direction campaign README."""

    return "\n".join(
        [
            f"# {campaign_slug}",
            "",
            f"- direction: `{direction_label}`",
            f"- family: `{family_name}`",
            "- attempt count: `1`",
            f"- paper-faithful split seed: `{PAPER_FAITHFUL_SPLIT_SEED}`",
            "- paper-faithful protocol: `GridSearchCV fit plus historical cross_validate replay`",
            "- implementation baseline: `literalized recovered original workflow`",
            "",
        ]
    )


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the campaign preparer."""

    argument_parser = argparse.ArgumentParser(
        description="Prepare the Track 1 bidirectional paper-faithful grid-search campaign."
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser.parse_args()


def main() -> None:

    """Prepare the complete paper-faithful bidirectional campaign."""

    command_line_arguments = parse_command_line_arguments()
    repository_path_platform = repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(command_line_arguments)
    )
    timestamp_string = datetime.now().astimezone().strftime("%Y-%m-%d_%H_%M_%S")
    campaign_name = (
        "track1_bidirectional_paper_faithful_grid_search_campaign_"
        f"{timestamp_string}"
    )
    queue_config_relative_path_list: list[str] = []
    protected_file_relative_path_list = [
        format_repository_path(PLANNING_REPORT_RELATIVE_PATH, repository_path_platform),
        format_repository_path(LAUNCHER_RELATIVE_PATH, repository_path_platform),
        format_repository_path(REMOTE_WRAPPER_RELATIVE_PATH, repository_path_platform),
        format_repository_path(LOCAL_HELPER_RELATIVE_PATH, repository_path_platform),
        format_repository_path(BASH_LAUNCHER_RELATIVE_PATH, repository_path_platform),
        format_repository_path(SHARED_LAUNCHER_RELATIVE_PATH, repository_path_platform),
        format_repository_path(LAUNCHER_NOTE_RELATIVE_PATH, repository_path_platform),
        format_repository_path("doc/running/active_training_campaign.yaml", repository_path_platform),
    ]

    for direction_label in ["forward", "backward"]:
        for family_name in exact_paper_model_bank_support.EXACT_FAMILY_ORDER:
            campaign_slug = (
                f"{datetime.now().strftime('%Y-%m-%d')}_track1_{direction_label}_"
                f"{family_name.lower()}_paper_faithful_grid_search_campaign"
            )
            campaign_directory = CAMPAIGN_CONFIG_ROOT / direction_label / family_name.lower() / campaign_slug
            campaign_directory.mkdir(parents=True, exist_ok=True)
            readme_path = campaign_directory / "README.md"
            readme_path.write_text(
                build_campaign_readme_markdown(campaign_slug, direction_label, family_name),
                encoding="utf-8",
            )
            protected_file_relative_path_list.append(
                format_repository_path(readme_path, repository_path_platform)
            )

            config_path = build_campaign_config_path(direction_label, family_name, campaign_slug)
            save_yaml_file(build_campaign_config(direction_label, family_name), config_path)
            queue_config_relative_path_list.append(
                format_repository_path(config_path, repository_path_platform)
            )

    active_campaign_payload = {
        "campaign_name": campaign_name,
        "status": "prepared",
        "planning_report_path": format_repository_path(PLANNING_REPORT_RELATIVE_PATH, repository_path_platform),
        "campaign_config_directory": format_repository_path(CAMPAIGN_CONFIG_ROOT, repository_path_platform),
        "queue_root": None,
        "campaign_output_root": "output/training_campaigns",
        "campaign_output_directory": CAMPAIGN_OUTPUT_DIRECTORY_TEMPLATE.format(
            campaign_name=campaign_name,
        ).replace("/", "\\" if repository_path_platform == repository_path_support.WINDOWS_PLATFORM_NAME else "/"),
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
        "remote_conda_environment_name": "pinns_lan_env",
        "queue_config_path_list": queue_config_relative_path_list,
        "protected_file_list": protected_file_relative_path_list,
        "launch_command_list": [
            ".\\scripts\\campaigns\\track1\\exact_paper\\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 -Remote",
            "bash scripts/campaigns/track_1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh --linux",
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
        "interruption_note": (
            "Prepared as the paper-faithful replacement for the superseded "
            "400-run literal-refresh campaign after restoring the historical "
            "GridSearchCV plus cross_validate protocol."
        ),
    }
    save_yaml_file(active_campaign_payload, ACTIVE_CAMPAIGN_STATE_PATH)
    print(f"[DONE] Prepared paper-faithful bidirectional campaign queue count | {len(queue_config_relative_path_list)}", flush=True)
    print(f"[DONE] Active campaign state updated | {ACTIVE_CAMPAIGN_STATE_PATH}", flush=True)


if __name__ == "__main__":

    main()
