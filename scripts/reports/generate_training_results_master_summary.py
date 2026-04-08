"""Generate the canonical training-results master summary report."""

from __future__ import annotations

# Import Python Utilities
import argparse, math, sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

PROJECT_PATH = Path(__file__).resolve().parents[2]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

DEFAULT_OUTPUT_MARKDOWN_PATH = PROJECT_PATH / "doc" / "reports" / "analysis" / "Training Results Master Summary.md"
DEFAULT_BACKLOG_PATH = PROJECT_PATH / "doc" / "running" / "te_model_live_backlog.md"
DEFAULT_ACTIVE_CAMPAIGN_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
DEFAULT_PROGRAM_REGISTRY_PATH = PROJECT_PATH / "output" / "registries" / "program" / "current_best_solution.yaml"
DEFAULT_FAMILY_REGISTRY_ROOT = PROJECT_PATH / "output" / "registries" / "families"
DEFAULT_TRAINING_RUN_ROOT = PROJECT_PATH / "output" / "training_runs"
DEFAULT_TRAINING_CAMPAIGN_ROOT = PROJECT_PATH / "output" / "training_campaigns"
DEFAULT_PAPER_REFERENCE_REPORT_PATH = PROJECT_PATH / "doc" / "reports" / "analysis" / "RCIM Paper Reference Benchmark.md"

TREE_MODEL_TYPE_SET = {"random_forest", "hist_gradient_boosting"}
NEURAL_MODEL_TYPE_SET = {"feedforward", "periodic_mlp", "residual_harmonic_mlp"}
PAPER_REFERENCE_DATA = {
    "dataset_sample_count": 1026,
    "input_axes": ["input speed", "applied torque", "oil temperature"],
    "prediction_validation_mean_percentage_error": [2.6, 3.1, 4.7],
    "selected_harmonics_primary": [0, 1, 39],
    "selected_harmonics_extended": [40, 78],
    "online_compensation": {
        "robot": {
            "best_rms_reduction_pct": 83.6,
            "best_max_reduction_pct": 54.7,
        },
        "cycloidal": {
            "best_rms_reduction_pct": 94.0,
            "best_max_reduction_pct": 91.7,
        },
    },
}


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser.

    Returns:
        Configured argument parser for the master-summary generator.
    """

    argument_parser = argparse.ArgumentParser(
        description=(
            "Generate the canonical training-results master summary from the "
            "current backlog, registries, and campaign artifacts."
        )
    )
    argument_parser.add_argument(
        "--output-markdown-path",
        default=str(DEFAULT_OUTPUT_MARKDOWN_PATH),
        help="Optional explicit Markdown output path.",
    )
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments.

    Returns:
        Parsed command-line namespace.
    """

    return build_argument_parser().parse_args()


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:

    """Load one YAML dictionary from disk.

    Args:
        input_path: YAML file path to load.

    Returns:
        Parsed YAML dictionary.
    """

    assert input_path.exists(), f"YAML path does not exist | {input_path}"
    with input_path.open("r", encoding="utf-8") as input_file:
        yaml_dictionary = yaml.safe_load(input_file)
    assert isinstance(yaml_dictionary, dict), f"YAML file must contain a dictionary | {input_path}"
    return yaml_dictionary


def read_text_file(input_path: Path) -> str:

    """Read one UTF-8 text file.

    Args:
        input_path: Text file path to read.

    Returns:
        File text content.
    """

    assert input_path.exists(), f"Text path does not exist | {input_path}"
    return input_path.read_text(encoding="utf-8")


def format_project_relative_path(path_value: Path | str | None) -> str:

    """Format a project-relative path string when possible.

    Args:
        path_value: Candidate path value.

    Returns:
        Repository-relative string when possible, otherwise the original path string.
    """

    if path_value in [None, ""]:
        return "N/A"

    candidate_path = Path(path_value)
    if not candidate_path.is_absolute():
        return candidate_path.as_posix()

    try:
        return candidate_path.resolve().relative_to(PROJECT_PATH).as_posix()
    except ValueError:
        return candidate_path.as_posix()


def resolve_existing_path(path_value: str | None) -> Path | None:

    """Resolve an existing local path from stored text.

    Args:
        path_value: Stored path string from one artifact.

    Returns:
        Existing local path when resolvable, otherwise `None`.
    """

    if path_value in [None, "", "N/A"]:
        return None

    candidate_path = Path(str(path_value))
    candidate_path_list = [candidate_path]
    if not candidate_path.is_absolute():
        candidate_path_list.append(PROJECT_PATH / candidate_path)

    for candidate in candidate_path_list:
        if candidate.exists():
            return candidate.resolve()

    return None


def parse_iso_datetime(datetime_text: str | None) -> datetime | None:

    """Parse one ISO-style datetime string.

    Args:
        datetime_text: Datetime string to parse.

    Returns:
        Parsed datetime when valid, otherwise `None`.
    """

    if datetime_text in [None, ""]:
        return None

    try:
        return datetime.fromisoformat(str(datetime_text).replace("Z", "+00:00"))
    except ValueError:
        return None


def format_timestamp(datetime_value: datetime | None) -> str:

    """Format one datetime for human-readable Markdown.

    Args:
        datetime_value: Datetime value to format.

    Returns:
        Formatted timestamp string.
    """

    if datetime_value is None:
        return "N/A"
    return datetime_value.strftime("%Y-%m-%d %H:%M:%S")


def format_float(value: Any, digits: int = 6) -> str:

    """Format one numeric value for Markdown.

    Args:
        value: Candidate numeric value.
        digits: Decimal precision.

    Returns:
        Formatted string or `N/A`.
    """

    if value in [None, ""]:
        return "N/A"
    try:
        return f"{float(value):.{digits}f}"
    except (TypeError, ValueError):
        return "N/A"


def format_parameter_count(value: Any) -> str:

    """Format one parameter-count value.

    Args:
        value: Candidate parameter count.

    Returns:
        Human-readable parameter count string.
    """

    if value in [None, ""]:
        return "N/A"
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return "N/A"


