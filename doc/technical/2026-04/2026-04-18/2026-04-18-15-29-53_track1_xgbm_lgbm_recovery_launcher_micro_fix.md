# Track 1 XGBM LGBM Recovery Launcher Micro Fix

## Overview

This technical document covers the micro-repair needed after the first
recovery attempt for the interrupted `Track 1` `XGBM` and `LGBM` remote
campaigns.

The previously approved recovery hardening added optional-dependency preflight
to `scripts/campaigns/run_exact_paper_campaign_remote.ps1`. That logic was
correct in intent but introduced a PowerShell runtime failure before the remote
host preflight could even start.

The observed error is:

`System.ArgumentException: Argument types do not match`

The stack trace points to:

- `Get-OptionalExactPaperDependencySpecificationList`
- `scripts/campaigns/run_exact_paper_campaign_remote.ps1`

This is therefore a launcher micro-fix task, not a model, YAML, or remote
environment task.

CRITICAL WARNING:
the affected launcher script and related launcher notes are currently listed in
`doc/running/active_training_campaign.yaml` as protected campaign files. They
must not be modified without explicit user approval.

No subagent use is planned for this implementation.

## Technical Approach

The failure happens before any remote execution. The most likely cause is the
way the optional-dependency helper currently builds and returns its list,
causing PowerShell to hit a runtime type mismatch during enumerable coercion.

The safest repair is to keep the same recovery behavior but simplify the helper
implementation:

1. avoid the current fragile list-return pattern;
2. return a plain PowerShell array of `PSCustomObject` records;
3. preserve the exact dependency mapping:
   - `XGBM -> xgboost -> XGBRegressor`
   - `LGBM -> lightgbm -> LGBMRegressor`
4. leave the remote preflight contract unchanged once the helper output is
   materialized correctly.

The implementation should stay intentionally narrow:

- fix the helper runtime error;
- re-validate the shared launcher parser behavior;
- update only the already affected launcher notes if wording needs alignment.

## Involved Components

- `scripts/campaigns/run_exact_paper_campaign_remote.ps1`
- `doc/scripts/campaigns/run_track1_xgbm_full_matrix_campaign.md`
- `doc/scripts/campaigns/run_track1_lgbm_full_matrix_campaign.md`
- `doc/scripts/campaigns/run_track1_remaining_family_full_matrix_campaigns.md`
- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Repair the optional-dependency helper in the shared remote exact-paper
   launcher.
2. Re-run local parser validation on the updated PowerShell file.
3. Keep the documentation aligned only if the user-facing launcher behavior
   changes.
4. Hand back the exact remote recovery commands for `XGBM` and `LGBM`.
