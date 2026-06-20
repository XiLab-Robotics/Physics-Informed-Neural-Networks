"""Build a parity report across the saved RCIM paper-reference archives."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[4]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.tooling import repository_path_support
from scripts.training import shared_training_infrastructure

TRACK2_VALIDATION_ROOT = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2_reference_comparison"
)
OUTPUT_ROOT = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "rcim_paper_reference_archive_parity"
)
CANONICAL_REPORT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "RCIM Paper Reference Archive Parity Interpretation.md"
)
TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"
SOURCE_LABEL_LIST = ["rcim_original", "rcim_retuned", "rcim_track1"]
FAMILY_LABEL_LIST = [
    "SVM",
    "MLP",
    "RF",
    "DT",
    "ET",
    "ERT",
    "GBM",
    "HGBM",
    "XGBM",
    "LGBM",
    "ELM",
]
PAIRWISE_COMPARISON_LIST = [
    {
        "comparison_id": "forward_original_vs_retuned",
        "direction_label": "forward",
        "surface_label": "Fw",
        "left_source_label": "rcim_original",
        "right_source_label": "rcim_retuned",
    },
    {
        "comparison_id": "forward_original_vs_track1",
        "direction_label": "forward",
        "surface_label": "Fw",
        "left_source_label": "rcim_original",
        "right_source_label": "rcim_track1",
    },
    {
        "comparison_id": "forward_retuned_vs_track1",
        "direction_label": "forward",
        "surface_label": "Fw",
        "left_source_label": "rcim_retuned",
        "right_source_label": "rcim_track1",
    },
    {
        "comparison_id": "backward_retuned_vs_track1",
        "direction_label": "backward",
        "surface_label": "Bw",
        "left_source_label": "rcim_retuned",
        "right_source_label": "rcim_track1",
    },
]


def load_yaml_dictionary(yaml_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    with yaml_path.open("r", encoding="utf-8") as yaml_file:
        loaded_dictionary = yaml.safe_load(yaml_file)
    assert isinstance(loaded_dictionary, dict), f"Expected YAML dictionary | {yaml_path}"
    return loaded_dictionary


def find_latest_track2_validation_summary() -> Path:

    """Find the newest TE Curve Verification Pipeline validation summary with paper-reference metrics."""

    candidate_path_list = sorted(
        TRACK2_VALIDATION_ROOT.glob("*/validation_summary.yaml"),
        key=lambda candidate_path: candidate_path.stat().st_mtime,
        reverse=True,
    )
    for candidate_path in candidate_path_list:
        summary_dictionary = load_yaml_dictionary(candidate_path)
        candidate_source_set = {
            str(candidate_entry["candidate_source_label"])
            for candidate_entry in summary_dictionary.get("candidate_list", [])
        }
        if set(SOURCE_LABEL_LIST).issubset(candidate_source_set):
            return candidate_path

    raise FileNotFoundError(
        "Could not find a TE Curve Verification Pipeline validation summary containing all paper-reference archives."
    )


def resolve_candidate_key(source_label: str, family_label: str, surface_label: str) -> str:

    """Resolve the TE Curve Verification Pipeline candidate id for one paper-reference archive model."""

    if source_label == "rcim_track1":
        return f"{family_label}19_{surface_label}"
    return f"{source_label}_{family_label}19_{surface_label}"


def resolve_composite_candidate_key(source_label: str, surface_label: str) -> str | None:

    """Resolve the composed best-candidate id for one source and surface."""

    if source_label == "rcim_original" and surface_label == "Fw":
        return "paper_original_best_Fw"
    if source_label == "rcim_retuned" and surface_label == "Fw":
        return "paper_retuned_best_Fw"
    if source_label == "rcim_track1" and surface_label == "Fw":
        return "track1_best_Fw"
    if source_label == "rcim_retuned" and surface_label == "Bw":
        return "paper_retuned_best_Bw"
    if source_label == "rcim_track1" and surface_label == "Bw":
        return "track1_best_Bw"
    return None


def build_candidate_lookup(track2_summary: dict[str, Any]) -> dict[str, dict[str, Any]]:

    """Build a lookup from candidate id to candidate metadata."""

    return {
        str(candidate_entry["candidate_id"]): candidate_entry
        for candidate_entry in track2_summary["candidate_list"]
    }


def resolve_direction_metric(
    track2_summary: dict[str, Any],
    candidate_id: str,
    direction_label: str,
) -> dict[str, float] | None:

    """Resolve the direction-filtered TE Curve Verification Pipeline curve metric for one candidate."""

    direction_breakdown = track2_summary["direction_breakdown"]
    direction_dictionary = direction_breakdown.get(direction_label, {})
    metric_dictionary = direction_dictionary.get(candidate_id)
    if metric_dictionary is None:
        return None
    return {
        "curve_mae_deg": float(metric_dictionary["mae"]),
        "curve_rmse_deg": float(metric_dictionary["rmse"]),
        "mean_percentage_error_pct": float(metric_dictionary["mean_percentage_error_pct"]),
        "p95_mean_percentage_error_pct": float(metric_dictionary["p95_mean_percentage_error_pct"]),
    }


def resolve_target_metric(
    track2_summary: dict[str, Any],
    candidate_id: str,
) -> dict[str, float] | None:

    """Resolve the target-level metric summary for one reference-bank candidate."""

    target_metric_dictionary = track2_summary.get("candidate_target_metric_summary", {}).get(candidate_id)
    if target_metric_dictionary is None:
        return None
    return {
        "amplitude_mae": float(target_metric_dictionary["amplitude_mae"]),
        "amplitude_rmse": float(target_metric_dictionary["amplitude_rmse"]),
        "phase_mae_rad": float(target_metric_dictionary["phase_mae_rad"]),
        "phase_rmse_rad": float(target_metric_dictionary["phase_rmse_rad"]),
    }


def build_curve_metric_row_list(track2_summary: dict[str, Any]) -> list[dict[str, Any]]:

    """Build family-level TE Curve Verification Pipeline curve metric rows for paper-reference archives."""

    candidate_lookup = build_candidate_lookup(track2_summary)
    row_list: list[dict[str, Any]] = []
    comparison_surface_list = [
        ("forward", "Fw", ["rcim_original", "rcim_retuned", "rcim_track1"]),
        ("backward", "Bw", ["rcim_retuned", "rcim_track1"]),
    ]

    for direction_label, surface_label, source_label_list in comparison_surface_list:
        for source_label in source_label_list:
            for family_label in FAMILY_LABEL_LIST:
                candidate_id = resolve_candidate_key(source_label, family_label, surface_label)
                if candidate_id not in candidate_lookup:
                    continue
                metric_dictionary = resolve_direction_metric(track2_summary, candidate_id, direction_label)
                if metric_dictionary is None:
                    continue
                row_list.append(
                    {
                        "candidate_id": candidate_id,
                        "source_label": source_label,
                        "family_label": family_label,
                        "surface_label": surface_label,
                        "direction_label": direction_label,
                        **metric_dictionary,
                    }
                )

            composite_candidate_id = resolve_composite_candidate_key(source_label, surface_label)
            if composite_candidate_id is None or composite_candidate_id not in candidate_lookup:
                continue
            metric_dictionary = resolve_direction_metric(
                track2_summary,
                composite_candidate_id,
                direction_label,
            )
            if metric_dictionary is None:
                continue
            row_list.append(
                {
                    "candidate_id": composite_candidate_id,
                    "source_label": source_label,
                    "family_label": "best_composite",
                    "surface_label": surface_label,
                    "direction_label": direction_label,
                    **metric_dictionary,
                }
            )

    return row_list


def build_target_metric_row_list(track2_summary: dict[str, Any]) -> list[dict[str, Any]]:

    """Build harmonic-target metric rows for paper-reference archives."""

    candidate_lookup = build_candidate_lookup(track2_summary)
    row_list: list[dict[str, Any]] = []
    comparison_surface_list = [
        ("Fw", ["rcim_original", "rcim_retuned", "rcim_track1"]),
        ("Bw", ["rcim_retuned", "rcim_track1"]),
    ]

    for surface_label, source_label_list in comparison_surface_list:
        for source_label in source_label_list:
            for family_label in FAMILY_LABEL_LIST:
                candidate_id = resolve_candidate_key(source_label, family_label, surface_label)
                if candidate_id not in candidate_lookup:
                    continue
                metric_dictionary = resolve_target_metric(track2_summary, candidate_id)
                if metric_dictionary is None:
                    continue
                row_list.append(
                    {
                        "candidate_id": candidate_id,
                        "source_label": source_label,
                        "family_label": family_label,
                        "surface_label": surface_label,
                        **metric_dictionary,
                    }
                )

    return row_list


def write_csv(row_list: list[dict[str, Any]], csv_path: Path) -> None:

    """Write a homogeneous row list to CSV."""

    assert row_list, f"Cannot write empty CSV | {csv_path}"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    field_name_list = list(row_list[0].keys())
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_name_list)
        csv_writer.writeheader()
        csv_writer.writerows(row_list)


def build_row_lookup(row_list: list[dict[str, Any]]) -> dict[tuple[str, str, str], dict[str, Any]]:

    """Build a source/family/surface lookup for metric rows."""

    return {
        (
            str(row["source_label"]),
            str(row["family_label"]),
            str(row["surface_label"]),
        ): row
        for row in row_list
    }


def classify_pairwise_similarity(delta_mean_percentage_error_pct: float) -> str:

    """Classify archive similarity from the TE Curve Verification Pipeline MPE delta."""

    absolute_delta = abs(float(delta_mean_percentage_error_pct))
    if absolute_delta <= 0.25:
        return "near-equivalent"
    if absolute_delta <= 2.0:
        return "similar"
    return "substantial difference"


def build_pairwise_comparison_row_list(
    curve_metric_row_list: list[dict[str, Any]],
    target_metric_row_list: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    """Build same-family pairwise comparisons across archive groups."""

    curve_lookup = build_row_lookup(curve_metric_row_list)
    target_lookup = build_row_lookup(target_metric_row_list)
    row_list: list[dict[str, Any]] = []

    for comparison_configuration in PAIRWISE_COMPARISON_LIST:
        surface_label = str(comparison_configuration["surface_label"])
        left_source_label = str(comparison_configuration["left_source_label"])
        right_source_label = str(comparison_configuration["right_source_label"])
        for family_label in FAMILY_LABEL_LIST:
            left_key = (left_source_label, family_label, surface_label)
            right_key = (right_source_label, family_label, surface_label)
            if left_key not in curve_lookup or right_key not in curve_lookup:
                continue

            left_curve_row = curve_lookup[left_key]
            right_curve_row = curve_lookup[right_key]
            left_target_row = target_lookup.get(left_key)
            right_target_row = target_lookup.get(right_key)
            delta_mean_percentage_error_pct = (
                float(right_curve_row["mean_percentage_error_pct"])
                - float(left_curve_row["mean_percentage_error_pct"])
            )
            delta_curve_mae_deg = (
                float(right_curve_row["curve_mae_deg"])
                - float(left_curve_row["curve_mae_deg"])
            )
            row = {
                "comparison_id": str(comparison_configuration["comparison_id"]),
                "direction_label": str(comparison_configuration["direction_label"]),
                "surface_label": surface_label,
                "family_label": family_label,
                "left_source_label": left_source_label,
                "right_source_label": right_source_label,
                "left_candidate_id": str(left_curve_row["candidate_id"]),
                "right_candidate_id": str(right_curve_row["candidate_id"]),
                "left_mean_percentage_error_pct": float(left_curve_row["mean_percentage_error_pct"]),
                "right_mean_percentage_error_pct": float(right_curve_row["mean_percentage_error_pct"]),
                "delta_mean_percentage_error_pct": delta_mean_percentage_error_pct,
                "left_curve_mae_deg": float(left_curve_row["curve_mae_deg"]),
                "right_curve_mae_deg": float(right_curve_row["curve_mae_deg"]),
                "delta_curve_mae_deg": delta_curve_mae_deg,
                "similarity_verdict": classify_pairwise_similarity(delta_mean_percentage_error_pct),
                "delta_amplitude_mae": None,
                "delta_phase_mae_rad": None,
            }
            if left_target_row is not None and right_target_row is not None:
                row["delta_amplitude_mae"] = (
                    float(right_target_row["amplitude_mae"])
                    - float(left_target_row["amplitude_mae"])
                )
                row["delta_phase_mae_rad"] = (
                    float(right_target_row["phase_mae_rad"])
                    - float(left_target_row["phase_mae_rad"])
                )
            row_list.append(row)

    return row_list


def select_rows(
    row_list: list[dict[str, Any]],
    direction_label: str,
    source_label: str,
) -> list[dict[str, Any]]:

    """Select rows for one direction and source."""

    selected_row_list = [
        row
        for row in row_list
        if row["direction_label"] == direction_label
        and row["source_label"] == source_label
    ]
    return sorted(selected_row_list, key=lambda row: float(row["mean_percentage_error_pct"]))


def find_best_row(
    row_list: list[dict[str, Any]],
    direction_label: str,
    source_label: str,
    include_composite: bool = False,
) -> dict[str, Any]:

    """Find the best curve row for one source and direction."""

    selected_row_list = [
        row
        for row in row_list
        if row["direction_label"] == direction_label
        and row["source_label"] == source_label
        and (include_composite or row["family_label"] != "best_composite")
    ]
    assert selected_row_list, f"No rows for {source_label} {direction_label}"
    return min(selected_row_list, key=lambda row: float(row["mean_percentage_error_pct"]))


def format_float(value: float, decimal_count: int = 3) -> str:

    """Format one floating-point value for Markdown tables."""

    return f"{value:.{decimal_count}f}"


def build_curve_table(row_list: list[dict[str, Any]]) -> list[str]:

    """Build one Markdown table for TE Curve Verification Pipeline curve rows."""

    line_list = [
        "| Candidate | Family | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for row in row_list:
        line_list.append(
            "| "
            f"`{row['candidate_id']}` | "
            f"`{row['family_label']}` | "
            f"{format_float(float(row['curve_mae_deg']), 6)} | "
            f"{format_float(float(row['curve_rmse_deg']), 6)} | "
            f"{format_float(float(row['mean_percentage_error_pct']), 3)} | "
            f"{format_float(float(row['p95_mean_percentage_error_pct']), 3)} |"
        )
    return line_list


def build_target_table(row_list: list[dict[str, Any]]) -> list[str]:

    """Build one Markdown table for target-level rows."""

    line_list = [
        "| Candidate | Family | Amplitude MAE | Amplitude RMSE | Phase MAE [rad] | Phase RMSE [rad] |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for row in row_list:
        line_list.append(
            "| "
            f"`{row['candidate_id']}` | "
            f"`{row['family_label']}` | "
            f"{format_float(float(row['amplitude_mae']), 6)} | "
            f"{format_float(float(row['amplitude_rmse']), 6)} | "
            f"{format_float(float(row['phase_mae_rad']), 6)} | "
            f"{format_float(float(row['phase_rmse_rad']), 6)} |"
        )
    return line_list


def select_pairwise_rows(
    row_list: list[dict[str, Any]],
    comparison_id: str,
) -> list[dict[str, Any]]:

    """Select pairwise rows for one comparison id."""

    return [
        row
        for row in row_list
        if row["comparison_id"] == comparison_id
    ]


def build_pairwise_table(row_list: list[dict[str, Any]]) -> list[str]:

    """Build one Markdown table for same-family archive pairwise rows."""

    line_list = [
        "| Family | Left Candidate | Right Candidate | Left MPE [%] | Right MPE [%] | Delta MPE [pp] | Delta Curve MAE [deg] | Verdict |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in row_list:
        line_list.append(
            "| "
            f"`{row['family_label']}` | "
            f"`{row['left_candidate_id']}` | "
            f"`{row['right_candidate_id']}` | "
            f"{format_float(float(row['left_mean_percentage_error_pct']), 3)} | "
            f"{format_float(float(row['right_mean_percentage_error_pct']), 3)} | "
            f"{format_float(float(row['delta_mean_percentage_error_pct']), 3)} | "
            f"{format_float(float(row['delta_curve_mae_deg']), 6)} | "
            f"`{row['similarity_verdict']}` |"
        )
    return line_list


def build_pairwise_verdict_summary(row_list: list[dict[str, Any]]) -> list[str]:

    """Build compact count summary for pairwise verdict classes."""

    line_list = [
        "| Comparison | Near-Equivalent | Similar | Substantial Difference |",
        "| --- | ---: | ---: | ---: |",
    ]
    for comparison_configuration in PAIRWISE_COMPARISON_LIST:
        comparison_id = str(comparison_configuration["comparison_id"])
        selected_row_list = select_pairwise_rows(row_list, comparison_id)
        verdict_count_dictionary = {
            "near-equivalent": 0,
            "similar": 0,
            "substantial difference": 0,
        }
        for row in selected_row_list:
            verdict_count_dictionary[str(row["similarity_verdict"])] += 1
        line_list.append(
            "| "
            f"`{comparison_id}` | "
            f"{verdict_count_dictionary['near-equivalent']} | "
            f"{verdict_count_dictionary['similar']} | "
            f"{verdict_count_dictionary['substantial difference']} |"
        )
    return line_list


def build_canonical_report_markdown(summary_dictionary: dict[str, Any]) -> str:

    """Build the canonical paper-reference archive parity Markdown report."""

    curve_row_list = summary_dictionary["curve_metric_row_list"]
    target_row_list = summary_dictionary["target_metric_row_list"]
    pairwise_row_list = summary_dictionary["pairwise_comparison_row_list"]
    forward_original_best = find_best_row(curve_row_list, "forward", "rcim_original")
    forward_retuned_best = find_best_row(curve_row_list, "forward", "rcim_retuned")
    forward_track1_best = find_best_row(curve_row_list, "forward", "rcim_track1")
    backward_retuned_best = find_best_row(curve_row_list, "backward", "rcim_retuned")
    backward_track1_best = find_best_row(curve_row_list, "backward", "rcim_track1")

    report_line_list = [
        "# RCIM Paper Reference Archive Parity Interpretation",
        "",
        "## Executive Verdict",
        "",
        "The repository paper-reference archives are internally consistent but they",
        "are not three equivalent implementations of the same fitted model surface.",
        "",
        "The direct same-family comparison shows that `rcim_original/forward` and",
        "`rcim_retuned/forward` are mostly similar, with `DT` and `LGBM` effectively",
        "near-equivalent on TE Curve Verification Pipeline curve metrics and substantial differences only",
        "for `MLP` and `ELM`. By contrast, `rcim_track1` is not a near-copy of either",
        "`rcim_original` or `rcim_retuned`: many forward families and all backward",
        "families show substantial TE Curve Verification Pipeline metric differences.",
        "",
        "`rcim_original/forward` remains the recovered original-pipeline baseline.",
        "`rcim_retuned` is the closest repository-local continuation of that",
        "pipeline and the strongest TE Curve Verification Pipeline curve performer in this comparison.",
        "`rcim_track1` is the closed faithful full-dataset RCIM Model-Bank Reproduction archive: it is",
        "structurally complete and direction-valid, but it is a materially different",
        "trained archive rather than an interchangeable implementation of the",
        "original or retuned bank.",
        "",
        "The practical conclusion is that the three archives are usable as distinct",
        "baselines: original-paper behavior, retuned recovered-pipeline behavior,",
        "and final RCIM Model-Bank Reproduction faithful full-dataset behavior.",
        "",
        "## Source Validation Artifacts",
        "",
        "| Artifact | Path |",
        "| --- | --- |",
        f"| Source TE Curve Verification Pipeline summary | `{summary_dictionary['source_track2_summary_path']}` |",
        f"| Validation summary YAML | `{summary_dictionary['validation_summary_path']}` |",
        f"| Curve metric CSV | `{summary_dictionary['curve_metric_csv_path']}` |",
        f"| Target metric CSV | `{summary_dictionary['target_metric_csv_path']}` |",
        f"| Pairwise comparison CSV | `{summary_dictionary['pairwise_comparison_csv_path']}` |",
        "| Original archive | `models/paper_reference/rcim_original` |",
        "| Retuned archive | `models/paper_reference/rcim_retuned` |",
        "| RCIM Model-Bank Reproduction archive | `models/paper_reference/rcim_track1` |",
        "",
        "## Test Context",
        "",
        "| Item | Value |",
        "| --- | --- |",
        f"| Dataset config | `{summary_dictionary['dataset']['dataset_config_path']}` |",
        f"| Dataset root | `{summary_dictionary['dataset']['dataset_root']}` |",
        f"| Source contract | `{summary_dictionary['dataset']['source_contract']}` |",
        f"| Source comparison mode | `{summary_dictionary['comparison_scope']['comparison_mode']}` |",
        f"| Held-out curve count | `{summary_dictionary['comparison_scope']['curve_count']}` |",
        f"| Percentage-error denominator | `{summary_dictionary['comparison_scope']['percentage_error_denominator']}` |",
        "| Forward policy | `Fw` archives evaluated only on forward curves |",
        "| Backward policy | `Bw` archives evaluated only on backward curves |",
        "| Original backward coverage | not available in `rcim_original` |",
        "",
        "## Same-Family Archive Parity Verdict",
        "",
        "This is the direct implementation-to-implementation comparison. It compares",
        "the same family across archive groups on the same direction-valid TE Curve Verification Pipeline",
        "curve surface. A positive delta means the right-side archive has higher",
        "mean percentage error than the left-side archive.",
        "",
        "Classification thresholds are intentionally pragmatic:",
        "",
        "- `near-equivalent`: absolute delta MPE at or below `0.25` percentage points;",
        "- `similar`: absolute delta MPE above `0.25` and at or below `2.0` points;",
        "- `substantial difference`: absolute delta MPE above `2.0` points.",
        "",
        *build_pairwise_verdict_summary(pairwise_row_list),
        "",
        "### Forward Original Vs Retuned",
        "",
        *build_pairwise_table(select_pairwise_rows(pairwise_row_list, "forward_original_vs_retuned")),
        "",
        "### Forward Original Vs RCIM Model-Bank Reproduction",
        "",
        *build_pairwise_table(select_pairwise_rows(pairwise_row_list, "forward_original_vs_track1")),
        "",
        "### Forward Retuned Vs RCIM Model-Bank Reproduction",
        "",
        *build_pairwise_table(select_pairwise_rows(pairwise_row_list, "forward_retuned_vs_track1")),
        "",
        "### Backward Retuned Vs RCIM Model-Bank Reproduction",
        "",
        *build_pairwise_table(select_pairwise_rows(pairwise_row_list, "backward_retuned_vs_track1")),
        "",
        "## Forward Archive Comparison",
        "",
        "Forward compares all three archives on the same forward TE Curve Verification Pipeline curve",
        "surface. The best family rows are:",
        "",
        "| Archive | Best Family Candidate | Mean Percentage Error [%] | Curve MAE [deg] |",
        "| --- | --- | ---: | ---: |",
        f"| `rcim_original` | `{forward_original_best['candidate_id']}` | "
        f"{format_float(float(forward_original_best['mean_percentage_error_pct']))} | "
        f"{format_float(float(forward_original_best['curve_mae_deg']), 6)} |",
        f"| `rcim_retuned` | `{forward_retuned_best['candidate_id']}` | "
        f"{format_float(float(forward_retuned_best['mean_percentage_error_pct']))} | "
        f"{format_float(float(forward_retuned_best['curve_mae_deg']), 6)} |",
        f"| `rcim_track1` | `{forward_track1_best['candidate_id']}` | "
        f"{format_float(float(forward_track1_best['mean_percentage_error_pct']))} | "
        f"{format_float(float(forward_track1_best['curve_mae_deg']), 6)} |",
        "",
        "### Original Forward Models",
        "",
        *build_curve_table(select_rows(curve_row_list, "forward", "rcim_original")),
        "",
        "### Retuned Forward Models",
        "",
        *build_curve_table(select_rows(curve_row_list, "forward", "rcim_retuned")),
        "",
        "### RCIM Model-Bank Reproduction Forward Models",
        "",
        *build_curve_table(select_rows(curve_row_list, "forward", "rcim_track1")),
        "",
        "## Backward Archive Comparison",
        "",
        "Backward comparison is available for `rcim_retuned` and `rcim_track1`.",
        "`rcim_original` has no original backward archive and is therefore absent",
        "from this section.",
        "",
        "| Archive | Best Family Candidate | Mean Percentage Error [%] | Curve MAE [deg] |",
        "| --- | --- | ---: | ---: |",
        f"| `rcim_retuned` | `{backward_retuned_best['candidate_id']}` | "
        f"{format_float(float(backward_retuned_best['mean_percentage_error_pct']))} | "
        f"{format_float(float(backward_retuned_best['curve_mae_deg']), 6)} |",
        f"| `rcim_track1` | `{backward_track1_best['candidate_id']}` | "
        f"{format_float(float(backward_track1_best['mean_percentage_error_pct']))} | "
        f"{format_float(float(backward_track1_best['curve_mae_deg']), 6)} |",
        "",
        "### Retuned Backward Models",
        "",
        *build_curve_table(select_rows(curve_row_list, "backward", "rcim_retuned")),
        "",
        "### RCIM Model-Bank Reproduction Backward Models",
        "",
        *build_curve_table(select_rows(curve_row_list, "backward", "rcim_track1")),
        "",
        "## Target-Level Metric Snapshot",
        "",
        "These target-level rows come from the saved harmonic target model archives.",
        "They are not a replacement for TE Curve Verification Pipeline curve evaluation, but they explain",
        "how amplitude and phase prediction quality changes before TE reconstruction.",
        "",
        "### Forward Target Metrics",
        "",
        "#### Original Forward",
        "",
        *build_target_table([
            row for row in target_row_list
            if row["surface_label"] == "Fw" and row["source_label"] == "rcim_original"
        ]),
        "",
        "#### Retuned Forward",
        "",
        *build_target_table([
            row for row in target_row_list
            if row["surface_label"] == "Fw" and row["source_label"] == "rcim_retuned"
        ]),
        "",
        "#### RCIM Model-Bank Reproduction Forward",
        "",
        *build_target_table([
            row for row in target_row_list
            if row["surface_label"] == "Fw" and row["source_label"] == "rcim_track1"
        ]),
        "",
        "### Backward Target Metrics",
        "",
        "#### Retuned Backward",
        "",
        *build_target_table([
            row for row in target_row_list
            if row["surface_label"] == "Bw" and row["source_label"] == "rcim_retuned"
        ]),
        "",
        "#### RCIM Model-Bank Reproduction Backward",
        "",
        *build_target_table([
            row for row in target_row_list
            if row["surface_label"] == "Bw" and row["source_label"] == "rcim_track1"
        ]),
        "",
        "## Interpretation By Archive",
        "",
        "| Archive | Coverage | Interpretation |",
        "| --- | --- | --- |",
        "| `rcim_original` | forward only | Recovered original-pipeline reference. It remains the correct baseline for paper-original forward behavior and ONNX parity context. |",
        "| `rcim_retuned` | forward and backward | Best current paper-reference curve performer in this comparison; it reflects repository retuning rather than exact original-paper hyperparameter behavior. |",
        "| `rcim_track1` | forward and backward | Closed faithful full-dataset RCIM Model-Bank Reproduction archive. It is the most complete paper-reference family bank but is not the lowest-error TE Curve Verification Pipeline archive in this validation. |",
        "",
        "## Final Conclusion",
        "",
        "The repository `models/paper_reference` surface is coherent and usable as a",
        "three-baseline system rather than a single interchangeable model bank.",
        "`rcim_original` and `rcim_retuned` forward are broadly analogous but not",
        "identical. `rcim_track1` is substantially different from both on the TE Curve Verification Pipeline",
        "curve surface, especially in backward where every family differs",
        "substantially from the retuned counterpart under the selected thresholds.",
        "",
        "The defensible wording is:",
        "",
        "> `rcim_original` preserves the recovered forward original-pipeline baseline;",
        "> `rcim_retuned` provides the strongest current paper-reference TE Curve Verification Pipeline curve",
        "> metrics; and `rcim_track1` provides the final faithful full-dataset",
        "> RCIM Model-Bank Reproduction family archive for both directions.",
        "",
        "This report should be used together with the canonical curve-verification matrix when",
        "choosing which paper-reference archive to cite in downstream comparisons.",
    ]

    return "\n".join(report_line_list) + "\n"


def build_archive_parity_summary(track2_summary_path: Path, output_suffix: str) -> dict[str, Any]:

    """Build and persist the archive parity summary and report."""

    track2_summary = load_yaml_dictionary(track2_summary_path)
    run_timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    run_name = f"{run_timestamp}__paper_reference_archive_parity_{output_suffix}"
    output_directory = OUTPUT_ROOT / shared_training_infrastructure.sanitize_name(run_name)
    output_directory.mkdir(parents=True, exist_ok=True)

    curve_metric_row_list = build_curve_metric_row_list(track2_summary)
    target_metric_row_list = build_target_metric_row_list(track2_summary)
    pairwise_comparison_row_list = build_pairwise_comparison_row_list(
        curve_metric_row_list,
        target_metric_row_list,
    )
    curve_metric_csv_path = output_directory / "curve_metric_comparison.csv"
    target_metric_csv_path = output_directory / "target_metric_comparison.csv"
    pairwise_comparison_csv_path = output_directory / "pairwise_archive_comparison.csv"
    validation_summary_path = output_directory / shared_training_infrastructure.COMMON_VALIDATION_FILENAME

    write_csv(curve_metric_row_list, curve_metric_csv_path)
    write_csv(target_metric_row_list, target_metric_csv_path)
    write_csv(pairwise_comparison_row_list, pairwise_comparison_csv_path)

    summary_dictionary = {
        "source_track2_summary_path": shared_training_infrastructure.format_project_relative_path(
            track2_summary_path
        ),
        "validation_summary_path": shared_training_infrastructure.format_project_relative_path(
            validation_summary_path
        ),
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "curve_metric_csv_path": shared_training_infrastructure.format_project_relative_path(curve_metric_csv_path),
        "target_metric_csv_path": shared_training_infrastructure.format_project_relative_path(target_metric_csv_path),
        "pairwise_comparison_csv_path": shared_training_infrastructure.format_project_relative_path(
            pairwise_comparison_csv_path
        ),
        "dataset": track2_summary["dataset"],
        "comparison_scope": track2_summary["comparison_scope"],
        "archive_scope": {
            "source_label_list": SOURCE_LABEL_LIST,
            "family_label_list": FAMILY_LABEL_LIST,
            "forward_source_label_list": ["rcim_original", "rcim_retuned", "rcim_track1"],
            "backward_source_label_list": ["rcim_retuned", "rcim_track1"],
            "original_backward_available": False,
        },
        "curve_metric_row_list": curve_metric_row_list,
        "target_metric_row_list": target_metric_row_list,
        "pairwise_comparison_row_list": pairwise_comparison_row_list,
    }
    shared_training_infrastructure.save_yaml_snapshot(summary_dictionary, validation_summary_path)

    CANONICAL_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    CANONICAL_REPORT_PATH.write_text(
        build_canonical_report_markdown(summary_dictionary),
        encoding="utf-8",
    )
    return summary_dictionary


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the parity report builder."""

    argument_parser = argparse.ArgumentParser(
        description="Build a parity report across saved RCIM paper-reference archives."
    )
    argument_parser.add_argument(
        "--track2-summary-path",
        type=Path,
        default=None,
        help="TE Curve Verification Pipeline validation_summary.yaml to use. Defaults to the newest compatible summary.",
    )
    argument_parser.add_argument(
        "--output-suffix",
        type=str,
        default="validation",
        help="Suffix appended to the immutable validation-check artifact.",
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser.parse_args()


def main() -> None:

    """Run the command-line parity report builder."""

    command_line_arguments = parse_command_line_arguments()
    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(command_line_arguments)
    )
    track2_summary_path = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(
            command_line_arguments.track2_summary_path
        )
        if command_line_arguments.track2_summary_path is not None
        else find_latest_track2_validation_summary()
    )
    summary_dictionary = build_archive_parity_summary(
        track2_summary_path=track2_summary_path,
        output_suffix=command_line_arguments.output_suffix,
    )
    print(
        "[DONE] Paper-reference archive parity summary written | "
        f"{summary_dictionary['validation_summary_path']}"
    )
    print(
        "[DONE] Paper-reference archive parity report written | "
        f"{shared_training_infrastructure.format_project_relative_path(CANONICAL_REPORT_PATH)}"
    )


if __name__ == "__main__":

    main()
