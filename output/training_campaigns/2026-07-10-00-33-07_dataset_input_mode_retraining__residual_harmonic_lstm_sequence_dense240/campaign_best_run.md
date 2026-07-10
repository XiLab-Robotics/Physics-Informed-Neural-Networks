# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__polished_setpoints`
- Run Name: `te_residual_harmonic_lstm_sequence_dense240_fw__polished_setpoints`
- Run Instance Id: `2026-07-10-00-54-03__te_residual_harmonic_lstm_sequence_dense240_fw__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense240_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Test MAE: `0.0022754415404051542`
- Test RMSE: `0.0036361529491841793`
- Validation MAE: `0.001994808902963996`
- Output Directory: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-10-00-54-03__te_residual_harmonic_lstm_sequence_dense240_fw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-10-00-54-03__te_residual_harmonic_lstm_sequence_dense240_fw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-10-00-54-03__te_residual_harmonic_lstm_sequence_dense240_fw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-07-10-00-54-03__te_residual_harmonic_lstm_sequence_dense240_fw__polished_setpoints\checkpoints\residual_harmonic_lstm_sequence-epoch=067-val_mae=0.00199481.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
