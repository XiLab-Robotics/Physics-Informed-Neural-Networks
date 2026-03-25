""" Check Repository Markdown Style Warnings """

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
import argparse
from dataclasses import dataclass
from pathlib import Path

# Markdown Check Constants
REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INCLUDED_PATHS = [
    "README.md",
    "AGENTS.md",
    "config",
    "models",
    "doc",
    "site",
]
DEFAULT_EXCLUDED_ROOT_NAMES = {
    ".git",
    ".temp",
    ".tools",
    ".vs",
    "isolated",
    "output",
}
DEFAULT_EXCLUDED_PATH_PARTS = {
    "__pycache__",
    "_build",
}
MARKDOWN_SUFFIXES = {".md", ".markdown"}

@dataclass
class MarkdownWarning:

    """ Store Markdown Warning """

    file_path: Path
    line_number: int
    rule_code: str
    rule_name: str
    message: str

    def format_for_terminal(self) -> str:

        """ Format Warning For Terminal """

        relative_file_path = self.file_path.relative_to(REPOSITORY_ROOT).as_posix()
        return (
            f"{relative_file_path}:{self.line_number} "
            f"{self.rule_code}/{self.rule_name} "
            f"{self.message}"
        )

def build_argument_parser() -> argparse.ArgumentParser:

    """ Build Argument Parser """

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(
        description="Check repository-authored Markdown files for common structural warnings.",
    )

    # Configure Scan Scope
    argument_parser.add_argument(
        "paths",
        nargs="*",
        default=DEFAULT_INCLUDED_PATHS,
        help="Repository-relative files or folders to scan. Defaults to the canonical Markdown source roots.",
    )
    argument_parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Return a non-zero exit code when warnings are found.",
    )

    return argument_parser

