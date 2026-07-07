# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__feedforward__simplified_setpoints`
- Run Name: `te_feedforward_global__simplified_setpoints`
- Run Instance Id: `2026-07-07-16-02-57__te_feedforward_global__simplified_setpoints`
- Model Family: `feedforward_global`
- Model Type: `feedforward`
- Test MAE: `0.0032426551915705204`
- Test RMSE: `0.0038749626837670803`
- Validation MAE: `0.0029678812716156244`
- Output Directory: `output\training_runs\feedforward\2026-07-07-16-02-57__te_feedforward_global__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\feedforward\2026-07-07-16-02-57__te_feedforward_global__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\feedforward\2026-07-07-16-02-57__te_feedforward_global__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\feedforward\2026-07-07-16-02-57__te_feedforward_global__simplified_setpoints\checkpoints\feedforward-epoch=095-val_mae=0.00296788.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

