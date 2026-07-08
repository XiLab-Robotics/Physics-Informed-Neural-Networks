# Periodic Mlp Harmonic Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_fw__polished_actual_values`
- Model Family: `periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-03-17-38__te_periodic_mlp_harmonic_fw__polished_actual_values/checkpoints/periodic_mlp-epoch=045-val_mae=0.00131065.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002078`
- val_mae: `0.001311`
- val_rmse: `0.001818`
- val_pointwise_loss: `0.002078`
- val_centered_curve_shape_loss: `0.002555`
- val_curve_offset_loss: `0.000576`
- val_curve_amplitude_loss: `0.028218`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003772`
- test_mae: `0.001590`
- test_rmse: `0.002522`
- test_pointwise_loss: `0.003772`
- test_centered_curve_shape_loss: `0.004507`
- test_curve_offset_loss: `0.003651`
- test_curve_amplitude_loss: `0.047434`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001311 deg and RMSE=0.001818 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001590 deg and RMSE=0.002522 deg, which indicates a numerically stable baseline run.
