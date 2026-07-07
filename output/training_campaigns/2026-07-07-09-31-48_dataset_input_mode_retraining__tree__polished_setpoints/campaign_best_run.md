# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__tree__polished_setpoints`
- Run Name: `te_tree_global__polished_setpoints`
- Run Instance Id: `2026-07-07-09-31-48__te_tree_global__polished_setpoints`
- Model Family: `tree_global`
- Model Type: `hist_gradient_boosting`
- Test MAE: `0.0016992991767779192`
- Test RMSE: `0.0029467764239082105`
- Validation MAE: `0.001497939282891613`
- Output Directory: `output\training_runs\tree\2026-07-07-09-31-48__te_tree_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\tree\2026-07-07-09-31-48__te_tree_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\tree\2026-07-07-09-31-48__te_tree_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\tree\2026-07-07-09-31-48__te_tree_global__polished_setpoints\tree_model.pkl`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
