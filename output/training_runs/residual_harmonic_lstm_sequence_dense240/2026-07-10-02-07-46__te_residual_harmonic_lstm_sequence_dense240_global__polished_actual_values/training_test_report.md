# Residual Harmonic Lstm Sequence Dense240 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_global__polished_actual_values`
- Model Family: `residual_harmonic_lstm_sequence_dense240_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-10-02-07-46__te_residual_harmonic_lstm_sequence_dense240_global__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=055-val_mae=0.00202673.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005340`
- val_mae: `0.002027`
- val_rmse: `0.002814`
- val_pointwise_loss: `0.005340`
- val_centered_curve_shape_loss: `0.004950`
- val_curve_offset_loss: `0.000391`
- val_curve_amplitude_loss: `0.037012`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039662`
- val_structured_rmse: `0.044416`

## Test Metrics

- test_loss: `0.008583`
- test_mae: `0.002297`
- test_rmse: `0.003625`
- test_pointwise_loss: `0.008583`
- test_centered_curve_shape_loss: `0.005733`
- test_curve_offset_loss: `0.002850`
- test_curve_amplitude_loss: `0.046679`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037438`
- test_structured_rmse: `0.042550`

## Interpretation

The held-out val error stayed finite with MAE=0.002027 deg and RMSE=0.002814 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002297 deg and RMSE=0.003625 deg, which indicates a numerically stable baseline run.
