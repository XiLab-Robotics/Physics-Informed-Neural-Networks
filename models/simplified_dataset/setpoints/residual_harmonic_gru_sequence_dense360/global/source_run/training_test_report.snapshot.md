# Residual Harmonic Gru Sequence Dense360 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense360_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-30-19__te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=090-val_mae=0.00360722.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011036`
- val_mae: `0.003607`
- val_rmse: `0.004492`
- val_pointwise_loss: `0.011036`
- val_centered_curve_shape_loss: `0.006590`
- val_curve_offset_loss: `0.004446`
- val_curve_amplitude_loss: `0.043294`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037824`
- val_structured_rmse: `0.042709`

## Test Metrics

- test_loss: `0.008580`
- test_mae: `0.003404`
- test_rmse: `0.004244`
- test_pointwise_loss: `0.008580`
- test_centered_curve_shape_loss: `0.003438`
- test_curve_offset_loss: `0.005143`
- test_curve_amplitude_loss: `0.019707`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040700`
- test_structured_rmse: `0.045443`

## Interpretation

The held-out val error stayed finite with MAE=0.003607 deg and RMSE=0.004492 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003404 deg and RMSE=0.004244 deg, which indicates a numerically stable baseline run.
