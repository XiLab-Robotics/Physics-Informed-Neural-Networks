# Residual Harmonic Lstm Sequence Dense360 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense360_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-53-57__te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=101-val_mae=0.00197679.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005265`
- val_mae: `0.001977`
- val_rmse: `0.002763`
- val_pointwise_loss: `0.005265`
- val_centered_curve_shape_loss: `0.004875`
- val_curve_offset_loss: `0.000390`
- val_curve_amplitude_loss: `0.034780`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039606`
- val_structured_rmse: `0.044089`

## Test Metrics

- test_loss: `0.008712`
- test_mae: `0.002282`
- test_rmse: `0.003645`
- test_pointwise_loss: `0.008712`
- test_centered_curve_shape_loss: `0.005718`
- test_curve_offset_loss: `0.002995`
- test_curve_amplitude_loss: `0.044974`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037303`
- test_structured_rmse: `0.042179`

## Interpretation

The held-out val error stayed finite with MAE=0.001977 deg and RMSE=0.002763 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002282 deg and RMSE=0.003645 deg, which indicates a numerically stable baseline run.
