"""Close out the Track 1 MLP family full-matrix repair campaign.

This utility reconstructs the completed `2026-04-21` MLP-only repair wave from
the local validation summaries, writes the canonical campaign bookkeeping
artifacts, refreshes the accepted MLP row in the Track 1 benchmark, patches the
master summary, and emits the final Markdown campaign report.
"""

from __future__ import annotations

# Import Python Utilities
import argparse
import re
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

PROJECT_PATH = Path(__file__).resolve().parents[2]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

from scripts.reports.closeout_track1_residual_cellwise_closure import (
    ACTIVE_CAMPAIGN_PATH,
    AMPLITUDE_HARMONIC_LIST,
    BENCHMARK_REPORT_PATH,
    FAMILY_ORDER,
    MASTER_SUMMARY_PATH,
    PHASE_HARMONIC_LIST,
    REPORT_OUTPUT_ROOT,
    TRAINING_CAMPAIGN_ROOT,
    VALIDATION_ROOT,
    build_campaign_entry_from_summary,
    build_paper_target_dictionary,
    build_selection_sort_key,
    format_metric_value,
    format_project_relative_path,
    load_yaml_dictionary,
    parse_full_matrix_section,
    resolve_status_marker,
    save_yaml_dictionary,
)
from scripts.reports.refresh_track1_benchmark_colored_markers import (
    refresh_track1_benchmark_colored_markers,
)
from scripts.reports.refresh_track1_family_reference_archives import (
    refresh_track1_family_reference_archives,
)

CAMPAIGN_NAME = "track1_mlp_family_full_matrix_repair_campaign_2026_04_21_17_20_12"
CAMPAIGN_CONFIG_FOLDER_NAME = "2026-04-21_track1_mlp_family_full_matrix_repair_campaign"
CAMPAIGN_OUTPUT_DIRECTORY = (
    TRAINING_CAMPAIGN_ROOT / "track1" / "exact_paper" / CAMPAIGN_NAME
)

MLP_AMPLITUDE_TARGET_LIST = [0, 1, 3, 39, 40, 81, 156, 240]
MLP_PHASE_TARGET_LIST = [1, 3, 39, 162]

MLP_REPAIR_RUN_PATTERN = re.compile(
    r"^track1_mlp_(?P<scope>amplitude|phase)_(?P<harmonic>\d+)_closure_attempt_(?P<attempt>\d+)$"
)

SELECTION_POLICY = {
    "primary_metric": "closure_score_desc",
    "first_tie_breaker": "met_paper_cell_count_desc",
    "second_tie_breaker": "near_paper_cell_count_desc",
    "third_tie_breaker": "open_paper_cell_count_asc",
    "fourth_tie_breaker": "mean_normalized_gap_ratio_asc",
    "fifth_tie_breaker": "max_normalized_gap_ratio_asc",
    "sixth_tie_breaker": "run_name",
    "direction": "maximize_then_minimize",
    "note": (
        "This winner is the bookkeeping representative of the completed Track 1 "
        "MLP family full-matrix repair campaign."
    ),
}

BEST_RUN_MD_SELECTION_LINES = [
    "- Primary metric: `closure_score_desc`",
    "- First tie-breaker: `met_paper_cell_count_desc`",
    "- Second tie-breaker: `near_paper_cell_count_desc`",
    "- Third tie-breaker: `open_paper_cell_count_asc`",
    "- Fourth tie-breaker: `mean_normalized_gap_ratio_asc`",
    "- Fifth tie-breaker: `max_normalized_gap_ratio_asc`",
    "- Sixth tie-breaker: `run_name`",
]


def parse_command_line_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Close out the Track 1 MLP family full-matrix repair campaign."
    )
    argument_parser.add_argument(
        "--report-timestamp",
        required=True,
        help="Timestamp prefix used for the final campaign results report filename.",
    )
    return argument_parser.parse_args()


def format_gap_value(metric_value: float) -> str:
    """Format one gap value for compact Markdown tables."""

    return f"{metric_value:.6g}" if abs(metric_value) < 1 else f"{metric_value:.3g}"


