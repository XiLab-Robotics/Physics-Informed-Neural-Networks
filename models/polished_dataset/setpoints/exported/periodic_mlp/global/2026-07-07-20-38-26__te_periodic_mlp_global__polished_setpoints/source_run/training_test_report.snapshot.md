# Periodic Mlp Global Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_global__polished_setpoints`
- Model Family: `periodic_mlp_global`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-20-38-26__te_periodic_mlp_global__polished_setpoints/checkpoints/periodic_mlp-epoch=080-val_mae=0.00165354.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002799`
- val_mae: `0.001654`
- val_rmse: `0.002219`
- val_pointwise_loss: `0.002799`
- val_centered_curve_shape_loss: `0.003301`
- val_curve_offset_loss: `0.000485`
- val_curve_amplitude_loss: `0.057898`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004229`
- test_mae: `0.001794`
- test_rmse: `0.002792`
- test_pointwise_loss: `0.004229`
- test_centered_curve_shape_loss: `0.005294`
- test_curve_offset_loss: `0.003781`
- test_curve_amplitude_loss: `0.083394`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001654 deg and RMSE=0.002219 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001794 deg and RMSE=0.002792 deg, which indicates a numerically stable baseline run.
