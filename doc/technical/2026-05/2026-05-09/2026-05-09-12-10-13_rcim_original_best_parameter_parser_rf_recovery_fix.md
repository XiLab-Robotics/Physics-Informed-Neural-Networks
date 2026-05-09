# RCIM Original Best Parameter Parser RF Recovery Fix

## Overview

The recovered-original RCIM unified launcher completed the `Backward` `Retune`
stage for family `RF`, persisted the retune artifacts, and then failed only in
the downstream `Eval` stage.

The failure occurs when the launcher reuses the generated
`summaryBestParameter+_3.8_allFreq.csv` file and the training surface parses
the stored best-parameter payload before instantiating the
`RandomForestRegressor`.

The concrete failure is:

- the retune summary stores the correct key `estimator__n_estimators`;
- the current parser rewrites `estimator__n_estimator` to
  `estimator__n_estimators` using a broad substring replacement;
- when the source string already contains `estimator__n_estimators`, the broad
  replacement corrupts it into `n_estimatorss`;
- `set_params(...)` then fails during `Eval`.

This means the expensive `Retune` result is already valid and the recovery path
should be limited to a parser fix followed by a rerun of only `Eval` and
`Export`.

## Technical Approach

Apply a narrow parser fix in the recovered-original RCIM training surface so
historical malformed parameter keys are normalized without corrupting already
correct keys.

The fix should:

1. keep compatibility with any older payloads that may contain
   `estimator__n_estimator`;
2. avoid rewriting the valid key `estimator__n_estimators`;
3. preserve the current retune summary contract and registry flow;
4. avoid re-running the completed `Retune` stage.

After the code fix:

- the existing `RF` retune bundle can be reused directly;
- the operator only needs to rerun `Eval` and `Export` against the stored
  `summaryBestParameter+_3.8_allFreq.csv` file from the completed retune
  bundle.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/guide/project_usage_guide.md`
- `doc/technical/2026-05/2026-05-09/2026-05-09-12-10-13_rcim_original_best_parameter_parser_rf_recovery_fix.md`

## Implementation Steps

1. Narrow the best-parameter payload sanitation logic so only the malformed
   historical key is normalized and the valid `n_estimators` key remains
   unchanged.
2. Re-run a local parser-targeted smoke validation using an `RF`
   `summaryBestParameter+_3.8_allFreq.csv` payload equivalent to the crashed
   bundle.
3. Verify that the fixed path can instantiate the `RF` paper-eval model
   successfully without re-running `Retune`.
4. Update the operator-facing workflow notes if the recovery path needs a
   durable note.
5. Run Markdown QA on the touched Markdown scope before closing the task.
