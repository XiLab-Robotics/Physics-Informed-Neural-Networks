"""Close out the bidirectional original-dataset Track 1 mega campaign.

This utility reconciles the completed remote bidirectional exact-paper wave
against its canonical queue, refreshes the benchmark restart matrices, rebuilds
the `models/paper_reference/rcim_track1` archives for both directions, patches
the campaign bookkeeping artifacts, and writes the final campaign-results
report.
"""

from __future__ import annotations

# Import Python Utilities
import argparse
import hashlib
import pickle
import re
import shutil
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import Third-Party Utilities
import yaml

PROJECT_PATH = Path(__file__).resolve().parents[2]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation import exact_paper_model_bank_support
from scripts.paper_reimplementation.rcim_ml_compensation import original_dataset_exact_model_bank_support
from scripts.training import shared_training_infrastructure

ACTIVE_CAMPAIGN_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
BENCHMARK_REPORT_PATH = (
    PROJECT_PATH / "doc" / "reports" / "analysis" / "RCIM Paper Reference Benchmark.md"
)
MASTER_SUMMARY_PATH = (
    PROJECT_PATH / "doc" / "reports" / "analysis" / "Training Results Master Summary.md"
)
MODELS_ROOT_README_PATH = PROJECT_PATH / "models" / "README.md"
PAPER_REFERENCE_ROOT_README_PATH = PROJECT_PATH / "models" / "paper_reference" / "README.md"
TRACK1_REFERENCE_ROOT = PROJECT_PATH / "models" / "paper_reference" / "rcim_track1"
TRACK1_REFERENCE_ROOT_README_PATH = TRACK1_REFERENCE_ROOT / "README.md"
TRACK1_REFERENCE_FORWARD_ROOT = TRACK1_REFERENCE_ROOT / "forward"
TRACK1_REFERENCE_BACKWARD_ROOT = TRACK1_REFERENCE_ROOT / "backward"
VALIDATION_ROOT = (
    PROJECT_PATH / "output" / "validation_checks" / "paper_reimplementation_rcim_original_dataset_exact_model_bank"
)
REPORT_OUTPUT_ROOT = PROJECT_PATH / "doc" / "reports" / "campaign_results" / "track1" / "exact_paper"

FAMILY_ORDER = ["SVM", "MLP", "RF", "DT", "ET", "ERT", "GBM", "HGBM", "XGBM", "LGBM"]
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
}
PAPER_TO_IMPLEMENTATION_FAMILY_MAP = {
    paper_family: implementation_family
    for implementation_family, paper_family in IMPLEMENTATION_TO_PAPER_FAMILY_MAP.items()
}
FAMILY_ARCHIVE_FOLDER_MAP = {
    family_code: f"{family_code.lower()}_reference_models"
    for family_code in FAMILY_ORDER
}
DIRECTION_ORDER = ["forward", "backward"]
AMPLITUDE_HARMONIC_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
PHASE_HARMONIC_LIST = [1, 3, 39, 40, 78, 81, 156, 162, 240]
TABLE_HEADING_LIST = [
    "#### Table 2 - Amplitude MAE Full-Matrix Replication",
    "#### Table 3 - Amplitude RMSE Full-Matrix Replication",
    "#### Table 4 - Phase MAE Full-Matrix Replication",
    "#### Table 5 - Phase RMSE Full-Matrix Replication",
]
GREEN_MARKER = "\U0001F7E2"
YELLOW_MARKER = "\U0001F7E1"
RED_MARKER = "\U0001F534"
ARCHIVE_SECTION_START_HEADING = "### Track 1 Family Archive Standard"
ARCHIVE_SECTION_END_HEADING = "### Supporting Harmonic-Wise Offline Result"
CAMPAIGN_SELECTION_POLICY = {
    "primary_metric": "winning_mean_component_mae_asc",
    "first_tie_breaker": "winning_mean_component_rmse_asc",
    "second_tie_breaker": "winning_mean_component_mape_percent_asc",
    "third_tie_breaker": "run_name",
    "direction": "minimize_then_lexicographic",
    "note": (
        "This campaign-best representative is a bookkeeping convenience for the "
        "completed bidirectional original-dataset exact-paper mega campaign. "
        "The canonical paper-reference archive remains target-level, not run-level."
    ),
}
CAMPAIGN_BEST_RUN_SELECTION_LINES = [
    "- Primary metric: `winning_mean_component_mae_asc`",
    "- First tie-breaker: `winning_mean_component_rmse_asc`",
    "- Second tie-breaker: `winning_mean_component_mape_percent_asc`",
    "- Third tie-breaker: `run_name`",
]
MARKER_PREFIX_PATTERN = re.compile(r"^(?:🟢|🟡|🔴)\s+")
TARGET_NAME_PATTERN = re.compile(
    r"^fft_y_(?P<direction_prefix>Fw|Bw)_filtered_(?P<kind>ampl|phase)_(?P<harmonic>\d+)$"
)

VALIDATION_SUMMARY_CACHE: dict[Path, dict[str, Any]] = {}
MODEL_BUNDLE_CACHE: dict[str, dict[str, Any]] = {}
TRAINING_CONFIG_CACHE: dict[str, dict[str, Any]] = {}
ORIGINAL_DATASET_BUNDLE_CACHE: dict[str, original_dataset_exact_model_bank_support.OriginalDatasetExactModelBankBundle] = {}
DIRECTIONAL_DATASET_SNAPSHOT_CACHE: dict[str, tuple[str, dict[str, Any]]] = {}


@dataclass(frozen=True)
class AcceptedTargetArtifact:

    """Accepted target-level winner selected from the completed mega campaign."""

    direction_label: str
    paper_family_code: str
    implementation_family_code: str
    target_name: str
    target_kind: str
    harmonic_order: int
    source_summary_path: Path
    source_summary_dictionary: dict[str, Any]
    source_target_metric: dict[str, Any]


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse CLI arguments for the campaign closeout utility."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Close out the Track 1 bidirectional original-dataset exact-paper "
            "mega campaign."
        )
    )
    argument_parser.add_argument(
        "--campaign-name",
        default="",
        help=(
            "Optional explicit campaign name. When omitted, the active campaign "
            "state is used."
        ),
    )
    return argument_parser.parse_args()


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    with input_path.open("r", encoding="utf-8") as input_file:
        loaded_dictionary = yaml.safe_load(input_file)
    assert isinstance(loaded_dictionary, dict), f"Expected YAML dictionary | path={input_path}"
    return loaded_dictionary


