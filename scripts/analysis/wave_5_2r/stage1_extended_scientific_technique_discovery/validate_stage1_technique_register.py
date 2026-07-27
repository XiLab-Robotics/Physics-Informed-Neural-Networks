"""Validate and summarize the Wave 5.2R Stage 1 technique register."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


# Repository paths and schema constants.
REPOSITORY_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT_ROOT = (
    REPOSITORY_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage1_extended_scientific_technique_discovery"
)
DEFAULT_SOURCE_REGISTER_PATH = DEFAULT_OUTPUT_ROOT / "stage1_source_register.yaml"
DEFAULT_TECHNIQUE_REGISTER_PATH = DEFAULT_OUTPUT_ROOT / "stage1_technique_register.yaml"
DEFAULT_CSV_PATH = DEFAULT_OUTPUT_ROOT / "stage1_candidate_register.csv"
DEFAULT_SUMMARY_PATH = DEFAULT_OUTPUT_ROOT / "stage1_exit_gate_summary.json"

REQUIRED_TECHNIQUE_FIELD_SET = {
    "technique_id",
    "family",
    "technique",
    "source_ids",
    "claimed_benefit",
    "required_variables",
    "availability",
    "missing_variables",
    "local_formulation",
    "matched_control",
    "falsification",
    "deployment_impact",
    "deployment_note",
    "priority",
    "roster",
    "target_stage",
}
ALLOWED_ROSTER_SET = {
    "active_real_data",
    "conditional_real_data",
    "oracle_only",
    "excluded",
}
ALLOWED_PRIORITY_SET = {"high", "medium", "low", "excluded"}
ALLOWED_AVAILABILITY_SET = {
    "available",
    "train_derived",
    "synthetic_only",
    "unavailable",
}
ALLOWED_DEPLOYMENT_IMPACT_SET = {"none", "low", "medium", "high"}
REAL_DATA_ROSTER_SET = {"active_real_data", "conditional_real_data"}
ACCEPTED_SOURCE_KIND_SET = {
    "primary_paper",
    "official_implementation",
    "repository_primary",
}
DISALLOWED_RUNTIME_VARIABLE_SET = {
    "measured_te_runtime",
    "target_te_runtime",
    "target_curve_mean_runtime",
    "target_harmonic_coefficients_runtime",
}
REQUIRED_SEARCH_FAMILY_SET = {
    "model_discrepancy_and_grey_box",
    "weak_form_and_variational",
    "adaptive_weighting_and_constraints",
    "gradient_conflict",
    "spectral_bias_and_coordinate_networks",
    "sobolev_and_derivative_training",
    "sparse_and_symbolic_discovery",
    "uncertainty_aware_weighting",
    "curriculum_transfer_and_synthetic_to_real",
    "failure_informed_sampling",
    "certified_residual_bounds",
    "neural_operators",
    "mechanical_system_identification",
}
TECHNIQUE_FAMILY_TO_SEARCH_FAMILY_MAP = {
    "model_discrepancy": "model_discrepancy_and_grey_box",
    "harmonic_supervision": "spectral_bias_and_coordinate_networks",
    "structured_output": "mechanical_system_identification",
    "spectral_architecture": "spectral_bias_and_coordinate_networks",
    "spectral_objective": "spectral_bias_and_coordinate_networks",
    "derivative_guidance": "sobolev_and_derivative_training",
    "weak_form": "weak_form_and_variational",
    "weak_mechanical_prior": "mechanical_system_identification",
    "objective_optimization": "gradient_conflict",
    "constraint_optimization": "adaptive_weighting_and_constraints",
    "curriculum_transfer": "curriculum_transfer_and_synthetic_to_real",
    "adaptive_sampling": "failure_informed_sampling",
    "uncertainty": "uncertainty_aware_weighting",
    "sparse_discovery": "sparse_and_symbolic_discovery",
    "symbolic_discovery": "sparse_and_symbolic_discovery",
    "temporal_grey_box": "model_discrepancy_and_grey_box",
    "hard_constraints": "adaptive_weighting_and_constraints",
    "certification": "certified_residual_bounds",
    "neural_operator": "neural_operators",
    "dynamic_equation_hybrid": "model_discrepancy_and_grey_box",
    "synthetic_transfer": "curriculum_transfer_and_synthetic_to_real",
    "mmt_oracle": "mechanical_system_identification",
    "contact_mechanics": "mechanical_system_identification",
    "hysteresis_backlash": "mechanical_system_identification",
}


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description=(
            "Validate the Stage 1 source and technique registers and write "
            "the canonical candidate table and exit-gate summary."
        )
    )
    parser.add_argument(
        "--source-register",
        type=Path,
        default=DEFAULT_SOURCE_REGISTER_PATH,
        help="Path to the source register YAML.",
    )
    parser.add_argument(
        "--technique-register",
        type=Path,
        default=DEFAULT_TECHNIQUE_REGISTER_PATH,
        help="Path to the technique register YAML.",
    )
    parser.add_argument(
        "--candidate-csv",
        type=Path,
        default=DEFAULT_CSV_PATH,
        help="Path to the generated candidate CSV.",
    )
    parser.add_argument(
        "--summary",
        type=Path,
        default=DEFAULT_SUMMARY_PATH,
        help="Path to the generated exit-gate JSON summary.",
    )
    return parser.parse_args()


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    """Load a YAML file and require a top-level mapping."""

    with path.open("r", encoding="utf-8") as stream:
        payload = yaml.safe_load(stream)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected a top-level mapping in {path}")
    return payload


def calculate_sha256(path: Path) -> str:
    """Return the SHA-256 digest of a file."""

    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_source_register(
    source_payload: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    """Validate source identity and return an ID-indexed source map."""

    error_list: list[str] = []
    source_list = source_payload.get("sources")
    if not isinstance(source_list, list) or not source_list:
        return {}, ["Source register must contain a non-empty sources list."]

    source_by_id: dict[str, dict[str, Any]] = {}
    for source in source_list:
        if not isinstance(source, dict):
            error_list.append("Every source entry must be a mapping.")
            continue
        source_id = str(source.get("source_id", "")).strip()
        if not source_id:
            error_list.append("A source entry is missing source_id.")
            continue
        if source_id in source_by_id:
            error_list.append(f"Duplicate source_id: {source_id}")
            continue
        source_kind = source.get("source_kind")
        if source_kind not in ACCEPTED_SOURCE_KIND_SET:
            error_list.append(
                f"{source_id}: unsupported source_kind {source_kind!r}"
            )
        for field_name in (
            "title",
            "authors",
            "year",
            "locator",
            "retained_claim",
        ):
            if source.get(field_name) in (None, "", []):
                error_list.append(f"{source_id}: missing {field_name}")
        source_by_id[source_id] = source

    return source_by_id, error_list


def validate_technique_register(
    technique_payload: dict[str, Any],
    source_by_id: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[str], set[str]]:
    """Validate technique fields, observability, sources, and family coverage."""

    error_list: list[str] = []
    covered_search_family_set: set[str] = set()
    technique_list = technique_payload.get("techniques")
    if not isinstance(technique_list, list) or not technique_list:
        return [], ["Technique register must contain a non-empty techniques list."], set()

    contract = technique_payload.get("contract")
    if not isinstance(contract, dict):
        return technique_list, ["Technique register is missing the contract mapping."], set()

    runtime_allowlist = set(contract.get("runtime_variable_allowlist", []))
    training_allowlist = set(contract.get("training_only_variable_allowlist", []))
    allowed_real_data_variable_set = runtime_allowlist | training_allowlist

    technique_id_set: set[str] = set()
    for technique in technique_list:
        if not isinstance(technique, dict):
            error_list.append("Every technique entry must be a mapping.")
            continue

        technique_id = str(technique.get("technique_id", "")).strip()
        if not technique_id:
            error_list.append("A technique entry is missing technique_id.")
            continue
        if technique_id in technique_id_set:
            error_list.append(f"Duplicate technique_id: {technique_id}")
        technique_id_set.add(technique_id)

        missing_field_set = REQUIRED_TECHNIQUE_FIELD_SET - set(technique)
        if missing_field_set:
            error_list.append(
                f"{technique_id}: missing fields {sorted(missing_field_set)}"
            )
            continue

        roster = technique["roster"]
        priority = technique["priority"]
        availability = technique["availability"]
        deployment_impact = technique["deployment_impact"]
        if roster not in ALLOWED_ROSTER_SET:
            error_list.append(f"{technique_id}: invalid roster {roster!r}")
        if priority not in ALLOWED_PRIORITY_SET:
            error_list.append(f"{technique_id}: invalid priority {priority!r}")
        if availability not in ALLOWED_AVAILABILITY_SET:
            error_list.append(
                f"{technique_id}: invalid availability {availability!r}"
            )
        if deployment_impact not in ALLOWED_DEPLOYMENT_IMPACT_SET:
            error_list.append(
                f"{technique_id}: invalid deployment impact "
                f"{deployment_impact!r}"
            )

        family = technique["family"]
        search_family = TECHNIQUE_FAMILY_TO_SEARCH_FAMILY_MAP.get(family)
        if search_family is None:
            error_list.append(f"{technique_id}: unmapped family {family!r}")
        else:
            covered_search_family_set.add(search_family)

        source_id_list = technique["source_ids"]
        if not isinstance(source_id_list, list) or not source_id_list:
            error_list.append(f"{technique_id}: source_ids must be non-empty")
        else:
            unknown_source_id_list = [
                source_id
                for source_id in source_id_list
                if source_id not in source_by_id
            ]
            if unknown_source_id_list:
                error_list.append(
                    f"{technique_id}: unknown sources "
                    f"{unknown_source_id_list}"
                )

        required_variable_set = set(technique["required_variables"])
        missing_variable_set = set(technique["missing_variables"])
        if required_variable_set & DISALLOWED_RUNTIME_VARIABLE_SET:
            error_list.append(
                f"{technique_id}: target-derived runtime variable requested"
            )
        if roster in REAL_DATA_ROSTER_SET:
            if availability not in {"available", "train_derived"}:
                error_list.append(
                    f"{technique_id}: real-data roster has unavailable inputs"
                )
            if missing_variable_set:
                error_list.append(
                    f"{technique_id}: real-data roster has missing variables "
                    f"{sorted(missing_variable_set)}"
                )
            unknown_real_variable_set = (
                required_variable_set - allowed_real_data_variable_set
            )
            if unknown_real_variable_set:
                error_list.append(
                    f"{technique_id}: real-data roster requests non-contract "
                    f"variables {sorted(unknown_real_variable_set)}"
                )
            if priority == "excluded":
                error_list.append(
                    f"{technique_id}: real-data roster cannot be excluded"
                )

        for text_field_name in (
            "claimed_benefit",
            "local_formulation",
            "matched_control",
            "falsification",
            "deployment_note",
        ):
            if not str(technique[text_field_name]).strip():
                error_list.append(
                    f"{technique_id}: empty {text_field_name}"
                )

        target_stage = technique["target_stage"]
        if not isinstance(target_stage, int) or not 2 <= target_stage <= 13:
            error_list.append(
                f"{technique_id}: target_stage must be an integer from 2 to 13"
            )

    missing_search_family_set = (
        REQUIRED_SEARCH_FAMILY_SET - covered_search_family_set
    )
    if missing_search_family_set:
        error_list.append(
            "Missing roadmap search families: "
            f"{sorted(missing_search_family_set)}"
        )

    return technique_list, error_list, covered_search_family_set


def write_candidate_csv(
    technique_list: list[dict[str, Any]],
    destination_path: Path,
) -> None:
    """Write a flat human-reviewable candidate table."""

    destination_path.parent.mkdir(parents=True, exist_ok=True)
    field_name_list = [
        "technique_id",
        "family",
        "technique",
        "roster",
        "priority",
        "target_stage",
        "availability",
        "source_ids",
        "required_variables",
        "missing_variables",
        "claimed_benefit",
        "local_formulation",
        "matched_control",
        "falsification",
        "deployment_impact",
        "deployment_note",
    ]
    with destination_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=field_name_list)
        writer.writeheader()
        for technique in technique_list:
            row = dict(technique)
            for list_field_name in (
                "source_ids",
                "required_variables",
                "missing_variables",
            ):
                row[list_field_name] = "|".join(
                    str(value) for value in row[list_field_name]
                )
            writer.writerow(
                {field_name: row[field_name] for field_name in field_name_list}
            )


def write_exit_gate_summary(
    technique_list: list[dict[str, Any]],
    covered_search_family_set: set[str],
    source_register_path: Path,
    technique_register_path: Path,
    error_list: list[str],
    destination_path: Path,
) -> dict[str, Any]:
    """Write the canonical Stage 1 decision summary."""

    roster_count_map = Counter(
        technique["roster"] for technique in technique_list
    )
    priority_count_map = Counter(
        technique["priority"] for technique in technique_list
    )
    target_stage_count_map = Counter(
        str(technique["target_stage"]) for technique in technique_list
    )
    summary = {
        "schema_version": "wave52r_stage1_exit_gate_summary_v1",
        "generated_at": "2026-07-27",
        "scope": {
            "dataset_id": "polished_dataset",
            "input_mode": "setpoints",
            "surface": "Fw",
        },
        "source_register_sha256": calculate_sha256(source_register_path),
        "technique_register_sha256": calculate_sha256(
            technique_register_path
        ),
        "technique_count": len(technique_list),
        "roster_counts": dict(sorted(roster_count_map.items())),
        "priority_counts": dict(sorted(priority_count_map.items())),
        "target_stage_counts": dict(
            sorted(target_stage_count_map.items(), key=lambda item: int(item[0]))
        ),
        "covered_search_family_count": len(covered_search_family_set),
        "required_search_family_count": len(REQUIRED_SEARCH_FAMILY_SET),
        "covered_search_families": sorted(covered_search_family_set),
        "real_data_technique_ids": [
            technique["technique_id"]
            for technique in technique_list
            if technique["roster"] in REAL_DATA_ROSTER_SET
        ],
        "oracle_only_technique_ids": [
            technique["technique_id"]
            for technique in technique_list
            if technique["roster"] == "oracle_only"
        ],
        "excluded_technique_ids": [
            technique["technique_id"]
            for technique in technique_list
            if technique["roster"] == "excluded"
        ],
        "target_derived_runtime_variable_count": 0
        if not error_list
        else None,
        "real_data_missing_variable_count": 0
        if not error_list
        else None,
        "exit_gate_passed": not error_list,
        "error_list": error_list,
        "decision": (
            "freeze_candidate_register"
            if not error_list
            else "repair_register_before_stage2"
        ),
    }
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    with destination_path.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(summary, stream, indent=2)
        stream.write("\n")
    return summary


def main() -> None:
    """Validate the registers, write derived artifacts, and enforce the gate."""

    arguments = parse_arguments()
    source_payload = load_yaml_mapping(arguments.source_register)
    technique_payload = load_yaml_mapping(arguments.technique_register)

    source_by_id, source_error_list = validate_source_register(source_payload)
    (
        technique_list,
        technique_error_list,
        covered_search_family_set,
    ) = validate_technique_register(technique_payload, source_by_id)
    error_list = source_error_list + technique_error_list

    write_candidate_csv(technique_list, arguments.candidate_csv)
    summary = write_exit_gate_summary(
        technique_list=technique_list,
        covered_search_family_set=covered_search_family_set,
        source_register_path=arguments.source_register,
        technique_register_path=arguments.technique_register,
        error_list=error_list,
        destination_path=arguments.summary,
    )

    if error_list:
        for error in error_list:
            print(f"ERROR: {error}")
        raise SystemExit(1)

    print(
        "WAVE52R_STAGE1_VALIDATION_OK "
        f"techniques={summary['technique_count']} "
        f"real_data={len(summary['real_data_technique_ids'])} "
        f"oracle_only={len(summary['oracle_only_technique_ids'])} "
        f"excluded={len(summary['excluded_technique_ids'])} "
        f"search_families={summary['covered_search_family_count']}"
    )


if __name__ == "__main__":
    main()
