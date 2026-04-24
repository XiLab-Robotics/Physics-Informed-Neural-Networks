# 2026-04-24-18-01-00 Track1 Exact Paper Second Pass Taxonomy Reorganization

## Overview

The first forward-versus-backward reorganization pass correctly restored the
generic recovered-asset root and moved the exact-paper `Track 1` forward
artifacts under direction-aware roots, but it stopped at the first taxonomy
level. Several heavy directories still remain internally flat:

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/`
- `output/training_campaigns/track1/exact_paper/forward/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/`
- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/`

This second pass will reorganize those forward roots into inspectable
subfolders grouped by campaign phase, family, and shared-bundle scope. It will
also absorb the still-unmigrated flat output campaign roots listed by the user
and fix the accidental duplicated `forward/forward` fragment currently present
in `doc/running/active_training_campaign.yaml`.

## Technical Approach

The reorganization will keep the top-level direction split already introduced,
but will add one more stable taxonomy layer below each `forward/` root.

Proposed exact-paper forward campaign-config taxonomy:

- `campaigns/track1/exact_paper/forward/baseline_reproduction/`
- `campaigns/track1/exact_paper/forward/open_cell_repair/`
- `campaigns/track1/exact_paper/forward/full_matrix/`
- `campaigns/track1/exact_paper/forward/cellwise_reference/`
- `campaigns/track1/exact_paper/forward/residual_cellwise_closure/`
- `campaigns/track1/exact_paper/forward/open_cell_full_matrix_closure/`
- `campaigns/track1/exact_paper/forward/family_repair/`
- `campaigns/track1/exact_paper/forward/remaining_yellow_cells/`

Inside each phase folder, family-specific campaigns will stay as separate
directories, while shared multi-family bundles keep a `shared/` subfolder when
needed.

Proposed exact-paper forward training-campaign taxonomy:

- `output/training_campaigns/track1/exact_paper/forward/<phase>/<family or shared>/<campaign_dir>/`

This explicitly covers the still-flat roots:

- `track1_dt_open_cell_full_matrix_closure_campaign_2026_04_20_23_50_13`
- `track1_ert_open_cell_full_matrix_closure_campaign_2026_04_20_23_50_13`
- `track1_et_open_cell_full_matrix_closure_campaign_2026_04_20_23_50_13`
- `track1_gbm_open_cell_full_matrix_closure_campaign_2026_04_20_23_50_13`
- `track1_hgbm_open_cell_full_matrix_closure_campaign_2026_04_20_23_50_13`
- `track1_lgbm_open_cell_full_matrix_closure_campaign_2026_04_20_23_50_13`
- `track1_rf_open_cell_full_matrix_closure_campaign_2026_04_20_23_50_13`
- `track1_xgbm_open_cell_full_matrix_closure_campaign_2026_04_20_23_50_13`

Proposed exact-paper forward validation taxonomy:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/<phase>/<family or shared>/<run_instance_id>/`

Proposed harmonic-wise forward validation taxonomy:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/<phase>/<family or shared>/<run_instance_id>/`

The implementation will propagate the new taxonomy into:

- exact-paper launcher scripts;
- exact-paper closeout/report scripts;
- active campaign state;
- validation summaries and campaign manifests that carry persisted paths;
- canonical documentation that describes the new storage contract.

No subagent use is planned for this task.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/`
- `output/training_campaigns/track1/exact_paper/forward/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/`
- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/`
- `doc/running/active_training_campaign.yaml`
- `scripts/campaigns/track1/exact_paper/`
- `scripts/reports/`
- `doc/reports/analysis/validation_checks/track1/exact_paper/forward/`
- `doc/reports/campaign_results/track1/exact_paper/forward/`

## Implementation Steps

1. Inventory the current flat forward roots and map every campaign or run to a
   canonical `<phase>/<family or shared>/` destination.
2. Reorganize exact-paper campaign configs under
   `campaigns/track1/exact_paper/forward/` using the phase-first taxonomy.
3. Reorganize exact-paper training-campaign outputs under
   `output/training_campaigns/track1/exact_paper/forward/`, including the
   still-flat `open_cell_full_matrix_closure` family folders.
4. Reorganize exact-paper and harmonic-wise forward validation outputs under
   their new `<phase>/<family or shared>/` roots.
5. Propagate the new paths into scripts, active campaign state, persisted YAML
   artifacts, and canonical documentation; remove any duplicated
   `forward/forward` fragments.
6. Re-run repository searches for legacy flat paths or partially migrated
   roots, verify the touched Python and Markdown scope, and stop before any
   commit.
