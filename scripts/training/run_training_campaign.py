from __future__ import annotations

# Import Python Utilities
import argparse, shutil, sys, traceback
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import Dataset Utilities
from scripts.datasets.transmission_error_dataset import resolve_project_relative_path

DEFAULT_QUEUE_ROOT = PROJECT_PATH / "config" / "training" / "queue"
DEFAULT_CAMPAIGN_OUTPUT_ROOT = PROJECT_PATH / "output" / "training_campaigns"
SUPPORTED_MODEL_ENTRYPOINT_NAME_DICTIONARY = {"feedforward": "scripts/training/train_feedforward_network.py"}
CONFIG_SNAPSHOT_FILENAME_LIST = ["feedforward_network_training.yaml", "training_config.yaml"]
TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"
SECTION_DIVIDER_WIDTH = 96
CAMPAIGN_PROGRESS_BAR_WIDTH = 24

@dataclass(frozen=True)
class QueueDirectories:

    """ Queue Directories """

    root: Path
    pending: Path
    running: Path
    completed: Path
    failed: Path

@dataclass(frozen=True)
class QueueItemContext:

    """ Queue Item Context """

    queue_config_path: Path
    source_config_path: Path | None
    training_config: dict[str, Any]

@dataclass(frozen=True)
class TrainingRunResult:

    """ Training Run Result """

    original_queue_config_path: Path
    final_queue_config_path: Path
    source_config_path: Path | None
    run_name: str
    model_type: str
    queue_status: str
    start_time: str
    end_time: str
    duration_seconds: float
    process_return_code: int | None
    output_directory: Path
    config_snapshot_path: Path | None
    best_checkpoint_reference_path: Path | None
    best_checkpoint_path: str | None
    metrics_path: Path | None
    training_report_path: Path | None
    log_path: Path
    planning_report_path: str | None
    campaign_name: str | None
    error_message: str | None

class TeeTerminalStream:

    """ Tee Terminal Stream """

    def __init__(self, terminal_stream, log_file) -> None:

        """ Initialize Tee Terminal Stream """

        self.terminal_stream = terminal_stream
        self.log_file = log_file
        self.log_file_is_available = True

    def write_log_message(self, log_message: str) -> None:

        """ Write Log Message """

        if not self.log_file_is_available:
            return

        if getattr(self.log_file, "closed", False):
            self.log_file_is_available = False
            return

        try:

            self.log_file.write(log_message)
            self.log_file.flush()

        except (OSError, ValueError):

            self.log_file_is_available = False

    def write(self, message: str) -> int:

        """ Write Message """

        if message == "":
            return 0

        self.terminal_stream.write(message)
        self.terminal_stream.flush()

        log_message = message.replace("\r", "\n")
        self.write_log_message(log_message)
        return len(message)

    def flush(self) -> None:

        """ Flush Streams """

        self.terminal_stream.flush()

        if not self.log_file_is_available:
            return

        if getattr(self.log_file, "closed", False):
            self.log_file_is_available = False
            return

        try:

            self.log_file.flush()

        except (OSError, ValueError):

            self.log_file_is_available = False

    def isatty(self) -> bool:

        """ Check Interactive Terminal """

        terminal_isatty = getattr(self.terminal_stream, "isatty", None)
        if callable(terminal_isatty): return bool(terminal_isatty())
        return False

    @property
    def encoding(self) -> str:

        """ Resolve Encoding """

        return getattr(self.terminal_stream, "encoding", None) or "utf-8"

    def __getattr__(self, attribute_name: str):

        """ Forward Missing Attributes """

        return getattr(self.terminal_stream, attribute_name)

def print_info_message(message: str) -> None:

    """ Print Info Message """

    print(f"[INFO] {message}", flush=True)

def print_success_message(message: str) -> None:

    """ Print Success Message """

    print(f"[DONE] {message}", flush=True)

def print_warning_message(message: str) -> None:

    """ Print Warning Message """

    print(f"[WARN] {message}", flush=True)

def build_campaign_progress_bar(completed_run_count: int, total_run_count: int) -> str:

    """ Build Campaign Progress Bar """

    if total_run_count <= 0:
        return "[" + "-" * CAMPAIGN_PROGRESS_BAR_WIDTH + "]"

    filled_width = int((completed_run_count / total_run_count) * CAMPAIGN_PROGRESS_BAR_WIDTH)
    empty_width = CAMPAIGN_PROGRESS_BAR_WIDTH - filled_width
    return "[" + "#" * filled_width + "-" * empty_width + "]"

