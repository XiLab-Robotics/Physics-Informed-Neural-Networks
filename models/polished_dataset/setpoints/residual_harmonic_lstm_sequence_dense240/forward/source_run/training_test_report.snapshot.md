# Residual Harmonic Lstm Sequence Dense240 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_fw__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense240_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-10-00-54-03__te_residual_harmonic_lstm_sequence_dense240_fw__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=067-val_mae=0.00199481.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005291`
- val_mae: `0.001995`
- val_rmse: `0.002775`
- val_pointwise_loss: `0.005291`
- val_centered_curve_shape_loss: `0.004907`
- val_curve_offset_loss: `0.000384`
- val_curve_amplitude_loss: `0.036392`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039640`
- val_structured_rmse: `0.044146`

## Test Metrics

- test_loss: `0.008615`
- test_mae: `0.002275`
- test_rmse: `0.003636`
- test_pointwise_loss: `0.008615`
- test_centered_curve_shape_loss: `0.005765`
- test_curve_offset_loss: `0.002850`
- test_curve_amplitude_loss: `0.046895`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037319`
- test_structured_rmse: `0.042223`

## Interpretation

The held-out val error stayed finite with MAE=0.001995 deg and RMSE=0.002775 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002275 deg and RMSE=0.003636 deg, which indicates a numerically stable baseline run.
