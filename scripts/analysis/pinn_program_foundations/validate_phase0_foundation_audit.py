"""Validate the written Phase 0 PINN foundation package."""

from __future__ import annotations

import argparse
from pathlib import Path

from build_phase0_foundation_audit import (
    DEFAULT_CONFIG_PATH,
    load_configuration,
    validate_written_outputs,
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Validate the complete written Phase 0 foundation package."
    )
    argument_parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the Phase 0 foundation-audit configuration.",
    )
    return argument_parser.parse_args()


def main() -> None:
    """Run the Phase 0 output-identity and exit-gate checks."""

    arguments = parse_arguments()
    configuration = load_configuration(arguments.config)
    row_count_map = validate_written_outputs(configuration)
    print(
        "PHASE0_FOUNDATION_VALIDATION_OK "
        f"curve_rows={row_count_map['curve_audit_csv']} "
        f"condition_rows={row_count_map['condition_support_csv']} "
        f"harmonic_rows={row_count_map['harmonic_prevalence_csv']} "
        f"signal_rows={row_count_map['signal_availability_csv']}"
    )


if __name__ == "__main__":
    main()
