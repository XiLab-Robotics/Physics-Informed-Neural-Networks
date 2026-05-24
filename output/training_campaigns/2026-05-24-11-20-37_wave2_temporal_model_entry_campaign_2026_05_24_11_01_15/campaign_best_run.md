# Campaign Best Run

## Overview

- Campaign Name: `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15`
- Run Name: `te_gru_sequence_remote_Fw`
- Run Instance Id: `2026-05-24-11-54-04__te_gru_sequence_remote_fw`
- Model Family: `gru_sequence_fw`
- Model Type: `gru_sequence`
- Test MAE: `0.0033327306155115366`
- Test RMSE: `0.003880843287333846`
- Validation MAE: `0.003408669261261821`
- Output Directory: `output\training_runs\gru_sequence_fw\2026-05-24-11-54-04__te_gru_sequence_remote_fw`
- Metrics Snapshot: `output\training_runs\gru_sequence_fw\2026-05-24-11-54-04__te_gru_sequence_remote_fw/metrics_summary.yaml`
- Report Path: `output\training_runs\gru_sequence_fw\2026-05-24-11-54-04__te_gru_sequence_remote_fw/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\gru_sequence_fw\2026-05-24-11-54-04__te_gru_sequence_remote_fw\checkpoints\gru_sequence-epoch=045-val_mae=0.00340867.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
