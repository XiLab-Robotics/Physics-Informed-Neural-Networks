# Track 1 Remaining Family Final Closeout After XGBM LGBM Reruns

## Overview

This technical document covers the final closeout of the interrupted
remaining-family `Track 1` exact-paper batch after the pending `XGBM` and
`LGBM` reruns completed successfully.

The repository already contains the partial closeout for the first seven
families. The missing final step is now to promote the recovered `XGBM` and
`LGBM` runs into the canonical campaign bookkeeping and refresh the benchmark
surfaces so the batch is no longer represented as interrupted.

## Technical Approach

The closeout should preserve the already accepted partial-closeout results and
extend them with the two completed families, rather than rewriting the full
campaign package from scratch.

The final pass should:

1. verify the four new validation artifacts:
   - `track1_xgbm_amplitude_full_matrix`
   - `track1_xgbm_phase_full_matrix`
   - `track1_lgbm_amplitude_full_matrix`
   - `track1_lgbm_phase_full_matrix`
2. serialize the missing winner-bookkeeping artifacts for:
   - the `XGBM` family campaign;
   - the `LGBM` family campaign;
   - the aggregate remaining-family campaign root;
3. promote the aggregate campaign state from `interrupted` to `finished`;
4. write the final campaign-results report and validate its PDF export;
5. refresh the canonical benchmark and master-summary surfaces with the final
   batch outcome.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/track1_xgbm_full_matrix_campaign_2026_04_18_00_48_05/`
- `output/training_campaigns/track1_lgbm_full_matrix_campaign_2026_04_18_00_48_05/`
- `output/training_campaigns/track1_remaining_family_full_matrix_campaigns_2026_04_18_00_48_05/`
- `doc/reports/campaign_results/track1/exact_paper/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`

## Implementation Steps

1. Materialize the missing `campaign_leaderboard.yaml`,
   `campaign_best_run.yaml`, and `campaign_best_run.md` artifacts.
2. Update the aggregate campaign state to `finished`.
3. Write the final remaining-family closeout report in Markdown.
4. Export and validate the PDF companion.
5. Refresh the canonical benchmark and master summary to remove the pending
   `XGBM/LGBM` status.