def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command-Line Arguments """

    # Build Argument Parser
    argument_parser = build_argument_parser()

    # Parse Command-Line Arguments
    parsed_arguments = argument_parser.parse_args()

    return parsed_arguments

def resolve_input_paths(path_argument_list: list[str]) -> list[Path]:

    """ Resolve Input Paths """

    resolved_path_list: list[Path] = []

    for path_argument in path_argument_list:
        candidate_path = (REPOSITORY_ROOT / path_argument).resolve()
        assert candidate_path.exists(), f"Input path does not exist | {candidate_path}"
        resolved_path_list.append(candidate_path)

    return resolved_path_list

def should_exclude_path(file_path: Path) -> bool:

    """ Determine Whether File Path Should Be Excluded """

    relative_file_path = file_path.relative_to(REPOSITORY_ROOT)

    if relative_file_path.parts[0] in DEFAULT_EXCLUDED_ROOT_NAMES:
        return True

    if any(path_part in DEFAULT_EXCLUDED_PATH_PARTS for path_part in relative_file_path.parts):
        return True

    return False

def collect_markdown_file_path_list(input_path_list: list[Path]) -> list[Path]:

    """ Collect Markdown File Paths """

    markdown_file_path_set: set[Path] = set()

    for input_path in input_path_list:
        if input_path.is_file():
            if input_path.suffix.lower() in MARKDOWN_SUFFIXES and not should_exclude_path(input_path):
                markdown_file_path_set.add(input_path)
            continue

        for file_path in input_path.rglob("*"):
            if not file_path.is_file():
                continue
            if file_path.suffix.lower() not in MARKDOWN_SUFFIXES:
                continue
            if should_exclude_path(file_path):
                continue
            markdown_file_path_set.add(file_path)

    return sorted(markdown_file_path_set)

def build_fence_state_list(markdown_line_list: list[str]) -> list[bool]:

    """ Build Fence State List """

    inside_fenced_block = False
    fence_state_list: list[bool] = []

    for markdown_line in markdown_line_list:
        stripped_line = markdown_line.lstrip()
        fence_state_list.append(inside_fenced_block)

        if stripped_line.startswith("```") or stripped_line.startswith("~~~"):
            inside_fenced_block = not inside_fenced_block

    return fence_state_list

def is_heading_line(markdown_line: str, inside_fenced_block: bool) -> bool:

    """ Determine Whether Line Is Heading """

    if inside_fenced_block:
        return False

    stripped_line = markdown_line.lstrip()
    if not stripped_line.startswith("#"):
        return False

    heading_marker_count = len(stripped_line) - len(stripped_line.lstrip("#"))
    if heading_marker_count == 0 or heading_marker_count > 6:
        return False

    if len(stripped_line) == heading_marker_count:
        return False

    return stripped_line[heading_marker_count] == " "

def resolve_heading_level(markdown_line: str) -> int:

    """ Resolve Heading Level """

    stripped_line = markdown_line.lstrip()
    return len(stripped_line) - len(stripped_line.lstrip("#"))

def find_previous_non_blank_line_index(markdown_line_list: list[str], start_index: int) -> int | None:

    """ Find Previous Non-Blank Line Index """

    for line_index in range(start_index - 1, -1, -1):
        if markdown_line_list[line_index].strip():
            return line_index
    return None

def find_next_non_blank_line_index(markdown_line_list: list[str], start_index: int) -> int | None:

    """ Find Next Non-Blank Line Index """

    for line_index in range(start_index + 1, len(markdown_line_list)):
        if markdown_line_list[line_index].strip():
            return line_index
    return None

def check_md012_multiple_blanks(file_path: Path, markdown_line_list: list[str]) -> list[MarkdownWarning]:

    """ Check MD012 Multiple Blanks """

    warning_list: list[MarkdownWarning] = []
    consecutive_blank_count = 0

    for line_index, markdown_line in enumerate(markdown_line_list):
        if markdown_line.strip():
            consecutive_blank_count = 0
            continue

        consecutive_blank_count += 1
        if consecutive_blank_count <= 1:
            continue

        warning_list.append(
            MarkdownWarning(
                file_path=file_path,
                line_number=line_index + 1,
                rule_code="MD012",
                rule_name="no-multiple-blanks",
                message="Multiple consecutive blank lines [Expected: 1; Actual: 2+]",
            )
        )

    return warning_list

def check_md022_blanks_around_headings(file_path: Path, markdown_line_list: list[str], fence_state_list: list[bool]) -> list[MarkdownWarning]:

    """ Check MD022 Blanks Around Headings """

    warning_list: list[MarkdownWarning] = []

    for line_index, markdown_line in enumerate(markdown_line_list):
        if not is_heading_line(markdown_line, fence_state_list[line_index]):
            continue

        previous_non_blank_line_index = find_previous_non_blank_line_index(markdown_line_list, line_index)
        if previous_non_blank_line_index is not None and previous_non_blank_line_index == line_index - 1:
            warning_list.append(
                MarkdownWarning(
                    file_path=file_path,
                    line_number=line_index + 1,
                    rule_code="MD022",
                    rule_name="blanks-around-headings",
                    message="Heading should be preceded by one blank line.",
                )
            )

        next_non_blank_line_index = find_next_non_blank_line_index(markdown_line_list, line_index)
        if next_non_blank_line_index is not None and next_non_blank_line_index == line_index + 1:
            warning_list.append(
                MarkdownWarning(
                    file_path=file_path,
                    line_number=line_index + 1,
                    rule_code="MD022",
                    rule_name="blanks-around-headings",
                    message="Heading should be followed by one blank line.",
                )
            )

    return warning_list

def check_md025_single_title(file_path: Path, markdown_line_list: list[str], fence_state_list: list[bool]) -> list[MarkdownWarning]:

    """ Check MD025 Single Title """

    warning_list: list[MarkdownWarning] = []
    top_level_heading_line_list: list[int] = []

    for line_index, markdown_line in enumerate(markdown_line_list):
        if not is_heading_line(markdown_line, fence_state_list[line_index]):
            continue
        if resolve_heading_level(markdown_line) != 1:
            continue
        top_level_heading_line_list.append(line_index + 1)

    if len(top_level_heading_line_list) <= 1:
        return warning_list

    for line_number in top_level_heading_line_list[1:]:
        warning_list.append(
            MarkdownWarning(
                file_path=file_path,
                line_number=line_number,
                rule_code="MD025",
                rule_name="single-title",
                message="Multiple top-level headings in the same document.",
            )
        )

    return warning_list

def check_markdown_file(file_path: Path) -> list[MarkdownWarning]:

    """ Check Markdown File """

    markdown_line_list = file_path.read_text(encoding="utf-8").splitlines()
    fence_state_list = build_fence_state_list(markdown_line_list)

    warning_list: list[MarkdownWarning] = []
    warning_list.extend(check_md012_multiple_blanks(file_path, markdown_line_list))
    warning_list.extend(check_md022_blanks_around_headings(file_path, markdown_line_list, fence_state_list))
    warning_list.extend(check_md025_single_title(file_path, markdown_line_list, fence_state_list))

    return warning_list

def print_warning_summary(markdown_file_path_list: list[Path], warning_list: list[MarkdownWarning]) -> None:

    """ Print Warning Summary """

    print("")
    print("================================================================================================")
    print("Markdown Style Check")
    print("================================================================================================")
    print(f"Scanned Markdown Files             {len(markdown_file_path_list)}")
    print(f"Warnings Found                     {len(warning_list)}")
    print("")

    if not warning_list:
        print("[DONE] No Markdown style warnings found")
        return

    print("Warnings")
    print("--------")
    for warning in warning_list:
        print(warning.format_for_terminal())

def main() -> int:

    """ Run Markdown Style Check """

    parsed_arguments = parse_command_line_arguments()
    input_path_list = resolve_input_paths(parsed_arguments.paths)
    markdown_file_path_list = collect_markdown_file_path_list(input_path_list)

    warning_list: list[MarkdownWarning] = []
    for markdown_file_path in markdown_file_path_list:
        warning_list.extend(check_markdown_file(markdown_file_path))

    print_warning_summary(markdown_file_path_list, warning_list)

    if parsed_arguments.fail_on_warning and warning_list:
        return 1

    return 0

if __name__ == "__main__":

    raise SystemExit(main())
