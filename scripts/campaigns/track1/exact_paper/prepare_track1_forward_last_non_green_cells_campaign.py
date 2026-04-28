"""Prepare the final aggressive forward-only residual campaign package for Track 1."""

from __future__ import annotations

# Import Python Utilities
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[4]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import YAML Utilities
import yaml

CONFIG_ROOT = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "original_dataset_exact_model_bank"
)
BASELINE_CONFIG_PATH = CONFIG_ROOT / "baseline_forward.yaml"
CAMPAIGN_CONFIG_ROOT = (
    CONFIG_ROOT
    / "campaigns"
    / "track1"
    / "exact_paper"
    / "forward_last_non_green_cells"
)
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
PLANNING_REPORT_RELATIVE_PATH = (
    "doc/reports/campaign_plans/track1/exact_paper/"
    "2026-04-28-11-21-25_track1_forward_last_non_green_cells_campaign_plan_report.md"
)
LAUNCHER_RELATIVE_PATH = (
    "scripts/campaigns/track1/exact_paper/"
    "run_track1_forward_last_non_green_cells_campaign.ps1"
)
REMOTE_WRAPPER_RELATIVE_PATH = "scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1"
LOCAL_HELPER_RELATIVE_PATH = "scripts/campaigns/track1/exact_paper/invoke_exact_paper_campaign_local.ps1"
SHARED_LAUNCHER_RELATIVE_PATH = "scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1"
LAUNCHER_NOTE_RELATIVE_PATH = (
    "doc/scripts/campaigns/run_track1_forward_last_non_green_cells_campaign.md"
)
CAMPAIGN_OUTPUT_DIRECTORY_TEMPLATE = (
    "output/training_campaigns/track1/exact_paper/forward_last_non_green_cells/{campaign_name}"
)
VALIDATION_OUTPUT_ROOT = (
    "output/validation_checks/"
    "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_non_green_cells"
)


@dataclass(frozen=True)
class AttemptSpecification:

    """One exact retry specification."""

    validation_split: float
    test_size: float
    random_seed: int
    profile_label: str


@dataclass(frozen=True)
class ForwardResidualRepairItem:

    """One final grouped forward residual target."""

    family_name: str
    target_kind: str
    harmonic_order: int
    severity_label: str
    covered_table_label_list: tuple[str, ...]


BASE_ATTEMPT_SPECIFICATION_LIST = [
    AttemptSpecification(0.20, 0.10, 11, "base_a"),
    AttemptSpecification(0.20, 0.10, 13, "base_a"),
    AttemptSpecification(0.20, 0.10, 17, "base_a"),
    AttemptSpecification(0.20, 0.10, 19, "base_a"),
    AttemptSpecification(0.15, 0.15, 23, "base_b"),
    AttemptSpecification(0.15, 0.15, 29, "base_b"),
    AttemptSpecification(0.15, 0.15, 31, "base_b"),
    AttemptSpecification(0.15, 0.15, 37, "base_b"),
    AttemptSpecification(0.25, 0.10, 41, "base_c"),
    AttemptSpecification(0.25, 0.10, 43, "base_c"),
    AttemptSpecification(0.20, 0.15, 47, "base_c"),
    AttemptSpecification(0.20, 0.15, 53, "base_c"),
]
RED_ESCALATION_ATTEMPT_SPECIFICATION_LIST = [
    AttemptSpecification(0.10, 0.20, 59, "red_escalation"),
    AttemptSpecification(0.10, 0.20, 61, "red_escalation"),
    AttemptSpecification(0.18, 0.12, 67, "red_escalation"),
    AttemptSpecification(0.18, 0.12, 71, "red_escalation"),
    AttemptSpecification(0.22, 0.08, 73, "red_escalation"),
    AttemptSpecification(0.22, 0.08, 79, "red_escalation"),
    AttemptSpecification(0.12, 0.18, 83, "red_escalation"),
    AttemptSpecification(0.12, 0.18, 89, "red_escalation"),
]
FORWARD_RESIDUAL_REPAIR_ITEM_LIST = [
    ForwardResidualRepairItem("ERT", "ampl", 156, "yellow_only", ("Table 2",)),
    ForwardResidualRepairItem("ERT", "ampl", 162, "red_multi_surface", ("Table 2", "Table 3")),
    ForwardResidualRepairItem("ERT", "ampl", 240, "yellow_multi_surface", ("Table 2", "Table 3")),
    ForwardResidualRepairItem("GBM", "ampl", 162, "red_multi_surface", ("Table 2", "Table 3")),
    ForwardResidualRepairItem("LGBM", "ampl", 0, "yellow_only", ("Table 2",)),
    ForwardResidualRepairItem("LGBM", "ampl", 162, "red_multi_surface", ("Table 2", "Table 3")),
    ForwardResidualRepairItem("XGBM", "ampl", 240, "yellow_only", ("Table 2",)),
]


