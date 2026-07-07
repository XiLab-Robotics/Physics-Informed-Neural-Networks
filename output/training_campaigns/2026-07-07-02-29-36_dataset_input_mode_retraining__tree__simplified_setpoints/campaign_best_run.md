# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__tree__simplified_setpoints`
- Run Name: `te_tree_global__simplified_setpoints`
- Run Instance Id: `2026-07-07-02-29-36__te_tree_global__simplified_setpoints`
- Model Family: `tree_global`
- Model Type: `hist_gradient_boosting`
- Test MAE: `0.0028851175665997324`
- Test RMSE: `0.0036068646647811403`
- Validation MAE: `0.0027194633401988267`
- Output Directory: `output\training_runs\tree\2026-07-07-02-29-36__te_tree_global__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\tree\2026-07-07-02-29-36__te_tree_global__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\tree\2026-07-07-02-29-36__te_tree_global__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\tree\2026-07-07-02-29-36__te_tree_global__simplified_setpoints\tree_model.pkl`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
