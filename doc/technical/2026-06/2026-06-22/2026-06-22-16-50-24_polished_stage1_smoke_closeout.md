# Polished Stage 1 Smoke Closeout

## Overview

The operator reported that the local
`polished_dataset_stage1_smoke_2026_06_21` campaign completed. The current
canonical completed output is:

```text
output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21
```

The campaign execution report records:

- completed runs: `8`;
- failed runs: `0`;
- campaign scalar winner:
  `te_periodic_gru_sequence_remote_global`;
- winner test `MAE`: `0.0012794497888535261`;
- winner test `RMSE`: `0.0016375193372368813`;
- dataset schema for neural winner: `polished_point_v1`;
- input features: `theta`, `theta_dot`, `tau_load`, `T`;
- target feature: `theta_TE`.

This closeout must preserve earlier failed and interrupted attempts as
diagnostic history while accepting the `13:09:57` attempt as the successful
Stage 1 smoke result.

## Technical Approach

Perform a normal campaign closeout, not a `TE Curve Verification Pipeline`
refresh. The closeout should:

1. Inspect the final campaign execution report, leaderboard, best-run artifact,
   per-run `metrics_summary.yaml`, and terminal logs.
2. Produce a campaign-results Markdown report under
   `doc/reports/campaign_results/`.
3. Export and validate the real styled PDF companion for that report.
4. Update `doc/running/active_training_campaign.yaml` from the stale prepared
   state into a completed/closed state while preserving:
   - the first failed reload attempt;
   - the interrupted slow-worker attempt;
   - the accepted completed attempt.
5. Synchronize `doc/reports/analysis/Training Results Master Summary.md` so it
   reflects the completed Stage 1 smoke result instead of the earlier failed
   partial attempt.
6. Check `doc/reports/analysis/TE Program Status And Closeout Ledger.md` and
   update it only if Stage 1 materially changes the program state.
7. Keep official `TE Curve Verification Pipeline` work separate. The closeout
   may recommend a later operator-approved verification refresh, but must not
   launch the heavy offline matrix.

## Involved Components

- `output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21/`
  - final campaign execution report, logs, leaderboard, and best-run files.
- `output/training_runs/*/2026-06-22-*`
  - per-run metrics, checkpoints, and training reports for the eight completed
    Stage 1 smoke runs.
- `output/registries/families/`
  - family registries updated by the completed runs.
- `output/registries/program/current_best_solution.yaml`
  - program-level scalar best registry after the Stage 1 smoke campaign.
- `doc/running/active_training_campaign.yaml`
  - protected campaign state to close out.
- `doc/reports/campaign_results/`
  - destination for the Stage 1 closeout report and PDF.
- `doc/reports/analysis/Training Results Master Summary.md`
  - canonical program summary that must stop reflecting the failed partial
    attempt as the current campaign result.
- `doc/reports/analysis/TE Program Status And Closeout Ledger.md`
  - program ledger to check for required status synchronization.
- `doc/README.md`
  - report and technical-document index.

## Implementation Steps

1. Parse the completed campaign artifacts and per-run metrics into a compact
   result table.
2. Draft the Stage 1 campaign-results report with:
   - execution summary;
   - failed/interrupted attempt history;
   - accepted run leaderboard;
   - dataset schema confirmation;
   - worker-auto and checkpoint-reload repair notes;
   - next-step recommendation.
3. Export the report to PDF using the repository styled-report pipeline and
   validate the real PDF.
4. Update active campaign state to completed/closed while retaining the
   `last_completed_campaign` block.
5. Regenerate or repair the Training Results Master Summary so the completed
   Stage 1 result is represented cleanly.
6. Check and update the TE Program Status And Closeout Ledger if needed.
7. Run Markdown QA, PDF validation, Python/YAML sanity checks where relevant,
   and `git diff --check`.
8. Stop before committing and request explicit commit approval.
