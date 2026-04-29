"""Direct entrypoint for the recovered original RCIM dataframe-creation stage."""

import argparse
import json
import os
import shutil
import sys
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path


SCRIPT_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = SCRIPT_ROOT.parents[3]
UTILITIES_ROOT = SCRIPT_ROOT / "utilities"
DEFAULT_INSTANCES_PATH = REPOSITORY_ROOT / "reference" / "rcim_ml_compensation_recovered_assets" / "code" / "original_pipeline" / "instances_V3"
DEFAULT_VALIDATION_ROOT = REPOSITORY_ROOT / "output" / "validation_checks" / "paper_reimplementation_rcim_recovered_original_workflow"


def _ensure_utilities_on_path():
    """Expose the copied original utility modules to Python imports."""
    if str(UTILITIES_ROOT) not in sys.path:
        sys.path.insert(0, str(UTILITIES_ROOT))


def _normalize_direction(direction):
    """Map CLI direction aliases to the original RCIM suffixes."""
    normalized_direction = direction.strip().lower()
    if normalized_direction in {"fw", "forward"}:
        return "Fw", "forward"
    if normalized_direction in {"bw", "backward"}:
        return "Bw", "backward"
    raise ValueError(f"Unsupported direction: {direction}")


def _build_default_output_root(direction_label, output_suffix):
    """Create the default repository-owned runtime root for this stage."""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    suffix = f"_{output_suffix}" if output_suffix else ""
    return DEFAULT_VALIDATION_ROOT / f"{timestamp}__create_dataframe_{direction_label}{suffix}"


def _write_summary(summary_path, payload):
    """Persist a minimal JSON summary for reproducibility."""
    with open(summary_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


def _copy_directory_contents(source_directory_path, destination_directory_path):
    """Copy the source directory contents into the destination directory."""
    destination_directory_path.mkdir(parents=True, exist_ok=True)
    for child_path in source_directory_path.iterdir():
        target_path = destination_directory_path / child_path.name
        if child_path.is_dir():
            shutil.copytree(child_path, target_path, dirs_exist_ok=True)
        else:
            shutil.copy2(child_path, target_path)


def _prepare_runtime_instances_input(source_directory_path, runtime_cache_directory_path):
    """Prepare the input directory expected by the original Statistics helper."""
    source_file_list = list(source_directory_path.iterdir())
    if any(file_path.suffix.lower() == ".pickle" for file_path in source_file_list):
        _copy_directory_contents(source_directory_path, runtime_cache_directory_path)
        return runtime_cache_directory_path
    return source_directory_path


@contextmanager
def _pushd(target_directory_path):
    """Temporarily change the working directory."""
    original_directory = Path.cwd()
    os.chdir(target_directory_path)
    try:
        yield
    finally:
        os.chdir(original_directory)


def _build_argument_parser():
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--instances-path",
        type=Path,
        default=DEFAULT_INSTANCES_PATH,
        help="Directory containing the original RCIM instance CSVs or pickles.",
    )
    parser.add_argument(
        "--direction",
        default="backward",
        help="Direction to generate: forward/Fw or backward/Bw.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=None,
        help="Repository-owned runtime root. Defaults under output/validation_checks/.",
    )
    parser.add_argument(
        "--output-suffix",
        default="",
        help="Optional suffix appended to the default runtime root name.",
    )
    return parser


def main():
    """Run the recovered original dataframe-creation stage with repository paths."""
    parser = _build_argument_parser()
    args = parser.parse_args()

    _ensure_utilities_on_path()
    from statistics import Statistics  # pylint: disable=import-outside-toplevel

    direction_code, direction_label = _normalize_direction(args.direction)
    output_root = args.output_root or _build_default_output_root(direction_label, args.output_suffix)
    output_root = output_root.resolve()
    runtime_cache_directory_path = output_root / "instances_V3"
    runtime_cache_directory_path.mkdir(parents=True, exist_ok=True)

    instances_path = args.instances_path.resolve()
    runtime_instances_input_path = _prepare_runtime_instances_input(instances_path, runtime_cache_directory_path)
    output_csv_name = f"dataFrame_prediction_{direction_code}_v14_newFreq.csv"
    output_csv_path = output_root / output_csv_name

    with _pushd(output_root):
        statistics = Statistics()
        statistics.read_all_fft(str(runtime_instances_input_path))
        dataframe = statistics.genDfWithAmplEPhase(direction_code)
        dataframe.to_csv(output_csv_name, sep=";", decimal=",")

    _write_summary(
        output_root / "run_summary.json",
        {
            "stage": "create_dataframe",
            "direction": direction_label,
            "instances_path": str(instances_path),
            "runtime_instances_input_path": str(runtime_instances_input_path),
            "runtime_cache_directory_path": str(runtime_cache_directory_path),
            "output_csv_path": str(output_csv_path),
            "row_count": int(len(dataframe)),
            "column_count": int(len(dataframe.columns)),
        },
    )
    print(output_csv_path)


if __name__ == "__main__":
    main()
