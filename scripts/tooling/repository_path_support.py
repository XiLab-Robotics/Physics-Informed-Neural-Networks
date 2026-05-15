"""Repository-relative path helpers for cross-platform script entry points."""

from __future__ import annotations

# Import Python Utilities
import argparse
import os
import re
from pathlib import Path
from typing import Any

WINDOWS_PLATFORM_NAME = "windows"
LINUX_PLATFORM_NAME = "linux"
DEFAULT_PLATFORM_NAME = WINDOWS_PLATFORM_NAME
PLATFORM_ENVIRONMENT_VARIABLE_NAME = "STANDARDML_REPOSITORY_PATH_PLATFORM"
WINDOWS_ABSOLUTE_PATH_PATTERN = re.compile(r"^[A-Za-z]:[\\/]")


def add_platform_arguments(argument_parser: argparse.ArgumentParser) -> None:

    """Add mutually exclusive repository path platform flags."""

    platform_group = argument_parser.add_mutually_exclusive_group()
    platform_group.add_argument(
        "--windows",
        dest="repository_path_platform",
        action="store_const",
        const=WINDOWS_PLATFORM_NAME,
        default=DEFAULT_PLATFORM_NAME,
        help="Format repository-relative paths for Windows operator surfaces.",
    )
    platform_group.add_argument(
        "--linux",
        dest="repository_path_platform",
        action="store_const",
        const=LINUX_PLATFORM_NAME,
        help="Format repository-relative paths for Linux operator surfaces.",
    )


def normalize_platform_name(platform_name: str | None) -> str:

    """Normalize one repository path platform name."""

    normalized_platform_name = str(platform_name or DEFAULT_PLATFORM_NAME).strip().lower()
    if normalized_platform_name not in {WINDOWS_PLATFORM_NAME, LINUX_PLATFORM_NAME}:
        raise ValueError(f"Unsupported repository path platform | {platform_name}")
    return normalized_platform_name


def resolve_argument_platform(command_line_arguments: Any) -> str:

    """Resolve the platform selected by argparse flags."""

    return normalize_platform_name(
        getattr(command_line_arguments, "repository_path_platform", DEFAULT_PLATFORM_NAME)
    )


def set_runtime_platform(platform_name: str | None) -> str:

    """Persist the selected repository path platform for shared helpers."""

    normalized_platform_name = normalize_platform_name(platform_name)
    os.environ[PLATFORM_ENVIRONMENT_VARIABLE_NAME] = normalized_platform_name
    return normalized_platform_name


def get_runtime_platform() -> str:

    """Resolve the active repository path platform."""

    return normalize_platform_name(os.environ.get(PLATFORM_ENVIRONMENT_VARIABLE_NAME))


def is_windows_absolute_path_text(path_text: str) -> bool:

    """Return whether path text is a Windows absolute path."""

    return bool(WINDOWS_ABSOLUTE_PATH_PATTERN.match(path_text)) or path_text.startswith("\\\\")


def normalize_repository_relative_path_text(path_value: str | Path) -> str:

    """Normalize a repository-relative path string for pathlib on any OS."""

    return str(path_value).replace("\\", "/")


def resolve_repository_path(
    path_value: str | Path,
    repository_root: str | Path,
    allow_absolute: bool = False,
) -> Path:

    """Resolve one path, treating non-absolute values as repository-relative."""

    path_text = str(path_value)
    candidate_path = Path(path_text)
    if candidate_path.is_absolute():
        if allow_absolute:
            return candidate_path
        raise ValueError(f"Absolute path is not allowed | {path_text}")

    if is_windows_absolute_path_text(path_text):
        if allow_absolute:
            return Path(path_text)
        raise ValueError(f"Windows absolute path is not allowed | {path_text}")

    normalized_path_text = normalize_repository_relative_path_text(path_text)
    return Path(os.path.abspath(str(Path(repository_root) / normalized_path_text)))


def format_repository_relative_path(
    path_value: str | Path,
    repository_root: str | Path,
    platform_name: str | None = None,
) -> str:

    """Format one path relative to the repository root for a target platform."""

    normalized_platform_name = normalize_platform_name(platform_name or get_runtime_platform())
    repository_root_path = Path(repository_root).resolve()
    resolved_path = Path(path_value).resolve()

    try:
        relative_path_text = resolved_path.relative_to(repository_root_path).as_posix()
    except ValueError:
        relative_path_text = resolved_path.as_posix()

    if normalized_platform_name == WINDOWS_PLATFORM_NAME:
        return relative_path_text.replace("/", "\\")
    return relative_path_text
