"""Add selected-model curve collages to reduced TE Curve Verification reports."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Third-Party Libraries
import yaml

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)
from scripts.reports.analysis import build_track2_best_model_collage_report
from scripts.training import shared_training_infrastructure

ConditionKey = tuple[str, str, str, str]
NOMINAL_CONDITION_PATTERN = re.compile(
    r"(?P<speed>[+-]?\d+(?:\.\d+)?)rpm"
    r"(?P<torque>[+-]?\d+(?:\.\d+)?)Nm"
    r"(?P<temperature>[+-]?\d+(?:\.\d+)?)deg",
    re.IGNORECASE,
)

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "reduced_selected_track2_matrix.yaml"
)
DEFAULT_REPORT_ROOT = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "te_curve_verification_pipeline"
    / "04_selected_model_reports"
    / "[2026-07-06]"
)
DEFAULT_VALIDATION_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_reference_comparison"
SELECTED_REPORT_DEFINITION_LIST = [
    {
        "dataset_name": "polished_dataset",
        "surface_scope": "forward",
        "report_filename": "track2_selected_models_polished_dataset_forward_report.md",
        "summary_glob": "*track2_selected_polished_dataset_forward_2026_07_06/validation_summary.yaml",
    },
    {
        "dataset_name": "polished_dataset",
        "surface_scope": "backward",
        "report_filename": "track2_selected_models_polished_dataset_backward_report.md",
        "summary_glob": "*track2_selected_polished_dataset_backward_2026_07_06/validation_summary.yaml",
    },
    {
        "dataset_name": "simplified_dataset",
        "surface_scope": "forward",
        "report_filename": "track2_selected_models_simplified_dataset_forward_report.md",
        "summary_glob": "*track2_selected_simplified_dataset_forward_2026_07_06/validation_summary.yaml",
    },
    {
        "dataset_name": "simplified_dataset",
        "surface_scope": "backward",
        "report_filename": "track2_selected_models_simplified_dataset_backward_report.md",
        "summary_glob": "*track2_selected_simplified_dataset_backward_2026_07_06/validation_summary.yaml",
    },
]


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description="Add measured-versus-predicted four-curve collages to selected Track 2 reports."
    )
    argument_parser.add_argument("--config-path", type=Path, default=DEFAULT_CONFIG_PATH)
    argument_parser.add_argument("--report-root", type=Path, default=DEFAULT_REPORT_ROOT)
    argument_parser.add_argument("--validation-root", type=Path, default=DEFAULT_VALIDATION_ROOT)
    argument_parser.add_argument("--curves-per-candidate", type=int, default=4)
    return argument_parser


def load_yaml_dictionary(yaml_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary."""

    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        yaml_dictionary = yaml.safe_load(yaml_file)
    assert isinstance(yaml_dictionary, dict), f"Expected YAML dictionary | {yaml_path}"
    return yaml_dictionary


def resolve_single_summary_path(validation_root: Path, summary_glob: str) -> Path:

    """Resolve one selected-model validation summary path."""

    matching_path_list = sorted(validation_root.glob(summary_glob))
    assert len(matching_path_list) == 1, (
        "Expected exactly one selected-model validation summary | "
        f"glob={summary_glob} | count={len(matching_path_list)}"
    )
    return matching_path_list[0]


def load_per_condition_entry_list(per_condition_metrics_path: Path) -> list[dict[str, Any]]:

    """Load one per-condition metrics CSV."""

    with per_condition_metrics_path.open("r", encoding="utf-8", newline="") as csv_file:
        return list(csv.DictReader(csv_file))


def resolve_candidate_configuration_lookup(training_config: dict[str, Any]) -> dict[str, dict[str, Any]]:

    """Resolve the candidate configuration lookup from the reduced matrix config."""

    return {
        str(candidate_configuration["candidate_id"]): candidate_configuration
        for candidate_configuration in reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(
            training_config
        )
    }


def build_condition_key_from_values(
    direction_label: Any,
    speed_rpm: Any,
    torque_nm: Any,
    oil_temperature_deg: Any,
) -> ConditionKey:

    """Build a dataset-independent operating-condition key."""

    return (
        str(direction_label).strip().lower(),
        f"{abs(round(float(speed_rpm) / 100.0) * 100.0):.1f}",
        f"{abs(round(float(torque_nm) / 100.0) * 100.0):.1f}",
        f"{round(float(oil_temperature_deg) / 5.0) * 5.0:.1f}",
    )


