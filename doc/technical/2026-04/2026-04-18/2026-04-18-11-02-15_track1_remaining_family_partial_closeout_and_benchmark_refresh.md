# Track 1 Remaining Family Partial Closeout And Benchmark Refresh

## Overview

This document formalizes the next repository step after the interrupted
`Track 1` remaining-family exact-paper campaign sequence.

The current observable state is:

- completed family campaigns:
  - `MLP`
  - `RF`
  - `DT`
  - `ET`
  - `ERT`
  - `GBM`
  - `HGBM`
- not yet completed family campaigns:
  - `XGBM`
  - `LGBM`

The user's requested next action is:

- verify the campaigns that appear to have finished successfully;
- close out those completed campaigns;
- update the canonical comparison tables with the new results;
- postpone crash investigation and the final two campaign reruns to a second
  step driven by the later terminal log review.

## Technical Approach

The repository should treat this situation as a partial campaign closeout, not
as a fully completed `9`-family sequence.

The correct implementation scope is:

1. inspect the materialized campaign outputs and validation artifacts for the
   `7` completed family campaigns;
2. verify whether each completed family campaign has the minimum required
   outputs for closeout:
   - campaign output directory;
   - logs;
   - validation-summary artifacts for amplitude and phase runs;
   - validation reports for amplitude and phase runs;
3. serialize campaign-level winner bookkeeping for the completed family
   campaigns when missing;
4. produce results reports only for the completed family campaigns;
5. update the canonical benchmark surface with the newly completed rows;
6. update the master summary so the active `Track 1` state reflects:
   - `7` completed family campaigns closed out;
   - `2` remaining interrupted families still pending rerun.

The interrupted aggregate sequence itself should not yet be represented as a
completed campaign-results package because the `XGBM` and `LGBM` branches still
need crash recovery and rerun.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/track1/exact_paper/track1_*_full_matrix_campaign_2026_04_18_00_48_05/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- `doc/reports/campaign_results/track1/exact_paper/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `models/paper_reference/rcim_track1/`

No subagent is planned for this work. The closeout and benchmark refresh
remain local to the repository workflow.

## Implementation Steps

1. Inspect the completed family campaign outputs for `MLP`, `RF`, `DT`, `ET`,
   `ERT`, `GBM`, and `HGBM`.
2. Confirm the absence or incompleteness of `XGBM` and `LGBM` so they remain
   excluded from the current closeout pass.
3. Generate family-level campaign bookkeeping artifacts where missing:
   - `campaign_leaderboard.yaml`
   - `campaign_best_run.yaml`
   - `campaign_best_run.md`
4. Write campaign-results reports for the `7` completed family campaigns.
5. Refresh `RCIM Paper Reference Benchmark.md` using only the newly verified
   completed family rows.
6. Refresh `Training Results Master Summary.md` so it reflects the partial
   closeout status and the still-pending interrupted families.
7. Leave crash diagnosis and rerun preparation for `XGBM` and `LGBM` to the
   later dedicated recovery step.