def save_yaml_dictionary(output_path: Path, payload: dict[str, Any]) -> None:

    """Persist one YAML dictionary using repository-normalized formatting."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=True)


def format_project_relative_path(path_value: Path | str) -> str:

    """Format one path relative to the repository root."""

    return shared_training_infrastructure.format_project_relative_path(path_value)


def normalize_config_path(path_text: str | Path) -> str:

    """Normalize one config path to a slash-separated repository-relative path."""

    return str(path_text).replace("\\", "/").strip()


def normalize_yaml_value(value: Any) -> Any:

    """Convert Python and NumPy values into YAML-safe builtins."""

    if isinstance(value, dict):
        return {
            str(key): normalize_yaml_value(child_value)
            for key, child_value in value.items()
        }
    if isinstance(value, (list, tuple, set)):
        return [normalize_yaml_value(child_value) for child_value in value]
    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            return str(value)
    if isinstance(value, Path):
        return format_project_relative_path(value)
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def compute_sha256(file_path: Path) -> str:

    """Compute the SHA256 digest of one file."""

    hasher = hashlib.sha256()
    with file_path.open("rb") as input_file:
        for chunk in iter(lambda: input_file.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def format_metric_value(metric_value: float) -> str:

    """Format one floating-point metric for report-facing tables."""

    return f"{float(metric_value):.6g}"


def resolve_status_marker(repository_value: float, paper_value: float) -> str:

    """Resolve the benchmark marker for one repository-vs-paper cell."""

    if float(repository_value) <= float(paper_value):
        return GREEN_MARKER
    if float(repository_value) <= (float(paper_value) * 1.25):
        return YELLOW_MARKER
    return RED_MARKER


def parse_markdown_row(markdown_line: str) -> list[str]:

    """Parse one Markdown table row into stripped cells."""

    normalized_line = markdown_line.strip().strip("|")
    return [cell.strip() for cell in normalized_line.split("|")]


def find_line_index(line_list: list[str], expected_text: str, start_index: int = 0) -> int:

    """Find the index of one exact line."""

    for line_index in range(start_index, len(line_list)):
        if line_list[line_index].strip() == expected_text:
            return line_index
    raise RuntimeError(f"Failed to find line | text={expected_text}")


def collect_model_rows(
    line_list: list[str],
    start_index: int,
    expected_row_count: int,
) -> list[tuple[int, list[str]]]:

    """Collect family rows from one Markdown table block."""

    collected_row_list: list[tuple[int, list[str]]] = []
    for line_index in range(start_index, len(line_list)):
        current_line = line_list[line_index]
        if current_line.startswith("| `"):
            collected_row_list.append((line_index, parse_markdown_row(current_line)))
            if len(collected_row_list) == expected_row_count:
                return collected_row_list
    raise RuntimeError(
        "Failed to collect the expected model rows | "
        f"start_index={start_index} | expected_row_count={expected_row_count}"
    )


def parse_dual_direction_matrix_section(
    line_list: list[str],
    heading_text: str,
    expected_row_count: int,
) -> dict[str, Any]:

    """Parse one benchmark section with paper, forward, and backward matrices."""

    heading_index = find_line_index(line_list, heading_text)
    paper_anchor_index = find_line_index(
        line_list,
        "Paper-side repository-owned reconstruction:",
        start_index=heading_index,
    )
    forward_anchor_index = find_line_index(
        line_list,
        "Forward repository-owned restart matrix:",
        start_index=heading_index,
    )
    backward_anchor_index = find_line_index(
        line_list,
        "Backward repository-owned restart matrix:",
        start_index=heading_index,
    )

    paper_header_index = next(
        line_index
        for line_index in range(paper_anchor_index, len(line_list))
        if line_list[line_index].startswith("| Model |")
    )
    forward_header_index = next(
        line_index
        for line_index in range(forward_anchor_index, len(line_list))
        if line_list[line_index].startswith("| Model |")
    )
    backward_header_index = next(
        line_index
        for line_index in range(backward_anchor_index, len(line_list))
        if line_list[line_index].startswith("| Model |")
    )

    header_cell_list = parse_markdown_row(line_list[paper_header_index])
    assert header_cell_list == parse_markdown_row(line_list[forward_header_index])
    assert header_cell_list == parse_markdown_row(line_list[backward_header_index])
    harmonic_list = [int(cell.strip("`")) for cell in header_cell_list[1:]]

    paper_row_list = collect_model_rows(line_list, paper_anchor_index, expected_row_count)
    forward_row_list = collect_model_rows(line_list, forward_anchor_index, expected_row_count)
    backward_row_list = collect_model_rows(line_list, backward_anchor_index, expected_row_count)

    paper_row_dictionary: dict[str, dict[int, float]] = {}
    forward_row_index_map: dict[str, int] = {}
    backward_row_index_map: dict[str, int] = {}

    for _, paper_row in paper_row_list:
        family_code = paper_row[0].strip("`")
        paper_row_dictionary[family_code] = {
            harmonic_order: float(paper_cell)
            for harmonic_order, paper_cell in zip(harmonic_list, paper_row[1:], strict=True)
        }
    for row_index, forward_row in forward_row_list:
        family_code = forward_row[0].strip("`")
        forward_row_index_map[family_code] = row_index
    for row_index, backward_row in backward_row_list:
        family_code = backward_row[0].strip("`")
        backward_row_index_map[family_code] = row_index

    return {
        "heading_index": heading_index,
        "harmonic_list": harmonic_list,
        "paper_rows": paper_row_dictionary,
        "forward_row_index_map": forward_row_index_map,
        "backward_row_index_map": backward_row_index_map,
    }


def load_active_campaign_state() -> dict[str, Any]:

    """Load the canonical active campaign state."""

    return load_yaml_dictionary(ACTIVE_CAMPAIGN_PATH)


def collect_validation_summary_path_list() -> list[Path]:

    """Collect all original-dataset validation-summary paths."""

    return sorted(VALIDATION_ROOT.rglob("validation_summary.yaml"))


def load_validation_summary(summary_path: Path) -> dict[str, Any]:

    """Load one cached validation summary."""

    if summary_path not in VALIDATION_SUMMARY_CACHE:
        VALIDATION_SUMMARY_CACHE[summary_path] = load_yaml_dictionary(summary_path)
    return VALIDATION_SUMMARY_CACHE[summary_path]


def collect_campaign_summary_bundle(
    active_campaign_dictionary: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Path]]:

    """Collect and validate the exact set of summaries for the active wave."""

    queue_config_path_list = [
        normalize_config_path(config_path)
        for config_path in active_campaign_dictionary["queue_config_path_list"]
    ]
    summary_path_map: dict[str, Path] = {}
    summary_dictionary_list: list[dict[str, Any]] = []
    for summary_path in collect_validation_summary_path_list():
        summary_dictionary = load_validation_summary(summary_path)
        config_path = normalize_config_path(summary_dictionary.get("config_path", ""))
        if config_path not in queue_config_path_list:
            continue
        summary_path_map[config_path] = summary_path
        summary_dictionary_list.append(summary_dictionary)

    missing_config_path_list = sorted(
        config_path
        for config_path in queue_config_path_list
        if config_path not in summary_path_map
    )
    assert not missing_config_path_list, (
        "Campaign queue is missing validation summaries | "
        f"missing_count={len(missing_config_path_list)} | first_missing={missing_config_path_list[:5]}"
    )
    assert len(summary_dictionary_list) == len(queue_config_path_list), (
        "Resolved validation-summary count does not match queue size | "
        f"summary_count={len(summary_dictionary_list)} | queue_count={len(queue_config_path_list)}"
    )
    return summary_dictionary_list, summary_path_map


def parse_target_name(target_name: str) -> tuple[str, str, int]:

    """Parse one directional exact-paper target name."""

    target_name_match = TARGET_NAME_PATTERN.match(target_name)
    assert target_name_match is not None, f"Unsupported target name format | {target_name}"
    direction_prefix = str(target_name_match.group("direction_prefix"))
    kind_slug = str(target_name_match.group("kind"))
    harmonic_order = int(target_name_match.group("harmonic"))
    direction_label = "forward" if direction_prefix == "Fw" else "backward"
    target_kind = "amplitude" if kind_slug == "ampl" else "phase"
    return direction_label, target_kind, harmonic_order


def build_run_sort_key(summary_dictionary: dict[str, Any]) -> tuple[float, float, float, str]:

    """Build the run-level sorting key for campaign-best bookkeeping."""

    winner_summary = summary_dictionary["winner_summary"]
    return (
        float(winner_summary["winning_mean_component_mae"]),
        float(winner_summary["winning_mean_component_rmse"]),
        float(winner_summary["winning_mean_component_mape_percent"]),
        str(summary_dictionary["experiment"]["run_name"]),
    )


def build_target_sort_key(target_metric_entry: dict[str, Any], run_name: str) -> tuple[float, float, float, str]:

    """Build the target-level canonical selection key."""

    return (
        float(target_metric_entry["mae"]),
        float(target_metric_entry["rmse"]),
        float(target_metric_entry["mape_percent"]),
        run_name,
    )


def build_accepted_target_artifact_map(
    summary_dictionary_list: list[dict[str, Any]],
    summary_path_map: dict[str, Path],
) -> dict[tuple[str, str, str], AcceptedTargetArtifact]:

    """Select the accepted best artifact for every direction/family/target tuple."""

    accepted_target_artifact_map: dict[tuple[str, str, str], AcceptedTargetArtifact] = {}
    for summary_dictionary in summary_dictionary_list:
        source_summary_path = summary_path_map[
            normalize_config_path(summary_dictionary["config_path"])
        ]
        run_name = str(summary_dictionary["experiment"]["run_name"])
        winning_family_code = str(summary_dictionary["winner_summary"]["winning_family"])
        paper_family_code = IMPLEMENTATION_TO_PAPER_FAMILY_MAP[winning_family_code]
        family_ranking_entry = summary_dictionary["family_ranking"][0]
        for target_metric_entry in family_ranking_entry["target_metrics"]:
            target_name = str(target_metric_entry["target_name"])
            direction_label, target_kind, harmonic_order = parse_target_name(target_name)
            artifact_key = (direction_label, paper_family_code, target_name)
            candidate_artifact = AcceptedTargetArtifact(
                direction_label=direction_label,
                paper_family_code=paper_family_code,
                implementation_family_code=winning_family_code,
                target_name=target_name,
                target_kind=target_kind,
                harmonic_order=harmonic_order,
                source_summary_path=source_summary_path,
                source_summary_dictionary=summary_dictionary,
                source_target_metric=target_metric_entry,
            )
            current_artifact = accepted_target_artifact_map.get(artifact_key)
            if current_artifact is None:
                accepted_target_artifact_map[artifact_key] = candidate_artifact
                continue
            current_sort_key = build_target_sort_key(
                current_artifact.source_target_metric,
                str(current_artifact.source_summary_dictionary["experiment"]["run_name"]),
            )
            candidate_sort_key = build_target_sort_key(target_metric_entry, run_name)
            if candidate_sort_key < current_sort_key:
                accepted_target_artifact_map[artifact_key] = candidate_artifact

    expected_target_count = len(DIRECTION_ORDER) * len(FAMILY_ORDER) * 19
    assert len(accepted_target_artifact_map) == expected_target_count, (
        "Unexpected accepted target count for the bidirectional exact closeout | "
        f"found={len(accepted_target_artifact_map)} | expected={expected_target_count}"
    )
    return accepted_target_artifact_map


def update_benchmark_restart_matrices(
    accepted_target_artifact_map: dict[tuple[str, str, str], AcceptedTargetArtifact]
) -> tuple[dict[str, Any], dict[str, Any]]:

    """Refresh the bidirectional benchmark restart matrices in-place."""

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

    benchmark_status_dictionary: dict[str, Any] = {}
    direction_family_metric_dictionary: dict[str, Any] = defaultdict(lambda: defaultdict(dict))
    for table_key, section_dictionary in section_dictionary_map.items():
        benchmark_status_dictionary[table_key] = {}
        metric_name = "mae" if table_key in {"table2", "table4"} else "rmse"
        target_kind = "amplitude" if table_key in {"table2", "table3"} else "phase"

        harmonic_list = AMPLITUDE_HARMONIC_LIST if target_kind == "amplitude" else PHASE_HARMONIC_LIST
        for direction_label in DIRECTION_ORDER:
            row_index_map = section_dictionary[f"{direction_label}_row_index_map"]
            benchmark_status_dictionary[table_key][direction_label] = {
                "green": 0,
                "yellow": 0,
                "red": 0,
                "total": 0,
            }
            for paper_family_code in FAMILY_ORDER:
                paper_value_map = section_dictionary["paper_rows"][paper_family_code]
                row_index = row_index_map[paper_family_code]
                row_cell_list = [f"`{paper_family_code}`"]
                for harmonic_order in harmonic_list:
                    target_name = (
                        f"fft_y_{'Fw' if direction_label == 'forward' else 'Bw'}_filtered_"
                        f"{'ampl' if target_kind == 'amplitude' else 'phase'}_{harmonic_order}"
                    )
                    accepted_target_artifact = accepted_target_artifact_map[
                        (direction_label, paper_family_code, target_name)
                    ]
                    repository_value = float(
                        accepted_target_artifact.source_target_metric[metric_name]
                    )
                    paper_value = float(paper_value_map[harmonic_order])
                    marker = resolve_status_marker(repository_value, paper_value)
                    benchmark_status_dictionary[table_key][direction_label]["total"] += 1
                    if marker == GREEN_MARKER:
                        benchmark_status_dictionary[table_key][direction_label]["green"] += 1
                    elif marker == YELLOW_MARKER:
                        benchmark_status_dictionary[table_key][direction_label]["yellow"] += 1
                    else:
                        benchmark_status_dictionary[table_key][direction_label]["red"] += 1
                    row_cell_list.append(f"`{marker} {format_metric_value(repository_value)}`")
                    direction_family_metric_dictionary[direction_label][paper_family_code][target_name] = {
                        "mae": float(accepted_target_artifact.source_target_metric["mae"]),
                        "rmse": float(accepted_target_artifact.source_target_metric["rmse"]),
                    }
                benchmark_line_list[row_index] = (
                    "| " + " | ".join(row_cell_list) + " |"
                )

    benchmark_line_list = refresh_track1_archive_standard_and_family_sections(
        benchmark_line_list,
        accepted_target_artifact_map,
    )
    BENCHMARK_REPORT_PATH.write_text(
        "\n".join(benchmark_line_list).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return benchmark_status_dictionary, direction_family_metric_dictionary


def build_family_reference_section_lines(
    paper_family_code: str,
    accepted_target_artifact_map: dict[tuple[str, str, str], AcceptedTargetArtifact],
) -> list[str]:

    """Build one compact benchmark section for one family archive pair."""

    archive_folder_name = FAMILY_ARCHIVE_FOLDER_MAP[paper_family_code]
    implementation_family_code = PAPER_TO_IMPLEMENTATION_FAMILY_MAP[paper_family_code]
    line_list = [
        f"### {paper_family_code} Reference Model Inventory",
        "",
        f"The accepted repository-owned `{paper_family_code}` row is now pinned to explicit curated",
        "directional archives rebuilt from the completed original-dataset exact-paper mega",
        "campaign.",
        "",
        "<!-- markdownlint-disable MD013 -->",
        f"- forward archive root: `models/paper_reference/rcim_track1/forward/{archive_folder_name}`",
        f"- backward archive root: `models/paper_reference/rcim_track1/backward/{archive_folder_name}`",
        f"- forward machine-readable inventory: `models/paper_reference/rcim_track1/forward/{archive_folder_name}/reference_inventory.yaml`",
        f"- backward machine-readable inventory: `models/paper_reference/rcim_track1/backward/{archive_folder_name}/reference_inventory.yaml`",
        f"- forward dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/{archive_folder_name}/dataset_snapshot_manifest.yaml`",
        f"- backward dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/{archive_folder_name}/dataset_snapshot_manifest.yaml`",
        "",
        "Selection rule:",
        "",
        "- for each direction and target, the canonical archive promotes the attempt with the lowest `MAE`;",
        "- ties break on lower `RMSE`, then lower target `MAPE`, then lexicographically earlier run name;",
        "- every future closeout must refresh the archive only when the accepted target winner improves over the stored archive entry.",
        "",
        "Important implementation note:",
        "",
        f"- paper family name: `{paper_family_code}`",
        f"- repository implementation family: `{implementation_family_code}`",
        "- workflow scope: `original_dataset_directional_exact_model_bank`",
        "- both directions archive deployment-facing `ONNX` exports and Python-usable fitted estimator pickles.",
        "",
        "Accepted directional target coverage:",
        "",
        "| Direction | Target Count | Amplitude Harmonics | Phase Harmonics |",
        "| --- | ---: | --- | --- |",
        f"| `forward` | `19` | `{', '.join(str(harmonic_order) for harmonic_order in AMPLITUDE_HARMONIC_LIST)}` | `{', '.join(str(harmonic_order) for harmonic_order in PHASE_HARMONIC_LIST)}` |",
        f"| `backward` | `19` | `{', '.join(str(harmonic_order) for harmonic_order in AMPLITUDE_HARMONIC_LIST)}` | `{', '.join(str(harmonic_order) for harmonic_order in PHASE_HARMONIC_LIST)}` |",
        "",
        "Directional archive snapshot:",
        "",
        "| Direction | Unique Source Runs | Representative Source Config |",
        "| --- | ---: | --- |",
    ]
    for direction_label in DIRECTION_ORDER:
        target_artifact_list = [
            accepted_target_artifact_map[(direction_label, paper_family_code, target_name)]
            for target_name in sorted(
                artifact.target_name
                for artifact_key, artifact in accepted_target_artifact_map.items()
                if artifact_key[0] == direction_label and artifact_key[1] == paper_family_code
            )
        ]
        source_run_name_list = sorted(
            {
                str(target_artifact.source_summary_dictionary["experiment"]["run_instance_id"])
                for target_artifact in target_artifact_list
            }
        )
        representative_source_config = str(
            target_artifact_list[0].source_summary_dictionary["config_path"]
        ).replace("\\", "/")
        line_list.append(
            f"| `{direction_label}` | `{len(source_run_name_list)}` | `{representative_source_config}` |"
        )
    line_list.extend([
        "<!-- markdownlint-enable MD013 -->",
        "",
    ])
    return line_list


def refresh_track1_archive_standard_and_family_sections(
    benchmark_line_list: list[str],
    accepted_target_artifact_map: dict[tuple[str, str, str], AcceptedTargetArtifact],
) -> list[str]:

    """Replace the stale forward-only archive block with a bidirectional compact block."""

    start_index = find_line_index(benchmark_line_list, ARCHIVE_SECTION_START_HEADING)
    end_index = find_line_index(benchmark_line_list, ARCHIVE_SECTION_END_HEADING, start_index=start_index)

    replacement_line_list = [
        "### Track 1 Family Archive Standard",
        "",
        "The repository now treats curated `Track 1` family archives as canonical",
        "benchmark assets rather than optional side notes.",
        "",
        "Every family that reaches archive-grade `Track 1` closure now follows the",
        "same bidirectional package contract under `models/paper_reference/rcim_track1/`:",
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
        "Closeout governance rule:",
        "",
        "- every future accepted `Track 1` closeout must compare the newly accepted target winner against the archived target entry already stored under `models/paper_reference/rcim_track1/`;",
        "- when the new closeout improves the accepted target winner, the archive entry must be replaced together with its provenance snapshots, dataset snapshot manifest, and benchmark references;",
        "- when the accepted target winner does not improve, the existing archive entry must be retained unchanged to avoid unnecessary canonical churn.",
        "",
        "Planned family rollout under this standard:",
        "",
        *[f"- `{family_code}`" for family_code in FAMILY_ORDER],
        "",
        "The bidirectional original-dataset restart wave is the first closeout that",
        "materializes both `forward` and `backward` archive branches under this",
        "standard.",
        "",
    ]
    for paper_family_code in FAMILY_ORDER:
        replacement_line_list.extend(
            build_family_reference_section_lines(
                paper_family_code,
                accepted_target_artifact_map,
            )
        )

    return benchmark_line_list[:start_index] + replacement_line_list + benchmark_line_list[end_index:]


def resolve_family_export_target_entry(
    summary_dictionary: dict[str, Any],
    implementation_family_code: str,
    target_name: str,
) -> dict[str, Any]:

    """Resolve one ONNX export entry for one family target."""

    onnx_export_summary = summary_dictionary["onnx_export_summary"]
    for family_export_entry in onnx_export_summary["family_exports"]:
        if str(family_export_entry["family_name"]) != implementation_family_code:
            continue
        for export_target_entry in family_export_entry["exported_targets"]:
            if str(export_target_entry["target_name"]) == target_name:
                return export_target_entry
    raise AssertionError(
        "Missing ONNX export target entry | "
        f"family={implementation_family_code} | target={target_name}"
    )


def load_model_bundle(summary_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Load one cached original-dataset family model bundle."""

    run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
    if run_instance_id not in MODEL_BUNDLE_CACHE:
        model_bundle_path = shared_training_infrastructure.resolve_project_relative_path(
            summary_dictionary["artifacts"]["model_bundle_path"]
        )
        with model_bundle_path.open("rb") as input_file:
            model_bundle = pickle.load(input_file)
        assert isinstance(model_bundle, dict), "Expected family model bundle to be a dictionary."
        MODEL_BUNDLE_CACHE[run_instance_id] = model_bundle
    return MODEL_BUNDLE_CACHE[run_instance_id]