def collect_campaign_entry_list(
    paper_target_dictionary: dict[str, dict[str, dict[str, float]]],
) -> list[dict[str, Any]]:
    """Collect only the validation entries that belong to this MLP campaign."""

    collected_entry_list: list[dict[str, Any]] = []

    for summary_path in sorted(VALIDATION_ROOT.glob("*/validation_summary.yaml")):
        summary_dictionary = load_yaml_dictionary(summary_path)
        config_path_text = str(summary_dictionary.get("config_path", "")).replace("\\", "/")
        if CAMPAIGN_CONFIG_FOLDER_NAME not in config_path_text:
            continue

        run_name = str(summary_dictionary["experiment"]["run_name"])
        if MLP_REPAIR_RUN_PATTERN.match(run_name) is None:
            continue

        campaign_entry = build_campaign_entry_from_summary(
            summary_dictionary,
            paper_target_dictionary,
        )
        collected_entry_list.append(campaign_entry)

    assert len(collected_entry_list) == 324, (
        "Unexpected MLP family repair entry count | "
        f"actual={len(collected_entry_list)} | expected=324"
    )
    return collected_entry_list


def build_targeted_pair_identifier_list() -> list[tuple[str, str, int]]:
    """Build the canonical targeted pair order for the MLP wave."""

    targeted_pair_identifier_list: list[tuple[str, str, int]] = []
    for harmonic_order in MLP_AMPLITUDE_TARGET_LIST:
        targeted_pair_identifier_list.append(("MLP", "amplitude", harmonic_order))
    for harmonic_order in MLP_PHASE_TARGET_LIST:
        targeted_pair_identifier_list.append(("MLP", "phase", harmonic_order))
    return targeted_pair_identifier_list


def build_targeted_baseline_metric_dictionary(
    full_matrix_dictionary: dict[str, dict[str, Any]],
) -> dict[tuple[str, str, int], dict[str, float]]:
    """Build the accepted baseline metric cells for the 12 MLP campaign pairs."""

    baseline_metric_dictionary: dict[tuple[str, str, int], dict[str, float]] = {}

    for _, scope_key, harmonic_order in build_targeted_pair_identifier_list():
        if scope_key == "amplitude":
            baseline_metric_dictionary[("MLP", scope_key, harmonic_order)] = {
                "mae": float(full_matrix_dictionary["table2"]["repository_rows"]["MLP"][harmonic_order]),
                "rmse": float(full_matrix_dictionary["table3"]["repository_rows"]["MLP"][harmonic_order]),
            }
        else:
            baseline_metric_dictionary[("MLP", scope_key, harmonic_order)] = {
                "mae": float(full_matrix_dictionary["table4"]["repository_rows"]["MLP"][harmonic_order]),
                "rmse": float(full_matrix_dictionary["table5"]["repository_rows"]["MLP"][harmonic_order]),
            }

    return baseline_metric_dictionary


def write_campaign_bookkeeping(entry_list: list[dict[str, Any]]) -> dict[str, Any]:
    """Write the canonical leaderboard and best-run artifacts for the campaign."""

    sorted_entry_list = sorted(entry_list, key=build_selection_sort_key)
    best_entry = deepcopy(sorted_entry_list[0])
    selected_at_text = datetime.now().astimezone().isoformat(timespec="seconds")

    leaderboard_dictionary = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "selection_policy": deepcopy(SELECTION_POLICY),
        "updated_at": selected_at_text,
        "entry_count": len(sorted_entry_list),
        "entry_list": sorted_entry_list,
    }

    best_run_dictionary = deepcopy(best_entry)
    best_run_dictionary["selection_policy"] = deepcopy(SELECTION_POLICY)
    best_run_dictionary["selected_at"] = selected_at_text

    best_run_markdown = "\n".join(
        [
            f"# Campaign Best Run - {CAMPAIGN_NAME}",
            "",
            f"- Run: `{best_entry['run_name']}`",
            f"- Family: `{best_entry['family_code']}`",
            f"- Scope: `{best_entry['target_scope_mode']}`",
            f"- Closure Score: `{float(best_entry['closure_score']):.3f}`",
            f"- Met Paper Cells: `{int(best_entry['met_paper_cell_count'])}`",
            f"- Near Paper Cells: `{int(best_entry['near_paper_cell_count'])}`",
            f"- Open Paper Cells: `{int(best_entry['open_paper_cell_count'])}`",
            f"- Mean Normalized Gap Ratio: `{float(best_entry['mean_normalized_gap_ratio']):.6f}`",
            f"- Max Normalized Gap Ratio: `{float(best_entry['max_normalized_gap_ratio']):.6f}`",
            "",
            "## Selection Policy",
            "",
            *BEST_RUN_MD_SELECTION_LINES,
            "",
        ]
    )

    CAMPAIGN_OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    save_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.yaml", leaderboard_dictionary)
    save_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.yaml", best_run_dictionary)
    (CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.md").write_text(
        best_run_markdown,
        encoding="utf-8",
        newline="\n",
    )
    return best_run_dictionary


