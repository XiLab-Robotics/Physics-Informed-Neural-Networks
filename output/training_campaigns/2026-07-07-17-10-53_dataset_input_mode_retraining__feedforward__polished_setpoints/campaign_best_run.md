# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__feedforward__polished_setpoints`
- Run Name: `te_feedforward_bw__polished_setpoints`
- Run Instance Id: `2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Test MAE: `0.001852865912951529`
- Test RMSE: `0.002874168334528804`
- Validation MAE: `0.0016406569629907608`
- Output Directory: `output\training_runs\feedforward\2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\feedforward\2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\feedforward\2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\feedforward\2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints\checkpoints\feedforward-epoch=057-val_mae=0.00164066.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

