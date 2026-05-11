# RCIM Original LGBM Retune Log Flood And Failure Capture Fix

## Overview

The recovered-original RCIM `retune` path for the `LGBM` family currently
floods the console with repeated LightGBM warnings such as
`No further splits with positive gain, best gain: -inf` and repeated
auto-threading info lines. In practice that flood hides the repository-owned
progress lines, makes the terminal difficult to use, and prevents the operator
from reliably seeing the final failure reason when the run later crashes.

The current behavior is operationally unacceptable even when the underlying
LightGBM warnings are non-fatal. The workflow needs a narrow fix that keeps the
historical training protocol intact while making the `LGBM` retune path
readable, diagnosable, and recoverable.

## Technical Approach

The fix will target the recovered-original training and launcher surfaces
without changing the mathematical search protocol:

1. Reduce LightGBM-native logging noise in the repository-owned `LGBMRegressor`
   instantiation by using documented logging controls and stable threading
   configuration, including `verbosity` and `force_col_wise`.
2. Preserve the repository-owned retune progress lines so the operator can
   still see stage-level progress around `GridSearchCV`, wrapper
   `cross_validate(...)`, and per-target `cross_validate(...)`.
3. Preserve the true Python traceback and final failure reason in the stage log
   files even when the console is noisy or VS Code later becomes unstable.
4. Keep the fix narrow to `LGBM` logging and failure-capture behavior; do not
   change the recovered-original `GridSearchCV + cross_validate + per-target
   cross_validate` protocol.

Context7 was used for the LightGBM parameter surface in this session. The
relevant documented guidance is that `verbosity` controls logging level and
that `force_col_wise=true` removes the auto-selection overhead/info chatter for
the histogram strategy.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/guide/project_usage_guide.md`
- `doc/technical/2026-05/2026-05-11/2026-05-11-15-39-02_rcim_original_lgbm_retune_log_flood_and_failure_capture_fix.md`

## Implementation Steps

1. Inspect the current recovered-original `LGBMRegressor` instantiation and the
   launcher logging contract for the `retune` path.
2. Apply a narrow LightGBM logging-control fix so repeated native warnings and
   info lines stop flooding the operator console during `retune`.
3. Confirm that repository-owned progress lines remain visible and that the
   final traceback still lands in the persistent stage logs.
4. Run a narrow validation probe focused on `LGBM` retune startup and log
   readability rather than the full long-running search completion.
5. Update the recovered-original workflow documentation if the operator-facing
   logging contract changes.
6. Run Markdown QA on the touched Markdown scope before closing the task.
