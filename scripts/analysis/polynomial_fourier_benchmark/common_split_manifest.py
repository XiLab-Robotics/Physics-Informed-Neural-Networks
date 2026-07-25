"""Build and validate the paired Fw/Bw Polynomial-Fourier benchmark split."""

from __future__ import annotations

import csv
import hashlib
import json
import random
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


# Repository Paths
PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "analysis"
    / "polynomial_fourier_benchmark"
    / "common_split_manifest.yaml"
)


# Dataset Contract
FILENAME_PATTERN = re.compile(
    r"(?P<speed_rpm>-?[0-9.]+)rpm"
    r"(?P<torque_nm>-?[0-9.]+)Nm"
    r"(?P<oil_temperature_deg>-?[0-9.]+)deg\.csv$"
)
SPEED_DIRECTORY_PATTERN = re.compile(r"(?P<speed_rpm>-?[0-9.]+)rpm$")
TEMPERATURE_DIRECTORY_PATTERN = re.compile(
    r"(?P<oil_temperature_deg>-?[0-9.]+)degree$"
)
SPLIT_NAME_LIST = ("train", "validation", "test")
DIRECTION_NAME_LIST = ("Fw", "Bw")


@dataclass(frozen=True, order=True)
class OperatingCondition:
    """Represent one nominal TE operating condition."""

    input_speed_rpm: float
    output_torque_nm: float
    oil_temperature_deg_c: float

    @property
    def condition_id(self) -> str:
        """Return a stable, readable identifier for this condition."""

        return (
            f"speed_{_format_number(self.input_speed_rpm)}rpm__"
            f"torque_{_format_number(self.output_torque_nm)}Nm__"
            f"temperature_{_format_number(self.oil_temperature_deg_c)}degC"
        )


@dataclass(frozen=True)
class DirectionalConditionFiles:
    """Hold the paired directional files for one operating condition."""

    condition: OperatingCondition
    forward_path: Path
    backward_path: Path


def load_configuration(config_path: Path) -> dict[str, Any]:
    """Load and minimally validate the benchmark configuration.

    Args:
        config_path: YAML configuration path.

    Returns:
        Parsed configuration dictionary.
    """

    # Load Configuration
    resolved_config_path = config_path.resolve()
    assert resolved_config_path.is_file(), (
        f"Common-split configuration does not exist | {resolved_config_path}"
    )
    configuration = yaml.safe_load(resolved_config_path.read_text(encoding="utf-8"))

    # Validate Required Sections
    assert isinstance(configuration, dict), "Common-split configuration must be a mapping"
    for required_section in ("metadata", "dataset", "split", "outputs"):
        assert required_section in configuration, (
            f"Missing common-split configuration section | {required_section}"
        )

    return configuration


