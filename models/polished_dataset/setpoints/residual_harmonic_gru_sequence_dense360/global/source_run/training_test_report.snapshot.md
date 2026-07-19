# Residual Harmonic Gru Sequence Dense360 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense360_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-15-18-00__te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=111-val_mae=0.00197378.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005265`
- val_mae: `0.001974`
- val_rmse: `0.002761`
- val_pointwise_loss: `0.005265`
- val_centered_curve_shape_loss: `0.004851`
- val_curve_offset_loss: `0.000414`
- val_curve_amplitude_loss: `0.036202`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039699`
- val_structured_rmse: `0.044173`

## Test Metrics

- test_loss: `0.008723`
- test_mae: `0.002284`
- test_rmse: `0.003660`
- test_pointwise_loss: `0.008723`
- test_centered_curve_shape_loss: `0.005718`
- test_curve_offset_loss: `0.003005`
- test_curve_amplitude_loss: `0.046851`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037331`
- test_structured_rmse: `0.042225`

## Interpretation

The held-out val error stayed finite with MAE=0.001974 deg and RMSE=0.002761 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002284 deg and RMSE=0.003660 deg, which indicates a numerically stable baseline run.