def build_nominal_condition_key_from_source_path(
    source_file_path: Any,
    direction_label: Any,
) -> ConditionKey | None:

    """Build a nominal operating-condition key from a dataset source path."""

    source_name = Path(str(source_file_path)).name
    condition_match = NOMINAL_CONDITION_PATTERN.search(source_name)
    if condition_match is None:
        return None

    return build_condition_key_from_values(
        direction_label,
        condition_match.group("speed"),
        condition_match.group("torque"),
        condition_match.group("temperature"),
    )


def build_curve_record_lookup(curve_record_list: list[Any]) -> dict[ConditionKey, Any]:

    """Build a lookup from physical operating condition to curve record."""

    return {
        (
            build_nominal_condition_key_from_source_path(
                curve_record.source_file_path,
                curve_record.direction_label,
            )
            or build_condition_key_from_values(
                curve_record.direction_label,
                curve_record.speed_rpm,
                curve_record.torque_nm,
                curve_record.oil_temperature_deg,
            )
        ): curve_record
        for curve_record in curve_record_list
    }


def build_curve_key(entry_dictionary: dict[str, Any]) -> ConditionKey:

    """Build a stable dataset-independent curve key from one per-condition entry."""

    return (
        build_nominal_condition_key_from_source_path(
            entry_dictionary["source_file_path"],
            entry_dictionary["direction_label"],
        )
        or build_condition_key_from_values(
            entry_dictionary["direction_label"],
            entry_dictionary["speed_rpm"],
            entry_dictionary["torque_nm"],
            entry_dictionary["oil_temperature_deg"],
        )
    )


def build_condition_label(entry_dictionary: dict[str, Any]) -> str:

    """Build one compact human-facing operating-condition label."""

    _, speed_rpm, torque_nm, oil_temperature_deg = build_curve_key(entry_dictionary)
    return (
        f"{float(speed_rpm):.0f} rpm, "
        f"{float(torque_nm):.0f} Nm, "
        f"{float(oil_temperature_deg):.0f} C"
    )


def build_relative_markdown_path(target_path: Path, markdown_directory: Path) -> str:

    """Build one Markdown-safe relative path."""

    relative_path = os.path.relpath(target_path.resolve(), markdown_directory.resolve())
    return relative_path.replace("\\", "/")


def select_best_candidate_id(validation_summary: dict[str, Any]) -> str:

    """Select the best candidate by mean percentage error."""

    candidate_metric_summary = validation_summary["candidate_metric_summary"]
    assert isinstance(candidate_metric_summary, dict)
    return min(
        candidate_metric_summary,
        key=lambda candidate_id: float(candidate_metric_summary[candidate_id]["mean_percentage_error_pct"]),
    )


def strip_existing_curve_evidence_section(markdown_text: str) -> str:

    """Remove a previously generated Curve Evidence section."""

    section_start = markdown_text.find("\n## Curve Evidence\n")
    if section_start < 0:
        return markdown_text
    next_section_start = markdown_text.find("\n## Artifacts\n", section_start + 1)
    assert next_section_start >= 0, "Curve Evidence section exists but Artifacts section was not found."
    return markdown_text[:section_start] + markdown_text[next_section_start:]


def build_visual_summary_table_line(candidate_summary: dict[str, Any]) -> str:

    """Build one Markdown table row for the visual evidence summary."""

    metric_dictionary = candidate_summary["metrics"]
    role_label = "Surface leader" if candidate_summary["is_surface_leader"] else "Selected candidate"
    return (
        f"| `{candidate_summary['candidate_id']}` | {role_label} | "
        f"{metric_dictionary['mae']:.6f} | "
        f"{metric_dictionary['rmse']:.6f} | "
        f"{metric_dictionary['mean_percentage_error_pct']:.3f} | "
        f"{metric_dictionary['p95_mean_percentage_error_pct']:.3f} |"
    )


