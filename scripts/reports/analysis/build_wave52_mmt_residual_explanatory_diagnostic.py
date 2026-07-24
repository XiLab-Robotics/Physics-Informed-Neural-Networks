"""Build the Wave 5.2 MMT residual-explanatory diagnostic.

This script audits the exact dataset split used by the selected polished
setpoint baselines, joins that provenance to existing per-curve residual
metrics, materializes leakage-safe MMT signatures, and runs transparent
least-squares comparisons only when training residual rows are available.

The diagnostic is intentionally non-training. It must not create campaign
state, update registries, or fit explanatory coefficients on validation or
test targets.
"""

from __future__ import annotations

# Import Standard Libraries
import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
import random
from statistics import fmean
from statistics import pstdev
import sys
from typing import Any

# Import Numerical And Configuration Libraries
import numpy as np
import yaml

# Resolve Project Imports
PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.features.wave4b_mmt_feature_generator import generate_wave4b_feature_payload


DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "analysis"
    / "wave52_mmt_residual_explanatory_diagnostic.yaml"
)
DEFAULT_FLOAT_FORMAT = ".9f"
MISSING_RESIDUAL_DECISION = "blocked_by_missing_training_residuals"
PARAMETER_BLOCKED_DECISION = "blocked_by_parameter_availability"
DIAGNOSTIC_ONLY_DECISION = "diagnostic_only"
FEATURE_PILOT_DECISION = "feature_or_auxiliary_pilot_justified"


@dataclass(frozen=True)
class BaselineSpecification:

    """Describe one selected baseline and its provenance surfaces.

    Attributes:
        candidate_id: Candidate identifier used by curve-verification outputs.
        surface: Directional project surface label.
        direction_label: Dataset direction label.
        architecture_class: Windowed or non-windowed comparison class.
        registry_path: Dataset-scoped family registry.
        reference_inventory_path: Archived model reference inventory.
    """

    candidate_id: str
    surface: str
    direction_label: str
    architecture_class: str
    registry_path: Path
    reference_inventory_path: Path


