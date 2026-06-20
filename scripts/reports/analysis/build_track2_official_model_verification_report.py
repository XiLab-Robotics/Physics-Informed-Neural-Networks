"""Build the official TE Curve Verification Pipeline model-verification report from refresh artifacts."""

from __future__ import annotations

# Import Python Utilities
import argparse
from pathlib import Path
from typing import Any

# Import Third-Party Utilities
import yaml

# Define Project Paths
PROJECT_PATH = Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT_ROOT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "official_model_verification_report"
)

METRIC_KEY_LIST = [
    "mae",
    "rmse",
    "mean_percentage_error_pct",
    "p95_mean_percentage_error_pct",
]


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Build the official TE Curve Verification Pipeline model-verification report.",
    )
    argument_parser.add_argument(
        "--matrix-summary-path",
        type=Path,
        required=True,
        help="curve-verification matrix validation_summary.yaml path.",
    )
    argument_parser.add_argument(
        "--collage-summary-path",
        type=Path,
        required=True,
        help="TE Curve Verification Pipeline collage summary YAML path.",
    )
    argument_parser.add_argument(
        "--overlay-summary-path",
        type=Path,
        required=True,
        help="TE Curve Verification Pipeline overlay summary YAML path.",
    )
    argument_parser.add_argument(
        "--report-date",
        required=True,
        help="Dated report bundle label, for example 2026-06-13.",
    )
    argument_parser.add_argument(
        "--refresh-label",
        required=True,
        help="Human-readable refresh label.",
    )
    argument_parser.add_argument(
        "--candidate-source-label",
        required=True,
        help="Matrix candidate source label that must be present in the refresh.",
    )
    argument_parser.add_argument(
        "--decision",
        default="verified exploratory baseline; not promoted",
        help="Official decision text for the refreshed candidate source.",
    )
    argument_parser.add_argument(
        "--next-step",
        default="Review the accepted direction-parallel leaders before preparing the next modeling branch.",
        help="Short next-step text for the closeout section.",
    )
    argument_parser.add_argument(
        "--output-report-path",
        type=Path,
        default=None,
        help="Optional explicit output Markdown path.",
    )
    argument_parser.add_argument(
        "--operator-log-root",
        type=Path,
        default=None,
        help="Optional operator launcher log directory.",
    )
    return argument_parser.parse_args()


def load_yaml_dictionary(yaml_path: Path) -> dict[str, Any]:

    """Load a YAML dictionary from disk."""

    if not yaml_path.is_file():
        raise FileNotFoundError(f"Missing YAML artifact: {yaml_path}")
    with yaml_path.open("r", encoding="utf-8") as input_file:
        loaded_dictionary = yaml.safe_load(input_file) or {}
    if not isinstance(loaded_dictionary, dict):
        raise TypeError(f"Expected YAML dictionary: {yaml_path}")
    return loaded_dictionary


def normalize_path_text(path_value: Path | str | None) -> str:

    """Return a repository-friendly path string."""

    if path_value is None:
        return ""
    path_text = str(path_value)
    try:
        absolute_path = Path(path_text).resolve()
        return absolute_path.relative_to(PROJECT_PATH.resolve()).as_posix()
    except (OSError, ValueError):
        return path_text.replace("\\", "/")


def format_metric(metric_value: Any) -> str:

    """Format a numeric metric for Markdown tables."""

    try:
        return f"{float(metric_value):.6f}"
    except (TypeError, ValueError):
        return "n/a"


def format_percentage_metric(metric_value: Any) -> str:

    """Format a numeric percentage metric for Markdown tables."""

    try:
        return f"{float(metric_value):.3f}"
    except (TypeError, ValueError):
        return "n/a"


def collect_source_candidate_list(
    matrix_summary_dictionary: dict[str, Any],
    candidate_source_label: str,
) -> list[dict[str, Any]]:

    """Collect candidates belonging to the refreshed source label."""

    candidate_list = matrix_summary_dictionary.get("candidate_list", [])
    if not isinstance(candidate_list, list):
        raise TypeError("Matrix summary candidate_list must be a list.")

    source_candidate_list = [
        candidate_dictionary
        for candidate_dictionary in candidate_list
        if str(candidate_dictionary.get("candidate_source_label", "")).strip()
        == candidate_source_label
    ]
    if not source_candidate_list:
        raise AssertionError(
            "The official report builder could not find refreshed candidates "
            f"for source label: {candidate_source_label}"
        )
    return source_candidate_list