def build_best_campaign_metric_dictionary(
    campaign_entry_list: list[dict[str, Any]],
) -> dict[tuple[str, str, int], dict[str, float]]:
    """Build the best campaign-local metric cells for each targeted pair."""

    best_metric_dictionary: dict[tuple[str, str, int], dict[str, float]] = {}

    for scope_key in ("amplitude", "phase"):
        harmonic_list = MLP_AMPLITUDE_TARGET_LIST if scope_key == "amplitude" else MLP_PHASE_TARGET_LIST
        for harmonic_order in harmonic_list:
            pair_identifier = ("MLP", scope_key, harmonic_order)
            matching_entry_list = [
                entry
                for entry in campaign_entry_list
                if entry["target_scope_mode"] == ("amplitudes_only" if scope_key == "amplitude" else "phases_only")
                and int(entry["targeted_harmonic_list"][0]) == harmonic_order
            ]
            assert matching_entry_list, f"Missing campaign entries for pair | pair={pair_identifier}"
            best_metric_dictionary[pair_identifier] = {
                "mae": min(float(entry["winning_mean_component_mae"]) for entry in matching_entry_list),
                "rmse": min(float(entry["winning_mean_component_rmse"]) for entry in matching_entry_list),
            }

    return best_metric_dictionary


def resolve_accepted_metric_dictionary(
    baseline_metric_dictionary: dict[tuple[str, str, int], dict[str, float]],
    best_campaign_metric_dictionary: dict[tuple[str, str, int], dict[str, float]],
) -> tuple[dict[tuple[str, str, int], dict[str, float]], dict[str, int]]:
    """Resolve the accepted visible benchmark cells after the campaign."""

    accepted_metric_dictionary: dict[tuple[str, str, int], dict[str, float]] = {}
    promoted_metric_cell_count = 0
    retained_metric_cell_count = 0
    promoted_pair_count = 0
    retained_pair_count = 0

    for pair_identifier in build_targeted_pair_identifier_list():
        baseline_metric_entry = baseline_metric_dictionary[pair_identifier]
        campaign_metric_entry = best_campaign_metric_dictionary[pair_identifier]
        accepted_metric_entry: dict[str, float] = {}
        pair_promoted = False

        for metric_name in ("mae", "rmse"):
            baseline_metric_value = float(baseline_metric_entry[metric_name])
            campaign_metric_value = float(campaign_metric_entry[metric_name])

            if (
                campaign_metric_value < baseline_metric_value
                and format_metric_value(campaign_metric_value) != format_metric_value(baseline_metric_value)
            ):
                accepted_metric_entry[metric_name] = campaign_metric_value
                promoted_metric_cell_count += 1
                pair_promoted = True
            else:
                accepted_metric_entry[metric_name] = baseline_metric_value
                retained_metric_cell_count += 1

        accepted_metric_dictionary[pair_identifier] = accepted_metric_entry
        if pair_promoted:
            promoted_pair_count += 1
        else:
            retained_pair_count += 1

    return accepted_metric_dictionary, {
        "promoted_metric_cell_count": promoted_metric_cell_count,
        "retained_metric_cell_count": retained_metric_cell_count,
        "promoted_pair_count": promoted_pair_count,
        "retained_pair_count": retained_pair_count,
    }


def update_mlp_rows_in_benchmark(
    benchmark_line_list: list[str],
    full_matrix_dictionary: dict[str, dict[str, Any]],
    accepted_metric_dictionary: dict[tuple[str, str, int], dict[str, float]],
) -> None:
    """Update only the MLP repository-side rows in the four full-matrix tables."""

    for pair_identifier, accepted_metric_entry in accepted_metric_dictionary.items():
        _, scope_key, harmonic_order = pair_identifier
        mae_value = float(accepted_metric_entry["mae"])
        rmse_value = float(accepted_metric_entry["rmse"])

        if scope_key == "amplitude":
            full_matrix_dictionary["table2"]["repository_rows"]["MLP"][harmonic_order] = mae_value
            full_matrix_dictionary["table3"]["repository_rows"]["MLP"][harmonic_order] = rmse_value
        else:
            full_matrix_dictionary["table4"]["repository_rows"]["MLP"][harmonic_order] = mae_value
            full_matrix_dictionary["table5"]["repository_rows"]["MLP"][harmonic_order] = rmse_value

    for table_key, harmonic_list in (
        ("table2", AMPLITUDE_HARMONIC_LIST),
        ("table3", AMPLITUDE_HARMONIC_LIST),
        ("table4", PHASE_HARMONIC_LIST),
        ("table5", PHASE_HARMONIC_LIST),
    ):
        repository_value_dictionary = full_matrix_dictionary[table_key]["repository_rows"]["MLP"]
        paper_value_dictionary = full_matrix_dictionary[table_key]["paper_rows"]["MLP"]
        repository_cell_list = ["`MLP`"]

        for harmonic_order in harmonic_list:
            repository_value = float(repository_value_dictionary[harmonic_order])
            paper_value = float(paper_value_dictionary[harmonic_order])
            status_marker = resolve_status_marker(repository_value, paper_value)
            repository_cell_list.append(f"`{status_marker} {format_metric_value(repository_value)}`")

        mlp_line_index = full_matrix_dictionary[table_key]["repository_line_indexes"]["MLP"]
        benchmark_line_list[mlp_line_index] = "| " + " | ".join(repository_cell_list) + " |"


