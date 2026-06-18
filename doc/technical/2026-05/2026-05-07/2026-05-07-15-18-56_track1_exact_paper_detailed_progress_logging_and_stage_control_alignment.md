# Track 1 Exact-Paper Detailed Progress Logging And Stage Control Alignment

## Overview

This document plans a combined observability and control-surface upgrade for
the `Track 1` exact-paper reimplementation under
`scripts/paper_reimplementation/rcim_ml_compensation/`.

The immediate operator problem is that the active paper-faithful bidirectional
campaign can remain on `SVR 1/20` for days while exposing only the initial
`Grid search configured` line and no reliable internal heartbeat. The user also
wants the reimplementation-side training flow to be manageable in the same
spirit as the recovered original RCIM pipeline introduced by commits
`c4e5cb9b0d5daf46d2d2c5c49bfe4e9ebdcbe0b6`,
`7c82f3b72ad7fd1821d50a7f2af137940ca3b0b5`, and
`daffa0d3112095fac6f683a476854331131334c3`.

This work therefore targets two coupled goals:

- add much more detailed and frequent live progress logging inside the exact
  paper-faithful training/search protocol;
- expose a stage-aware training control surface for the exact-paper branch that
  mirrors the recovered-original operator experience, including explicit
  management of best-parameter handoff and downstream evaluation/export stages.

CRITICAL WARNING: the active campaign state is currently `running` in
`doc/running/active_training_campaign.yaml`, and the protected file list
includes the paper-faithful launcher and shared campaign infrastructure.
Implementation must therefore preserve campaign-state integrity and must not
silently mutate the active queue semantics.

## Technical Approach

The implementation will align the exact-paper branch with the operator
principles already adopted for the recovered-original RCIM workflow, while
keeping the exact-paper numerical protocol intact.

The planned technical changes are:

- introduce flush-safe, high-frequency progress emission around the exact-paper
  `GridSearchCV` and historical `cross_validate(...)` replay stages;
- surface granular progress markers before and after:
  - train/test split materialization;
  - family-level fit start;
  - parameter-grid construction and candidate counting;
  - `GridSearchCV.fit(...)` start and completion;
  - wrapper-level `cross_validate(...)` start and completion;
  - per-target `cross_validate(...)` start and completion;
  - summary/report persistence;
  - validation/report/export stage transitions;
- extend the local exact-paper runner and its launcher surface so the operator
  can invoke normalized stages analogously to the recovered-original workflow,
  instead of only the current monolithic `campaign config -> full run`
  execution shape;
- define an exact-paper best-parameter persistence and reuse path so one
  completed paper-faithful grid-search run can feed later evaluation/export
  stages without rerunning the full search;
- reuse the original-pipeline control model from
  `2026-05-04-19-12-31_rcim_original_unified_launcher_and_best_parameter_flow.md`
  as the behavioral template, but map it onto the exact-paper branch-specific
  files and artifacts;
- keep the paper-faithful search semantics unchanged:
  - same family definitions;
  - same parameter grids;
  - same `train_test_split(..., random_state=0)`;
  - same historical wrapper and per-target `cross_validate(...)` replay;
- add operator-visible heartbeat output in places where sklearn itself does not
  provide stable fine-grained progress signals, instead of relying only on
  `verbose` chatter.

Context7 must be used for any scikit-learn API-detail decisions touched during
implementation, especially around `GridSearchCV`, `cross_validate`, and
progress-related parameter behavior.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py`
- `scripts/campaigns/track_1/exact_paper/invoke_exact_paper_campaign_local.ps1`
- `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1`
- `scripts/campaigns/track_1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`
- `scripts/campaigns/track_1/exact_paper/prepare_track1_bidirectional_paper_faithful_grid_search_campaign.py`
- `doc/scripts/campaigns/run_track1_bidirectional_paper_faithful_grid_search_campaign.md`
- `doc/running/active_training_campaign.yaml`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`

## Implementation Steps

1. Audit the exact-paper local runner, shared training support, and current
   paper-faithful campaign launcher against the recovered-original launcher and
   progress-logging commits that the user referenced.
2. Design the exact-paper stage vocabulary and best-parameter handoff rules so
   they mirror the recovered-original operator surface without changing the
   exact-paper numerical protocol.
3. Add detailed family-level and sub-stage progress markers to the
   exact-paper Python training path, with special attention to the long
   `SVR` search and historical `cross_validate(...)` replay stages.
4. Extend the exact-paper launcher/control path so the operator can run
   search-only, evaluation-only, export-only, or stored-best downstream stages
   in a normalized way comparable to the original unified launcher.
5. Update the paper-faithful campaign preparer/launcher/note surface so the
   new logging and stage-control contract is explicit and the active campaign
   state remains accurate.
6. Run targeted verification on the exact-paper path:
   - Python compile checks for touched scripts;
   - narrow launcher print-only or smoke checks for stage resolution;
   - Markdown QA on the touched documentation scope.
7. Report the implementation outcome and wait for explicit approval before any
   commit.
