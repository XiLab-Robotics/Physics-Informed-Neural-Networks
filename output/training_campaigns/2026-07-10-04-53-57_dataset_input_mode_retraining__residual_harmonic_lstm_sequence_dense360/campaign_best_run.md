# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints`
- Run Name: `te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints`
- Run Instance Id: `2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense360_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Test MAE: `0.0022816963028162718`
- Test RMSE: `0.003645189106464386`
- Validation MAE: `0.0019767913036048412`
- Output Directory: `output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints`
- Metrics Snapshot: `output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints\checkpoints\residual_harmonic_lstm_sequence-epoch=101-val_mae=0.00197679.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
