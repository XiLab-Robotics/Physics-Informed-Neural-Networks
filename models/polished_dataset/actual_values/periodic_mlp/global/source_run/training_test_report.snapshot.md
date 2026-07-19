# Periodic Mlp Global Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_global__polished_actual_values`
- Model Family: `periodic_mlp_global`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-21-37-50__te_periodic_mlp_global__polished_actual_values/checkpoints/periodic_mlp-epoch=094-val_mae=0.00165445.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002828`
- val_mae: `0.001654`
- val_rmse: `0.002237`
- val_pointwise_loss: `0.002828`
- val_centered_curve_shape_loss: `0.003355`
- val_curve_offset_loss: `0.000509`
- val_curve_amplitude_loss: `0.048243`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004297`
- test_mae: `0.001813`
- test_rmse: `0.002796`
- test_pointwise_loss: `0.004297`
- test_centered_curve_shape_loss: `0.005480`
- test_curve_offset_loss: `0.003582`
- test_curve_amplitude_loss: `0.072452`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001654 deg and RMSE=0.002237 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001813 deg and RMSE=0.002796 deg, which indicates a numerically stable baseline run.
