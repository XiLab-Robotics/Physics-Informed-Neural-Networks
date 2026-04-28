"""Refresh the canonical forward Track 1 family reference archives.

This utility rebuilds the curated paper-reference archive packages under
`models/paper_reference/rcim_track1/forward/` from the currently accepted
family rows stored in the canonical Track 1 benchmark.
"""

from __future__ import annotations

import argparse
import hashlib
import pickle
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

from scripts.paper_reimplementation.rcim_ml_compensation import exact_paper_model_bank_support
from scripts.training import shared_training_infrastructure

TRACK1_REFERENCE_ROOT = PROJECT_PATH / "models" / "paper_reference" / "rcim_track1"
TRACK1_REFERENCE_FORWARD_ROOT = TRACK1_REFERENCE_ROOT / "forward"
BENCHMARK_REPORT_PATH = (
    PROJECT_PATH / "doc" / "reports" / "analysis" / "RCIM Paper Reference Benchmark.md"
)
MODELS_README_PATH = PROJECT_PATH / "models" / "README.md"
MODELS_GITIGNORE_PATH = PROJECT_PATH / "models" / ".gitignore"
TRACK1_REFERENCE_README_PATH = TRACK1_REFERENCE_ROOT / "README.md"
VALIDATION_ROOT = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "paper_reimplementation_rcim_exact_model_bank"
    / "forward"
)
SOURCE_DATAFRAME_PATH = (
    "reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/"
    "dataFrame_prediction_Fw_v14_newFreq.csv"
)
CANONICAL_DATASET_SNAPSHOT_FILENAME = "filtered_dataframe_deg_le_35.csv"
FAMILY_ORDER = ["SVM", "MLP", "RF", "DT", "ET", "ERT", "GBM", "HGBM", "XGBM", "LGBM"]
AMPLITUDE_HARMONIC_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
PHASE_HARMONIC_LIST = [1, 3, 39, 40, 78, 81, 156, 162, 240]
MARKER_PREFIX_PATTERN = re.compile(
    r"^(?:\?\?|G|Y|R|ðŸŸ¢|ðŸŸ¡|ðŸ”´|Ã°Å¸Å¸Â¢|Ã°Å¸Å¸Â¡|Ã°Å¸â€Â´|ÃƒÂ°Ã…Â¸Ã…Â¸Ã‚Â¢|ÃƒÂ°Ã…Â¸Ã…Â¸Ã‚Â¡|ÃƒÂ°Ã…Â¸Ã¢â‚¬ÂÃ‚Â´)\s+"
)