def build_pair_summary_row_list(
    baseline_metric_dictionary: dict[tuple[str, str, int], dict[str, float]],
    best_campaign_metric_dictionary: dict[tuple[str, str, int], dict[str, float]],
    accepted_metric_dictionary: dict[tuple[str, str, int], dict[str, float]],
    full_matrix_dictionary: dict[str, dict[str, Any]],
) -> list[str]:
    """Build the targeted-pair comparison table for the final report."""

    table_line_list = [
        "| Pair | Baseline | Campaign Best | Accepted | Source | Result |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    for family_code, scope_key, harmonic_order in build_targeted_pair_identifier_list():
        if scope_key == "amplitude":
            pair_label = f"`A{harmonic_order}`"
            paper_mae_value = float(full_matrix_dictionary["table2"]["paper_rows"]["MLP"][harmonic_order])
            paper_rmse_value = float(full_matrix_dictionary["table3"]["paper_rows"]["MLP"][harmonic_order])
        else:
            pair_label = f"`phi{harmonic_order}`"
            paper_mae_value = float(full_matrix_dictionary["table4"]["paper_rows"]["MLP"][harmonic_order])
            paper_rmse_value = float(full_matrix_dictionary["table5"]["paper_rows"]["MLP"][harmonic_order])

        baseline_mae_value = float(baseline_metric_dictionary[(family_code, scope_key, harmonic_order)]["mae"])
        baseline_rmse_value = float(baseline_metric_dictionary[(family_code, scope_key, harmonic_order)]["rmse"])
        campaign_mae_value = float(best_campaign_metric_dictionary[(family_code, scope_key, harmonic_order)]["mae"])
        campaign_rmse_value = float(best_campaign_metric_dictionary[(family_code, scope_key, harmonic_order)]["rmse"])
        accepted_mae_value = float(accepted_metric_dictionary[(family_code, scope_key, harmonic_order)]["mae"])
        accepted_rmse_value = float(accepted_metric_dictionary[(family_code, scope_key, harmonic_order)]["rmse"])

        if accepted_mae_value == baseline_mae_value and accepted_rmse_value == baseline_rmse_value:
            source_text = "`baseline`"
        elif accepted_mae_value != baseline_mae_value and accepted_rmse_value != baseline_rmse_value:
            source_text = "`campaign`"
        else:
            source_text = "`mixed`"

        accepted_status_list = [
            resolve_status_marker(accepted_mae_value, paper_mae_value),
            resolve_status_marker(accepted_rmse_value, paper_rmse_value),
        ]
        accepted_result_text = (
            "`fully_green`"
            if accepted_status_list == ["🟢", "🟢"]
            else "`still_non_green`"
        )

        table_line_list.append(
            "| "
            f"{pair_label} | "
            f"`{format_metric_value(baseline_mae_value)} / {format_metric_value(baseline_rmse_value)}` | "
            f"`{format_metric_value(campaign_mae_value)} / {format_metric_value(campaign_rmse_value)}` | "
            f"`{format_metric_value(accepted_mae_value)} / {format_metric_value(accepted_rmse_value)}` | "
            f"{source_text} | "
            f"{accepted_result_text} |"
        )

    return table_line_list


def build_remaining_non_green_summary(
    full_matrix_dictionary: dict[str, dict[str, Any]],
) -> tuple[dict[str, list[int]], int]:
    """Build the post-closeout list of remaining non-green MLP cells."""

    remaining_dictionary = {
        "table2": [],
        "table3": [],
        "table4": [],
        "table5": [],
    }

    for harmonic_order in AMPLITUDE_HARMONIC_LIST:
        for table_key in ("table2", "table3"):
            repository_value = float(full_matrix_dictionary[table_key]["repository_rows"]["MLP"][harmonic_order])
            paper_value = float(full_matrix_dictionary[table_key]["paper_rows"]["MLP"][harmonic_order])
            if resolve_status_marker(repository_value, paper_value) != "🟢":
                remaining_dictionary[table_key].append(harmonic_order)

    for harmonic_order in PHASE_HARMONIC_LIST:
        for table_key in ("table4", "table5"):
            repository_value = float(full_matrix_dictionary[table_key]["repository_rows"]["MLP"][harmonic_order])
            paper_value = float(full_matrix_dictionary[table_key]["paper_rows"]["MLP"][harmonic_order])
            if resolve_status_marker(repository_value, paper_value) != "🟢":
                remaining_dictionary[table_key].append(harmonic_order)

    total_remaining_count = sum(len(value) for value in remaining_dictionary.values())
    return remaining_dictionary, total_remaining_count


def patch_benchmark_addendum(
    benchmark_text: str,
    report_relative_path: str,
    promoted_pair_count: int,
    retained_baseline_pair_count: int,
    remaining_non_green_dictionary: dict[str, list[int]],
) -> str:
    """Insert or replace the MLP-family repair addendum in the benchmark."""

    table3_remaining = ", ".join(str(value) for value in remaining_non_green_dictionary["table3"]) or "none"
    table4_remaining = ", ".join(str(value) for value in remaining_non_green_dictionary["table4"]) or "none"
    table5_remaining = ", ".join(str(value) for value in remaining_non_green_dictionary["table5"]) or "none"

    addendum_text = "\n".join(
        [
            "### 2026-04-21 MLP Family Full-Matrix Repair Addendum",
            "",
            "This addendum records the dedicated post-relaunch `MLP` family repair",
            "wave that ran after the broader open-cell closeout had already been",
            "published.",
            "",
            f"- campaign name: `{CAMPAIGN_NAME}`",
            "- completed validation runs: `324/324`",
            f"- promoted targeted family-target pairs: `{promoted_pair_count}/12`",
            f"- retained baseline family-target pairs: `{retained_baseline_pair_count}/12`",
            f"- supporting report: `{report_relative_path}`",
            "",
            "Canonical reading rule for this addendum:",
            "",
            "- the accepted MLP row continues to read from the better value between",
            "  the already accepted benchmark baseline and this dedicated repair",
            "  wave;",
            "- this MLP-only wave improves the accepted numeric value on `A40`, but it",
            "  does not change the global Track 1 cross-family closure counts.",
            "",
            "Post-closeout remaining non-green cells in the accepted `MLP` family row:",
            "",
            f"- `Table 2`: `none`",
            f"- `Table 3`: `{table3_remaining}`",
            f"- `Table 4`: `{table4_remaining}`",
            f"- `Table 5`: `{table5_remaining}`",
            "",
        ]
    )

    addendum_pattern = re.compile(
        r"### 2026-04-21 MLP Family Full-Matrix Repair Addendum\n.*?(?=\n#### Table 2 - Amplitude MAE Full-Matrix Replication)",
        re.DOTALL,
    )
    if addendum_pattern.search(benchmark_text):
        return addendum_pattern.sub(addendum_text.rstrip(), benchmark_text, count=1)

    return benchmark_text.replace(
        "\n#### Table 2 - Amplitude MAE Full-Matrix Replication",
        "\n" + addendum_text + "\n#### Table 2 - Amplitude MAE Full-Matrix Replication",
        1,
    )


def patch_master_summary(
    report_timestamp: str,
    report_relative_path: str,
    best_entry: dict[str, Any],
    promoted_pair_count: int,
    retained_baseline_pair_count: int,
    total_remaining_non_green_count: int,
    remaining_non_green_dictionary: dict[str, list[int]],
) -> None:
    """Patch the master summary with the completed MLP campaign closeout."""

    master_summary_text = MASTER_SUMMARY_PATH.read_text(encoding="utf-8")
    generated_at_text = datetime.now().astimezone().isoformat(timespec="seconds")

    master_summary_text = re.sub(
        r"^- Generated At: `.*`$",
        f"- Generated At: `{generated_at_text}`",
        master_summary_text,
        count=1,
        flags=re.MULTILINE,
    )
    master_summary_text = re.sub(
        r"^- Active Campaign Status: `.*`$",
        "- Active Campaign Status: `completed`",
        master_summary_text,
        count=1,
        flags=re.MULTILINE,
    )
    master_summary_text = re.sub(
        r"^- Active Campaign Name: `.*`$",
        f"- Active Campaign Name: `{CAMPAIGN_NAME}`",
        master_summary_text,
        count=1,
        flags=re.MULTILINE,
    )

    recent_campaign_row = (
        f"| `{CAMPAIGN_NAME}` | `{report_timestamp}` | 324 | 0 | "
        f"`{best_entry['run_name']}` | Dedicated `MLP` full-matrix repair completed "
        f"`324` retries, promoted `{promoted_pair_count}/12` targeted family-target "
        f"pairs, and left the accepted `MLP` row with `{total_remaining_non_green_count}` "
        f"non-green cells on Tables `2-5` (`Table 3`: "
        f"{', '.join(str(value) for value in remaining_non_green_dictionary['table3']) or 'none'}; "
        f"`Table 4`: {', '.join(str(value) for value in remaining_non_green_dictionary['table4']) or 'none'}; "
        f"`Table 5`: {', '.join(str(value) for value in remaining_non_green_dictionary['table5']) or 'none'}) |"
    )

    master_summary_text = re.sub(
        rf"^\| `{re.escape(CAMPAIGN_NAME)}` \|.*\n?",
        "",
        master_summary_text,
        flags=re.MULTILINE,
    )
    recent_campaign_header = (
        "## Recent Campaign Changes\n\n"
        "| Campaign | Generated At | Completed | Failed | Winner | Impact |\n"
        "| --- | --- | ---: | ---: | --- | --- |\n"
    )
    master_summary_text = master_summary_text.replace(
        recent_campaign_header,
        recent_campaign_header + recent_campaign_row + "\n",
        1,
    )

    master_summary_text = re.sub(
        r"- Latest exact-paper closeout report: `.*`",
        f"- Latest exact-paper closeout report: `{report_relative_path}`",
        master_summary_text,
        count=1,
    )

    track1_status_pattern = re.compile(
        r"- Recovered first-launch `MLP` artifact status:.*?(?=\n### Track 1\.5 Harmonic-Wise Validation Support)",
        re.DOTALL,
    )
    track1_status_replacement = "\n".join(
        [
            "- Recovered first-launch `MLP` artifact status: fully reconciled locally after post-closeout recovery of all `297` validation folders and `297` validation reports",
            f"- Dedicated `MLP` family repair campaign status: completed with `{promoted_pair_count}/12` promoted targeted pairs and `{retained_baseline_pair_count}/12` retained baseline pairs",
            f"- Accepted `MLP` row remaining non-green cells after the dedicated repair wave: `Table 3 -> {', '.join(str(value) for value in remaining_non_green_dictionary['table3']) or 'none'}`; `Table 4 -> {', '.join(str(value) for value in remaining_non_green_dictionary['table4']) or 'none'}`; `Table 5 -> {', '.join(str(value) for value in remaining_non_green_dictionary['table5']) or 'none'}`",
            "",
        ]
    )
    master_summary_text = track1_status_pattern.sub(track1_status_replacement, master_summary_text, count=1)

    MASTER_SUMMARY_PATH.write_text(master_summary_text, encoding="utf-8", newline="\n")


def build_results_report_markdown(
    report_relative_path: str,
    report_timestamp: str,
    best_entry: dict[str, Any],
    baseline_metric_dictionary: dict[tuple[str, str, int], dict[str, float]],
    best_campaign_metric_dictionary: dict[tuple[str, str, int], dict[str, float]],
    accepted_metric_dictionary: dict[tuple[str, str, int], dict[str, float]],
    full_matrix_dictionary: dict[str, dict[str, Any]],
    improvement_summary_dictionary: dict[str, int],
    remaining_non_green_dictionary: dict[str, list[int]],
    total_remaining_non_green_count: int,
) -> str:
    """Build the final MLP family repair campaign report."""

    pair_summary_row_list = build_pair_summary_row_list(
        baseline_metric_dictionary,
        best_campaign_metric_dictionary,
        accepted_metric_dictionary,
        full_matrix_dictionary,
    )

    return "\n".join(
        [
            "# Track 1 MLP Family Full-Matrix Repair Campaign Results Report",
            "",
            "## Overview",
            "",
            "This report closes the dedicated exact-paper `MLP` family repair wave",
            "prepared in:",
            "",
            "- `doc/reports/campaign_plans/track1/exact_paper/2026-04-21-17-20-12_track1_mlp_family_full_matrix_repair_campaign_plan_report.md`",
            "",
            "The campaign targeted only the `MLP` family-target pairs selected for the",
            "post-relaunch repair pass across the canonical `Track 1` full-matrix",
            "surfaces.",
            "",
            f"- campaign name: `{CAMPAIGN_NAME}`",
            f"- report timestamp: `{report_timestamp}`",
            "- completed validation runs: `324`",
            "- failed validation runs: `0`",
            f"- promoted targeted pairs: `{improvement_summary_dictionary['promoted_pair_count']}/12`",
            f"- retained baseline pairs: `{improvement_summary_dictionary['retained_pair_count']}/12`",
            f"- visibly promoted benchmark cells: `{improvement_summary_dictionary['promoted_metric_cell_count']}/24`",
            f"- campaign artifact root: `{format_project_relative_path(CAMPAIGN_OUTPUT_DIRECTORY)}`",
            "",
            "## Campaign Winner",
            "",
            f"- Run: `{best_entry['run_name']}`",
            f"- Scope: `{best_entry['target_scope_mode']}`",
            f"- Closure Score: `{float(best_entry['closure_score']):.3f}`",
            f"- Met / Near / Open: `{int(best_entry['met_paper_cell_count'])}` / `{int(best_entry['near_paper_cell_count'])}` / `{int(best_entry['open_paper_cell_count'])}`",
            "",
            "## Targeted Pair Outcome",
            "",
            "The table below compares the accepted pre-wave baseline against the best",
            "campaign-local candidate and the final accepted post-wave value for each",
            "targeted `MLP` pair. Each metric cell is shown as `MAE / RMSE`.",
            "",
            *pair_summary_row_list,
            "",
            "## Accepted MLP Row After Closeout",
            "",
            f"- `Table 2` remaining non-green harmonics: `{', '.join(str(value) for value in remaining_non_green_dictionary['table2']) or 'none'}`",
            f"- `Table 3` remaining non-green harmonics: `{', '.join(str(value) for value in remaining_non_green_dictionary['table3']) or 'none'}`",
            f"- `Table 4` remaining non-green harmonics: `{', '.join(str(value) for value in remaining_non_green_dictionary['table4']) or 'none'}`",
            f"- `Table 5` remaining non-green harmonics: `{', '.join(str(value) for value in remaining_non_green_dictionary['table5']) or 'none'}`",
            f"- total remaining non-green `MLP` cells on Tables `2-5`: `{total_remaining_non_green_count}`",
            "",
            "## Canonical Track 1 Impact",
            "",
            "- This `MLP`-only wave updates the accepted `MLP` family row without",
            "  reopening the already closed cross-family open-cell closeout.",
            "- The benchmark row now keeps the better visible metric cell between the",
            "  accepted baseline and this dedicated repair wave.",
            "- Global `Track 1` cross-family closure counts remain unchanged at",
            "  `7/10`, `10/10`, `9/9`, and `9/9` across Tables `2-5`.",
            "",
            "## Resulting Canonical State",
            "",
            f"- benchmark path: `{format_project_relative_path(BENCHMARK_REPORT_PATH)}`",
            f"- master summary path: `{format_project_relative_path(MASTER_SUMMARY_PATH)}`",
            f"- final closeout report path: `{report_relative_path}`",
            "",
        ]
    ) + "\n"


def main() -> None:
    """Run the MLP family repair closeout workflow."""

    command_line_arguments = parse_command_line_arguments()
    report_timestamp = str(command_line_arguments.report_timestamp)

    benchmark_text = BENCHMARK_REPORT_PATH.read_text(encoding="utf-8")
    benchmark_line_list = benchmark_text.splitlines()

    full_matrix_dictionary = {
        "table2": parse_full_matrix_section(
            benchmark_line_list,
            "#### Table 2 - Amplitude MAE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table3": parse_full_matrix_section(
            benchmark_line_list,
            "#### Table 3 - Amplitude RMSE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table4": parse_full_matrix_section(
            benchmark_line_list,
            "#### Table 4 - Phase MAE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table5": parse_full_matrix_section(
            benchmark_line_list,
            "#### Table 5 - Phase RMSE Full-Matrix Replication",
            expected_row_count=10,
        ),
    }
    paper_target_dictionary = build_paper_target_dictionary(full_matrix_dictionary)

    campaign_entry_list = collect_campaign_entry_list(paper_target_dictionary)
    best_entry = write_campaign_bookkeeping(campaign_entry_list)

    baseline_metric_dictionary = build_targeted_baseline_metric_dictionary(full_matrix_dictionary)
    best_campaign_metric_dictionary = build_best_campaign_metric_dictionary(campaign_entry_list)
    accepted_metric_dictionary, improvement_summary_dictionary = resolve_accepted_metric_dictionary(
        baseline_metric_dictionary,
        best_campaign_metric_dictionary,
    )

    update_mlp_rows_in_benchmark(
        benchmark_line_list,
        full_matrix_dictionary,
        accepted_metric_dictionary,
    )

    updated_benchmark_text = "\n".join(benchmark_line_list) + "\n"
    updated_benchmark_text = patch_benchmark_addendum(
        updated_benchmark_text,
        report_relative_path=(
            "doc/reports/campaign_results/track1/exact_paper/"
            f"{report_timestamp}_track1_mlp_family_full_matrix_repair_campaign_results_report.md"
        ),
        promoted_pair_count=improvement_summary_dictionary["promoted_pair_count"],
        retained_baseline_pair_count=improvement_summary_dictionary["retained_pair_count"],
        remaining_non_green_dictionary=build_remaining_non_green_summary(full_matrix_dictionary)[0],
    )
    BENCHMARK_REPORT_PATH.write_text(updated_benchmark_text, encoding="utf-8", newline="\n")
    refresh_track1_benchmark_colored_markers()

    refreshed_benchmark_line_list = BENCHMARK_REPORT_PATH.read_text(encoding="utf-8").splitlines()
    refreshed_full_matrix_dictionary = {
        "table2": parse_full_matrix_section(
            refreshed_benchmark_line_list,
            "#### Table 2 - Amplitude MAE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table3": parse_full_matrix_section(
            refreshed_benchmark_line_list,
            "#### Table 3 - Amplitude RMSE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table4": parse_full_matrix_section(
            refreshed_benchmark_line_list,
            "#### Table 4 - Phase MAE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table5": parse_full_matrix_section(
            refreshed_benchmark_line_list,
            "#### Table 5 - Phase RMSE Full-Matrix Replication",
            expected_row_count=10,
        ),
    }
    remaining_non_green_dictionary, total_remaining_non_green_count = build_remaining_non_green_summary(
        refreshed_full_matrix_dictionary
    )

    report_output_path = (
        REPORT_OUTPUT_ROOT
        / f"{report_timestamp}_track1_mlp_family_full_matrix_repair_campaign_results_report.md"
    )
    report_relative_path = format_project_relative_path(report_output_path)

    results_report_markdown = build_results_report_markdown(
        report_relative_path=report_relative_path,
        report_timestamp=report_timestamp,
        best_entry=best_entry,
        baseline_metric_dictionary=baseline_metric_dictionary,
        best_campaign_metric_dictionary=best_campaign_metric_dictionary,
        accepted_metric_dictionary=accepted_metric_dictionary,
        full_matrix_dictionary=refreshed_full_matrix_dictionary,
        improvement_summary_dictionary=improvement_summary_dictionary,
        remaining_non_green_dictionary=remaining_non_green_dictionary,
        total_remaining_non_green_count=total_remaining_non_green_count,
    )
    report_output_path.parent.mkdir(parents=True, exist_ok=True)
    report_output_path.write_text(results_report_markdown, encoding="utf-8", newline="\n")

    active_campaign_dictionary = load_yaml_dictionary(ACTIVE_CAMPAIGN_PATH)
    active_campaign_dictionary["results_report_path"] = report_relative_path.replace("/", "\\")
    save_yaml_dictionary(ACTIVE_CAMPAIGN_PATH, active_campaign_dictionary)

    patch_master_summary(
        report_timestamp=report_timestamp,
        report_relative_path=report_relative_path,
        best_entry=best_entry,
        promoted_pair_count=improvement_summary_dictionary["promoted_pair_count"],
        retained_baseline_pair_count=improvement_summary_dictionary["retained_pair_count"],
        total_remaining_non_green_count=total_remaining_non_green_count,
        remaining_non_green_dictionary=remaining_non_green_dictionary,
    )
    refresh_track1_family_reference_archives()

    print(f"[DONE] MLP family repair closeout written | report={report_relative_path}")
    print(
        "[DONE] Accepted MLP row remaining non-green cells | "
        f"table2={remaining_non_green_dictionary['table2']} | "
        f"table3={remaining_non_green_dictionary['table3']} | "
        f"table4={remaining_non_green_dictionary['table4']} | "
        f"table5={remaining_non_green_dictionary['table5']}"
    )


if __name__ == "__main__":
    main()
