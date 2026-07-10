# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints`
- Run Name: `te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints`
- Run Instance Id: `2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense360_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Test MAE: `0.00340180448256433`
- Test RMSE: `0.004177093505859375`
- Validation MAE: `0.0035822251811623573`
- Output Directory: `output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints\checkpoints\residual_harmonic_lstm_sequence-epoch=047-val_mae=0.00358223.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