FAMILY_IMPLEMENTATION_CODE_MAP = {
    "SVM": "SVR",
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
FAMILY_ARCHIVE_FOLDER_MAP = {
    family_code: f"{family_code.lower()}_reference_models"
    for family_code in FAMILY_ORDER
}
TRACK1_ARCHIVE_SECTION_START_HEADING = "### SVM Reference Model Inventory"
TRACK1_ARCHIVE_SECTION_END_HEADING = "### Supporting Harmonic-Wise Offline Result"
MD013_DISABLE = "<!-- markdownlint-disable MD013 -->"
MD013_ENABLE = "<!-- markdownlint-enable MD013 -->"

VALIDATION_SUMMARY_CACHE: dict[Path, dict[str, Any]] = {}
MODEL_BUNDLE_CACHE: dict[str, dict[str, Any]] = {}
TRAINING_CONFIG_CACHE: dict[str, dict[str, Any]] = {}
TARGET_SCOPE_CACHE: dict[str, dict[str, Any]] = {}
SPLIT_MANIFEST_CACHE: dict[str, dict[str, Any]] = {}


@dataclass(frozen=True)
class AcceptedTargetMetric:

    """Accepted benchmark surface entry for one family target."""

    paper_family_code: str
    implementation_family_code: str
    target_name: str
    target_kind: str
    harmonic_order: int
    benchmark_visible_mae: float
    benchmark_visible_rmse: float


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk."""

    with input_path.open("r", encoding="utf-8") as input_file:
        loaded_dictionary = yaml.safe_load(input_file)
    assert isinstance(loaded_dictionary, dict), f"Expected YAML dictionary | path={input_path}"
    return loaded_dictionary


def format_metric_value(metric_value: float) -> str:

    """Format one floating-point metric for benchmark-aligned comparisons."""

    return f"{metric_value:.6g}"


def parse_markdown_row(markdown_line: str) -> list[str]:

    """Parse one Markdown table row into stripped cells."""

    normalized_line = markdown_line.strip().strip("|")
    return [cell.strip() for cell in normalized_line.split("|")]


def sanitize_repository_metric_cell(cell_text: str) -> str:

    """Strip markers and backticks from one repository table cell."""

    normalized_cell_text = cell_text.strip().strip("`")
    normalized_cell_text = MARKER_PREFIX_PATTERN.sub("", normalized_cell_text)
    normalized_cell_text = re.sub(r"^[^0-9+\-\.eE]+", "", normalized_cell_text)
    return normalized_cell_text


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

    """Collect model rows from one Markdown table block."""

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


def parse_full_matrix_section(
    line_list: list[str],
    heading_text: str,
    expected_row_count: int,
) -> dict[str, Any]:

    """Parse one full-matrix section from the benchmark report."""

    heading_index = find_line_index(line_list, heading_text)
    paper_anchor_index = find_line_index(
        line_list,
        "Paper-side repository-owned reconstruction:",
        start_index=heading_index,
    )
    repository_anchor_index = find_line_index(
        line_list,
        "Repository-side analogous matrix:",
        start_index=heading_index,
    )
    paper_header_index = next(
        line_index
        for line_index in range(paper_anchor_index, len(line_list))
        if line_list[line_index].startswith("| Model |")
    )
    repository_header_index = next(
        line_index
        for line_index in range(repository_anchor_index, len(line_list))
        if line_list[line_index].startswith("| Model |")
    )
    paper_header_cell_list = parse_markdown_row(line_list[paper_header_index])
    repository_header_cell_list = parse_markdown_row(line_list[repository_header_index])
    assert paper_header_cell_list == repository_header_cell_list, (
        "Paper and repository headers must match | "
        f"heading={heading_text}"
    )
    harmonic_list = [int(cell.strip("`")) for cell in paper_header_cell_list[1:]]

    paper_row_list = collect_model_rows(line_list, paper_anchor_index, expected_row_count)
    repository_row_list = collect_model_rows(
        line_list,
        repository_anchor_index,
        expected_row_count,
    )

    paper_row_dictionary: dict[str, dict[int, float]] = {}
    repository_row_dictionary: dict[str, dict[int, float]] = {}
    for _, paper_row in paper_row_list:
        family_code = paper_row[0].strip("`")
        paper_row_dictionary[family_code] = {
            harmonic_order: float(paper_cell)
            for harmonic_order, paper_cell in zip(harmonic_list, paper_row[1:], strict=True)
        }

    for _, repository_row in repository_row_list:
        family_code = repository_row[0].strip("`")
        repository_row_dictionary[family_code] = {
            harmonic_order: float(sanitize_repository_metric_cell(repository_cell))
            for harmonic_order, repository_cell in zip(
                harmonic_list,
                repository_row[1:],
                strict=True,
            )
        }

    return {
        "heading_index": heading_index,
        "harmonic_list": harmonic_list,
        "paper_rows": paper_row_dictionary,
        "repository_rows": repository_row_dictionary,
    }


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse CLI arguments for the archive refresh utility."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Refresh the canonical Track 1 family reference archives from the "
            "currently accepted benchmark surface."
        )
    )
    argument_parser.add_argument(
        "--family",
        action="append",
        default=[],
        help=(
            "Optional paper-facing family code to refresh. Repeatable. "
            "When omitted, refresh all Track 1 families."
        ),
    )
    return argument_parser.parse_args()


def compute_sha256(file_path: Path) -> str:

    """Compute the SHA256 digest of one file."""

    hasher = hashlib.sha256()
    with file_path.open("rb") as input_file:
        for chunk in iter(lambda: input_file.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


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
        return shared_training_infrastructure.format_project_relative_path(value)
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def build_accepted_target_metric_list(
    selected_family_code_list: list[str],
) -> list[AcceptedTargetMetric]:

    """Build the accepted family-target metric list from the benchmark tables."""

    benchmark_line_list = BENCHMARK_REPORT_PATH.read_text(encoding="utf-8").splitlines()
    table_dictionary = {
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

    accepted_metric_list: list[AcceptedTargetMetric] = []
    for family_code in selected_family_code_list:
        implementation_family_code = FAMILY_IMPLEMENTATION_CODE_MAP[family_code]
        for harmonic_order in AMPLITUDE_HARMONIC_LIST:
            accepted_metric_list.append(
                AcceptedTargetMetric(
                    paper_family_code=family_code,
                    implementation_family_code=implementation_family_code,
                    target_name=f"fft_y_Fw_filtered_ampl_{harmonic_order}",
                    target_kind="amplitude",
                    harmonic_order=harmonic_order,
                    benchmark_visible_mae=float(
                        table_dictionary["table2"]["repository_rows"][family_code][harmonic_order]
                    ),
                    benchmark_visible_rmse=float(
                        table_dictionary["table3"]["repository_rows"][family_code][harmonic_order]
                    ),
                )
            )

        for harmonic_order in PHASE_HARMONIC_LIST:
            accepted_metric_list.append(
                AcceptedTargetMetric(
                    paper_family_code=family_code,
                    implementation_family_code=implementation_family_code,
                    target_name=f"fft_y_Fw_filtered_phase_{harmonic_order}",
                    target_kind="phase",
                    harmonic_order=harmonic_order,
                    benchmark_visible_mae=float(
                        table_dictionary["table4"]["repository_rows"][family_code][harmonic_order]
                    ),
                    benchmark_visible_rmse=float(
                        table_dictionary["table5"]["repository_rows"][family_code][harmonic_order]
                    ),
                )
            )

    return accepted_metric_list


def build_canonical_dataset_snapshot_bundle() -> tuple[str, dict[str, Any]]:

    """Build the canonical filtered dataset snapshot text and manifest."""

    training_config = {
        "paths": {
            "source_dataframe_path": SOURCE_DATAFRAME_PATH,
        },
        "data": {
            "csv_separator": ";",
            "csv_decimal": ",",
            "maximum_deg": 35.0,
        },
    }
    filtered_dataframe = exact_paper_model_bank_support.load_exact_paper_dataframe(
        training_config
    )
    snapshot_text = filtered_dataframe.to_csv(
        index=True,
        index_label="filtered_row_index",
        lineterminator="\n",
    )
    snapshot_sha256 = hashlib.sha256(snapshot_text.encode("utf-8")).hexdigest()
    source_dataframe_path = shared_training_infrastructure.resolve_project_relative_path(
        SOURCE_DATAFRAME_PATH
    )
    manifest_dictionary = {
        "schema_version": 1,
        "dataset_snapshot_path": (
            "models/paper_reference/rcim_track1/forward/<family>_reference_models/data/"
            f"{CANONICAL_DATASET_SNAPSHOT_FILENAME}"
        ),
        "dataset_snapshot_sha256": snapshot_sha256,
        "source_dataframe_path": SOURCE_DATAFRAME_PATH,
        "source_dataframe_sha256": compute_sha256(source_dataframe_path),
        "filtered_row_count": int(len(filtered_dataframe)),
        "column_name_list": list(filtered_dataframe.columns),
        "index_name": "filtered_row_index",
        "maximum_deg": 35.0,
    }
    return snapshot_text, manifest_dictionary


def collect_validation_summary_path_list() -> list[Path]:

    """Collect all exact-paper validation-summary paths."""

    return sorted(VALIDATION_ROOT.rglob("validation_summary.yaml"))


def load_validation_summary(summary_path: Path) -> dict[str, Any]:

    """Load one cached validation summary."""

    if summary_path not in VALIDATION_SUMMARY_CACHE:
        VALIDATION_SUMMARY_CACHE[summary_path] = load_yaml_dictionary(summary_path)
    return VALIDATION_SUMMARY_CACHE[summary_path]


def collect_validation_summary_dictionary_list() -> list[dict[str, Any]]:

    """Collect all exact-paper validation summaries."""

    return [
        load_validation_summary(summary_path)
        for summary_path in collect_validation_summary_path_list()
    ]


def load_existing_reference_inventory(archive_root: Path) -> dict[str, Any] | None:

    """Load the existing family inventory when an archive is already present."""

    reference_inventory_path = archive_root / "reference_inventory.yaml"
    if not reference_inventory_path.exists():
        return None
    try:
        return load_yaml_dictionary(reference_inventory_path)
    except yaml.YAMLError:
        return None


def load_existing_yaml_dictionary(input_path: Path) -> dict[str, Any] | None:

    """Load an existing YAML dictionary, ignoring interrupted partial writes."""

    if not input_path.exists():
        return None
    try:
        return load_yaml_dictionary(input_path)
    except yaml.YAMLError:
        return None


def build_existing_reference_entry_map(
    existing_reference_inventory: dict[str, Any] | None,
) -> dict[str, dict[str, Any]]:

    """Build a target-name keyed lookup for the existing canonical entries."""

    if existing_reference_inventory is None:
        return {}
    reference_model_list = existing_reference_inventory.get("reference_models", [])
    if not isinstance(reference_model_list, list):
        return {}

    existing_reference_entry_map: dict[str, dict[str, Any]] = {}
    for reference_entry in reference_model_list:
        if not isinstance(reference_entry, dict):
            continue
        target_name = reference_entry.get("target_name")
        if not isinstance(target_name, str):
            continue
        existing_reference_entry_map[target_name] = reference_entry
    return existing_reference_entry_map


def resolve_target_metric_entry(
    summary_dictionary: dict[str, Any],
    target_name: str,
    implementation_family_code: str,
) -> dict[str, Any] | None:

    """Resolve one family-target metric entry from a validation summary."""

    ranking_dictionary = summary_dictionary.get("per_target_ranking", {})
    if not isinstance(ranking_dictionary, dict):
        return None

    ranking_list = ranking_dictionary.get(target_name, [])
    if not isinstance(ranking_list, list):
        return None

    for ranking_entry in ranking_list:
        if not isinstance(ranking_entry, dict):
            continue
        if str(ranking_entry.get("family_name")) == implementation_family_code:
            return ranking_entry

    return None


def metrics_match_visible_benchmark(
    target_metric_entry: dict[str, Any],
    accepted_metric: AcceptedTargetMetric,
) -> bool:

    """Check whether one summary target entry matches the visible benchmark."""

    def resolve_metric_tolerance(benchmark_value: float) -> float:
        absolute_value = abs(float(benchmark_value))
        if absolute_value >= 1.0:
            return 5e-4
        if absolute_value >= 1e-2:
            return 5e-5
        if absolute_value >= 1e-3:
            return 5e-6
        return 5e-7

    mae_value = float(target_metric_entry["mae"])
    rmse_value = float(target_metric_entry["rmse"])
    mae_tolerance = resolve_metric_tolerance(accepted_metric.benchmark_visible_mae)
    rmse_tolerance = resolve_metric_tolerance(accepted_metric.benchmark_visible_rmse)
    return (
        abs(mae_value - accepted_metric.benchmark_visible_mae) <= mae_tolerance
        and abs(rmse_value - accepted_metric.benchmark_visible_rmse) <= rmse_tolerance
    )


def entry_metrics_match_visible_benchmark(
    mae_value: float,
    rmse_value: float,
    accepted_metric: AcceptedTargetMetric,
) -> bool:

    """Check whether raw metric values match the visible benchmark tolerance."""

    return metrics_match_visible_benchmark(
        {
            "mae": float(mae_value),
            "rmse": float(rmse_value),
        },
        accepted_metric,
    )


def select_canonical_summary_for_target(
    accepted_metric: AcceptedTargetMetric,
    summary_dictionary_list: list[dict[str, Any]],
    preferred_run_instance_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:

    """Select the canonical source summary for one accepted family target."""

    candidate_list: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
    preferred_candidate: tuple[dict[str, Any], dict[str, Any]] | None = None
    fallback_candidate_list: list[tuple[float, str, dict[str, Any], dict[str, Any]]] = []
    for summary_dictionary in summary_dictionary_list:
        target_metric_entry = resolve_target_metric_entry(
            summary_dictionary,
            accepted_metric.target_name,
            accepted_metric.implementation_family_code,
        )
        if target_metric_entry is None:
            continue
        try:
            export_target_entry = resolve_family_export_target_entry(
                summary_dictionary,
                accepted_metric.implementation_family_code,
                accepted_metric.target_name,
            )
        except AssertionError:
            continue
        source_export_path = shared_training_infrastructure.resolve_project_relative_path(
            export_target_entry["export_path"]
        )
        if not source_export_path.exists():
            continue
        run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
        metric_gap = (
            abs(float(target_metric_entry["mae"]) - accepted_metric.benchmark_visible_mae)
            + abs(float(target_metric_entry["rmse"]) - accepted_metric.benchmark_visible_rmse)
        )
        fallback_candidate_list.append(
            (metric_gap, run_instance_id, summary_dictionary, target_metric_entry)
        )
        if not metrics_match_visible_benchmark(target_metric_entry, accepted_metric):
            continue
        candidate_list.append(
            (run_instance_id, summary_dictionary, target_metric_entry)
        )
        if preferred_run_instance_id and run_instance_id == preferred_run_instance_id:
            preferred_candidate = (summary_dictionary, target_metric_entry)

    if preferred_candidate is not None:
        return preferred_candidate

    if candidate_list:
        candidate_list.sort(key=lambda item: item[0])
        _, selected_summary_dictionary, selected_target_entry = candidate_list[0]
        return selected_summary_dictionary, selected_target_entry

    assert fallback_candidate_list, (
        "Failed to resolve canonical source summary for accepted family target | "
        f"family={accepted_metric.paper_family_code} | "
        f"target={accepted_metric.target_name}"
    )
    fallback_candidate_list.sort(key=lambda item: (item[0], item[1]))
    _, _, selected_summary_dictionary, selected_target_entry = fallback_candidate_list[0]
    return selected_summary_dictionary, selected_target_entry


def resolve_family_export_target_entry(
    summary_dictionary: dict[str, Any],
    implementation_family_code: str,
    target_name: str,
) -> dict[str, Any]:

    """Resolve one ONNX export entry for one family target."""

    onnx_export_summary = summary_dictionary["onnx_export_summary"]
    family_export_list = onnx_export_summary["family_exports"]
    for family_export_entry in family_export_list:
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

    """Load one exact-paper family model bundle from the validation summary."""

    run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
    if run_instance_id not in MODEL_BUNDLE_CACHE:
        model_bundle_path = shared_training_infrastructure.resolve_project_relative_path(
            summary_dictionary["artifacts"]["model_bundle_path"]
        )
        with model_bundle_path.open("rb") as input_file:
            model_bundle = pickle.load(input_file)
        assert isinstance(model_bundle, dict), "Exact-paper model bundle must be a dictionary."
        MODEL_BUNDLE_CACHE[run_instance_id] = model_bundle
    return MODEL_BUNDLE_CACHE[run_instance_id]


def resolve_training_config_dictionary(summary_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Resolve the cached training-config snapshot for one source run."""

    run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
    if run_instance_id not in TRAINING_CONFIG_CACHE:
        output_directory = shared_training_infrastructure.resolve_project_relative_path(
            summary_dictionary["experiment"]["output_directory"]
        )
        training_config_path = output_directory / "training_config.yaml"
        TRAINING_CONFIG_CACHE[run_instance_id] = load_yaml_dictionary(training_config_path)
    return TRAINING_CONFIG_CACHE[run_instance_id]


def resolve_target_scope_dictionary(summary_dictionary: dict[str, Any]) -> dict[str, Any]:

    """Resolve the cached target-scope dictionary for one source run."""

    run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
    if run_instance_id not in TARGET_SCOPE_CACHE:
        TARGET_SCOPE_CACHE[run_instance_id] = (
            exact_paper_model_bank_support.resolve_exact_target_scope(
                resolve_training_config_dictionary(summary_dictionary)
            )
        )
    return TARGET_SCOPE_CACHE[run_instance_id]


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


def build_split_manifest_dictionary(
    archive_root: Path,
    summary_dictionary: dict[str, Any],
    run_instance_id: str,
    dataset_manifest_dictionary: dict[str, Any],
) -> dict[str, Any]:

    """Build one deterministic split manifest for a source run."""

    if run_instance_id in SPLIT_MANIFEST_CACHE:
        split_manifest_dictionary = dict(SPLIT_MANIFEST_CACHE[run_instance_id])
        split_manifest_dictionary["dataset_snapshot_path"] = (
            shared_training_infrastructure.format_project_relative_path(
                archive_root / "data" / CANONICAL_DATASET_SNAPSHOT_FILENAME
            )
        )
        return split_manifest_dictionary

    output_directory = shared_training_infrastructure.resolve_project_relative_path(
        summary_dictionary["experiment"]["output_directory"]
    )
    training_config_path = output_directory / "training_config.yaml"
    run_metadata_path = output_directory / "run_metadata.yaml"
    training_config = resolve_training_config_dictionary(summary_dictionary)
    dataset_bundle = exact_paper_model_bank_support.build_exact_paper_dataset_bundle(
        training_config
    )
    target_scope_dictionary = resolve_target_scope_dictionary(summary_dictionary)

    split_manifest_dictionary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "source_validation_summary_path": shared_training_infrastructure.format_project_relative_path(
            output_directory / "validation_summary.yaml"
        ),
        "source_training_config_path": shared_training_infrastructure.format_project_relative_path(
            training_config_path
        ),
        "source_run_metadata_path": shared_training_infrastructure.format_project_relative_path(
            run_metadata_path
        ),
        "source_model_bundle_path": shared_training_infrastructure.format_project_relative_path(
            output_directory / exact_paper_model_bank_support.EXACT_MODEL_BANK_FILENAME
        ),
        "dataset_snapshot_path": shared_training_infrastructure.format_project_relative_path(
            archive_root / "data" / CANONICAL_DATASET_SNAPSHOT_FILENAME
        ),
        "source_dataframe_path": str(training_config["paths"]["source_dataframe_path"]).replace(
            "\\", "/"
        ),
        "source_dataframe_sha256": str(dataset_manifest_dictionary["source_dataframe_sha256"]),
        "filtered_dataframe_sha256": str(dataset_manifest_dictionary["dataset_snapshot_sha256"]),
        "filtered_row_count": int(summary_dictionary["dataset"]["filtered_row_count"]),
        "train_row_count": int(summary_dictionary["dataset"]["train_row_count"]),
        "test_row_count": int(summary_dictionary["dataset"]["test_row_count"]),
        "feature_name_list": list(summary_dictionary["dataset"]["feature_name_list"]),
        "target_name_list": list(summary_dictionary["dataset"]["target_name_list"]),
        "test_size": float(summary_dictionary["dataset"]["test_size"]),
        "random_seed": int(summary_dictionary["dataset"]["random_seed"]),
        "maximum_deg": float(summary_dictionary["dataset"]["maximum_deg"]),
        "target_scope_mode": str(target_scope_dictionary["mode"]),
        "include_phase_zero": bool(target_scope_dictionary["include_phase_zero"]),
        "harmonic_order_filter": list(target_scope_dictionary["harmonic_order_filter"]),
        "train_filtered_row_indices": [int(index) for index in dataset_bundle.train_feature_matrix.index.tolist()],
        "test_filtered_row_indices": [int(index) for index in dataset_bundle.test_feature_matrix.index.tolist()],
    }
    SPLIT_MANIFEST_CACHE[run_instance_id] = dict(split_manifest_dictionary)
    return split_manifest_dictionary


