# Campaign Best Run

## Overview

- Campaign Name: `track1_full_matrix_family_reproduction_campaign_2026_04_14_13_50_51`
- Run Name: `track1_rf_phase_full_matrix`
- Run Instance Id: `2026-04-14-14-13-04__track1_rf_phase_full_matrix_campaign_run`
- Family Scope: `RF`
- Target Scope: `phases_only`
- Target Count: `9`
- Closure Score: `0.555556`
- Met Cells: `3`
- Near Cells: `4`
- Open Cells: `2`
- Matched Table 6 Family Targets: `3`
- Mean Normalized Gap Ratio: `0.140915`
- Max Normalized Gap Ratio: `0.789387`
- Winning Family: `RF`
- Winning Display Name: `Random Forest`
- Winning Estimator: `RandomForestRegressor`
- Winning Mean Component MAPE: `33.123052`
- Winning Mean Component MAE: `0.124699`
- Winning Mean Component RMSE: `0.321338`
- Exported ONNX Files: `9`
- Failed Exports: `0`
- Surrogate Exports: `0`
- Output Directory: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-14-14-13-04__track1_rf_phase_full_matrix_campaign_run`
- Validation Summary Path: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-14-14-13-04__track1_rf_phase_full_matrix_campaign_run/validation_summary.yaml`
- Model Bundle Path: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-14-14-13-04__track1_rf_phase_full_matrix_campaign_run/paper_family_model_bank.pkl`

## Selection Policy

- Primary Metric: `row_closure_score_desc`
- First Tie Breaker: `met_paper_cell_count_desc`
- Second Tie Breaker: `open_paper_cell_count_asc`
- Third Tie Breaker: `mean_normalized_gap_ratio_asc`
- Fourth Tie Breaker: `max_normalized_gap_ratio_asc`
- Fifth Tie Breaker: `matched_table6_family_target_count_desc`
- Sixth Tie Breaker: `run_name`

## Interpretation

This best run is a campaign bookkeeping artifact only.

For `Track 1`, the primary scientific reading is now the family-row matrix
replication across paper Tables `3`, `4`, and `5`, not the existence of
one global winner run.
