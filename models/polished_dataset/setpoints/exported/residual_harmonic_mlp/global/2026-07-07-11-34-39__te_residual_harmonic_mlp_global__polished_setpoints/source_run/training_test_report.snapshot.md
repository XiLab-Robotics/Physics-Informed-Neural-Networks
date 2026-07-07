# Residual Harmonic Mlp Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_global__polished_setpoints`
- Model Family: `residual_harmonic_mlp_global`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-11-34-39__te_residual_harmonic_mlp_global__polished_setpoints/checkpoints/residual_harmonic_mlp-epoch=069-val_mae=0.00158201.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002659`
- val_mae: `0.001582`
- val_rmse: `0.002046`
- val_pointwise_loss: `0.002659`
- val_centered_curve_shape_loss: `0.003035`
- val_curve_offset_loss: `0.000307`
- val_curve_amplitude_loss: `0.054746`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040310`
- val_structured_rmse: `0.043849`

## Test Metrics

- test_loss: `0.004158`
- test_mae: `0.001758`
- test_rmse: `0.002348`
- test_pointwise_loss: `0.004158`
- test_centered_curve_shape_loss: `0.003779`
- test_curve_offset_loss: `0.001426`
- test_curve_amplitude_loss: `0.068066`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039808`
- test_structured_rmse: `0.043845`

## Interpretation

The held-out val error stayed finite with MAE=0.001582 deg and RMSE=0.002046 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001758 deg and RMSE=0.002348 deg, which indicates a numerically stable baseline run.
