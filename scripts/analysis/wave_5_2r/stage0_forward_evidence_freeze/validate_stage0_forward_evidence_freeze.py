"""Validate the written Wave 5.2R Stage 0 forward evidence freeze."""

from __future__ import annotations

import argparse
from pathlib import Path

from build_stage0_forward_evidence_freeze import (
    DEFAULT_CONFIG_PATH,
    load_configuration,
    validate_written_outputs,
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Validate the Wave 5.2R Stage 0 evidence-freeze outputs."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the Stage 0 freeze-contract configuration.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the persisted Stage 0 exit-gate checks."""

    arguments = parse_arguments()
    configuration = load_configuration(arguments.config)
    row_count_map = validate_written_outputs(configuration)
    print(
        "WAVE52R_STAGE0_VALIDATION_OK "
        f"manifest_rows={row_count_map['manifest_rows']} "
        f"baseline_rows={row_count_map['baseline_rows']} "
        f"operating_cell_rows={row_count_map['operating_cell_rows']} "
        f"provenance_rows={row_count_map['provenance_rows']}"
    )


if __name__ == "__main__":
    main()
