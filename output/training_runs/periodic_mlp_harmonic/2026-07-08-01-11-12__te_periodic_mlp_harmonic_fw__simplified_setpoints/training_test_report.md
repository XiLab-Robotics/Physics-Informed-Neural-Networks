# Periodic Mlp Harmonic Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_fw__simplified_setpoints`
- Model Family: `periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-01-11-12__te_periodic_mlp_harmonic_fw__simplified_setpoints/checkpoints/periodic_mlp-epoch=055-val_mae=0.00280280.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006502`
- val_mae: `0.002803`
- val_rmse: `0.003451`
- val_pointwise_loss: `0.006502`
- val_centered_curve_shape_loss: `0.002749`
- val_curve_offset_loss: `0.004872`
- val_curve_amplitude_loss: `0.029788`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006783`
- test_mae: `0.003065`
- test_rmse: `0.003709`
- test_pointwise_loss: `0.006783`
- test_centered_curve_shape_loss: `0.002423`
- test_curve_offset_loss: `0.005496`
- test_curve_amplitude_loss: `0.026880`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002803 deg and RMSE=0.003451 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003065 deg and RMSE=0.003709 deg, which indicates a numerically stable baseline run.
