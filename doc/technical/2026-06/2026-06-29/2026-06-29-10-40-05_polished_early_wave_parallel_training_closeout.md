# Polished Early-Wave Parallel Training Closeout

## Overview

The operator reported that the local
`polished_dataset_early_wave_parallel_training_2026_06_25` campaign has
completed. The inspected campaign artifact root is:

```text
output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25
```

Initial artifact inspection found:

- completed queue entries: `36`;
- failed queue entries: `0`;
- running queue entries: `0`;
- pending queue entries: `0`;
- leaderboard entries: `36`;
- surface split: `12` global, `12` forward-only, and `12` backward-only runs;
- dataset: `polished_dataset`;
- dataset schema: `polished_point_v1`;
- no missing referenced metric, report, or checkpoint artifact.

The scalar leaderboard winner is currently
`te_periodic_gru_sequence_bw`, with test `MAE` `0.0010836307192221284`
and test `RMSE` `0.0013926418032497168`.

## Technical Approach

Perform a normal campaign closeout for the completed early-wave
`polished_dataset` batch. This is not a `TE Curve Verification Pipeline`
refresh. The closeout will accept the completed 36-run campaign artifacts,
publish a repository campaign-results report and PDF companion, synchronize
registry-facing status documents, and close the active campaign state while
preserving the parallel RCIM campaign provenance that is still recorded as
operator-running on another workstation.

The closeout must not launch additional training and must not execute the heavy
offline verification matrix. Any later `TE Curve Verification Pipeline`
refresh remains a separate operator-approved step after this closeout.

## Involved Components

- `doc/running/active_training_campaign.yaml`
  - protected active campaign state that currently still records the
    early-wave campaign as `prepared`;
  - also preserves the parallel
    `polished_dataset_rcim_model_bank_reproduction_2026_06_22` provenance.
- `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/`
  - completed campaign manifest, execution report, leaderboard, logs, and
    winner files.
- `config/training/queue/polished_dataset_early_wave_parallel_training/`
  - final queue state, expected to contain all 36 configs under `completed/`.
- `output/training_runs/`
  - per-run metrics, checkpoints, and training reports referenced by the
    leaderboard.
- `output/registries/families/`
  - family-level registries updated by the completed runs.
- `output/registries/program/current_best_solution.yaml`
  - program-level scalar best registry after early-wave completion.
- `doc/reports/campaign_results/cross_wave/polished_dataset/`
  - destination for the closeout Markdown report and PDF companion.
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
  - canonical training-result summary to synchronize with the completed
    early-wave result.
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
  - program ledger to inspect and update only if this closeout materially
    changes current modeling status.
- `doc/README.md`
  - technical-document and campaign-results index.

## Implementation Steps

1. Re-parse the completed campaign root, queue end state, leaderboard, best-run
   artifact, and referenced per-run metric/report/checkpoint paths.
2. Create the campaign-results Markdown report under
   `doc/reports/campaign_results/cross_wave/polished_dataset/`.
3. Export the report to a styled PDF using the repository-owned PDF workflow
   and validate the real exported PDF.
4. Update `doc/running/active_training_campaign.yaml` from the stale
   `prepared` state to a completed closeout state while preserving the parallel
   RCIM campaign block.
5. Synchronize the Training Results Master Summary with the accepted
   early-wave campaign winner and surface-level winners.
6. Inspect the TE Program Status And Closeout Ledger and update it only if the
   campaign result changes the current closeout state.
7. Register the campaign-results report and this technical document from
   `doc/README.md`.
8. Run Markdown QA on the touched Markdown scope, PDF validation on the real
   exported report PDF, and repository consistency checks such as
   `git diff --check`.
9. Stop before creating any Git commit and request explicit commit approval.