def print_campaign_run_header(
    campaign_name: str,
    queue_index: int,
    queue_total: int,
    run_name: str,
    queue_config_path: Path,
    source_config_path: Path | None,
) -> None:

    """ Print Campaign Run Header """

    progress_bar = build_campaign_progress_bar(completed_run_count=max(queue_index - 1, 0), total_run_count=queue_total)

    print()
    print("=" * SECTION_DIVIDER_WIDTH, flush=True)
    print(f"Campaign Progress {queue_index}/{queue_total} {progress_bar}", flush=True)
    print("=" * SECTION_DIVIDER_WIDTH, flush=True)
    print_info_message(f"Campaign Name | {campaign_name}")
    print_info_message(f"Run Name | {run_name}")
    print_info_message(f"Queue Config | {queue_config_path}")
    print_info_message(f"Source Config | {source_config_path if source_config_path is not None else 'N/A'}")

def print_campaign_run_footer(
    queue_index: int,
    queue_total: int,
    run_name: str,
    queue_status: str,
    duration_seconds: float,
    completed_count: int,
    failed_count: int,
) -> None:

    """ Print Campaign Run Footer """

    progress_bar = build_campaign_progress_bar(completed_run_count=queue_index, total_run_count=queue_total)
    duration_string = format_duration_seconds(duration_seconds)

    print()
    print("=" * SECTION_DIVIDER_WIDTH, flush=True)
    print(f"Campaign Progress {queue_index}/{queue_total} {progress_bar}", flush=True)
    print("=" * SECTION_DIVIDER_WIDTH, flush=True)

    if queue_status == "completed": print_success_message(f"Run Completed | {run_name} | Duration {duration_string}")
    else: print_warning_message(f"Run Failed | {run_name} | Duration {duration_string}")

    print_info_message(f"Cumulative Status | Completed {completed_count} | Failed {failed_count}")

