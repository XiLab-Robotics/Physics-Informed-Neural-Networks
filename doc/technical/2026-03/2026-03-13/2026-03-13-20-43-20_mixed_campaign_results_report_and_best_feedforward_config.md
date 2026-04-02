# Mixed Campaign Results Report And Best Feedforward Config

## Overview

The user requested the final post-training report for the completed mixed feedforward campaign:

- `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`

The user also requested a new feedforward configuration representing the best current training setup, to be stored as a dedicated `best_training` YAML preset.

The campaign has already been completed and the persistent campaign state confirms:

- `9` completed runs;
- `0` failed runs;
- queue folders cleared of pending/running items;
- a campaign execution manifest and report under:
  - `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/`

## Technical Approach

The final report should synthesize:

- the previously established historical references:
  - `trial`
  - `baseline`
  - `high_density`
  - `high_epoch`
  - `high_compute`
- the `9` newly completed mixed-campaign runs;
- the main conclusions about density, batch regime, larger capacity, and runtime cost.

The report should be written under:

- `doc/reports/campaign_results/`

and it should also be exported as a styled PDF aligned with the project report golden standard.

and should include:

- a campaign overview;
- executed-configuration summary;
- comparative metric tables;
- written interpretation of the three campaign phases;
- identification of the best-performing configuration;
- recommended next steps;
- a validated PDF export of the final report.

### Best-Training Config Selection Logic

The new `best_training` YAML should not be chosen only by one metric in isolation.

The selection should weigh:

- held-out `test_mae`;
- held-out `test_rmse`;
- validation stability;
- runtime cost;
- architectural simplicity and reproducibility.

Observed preliminary result:

- among the `9` new mixed runs, `te_feedforward_stride5_long_large_batch` achieved the best `test_mae`;
- the older `te_feedforward_high_epoch` still appears marginally best on historical `test_rmse`;
- several heavier variants increased runtime substantially without a decisive win on both held-out metrics.

This means the best final preset may reasonably follow one of two defensible philosophies:

1. **lowest test MAE among the new campaign**
   - favor `stride5_long_large_batch`;
2. **most balanced historical default**
   - retain `high_epoch` as the main default if its held-out stability and simplicity remain the stronger argument overall.

The report should make that tradeoff explicit and the final `best_training` YAML should align with the chosen interpretation.

## Involved Components

- `README.md`
  Main project document that must reference this technical document.
- `doc/README.md`
  Internal documentation index that should also reference this technical document.
- `doc/running/active_training_campaign.yaml`
  Persistent campaign state, already marked as completed and pointing to the execution artifact root.
- `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
  Approved planning report for the completed campaign.
- `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/campaign_manifest.yaml`
  Machine-readable index of the `9` completed runs and their artifacts.
- `output/training_campaigns/2026-03-12-18-52-30_mixed_training_campaign_2026_03_12_15_32_28/campaign_execution_report.md`
  Human-readable execution summary for the completed campaign.
- `doc/reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md`
  Previous feedforward comparison report that should be used as historical context.
- `config/training/feedforward/presets/high_epoch.yaml`
  Current strongest historical reference before the mixed campaign.
- `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/05_stride5_long_large_batch.yaml`
  Strong candidate for the new best-training preset because it achieved the best mixed-campaign `test_mae`.
- `config/training/feedforward/presets/`
  Target location for the new `best_training` feedforward YAML.
- `doc/guide/project_usage_guide.md`
  User-facing guide that should be updated because a new recommended best-training preset will be added.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, write the final campaign results report in `doc/reports/campaign_results/` using the completed campaign manifest, execution report, and per-run metric files.
3. Export the final campaign results report to PDF and validate the real exported PDF output before closing the task.
4. Compare the mixed-campaign winner against the previous `high_epoch` reference and make the selection logic explicit in the report.
5. Create a new feedforward preset such as `config/training/feedforward/presets/best_training.yaml` aligned with the selected best current configuration.
6. Update `doc/guide/project_usage_guide.md` so the new recommended preset and its intended usage are documented.
7. Leave the campaign-specific YAML files untouched, because they are historical execution artifacts rather than the new reusable default.
