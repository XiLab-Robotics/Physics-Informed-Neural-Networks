# Track1 Exact-Paper Family-Stage Launcher And Live Progress Rework

## Overview

This task replaces the current monolithic exact-paper paper-faithful launch
experience with a more operator-friendly surface modeled after the recovered
original unified launcher.

The immediate trigger is that the active `20`-run paper-faithful RCIM Model-Bank Reproduction
campaign was manually interrupted after remaining too long on the first `SVR`
run with poor live observability. The mathematical search protocol must remain
unchanged, but the operator experience must improve substantially.

The requested end state is:

- the interrupted full campaign is recorded as interrupted in the persistent
  campaign state;
- the exact-paper launcher surface can execute one family and one stage at a
  time, analogous to the recovered-original `-Stage` / `-Families` flow;
- live logging during `GridSearchCV` and historical `cross_validate(...)`
  replay is much richer and does not remain silent for long stretches;
- the operator can follow ongoing progress through readable heartbeat lines and
  a stronger progress display without changing the underlying math.

## Technical Approach

The implementation will keep the paper-faithful search protocol exactly as it
is numerically:

- same family definitions;
- same exact-paper grids;
- same train/test split policy;
- same historical `cross_validate(...)` replay stages.

Only the orchestration and observability surface will change.

The work will introduce a new exact-paper launcher wrapper analogous to the
recovered-original unified RCIM launcher. The new launcher will expose a
family-and-stage operator surface for the current RCIM Model-Bank Reproduction paper-faithful
campaign package, while still resolving the prepared campaign YAMLs generated
by the exact-paper campaign preparer.

The planned public CLI surface is:

- `-Direction Forward|Backward|Both`
- `-Family SVR|MLP|RF|DT|ET|ERT|GBM|HGBM|XGBM|LGBM|All`
- `-Stage Search|Eval|Export|LoadBest`
- `-Remote`
- `-NoEval`
- `-NoExport`
- `-BestParameterSummaryPath`
- `-GridSearchVerboseOverride`
- `-HistoricalCrossValidateVerboseOverride`

The logging and progress rework will focus on:

- more frequent heartbeat emission while the search wrapper is still active;
- explicit stage markers before and after:
  - split preparation;
  - wrapper search;
  - wrapper historical cross-validation;
  - per-target historical cross-validation;
  - summary writing;
  - evaluation;
  - export;
- operator-readable counters and elapsed-time reporting;
- a progress display in the PowerShell wrapper that reflects known config-level
  and substage-level advancement as closely as possible without rewriting the
  scikit-learn internals.

The rework will reuse the recovered-original launcher lessons and the policy
already formalized in:

- `doc/technical/2026-05/2026-05-04/2026-05-04-19-12-31_rcim_original_unified_launcher_and_best_parameter_flow.md`
- the later recovered-original launcher logging fixes on `2026-05-08`

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `scripts/campaigns/track_1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`
- `scripts/campaigns/track_1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `scripts/campaigns/track_1/exact_paper/invoke_exact_paper_campaign_local.ps1`
- `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py`
- `scripts/campaigns/track_1/exact_paper/prepare_track1_bidirectional_paper_faithful_grid_search_campaign.py`
- `doc/scripts/campaigns/run_track1_bidirectional_paper_faithful_grid_search_campaign.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/README.md`

## Implementation Steps

1. Confirm the active paper-faithful campaign state is recorded as interrupted
   in `doc/running/active_training_campaign.yaml`.
2. Design an exact-paper launcher surface analogous to the recovered-original
   unified launcher, with explicit direction, family, and stage selectors.
3. Refactor the current exact-paper launcher so it can resolve a selected
   family subset from the prepared `20`-run campaign package instead of always
   consuming the full queue.
4. Extend the shared streaming launcher and/or the Python exact-paper runners
   so long-running search and historical replay phases emit frequent progress
   updates and never stay silent for long stretches.
5. Add operator-readable progress indicators in the PowerShell wrapper using
   the best available config-level and substage-level counters.
6. Update the launcher note and the exact-paper workflow README so the new
   family/stage command surface is documented with ready-to-run examples.
7. Run focused verification on the new operator surface and scoped Markdown QA
   on all touched documentation.
