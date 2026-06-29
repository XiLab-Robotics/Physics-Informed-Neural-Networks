"""Report Repository Workflow Gate Signals For Codex Tasks."""

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
import argparse
import subprocess
from pathlib import Path

# Repository Paths
REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
ACTIVE_CAMPAIGN_STATE_PATH = REPOSITORY_ROOT / "doc" / "running" / "active_training_campaign.yaml"
TECHNICAL_ROOT = REPOSITORY_ROOT / "doc" / "technical"


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Print a non-blocking report of StandardML workflow gates based on "
            "current Git changes and active campaign state."
        ),
    )
    argument_parser.add_argument(
        "--changed-path",
        action="append",
        default=[],
        help="Path to include in the gate report. Defaults to Git changed paths.",
    )

    return argument_parser


def run_git_changed_path_list() -> list[str]:

    """Return changed paths from Git status."""

    git_command = ["git", "status", "--short"]
    completed_process = subprocess.run(
        git_command,
        cwd=REPOSITORY_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

    changed_path_list: list[str] = []
    for status_line in completed_process.stdout.splitlines():
        if not status_line.strip():
            continue

        path_fragment = status_line[3:].strip()
        if " -> " in path_fragment:
            path_fragment = path_fragment.split(" -> ", maxsplit=1)[1].strip()
        changed_path_list.append(path_fragment)

    return changed_path_list


def read_active_campaign_state_text() -> str:

    """Read the active campaign state file."""

    if not ACTIVE_CAMPAIGN_STATE_PATH.exists():
        return ""

    return ACTIVE_CAMPAIGN_STATE_PATH.read_text(encoding="utf-8")


def extract_scalar_value(yaml_text: str, key: str) -> str:

    """Extract a simple top-level scalar from repository YAML text."""

    key_prefix = f"{key}:"
    for line in yaml_text.splitlines():
        if not line.startswith(key_prefix):
            continue

        return line.split(":", maxsplit=1)[1].strip()

    return ""


def extract_list_value(yaml_text: str, key: str) -> list[str]:

    """Extract a simple YAML list from repository active-state text."""

    extracted_value_list: list[str] = []
    line_list = yaml_text.splitlines()
    list_header = f"{key}:"

    for line_index, line in enumerate(line_list):
        if not line.startswith(list_header):
            continue

        inline_value = line.split(":", maxsplit=1)[1].strip()
        if inline_value == "[]":
            return []

        for item_line in line_list[line_index + 1:]:
            if item_line and not item_line.startswith(" "):
                break

            stripped_item_line = item_line.strip()
            if not stripped_item_line.startswith("- "):
                continue

            extracted_value_list.append(stripped_item_line[2:].strip().strip("'\""))

        return extracted_value_list

    return []


def normalize_path(path_text: str) -> str:

    """Normalize repository path text for prefix comparisons."""

    return path_text.replace("\\", "/").strip("/")


def path_matches_prefix(path_text: str, prefix_text: str) -> bool:

    """Return whether path text is equal to or below a prefix."""

    normalized_path = normalize_path(path_text)
    normalized_prefix = normalize_path(prefix_text)

    return normalized_path == normalized_prefix or normalized_path.startswith(f"{normalized_prefix}/")


def find_latest_technical_document() -> Path | None:

    """Find the latest technical document by timestamped filename."""

    if not TECHNICAL_ROOT.exists():
        return None

    technical_document_list = sorted(
        path for path in TECHNICAL_ROOT.rglob("*.md")
        if path.name != "README.md"
    )
    if not technical_document_list:
        return None

    return technical_document_list[-1]


def classify_gate_list(changed_path_list: list[str]) -> list[str]:

    """Classify likely workflow gates from changed paths."""

    gate_list: list[str] = []

    if any(path.endswith(".md") for path in changed_path_list):
        gate_list.append("Markdown QA required for touched authored Markdown.")

    if any(path.endswith(".py") for path in changed_path_list):
        gate_list.append("Python syntax or stronger task-specific validation required.")

    if any(path_matches_prefix(path, "site") for path in changed_path_list):
        gate_list.append("Sphinx portal build likely required.")

    campaign_prefix_list = [
        "config",
        "scripts/campaigns",
        "scripts/training",
        "scripts/models",
        "doc/running",
        "doc/reports/campaign_plans",
        "doc/reports/campaign_results",
        "output/registries",
    ]
    if any(
        path_matches_prefix(path, campaign_prefix)
        for path in changed_path_list
        for campaign_prefix in campaign_prefix_list
    ):
        gate_list.append("Active campaign state and protected-file review required.")

    if any(path_matches_prefix(path, "doc/reports/campaign_results") for path in changed_path_list):
        gate_list.append("Campaign-result PDF export and real PDF validation may be required.")

    if any(path_matches_prefix(path, ".codex") for path in changed_path_list):
        gate_list.append("Codex workflow guide or skill/subagent documentation update may be required.")

    return gate_list


def print_report(changed_path_list: list[str]) -> None:

    """Print the workflow preflight report."""

    active_campaign_state_text = read_active_campaign_state_text()
    active_campaign_status = extract_scalar_value(active_campaign_state_text, "status") or "unknown"
    protected_file_list = extract_list_value(active_campaign_state_text, "protected_file_list")
    latest_technical_document = find_latest_technical_document()

    protected_overlap_list = [
        path for path in changed_path_list
        for protected_path in protected_file_list
        if path_matches_prefix(path, protected_path)
    ]
    gate_list = classify_gate_list(changed_path_list)

    print("")
    print("================================================================================================")
    print("StandardML Workflow Gate Preflight Report")
    print("================================================================================================")
    print(f"Changed Path Count                {len(changed_path_list)}")
    print(f"Active Campaign Status            {active_campaign_status}")
    print(f"Protected File Count              {len(protected_file_list)}")
    print(f"Protected Overlap Count           {len(protected_overlap_list)}")
    if latest_technical_document is not None:
        print(f"Latest Technical Document         {latest_technical_document.relative_to(REPOSITORY_ROOT)}")
    else:
        print("Latest Technical Document         none")

    print("")
    print("Gate Signals")
    if gate_list:
        for gate_item in gate_list:
            print(f"- {gate_item}")
    else:
        print("- No path-derived gate signals detected.")

    print("")
    print("Protected Overlaps")
    if protected_overlap_list:
        for protected_overlap in sorted(set(protected_overlap_list)):
            print(f"- {protected_overlap}")
    else:
        print("- None detected.")

    print("")
    print("[INFO] This script is report-only. Read the referenced files before acting.")


def main() -> None:

    """Run the workflow preflight report."""

    argument_parser = build_argument_parser()
    parsed_arguments = argument_parser.parse_args()

    if parsed_arguments.changed_path:
        changed_path_list = parsed_arguments.changed_path
    else:
        changed_path_list = run_git_changed_path_list()

    print_report(changed_path_list)


if __name__ == "__main__":

    main()
