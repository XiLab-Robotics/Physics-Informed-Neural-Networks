# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__gru_sequence__simplified_setpoints`
- Run Name: `te_gru_sequence_bw__simplified_setpoints`
- Run Instance Id: `2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints`
- Model Family: `gru_sequence_bw`
- Model Type: `gru_sequence`
- Test MAE: `0.003509706584736705`
- Test RMSE: `0.004340673331171274`
- Validation MAE: `0.003661188529804349`
- Output Directory: `output\training_runs\gru_sequence\2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\gru_sequence\2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\gru_sequence\2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\gru_sequence\2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints\checkpoints\gru_sequence-epoch=132-val_mae=0.00366119.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

