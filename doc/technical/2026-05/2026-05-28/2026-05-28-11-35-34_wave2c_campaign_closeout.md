# Wave 2.3 Campaign Closeout

## Overview

This technical document plans the closeout for the completed `Wave 2.3`
residual harmonic temporal hybrid campaign. The campaign was executed directly
on the remote workstation without the `-Remote` wrapper, and the local artifact
surface now contains the completed queue records, campaign manifest,
leaderboard, best-run pointers, per-run outputs, and refreshed registries.

The closeout must verify that all `18` planned runs completed successfully,
produce the final campaign-results Markdown and PDF deliverables, synchronize
the persistent campaign state, and keep `TE Curve Verification Pipeline` verification as a separate
operator-approved follow-up.

## Technical Approach

The closeout will use the existing Wave 2.2 closeout pattern as the local
implementation reference while adapting the campaign identity, candidate
matrix, artifact paths, and interpretation to Wave 2.3. The campaign result
will be accepted as an execution closeout only, not as official `TE Curve Verification Pipeline`
model acceptance.

The workflow will:

- load `campaign_manifest.yaml`, `campaign_leaderboard.yaml`, and
  `campaign_best_run.yaml` from the completed campaign output directory;
- assert that all planned queue entries completed with return code `0`;
- generate a final campaign-results report under
  `doc/reports/campaign_results/wave_2/`;
- export and validate the styled PDF companion;
- update `doc/README.md`, `doc/running/active_training_campaign.yaml`, and
  the training summary/report surfaces that must reflect completed campaign
  status;
- leave optional `TE Curve Verification Pipeline` refresh outside the normal closeout.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/wave_2/2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrid_campaign_plan_report.md`
- `output/training_campaigns/2026-05-27-18-55-47_wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27/`
- `output/training_runs/residual_harmonic_*`
- `output/registries/families/residual_harmonic_*`
- `output/registries/program/current_best_solution.yaml`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_results/wave_2/`
- `scripts/reports/pdf/`

## Implementation Steps

1. Verify the completed campaign manifest, run count, queue status, return
   codes, leaderboard, best-run pointer, and registry side effects.
2. Add or adapt a repository-owned closeout helper for Wave 2.3 if the existing
   Wave 2.2 helper cannot be reused directly.
3. Generate the final campaign-results Markdown report and register it in
   `doc/README.md`.
4. Export the final report to PDF and validate the real exported PDF.
5. Update the active campaign state to clear the prepared/running surface and
   preserve a `last_completed_campaign` summary.
6. Run scoped Markdown QA, PDF validation, and status checks before reporting
   the closeout package.
