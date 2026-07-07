# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_fw__polished_setpoints`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-20-52-32__te_periodic_mlp_fw__polished_setpoints/checkpoints/periodic_mlp-epoch=089-val_mae=0.00162401.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002761`
- val_mae: `0.001624`
- val_rmse: `0.002193`
- val_pointwise_loss: `0.002761`
- val_centered_curve_shape_loss: `0.003287`
- val_curve_offset_loss: `0.000434`
- val_curve_amplitude_loss: `0.058172`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004172`
- test_mae: `0.001770`
- test_rmse: `0.002770`
- test_pointwise_loss: `0.004172`
- test_centered_curve_shape_loss: `0.005287`
- test_curve_offset_loss: `0.003599`
- test_curve_amplitude_loss: `0.085366`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001624 deg and RMSE=0.002193 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001770 deg and RMSE=0.002770 deg, which indicates a numerically stable baseline run.