def save_yaml(path: Path, payload: dict[str, Any]) -> None:

    """Save one YAML payload with repository-normalized formatting."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=True)


def format_archive_metric_value(metric_value: float) -> str:

    """Format one exact metric value for archive-facing Markdown tables."""

    return exact_paper_model_bank_support.format_exact_paper_metric_value(metric_value)


def prepare_archive_root(archive_root: Path) -> None:

    """Create a clean archive root for one family."""

    if archive_root.exists():
        shutil.rmtree(archive_root)
    (archive_root / "onnx" / "amplitude").mkdir(parents=True, exist_ok=True)
    (archive_root / "onnx" / "phase").mkdir(parents=True, exist_ok=True)
    (archive_root / "python" / "amplitude").mkdir(parents=True, exist_ok=True)
    (archive_root / "python" / "phase").mkdir(parents=True, exist_ok=True)
    (archive_root / "data").mkdir(parents=True, exist_ok=True)
    (archive_root / "source_runs").mkdir(parents=True, exist_ok=True)


def build_family_archive(
    paper_family_code: str,
    accepted_metric_list: list[AcceptedTargetMetric],
    summary_dictionary_list: list[dict[str, Any]],
    dataset_snapshot_text: str,
    canonical_dataset_manifest_dictionary: dict[str, Any],
) -> dict[str, Any]:

    """Build the complete reference archive for one paper-facing family."""

    implementation_family_code = FAMILY_IMPLEMENTATION_CODE_MAP[paper_family_code]
    archive_folder_name = FAMILY_ARCHIVE_FOLDER_MAP[paper_family_code]
    archive_root = TRACK1_REFERENCE_FORWARD_ROOT / archive_folder_name
    existing_reference_inventory = load_existing_reference_inventory(archive_root)
    existing_reference_entry_map = build_existing_reference_entry_map(
        existing_reference_inventory
    )
    existing_dataset_snapshot_path = archive_root / "data" / CANONICAL_DATASET_SNAPSHOT_FILENAME
    existing_dataset_snapshot_text = None
    existing_dataset_manifest_dictionary = None
    if existing_dataset_snapshot_path.exists():
        existing_dataset_snapshot_text = existing_dataset_snapshot_path.read_text(
            encoding="utf-8"
        )
    existing_dataset_manifest_path = archive_root / "dataset_snapshot_manifest.yaml"
    existing_dataset_manifest_dictionary = load_existing_yaml_dictionary(
        existing_dataset_manifest_path
    )

    prepare_archive_root(archive_root)

    dataset_snapshot_output_path = (
        archive_root / "data" / CANONICAL_DATASET_SNAPSHOT_FILENAME
    )
    dataset_snapshot_to_write = dataset_snapshot_text
    dataset_manifest_dictionary = dict(canonical_dataset_manifest_dictionary)
    if (
        existing_dataset_snapshot_text is not None
        and existing_dataset_manifest_dictionary is not None
    ):
        dataset_snapshot_to_write = existing_dataset_snapshot_text
        dataset_manifest_dictionary = dict(existing_dataset_manifest_dictionary)
    dataset_snapshot_output_path.write_text(
        dataset_snapshot_to_write,
        encoding="utf-8",
        newline="\n",
    )
    dataset_manifest_dictionary["dataset_snapshot_path"] = shared_training_infrastructure.format_project_relative_path(
        dataset_snapshot_output_path
    )
    save_yaml(archive_root / "dataset_snapshot_manifest.yaml", dataset_manifest_dictionary)

    amplitude_target_entry_list: list[dict[str, Any]] = []
    phase_target_entry_list: list[dict[str, Any]] = []
    all_reference_model_entry_list: list[dict[str, Any]] = []
    source_run_id_set: set[str] = set()
    source_config_path_set: set[str] = set()

    family_metric_list = [
        accepted_metric
        for accepted_metric in accepted_metric_list
        if accepted_metric.paper_family_code == paper_family_code
    ]
    for accepted_metric in family_metric_list:
        existing_reference_entry = existing_reference_entry_map.get(accepted_metric.target_name)
        preferred_run_instance_id = None
        if existing_reference_entry is not None:
            existing_entry_mae = existing_reference_entry.get("benchmark_mae")
            existing_entry_rmse = existing_reference_entry.get("benchmark_rmse")
            if existing_entry_mae is not None and existing_entry_rmse is not None:
                existing_mae_value = float(existing_entry_mae)
                existing_rmse_value = float(existing_entry_rmse)
                if entry_metrics_match_visible_benchmark(
                    existing_mae_value,
                    existing_rmse_value,
                    accepted_metric,
                ):
                    preferred_run_instance_id = str(
                        existing_reference_entry.get("source_run_instance_id", "")
                    )
                    if not preferred_run_instance_id:
                        preferred_run_instance_id = None

        summary_dictionary, target_metric_entry = select_canonical_summary_for_target(
            accepted_metric,
            summary_dictionary_list,
            preferred_run_instance_id=preferred_run_instance_id,
        )

        run_instance_id = str(summary_dictionary["experiment"]["run_instance_id"])
        output_directory = shared_training_infrastructure.resolve_project_relative_path(
            summary_dictionary["experiment"]["output_directory"]
        )
        training_config_path = output_directory / "training_config.yaml"
        target_scope_dictionary = resolve_target_scope_dictionary(summary_dictionary)
        run_metadata_path = output_directory / "run_metadata.yaml"
        validation_summary_path = output_directory / "validation_summary.yaml"
        source_config_path = str(summary_dictionary["config_path"]).replace("\\", "/")

        export_target_entry = resolve_family_export_target_entry(
            summary_dictionary,
            implementation_family_code,
            accepted_metric.target_name,
        )
        source_export_path = shared_training_infrastructure.resolve_project_relative_path(
            export_target_entry["export_path"]
        )
        export_target_name = str(export_target_entry["export_target_name"])
        archived_onnx_path = (
            archive_root
            / "onnx"
            / accepted_metric.target_kind
            / source_export_path.name
        )
        copy_file(source_export_path, archived_onnx_path)

        target_estimator = resolve_target_estimator(
            summary_dictionary,
            implementation_family_code,
            accepted_metric.target_name,
        )
        python_filename = (
            f"{exact_paper_model_bank_support.EXACT_FAMILY_ESTIMATOR_NAME_MAP[implementation_family_code]}_"
            f"{export_target_name}.pkl"
        )
        archived_python_path = (
            archive_root
            / "python"
            / accepted_metric.target_kind
            / python_filename
        )
        with archived_python_path.open("wb") as output_file:
            pickle.dump(target_estimator, output_file, protocol=5)

        archive_source_run_root = archive_root / "source_runs" / run_instance_id
        copy_file(
            training_config_path,
            archive_source_run_root / "training_config.snapshot.yaml",
        )
        copy_file(
            run_metadata_path,
            archive_source_run_root / "run_metadata.snapshot.yaml",
        )
        split_manifest_dictionary = build_split_manifest_dictionary(
            archive_root,
            summary_dictionary,
            run_instance_id,
            dataset_manifest_dictionary,
        )
        save_yaml(archive_source_run_root / "split_manifest.yaml", split_manifest_dictionary)

        reference_model_entry = {
            "target_name": accepted_metric.target_name,
            "target_kind": accepted_metric.target_kind,
            "harmonic_order": int(accepted_metric.harmonic_order),
            "benchmark_mae": float(target_metric_entry["mae"]),
            "benchmark_rmse": float(target_metric_entry["rmse"]),
            "source_run_instance_id": run_instance_id,
            "source_config_path": source_config_path,
            "source_export_path": shared_training_infrastructure.format_project_relative_path(
                source_export_path
            ),
            "archived_model_path": shared_training_infrastructure.format_project_relative_path(
                archived_onnx_path
            ),
            "export_estimator_name": str(export_target_entry["export_estimator_name"]),
            "surrogate_strategy": str(export_target_entry["surrogate_strategy"]),
            "source_validation_summary_path": shared_training_infrastructure.format_project_relative_path(
                validation_summary_path
            ),
            "source_training_config_snapshot_path": shared_training_infrastructure.format_project_relative_path(
                archive_source_run_root / "training_config.snapshot.yaml"
            ),
            "source_run_metadata_snapshot_path": shared_training_infrastructure.format_project_relative_path(
                archive_source_run_root / "run_metadata.snapshot.yaml"
            ),
            "source_model_bundle_path": shared_training_infrastructure.format_project_relative_path(
                output_directory / exact_paper_model_bank_support.EXACT_MODEL_BANK_FILENAME
            ),
            "split_manifest_path": shared_training_infrastructure.format_project_relative_path(
                archive_source_run_root / "split_manifest.yaml"
            ),
            "dataset_snapshot_path": shared_training_infrastructure.format_project_relative_path(
                dataset_snapshot_output_path
            ),
            "dataset_snapshot_sha256": str(dataset_manifest_dictionary["dataset_snapshot_sha256"]),
            "python_model_path": shared_training_infrastructure.format_project_relative_path(
                archived_python_path
            ),
            "python_model_serialization": "pickle_protocol_5",
            "python_estimator_class_name": type(target_estimator).__name__,
            "python_model_sha256": compute_sha256(archived_python_path),
            "archived_model_sha256": compute_sha256(archived_onnx_path),
            "feature_name_list": list(summary_dictionary["dataset"]["feature_name_list"]),
            "source_run_target_name_list": list(summary_dictionary["dataset"]["target_name_list"]),
            "filtered_row_count": int(summary_dictionary["dataset"]["filtered_row_count"]),
            "train_row_count": int(summary_dictionary["dataset"]["train_row_count"]),
            "test_row_count": int(summary_dictionary["dataset"]["test_row_count"]),
            "test_size": float(summary_dictionary["dataset"]["test_size"]),
            "random_seed": int(summary_dictionary["dataset"]["random_seed"]),
            "maximum_deg": float(summary_dictionary["dataset"]["maximum_deg"]),
            "target_scope_mode": str(target_scope_dictionary["mode"]),
            "harmonic_order_filter": list(target_scope_dictionary["harmonic_order_filter"]),
            "exact_estimator_params": normalize_yaml_value(target_estimator.get_params()),
            "training_metric_mae": float(target_metric_entry["mae"]),
            "training_metric_rmse": float(target_metric_entry["rmse"]),
            "training_metric_mse": float(target_metric_entry["mse"]),
            "training_metric_mape_percent": float(target_metric_entry["mape_percent"]),
        }
        all_reference_model_entry_list.append(reference_model_entry)
        if accepted_metric.target_kind == "amplitude":
            amplitude_target_entry_list.append(reference_model_entry)
        else:
            phase_target_entry_list.append(reference_model_entry)

        source_run_id_set.add(run_instance_id)
        source_config_path_set.add(source_config_path)

    amplitude_target_entry_list.sort(key=lambda entry: int(entry["harmonic_order"]))
    phase_target_entry_list.sort(key=lambda entry: int(entry["harmonic_order"]))
    all_reference_model_entry_list.sort(
        key=lambda entry: (entry["target_kind"], int(entry["harmonic_order"]))
    )

    reference_inventory_dictionary = {
        "schema_version": 1,
        "topic": f"rcim_track1_{paper_family_code.lower()}_reference_models",
        "paper_family_name": paper_family_code,
        "implementation_family_name": implementation_family_code,
        "archive_scope": {
            "amplitude_harmonic_order_list": [int(entry["harmonic_order"]) for entry in amplitude_target_entry_list],
            "phase_harmonic_order_list": [int(entry["harmonic_order"]) for entry in phase_target_entry_list],
        },
        "canonical_selection_rule": (
            "when several runs reproduce the same accepted benchmark metric pair, "
            "pin the earliest stable canonical source run and keep later campaigns "
            "only when they introduce the accepted improvement."
        ),
        "source_code": {
            "validation_script": "scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py",
            "support_module": "scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py",
        },
        "source_data": {
            "dataframe_path": str(dataset_manifest_dictionary["source_dataframe_path"]).replace("\\", "/"),
            "recovered_reference_onnx_root": (
                "reference/rcim_ml_compensation_recovered_assets/models/"
                "exact_onnx_paper_release"
            ),
        },
        "notes": [
            "phase harmonic 0 is intentionally excluded from the curated Track 1 paper-facing archive.",
            "the archive pins the accepted family row currently visible in Tables 2-5 of the canonical benchmark.",
        ],
        "reference_models": all_reference_model_entry_list,
        "python_archive_format": "pickle_protocol_5_single_target_estimators",
        "dataset_snapshot_path": shared_training_infrastructure.format_project_relative_path(
            dataset_snapshot_output_path
        ),
        "dataset_snapshot_manifest_path": shared_training_infrastructure.format_project_relative_path(
            archive_root / "dataset_snapshot_manifest.yaml"
        ),
        "source_run_count": len(source_run_id_set),
    }
    save_yaml(archive_root / "reference_inventory.yaml", reference_inventory_dictionary)

    archive_readme_text = build_family_archive_readme(
        paper_family_code,
        implementation_family_code,
        amplitude_target_entry_list,
        phase_target_entry_list,
        source_run_id_set,
        source_config_path_set,
    )
    (archive_root / "README.md").write_text(
        archive_readme_text,
        encoding="utf-8",
        newline="\n",
    )

    return {
        "paper_family_code": paper_family_code,
        "implementation_family_code": implementation_family_code,
        "archive_root": archive_root,
        "amplitude_entries": amplitude_target_entry_list,
        "phase_entries": phase_target_entry_list,
        "source_run_id_list": sorted(source_run_id_set),
        "source_config_path_list": sorted(source_config_path_set),
    }


def build_family_archive_readme(
    paper_family_code: str,
    implementation_family_code: str,
    amplitude_target_entry_list: list[dict[str, Any]],
    phase_target_entry_list: list[dict[str, Any]],
    source_run_id_set: set[str],
    source_config_path_set: set[str],
) -> str:

    """Build the archive README for one family."""

    total_model_count = len(amplitude_target_entry_list) + len(phase_target_entry_list)
    phase_harmonic_text = ", ".join(
        str(entry["harmonic_order"]) for entry in phase_target_entry_list
    )
    amplitude_harmonic_text = ", ".join(
        str(entry["harmonic_order"]) for entry in amplitude_target_entry_list
    )
    source_run_line_list = [
        f"- `{run_instance_id}`" for run_instance_id in sorted(source_run_id_set)
    ]
    source_config_line_list = [
        f"- `{config_path}`" for config_path in sorted(source_config_path_set)
    ]

    note_line_list: list[str] = []
    if paper_family_code == "SVM":
        note_line_list.extend(
            [
                "",
                "Important naming note:",
                "",
                "- the paper family name is `SVM`;",
                "- the repository implementation family is `SVR`;",
                "- the archived ONNX files therefore retain the implementation-side `SVR_*` filenames.",
            ]
        )

    return "\n".join(
        [
            f"# {paper_family_code} Reference Models",
            "",
            f"This archive stores the canonical `{paper_family_code}` Track 1 reference model artifacts that",
            "reproduce the currently accepted repository-owned family row in",
            "`doc/reports/analysis/RCIM Paper Reference Benchmark.md`.",
            *note_line_list,
            "",
            "Archive scope:",
            "",
            f"- `{len(amplitude_target_entry_list)}` amplitude reference models for harmonics `{amplitude_harmonic_text}`;",
            f"- `{len(phase_target_entry_list)}` phase reference models for harmonics `{phase_harmonic_text}`;",
            f"- phase harmonic `0` is intentionally excluded because it is not part of the Track 1 paper-facing `{total_model_count}`-model family archive.",
            "",
            "## Canonical Selection Rule",
            "",
            "The canonical reference rule for this archive is:",
            "",
            "1. choose the exact run whose family-target metrics reproduce the currently accepted benchmark cell values for that target;",
            "2. when several runs reproduce the same accepted metric pair, prefer the earliest stable canonical source run;",
            "3. when a later Track 1 campaign introduced the accepted improvement, pin that later run explicitly instead of the older baseline;",
            "4. when a later campaign merely reproduces the same accepted value, retain the earlier canonical source run.",
            "",
            "## Source Surface",
            "",
            "Current pinned source runs:",
            "",
            *source_run_line_list,
            "",
            "Canonical reconstruction config paths represented in this archive:",
            "",
            *source_config_line_list,
            "",
            "## Training And Reconstruction References",
            "",
            "Canonical training and validation code:",
            "",
            "- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py`",
            "- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`",
            "",
            "Canonical reconstruction inputs:",
            "",
            "- dataframe source:",
            "  `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv`",
            "- recovered reference ONNX root:",
            "  `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`",
            "",
            "## Inventory Files",
            "",
            "- machine-readable inventory:",
            "  `reference_inventory.yaml`",
            "- dataset snapshot manifest:",
            "  `dataset_snapshot_manifest.yaml`",
            "- dataset snapshot copy:",
            "  `data/filtered_dataframe_deg_le_35.csv`",
            "- Python estimator archive:",
            "  `python/amplitude/*.pkl`",
            "  `python/phase/*.pkl`",
            "- source-run reconstruction manifests:",
            "  `source_runs/<run_instance_id>/split_manifest.yaml`",
            "- source-run config and metadata snapshots:",
            "  `source_runs/<run_instance_id>/training_config.snapshot.yaml`",
            "  `source_runs/<run_instance_id>/run_metadata.snapshot.yaml`",
            "- benchmark-facing canonical report:",
            "  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`",
            "",
            "## Full Regeneration Coverage",
            "",
            "The archive is intended to support deterministic reconstruction of the",
            f"accepted repository-owned `{paper_family_code}` benchmark row.",
            "",
            f"For each of the `{total_model_count}` canonical targets, the archive records:",
            "",
            "- the accepted benchmark metrics;",
            "- the canonical source validation run;",
            "- the archived ONNX export path;",
            "- the archived Python pickle path for the fitted estimator;",
            "- the exact fitted estimator class and parameter dictionary;",
            "- the filtered dataset snapshot hash;",
            "- the feature list and target list;",
            "- the train/test row counts and exact filtered row indices;",
            "- the test size, random seed, harmonic filter, and target-scope mode;",
            "- the source config snapshot and run metadata snapshot;",
            "- the immutable source bundle path that contained the fitted estimator.",
            "",
            "This means the repository preserves both deployment-facing and Python-facing",
            f"access paths for the accepted `{paper_family_code}` reference row:",
            "",
            "- `onnx/` via `onnx/amplitude/*.onnx` and `onnx/phase/*.onnx`;",
            "- Python-side fitted estimator access via `python/amplitude/*.pkl` and `python/phase/*.pkl`.",
            "",
        ]
    )


def build_benchmark_family_archive_section(
    archive_summary_list: list[dict[str, Any]],
) -> str:

    """Build the benchmark family-archive appendix sections."""

    section_line_list: list[str] = []
    for archive_summary in archive_summary_list:
        paper_family_code = str(archive_summary["paper_family_code"])
        implementation_family_code = str(archive_summary["implementation_family_code"])
        archive_root = Path(archive_summary["archive_root"])
        amplitude_entry_list = list(archive_summary["amplitude_entries"])
        phase_entry_list = list(archive_summary["phase_entries"])
        source_config_path_list = list(archive_summary["source_config_path_list"])

        section_line_list.extend(
            [
                f"### {paper_family_code} Reference Model Inventory",
                "",
                f"The accepted repository-owned `{paper_family_code}` row is now pinned to an explicit curated",
                f"set of `{len(amplitude_entry_list) + len(phase_entry_list)}` archived model artifacts:",
                "",
                MD013_DISABLE,
                "- archive root:",
                f"  `{shared_training_infrastructure.format_project_relative_path(archive_root)}`",
                "- machine-readable inventory:",
                f"  `{shared_training_infrastructure.format_project_relative_path(archive_root / 'reference_inventory.yaml')}`",
                "- dedicated archive note:",
                f"  `{shared_training_infrastructure.format_project_relative_path(archive_root / 'README.md')}`",
                "- dataset snapshot manifest:",
                f"  `{shared_training_infrastructure.format_project_relative_path(archive_root / 'dataset_snapshot_manifest.yaml')}`",
                "",
                "Full regeneration coverage:",
                "",
                "- the archive stores both deployment-facing `ONNX` exports and Python-usable fitted estimator pickles for the same accepted targets;",
                "- each target entry in `reference_inventory.yaml` records the exact fitted estimator parameters, source bundle path, dataset snapshot hash, feature list, target list, train/test row counts, split indices, test size, random seed, harmonic filter, and target-scope mode;",
                "- source-run config snapshots and run-metadata snapshots are copied under the archive `source_runs/` subtree, making the accepted family row reconstructible without implicit notebook memory or manual campaign-folder inspection.",
                "",
                "Selection rule:",
                "",
                f"- when several runs reproduce the same accepted `{paper_family_code}` target metrics, the repository pins the earliest stable canonical source run;",
                "- later Track 1 repair or closure runs are pinned only for harmonics whose accepted benchmark value improved after the older stable baseline.",
                "",
                "Important implementation note:",
                "",
                f"- paper family name: `{paper_family_code}`",
                f"- repository implementation family: `{implementation_family_code}`",
                "- the archive keeps the original Python-side fitted estimator identity even when the deployment export uses a surrogate surface for ONNX compatibility.",
                "",
                f"#### {paper_family_code} Reference Amplitude Models",
                "",
                "| Target | Harmonic | Accepted MAE | Accepted RMSE | Source Run | Export Estimator | Surrogate | Archived Model |",
                "| --- | ---: | ---: | ---: | --- | --- | --- | --- |",
            ]
        )
        for entry in amplitude_entry_list:
            section_line_list.append(
                "| "
                f"`{entry['target_name']}` | "
                f"`{entry['harmonic_order']}` | "
                f"`{format_archive_metric_value(float(entry['benchmark_mae']))}` | "
                f"`{format_archive_metric_value(float(entry['benchmark_rmse']))}` | "
                f"`{entry['source_run_instance_id']}` | "
                f"`{entry['export_estimator_name']}` | "
                f"`{entry['surrogate_strategy']}` | "
                f"`{entry['archived_model_path']}` |"
            )

        section_line_list.extend(
            [
                "",
                f"#### {paper_family_code} Reference Phase Models",
                "",
                "| Target | Harmonic | Accepted MAE | Accepted RMSE | Source Run | Export Estimator | Surrogate | Archived Model |",
                "| --- | ---: | ---: | ---: | --- | --- | --- | --- |",
            ]
        )
        for entry in phase_entry_list:
            section_line_list.append(
                "| "
                f"`{entry['target_name']}` | "
                f"`{entry['harmonic_order']}` | "
                f"`{format_archive_metric_value(float(entry['benchmark_mae']))}` | "
                f"`{format_archive_metric_value(float(entry['benchmark_rmse']))}` | "
                f"`{entry['source_run_instance_id']}` | "
                f"`{entry['export_estimator_name']}` | "
                f"`{entry['surrogate_strategy']}` | "
                f"`{entry['archived_model_path']}` |"
            )

        section_line_list.extend(
            [
                "",
                "Reconstruction references:",
                "",
            ]
        )
        for source_config_path in source_config_path_list:
            section_line_list.append(f"- `{source_config_path}`")
        section_line_list.extend(
            [
                "",
                MD013_ENABLE,
                "",
            ]
        )

    return "\n".join(section_line_list).rstrip() + "\n"


def replace_benchmark_archive_section(
    benchmark_text: str,
    replacement_section_text: str,
) -> str:

    """Replace the generated benchmark archive appendix block."""

    pattern = re.compile(
        rf"{re.escape(TRACK1_ARCHIVE_SECTION_START_HEADING)}\n.*?(?=\n{re.escape(TRACK1_ARCHIVE_SECTION_END_HEADING)})",
        re.DOTALL,
    )
    return pattern.sub(replacement_section_text, benchmark_text, count=1)


def update_track1_reference_readme(archive_summary_list: list[dict[str, Any]]) -> None:

    """Update the Track 1 paper-reference root README."""

    current_family_archive_line_list = [
        f"- `{FAMILY_ARCHIVE_FOLDER_MAP[archive_summary['paper_family_code']]}/`"
        for archive_summary in archive_summary_list
    ]
    readme_text = "\n".join(
        [
            "# RCIM Track 1 Paper Reference Models",
            "",
            "This folder groups curated paper-reference model archives for the canonical",
            "`Track 1` RCIM paper-reimplementation branch.",
            "",
            "Current family archives:",
            "",
            *current_family_archive_line_list,
            "",
            "Canonical family archive template:",
            "",
            "- `forward/<family>_reference_models/README.md`",
            "- `forward/<family>_reference_models/reference_inventory.yaml`",
            "- `forward/<family>_reference_models/onnx/amplitude/`",
            "- `forward/<family>_reference_models/onnx/phase/`",
            "- `forward/<family>_reference_models/python/amplitude/`",
            "- `forward/<family>_reference_models/python/phase/`",
            "- `forward/<family>_reference_models/data/`",
            "- `forward/<family>_reference_models/dataset_snapshot_manifest.yaml`",
            "- `forward/<family>_reference_models/source_runs/<run_instance_id>/training_config.snapshot.yaml`",
            "- `forward/<family>_reference_models/source_runs/<run_instance_id>/run_metadata.snapshot.yaml`",
            "- `forward/<family>_reference_models/source_runs/<run_instance_id>/split_manifest.yaml`",
            "",
            "Benchmark integration rule for every future family archive:",
            "",
            "- add one dedicated family section to",
            "  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;",
            "- list the accepted `Track 1` targets, accepted metrics, canonical source run,",
            "  archived `ONNX` path, and any surrogate-export note;",
            "- point the family section to the archive root, inventory, dataset snapshot",
            "  manifest, and reconstruction references.",
            "",
            "Current Track 1 family archive rollout under this standard:",
            "",
            *current_family_archive_line_list,
            "",
            "The current repository now treats all listed Track 1 family archives as",
            "canonical benchmark assets. The `svm_reference_models/` package remains the",
            "template instance that originally established this contract.",
            "",
        ]
    )
    TRACK1_REFERENCE_README_PATH.write_text(
        readme_text,
        encoding="utf-8",
        newline="\n",
    )


def update_models_readme(archive_summary_list: list[dict[str, Any]]) -> None:

    """Update the high-level models README current archive list."""

    archive_line_list = [
        f"- `paper_reference/rcim_track1/{FAMILY_ARCHIVE_FOLDER_MAP[archive_summary['paper_family_code']]}/`"
        for archive_summary in archive_summary_list
    ]
    readme_text = "\n".join(
        [
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
            *archive_line_list,
            "",
        ]
    )
    MODELS_README_PATH.write_text(
        readme_text,
        encoding="utf-8",
        newline="\n",
    )


def update_models_gitignore() -> None:

    """Update models/.gitignore so every Track 1 family archive is tracked."""

    gitignore_text = "\n".join(
        [
            "*",
            "!README.md",
            "!.gitignore",
            "!checkpoints/",
            "!checkpoints/.gitkeep",
            "!exported/",
            "!exported/.gitkeep",
            "!paper_reference/",
            "!paper_reference/README.md",
            "!paper_reference/rcim_track1/",
            "!paper_reference/rcim_track1/README.md",
            "!paper_reference/rcim_track1/*_reference_models/",
            "!paper_reference/rcim_track1/*_reference_models/README.md",
            "!paper_reference/rcim_track1/*_reference_models/reference_inventory.yaml",
            "!paper_reference/rcim_track1/*_reference_models/dataset_snapshot_manifest.yaml",
            "!paper_reference/rcim_track1/*_reference_models/onnx/",
            "!paper_reference/rcim_track1/*_reference_models/onnx/amplitude/",
            "!paper_reference/rcim_track1/*_reference_models/onnx/amplitude/*.onnx",
            "!paper_reference/rcim_track1/*_reference_models/onnx/phase/",
            "!paper_reference/rcim_track1/*_reference_models/onnx/phase/*.onnx",
            "!paper_reference/rcim_track1/*_reference_models/python/",
            "!paper_reference/rcim_track1/*_reference_models/python/amplitude/",
            "!paper_reference/rcim_track1/*_reference_models/python/amplitude/*.pkl",
            "!paper_reference/rcim_track1/*_reference_models/python/phase/",
            "!paper_reference/rcim_track1/*_reference_models/python/phase/*.pkl",
            "!paper_reference/rcim_track1/*_reference_models/data/",
            "!paper_reference/rcim_track1/*_reference_models/data/*.csv",
            "!paper_reference/rcim_track1/*_reference_models/source_runs/",
            "!paper_reference/rcim_track1/*_reference_models/source_runs/**/",
            "!paper_reference/rcim_track1/*_reference_models/source_runs/**/*.yaml",
            "",
        ]
    )
    MODELS_GITIGNORE_PATH.write_text(
        gitignore_text,
        encoding="utf-8",
        newline="\n",
    )


def refresh_track1_family_reference_archives(
    selected_family_code_list: list[str] | None = None,
) -> list[dict[str, Any]]:

    """Refresh the curated Track 1 family reference archives."""

    family_code_list = selected_family_code_list or list(FAMILY_ORDER)
    summary_dictionary_list = collect_validation_summary_dictionary_list()
    accepted_metric_list = build_accepted_target_metric_list(family_code_list)
    dataset_snapshot_text, canonical_dataset_manifest_dictionary = (
        build_canonical_dataset_snapshot_bundle()
    )

    archive_summary_list = []
    for family_code in family_code_list:
        archive_summary = build_family_archive(
            family_code,
            accepted_metric_list,
            summary_dictionary_list,
            dataset_snapshot_text,
            canonical_dataset_manifest_dictionary,
        )
        archive_summary_list.append(archive_summary)

    update_models_gitignore()
    update_models_readme(archive_summary_list)
    update_track1_reference_readme(archive_summary_list)

    benchmark_text = BENCHMARK_REPORT_PATH.read_text(encoding="utf-8")
    replacement_section_text = build_benchmark_family_archive_section(archive_summary_list)
    benchmark_text = replace_benchmark_archive_section(
        benchmark_text,
        replacement_section_text,
    )
    BENCHMARK_REPORT_PATH.write_text(
        benchmark_text,
        encoding="utf-8",
        newline="\n",
    )

    return archive_summary_list


def main() -> None:

    """Run the Track 1 family archive refresh CLI."""

    command_line_arguments = parse_command_line_arguments()
    selected_family_code_list = [
        family_code.upper() for family_code in command_line_arguments.family
    ]
    if selected_family_code_list:
        for family_code in selected_family_code_list:
            assert family_code in FAMILY_ORDER, f"Unsupported Track 1 family code | {family_code}"

    archive_summary_list = refresh_track1_family_reference_archives(
        selected_family_code_list=selected_family_code_list or None
    )
    refreshed_family_text = ", ".join(
        archive_summary["paper_family_code"] for archive_summary in archive_summary_list
    )
    print(
        "[DONE] Refreshed Track 1 family reference archives | "
        f"families={refreshed_family_text}"
    )


if __name__ == "__main__":
    main()
