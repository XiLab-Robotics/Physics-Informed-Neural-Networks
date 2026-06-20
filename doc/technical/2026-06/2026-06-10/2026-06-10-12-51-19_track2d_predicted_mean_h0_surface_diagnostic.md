# CVP 1.4 Predicted Mean h0 Surface Diagnostic

## Overview

Prepare a follow-up diagnostic that compares each model's
`predicted_mean_deg` surface against measured `h0` / `truth_mean_deg` after the
completed `CVP 1.4` h0 cross-check showed that `h0` magnitude alone does not
explain most model offset failures.

## Technical Approach

Use the existing `CVP 1.4` per-curve metrics table as the canonical source for
`truth_mean_deg`, `predicted_mean_deg`, `signed_offset_error_deg`, operating
point, direction, candidate, and surface. Treat `truth_mean_deg` as the
measured `h0` value, already validated against the component-offset table by
the prior cross-check. Build per-candidate and per-surface diagnostics that
separate:

- constant mean bias;
- slope/compression error in `predicted_mean_deg` versus measured `h0`;
- direction-specific sign or offset behavior;
- speed, torque, and temperature regime structure;
- high-error candidates where large offset appears despite normal measured
  `h0`.

The report should stay analysis-only. It should not train models, promote
candidates, or introduce deploy-time corrections.

## Involved Components

- `output/validation_checks/track2d_mean_offset_full_matrix_audit/2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit/track2d_per_curve_metrics.csv`
- `output/validation_checks/track2d_h0_offset_crosscheck/2026-06-09-20-09-16__track2d_h0_offset_crosscheck/`
- `scripts/reports/analysis/`
- `doc/reports/analysis/track2/component_offset_identification/`
- `doc/README.md`
- `doc/running/te_model_live_backlog.md`

## Implementation Steps

1. Add a repository-owned report script that loads the `CVP 1.4` per-curve
   metrics and selects the most relevant candidates: largest mean offset error,
   current surface leaders, high h0/error-overlap candidates, and global
   high-error cases.
2. Compute candidate-level mean-prediction diagnostics: bias, absolute bias,
   slope/intercept between measured `h0` and predicted mean, correlation,
   residual standard deviation, P90 absolute offset error, and direction-level
   splits.
3. Generate selected visual assets comparing measured `h0`, predicted mean,
   and signed offset error by speed/torque with separate temperature and
   direction handling where the data supports it.
4. Write a dated Markdown report and PDF companion under the existing
   component-offset identification report folder, plus CSV/YAML artifacts under
   `output/validation_checks/track2d_predicted_mean_h0_surface_diagnostic/`.
5. Update the documentation index and live backlog with the resulting decision
   boundary for the next training/calibration branch.
6. Run scoped Markdown QA, Python compile checks, PDF validation, and
   `git diff --check`.
