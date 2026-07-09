# Residual Harmonic Lstm Sequence Sparse Rcim Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-21-46-24__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=219-val_mae=0.00195141.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005263`
- val_mae: `0.001951`
- val_rmse: `0.002755`
- val_pointwise_loss: `0.005263`
- val_centered_curve_shape_loss: `0.004937`
- val_curve_offset_loss: `0.000326`
- val_curve_amplitude_loss: `0.041003`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039675`
- val_structured_rmse: `0.044137`

## Test Metrics

- test_loss: `0.006042`
- test_mae: `0.002067`
- test_rmse: `0.003129`
- test_pointwise_loss: `0.006042`
- test_centered_curve_shape_loss: `0.005702`
- test_curve_offset_loss: `0.000340`
- test_curve_amplitude_loss: `0.046205`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037314`
- test_structured_rmse: `0.042174`

## Interpretation

The held-out val error stayed finite with MAE=0.001951 deg and RMSE=0.002755 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002067 deg and RMSE=0.003129 deg, which indicates a numerically stable baseline run.
