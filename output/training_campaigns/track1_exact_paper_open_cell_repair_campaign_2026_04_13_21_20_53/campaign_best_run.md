# Campaign Best Run

## Overview

- Campaign Name: `track1_exact_paper_open_cell_repair_campaign_2026_04_13_21_20_53`
- Run Name: `exact_open_cell_paper_family_reference`
- Run Instance Id:
  `2026-04-13-22-08-40__exact_open_cell_paper_family_reference_campaign_run`
- Output Artifact Kind: `validation_check`
- Winning Family: `RF`
- Winning Display Name: `Random Forest`
- Winning Estimator: `RandomForestRegressor`
- Enabled Family Count: `6`
- Winner Mean Component MAPE: `18.36882351011561`
- Winner Mean Component MAE: `0.05628443554453616`
- Winner Mean Component RMSE: `0.1448385161017404`
- Harmonic Closed Count: `0`
- Harmonic Partial Count: `8`
- Harmonic Open Count: `2`
- Met Paper Cell Count: `14`
- Matched Table 6 Family Target Count: `8`
- Regression Count: `0`
- Export Failure Mode: `strict`
- Exported ONNX Files: `120`
- Failed Exports: `0`
- Surrogate Exports: `0`
- Output Directory:
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-13-22-08-40__exact_open_cell_paper_family_reference_campaign_run`
- Validation Summary Path:
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-13-22-08-40__exact_open_cell_paper_family_reference_campaign_run/validation_summary.yaml`
- Model Bundle Path:
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-13-22-08-40__exact_open_cell_paper_family_reference_campaign_run/paper_family_model_bank.pkl`

## Selection Policy

- Primary Metric: `harmonic_closed_count_desc`
- First Tie Breaker: `harmonic_open_count_asc`
- Second Tie Breaker: `met_paper_cell_count_desc`
- Third Tie Breaker: `matched_table6_family_target_count_desc`
- Fourth Tie Breaker: `regression_count_asc`
- Fifth Tie Breaker: `enabled_family_count_desc`
- Sixth Tie Breaker: `run_name`

## Interpretation

This best run is a campaign bookkeeping artifact only.

For `Track 1`, the primary campaign interpretation remains the exact-paper
cell-closure outcome across Tables `3-6`, not the existence of a single winner
run.
