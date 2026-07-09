# Residual Harmonic Lstm Sequence Dense240 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense240_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-32-01__te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=061-val_mae=0.00356071.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010653`
- val_mae: `0.003561`
- val_rmse: `0.004400`
- val_pointwise_loss: `0.010653`
- val_centered_curve_shape_loss: `0.006601`
- val_curve_offset_loss: `0.004052`
- val_curve_amplitude_loss: `0.046997`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037834`
- val_structured_rmse: `0.042654`

## Test Metrics

- test_loss: `0.008114`
- test_mae: `0.003354`
- test_rmse: `0.004116`
- test_pointwise_loss: `0.008114`
- test_centered_curve_shape_loss: `0.003423`
- test_curve_offset_loss: `0.004691`
- test_curve_amplitude_loss: `0.021481`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040704`
- test_structured_rmse: `0.045402`

## Interpretation

The held-out val error stayed finite with MAE=0.003561 deg and RMSE=0.004400 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003354 deg and RMSE=0.004116 deg, which indicates a numerically stable baseline run.