def format_duration_seconds(duration_seconds: float | None) -> str:

    """Format one duration in seconds.

    Args:
        duration_seconds: Raw duration in seconds.

    Returns:
        Compact human-readable duration string.
    """

    if duration_seconds is None:
        return "N/A"

    total_seconds = max(int(round(duration_seconds)), 0)
    hour_count, remaining_seconds = divmod(total_seconds, 3600)
    minute_count, second_count = divmod(remaining_seconds, 60)

    if hour_count > 0:
        return f"{hour_count}h {minute_count:02d}m {second_count:02d}s"
    if minute_count > 0:
        return f"{minute_count}m {second_count:02d}s"
    return f"{second_count}s"


def format_size_megabytes(size_megabytes: float | None) -> str:

    """Format one size value in megabytes.

    Args:
        size_megabytes: Size in megabytes.

    Returns:
        Compact human-readable size string.
    """

    if size_megabytes is None:
        return "N/A"
    if size_megabytes >= 1024.0:
        return f"{size_megabytes / 1024.0:.2f} GB"
    return f"{size_megabytes:.2f} MB"


def resolve_model_family(model_type: str | None, family_hint: str | None = None) -> str:

    """Resolve the canonical model-family name.

    Args:
        model_type: Stored model type.
        family_hint: Optional family hint from paths or metrics.

    Returns:
        Canonical model-family label.
    """

    if family_hint not in [None, ""]:
        return str(family_hint)

    if model_type is None:
        return "unknown"

    normalized_model_type = str(model_type)
    if normalized_model_type in TREE_MODEL_TYPE_SET:
        return "tree"
    return normalized_model_type


def classify_model_complexity(trainable_parameter_count: int | None, artifact_size_megabytes: float | None, model_family: str) -> str:

    """Classify model-side complexity.

    Args:
        trainable_parameter_count: Model parameter count when available.
        artifact_size_megabytes: Stored artifact size when available.
        model_family: Canonical family label.

    Returns:
        Compact complexity label.
    """

    if model_family == "tree" and artifact_size_megabytes is not None:
        if artifact_size_megabytes >= 1024.0:
            return "Extreme Artifact"
        if artifact_size_megabytes >= 256.0:
            return "Very Heavy Artifact"
        if artifact_size_megabytes >= 32.0:
            return "Heavy Artifact"
        if artifact_size_megabytes >= 4.0:
            return "Medium Artifact"
        return "Light Artifact"

    if trainable_parameter_count is None:
        return "Unknown"
    if trainable_parameter_count <= 500:
        return "Very Low"
    if trainable_parameter_count <= 10000:
        return "Low"
    if trainable_parameter_count <= 50000:
        return "Medium"
    if trainable_parameter_count <= 150000:
        return "High"
    return "Very High"


def classify_training_heaviness(duration_seconds: float | None) -> str:

    """Classify training-side heaviness.

    Args:
        duration_seconds: Known training duration.

    Returns:
        Compact training-cost label.
    """

    if duration_seconds is None:
        return "Unknown"
    if duration_seconds <= 120:
        return "Very Low"
    if duration_seconds <= 900:
        return "Low"
    if duration_seconds <= 2400:
        return "Medium"
    if duration_seconds <= 5400:
        return "High"
    return "Very High"


def build_sort_key(entry_dictionary: dict[str, Any], selection_policy: dict[str, Any]) -> tuple[float, float, float, float]:

    """Build one ranking sort key from the selection policy.

    Args:
        entry_dictionary: Candidate result entry.
        selection_policy: Ranking policy dictionary.

    Returns:
        Comparable tuple aligned with the repository ranking policy.
    """

    metric_name_list = [
        selection_policy.get("primary_metric", "test_mae"),
        selection_policy.get("first_tie_breaker", "test_rmse"),
        selection_policy.get("second_tie_breaker", "val_mae"),
        selection_policy.get("third_tie_breaker", "trainable_parameter_count"),
    ]

    key_value_list: list[float] = []
    for metric_name in metric_name_list:
        metric_value = entry_dictionary.get(str(metric_name))
        if metric_value in [None, ""]:
            key_value_list.append(math.inf)
            continue
        try:
            key_value_list.append(float(metric_value))
        except (TypeError, ValueError):
            key_value_list.append(math.inf)

    return tuple(key_value_list)  # type: ignore[return-value]


def extract_backlog_snapshot(backlog_text: str) -> dict[str, Any]:

    """Extract the key backlog snapshot fields from Markdown.

    Args:
        backlog_text: Live backlog Markdown text.

    Returns:
        Dictionary with current-status values, wave status lines, and low-priority families.
    """

    current_status_dictionary: dict[str, str] = {}
    wave_status_dictionary: dict[str, str] = {}
    exploratory_family_list: list[str] = []

    current_h2 = ""
    current_h3 = ""
    line_list = backlog_text.splitlines()

    for raw_line in line_list:
        stripped_line = raw_line.strip()
        if stripped_line.startswith("## "):
            current_h2 = stripped_line[3:].strip()
            current_h3 = ""
            continue
        if stripped_line.startswith("### "):
            current_h3 = stripped_line[4:].strip()
            continue

        if current_h2 == "Current Status" and stripped_line.startswith("- ") and ": " in stripped_line:
            label_text, value_text = stripped_line[2:].split(": ", maxsplit=1)
            current_status_dictionary[label_text.strip()] = value_text.strip()
            continue

        if current_h2 == "Wave Checklist" and current_h3 and stripped_line.startswith("- "):
            status_text = stripped_line[2:].strip()
            existing_status = wave_status_dictionary.get(current_h3)
            if existing_status is None:
                wave_status_dictionary[current_h3] = status_text
            else:
                wave_status_dictionary[current_h3] = f"{existing_status}; {status_text}"
            continue

        if current_h3 == "Explicit Low-Priority Exploratory Families" and stripped_line.startswith("Entry rule:"):
            current_h3 = ""
            continue

        if current_h3 == "Explicit Low-Priority Exploratory Families" and stripped_line.startswith("- "):
            exploratory_family_list.append(stripped_line[2:].strip().strip("`"))

    return {
        "current_status": current_status_dictionary,
        "wave_status": wave_status_dictionary,
        "exploratory_family_list": exploratory_family_list,
    }


