"""Close out one Track 1 forward residual-repair campaign.

This utility promotes only the real pair-level improvements from the completed
forward-only original-dataset repair wave, refreshes the canonical benchmark
and master summary, materializes campaign bookkeeping artifacts, and writes the
final campaign-results report.
"""

from __future__ import annotations

# Import Python Utilities
import argparse
import re
import sys
from collections import defaultdict
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Third-Party Utilities
import yaml

PROJECT_PATH = Path(__file__).resolve().parents[4]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.reports.closeout.track1.closeout_track1_bidirectional_original_dataset_mega_campaign import (
    AMPLITUDE_HARMONIC_LIST,
    FAMILY_ORDER,
    GREEN_MARKER,
    PHASE_HARMONIC_LIST,
    RED_MARKER,
    YELLOW_MARKER,
    find_line_index,
    format_metric_value,
    parse_dual_direction_matrix_section,
    resolve_status_marker,
)
from scripts.reports.track1.refresh_track1_family_reference_archives import (
    sanitize_repository_metric_cell,
)
from scripts.reports.closeout.track1.track1_reference_archive_closeout_support import (
    refresh_directional_reference_archives_from_selection,
)

ACTIVE_CAMPAIGN_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
BENCHMARK_REPORT_PATH = (
    PROJECT_PATH / "doc" / "reports" / "analysis" / "RCIM Paper Reference Benchmark.md"
)
MASTER_SUMMARY_PATH = (
    PROJECT_PATH / "doc" / "reports" / "analysis" / "Training Results Master Summary.md"
)
REPORT_OUTPUT_ROOT = (
    PROJECT_PATH / "doc" / "reports" / "campaign_results" / "track1" / "exact_paper"
)
TRACK1_COMPARISON_ROW_PATTERN = re.compile(
    r"(\| Track 1 canonical closure rule \| Four full-matrix replication tables plus `10 x 19` accepted family-bank models \| )(.*?)( \| not_yet_met \|)"
)
TRACK1_STATUS_BLOCK_PATTERN = re.compile(
    r"### Track 1 Canonical Status\n\n.*?\n### Track 1\.5 Harmonic-Wise Validation Support",
    re.DOTALL,
)
CURRENT_EVIDENCE_BLOCK_PATTERN = re.compile(
    r"Current repository evidence source for the full matrices:\n\n.*?\nStatus legend used in the repository matrices:",
    re.DOTALL,
)
GAP_SUMMARY_LINE_PATTERN = re.compile(
    r"- `Track 1` still has `\d+` non-green cells across the bidirectional original-dataset restart benchmark surface\."
)

SELECTION_POLICY = {
    "primary_metric": "closure_score_desc",
    "first_tie_breaker": "met_paper_cell_count_desc",
    "second_tie_breaker": "near_paper_cell_count_desc",
    "third_tie_breaker": "open_paper_cell_count_asc",
    "fourth_tie_breaker": "mean_normalized_gap_ratio_asc",
    "fifth_tie_breaker": "max_normalized_gap_ratio_asc",
    "sixth_tie_breaker": "winning_mean_component_mae_asc",
    "seventh_tie_breaker": "winning_mean_component_rmse_asc",
    "eighth_tie_breaker": "run_name",
    "direction": "maximize_then_minimize",
    "note": (
        "This winner is the bookkeeping representative of the completed Track 1 "
        "forward open-cell repair campaign."
    ),
}
BEST_RUN_MD_SELECTION_LINES = [
    "- Primary metric: `closure_score_desc`",
    "- First tie-breaker: `met_paper_cell_count_desc`",
    "- Second tie-breaker: `near_paper_cell_count_desc`",
    "- Third tie-breaker: `open_paper_cell_count_asc`",
    "- Fourth tie-breaker: `mean_normalized_gap_ratio_asc`",
    "- Fifth tie-breaker: `max_normalized_gap_ratio_asc`",
    "- Sixth tie-breaker: `winning_mean_component_mae_asc`",
    "- Seventh tie-breaker: `winning_mean_component_rmse_asc`",
    "- Eighth tie-breaker: `run_name`",
]
FAMILY_SLUG_TO_PAPER_CODE = {
    "svm": "SVM",
    "mlp": "MLP",
    "rf": "RF",
    "dt": "DT",
    "et": "ET",
    "ert": "ERT",
    "gbm": "GBM",
    "hgbm": "HGBM",
    "xgbm": "XGBM",
    "lgbm": "LGBM",
}

