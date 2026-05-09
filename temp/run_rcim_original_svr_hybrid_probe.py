""" Run a temporary hybrid search with SVR RBF and scaled LinearSVR. """

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rcim_original_svr_temp_common import build_custom_hybrid_param_grid
from rcim_original_svr_temp_common import build_hybrid_rbf_plus_linear_svr_param_grid
from rcim_original_svr_temp_common import build_shared_argument_parser
from rcim_original_svr_temp_common import initialize_temp_cli
from rcim_original_svr_temp_common import parse_float_csv
from rcim_original_svr_temp_common import parse_int_csv
from rcim_original_svr_temp_common import resolve_dataframe_inputs
from rcim_original_svr_temp_common import resolve_output_json_path
from rcim_original_svr_temp_common import run_multioutput_svr_search
from rcim_original_svr_temp_common import write_json_summary


def main() -> None:

    """ Run the temporary hybrid probe. """

    initialize_temp_cli()
    parser = build_shared_argument_parser(__doc__)
    parser.add_argument("--rbf-c-values", default="1", help="Comma-separated RBF SVR C values.")
    parser.add_argument("--rbf-epsilon-values", default="1e-4,1e-6", help="Comma-separated RBF SVR epsilon values.")
    parser.add_argument("--rbf-gamma-values", default="1.1e-6", help="Comma-separated RBF SVR gamma values.")
    parser.add_argument("--linear-c-values", default="1", help="Comma-separated LinearSVR C values.")
    parser.add_argument("--linear-epsilon-values", default="0.0", help="Comma-separated LinearSVR epsilon values.")
    parser.add_argument("--linear-tol-values", default="1e-4", help="Comma-separated LinearSVR tolerance values.")
    parser.add_argument("--linear-max-iter-values", default="5000", help="Comma-separated LinearSVR max_iter values.")
    args = parser.parse_args()
    inputs = resolve_dataframe_inputs(args.direction, args.dataframe_path)
    parameter_grid = build_custom_hybrid_param_grid(
        rbf_c_values=parse_float_csv(args.rbf_c_values),
        rbf_epsilon_values=parse_float_csv(args.rbf_epsilon_values),
        rbf_gamma_values=parse_float_csv(args.rbf_gamma_values),
        linear_c_values=parse_float_csv(args.linear_c_values),
        linear_epsilon_values=parse_float_csv(args.linear_epsilon_values),
        linear_tol_values=parse_float_csv(args.linear_tol_values),
        linear_max_iter_values=parse_int_csv(args.linear_max_iter_values),
    )
    if parameter_grid == build_custom_hybrid_param_grid(
        rbf_c_values=[1.0],
        rbf_epsilon_values=[1e-4, 1e-6],
        rbf_gamma_values=[1.1e-6],
        linear_c_values=[1.0],
        linear_epsilon_values=[0.0],
        linear_tol_values=[1e-4],
        linear_max_iter_values=[5000],
    ):
        parameter_grid = build_hybrid_rbf_plus_linear_svr_param_grid()
    summary_payload = run_multioutput_svr_search(
        inputs=inputs,
        parameter_grid=parameter_grid,
        test_size=args.test_size,
        cv_folds=args.cv_folds,
        n_jobs=args.n_jobs,
        verbose=args.verbose,
    )
    output_json_path = resolve_output_json_path(args.output_json, "rcim_original_svr_hybrid_probe")
    write_json_summary(output_json_path, summary_payload)


if __name__ == "__main__":

    main()
