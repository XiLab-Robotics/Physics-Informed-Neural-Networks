# Campaign Best Run

## Overview

- Campaign Name: `wave1_directional_retraining_campaign_2026_05_06_16_07_16`
- Run Name: `te_hist_gbr_tabular_Fw`
- Run Instance Id: `2026-05-06-17-00-56__te_hist_gbr_tabular_fw`
- Model Family: `tree_fw`
- Base Model Family: `tree`
- Training Variant: `Fw`
- Model Type: `hist_gradient_boosting`
- Test MAE: `0.0028447329827252245`
- Test RMSE: `0.0034762901949771867`
- Validation MAE: `0.0026658739712788334`
- Output Directory: `output/training_runs/tree_fw/2026-05-06-17-00-56__te_hist_gbr_tabular_fw`
- Metrics Snapshot: `output/training_runs/tree_fw/2026-05-06-17-00-56__te_hist_gbr_tabular_fw/metrics_summary.yaml`
- Report Path: `output/training_runs/tree_fw/2026-05-06-17-00-56__te_hist_gbr_tabular_fw/training_test_report.md`
- Best Checkpoint Path: `output/training_runs/tree_fw/2026-05-06-17-00-56__te_hist_gbr_tabular_fw/tree_model.pkl`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