CAMPAIGN_PROFILE_BY_NAME: dict[str, dict[str, str]] = {
    "track1_forward_open_cell_repair_campaign_2026-04-27_13_08_10": {
        "validation_root_relative_path": (
            "output/validation_checks/"
            "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair"
        ),
        "run_pattern": (
            r"^track1_forward_(?P<family>[a-z0-9]+)_(?P<scope>ampl|phase)_h(?P<harmonic>\d+)"
            r"_open_cell_repair_attempt_(?P<attempt>\d+)$"
        ),
        "report_filename_suffix": "track1_forward_open_cell_repair_campaign_results_report.md",
        "report_heading": "# Track 1 Forward Open-Cell Repair Campaign Results",
        "closeout_label": "forward open-cell repair closeout",
        "evidence_campaign_label": "latest exact-paper forward open-cell repair campaign:",
        "wave_completion_line": "- The forward-only repair wave completed the full `300/300` queue successfully.",
        "master_summary_impact_line": (
            "Forward-only original-dataset open-cell repair wave completed `300/300`, "
            "promoted only real pair-level improvements, and refreshed the canonical "
            "forward restart surface |"
        ),
        "archive_note_line": (
            "This archive was refreshed during the forward open-cell repair closeout. "
            "Improved accepted targets were replaced and retained targets preserved "
            "their previous canonical source runs."
        ),
        "report_written_label": "Forward open-cell repair closeout written",
    },
    "track1_forward_final_open_cells_campaign_2026-04-28_00_30_09": {
        "validation_root_relative_path": (
            "output/validation_checks/"
            "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_final_open_cells"
        ),
        "run_pattern": (
            r"^track1_forward_(?P<family>[a-z0-9]+)_(?P<scope>ampl|phase)_h(?P<harmonic>\d+)"
            r"_final_open_cells_attempt_(?P<attempt>\d+)$"
        ),
        "report_filename_suffix": "track1_forward_final_open_cells_campaign_results_report.md",
        "report_heading": "# Track 1 Forward Final Open-Cells Campaign Results",
        "closeout_label": "forward final open-cells closeout",
        "evidence_campaign_label": "latest exact-paper forward final open-cells campaign:",
        "wave_completion_line": "- The final forward-only residual wave completed the full `76/76` queue successfully.",
        "master_summary_impact_line": (
            "Forward-only original-dataset final residual wave completed `76/76`, "
            "promoted only real pair-level improvements, and refreshed the canonical "
            "forward restart surface |"
        ),
        "archive_note_line": (
            "This archive was refreshed during the forward final open-cells closeout. "
            "Improved accepted targets were replaced and retained targets preserved "
            "their previous canonical source runs."
        ),
        "report_written_label": "Forward final open-cells closeout written",
    },
    "track1_forward_last_non_green_cells_campaign_2026-04-28_11_36_05": {
        "validation_root_relative_path": (
            "output/validation_checks/"
            "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_non_green_cells"
        ),
        "run_pattern": (
            r"^track1_forward_(?P<family>[a-z0-9]+)_(?P<scope>ampl|phase)_h(?P<harmonic>\d+)"
            r"_last_non_green_cells_attempt_(?P<attempt>\d+)$"
        ),
        "report_filename_suffix": "track1_forward_last_non_green_cells_campaign_results_report.md",
        "report_heading": "# Track 1 Forward Last Non-Green Cells Campaign Results",
        "closeout_label": "forward last non-green cells closeout",
        "evidence_campaign_label": "latest exact-paper forward last non-green cells campaign:",
        "wave_completion_line": "- The final forward-only last non-green wave completed the full `108/108` queue successfully.",
        "master_summary_impact_line": (
            "Forward-only original-dataset last non-green wave completed `108/108`, "
            "promoted only real pair-level improvements, and refreshed the canonical "
            "forward restart surface |"
        ),
        "archive_note_line": (
            "This archive was refreshed during the forward last non-green cells closeout. "
            "Improved accepted targets were replaced and retained targets preserved "
            "their previous canonical source runs."
        ),
        "report_written_label": "Forward last non-green cells closeout written",
    },
    "track1_forward_maxi_last_non_green_cells_campaign_2026-04-29_01_44_22": {
        "validation_root_relative_path": (
            "output/validation_checks/"
            "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_maxi_last_non_green_cells"
        ),
        "run_pattern": (
            r"^track1_forward_(?P<family>[a-z0-9]+)_(?P<scope>ampl|phase)_h(?P<harmonic>\d+)"
            r"_maxi_last_non_green_cells_attempt_(?P<attempt>\d+)$"
        ),
        "report_filename_suffix": "track1_forward_maxi_last_non_green_cells_campaign_results_report.md",
        "report_heading": "# Track 1 Forward Maxi Last Non-Green Cells Campaign Results",
        "closeout_label": "forward maxi last non-green cells closeout",
        "evidence_campaign_label": "latest exact-paper forward maxi last non-green cells campaign:",
        "wave_completion_line": "- The forward-only maxi residual wave completed the full `270/270` queue successfully.",
        "master_summary_impact_line": (
            "Forward-only original-dataset maxi last non-green wave completed `270/270`, "
            "promoted only real pair-level improvements, and refreshed the canonical "
            "forward restart surface |"
        ),
        "archive_note_line": (
            "This archive was refreshed during the forward maxi last non-green cells closeout. "
            "Improved accepted targets were replaced and retained targets preserved "
            "their previous canonical source runs."
        ),
        "report_written_label": "Forward maxi last non-green cells closeout written",
    },
    "track1_forward_last_four_open_cells_campaign_2026-04-29_12_01_54": {
        "validation_root_relative_path": (
            "output/validation_checks/"
            "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_four_open_cells"
        ),
        "run_pattern": (
            r"^track1_forward_(?P<family>[a-z0-9]+)_(?P<scope>ampl|phase)_h(?P<harmonic>\d+)"
            r"_last_four_open_cells_attempt_(?P<attempt>\d+)$"
        ),
        "report_filename_suffix": "track1_forward_last_four_open_cells_campaign_results_report.md",
        "report_heading": "# Track 1 Forward Last Four Open Cells Campaign Results",
        "closeout_label": "forward last four open cells closeout",
        "evidence_campaign_label": "latest exact-paper forward last four open cells campaign:",
        "wave_completion_line": "- The final forward-only last-four-open-cells wave completed the full `84/84` queue successfully.",
        "master_summary_impact_line": (
            "Forward-only original-dataset last four open cells wave completed `84/84`, "
            "promoted only real pair-level improvements, and refreshed the canonical "
            "forward restart surface |"
        ),
        "archive_note_line": (
            "This archive was refreshed during the forward last four open cells closeout. "
            "Improved accepted targets were replaced and retained targets preserved "
            "their previous canonical source runs."
        ),
        "report_written_label": "Forward last four open cells closeout written",
    },
    "track1_forward_last_three_open_cells_campaign_2026-04-29_14_37_21": {
        "validation_root_relative_path": (
            "output/validation_checks/"
            "paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_three_open_cells"
        ),
        "run_pattern": (
            r"^track1_forward_(?P<family>[a-z0-9]+)_(?P<scope>ampl|phase)_h(?P<harmonic>\d+)"
            r"_last_three_open_cells_attempt_(?P<attempt>\d+)$"
        ),
        "report_filename_suffix": "track1_forward_last_three_open_cells_campaign_results_report.md",
        "report_heading": "# Track 1 Forward Last Three Open Cells Campaign Results",
        "closeout_label": "forward last three open cells closeout",
        "evidence_campaign_label": "latest exact-paper forward last three open cells campaign:",
        "wave_completion_line": "- The final forward-only last-three-open-cells wave completed the full `84/84` queue successfully.",
        "master_summary_impact_line": (
            "Forward-only original-dataset last three open cells wave completed `84/84`, "
            "promoted only real pair-level improvements, and refreshed the canonical "
            "forward restart surface |"
        ),
        "archive_note_line": (
            "This archive was refreshed during the forward last three open cells closeout. "
            "Improved accepted targets were replaced and retained targets preserved "
            "their previous canonical source runs."
        ),
        "report_written_label": "Forward last three open cells closeout written",
    },
}


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse the CLI arguments for the closeout utility."""

    argument_parser = argparse.ArgumentParser(
        description="Close out one Track 1 forward residual-repair campaign."
    )
    argument_parser.add_argument(
        "--report-timestamp",
        required=True,
        help="Timestamp prefix used for the final campaign results report filename.",
    )
    return argument_parser.parse_args()


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    with input_path.open("r", encoding="utf-8") as input_file:
        loaded_dictionary = yaml.safe_load(input_file)
    assert isinstance(loaded_dictionary, dict), f"Expected YAML dictionary | path={input_path}"
    return loaded_dictionary


def save_yaml_dictionary(output_path: Path, payload: dict[str, Any]) -> None:

    """Persist one YAML dictionary to disk."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=True)


def format_project_relative_path(path_value: Path | str) -> str:

    """Format one path relative to the repository root."""

    resolved_path = Path(path_value)
    if not resolved_path.is_absolute():
        resolved_path = PROJECT_PATH / resolved_path
    return resolved_path.resolve().relative_to(PROJECT_PATH.resolve()).as_posix()


def normalize_config_path(path_text: str | Path) -> str:

    """Normalize one config path to slash-separated relative form."""

    return str(path_text).replace("\\", "/").strip()


