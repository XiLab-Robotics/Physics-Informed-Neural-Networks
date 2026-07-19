# Periodic Mlp Harmonic Global Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_global__simplified_setpoints`
- Model Family: `periodic_mlp_harmonic_global`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-01-02-50__te_periodic_mlp_harmonic_global__simplified_setpoints/checkpoints/periodic_mlp-epoch=059-val_mae=0.00284742.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006431`
- val_mae: `0.002847`
- val_rmse: `0.003455`
- val_pointwise_loss: `0.006431`
- val_centered_curve_shape_loss: `0.002778`
- val_curve_offset_loss: `0.004722`
- val_curve_amplitude_loss: `0.034000`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007199`
- test_mae: `0.003293`
- test_rmse: `0.003865`
- test_pointwise_loss: `0.007199`
- test_centered_curve_shape_loss: `0.002461`
- test_curve_offset_loss: `0.005770`
- test_curve_amplitude_loss: `0.030894`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002847 deg and RMSE=0.003455 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003293 deg and RMSE=0.003865 deg, which indicates a numerically stable baseline run.
