""" Shared runtime helpers for the recovered original RCIM direct workflow. """

import hashlib
import json
import os
import re
import shutil
import sys
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
DATA_ROOT = REPOSITORY_ROOT / "data"
DEFAULT_INSTANCE_CACHE_ROOT = (
    DATA_ROOT
    / "paper_reimplementation_rcim_recovered_original_workflow"
    / "instance_pickle_cache"
)
DEFAULT_VALIDATION_ROOT = (
    REPOSITORY_ROOT
    / "output"
    / "validation_checks"
    / "paper_reimplementation_rcim_recovered_original_workflow"
)


def ensure_utilities_on_path():

    """ Expose the copied original utility modules to Python imports. """

    # The Recovered Original Workflow Relies On Utility Modules That Were Copied.
    if str(UTILITIES_ROOT) not in sys.path:
        sys.path.insert(0, str(UTILITIES_ROOT))


def normalize_direction(direction):

    """ Map CLI direction aliases to the original RCIM suffixes. """

    normalized_direction = direction.strip().lower()

    # Map CLI Direction Aliases To The Original RCIM Suffixes.
    if normalized_direction in {"fw", "forward"}:
        return "Fw", "forward"
    if normalized_direction in {"bw", "backward"}:
        return "Bw", "backward"
    raise ValueError(f"Unsupported direction: {direction}")


def build_default_output_root(stage_name, direction_label, output_suffix, mode_name=""):

    """ Create the default repository-owned runtime root for one workflow stage. """

    # Create A Timestamped Runtime Root For One Workflow Stage.
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    mode_suffix = f"_{mode_name}" if mode_name else ""
    custom_suffix = f"_{output_suffix}" if output_suffix else ""
    return DEFAULT_VALIDATION_ROOT / f"{timestamp}__{stage_name}{mode_suffix}_{direction_label}{custom_suffix}"


def ensure_directory(directory_path):

    """ Ensure that one directory exists and return the resolved path. """

    # Create The Directory Before Returning The Normalized Path.
    directory_path = Path(directory_path).resolve()
    directory_path.mkdir(parents=True, exist_ok=True)
    return directory_path


def build_default_instance_cache_directory(source_directory_path):

    """ Build the shared repository-owned pickle cache directory for one source tree. """

    # Encode The Source Tree Into A Stable, Human-Readable Cache Folder Name.
    normalized_source = Path(source_directory_path).resolve()
    relative_parts = normalized_source.parts[-2:]
    readable_stem = "_".join(relative_parts)
    readable_stem = re.sub(r"[^A-Za-z0-9]+", "_", readable_stem).strip("_").lower()
    source_hash = hashlib.sha1(str(normalized_source).encode("utf-8")).hexdigest()[:12]
    cache_directory_name = f"{readable_stem}_{source_hash}" if readable_stem else source_hash
    return DEFAULT_INSTANCE_CACHE_ROOT / cache_directory_name


def resolve_instance_cache_directory(source_directory_path, cache_directory_path=None):

    """ Resolve the shared pickle cache directory for one source tree. """

    # Use The Explicit Cache Directory When The Caller Provides One.
    if cache_directory_path is not None:
        return ensure_directory(cache_directory_path)

    # Otherwise Build The Stable Repository-Owned Cache Path Under data/.
    default_cache_directory = build_default_instance_cache_directory(source_directory_path)
    return ensure_directory(default_cache_directory)


def write_summary(summary_path, payload):

    """ Persist a minimal JSON summary for reproducibility. """

    # Persist The JSON Summary Payload.
    with open(summary_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


def copy_directory_contents(source_directory_path, destination_directory_path):

    """ Copy the source directory contents into the destination directory. """

    # Mirror The Original Folder-Local Runtime Expectation Inside One Repository-Owned Artifact Root.
    destination_directory_path = ensure_directory(destination_directory_path)
    for child_path in Path(source_directory_path).iterdir():
        target_path = destination_directory_path / child_path.name
        if child_path.is_dir():
            shutil.copytree(child_path, target_path, dirs_exist_ok=True)
        else:
            shutil.copy2(child_path, target_path)


def copy_dataframe_to_runtime(source_dataframe_path, runtime_root, direction_code):

    """ Copy one dataframe into the runtime root using the original filename. """

    # Preserve The Original Filename Contract Inside The Repository-Owned Runtime Root.
    runtime_dataframe_name = f"dataFrame_prediction_{direction_code}_v14_newFreq.csv"
    runtime_dataframe_path = Path(runtime_root) / runtime_dataframe_name
    shutil.copy2(source_dataframe_path, runtime_dataframe_path)
    return runtime_dataframe_name, runtime_dataframe_path


def build_prediction_output_folder_name(mode_name, direction_code):

    """ Resolve the original-style prediction folder for one training mode. """

    # Keep The Historical Folder Naming Contract For The Copied Original Helpers.
    if mode_name == "paper_eval":
        return f"output_prediction/instV3.8_{direction_code}_allFreq_def/"
    return "output_prediction/"


@contextmanager
def pushd(target_directory_path):

    """ Temporarily change the working directory. """

    # Temporarily Change The Working Directory.
    original_directory = Path.cwd()
    os.chdir(target_directory_path)
    try:
        yield
    finally:
        os.chdir(original_directory)