def resolve_campaign_profile(active_campaign_dictionary: dict[str, Any]) -> dict[str, str]:

    """Resolve the closeout profile for the active forward campaign."""

    campaign_name = str(active_campaign_dictionary["campaign_name"])
    assert campaign_name in CAMPAIGN_PROFILE_BY_NAME, (
        "Unexpected active campaign for this closeout script | "
        f"campaign_name={campaign_name}"
    )
    return CAMPAIGN_PROFILE_BY_NAME[campaign_name]


def resolve_validation_root(campaign_profile: dict[str, str]) -> Path:

    """Resolve the validation root for one supported campaign profile."""

    return PROJECT_PATH / str(campaign_profile["validation_root_relative_path"])


def resolve_campaign_finished_at_text(
    active_campaign_dictionary: dict[str, Any],
    validation_root: Path,
) -> str:

    """Resolve one durable finished-at timestamp from the local campaign artifacts."""

    existing_finished_at = active_campaign_dictionary.get("finished_at")
    if existing_finished_at:
        return str(existing_finished_at)

    candidate_datetime_list: list[datetime] = []
    for summary_path in validation_root.rglob("validation_summary.yaml"):
        candidate_datetime_list.append(
            datetime.fromtimestamp(summary_path.stat().st_mtime).astimezone()
        )

    campaign_output_directory = PROJECT_PATH / str(active_campaign_dictionary["campaign_output_directory"])
    log_directory = campaign_output_directory / "logs"
    if log_directory.exists():
        for log_path in log_directory.rglob("*.log"):
            candidate_datetime_list.append(
                datetime.fromtimestamp(log_path.stat().st_mtime).astimezone()
            )

    assert candidate_datetime_list, (
        "Unable to derive one campaign finished timestamp from the local artifacts | "
        f"validation_root={validation_root}"
    )
    return max(candidate_datetime_list).isoformat(timespec="seconds")


def parse_markdown_row(markdown_line: str) -> list[str]:

    """Parse one Markdown table row into stripped cells."""

    normalized_line = markdown_line.strip().strip("|")
    return [cell.strip() for cell in normalized_line.split("|")]


def parse_current_repository_rows(
    benchmark_line_list: list[str],
    heading_text: str,
    expected_row_count: int,
) -> dict[str, dict[str, dict[int, float]]]:

    """Parse current paper and repository values for one dual-direction section."""

    section_dictionary = parse_dual_direction_matrix_section(
        benchmark_line_list,
        heading_text,
        expected_row_count=expected_row_count,
    )
    heading_index = section_dictionary["heading_index"]
    forward_anchor_index = find_line_index(
        benchmark_line_list,
        "Forward repository-owned restart matrix:",
        start_index=heading_index,
    )
    backward_anchor_index = find_line_index(
        benchmark_line_list,
        "Backward repository-owned restart matrix:",
        start_index=heading_index,
    )
    forward_row_list = []
    backward_row_list = []
    for row_index, row_cell_list in (
        collect_matrix_rows(benchmark_line_list, forward_anchor_index, expected_row_count)
    ):
        forward_row_list.append((row_index, row_cell_list))
    for row_index, row_cell_list in (
        collect_matrix_rows(benchmark_line_list, backward_anchor_index, expected_row_count)
    ):
        backward_row_list.append((row_index, row_cell_list))

    harmonic_list = section_dictionary["harmonic_list"]
    repository_rows: dict[str, dict[str, dict[int, float]]] = {
        "paper": deepcopy(section_dictionary["paper_rows"]),
        "forward": {},
        "backward": {},
    }
    for _, row_cell_list in forward_row_list:
        family_code = row_cell_list[0].strip("`")
        repository_rows["forward"][family_code] = {
            harmonic_order: float(sanitize_repository_metric_cell(repository_cell))
            for harmonic_order, repository_cell in zip(harmonic_list, row_cell_list[1:], strict=True)
        }
    for _, row_cell_list in backward_row_list:
        family_code = row_cell_list[0].strip("`")
        repository_rows["backward"][family_code] = {
            harmonic_order: float(sanitize_repository_metric_cell(repository_cell))
            for harmonic_order, repository_cell in zip(harmonic_list, row_cell_list[1:], strict=True)
        }
    repository_rows["line_indexes"] = {
        "forward": section_dictionary["forward_row_index_map"],
        "backward": section_dictionary["backward_row_index_map"],
    }
    return repository_rows


def collect_matrix_rows(
    line_list: list[str],
    start_index: int,
    expected_row_count: int,
) -> list[tuple[int, list[str]]]:

    """Collect model rows from one matrix section."""

    collected_row_list: list[tuple[int, list[str]]] = []
    for line_index in range(start_index, len(line_list)):
        current_line = line_list[line_index]
        if current_line.startswith("| `"):
            collected_row_list.append((line_index, parse_markdown_row(current_line)))
            if len(collected_row_list) == expected_row_count:
                return collected_row_list
    raise RuntimeError(
        "Failed to collect expected matrix rows | "
        f"start_index={start_index} | expected_row_count={expected_row_count}"
    )


def build_selection_sort_key(entry: dict[str, Any]) -> tuple[Any, ...]:

    """Build the pair-promotion selection sort key."""

    return (
        -float(entry["closure_score"]),
        -int(entry["met_paper_cell_count"]),
        -int(entry["near_paper_cell_count"]),
        int(entry["open_paper_cell_count"]),
        float(entry["mean_normalized_gap_ratio"]),
        float(entry["max_normalized_gap_ratio"]),
        float(entry["winning_mean_component_mae"]),
        float(entry["winning_mean_component_rmse"]),
        str(entry["run_name"]),
    )


def build_paper_target_dictionary(
    benchmark_section_dictionary: dict[str, dict[str, dict[int, float]]],
) -> dict[str, dict[str, dict[str, float]]]:

    """Build the paper target lookup dictionary from the benchmark matrices."""

    paper_target_dictionary: dict[str, dict[str, dict[str, float]]] = {
        "amplitude": {"mae": defaultdict(dict), "rmse": defaultdict(dict)},
        "phase": {"mae": defaultdict(dict), "rmse": defaultdict(dict)},
    }

    for family_code in FAMILY_ORDER:
        for harmonic_order in AMPLITUDE_HARMONIC_LIST:
            paper_target_dictionary["amplitude"]["mae"][family_code][str(harmonic_order)] = (
                benchmark_section_dictionary["table2"]["paper"][family_code][harmonic_order]
            )
            paper_target_dictionary["amplitude"]["rmse"][family_code][str(harmonic_order)] = (
                benchmark_section_dictionary["table3"]["paper"][family_code][harmonic_order]
            )
        for harmonic_order in PHASE_HARMONIC_LIST:
            paper_target_dictionary["phase"]["mae"][family_code][str(harmonic_order)] = (
                benchmark_section_dictionary["table4"]["paper"][family_code][harmonic_order]
            )
            paper_target_dictionary["phase"]["rmse"][family_code][str(harmonic_order)] = (
                benchmark_section_dictionary["table5"]["paper"][family_code][harmonic_order]
            )
    return paper_target_dictionary


