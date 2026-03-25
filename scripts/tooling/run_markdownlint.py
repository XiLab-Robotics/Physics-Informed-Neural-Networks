""" Run Repository Markdownlint Configuration """

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
import argparse
import subprocess
from pathlib import Path

# Markdownlint Runner Constants
REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
MARKDOWNLINT_CONFIG_PATH = REPOSITORY_ROOT / ".markdownlint-cli2.jsonc"
MARKDOWNLINT_COMMAND = [
    "npx.cmd",
    "--yes",
    "markdownlint-cli2",
    "--config",
    str(MARKDOWNLINT_CONFIG_PATH),
]


def build_argument_parser() -> argparse.ArgumentParser:

    """ Build Argument Parser """

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(
        description="Run the repository Markdownlint profile on canonical Markdown sources.",
    )

    # Configure Scan Scope
    argument_parser.add_argument(
        "paths",
        nargs="*",
        help="Optional repository-relative files or folders to lint instead of the configured default globs.",
    )
    argument_parser.add_argument(
        "--fix",
        action="store_true",
        help="Apply fixable Markdownlint corrections in place.",
    )

    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command-Line Arguments """

    # Build Argument Parser
    argument_parser = build_argument_parser()

    # Parse Command-Line Arguments
    parsed_arguments = argument_parser.parse_args()

    return parsed_arguments


def build_markdownlint_command(parsed_arguments: argparse.Namespace) -> list[str]:

    """ Build Markdownlint Command """

    markdownlint_command = list(MARKDOWNLINT_COMMAND)

    if parsed_arguments.fix:
        markdownlint_command.append("--fix")

    if parsed_arguments.paths:
        markdownlint_command.append("--no-globs")
        for relative_path in parsed_arguments.paths:
            markdownlint_command.append(relative_path.replace("\\", "/"))

    return markdownlint_command


def main() -> int:

    """ Run Markdownlint """

    # Parse Command-Line Arguments
    parsed_arguments = parse_command_line_arguments()

    # Build Markdownlint Command
    markdownlint_command = build_markdownlint_command(parsed_arguments)

    # Execute Markdownlint
    completed_process = subprocess.run(
        markdownlint_command,
        cwd=REPOSITORY_ROOT,
        check=False,
    )

    return completed_process.returncode


if __name__ == "__main__":
    raise SystemExit(main())