def collect_candidate_metric_dictionary(
    matrix_summary_dictionary: dict[str, Any],
) -> dict[str, dict[str, Any]]:

    """Collect aggregate candidate metrics from the matrix summary."""

    metric_dictionary = matrix_summary_dictionary.get("candidate_metric_summary", {})
    if not isinstance(metric_dictionary, dict):
        raise TypeError("Matrix summary candidate_metric_summary must be a dictionary.")
    return {
        str(candidate_id): metric_payload
        for candidate_id, metric_payload in metric_dictionary.items()
        if isinstance(metric_payload, dict)
    }


def collect_ranked_candidate_rows(
    source_candidate_list: list[dict[str, Any]],
    candidate_metric_dictionary: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:

    """Collect candidate rows sorted by aggregate MAE."""

    ranked_row_list: list[dict[str, Any]] = []
    for candidate_dictionary in source_candidate_list:
        candidate_id = str(candidate_dictionary.get("candidate_id", "")).strip()
        if not candidate_id:
            continue
        metric_dictionary = candidate_metric_dictionary.get(candidate_id, {})
        if not metric_dictionary:
            continue
        ranked_row_list.append(
            {
                "candidate_id": candidate_id,
                "surface": str(candidate_dictionary.get("candidate_surface", "")).strip(),
                "family": str(candidate_dictionary.get("candidate_family", "")).strip(),
                "mae": metric_dictionary.get("mae"),
                "rmse": metric_dictionary.get("rmse"),
                "mean_percentage_error_pct": metric_dictionary.get("mean_percentage_error_pct"),
                "p95_mean_percentage_error_pct": metric_dictionary.get(
                    "p95_mean_percentage_error_pct"
                ),
            }
        )

    ranked_row_list.sort(key=lambda row: float(row.get("mae", 1.0e9)))
    return ranked_row_list


def collect_surface_leader_rows(
    ranked_candidate_row_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    """Collect one leader row per candidate surface."""

    surface_order_list = ["Fw", "Bw", "global"]
    leader_row_list: list[dict[str, Any]] = []
    for surface in surface_order_list:
        surface_row_list = [
            row
            for row in ranked_candidate_row_list
            if str(row.get("surface", "")).strip() == surface
        ]
        if surface_row_list:
            leader_row_list.append(surface_row_list[0])
    return leader_row_list


def collect_direction_leader_rows(
    matrix_summary_dictionary: dict[str, Any],
) -> list[dict[str, Any]]:

    """Collect current overall leaders from the direction breakdown."""

    direction_breakdown_dictionary = matrix_summary_dictionary.get("direction_breakdown", {})
    if not isinstance(direction_breakdown_dictionary, dict):
        return []

    leader_row_list: list[dict[str, Any]] = []
    for direction_label, direction_metric_dictionary in sorted(direction_breakdown_dictionary.items()):
        if not isinstance(direction_metric_dictionary, dict):
            continue
        candidate_metric_rows = [
            {
                "direction": str(direction_label),
                "candidate_id": str(candidate_id),
                "mae": metric_dictionary.get("mae"),
                "rmse": metric_dictionary.get("rmse"),
                "mean_percentage_error_pct": metric_dictionary.get("mean_percentage_error_pct"),
                "p95_mean_percentage_error_pct": metric_dictionary.get(
                    "p95_mean_percentage_error_pct"
                ),
            }
            for candidate_id, metric_dictionary in direction_metric_dictionary.items()
            if isinstance(metric_dictionary, dict)
        ]
        candidate_metric_rows.sort(key=lambda row: float(row.get("mae", 1.0e9)))
        if candidate_metric_rows:
            leader_row_list.append(candidate_metric_rows[0])
    return leader_row_list


def collect_visual_source_count(
    collage_summary_dictionary: dict[str, Any],
    overlay_summary_dictionary: dict[str, Any],
    candidate_source_label: str,
) -> dict[str, int]:

    """Collect visual report coverage counts for the refreshed source label."""

    collage_count = 0
    for candidate_dictionary in collage_summary_dictionary.get("candidate_summary_list", []):
        if not isinstance(candidate_dictionary, dict):
            continue
        if str(candidate_dictionary.get("candidate_source_label", "")).strip() == candidate_source_label:
            collage_count += 1

    overlay_forward_count = 0
    overlay_backward_count = 0
    for comparison_dictionary in overlay_summary_dictionary.get("comparison_summary_list", []):
        if not isinstance(comparison_dictionary, dict):
            continue
        direction_scope = str(comparison_dictionary.get("direction_scope", "")).strip()
        for candidate_dictionary in comparison_dictionary.get("candidate_summary_list", []):
            if not isinstance(candidate_dictionary, dict):
                continue
            if str(candidate_dictionary.get("candidate_source_label", "")).strip() != candidate_source_label:
                continue
            if direction_scope == "forward":
                overlay_forward_count += 1
            elif direction_scope == "backward":
                overlay_backward_count += 1

    return {
        "collage": collage_count,
        "overlay_forward": overlay_forward_count,
        "overlay_backward": overlay_backward_count,
    }


def build_metric_table(row_list: list[dict[str, Any]], leading_column_list: list[str]) -> list[str]:

    """Build a Markdown metric table."""

    header_list = leading_column_list + ["MAE [deg]", "RMSE [deg]", "Mean [%]", "P95 [%]"]
    alignment_list = ["---"] * len(leading_column_list) + ["---:", "---:", "---:", "---:"]
    output_line_list = [
        "| " + " | ".join(header_list) + " |",
        "| " + " | ".join(alignment_list) + " |",
    ]
    for row_dictionary in row_list:
        leading_value_list = [str(row_dictionary.get(column_key, "")) for column_key in leading_column_list]
        output_line_list.append(
            "| "
            + " | ".join(
                leading_value_list
                + [
                    format_metric(row_dictionary.get("mae")),
                    format_metric(row_dictionary.get("rmse")),
                    format_percentage_metric(row_dictionary.get("mean_percentage_error_pct")),
                    format_percentage_metric(row_dictionary.get("p95_mean_percentage_error_pct")),
                ]
            )
            + " |"
        )
    return output_line_list


def build_report_markdown(
    arguments: argparse.Namespace,
    matrix_summary_dictionary: dict[str, Any],
    collage_summary_dictionary: dict[str, Any],
    overlay_summary_dictionary: dict[str, Any],
    source_candidate_list: list[dict[str, Any]],
    ranked_candidate_row_list: list[dict[str, Any]],
) -> str:

    """Build the official report Markdown."""

    comparison_scope_dictionary = matrix_summary_dictionary.get("comparison_scope", {})
    if not isinstance(comparison_scope_dictionary, dict):
        comparison_scope_dictionary = {}

    visual_count_dictionary = collect_visual_source_count(
        collage_summary_dictionary,
        overlay_summary_dictionary,
        arguments.candidate_source_label,
    )
    if visual_count_dictionary["collage"] == 0:
        raise AssertionError(
            f"Collage summary does not expose source {arguments.candidate_source_label}."
        )
    if visual_count_dictionary["overlay_forward"] == 0 and visual_count_dictionary["overlay_backward"] == 0:
        raise AssertionError(
            f"Overlay summary does not expose source {arguments.candidate_source_label}."
        )

    source_candidate_count = len(source_candidate_list)
    strongest_candidate = ranked_candidate_row_list[0]
    surface_leader_row_list = collect_surface_leader_rows(ranked_candidate_row_list)
    direction_leader_row_list = collect_direction_leader_rows(matrix_summary_dictionary)
    candidate_inventory_row_list = [
        {
            "Surface": str(candidate_dictionary.get("candidate_surface", "")).strip(),
            "Candidate": str(candidate_dictionary.get("candidate_id", "")).strip(),
            "Family": str(candidate_dictionary.get("candidate_family", "")).strip(),
        }
        for candidate_dictionary in source_candidate_list
    ]

    output_line_list = [
        "# TE Curve Verification Pipeline Official Model Verification Report",
        "",
        "## Executive Verdict",
        "",
        f"This automated official refresh report closes `{arguments.refresh_label}`.",
        "",
        "Decision:",
        "",
        f"- `{arguments.candidate_source_label}` is closed as {arguments.decision}.",
        f"- The strongest refreshed aggregate candidate is `{strongest_candidate['candidate_id']}`.",
        "- The accepted direction-parallel baseline changes only after a human closure review records that promotion explicitly.",
        "- This launcher-generated report is part of the same operator run as the matrix, collage, overlay, and PDF exports.",
        "",
        "## Source Package",
        "",
        "This official report consolidates these refreshed artifacts:",
        "",
        "- metric matrix:",
        "  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;",
        "- matrix summary:",
        f"  `{normalize_path_text(arguments.matrix_summary_path)}`;",
        "- per-condition metrics:",
        f"  `{normalize_path_text(matrix_summary_dictionary.get('per_condition_metrics_csv_path'))}`;",
        "- best-model collage report:",
        f"  `{normalize_path_text(collage_summary_dictionary.get('report_path'))}`;",
        "- multi-model curve comparison report:",
        f"  `{normalize_path_text(overlay_summary_dictionary.get('report_path'))}`;",
    ]
    if arguments.operator_log_root is not None:
        output_line_list.extend(
            [
                "- operator launch logs:",
                f"  `{normalize_path_text(arguments.operator_log_root)}`.",
            ]
        )

    output_line_list.extend(
        [
            "",
            "## Candidate Refresh",
            "",
            f"The refresh added `{source_candidate_count}` candidates from "
            f"`{arguments.candidate_source_label}` into the official "
            f"`{comparison_scope_dictionary.get('candidate_count', 'n/a')}`-candidate matrix.",
            "",
            "| Surface | Candidate | Family |",
            "| --- | --- | --- |",
        ]
    )
    for row_dictionary in candidate_inventory_row_list:
        output_line_list.append(
            "| {Surface} | `{Candidate}` | `{Family}` |".format(**row_dictionary)
        )

    output_line_list.extend(
        [
            "",
            "## Refreshed Source Leaders",
            "",
            "The table ranks the refreshed source by aggregate offline TE Curve Verification Pipeline metrics.",
            "",
            *build_metric_table(
                [
                    {
                        "Surface": row_dictionary["surface"],
                        "Candidate": f"`{row_dictionary['candidate_id']}`",
                        **row_dictionary,
                    }
                    for row_dictionary in surface_leader_row_list
                ],
                ["Surface", "Candidate"],
            ),
            "",
            "## Refreshed Source Leaderboard",
            "",
            *build_metric_table(
                [
                    {
                        "Rank": str(rank_index),
                        "Surface": row_dictionary["surface"],
                        "Candidate": f"`{row_dictionary['candidate_id']}`",
                        **row_dictionary,
                    }
                    for rank_index, row_dictionary in enumerate(ranked_candidate_row_list, start=1)
                ],
                ["Rank", "Surface", "Candidate"],
            ),
            "",
            "## Current Direction Leaders",
            "",
            "These leaders are read from the matrix direction breakdown after the refresh.",
            "",
            *build_metric_table(
                [
                    {
                        "Direction": row_dictionary["direction"],
                        "Candidate": f"`{row_dictionary['candidate_id']}`",
                        **row_dictionary,
                    }
                    for row_dictionary in direction_leader_row_list
                ],
                ["Direction", "Candidate"],
            ),
            "",
            "## Visual Evidence",
            "",
            "The same launcher run regenerated the visual companion reports and verified",
            "that the refreshed source appears in the visual package.",
            "",
            "| Source | Collage | Overlay Forward | Overlay Backward |",
            "| --- | ---: | ---: | ---: |",
            f"| `{arguments.candidate_source_label}` | {visual_count_dictionary['collage']} | "
            f"{visual_count_dictionary['overlay_forward']} | "
            f"{visual_count_dictionary['overlay_backward']} |",
            "",
            "## Closeout Decision",
            "",
            f"`{arguments.refresh_label}` is closed as: {arguments.decision}.",
            "",
            arguments.next_step,
            "",
        ]
    )
    return "\n".join(output_line_list)


def build_track2_official_model_verification_report(arguments: argparse.Namespace) -> Path:

    """Build and write the official TE Curve Verification Pipeline model-verification report."""

    matrix_summary_dictionary = load_yaml_dictionary(arguments.matrix_summary_path)
    collage_summary_dictionary = load_yaml_dictionary(arguments.collage_summary_path)
    overlay_summary_dictionary = load_yaml_dictionary(arguments.overlay_summary_path)
    source_candidate_list = collect_source_candidate_list(
        matrix_summary_dictionary,
        arguments.candidate_source_label,
    )
    candidate_metric_dictionary = collect_candidate_metric_dictionary(matrix_summary_dictionary)
    ranked_candidate_row_list = collect_ranked_candidate_rows(
        source_candidate_list,
        candidate_metric_dictionary,
    )
    if not ranked_candidate_row_list:
        raise AssertionError(
            "The official report builder found refreshed candidates but no "
            "aggregate metrics for them."
        )

    output_report_path = arguments.output_report_path
    if output_report_path is None:
        output_report_path = (
            DEFAULT_OUTPUT_ROOT_PATH
            / f"[{arguments.report_date}]"
            / "track2_official_model_verification_report.md"
        )
    output_report_path.parent.mkdir(parents=True, exist_ok=True)
    report_markdown = build_report_markdown(
        arguments,
        matrix_summary_dictionary,
        collage_summary_dictionary,
        overlay_summary_dictionary,
        source_candidate_list,
        ranked_candidate_row_list,
    )
    output_report_path.write_text(report_markdown, encoding="utf-8")
    print(f"Prepared TE Curve Verification Pipeline official verification report | {output_report_path}")
    return output_report_path


if __name__ == "__main__":
    build_track2_official_model_verification_report(parse_command_line_arguments())