def build_campaign_entry_from_summary(
    summary_dictionary: dict[str, Any],
    paper_target_dictionary: dict[str, dict[str, dict[str, float]]],
    run_pattern: re.Pattern[str],
) -> dict[str, Any]:

    """Build one promotion candidate entry from one validation summary."""

    run_name = str(summary_dictionary["experiment"]["run_name"])
    matched_run = run_pattern.match(run_name)
    assert matched_run is not None, f"Unsupported campaign run format | run_name={run_name}"

    family_slug = str(matched_run.group("family"))
    paper_family_code = FAMILY_SLUG_TO_PAPER_CODE[family_slug]
    scope_key = "amplitude" if str(matched_run.group("scope")) == "ampl" else "phase"
    harmonic_order = int(matched_run.group("harmonic"))

    winning_mae = float(summary_dictionary["winner_summary"]["winning_mean_component_mae"])
    winning_rmse = float(summary_dictionary["winner_summary"]["winning_mean_component_rmse"])
    winning_mape = float(summary_dictionary["winner_summary"]["winning_mean_component_mape_percent"])
    paper_mae = float(paper_target_dictionary[scope_key]["mae"][paper_family_code][str(harmonic_order)])
    paper_rmse = float(paper_target_dictionary[scope_key]["rmse"][paper_family_code][str(harmonic_order)])

    met_paper_cell_count = 0
    near_paper_cell_count = 0
    open_paper_cell_count = 0
    normalized_gap_ratio_list: list[float] = []
    for repository_value, paper_value in ((winning_mae, paper_mae), (winning_rmse, paper_rmse)):
        if repository_value <= paper_value:
            met_paper_cell_count += 1
            normalized_gap_ratio_list.append(0.0)
        else:
            normalized_gap_ratio = (repository_value - paper_value) / paper_value
            normalized_gap_ratio_list.append(normalized_gap_ratio)
            if repository_value <= (paper_value * 1.25):
                near_paper_cell_count += 1
            else:
                open_paper_cell_count += 1
    closure_score = (met_paper_cell_count + (0.5 * near_paper_cell_count)) / 2.0

    return {
        "entry_origin": "campaign",
        "run_name": run_name,
        "paper_family_code": paper_family_code,
        "scope_key": scope_key,
        "harmonic_order": harmonic_order,
        "winning_mean_component_mae": winning_mae,
        "winning_mean_component_rmse": winning_rmse,
        "winning_mean_component_mape_percent": winning_mape,
        "paper_mae": paper_mae,
        "paper_rmse": paper_rmse,
        "met_paper_cell_count": met_paper_cell_count,
        "near_paper_cell_count": near_paper_cell_count,
        "open_paper_cell_count": open_paper_cell_count,
        "closure_score": closure_score,
        "mean_normalized_gap_ratio": sum(normalized_gap_ratio_list) / len(normalized_gap_ratio_list),
        "max_normalized_gap_ratio": max(normalized_gap_ratio_list),
        "validation_summary_path": format_project_relative_path(
            Path(str(summary_dictionary["artifacts"]["validation_summary_path"]).replace("/", "\\"))
        ),
        "config_path": normalize_config_path(summary_dictionary["config_path"]),
        "experiment_output_directory": normalize_config_path(summary_dictionary["experiment"]["output_directory"]),
    }


def build_baseline_entry(
    paper_family_code: str,
    scope_key: str,
    harmonic_order: int,
    current_mae: float,
    current_rmse: float,
    paper_mae: float,
    paper_rmse: float,
) -> dict[str, Any]:

    """Build one synthetic baseline entry from the current accepted benchmark cell."""

    met_paper_cell_count = 0
    near_paper_cell_count = 0
    open_paper_cell_count = 0
    normalized_gap_ratio_list: list[float] = []
    for repository_value, paper_value in ((current_mae, paper_mae), (current_rmse, paper_rmse)):
        if repository_value <= paper_value:
            met_paper_cell_count += 1
            normalized_gap_ratio_list.append(0.0)
        else:
            normalized_gap_ratio = (repository_value - paper_value) / paper_value
            normalized_gap_ratio_list.append(normalized_gap_ratio)
            if repository_value <= (paper_value * 1.25):
                near_paper_cell_count += 1
            else:
                open_paper_cell_count += 1
    closure_score = (met_paper_cell_count + (0.5 * near_paper_cell_count)) / 2.0

    return {
        "entry_origin": "baseline",
        "run_name": f"current_benchmark_{paper_family_code.lower()}_{scope_key}_h{harmonic_order}",
        "paper_family_code": paper_family_code,
        "scope_key": scope_key,
        "harmonic_order": harmonic_order,
        "winning_mean_component_mae": float(current_mae),
        "winning_mean_component_rmse": float(current_rmse),
        "winning_mean_component_mape_percent": float("inf"),
        "paper_mae": float(paper_mae),
        "paper_rmse": float(paper_rmse),
        "met_paper_cell_count": met_paper_cell_count,
        "near_paper_cell_count": near_paper_cell_count,
        "open_paper_cell_count": open_paper_cell_count,
        "closure_score": closure_score,
        "mean_normalized_gap_ratio": sum(normalized_gap_ratio_list) / len(normalized_gap_ratio_list),
        "max_normalized_gap_ratio": max(normalized_gap_ratio_list),
        "validation_summary_path": "",
        "config_path": "",
        "experiment_output_directory": "",
    }


def collect_campaign_summary_bundle(
    active_campaign_dictionary: dict[str, Any],
    paper_target_dictionary: dict[str, dict[str, dict[str, float]]],
    validation_root: Path,
    run_pattern: re.Pattern[str],
) -> tuple[list[dict[str, Any]], dict[tuple[str, str, int], dict[str, Any]], dict[str, list[dict[str, Any]]]]:

    """Collect all campaign entries and the best retry per targeted pair."""

    queue_config_path_set = {
        normalize_config_path(config_path)
        for config_path in active_campaign_dictionary["queue_config_path_list"]
    }
    collected_entry_list: list[dict[str, Any]] = []
    pair_entry_list_dictionary: dict[tuple[str, str, int], list[dict[str, Any]]] = defaultdict(list)

    for summary_path in sorted(validation_root.rglob("validation_summary.yaml")):
        summary_dictionary = load_yaml_dictionary(summary_path)
        config_path = normalize_config_path(summary_dictionary.get("config_path", ""))
        if config_path not in queue_config_path_set:
            continue
        campaign_entry = build_campaign_entry_from_summary(
            summary_dictionary,
            paper_target_dictionary,
            run_pattern,
        )
        pair_identifier = (
            campaign_entry["paper_family_code"],
            campaign_entry["scope_key"],
            int(campaign_entry["harmonic_order"]),
        )
        collected_entry_list.append(campaign_entry)
        pair_entry_list_dictionary[pair_identifier].append(campaign_entry)

    assert len(collected_entry_list) == len(queue_config_path_set), (
        "Resolved validation-summary count does not match the campaign queue | "
        f"resolved={len(collected_entry_list)} | expected={len(queue_config_path_set)}"
    )

    best_pair_retry_dictionary: dict[tuple[str, str, int], dict[str, Any]] = {}
    for pair_identifier, pair_entry_list in pair_entry_list_dictionary.items():
        best_pair_retry_dictionary[pair_identifier] = sorted(
            pair_entry_list,
            key=build_selection_sort_key,
        )[0]
    return collected_entry_list, best_pair_retry_dictionary, pair_entry_list_dictionary


