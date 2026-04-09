# Track 1 Second Harmonic-Wise Iteration

## Overview

This document proposes the next implementation pass for `Track 1`, the
repository-owned paper-faithful harmonic-wise reproduction branch derived from
`reference/RCIM_ML-compensation.pdf`.

The first implemented baseline already proves that the offline harmonic-wise
pipeline works end to end:

- harmonic decomposition is running;
- harmonic-target prediction is running;
- TE reconstruction is running;
- offline `Robot` and `Cycloidal` playback probes are running;
- the paper-comparable offline validation path is running.

However, the current baseline does not yet meet `Target A`.

Current status:

- current test mean percentage error: `9.403%`
- current validation mean percentage error: `9.474%`
- target threshold from the paper: `<= 4.7%`
- current `Target A` status: `not_yet_met`

At the same time, the oracle reconstruction result is already materially
better:

- current oracle test mean percentage error: `2.749%`

This indicates that the selected harmonic representation is expressive enough
and that the current bottleneck is the predictor from operating conditions to
harmonic coefficients rather than the reconstruction layer itself.

The goal of this second iteration is therefore not to open a new branch, but
to improve the existing `Track 1` pipeline until it has a realistic path to
closing `Target A`.

## Technical Approach

Use a staged experimental progression rather than one monolithic retraining
pass.

The core idea is:

1. reduce the harmonic set temporarily to the most deployment-relevant terms in
   order to isolate predictor behavior;
2. improve feature engineering and predictor capacity on that smaller problem;
3. measure which harmonic groups dominate the residual error;
4. promote the improved predictor configuration back toward the full RCIM
   harmonic set;
5. require the final promotion candidate to reach at least the harmonic set
   used in the paper:
   - `0`
   - `1`
   - `3`
   - `39`
   - `40`
   - `78`
   - `81`
   - `156`
   - `162`
   - `240`

This means the reduced harmonic sets are debugging and optimization stages, not
the final scope of `Track 1`.

The final acceptance bar for this branch remains:

- paper-faithful offline structure;
- RCIM-aligned harmonic coverage;
- `<= 4.7%` mean percentage error on the comparable offline benchmark.

The second iteration should therefore evaluate three coupled levers:

- harmonic-set progression;
- operating-condition feature engineering;
- predictor configuration refinement.

Planned harmonic-set progression:

1. `0, 1, 39`
2. `0, 1, 39, 40`
3. `0, 1, 39, 40, 78`
4. promoted best configuration on the full RCIM set:
   `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`

Planned feature-engineering additions:

- `speed * torque`
- `speed * temperature`
- `torque * temperature`
- `speed^2`
- `torque^2`

Planned predictor refinements:

- higher-capacity `HistGradientBoosting` variants
- potentially per-target tuning rather than one fully uniform setting
- optional `RandomForest` comparison as a diagnostic baseline only, not as a
  deployment promotion target

Planned analysis additions:

- per-harmonic error breakdown
- explicit reporting of which harmonics dominate the curve-level percentage
  error
- comparison of reduced-set versus full-set behavior

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/running/te_model_live_backlog.md`
- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_support.py`
- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`

## Implementation Steps

1. Extend the harmonic-wise configuration layer so multiple harmonic-set
   presets can be executed cleanly under the paper-reimplementation root.
2. Add feature-engineering support for the derived operating-condition features
   required by the second iteration.
3. Add predictor-configuration support for the refined harmonic-wise tree
   baselines and any diagnostic `RandomForest` comparison runs.
4. Add per-harmonic error reporting so the validation summary and Markdown
   report expose which harmonic groups dominate the current residual error.
5. Execute the staged progression:
   - `0, 1, 39`
   - `0, 1, 39, 40`
   - `0, 1, 39, 40, 78`
6. Promote the best improved configuration back to the full RCIM harmonic set:
   - `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
7. Compare every second-iteration run against the current baseline at
   `9.403%` test mean percentage error and update the canonical paper-reference
   reporting accordingly.
8. Close this iteration only after the repository has clear evidence either
   that:
   - `Target A` is met on the full RCIM-aligned harmonic set;
   - or another precisely justified follow-up iteration is required.