def collect_campaign_artifacts() -> dict[str, Any]:

    """Collect campaign summaries and run-level metadata.

    Returns:
        Campaign summary list plus per-run metadata maps.
    """

    campaign_summary_list: list[dict[str, Any]] = []
    run_metadata_dictionary: dict[str, dict[str, Any]] = {}
    family_failure_dictionary: dict[str, list[dict[str, Any]]] = {}

    if not DEFAULT_TRAINING_CAMPAIGN_ROOT.exists():
        return {
            "campaign_summary_list": campaign_summary_list,
            "run_metadata_dictionary": run_metadata_dictionary,
            "family_failure_dictionary": family_failure_dictionary,
        }

    campaign_manifest_path_list = sorted(
        DEFAULT_TRAINING_CAMPAIGN_ROOT.glob("*/campaign_manifest.yaml"),
        key=lambda manifest_path: manifest_path.stat().st_mtime,
        reverse=True,
    )

    for campaign_manifest_path in campaign_manifest_path_list:

        # Load Campaign Artifacts
        manifest_dictionary = load_yaml_dictionary(campaign_manifest_path)
        campaign_directory = campaign_manifest_path.parent
        best_run_path = campaign_directory / "campaign_best_run.yaml"
        best_run_dictionary = load_yaml_dictionary(best_run_path) if best_run_path.exists() else {}
        best_entry_dictionary = best_run_dictionary.get("best_entry", {}) if isinstance(best_run_dictionary.get("best_entry", {}), dict) else {}

        run_list = manifest_dictionary.get("run_list", [])
        assert isinstance(run_list, list), f"Campaign run_list must be a list | {campaign_manifest_path}"
        completed_count = sum(isinstance(run_dictionary, dict) and run_dictionary.get("queue_status") == "completed" for run_dictionary in run_list)
        failed_count = sum(isinstance(run_dictionary, dict) and run_dictionary.get("queue_status") == "failed" for run_dictionary in run_list)

        # Build Campaign Summary
        campaign_summary_list.append(
            {
                "generated_at": parse_iso_datetime(str(manifest_dictionary.get("generated_at"))),
                "campaign_name": str(manifest_dictionary.get("campaign_name", campaign_directory.name)),
                "campaign_output_directory": format_project_relative_path(campaign_directory),
                "planning_report_path": str(manifest_dictionary.get("planning_report_path", "N/A")),
                "completed_count": completed_count,
                "failed_count": failed_count,
                "best_entry": best_entry_dictionary,
            }
        )

        # Index Run-Level Campaign Metadata
        for run_dictionary in run_list:
            if not isinstance(run_dictionary, dict):
                continue

            run_instance_id = str(run_dictionary.get("run_instance_id", ""))
            model_type = str(run_dictionary.get("model_type", ""))
            output_directory_text = str(run_dictionary.get("output_directory", ""))
            family_hint = None
            if output_directory_text not in [None, ""]:
                output_directory_parts = Path(output_directory_text).parts
                if "training_runs" in output_directory_parts:
                    training_runs_index = output_directory_parts.index("training_runs")
                    if len(output_directory_parts) > training_runs_index + 1:
                        family_hint = output_directory_parts[training_runs_index + 1]

            model_family = resolve_model_family(model_type, family_hint)
            run_metadata_dictionary[run_instance_id] = {
                "campaign_name": str(run_dictionary.get("campaign_name") or manifest_dictionary.get("campaign_name") or campaign_directory.name),
                "duration_seconds": run_dictionary.get("duration_seconds"),
                "queue_status": str(run_dictionary.get("queue_status", "")),
                "planning_report_path": str(run_dictionary.get("planning_report_path") or manifest_dictionary.get("planning_report_path") or "N/A"),
            }

            if str(run_dictionary.get("queue_status", "")) != "failed":
                continue

            family_failure_dictionary.setdefault(model_family, []).append(
                {
                    "campaign_name": str(run_dictionary.get("campaign_name") or manifest_dictionary.get("campaign_name") or campaign_directory.name),
                    "run_name": str(run_dictionary.get("run_name", "unknown_run")),
                    "model_type": model_type or "unknown",
                    "error_message": str(run_dictionary.get("error_message") or "N/A"),
                }
            )

    return {
        "campaign_summary_list": campaign_summary_list,
        "run_metadata_dictionary": run_metadata_dictionary,
        "family_failure_dictionary": family_failure_dictionary,
    }


def resolve_local_model_artifact_path(run_directory: Path) -> Path | None:

    """Resolve the main local model artifact path for one run.

    Args:
        run_directory: Immutable training-run directory.

    Returns:
        Local artifact path when found, otherwise `None`.
    """

    tree_model_path = run_directory / "tree_model.pkl"
    if tree_model_path.exists():
        return tree_model_path.resolve()

    checkpoint_directory = run_directory / "checkpoints"
    if checkpoint_directory.exists():
        checkpoint_path_list = sorted(checkpoint_directory.glob("*"), key=lambda path_value: path_value.stat().st_mtime, reverse=True)
        if checkpoint_path_list:
            return checkpoint_path_list[0].resolve()

    best_checkpoint_pointer_path = run_directory / "best_checkpoint_path.txt"
    if best_checkpoint_pointer_path.exists():
        stored_checkpoint_text = best_checkpoint_pointer_path.read_text(encoding="utf-8").strip()
        if stored_checkpoint_text:
            stored_checkpoint_name = Path(stored_checkpoint_text).name
            matching_checkpoint_path_list = list(run_directory.rglob(stored_checkpoint_name))
            if matching_checkpoint_path_list:
                return matching_checkpoint_path_list[0].resolve()

    return None