def build_promotion_bundle(
    benchmark_section_dictionary: dict[str, dict[str, dict[int, float]]],
    paper_target_dictionary: dict[str, dict[str, dict[str, float]]],
    pair_entry_list_dictionary: dict[tuple[str, str, int], list[dict[str, Any]]],
) -> tuple[dict[tuple[str, str, int], dict[str, Any]], dict[str, int]]:

    """Promote the better value between the current benchmark and campaign retries."""

    promoted_entry_dictionary: dict[tuple[str, str, int], dict[str, Any]] = {}
    improvement_summary_dictionary = {
        "promoted_pair_count": 0,
        "retained_baseline_pair_count": 0,
        "targeted_pair_count": 0,
    }

    for pair_identifier, pair_entry_list in pair_entry_list_dictionary.items():
        paper_family_code, scope_key, harmonic_order = pair_identifier
        direction_label = "forward"
        table_mae_key = "table2" if scope_key == "amplitude" else "table4"
        table_rmse_key = "table3" if scope_key == "amplitude" else "table5"
        current_mae = benchmark_section_dictionary[table_mae_key][direction_label][paper_family_code][harmonic_order]
        current_rmse = benchmark_section_dictionary[table_rmse_key][direction_label][paper_family_code][harmonic_order]
        paper_mae = paper_target_dictionary[scope_key]["mae"][paper_family_code][str(harmonic_order)]
        paper_rmse = paper_target_dictionary[scope_key]["rmse"][paper_family_code][str(harmonic_order)]
        baseline_entry = build_baseline_entry(
            paper_family_code,
            scope_key,
            harmonic_order,
            current_mae,
            current_rmse,
            paper_mae,
            paper_rmse,
        )
        selected_entry = sorted([baseline_entry, *pair_entry_list], key=build_selection_sort_key)[0]
        promoted_entry_dictionary[pair_identifier] = selected_entry
        improvement_summary_dictionary["targeted_pair_count"] += 1
        if selected_entry["entry_origin"] == "campaign":
            improvement_summary_dictionary["promoted_pair_count"] += 1
        else:
            improvement_summary_dictionary["retained_baseline_pair_count"] += 1

    return promoted_entry_dictionary, improvement_summary_dictionary


def compute_benchmark_status_dictionary(
    benchmark_line_list: list[str],
) -> dict[str, dict[str, dict[str, int]]]:

    """Compute table-level green, yellow, and red counts from the benchmark text."""

    status_dictionary: dict[str, dict[str, dict[str, int]]] = {}
    for table_key, heading_text in (
        ("table2", "#### Table 2 - Amplitude MAE Full-Matrix Replication"),
        ("table3", "#### Table 3 - Amplitude RMSE Full-Matrix Replication"),
        ("table4", "#### Table 4 - Phase MAE Full-Matrix Replication"),
        ("table5", "#### Table 5 - Phase RMSE Full-Matrix Replication"),
    ):
        section_dictionary = parse_dual_direction_matrix_section(
            benchmark_line_list,
            heading_text,
            expected_row_count=10,
        )
        harmonic_list = section_dictionary["harmonic_list"]
        status_dictionary[table_key] = {}
        for direction_label, row_index_map in (
            ("forward", section_dictionary["forward_row_index_map"]),
            ("backward", section_dictionary["backward_row_index_map"]),
        ):
            counts = {"green": 0, "yellow": 0, "red": 0, "total": 0}
            for paper_family_code in FAMILY_ORDER:
                row_line = benchmark_line_list[row_index_map[paper_family_code]]
                row_cells = parse_markdown_row(row_line)
                for harmonic_order, repository_cell in zip(harmonic_list, row_cells[1:], strict=True):
                    repository_value = float(sanitize_repository_metric_cell(repository_cell))
                    paper_value = section_dictionary["paper_rows"][paper_family_code][harmonic_order]
                    marker = resolve_status_marker(repository_value, paper_value)
                    counts["total"] += 1
                    if marker == GREEN_MARKER:
                        counts["green"] += 1
                    elif marker == YELLOW_MARKER:
                        counts["yellow"] += 1
                    else:
                        counts["red"] += 1
            status_dictionary[table_key][direction_label] = counts
    return status_dictionary


