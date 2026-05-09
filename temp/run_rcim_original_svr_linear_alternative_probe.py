""" Compare temporary SVR linear and LinearSVR fits on the RCIM dataset surface. """

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rcim_original_svr_temp_common import build_shared_argument_parser
from rcim_original_svr_temp_common import initialize_temp_cli
from rcim_original_svr_temp_common import resolve_dataframe_inputs
from rcim_original_svr_temp_common import resolve_output_json_path
from rcim_original_svr_temp_common import run_linear_model_comparison
from rcim_original_svr_temp_common import write_json_summary


def main() -> None:

    """ Run the temporary SVR linear versus LinearSVR comparison. """

    initialize_temp_cli()
    parser = build_shared_argument_parser(__doc__)
    args = parser.parse_args()
    inputs = resolve_dataframe_inputs(args.direction, args.dataframe_path)
    summary_payload = run_linear_model_comparison(
        inputs=inputs,
        test_size=args.test_size,
        n_jobs=args.n_jobs,
        verbose=args.verbose,
    )
    output_json_path = resolve_output_json_path(args.output_json, "rcim_original_svr_linear_alternative_probe")
    write_json_summary(output_json_path, summary_payload)


if __name__ == "__main__":

    main()
