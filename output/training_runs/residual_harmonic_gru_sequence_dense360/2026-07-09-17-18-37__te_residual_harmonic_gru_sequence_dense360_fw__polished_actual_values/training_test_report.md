# Residual Harmonic Gru Sequence Dense360 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values`
- Model Family: `residual_harmonic_gru_sequence_dense360_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-18-37__te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=156-val_mae=0.00195537.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005257`
- val_mae: `0.001955`
- val_rmse: `0.002747`
- val_pointwise_loss: `0.005257`
- val_centered_curve_shape_loss: `0.004919`
- val_curve_offset_loss: `0.000339`
- val_curve_amplitude_loss: `0.036715`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039802`
- val_structured_rmse: `0.044281`

## Test Metrics

- test_loss: `0.006025`
- test_mae: `0.002074`
- test_rmse: `0.003114`
- test_pointwise_loss: `0.006025`
- test_centered_curve_shape_loss: `0.005660`
- test_curve_offset_loss: `0.000365`
- test_curve_amplitude_loss: `0.041553`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037381`
- test_structured_rmse: `0.042298`

## Interpretation

The held-out val error stayed finite with MAE=0.001955 deg and RMSE=0.002747 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002074 deg and RMSE=0.003114 deg, which indicates a numerically stable baseline run.
