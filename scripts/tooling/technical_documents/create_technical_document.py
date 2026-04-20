""" Create Timestamped Technical Documents And Register Them """

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
import argparse
from datetime import datetime
from pathlib import Path

# Repository Paths
REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
DOCUMENTATION_ROOT = REPOSITORY_ROOT / "doc"
TECHNICAL_ROOT = DOCUMENTATION_ROOT / "technical"
DOC_INDEX_PATH = DOCUMENTATION_ROOT / "README.md"


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(
        description=(
            "Create a timestamped technical document with the required section "
            "scaffold and register it in the day-local technical README plus "
            "doc/README.md."
        ),
    )

    # Configure Document Identity
    argument_parser.add_argument(
        "--slug",
        required=True,
        help="Slug appended to the timestamp-based technical document filename.",
    )
    argument_parser.add_argument(
        "--summary",
        required=True,
        help="Short summary sentence used in the technical-document index entries.",
    )

    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    # Build Argument Parser
    argument_parser = build_argument_parser()

    # Parse Command-Line Arguments
    parsed_arguments = argument_parser.parse_args()

    return parsed_arguments


def slugify_document_name(document_slug: str) -> str:

    """Slugify a technical-document suffix.

    Args:
        document_slug: Raw slug string supplied from the CLI.

    Returns:
        Normalized lowercase slug using underscores as separators.

    Raises:
        AssertionError: If the slug normalizes to an empty value.
    """

    # Normalize Slug Characters
    normalized_character_list: list[str] = []
    previous_character_was_separator = False

    for character in document_slug.strip().lower():
        if character.isalnum():
            normalized_character_list.append(character)
            previous_character_was_separator = False
            continue

        if previous_character_was_separator:
            continue

        normalized_character_list.append("_")
        previous_character_was_separator = True

    # Resolve Final Slug
    normalized_slug = "".join(normalized_character_list).strip("_")
    assert normalized_slug, "Document slug normalized to an empty value."

    return normalized_slug


def build_timestamp_bundle() -> dict[str, str]:

    """Build the current local timestamp bundle."""

    # Resolve Local Timestamp
    current_timestamp = datetime.now().astimezone()

    # Build Timestamp Fields
    timestamp_bundle = {
        "month_label": current_timestamp.strftime("%Y-%m"),
        "day_label": current_timestamp.strftime("%Y-%m-%d"),
        "file_timestamp": current_timestamp.strftime("%Y-%m-%d-%H-%M-%S"),
    }

    return timestamp_bundle


def build_document_path(timestamp_bundle: dict[str, str], normalized_slug: str) -> Path:

    """Build the absolute technical-document path."""

    # Resolve Technical Directory
    technical_day_directory = TECHNICAL_ROOT / timestamp_bundle["month_label"] / timestamp_bundle["day_label"]

    # Build Technical Document Path
    technical_document_name = f"{timestamp_bundle['file_timestamp']}_{normalized_slug}.md"
    technical_document_path = technical_day_directory / technical_document_name

    return technical_document_path


def build_day_readme_path(technical_document_path: Path) -> Path:

    """Build the day-local technical README path."""

    return technical_document_path.parent / "README.md"


def build_technical_document_markdown(document_title: str) -> str:

    """Build the default technical-document scaffold."""

    # Build Markdown Scaffold
    technical_document_markdown = f"""# {document_title}

## Overview

TBD.

## Technical Approach

TBD.

## Involved Components

- TBD

## Implementation Steps

1. TBD
"""

    return technical_document_markdown


def build_day_readme_markdown(day_label: str) -> str:

    """Build the default day-local technical README."""

    # Build README Content
    day_readme_markdown = f"""# {day_label} Technical Documents
"""

    return day_readme_markdown


def ensure_parent_directory_exists(file_path: Path) -> None:

    """Ensure the parent directory exists."""

    file_path.parent.mkdir(parents=True, exist_ok=True)


def read_text_or_default(file_path: Path, default_text: str) -> str:

    """Read UTF-8 text or return a default value."""

    # Read Existing File
    if file_path.exists():
        return file_path.read_text(encoding="utf-8")

    # Return Default Content
    return default_text


def build_day_readme_entry(document_file_name: str, summary: str) -> str:

    """Build one day-local README entry."""

    return (
        f"- [{document_file_name}](./{document_file_name})\n"
        f"  {summary}\n"
    )


def build_doc_index_entry(document_relative_path: Path, summary: str) -> str:

    """Build one doc/README technical-document entry."""

    normalized_relative_path = document_relative_path.as_posix()

    return (
        f"- [{normalized_relative_path}](./{normalized_relative_path})\n"
        f"  {summary}\n"
    )


