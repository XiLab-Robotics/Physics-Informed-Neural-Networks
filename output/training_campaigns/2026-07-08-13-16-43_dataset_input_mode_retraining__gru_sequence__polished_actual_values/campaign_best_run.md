# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__gru_sequence__polished_actual_values`
- Run Name: `te_gru_sequence_bw__polished_actual_values`
- Run Instance Id: `2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values`
- Model Family: `gru_sequence_bw`
- Model Type: `gru_sequence`
- Test MAE: `0.0022579296492040157`
- Test RMSE: `0.003322328208014369`
- Validation MAE: `0.0021438999101519585`
- Output Directory: `output\training_runs\gru_sequence\2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\gru_sequence\2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\gru_sequence\2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\gru_sequence\2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values\checkpoints\gru_sequence-epoch=172-val_mae=0.00214390.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

