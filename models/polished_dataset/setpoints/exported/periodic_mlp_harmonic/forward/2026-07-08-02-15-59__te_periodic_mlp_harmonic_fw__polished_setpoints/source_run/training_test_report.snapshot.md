# Periodic Mlp Harmonic Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_fw__polished_setpoints`
- Model Family: `periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-02-15-59__te_periodic_mlp_harmonic_fw__polished_setpoints/checkpoints/periodic_mlp-epoch=051-val_mae=0.00120808.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001941`
- val_mae: `0.001208`
- val_rmse: `0.001696`
- val_pointwise_loss: `0.001941`
- val_centered_curve_shape_loss: `0.002465`
- val_curve_offset_loss: `0.000497`
- val_curve_amplitude_loss: `0.026900`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003415`
- test_mae: `0.001442`
- test_rmse: `0.002411`
- test_pointwise_loss: `0.003415`
- test_centered_curve_shape_loss: `0.004309`
- test_curve_offset_loss: `0.003650`
- test_curve_amplitude_loss: `0.047372`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001208 deg and RMSE=0.001696 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001442 deg and RMSE=0.002411 deg, which indicates a numerically stable baseline run.
