"""Close out the RCIM Model-Bank Reproduction backward paper-faithful grid-search campaign."""

from __future__ import annotations

# Import Python Utilities
import argparse
import re
import shutil
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Third-Party Utilities
import yaml

PROJECT_PATH = Path(__file__).resolve().parents[4]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.tooling import repository_path_support
from scripts.reports.closeout.track1 import closeout_track1_bidirectional_original_dataset_mega_campaign as archive_support
from scripts.training import shared_training_infrastructure

ACTIVE_CAMPAIGN_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
BENCHMARK_REPORT_PATH = (
    PROJECT_PATH / "doc" / "reports" / "analysis" / "RCIM Paper Reference Benchmark.md"
)
MASTER_SUMMARY_PATH = (
    PROJECT_PATH / "doc" / "reports" / "analysis" / "Training Results Master Summary.md"
)
PAPER_REFERENCE_ROOT_README_PATH = PROJECT_PATH / "models" / "paper_reference" / "README.md"
TRACK1_REFERENCE_ROOT = PROJECT_PATH / "models" / "paper_reference" / "rcim_track1"
TRACK1_REFERENCE_ROOT_README_PATH = TRACK1_REFERENCE_ROOT / "README.md"
TRACK1_REFERENCE_BACKWARD_ROOT = TRACK1_REFERENCE_ROOT / "backward"
MODELS_ROOT_README_PATH = PROJECT_PATH / "models" / "README.md"
VALIDATION_ROOT = (
    PROJECT_PATH / "output" / "validation_checks" / "paper_reimplementation_rcim_original_dataset_exact_model_bank"
)
REPORT_OUTPUT_ROOT = (
    PROJECT_PATH / "doc" / "reports" / "campaign_results" / "track1" / "exact_paper" / "backward"
)

