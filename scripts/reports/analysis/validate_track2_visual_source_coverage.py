"""Validate that TE Curve Verification Pipeline visual reports expose matrix registry sources."""

from __future__ import annotations

# Import Python Utilities
import argparse
import sys
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)
from scripts.tooling import repository_path_support
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "full_track2_matrix_template.yaml"
)
DEFAULT_COLLAGE_REPORT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "best_model_collage_report"
    / "[2026-06-12]"
    / "track2_best_model_collage_report.md"
)
DEFAULT_OVERLAY_REPORT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "multi_model_curve_comparison_report"
    / "[2026-06-12]"
    / "track2_multi_model_curve_comparison_report.md"
)


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Validate TE Curve Verification Pipeline visual report source coverage.",
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="curve-verification matrix configuration path.",
    )
    argument_parser.add_argument(
        "--collage-report-path",
        type=Path,
        default=DEFAULT_COLLAGE_REPORT_PATH,
        help="Generated TE Curve Verification Pipeline best-model collage Markdown path.",
    )
    argument_parser.add_argument(
        "--overlay-report-path",
        type=Path,
        default=DEFAULT_OVERLAY_REPORT_PATH,
        help="Generated TE Curve Verification Pipeline multi-model overlay Markdown path.",
    )
    argument_parser.add_argument(
        "--candidate-source-label",
        action="append",
        default=[],
        help=(
            "Registry source label that must be visible in the generated visual reports. "
            "May be passed more than once. When omitted, every configured registry "
            "source is validated for backward compatibility."
        ),
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser.parse_args()


def collect_configured_registry_source_label_set(training_config: dict[str, Any]) -> set[str]:

    """Collect explicitly labeled registry sources from the curve-verification matrix config."""

    generation_configuration = training_config["comparison"]["candidate_generation"]
    source_label_set: set[str] = set()
    for configuration_name, registry_group_configuration in generation_configuration.items():
        if not str(configuration_name).endswith("_registry_models"):
            continue
        source_label = str(registry_group_configuration.get("source_label", "")).strip()
        if source_label:
            source_label_set.add(source_label)
    return source_label_set


def collect_expected_candidate_dictionary(
    training_config: dict[str, Any],
) -> dict[str, dict[str, list[str]]]:

    """Collect expected registry candidates grouped by source and visual scope."""

    configured_source_label_set = collect_configured_registry_source_label_set(training_config)
    candidate_configuration_list = (
        reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(training_config)
    )
    expected_candidate_dictionary: dict[str, dict[str, list[str]]] = {}
    for candidate_configuration in candidate_configuration_list:
        if str(candidate_configuration.get("candidate_kind", "")).strip() != "wave1_registry_model":
            continue
        candidate_source_label = str(candidate_configuration.get("candidate_source_label", "")).strip()
        if candidate_source_label not in configured_source_label_set:
            continue
        candidate_id = str(candidate_configuration["candidate_id"])
        candidate_surface = str(candidate_configuration.get("candidate_surface", "")).strip()
        expected_candidate_dictionary.setdefault(
            candidate_source_label,
            {
                "all": [],
                "forward": [],
                "backward": [],
                "global": [],
            },
        )
        expected_candidate_dictionary[candidate_source_label]["all"].append(candidate_id)
        if candidate_surface == "Fw":
            expected_candidate_dictionary[candidate_source_label]["forward"].append(candidate_id)
        elif candidate_surface == "Bw":
            expected_candidate_dictionary[candidate_source_label]["backward"].append(candidate_id)
        elif candidate_surface == "global":
            expected_candidate_dictionary[candidate_source_label]["global"].append(candidate_id)

    return expected_candidate_dictionary


def read_report_text(report_path: Path) -> str:

    """Read a generated Markdown report."""

    if not report_path.is_file():
        raise FileNotFoundError(f"Missing TE Curve Verification Pipeline visual report: {report_path}")
    return report_path.read_text(encoding="utf-8")


def collect_missing_candidate_list(
    report_text: str,
    candidate_id_list: list[str],
) -> list[str]:

    """Collect candidate IDs not present in a generated report."""

    def build_candidate_id_alias_set(candidate_id: str) -> set[str]:
        alias_set = {candidate_id}
        if candidate_id.endswith("_Fw"):
            alias_set.add(f"{candidate_id[:-3]}_fw")
        elif candidate_id.endswith("_Bw"):
            alias_set.add(f"{candidate_id[:-3]}_bw")
        return alias_set

    return [
        candidate_id
        for candidate_id in candidate_id_list
        if not any(candidate_id_alias in report_text for candidate_id_alias in build_candidate_id_alias_set(candidate_id))
    ]


def validate_visual_source_coverage(arguments: argparse.Namespace) -> dict[str, Any]:

    """Validate source coverage in the generated TE Curve Verification Pipeline visual reports."""

    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(arguments)
    )
    training_config = shared_training_infrastructure.load_training_config(arguments.config_path)
    expected_candidate_dictionary = collect_expected_candidate_dictionary(training_config)
    selected_source_label_set = {
        str(candidate_source_label).strip()
        for candidate_source_label in arguments.candidate_source_label
        if str(candidate_source_label).strip()
    }
    if selected_source_label_set:
        expected_candidate_dictionary = {
            source_label: scoped_candidate_dictionary
            for source_label, scoped_candidate_dictionary in expected_candidate_dictionary.items()
            if source_label in selected_source_label_set
        }
        missing_source_label_set = selected_source_label_set - set(expected_candidate_dictionary)
        if missing_source_label_set:
            missing_source_text = ", ".join(sorted(missing_source_label_set))
            raise AssertionError(
                "TE Curve Verification Pipeline visual source coverage requested "
                f"unknown registry source label(s): {missing_source_text}"
            )
    collage_report_text = read_report_text(arguments.collage_report_path)
    overlay_report_text = read_report_text(arguments.overlay_report_path)

    failure_list: list[str] = []
    source_summary_list: list[dict[str, Any]] = []
    for source_label, scoped_candidate_dictionary in sorted(expected_candidate_dictionary.items()):
        collage_missing_candidate_list = collect_missing_candidate_list(
            collage_report_text,
            scoped_candidate_dictionary["all"],
        )
        if collage_missing_candidate_list:
            failure_list.append(
                "collage report is missing registry source "
                f"{source_label}: {', '.join(collage_missing_candidate_list)}"
            )

        forward_candidate_id_list = (
            scoped_candidate_dictionary["forward"]
            or scoped_candidate_dictionary["global"]
        )
        backward_candidate_id_list = (
            scoped_candidate_dictionary["backward"]
            or scoped_candidate_dictionary["global"]
        )
        overlay_forward_missing_candidate_list = collect_missing_candidate_list(
            overlay_report_text,
            forward_candidate_id_list,
        )
        overlay_backward_missing_candidate_list = collect_missing_candidate_list(
            overlay_report_text,
            backward_candidate_id_list,
        )
        if overlay_forward_missing_candidate_list:
            failure_list.append(
                "overlay report is missing forward registry source "
                f"{source_label}: {', '.join(overlay_forward_missing_candidate_list)}"
            )
        if overlay_backward_missing_candidate_list:
            failure_list.append(
                "overlay report is missing backward registry source "
                f"{source_label}: {', '.join(overlay_backward_missing_candidate_list)}"
            )

        source_summary_list.append(
            {
                "source_label": source_label,
                "collage_candidate_count": len(scoped_candidate_dictionary["all"]),
                "overlay_forward_candidate_count": len(forward_candidate_id_list),
                "overlay_backward_candidate_count": len(backward_candidate_id_list),
            }
        )

    if failure_list:
        failure_text = "\n".join(f"- {failure}" for failure in failure_list)
        raise AssertionError(f"TE Curve Verification Pipeline visual source coverage failed:\n{failure_text}")

    print(
        "TE Curve Verification Pipeline visual source coverage passed | "
        f"registry_source_count={len(source_summary_list)}"
    )
    for source_summary in source_summary_list:
        print(
            " - {source_label}: collage={collage_candidate_count}, "
            "overlay_forward={overlay_forward_candidate_count}, "
            "overlay_backward={overlay_backward_candidate_count}".format(**source_summary)
        )

    return {
        "schema_version": 1,
        "registry_source_count": len(source_summary_list),
        "source_summary_list": source_summary_list,
    }


if __name__ == "__main__":
    validate_visual_source_coverage(parse_command_line_arguments())
