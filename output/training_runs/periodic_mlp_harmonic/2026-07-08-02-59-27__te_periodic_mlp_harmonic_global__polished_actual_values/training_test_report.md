# Periodic Mlp Harmonic Global Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_global__polished_actual_values`
- Model Family: `periodic_mlp_harmonic_global`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-02-59-27__te_periodic_mlp_harmonic_global__polished_actual_values/checkpoints/periodic_mlp-epoch=074-val_mae=0.00123779.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001956`
- val_mae: `0.001238`
- val_rmse: `0.001714`
- val_pointwise_loss: `0.001956`
- val_centered_curve_shape_loss: `0.002472`
- val_curve_offset_loss: `0.000547`
- val_curve_amplitude_loss: `0.022778`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003476`
- test_mae: `0.001445`
- test_rmse: `0.002405`
- test_pointwise_loss: `0.003476`
- test_centered_curve_shape_loss: `0.004460`
- test_curve_offset_loss: `0.003492`
- test_curve_amplitude_loss: `0.040721`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001238 deg and RMSE=0.001714 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001445 deg and RMSE=0.002405 deg, which indicates a numerically stable baseline run.
