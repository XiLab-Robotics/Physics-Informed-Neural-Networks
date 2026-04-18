# Track 1 XGBM LGBM Recovery V2 Exact-Paper And Remote Preflight Fix

## Overview

This technical document covers the second recovery pass for the pending
`Track 1` `XGBM` and `LGBM` campaigns after the latest remote rerun attempt
progressed past package installation and exposed two new issues.

Observed issues from the latest `XGBM` rerun:

1. the remote preflight still prints a `conda.bat` command-binding error and
   does not correctly stop before the sync-and-run sequence;
2. the exact-paper `XGBM` parameter-grid builder fails during runtime because
   it assumes `learning_rate` is always numeric, while the current
   `XGBRegressor` default returned by `get_params()` is `None`.

The failing Python line is:

`float(base_estimator.get_params()["learning_rate"])`

inside `build_exact_paper_reference_parameter_grid("XGBM", ...)`.

This means the recovery problem is now split across:

- the shared remote exact-paper launcher;
- the repository-owned exact-paper model-bank support code.

CRITICAL WARNING:
the affected scripts and launcher notes are still listed in
`doc/running/active_training_campaign.yaml` as protected campaign files. They
must not be modified without explicit user approval.

No subagent use is planned for this implementation.

## Technical Approach

The fix should stay narrow and repair only the newly exposed recovery blockers.

For the remote launcher:

1. repair the `conda run ... python -c ...` quoting used by the optional
   dependency preflight;
2. make the dependency detection explicit and reliable for `XGBM` and `LGBM`;
3. fail early if `xgboost` or `lightgbm` is still missing instead of letting
   the launcher continue.

For the exact-paper family bank:

1. introduce safe fallback extraction for estimator parameters that may be
   `None`;
2. use those safe values when building the `XGBM` and, if needed, `LGBM`
   paper-reference parameter grids;
3. preserve the same exact-paper family identity and not widen the search
   beyond the repository-owned intended baseline.

The expected direction is not to redesign the family search. It is only to
make the current exact-paper implementation robust to modern estimator defaults
and to make the remote preflight truthful.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `scripts/campaigns/run_exact_paper_campaign_remote.ps1`
- `doc/scripts/campaigns/run_track1_xgbm_full_matrix_campaign.md`
- `doc/scripts/campaigns/run_track1_lgbm_full_matrix_campaign.md`
- `doc/scripts/campaigns/run_track1_remaining_family_full_matrix_campaigns.md`
- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Repair the remote optional-dependency preflight quoting and family detection.
2. Add safe parameter fallback handling in the exact-paper family-grid builder.
3. Re-validate the PowerShell parser and the touched Markdown scope.
4. Hand back the pending remote recovery commands for `XGBM` and `LGBM`.