PAPER_FAMILY_ORDER = ["SVM", "MLP", "RF", "DT", "ET", "ERT", "GBM", "HGBM", "XGBM", "LGBM"]
ARCHIVE_FAMILY_ORDER = [*PAPER_FAMILY_ORDER, "ELM"]
IMPLEMENTATION_TO_PAPER_FAMILY_MAP = {
    "SVR": "SVM",
    "MLP": "MLP",
    "RF": "RF",
    "DT": "DT",
    "ET": "ET",
    "ERT": "ERT",
    "GBM": "GBM",
    "HGBM": "HGBM",
    "XGBM": "XGBM",
    "LGBM": "LGBM",
    "ELM": "ELM",
}
PAPER_TO_IMPLEMENTATION_FAMILY_MAP = {
    paper_family: implementation_family
    for implementation_family, paper_family in IMPLEMENTATION_TO_PAPER_FAMILY_MAP.items()
}
FAMILY_ARCHIVE_FOLDER_MAP = {
    family_code: f"{family_code.lower()}_reference_models"
    for family_code in ARCHIVE_FAMILY_ORDER
}
AMPLITUDE_HARMONIC_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
PHASE_HARMONIC_LIST = [1, 3, 39, 40, 78, 81, 156, 162, 240]
GREEN_MARKER = "\U0001F7E2"
YELLOW_MARKER = "\U0001F7E1"
RED_MARKER = "\U0001F534"
MARKER_PREFIX_PATTERN = re.compile(r"^(?:\U0001F7E2|\U0001F7E1|\U0001F534|🟢|🟡|🔴)\s+")


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse CLI arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Close out the completed RCIM Model-Bank Reproduction backward paper-faithful grid-search campaign."
    )
    argument_parser.add_argument(
        "--finished-at",
        default="2026-05-16T19:04:25+02:00",
        help="Finished timestamp to record in campaign state and reports.",
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser.parse_args()


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | path={input_path}"
    return payload


def save_yaml_dictionary(output_path: Path, payload: dict[str, Any]) -> None:

    """Save one YAML dictionary."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=True)


def format_project_relative_path(path_value: Path | str) -> str:

    """Format one path relative to the repository root."""

    path_object = Path(path_value)
    if not path_object.is_absolute():
        return str(path_object).replace("\\", "/")
    return str(path_object.relative_to(PROJECT_PATH)).replace("\\", "/")


def resolve_project_relative_path(path_value: str | Path) -> Path:

    """Resolve one repository-relative path."""

    return shared_training_infrastructure.resolve_project_relative_path(path_value)


def parse_markdown_row(markdown_line: str) -> list[str]:

    """Parse one Markdown table row."""

    return [cell.strip() for cell in markdown_line.strip().strip("|").split("|")]


def sanitize_metric_cell(metric_cell: str) -> float:

    """Extract the numeric value from one benchmark table cell."""

    stripped_cell = metric_cell.strip().strip("`")
    stripped_cell = MARKER_PREFIX_PATTERN.sub("", stripped_cell).strip()
    return float(stripped_cell)


def format_metric_value(metric_value: float) -> str:

    """Format one metric for the benchmark tables."""

    return f"{float(metric_value):.6g}"


def resolve_status_marker(repository_value: float, paper_value: float) -> str:

    """Resolve green, yellow, or red status for one benchmark cell."""

    if float(repository_value) <= float(paper_value):
        return GREEN_MARKER
    if float(repository_value) <= float(paper_value) * 1.25:
        return YELLOW_MARKER
    return RED_MARKER


def parse_target_name(target_name: str) -> tuple[str, str, int]:

    """Parse one exact-paper target name into direction, scope, and harmonic."""

    target_pattern = re.compile(
        r"^fft_y_(?P<direction_prefix>Fw|Bw)_filtered_(?P<target_scope>ampl|phase)_(?P<harmonic>\d+)$"
    )
    match = target_pattern.match(str(target_name))
    assert match is not None, f"Unsupported target name | {target_name}"
    direction_label = "forward" if match.group("direction_prefix") == "Fw" else "backward"
    target_scope = "amplitude" if match.group("target_scope") == "ampl" else "phase"
    return direction_label, target_scope, int(match.group("harmonic"))


def build_target_name(scope_key: str, harmonic_order: int) -> str:

    """Build one backward target name."""

    target_scope = "ampl" if scope_key == "amplitude" else "phase"
    return f"fft_y_Bw_filtered_{target_scope}_{int(harmonic_order)}"


def resolve_latest_backward_summary_dictionary() -> dict[str, dict[str, Any]]:

    """Resolve the latest completed backward summary for each archive family."""

    latest_summary_dictionary: dict[str, dict[str, Any]] = {}
    for summary_path in sorted(VALIDATION_ROOT.rglob("validation_summary.yaml")):
        summary_dictionary = load_yaml_dictionary(summary_path)
        if str(summary_dictionary["dataset"]["direction_label"]) != "backward":
            continue
        run_name = str(summary_dictionary["experiment"]["run_name"])
        if not run_name.startswith("track1_paper_faithful_grid_search_backward_"):
            continue
        implementation_family = str(summary_dictionary["winner_summary"]["winning_family"])
        if implementation_family not in IMPLEMENTATION_TO_PAPER_FAMILY_MAP:
            continue
        paper_family = IMPLEMENTATION_TO_PAPER_FAMILY_MAP[implementation_family]
        current_summary = latest_summary_dictionary.get(paper_family)
        if current_summary is None:
            latest_summary_dictionary[paper_family] = {
                "summary_path": summary_path,
                "summary_dictionary": summary_dictionary,
            }
            continue
        current_run_instance_id = str(current_summary["summary_dictionary"]["experiment"]["run_instance_id"])
        candidate_run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
        if candidate_run_instance_id > current_run_instance_id:
            latest_summary_dictionary[paper_family] = {
                "summary_path": summary_path,
                "summary_dictionary": summary_dictionary,
            }

    missing_family_list = [
        family_code for family_code in ARCHIVE_FAMILY_ORDER
        if family_code not in latest_summary_dictionary
    ]
    assert not missing_family_list, (
        "Missing completed backward validation summaries | "
        f"families={missing_family_list}"
    )
    return latest_summary_dictionary


def resolve_family_export_entry(summary_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Resolve the single family export entry from one validation summary."""

    family_export_list = summary_dictionary["onnx_export_summary"]["family_exports"]
    assert len(family_export_list) == 1, "Expected one family export entry per backward family run."
    return dict(family_export_list[0])


def build_accepted_artifact_map(
    summary_bundle_dictionary: dict[str, dict[str, Any]]
) -> dict[tuple[str, str, str], archive_support.AcceptedTargetArtifact]:

    """Build accepted target artifacts for all backward paper families plus ELM."""

    accepted_artifact_map: dict[tuple[str, str, str], archive_support.AcceptedTargetArtifact] = {}
    for paper_family, summary_bundle in summary_bundle_dictionary.items():
        summary_dictionary = summary_bundle["summary_dictionary"]
        implementation_family = PAPER_TO_IMPLEMENTATION_FAMILY_MAP[paper_family]
        family_ranking_entry = summary_dictionary["family_ranking"][0]
        assert str(family_ranking_entry["family_name"]) == implementation_family
        for target_metric_entry in family_ranking_entry["target_metrics"]:
            target_name = str(target_metric_entry["target_name"])
            direction_label, _, _ = parse_target_name(target_name)
            assert direction_label == "backward", f"Expected backward target | {target_name}"
            accepted_artifact_map[(direction_label, paper_family, target_name)] = (
                archive_support.AcceptedTargetArtifact(
                    direction_label=direction_label,
                    paper_family_code=paper_family,
                    implementation_family_code=implementation_family,
                    target_name=target_name,
                    target_kind=parse_target_name(target_name)[1],
                    harmonic_order=parse_target_name(target_name)[2],
                    source_summary_path=summary_bundle["summary_path"],
                    source_summary_dictionary=summary_dictionary,
                    source_target_metric=dict(target_metric_entry),
                )
            )

    expected_target_count = len(ARCHIVE_FAMILY_ORDER) * 19
    assert len(accepted_artifact_map) == expected_target_count, (
        "Unexpected accepted target artifact count | "
        f"found={len(accepted_artifact_map)} expected={expected_target_count}"
    )
    return accepted_artifact_map


def apply_archive_support_family_extension() -> None:

    """Extend archive-support globals for the operational ELM archive."""

    if "ELM" not in archive_support.FAMILY_ORDER:
        archive_support.FAMILY_ORDER.append("ELM")
    archive_support.IMPLEMENTATION_TO_PAPER_FAMILY_MAP["ELM"] = "ELM"
    archive_support.PAPER_TO_IMPLEMENTATION_FAMILY_MAP["ELM"] = "ELM"
    archive_support.FAMILY_ARCHIVE_FOLDER_MAP["ELM"] = "elm_reference_models"


def refresh_backward_reference_archives(
    accepted_artifact_map: dict[tuple[str, str, str], archive_support.AcceptedTargetArtifact],
) -> list[dict[str, Any]]:

    """Refresh all backward family reference archives from the completed campaign."""

    apply_archive_support_family_extension()
    archive_summary_list: list[dict[str, Any]] = []
    for family_code in ARCHIVE_FAMILY_ORDER:
        archive_summary_list.append(
            archive_support.build_directional_family_archive(
                "backward",
                family_code,
                accepted_artifact_map,
                (
                    "This archive was replaced during the RCIM Model-Bank Reproduction backward "
                    "paper-faithful grid-search closeout after the exact-paper "
                    "pipeline fixes for ELM, remote sync, and search-summary serialization."
                ),
            )
        )
    write_reference_root_readmes()
    return archive_summary_list


def write_reference_root_readmes() -> None:

    """Refresh root archive README files after bidirectional RCIM Model-Bank Reproduction closeout."""

    forward_archive_line_list = [
        f"- `forward/{FAMILY_ARCHIVE_FOLDER_MAP[family_code]}/`"
        for family_code in ARCHIVE_FAMILY_ORDER
    ]
    backward_archive_line_list = [
        f"- `backward/{FAMILY_ARCHIVE_FOLDER_MAP[family_code]}/`"
        for family_code in ARCHIVE_FAMILY_ORDER
    ]
    TRACK1_REFERENCE_ROOT_README_PATH.write_text(
        "\n".join([
            "# RCIM Model-Bank Reproduction Paper Reference Models",
            "",
            "This folder groups curated paper-reference model archives for the canonical",
            "`RCIM Model-Bank Reproduction` RCIM paper-reimplementation branch.",
            "",
            "Direction branches:",
            "",
            "- `forward/`",
            "- `backward/`",
            "",
            "Current populated family archives:",
            "",
            *forward_archive_line_list,
            *backward_archive_line_list,
            "",
            "Paper-table families remain the original `10` families used by Tables `2`-`5`.",
            "`ELM` is an additional operational RCIM Model-Bank Reproduction family and is archived for both",
            "directions after the completed paper-faithful campaigns provide it.",
            "",
            "Canonical family archive template:",
            "",
            "- `<direction>/<family>_reference_models/README.md`",
            "- `<direction>/<family>_reference_models/reference_inventory.yaml`",
            "- `<direction>/<family>_reference_models/onnx/amplitude/`",
            "- `<direction>/<family>_reference_models/onnx/phase/`",
            "- `<direction>/<family>_reference_models/python/amplitude/`",
            "- `<direction>/<family>_reference_models/python/phase/`",
            "- `<direction>/<family>_reference_models/data/`",
            "- `<direction>/<family>_reference_models/dataset_snapshot_manifest.yaml`",
            "- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/training_config.snapshot.yaml`",
            "- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/run_metadata.snapshot.yaml`",
            "- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/split_manifest.yaml`",
            "",
            "Closeout rule:",
            "",
            "- every future RCIM Model-Bank Reproduction closeout must refresh the affected family-reference archive when accepted models change;",
            "- archive entries must preserve source validation summaries, training configs, run metadata, exported ONNX files, Python pickles, and dataset provenance;",
            "- direction-specific closeouts must only replace archives for the completed direction.",
            "",
        ]).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )

    (TRACK1_REFERENCE_BACKWARD_ROOT / "README.md").write_text(
        "\n".join([
            "# RCIM Model-Bank Reproduction Backward Reference Branch",
            "",
            "This branch stores the canonical backward-direction paper-reference archives",
            "rebuilt from the completed RCIM Model-Bank Reproduction backward paper-faithful grid-search campaign.",
            "",
            "Populated family archives:",
            "",
            *[f"- `{FAMILY_ARCHIVE_FOLDER_MAP[family_code]}/`" for family_code in ARCHIVE_FAMILY_ORDER],
            "",
        ]).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )

    PAPER_REFERENCE_ROOT_README_PATH.write_text(
        "\n".join([
            "# Paper Reference Models",
            "",
            "This folder stores curated repository-local copies of model artifacts used as",
            "canonical paper-reference anchors.",
            "",
            "Current topic roots:",
            "",
            "- `rcim_track1/`",
            "- `rcim_original/`",
            "- `rcim_retuned/`",
            "",
            "For `RCIM Model-Bank Reproduction` paper-reimplementation families, the canonical family package",
            "contract is:",
            "",
            "- `models/paper_reference/rcim_track1/forward/<family>_reference_models/`",
            "- `models/paper_reference/rcim_track1/backward/<family>_reference_models/`",
            "- `README.md`",
            "- `reference_inventory.yaml`",
            "- `onnx/amplitude/`",
            "- `onnx/phase/`",
            "- `python/amplitude/`",
            "- `python/phase/`",
            "- `data/`",
            "- `dataset_snapshot_manifest.yaml`",
            "- `source_runs/<run_instance_id>/training_config.snapshot.yaml`",
            "- `source_runs/<run_instance_id>/run_metadata.snapshot.yaml`",
            "- `source_runs/<run_instance_id>/split_manifest.yaml`",
            "",
            "The RCIM Model-Bank Reproduction forward and backward branches now include the operational",
            "`ELM` archive in addition to the original `10` paper-table families.",
            "",
            "Every fully curated family archive is expected to preserve:",
            "",
            "- the accepted target-level benchmark metrics;",
            "- the canonical source run per accepted target;",
            "- deployment-facing archived exports;",
            "- Python-usable fitted estimators when the training stack supports them;",
            "- dataset provenance and deterministic split reconstruction metadata.",
            "",
        ]).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )

    MODELS_ROOT_README_PATH.write_text(
        "\n".join([
            "# Model Artifact Folder",
            "",
            "This folder is reserved for trained and exported model artifacts.",
            "",
            "Suggested subfolders:",
            "",
            "- `checkpoints/` for copied or curated training checkpoints",
            "- `exported/` for ONNX, Structured Text, or other deployment-ready exports",
            "- `paper_reference/` for curated paper-baseline model archives with provenance",
            "  and reconstruction notes",
            "",
            "Project-authored Python source code no longer lives here. Source files are stored under:",
            "",
            "- `scripts/models/`",
            "- `scripts/training/`",
            "",
            "Current curated RCIM Model-Bank Reproduction paper-reference archives include:",
            "",
            *forward_archive_line_list,
            *backward_archive_line_list,
            "",
        ]).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )


def collect_table_block(line_list: list[str], heading: str, subsection: str) -> tuple[list[int], dict[str, list[str]]]:

    """Collect table row indices and cells under one benchmark subsection."""

    heading_index = line_list.index(heading)
    subsection_index = line_list.index(subsection, heading_index)
    row_index_list: list[int] = []
    row_dictionary: dict[str, list[str]] = {}
    for line_index in range(subsection_index + 1, len(line_list)):
        line_text = line_list[line_index]
        if line_text.startswith("###") or line_text.startswith("#### "):
            break
        if not line_text.startswith("| `"):
            continue
        cell_list = parse_markdown_row(line_text)
        family_code = cell_list[0].strip("`")
        row_index_list.append(line_index)
        row_dictionary[family_code] = cell_list
    return row_index_list, row_dictionary


def build_reference_threshold_dictionary(
    original_rows: dict[str, list[str]],
    retuned_rows: dict[str, list[str]],
    harmonic_list: list[int],
) -> dict[str, dict[int, float]]:

    """Build the paper-reference threshold dictionary for one forward table."""

    threshold_dictionary: dict[str, dict[int, float]] = {}
    for family_code in ARCHIVE_FAMILY_ORDER:
        threshold_dictionary[family_code] = {}
        for harmonic_index, harmonic_order in enumerate(harmonic_list):
            candidate_list: list[float] = []
            if family_code in original_rows:
                candidate_list.append(sanitize_metric_cell(original_rows[family_code][harmonic_index + 1]))
            if family_code in retuned_rows:
                candidate_list.append(sanitize_metric_cell(retuned_rows[family_code][harmonic_index + 1]))
            assert candidate_list, f"Missing reference threshold | family={family_code}"
            threshold_dictionary[family_code][int(harmonic_order)] = min(candidate_list)
    return threshold_dictionary


def update_backward_benchmark_tables(
    summary_bundle_dictionary: dict[str, dict[str, Any]],
    report_relative_path: str,
    finished_at: str,
) -> dict[str, dict[str, int]]:

    """Update backward Tables 2-5 in the RCIM benchmark report."""

    benchmark_line_list = BENCHMARK_REPORT_PATH.read_text(encoding="utf-8").splitlines()
    table_specification_list = [
        ("table2", "### Backward Table 2 - Amplitude MAE", "amplitude", "mae", AMPLITUDE_HARMONIC_LIST),
        ("table3", "### Backward Table 3 - Amplitude RMSE", "amplitude", "rmse", AMPLITUDE_HARMONIC_LIST),
        ("table4", "### Backward Table 4 - Phase MAE", "phase", "mae", PHASE_HARMONIC_LIST),
        ("table5", "### Backward Table 5 - Phase RMSE", "phase", "rmse", PHASE_HARMONIC_LIST),
    ]
    status_dictionary: dict[str, dict[str, int]] = {}

    for table_key, heading, scope_key, metric_key, harmonic_list in table_specification_list:
        _, original_rows = collect_table_block(benchmark_line_list, heading, "#### Paper Original")
        _, retuned_rows = collect_table_block(benchmark_line_list, heading, "#### Paper Retuned")
        track1_row_index_list, track1_rows = collect_table_block(benchmark_line_list, heading, "#### RCIM Model-Bank Reproduction")
        track1_row_index_map = {
            parse_markdown_row(benchmark_line_list[row_index])[0].strip("`"): row_index
            for row_index in track1_row_index_list
        }
        reference_threshold_dictionary = build_reference_threshold_dictionary(
            original_rows,
            retuned_rows,
            harmonic_list,
        )
        status_dictionary[table_key] = {"green": 0, "yellow": 0, "red": 0, "total": 0}
        for family_code in ARCHIVE_FAMILY_ORDER:
            summary_dictionary = summary_bundle_dictionary[family_code]["summary_dictionary"]
            family_metric_map = {
                str(target_metric["target_name"]): dict(target_metric)
                for target_metric in summary_dictionary["family_ranking"][0]["target_metrics"]
            }
            row_cells = [f"`{family_code}`"]
            for harmonic_order in harmonic_list:
                target_name = build_target_name(scope_key, int(harmonic_order))
                repository_value = float(family_metric_map[target_name][metric_key])
                reference_value = reference_threshold_dictionary[family_code][int(harmonic_order)]
                marker = resolve_status_marker(repository_value, reference_value)
                status_dictionary[table_key]["total"] += 1
                if marker == GREEN_MARKER:
                    status_dictionary[table_key]["green"] += 1
                elif marker == YELLOW_MARKER:
                    status_dictionary[table_key]["yellow"] += 1
                else:
                    status_dictionary[table_key]["red"] += 1
                row_cells.append(f"`{marker} {format_metric_value(repository_value)}`")
            row_index = track1_row_index_map[family_code]
            benchmark_line_list[row_index] = "| " + " | ".join(row_cells) + " |"

    current_archive_start = benchmark_line_list.index("## Current Archive Status")
    current_archive_end = next(
        index for index in range(current_archive_start + 1, len(benchmark_line_list))
        if benchmark_line_list[index].startswith("## ")
    )
    replacement_archive_status = [
        "## Current Archive Status",
        "",
        "- retuned family-direction archives promoted: `22`",
        "- RCIM Model-Bank Reproduction forward family archives refreshed: `11`",
        "- RCIM Model-Bank Reproduction backward family archives refreshed: `11`",
        "- RCIM Model-Bank Reproduction forward archive root: `models/paper_reference/rcim_track1/forward/`",
        "- RCIM Model-Bank Reproduction backward archive root: `models/paper_reference/rcim_track1/backward/`",
        "- RCIM Model-Bank Reproduction forward closeout report: `doc/reports/campaign_results/track_1/exact_paper/forward/2026-05-15-11-11-35_track1_forward_paper_faithful_grid_search_closeout_report.md`",
        f"- RCIM Model-Bank Reproduction backward closeout report: `{report_relative_path}`",
        f"- RCIM Model-Bank Reproduction backward completion timestamp: `{finished_at}`",
        "- `ELM` is archived as an operational RCIM Model-Bank Reproduction family but remains outside the original paper-family order.",
        "",
    ]
    benchmark_line_list = (
        benchmark_line_list[:current_archive_start]
        + replacement_archive_status
        + benchmark_line_list[current_archive_end:]
    )
    BENCHMARK_REPORT_PATH.write_text(
        "\n".join(benchmark_line_list).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return status_dictionary


def build_campaign_bookkeeping(
    active_campaign_dictionary: dict[str, Any],
    summary_bundle_dictionary: dict[str, dict[str, Any]],
    finished_at: str,
) -> dict[str, Any]:

    """Write campaign leaderboard and best-run artifacts."""

    campaign_output_directory = PROJECT_PATH / str(active_campaign_dictionary["campaign_output_directory"])
    leaderboard_entry_list: list[dict[str, Any]] = []
    for family_code in ARCHIVE_FAMILY_ORDER:
        summary_dictionary = summary_bundle_dictionary[family_code]["summary_dictionary"]
        winner_summary = summary_dictionary["winner_summary"]
        leaderboard_entry_list.append({
            "paper_family": family_code,
            "implementation_family": PAPER_TO_IMPLEMENTATION_FAMILY_MAP[family_code],
            "run_instance_id": str(summary_dictionary["experiment"]["run_instance_id"]),
            "run_name": str(summary_dictionary["experiment"]["run_name"]),
            "direction_label": "backward",
            "winning_mean_component_mae": float(winner_summary["winning_mean_component_mae"]),
            "winning_mean_component_rmse": float(winner_summary["winning_mean_component_rmse"]),
            "winning_mean_component_mape_percent": float(winner_summary["winning_mean_component_mape_percent"]),
            "validation_summary_path": format_project_relative_path(summary_bundle_dictionary[family_code]["summary_path"]),
            "config_path": str(summary_dictionary["config_path"]).replace("\\", "/"),
        })
    leaderboard_entry_list = sorted(
        leaderboard_entry_list,
        key=lambda entry: (
            float(entry["winning_mean_component_mae"]),
            float(entry["winning_mean_component_rmse"]),
            float(entry["winning_mean_component_mape_percent"]),
            str(entry["run_name"]),
        ),
    )
    best_entry = dict(leaderboard_entry_list[0])
    selection_policy = {
        "primary_metric": "winning_mean_component_mae_asc",
        "first_tie_breaker": "winning_mean_component_rmse_asc",
        "second_tie_breaker": "winning_mean_component_mape_percent_asc",
        "third_tie_breaker": "run_name",
    }
    save_yaml_dictionary(
        campaign_output_directory / "campaign_leaderboard.yaml",
        {
            "schema_version": 1,
            "campaign_name": str(active_campaign_dictionary["campaign_name"]),
            "generated_at": finished_at,
            "selection_policy": selection_policy,
            "entry_count": len(leaderboard_entry_list),
            "leaderboard": leaderboard_entry_list,
        },
    )
    best_entry["selected_at"] = finished_at
    best_entry["selection_policy"] = selection_policy
    save_yaml_dictionary(campaign_output_directory / "campaign_best_run.yaml", best_entry)
    (campaign_output_directory / "campaign_best_run.md").write_text(
        "\n".join([
            "# Campaign Best Run",
            "",
            f"- run instance id: `{best_entry['run_instance_id']}`",
            f"- run name: `{best_entry['run_name']}`",
            f"- paper family: `{best_entry['paper_family']}`",
            f"- implementation family: `{best_entry['implementation_family']}`",
            f"- direction label: `{best_entry['direction_label']}`",
            f"- winning mean component MAE: `{format_metric_value(best_entry['winning_mean_component_mae'])}`",
            f"- winning mean component RMSE: `{format_metric_value(best_entry['winning_mean_component_rmse'])}`",
            f"- winning mean component MAPE: `{format_metric_value(best_entry['winning_mean_component_mape_percent'])}%`",
            "",
        ]).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return best_entry


def build_closeout_report(
    report_path: Path,
    active_campaign_dictionary: dict[str, Any],
    summary_bundle_dictionary: dict[str, dict[str, Any]],
    archive_summary_list: list[dict[str, Any]],
    status_dictionary: dict[str, dict[str, int]],
    best_run_dictionary: dict[str, Any],
    finished_at: str,
) -> None:

    """Write the campaign closeout Markdown report."""

    family_lines = [
        "| Family | Run Instance | Mean MAE | Mean RMSE | Mean MAPE % | Exported ONNX | Exported PKL |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for family_code in ARCHIVE_FAMILY_ORDER:
        summary_dictionary = summary_bundle_dictionary[family_code]["summary_dictionary"]
        winner_summary = summary_dictionary["winner_summary"]
        export_summary = summary_dictionary["onnx_export_summary"]
        family_lines.append(
            "| "
            f"`{family_code}` | "
            f"`{summary_dictionary['experiment']['run_instance_id']}` | "
            f"`{format_metric_value(winner_summary['winning_mean_component_mae'])}` | "
            f"`{format_metric_value(winner_summary['winning_mean_component_rmse'])}` | "
            f"`{format_metric_value(winner_summary['winning_mean_component_mape_percent'])}` | "
            f"`{int(export_summary['onnx_exported_file_count'])}` | "
            f"`{int(export_summary['python_exported_file_count'])}` |"
        )

    status_lines = [
        "| Table | Green | Yellow | Red | Total |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for table_key, table_label in (
        ("table2", "Backward Table 2 - Amplitude MAE"),
        ("table3", "Backward Table 3 - Amplitude RMSE"),
        ("table4", "Backward Table 4 - Phase MAE"),
        ("table5", "Backward Table 5 - Phase RMSE"),
    ):
        counts = status_dictionary[table_key]
        status_lines.append(
            f"| {table_label} | `{counts['green']}` | `{counts['yellow']}` | `{counts['red']}` | `{counts['total']}` |"
        )

    archive_lines = [
        "| Family | Archived Targets | Source Runs | Archive Root |",
        "| --- | ---: | ---: | --- |",
    ]
    for archive_summary in archive_summary_list:
        archive_lines.append(
            "| "
            f"`{archive_summary['paper_family_code']}` | "
            f"`{archive_summary['reference_target_count']}` | "
            f"`{archive_summary['source_run_count']}` | "
            f"`{format_project_relative_path(archive_summary['archive_root'])}` |"
        )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        "\n".join([
            "# RCIM Model-Bank Reproduction Backward Paper-Faithful Grid-Search Closeout",
            "",
            "## Overview",
            "",
            f"- campaign name: `{active_campaign_dictionary['campaign_name']}`",
            f"- started at: `{active_campaign_dictionary['started_at']}`",
            f"- finished at: `{finished_at}`",
            "- closed direction: `backward`",
            f"- refreshed archive root: `{format_project_relative_path(TRACK1_REFERENCE_BACKWARD_ROOT)}`",
            f"- benchmark report: `{format_project_relative_path(BENCHMARK_REPORT_PATH)}`",
            "",
            "## Family Results",
            "",
            *family_lines,
            "",
            "## Benchmark Status",
            "",
            *status_lines,
            "",
            "## Reference Archive Refresh",
            "",
            *archive_lines,
            "",
            "## Best Campaign Representative",
            "",
            f"- run: `{best_run_dictionary['run_name']}`",
            f"- family: `{best_run_dictionary['paper_family']}`",
            f"- mean MAE: `{format_metric_value(best_run_dictionary['winning_mean_component_mae'])}`",
            f"- mean RMSE: `{format_metric_value(best_run_dictionary['winning_mean_component_rmse'])}`",
            "",
            "## Notes",
            "",
            "- The original paper-family order for Tables `2`-`5` remains unchanged.",
            "- `ELM` is archived and benchmarked as an operational RCIM Model-Bank Reproduction family because the completed campaign includes it.",
            "- Forward RCIM Model-Bank Reproduction paper-reference archives were not modified by this backward-only closeout.",
            "",
        ]).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )


def patch_master_summary(report_relative_path: str, status_dictionary: dict[str, dict[str, int]]) -> None:

    """Patch the RCIM Model-Bank Reproduction status block in the master summary."""

    master_summary_text = MASTER_SUMMARY_PATH.read_text(encoding="utf-8")
    replacement = "\n".join([
        "### RCIM Model-Bank Reproduction Canonical Status",
        "",
        f"- Latest exact-paper closeout report: `{report_relative_path}`",
        "- Prior forward exact-paper closeout report: `doc/reports/campaign_results/track_1/exact_paper/forward/2026-05-15-11-11-35_track1_forward_paper_faithful_grid_search_closeout_report.md`",
        "- Latest completed surface: `backward` paper-faithful grid search across `SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, LGBM, XGBM, ELM`",
        "- Table `2` `forward` status: `19` green, `25` yellow, `66` red",
        "- Table `3` `forward` status: `21` green, `28` yellow, `61` red",
        "- Table `4` `forward` status: `23` green, `21` yellow, `55` red",
        "- Table `5` `forward` status: `23` green, `32` yellow, `44` red",
        f"- Table `2` `backward` status: `{status_dictionary['table2']['green']}` green, `{status_dictionary['table2']['yellow']}` yellow, `{status_dictionary['table2']['red']}` red",
        f"- Table `3` `backward` status: `{status_dictionary['table3']['green']}` green, `{status_dictionary['table3']['yellow']}` yellow, `{status_dictionary['table3']['red']}` red",
        f"- Table `4` `backward` status: `{status_dictionary['table4']['green']}` green, `{status_dictionary['table4']['yellow']}` yellow, `{status_dictionary['table4']['red']}` red",
        f"- Table `5` `backward` status: `{status_dictionary['table5']['green']}` green, `{status_dictionary['table5']['yellow']}` yellow, `{status_dictionary['table5']['red']}` red",
        "- Forward and backward RCIM Model-Bank Reproduction Tables `2`-`5` are now populated for the completed paper-faithful campaigns.",
        "- Harmonic-wise Table `6` evidence remains postponed into `RCIM Harmonic-Wise Follow-Up` and does not gate this closeout.",
        "",
        "### Latest Harmonic-Wise Validation Support",
    ])
    master_summary_text = re.sub(
        r"### RCIM Model-Bank Reproduction Canonical Status\n.*?\n### Latest Harmonic-Wise Validation Support",
        replacement,
        master_summary_text,
        count=1,
        flags=re.DOTALL,
    )

    recent_campaign_row = (
        "| `track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30__backward_svr_mlp_rf_dt_et_ert_gbm_hgbm_lgbm_xgbm_elm_search` "
        "| `2026-05-16-19-04-25` | 11 | 0 | `backward` | Refreshed RCIM Model-Bank Reproduction backward paper-reference archives and RCIM Tables `2`-`5` |"
    )
    recent_header = "| Campaign | Generated At | Completed | Failed | Winner | Impact |"
    line_list = master_summary_text.splitlines()
    if recent_campaign_row not in line_list and recent_header in line_list:
        header_index = line_list.index(recent_header)
        line_list.insert(header_index + 2, recent_campaign_row)
        master_summary_text = "\n".join(line_list) + "\n"

    MASTER_SUMMARY_PATH.write_text(master_summary_text, encoding="utf-8", newline="\n")


def update_active_campaign_state(
    active_campaign_dictionary: dict[str, Any],
    report_relative_path: str,
    finished_at: str,
) -> None:

    """Mark the bidirectional campaign completed in active state."""

    active_campaign_dictionary["status"] = "completed"
    active_campaign_dictionary["finished_at"] = finished_at
    active_campaign_dictionary["completion_recorded_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
    active_campaign_dictionary["results_report_path"] = report_relative_path
    active_campaign_dictionary["completed_family_list"] = [
        "SVR", "MLP", "RF", "DT", "ET", "ERT", "GBM", "HGBM", "XGBM", "LGBM", "ELM"
    ]
    active_campaign_dictionary["pending_family_list"] = []
    active_campaign_dictionary["interruption_note"] = (
        "Forward and backward paper-faithful grid-search slices completed and closed out."
    )
    save_yaml_dictionary(ACTIVE_CAMPAIGN_PATH, active_campaign_dictionary)


def main() -> None:

    """Run the RCIM Model-Bank Reproduction backward paper-faithful closeout."""

    parsed_arguments = parse_command_line_arguments()
    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(parsed_arguments)
    )
    finished_at = str(parsed_arguments.finished_at)
    active_campaign_dictionary = load_yaml_dictionary(ACTIVE_CAMPAIGN_PATH)
    summary_bundle_dictionary = resolve_latest_backward_summary_dictionary()
    accepted_artifact_map = build_accepted_artifact_map(summary_bundle_dictionary)
    archive_summary_list = refresh_backward_reference_archives(accepted_artifact_map)
    report_timestamp = "2026-05-16-20-07-07"
    report_path = REPORT_OUTPUT_ROOT / f"{report_timestamp}_track1_backward_paper_faithful_grid_search_closeout_report.md"
    report_relative_path = format_project_relative_path(report_path)
    status_dictionary = update_backward_benchmark_tables(
        summary_bundle_dictionary,
        report_relative_path,
        finished_at,
    )
    best_run_dictionary = build_campaign_bookkeeping(
        active_campaign_dictionary,
        summary_bundle_dictionary,
        finished_at,
    )
    build_closeout_report(
        report_path,
        active_campaign_dictionary,
        summary_bundle_dictionary,
        archive_summary_list,
        status_dictionary,
        best_run_dictionary,
        finished_at,
    )
    patch_master_summary(report_relative_path, status_dictionary)
    update_active_campaign_state(active_campaign_dictionary, report_relative_path, finished_at)
    print(f"[DONE] RCIM Model-Bank Reproduction backward paper-faithful closeout report | {report_path}")


if __name__ == "__main__":
    main()
