# Residual Harmonic Lstm Sequence Dense240 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values`
- Model Family: `residual_harmonic_lstm_sequence_dense240_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-10-02-54-22__te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=126-val_mae=0.00198495.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005258`
- val_mae: `0.001985`
- val_rmse: `0.002771`
- val_pointwise_loss: `0.005258`
- val_centered_curve_shape_loss: `0.004895`
- val_curve_offset_loss: `0.000363`
- val_curve_amplitude_loss: `0.034981`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039602`
- val_structured_rmse: `0.044121`

## Test Metrics

- test_loss: `0.006124`
- test_mae: `0.002116`
- test_rmse: `0.003149`
- test_pointwise_loss: `0.006124`
- test_centered_curve_shape_loss: `0.005798`
- test_curve_offset_loss: `0.000326`
- test_curve_amplitude_loss: `0.039730`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037323`
- test_structured_rmse: `0.042234`

## Interpretation

The held-out val error stayed finite with MAE=0.001985 deg and RMSE=0.002771 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002116 deg and RMSE=0.003149 deg, which indicates a numerically stable baseline run.
