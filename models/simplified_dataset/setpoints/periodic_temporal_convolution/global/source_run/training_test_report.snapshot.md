# Periodic Temporal Convolution Global Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_global__simplified_setpoints`
- Model Family: `periodic_temporal_convolution_global`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-19-09-50__te_periodic_temporal_convolution_global__simplified_setpoints/checkpoints/periodic_temporal_convolution-epoch=095-val_mae=0.00360046.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010238`
- val_mae: `0.003600`
- val_rmse: `0.004375`
- val_pointwise_loss: `0.010238`
- val_centered_curve_shape_loss: `0.005816`
- val_curve_offset_loss: `0.004421`
- val_curve_amplitude_loss: `0.039066`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008029`
- test_mae: `0.003436`
- test_rmse: `0.004106`
- test_pointwise_loss: `0.008029`
- test_centered_curve_shape_loss: `0.002870`
- test_curve_offset_loss: `0.005159`
- test_curve_amplitude_loss: `0.015555`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003600 deg and RMSE=0.004375 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003436 deg and RMSE=0.004106 deg, which indicates a numerically stable baseline run.