def resolve_training_config_dictionary(summary_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Resolve the cached training-config snapshot for one source run."""

    run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
    if run_instance_id not in TRAINING_CONFIG_CACHE:
        output_directory = shared_training_infrastructure.resolve_project_relative_path(
            summary_dictionary["experiment"]["output_directory"]
        )
        TRAINING_CONFIG_CACHE[run_instance_id] = load_yaml_dictionary(
            output_directory / "training_config.yaml"
        )
    return TRAINING_CONFIG_CACHE[run_instance_id]


def resolve_original_dataset_bundle(
    summary_dictionary: dict[str, Any],
) -> original_dataset_exact_model_bank_support.OriginalDatasetExactModelBankBundle:

    """Rebuild and cache the original-dataset exact bundle for one source run."""

    run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
    if run_instance_id not in ORIGINAL_DATASET_BUNDLE_CACHE:
        training_config = resolve_training_config_dictionary(summary_dictionary)
        ORIGINAL_DATASET_BUNDLE_CACHE[run_instance_id] = (
            original_dataset_exact_model_bank_support.build_original_dataset_exact_model_bank_bundle(
                training_config
            )
        )
    return ORIGINAL_DATASET_BUNDLE_CACHE[run_instance_id]


def resolve_target_estimator(
    summary_dictionary: dict[str, Any],
    implementation_family_code: str,
    target_name: str,
) -> Any:

    """Resolve one fitted per-target estimator from the model bundle."""

    model_bundle = load_model_bundle(summary_dictionary)
    wrapped_estimator = model_bundle[implementation_family_code]
    target_name_list = list(summary_dictionary["dataset"]["target_name_list"])
    target_index = target_name_list.index(target_name)
    return wrapped_estimator.estimators_[target_index]


def copy_file(source_path: Path, destination_path: Path) -> None:

    """Copy one file while ensuring the destination parent exists."""

    assert source_path.exists(), f"Source file does not exist | {source_path}"
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, destination_path)


def prepare_archive_root(archive_root: Path) -> None:

    """Create a clean archive root for one directional family archive."""

    if archive_root.exists():
        shutil.rmtree(archive_root)
    (archive_root / "onnx" / "amplitude").mkdir(parents=True, exist_ok=True)
    (archive_root / "onnx" / "phase").mkdir(parents=True, exist_ok=True)
    (archive_root / "python" / "amplitude").mkdir(parents=True, exist_ok=True)
    (archive_root / "python" / "phase").mkdir(parents=True, exist_ok=True)
    (archive_root / "data").mkdir(parents=True, exist_ok=True)
    (archive_root / "source_runs").mkdir(parents=True, exist_ok=True)


def build_directional_dataset_snapshot_bundle(
    reference_direction_label: str,
    reference_summary_dictionary: dict[str, Any],
) -> tuple[str, dict[str, Any]]:

    """Build the canonical dataset snapshot CSV and manifest for one direction."""

    if reference_direction_label in DIRECTIONAL_DATASET_SNAPSHOT_CACHE:
        cached_snapshot_text, cached_manifest_dictionary = DIRECTIONAL_DATASET_SNAPSHOT_CACHE[
            reference_direction_label
        ]
        return cached_snapshot_text, dict(cached_manifest_dictionary)

    original_dataset_bundle = resolve_original_dataset_bundle(reference_summary_dictionary)
    full_dataframe = original_dataset_bundle.exact_dataset_bundle.full_dataframe.copy()
    dataset_snapshot_text = full_dataframe.to_csv(
        index=True,
        index_label="filtered_row_index",
        lineterminator="\n",
    )
    dataset_snapshot_sha256 = hashlib.sha256(dataset_snapshot_text.encode("utf-8")).hexdigest()
    manifest_dictionary = {
        "schema_version": 1,
        "dataset_snapshot_path": (
            "models/paper_reference/rcim_track1/"
            f"{reference_direction_label}/<family>_reference_models/data/filtered_dataframe_deg_le_35.csv"
        ),
        "dataset_snapshot_sha256": dataset_snapshot_sha256,
        "source_dataset_root": format_project_relative_path(original_dataset_bundle.dataset_root),
        "source_dataset_config_path": format_project_relative_path(
            original_dataset_bundle.dataset_config_path
        ),
        "direction_label": reference_direction_label,
        "filtered_row_count": int(len(full_dataframe)),
        "feature_name_list": list(original_dataset_bundle.exact_dataset_bundle.feature_name_list),
        "target_name_list": list(original_dataset_bundle.exact_dataset_bundle.target_name_list),
        "selected_harmonic_list": [int(harmonic_order) for harmonic_order in original_dataset_bundle.selected_harmonic_list],
        "decomposition_point_stride": int(original_dataset_bundle.decomposition_point_stride),
        "train_row_count": int(original_dataset_bundle.split_row_count_dictionary["train"]),
        "validation_row_count": int(original_dataset_bundle.split_row_count_dictionary["validation"]),
        "test_row_count": int(original_dataset_bundle.split_row_count_dictionary["test"]),
        "train_file_count": int(original_dataset_bundle.split_file_count_dictionary["train"]),
        "validation_file_count": int(original_dataset_bundle.split_file_count_dictionary["validation"]),
        "test_file_count": int(original_dataset_bundle.split_file_count_dictionary["test"]),
        "validation_split": float(
            reference_summary_dictionary["dataset"]["validation_split"]
        ),
        "test_size": float(reference_summary_dictionary["dataset"]["test_size"]),
        "random_seed": int(reference_summary_dictionary["dataset"]["random_seed"]),
        "smoke_settings": dict(original_dataset_bundle.smoke_settings),
    }
    DIRECTIONAL_DATASET_SNAPSHOT_CACHE[reference_direction_label] = (
        dataset_snapshot_text,
        dict(manifest_dictionary),
    )
    return dataset_snapshot_text, manifest_dictionary


def build_directional_split_manifest_dictionary(
    archive_root: Path,
    summary_dictionary: dict[str, Any],
    dataset_manifest_dictionary: dict[str, Any],
) -> dict[str, Any]:

    """Build one deterministic source-run manifest for the original-dataset branch."""

    run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
    return {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "source_validation_summary_path": format_project_relative_path(
            shared_training_infrastructure.resolve_project_relative_path(
                summary_dictionary["artifacts"]["validation_summary_path"]
            )
        ),
        "source_training_config_path": format_project_relative_path(
            shared_training_infrastructure.resolve_project_relative_path(
                summary_dictionary["experiment"]["output_directory"]
            )
            / "training_config.yaml"
        ),
        "source_run_metadata_path": format_project_relative_path(
            shared_training_infrastructure.resolve_project_relative_path(
                summary_dictionary["experiment"]["output_directory"]
            )
            / "run_metadata.yaml"
        ),
        "source_model_bundle_path": format_project_relative_path(
            shared_training_infrastructure.resolve_project_relative_path(
                summary_dictionary["artifacts"]["model_bundle_path"]
            )
        ),
        "dataset_snapshot_path": format_project_relative_path(
            archive_root / "data" / "filtered_dataframe_deg_le_35.csv"
        ),
        "dataset_snapshot_sha256": str(dataset_manifest_dictionary["dataset_snapshot_sha256"]),
        "source_dataset_root": str(dataset_manifest_dictionary["source_dataset_root"]),
        "source_dataset_config_path": str(dataset_manifest_dictionary["source_dataset_config_path"]),
        "direction_label": str(dataset_manifest_dictionary["direction_label"]),
        "feature_name_list": list(dataset_manifest_dictionary["feature_name_list"]),
        "target_name_list": list(dataset_manifest_dictionary["target_name_list"]),
        "selected_harmonic_list": list(dataset_manifest_dictionary["selected_harmonic_list"]),
        "decomposition_point_stride": int(dataset_manifest_dictionary["decomposition_point_stride"]),
        "filtered_row_count": int(dataset_manifest_dictionary["filtered_row_count"]),
        "train_row_count": int(dataset_manifest_dictionary["train_row_count"]),
        "validation_row_count": int(dataset_manifest_dictionary["validation_row_count"]),
        "test_row_count": int(dataset_manifest_dictionary["test_row_count"]),
        "train_file_count": int(dataset_manifest_dictionary["train_file_count"]),
        "validation_file_count": int(dataset_manifest_dictionary["validation_file_count"]),
        "test_file_count": int(dataset_manifest_dictionary["test_file_count"]),
        "validation_split": float(dataset_manifest_dictionary["validation_split"]),
        "test_size": float(dataset_manifest_dictionary["test_size"]),
        "random_seed": int(dataset_manifest_dictionary["random_seed"]),
        "smoke_settings": dict(dataset_manifest_dictionary["smoke_settings"]),
        "config_path": str(summary_dictionary["config_path"]).replace("\\", "/"),
        "validation_feature_row_count": int(summary_dictionary["dataset"]["validation_row_count"]),
        "validation_target_row_count": int(summary_dictionary["dataset"]["validation_row_count"]),
    }


def build_directional_family_archive(
    direction_label: str,
    paper_family_code: str,
    accepted_target_artifact_map: dict[tuple[str, str, str], AcceptedTargetArtifact],
) -> dict[str, Any]:

    """Build one complete directional family archive."""

    implementation_family_code = PAPER_TO_IMPLEMENTATION_FAMILY_MAP[paper_family_code]
    archive_folder_name = FAMILY_ARCHIVE_FOLDER_MAP[paper_family_code]
    archive_root = (
        (TRACK1_REFERENCE_FORWARD_ROOT if direction_label == "forward" else TRACK1_REFERENCE_BACKWARD_ROOT)
        / archive_folder_name
    )
    print(
        "[INFO] Refreshing directional family archive | "
        f"direction={direction_label} | family={paper_family_code}"
    )
    prepare_archive_root(archive_root)

    reference_target_artifact_list = [
        accepted_target_artifact_map[(direction_label, paper_family_code, target_name)]
        for target_name in sorted(
            artifact.target_name
            for artifact_key, artifact in accepted_target_artifact_map.items()
            if artifact_key[0] == direction_label and artifact_key[1] == paper_family_code
        )
    ]
    reference_summary_dictionary = reference_target_artifact_list[0].source_summary_dictionary
    dataset_snapshot_text, dataset_manifest_dictionary = build_directional_dataset_snapshot_bundle(
        direction_label,
        reference_summary_dictionary,
    )
    dataset_snapshot_output_path = archive_root / "data" / "filtered_dataframe_deg_le_35.csv"
    dataset_snapshot_output_path.write_text(
        dataset_snapshot_text,
        encoding="utf-8",
        newline="\n",
    )
    dataset_manifest_dictionary["dataset_snapshot_path"] = format_project_relative_path(
        dataset_snapshot_output_path
    )
    save_yaml_dictionary(
        archive_root / "dataset_snapshot_manifest.yaml",
        normalize_yaml_value(dataset_manifest_dictionary),
    )

    all_reference_model_entry_list: list[dict[str, Any]] = []
    source_run_id_set: set[str] = set()
    source_config_path_set: set[str] = set()
    for target_artifact in reference_target_artifact_list:
        summary_dictionary = target_artifact.source_summary_dictionary
        run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
        output_directory = shared_training_infrastructure.resolve_project_relative_path(
            summary_dictionary["experiment"]["output_directory"]
        )
        source_run_root = archive_root / "source_runs" / run_instance_id
        training_config_path = output_directory / "training_config.yaml"
        run_metadata_path = output_directory / "run_metadata.yaml"
        split_manifest_path = source_run_root / "split_manifest.yaml"
        export_target_entry = resolve_family_export_target_entry(
            summary_dictionary,
            implementation_family_code,
            target_artifact.target_name,
        )
        source_export_path = shared_training_infrastructure.resolve_project_relative_path(
            export_target_entry["export_path"]
        )
        archived_onnx_path = (
            archive_root
            / "onnx"
            / target_artifact.target_kind
            / source_export_path.name
        )
        copy_file(source_export_path, archived_onnx_path)

        target_estimator = resolve_target_estimator(
            summary_dictionary,
            implementation_family_code,
            target_artifact.target_name,
        )
        python_filename = (
            f"{type(target_estimator).__name__}_"
            f"{str(export_target_entry['export_target_name'])}.pkl"
        )
        archived_python_path = (
            archive_root
            / "python"
            / target_artifact.target_kind
            / python_filename
        )
        with archived_python_path.open("wb") as output_file:
            pickle.dump(target_estimator, output_file, protocol=5)

        copy_file(training_config_path, source_run_root / "training_config.snapshot.yaml")
        copy_file(run_metadata_path, source_run_root / "run_metadata.snapshot.yaml")
        split_manifest_dictionary = build_directional_split_manifest_dictionary(
            archive_root,
            summary_dictionary,
            dataset_manifest_dictionary,
        )
        save_yaml_dictionary(split_manifest_path, normalize_yaml_value(split_manifest_dictionary))

        reference_model_entry = {
            "target_name": target_artifact.target_name,
            "target_kind": target_artifact.target_kind,
            "harmonic_order": int(target_artifact.harmonic_order),
            "direction_label": direction_label,
            "benchmark_mae": float(target_artifact.source_target_metric["mae"]),
            "benchmark_rmse": float(target_artifact.source_target_metric["rmse"]),
            "source_run_instance_id": run_instance_id,
            "source_config_path": str(summary_dictionary["config_path"]).replace("\\", "/"),
            "source_export_path": format_project_relative_path(source_export_path),
            "archived_model_path": format_project_relative_path(archived_onnx_path),
            "export_estimator_name": str(export_target_entry["export_estimator_name"]),
            "surrogate_strategy": str(export_target_entry["surrogate_strategy"]),
            "source_validation_summary_path": format_project_relative_path(
                shared_training_infrastructure.resolve_project_relative_path(
                    summary_dictionary["artifacts"]["validation_summary_path"]
                )
            ),
            "source_training_config_snapshot_path": format_project_relative_path(
                source_run_root / "training_config.snapshot.yaml"
            ),
            "source_run_metadata_snapshot_path": format_project_relative_path(
                source_run_root / "run_metadata.snapshot.yaml"
            ),
            "source_model_bundle_path": format_project_relative_path(
                shared_training_infrastructure.resolve_project_relative_path(
                    summary_dictionary["artifacts"]["model_bundle_path"]
                )
            ),
            "split_manifest_path": format_project_relative_path(split_manifest_path),
            "dataset_snapshot_path": format_project_relative_path(dataset_snapshot_output_path),
            "dataset_snapshot_sha256": str(dataset_manifest_dictionary["dataset_snapshot_sha256"]),
            "python_model_path": format_project_relative_path(archived_python_path),
            "python_model_serialization": "pickle_protocol_5",
            "python_estimator_class_name": type(target_estimator).__name__,
            "python_model_sha256": compute_sha256(archived_python_path),
            "archived_model_sha256": compute_sha256(archived_onnx_path),
            "feature_name_list": list(summary_dictionary["dataset"]["feature_name_list"]),
            "source_run_target_name_list": list(summary_dictionary["dataset"]["target_name_list"]),
            "filtered_row_count": int(summary_dictionary["dataset"]["filtered_row_count"]),
            "train_row_count": int(summary_dictionary["dataset"]["train_row_count"]),
            "validation_row_count": int(summary_dictionary["dataset"]["validation_row_count"]),
            "test_row_count": int(summary_dictionary["dataset"]["test_row_count"]),
            "train_file_count": int(summary_dictionary["dataset"]["train_file_count"]),
            "validation_file_count": int(summary_dictionary["dataset"]["validation_file_count"]),
            "test_file_count": int(summary_dictionary["dataset"]["test_file_count"]),
            "test_size": float(summary_dictionary["dataset"]["test_size"]),
            "random_seed": int(summary_dictionary["dataset"]["random_seed"]),
            "selected_harmonic_list": list(summary_dictionary["dataset"]["selected_harmonic_list"]),
            "decomposition_point_stride": int(summary_dictionary["dataset"]["decomposition_point_stride"]),
            "exact_estimator_params": normalize_yaml_value(target_estimator.get_params(deep=True)),
            "training_metric_mae": float(target_artifact.source_target_metric["mae"]),
            "training_metric_rmse": float(target_artifact.source_target_metric["rmse"]),
            "training_metric_mse": float(target_artifact.source_target_metric["mse"]),
            "training_metric_mape_percent": float(target_artifact.source_target_metric["mape_percent"]),
        }
        all_reference_model_entry_list.append(reference_model_entry)
        source_run_id_set.add(run_instance_id)
        source_config_path_set.add(str(summary_dictionary["config_path"]).replace("\\", "/"))

    reference_inventory_dictionary = {
        "schema_version": 2,
        "topic": "track1_bidirectional_original_dataset_reference_archive",
        "paper_family_name": paper_family_code,
        "implementation_family_name": implementation_family_code,
        "archive_scope": f"track1_original_dataset_{direction_label}",
        "canonical_selection_rule": (
            "Per direction and target, select the completed mega-campaign attempt "
            "with the lowest target MAE; ties break on target RMSE, then target "
            "MAPE, then run name."
        ),
        "source_code": "scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py",
        "source_data": str(dataset_manifest_dictionary["source_dataset_config_path"]),
        "notes": [
            "This archive was rebuilt during the bidirectional original-dataset mega-campaign closeout.",
            "Detailed per-target provenance remains machine-readable in the reference inventory entries.",
        ],
        "reference_models": normalize_yaml_value(all_reference_model_entry_list),
    }
    save_yaml_dictionary(
        archive_root / "reference_inventory.yaml",
        reference_inventory_dictionary,
    )

    amplitude_entry_list = [
        entry for entry in all_reference_model_entry_list if entry["target_kind"] == "amplitude"
    ]
    phase_entry_list = [
        entry for entry in all_reference_model_entry_list if entry["target_kind"] == "phase"
    ]
    archive_readme_line_list = [
        f"# RCIM Track 1 {direction_label.title()} {paper_family_code} Reference Models",
        "",
        f"This archive stores the accepted `{paper_family_code}` target-level winners for the",
        f"`{direction_label}` branch of the bidirectional original-dataset Track 1 restart wave.",
        "",
        "Archive contents:",
        "",
        "- `reference_inventory.yaml`",
        "- `onnx/amplitude/`",
        "- `onnx/phase/`",
        "- `python/amplitude/`",
        "- `python/phase/`",
        "- `data/filtered_dataframe_deg_le_35.csv`",
        "- `dataset_snapshot_manifest.yaml`",
        "- `source_runs/<run_instance_id>/training_config.snapshot.yaml`",
        "- `source_runs/<run_instance_id>/run_metadata.snapshot.yaml`",
        "- `source_runs/<run_instance_id>/split_manifest.yaml`",
        "",
        "Selection rule:",
        "",
        "- lowest target `MAE`; ties break on target `RMSE`, then target `MAPE`, then run name.",
        "- archive refresh is mandatory at closeout only when the accepted winner improves the stored target entry.",
        "",
        "Accepted amplitude targets:",
        "",
        "| Target | Harmonic | MAE | RMSE | Archived ONNX |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for entry in amplitude_entry_list:
        archive_readme_line_list.append(
            f"| `{entry['target_name']}` | `{entry['harmonic_order']}` | "
            f"`{format_metric_value(entry['benchmark_mae'])}` | "
            f"`{format_metric_value(entry['benchmark_rmse'])}` | "
            f"`{entry['archived_model_path']}` |"
        )
    archive_readme_line_list.extend([
        "",
        "Accepted phase targets:",
        "",
        "| Target | Harmonic | MAE | RMSE | Archived ONNX |",
        "| --- | ---: | ---: | ---: | --- |",
    ])
    for entry in phase_entry_list:
        archive_readme_line_list.append(
            f"| `{entry['target_name']}` | `{entry['harmonic_order']}` | "
            f"`{format_metric_value(entry['benchmark_mae'])}` | "
            f"`{format_metric_value(entry['benchmark_rmse'])}` | "
            f"`{entry['archived_model_path']}` |"
        )
    archive_readme_line_list.extend([
        "",
        "Provenance summary:",
        "",
        f"- direction label: `{direction_label}`",
        f"- paper family: `{paper_family_code}`",
        f"- implementation family: `{implementation_family_code}`",
        f"- archived target count: `{len(all_reference_model_entry_list)}`",
        f"- unique source runs: `{len(source_run_id_set)}`",
        f"- unique source configs: `{len(source_config_path_set)}`",
        f"- dataset snapshot manifest: `{format_project_relative_path(archive_root / 'dataset_snapshot_manifest.yaml')}`",
        f"- machine-readable inventory: `{format_project_relative_path(archive_root / 'reference_inventory.yaml')}`",
        "",
    ])
    (archive_root / "README.md").write_text(
        "\n".join(archive_readme_line_list).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return {
        "direction_label": direction_label,
        "paper_family_code": paper_family_code,
        "archive_root": archive_root,
        "reference_target_count": len(all_reference_model_entry_list),
        "source_run_count": len(source_run_id_set),
        "source_config_count": len(source_config_path_set),
    }


def refresh_track1_reference_archives(
    accepted_target_artifact_map: dict[tuple[str, str, str], AcceptedTargetArtifact]
) -> list[dict[str, Any]]:

    """Rebuild the complete bidirectional `rcim_track1` archive surface."""

    TRACK1_REFERENCE_FORWARD_ROOT.mkdir(parents=True, exist_ok=True)
    TRACK1_REFERENCE_BACKWARD_ROOT.mkdir(parents=True, exist_ok=True)
    archive_summary_list: list[dict[str, Any]] = []
    for direction_label in DIRECTION_ORDER:
        for paper_family_code in FAMILY_ORDER:
            archive_summary_list.append(
                build_directional_family_archive(
                    direction_label,
                    paper_family_code,
                    accepted_target_artifact_map,
                )
            )

    TRACK1_REFERENCE_ROOT_README_PATH.write_text(
        "\n".join([
            "# RCIM Track 1 Paper Reference Models",
            "",
            "This folder groups curated paper-reference model archives for the canonical",
            "`Track 1` RCIM paper-reimplementation branch.",
            "",
            "Direction branches:",
            "",
            "- `forward/`",
            "- `backward/`",
            "",
            "Current populated family archives under both directions:",
            "",
            *[
                f"- `{direction_label}/{FAMILY_ARCHIVE_FOLDER_MAP[family_code]}/`"
                for direction_label in DIRECTION_ORDER
                for family_code in FAMILY_ORDER
            ],
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
            "- every future Track 1 closeout must compare newly accepted target winners against the archive entries already stored here;",
            "- when a newly accepted winner improves the stored archive entry, the archive must be replaced together with its provenance bundle and linked benchmark references;",
            "- when the accepted winner does not improve, the stored archive entry must remain unchanged.",
            "",
        ]).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    (TRACK1_REFERENCE_BACKWARD_ROOT / "README.md").write_text(
        "\n".join([
            "# RCIM Track 1 Backward Reference Branch",
            "",
            "This branch now stores the canonical backward-direction paper-reference",
            "archives rebuilt from the original dataset under `data/datasets/`.",
            "",
            "Populated family archives:",
            "",
            *[
                f"- `{FAMILY_ARCHIVE_FOLDER_MAP[family_code]}/`"
                for family_code in FAMILY_ORDER
            ],
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
            "The purpose of this archive is not to replace the immutable raw validation",
            "artifacts under `output/validation_checks/`. Instead, it provides a stable,",
            "human-auditable location for the subset of models that the benchmark accepts as",
            "the repository-owned reference surface for paper replication.",
            "",
            "Current topic roots:",
            "",
            "- `rcim_track1/`",
            "",
            "For `Track 1` paper-reimplementation families, the canonical family package",
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
            "Every fully curated family archive is expected to preserve:",
            "",
            "- the accepted target-level benchmark metrics;",
            "- the canonical source run per accepted target;",
            "- deployment-facing archived exports;",
            "- Python-usable fitted estimators when the training stack supports them;",
            "- dataset provenance and deterministic split reconstruction metadata.",
            "",
            "The bidirectional original-dataset Track 1 mega-campaign closeout is the first",
            "wave that fully populates both `forward` and `backward` archive branches.",
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
            "Current curated Track 1 paper-reference archives:",
            "",
            *[
                f"- `paper_reference/rcim_track1/{direction_label}/{FAMILY_ARCHIVE_FOLDER_MAP[family_code]}/`"
                for direction_label in DIRECTION_ORDER
                for family_code in FAMILY_ORDER
            ],
            "",
        ]).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return archive_summary_list


def build_campaign_leaderboard_artifacts(
    summary_dictionary_list: list[dict[str, Any]],
    campaign_output_directory: Path,
    finished_timestamp: str,
) -> dict[str, Any]:

    """Materialize campaign-level leaderboard and best-run bookkeeping files."""

    ranked_summary_list = sorted(summary_dictionary_list, key=build_run_sort_key)
    leaderboard_entry_list: list[dict[str, Any]] = []
    for summary_dictionary in ranked_summary_list:
        winner_summary = summary_dictionary["winner_summary"]
        leaderboard_entry_list.append({
            "run_instance_id": str(summary_dictionary["experiment"]["run_instance_id"]),
            "run_name": str(summary_dictionary["experiment"]["run_name"]),
            "direction_label": str(summary_dictionary["dataset"]["direction_label"]),
            "winning_family": str(winner_summary["winning_family"]),
            "winning_estimator_name": str(winner_summary["winning_estimator_name"]),
            "winning_mean_component_mae": float(winner_summary["winning_mean_component_mae"]),
            "winning_mean_component_rmse": float(winner_summary["winning_mean_component_rmse"]),
            "winning_mean_component_mape_percent": float(winner_summary["winning_mean_component_mape_percent"]),
            "validation_summary_path": str(summary_dictionary["artifacts"]["validation_summary_path"]).replace("\\", "/"),
            "config_path": str(summary_dictionary["config_path"]).replace("\\", "/"),
        })

    leaderboard_dictionary = {
        "schema_version": 1,
        "campaign_name": str(load_active_campaign_state()["campaign_name"]),
        "selection_policy": CAMPAIGN_SELECTION_POLICY,
        "generated_at": finished_timestamp,
        "entry_count": len(leaderboard_entry_list),
        "leaderboard": leaderboard_entry_list,
    }
    best_entry = leaderboard_entry_list[0]
    best_run_dictionary = {
        **best_entry,
        "output_artifact_kind": "validation_check",
        "selection_policy": CAMPAIGN_SELECTION_POLICY,
        "selected_at": finished_timestamp,
    }
    best_run_markdown = "\n".join([
        "# Campaign Best Run",
        "",
        f"- run instance id: `{best_entry['run_instance_id']}`",
        f"- run name: `{best_entry['run_name']}`",
        f"- direction label: `{best_entry['direction_label']}`",
        f"- winning family: `{best_entry['winning_family']}`",
        f"- winning estimator: `{best_entry['winning_estimator_name']}`",
        f"- winning mean component MAE: `{format_metric_value(best_entry['winning_mean_component_mae'])}`",
        f"- winning mean component RMSE: `{format_metric_value(best_entry['winning_mean_component_rmse'])}`",
        f"- winning mean component MAPE: `{format_metric_value(best_entry['winning_mean_component_mape_percent'])}%`",
        "",
        "Selection rule:",
        "",
        *CAMPAIGN_BEST_RUN_SELECTION_LINES,
        "",
    ]).rstrip() + "\n"
    save_yaml_dictionary(campaign_output_directory / "campaign_leaderboard.yaml", leaderboard_dictionary)
    save_yaml_dictionary(campaign_output_directory / "campaign_best_run.yaml", best_run_dictionary)
    (campaign_output_directory / "campaign_best_run.md").write_text(
        best_run_markdown,
        encoding="utf-8",
        newline="\n",
    )
    return best_entry


def build_benchmark_status_lines(
    benchmark_status_dictionary: dict[str, Any],
) -> list[str]:

    """Build compact report lines for the refreshed benchmark surface."""

    report_line_list = [
        "| Table | Direction | Green | Yellow | Red | Total |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for table_key, table_heading in zip(
        ["table2", "table3", "table4", "table5"],
        ["Table 2 - Amplitude MAE", "Table 3 - Amplitude RMSE", "Table 4 - Phase MAE", "Table 5 - Phase RMSE"],
        strict=True,
    ):
        for direction_label in DIRECTION_ORDER:
            direction_status = benchmark_status_dictionary[table_key][direction_label]
            report_line_list.append(
                f"| `{table_heading}` | `{direction_label}` | "
                f"{direction_status['green']} | {direction_status['yellow']} | "
                f"{direction_status['red']} | {direction_status['total']} |"
            )
    return report_line_list


def patch_master_summary(
    active_campaign_dictionary: dict[str, Any],
    report_relative_path: str,
    benchmark_status_dictionary: dict[str, Any],
    best_run_entry: dict[str, Any],
) -> None:

    """Patch the canonical master summary with the new closeout state."""

    master_summary_line_list = MASTER_SUMMARY_PATH.read_text(encoding="utf-8").splitlines()
    generated_at_index = find_line_index(master_summary_line_list, "- Generated At: `2026-04-24T12:39:24+02:00`")
    master_summary_line_list[generated_at_index] = (
        f"- Generated At: `{datetime.now().astimezone().isoformat()}`"
    )
    active_campaign_status_index = next(
        line_index
        for line_index, line_text in enumerate(master_summary_line_list)
        if line_text.startswith("- Active Campaign Status:")
    )
    master_summary_line_list[active_campaign_status_index] = "- Active Campaign Status: `completed`"
    active_campaign_name_index = next(
        line_index
        for line_index, line_text in enumerate(master_summary_line_list)
        if line_text.startswith("- Active Campaign Name:")
    )
    master_summary_line_list[active_campaign_name_index] = (
        f"- Active Campaign Name: `{active_campaign_dictionary['campaign_name']}`"
    )

    recent_campaign_table_header_index = find_line_index(
        master_summary_line_list,
        "| Campaign | Generated At | Completed | Failed | Winner | Impact |",
    )
    insert_row_index = recent_campaign_table_header_index + 2
    completed_count = len(active_campaign_dictionary["queue_config_path_list"])
    master_summary_line_list.insert(
        insert_row_index,
        f"| `{active_campaign_dictionary['campaign_name']}` | "
        f"`{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}` | "
        f"{completed_count} | 0 | `{best_run_entry['run_name']}` | "
        "Bidirectional original-dataset mega wave completed `400/400`, refreshed both benchmark restart surfaces, and rebuilt the full `2 x 10 x 19` paper-reference archive set under `models/paper_reference/rcim_track1/` |",
    )

    track1_status_heading_index = find_line_index(master_summary_line_list, "### Track 1 Canonical Status")
    track15_heading_index = find_line_index(master_summary_line_list, "### Track 1.5 Harmonic-Wise Validation Support", start_index=track1_status_heading_index)
    total_non_green_count = sum(
        status_dictionary["yellow"] + status_dictionary["red"]
        for table_dictionary in benchmark_status_dictionary.values()
        for status_dictionary in table_dictionary.values()
    )
    replacement_line_list = [
        "### Track 1 Canonical Status",
        "",
        f"- Latest exact-paper closeout report: `{report_relative_path}`",
        "- Canonical progress surface:",
        "  - `Table 2 - Amplitude MAE Full-Matrix Replication`",
        "  - `Table 3 - Amplitude RMSE Full-Matrix Replication`",
        "  - `Table 4 - Phase MAE Full-Matrix Replication`",
        "  - `Table 5 - Phase RMSE Full-Matrix Replication`",
        "- Completion rule: `19` accepted models for each of the `10` algorithm families in both `forward` and `backward` directions",
        f"- Table `2` `forward` status: `{benchmark_status_dictionary['table2']['forward']['green']}` green, `{benchmark_status_dictionary['table2']['forward']['yellow']}` yellow, `{benchmark_status_dictionary['table2']['forward']['red']}` red",
        f"- Table `2` `backward` status: `{benchmark_status_dictionary['table2']['backward']['green']}` green, `{benchmark_status_dictionary['table2']['backward']['yellow']}` yellow, `{benchmark_status_dictionary['table2']['backward']['red']}` red",
        f"- Table `3` `forward` status: `{benchmark_status_dictionary['table3']['forward']['green']}` green, `{benchmark_status_dictionary['table3']['forward']['yellow']}` yellow, `{benchmark_status_dictionary['table3']['forward']['red']}` red",
        f"- Table `3` `backward` status: `{benchmark_status_dictionary['table3']['backward']['green']}` green, `{benchmark_status_dictionary['table3']['backward']['yellow']}` yellow, `{benchmark_status_dictionary['table3']['backward']['red']}` red",
        f"- Table `4` `forward` status: `{benchmark_status_dictionary['table4']['forward']['green']}` green, `{benchmark_status_dictionary['table4']['forward']['yellow']}` yellow, `{benchmark_status_dictionary['table4']['forward']['red']}` red",
        f"- Table `4` `backward` status: `{benchmark_status_dictionary['table4']['backward']['green']}` green, `{benchmark_status_dictionary['table4']['backward']['yellow']}` yellow, `{benchmark_status_dictionary['table4']['backward']['red']}` red",
        f"- Table `5` `forward` status: `{benchmark_status_dictionary['table5']['forward']['green']}` green, `{benchmark_status_dictionary['table5']['forward']['yellow']}` yellow, `{benchmark_status_dictionary['table5']['forward']['red']}` red",
        f"- Table `5` `backward` status: `{benchmark_status_dictionary['table5']['backward']['green']}` green, `{benchmark_status_dictionary['table5']['backward']['yellow']}` yellow, `{benchmark_status_dictionary['table5']['backward']['red']}` red",
        f"- Remaining non-green cells across both directional restart surfaces: `{total_non_green_count}`",
        "- Harmonic-wise Table `6` evidence remains postponed into `Track 1.5` and does not gate this closeout.",
        "",
    ]
    master_summary_line_list = (
        master_summary_line_list[:track1_status_heading_index]
        + replacement_line_list
        + master_summary_line_list[track15_heading_index:]
    )

    gap_summary_heading_index = find_line_index(master_summary_line_list, "### Gap Summary")
    gap_summary_first_bullet_index = gap_summary_heading_index + 2
    master_summary_line_list[gap_summary_first_bullet_index] = (
        f"- `Track 1` still has `{total_non_green_count}` non-green cells across the bidirectional original-dataset restart benchmark surface."
    )
    MASTER_SUMMARY_PATH.write_text(
        "\n".join(master_summary_line_list).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )


def build_campaign_results_report_markdown(
    active_campaign_dictionary: dict[str, Any],
    report_relative_path: str,
    benchmark_status_dictionary: dict[str, Any],
    archive_summary_list: list[dict[str, Any]],
    best_run_entry: dict[str, Any],
) -> str:

    """Build the final campaign-results report Markdown."""

    campaign_output_directory = shared_training_infrastructure.resolve_project_relative_path(
        active_campaign_dictionary["campaign_output_directory"]
    )
    report_line_list = [
        "# Track 1 Bidirectional Original-Dataset Mega Campaign Results",
        "",
        "## Overview",
        "",
        f"- campaign name: `{active_campaign_dictionary['campaign_name']}`",
        f"- planning report: `{str(active_campaign_dictionary['planning_report_path']).replace('\\', '/')}`",
        f"- campaign output directory: `{format_project_relative_path(campaign_output_directory)}`",
        f"- queue size: `{len(active_campaign_dictionary['queue_config_path_list'])}`",
        f"- launch mode: `{active_campaign_dictionary['launch_mode']}`",
        f"- remote host alias: `{active_campaign_dictionary['remote_host_alias']}`",
        "",
        "## Completion Summary",
        "",
        "- the bidirectional original-dataset exact-paper mega campaign completed the full `400/400` queue;",
        "- the closeout refreshed both directional repository-owned restart matrices in `RCIM Paper Reference Benchmark.md`;",
        "- the closeout rebuilt the canonical paper-reference archives under `models/paper_reference/rcim_track1/forward/` and `models/paper_reference/rcim_track1/backward/`;",
        "- the closeout materialized campaign-level `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and `campaign_best_run.md` bookkeeping artifacts.",
        "",
        "## Campaign Best Run",
        "",
        f"- run instance id: `{best_run_entry['run_instance_id']}`",
        f"- run name: `{best_run_entry['run_name']}`",
        f"- direction label: `{best_run_entry['direction_label']}`",
        f"- winning family: `{best_run_entry['winning_family']}`",
        f"- winning estimator: `{best_run_entry['winning_estimator_name']}`",
        f"- mean component MAE: `{format_metric_value(best_run_entry['winning_mean_component_mae'])}`",
        f"- mean component RMSE: `{format_metric_value(best_run_entry['winning_mean_component_rmse'])}`",
        f"- mean component MAPE: `{format_metric_value(best_run_entry['winning_mean_component_mape_percent'])}%`",
        "",
        "Selection rule:",
        "",
        *CAMPAIGN_BEST_RUN_SELECTION_LINES,
        "",
        "## Benchmark Restart Surface",
        "",
        *build_benchmark_status_lines(benchmark_status_dictionary),
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
        f"- track1 reference root: `{format_project_relative_path(TRACK1_REFERENCE_ROOT)}`",
        f"- campaign leaderboard: `{format_project_relative_path(campaign_output_directory / 'campaign_leaderboard.yaml')}`",
        f"- campaign best run YAML: `{format_project_relative_path(campaign_output_directory / 'campaign_best_run.yaml')}`",
        f"- campaign best run Markdown: `{format_project_relative_path(campaign_output_directory / 'campaign_best_run.md')}`",
        f"- active campaign state: `{format_project_relative_path(ACTIVE_CAMPAIGN_PATH)}`",
        "",
        "## Closeout Notes",
        "",
        "- the archive refresh rule remains mandatory for every future Track 1 closeout;",
        "- when a newly accepted target winner improves the stored archive entry under `models/paper_reference/rcim_track1/`, the archive must be updated together with its reference documents;",
        "- when the accepted target winner does not improve, the stored archive entry must remain unchanged.",
        "",
        f"This report is the canonical closeout record for `{active_campaign_dictionary['campaign_name']}` and is linked from `{report_relative_path}`.",
        "",
    ])
    return "\n".join(report_line_list).rstrip() + "\n"


def update_active_campaign_state(
    active_campaign_dictionary: dict[str, Any],
    report_relative_path: str,
    finished_timestamp: str,
) -> None:

    """Persist the completed campaign state."""

    active_campaign_dictionary["status"] = "completed"
    active_campaign_dictionary["finished_at"] = finished_timestamp
    active_campaign_dictionary["completion_recorded_at"] = finished_timestamp
    active_campaign_dictionary["results_report_path"] = report_relative_path.replace("/", "\\")
    active_campaign_dictionary["completed_family_list"] = list(FAMILY_ORDER)
    active_campaign_dictionary["pending_family_list"] = []
    active_campaign_dictionary["interruption_note"] = None
    save_yaml_dictionary(ACTIVE_CAMPAIGN_PATH, active_campaign_dictionary)


def run_closeout() -> Path:

    """Execute the full closeout workflow."""

    active_campaign_dictionary = load_active_campaign_state()
    assert str(active_campaign_dictionary["status"]) == "running", (
        "Expected the active campaign to still be marked as running before closeout | "
        f"status={active_campaign_dictionary['status']}"
    )
    summary_dictionary_list, summary_path_map = collect_campaign_summary_bundle(active_campaign_dictionary)
    accepted_target_artifact_map = build_accepted_target_artifact_map(
        summary_dictionary_list,
        summary_path_map,
    )
    benchmark_status_dictionary, _ = update_benchmark_restart_matrices(accepted_target_artifact_map)
    archive_summary_list = refresh_track1_reference_archives(accepted_target_artifact_map)

    campaign_output_directory = shared_training_infrastructure.resolve_project_relative_path(
        active_campaign_dictionary["campaign_output_directory"]
    )
    campaign_output_directory.mkdir(parents=True, exist_ok=True)
    finished_timestamp = datetime.now().astimezone().isoformat()
    best_run_entry = build_campaign_leaderboard_artifacts(
        summary_dictionary_list,
        campaign_output_directory,
        finished_timestamp,
    )

    report_timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    report_output_path = (
        REPORT_OUTPUT_ROOT
        / f"{report_timestamp}_track1_bidirectional_original_dataset_mega_campaign_results_report.md"
    )
    report_relative_path = format_project_relative_path(report_output_path)
    report_output_path.parent.mkdir(parents=True, exist_ok=True)
    report_output_path.write_text(
        build_campaign_results_report_markdown(
            active_campaign_dictionary,
            report_relative_path,
            benchmark_status_dictionary,
            archive_summary_list,
            best_run_entry,
        ),
        encoding="utf-8",
        newline="\n",
    )

    update_active_campaign_state(active_campaign_dictionary, report_relative_path, finished_timestamp)
    patch_master_summary(
        active_campaign_dictionary,
        report_relative_path,
        benchmark_status_dictionary,
        best_run_entry,
    )
    print(f"[DONE] Closed out campaign | report={report_relative_path}")
    return report_output_path


def main() -> None:

    """Run the closeout entry point."""

    parse_command_line_arguments()
    run_closeout()


if __name__ == "__main__":

    main()
