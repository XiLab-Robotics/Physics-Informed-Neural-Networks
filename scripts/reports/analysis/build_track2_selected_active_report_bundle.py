"""Build a selected-active TE Curve Verification Pipeline report bundle."""

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

# Import Third-Party Libraries
import yaml

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)


DEFAULT_REPORT_ROOT = Path(
    "doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[2026-07-19]"
)
DEFAULT_VALIDATION_ROOT = Path("output/validation_checks/track2_reference_comparison")
DEFAULT_REPORT_MAP = [
    (
        "*track2_selected_active_simplified_setpoints_forward_2026_07_19/validation_summary.yaml",
        "track2_selected_active_simplified_setpoints_forward_report.md",
    ),
    (
        "*track2_selected_active_simplified_setpoints_backward_2026_07_19/validation_summary.yaml",
        "track2_selected_active_simplified_setpoints_backward_report.md",
    ),
    (
        "*track2_selected_active_polished_setpoints_forward_2026_07_19/validation_summary.yaml",
        "track2_selected_active_polished_setpoints_forward_report.md",
    ),
    (
        "*track2_selected_active_polished_setpoints_backward_2026_07_19/validation_summary.yaml",
        "track2_selected_active_polished_setpoints_backward_report.md",
    ),
    (
        "*track2_selected_active_polished_actual_values_forward_2026_07_19/validation_summary.yaml",
        "track2_selected_active_polished_actual_values_forward_report.md",
    ),
    (
        "*track2_selected_active_polished_actual_values_backward_2026_07_19/validation_summary.yaml",
        "track2_selected_active_polished_actual_values_backward_report.md",
    ),
]


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description="Build selected-active TE Curve Verification Pipeline Markdown reports from validation summaries."
    )
    argument_parser.add_argument("--report-root", type=Path, default=DEFAULT_REPORT_ROOT)
    argument_parser.add_argument("--validation-root", type=Path, default=DEFAULT_VALIDATION_ROOT)
    return argument_parser


def load_yaml_dictionary(yaml_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary."""

    yaml_dictionary = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    assert isinstance(yaml_dictionary, dict), f"Expected YAML dictionary | {yaml_path}"
    return yaml_dictionary


def resolve_single_summary_path(validation_root: Path, summary_glob: str) -> Path:

    """Resolve one selected-active validation summary."""

    summary_path_list = sorted(validation_root.glob(summary_glob))
    assert len(summary_path_list) == 1, (
        "Expected exactly one selected-active validation summary | "
        f"glob={summary_glob} | count={len(summary_path_list)}"
    )
    return summary_path_list[0]


def build_selected_active_report_bundle(report_root: Path, validation_root: Path) -> list[Path]:

    """Build all selected-active Markdown reports."""

    report_root.mkdir(parents=True, exist_ok=True)
    written_report_path_list: list[Path] = []
    for summary_glob, report_filename in DEFAULT_REPORT_MAP:
        summary_path = resolve_single_summary_path(validation_root, summary_glob)
        summary_dictionary = load_yaml_dictionary(summary_path)
        report_path = report_root / report_filename
        report_path.write_text(
            reference_family_vs_feedforward_support.build_track2_directional_comparison_report_markdown(
                summary_dictionary
            ),
            encoding="utf-8",
            newline="\n",
        )
        written_report_path_list.append(report_path)
    return written_report_path_list


def main() -> None:

    """Run the command-line entry point."""

    arguments = build_argument_parser().parse_args()
    for report_path in build_selected_active_report_bundle(arguments.report_root, arguments.validation_root):
        print(f"[DONE] Selected-active report written | {report_path}")


if __name__ == "__main__":
    main()
