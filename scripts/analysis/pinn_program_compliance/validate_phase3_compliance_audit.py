"""Validate the persisted Phase 3 compliance identifiability audit."""

from __future__ import annotations

import argparse
from pathlib import Path

from build_phase3_compliance_audit import (
    DEFAULT_CONFIG_PATH,
    load_configuration,
    validate_written_outputs,
)


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Validate the complete written Phase 3 compliance package."
    )
    argument_parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the Phase 3 compliance-audit configuration.",
    )
    return argument_parser.parse_args()


def main() -> None:

    """Run the Phase 3 output-identity and entry-gate checks."""

    arguments = parse_arguments()
    configuration = load_configuration(arguments.config)
    row_count_map = validate_written_outputs(configuration)
    print(
        "PHASE3_COMPLIANCE_VALIDATION_OK "
        f"condition_rows={row_count_map['condition_audit_csv']} "
        f"metric_rows={row_count_map['formulation_metrics_csv']}"
    )


if __name__ == "__main__":
    main()
