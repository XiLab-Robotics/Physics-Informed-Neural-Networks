# Campaign Best Run

## Overview

- Campaign Name: `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints`
- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints`
- Run Instance Id: `2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Test MAE: `0.003371954895555973`
- Test RMSE: `0.0041620018891990185`
- Validation MAE: `0.0036782415118068457`
- Output Directory: `output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints`
- Metrics Snapshot: `output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints/metrics_summary.yaml`
- Report Path: `output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints/training_test_report.md`
- Best Checkpoint Path: `output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints\checkpoints\residual_harmonic_lstm_sequence-epoch=029-val_mae=0.00367824.ckpt`

## Selection Policy

- Primary Metric: `test_mae`
- First Tie Breaker: `test_rmse`
- Second Tie Breaker: `val_mae`
- Third Tie Breaker: `trainable_parameter_count`
