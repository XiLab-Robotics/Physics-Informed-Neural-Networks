""" Run temporary SVR kernel probes and estimate the ETA of the original search. """

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rcim_original_svr_temp_common import build_original_svr_param_grid
from rcim_original_svr_temp_common import build_prefixed_candidate_list
from rcim_original_svr_temp_common import build_shared_argument_parser
from rcim_original_svr_temp_common import initialize_temp_cli
from rcim_original_svr_temp_common import resolve_dataframe_inputs
from rcim_original_svr_temp_common import resolve_output_json_path
from rcim_original_svr_temp_common import run_multioutput_svr_search
from rcim_original_svr_temp_common import write_json_summary


def main() -> None:

    """ Run one temporary ETA probe from a controlled canonical-grid subset. """

    initialize_temp_cli()
    parser = build_shared_argument_parser(__doc__)
    parser.add_argument("--kernel", choices=["rbf", "linear"], default="linear", help="Kernel subset to probe.")
    parser.add_argument("--candidate-count", type=int, default=2, help="How many canonical candidates to probe for the selected kernel.")
    args = parser.parse_args()

    inputs = resolve_dataframe_inputs(args.direction, args.dataframe_path)
    original_grid = build_original_svr_param_grid()
    candidate_list = build_prefixed_candidate_list(original_grid, args.kernel, args.candidate_count)
    summary_payload = run_multioutput_svr_search(
        inputs=inputs,
        parameter_grid=candidate_list,
        test_size=args.test_size,
        cv_folds=args.cv_folds,
        n_jobs=args.n_jobs,
        verbose=args.verbose,
    )
    full_kernel_candidate_count = len(build_prefixed_candidate_list(original_grid, args.kernel, 10_000))
    if summary_payload["candidate_count"] > 0:
        candidate_scale = full_kernel_candidate_count / summary_payload["candidate_count"]
    else:
        candidate_scale = None
    if candidate_scale is not None:
        estimated_full_kernel_seconds = summary_payload["elapsed_seconds"] * candidate_scale
    else:
        estimated_full_kernel_seconds = None
    summary_payload["probe_kernel"] = args.kernel
    summary_payload["full_kernel_candidate_count"] = full_kernel_candidate_count
    summary_payload["estimated_full_kernel_seconds"] = estimated_full_kernel_seconds
    output_json_path = resolve_output_json_path(args.output_json, f"rcim_original_svr_eta_probe_{args.kernel}")
    write_json_summary(output_json_path, summary_payload)


if __name__ == "__main__":

    main()
