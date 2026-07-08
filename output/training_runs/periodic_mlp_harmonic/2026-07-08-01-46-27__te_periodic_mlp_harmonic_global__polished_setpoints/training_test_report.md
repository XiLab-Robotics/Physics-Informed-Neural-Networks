# Periodic Mlp Harmonic Global Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_global__polished_setpoints`
- Model Family: `periodic_mlp_harmonic_global`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-01-46-27__te_periodic_mlp_harmonic_global__polished_setpoints/checkpoints/periodic_mlp-epoch=183-val_mae=0.00113740.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001784`
- val_mae: `0.001137`
- val_rmse: `0.001604`
- val_pointwise_loss: `0.001784`
- val_centered_curve_shape_loss: `0.002597`
- val_curve_offset_loss: `0.000394`
- val_curve_amplitude_loss: `0.018855`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.002998`
- test_mae: `0.001270`
- test_rmse: `0.002217`
- test_pointwise_loss: `0.002998`
- test_centered_curve_shape_loss: `0.004064`
- test_curve_offset_loss: `0.003378`
- test_curve_amplitude_loss: `0.034242`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001137 deg and RMSE=0.001604 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001270 deg and RMSE=0.002217 deg, which indicates a numerically stable baseline run.
