# Periodic Mlp Global Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_global__simplified_setpoints`
- Model Family: `periodic_mlp_global`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-20-03-02__te_periodic_mlp_global__simplified_setpoints/checkpoints/periodic_mlp-epoch=090-val_mae=0.00301298.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007302`
- val_mae: `0.003013`
- val_rmse: `0.003696`
- val_pointwise_loss: `0.007302`
- val_centered_curve_shape_loss: `0.003609`
- val_curve_offset_loss: `0.004746`
- val_curve_amplitude_loss: `0.066035`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007824`
- test_mae: `0.003346`
- test_rmse: `0.004047`
- test_pointwise_loss: `0.007824`
- test_centered_curve_shape_loss: `0.003348`
- test_curve_offset_loss: `0.005630`
- test_curve_amplitude_loss: `0.062460`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003013 deg and RMSE=0.003696 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003346 deg and RMSE=0.004047 deg, which indicates a numerically stable baseline run.