@dataclass(frozen=True)
class LinearFitResult:

    """Store one transparent held-out linear-fit result.

    Attributes:
        coefficient_vector: Fitted intercept and standardized coefficients.
        matrix_rank: Least-squares design-matrix rank.
        train_mae: Mean absolute error on the fit split.
        evaluation_mae: Mean absolute error on the evaluation split.
        evaluation_r_squared: Held-out coefficient of determination.
    """

    coefficient_vector: np.ndarray
    matrix_rank: int
    train_mae: float
    evaluation_mae: float
    evaluation_r_squared: float


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the diagnostic builder."""

    parser = argparse.ArgumentParser(
        description=(
            "Build the non-training Wave 5.2 MMT residual-explanatory "
            "diagnostic from repository-owned provenance and residual artifacts."
        )
    )
    parser.add_argument(
        "--config-path",
        default=str(DEFAULT_CONFIG_PATH),
        help="Diagnostic YAML configuration path.",
    )
    parser.add_argument(
        "--run-instance-id",
        default=None,
        help="Optional stable run instance identifier for deterministic reruns.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run the bounded synthetic least-squares fixture before the real diagnostic.",
    )
    return parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:

    """Resolve a repository-relative or absolute path."""

    candidate_path = Path(path_value)
    if candidate_path.is_absolute():
        return candidate_path.resolve()
    return (PROJECT_PATH / candidate_path).resolve()


def format_project_path(path_value: str | Path) -> str:

    """Format one path relative to the repository when possible."""

    resolved_path = resolve_project_path(path_value)
    try:
        return resolved_path.relative_to(PROJECT_PATH).as_posix()
    except ValueError:
        return resolved_path.as_posix()


def format_float(value: float | int | str | None) -> str:

    """Format one optional numerical value for stable CSV output."""

    if value in [None, ""]:
        return ""
    return format(float(value), DEFAULT_FLOAT_FORMAT)


def load_yaml_dictionary(path_value: str | Path) -> dict[str, Any]:

    """Load one YAML file and require a dictionary root."""

    yaml_path = resolve_project_path(path_value)
    assert yaml_path.exists(), f"YAML path does not exist | {yaml_path}"
    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        payload = yaml.safe_load(yaml_file)
    assert isinstance(payload, dict), f"YAML root must be a dictionary | {yaml_path}"
    return payload


def write_yaml(path_value: str | Path, payload: dict[str, Any]) -> Path:

    """Write a stable YAML dictionary."""

    output_path = resolve_project_path(path_value)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=False)
    return output_path


def write_json(path_value: str | Path, payload: dict[str, Any]) -> Path:

    """Write one readable JSON dictionary."""

    output_path = resolve_project_path(path_value)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        json.dump(payload, output_file, indent=2, sort_keys=False)
        output_file.write("\n")
    return output_path


def write_csv(path_value: str | Path, row_list: list[dict[str, Any]]) -> Path:

    """Write a non-empty dictionary row list to CSV."""

    output_path = resolve_project_path(path_value)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    assert row_list, f"CSV row list is empty | {output_path}"
    field_name_list = list(row_list[0].keys())
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)
    return output_path


def load_config(config_path: Path) -> dict[str, Any]:

    """Load and validate the diagnostic configuration."""

    config_dictionary = load_yaml_dictionary(config_path)
    assert int(config_dictionary.get("schema_version", 0)) == 1, (
        f"Unsupported diagnostic schema version | {config_dictionary.get('schema_version')}"
    )

    metadata_dictionary = config_dictionary.get("metadata", {})
    assert metadata_dictionary.get("training_allowed") is False, (
        "Diagnostic configuration must keep training disabled"
    )
    assert metadata_dictionary.get("registry_update_allowed") is False, (
        "Diagnostic configuration must keep registry updates disabled"
    )
    assert config_dictionary.get("baselines"), "At least one baseline is required"
    assert config_dictionary.get("comparison", {}).get("residual_target_name_list"), (
        "Residual target list is required"
    )
    return config_dictionary


def build_baseline_specification_list(
    config_dictionary: dict[str, Any],
) -> list[BaselineSpecification]:

    """Build strongly typed baseline specifications from configuration."""

    specification_list: list[BaselineSpecification] = []
    for baseline_dictionary in config_dictionary["baselines"]:
        specification_list.append(
            BaselineSpecification(
                candidate_id=str(baseline_dictionary["candidate_id"]),
                surface=str(baseline_dictionary["surface"]),
                direction_label=str(baseline_dictionary["direction_label"]).lower(),
                architecture_class=str(baseline_dictionary["architecture_class"]),
                registry_path=resolve_project_path(baseline_dictionary["registry_path"]),
                reference_inventory_path=resolve_project_path(
                    baseline_dictionary["reference_inventory_path"]
                ),
            )
        )

    candidate_id_list = [entry.candidate_id for entry in specification_list]
    assert len(candidate_id_list) == len(set(candidate_id_list)), (
        f"Duplicate baseline candidate identifiers | {candidate_id_list}"
    )
    return specification_list


def build_dataset_split_lookup(
    dataset_root: Path,
    validation_split: float,
    test_split: float,
    random_seed: int,
) -> tuple[dict[str, str], dict[str, int]]:

    """Reconstruct the repository file-level split without importing training.

    The implementation mirrors
    ``scripts.datasets.transmission_error_dataset.split_directional_file_manifest``:
    sorted unique CSV paths are shuffled by ``random.Random`` and the validation
    and test prefixes are selected from that deterministic list.
    """

    assert dataset_root.exists(), f"Dataset root does not exist | {dataset_root}"
    assert 0.0 < validation_split < 1.0, (
        f"Validation split must be between zero and one | {validation_split}"
    )
    assert 0.0 <= test_split < 1.0, (
        f"Test split must be between zero and one | {test_split}"
    )
    assert validation_split + test_split < 1.0, (
        f"Validation and test splits must leave training data | "
        f"{validation_split} + {test_split}"
    )

    csv_path_list = sorted(dataset_root.rglob("*.csv"))
    assert len(csv_path_list) >= 2, f"Insufficient dataset CSV files | {dataset_root}"

    random_generator = random.Random(random_seed)
    random_generator.shuffle(csv_path_list)

    validation_file_count = max(1, int(round(len(csv_path_list) * validation_split)))
    if validation_file_count >= len(csv_path_list):
        validation_file_count = len(csv_path_list) - 1

    remaining_file_count = len(csv_path_list) - validation_file_count
    test_file_count = int(round(len(csv_path_list) * test_split))
    if test_split > 0.0:
        test_file_count = max(1, test_file_count)
    if test_file_count >= remaining_file_count:
        test_file_count = remaining_file_count - 1

    validation_path_set = set(csv_path_list[:validation_file_count])
    test_path_set = set(
        csv_path_list[
            validation_file_count : validation_file_count + test_file_count
        ]
    )

    split_lookup: dict[str, str] = {}
    for csv_path in csv_path_list:
        split_name = "train"
        if csv_path in validation_path_set:
            split_name = "validation"
        elif csv_path in test_path_set:
            split_name = "test"
        split_lookup[str(csv_path.resolve()).lower()] = split_name

    split_count_dictionary = {
        "total": len(csv_path_list),
        "train": len(csv_path_list) - validation_file_count - test_file_count,
        "validation": validation_file_count,
        "test": test_file_count,
    }
    return split_lookup, split_count_dictionary


def load_selected_residual_row_list(
    residual_metrics_path: Path,
    baseline_specification_list: list[BaselineSpecification],
    split_lookup: dict[str, str] | None,
    residual_target_name_list: list[str],
) -> list[dict[str, Any]]:

    """Load selected baseline residual rows with authoritative split labels."""

    assert residual_metrics_path.exists(), (
        f"Residual metrics path does not exist | {residual_metrics_path}"
    )
    baseline_dictionary = {
        entry.candidate_id: entry for entry in baseline_specification_list
    }
    selected_row_list: list[dict[str, Any]] = []

    with residual_metrics_path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        assert reader.fieldnames is not None, (
            f"Residual CSV has no header | {residual_metrics_path}"
        )
        required_column_set = {
            "candidate_id",
            "candidate_surface",
            "direction_label",
            "source_file_path",
            "speed_rpm",
            "torque_nm",
            "oil_temperature_deg",
            *residual_target_name_list,
        }
        source_has_split_labels = "split_name" in reader.fieldnames
        assert source_has_split_labels or split_lookup is not None, (
            "Residual CSV must contain split_name or receive a split lookup"
        )
        missing_column_set = required_column_set.difference(reader.fieldnames)
        assert not missing_column_set, (
            f"Residual CSV is missing required columns | {sorted(missing_column_set)}"
        )

        for source_row in reader:
            candidate_id = str(source_row["candidate_id"])
            if candidate_id not in baseline_dictionary:
                continue

            specification = baseline_dictionary[candidate_id]
            source_file_path = resolve_project_path(source_row["source_file_path"])
            if source_has_split_labels:
                split_name = str(source_row["split_name"]).strip().lower()
                assert split_name in {"train", "validation", "test"}, (
                    f"Unsupported residual split label | {split_name}"
                )
            else:
                assert split_lookup is not None
                split_name = split_lookup.get(str(source_file_path).lower())
                assert split_name is not None, (
                    f"Residual source path is absent from the dataset split | "
                    f"{source_file_path}"
                )
            assert str(source_row["direction_label"]).lower() == (
                specification.direction_label
            ), (
                f"Residual direction does not match baseline specification | "
                f"{candidate_id} | {source_row['direction_label']}"
            )

            selected_row: dict[str, Any] = {
                "candidate_id": candidate_id,
                "surface": specification.surface,
                "direction_label": specification.direction_label,
                "architecture_class": specification.architecture_class,
                "split_name": split_name,
                "source_file_path": format_project_path(source_file_path),
                "speed_rpm": format_float(source_row["speed_rpm"]),
                "torque_nm": format_float(source_row["torque_nm"]),
                "oil_temperature_deg": format_float(
                    source_row["oil_temperature_deg"]
                ),
            }
            for residual_target_name in residual_target_name_list:
                selected_row[residual_target_name] = format_float(
                    source_row[residual_target_name]
                )
            selected_row_list.append(selected_row)

    expected_candidate_id_set = set(baseline_dictionary)
    found_candidate_id_set = {row["candidate_id"] for row in selected_row_list}
    assert found_candidate_id_set == expected_candidate_id_set, (
        f"Residual metrics do not cover every configured baseline | "
        f"Expected: {sorted(expected_candidate_id_set)} | "
        f"Found: {sorted(found_candidate_id_set)}"
    )
    return selected_row_list


def build_split_count_dictionary_from_residual_rows(
    residual_row_list: list[dict[str, Any]],
) -> dict[str, int]:

    """Count unique dataset files using replay-provided split membership."""

    path_split_dictionary: dict[str, str] = {}
    for row in residual_row_list:
        source_file_path = str(row["source_file_path"]).lower()
        split_name = str(row["split_name"])
        previous_split_name = path_split_dictionary.get(source_file_path)
        assert previous_split_name in {None, split_name}, (
            "One source curve has conflicting split labels across baselines | "
            f"{row['source_file_path']} | {previous_split_name} vs {split_name}"
        )
        path_split_dictionary[source_file_path] = split_name

    split_count_dictionary = {
        split_name: sum(
            value == split_name for value in path_split_dictionary.values()
        )
        for split_name in ["train", "validation", "test"]
    }
    split_count_dictionary["total"] = len(path_split_dictionary)
    return split_count_dictionary


def build_baseline_manifest_row_list(
    baseline_specification_list: list[BaselineSpecification],
) -> list[dict[str, Any]]:

    """Resolve registry and archived-model provenance for each baseline."""

    manifest_row_list: list[dict[str, Any]] = []
    for specification in baseline_specification_list:
        registry_dictionary = load_yaml_dictionary(specification.registry_path)
        inventory_dictionary = load_yaml_dictionary(
            specification.reference_inventory_path
        )
        best_entry_dictionary = registry_dictionary.get("best_entry", {})

        onnx_model_path = resolve_project_path(
            inventory_dictionary["onnx_model_path"]
        )
        python_model_path = resolve_project_path(
            inventory_dictionary["python_model_path"]
        )
        training_config_snapshot_path = resolve_project_path(
            inventory_dictionary["source_run_snapshot_path_map"][
                "training_config.snapshot.yaml"
            ]
        )

        manifest_row_list.append(
            {
                "candidate_id": specification.candidate_id,
                "surface": specification.surface,
                "direction_label": specification.direction_label,
                "architecture_class": specification.architecture_class,
                "registry_path": format_project_path(specification.registry_path),
                "registry_run_instance_id": str(
                    best_entry_dictionary.get("run_instance_id", "")
                ),
                "reference_inventory_path": format_project_path(
                    specification.reference_inventory_path
                ),
                "archive_run_instance_id": str(
                    inventory_dictionary.get("run_instance_id", "")
                ),
                "dataset_id": str(inventory_dictionary.get("dataset_id", "")),
                "dataset_schema": str(
                    inventory_dictionary.get("dataset_schema", "")
                ),
                "input_mode": str(inventory_dictionary.get("input_mode", "")),
                "onnx_model_path": format_project_path(onnx_model_path),
                "onnx_model_exists": onnx_model_path.exists(),
                "python_model_path": format_project_path(python_model_path),
                "python_model_exists": python_model_path.exists(),
                "training_config_snapshot_path": format_project_path(
                    training_config_snapshot_path
                ),
                "training_config_snapshot_exists": (
                    training_config_snapshot_path.exists()
                ),
            }
        )

    assert all(row["onnx_model_exists"] for row in manifest_row_list), (
        "One or more archived ONNX baseline models are missing"
    )
    assert all(row["python_model_exists"] for row in manifest_row_list), (
        "One or more archived Python baseline models are missing"
    )
    assert all(
        row["training_config_snapshot_exists"] for row in manifest_row_list
    ), "One or more baseline training-config snapshots are missing"
    return manifest_row_list


def build_split_audit_row_list(
    residual_row_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    """Build per-candidate split coverage rows."""

    count_dictionary: dict[tuple[str, str, str, str], int] = {}
    for row in residual_row_list:
        key = (
            str(row["candidate_id"]),
            str(row["surface"]),
            str(row["architecture_class"]),
            str(row["split_name"]),
        )
        count_dictionary[key] = count_dictionary.get(key, 0) + 1

    return [
        {
            "candidate_id": key[0],
            "surface": key[1],
            "architecture_class": key[2],
            "split_name": key[3],
            "residual_row_count": count,
            "fit_allowed": key[3] == "train",
        }
        for key, count in sorted(count_dictionary.items())
    ]


def build_mmt_signature_row_list(
    config_dictionary: dict[str, Any],
) -> list[dict[str, Any]]:

    """Materialize the current geometry-locked MMT signature inventory."""

    mmt_dictionary = config_dictionary["mmt"]
    payload = generate_wave4b_feature_payload(
        sample_count=int(mmt_dictionary["sample_count"]),
        harmonic_index_list=[
            int(value) for value in mmt_dictionary["harmonic_index_list"]
        ],
    )

    signature_row_list: list[dict[str, Any]] = []
    sample_row_list = payload.sample_row_list
    assert sample_row_list, "MMT feature payload contains no sample rows"

    first_sample_row = sample_row_list[0]
    signature_row_list.extend(
        [
            {
                "signature_name": "mmt_rte_mean_arcsec",
                "signature_group": "geometry_locked_curve_summary",
                "harmonic_index": "",
                "value": first_sample_row["mmt_rte_mean_arcsec"],
                "usage_policy": "inference_safe",
                "condition_varying": False,
                "notes": "Current MMT demo value is fixed across operating conditions.",
            },
            {
                "signature_name": "mmt_rte_peak_to_peak_arcsec",
                "signature_group": "geometry_locked_curve_summary",
                "harmonic_index": "",
                "value": first_sample_row["mmt_rte_peak_to_peak_arcsec"],
                "usage_policy": "inference_safe",
                "condition_varying": False,
                "notes": "Current MMT demo value is fixed across operating conditions.",
            },
        ]
    )

    for harmonic_row in payload.harmonic_row_list:
        if not harmonic_row["is_available"]:
            continue
        signature_row_list.append(
            {
                "signature_name": "mmt_harmonic_amplitude_arcsec",
                "signature_group": "geometry_locked_harmonic",
                "harmonic_index": harmonic_row["harmonic_index"],
                "value": harmonic_row["mmt_harmonic_amplitude_arcsec"],
                "usage_policy": harmonic_row["usage_policy"],
                "condition_varying": False,
                "notes": (
                    "Current analytical signature is geometry-locked and has no "
                    "validated speed, torque, or temperature calibration."
                ),
            }
        )
        signature_row_list.append(
            {
                "signature_name": "mmt_harmonic_phase_rad",
                "signature_group": "geometry_locked_harmonic",
                "harmonic_index": harmonic_row["harmonic_index"],
                "value": harmonic_row["mmt_harmonic_phase_rad"],
                "usage_policy": harmonic_row["usage_policy"],
                "condition_varying": False,
                "notes": (
                    "Current analytical signature is geometry-locked and has no "
                    "validated speed, torque, or temperature calibration."
                ),
            }
        )
    return signature_row_list


def build_descriptive_summary_row_list(
    residual_row_list: list[dict[str, Any]],
    residual_target_name_list: list[str],
) -> list[dict[str, Any]]:

    """Summarize residual targets without fitting on held-out data."""

    candidate_id_list = sorted({str(row["candidate_id"]) for row in residual_row_list})
    summary_row_list: list[dict[str, Any]] = []
    for candidate_id in candidate_id_list:
        for split_name in ["train", "validation", "test"]:
            candidate_row_list = [
                row
                for row in residual_row_list
                if row["candidate_id"] == candidate_id
                and row["split_name"] == split_name
            ]
            assert candidate_row_list, (
                f"Missing descriptive split coverage | {candidate_id} | {split_name}"
            )
            for target_name in residual_target_name_list:
                value_list = [float(row[target_name]) for row in candidate_row_list]
                summary_row_list.append(
                    {
                        "candidate_id": candidate_id,
                        "surface": candidate_row_list[0]["surface"],
                        "architecture_class": candidate_row_list[0][
                            "architecture_class"
                        ],
                        "split_name": split_name,
                        "target_name": target_name,
                        "row_count": len(value_list),
                        "mean": format_float(fmean(value_list)),
                        "standard_deviation": format_float(pstdev(value_list)),
                        "minimum": format_float(min(value_list)),
                        "maximum": format_float(max(value_list)),
                        "fit_performed": False,
                    }
                )
    return summary_row_list


def standardize_matrix_from_training(
    training_matrix: np.ndarray,
    evaluation_matrix: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:

    """Standardize feature matrices with training statistics only."""

    training_matrix = np.asarray(training_matrix, dtype=float)
    evaluation_matrix = np.asarray(evaluation_matrix, dtype=float)
    assert training_matrix.ndim == 2, (
        f"Training feature matrix must be rank two | {training_matrix.shape}"
    )
    assert evaluation_matrix.ndim == 2, (
        f"Evaluation feature matrix must be rank two | {evaluation_matrix.shape}"
    )
    assert training_matrix.shape[1] == evaluation_matrix.shape[1], (
        f"Feature width mismatch | {training_matrix.shape} vs "
        f"{evaluation_matrix.shape}"
    )

    training_mean = np.mean(training_matrix, axis=0)
    training_standard_deviation = np.std(training_matrix, axis=0)
    safe_standard_deviation = np.where(
        training_standard_deviation > 1.0e-12,
        training_standard_deviation,
        1.0,
    )
    return (
        (training_matrix - training_mean) / safe_standard_deviation,
        (evaluation_matrix - training_mean) / safe_standard_deviation,
    )


def compute_r_squared(
    target_vector: np.ndarray,
    prediction_vector: np.ndarray,
) -> float:

    """Compute a finite coefficient of determination."""

    target_vector = np.asarray(target_vector, dtype=float).reshape(-1)
    prediction_vector = np.asarray(prediction_vector, dtype=float).reshape(-1)
    assert target_vector.shape == prediction_vector.shape, (
        f"Target and prediction shapes differ | {target_vector.shape} vs "
        f"{prediction_vector.shape}"
    )
    residual_sum_of_squares = float(
        np.sum(np.square(target_vector - prediction_vector))
    )
    centered_target_vector = target_vector - float(np.mean(target_vector))
    total_sum_of_squares = float(np.sum(np.square(centered_target_vector)))
    if total_sum_of_squares <= 1.0e-18:
        return 0.0
    return 1.0 - residual_sum_of_squares / total_sum_of_squares


def fit_transparent_linear_model(
    training_feature_matrix: np.ndarray,
    training_target_vector: np.ndarray,
    evaluation_feature_matrix: np.ndarray,
    evaluation_target_vector: np.ndarray,
) -> LinearFitResult:

    """Fit least squares on training data and score held-out data."""

    standardized_training_matrix, standardized_evaluation_matrix = (
        standardize_matrix_from_training(
            training_feature_matrix,
            evaluation_feature_matrix,
        )
    )
    training_design_matrix = np.column_stack(
        [
            np.ones(standardized_training_matrix.shape[0], dtype=float),
            standardized_training_matrix,
        ]
    )
    evaluation_design_matrix = np.column_stack(
        [
            np.ones(standardized_evaluation_matrix.shape[0], dtype=float),
            standardized_evaluation_matrix,
        ]
    )

    training_target_vector = np.asarray(training_target_vector, dtype=float)
    evaluation_target_vector = np.asarray(evaluation_target_vector, dtype=float)
    coefficient_vector, _, matrix_rank, _ = np.linalg.lstsq(
        training_design_matrix,
        training_target_vector,
        rcond=None,
    )
    training_prediction_vector = training_design_matrix @ coefficient_vector
    evaluation_prediction_vector = evaluation_design_matrix @ coefficient_vector

    return LinearFitResult(
        coefficient_vector=coefficient_vector,
        matrix_rank=int(matrix_rank),
        train_mae=float(
            np.mean(np.abs(training_target_vector - training_prediction_vector))
        ),
        evaluation_mae=float(
            np.mean(
                np.abs(evaluation_target_vector - evaluation_prediction_vector)
            )
        ),
        evaluation_r_squared=compute_r_squared(
            evaluation_target_vector,
            evaluation_prediction_vector,
        ),
    )


def run_bounded_self_test(random_seed: int) -> dict[str, Any]:

    """Verify the least-squares and shuffled-control helpers synthetically."""

    random_generator = np.random.default_rng(random_seed)
    metadata_matrix = random_generator.normal(size=(120, 3))
    mmt_signature_vector = random_generator.normal(size=120)
    target_vector = (
        0.4 * metadata_matrix[:, 0]
        - 0.2 * metadata_matrix[:, 1]
        + 0.8 * mmt_signature_vector
        + random_generator.normal(scale=0.05, size=120)
    )

    training_index_array = np.arange(0, 90)
    evaluation_index_array = np.arange(90, 120)
    metadata_result = fit_transparent_linear_model(
        metadata_matrix[training_index_array],
        target_vector[training_index_array],
        metadata_matrix[evaluation_index_array],
        target_vector[evaluation_index_array],
    )
    combined_matrix = np.column_stack([metadata_matrix, mmt_signature_vector])
    combined_result = fit_transparent_linear_model(
        combined_matrix[training_index_array],
        target_vector[training_index_array],
        combined_matrix[evaluation_index_array],
        target_vector[evaluation_index_array],
    )
    shuffled_signature_vector = random_generator.permutation(mmt_signature_vector)
    shuffled_matrix = np.column_stack(
        [metadata_matrix, shuffled_signature_vector]
    )
    shuffled_result = fit_transparent_linear_model(
        shuffled_matrix[training_index_array],
        target_vector[training_index_array],
        shuffled_matrix[evaluation_index_array],
        target_vector[evaluation_index_array],
    )

    assert combined_result.evaluation_r_squared > (
        metadata_result.evaluation_r_squared
    ), "Synthetic combined comparison should outperform metadata only"
    assert combined_result.evaluation_r_squared > (
        shuffled_result.evaluation_r_squared
    ), "Synthetic combined comparison should outperform shuffled control"
    return {
        "status": "passed",
        "random_seed": int(random_seed),
        "metadata_only_evaluation_r_squared": float(
            metadata_result.evaluation_r_squared
        ),
        "combined_evaluation_r_squared": float(
            combined_result.evaluation_r_squared
        ),
        "shuffled_evaluation_r_squared": float(
            shuffled_result.evaluation_r_squared
        ),
    }


def build_comparison_row_list(
    residual_row_list: list[dict[str, Any]],
    baseline_specification_list: list[BaselineSpecification],
    config_dictionary: dict[str, Any],
) -> tuple[list[dict[str, Any]], str, list[str]]:

    """Fit allowed controls and expose unavailable physical calibration."""

    comparison_dictionary = config_dictionary["comparison"]
    metadata_feature_name_list = [
        str(value)
        for value in comparison_dictionary["metadata_feature_name_list"]
    ]
    residual_target_name_list = [
        str(value)
        for value in comparison_dictionary["residual_target_name_list"]
    ]
    comparison_name_list = [
        str(value) for value in comparison_dictionary["comparison_name_list"]
    ]
    training_row_count = sum(
        row["split_name"] == "train" for row in residual_row_list
    )
    validation_row_count = sum(
        row["split_name"] == "validation" for row in residual_row_list
    )
    test_row_count = sum(
        row["split_name"] == "test" for row in residual_row_list
    )

    blocker_list: list[str] = []
    if training_row_count == 0:
        blocker_list.append(
            "configured residual artifact contains no training residual rows"
        )
    if validation_row_count == 0:
        blocker_list.append(
            "configured residual artifact contains no validation residual rows"
        )
    if test_row_count == 0:
        blocker_list.append(
            "configured residual artifact contains no held-out test residual rows"
        )

    comparison_row_list: list[dict[str, Any]] = []
    if training_row_count == 0 or validation_row_count == 0 or test_row_count == 0:
        for specification in baseline_specification_list:
            for target_name in residual_target_name_list:
                for comparison_name in comparison_name_list:
                    comparison_row_list.append(
                        {
                            "candidate_id": specification.candidate_id,
                            "surface": specification.surface,
                            "architecture_class": specification.architecture_class,
                            "target_name": target_name,
                            "comparison_name": comparison_name,
                            "evaluation_split": "",
                            "fit_status": MISSING_RESIDUAL_DECISION,
                            "training_row_count": training_row_count,
                            "validation_row_count": validation_row_count,
                            "test_row_count": test_row_count,
                            "matrix_rank": "",
                            "coefficient_vector_json": "",
                            "train_mae": "",
                            "evaluation_mae": "",
                            "evaluation_r_squared": "",
                            "mae_improvement_vs_metadata": "",
                            "r_squared_delta_vs_metadata": "",
                            "decision_eligible": False,
                            "notes": (
                                "No coefficients were fitted because required "
                                "split coverage is incomplete."
                            ),
                        }
                    )
        return (
            comparison_row_list,
            MISSING_RESIDUAL_DECISION,
            blocker_list,
        )

    blocker_list.extend(
        [
            (
                "train-only equivalent-error groups are unavailable as causal "
                "condition-level inputs and cannot be physically calibrated"
            ),
            (
                "current geometry-locked MMT signatures are invariant across "
                "operating conditions and collapse to the fitted intercept"
            ),
        ]
    )

    mmt_signature_row_list = build_mmt_signature_row_list(config_dictionary)
    geometry_signature_vector = np.asarray(
        [float(row["value"]) for row in mmt_signature_row_list],
        dtype=float,
    )
    assert geometry_signature_vector.size > 0
    evaluation_split_name_list = [
        str(value) for value in config_dictionary["split"]["evaluation_split_list"]
    ]
    random_generator = np.random.default_rng(
        int(config_dictionary["metadata"]["random_seed"])
    )

    for specification in baseline_specification_list:
        candidate_row_list = [
            row
            for row in residual_row_list
            if row["candidate_id"] == specification.candidate_id
        ]
        training_row_list = [
            row for row in candidate_row_list if row["split_name"] == "train"
        ]
        assert training_row_list, (
            f"Candidate has no training residual rows | {specification.candidate_id}"
        )
        training_metadata_matrix = np.asarray(
            [
                [float(row[name]) for name in metadata_feature_name_list]
                for row in training_row_list
            ],
            dtype=float,
        )
        training_geometry_matrix = np.repeat(
            geometry_signature_vector.reshape(1, -1),
            len(training_row_list),
            axis=0,
        )

        for evaluation_split_name in evaluation_split_name_list:
            evaluation_row_list = [
                row
                for row in candidate_row_list
                if row["split_name"] == evaluation_split_name
            ]
            assert evaluation_row_list, (
                f"Candidate has no evaluation rows | "
                f"{specification.candidate_id} | {evaluation_split_name}"
            )
            evaluation_metadata_matrix = np.asarray(
                [
                    [float(row[name]) for name in metadata_feature_name_list]
                    for row in evaluation_row_list
                ],
                dtype=float,
            )
            evaluation_geometry_matrix = np.repeat(
                geometry_signature_vector.reshape(1, -1),
                len(evaluation_row_list),
                axis=0,
            )

            for target_name in residual_target_name_list:
                training_target_vector = np.asarray(
                    [float(row[target_name]) for row in training_row_list],
                    dtype=float,
                )
                evaluation_target_vector = np.asarray(
                    [float(row[target_name]) for row in evaluation_row_list],
                    dtype=float,
                )
                metadata_result = fit_transparent_linear_model(
                    training_metadata_matrix,
                    training_target_vector,
                    evaluation_metadata_matrix,
                    evaluation_target_vector,
                )

                fitted_result_dictionary = {
                    "metadata_only": metadata_result,
                    "geometry_locked_mmt": fit_transparent_linear_model(
                        training_geometry_matrix,
                        training_target_vector,
                        evaluation_geometry_matrix,
                        evaluation_target_vector,
                    ),
                    "metadata_plus_geometry_locked_mmt": (
                        fit_transparent_linear_model(
                            np.column_stack(
                                [
                                    training_metadata_matrix,
                                    training_geometry_matrix,
                                ]
                            ),
                            training_target_vector,
                            np.column_stack(
                                [
                                    evaluation_metadata_matrix,
                                    evaluation_geometry_matrix,
                                ]
                            ),
                            evaluation_target_vector,
                        )
                    ),
                }
                shuffled_training_geometry_matrix = (
                    training_geometry_matrix[
                        random_generator.permutation(
                            training_geometry_matrix.shape[0]
                        )
                    ]
                )
                shuffled_evaluation_geometry_matrix = (
                    evaluation_geometry_matrix[
                        random_generator.permutation(
                            evaluation_geometry_matrix.shape[0]
                        )
                    ]
                )
                fitted_result_dictionary["shuffled_mmt_control"] = (
                    fit_transparent_linear_model(
                        np.column_stack(
                            [
                                training_metadata_matrix,
                                shuffled_training_geometry_matrix,
                            ]
                        ),
                        training_target_vector,
                        np.column_stack(
                            [
                                evaluation_metadata_matrix,
                                shuffled_evaluation_geometry_matrix,
                            ]
                        ),
                        evaluation_target_vector,
                    )
                )

                for comparison_name in comparison_name_list:
                    common_row = {
                        "candidate_id": specification.candidate_id,
                        "surface": specification.surface,
                        "architecture_class": specification.architecture_class,
                        "target_name": target_name,
                        "comparison_name": comparison_name,
                        "evaluation_split": evaluation_split_name,
                        "training_row_count": len(training_row_list),
                        "validation_row_count": sum(
                            row["split_name"] == "validation"
                            for row in candidate_row_list
                        ),
                        "test_row_count": sum(
                            row["split_name"] == "test"
                            for row in candidate_row_list
                        ),
                    }
                    if (
                        comparison_name
                        == "train_only_calibrated_equivalent_error"
                    ):
                        comparison_row_list.append(
                            {
                                **common_row,
                                "fit_status": PARAMETER_BLOCKED_DECISION,
                                "matrix_rank": "",
                                "coefficient_vector_json": "",
                                "train_mae": "",
                                "evaluation_mae": "",
                                "evaluation_r_squared": "",
                                "mae_improvement_vs_metadata": "",
                                "r_squared_delta_vs_metadata": "",
                                "decision_eligible": False,
                                "notes": (
                                    "No component-error observations or causal "
                                    "contact-state reconstruction are available; "
                                    "target-derived proxy calibration is forbidden."
                                ),
                            }
                        )
                        continue

                    assert comparison_name in fitted_result_dictionary, (
                        f"Unsupported comparison arm | {comparison_name}"
                    )
                    fit_result = fitted_result_dictionary[comparison_name]
                    comparison_row_list.append(
                        {
                            **common_row,
                            "fit_status": "fitted_training_only",
                            "matrix_rank": fit_result.matrix_rank,
                            "coefficient_vector_json": json.dumps(
                                fit_result.coefficient_vector.tolist()
                            ),
                            "train_mae": format_float(fit_result.train_mae),
                            "evaluation_mae": format_float(
                                fit_result.evaluation_mae
                            ),
                            "evaluation_r_squared": format_float(
                                fit_result.evaluation_r_squared
                            ),
                            "mae_improvement_vs_metadata": format_float(
                                metadata_result.evaluation_mae
                                - fit_result.evaluation_mae
                            ),
                            "r_squared_delta_vs_metadata": format_float(
                                fit_result.evaluation_r_squared
                                - metadata_result.evaluation_r_squared
                            ),
                            "decision_eligible": False,
                            "notes": (
                                "Geometry-locked values are condition-invariant; "
                                "the combined and shuffled arms therefore span "
                                "the same held-out design space as metadata only."
                            ),
                        }
                    )

    return comparison_row_list, PARAMETER_BLOCKED_DECISION, blocker_list


def build_report_markdown(
    run_instance_id: str,
    config_path: Path,
    output_directory: Path,
    residual_metrics_path: Path,
    baseline_manifest_row_list: list[dict[str, Any]],
    split_count_dictionary: dict[str, int],
    split_audit_row_list: list[dict[str, Any]],
    descriptive_summary_row_list: list[dict[str, Any]],
    mmt_signature_row_list: list[dict[str, Any]],
    comparison_row_list: list[dict[str, Any]],
    decision: str,
    blocker_list: list[str],
) -> str:

    """Build the human-readable analytical report."""

    training_residual_row_count = sum(
        int(row["residual_row_count"])
        for row in split_audit_row_list
        if row["split_name"] == "train"
    )
    validation_residual_row_count = sum(
        int(row["residual_row_count"])
        for row in split_audit_row_list
        if row["split_name"] == "validation"
    )
    test_residual_row_count = sum(
        int(row["residual_row_count"])
        for row in split_audit_row_list
        if row["split_name"] == "test"
    )

    report_line_list = [
        "# Wave 5.2 MMT Residual-Explanatory Diagnostic Rerun",
        "",
        "## Overview",
        "",
        "This non-training rerun tests whether repository-available MMT",
        "signatures explain frozen-baseline residual metrics beyond causal",
        "operating metadata. Coefficients are fitted on training rows only;",
        "validation and test rows remain held out.",
        "",
        "## Decision",
        "",
        f"Decision: `{decision}`.",
        "",
        "The exact-manifest replay closes the earlier residual-provenance",
        "blocker. The remaining blocker is physical parameter availability:",
        "geometry-locked MMT values are constant across operating conditions,",
        "while the five equivalent-error groups lack observed causal inputs or",
        "a validated contact-state reconstruction. Target-derived substitutes",
        "were not created.",
        "",
        "## Provenance And Split Isolation",
        "",
        f"- run instance: `{run_instance_id}`;",
        f"- config: `{format_project_path(config_path)}`;",
        f"- residual source: `{format_project_path(residual_metrics_path)}`;",
        f"- output directory: `{format_project_path(output_directory)}`;",
        f"- resolved baselines: `{len(baseline_manifest_row_list)}`;",
        f"- unique dataset files: `{split_count_dictionary['total']}`;",
        f"- train files: `{split_count_dictionary['train']}`;",
        f"- validation files: `{split_count_dictionary['validation']}`;",
        f"- test files: `{split_count_dictionary['test']}`.",
        "",
        "Split membership comes directly from the replayed direction-specific",
        "training snapshots. No global replacement split or held-out fitting was",
        "performed.",
        "",
        "| Residual split | Candidate rows | Policy |",
        "| --- | ---: | --- |",
        f"| train | {training_residual_row_count} | fit allowed |",
        f"| validation | {validation_residual_row_count} | evaluation only |",
        f"| test | {test_residual_row_count} | final held-out evaluation only |",
        "",
        "## MMT Evidence Arms",
        "",
        f"The diagnostic materialized `{len(mmt_signature_row_list)}`",
        "geometry-locked curve-summary and harmonic signature values. It fitted",
        "four permitted arms: metadata only, geometry only, metadata plus",
        "geometry, and metadata plus shuffled geometry. The fifth arm,",
        "train-only calibrated equivalent errors, is recorded as blocked rather",
        "than synthesized from TE targets.",
        "",
        "Because every geometry signature is identical for every operating",
        "condition, standardization maps those columns to zero. Geometry-only",
        "therefore reduces to an intercept; combined and shuffled arms are",
        "algebraically equivalent to metadata only.",
        "",
        "## Held-Out Test Comparison",
        "",
        "| Candidate | Residual target | Metadata MAE | Metadata + MMT MAE | "
        "MAE gain | Shuffled gain |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
    ]

    test_comparison_lookup = {
        (
            str(row["candidate_id"]),
            str(row["target_name"]),
            str(row["comparison_name"]),
        ): row
        for row in comparison_row_list
        if row["evaluation_split"] == "test"
        and row["fit_status"] == "fitted_training_only"
    }
    candidate_target_pair_list = sorted(
        {
            (str(row["candidate_id"]), str(row["target_name"]))
            for row in comparison_row_list
            if row["evaluation_split"] == "test"
        }
    )
    for candidate_id, target_name in candidate_target_pair_list:
        metadata_row = test_comparison_lookup[
            (candidate_id, target_name, "metadata_only")
        ]
        combined_row = test_comparison_lookup[
            (
                candidate_id,
                target_name,
                "metadata_plus_geometry_locked_mmt",
            )
        ]
        shuffled_row = test_comparison_lookup[
            (candidate_id, target_name, "shuffled_mmt_control")
        ]
        report_line_list.append(
            f"| `{candidate_id}` | `{target_name}` | "
            f"{float(metadata_row['evaluation_mae']):.6f} | "
            f"{float(combined_row['evaluation_mae']):.6f} | "
            f"{float(combined_row['mae_improvement_vs_metadata']):.9f} | "
            f"{float(shuffled_row['mae_improvement_vs_metadata']):.9f} |"
        )

    test_summary_lookup: dict[tuple[str, str], str] = {
        (str(row["candidate_id"]), str(row["target_name"])): str(row["mean"])
        for row in descriptive_summary_row_list
        if row["split_name"] == "test"
    }
    report_line_list.extend(
        [
            "",
            "All metadata-plus-MMT and shuffled gains are expected to be numerical",
            "zero because the available MMT design columns are constant. This is",
            "a structural result, not evidence that the underlying mechanical",
            "equations are false.",
            "",
            "## Descriptive Test Evidence",
            "",
            "| Candidate | Raw MAE [deg] | Centered MAE [deg] |",
            "| --- | ---: | ---: |",
        ]
    )
    for manifest_row in baseline_manifest_row_list:
        candidate_id = str(manifest_row["candidate_id"])
        report_line_list.append(
            f"| `{candidate_id}` | "
            f"{float(test_summary_lookup[(candidate_id, 'raw_mae_deg')]):.6f} | "
            f"{float(test_summary_lookup[(candidate_id, 'centered_mae_deg')]):.6f} |"
        )

    report_line_list.extend(["", "## Blockers", ""])
    for blocker in blocker_list:
        report_line_list.append(f"- {blocker}.")

    report_line_list.extend(
        [
            "",
            "## Next Action",
            "",
            "Keep MMT diagnostic-only. Do not prepare an MMT feature, auxiliary",
            "head, weak soft constraint, full PINN, or Wave 6 campaign from this",
            "evidence. Reopen the gate only after independent component-error",
            "measurements or a validated causal contact-state reconstruction",
            "provides condition-varying MMT inputs without using held-out TE.",
            "",
            "## Machine-Readable Artifacts",
            "",
            f"- baseline manifest: `{format_project_path(output_directory / 'resolved_baseline_manifest.yaml')}`;",
            f"- split audit: `{format_project_path(output_directory / 'split_boundary_audit.csv')}`;",
            f"- residual features: `{format_project_path(output_directory / 'per_curve_residual_features.csv')}`;",
            f"- MMT signatures: `{format_project_path(output_directory / 'mmt_signature_table.csv')}`;",
            f"- descriptive summary: `{format_project_path(output_directory / 'descriptive_split_summary.csv')}`;",
            f"- comparison table: `{format_project_path(output_directory / 'explanatory_comparison.csv')}`;",
            f"- decision summary: `{format_project_path(output_directory / 'decision_summary.yaml')}`;",
            f"- validation summary: `{format_project_path(output_directory / 'validation_summary.yaml')}`.",
            "",
        ]
    )
    return "\n".join(report_line_list)


def execute_diagnostic(
    config_path: Path,
    run_instance_id: str,
    run_self_test: bool,
) -> dict[str, Any]:

    """Execute the bounded non-training diagnostic."""

    config_dictionary = load_config(config_path)
    metadata_dictionary = config_dictionary["metadata"]
    path_dictionary = config_dictionary["paths"]
    split_dictionary = config_dictionary["split"]
    comparison_dictionary = config_dictionary["comparison"]

    output_root = resolve_project_path(path_dictionary["output_root"])
    output_directory = output_root / run_instance_id
    output_directory.mkdir(parents=True, exist_ok=False)
    report_path = resolve_project_path(path_dictionary["report_path"])
    residual_metrics_path = resolve_project_path(
        path_dictionary["residual_metrics_path"]
    )

    # Run Optional Numerical Fixture
    self_test_summary: dict[str, Any] | None = None
    if run_self_test:
        self_test_summary = run_bounded_self_test(
            int(metadata_dictionary["random_seed"])
        )
        write_yaml(output_directory / "self_test_summary.yaml", self_test_summary)

    # Resolve Baselines And Dataset Split
    baseline_specification_list = build_baseline_specification_list(
        config_dictionary
    )
    baseline_manifest_row_list = build_baseline_manifest_row_list(
        baseline_specification_list
    )
    dataset_root = resolve_project_path(path_dictionary["dataset_root"])
    assert dataset_root.exists(), f"Dataset root does not exist | {dataset_root}"

    # Load Residual Evidence
    residual_target_name_list = [
        str(value)
        for value in comparison_dictionary["residual_target_name_list"]
    ]
    residual_row_list = load_selected_residual_row_list(
        residual_metrics_path=residual_metrics_path,
        baseline_specification_list=baseline_specification_list,
        split_lookup=None,
        residual_target_name_list=residual_target_name_list,
    )
    split_count_dictionary = build_split_count_dictionary_from_residual_rows(
        residual_row_list
    )
    split_audit_row_list = build_split_audit_row_list(residual_row_list)
    descriptive_summary_row_list = build_descriptive_summary_row_list(
        residual_row_list,
        residual_target_name_list,
    )
    mmt_signature_row_list = build_mmt_signature_row_list(config_dictionary)
    comparison_row_list, decision, blocker_list = build_comparison_row_list(
        residual_row_list,
        baseline_specification_list,
        config_dictionary,
    )

    # Persist Machine-Readable Artifacts
    baseline_manifest_path = write_yaml(
        output_directory / "resolved_baseline_manifest.yaml",
        {
            "schema_version": 1,
            "baseline_count": len(baseline_manifest_row_list),
            "baseline_list": baseline_manifest_row_list,
        },
    )
    split_audit_path = write_csv(
        output_directory / "split_boundary_audit.csv",
        split_audit_row_list,
    )
    residual_feature_path = write_csv(
        output_directory / "per_curve_residual_features.csv",
        residual_row_list,
    )
    mmt_signature_path = write_csv(
        output_directory / "mmt_signature_table.csv",
        mmt_signature_row_list,
    )
    descriptive_summary_path = write_csv(
        output_directory / "descriptive_split_summary.csv",
        descriptive_summary_row_list,
    )
    comparison_path = write_csv(
        output_directory / "explanatory_comparison.csv",
        comparison_row_list,
    )
    run_configuration_path = write_yaml(
        output_directory / "run_configuration.yaml",
        config_dictionary,
    )

    split_coverage_dictionary = {
        split_name: sum(
            int(row["residual_row_count"])
            for row in split_audit_row_list
            if row["split_name"] == split_name
        )
        for split_name in ["train", "validation", "test"]
    }
    fitted_comparison_row_list = [
        row
        for row in comparison_row_list
        if row["fit_status"] == "fitted_training_only"
    ]
    metadata_plus_mmt_row_list = [
        row
        for row in fitted_comparison_row_list
        if row["comparison_name"] == "metadata_plus_geometry_locked_mmt"
    ]
    shuffled_control_row_list = [
        row
        for row in fitted_comparison_row_list
        if row["comparison_name"] == "shuffled_mmt_control"
    ]
    calibrated_blocked_row_count = sum(
        row["fit_status"] == PARAMETER_BLOCKED_DECISION
        and row["comparison_name"]
        == "train_only_calibrated_equivalent_error"
        for row in comparison_row_list
    )
    decision_summary_dictionary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "decision": decision,
        "training_executed": False,
        "registry_updated": False,
        "fit_performed": any(
            row["fit_status"] == "fitted_training_only"
            for row in comparison_row_list
        ),
        "split_coverage": split_coverage_dictionary,
        "comparison_evidence": {
            "fitted_comparison_row_count": len(fitted_comparison_row_list),
            "calibrated_equivalent_error_blocked_row_count": (
                calibrated_blocked_row_count
            ),
            "maximum_absolute_metadata_plus_mmt_mae_gain": max(
                abs(float(row["mae_improvement_vs_metadata"]))
                for row in metadata_plus_mmt_row_list
            ),
            "maximum_absolute_shuffled_control_mae_gain": max(
                abs(float(row["mae_improvement_vs_metadata"]))
                for row in shuffled_control_row_list
            ),
            "condition_varying_mmt_signature_available": False,
        },
        "blocker_list": blocker_list,
        "next_action": (
            "keep MMT diagnostic-only until independent component-error "
            "measurements or validated causal contact-state reconstruction "
            "provides condition-varying MMT inputs"
        ),
    }
    decision_summary_path = write_yaml(
        output_directory / "decision_summary.yaml",
        decision_summary_dictionary,
    )

    validation_summary_dictionary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "status": "completed_with_parameter_blocker"
        if decision == PARAMETER_BLOCKED_DECISION
        else "completed",
        "decision": decision,
        "baseline_count": len(baseline_manifest_row_list),
        "dataset_split_count": split_count_dictionary,
        "residual_row_count": len(residual_row_list),
        "mmt_signature_row_count": len(mmt_signature_row_list),
        "comparison_row_count": len(comparison_row_list),
        "self_test": self_test_summary,
        "artifact_path_list": [
            format_project_path(baseline_manifest_path),
            format_project_path(split_audit_path),
            format_project_path(residual_feature_path),
            format_project_path(mmt_signature_path),
            format_project_path(descriptive_summary_path),
            format_project_path(comparison_path),
            format_project_path(run_configuration_path),
            format_project_path(decision_summary_path),
            format_project_path(report_path),
        ],
    }
    validation_summary_path = write_yaml(
        output_directory / "validation_summary.yaml",
        validation_summary_dictionary,
    )

    # Write Human-Readable Report Last
    report_markdown = build_report_markdown(
        run_instance_id=run_instance_id,
        config_path=config_path,
        output_directory=output_directory,
        residual_metrics_path=residual_metrics_path,
        baseline_manifest_row_list=baseline_manifest_row_list,
        split_count_dictionary=split_count_dictionary,
        split_audit_row_list=split_audit_row_list,
        descriptive_summary_row_list=descriptive_summary_row_list,
        mmt_signature_row_list=mmt_signature_row_list,
        comparison_row_list=comparison_row_list,
        decision=decision,
        blocker_list=blocker_list,
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_markdown.rstrip() + "\n", encoding="utf-8")

    # Confirm Every Declared Artifact Exists
    expected_path_list = [
        baseline_manifest_path,
        split_audit_path,
        residual_feature_path,
        mmt_signature_path,
        descriptive_summary_path,
        comparison_path,
        run_configuration_path,
        decision_summary_path,
        validation_summary_path,
        report_path,
    ]
    assert all(path.exists() for path in expected_path_list), (
        f"Diagnostic artifact creation is incomplete | "
        f"{[str(path) for path in expected_path_list if not path.exists()]}"
    )

    return {
        "run_instance_id": run_instance_id,
        "decision": decision,
        "output_directory": format_project_path(output_directory),
        "report_path": format_project_path(report_path),
        "validation_summary_path": format_project_path(validation_summary_path),
    }


def main() -> None:

    """Run the diagnostic builder."""

    command_line_arguments = parse_command_line_arguments()
    config_path = resolve_project_path(command_line_arguments.config_path)
    run_instance_id = command_line_arguments.run_instance_id
    if run_instance_id in [None, ""]:
        run_instance_id = (
            datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            + "__wave52_mmt_residual_explanatory_diagnostic"
        )

    result_dictionary = execute_diagnostic(
        config_path=config_path,
        run_instance_id=str(run_instance_id),
        run_self_test=bool(command_line_arguments.self_test),
    )
    print("Wave 5.2 MMT residual-explanatory diagnostic completed")
    print(f"Decision: {result_dictionary['decision']}")
    print(f"Output: {result_dictionary['output_directory']}")
    print(f"Report: {result_dictionary['report_path']}")


if __name__ == "__main__":
    main()
