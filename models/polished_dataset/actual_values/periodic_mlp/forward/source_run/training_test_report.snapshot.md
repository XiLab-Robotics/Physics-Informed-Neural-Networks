# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_fw__polished_actual_values`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-21-58-17__te_periodic_mlp_fw__polished_actual_values/checkpoints/periodic_mlp-epoch=048-val_mae=0.00168924.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002921`
- val_mae: `0.001689`
- val_rmse: `0.002286`
- val_pointwise_loss: `0.002921`
- val_centered_curve_shape_loss: `0.003424`
- val_curve_offset_loss: `0.000533`
- val_curve_amplitude_loss: `0.056260`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004532`
- test_mae: `0.001877`
- test_rmse: `0.002885`
- test_pointwise_loss: `0.004532`
- test_centered_curve_shape_loss: `0.005559`
- test_curve_offset_loss: `0.003705`
- test_curve_amplitude_loss: `0.079874`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001689 deg and RMSE=0.002286 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001877 deg and RMSE=0.002885 deg, which indicates a numerically stable baseline run.
