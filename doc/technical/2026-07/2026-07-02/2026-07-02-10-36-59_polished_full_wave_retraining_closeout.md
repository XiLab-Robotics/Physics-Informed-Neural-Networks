# Polished Full-Wave Retraining Closeout

## Overview

Close out the completed `polished_dataset_full_wave_retraining_2026_06_22`
campaign after operator execution. The campaign was prepared to retrain the
full non-paper model-development bank on `polished_dataset` across `global`,
`fw`, and `bw` surfaces.

The closeout must accept only the completed campaign artifacts that are already
present in the repository workspace. It must not run additional training and
must not execute the heavy `TE Curve Verification Pipeline`; that remains a
separate operator-approved workflow after normal campaign closeout.

## Technical Approach

The closeout will:

1. Re-parse the completed campaign execution report, leaderboard, best-run
   artifact, queue end state, and referenced run artifacts.
2. Confirm the campaign completed the expected `108` runs with no failed,
   running, or pending queue entries.
3. Publish a canonical campaign-results Markdown report and PDF companion under
   `doc/reports/campaign_results/cross_wave/polished_dataset/`.
4. Synchronize `doc/running/active_training_campaign.yaml` so the completed
   full-wave campaign becomes the latest completed campaign while previous
   polished RCIM and early-wave closeouts remain traceable.
5. Update the program status surfaces that materially change after this
   campaign, including the master summary, TE closeout ledger, and `doc/`
   index.
6. Validate Markdown and the exported PDF using the repository-owned QA
   workflow.

## Involved Components

- `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/`
  - completed campaign execution report, leaderboard, best-run files, and logs.
- `config/training/queue/polished_dataset_full_wave_retraining/`
  - queue end-state folders for completed, failed, running, and pending configs.
- `output/training_runs/`
  - referenced model run artifacts and checkpoints.
- `output/registries/`
  - family-level and program-level scalar registries updated by campaign
    execution.
- `doc/reports/campaign_results/cross_wave/polished_dataset/`
  - closeout report and PDF destination.
- `doc/running/active_training_campaign.yaml`
  - persistent campaign-state ledger.
- `doc/reports/analysis/Training Results Master Summary.md`
  - scalar training summary synchronized by the training runner and checked by
    closeout.
- `doc/reports/analysis/TE Program Status And Closeout Ledger.md`
  - canonical modeling-status ledger for completed campaign state.
- `scripts/reports/pdf/`
  - styled PDF export and validation tools.

## Implementation Steps

1. Inspect the current Git state and completed campaign artifacts before making
   additional closeout edits.
2. Compute the campaign acceptance summary from `campaign_leaderboard.yaml` and
   queue state.
3. Generate the closeout Markdown report with the scalar winner, surface
   winners, leaderboard snapshot, registry effect, and explicit
   `TE Curve Verification Pipeline` boundary.
4. Export the styled PDF and inspect the real PDF output for table fit,
   right-edge pressure, wrapped headers, and awkward page breaks.
5. Update `active_training_campaign.yaml`, the TE closeout ledger, and the
   documentation index.
6. Run Markdown QA and relevant syntax checks.
7. Stop before commit and report the completed closeout state for explicit user
   approval.
