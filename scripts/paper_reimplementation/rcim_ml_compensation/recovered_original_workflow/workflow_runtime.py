""" Shared runtime helpers for the recovered original RCIM direct workflow. """

import os, sys, shutil, json
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

SCRIPT_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = SCRIPT_ROOT.parents[3]
UTILITIES_ROOT = SCRIPT_ROOT / "utilities"
REFERENCE_ROOT = (
    REPOSITORY_ROOT
    / "reference"
    / "rcim_ml_compensation_recovered_assets"
    / "code"
    / "original_pipeline"
)
DEFAULT_VALIDATION_ROOT = (
    REPOSITORY_ROOT
    / "output"
    / "validation_checks"
    / "paper_reimplementation_rcim_recovered_original_workflow"
)

def ensure_utilities_on_path():

    """ Expose the copied original utility modules to Python imports. """

    # The Recovered Original Workflow Relies On Utility Modules That Were Copied
    if str(UTILITIES_ROOT) not in sys.path: sys.path.insert(0, str(UTILITIES_ROOT))

def normalize_direction(direction):

    """ Map CLI direction aliases to the original RCIM suffixes. """

    normalized_direction = direction.strip().lower()

    # Map CLI Direction Aliases To The Original RCIM Suffixes
    if normalized_direction in {"fw", "forward"}: return "Fw", "forward"
    if normalized_direction in {"bw", "backward"}: return "Bw", "backward"
    raise ValueError(f"Unsupported direction: {direction}")

def build_default_output_root(stage_name, direction_label, output_suffix, mode_name=""):

    """ Create the default repository-owned runtime root for one workflow stage. """

    # Create a Timestamped Runtime Root For One Workflow Stage
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    mode_suffix = f"_{mode_name}" if mode_name else ""
    custom_suffix = f"_{output_suffix}" if output_suffix else ""
    return DEFAULT_VALIDATION_ROOT / f"{timestamp}__{stage_name}{mode_suffix}_{direction_label}{custom_suffix}"

def write_summary(summary_path, payload):

    """ Persist a minimal JSON summary for reproducibility. """

    # Persist The JSON Summary Payload
    with open(summary_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)

def copy_directory_contents(source_directory_path, destination_directory_path):

    """ Copy the source directory contents into the destination directory. """

    # Mirror The Original Folder-Local Runtime Expectation Inside One Repository-Owned Artifact Root.
    destination_directory_path.mkdir(parents=True, exist_ok=True)
    for child_path in source_directory_path.iterdir():
        target_path = destination_directory_path / child_path.name
        if child_path.is_dir(): shutil.copytree(child_path, target_path, dirs_exist_ok=True)
        else: shutil.copy2(child_path, target_path)

def prepare_runtime_instances_input(source_directory_path, runtime_cache_directory_path):

    """ Prepare the instance directory expected by the original Statistics helper. """

    # The Recovered Original Code Prefers Local Pickle Caches When Available.
    source_file_list = list(source_directory_path.iterdir())
    if any(file_path.suffix.lower() == ".pickle" for file_path in source_file_list):
        copy_directory_contents(source_directory_path, runtime_cache_directory_path)
        return runtime_cache_directory_path
    return source_directory_path

@contextmanager
def pushd(target_directory_path):

    """ Temporarily change the working directory. """

    # Temporarily Change The Working Directory
    original_directory = Path.cwd()
    os.chdir(target_directory_path)
    try: yield
    finally: os.chdir(original_directory)