def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command Line Arguments """

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(description="Execute queued training YAML files one by one.")

    # Add Positional Config Arguments
    argument_parser.add_argument("config_path_list", nargs="*", type=Path, help="Optional YAML files to enqueue before processing the pending queue.")

    # Add Queue Arguments
    argument_parser.add_argument("--queue-root", type=Path, default=DEFAULT_QUEUE_ROOT, help="Root directory containing the pending, running, completed, and failed queue folders.")
    argument_parser.add_argument("--campaign-output-root", type=Path, default=DEFAULT_CAMPAIGN_OUTPUT_ROOT, help="Root directory used for campaign manifests, reports, and terminal logs.")
    argument_parser.add_argument("--campaign-name", type=str, default=None, help="Optional campaign name used for the campaign output folder and report header.")
    argument_parser.add_argument("--planning-report-path", type=Path, default=None, help="Optional planning-report path recorded in the generated campaign report.")
    argument_parser.add_argument("--enqueue-only", action="store_true", help="Copy the provided YAML files into the pending queue without executing them.")
    argument_parser.add_argument("--stop-on-error", action="store_true", help="Stop the queue immediately after the first failed training run.")

    return argument_parser.parse_args()

def sanitize_name(name: str) -> str:

    """ Sanitize Name """

    sanitized_name = "".join(character.lower() if character.isalnum() else "_" for character in name.strip())
    sanitized_name = sanitized_name.strip("_")
    return sanitized_name or "campaign"

def ensure_queue_directories(queue_root: str | Path) -> QueueDirectories:

    """ Ensure Queue Directories """

    # Resolve Queue Root
    resolved_queue_root = resolve_project_relative_path(queue_root)

    # Build Queue Directories
    queue_directories = QueueDirectories(
        root=resolved_queue_root,
        pending=resolved_queue_root / "pending",
        running=resolved_queue_root / "running",
        completed=resolved_queue_root / "completed",
        failed=resolved_queue_root / "failed",
    )

    # Create Queue Directories
    for queue_directory in [
        queue_directories.root,
        queue_directories.pending,
        queue_directories.running,
        queue_directories.completed,
        queue_directories.failed,
    ]:
        queue_directory.mkdir(parents=True, exist_ok=True)

    return queue_directories

def load_yaml_dictionary(config_path: str | Path) -> dict[str, Any]:

    """ Load YAML Dictionary """

    # Resolve Config Path
    resolved_config_path = resolve_project_relative_path(config_path)
    assert resolved_config_path.exists(), f"Config Path does not exist | {resolved_config_path}"

    # Load YAML Configuration
    with resolved_config_path.open("r", encoding="utf-8") as config_file:
        yaml_dictionary = yaml.safe_load(config_file)

    # Validate Configuration
    assert isinstance(yaml_dictionary, dict), f"YAML file must contain a dictionary | {resolved_config_path}"

    return yaml_dictionary

def discover_pending_queue_paths(queue_directories: QueueDirectories) -> list[Path]:

    """ Discover Pending Queue Paths """

    return sorted([
        queue_path.resolve()
        for queue_path in queue_directories.pending.iterdir()
        if queue_path.is_file() and queue_path.suffix.lower() in [".yaml", ".yml"]
    ])

def build_enqueued_filename(source_config_path: Path, order_index: int) -> str:

    """ Build Enqueued Filename """

    # Format: {timestamp}_{order_index}_{sanitized_stem}.yaml
    timestamp_string = datetime.now().strftime(TIMESTAMP_FORMAT)
    sanitized_stem = sanitize_name(source_config_path.stem)
    return f"{timestamp_string}_{order_index:03d}_{sanitized_stem}.yaml"

def build_available_path(path_value: Path) -> Path:

    """ Build Available Path """

    # If the Candidate Path Does Not Exist, Return It As Is
    candidate_path = path_value.resolve()
    if not candidate_path.exists():
        return candidate_path

    suffix = candidate_path.suffix
    stem = candidate_path.stem
    parent = candidate_path.parent

    duplicate_index = 1
    while True:

        # Format: {stem}_{duplicate_index:03d}{suffix}
        indexed_candidate_path = (parent / f"{stem}_{duplicate_index:03d}{suffix}").resolve()
        if not indexed_candidate_path.exists(): return indexed_candidate_path

        duplicate_index += 1

def enqueue_configuration_paths(config_path_list: list[Path], queue_directories: QueueDirectories) -> dict[Path, Path]:

    """ Enqueue Configuration Paths """

    queue_source_path_dictionary: dict[Path, Path] = {}

    for order_index, source_config_path in enumerate(config_path_list, start=1):

        # Resolve Source Path
        resolved_source_config_path = resolve_project_relative_path(source_config_path)
        assert resolved_source_config_path.exists(), f"Source Config Path does not exist | {resolved_source_config_path}"

        # Reuse Existing Pending Config
        if resolved_source_config_path.parent == queue_directories.pending:
            queue_source_path_dictionary[resolved_source_config_path.resolve()] = resolved_source_config_path.resolve()
            continue

        # Copy Config Into Pending Queue
        queued_config_path = build_available_path(
            queue_directories.pending / build_enqueued_filename(
                source_config_path=resolved_source_config_path,
                order_index=order_index,
            )
        )
        shutil.copy2(resolved_source_config_path, queued_config_path)
        queue_source_path_dictionary[queued_config_path] = resolved_source_config_path.resolve()
        print_info_message(f"Enqueued Config | {queued_config_path}")

    return queue_source_path_dictionary

def build_queue_item_context(queue_config_path: Path, queue_source_path_dictionary: dict[Path, Path]) -> QueueItemContext:

    """ Build Queue Item Context """

    return QueueItemContext(
        queue_config_path=queue_config_path.resolve(),
        source_config_path=queue_source_path_dictionary.get(queue_config_path.resolve()),
        training_config=load_yaml_dictionary(queue_config_path),
    )

def format_path_for_report(path_value: Path | None) -> str:

    """ Format Path For Report """

    if path_value is None:
        return "N/A"

    resolved_path = path_value.resolve()

    # Attempt to Make the Path Relative to the Project Path
    try: return resolved_path.relative_to(PROJECT_PATH).as_posix()
    except ValueError: return resolved_path.as_posix()

def resolve_campaign_name(queue_item_context_list: list[QueueItemContext], requested_campaign_name: str | None) -> str:

    """ Resolve Campaign Name """

    if requested_campaign_name not in [None, ""]:
        return requested_campaign_name

    # Attempt to Infer Campaign Name from Metadata
    metadata_campaign_name_set = {
        str(queue_item_context.training_config.get("metadata", {}).get("campaign_name"))
        for queue_item_context in queue_item_context_list
        if isinstance(queue_item_context.training_config.get("metadata"), dict)
        and queue_item_context.training_config.get("metadata", {}).get("campaign_name") not in [None, ""]
    }

    # If All Campaign Names in Metadata Are the Same, Use That as the Campaign Name
    if len(metadata_campaign_name_set) == 1: return next(iter(metadata_campaign_name_set))

    return "queued_training_campaign"

def resolve_campaign_planning_report_path(queue_item_context_list: list[QueueItemContext], requested_planning_report_path: Path | None) -> str | None:

    """ Resolve Campaign Planning Report Path """

    if requested_planning_report_path is not None:
        return format_path_for_report(resolve_project_relative_path(requested_planning_report_path))

    # Attempt to Infer Planning Report Path from Metadata
    metadata_planning_report_path_set = {
        str(queue_item_context.training_config.get("metadata", {}).get("planning_report_path"))
        for queue_item_context in queue_item_context_list
        if isinstance(queue_item_context.training_config.get("metadata"), dict)
        and queue_item_context.training_config.get("metadata", {}).get("planning_report_path") not in [None, ""]
    }

    # If All Planning Report Paths in Metadata Are the Same, Use That as the Planning Report Path
    if len(metadata_planning_report_path_set) == 1: return next(iter(metadata_planning_report_path_set))

    return None

def resolve_training_entrypoint_path(model_type: str) -> Path:

    """ Resolve Training Entrypoint Path """

    # Model Type is Case-Insensitive
    normalized_model_type = model_type.lower()
    assert normalized_model_type in SUPPORTED_MODEL_ENTRYPOINT_NAME_DICTIONARY, (
        f"Unsupported Model Type for Campaign Runner | {model_type} | "
        f"Supported: {sorted(SUPPORTED_MODEL_ENTRYPOINT_NAME_DICTIONARY.keys())}"
    )

    return (PROJECT_PATH / SUPPORTED_MODEL_ENTRYPOINT_NAME_DICTIONARY[normalized_model_type]).resolve()

def run_feedforward_training(config_path: str | Path) -> None:

    """ Run Feedforward Training """

    from scripts.training.train_feedforward_network import train_feedforward_network

    train_feedforward_network(config_path=config_path)

def resolve_training_handler(model_type: str) -> Callable[[str | Path], None]:

    """ Resolve Training Handler """

    supported_model_handler_dictionary = {"feedforward": run_feedforward_training}

    normalized_model_type = model_type.lower()
    assert normalized_model_type in supported_model_handler_dictionary, (
        f"Unsupported Model Type for Campaign Runner | {model_type} | "
        f"Supported: {sorted(supported_model_handler_dictionary.keys())}"
    )

    return supported_model_handler_dictionary[normalized_model_type]

def resolve_output_directory(training_config: dict[str, Any]) -> Path:

    """ Resolve Output Directory """

    # Resolve the Output Root Path Relative to the Project Path
    output_root = resolve_project_relative_path(training_config["paths"]["output_root"])
    run_name = str(training_config["experiment"]["run_name"])
    return (output_root / run_name).resolve()

def resolve_config_snapshot_path(output_directory: Path) -> Path | None:

    """ Resolve Config Snapshot Path """

    # Resolve Config Snapshot Path Candidates in Order and Return the First One That Exists
    for config_snapshot_filename in CONFIG_SNAPSHOT_FILENAME_LIST:
        config_snapshot_path = output_directory / config_snapshot_filename
        if config_snapshot_path.exists(): return config_snapshot_path.resolve()

    return None

def read_best_checkpoint_path(best_checkpoint_reference_path: Path | None) -> str | None:

    """ Read Best Checkpoint Path """

    if best_checkpoint_reference_path is None or not best_checkpoint_reference_path.exists():
        return None

    return best_checkpoint_reference_path.read_text(encoding="utf-8").strip() or None

def build_training_command(training_entrypoint_path: Path, running_config_path: Path) -> list[str]:

    """ Build Training Command """

    return [
        sys.executable,
        str(training_entrypoint_path),
        "--config-path",
        str(running_config_path),
    ]

@contextmanager
def tee_terminal_output(log_path: Path, command: list[str]) -> Iterator[None]:

    """ Tee Terminal Output """

    with log_path.open("w", encoding="utf-8", newline="\n") as log_file:

        # Write Command Header
        log_file.write(f"Command: {' '.join(command)}\n")
        log_file.write(f"Working Directory: {PROJECT_PATH}\n\n")
        log_file.flush()

        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = TeeTerminalStream(terminal_stream=original_stdout, log_file=log_file)
        sys.stderr = TeeTerminalStream(terminal_stream=original_stderr, log_file=log_file)

        try:

            yield

        finally:

            sys.stdout.flush()
            sys.stderr.flush()
            sys.stdout = original_stdout
            sys.stderr = original_stderr

def format_duration_seconds(duration_seconds: float) -> str:

    """ Format Duration Seconds """

    total_seconds = max(int(round(duration_seconds)), 0)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def execute_queue_item(
    queue_item_context: QueueItemContext,
    queue_directories: QueueDirectories,
    log_directory: Path,
    campaign_name: str,
    planning_report_path: str | None,
    queue_index: int,
    queue_total: int,
) -> TrainingRunResult:

    """ Execute Queue Item """

    # Move Config from Pending to Running
    training_config = queue_item_context.training_config
    original_queue_config_path = queue_item_context.queue_config_path
    running_queue_config_path = build_available_path(queue_directories.running / original_queue_config_path.name)
    shutil.move(str(original_queue_config_path), str(running_queue_config_path))

    # Resolve Run Name, Model Type, and Output Directory
    experiment_dictionary = training_config.get("experiment", {}) if isinstance(training_config.get("experiment"), dict) else {}
    run_name = str(experiment_dictionary.get("run_name", running_queue_config_path.stem))
    model_type = str(experiment_dictionary.get("model_type", "unknown"))
    output_directory = (PROJECT_PATH / "output" / run_name).resolve()

    # Resolve Campaign Name and Planning Report Path from Metadata if Available
    metadata_dictionary = training_config.get("metadata", {}) if isinstance(training_config.get("metadata"), dict) else {}
    run_campaign_name = str(metadata_dictionary.get("campaign_name")) if metadata_dictionary.get("campaign_name") not in [None, ""] else campaign_name
    run_planning_report_path = (str(metadata_dictionary.get("planning_report_path")) if metadata_dictionary.get("planning_report_path") not in [None, ""] else planning_report_path)

    log_path = build_available_path(log_directory / f"{running_queue_config_path.stem}.log")
    start_datetime = datetime.now()

    try:

        # Resolve Output Directory, Entrypoint Path, and Training Handler
        output_directory = resolve_output_directory(training_config=training_config)
        training_entrypoint_path = resolve_training_entrypoint_path(model_type=model_type)
        training_handler = resolve_training_handler(model_type=model_type)
        command = build_training_command(training_entrypoint_path=training_entrypoint_path, running_config_path=running_queue_config_path)

        # Mirror Terminal Output While Preserving Interactive Training Behavior
        with tee_terminal_output(log_path=log_path, command=command):

            print_campaign_run_header(
                campaign_name=run_campaign_name,
                queue_index=queue_index,
                queue_total=queue_total,
                run_name=run_name,
                queue_config_path=running_queue_config_path,
                source_config_path=queue_item_context.source_config_path,
            )
            training_handler(running_queue_config_path)

        process_return_code = 0
        queue_status = "completed" if process_return_code == 0 else "failed"
        error_message = None if process_return_code == 0 else f"Training run exited with code {process_return_code}"

    except KeyboardInterrupt:

        print_warning_message(f"Campaign interrupted by user | Config left in running queue | {running_queue_config_path}")
        raise

    except Exception as error:

        process_return_code = None
        queue_status = "failed"
        error_message = str(error)
        with log_path.open("a", encoding="utf-8") as log_file:
            log_file.write(f"\n[RUNNER ERROR] {error}\n")
            log_file.write(traceback.format_exc())

    # Move Config from Running to Completed or Failed
    final_queue_directory = queue_directories.completed if queue_status == "completed" else queue_directories.failed
    final_queue_config_path = build_available_path(final_queue_directory / running_queue_config_path.name)
    shutil.move(str(running_queue_config_path), str(final_queue_config_path))

    # Record End Time and Check for Generated Artifacts
    end_datetime = datetime.now()
    best_checkpoint_reference_path = (output_directory / "best_checkpoint_path.txt").resolve()
    if not best_checkpoint_reference_path.exists(): best_checkpoint_reference_path = None
    metrics_path = (output_directory / "training_test_metrics.yaml").resolve()
    if not metrics_path.exists(): metrics_path = None
    training_report_path = (output_directory / "training_test_report.md").resolve()
    if not training_report_path.exists(): training_report_path = None

    # Build and Return Training Run Result
    return TrainingRunResult(
        original_queue_config_path=original_queue_config_path,
        final_queue_config_path=final_queue_config_path,
        source_config_path=queue_item_context.source_config_path,
        run_name=run_name,
        model_type=model_type,
        queue_status=queue_status,
        start_time=start_datetime.isoformat(timespec="seconds"),
        end_time=end_datetime.isoformat(timespec="seconds"),
        duration_seconds=(end_datetime - start_datetime).total_seconds(),
        process_return_code=process_return_code,
        output_directory=output_directory,
        config_snapshot_path=resolve_config_snapshot_path(output_directory=output_directory),
        best_checkpoint_reference_path=best_checkpoint_reference_path,
        best_checkpoint_path=read_best_checkpoint_path(best_checkpoint_reference_path=best_checkpoint_reference_path),
        metrics_path=metrics_path,
        training_report_path=training_report_path,
        log_path=log_path,
        planning_report_path=run_planning_report_path,
        campaign_name=run_campaign_name,
        error_message=error_message,
    )

def build_manifest_dictionary(
    campaign_name: str,
    planning_report_path: str | None,
    queue_directories: QueueDirectories,
    campaign_output_directory: Path,
    training_run_result_list: list[TrainingRunResult],
) -> dict[str, Any]:

    """ Build Manifest Dictionary """

    # Format Paths for Report and Build Manifest Dictionary
    return {
        "campaign_name": campaign_name,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "queue_root": format_path_for_report(queue_directories.root),
        "campaign_output_directory": format_path_for_report(campaign_output_directory),
        "planning_report_path": planning_report_path,
        "run_list": [
            {
                "original_queue_config_path": format_path_for_report(training_run_result.original_queue_config_path),
                "final_queue_config_path": format_path_for_report(training_run_result.final_queue_config_path),
                "source_config_path": format_path_for_report(training_run_result.source_config_path),
                "run_name": training_run_result.run_name,
                "model_type": training_run_result.model_type,
                "queue_status": training_run_result.queue_status,
                "start_time": training_run_result.start_time,
                "end_time": training_run_result.end_time,
                "duration_seconds": round(training_run_result.duration_seconds, 3),
                "process_return_code": training_run_result.process_return_code,
                "output_directory": format_path_for_report(training_run_result.output_directory),
                "config_snapshot_path": format_path_for_report(training_run_result.config_snapshot_path),
                "best_checkpoint_reference_path": format_path_for_report(training_run_result.best_checkpoint_reference_path),
                "best_checkpoint_path": training_run_result.best_checkpoint_path,
                "metrics_path": format_path_for_report(training_run_result.metrics_path),
                "training_report_path": format_path_for_report(training_run_result.training_report_path),
                "log_path": format_path_for_report(training_run_result.log_path),
                "planning_report_path": training_run_result.planning_report_path,
                "campaign_name": training_run_result.campaign_name,
                "error_message": training_run_result.error_message,
            }
            for training_run_result in training_run_result_list
        ],
    }

def write_campaign_manifest(
    campaign_name: str,
    planning_report_path: str | None,
    queue_directories: QueueDirectories,
    campaign_output_directory: Path,
    manifest_path: Path,
    training_run_result_list: list[TrainingRunResult],
) -> None:

    """ Write Campaign Manifest """

    # Build Manifest Dictionary and Write to YAML File
    manifest_dictionary = build_manifest_dictionary(
        campaign_name=campaign_name,
        planning_report_path=planning_report_path,
        queue_directories=queue_directories,
        campaign_output_directory=campaign_output_directory,
        training_run_result_list=training_run_result_list,
    )

    with manifest_path.open("w", encoding="utf-8") as manifest_file:
        yaml.safe_dump(manifest_dictionary, manifest_file, sort_keys=False)

def write_campaign_execution_report(
    campaign_name: str,
    planning_report_path: str | None,
    queue_directories: QueueDirectories,
    campaign_output_directory: Path,
    report_path: Path,
    training_run_result_list: list[TrainingRunResult],
) -> None:

    """ Write Campaign Execution Report """

    # Calculate Summary Statistics
    completed_count = sum(training_run_result.queue_status == "completed" for training_run_result in training_run_result_list)
    failed_count = sum(training_run_result.queue_status == "failed" for training_run_result in training_run_result_list)

    # Format Paths for Report and Build Report Lines
    report_line_list = [
        "# Training Campaign Execution Report",
        "",
        "## Overview",
        "",
        f"- Campaign Name: `{campaign_name}`",
        f"- Generated At: `{datetime.now().isoformat(timespec='seconds')}`",
        f"- Queue Root: `{format_path_for_report(queue_directories.root)}`",
        f"- Campaign Output Directory: `{format_path_for_report(campaign_output_directory)}`",
        f"- Planning Report Path: `{planning_report_path if planning_report_path is not None else 'N/A'}`",
        f"- Completed Runs: `{completed_count}`",
        f"- Failed Runs: `{failed_count}`",
        "",
        "## Run Summary",
        "",
        "| Queue Config | Run Name | Model Type | Status | Duration |",
        "| --- | --- | --- | --- | --- |",
    ]

    for training_run_result in training_run_result_list:

        # Add a Row for Each Training Run Result
        report_line_list.append(
            f"| `{format_path_for_report(training_run_result.final_queue_config_path)}` | "
            f"`{training_run_result.run_name}` | "
            f"`{training_run_result.model_type}` | "
            f"`{training_run_result.queue_status}` | "
            f"`{format_duration_seconds(training_run_result.duration_seconds)}` |"
        )

    # Add Detailed Sections for Each Training Run Result
    report_line_list.extend([
        "",
        "## Run Details",
        "",
    ])

    for training_run_result in training_run_result_list:

        # Add a Section for Each Training Run Result with Key Details and Paths
        report_line_list.extend([
            f"### {training_run_result.run_name}",
            "",
            f"- Queue Config: `{format_path_for_report(training_run_result.final_queue_config_path)}`",
            f"- Source Config: `{format_path_for_report(training_run_result.source_config_path)}`",
            f"- Model Type: `{training_run_result.model_type}`",
            f"- Queue Status: `{training_run_result.queue_status}`",
            f"- Start Time: `{training_run_result.start_time}`",
            f"- End Time: `{training_run_result.end_time}`",
            f"- Duration: `{format_duration_seconds(training_run_result.duration_seconds)}`",
            f"- Process Return Code: `{training_run_result.process_return_code if training_run_result.process_return_code is not None else 'N/A'}`",
            f"- Planning Report Path: `{training_run_result.planning_report_path if training_run_result.planning_report_path is not None else 'N/A'}`",
            f"- Output Directory: `{format_path_for_report(training_run_result.output_directory)}`",
            f"- Config Snapshot: `{format_path_for_report(training_run_result.config_snapshot_path)}`",
            f"- Best Checkpoint Pointer: `{format_path_for_report(training_run_result.best_checkpoint_reference_path)}`",
            f"- Best Checkpoint Path: `{training_run_result.best_checkpoint_path if training_run_result.best_checkpoint_path is not None else 'N/A'}`",
            f"- Metrics Snapshot: `{format_path_for_report(training_run_result.metrics_path)}`",
            f"- Training Report: `{format_path_for_report(training_run_result.training_report_path)}`",
            f"- Terminal Log: `{format_path_for_report(training_run_result.log_path)}`",
            f"- Error Message: `{training_run_result.error_message if training_run_result.error_message is not None else 'N/A'}`",
            "",
        ])

    # Add Post-Training Reporting Notes
    report_line_list.extend([
        "## Post-Training Reporting Notes",
        "",
        "Use this execution report together with the per-run metrics and markdown summaries to build the mandatory final campaign-results report under `doc/reports/campaign_results/`.",
        "",
        "Recommended references for the final report:",
        "",
        "- `training_test_metrics.yaml` for numeric comparison tables.",
        "- `training_test_report.md` for per-run interpretation notes.",
        "- `best_checkpoint_path.txt` for checkpoint traceability.",
        "- `logs/*.log` for terminal-level diagnostics and failure analysis.",
        "",
    ])

    # Write Report to Markdown File
    report_path.write_text("\n".join(report_line_list), encoding="utf-8")

def main() -> None:

    """ Main Function """

    # Parse Command Line Arguments and Ensure Queue Directories
    command_line_arguments = parse_command_line_arguments()
    queue_directories = ensure_queue_directories(queue_root=command_line_arguments.queue_root)

    # Enqueue Configuration Files and Build Source Path Dictionary
    queue_source_path_dictionary = enqueue_configuration_paths(
        config_path_list=command_line_arguments.config_path_list,
        queue_directories=queue_directories,
    )

    # If --enqueue-only was Requested, Exit After Enqueuing Configurations
    if command_line_arguments.enqueue_only:
        print_success_message("Configuration files enqueued without execution")
        return

    # Discover Pending Queue Configurations and Build Queue Item Contexts
    pending_queue_path_list = discover_pending_queue_paths(queue_directories=queue_directories)
    if len(pending_queue_path_list) == 0:
        print_warning_message("No pending queue configuration files found")
        return

    # Build Queue Item Contexts for Each Pending Queue Configuration
    queue_item_context_list = [
        build_queue_item_context(
            queue_config_path=pending_queue_path,
            queue_source_path_dictionary=queue_source_path_dictionary,
        )
        for pending_queue_path in pending_queue_path_list
    ]

    # Resolve Campaign Name, Planning Report Path, and Prepare Campaign Output Directories
    campaign_name = resolve_campaign_name(queue_item_context_list=queue_item_context_list, requested_campaign_name=command_line_arguments.campaign_name)
    planning_report_path = resolve_campaign_planning_report_path(queue_item_context_list=queue_item_context_list, requested_planning_report_path=command_line_arguments.planning_report_path)
    campaign_output_root = resolve_project_relative_path(command_line_arguments.campaign_output_root)
    campaign_output_directory = (campaign_output_root / f"{datetime.now().strftime(TIMESTAMP_FORMAT)}_{sanitize_name(campaign_name)}").resolve()
    campaign_output_directory.mkdir(parents=True, exist_ok=True)
    log_directory = (campaign_output_directory / "logs").resolve()
    log_directory.mkdir(parents=True, exist_ok=True)

    # Define Paths for Campaign Manifest and Execution Report
    manifest_path = (campaign_output_directory / "campaign_manifest.yaml").resolve()
    report_path = (campaign_output_directory / "campaign_execution_report.md").resolve()
    training_run_result_list: list[TrainingRunResult] = []

    for queue_index, queue_item_context in enumerate(queue_item_context_list, start=1):

        # Execute Queue Item and Append Result to List
        training_run_result = execute_queue_item(
            queue_item_context=queue_item_context,
            queue_directories=queue_directories,
            log_directory=log_directory,
            campaign_name=campaign_name,
            planning_report_path=planning_report_path,
            queue_index=queue_index,
            queue_total=len(queue_item_context_list),
        )
        training_run_result_list.append(training_run_result)

        # Update the Campaign Manifest
        write_campaign_manifest(
            campaign_name=campaign_name,
            planning_report_path=planning_report_path,
            queue_directories=queue_directories,
            campaign_output_directory=campaign_output_directory,
            manifest_path=manifest_path,
            training_run_result_list=training_run_result_list,
        )

        # Update the Campaign Execution Report
        write_campaign_execution_report(
            campaign_name=campaign_name,
            planning_report_path=planning_report_path,
            queue_directories=queue_directories,
            campaign_output_directory=campaign_output_directory,
            report_path=report_path,
            training_run_result_list=training_run_result_list,
        )

        completed_count = sum(training_run_result.queue_status == "completed" for training_run_result in training_run_result_list)
        failed_count = sum(training_run_result.queue_status == "failed" for training_run_result in training_run_result_list)
        print_campaign_run_footer(
            queue_index=queue_index,
            queue_total=len(queue_item_context_list),
            run_name=training_run_result.run_name,
            queue_status=training_run_result.queue_status,
            duration_seconds=training_run_result.duration_seconds,
            completed_count=completed_count,
            failed_count=failed_count,
        )

        if training_run_result.queue_status != "completed":

            # If --stop-on-error was Requested, Stop the Campaign After the First Failure
            if command_line_arguments.stop_on_error:
                print_warning_message("Stopping campaign because --stop-on-error was requested")
                break

    # Final Campaign Summary
    completed_count = sum(training_run_result.queue_status == "completed" for training_run_result in training_run_result_list)
    failed_count = sum(training_run_result.queue_status == "failed" for training_run_result in training_run_result_list)
    print_success_message(f"Campaign finished | Completed: {completed_count} | Failed: {failed_count} | Report: {report_path}")

if __name__ == "__main__":

    main()
