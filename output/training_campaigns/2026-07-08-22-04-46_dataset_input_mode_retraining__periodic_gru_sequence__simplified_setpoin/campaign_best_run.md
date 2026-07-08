# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints`
- Run Name: `te_periodic_gru_sequence_bw__simplified_setpoints`
- Run Instance Id: `2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints`
- Model Family: `periodic_gru_sequence_bw`
- Model Type: `periodic_gru_sequence`
- Test MAE: `0.0032499409280717373`
- Test RMSE: `0.003968670964241028`
- Validation MAE: `0.003499874845147133`
- Output Directory: `output\training_runs\periodic_gru_sequence\2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\periodic_gru_sequence\2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\periodic_gru_sequence\2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\periodic_gru_sequence\2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints\checkpoints\periodic_gru_sequence-epoch=081-val_mae=0.00349987.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`