def collect_training_run_records(run_metadata_dictionary: dict[str, dict[str, Any]], selection_policy: dict[str, Any]) -> list[dict[str, Any]]:

    """Collect all training-run records from immutable run artifacts.

    Args:
        run_metadata_dictionary: Campaign-derived run metadata keyed by run instance id.
        selection_policy: Ranking policy dictionary.

    Returns:
        Sorted training-run record list.
    """

    training_run_record_list: list[dict[str, Any]] = []
    if not DEFAULT_TRAINING_RUN_ROOT.exists():
        return training_run_record_list

    metrics_path_list = sorted(DEFAULT_TRAINING_RUN_ROOT.glob("*/*/metrics_summary.yaml"))
    for metrics_path in metrics_path_list:

        # Load Metrics Snapshot
        metrics_dictionary = load_yaml_dictionary(metrics_path)
        experiment_dictionary = metrics_dictionary.get("experiment", {}) if isinstance(metrics_dictionary.get("experiment", {}), dict) else {}
        model_summary_dictionary = metrics_dictionary.get("model_summary", {}) if isinstance(metrics_dictionary.get("model_summary", {}), dict) else {}
        validation_metrics_dictionary = metrics_dictionary.get("validation_metrics", {}) if isinstance(metrics_dictionary.get("validation_metrics", {}), dict) else {}
        test_metrics_dictionary = metrics_dictionary.get("test_metrics", {}) if isinstance(metrics_dictionary.get("test_metrics", {}), dict) else {}

        run_directory = metrics_path.parent.resolve()
        model_family = resolve_model_family(
            str(experiment_dictionary.get("model_type", "")),
            metrics_path.parents[1].name,
        )
        run_instance_id = str(experiment_dictionary.get("run_instance_id", run_directory.name))
        run_metadata = run_metadata_dictionary.get(run_instance_id, {})
        model_artifact_path = resolve_local_model_artifact_path(run_directory)
        artifact_size_megabytes = None
        if model_artifact_path is not None:
            artifact_size_megabytes = model_artifact_path.stat().st_size / (1024.0 * 1024.0)

        trainable_parameter_count = model_summary_dictionary.get("trainable_parameter_count")
        try:
            trainable_parameter_count = int(trainable_parameter_count) if trainable_parameter_count not in [None, ""] else None
        except (TypeError, ValueError):
            trainable_parameter_count = None

        total_parameter_count = model_summary_dictionary.get("total_parameter_count")
        try:
            total_parameter_count = int(total_parameter_count) if total_parameter_count not in [None, ""] else None
        except (TypeError, ValueError):
            total_parameter_count = None

        record_dictionary = {
            "model_family": model_family,
            "model_type": str(experiment_dictionary.get("model_type", "unknown")),
            "run_name": str(experiment_dictionary.get("run_name", run_directory.name)),
            "run_instance_id": run_instance_id,
            "run_directory": run_directory,
            "metrics_path": metrics_path.resolve(),
            "report_path": run_directory / "training_test_report.md",
            "trainable_parameter_count": trainable_parameter_count,
            "total_parameter_count": total_parameter_count,
            "val_mae": validation_metrics_dictionary.get("val_mae"),
            "val_rmse": validation_metrics_dictionary.get("val_rmse"),
            "test_mae": test_metrics_dictionary.get("test_mae"),
            "test_rmse": test_metrics_dictionary.get("test_rmse"),
            "campaign_name": run_metadata.get("campaign_name"),
            "duration_seconds": run_metadata.get("duration_seconds"),
            "artifact_path": model_artifact_path,
            "artifact_size_megabytes": artifact_size_megabytes,
        }
        record_dictionary["complexity_label"] = classify_model_complexity(
            trainable_parameter_count,
            artifact_size_megabytes,
            model_family,
        )
        record_dictionary["training_heaviness_label"] = classify_training_heaviness(record_dictionary["duration_seconds"])
        training_run_record_list.append(record_dictionary)

    return sorted(training_run_record_list, key=lambda record_dictionary: (record_dictionary["model_family"], build_sort_key(record_dictionary, selection_policy)))


def collect_family_best_records() -> list[dict[str, Any]]:

    """Collect the latest best-entry snapshot for each model family.

    Returns:
        Family-best record list.
    """

    family_best_record_list: list[dict[str, Any]] = []
    if not DEFAULT_FAMILY_REGISTRY_ROOT.exists():
        return family_best_record_list

    for family_best_path in sorted(DEFAULT_FAMILY_REGISTRY_ROOT.glob("*/latest_family_best.yaml")):
        family_dictionary = load_yaml_dictionary(family_best_path)
        best_entry_dictionary = family_dictionary.get("best_entry", {})
        if not isinstance(best_entry_dictionary, dict):
            continue

        family_best_record_list.append(
            {
                "model_family": family_best_path.parent.name,
                "updated_at": parse_iso_datetime(str(family_dictionary.get("updated_at"))),
                "best_entry": best_entry_dictionary,
            }
        )

    return family_best_record_list


