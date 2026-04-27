"""Prepare the forward-only Track 1 open-cell repair campaign package."""

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
    / "forward_open_cell_repair"
)
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
PLANNING_REPORT_RELATIVE_PATH = (
    "doc/reports/campaign_plans/track1/exact_paper/"
    "2026-04-27-13-00-21_track1_forward_open_cell_repair_campaign_plan_report.md"
)
LAUNCHER_RELATIVE_PATH = (
    "scripts/campaigns/track1/exact_paper/"
    "run_track1_forward_open_cell_repair_campaign.ps1"
)
REMOTE_WRAPPER_RELATIVE_PATH = "scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1"
LOCAL_HELPER_RELATIVE_PATH = "scripts/campaigns/track1/exact_paper/invoke_exact_paper_campaign_local.ps1"
SHARED_LAUNCHER_RELATIVE_PATH = "scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1"
LAUNCHER_NOTE_RELATIVE_PATH = (
    "doc/scripts/campaigns/run_track1_forward_open_cell_repair_campaign.md"
)
CAMPAIGN_OUTPUT_DIRECTORY_TEMPLATE = (
    "output/training_campaigns/track1/exact_paper/forward_open_cell_repair/{campaign_name}"
)
VALIDATION_OUTPUT_ROOT = (
    "output/validation_checks/"
    "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair"
)
ATTEMPT_SEED_LIST = [0, 5, 7, 9, 11, 13, 15, 17, 19, 21]


@dataclass(frozen=True)
class ForwardRepairItem:

    """One grouped forward repair target."""

    family_name: str
    target_kind: str
    harmonic_order: int
    covered_table_label_list: tuple[str, ...]


