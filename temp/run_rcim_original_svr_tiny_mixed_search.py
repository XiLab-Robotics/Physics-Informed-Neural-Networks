""" Run a tiny temporary mixed RBF plus linear SVR search for RCIM diagnostics. """

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rcim_original_svr_temp_common import build_shared_argument_parser
from rcim_original_svr_temp_common import build_tiny_mixed_param_grid
from rcim_original_svr_temp_common import initialize_temp_cli
from rcim_original_svr_temp_common import resolve_dataframe_inputs
from rcim_original_svr_temp_common import resolve_output_json_path
from rcim_original_svr_temp_common import run_multioutput_svr_search
from rcim_original_svr_temp_common import write_json_summary


def main() -> None:

    """ Run the tiny temporary search. """

    initialize_temp_cli()
    parser = build_shared_argument_parser(__doc__)
    args = parser.parse_args()
    inputs = resolve_dataframe_inputs(args.direction, args.dataframe_path)
    summary_payload = run_multioutput_svr_search(
        inputs=inputs,
        parameter_grid=build_tiny_mixed_param_grid(),
        test_size=args.test_size,
        cv_folds=args.cv_folds,
        n_jobs=args.n_jobs,
        verbose=args.verbose,
    )
    output_json_path = resolve_output_json_path(args.output_json, "rcim_original_svr_tiny_mixed_search")
    write_json_summary(output_json_path, summary_payload)


if __name__ == "__main__":

    main()
