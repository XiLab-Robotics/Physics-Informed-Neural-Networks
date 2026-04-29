"""Prepare the overnight mega forward-only last-three-open-cells campaign package for Track 1."""

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
    / "forward_last_three_open_cells_overnight_mega"
)
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
PLANNING_REPORT_RELATIVE_PATH = (
    "doc/reports/campaign_plans/track1/exact_paper/"
    "2026-04-29-17-59-02_track1_forward_last_three_open_cells_overnight_mega_campaign_plan_report.md"
)
LAUNCHER_RELATIVE_PATH = (
    "scripts/campaigns/track1/exact_paper/"
    "run_track1_forward_last_three_open_cells_overnight_mega_campaign.ps1"
)
REMOTE_WRAPPER_RELATIVE_PATH = "scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1"
LOCAL_HELPER_RELATIVE_PATH = "scripts/campaigns/track1/exact_paper/invoke_exact_paper_campaign_local.ps1"
SHARED_LAUNCHER_RELATIVE_PATH = "scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1"
LAUNCHER_NOTE_RELATIVE_PATH = (
    "doc/scripts/campaigns/run_track1_forward_last_three_open_cells_overnight_mega_campaign.md"
)
CAMPAIGN_OUTPUT_DIRECTORY_TEMPLATE = (
    "output/training_campaigns/track1/exact_paper/forward_last_three_open_cells_overnight_mega/{campaign_name}"
)
VALIDATION_OUTPUT_ROOT = (
    "output/validation_checks/"
    "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_three_open_cells_overnight_mega"
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

    """One grouped forward residual target."""

    family_name: str
    target_kind: str
    harmonic_order: int
    severity_label: str
    covered_table_label_list: tuple[str, ...]


COMMON_BASE_ATTEMPT_SPECIFICATION_LIST = [
    AttemptSpecification(0.20, 0.10, 11, "common_base"),
    AttemptSpecification(0.20, 0.10, 13, "common_base"),
    AttemptSpecification(0.20, 0.10, 17, "common_base"),
    AttemptSpecification(0.20, 0.10, 19, "common_base"),
    AttemptSpecification(0.15, 0.15, 23, "common_base"),
    AttemptSpecification(0.15, 0.15, 29, "common_base"),
    AttemptSpecification(0.15, 0.15, 31, "common_base"),
    AttemptSpecification(0.15, 0.15, 37, "common_base"),
    AttemptSpecification(0.25, 0.10, 41, "common_base"),
    AttemptSpecification(0.25, 0.10, 43, "common_base"),
    AttemptSpecification(0.20, 0.15, 47, "common_base"),
    AttemptSpecification(0.20, 0.15, 53, "common_base"),
]
YELLOW_SINGLE_EXTENSION_ATTEMPT_SPECIFICATION_LIST = [
    AttemptSpecification(0.18, 0.12, 59, "yellow_single_extension"),
    AttemptSpecification(0.18, 0.12, 61, "yellow_single_extension"),
    AttemptSpecification(0.22, 0.08, 67, "yellow_single_extension"),
    AttemptSpecification(0.22, 0.08, 71, "yellow_single_extension"),
    AttemptSpecification(0.12, 0.18, 73, "yellow_single_extension"),
    AttemptSpecification(0.12, 0.18, 79, "yellow_single_extension"),
    AttemptSpecification(0.10, 0.20, 83, "yellow_single_extension"),
    AttemptSpecification(0.10, 0.20, 89, "yellow_single_extension"),
    AttemptSpecification(0.24, 0.10, 97, "yellow_single_extension"),
    AttemptSpecification(0.24, 0.10, 101, "yellow_single_extension"),
    AttemptSpecification(0.16, 0.16, 103, "yellow_single_extension"),
    AttemptSpecification(0.16, 0.16, 107, "yellow_single_extension"),
]
DEEP_SINGLE_EXTENSION_ATTEMPT_SPECIFICATION_LIST = [
    AttemptSpecification(0.14, 0.16, 109, "deep_single_extension"),
    AttemptSpecification(0.14, 0.16, 113, "deep_single_extension"),
    AttemptSpecification(0.26, 0.08, 127, "deep_single_extension"),
    AttemptSpecification(0.26, 0.08, 131, "deep_single_extension"),
    AttemptSpecification(0.08, 0.22, 137, "deep_single_extension"),
    AttemptSpecification(0.08, 0.22, 139, "deep_single_extension"),
    AttemptSpecification(0.18, 0.18, 149, "deep_single_extension"),
    AttemptSpecification(0.18, 0.18, 151, "deep_single_extension"),
    AttemptSpecification(0.28, 0.06, 157, "deep_single_extension"),
    AttemptSpecification(0.28, 0.06, 163, "deep_single_extension"),
    AttemptSpecification(0.06, 0.24, 167, "deep_single_extension"),
    AttemptSpecification(0.06, 0.24, 173, "deep_single_extension"),
    AttemptSpecification(0.21, 0.09, 179, "deep_single_extension"),
    AttemptSpecification(0.21, 0.09, 181, "deep_single_extension"),
    AttemptSpecification(0.11, 0.19, 191, "deep_single_extension"),
    AttemptSpecification(0.11, 0.19, 193, "deep_single_extension"),
    AttemptSpecification(0.17, 0.17, 197, "deep_single_extension"),
    AttemptSpecification(0.17, 0.17, 199, "deep_single_extension"),
    AttemptSpecification(0.23, 0.07, 211, "deep_single_extension"),
    AttemptSpecification(0.23, 0.07, 223, "deep_single_extension"),
    AttemptSpecification(0.13, 0.17, 227, "deep_single_extension"),
    AttemptSpecification(0.13, 0.17, 229, "deep_single_extension"),
    AttemptSpecification(0.19, 0.11, 233, "deep_single_extension"),
    AttemptSpecification(0.19, 0.11, 239, "deep_single_extension"),
    AttemptSpecification(0.30, 0.05, 389, "deep_single_extension"),
    AttemptSpecification(0.30, 0.05, 397, "deep_single_extension"),
    AttemptSpecification(0.05, 0.25, 401, "deep_single_extension"),
    AttemptSpecification(0.05, 0.25, 409, "deep_single_extension"),
    AttemptSpecification(0.27, 0.09, 419, "deep_single_extension"),
    AttemptSpecification(0.27, 0.09, 421, "deep_single_extension"),
    AttemptSpecification(0.09, 0.21, 431, "deep_single_extension"),
    AttemptSpecification(0.09, 0.21, 433, "deep_single_extension"),
    AttemptSpecification(0.18, 0.12, 439, "deep_single_extension"),
    AttemptSpecification(0.18, 0.12, 443, "deep_single_extension"),
    AttemptSpecification(0.22, 0.10, 449, "deep_single_extension"),
    AttemptSpecification(0.22, 0.10, 457, "deep_single_extension"),
    AttemptSpecification(0.12, 0.18, 461, "deep_single_extension"),
    AttemptSpecification(0.12, 0.18, 463, "deep_single_extension"),
    AttemptSpecification(0.25, 0.07, 467, "deep_single_extension"),
    AttemptSpecification(0.25, 0.07, 479, "deep_single_extension"),
    AttemptSpecification(0.07, 0.23, 487, "deep_single_extension"),
    AttemptSpecification(0.07, 0.23, 491, "deep_single_extension"),
    AttemptSpecification(0.16, 0.14, 499, "deep_single_extension"),
    AttemptSpecification(0.16, 0.14, 503, "deep_single_extension"),
    AttemptSpecification(0.24, 0.06, 509, "deep_single_extension"),
    AttemptSpecification(0.24, 0.06, 521, "deep_single_extension"),
    AttemptSpecification(0.11, 0.17, 523, "deep_single_extension"),
    AttemptSpecification(0.11, 0.17, 541, "deep_single_extension"),
]
STUBBORN_MAXI_EXTENSION_ATTEMPT_SPECIFICATION_LIST = [
    AttemptSpecification(0.09, 0.21, 241, "stubborn_maxi_extension"),
    AttemptSpecification(0.09, 0.21, 251, "stubborn_maxi_extension"),
    AttemptSpecification(0.27, 0.07, 257, "stubborn_maxi_extension"),
    AttemptSpecification(0.27, 0.07, 263, "stubborn_maxi_extension"),
    AttemptSpecification(0.16, 0.18, 269, "stubborn_maxi_extension"),
    AttemptSpecification(0.16, 0.18, 271, "stubborn_maxi_extension"),
    AttemptSpecification(0.29, 0.05, 277, "stubborn_maxi_extension"),
    AttemptSpecification(0.29, 0.05, 281, "stubborn_maxi_extension"),
    AttemptSpecification(0.07, 0.23, 283, "stubborn_maxi_extension"),
    AttemptSpecification(0.07, 0.23, 293, "stubborn_maxi_extension"),
    AttemptSpecification(0.18, 0.14, 307, "stubborn_maxi_extension"),
    AttemptSpecification(0.18, 0.14, 311, "stubborn_maxi_extension"),
    AttemptSpecification(0.24, 0.08, 313, "stubborn_maxi_extension"),
    AttemptSpecification(0.24, 0.08, 317, "stubborn_maxi_extension"),
    AttemptSpecification(0.12, 0.18, 331, "stubborn_maxi_extension"),
    AttemptSpecification(0.12, 0.18, 337, "stubborn_maxi_extension"),
    AttemptSpecification(0.22, 0.12, 347, "stubborn_maxi_extension"),
    AttemptSpecification(0.22, 0.12, 349, "stubborn_maxi_extension"),
    AttemptSpecification(0.10, 0.20, 353, "stubborn_maxi_extension"),
    AttemptSpecification(0.10, 0.20, 359, "stubborn_maxi_extension"),
    AttemptSpecification(0.20, 0.10, 367, "stubborn_maxi_extension"),
    AttemptSpecification(0.20, 0.10, 373, "stubborn_maxi_extension"),
    AttemptSpecification(0.15, 0.15, 379, "stubborn_maxi_extension"),
    AttemptSpecification(0.15, 0.15, 383, "stubborn_maxi_extension"),
]
FORWARD_RESIDUAL_REPAIR_ITEM_LIST = [
    ForwardResidualRepairItem("ERT", "ampl", 156, "yellow_single_surface_deep", ("Table 2",)),
    ForwardResidualRepairItem("ERT", "ampl", 240, "yellow_single_surface_stubborn_maxi", ("Table 2",)),
    ForwardResidualRepairItem("GBM", "ampl", 162, "yellow_single_surface_deep", ("Table 2",)),
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

    attempt_specification_list = list(COMMON_BASE_ATTEMPT_SPECIFICATION_LIST)
    attempt_specification_list.extend(YELLOW_SINGLE_EXTENSION_ATTEMPT_SPECIFICATION_LIST)
    if repair_item.severity_label == "yellow_single_surface_deep":
        attempt_specification_list.extend(DEEP_SINGLE_EXTENSION_ATTEMPT_SPECIFICATION_LIST)
    if repair_item.severity_label == "yellow_single_surface_stubborn_maxi":
        attempt_specification_list.extend(DEEP_SINGLE_EXTENSION_ATTEMPT_SPECIFICATION_LIST)
        attempt_specification_list.extend(STUBBORN_MAXI_EXTENSION_ATTEMPT_SPECIFICATION_LIST)
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
        f"track1_forward_{family_slug}_{target_slug}_last_three_open_cells_overnight_mega_{attempt_slug}"
    )
    baseline_payload["experiment"]["model_family"] = (
        "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_three_open_cells_overnight_mega"
    )
    baseline_payload["experiment"]["model_type"] = (
        f"exact_model_bank_forward_last_three_open_cells_overnight_mega_{family_slug}_{target_slug}"
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
        f"h{repair_item.harmonic_order}_last_three_open_cells_overnight_mega"
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
        f"{repair_item.target_kind}_h{repair_item.harmonic_order}_last_three_open_cells_overnight_mega_"
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
            f"- severity tier: `{repair_item.severity_label}`",
            f"- covered tables: `{', '.join(repair_item.covered_table_label_list)}`",
            f"- attempt count: `{len(attempt_specification_list)}`",
            f"- split profiles: `{', '.join(unique_profile_label_list)}`",
            "",
        ]
    )


def main() -> None:

    """Prepare the complete overnight mega forward residual campaign package."""

    timestamp_string = datetime.now().astimezone().strftime("%Y-%m-%d_%H_%M_%S")
    campaign_name = f"track1_forward_last_three_open_cells_overnight_mega_campaign_{timestamp_string}"
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
            ".\\scripts\\campaigns\\track1\\exact_paper\\run_track1_forward_last_three_open_cells_overnight_mega_campaign.ps1 -Remote",
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
            "Prepared as the overnight mega residual repair wave "
            "after the failed forward last-three-open-cells closeout."
        ),
    }
    save_yaml_file(active_campaign_payload, ACTIVE_CAMPAIGN_STATE_PATH)
    print(
        f"[DONE] Prepared overnight mega forward residual queue count | "
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