FORWARD_REPAIR_ITEM_LIST = [
    ForwardRepairItem("ERT", "ampl", 156, ("Table 2",)),
    ForwardRepairItem("ERT", "ampl", 162, ("Table 2",)),
    ForwardRepairItem("ERT", "ampl", 240, ("Table 2", "Table 3")),
    ForwardRepairItem("GBM", "ampl", 3, ("Table 2", "Table 3")),
    ForwardRepairItem("GBM", "ampl", 39, ("Table 2", "Table 3")),
    ForwardRepairItem("GBM", "ampl", 78, ("Table 2", "Table 3")),
    ForwardRepairItem("GBM", "ampl", 156, ("Table 2",)),
    ForwardRepairItem("GBM", "ampl", 162, ("Table 2", "Table 3")),
    ForwardRepairItem("GBM", "ampl", 240, ("Table 2", "Table 3")),
    ForwardRepairItem("HGBM", "ampl", 0, ("Table 3",)),
    ForwardRepairItem("LGBM", "ampl", 0, ("Table 2", "Table 3")),
    ForwardRepairItem("LGBM", "ampl", 3, ("Table 2", "Table 3")),
    ForwardRepairItem("LGBM", "ampl", 39, ("Table 2", "Table 3")),
    ForwardRepairItem("LGBM", "ampl", 40, ("Table 2", "Table 3")),
    ForwardRepairItem("LGBM", "ampl", 78, ("Table 2", "Table 3")),
    ForwardRepairItem("LGBM", "ampl", 81, ("Table 2", "Table 3")),
    ForwardRepairItem("LGBM", "ampl", 156, ("Table 2", "Table 3")),
    ForwardRepairItem("LGBM", "ampl", 162, ("Table 2", "Table 3")),
    ForwardRepairItem("LGBM", "ampl", 240, ("Table 2", "Table 3")),
    ForwardRepairItem("SVM", "ampl", 40, ("Table 3",)),
    ForwardRepairItem("XGBM", "ampl", 240, ("Table 3",)),
    ForwardRepairItem("GBM", "phase", 81, ("Table 4", "Table 5")),
    ForwardRepairItem("LGBM", "phase", 1, ("Table 5",)),
    ForwardRepairItem("LGBM", "phase", 3, ("Table 4", "Table 5")),
    ForwardRepairItem("LGBM", "phase", 39, ("Table 4", "Table 5")),
    ForwardRepairItem("LGBM", "phase", 40, ("Table 4", "Table 5")),
    ForwardRepairItem("LGBM", "phase", 78, ("Table 4", "Table 5")),
    ForwardRepairItem("LGBM", "phase", 81, ("Table 4", "Table 5")),
    ForwardRepairItem("LGBM", "phase", 156, ("Table 4", "Table 5")),
    ForwardRepairItem("LGBM", "phase", 162, ("Table 4", "Table 5")),
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


def build_target_scope_dictionary(repair_item: ForwardRepairItem) -> dict:

    """Build the exact target-scope payload for one repair item."""

    return {
        "mode": "amplitudes_only" if repair_item.target_kind == "ampl" else "phases_only",
        "include_phase_zero": False,
        "harmonic_order_filter": [int(repair_item.harmonic_order)],
    }


def build_campaign_config(
    repair_item: ForwardRepairItem,
    attempt_index: int,
    split_seed: int,
) -> dict:

    """Build one repair config payload."""

    baseline_payload = load_yaml_file(BASELINE_CONFIG_PATH)
    family_slug = repair_item.family_name.lower()
    target_slug = f"{repair_item.target_kind}_h{repair_item.harmonic_order}"
    attempt_slug = f"attempt_{attempt_index:02d}"

    baseline_payload["paths"]["output_root"] = VALIDATION_OUTPUT_ROOT
    baseline_payload["experiment"]["run_name"] = (
        f"track1_forward_{family_slug}_{target_slug}_open_cell_repair_{attempt_slug}"
    )
    baseline_payload["experiment"]["model_family"] = (
        "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair"
    )
    baseline_payload["experiment"]["model_type"] = (
        f"exact_model_bank_forward_open_cell_repair_{family_slug}_{target_slug}"
    )
    baseline_payload["training"]["enabled_families"] = [repair_item.family_name]
    baseline_payload["training"]["random_seed"] = int(split_seed)
    baseline_payload["target_scope"] = build_target_scope_dictionary(repair_item)
    if repair_item.family_name == "SVR":
        baseline_payload["training"]["grid_search_disabled_families"] = ["SVR"]
    else:
        baseline_payload["training"]["grid_search_disabled_families"] = []
    baseline_payload.pop("smoke", None)
    return baseline_payload


def build_campaign_directory_slug(repair_item: ForwardRepairItem) -> str:

    """Build the per-item campaign directory slug."""

    return (
        f"{datetime.now().strftime('%Y-%m-%d')}_track1_forward_"
        f"{repair_item.family_name.lower()}_{repair_item.target_kind}_"
        f"h{repair_item.harmonic_order}_open_cell_repair"
    )


def build_campaign_config_path(
    repair_item: ForwardRepairItem,
    campaign_slug: str,
    attempt_index: int,
) -> Path:

    """Build one repair config path."""

    campaign_directory = CAMPAIGN_CONFIG_ROOT / repair_item.family_name.lower() / campaign_slug
    filename = (
        f"{attempt_index:03d}_track1_forward_{repair_item.family_name.lower()}_"
        f"{repair_item.target_kind}_h{repair_item.harmonic_order}_open_cell_repair_"
        f"attempt_{attempt_index:02d}.yaml"
    )
    return campaign_directory / filename


def build_campaign_readme_markdown(
    campaign_slug: str,
    repair_item: ForwardRepairItem,
) -> str:

    """Build one repair-directory README."""

    return "\n".join(
        [
            f"# {campaign_slug}",
            "",
            "- direction: `forward`",
            f"- family: `{repair_item.family_name}`",
            f"- target kind: `{repair_item.target_kind}`",
            f"- harmonic order: `{repair_item.harmonic_order}`",
            f"- covered tables: `{', '.join(repair_item.covered_table_label_list)}`",
            f"- attempt count: `{len(ATTEMPT_SEED_LIST)}`",
            f"- split seeds: `{', '.join(str(value) for value in ATTEMPT_SEED_LIST)}`",
            "",
        ]
    )


def main() -> None:

    """Prepare the complete forward open-cell repair campaign package."""

    timestamp_string = datetime.now().astimezone().strftime("%Y-%m-%d_%H_%M_%S")
    campaign_name = f"track1_forward_open_cell_repair_campaign_{timestamp_string}"
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

    unique_family_list = sorted({repair_item.family_name for repair_item in FORWARD_REPAIR_ITEM_LIST})

    for repair_item in FORWARD_REPAIR_ITEM_LIST:
        campaign_slug = build_campaign_directory_slug(repair_item)
        campaign_directory = CAMPAIGN_CONFIG_ROOT / repair_item.family_name.lower() / campaign_slug
        campaign_directory.mkdir(parents=True, exist_ok=True)
        readme_path = campaign_directory / "README.md"
        readme_path.write_text(
            build_campaign_readme_markdown(campaign_slug, repair_item),
            encoding="utf-8",
        )
        protected_file_relative_path_list.append(
            str(readme_path.relative_to(PROJECT_PATH)).replace("/", "\\")
        )

        for attempt_index, split_seed in enumerate(ATTEMPT_SEED_LIST, start=1):
            config_path = build_campaign_config_path(
                repair_item,
                campaign_slug,
                attempt_index,
            )
            save_yaml_file(
                build_campaign_config(repair_item, attempt_index, split_seed),
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
            ".\\scripts\\campaigns\\track1\\exact_paper\\run_track1_forward_open_cell_repair_campaign.ps1 -Remote",
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
            "Prepared as a forward-only residual repair wave after the completed "
            "bidirectional original-dataset mega campaign closeout."
        ),
    }
    save_yaml_file(active_campaign_payload, ACTIVE_CAMPAIGN_STATE_PATH)
    print(
        f"[DONE] Prepared forward open-cell repair queue count | "
        f"{len(queue_config_relative_path_list)}",
        flush=True,
    )
    print(f"[DONE] Unique grouped repair items | {len(FORWARD_REPAIR_ITEM_LIST)}", flush=True)
    print(f"[DONE] Active campaign state updated | {ACTIVE_CAMPAIGN_STATE_PATH}", flush=True)


if __name__ == "__main__":

    main()
