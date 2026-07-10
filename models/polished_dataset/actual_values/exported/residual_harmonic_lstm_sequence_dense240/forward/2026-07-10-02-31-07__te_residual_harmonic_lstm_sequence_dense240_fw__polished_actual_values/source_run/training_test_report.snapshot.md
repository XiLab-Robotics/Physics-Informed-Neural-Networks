# Residual Harmonic Lstm Sequence Dense240 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_fw__polished_actual_values`
- Model Family: `residual_harmonic_lstm_sequence_dense240_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-10-02-31-07__te_residual_harmonic_lstm_sequence_dense240_fw__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=055-val_mae=0.00202504.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005359`
- val_mae: `0.002025`
- val_rmse: `0.002823`
- val_pointwise_loss: `0.005359`
- val_centered_curve_shape_loss: `0.004927`
- val_curve_offset_loss: `0.000432`
- val_curve_amplitude_loss: `0.039993`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039732`
- val_structured_rmse: `0.044480`

## Test Metrics

- test_loss: `0.008722`
- test_mae: `0.002298`
- test_rmse: `0.003638`
- test_pointwise_loss: `0.008722`
- test_centered_curve_shape_loss: `0.005740`
- test_curve_offset_loss: `0.002982`
- test_curve_amplitude_loss: `0.050171`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037454`
- test_structured_rmse: `0.042572`

## Interpretation

The held-out val error stayed finite with MAE=0.002025 deg and RMSE=0.002823 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002298 deg and RMSE=0.003638 deg, which indicates a numerically stable baseline run.
