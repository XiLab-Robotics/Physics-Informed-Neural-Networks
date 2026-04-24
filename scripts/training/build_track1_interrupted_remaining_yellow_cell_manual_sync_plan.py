"""Build the manual sync checklist for the interrupted Track 1 yellow-cell wave."""

from __future__ import annotations

# Import Python Utilities
import argparse
import sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import YAML Utilities
import yaml


DEFAULT_ACTIVE_CAMPAIGN_PATH = Path("doc/running/active_training_campaign.yaml")
DEFAULT_OUTPUT_PATH = Path("doc/running/track1_interrupted_remaining_yellow_cell_manual_sync_checklist.md")
DEFAULT_WRAPPER_LOG_GLOB_LIST = [
    ".temp/remote_training_campaigns/*track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43*/remote_training_campaign.log",
]


def parse_command_line_arguments() -> argparse.Namespace:
    """Parse command-line arguments for the manual sync helper."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Build the manual sync checklist for the interrupted Track 1 "
            "remaining-yellow-cell campaign."
        )
    )
    argument_parser.add_argument(
        "--active-campaign-path",
        type=Path,
        default=DEFAULT_ACTIVE_CAMPAIGN_PATH,
        help="Path to the canonical active training campaign YAML file.",
    )
    argument_parser.add_argument(
        "--output-path",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path to the Markdown checklist to generate.",
    )
    return argument_parser.parse_args()


def load_yaml_file(yaml_path: Path) -> dict:
    """Load one YAML file as a dictionary."""

    resolved_yaml_path = yaml_path.resolve()
    assert resolved_yaml_path.exists(), f"YAML path does not exist | {resolved_yaml_path}"

    with resolved_yaml_path.open("r", encoding="utf-8") as yaml_file:
        loaded_payload = yaml.safe_load(yaml_file)

    assert isinstance(loaded_payload, dict), f"YAML payload must be a dictionary | {resolved_yaml_path}"
    return loaded_payload


def normalize_relative_path(path_text: str) -> str:
    """Normalize one repository-relative path to POSIX style."""

    return Path(str(path_text).replace("\\", "/")).as_posix()


def collect_matching_relative_path_list(glob_pattern_list: list[str]) -> list[str]:
    """Collect sorted repository-relative paths for the requested glob patterns."""

    matching_path_set: set[str] = set()

    for glob_pattern in glob_pattern_list:
        for matching_path in PROJECT_PATH.glob(glob_pattern):
            matching_path_set.add(matching_path.resolve().relative_to(PROJECT_PATH).as_posix())

    return sorted(matching_path_set)


def build_checklist_text(active_campaign_dictionary: dict) -> str:
    """Build the Markdown checklist text for the interrupted manual sync."""

    campaign_name = str(active_campaign_dictionary.get("campaign_name", "")).strip()
    assert campaign_name == "track1_remaining_yellow_cell_campaigns_2026_04_22_01_40_43", (
        "Unexpected active campaign for the interrupted Track 1 yellow-cell manual sync helper | "
        f"campaign_name={campaign_name}"
    )

    remote_repository_path = str(active_campaign_dictionary.get("remote_repository_path", "")).strip()
    remote_host_alias = str(active_campaign_dictionary.get("remote_host_alias", "")).strip()
    remote_conda_environment_name = str(active_campaign_dictionary.get("remote_conda_environment_name", "")).strip()
    campaign_status = str(active_campaign_dictionary.get("status", "")).strip()
    started_at = str(active_campaign_dictionary.get("started_at", "")).strip()

    wrapper_log_relative_path_list = collect_matching_relative_path_list(DEFAULT_WRAPPER_LOG_GLOB_LIST)

    queue_config_path_list = [
        normalize_relative_path(path_text)
        for path_text in active_campaign_dictionary.get("queue_config_path_list", [])
        if "track1_svm_remaining_yellow_cell_campaign" in str(path_text)
    ]

    remote_relative_copy_target_list = [
        "output/training_campaigns/track1/exact_paper/track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43",
        "output/validation_checks/paper_reimplementation_rcim_exact_model_bank/*__track1_svm_*_yellow_cell_attempt_*_campaign_run",
        "doc/reports/analysis/validation_checks/*_track1_svm_*_yellow_cell_attempt_*_campaign_run_exact_paper_model_bank_report.md",
    ]

    campaign_output_directory = PROJECT_PATH / "output/training_campaigns/track1/exact_paper/track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43"
    local_validation_directory_list = list(
        (PROJECT_PATH / "output/validation_checks/paper_reimplementation_rcim_exact_model_bank").glob(
            "*__track1_svm_*_yellow_cell_attempt_*_campaign_run"
        )
    )
    local_report_path_list = list(
        (PROJECT_PATH / "doc/reports/analysis/validation_checks").glob(
            "*_track1_svm_*_yellow_cell_attempt_*_campaign_run_exact_paper_model_bank_report.md"
        )
    )

    line_list: list[str] = [
        "# Track 1 Interrupted Remaining Yellow-Cell Manual Sync Checklist",
        "",
        "## Campaign Snapshot",
        "",
        f"- Campaign name: `{campaign_name}`",
        f"- Canonical local status before closeout: `{campaign_status}`",
        f"- Local start timestamp: `{started_at}`",
        f"- Remote host alias: `{remote_host_alias}`",
        f"- Remote repository path: `{remote_repository_path}`",
        f"- Remote Conda environment: `{remote_conda_environment_name}`",
        "- Scope for this manual sync: `SVM` only",
        "- Closeout gate: do not update the canonical campaign state, benchmark, or forward-only asset-root migration until the artifact copy below has completed",
        "",
        "## Current Local Evidence",
        "",
        f"- Local SVM campaign output directory present: `{campaign_output_directory.exists()}`",
        f"- Local SVM validation directory count: `{len(local_validation_directory_list)}`",
        f"- Local SVM validation report count: `{len(local_report_path_list)}`",
        "- Interpretation: the interrupted remote wave has not yet been synchronized back into the local repository",
        "",
        "## Local Wrapper Logs To Preserve",
        "",
    ]

    if wrapper_log_relative_path_list:
        for wrapper_log_relative_path in wrapper_log_relative_path_list:
            line_list.append(f"- `{wrapper_log_relative_path}`")
    else:
        line_list.append("- `no_matching_local_wrapper_logs_found`")

    line_list += [
        "",
        "## Remote Copy Targets",
        "",
        "- Copy the full remote SVM campaign output directory first so the run logs, launcher-level bookkeeping, and any partial manifest fragments are preserved together.",
        "- Then copy every exact-paper validation directory created by the interrupted SVM yellow-cell wave.",
        "- Then copy every per-run exact-paper analysis report tied to those validation directories.",
        "",
    ]

    for remote_relative_copy_target in remote_relative_copy_target_list:
        line_list.append(f"- `{remote_relative_copy_target}`")

    line_list += [
        "",
        "## Remote Copy Notes",
        "",
        "- The validation directory pattern is intentionally glob-based because the local wrapper log stopped before the remote workstation finished its long autonomous execution.",
        "- The report pattern is also glob-based because the per-run report filenames include remote timestamps that are unknown locally until the files are copied.",
        "- If the remote campaign output directory contains `campaign_manifest.yaml`, keep it with the rest of the campaign directory even if the wrapper never emitted a final sync marker.",
        "- Do not attempt benchmark refresh or artifact pruning during the copy step.",
        "",
        "## Family Queue Scope",
        "",
        f"- Config count expected for the interrupted `SVM` family wave: `{len(queue_config_path_list)}`",
        "- Queue family branches not to copy now: `MLP`, `ET`, `ERT`, `HGBM`, `XGBM`",
        "",
        "## Immediate Post-Sync Local Verification",
        "",
        "```powershell",
        "Get-ChildItem -LiteralPath 'output\\validation_checks\\paper_reimplementation_rcim_exact_model_bank' -Directory |",
        "  Where-Object { $_.Name -like '*__track1_svm_*_yellow_cell_attempt_*_campaign_run' } |",
        "  Sort-Object Name |",
        "  Select-Object Name, LastWriteTime",
        "```",
        "",
        "```powershell",
        "Get-ChildItem -LiteralPath 'doc\\reports\\analysis\\validation_checks' -File |",
        "  Where-Object { $_.Name -like '*_track1_svm_*_yellow_cell_attempt_*_campaign_run_exact_paper_model_bank_report.md' } |",
        "  Sort-Object Name |",
        "  Select-Object Name, LastWriteTime",
        "```",
        "",
        "```powershell",
        "Get-ChildItem -LiteralPath 'output\\training_campaigns\\track1\\exact_paper\\track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43\\logs' -File |",
        "  Sort-Object Name |",
        "  Select-Object -Last 20 Name, LastWriteTime, Length",
        "```",
        "",
        "```powershell",
        "Get-ChildItem -LiteralPath 'output\\validation_checks\\paper_reimplementation_rcim_exact_model_bank' -Directory |",
        "  Where-Object { $_.Name -like '*__track1_svm_*_yellow_cell_attempt_*_campaign_run' } |",
        "  Group-Object { $_.Name -replace '^[0-9-]+__', '' } |",
        "  Where-Object { $_.Count -gt 1 } |",
        "  Select-Object Name, Count",
        "```",
        "",
        "## Next Step After Successful Manual Sync",
        "",
        "- Run the interrupted-campaign partial closeout from the newly synchronized local artifact set.",
        "- Only after that closeout is completed should the workflow continue with `2026-04-23-23-15-55_post_closeout_forward_asset_root_migration_workflow.md`.",
        "",
    ]

    return "\n".join(line_list)


def main() -> int:
    """Run the manual sync checklist builder."""

    command_line_arguments = parse_command_line_arguments()
    active_campaign_path = (PROJECT_PATH / command_line_arguments.active_campaign_path).resolve()
    output_path = (PROJECT_PATH / command_line_arguments.output_path).resolve()

    active_campaign_dictionary = load_yaml_file(active_campaign_path)
    output_text = build_checklist_text(active_campaign_dictionary).rstrip() + "\n"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_text, encoding="utf-8")
    print(output_path.relative_to(PROJECT_PATH).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