def update_benchmark_report(
    benchmark_section_dictionary: dict[str, dict[str, dict[int, float]]],
    promoted_entry_dictionary: dict[tuple[str, str, int], dict[str, Any]],
    report_relative_path: str,
    active_campaign_dictionary: dict[str, Any],
    campaign_profile: dict[str, str],
) -> dict[str, dict[str, dict[str, int]]]:

    """Apply the promoted forward entries to the canonical benchmark report."""

    benchmark_line_list = BENCHMARK_REPORT_PATH.read_text(encoding="utf-8").splitlines()
    section_dictionary_map = {
        "table2": parse_dual_direction_matrix_section(
            benchmark_line_list,
            "#### Table 2 - Amplitude MAE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table3": parse_dual_direction_matrix_section(
            benchmark_line_list,
            "#### Table 3 - Amplitude RMSE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table4": parse_dual_direction_matrix_section(
            benchmark_line_list,
            "#### Table 4 - Phase MAE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table5": parse_dual_direction_matrix_section(
            benchmark_line_list,
            "#### Table 5 - Phase RMSE Full-Matrix Replication",
            expected_row_count=10,
        ),
    }

    updated_metric_dictionary = deepcopy(benchmark_section_dictionary)
    for (paper_family_code, scope_key, harmonic_order), promoted_entry in promoted_entry_dictionary.items():
        updated_metric_dictionary["table2" if scope_key == "amplitude" else "table4"]["forward"][paper_family_code][harmonic_order] = (
            float(promoted_entry["winning_mean_component_mae"])
        )
        updated_metric_dictionary["table3" if scope_key == "amplitude" else "table5"]["forward"][paper_family_code][harmonic_order] = (
            float(promoted_entry["winning_mean_component_rmse"])
        )

    for table_key, section_dictionary in section_dictionary_map.items():
        target_kind = "amplitude" if table_key in {"table2", "table3"} else "phase"
        harmonic_list = AMPLITUDE_HARMONIC_LIST if target_kind == "amplitude" else PHASE_HARMONIC_LIST
        for direction_label, row_index_map in (
            ("forward", section_dictionary["forward_row_index_map"]),
            ("backward", section_dictionary["backward_row_index_map"]),
        ):
            for paper_family_code in FAMILY_ORDER:
                row_cell_list = [f"`{paper_family_code}`"]
                for harmonic_order in harmonic_list:
                    repository_value = updated_metric_dictionary[table_key][direction_label][paper_family_code][harmonic_order]
                    paper_value = section_dictionary["paper_rows"][paper_family_code][harmonic_order]
                    marker = resolve_status_marker(repository_value, paper_value)
                    row_cell_list.append(f"`{marker} {format_metric_value(repository_value)}`")
                benchmark_line_list[row_index_map[paper_family_code]] = "| " + " | ".join(row_cell_list) + " |"

    evidence_block_replacement = "\n".join(
        [
            "Current repository evidence source for the full matrices:",
            "",
            f"- {campaign_profile['evidence_campaign_label']}",
            f"  `{active_campaign_dictionary['campaign_name']}`",
            "- execution window:",
            f"  `{active_campaign_dictionary['started_at']}` to `{active_campaign_dictionary['finished_at']}`",
            "- supporting campaign report:",
            f"  `{report_relative_path}`",
            "",
            "Status legend used in the repository matrices:",
        ]
    )
    updated_benchmark_text = "\n".join(benchmark_line_list) + "\n"
    updated_benchmark_text = CURRENT_EVIDENCE_BLOCK_PATTERN.sub(
        evidence_block_replacement,
        updated_benchmark_text,
        count=1,
    )
    BENCHMARK_REPORT_PATH.write_text(updated_benchmark_text, encoding="utf-8", newline="\n")
    return compute_benchmark_status_dictionary(updated_benchmark_text.splitlines())


def write_campaign_bookkeeping(
    active_campaign_dictionary: dict[str, Any],
    entry_list: list[dict[str, Any]],
) -> dict[str, Any]:

    """Write leaderboard and best-run artifacts for the campaign."""

    campaign_output_directory = PROJECT_PATH / str(active_campaign_dictionary["campaign_output_directory"])
    sorted_entry_list = sorted(entry_list, key=build_selection_sort_key)
    best_entry = deepcopy(sorted_entry_list[0])
    selected_at_text = datetime.now().astimezone().isoformat(timespec="seconds")

    leaderboard_dictionary = {
        "schema_version": 1,
        "campaign_name": str(active_campaign_dictionary["campaign_name"]),
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
            f"# Campaign Best Run - {active_campaign_dictionary['campaign_name']}",
            "",
            f"- Run: `{best_entry['run_name']}`",
            f"- Family: `{best_entry['paper_family_code']}`",
            f"- Scope: `{best_entry['scope_key']}`",
            f"- Harmonic: `{int(best_entry['harmonic_order'])}`",
            f"- Closure Score: `{float(best_entry['closure_score']):.3f}`",
            f"- Met / Near / Open: `{int(best_entry['met_paper_cell_count'])}` / `{int(best_entry['near_paper_cell_count'])}` / `{int(best_entry['open_paper_cell_count'])}`",
            "",
            "## Selection Policy",
            "",
            *BEST_RUN_MD_SELECTION_LINES,
            "",
        ]
    )

    campaign_output_directory.mkdir(parents=True, exist_ok=True)
    save_yaml_dictionary(campaign_output_directory / "campaign_leaderboard.yaml", leaderboard_dictionary)
    save_yaml_dictionary(campaign_output_directory / "campaign_best_run.yaml", best_run_dictionary)
    (campaign_output_directory / "campaign_best_run.md").write_text(
        best_run_markdown,
        encoding="utf-8",
        newline="\n",
    )
    return best_run_dictionary


def build_results_report_markdown(
    report_timestamp: str,
    active_campaign_dictionary: dict[str, Any],
    campaign_profile: dict[str, str],
    validation_root: Path,
    family_best_dictionary: dict[str, dict[str, Any]],
    best_run_dictionary: dict[str, Any],
    improvement_summary_dictionary: dict[str, int],
    previous_status_dictionary: dict[str, dict[str, dict[str, int]]],
    updated_status_dictionary: dict[str, dict[str, dict[str, int]]],
    archive_summary_list: list[dict[str, Any]],
) -> str:

    """Build the final campaign-results report Markdown."""

    family_table_line_list = [
        "| Family | Best Run | Scope | Harmonic | Closure Score | Met | Near | Open |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for family_code in FAMILY_ORDER:
        if family_code not in family_best_dictionary:
            continue
        family_entry = family_best_dictionary[family_code]
        family_table_line_list.append(
            "| "
            f"`{family_code}` | "
            f"`{family_entry['run_name']}` | "
            f"`{family_entry['scope_key']}` | "
            f"{int(family_entry['harmonic_order'])} | "
            f"{float(family_entry['closure_score']):.3f} | "
            f"{int(family_entry['met_paper_cell_count'])} | "
            f"{int(family_entry['near_paper_cell_count'])} | "
            f"{int(family_entry['open_paper_cell_count'])} |"
        )

    before_after_line_list = [
        "| Surface | Before | After | Delta |",
        "| --- | --- | --- | --- |",
    ]
    for table_key, table_label in (
        ("table2", "Table `2` forward amplitude MAE"),
        ("table3", "Table `3` forward amplitude RMSE"),
        ("table4", "Table `4` forward phase MAE"),
        ("table5", "Table `5` forward phase RMSE"),
    ):
        previous_counts = previous_status_dictionary[table_key]["forward"]
        updated_counts = updated_status_dictionary[table_key]["forward"]
        before_after_line_list.append(
            f"| {table_label} | "
            f"`{previous_counts['green']}G / {previous_counts['yellow']}Y / {previous_counts['red']}R` | "
            f"`{updated_counts['green']}G / {updated_counts['yellow']}Y / {updated_counts['red']}R` | "
            f"`{updated_counts['yellow'] - previous_counts['yellow']}Y / {updated_counts['red'] - previous_counts['red']}R` |"
        )

    total_forward_non_green_before = sum(
        previous_status_dictionary[table_key]["forward"]["yellow"] + previous_status_dictionary[table_key]["forward"]["red"]
        for table_key in ("table2", "table3", "table4", "table5")
    )
    total_forward_non_green_after = sum(
        updated_status_dictionary[table_key]["forward"]["yellow"] + updated_status_dictionary[table_key]["forward"]["red"]
        for table_key in ("table2", "table3", "table4", "table5")
    )

    report_line_list = [
        str(campaign_profile["report_heading"]),
        "",
        "## Overview",
        "",
        f"- campaign name: `{active_campaign_dictionary['campaign_name']}`",
        f"- planning report: `{str(active_campaign_dictionary['planning_report_path']).replace(chr(92), '/')}`",
        f"- queue size: `{len(active_campaign_dictionary['queue_config_path_list'])}`",
        f"- execution window: `{active_campaign_dictionary['started_at']}` to `{active_campaign_dictionary['finished_at']}`",
        f"- campaign output directory: `{format_project_relative_path(active_campaign_dictionary['campaign_output_directory'])}`",
        f"- validation root: `{format_project_relative_path(validation_root)}`",
        f"- report timestamp: `{report_timestamp}`",
        "",
        "## Executive Summary",
        "",
        str(campaign_profile["wave_completion_line"]),
        f"- Targeted family-target pairs: `{improvement_summary_dictionary['targeted_pair_count']}`.",
        f"- Promoted pair winners: `{improvement_summary_dictionary['promoted_pair_count']}`.",
        f"- Retained baseline pair winners: `{improvement_summary_dictionary['retained_baseline_pair_count']}`.",
        f"- Forward non-green cells moved from `{total_forward_non_green_before}` to `{total_forward_non_green_after}`.",
        "",
        "## Family Best Retry Outcome",
        "",
        *family_table_line_list,
        "",
        "## Campaign Best Run",
        "",
        f"- run: `{best_run_dictionary['run_name']}`",
        f"- family: `{best_run_dictionary['paper_family_code']}`",
        f"- scope: `{best_run_dictionary['scope_key']}`",
        f"- harmonic: `{int(best_run_dictionary['harmonic_order'])}`",
        f"- closure score: `{float(best_run_dictionary['closure_score']):.3f}`",
        f"- met / near / open: `{int(best_run_dictionary['met_paper_cell_count'])}` / `{int(best_run_dictionary['near_paper_cell_count'])}` / `{int(best_run_dictionary['open_paper_cell_count'])}`",
        "",
        "## Forward Benchmark Delta",
        "",
        *before_after_line_list,
        "",
        "## Canonical Forward Status After Closeout",
        "",
        f"- Table `2`: `{updated_status_dictionary['table2']['forward']['yellow']}` yellow, `{updated_status_dictionary['table2']['forward']['red']}` red",
        f"- Table `3`: `{updated_status_dictionary['table3']['forward']['yellow']}` yellow, `{updated_status_dictionary['table3']['forward']['red']}` red",
        f"- Table `4`: `{updated_status_dictionary['table4']['forward']['yellow']}` yellow, `{updated_status_dictionary['table4']['forward']['red']}` red",
        f"- Table `5`: `{updated_status_dictionary['table5']['forward']['yellow']}` yellow, `{updated_status_dictionary['table5']['forward']['red']}` red",
        "",
        "## Reference Archive Refresh",
        "",
        "| Direction | Family | Archived Targets | Unique Source Runs | Unique Source Configs | Archive Root |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ]
    for archive_summary in archive_summary_list:
        report_line_list.append(
            f"| `{archive_summary['direction_label']}` | "
            f"`{archive_summary['paper_family_code']}` | "
            f"{archive_summary['reference_target_count']} | "
            f"{archive_summary['source_run_count']} | "
            f"{archive_summary['source_config_count']} | "
            f"`{format_project_relative_path(archive_summary['archive_root'])}` |"
        )
    report_line_list.extend([
        "",
        "## Linked Artifacts",
        "",
        f"- benchmark report: `{format_project_relative_path(BENCHMARK_REPORT_PATH)}`",
        f"- training results master summary: `{format_project_relative_path(MASTER_SUMMARY_PATH)}`",
        "- track1 reference root: `models/paper_reference/rcim_track1/forward/`",
        f"- campaign leaderboard: `{format_project_relative_path(Path(active_campaign_dictionary['campaign_output_directory']) / 'campaign_leaderboard.yaml')}`",
        f"- campaign best run YAML: `{format_project_relative_path(Path(active_campaign_dictionary['campaign_output_directory']) / 'campaign_best_run.yaml')}`",
        f"- campaign best run Markdown: `{format_project_relative_path(Path(active_campaign_dictionary['campaign_output_directory']) / 'campaign_best_run.md')}`",
        "",
    ])
    return "\n".join(report_line_list).rstrip() + "\n"


def patch_master_summary(
    report_relative_path: str,
    active_campaign_dictionary: dict[str, Any],
    campaign_profile: dict[str, str],
    updated_status_dictionary: dict[str, dict[str, dict[str, int]]],
    best_run_dictionary: dict[str, Any],
) -> None:

    """Patch the master summary exact-paper status after the closeout."""

    master_summary_text = MASTER_SUMMARY_PATH.read_text(encoding="utf-8")
    total_non_green_count = sum(
        status_dictionary["yellow"] + status_dictionary["red"]
        for table_dictionary in updated_status_dictionary.values()
        for status_dictionary in table_dictionary.values()
    )
    forward_non_green_count = sum(
        updated_status_dictionary[table_key]["forward"]["yellow"] + updated_status_dictionary[table_key]["forward"]["red"]
        for table_key in ("table2", "table3", "table4", "table5")
    )
    backward_non_green_count = total_non_green_count - forward_non_green_count

    master_summary_text = TRACK1_COMPARISON_ROW_PATTERN.sub(
        (
            r"\1"
            f"Canonical benchmark now has `{total_non_green_count}` non-green cells across Tables `2-5` "
            f"after the {campaign_profile['closeout_label']} (`forward`: `{forward_non_green_count}`, "
            f"`backward`: `{backward_non_green_count}`)"
            r"\3"
        ),
        master_summary_text,
        count=1,
    )

    track1_block_replacement = "\n".join(
        [
            "### Track 1 Canonical Status",
            "",
            f"- Latest exact-paper closeout report: `{report_relative_path}`",
            "- Canonical progress surface:",
            "  - `Table 2 - Amplitude MAE Full-Matrix Replication`",
            "  - `Table 3 - Amplitude RMSE Full-Matrix Replication`",
            "  - `Table 4 - Phase MAE Full-Matrix Replication`",
            "  - `Table 5 - Phase RMSE Full-Matrix Replication`",
            "- Completion rule: `19` accepted models for each of the `10` algorithm families in both `forward` and `backward` directions",
            f"- Table `2` `forward` status: `{updated_status_dictionary['table2']['forward']['green']}` green, `{updated_status_dictionary['table2']['forward']['yellow']}` yellow, `{updated_status_dictionary['table2']['forward']['red']}` red",
            f"- Table `2` `backward` status: `{updated_status_dictionary['table2']['backward']['green']}` green, `{updated_status_dictionary['table2']['backward']['yellow']}` yellow, `{updated_status_dictionary['table2']['backward']['red']}` red",
            f"- Table `3` `forward` status: `{updated_status_dictionary['table3']['forward']['green']}` green, `{updated_status_dictionary['table3']['forward']['yellow']}` yellow, `{updated_status_dictionary['table3']['forward']['red']}` red",
            f"- Table `3` `backward` status: `{updated_status_dictionary['table3']['backward']['green']}` green, `{updated_status_dictionary['table3']['backward']['yellow']}` yellow, `{updated_status_dictionary['table3']['backward']['red']}` red",
            f"- Table `4` `forward` status: `{updated_status_dictionary['table4']['forward']['green']}` green, `{updated_status_dictionary['table4']['forward']['yellow']}` yellow, `{updated_status_dictionary['table4']['forward']['red']}` red",
            f"- Table `4` `backward` status: `{updated_status_dictionary['table4']['backward']['green']}` green, `{updated_status_dictionary['table4']['backward']['yellow']}` yellow, `{updated_status_dictionary['table4']['backward']['red']}` red",
            f"- Table `5` `forward` status: `{updated_status_dictionary['table5']['forward']['green']}` green, `{updated_status_dictionary['table5']['forward']['yellow']}` yellow, `{updated_status_dictionary['table5']['forward']['red']}` red",
            f"- Table `5` `backward` status: `{updated_status_dictionary['table5']['backward']['green']}` green, `{updated_status_dictionary['table5']['backward']['yellow']}` yellow, `{updated_status_dictionary['table5']['backward']['red']}` red",
            f"- Remaining non-green cells across both directional restart surfaces: `{total_non_green_count}`",
            "- Harmonic-wise Table `6` evidence remains postponed into `Track 1.5` and does not gate this closeout.",
            "",
            "### Track 1.5 Harmonic-Wise Validation Support",
        ]
    )
    master_summary_text = TRACK1_STATUS_BLOCK_PATTERN.sub(
        track1_block_replacement,
        master_summary_text,
        count=1,
    )

    recent_campaign_header = "| Campaign | Generated At | Completed | Failed | Winner | Impact |"
    recent_campaign_header_index = master_summary_text.find(recent_campaign_header)
    if recent_campaign_header_index != -1:
        line_list = master_summary_text.splitlines()
        header_index = line_list.index(recent_campaign_header)
        row_index = header_index + 2
        new_row = (
            f"| `{active_campaign_dictionary['campaign_name']}` | "
            f"`{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}` | "
            f"{len(active_campaign_dictionary['queue_config_path_list'])} | 0 | "
            f"`{best_run_dictionary['run_name']}` | "
            f"{campaign_profile['master_summary_impact_line']}"
        )
        line_list.insert(row_index, new_row)
        master_summary_text = "\n".join(line_list) + "\n"

    master_summary_text = GAP_SUMMARY_LINE_PATTERN.sub(
        f"- `Track 1` still has `{total_non_green_count}` non-green cells across the bidirectional original-dataset restart benchmark surface.",
        master_summary_text,
        count=1,
    )

    MASTER_SUMMARY_PATH.write_text(master_summary_text, encoding="utf-8", newline="\n")


def update_active_campaign_state(
    active_campaign_dictionary: dict[str, Any],
    report_relative_path: str,
    finished_at_text: str,
) -> None:

    """Persist the final report backlink inside the campaign state."""

    active_campaign_dictionary["status"] = "completed"
    active_campaign_dictionary["finished_at"] = finished_at_text
    active_campaign_dictionary["completion_recorded_at"] = (
        datetime.now().astimezone().isoformat(timespec="seconds")
    )
    active_campaign_dictionary["results_report_path"] = report_relative_path.replace("/", "\\")
    active_campaign_dictionary["completed_family_list"] = sorted({
        str(Path(config_path).parts[-3]).upper()
        for config_path in active_campaign_dictionary["queue_config_path_list"]
    })
    active_campaign_dictionary["pending_family_list"] = []
    save_yaml_dictionary(ACTIVE_CAMPAIGN_PATH, active_campaign_dictionary)


def main() -> None:

    """Run one supported Track 1 forward residual-repair closeout workflow."""

    command_line_arguments = parse_command_line_arguments()
    report_timestamp = str(command_line_arguments.report_timestamp)
    active_campaign_dictionary = load_yaml_dictionary(ACTIVE_CAMPAIGN_PATH)
    campaign_profile = resolve_campaign_profile(active_campaign_dictionary)
    validation_root = resolve_validation_root(campaign_profile)
    run_pattern = re.compile(str(campaign_profile["run_pattern"]))
    active_campaign_dictionary["finished_at"] = resolve_campaign_finished_at_text(
        active_campaign_dictionary,
        validation_root,
    )

    benchmark_line_list = BENCHMARK_REPORT_PATH.read_text(encoding="utf-8").splitlines()
    benchmark_section_dictionary = {
        "table2": parse_current_repository_rows(
            benchmark_line_list,
            "#### Table 2 - Amplitude MAE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table3": parse_current_repository_rows(
            benchmark_line_list,
            "#### Table 3 - Amplitude RMSE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table4": parse_current_repository_rows(
            benchmark_line_list,
            "#### Table 4 - Phase MAE Full-Matrix Replication",
            expected_row_count=10,
        ),
        "table5": parse_current_repository_rows(
            benchmark_line_list,
            "#### Table 5 - Phase RMSE Full-Matrix Replication",
            expected_row_count=10,
        ),
    }
    previous_status_dictionary = compute_benchmark_status_dictionary(benchmark_line_list)
    paper_target_dictionary = build_paper_target_dictionary(benchmark_section_dictionary)
    entry_list, _, pair_entry_list_dictionary = collect_campaign_summary_bundle(
        active_campaign_dictionary,
        paper_target_dictionary,
        validation_root,
        run_pattern,
    )
    promoted_entry_dictionary, improvement_summary_dictionary = build_promotion_bundle(
        benchmark_section_dictionary,
        paper_target_dictionary,
        pair_entry_list_dictionary,
    )

    best_run_dictionary = write_campaign_bookkeeping(active_campaign_dictionary, entry_list)
    family_best_dictionary: dict[str, dict[str, Any]] = {}
    for family_code in FAMILY_ORDER:
        family_entry_list = [entry for entry in entry_list if entry["paper_family_code"] == family_code]
        if family_entry_list:
            family_best_dictionary[family_code] = sorted(
                family_entry_list,
                key=build_selection_sort_key,
            )[0]

    report_output_path = (
        REPORT_OUTPUT_ROOT
        / f"{report_timestamp}_{campaign_profile['report_filename_suffix']}"
    )
    report_relative_path = format_project_relative_path(report_output_path)
    updated_status_dictionary = update_benchmark_report(
        benchmark_section_dictionary,
        promoted_entry_dictionary,
        report_relative_path,
        active_campaign_dictionary,
        campaign_profile,
    )
    archive_summary_list = refresh_directional_reference_archives_from_selection(
        direction_label="forward",
        selected_entry_dictionary=promoted_entry_dictionary,
        archive_note_line=str(campaign_profile["archive_note_line"]),
    )
    report_output_path.parent.mkdir(parents=True, exist_ok=True)
    report_output_path.write_text(
        build_results_report_markdown(
            report_timestamp,
            active_campaign_dictionary,
            campaign_profile,
            validation_root,
            family_best_dictionary,
            best_run_dictionary,
            improvement_summary_dictionary,
            previous_status_dictionary,
            updated_status_dictionary,
            archive_summary_list,
        ),
        encoding="utf-8",
        newline="\n",
    )
    update_active_campaign_state(
        active_campaign_dictionary,
        report_relative_path,
        str(active_campaign_dictionary["finished_at"]),
    )
    patch_master_summary(
        report_relative_path,
        active_campaign_dictionary,
        campaign_profile,
        updated_status_dictionary,
        best_run_dictionary,
    )
    print(f"[DONE] {campaign_profile['report_written_label']} | report={report_relative_path}")


if __name__ == "__main__":

    main()