def build_curve_evidence_markdown(candidate_summary_list: list[dict[str, Any]]) -> str:

    """Build the Markdown curve-evidence section."""

    condition_label_list = candidate_summary_list[0]["condition_label_list"] if candidate_summary_list else []
    report_line_list = [
        "## Curve Evidence",
        "",
        "Each selected candidate is shown with the same four deterministic held-out operating conditions for this direction.",
        "The dark line is the measured TE curve and the blue line is the model",
        "prediction for the same operating condition.",
        "",
        "Shared operating conditions:",
    ]
    for condition_label in condition_label_list:
        report_line_list.append(f"- {condition_label}")

    report_line_list.extend(
        [
            "",
        "| Candidate | Role | Curve MAE [deg] | Curve RMSE [deg] | Mean MPE [%] | P95 MPE [%] |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for candidate_summary in candidate_summary_list:
        report_line_list.append(build_visual_summary_table_line(candidate_summary))

    for candidate_summary in candidate_summary_list:
        report_line_list.extend(
            [
                "",
                f"### {candidate_summary['candidate_id']}",
                "",
                (
                    f"![{candidate_summary['candidate_id']} measured-versus-predicted TE collage]"
                    f"({candidate_summary['collage_markdown_path']})"
                ),
            ]
        )
    return "\n".join(report_line_list) + "\n"


def insert_curve_evidence_section(markdown_text: str, curve_evidence_markdown: str) -> str:

    """Insert curve evidence before the Artifacts section."""

    stripped_markdown_text = strip_existing_curve_evidence_section(markdown_text)
    artifacts_index = stripped_markdown_text.find("\n## Artifacts\n")
    assert artifacts_index >= 0, "Expected report Artifacts section."
    return (
        stripped_markdown_text[:artifacts_index]
        + "\n"
        + curve_evidence_markdown.rstrip()
        + "\n"
        + stripped_markdown_text[artifacts_index:]
    )


def build_shared_condition_key_list_by_surface(
    report_definition_list: list[dict[str, str]],
    validation_root: Path,
    curves_per_candidate: int,
) -> dict[str, list[ConditionKey]]:

    """Choose one shared operating-condition set for each direction."""

    shared_condition_key_list_by_surface: dict[str, list[ConditionKey]] = {}
    for surface_scope in ["forward", "backward"]:
        surface_report_definition_list = [
            report_definition
            for report_definition in report_definition_list
            if report_definition["surface_scope"] == surface_scope
        ]
        condition_key_set_list: list[set[ConditionKey]] = []
        per_condition_entry_list_by_report: dict[str, list[dict[str, Any]]] = {}
        validation_summary_by_report: dict[str, dict[str, Any]] = {}
        for report_definition in surface_report_definition_list:
            summary_path = resolve_single_summary_path(validation_root, report_definition["summary_glob"])
            report_key = str(report_definition["report_filename"])
            per_condition_entry_list = load_per_condition_entry_list(summary_path.parent / "per_condition_metrics.csv")
            per_condition_entry_list_by_report[report_key] = per_condition_entry_list
            validation_summary_by_report[report_key] = load_yaml_dictionary(summary_path)
            condition_key_set_list.append(
                {
                    build_curve_key(entry)
                    for entry in per_condition_entry_list
                }
            )
        shared_available_condition_key_set = set.intersection(*condition_key_set_list)
        assert len(shared_available_condition_key_set) >= curves_per_candidate, (
            "Not enough operating conditions are shared by all selected-model reports | "
            f"surface_scope={surface_scope} | "
            f"shared_condition_count={len(shared_available_condition_key_set)}"
        )
        surface_report_definition_list.sort(
            key=lambda report_definition: 0
            if report_definition["dataset_name"] == "simplified_dataset"
            else 1
        )

        selected_condition_key_list: list[ConditionKey] | None = None
        for report_definition in surface_report_definition_list:
            report_key = str(report_definition["report_filename"])
            validation_summary = validation_summary_by_report[report_key]
            per_condition_entry_list = per_condition_entry_list_by_report[report_key]
            best_candidate_id = select_best_candidate_id(validation_summary)
            candidate_entry_list = [
                entry
                for entry in per_condition_entry_list
                if str(entry["candidate_id"]) == best_candidate_id
                and build_curve_key(entry) in shared_available_condition_key_set
            ]
            if len(candidate_entry_list) < curves_per_candidate:
                continue
            selected_entry_list = build_track2_best_model_collage_report.select_candidate_collage_entries(
                candidate_entry_list,
                surface_scope,
                curves_per_candidate,
            )
            selected_condition_key_list = [build_curve_key(selected_entry) for selected_entry in selected_entry_list]
            break

        assert selected_condition_key_list is not None, (
            "Could not select shared operating conditions for selected-model report | "
            f"surface_scope={surface_scope}"
        )
        shared_condition_key_list_by_surface[surface_scope] = selected_condition_key_list
    return shared_condition_key_list_by_surface


def augment_one_report(
    report_definition: dict[str, str],
    config_path: Path,
    report_root: Path,
    validation_root: Path,
    curves_per_candidate: int,
    shared_condition_key_list: list[ConditionKey],
) -> dict[str, Any]:

    """Regenerate visual evidence for one selected-model report."""

    assert curves_per_candidate == 4, "Selected-model visual reports require four curves per candidate."
    report_path = report_root / report_definition["report_filename"]
    assert report_path.exists(), f"Selected report Markdown does not exist | {report_path}"
    summary_path = resolve_single_summary_path(validation_root, report_definition["summary_glob"])
    validation_summary = load_yaml_dictionary(summary_path)
    output_directory = summary_path.parent
    per_condition_entry_list = load_per_condition_entry_list(output_directory / "per_condition_metrics.csv")
    best_candidate_id = select_best_candidate_id(validation_summary)

    training_config = shared_training_infrastructure.apply_dataset_override(
        shared_training_infrastructure.load_training_config(config_path),
        report_definition["dataset_name"],
    )
    selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
    curve_record_list, _, _, _ = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    curve_record_list = [
        curve_record
        for curve_record in curve_record_list
        if str(curve_record.direction_label).strip().lower() == report_definition["surface_scope"]
    ]
    curve_record_lookup = build_curve_record_lookup(curve_record_list)
    candidate_configuration_lookup = resolve_candidate_configuration_lookup(training_config)
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])
    candidate_metric_summary = validation_summary["candidate_metric_summary"]
    asset_root = report_root / "assets" / report_path.stem
    if asset_root.exists():
        shutil.rmtree(asset_root)
    asset_root.mkdir(parents=True, exist_ok=True)

    candidate_summary_list: list[dict[str, Any]] = []
    candidate_id_list = [str(candidate_entry["candidate_id"]) for candidate_entry in validation_summary["candidate_list"]]
    for candidate_id in candidate_id_list:
        candidate_entry_list = [entry for entry in per_condition_entry_list if str(entry["candidate_id"]) == candidate_id]
        candidate_entry_by_condition_key = {
            build_curve_key(candidate_entry): candidate_entry
            for candidate_entry in candidate_entry_list
        }
        selected_entry_list = [
            candidate_entry_by_condition_key[condition_key]
            for condition_key in shared_condition_key_list
            if condition_key in candidate_entry_by_condition_key
        ]
        assert len(selected_entry_list) == curves_per_candidate, (
            "Candidate is missing at least one shared selected-model operating condition | "
            f"candidate_id={candidate_id} | "
            f"dataset={report_definition['dataset_name']} | "
            f"surface_scope={report_definition['surface_scope']}"
        )
        selected_curve_record_list = [
            curve_record_lookup[build_curve_key(selected_entry)]
            for selected_entry in selected_entry_list
        ]
        candidate = reference_family_vs_feedforward_support.load_track2_candidate(
            candidate_configuration_lookup[candidate_id]
        )
        selected_payload_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
            candidate,
            selected_curve_record_list,
            percentage_error_denominator,
            include_curve_payload=True,
        )
        collage_path = asset_root / f"{shared_training_infrastructure.sanitize_name(candidate_id)}.png"
        build_track2_best_model_collage_report.save_candidate_collage(
            collage_path,
            candidate_id,
            selected_payload_entry_list,
        )
        candidate_summary_list.append(
            {
                "candidate_id": candidate_id,
                "is_surface_leader": candidate_id == best_candidate_id,
                "metrics": candidate_metric_summary[candidate_id],
                "collage_markdown_path": build_relative_markdown_path(collage_path, report_path.parent),
                "condition_label_list": [
                    build_condition_label(selected_entry)
                    for selected_entry in selected_entry_list
                ],
            }
        )

    markdown_text = report_path.read_text(encoding="utf-8")
    report_path.write_text(
        insert_curve_evidence_section(markdown_text, build_curve_evidence_markdown(candidate_summary_list)),
        encoding="utf-8",
    )
    return {
        "report_path": shared_training_infrastructure.format_project_relative_path(report_path),
        "best_candidate_id": best_candidate_id,
        "candidate_count": len(candidate_summary_list),
    }


def run_selected_model_visual_report_builder(arguments: argparse.Namespace) -> list[dict[str, Any]]:

    """Run visual augmentation for all selected reports."""

    config_path = shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.config_path)
    report_root = shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.report_root)
    validation_root = shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.validation_root)
    shared_condition_key_list_by_surface = build_shared_condition_key_list_by_surface(
        SELECTED_REPORT_DEFINITION_LIST,
        validation_root,
        int(arguments.curves_per_candidate),
    )
    return [
        augment_one_report(
            report_definition,
            config_path,
            report_root,
            validation_root,
            int(arguments.curves_per_candidate),
            shared_condition_key_list_by_surface[report_definition["surface_scope"]],
        )
        for report_definition in SELECTED_REPORT_DEFINITION_LIST
    ]


def main() -> None:

    """Run the command-line entry point."""

    summary_list = run_selected_model_visual_report_builder(build_argument_parser().parse_args())
    for summary in summary_list:
        print(
            "[DONE] Selected visual report updated | "
            f"report={summary['report_path']} | "
            f"candidate_count={summary['candidate_count']} | "
            f"leader={summary['best_candidate_id']}"
        )


if __name__ == "__main__":
    main()
