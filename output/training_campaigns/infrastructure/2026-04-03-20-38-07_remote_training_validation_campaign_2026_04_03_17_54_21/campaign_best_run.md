# Campaign Best Run

## Overview

- Campaign Name: `remote_training_validation_campaign_2026_04_03_17_54_21`
- Run Name: `te_hist_gbr_remote_deep`
- Run Instance Id: `2026-04-03-21-48-11__te_hist_gbr_remote_deep`
- Model Family: `tree`
- Model Type: `hist_gradient_boosting`
- Test MAE: `0.0029198281928917787`
- Test RMSE: `0.003644374228539183`
- Validation MAE: `0.002748584105610242`
- Output Directory: `output/training_runs/tree/2026-04-03-21-48-11__te_hist_gbr_remote_deep`
- Metrics Snapshot: `output/training_runs/tree/2026-04-03-21-48-11__te_hist_gbr_remote_deep/metrics_summary.yaml`
- Report Path: `output/training_runs/tree/2026-04-03-21-48-11__te_hist_gbr_remote_deep/training_test_report.md`
- Best Checkpoint Path: `output/training_runs/tree/2026-04-03-21-48-11__te_hist_gbr_remote_deep/tree_model.pkl`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

