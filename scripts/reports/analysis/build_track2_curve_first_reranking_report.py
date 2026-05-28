"""Build the Track 2B curve-first reranking report from Track 2 metrics."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from statistics import mean, pstdev
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import yaml

DEFAULT_TRACK2_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_reference_comparison"
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_curve_first_reranking"
DEFAULT_REPORT_TOPIC_ROOT = PROJECT_PATH / "doc" / "reports" / "analysis" / "track2" / "curve_first_reranking_report"
DEFAULT_PROGRAM_BEST_PATH = PROJECT_PATH / "output" / "registries" / "program" / "current_best_solution.yaml"

PER_CONDITION_METRICS_FILENAME = "per_condition_metrics.csv"
TRACK2_SUMMARY_FILENAME = "validation_summary.yaml"
OVERALL_RANKING_FILENAME = "candidate_curve_first_ranking.csv"
DIRECTION_RANKING_FILENAME = "direction_curve_first_ranking.csv"
SUMMARY_FILENAME = "track2_curve_first_reranking_summary.yaml"
REPORT_FILENAME = "track2_curve_first_reranking_report.md"


@dataclass(frozen=True)
class CandidateMetricSummary:

    """Curve-first aggregate metrics for one candidate scope."""

    rank: int
    candidate_id: str
    candidate_family: str
    candidate_kind: str
    candidate_source_label: str
    candidate_surface: str
    ranking_scope: str
    direction_label: str
    condition_count: int
    mean_curve_mae_deg: float
    mean_curve_rmse_deg: float
    mean_percentage_error_pct: float
    p95_mean_percentage_error_pct: float
    worst_mean_percentage_error_pct: float
    worst_curve_mae_deg: float
    worst_curve_rmse_deg: float
    std_mean_percentage_error_pct: float
    valid_direction_list: tuple[str, ...]

    def ranking_key(self) -> tuple[float, float, float, float, str]:

        """Return the deterministic curve-first ordering key."""

        return (
            self.mean_percentage_error_pct,
            self.p95_mean_percentage_error_pct,
            self.worst_mean_percentage_error_pct,
            self.mean_curve_mae_deg,
            self.candidate_id,
        )

    def to_csv_row(self) -> dict[str, Any]:

        """Return a serializable CSV row."""

        return {
            "rank": self.rank,
            "candidate_id": self.candidate_id,
            "candidate_family": self.candidate_family,
            "candidate_kind": self.candidate_kind,
            "candidate_source_label": self.candidate_source_label,
            "candidate_surface": self.candidate_surface,
            "ranking_scope": self.ranking_scope,
            "direction_label": self.direction_label,
            "condition_count": self.condition_count,
            "mean_curve_mae_deg": format_float(self.mean_curve_mae_deg),
            "mean_curve_rmse_deg": format_float(self.mean_curve_rmse_deg),
            "mean_percentage_error_pct": format_float(self.mean_percentage_error_pct),
            "p95_mean_percentage_error_pct": format_float(self.p95_mean_percentage_error_pct),
            "worst_mean_percentage_error_pct": format_float(self.worst_mean_percentage_error_pct),
            "worst_curve_mae_deg": format_float(self.worst_curve_mae_deg),
            "worst_curve_rmse_deg": format_float(self.worst_curve_rmse_deg),
            "std_mean_percentage_error_pct": format_float(self.std_mean_percentage_error_pct),
            "valid_direction_list": ", ".join(self.valid_direction_list),
        }


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Rerank accepted Track 2 candidates by full-curve validation metrics "
            "without rerunning training or changing the causal input contract."
        )
    )
    argument_parser.add_argument(
        "--track2-run-directory",
        type=Path,
        default=None,
        help="Optional Track 2 validation run directory. Defaults to the latest complete run.",
    )
    argument_parser.add_argument(
        "--track2-root",
        type=Path,
        default=DEFAULT_TRACK2_ROOT,
        help="Root containing Track 2 validation run directories.",
    )
    argument_parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root for generated reranking artifacts.",
    )
    argument_parser.add_argument(
        "--report-topic-root",
        type=Path,
        default=DEFAULT_REPORT_TOPIC_ROOT,
        help="Root for the dated Markdown report bundle.",
    )
    argument_parser.add_argument(
        "--program-best-path",
        type=Path,
        default=DEFAULT_PROGRAM_BEST_PATH,
        help="Program scalar-best registry used for scalar-vs-curve context.",
    )
    argument_parser.add_argument(
        "--report-date",
        type=str,
        default=None,
        help="Optional YYYY-MM-DD report bundle date.",
    )
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def resolve_runtime_project_relative_path(input_path: Path) -> Path:

    """Resolve a project-relative or absolute runtime path."""

    if input_path.is_absolute():
        return input_path
    return PROJECT_PATH / input_path


def resolve_timestamped_output_paths(
    output_root: Path,
    report_topic_root: Path,
    report_date: str | None,
) -> tuple[str, Path, Path]:

    """Resolve timestamped output and report directories."""

    current_timestamp = datetime.now().astimezone()
    run_instance_id = (
        f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}"
        "__track2b_curve_first_reranking"
    )
    if report_date is None:
        report_date = current_timestamp.strftime("%Y-%m-%d")
    else:
        datetime.strptime(report_date, "%Y-%m-%d")

    output_directory = resolve_runtime_project_relative_path(output_root) / run_instance_id
    report_directory = resolve_runtime_project_relative_path(report_topic_root) / f"[{report_date}]"
    output_directory.mkdir(parents=True, exist_ok=True)
    report_directory.mkdir(parents=True, exist_ok=True)
    return run_instance_id, output_directory, report_directory


def find_latest_complete_track2_run(track2_root: Path) -> Path:

    """Find the latest Track 2 run containing metrics and summary files."""

    resolved_root = resolve_runtime_project_relative_path(track2_root)
    if not resolved_root.exists():
        raise FileNotFoundError(f"Track 2 root does not exist: {resolved_root}")

    candidate_directory_list = sorted(
        [path for path in resolved_root.iterdir() if path.is_dir()],
        key=lambda path: path.name,
        reverse=True,
    )
    for candidate_directory in candidate_directory_list:
        metrics_path = candidate_directory / PER_CONDITION_METRICS_FILENAME
        summary_path = candidate_directory / TRACK2_SUMMARY_FILENAME
        if metrics_path.exists() and summary_path.exists():
            return candidate_directory
    raise FileNotFoundError(
        f"No complete Track 2 run found under {resolved_root} with "
        f"{PER_CONDITION_METRICS_FILENAME} and {TRACK2_SUMMARY_FILENAME}."
    )


def load_yaml_file(yaml_path: Path) -> dict[str, Any]:

    """Load a YAML mapping from disk."""

    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        loaded_data = yaml.safe_load(yaml_file) or {}
    if not isinstance(loaded_data, dict):
        raise TypeError(f"Expected YAML mapping in {yaml_path}")
    return loaded_data


def load_metrics_rows(metrics_path: Path) -> list[dict[str, Any]]:

    """Load Track 2 per-condition metric rows."""

    with metrics_path.open("r", encoding="utf-8", newline="") as metrics_file:
        reader = csv.DictReader(metrics_file)
        return [dict(row) for row in reader]


def parse_float(value: Any) -> float:

    """Parse a numeric metric value."""

    if value is None:
        return math.nan
    text_value = str(value).strip()
    if text_value == "":
        return math.nan
    return float(text_value)


def format_float(value: float) -> str:

    """Format a metric value for stable CSV and Markdown output."""

    if math.isnan(value):
        return ""
    return f"{value:.6f}"


def percentile(value_list: list[float], percentile_value: float) -> float:

    """Compute a deterministic linear percentile without adding dependencies."""

    clean_value_list = sorted(value for value in value_list if not math.isnan(value))
    if not clean_value_list:
        return math.nan
    if len(clean_value_list) == 1:
        return clean_value_list[0]
    fractional_index = (len(clean_value_list) - 1) * percentile_value / 100.0
    lower_index = math.floor(fractional_index)
    upper_index = math.ceil(fractional_index)
    if lower_index == upper_index:
        return clean_value_list[int(fractional_index)]
    lower_value = clean_value_list[lower_index]
    upper_value = clean_value_list[upper_index]
    weight = fractional_index - lower_index
    return lower_value + (upper_value - lower_value) * weight


def build_candidate_metadata_map(track2_summary: dict[str, Any]) -> dict[str, dict[str, Any]]:

    """Build a candidate metadata lookup from the Track 2 summary."""

    metadata_map: dict[str, dict[str, Any]] = {}
    for candidate_entry in track2_summary.get("candidate_list", []):
        if not isinstance(candidate_entry, dict):
            continue
        candidate_id = str(candidate_entry.get("candidate_id", "")).strip()
        if candidate_id:
            metadata_map[candidate_id] = candidate_entry
    return metadata_map


def build_candidate_summary(
    rank: int,
    candidate_id: str,
    row_list: list[dict[str, Any]],
    metadata_map: dict[str, dict[str, Any]],
    ranking_scope: str,
    direction_label: str,
) -> CandidateMetricSummary:

    """Build one aggregate candidate summary."""

    if not row_list:
        raise ValueError(f"No rows available for candidate {candidate_id}")

    first_row = row_list[0]
    metadata = metadata_map.get(candidate_id, {})
    curve_mae_list = [parse_float(row.get("curve_mae_deg")) for row in row_list]
    curve_rmse_list = [parse_float(row.get("curve_rmse_deg")) for row in row_list]
    mpe_list = [parse_float(row.get("mean_percentage_error_pct")) for row in row_list]
    clean_mpe_list = [value for value in mpe_list if not math.isnan(value)]
    valid_direction_list = tuple(
        sorted({str(row.get("direction_label", "")).strip() for row in row_list if row.get("direction_label")})
    )

    return CandidateMetricSummary(
        rank=rank,
        candidate_id=candidate_id,
        candidate_family=str(first_row.get("candidate_family", "")).strip(),
        candidate_kind=str(first_row.get("candidate_kind", "")).strip(),
        candidate_source_label=str(first_row.get("candidate_source_label", "")).strip(),
        candidate_surface=str(first_row.get("candidate_surface", "")).strip(),
        ranking_scope=ranking_scope,
        direction_label=direction_label,
        condition_count=len(row_list),
        mean_curve_mae_deg=mean([value for value in curve_mae_list if not math.isnan(value)]),
        mean_curve_rmse_deg=mean([value for value in curve_rmse_list if not math.isnan(value)]),
        mean_percentage_error_pct=mean(clean_mpe_list),
        p95_mean_percentage_error_pct=percentile(clean_mpe_list, 95.0),
        worst_mean_percentage_error_pct=max(clean_mpe_list),
        worst_curve_mae_deg=max(value for value in curve_mae_list if not math.isnan(value)),
        worst_curve_rmse_deg=max(value for value in curve_rmse_list if not math.isnan(value)),
        std_mean_percentage_error_pct=pstdev(clean_mpe_list) if len(clean_mpe_list) > 1 else 0.0,
        valid_direction_list=tuple(metadata.get("allowed_direction_list", valid_direction_list) or valid_direction_list),
    )


def rerank_summaries(summary_list: list[CandidateMetricSummary]) -> list[CandidateMetricSummary]:

    """Sort summaries and replace ranks after sorting."""

    sorted_summary_list = sorted(summary_list, key=lambda summary: summary.ranking_key())
    reranked_summary_list: list[CandidateMetricSummary] = []
    for rank_index, summary in enumerate(sorted_summary_list, start=1):
        reranked_summary_list.append(
            CandidateMetricSummary(
                rank=rank_index,
                candidate_id=summary.candidate_id,
                candidate_family=summary.candidate_family,
                candidate_kind=summary.candidate_kind,
                candidate_source_label=summary.candidate_source_label,
                candidate_surface=summary.candidate_surface,
                ranking_scope=summary.ranking_scope,
                direction_label=summary.direction_label,
                condition_count=summary.condition_count,
                mean_curve_mae_deg=summary.mean_curve_mae_deg,
                mean_curve_rmse_deg=summary.mean_curve_rmse_deg,
                mean_percentage_error_pct=summary.mean_percentage_error_pct,
                p95_mean_percentage_error_pct=summary.p95_mean_percentage_error_pct,
                worst_mean_percentage_error_pct=summary.worst_mean_percentage_error_pct,
                worst_curve_mae_deg=summary.worst_curve_mae_deg,
                worst_curve_rmse_deg=summary.worst_curve_rmse_deg,
                std_mean_percentage_error_pct=summary.std_mean_percentage_error_pct,
                valid_direction_list=summary.valid_direction_list,
            )
        )
    return reranked_summary_list


def build_rankings(
    metrics_row_list: list[dict[str, Any]],
    metadata_map: dict[str, dict[str, Any]],
) -> tuple[list[CandidateMetricSummary], list[CandidateMetricSummary]]:

    """Build overall and direction-specific curve-first rankings."""

    candidate_row_map: dict[str, list[dict[str, Any]]] = defaultdict(list)
    direction_candidate_row_map: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for metrics_row in metrics_row_list:
        candidate_id = str(metrics_row.get("candidate_id", "")).strip()
        direction_label = str(metrics_row.get("direction_label", "")).strip()
        if not candidate_id or not direction_label:
            continue
        candidate_row_map[candidate_id].append(metrics_row)
        direction_candidate_row_map[(direction_label, candidate_id)].append(metrics_row)

    overall_summary_list = [
        build_candidate_summary(
            rank=0,
            candidate_id=candidate_id,
            row_list=row_list,
            metadata_map=metadata_map,
            ranking_scope="overall_valid_direction_surface",
            direction_label="all_valid",
        )
        for candidate_id, row_list in candidate_row_map.items()
    ]
    direction_summary_map: dict[str, list[CandidateMetricSummary]] = defaultdict(list)
    for (direction_label, candidate_id), row_list in direction_candidate_row_map.items():
        direction_summary_map[direction_label].append(
            build_candidate_summary(
                rank=0,
                candidate_id=candidate_id,
                row_list=row_list,
                metadata_map=metadata_map,
                ranking_scope=f"{direction_label}_only",
                direction_label=direction_label,
            )
        )

    direction_summary_list: list[CandidateMetricSummary] = []
    for direction_label in sorted(direction_summary_map):
        direction_summary_list.extend(rerank_summaries(direction_summary_map[direction_label]))

    return rerank_summaries(overall_summary_list), direction_summary_list


def write_ranking_csv(csv_path: Path, summary_list: list[CandidateMetricSummary]) -> None:

    """Write a ranking CSV file."""

    field_name_list = list(summary_list[0].to_csv_row().keys()) if summary_list else []
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_list, lineterminator="\n")
        writer.writeheader()
        for summary in summary_list:
            writer.writerow(summary.to_csv_row())


def build_surface_leader_map(
    overall_summary_list: list[CandidateMetricSummary],
) -> dict[str, CandidateMetricSummary]:

    """Return the best candidate per candidate surface."""

    surface_leader_map: dict[str, CandidateMetricSummary] = {}
    for summary in overall_summary_list:
        surface = summary.candidate_surface or "unspecified"
        if surface not in surface_leader_map:
            surface_leader_map[surface] = summary
    return surface_leader_map


def load_scalar_program_best(program_best_path: Path) -> dict[str, Any]:

    """Load the scalar registry best entry when available."""

    resolved_program_best_path = resolve_runtime_project_relative_path(program_best_path)
    if not resolved_program_best_path.exists():
        return {}
    program_best_data = load_yaml_file(resolved_program_best_path)
    best_entry = program_best_data.get("best_entry", {})
    return best_entry if isinstance(best_entry, dict) else {}


def markdown_table(header_list: list[str], row_list: list[list[str]]) -> list[str]:

    """Build a compact Markdown table."""

    line_list = [
        "| " + " | ".join(header_list) + " |",
        "| " + " | ".join(["---"] * len(header_list)) + " |",
    ]
    for row in row_list:
        line_list.append("| " + " | ".join(row) + " |")
    return line_list


def build_summary_table_rows(summary_list: list[CandidateMetricSummary], limit: int) -> list[list[str]]:

    """Build Markdown table rows for candidate summaries."""

    row_list: list[list[str]] = []
    for summary in summary_list[:limit]:
        row_list.append(
            [
                str(summary.rank),
                f"`{summary.candidate_id}`",
                f"`{summary.candidate_family}`",
                summary.candidate_source_label,
                summary.candidate_surface,
                summary.direction_label,
                str(summary.condition_count),
                format_float(summary.mean_percentage_error_pct),
                format_float(summary.p95_mean_percentage_error_pct),
                format_float(summary.worst_mean_percentage_error_pct),
                format_float(summary.mean_curve_mae_deg),
            ]
        )
    return row_list


def build_direction_section(
    direction_summary_list: list[CandidateMetricSummary],
    direction_label: str,
) -> list[str]:

    """Build one direction-specific report section."""

    filtered_summary_list = [summary for summary in direction_summary_list if summary.direction_label == direction_label]
    line_list = [f"## {direction_label.title()} Curve-First Leaders", ""]
    line_list.extend(
        markdown_table(
            [
                "Rank",
                "Candidate",
                "Family",
                "Source",
                "Surface",
                "Direction",
                "Curves",
                "Mean MPE [%]",
                "P95 MPE [%]",
                "Worst MPE [%]",
                "Mean Curve MAE [deg]",
            ],
            build_summary_table_rows(filtered_summary_list, 12),
        )
    )
    line_list.append("")
    return line_list


def build_report_lines(
    run_instance_id: str,
    track2_run_directory: Path,
    output_directory: Path,
    overall_summary_list: list[CandidateMetricSummary],
    direction_summary_list: list[CandidateMetricSummary],
    track2_summary: dict[str, Any],
    scalar_best_entry: dict[str, Any],
) -> list[str]:

    """Build the Markdown report body."""

    overall_winner = overall_summary_list[0]
    surface_leader_map = build_surface_leader_map(overall_summary_list)
    comparison_scope = track2_summary.get("comparison_scope", {})
    curve_count = comparison_scope.get("curve_count", "unknown")
    candidate_count = comparison_scope.get("candidate_count", "unknown")

    line_list = [
        "# Track 2B Curve-First Reranking Report",
        "",
        "## Overview",
        "",
        (
            "This report reranks the already accepted `Track 2` candidate matrix "
            "by full-curve validation behavior. It does not execute training, "
            "does not alter the dataset structure, and does not provide future "
            "curve samples to any model."
        ),
        "",
        f"- Run Instance: `{run_instance_id}`",
        f"- Source Track 2 Run: `{track2_run_directory.relative_to(PROJECT_PATH)}`",
        f"- Source Curve Count: `{curve_count}`",
        f"- Source Candidate Count: `{candidate_count}`",
        f"- Generated Artifact Directory: `{output_directory.relative_to(PROJECT_PATH)}`",
        "",
        "## Method",
        "",
        (
            "The primary ordering key is mean `Track 2` mean-percentage-error over "
            "each candidate's valid direction surface. Ties are resolved by P95 "
            "mean-percentage-error, worst mean-percentage-error, and mean curve "
            "`MAE`. This keeps scalar pointwise registry metrics separate from "
            "curve-following evidence."
        ),
        "",
        "Available diagnostics from the existing `Track 2` matrix:",
        "",
        "- mean curve `MAE` and `RMSE` per operating condition;",
        "- mean percentage error per operating condition;",
        "- P95, worst-condition, and standard-deviation aggregates across conditions.",
        "",
        "Deferred diagnostics requiring a future curve-payload export:",
        "",
        "- harmonic amplitude and phase error by order;",
        "- derivative or slope continuity error;",
        "- per-revolution residual drift and continuity checks across stitched curves.",
        "",
        "## Causal Input Boundary",
        "",
        (
            "The validation surface is full-curve because the compensation target is "
            "continuous `TE` over many consecutive motor revolutions. The runtime "
            "input contract remains causal: current point-level operating state, "
            "optional short history of already observed samples, or derived causal "
            "features only."
        ),
        "",
        "## Overall Curve-First Leaders",
        "",
    ]
    line_list.extend(
        markdown_table(
            [
                "Rank",
                "Candidate",
                "Family",
                "Source",
                "Surface",
                "Direction",
                "Curves",
                "Mean MPE [%]",
                "P95 MPE [%]",
                "Worst MPE [%]",
                "Mean Curve MAE [deg]",
            ],
            build_summary_table_rows(overall_summary_list, 15),
        )
    )
    line_list.extend([""])
    line_list.extend(build_direction_section(direction_summary_list, "forward"))
    line_list.extend(build_direction_section(direction_summary_list, "backward"))
    line_list.extend(
        [
            "## Surface Leaders",
            "",
        ]
    )
    surface_row_list = []
    for surface, summary in sorted(surface_leader_map.items()):
        surface_row_list.append(
            [
                surface,
                f"`{summary.candidate_id}`",
                f"`{summary.candidate_family}`",
                summary.candidate_source_label,
                str(summary.condition_count),
                format_float(summary.mean_percentage_error_pct),
                format_float(summary.p95_mean_percentage_error_pct),
                format_float(summary.mean_curve_mae_deg),
            ]
        )
    line_list.extend(
        markdown_table(
            [
                "Surface",
                "Leader",
                "Family",
                "Source",
                "Curves",
                "Mean MPE [%]",
                "P95 MPE [%]",
                "Mean Curve MAE [deg]",
            ],
            surface_row_list,
        )
    )
    line_list.extend(
        [
            "",
            "## Scalar Registry Context",
            "",
        ]
    )
    if scalar_best_entry:
        line_list.extend(
            [
                (
                    f"- Current scalar registry winner: `{scalar_best_entry.get('run_name', 'unknown')}` "
                    f"from family `{scalar_best_entry.get('model_family', 'unknown')}`."
                ),
                (
                    f"- Scalar test `MAE`: `{float(scalar_best_entry.get('test_mae', math.nan)):.6f}` "
                    f"and scalar test `RMSE`: `{float(scalar_best_entry.get('test_rmse', math.nan)):.6f}`."
                ),
            ]
        )
    else:
        line_list.append("- Current scalar registry winner was not available.")
    line_list.extend(
        [
            "",
            (
                f"The curve-first winner in this reranking is `{overall_winner.candidate_id}` "
                f"from family `{overall_winner.candidate_family}` with mean `MPE` "
                f"`{format_float(overall_winner.mean_percentage_error_pct)}` percent and "
                f"P95 `MPE` `{format_float(overall_winner.p95_mean_percentage_error_pct)}` percent."
            ),
            "",
            "## Decision",
            "",
            (
                "This pass standardizes the curve-first evidence surface and should be "
                "used before deciding whether the next branch is a loss/reranking "
                "change for existing families or a new model-family wave. It does "
                "not promote a new program-best model by itself because richer "
                "harmonic/phase diagnostics still require curve-payload export."
            ),
            "",
            "Machine-readable artifacts:",
            "",
            f"- `{(output_directory / OVERALL_RANKING_FILENAME).relative_to(PROJECT_PATH)}`",
            f"- `{(output_directory / DIRECTION_RANKING_FILENAME).relative_to(PROJECT_PATH)}`",
            f"- `{(output_directory / SUMMARY_FILENAME).relative_to(PROJECT_PATH)}`",
            "",
        ]
    )
    return line_list


def write_summary_yaml(
    summary_path: Path,
    run_instance_id: str,
    track2_run_directory: Path,
    output_directory: Path,
    report_path: Path,
    overall_summary_list: list[CandidateMetricSummary],
    direction_summary_list: list[CandidateMetricSummary],
) -> None:

    """Write the machine-readable reranking summary."""

    forward_leader_list = [
        summary for summary in direction_summary_list if summary.direction_label == "forward"
    ]
    backward_leader_list = [
        summary for summary in direction_summary_list if summary.direction_label == "backward"
    ]
    summary_payload = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "source_track2_run_directory": str(track2_run_directory.relative_to(PROJECT_PATH)),
        "output_directory": str(output_directory.relative_to(PROJECT_PATH)),
        "report_path": str(report_path.relative_to(PROJECT_PATH)),
        "ranking_policy": {
            "primary_metric": "mean_percentage_error_pct",
            "first_tie_breaker": "p95_mean_percentage_error_pct",
            "second_tie_breaker": "worst_mean_percentage_error_pct",
            "third_tie_breaker": "mean_curve_mae_deg",
            "direction": "minimize",
            "causal_input_contract": (
                "current point, optional short causal history, or derived causal features only"
            ),
        },
        "overall_best": overall_summary_list[0].to_csv_row() if overall_summary_list else {},
        "forward_best": forward_leader_list[0].to_csv_row() if forward_leader_list else {},
        "backward_best": backward_leader_list[0].to_csv_row() if backward_leader_list else {},
        "deferred_diagnostics": [
            "harmonic_amplitude_error_by_order",
            "harmonic_phase_error_by_order",
            "derivative_or_slope_continuity_error",
            "stitched_revolution_residual_drift",
        ],
    }
    with summary_path.open("w", encoding="utf-8") as summary_file:
        yaml.safe_dump(summary_payload, summary_file, sort_keys=False, allow_unicode=False)


def main() -> None:

    """Run the report generation workflow."""

    arguments = parse_command_line_arguments()
    track2_run_directory = (
        resolve_runtime_project_relative_path(arguments.track2_run_directory)
        if arguments.track2_run_directory is not None
        else find_latest_complete_track2_run(arguments.track2_root)
    )
    metrics_path = track2_run_directory / PER_CONDITION_METRICS_FILENAME
    track2_summary_path = track2_run_directory / TRACK2_SUMMARY_FILENAME
    if not metrics_path.exists():
        raise FileNotFoundError(f"Missing Track 2 metrics CSV: {metrics_path}")
    if not track2_summary_path.exists():
        raise FileNotFoundError(f"Missing Track 2 summary YAML: {track2_summary_path}")

    run_instance_id, output_directory, report_directory = resolve_timestamped_output_paths(
        output_root=arguments.output_root,
        report_topic_root=arguments.report_topic_root,
        report_date=arguments.report_date,
    )
    report_path = report_directory / REPORT_FILENAME
    overall_ranking_path = output_directory / OVERALL_RANKING_FILENAME
    direction_ranking_path = output_directory / DIRECTION_RANKING_FILENAME
    summary_path = output_directory / SUMMARY_FILENAME

    track2_summary = load_yaml_file(track2_summary_path)
    metadata_map = build_candidate_metadata_map(track2_summary)
    metrics_row_list = load_metrics_rows(metrics_path)
    overall_summary_list, direction_summary_list = build_rankings(metrics_row_list, metadata_map)
    scalar_best_entry = load_scalar_program_best(arguments.program_best_path)

    write_ranking_csv(overall_ranking_path, overall_summary_list)
    write_ranking_csv(direction_ranking_path, direction_summary_list)
    write_summary_yaml(
        summary_path=summary_path,
        run_instance_id=run_instance_id,
        track2_run_directory=track2_run_directory,
        output_directory=output_directory,
        report_path=report_path,
        overall_summary_list=overall_summary_list,
        direction_summary_list=direction_summary_list,
    )
    report_lines = build_report_lines(
        run_instance_id=run_instance_id,
        track2_run_directory=track2_run_directory,
        output_directory=output_directory,
        overall_summary_list=overall_summary_list,
        direction_summary_list=direction_summary_list,
        track2_summary=track2_summary,
        scalar_best_entry=scalar_best_entry,
    )
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Wrote Track 2B curve-first report: {report_path}")
    print(f"Wrote Track 2B reranking artifacts: {output_directory}")


if __name__ == "__main__":
    main()
