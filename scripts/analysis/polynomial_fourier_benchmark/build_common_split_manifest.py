"""Build the paired Fw/Bw Polynomial-Fourier benchmark manifest."""

from __future__ import annotations

import argparse
from pathlib import Path

from common_split_manifest import (
    DEFAULT_CONFIG_PATH,
    build_manifest_payload,
    load_configuration,
    write_manifest_outputs,
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Build the content-addressed paired Fw/Bw common split for the "
            "Polynomial-Fourier benchmark."
        )
    )
    argument_parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the common-split YAML configuration.",
    )
    return argument_parser.parse_args()


def main() -> None:
    """Build, validate, and write the common-split artifacts."""

    arguments = parse_arguments()
    configuration = load_configuration(arguments.config)
    manifest_payload = build_manifest_payload(configuration, arguments.config)
    manifest_yaml_path, manifest_csv_path, report_path = write_manifest_outputs(
        manifest_payload,
        configuration,
    )

    split_count_map = manifest_payload["split"]["condition_count_by_split"]
    print(
        "COMMON_SPLIT_MANIFEST_OK "
        f"paired_conditions={manifest_payload['dataset']['paired_condition_count']} "
        f"train={split_count_map['train']} "
        f"validation={split_count_map['validation']} "
        f"test={split_count_map['test']}"
    )
    print(f"manifest_yaml={manifest_yaml_path}")
    print(f"manifest_csv={manifest_csv_path}")
    print(f"data_contract_report={report_path}")


if __name__ == "__main__":
    main()
