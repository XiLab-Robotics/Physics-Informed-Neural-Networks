# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__feedforward__polished_actual_values`
- Run Name: `te_feedforward_fw__polished_actual_values`
- Run Instance Id: `2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Test MAE: `0.0017583367880433798`
- Test RMSE: `0.002735764253884554`
- Validation MAE: `0.001615521963685751`
- Output Directory: `output\training_runs\feedforward\2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\feedforward\2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\feedforward\2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\feedforward\2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values\checkpoints\feedforward-epoch=181-val_mae=0.00161552.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