def extract_active_campaign_snapshot() -> dict[str, Any]:

    """Extract the active-campaign snapshot from persistent running state.

    Returns:
        Active-campaign dictionary.
    """

    if not DEFAULT_ACTIVE_CAMPAIGN_PATH.exists():
        return {
            "status": "missing",
            "campaign_name": "N/A",
            "family_set": set(),
            "launch_mode": "N/A",
        }

    active_campaign_dictionary = load_yaml_dictionary(DEFAULT_ACTIVE_CAMPAIGN_PATH)
    queue_config_path_list = active_campaign_dictionary.get("queue_config_path_list", [])
    family_set: set[str] = set()

    if isinstance(queue_config_path_list, list):
        for queue_config_path in queue_config_path_list:
            queue_config_text = str(queue_config_path)
            path_part_list = Path(queue_config_text).parts
            if "feedforward" in path_part_list:
                family_set.add("feedforward")
            if "residual_harmonic_mlp" in path_part_list or ("residual" in queue_config_text and "harmonic" in queue_config_text):
                family_set.add("residual_harmonic_mlp")
            if "periodic" in queue_config_text:
                family_set.add("periodic_mlp")
            if "harmonic" in queue_config_text and "residual" not in queue_config_text:
                family_set.add("harmonic_regression")
            if "hist_gbr" in queue_config_text or "random_forest" in queue_config_text:
                family_set.add("tree")

    return {
        "status": str(active_campaign_dictionary.get("status", "unknown")),
        "campaign_name": str(active_campaign_dictionary.get("campaign_name", "N/A")),
        "family_set": family_set,
        "launch_mode": str(active_campaign_dictionary.get("launch_mode", "N/A")),
        "planning_report_path": str(active_campaign_dictionary.get("planning_report_path", "N/A")),
    }


def build_family_role(model_family: str, best_entry_dictionary: dict[str, Any], program_best_entry: dict[str, Any], strongest_neural_family: str | None, active_family_set: set[str]) -> str:

    """Build one compact current-role label for a family.

    Args:
        model_family: Canonical family label.
        best_entry_dictionary: Family best-entry dictionary.
        program_best_entry: Program best-entry dictionary.
        strongest_neural_family: Strongest current neural family label.
        active_family_set: Families currently under active campaign work.

    Returns:
        Human-readable role label.
    """

    if best_entry_dictionary.get("run_instance_id") == program_best_entry.get("run_instance_id"):
        return "Current Global Winner"
    if strongest_neural_family == model_family:
        return "Strongest Neural Family"
    if model_family == "feedforward":
        return "Current Plain MLP Anchor"
    if model_family in active_family_set:
        return "Active Improvement"
    return "Implemented Benchmark"


def build_recent_change_label(campaign_summary: dict[str, Any], family_best_by_run_instance: dict[str, str], program_best_entry: dict[str, Any]) -> str:

    """Build the recent-change interpretation for one campaign.

    Args:
        campaign_summary: Campaign summary dictionary.
        family_best_by_run_instance: Map from run instance id to family label.
        program_best_entry: Program best-entry dictionary.

    Returns:
        Recent-change label.
    """

    best_entry_dictionary = campaign_summary.get("best_entry", {})
    if not isinstance(best_entry_dictionary, dict) or len(best_entry_dictionary) == 0:
        return "No winner artifact"

    run_instance_id = best_entry_dictionary.get("run_instance_id")
    if run_instance_id == program_best_entry.get("run_instance_id"):
        return "Updated global best"
    if run_instance_id in family_best_by_run_instance:
        return f"Updated {family_best_by_run_instance[run_instance_id]} family best"
    return "No family-best change"


def build_paper_alignment_status_list(
    program_best_entry: dict[str, Any], strongest_neural_family: str | None
) -> list[str]:

    """Build compact paper-alignment bullets.

    Args:
        program_best_entry: Current program-best registry entry.
        strongest_neural_family: Current strongest neural family.

    Returns:
        Markdown bullet lines for paper alignment status.
    """

    current_best_family = str(program_best_entry.get("model_family", "N/A"))
    current_best_model_type = str(program_best_entry.get("model_type", "N/A"))
    offline_alignment_text = (
        "Partially aligned: the current repository winner is tree-based "
        f"(`{current_best_model_type}` / family `{current_best_family}`), which is "
        "consistent with the paper's boosting/tree-heavy deployed predictors."
        if current_best_family == "tree"
        else "Not yet aligned: the current repository winner is not tree-based, "
        "while the paper deployment path is dominated by boosting/tree models."
    )

    neural_alignment_text = (
        f"Neural models remain secondary in the repository (`{strongest_neural_family or 'N/A'}`), "
        "which is also consistent with the paper not promoting a plain neural winner for deployment."
    )

    return [
        "- Offline benchmark scope remains `partially comparable` rather than like-for-like.",
        f"- {offline_alignment_text}",
        f"- {neural_alignment_text}",
        "- End-to-end paper comparison remains `not yet comparable` until repository-owned online compensation tests exist.",
    ]


