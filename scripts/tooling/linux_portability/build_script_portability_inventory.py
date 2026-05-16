"""Build the repository script portability inventory."""

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
import argparse
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Repository Paths
REPOSITORY_ROOT = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

# Import Project Utilities
from scripts.tooling import repository_path_support

SCRIPT_ROOT = REPOSITORY_ROOT / "scripts"
DEFAULT_OUTPUT_ROOT = (
    REPOSITORY_ROOT
    / "doc"
    / "reports"
    / "analysis"
    / "linux_script_portability"
)
RUNNABLE_SUFFIX_SET = {".py", ".ps1", ".sh"}
ARGPARSE_MARKER_LIST = ["argparse", "ArgumentParser", "add_argument"]
PLATFORM_MARKER_LIST = [
    "--linux",
    "--windows",
    "repository_path_platform",
    "add_platform_arguments",
]
WINDOWS_SPECIFIC_MARKER_LIST = [
    "powershell",
    "powershell.exe",
    "cmd.exe",
    "where.exe",
    "conda.exe",
    "Resolve-Path",
    "Join-Path",
    "Start-Process",
    "C:\\",
    "C:/",
    ".ps1",
]
REPORT_MARKER_PARTS = ("scripts", "reports")
CAMPAIGN_MARKER_PARTS = ("scripts", "campaigns")


