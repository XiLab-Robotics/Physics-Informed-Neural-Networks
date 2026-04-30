""" Direct entrypoint for the recovered original RCIM dataframe-creation stage. """

import argparse
from pathlib import Path

try:

    # Import shared runtime helpers for the recovered original workflow.
    from workflow_runtime import REFERENCE_ROOT
    from workflow_runtime import build_default_output_root
    from workflow_runtime import ensure_utilities_on_path
    from workflow_runtime import normalize_direction
    from workflow_runtime import prepare_runtime_instances_input
    from workflow_runtime import pushd
    from workflow_runtime import write_summary

except ModuleNotFoundError:

    # Pragma: no cover - import compatibility for Sphinx
    from .workflow_runtime import REFERENCE_ROOT
    from .workflow_runtime import build_default_output_root
    from .workflow_runtime import ensure_utilities_on_path
    from .workflow_runtime import normalize_direction
    from .workflow_runtime import prepare_runtime_instances_input
    from .workflow_runtime import pushd
    from .workflow_runtime import write_summary

DEFAULT_INSTANCES_PATH = REFERENCE_ROOT / "instances_V3"

def _build_argument_parser():

    """ Build the CLI argument parser. """

    # Argument Parser
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--instances-path", type=Path, default=DEFAULT_INSTANCES_PATH, help="Directory containing the original RCIM instance CSVs or pickles.")
    parser.add_argument("--direction", default="backward", help="Direction to generate: forward/Fw or backward/Bw.")
    parser.add_argument("--output-root", type=Path, default=None, help="Repository-owned runtime root. Defaults under output/validation_checks/.")
    parser.add_argument("--output-suffix", default="", help="Optional suffix appended to the default runtime root name.")
    return parser

def main():

    """ Run the recovered original dataframe-creation stage with repository paths. """

    # Argument Parser
    parser = _build_argument_parser()
    args = parser.parse_args()

    # Ensure The Original Utility Modules Are On The Path For Imports
    ensure_utilities_on_path()

    # Import The Original Statistics Helper
    from utilities.statistics import Statistics

    # Normalize The Direction Argument
    direction_code, direction_label = normalize_direction(args.direction)
    output_root = args.output_root or build_default_output_root("create_dataframe", direction_label, args.output_suffix)
    output_root = output_root.resolve()

    # Keep The Legacy Local Cache Layout, But Only Inside The Immutable Repository-Owned Runtime Root.
    runtime_cache_directory_path = output_root / "instances_V3"
    runtime_cache_directory_path.mkdir(parents=True, exist_ok=True)

    # Prepare The Instance Directory Expected By The Original Statistics Helper
    instances_path = args.instances_path.resolve()
    runtime_instances_input_path = prepare_runtime_instances_input(instances_path, runtime_cache_directory_path)
    output_csv_name = f"dataFrame_prediction_{direction_code}_v14_newFreq.csv"
    output_csv_path = output_root / output_csv_name

    with pushd(output_root):

        # Call The Copied Original Dataframe-Generation Logic Without Changing Its Numerical Behavior.
        statistics = Statistics()
        statistics.read_all_fft(str(runtime_instances_input_path))
        dataframe = statistics.genDfWithAmplEPhase(direction_code)
        dataframe.to_csv(output_csv_name, sep=";", decimal=",")

    # Write The Run Summary
    write_summary(
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
