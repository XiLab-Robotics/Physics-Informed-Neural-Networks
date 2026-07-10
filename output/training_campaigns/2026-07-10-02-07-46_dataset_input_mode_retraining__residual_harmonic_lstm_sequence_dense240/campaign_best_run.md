# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__polished_actual_values`
- Run Name: `te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values`
- Run Instance Id: `2026-07-10-02-54-22__te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values`
- Model Family: `residual_harmonic_lstm_sequence_dense240_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Test MAE: `0.0021164012141525745`
- Test RMSE: `0.003149408148601651`
- Validation MAE: `0.001984954345971346`
- Output Directory: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-10-02-54-22__te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values`
- Metrics Snapshot: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-10-02-54-22__te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values/metrics_summary.yaml`
- Report Path: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-10-02-54-22__te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-10-02-54-22__te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values\checkpoints\residual_harmonic_lstm_sequence-epoch=126-val_mae=0.00198495.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