@dataclass(frozen=True)
class ScriptInventoryEntry:

    """One repository script inventory entry."""

    relative_path: str
    suffix: str
    script_domain: str
    script_kind: str
    has_cli_surface: bool
    has_platform_flags: bool
    has_linux_equivalent: bool
    linux_equivalent_path: str | None
    has_windows_specific_markers: bool
    portability_status: str
    note: str


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description="Build a repository-wide Linux script portability inventory."
    )
    argument_parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root directory where the dated inventory bundle is written.",
    )
    argument_parser.add_argument(
        "--bundle-date",
        default=datetime.now().astimezone().strftime("%Y-%m-%d"),
        help="Date folder used under the output root.",
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = build_argument_parser()
    return argument_parser.parse_args()


def read_script_text(script_path: Path) -> str:

    """Read script text with a conservative fallback."""

    try:
        return script_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return script_path.read_text(encoding="utf-8", errors="replace")


def format_repository_path(path_value: Path, platform_name: str) -> str:

    """Format one path relative to the repository root."""

    return repository_path_support.format_repository_relative_path(
        path_value,
        REPOSITORY_ROOT,
        platform_name,
    )


def classify_script_domain(relative_path: Path) -> str:

    """Classify a script into a broad repository domain."""

    part_tuple = tuple(relative_path.parts)
    if part_tuple[:2] == REPORT_MARKER_PARTS:
        return "reports"
    if part_tuple[:2] == CAMPAIGN_MARKER_PARTS:
        return "campaigns"
    if len(part_tuple) >= 2:
        return part_tuple[1]
    return "scripts"


def classify_script_kind(script_path: Path, script_text: str) -> str:

    """Classify the script as runnable, helper, or wrapper."""

    suffix = script_path.suffix.lower()
    if suffix in {".ps1", ".sh"}:
        return "launcher"
    if "if __name__ == \"__main__\"" in script_text:
        return "python_entrypoint"
    if any(marker in script_text for marker in ARGPARSE_MARKER_LIST):
        return "python_cli_like"
    return "python_helper"


def resolve_linux_equivalent(script_path: Path) -> tuple[bool, str | None]:

    """Resolve whether a PowerShell script has a sibling Bash equivalent."""

    if script_path.suffix.lower() != ".ps1":
        return True, None

    sibling_bash_path = script_path.with_suffix(".sh")
    if sibling_bash_path.exists():
        return True, format_repository_path(sibling_bash_path, repository_path_support.LINUX_PLATFORM_NAME)
    return False, None


def resolve_portability_status(
    script_path: Path,
    script_kind: str,
    has_cli_surface: bool,
    has_platform_flags: bool,
    has_linux_equivalent: bool,
    has_windows_specific_markers: bool,
) -> tuple[str, str]:

    """Resolve the current Linux portability status for one script."""

    suffix = script_path.suffix.lower()
    if suffix == ".sh":
        return "linux_launcher_present", "Bash launcher is available."
    if suffix == ".ps1":
        if has_linux_equivalent:
            return "linux_equivalent_present", "PowerShell launcher has a sibling Bash launcher."
        return "missing_linux_equivalent", "PowerShell launcher has no sibling Bash launcher."
    if script_kind == "python_helper":
        if has_windows_specific_markers:
            return "needs_review", "Python helper contains Windows-specific markers."
        return "helper_no_cli", "Python helper has no direct CLI surface."
    if has_cli_surface and not has_platform_flags:
        return "missing_platform_flags", "Python CLI entry point lacks --linux/--windows."
    if has_windows_specific_markers:
        return "platform_flagged", "Python CLI entry point exposes platform flags and contains reviewed Windows markers."
    return "platform_flagged", "Python CLI entry point exposes platform flags."


def build_inventory_entry(script_path: Path, platform_name: str) -> ScriptInventoryEntry:

    """Build one script inventory entry."""

    script_text = read_script_text(script_path)
    relative_path = script_path.relative_to(REPOSITORY_ROOT)
    suffix = script_path.suffix.lower()
    script_domain = classify_script_domain(relative_path)
    script_kind = classify_script_kind(script_path, script_text)
    has_cli_surface = script_kind in {"launcher", "python_entrypoint", "python_cli_like"}
    has_platform_flags = any(marker in script_text for marker in PLATFORM_MARKER_LIST)
    has_windows_specific_markers = any(
        marker.lower() in script_text.lower()
        for marker in WINDOWS_SPECIFIC_MARKER_LIST
    )
    has_linux_equivalent, linux_equivalent_path = resolve_linux_equivalent(script_path)
    portability_status, note = resolve_portability_status(
        script_path=script_path,
        script_kind=script_kind,
        has_cli_surface=has_cli_surface,
        has_platform_flags=has_platform_flags,
        has_linux_equivalent=has_linux_equivalent,
        has_windows_specific_markers=has_windows_specific_markers,
    )

    return ScriptInventoryEntry(
        relative_path=format_repository_path(script_path, platform_name),
        suffix=suffix,
        script_domain=script_domain,
        script_kind=script_kind,
        has_cli_surface=has_cli_surface,
        has_platform_flags=has_platform_flags,
        has_linux_equivalent=has_linux_equivalent,
        linux_equivalent_path=linux_equivalent_path,
        has_windows_specific_markers=has_windows_specific_markers,
        portability_status=portability_status,
        note=note,
    )


def discover_script_paths() -> list[Path]:

    """Discover repository-owned runnable script files."""

    return sorted(
        script_path
        for script_path in SCRIPT_ROOT.rglob("*")
        if script_path.is_file() and script_path.suffix.lower() in RUNNABLE_SUFFIX_SET
    )


def summarize_inventory(entry_list: list[ScriptInventoryEntry]) -> dict[str, Any]:

    """Build aggregate inventory summary counts."""

    summary_dictionary: dict[str, Any] = {
        "script_count": len(entry_list),
        "by_suffix": {},
        "by_domain": {},
        "by_status": {},
        "python_cli_like_count": 0,
        "python_cli_with_platform_flags_count": 0,
        "powershell_count": 0,
        "powershell_missing_linux_equivalent_count": 0,
        "bash_count": 0,
        "report_script_count": 0,
        "report_script_with_platform_flags_count": 0,
    }
    for entry in entry_list:
        summary_dictionary["by_suffix"][entry.suffix] = (
            summary_dictionary["by_suffix"].get(entry.suffix, 0) + 1
        )
        summary_dictionary["by_domain"][entry.script_domain] = (
            summary_dictionary["by_domain"].get(entry.script_domain, 0) + 1
        )
        summary_dictionary["by_status"][entry.portability_status] = (
            summary_dictionary["by_status"].get(entry.portability_status, 0) + 1
        )
        if entry.suffix == ".py" and entry.has_cli_surface:
            summary_dictionary["python_cli_like_count"] += 1
            if entry.has_platform_flags:
                summary_dictionary["python_cli_with_platform_flags_count"] += 1
        if entry.suffix == ".ps1":
            summary_dictionary["powershell_count"] += 1
            if not entry.has_linux_equivalent:
                summary_dictionary["powershell_missing_linux_equivalent_count"] += 1
        if entry.suffix == ".sh":
            summary_dictionary["bash_count"] += 1
        if entry.script_domain == "reports":
            summary_dictionary["report_script_count"] += 1
            if entry.has_platform_flags:
                summary_dictionary["report_script_with_platform_flags_count"] += 1
    return summary_dictionary


def build_markdown_report(
    entry_list: list[ScriptInventoryEntry],
    summary_dictionary: dict[str, Any],
    inventory_yaml_path: Path,
    platform_name: str,
) -> str:

    """Build a Markdown script portability report."""

    row_list = []
    for entry in entry_list:
        row_list.append(
            "| "
            f"`{entry.relative_path}` | "
            f"`{entry.script_domain}` | "
            f"`{entry.script_kind}` | "
            f"`{entry.portability_status}` | "
            f"{'yes' if entry.has_platform_flags else 'no'} | "
            f"{'yes' if entry.has_linux_equivalent else 'no'} | "
            f"{entry.note} |"
        )

    return "\n".join(
        [
            "# Repository Script Linux Portability Inventory",
            "",
            "## Summary",
            "",
            f"- script count: `{summary_dictionary['script_count']}`",
            f"- Python CLI-like scripts: `{summary_dictionary['python_cli_like_count']}`",
            f"- Python CLI-like scripts with platform flags: `{summary_dictionary['python_cli_with_platform_flags_count']}`",
            f"- PowerShell scripts: `{summary_dictionary['powershell_count']}`",
            f"- PowerShell scripts missing Linux equivalents: `{summary_dictionary['powershell_missing_linux_equivalent_count']}`",
            f"- Bash scripts: `{summary_dictionary['bash_count']}`",
            f"- report-domain scripts: `{summary_dictionary['report_script_count']}`",
            f"- report-domain scripts with platform flags: `{summary_dictionary['report_script_with_platform_flags_count']}`",
            f"- inventory YAML: `{format_repository_path(inventory_yaml_path, platform_name)}`",
            "",
            "## Status Counts",
            "",
            "| Status | Count |",
            "| --- | ---: |",
            *[
                f"| `{status_name}` | {status_count} |"
                for status_name, status_count in sorted(summary_dictionary["by_status"].items())
            ],
            "",
            "## Script Inventory",
            "",
            "| Script | Domain | Kind | Status | Platform Flags | Linux Equivalent | Note |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            *row_list,
            "",
        ]
    )


def write_inventory_outputs(
    entry_list: list[ScriptInventoryEntry],
    summary_dictionary: dict[str, Any],
    output_root: Path,
    bundle_date: str,
    platform_name: str,
) -> tuple[Path, Path]:

    """Write inventory YAML and Markdown outputs."""

    bundle_root = output_root / f"[{bundle_date}]"
    bundle_root.mkdir(parents=True, exist_ok=True)
    inventory_yaml_path = bundle_root / "script_portability_inventory.yaml"
    inventory_markdown_path = bundle_root / "script_portability_inventory.md"
    inventory_payload = {
        "schema_version": 1,
        "generated_at": datetime.now().astimezone().isoformat(),
        "platform_format": platform_name,
        "summary": summary_dictionary,
        "scripts": [entry.__dict__ for entry in entry_list],
    }
    inventory_yaml_path.write_text(
        yaml.safe_dump(inventory_payload, sort_keys=False, allow_unicode=False),
        encoding="utf-8",
    )
    inventory_markdown_path.write_text(
        build_markdown_report(
            entry_list=entry_list,
            summary_dictionary=summary_dictionary,
            inventory_yaml_path=inventory_yaml_path,
            platform_name=platform_name,
        ),
        encoding="utf-8",
    )
    return inventory_yaml_path, inventory_markdown_path


def main() -> None:

    """Build and write the script portability inventory."""

    parsed_arguments = parse_command_line_arguments()
    platform_name = repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(parsed_arguments)
    )
    output_root = repository_path_support.resolve_repository_path(
        parsed_arguments.output_root,
        REPOSITORY_ROOT,
        allow_absolute=True,
    )
    entry_list = [
        build_inventory_entry(script_path, platform_name)
        for script_path in discover_script_paths()
    ]
    summary_dictionary = summarize_inventory(entry_list)
    inventory_yaml_path, inventory_markdown_path = write_inventory_outputs(
        entry_list=entry_list,
        summary_dictionary=summary_dictionary,
        output_root=output_root,
        bundle_date=parsed_arguments.bundle_date,
        platform_name=platform_name,
    )
    print(f"[DONE] Inventory YAML | {format_repository_path(inventory_yaml_path, platform_name)}")
    print(f"[DONE] Inventory Markdown | {format_repository_path(inventory_markdown_path, platform_name)}")
    print(f"[DONE] Script count | {summary_dictionary['script_count']}")


if __name__ == "__main__":

    main()