def build_manifest_payload(
    configuration: dict[str, Any],
    config_path: Path,
) -> dict[str, Any]:
    """Build a content-addressed paired Fw/Bw split manifest.

    Args:
        configuration: Parsed benchmark configuration.
        config_path: Source configuration path.

    Returns:
        Complete manifest payload.
    """

    # Resolve Dataset Roots
    dataset_configuration = configuration["dataset"]
    dataset_root = _resolve_project_path(dataset_configuration["root"])
    assert dataset_root.is_dir(), f"Dataset root does not exist | {dataset_root}"

    direction_directory_map = dataset_configuration["direction_directory_map"]
    assert set(direction_directory_map) == set(DIRECTION_NAME_LIST), (
        "Direction directory map must define exactly Fw and Bw"
    )

    # Index Each Direction
    directional_condition_map: dict[str, dict[OperatingCondition, Path]] = {}
    for direction_name in DIRECTION_NAME_LIST:
        direction_root = dataset_root / direction_directory_map[direction_name]
        directional_condition_map[direction_name] = _index_directional_files(
            direction_root=direction_root,
            expected_csv_column_list=dataset_configuration[
                "expected_csv_column_list"
            ],
        )

    # Require Exact Pairing
    forward_condition_set = set(directional_condition_map["Fw"])
    backward_condition_set = set(directional_condition_map["Bw"])
    assert forward_condition_set == backward_condition_set, (
        "Forward and backward operating-condition sets differ | "
        f"Fw-only={len(forward_condition_set - backward_condition_set)} | "
        f"Bw-only={len(backward_condition_set - forward_condition_set)}"
    )

    paired_condition_files = [
        DirectionalConditionFiles(
            condition=condition,
            forward_path=directional_condition_map["Fw"][condition],
            backward_path=directional_condition_map["Bw"][condition],
        )
        for condition in sorted(forward_condition_set)
    ]

    # Split Conditions Once
    split_configuration = configuration["split"]
    assert split_configuration["require_paired_directions"] is True, (
        "The Polynomial-Fourier benchmark requires paired Fw and Bw conditions"
    )
    assert split_configuration["content_hash_algorithm"] == "sha256", (
        "Only SHA-256 content addressing is supported"
    )
    split_condition_map = _split_paired_conditions(
        paired_condition_files=paired_condition_files,
        validation_fraction=float(split_configuration["validation_fraction"]),
        test_fraction=float(split_configuration["test_fraction"]),
        random_seed=int(split_configuration["random_seed"]),
    )

    # Build Manifest Entries
    manifest_entry_list: list[dict[str, Any]] = []
    split_count_map: dict[str, int] = {}
    for split_name in SPLIT_NAME_LIST:
        split_condition_list = sorted(
            split_condition_map[split_name],
            key=lambda paired_files: paired_files.condition,
        )
        split_count_map[split_name] = len(split_condition_list)

        for paired_files in split_condition_list:
            manifest_entry_list.append(
                _build_manifest_entry(
                    paired_files=paired_files,
                    split_name=split_name,
                    dataset_root=dataset_root,
                )
            )

    # Record Provenance And Counts
    config_hash = _compute_file_sha256(config_path.resolve())
    manifest_payload: dict[str, Any] = {
        "schema_version": 1,
        "manifest_id": configuration["metadata"]["benchmark_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_configuration": {
            "path": _project_relative_path(config_path.resolve()),
            "sha256": config_hash,
        },
        "dataset": {
            "dataset_id": configuration["metadata"]["dataset_id"],
            "dataset_schema": configuration["metadata"]["dataset_schema"],
            "root": _project_relative_path(dataset_root),
            "paired_condition_count": len(paired_condition_files),
            "directional_file_count": len(paired_condition_files) * 2,
        },
        "split": {
            "random_seed": int(split_configuration["random_seed"]),
            "validation_fraction": float(split_configuration["validation_fraction"]),
            "test_fraction": float(split_configuration["test_fraction"]),
            "assignment_unit": "paired_operating_condition",
            "condition_count_by_split": split_count_map,
            "directional_file_count_by_split": {
                split_name: split_count_map[split_name] * 2
                for split_name in SPLIT_NAME_LIST
            },
        },
        "units": {
            "angular_position": dataset_configuration["angular_position_unit"],
            "transmission_error": dataset_configuration["transmission_error_unit"],
            "input_speed": dataset_configuration["input_speed_unit"],
            "output_torque": dataset_configuration["output_torque_unit"],
            "oil_temperature": dataset_configuration["oil_temperature_unit"],
        },
        "entry_list": manifest_entry_list,
    }
    manifest_payload["split"]["assignment_sha256"] = _compute_assignment_sha256(
        manifest_entry_list
    )

    validate_manifest_payload(manifest_payload, verify_content_hashes=True)
    return manifest_payload


def write_manifest_outputs(
    manifest_payload: dict[str, Any],
    configuration: dict[str, Any],
) -> tuple[Path, Path, Path]:
    """Write the YAML, CSV, and Markdown data-contract outputs.

    Args:
        manifest_payload: Validated manifest payload.
        configuration: Parsed benchmark configuration.

    Returns:
        Paths to the YAML manifest, CSV manifest, and Markdown report.
    """

    # Resolve Output Paths
    output_configuration = configuration["outputs"]
    manifest_yaml_path = _resolve_project_path(output_configuration["manifest_yaml"])
    manifest_csv_path = _resolve_project_path(output_configuration["manifest_csv"])
    report_path = _resolve_project_path(output_configuration["data_contract_report"])

    for output_path in (manifest_yaml_path, manifest_csv_path, report_path):
        output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write Machine-Readable Outputs
    manifest_yaml_path.write_text(
        yaml.safe_dump(
            manifest_payload,
            sort_keys=False,
            allow_unicode=False,
            width=120,
        ),
        encoding="utf-8",
    )
    _write_manifest_csv(manifest_payload, manifest_csv_path)

    # Write Human-Readable Contract
    report_path.write_text(
        _build_data_contract_markdown(
            manifest_payload=manifest_payload,
            manifest_yaml_path=manifest_yaml_path,
            manifest_csv_path=manifest_csv_path,
        ),
        encoding="utf-8",
    )

    return manifest_yaml_path, manifest_csv_path, report_path


def validate_manifest_payload(
    manifest_payload: dict[str, Any],
    verify_content_hashes: bool,
) -> dict[str, int]:
    """Validate pairing, split isolation, path uniqueness, and file hashes.

    Args:
        manifest_payload: Parsed manifest dictionary.
        verify_content_hashes: Whether to recompute every source-file SHA-256.

    Returns:
        Validated paired-condition counts by split.
    """

    # Validate Top-Level Contract
    assert manifest_payload["schema_version"] == 1, "Unsupported manifest schema"
    entry_list = manifest_payload["entry_list"]
    assert isinstance(entry_list, list) and entry_list, "Manifest entry list is empty"
    source_configuration = manifest_payload["source_configuration"]
    source_configuration_path = _resolve_project_path(source_configuration["path"])
    assert source_configuration_path.is_file(), (
        f"Manifest source configuration does not exist | {source_configuration_path}"
    )
    assert (
        _compute_file_sha256(source_configuration_path)
        == source_configuration["sha256"]
    ), "Manifest source-configuration SHA-256 mismatch"

    # Validate Condition And Path Isolation
    condition_id_set: set[str] = set()
    source_path_set: set[str] = set()
    split_condition_id_map = {split_name: set() for split_name in SPLIT_NAME_LIST}

    for entry in entry_list:
        split_name = entry["split"]
        assert split_name in SPLIT_NAME_LIST, f"Unknown split name | {split_name}"

        condition_id = entry["condition_id"]
        assert condition_id not in condition_id_set, (
            f"Operating condition appears more than once | {condition_id}"
        )
        condition_id_set.add(condition_id)
        split_condition_id_map[split_name].add(condition_id)

        direction_files = entry["direction_files"]
        assert set(direction_files) == set(DIRECTION_NAME_LIST), (
            f"Condition must include exactly Fw and Bw | {condition_id}"
        )

        for direction_name in DIRECTION_NAME_LIST:
            source_record = direction_files[direction_name]
            relative_source_path = source_record["path"]
            assert relative_source_path not in source_path_set, (
                f"Directional source file appears more than once | {relative_source_path}"
            )
            source_path_set.add(relative_source_path)

            source_path = _resolve_project_path(relative_source_path)
            assert source_path.is_file(), f"Manifest source file does not exist | {source_path}"
            assert source_path.stat().st_size == source_record["size_bytes"], (
                f"Manifest source-file size mismatch | {source_path}"
            )

            if verify_content_hashes:
                assert _compute_file_sha256(source_path) == source_record["sha256"], (
                    f"Manifest source-file SHA-256 mismatch | {source_path}"
                )

    # Validate Split Disjointness
    for first_index, first_split_name in enumerate(SPLIT_NAME_LIST):
        for second_split_name in SPLIT_NAME_LIST[first_index + 1 :]:
            overlap = (
                split_condition_id_map[first_split_name]
                & split_condition_id_map[second_split_name]
            )
            assert not overlap, (
                f"Condition leakage between {first_split_name} and "
                f"{second_split_name} | {sorted(overlap)[:3]}"
            )

    validated_count_map = {
        split_name: len(split_condition_id_map[split_name])
        for split_name in SPLIT_NAME_LIST
    }
    expected_count_map = manifest_payload["split"]["condition_count_by_split"]
    assert validated_count_map == expected_count_map, (
        f"Split-count mismatch | validated={validated_count_map} | "
        f"expected={expected_count_map}"
    )
    assert len(source_path_set) == len(condition_id_set) * 2, (
        "Every paired operating condition must expose two unique source files"
    )
    assert (
        _compute_assignment_sha256(entry_list)
        == manifest_payload["split"]["assignment_sha256"]
    ), "Stable split-assignment SHA-256 mismatch"

    return validated_count_map


def load_and_validate_manifest(
    manifest_path: Path,
    verify_content_hashes: bool = True,
) -> dict[str, int]:
    """Load and validate a written common-split manifest.

    Args:
        manifest_path: YAML manifest path.
        verify_content_hashes: Whether to recompute source-file hashes.

    Returns:
        Validated paired-condition counts by split.
    """

    resolved_manifest_path = manifest_path.resolve()
    assert resolved_manifest_path.is_file(), (
        f"Common-split manifest does not exist | {resolved_manifest_path}"
    )
    manifest_payload = yaml.safe_load(
        resolved_manifest_path.read_text(encoding="utf-8")
    )
    assert isinstance(manifest_payload, dict), "Manifest YAML must contain a mapping"
    return validate_manifest_payload(manifest_payload, verify_content_hashes)


def validate_manifest_csv(manifest_path: Path, manifest_csv_path: Path) -> int:
    """Validate the flat CSV audit view against the canonical YAML entries.

    Args:
        manifest_path: Canonical YAML manifest path.
        manifest_csv_path: Flat CSV audit-view path.

    Returns:
        Number of validated paired-condition rows.
    """

    # Load Canonical And Flat Manifests
    manifest_payload = yaml.safe_load(
        manifest_path.resolve().read_text(encoding="utf-8")
    )
    with manifest_csv_path.resolve().open(
        "r",
        encoding="utf-8",
        newline="",
    ) as csv_file:
        csv_row_list = list(csv.DictReader(csv_file))

    entry_list = manifest_payload["entry_list"]
    assert len(csv_row_list) == len(entry_list), (
        f"CSV and YAML manifest row counts differ | "
        f"csv={len(csv_row_list)} | yaml={len(entry_list)}"
    )

    # Compare Every Flattened Record
    for entry, csv_row in zip(entry_list, csv_row_list, strict=True):
        operating_condition = entry["nominal_operating_condition"]
        direction_files = entry["direction_files"]
        expected_csv_row = {
            "condition_id": entry["condition_id"],
            "split": entry["split"],
            "input_speed_rpm": str(operating_condition["input_speed_rpm"]),
            "output_torque_nm": str(operating_condition["output_torque_nm"]),
            "oil_temperature_deg_c": str(
                operating_condition["oil_temperature_deg_c"]
            ),
            "fw_path": direction_files["Fw"]["path"],
            "fw_size_bytes": str(direction_files["Fw"]["size_bytes"]),
            "fw_sha256": direction_files["Fw"]["sha256"],
            "bw_path": direction_files["Bw"]["path"],
            "bw_size_bytes": str(direction_files["Bw"]["size_bytes"]),
            "bw_sha256": direction_files["Bw"]["sha256"],
        }
        assert csv_row == expected_csv_row, (
            f"CSV audit row differs from YAML manifest | {entry['condition_id']}"
        )

    return len(csv_row_list)


def _index_directional_files(
    direction_root: Path,
    expected_csv_column_list: list[str],
) -> dict[OperatingCondition, Path]:
    """Index and validate every curve file for one direction."""

    # Collect Directional Files
    assert direction_root.is_dir(), f"Direction root does not exist | {direction_root}"
    csv_file_path_list = sorted(direction_root.rglob("*.csv"))
    assert csv_file_path_list, f"No CSV files found | {direction_root}"

    # Parse And Validate Conditions
    condition_path_map: dict[OperatingCondition, Path] = {}
    for csv_file_path in csv_file_path_list:
        operating_condition = _parse_operating_condition(csv_file_path)
        assert operating_condition not in condition_path_map, (
            f"Duplicate operating condition | {operating_condition.condition_id} | "
            f"{condition_path_map.get(operating_condition)} | {csv_file_path}"
        )
        _validate_csv_header(csv_file_path, expected_csv_column_list)
        condition_path_map[operating_condition] = csv_file_path.resolve()

    return condition_path_map


def _parse_operating_condition(csv_file_path: Path) -> OperatingCondition:
    """Parse filename metadata and cross-check its two parent directories."""

    filename_match = FILENAME_PATTERN.fullmatch(csv_file_path.name)
    assert filename_match is not None, (
        f"Unable to parse operating condition from filename | {csv_file_path}"
    )

    speed_rpm = float(filename_match.group("speed_rpm"))
    torque_nm = float(filename_match.group("torque_nm"))
    oil_temperature_deg_c = float(
        filename_match.group("oil_temperature_deg")
    )

    speed_directory_match = SPEED_DIRECTORY_PATTERN.fullmatch(
        csv_file_path.parent.name
    )
    temperature_directory_match = TEMPERATURE_DIRECTORY_PATTERN.fullmatch(
        csv_file_path.parent.parent.name
    )
    assert speed_directory_match is not None, (
        f"Unable to parse speed directory | {csv_file_path.parent}"
    )
    assert temperature_directory_match is not None, (
        f"Unable to parse temperature directory | {csv_file_path.parent.parent}"
    )
    assert float(speed_directory_match.group("speed_rpm")) == speed_rpm, (
        f"Filename and directory speed differ | {csv_file_path}"
    )
    assert (
        float(temperature_directory_match.group("oil_temperature_deg"))
        == oil_temperature_deg_c
    ), f"Filename and directory temperature differ | {csv_file_path}"

    return OperatingCondition(
        input_speed_rpm=speed_rpm,
        output_torque_nm=torque_nm,
        oil_temperature_deg_c=oil_temperature_deg_c,
    )


def _validate_csv_header(
    csv_file_path: Path,
    expected_csv_column_list: list[str],
) -> None:
    """Validate the exact ordered polished-dataset CSV header."""

    with csv_file_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        actual_csv_column_list = next(csv_reader, None)

    assert actual_csv_column_list == expected_csv_column_list, (
        f"Unexpected CSV schema | {csv_file_path} | "
        f"expected={expected_csv_column_list} | actual={actual_csv_column_list}"
    )


def _split_paired_conditions(
    paired_condition_files: list[DirectionalConditionFiles],
    validation_fraction: float,
    test_fraction: float,
    random_seed: int,
) -> dict[str, list[DirectionalConditionFiles]]:
    """Assign paired conditions to train, validation, and test exactly once."""

    # Validate Fractions
    assert 0.0 < validation_fraction < 1.0, (
        f"Validation fraction must be between zero and one | {validation_fraction}"
    )
    assert 0.0 <= test_fraction < 1.0, (
        f"Test fraction must be between zero and one | {test_fraction}"
    )
    assert validation_fraction + test_fraction < 1.0, (
        "Validation and test fractions must leave a non-empty training split"
    )
    assert len(paired_condition_files) >= 3, (
        "At least three paired conditions are required"
    )

    # Shuffle One Paired List
    shuffled_condition_list = list(paired_condition_files)
    random_generator = random.Random(random_seed)
    random_generator.shuffle(shuffled_condition_list)

    # Match Repository Split Rounding
    condition_count = len(shuffled_condition_list)
    validation_count = max(1, int(round(condition_count * validation_fraction)))
    validation_count = min(validation_count, condition_count - 1)
    remaining_count = condition_count - validation_count

    test_count = int(round(condition_count * test_fraction))
    if test_fraction > 0.0:
        test_count = max(1, test_count)
    test_count = min(test_count, remaining_count - 1)

    validation_end_index = validation_count
    test_end_index = validation_end_index + test_count
    split_condition_map = {
        "validation": shuffled_condition_list[:validation_end_index],
        "test": shuffled_condition_list[validation_end_index:test_end_index],
        "train": shuffled_condition_list[test_end_index:],
    }

    # Validate Split Completeness
    assert all(split_condition_map.values()), "Every configured split must be non-empty"
    assert sum(map(len, split_condition_map.values())) == condition_count, (
        "Split assignment changed the paired-condition count"
    )

    return split_condition_map


def _build_manifest_entry(
    paired_files: DirectionalConditionFiles,
    split_name: str,
    dataset_root: Path,
) -> dict[str, Any]:
    """Build one content-addressed paired-condition record."""

    condition = paired_files.condition
    direction_files: dict[str, dict[str, Any]] = {}
    for direction_name, source_path in (
        ("Fw", paired_files.forward_path),
        ("Bw", paired_files.backward_path),
    ):
        assert source_path.is_relative_to(dataset_root), (
            f"Directional source path escapes dataset root | {source_path}"
        )
        direction_files[direction_name] = {
            "path": _project_relative_path(source_path),
            "size_bytes": source_path.stat().st_size,
            "sha256": _compute_file_sha256(source_path),
        }

    return {
        "condition_id": condition.condition_id,
        "split": split_name,
        "nominal_operating_condition": {
            "input_speed_rpm": condition.input_speed_rpm,
            "output_torque_nm": condition.output_torque_nm,
            "oil_temperature_deg_c": condition.oil_temperature_deg_c,
        },
        "direction_files": direction_files,
    }


def _write_manifest_csv(
    manifest_payload: dict[str, Any],
    manifest_csv_path: Path,
) -> None:
    """Write a flat paired-condition table for audits and downstream tools."""

    field_name_list = [
        "condition_id",
        "split",
        "input_speed_rpm",
        "output_torque_nm",
        "oil_temperature_deg_c",
        "fw_path",
        "fw_size_bytes",
        "fw_sha256",
        "bw_path",
        "bw_size_bytes",
        "bw_sha256",
    ]

    with manifest_csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        csv_writer.writeheader()

        for entry in manifest_payload["entry_list"]:
            operating_condition = entry["nominal_operating_condition"]
            direction_files = entry["direction_files"]
            csv_writer.writerow(
                {
                    "condition_id": entry["condition_id"],
                    "split": entry["split"],
                    "input_speed_rpm": operating_condition["input_speed_rpm"],
                    "output_torque_nm": operating_condition["output_torque_nm"],
                    "oil_temperature_deg_c": operating_condition[
                        "oil_temperature_deg_c"
                    ],
                    "fw_path": direction_files["Fw"]["path"],
                    "fw_size_bytes": direction_files["Fw"]["size_bytes"],
                    "fw_sha256": direction_files["Fw"]["sha256"],
                    "bw_path": direction_files["Bw"]["path"],
                    "bw_size_bytes": direction_files["Bw"]["size_bytes"],
                    "bw_sha256": direction_files["Bw"]["sha256"],
                }
            )


def _build_data_contract_markdown(
    manifest_payload: dict[str, Any],
    manifest_yaml_path: Path,
    manifest_csv_path: Path,
) -> str:
    """Render the common-split provenance and semantic contract."""

    split_count_map = manifest_payload["split"]["condition_count_by_split"]
    paired_condition_count = manifest_payload["dataset"]["paired_condition_count"]
    directional_file_count = manifest_payload["dataset"]["directional_file_count"]
    manifest_yaml_hash = _compute_file_sha256(manifest_yaml_path)
    manifest_csv_hash = _compute_file_sha256(manifest_csv_path)

    return f"""# Polynomial-Fourier Common-Split Data Contract

## Overview

This document freezes the first dataset surface of the Wave 5.2
Polynomial-Fourier benchmark. It is a non-training analytical contract for
comparing the Bauer, recovered ONNX, and PLC formulations on exactly the same
paired forward and backward operating conditions.

## Canonical Inputs

- Dataset: `{manifest_payload["dataset"]["dataset_id"]}`
- Dataset schema: `{manifest_payload["dataset"]["dataset_schema"]}`
- Dataset root: `{manifest_payload["dataset"]["root"]}`
- Assignment unit: `paired_operating_condition`
- Random seed: `{manifest_payload["split"]["random_seed"]}`
- Validation fraction: `{manifest_payload["split"]["validation_fraction"]}`
- Test fraction: `{manifest_payload["split"]["test_fraction"]}`
- Content hash: `SHA-256` for every directional CSV
- Stable split-assignment SHA-256:
  `{manifest_payload["split"]["assignment_sha256"]}`

Nominal speed, torque, and temperature are parsed from each filename and
cross-checked against the speed and temperature parent directories. The exact
ordered CSV schema is checked before a curve enters the manifest.

## Paired Split

| Split | Paired Conditions | Directional Curves |
| --- | ---: | ---: |
| Train | {split_count_map["train"]} | {split_count_map["train"] * 2} |
| Validation | {split_count_map["validation"]} | {split_count_map["validation"] * 2} |
| Test | {split_count_map["test"]} | {split_count_map["test"] * 2} |
| Total | {paired_condition_count} | {directional_file_count} |

The operating-condition key is shuffled once. Its `Fw` and `Bw` files are then
assigned together. No condition or directional file may appear in more than
one split.

## Units And Coordinates

- `theta`: output-equivalent reducer angle in degrees
- `theta_dot`: measured input or motor-side speed in revolutions per minute
- `tau_load`: measured signed output-side torque in newton-metres
- `T`: measured oil temperature in degrees Celsius
- `theta_TE`: measured transmission error in degrees

The directory direction is authoritative for the `Fw` or `Bw` surface. The
filename values define the nominal operating-condition key; measured
condition channels inside each curve remain available for later formulation
audits and must not be silently replaced by the nominal values.

## Immutable Artifacts

- YAML manifest: `{_project_relative_path(manifest_yaml_path)}`
  - SHA-256: `{manifest_yaml_hash}`
- CSV manifest: `{_project_relative_path(manifest_csv_path)}`
  - SHA-256: `{manifest_csv_hash}`
- Source configuration:
  `{manifest_payload["source_configuration"]["path"]}`
  - SHA-256: `{manifest_payload["source_configuration"]["sha256"]}`

The YAML file is the canonical machine-readable manifest. The CSV file is a
flat audit view. Each entry records the nominal condition, split, Fw and Bw
paths, file sizes, and source hashes.

## Validation Gates

The repository validator confirms:

1. exact equality of the Fw and Bw operating-condition sets;
2. one paired entry per nominal condition;
3. split disjointness at condition level;
4. unique directional source paths;
5. exact CSV header compatibility;
6. current source-file sizes and SHA-256 hashes;
7. source-configuration identity and stable assignment signature;
8. agreement between the YAML manifest and flat CSV audit rows;
9. agreement between declared and recomputed split counts.

This contract completes only the common-data portion of benchmark Phase 1.
The Bauer, recovered ONNX, and PLC formulation reproductions remain pending.
"""


def _resolve_project_path(path_value: str | Path) -> Path:
    """Resolve a repository-relative or absolute path."""

    path = Path(path_value)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path.resolve()


def _project_relative_path(path: Path) -> str:
    """Return a forward-slash repository-relative path."""

    return path.resolve().relative_to(PROJECT_ROOT).as_posix()


def _compute_file_sha256(file_path: Path) -> str:
    """Compute a file SHA-256 without loading the whole file into memory."""

    digest = hashlib.sha256()
    with file_path.open("rb") as source_file:
        for file_chunk in iter(lambda: source_file.read(1024 * 1024), b""):
            digest.update(file_chunk)
    return digest.hexdigest()


def _compute_assignment_sha256(manifest_entry_list: list[dict[str, Any]]) -> str:
    """Compute a stable signature over split, condition, paths, and hashes."""

    canonical_assignment_text = json.dumps(
        manifest_entry_list,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    )
    return hashlib.sha256(canonical_assignment_text.encode("utf-8")).hexdigest()


def _format_number(number: float) -> str:
    """Format an integral float without a redundant decimal suffix."""

    if number.is_integer():
        return str(int(number))
    return format(number, ".12g")
