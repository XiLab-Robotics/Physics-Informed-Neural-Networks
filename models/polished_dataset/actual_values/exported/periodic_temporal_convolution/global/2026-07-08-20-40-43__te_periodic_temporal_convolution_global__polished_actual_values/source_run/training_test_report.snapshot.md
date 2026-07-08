# Periodic Temporal Convolution Global Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_global__polished_actual_values`
- Model Family: `periodic_temporal_convolution_global`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-20-40-43__te_periodic_temporal_convolution_global__polished_actual_values/checkpoints/periodic_temporal_convolution-epoch=109-val_mae=0.00190820.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004737`
- val_mae: `0.001908`
- val_rmse: `0.002644`
- val_pointwise_loss: `0.004737`
- val_centered_curve_shape_loss: `0.004290`
- val_curve_offset_loss: `0.000447`
- val_curve_amplitude_loss: `0.023856`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.005351`
- test_mae: `0.001999`
- test_rmse: `0.002971`
- test_pointwise_loss: `0.005351`
- test_centered_curve_shape_loss: `0.004853`
- test_curve_offset_loss: `0.000498`
- test_curve_amplitude_loss: `0.027483`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001908 deg and RMSE=0.002644 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001999 deg and RMSE=0.002971 deg, which indicates a numerically stable baseline run.
