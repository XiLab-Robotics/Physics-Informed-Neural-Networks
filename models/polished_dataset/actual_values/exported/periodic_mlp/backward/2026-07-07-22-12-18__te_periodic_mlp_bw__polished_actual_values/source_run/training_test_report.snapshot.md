# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_bw__polished_actual_values`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-22-12-18__te_periodic_mlp_bw__polished_actual_values/checkpoints/periodic_mlp-epoch=076-val_mae=0.00167645.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002922`
- val_mae: `0.001676`
- val_rmse: `0.002276`
- val_pointwise_loss: `0.002922`
- val_centered_curve_shape_loss: `0.003358`
- val_curve_offset_loss: `0.000612`
- val_curve_amplitude_loss: `0.051288`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004411`
- test_mae: `0.001869`
- test_rmse: `0.002856`
- test_pointwise_loss: `0.004411`
- test_centered_curve_shape_loss: `0.005529`
- test_curve_offset_loss: `0.003525`
- test_curve_amplitude_loss: `0.075753`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001676 deg and RMSE=0.002276 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001869 deg and RMSE=0.002856 deg, which indicates a numerically stable baseline run.
