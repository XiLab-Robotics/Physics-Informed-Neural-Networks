# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_setpoints`
- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_setpoints`
- Run Instance Id: `2026-07-09-20-17-04__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Test MAE: `0.0023246619384735823`
- Test RMSE: `0.0036687084939330816`
- Validation MAE: `0.0020448039285838604`
- Output Directory: `output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-07-09-20-17-04__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_setpoints`
- Metrics Snapshot: `output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-07-09-20-17-04__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-07-09-20-17-04__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-07-09-20-17-04__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_setpoints\checkpoints\residual_harmonic_lstm_sequence-epoch=088-val_mae=0.00204480.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