def build_paper_reference_section(
    program_best_entry: dict[str, Any], strongest_neural_family: str | None
) -> list[str]:

    """Build the paper-reference benchmark section.

    Args:
        program_best_entry: Current program-best registry entry.
        strongest_neural_family: Current strongest neural family.

    Returns:
        Markdown lines for the paper-reference benchmark section.
    """

    robot_dictionary = PAPER_REFERENCE_DATA["online_compensation"]["robot"]
    cycloidal_dictionary = PAPER_REFERENCE_DATA["online_compensation"]["cycloidal"]
    current_best_family = str(program_best_entry.get("model_family", "N/A"))
    current_best_model_type = str(program_best_entry.get("model_type", "N/A"))
    current_best_run_name = str(program_best_entry.get("run_name", "N/A"))
    current_offline_verdict = "aligned" if current_best_family == "tree" else "not_aligned"

    return [
        "## Paper Reference Benchmark",
        "",
        "The repository benchmark paper is `reference/RCIM_ML-compensation.pdf`.",
        "At the current repository state, the comparison is explicitly `offline-only`. A real paper-equivalent comparison still requires repository-owned online compensation tests.",
        "",
        "### Extracted Paper Targets",
        "",
        f"- Paper dataset size: `{PAPER_REFERENCE_DATA['dataset_sample_count']}` operating-condition samples.",
        f"- Paper input axes: {', '.join(f'`{axis_name}`' for axis_name in PAPER_REFERENCE_DATA['input_axes'])}.",
        f"- Offline prediction target: TE-curve mean percentage error at or below `{max(PAPER_REFERENCE_DATA['prediction_validation_mean_percentage_error']):.1f}%` on unseen validation scenarios.",
        f"- Online `robot` compensation target: at least `{robot_dictionary['best_rms_reduction_pct']:.1f}%` TE RMS reduction.",
        f"- Online `cycloidal` compensation target: at least `{cycloidal_dictionary['best_rms_reduction_pct']:.1f}%` TE RMS reduction and `{cycloidal_dictionary['best_max_reduction_pct']:.1f}%` TE max reduction.",
        f"- Paper compensation harmonics baseline: `{', '.join(str(harmonic) for harmonic in PAPER_REFERENCE_DATA['selected_harmonics_primary'])}` with additional checks on `{', '.join(str(harmonic) for harmonic in PAPER_REFERENCE_DATA['selected_harmonics_extended'])}`.",
        "",
        "### Paper Vs Repository",
        "",
        "| Comparison Item | Paper Reference | Repository Status | Current Verdict |",
        "| --- | --- | --- | --- |",
        f"| Offline model-selection direction | Boosting/tree-heavy deployed harmonic predictors | Current winner `{current_best_run_name}` from family `{current_best_family}` with model type `{current_best_model_type}` | {current_offline_verdict} |",
        f"| Strongest neural branch role | Neural models are evaluated, but not the primary deployed winners | Strongest repository neural family is `{strongest_neural_family or 'N/A'}` and still trails the tree winner | aligned |",
        "| Offline prediction metric protocol | Mean percentage error over full TE curves | Repository currently tracks `test_mae` / `test_rmse` in degrees, not the same protocol | not_yet_comparable |",
        f"| Online robot-profile compensation | TE RMS reduction `{robot_dictionary['best_rms_reduction_pct']:.1f}%` | No repository-owned online compensation result yet | not_yet_comparable |",
        f"| Online cycloidal-profile compensation | TE RMS reduction `{cycloidal_dictionary['best_rms_reduction_pct']:.1f}%`, TE max reduction `{cycloidal_dictionary['best_max_reduction_pct']:.1f}%` | No repository-owned online compensation result yet | not_yet_comparable |",
        "| Table 9-style end-to-end benchmark | PLC-integrated motion-profile compensation benchmark | Missing in the repository at the current state | not_yet_comparable |",
        "",
        "### Online Compensation Tracking Placeholder",
        "",
        "- Repository online compensation status: `not yet available`.",
        "- When online compensation tests are implemented, update this master summary with TE RMS, TE max, and reduction percentages for both robot and cycloidal motion profiles.",
        "- Until those tests exist, present the paper comparison as `offline-only` rather than end-to-end equivalent.",
        "",
        "### Gap Summary",
        "",
        *build_paper_alignment_status_list(program_best_entry, strongest_neural_family),
        "",
    ]


