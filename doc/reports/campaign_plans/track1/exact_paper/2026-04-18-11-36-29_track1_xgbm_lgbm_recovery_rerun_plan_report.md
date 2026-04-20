# Track 1 XGBM LGBM Recovery Rerun Plan Report

## Overview

This planning report covers the recovery phase for the interrupted
`Track 1` remaining-family exact-paper batch.

The `2026-04-18` remote sequence stopped during the first `XGBM` run because
the remote Conda environment `standard_ml_lan_node` did not provide the
optional package `xgboost`. The aggregate batch therefore remains only
partially closed out, with two families still pending:

- `XGBM`
- `LGBM`

The recovery objective is not to repeat the seven already completed families.
It is to:

1. harden the remote exact-paper launcher with optional-dependency preflight;
2. re-run only the pending `XGBM` and `LGBM` exact-paper full-matrix campaigns;
3. refresh the canonical benchmark only after those two families complete.

## Failure Analysis

The crash happened before model fitting actually started for `XGBM`. The
remote traceback shows:

- family requested: `XGBM`
- first run: `track1_xgbm_amplitude_full_matrix`
- failing package requirement: `xgboost`

No evidence currently shows that `LGBM` itself is broken, but the same failure
class is possible because `lightgbm` is also an optional dependency. The
recovery path should therefore preflight both optional family packages before
runtime:

- `xgboost`
- `lightgbm`

## Recovery Scope

The recovery package should stay narrow:

| Campaign | Runs | Status |
| --- | --- | --- |
| `track1_xgbm_full_matrix_campaign_2026_04_18_00_48_05` | amplitude, phase | pending rerun |
| `track1_lgbm_full_matrix_campaign_2026_04_18_00_48_05` | amplitude, phase | pending rerun |

The seven already completed families remain closed out and should not be
relaunched.

## Remote Dependency Preflight Rule

Before the remote sync-and-run stage starts, the launcher should derive the
required optional packages from the requested family scope and verify import
availability in the remote Conda environment.

Expected mapping:

| Family | Python Package | Import Surface |
| --- | --- | --- |
| `XGBM` | `xgboost` | `XGBRegressor` |
| `LGBM` | `lightgbm` | `LGBMRegressor` |

If one package is missing, the remote launcher should stop immediately with a
clear preflight failure instead of failing later during model creation.

## Candidate Execution Order

Recommended recovery order:

1. repair the remote environment so `xgboost` and `lightgbm` are installed in
   `standard_ml_lan_node`;
2. run the dedicated `XGBM` campaign in remote mode;
3. run the dedicated `LGBM` campaign in remote mode;
4. perform the final remaining-family closeout and benchmark refresh.

## Intended Recovery Commands

After the launcher-hardening implementation is approved and generated, the
intended commands remain:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_xgbm_full_matrix_campaign.ps1 -Remote
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_lgbm_full_matrix_campaign.ps1 -Remote
```

If the user prefers the convenience wrapper, the aggregate launcher may also be
used again, but only after the pending-queue behavior is confirmed to skip the
already completed families cleanly.

## Acceptance Criteria

The recovery phase should be considered complete only when all of the following
are true:

1. remote optional-dependency preflight fails early and names missing packages
   explicitly;
2. `XGBM` remote campaign completes or fails for a model/runtime reason beyond
   missing package setup;
3. `LGBM` remote campaign completes or fails for a model/runtime reason beyond
   missing package setup;
4. the final remaining-family campaign closeout updates:
   - `RCIM Paper Reference Benchmark.md`
   - `Training Results Master Summary.md`
   - `doc/running/active_training_campaign.yaml`

## Approval Gate

Implementation should start only after explicit approval of:

1. the technical recovery document;
2. this recovery rerun planning report;
3. the narrow scope decision to harden the launcher and rerun only `XGBM` and
   `LGBM`.
