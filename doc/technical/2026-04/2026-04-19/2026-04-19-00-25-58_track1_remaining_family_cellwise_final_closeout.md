# Track 1 Remaining Family Cellwise Final Closeout

## Overview

This technical document covers the final closeout of the completed
remaining-family `Track 1` exact-paper `cell-wise` batch launched through the
aggregate remote wrapper:

- `track1_remaining_family_cellwise_reference_campaigns_2026_04_18_22_28_04`

The wave generalized the accepted `SVM` closure pattern to the remaining paper
families:

- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

The executed batch contains the full planned `171` target-specific runs:

- `9` family campaign packages;
- `10` amplitude targets per family;
- `9` phase targets per family.

The run artifacts are present, but the campaign closeout is not complete yet.
The repository still needs the final reporting and bookkeeping layer that turns
raw run artifacts into a canonical program state.

## Technical Approach

The closeout should treat the `171`-run wave as one aggregate campaign with
`9` family-local subcampaigns, following the same discipline already used for
the earlier `Track 1` exact-paper closeouts.

The final pass must cover four surfaces together:

1. campaign bookkeeping:
   - one `campaign_leaderboard.yaml` per family campaign;
   - one `campaign_best_run.yaml` per family campaign;
   - one `campaign_best_run.md` per family campaign;
   - the same winner artifacts for the aggregate batch root;
2. campaign-state closure:
   - refresh `doc/running/active_training_campaign.yaml` from `finished` with
     raw completion timestamps into a fully closed campaign record that points
     to the final results report;
3. canonical analysis refresh:
   - refresh
     `doc/reports/analysis/RCIM Paper Reference Benchmark.md`;
   - refresh
     `doc/reports/analysis/Training Results Master Summary.md`;
   - refresh the family-by-family colored `Tables 2-5` whenever accepted cell
     values improved;
4. final deliverables:
   - write the campaign-results report in
     `doc/reports/campaign_results/track1/exact_paper/`;
   - export the PDF companion;
   - validate the real PDF output.

The closeout should also explicitly acknowledge the current artifact gap:

- the `171` run folders do expose `validation_summary.yaml`;
- the family campaign roots do not yet expose their winner-bookkeeping files;
- the closeout therefore needs to reconstruct the canonical ranking surfaces
  from the stored summaries rather than relying on already materialized
  campaign-level winners.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/track1/exact_paper/track1_remaining_family_cellwise_reference_campaigns_2026_04_18_22_28_04/`
- `output/training_campaigns/track1/exact_paper/track1_mlp_cellwise_reference_campaign_2026_04_18_22_28_04/`
- `output/training_campaigns/track1/exact_paper/track1_rf_cellwise_reference_campaign_2026_04_18_22_28_04/`
- `output/training_campaigns/track1/exact_paper/track1_dt_cellwise_reference_campaign_2026_04_18_22_28_04/`
- `output/training_campaigns/track1/exact_paper/track1_et_cellwise_reference_campaign_2026_04_18_22_28_04/`
- `output/training_campaigns/track1/exact_paper/track1_ert_cellwise_reference_campaign_2026_04_18_22_28_04/`
- `output/training_campaigns/track1/exact_paper/track1_gbm_cellwise_reference_campaign_2026_04_18_22_28_04/`
- `output/training_campaigns/track1/exact_paper/track1_hgbm_cellwise_reference_campaign_2026_04_18_22_28_04/`
- `output/training_campaigns/track1/exact_paper/track1_xgbm_cellwise_reference_campaign_2026_04_18_22_28_04/`
- `output/training_campaigns/track1/exact_paper/track1_lgbm_cellwise_reference_campaign_2026_04_18_22_28_04/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
- `doc/reports/campaign_results/track1/exact_paper/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`

## Implementation Steps

1. Verify the `171` run artifacts and reconstruct the family-local and
   aggregate ranking surfaces needed for closeout.
2. Materialize the missing `campaign_leaderboard.yaml`,
   `campaign_best_run.yaml`, and `campaign_best_run.md` files for the `9`
   family campaign roots and for the aggregate batch root.
3. Write the final campaign-results report in Markdown under
   `doc/reports/campaign_results/track1/exact_paper/`.
4. Export and validate the PDF companion.
5. Refresh the canonical benchmark and master-summary surfaces, including the
   colored `Tables 2-5` when accepted values changed.
6. Update `doc/running/active_training_campaign.yaml` so the campaign points to
   the final report and no longer remains only a raw finished execution record.
7. Run Markdown warning checks on the touched Markdown scope before closing the
   task.