def build_master_summary_markdown() -> str:

    """Build the full master-summary Markdown text.

    Returns:
        Complete Markdown report text.
    """

    # Load Canonical Source Artifacts
    backlog_text = read_text_file(DEFAULT_BACKLOG_PATH)
    backlog_snapshot = extract_backlog_snapshot(backlog_text)
    active_campaign_snapshot = extract_active_campaign_snapshot()
    program_registry_dictionary = load_yaml_dictionary(DEFAULT_PROGRAM_REGISTRY_PATH)
    program_best_entry = program_registry_dictionary.get("best_entry", {})
    assert isinstance(program_best_entry, dict), "Program registry best_entry must be a dictionary."
    selection_policy = program_registry_dictionary.get("selection_policy", {})
    assert isinstance(selection_policy, dict), "Program registry selection_policy must be a dictionary."

    campaign_artifact_dictionary = collect_campaign_artifacts()
    campaign_summary_list = campaign_artifact_dictionary["campaign_summary_list"]
    run_metadata_dictionary = campaign_artifact_dictionary["run_metadata_dictionary"]
    family_failure_dictionary = campaign_artifact_dictionary["family_failure_dictionary"]
    training_run_record_list = collect_training_run_records(run_metadata_dictionary, selection_policy)
    family_best_record_list = collect_family_best_records()

    # Build Derived Lookups
    family_best_entry_dictionary = {
        family_best_record["model_family"]: family_best_record["best_entry"]
        for family_best_record in family_best_record_list
        if isinstance(family_best_record.get("best_entry"), dict)
    }
    family_best_by_run_instance = {
        best_entry_dictionary.get("run_instance_id"): model_family
        for model_family, best_entry_dictionary in family_best_entry_dictionary.items()
        if best_entry_dictionary.get("run_instance_id") not in [None, ""]
    }

    neural_family_best_record_list = [
        family_best_record
        for family_best_record in family_best_record_list
        if isinstance(family_best_record.get("best_entry"), dict)
        and str(family_best_record["best_entry"].get("model_type", "")) in NEURAL_MODEL_TYPE_SET
    ]
    strongest_neural_family = None
    if neural_family_best_record_list:
        strongest_neural_family = sorted(
            neural_family_best_record_list,
            key=lambda family_best_record: build_sort_key(family_best_record["best_entry"], selection_policy),
        )[0]["model_family"]

    run_records_by_family: dict[str, list[dict[str, Any]]] = {}
    for training_run_record in training_run_record_list:
        run_records_by_family.setdefault(training_run_record["model_family"], []).append(training_run_record)

    active_family_set = set(active_campaign_snapshot["family_set"]) if active_campaign_snapshot["status"] in {"prepared", "running"} else set()
    implemented_family_list = sorted(family_best_entry_dictionary.keys())
    concluded_family_list = [family_name for family_name in implemented_family_list if family_name not in active_family_set]

    current_status_dictionary = backlog_snapshot["current_status"]
    wave_status_dictionary = backlog_snapshot["wave_status"]
    exploratory_family_list = backlog_snapshot["exploratory_family_list"]

    # Start Report Body
    report_line_list = [
        "# Training Results Master Summary",
        "",
        "## Executive Snapshot",
        "",
        f"- Generated At: `{datetime.now().isoformat(timespec='seconds')}`",
        f"- Program State: {current_status_dictionary.get('Program State', 'N/A')}",
        f"- Current Completed Wave: {current_status_dictionary.get('Current Completed Wave', 'N/A')}",
        f"- Current Focus: {current_status_dictionary.get('Current Focus', 'N/A')}",
        f"- Active Campaign Status: `{active_campaign_snapshot['status']}`",
        f"- Active Campaign Name: `{active_campaign_snapshot['campaign_name']}`",
        f"- Current Global Winner: `{program_best_entry.get('run_name', 'N/A')}` | Family `{program_best_entry.get('model_family', 'N/A')}` | Test MAE `{format_float(program_best_entry.get('test_mae'))}`",
        "",
        "## Main Takeaways",
        "",
        f"- Strongest current neural family: `{strongest_neural_family or 'N/A'}`",
        f"- Current plain MLP anchor: `{family_best_entry_dictionary.get('feedforward', {}).get('run_name', 'N/A')}`",
        f"- Active family-improvement branch count: `{len(active_family_set)}`",
        f"- Implemented and benchmarked family count: `{len(concluded_family_list)}`",
        "",
        "## Current Project Status",
        "",
        "### Implemented And Benchmarked Families",
        "",
        "| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |",
        "| --- | --- | --- | --- | ---: | ---: | --- |",
    ]

    for family_best_record in sorted(family_best_record_list, key=lambda record: build_sort_key(record["best_entry"], selection_policy)):
        best_entry_dictionary = family_best_record["best_entry"]
        report_line_list.append(
            f"| `{family_best_record['model_family']}` | "
            f"{build_family_role(family_best_record['model_family'], best_entry_dictionary, program_best_entry, strongest_neural_family, active_family_set)} | "
            f"`{best_entry_dictionary.get('run_name', 'N/A')}` | "
            f"`{best_entry_dictionary.get('model_type', 'N/A')}` | "
            f"{format_float(best_entry_dictionary.get('test_mae'))} | "
            f"{format_parameter_count(best_entry_dictionary.get('trainable_parameter_count'))} | "
            f"`{format_timestamp(family_best_record['updated_at'])}` |"
        )

    report_line_list.extend([
        "",
        "### Active Training Or Improvement Branches",
        "",
    ])

    if active_campaign_snapshot["status"] in {"prepared", "running"} and active_family_set:
        report_line_list.extend([
            f"- Current campaign: `{active_campaign_snapshot['campaign_name']}`",
            f"- Launch mode: `{active_campaign_snapshot['launch_mode']}`",
            f"- Families under active improvement: {', '.join(f'`{family_name}`' for family_name in sorted(active_family_set))}",
            f"- Planning report: `{active_campaign_snapshot['planning_report_path']}`",
            "",
        ])
    else:
        report_line_list.extend([
            "- No campaign is currently in `prepared` or `running` state.",
            "- The next active implementation branch should therefore be read from the live backlog focus and the next approved campaign plan.",
            "",
        ])

    report_line_list.extend([
        "### Roadmap And Planned Work",
        "",
        "| Wave Or Track | Status |",
        "| --- | --- |",
    ])

    for wave_name, wave_status in wave_status_dictionary.items():
        report_line_list.append(f"| {wave_name} | {wave_status} |")

        if exploratory_family_list:
            report_line_list.extend([
                "",
                "Low-priority exploratory families currently listed in the backlog:",
                "",
            ])
        for exploratory_family in exploratory_family_list:
            cleaned_exploratory_family = exploratory_family.replace("`", "")
            report_line_list.append(f"- `{cleaned_exploratory_family}`")

    report_line_list.extend([
        "",
        "## Recent Campaign Changes",
        "",
        "| Campaign | Generated At | Completed | Failed | Winner | Impact |",
        "| --- | --- | ---: | ---: | --- | --- |",
    ])

    for campaign_summary in sorted(campaign_summary_list, key=lambda summary: summary["generated_at"] or datetime.min, reverse=True)[:5]:
        best_entry_dictionary = campaign_summary.get("best_entry", {})
        winner_text = "N/A"
        if isinstance(best_entry_dictionary, dict) and len(best_entry_dictionary) > 0:
            winner_text = f"`{best_entry_dictionary.get('run_name', 'N/A')}`"

        report_line_list.append(
            f"| `{campaign_summary['campaign_name']}` | "
            f"`{format_timestamp(campaign_summary['generated_at'])}` | "
            f"{campaign_summary['completed_count']} | "
            f"{campaign_summary['failed_count']} | "
            f"{winner_text} | "
            f"{build_recent_change_label(campaign_summary, family_best_by_run_instance, program_best_entry)} |"
        )

    report_line_list.extend([
        "",
        "## Ranking Policy",
        "",
        f"- Primary metric: `{selection_policy.get('primary_metric', 'N/A')}`",
        f"- First tie-breaker: `{selection_policy.get('first_tie_breaker', 'N/A')}`",
        f"- Second tie-breaker: `{selection_policy.get('second_tie_breaker', 'N/A')}`",
        f"- Third tie-breaker: `{selection_policy.get('third_tie_breaker', 'N/A')}`",
        f"- Direction: `{selection_policy.get('direction', 'N/A')}`",
        "",
        "## Best Result Per Family",
        "",
        "| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |",
    ])

    for family_best_record in sorted(family_best_record_list, key=lambda record: build_sort_key(record["best_entry"], selection_policy)):
        best_entry_dictionary = family_best_record["best_entry"]
        matching_run_record = next(
            (
                run_record
                for run_record in run_records_by_family.get(family_best_record["model_family"], [])
                if run_record["run_instance_id"] == best_entry_dictionary.get("run_instance_id")
            ),
            None,
        )
        artifact_size_text = format_size_megabytes(matching_run_record["artifact_size_megabytes"]) if matching_run_record is not None else "N/A"
        training_cost_text = matching_run_record["training_heaviness_label"] if matching_run_record is not None else "Unknown"

        report_line_list.append(
            f"| `{family_best_record['model_family']}` | "
            f"`{best_entry_dictionary.get('run_name', 'N/A')}` | "
            f"`{best_entry_dictionary.get('model_type', 'N/A')}` | "
            f"{format_float(best_entry_dictionary.get('val_mae'))} | "
            f"{format_float(best_entry_dictionary.get('test_mae'))} | "
            f"{format_float(best_entry_dictionary.get('test_rmse'))} | "
            f"{format_parameter_count(best_entry_dictionary.get('trainable_parameter_count'))} | "
            f"{artifact_size_text} | "
            f"{training_cost_text} | "
            f"{build_family_role(family_best_record['model_family'], best_entry_dictionary, program_best_entry, strongest_neural_family, active_family_set)} |"
        )

    report_line_list.extend([
        "",
        "## Cross-Family Interpretation",
        "",
        f"- Current global reference winner: `{program_best_entry.get('run_name', 'N/A')}` from family `{program_best_entry.get('model_family', 'N/A')}`.",
        f"- Strongest current neural family: `{strongest_neural_family or 'N/A'}`.",
        f"- Current plain-MLP comparison anchor: `{family_best_entry_dictionary.get('feedforward', {}).get('run_name', 'N/A')}`.",
        "- Predictive quality and deployment suitability must stay separate: the best leaderboard entry is not automatically the best TwinCAT/PLC candidate.",
        "- Large tree artifacts should be treated cautiously even when tree-based accuracy remains strong, because model weight and memory footprint can dominate deployment feasibility.",
        "",
    ])

    report_line_list.extend(build_paper_reference_section(program_best_entry, strongest_neural_family))

    report_line_list.extend([
        "## Family-By-Family Result Breakdowns",
        "",
    ])

    for model_family in sorted(run_records_by_family.keys()):
        family_run_record_list = sorted(run_records_by_family[model_family], key=lambda record: build_sort_key(record, selection_policy))
        family_best_entry = family_best_entry_dictionary.get(model_family, {})
        family_failure_record_list = family_failure_dictionary.get(model_family, [])

        report_line_list.extend([
            f"### {model_family}",
            "",
            f"- Best run: `{family_best_entry.get('run_name', 'N/A')}`",
            f"- Best test MAE: `{format_float(family_best_entry.get('test_mae'))}`",
            f"- Completed tracked runs: `{len(family_run_record_list)}`",
            f"- Known failed campaign attempts: `{len(family_failure_record_list)}`",
            "",
            "| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |",
            "| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |",
        ])

        for rank_index, family_run_record in enumerate(family_run_record_list, start=1):
            report_line_list.append(
                f"| {rank_index} | "
                f"`{family_run_record['run_name']}` | "
                f"`{family_run_record['model_type']}` | "
                f"{format_float(family_run_record.get('test_mae'))} | "
                f"{format_float(family_run_record.get('test_rmse'))} | "
                f"{format_float(family_run_record.get('val_mae'))} | "
                f"{format_parameter_count(family_run_record.get('trainable_parameter_count'))} | "
                f"{format_duration_seconds(family_run_record.get('duration_seconds'))} | "
                f"{format_size_megabytes(family_run_record.get('artifact_size_megabytes'))} | "
                f"{family_run_record['complexity_label']} | "
                f"{family_run_record['training_heaviness_label']} | "
                f"`{family_run_record.get('campaign_name') or 'standalone_or_unknown'}` |"
            )

        if family_failure_record_list:
            report_line_list.extend([
                "",
                "Known failed campaign attempts for this family:",
                "",
            ])
            for failure_record in family_failure_record_list:
                report_line_list.append(
                    f"- `{failure_record['run_name']}` | campaign `{failure_record['campaign_name']}` | model type `{failure_record['model_type']}` | error `{failure_record['error_message']}`"
                )

        report_line_list.append("")

    report_line_list.extend([
        "## Source Of Truth",
        "",
        f"- Live backlog: `{format_project_relative_path(DEFAULT_BACKLOG_PATH)}`",
        f"- Active campaign state: `{format_project_relative_path(DEFAULT_ACTIVE_CAMPAIGN_PATH)}`",
        f"- Program registry: `{format_project_relative_path(DEFAULT_PROGRAM_REGISTRY_PATH)}`",
        f"- Family registries root: `{format_project_relative_path(DEFAULT_FAMILY_REGISTRY_ROOT)}`",
        f"- Training campaign root: `{format_project_relative_path(DEFAULT_TRAINING_CAMPAIGN_ROOT)}`",
        f"- Training run root: `{format_project_relative_path(DEFAULT_TRAINING_RUN_ROOT)}`",
        f"- Paper reference report: `{format_project_relative_path(DEFAULT_PAPER_REFERENCE_REPORT_PATH)}`",
        "",
        "This document is repository-generated. Regenerate it after new campaign results so the cross-family snapshot stays aligned with the canonical registries and campaign artifacts.",
        "",
    ])

    return "\n".join(report_line_list)


def generate_training_results_master_summary(output_markdown_path: Path) -> Path:

    """Generate and write the canonical master summary.

    Args:
        output_markdown_path: Markdown output path.

    Returns:
        Resolved output Markdown path.
    """

    output_markdown_path = output_markdown_path.expanduser().resolve()
    output_markdown_path.parent.mkdir(parents=True, exist_ok=True)

    # Build And Write Markdown Report
    markdown_text = build_master_summary_markdown().rstrip() + "\n"
    output_markdown_path.write_text(markdown_text, encoding="utf-8")
    return output_markdown_path


def main() -> None:

    """Run the master-summary generator CLI."""

    parsed_arguments = parse_command_line_arguments()
    output_markdown_path = generate_training_results_master_summary(Path(parsed_arguments.output_markdown_path))
    print(f"[DONE] Generated training results master summary | {format_project_relative_path(output_markdown_path)}")


if __name__ == "__main__":

    main()