def insert_entry_after_heading(readme_text: str, entry_text: str) -> str:

    """Insert one entry after the README heading block."""

    # Skip Duplicate Entry
    if entry_text.strip() in readme_text:
        return readme_text

    # Split Heading From Body
    stripped_readme_text = readme_text.rstrip() + "\n"
    split_marker = "\n\n"
    assert split_marker in stripped_readme_text, "README heading block is malformed."
    heading_block, remainder = stripped_readme_text.split(split_marker, maxsplit=1)

    # Rebuild README Content
    updated_readme_text = f"{heading_block}\n\n{entry_text}{remainder.lstrip()}"

    return updated_readme_text


def insert_entry_before_first_technical_item(readme_text: str, entry_text: str) -> str:

    """Insert one entry before the first technical-document bullet."""

    # Skip Duplicate Entry
    if entry_text.strip() in readme_text:
        return readme_text

    # Resolve Insertion Marker
    technical_entry_marker = "- [technical/"
    technical_entry_index = readme_text.find(technical_entry_marker)
    assert technical_entry_index >= 0, "Could not find the technical-document section marker in doc/README.md."

    # Rebuild README Content
    updated_readme_text = (
        readme_text[:technical_entry_index]
        + entry_text
        + readme_text[technical_entry_index:]
    )

    return updated_readme_text


def write_normalized_markdown(file_path: Path, markdown_text: str) -> None:

    """Write normalized Markdown with one final newline."""

    normalized_markdown_text = markdown_text.rstrip() + "\n"
    file_path.write_text(normalized_markdown_text, encoding="utf-8")


def create_technical_document(technical_document_path: Path) -> None:

    """Create the technical document scaffold."""

    # Validate Non-Existing Target
    assert not technical_document_path.exists(), f"Technical document already exists | {technical_document_path}"

    # Resolve Document Title
    document_title = technical_document_path.stem.replace("_", " ").title()

    # Create Technical Document
    ensure_parent_directory_exists(technical_document_path)
    technical_document_markdown = build_technical_document_markdown(document_title)
    write_normalized_markdown(technical_document_path, technical_document_markdown)


def update_day_readme(technical_document_path: Path, summary: str, day_label: str) -> Path:

    """Update the day-local technical README."""

    # Resolve README Paths
    day_readme_path = build_day_readme_path(technical_document_path)
    default_day_readme_text = build_day_readme_markdown(day_label)
    current_day_readme_text = read_text_or_default(day_readme_path, default_day_readme_text)

    # Insert New Entry
    day_readme_entry = build_day_readme_entry(technical_document_path.name, summary)
    updated_day_readme_text = insert_entry_after_heading(current_day_readme_text, day_readme_entry)

    # Write Updated README
    ensure_parent_directory_exists(day_readme_path)
    write_normalized_markdown(day_readme_path, updated_day_readme_text)

    return day_readme_path


def update_doc_index(technical_document_path: Path, summary: str) -> Path:

    """Update the canonical doc/README index."""

    # Resolve Current Index Text
    assert DOC_INDEX_PATH.exists(), f"Canonical doc index does not exist | {DOC_INDEX_PATH}"
    current_doc_index_text = DOC_INDEX_PATH.read_text(encoding="utf-8")

    # Insert New Entry
    document_relative_path = technical_document_path.relative_to(DOCUMENTATION_ROOT)
    doc_index_entry = build_doc_index_entry(document_relative_path, summary)
    updated_doc_index_text = insert_entry_before_first_technical_item(current_doc_index_text, doc_index_entry)

    # Write Updated Index
    write_normalized_markdown(DOC_INDEX_PATH, updated_doc_index_text)

    return DOC_INDEX_PATH


def print_creation_summary(technical_document_path: Path, day_readme_path: Path, doc_index_path: Path) -> None:

    """Print a concise creation summary."""

    print("")
    print("================================================================================================")
    print("Technical Document Created")
    print("================================================================================================")
    print(f"Technical Document Path            {technical_document_path}")
    print(f"Day README Path                    {day_readme_path}")
    print(f"Doc Index Path                     {doc_index_path}")
    print("")
    print("[DONE] Technical document scaffold and index registration completed")


def main() -> None:

    """Run the technical-document scaffold workflow."""

    # Parse Command-Line Arguments
    parsed_arguments = parse_command_line_arguments()

    # Resolve Timestamped Output Path
    normalized_slug = slugify_document_name(parsed_arguments.slug)
    timestamp_bundle = build_timestamp_bundle()
    technical_document_path = build_document_path(timestamp_bundle, normalized_slug)

    # Create Technical Document And Update Indices
    create_technical_document(technical_document_path)
    day_readme_path = update_day_readme(
        technical_document_path,
        parsed_arguments.summary,
        timestamp_bundle["day_label"],
    )
    doc_index_path = update_doc_index(technical_document_path, parsed_arguments.summary)

    # Print Completion Summary
    print_creation_summary(technical_document_path, day_readme_path, doc_index_path)


if __name__ == "__main__":

    main()
