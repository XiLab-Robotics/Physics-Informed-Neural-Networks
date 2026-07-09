# Residual Harmonic Lstm Sequence Sparse Rcim Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-19-35-45__te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=060-val_mae=0.00204293.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005423`
- val_mae: `0.002043`
- val_rmse: `0.002835`
- val_pointwise_loss: `0.005423`
- val_centered_curve_shape_loss: `0.004913`
- val_curve_offset_loss: `0.000511`
- val_curve_amplitude_loss: `0.041112`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039748`
- val_structured_rmse: `0.044402`

## Test Metrics

- test_loss: `0.008949`
- test_mae: `0.002349`
- test_rmse: `0.003726`
- test_pointwise_loss: `0.008949`
- test_centered_curve_shape_loss: `0.005817`
- test_curve_offset_loss: `0.003132`
- test_curve_amplitude_loss: `0.051411`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037394`
- test_structured_rmse: `0.042432`

## Interpretation

The held-out val error stayed finite with MAE=0.002043 deg and RMSE=0.002835 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002349 deg and RMSE=0.003726 deg, which indicates a numerically stable baseline run.
