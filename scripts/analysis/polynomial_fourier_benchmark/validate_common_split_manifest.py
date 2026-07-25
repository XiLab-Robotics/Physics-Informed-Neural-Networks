"""Validate the written Polynomial-Fourier common-split manifest."""

from __future__ import annotations

import argparse
from pathlib import Path

from common_split_manifest import (
    DEFAULT_CONFIG_PATH,
    PROJECT_ROOT,
    load_and_validate_manifest,
    load_configuration,
    validate_manifest_csv,
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Validate pairing, split isolation, paths, sizes, and hashes in "
            "the Polynomial-Fourier benchmark manifest."
        )
    )
    argument_parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the common-split YAML configuration.",
    )
    argument_parser.add_argument(
        "--skip-content-hashes",
        action="store_true",
        help="Validate structure and sizes without recomputing source hashes.",
    )
    return argument_parser.parse_args()


def main() -> None:
    """Load the configured manifest and run all validation gates."""

    arguments = parse_arguments()
    configuration = load_configuration(arguments.config)
    manifest_path = Path(configuration["outputs"]["manifest_yaml"])
    if not manifest_path.is_absolute():
        manifest_path = PROJECT_ROOT / manifest_path
    manifest_csv_path = Path(configuration["outputs"]["manifest_csv"])
    if not manifest_csv_path.is_absolute():
        manifest_csv_path = PROJECT_ROOT / manifest_csv_path

    split_count_map = load_and_validate_manifest(
        manifest_path,
        verify_content_hashes=not arguments.skip_content_hashes,
    )
    validated_csv_row_count = validate_manifest_csv(
        manifest_path,
        manifest_csv_path,
    )
    print(
        "COMMON_SPLIT_VALIDATION_OK "
        f"train={split_count_map['train']} "
        f"validation={split_count_map['validation']} "
        f"test={split_count_map['test']} "
        f"csv_rows={validated_csv_row_count} "
        f"content_hashes={not arguments.skip_content_hashes}"
    )


if __name__ == "__main__":
    main()
