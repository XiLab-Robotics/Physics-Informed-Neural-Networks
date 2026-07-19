# Residual Harmonic Gru Sequence Dense240 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_fw__polished_actual_values`
- Model Family: `residual_harmonic_gru_sequence_dense240_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-11-57-58__te_residual_harmonic_gru_sequence_dense240_fw__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=120-val_mae=0.00196886.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005250`
- val_mae: `0.001969`
- val_rmse: `0.002762`
- val_pointwise_loss: `0.005250`
- val_centered_curve_shape_loss: `0.004926`
- val_curve_offset_loss: `0.000324`
- val_curve_amplitude_loss: `0.037373`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039685`
- val_structured_rmse: `0.044200`

## Test Metrics

- test_loss: `0.006066`
- test_mae: `0.002101`
- test_rmse: `0.003138`
- test_pointwise_loss: `0.006066`
- test_centered_curve_shape_loss: `0.005676`
- test_curve_offset_loss: `0.000390`
- test_curve_amplitude_loss: `0.042115`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037352`
- test_structured_rmse: `0.042276`

## Interpretation

The held-out val error stayed finite with MAE=0.001969 deg and RMSE=0.002762 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002101 deg and RMSE=0.003138 deg, which indicates a numerically stable baseline run.
