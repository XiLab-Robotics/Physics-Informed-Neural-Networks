# Campaign Best Run

## Overview

- Campaign Name: `exact_paper_model_bank_campaign_2026_04_10_17_04_41`
- Run Name: `exact_full_bank_strict_reference`
- Run Instance Id: `2026-04-10-19-12-14__exact_full_bank_strict_reference_campaign_run`
- Output Artifact Kind: `validation_check`
- Winning Family: `RF`
- Winning Display Name: `Random Forest`
- Winning Estimator: `RandomForestRegressor`
- Enabled Family Count: `10`
- Winner Mean Component MAPE: `18.36882351011561`
- Winner Mean Component MAE: `0.05628443554453616`
- Winner Mean Component RMSE: `0.1448385161017404`
- Export Failure Mode: `strict`
- Exported ONNX Files: `200`
- Failed Exports: `0`
- Surrogate Exports: `5`
- Output Directory: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/baseline_reproduction/shared/2026-04-10-19-12-14__exact_full_bank_strict_reference_campaign_run`
- Validation Summary Path: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/baseline_reproduction/shared/2026-04-10-19-12-14__exact_full_bank_strict_reference_campaign_run/validation_summary.yaml`
- Model Bundle Path: `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/baseline_reproduction/shared/2026-04-10-19-12-14__exact_full_bank_strict_reference_campaign_run/paper_family_model_bank.pkl`

## Selection Policy

- Primary Metric: `winning_mean_component_mape_percent`
- First Tie Breaker: `winning_mean_component_mae`
- Second Tie Breaker: `prefer_export_failure_mode_strict`
- Third Tie Breaker: `enabled_family_count_desc`
- Fourth Tie Breaker: `winning_mean_component_rmse`
- Fifth Tie Breaker: `run_name`
