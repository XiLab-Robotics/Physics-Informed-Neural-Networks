# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints`
- Run Name: `te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints`
- Run Instance Id: `2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense240_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Test MAE: `0.003354056039825082`
- Test RMSE: `0.004116442985832691`
- Validation MAE: `0.003560707438737154`
- Output Directory: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints\checkpoints\residual_harmonic_lstm_sequence-epoch=061-val_mae=0.00356071.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
