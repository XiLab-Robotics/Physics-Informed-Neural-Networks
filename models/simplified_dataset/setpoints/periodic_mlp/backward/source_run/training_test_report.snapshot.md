# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_bw__simplified_setpoints`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp/2026-07-07-20-20-54__te_periodic_mlp_bw__simplified_setpoints/checkpoints/periodic_mlp-epoch=062-val_mae=0.00301630.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007477`
- val_mae: `0.003016`
- val_rmse: `0.003734`
- val_pointwise_loss: `0.007477`
- val_centered_curve_shape_loss: `0.003611`
- val_curve_offset_loss: `0.004849`
- val_curve_amplitude_loss: `0.065427`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008314`
- test_mae: `0.003446`
- test_rmse: `0.004162`
- test_pointwise_loss: `0.008314`
- test_centered_curve_shape_loss: `0.003359`
- test_curve_offset_loss: `0.006078`
- test_curve_amplitude_loss: `0.062618`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003016 deg and RMSE=0.003734 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003446 deg and RMSE=0.004162 deg, which indicates a numerically stable baseline run.
