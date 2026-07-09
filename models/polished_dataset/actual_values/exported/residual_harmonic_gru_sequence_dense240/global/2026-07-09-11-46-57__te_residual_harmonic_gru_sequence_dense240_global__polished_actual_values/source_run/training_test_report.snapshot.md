# Residual Harmonic Gru Sequence Dense240 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_global__polished_actual_values`
- Model Family: `residual_harmonic_gru_sequence_dense240_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-11-46-57__te_residual_harmonic_gru_sequence_dense240_global__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=056-val_mae=0.00204583.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005369`
- val_mae: `0.002046`
- val_rmse: `0.002842`
- val_pointwise_loss: `0.005369`
- val_centered_curve_shape_loss: `0.004948`
- val_curve_offset_loss: `0.000420`
- val_curve_amplitude_loss: `0.033895`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039621`
- val_structured_rmse: `0.044358`

## Test Metrics

- test_loss: `0.006384`
- test_mae: `0.002213`
- test_rmse: `0.003268`
- test_pointwise_loss: `0.006384`
- test_centered_curve_shape_loss: `0.005892`
- test_curve_offset_loss: `0.000493`
- test_curve_amplitude_loss: `0.038435`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037429`
- test_structured_rmse: `0.042520`

## Interpretation

The held-out val error stayed finite with MAE=0.002046 deg and RMSE=0.002842 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002213 deg and RMSE=0.003268 deg, which indicates a numerically stable baseline run.
