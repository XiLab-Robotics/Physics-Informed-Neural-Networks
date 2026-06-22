# Campaign Best Run

## Overview

- Campaign Name: `polished_dataset_stage1_smoke_2026_06_21`
- Run Name: `te_periodic_gru_sequence_remote_global`
- Run Instance Id: `2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global`
- Model Family: `periodic_gru_sequence`
- Model Type: `periodic_gru_sequence`
- Test MAE: `0.0012794497888535261`
- Test RMSE: `0.0016375193372368813`
- Validation MAE: `0.0012736358912661672`
- Output Directory: `output\training_runs\periodic_gru_sequence\2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global`
- Metrics Snapshot: `output\training_runs\periodic_gru_sequence\2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global/metrics_summary.yaml`
- Report Path: `output\training_runs\periodic_gru_sequence\2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\periodic_gru_sequence\2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global\checkpoints\periodic_gru_sequence-epoch=190-val_mae=0.00127364.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