def load_yaml_file(config_path: Path) -> dict:

    """Load one YAML file."""

    with config_path.open("r", encoding="utf-8") as input_file:
        return yaml.safe_load(input_file)


def save_yaml_file(payload: dict, output_path: Path) -> None:

    """Persist one YAML payload."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False)


def build_target_scope_dictionary(repair_item: ForwardResidualRepairItem) -> dict:

    """Build the exact target-scope payload for one repair item."""

    return {
        "mode": "amplitudes_only",
        "include_phase_zero": False,
        "harmonic_order_filter": [int(repair_item.harmonic_order)],
    }


def build_attempt_specification_list(
    repair_item: ForwardResidualRepairItem,
) -> list[AttemptSpecification]:

    """Build the exact retry list for one residual repair item."""

    attempt_specification_list = list(BASE_ATTEMPT_SPECIFICATION_LIST)
    if "red" in repair_item.severity_label:
        attempt_specification_list.extend(RED_ESCALATION_ATTEMPT_SPECIFICATION_LIST)
    return attempt_specification_list


def build_campaign_config(
    repair_item: ForwardResidualRepairItem,
    attempt_index: int,
    attempt_specification: AttemptSpecification,
) -> dict:

    """Build one residual repair config payload."""

    baseline_payload = load_yaml_file(BASELINE_CONFIG_PATH)
    family_slug = repair_item.family_name.lower()
    target_slug = f"{repair_item.target_kind}_h{repair_item.harmonic_order}"
    attempt_slug = f"attempt_{attempt_index:02d}"

    baseline_payload["paths"]["output_root"] = VALIDATION_OUTPUT_ROOT
    baseline_payload["experiment"]["run_name"] = (
        f"track1_forward_{family_slug}_{target_slug}_last_non_green_cells_{attempt_slug}"
    )
    baseline_payload["experiment"]["model_family"] = (
        "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_non_green_cells"
    )
    baseline_payload["experiment"]["model_type"] = (
        f"exact_model_bank_forward_last_non_green_cells_{family_slug}_{target_slug}"
    )
    baseline_payload["training"]["enabled_families"] = [repair_item.family_name]
    baseline_payload["training"]["validation_split"] = float(attempt_specification.validation_split)
    baseline_payload["training"]["test_size"] = float(attempt_specification.test_size)
    baseline_payload["training"]["random_seed"] = int(attempt_specification.random_seed)
    baseline_payload["target_scope"] = build_target_scope_dictionary(repair_item)
    baseline_payload["training"]["grid_search_disabled_families"] = []
    baseline_payload.pop("smoke", None)
    return baseline_payload


def build_campaign_directory_slug(repair_item: ForwardResidualRepairItem) -> str:

    """Build the per-item campaign directory slug."""

    return (
        f"{datetime.now().strftime('%Y-%m-%d')}_track1_forward_"
        f"{repair_item.family_name.lower()}_{repair_item.target_kind}_"
        f"h{repair_item.harmonic_order}_last_non_green_cells"
    )


def build_campaign_config_path(
    repair_item: ForwardResidualRepairItem,
    campaign_slug: str,
    attempt_index: int,
) -> Path:

    """Build one residual repair config path."""

    campaign_directory = CAMPAIGN_CONFIG_ROOT / repair_item.family_name.lower() / campaign_slug
    filename = (
        f"{attempt_index:03d}_track1_forward_{repair_item.family_name.lower()}_"
        f"{repair_item.target_kind}_h{repair_item.harmonic_order}_last_non_green_cells_"
        f"attempt_{attempt_index:02d}.yaml"
    )
    return campaign_directory / filename


def build_campaign_readme_markdown(
    campaign_slug: str,
    repair_item: ForwardResidualRepairItem,
    attempt_specification_list: list[AttemptSpecification],
) -> str:

    """Build one repair-directory README."""

    unique_profile_label_list = sorted(
        {attempt_specification.profile_label for attempt_specification in attempt_specification_list}
    )
    return "\n".join(
        [
            f"# {campaign_slug}",
            "",
            "- direction: `forward`",
            f"- family: `{repair_item.family_name}`",
            f"- target kind: `{repair_item.target_kind}`",
            f"- harmonic order: `{repair_item.harmonic_order}`",
            f"- severity: `{repair_item.severity_label}`",
            f"- covered tables: `{', '.join(repair_item.covered_table_label_list)}`",
            f"- attempt count: `{len(attempt_specification_list)}`",
            f"- split profiles: `{', '.join(unique_profile_label_list)}`",
            "",
        ]
    )


def main() -> None:

    """Prepare the complete final aggressive forward residual campaign package."""

    timestamp_string = datetime.now().astimezone().strftime("%Y-%m-%d_%H_%M_%S")
    campaign_name = f"track1_forward_last_non_green_cells_campaign_{timestamp_string}"
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

    unique_family_list = sorted({repair_item.family_name for repair_item in FORWARD_RESIDUAL_REPAIR_ITEM_LIST})

    for repair_item in FORWARD_RESIDUAL_REPAIR_ITEM_LIST:
        campaign_slug = build_campaign_directory_slug(repair_item)
        campaign_directory = CAMPAIGN_CONFIG_ROOT / repair_item.family_name.lower() / campaign_slug
        campaign_directory.mkdir(parents=True, exist_ok=True)
        attempt_specification_list = build_attempt_specification_list(repair_item)
        readme_path = campaign_directory / "README.md"
        readme_path.write_text(
            build_campaign_readme_markdown(
                campaign_slug,
                repair_item,
                attempt_specification_list,
            ),
            encoding="utf-8",
        )
        protected_file_relative_path_list.append(
            str(readme_path.relative_to(PROJECT_PATH)).replace("/", "\\")
        )

        for attempt_index, attempt_specification in enumerate(attempt_specification_list, start=1):
            config_path = build_campaign_config_path(
                repair_item,
                campaign_slug,
                attempt_index,
            )
            save_yaml_file(
                build_campaign_config(repair_item, attempt_index, attempt_specification),
                config_path,
            )
            queue_config_relative_path_list.append(
                str(config_path.relative_to(PROJECT_PATH)).replace("/", "\\")
            )

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
            ".\\scripts\\campaigns\\track1\\exact_paper\\run_track1_forward_last_non_green_cells_campaign.ps1 -Remote",
        ],
        "remote_bootstrap_contract": {
            "queue_bundle_transport": "temporary_python_script_with_json_safe_path_literals",
            "remote_preflight_transport": "temporary_python_script_with_conda_run",
            "remote_progress_surface": {
                "queue_progress_markers": "remote_active_config_and_remote_completed_config",
                "console_noise_policy": "suppress_raw_gridsearch_cv_lines_from_operator_terminal",
            },
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
        "pending_family_list": unique_family_list,
        "interruption_note": (
            "Prepared as the final aggressive forward-only residual repair wave "
            "after the completed forward final-open-cells closeout."
        ),
    }
    save_yaml_file(active_campaign_payload, ACTIVE_CAMPAIGN_STATE_PATH)
    print(
        f"[DONE] Prepared final aggressive forward residual queue count | "
        f"{len(queue_config_relative_path_list)}",
        flush=True,
    )
    print(
        f"[DONE] Unique grouped residual repair items | "
        f"{len(FORWARD_RESIDUAL_REPAIR_ITEM_LIST)}",
        flush=True,
    )
    print(f"[DONE] Active campaign state updated | {ACTIVE_CAMPAIGN_STATE_PATH}", flush=True)


if __name__ == "__main__":

    main()
