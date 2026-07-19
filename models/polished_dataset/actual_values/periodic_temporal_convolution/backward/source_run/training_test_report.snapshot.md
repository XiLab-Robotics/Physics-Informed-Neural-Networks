# Periodic Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_bw__polished_actual_values`
- Model Family: `periodic_temporal_convolution_bw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-21-27-59__te_periodic_temporal_convolution_bw__polished_actual_values/checkpoints/periodic_temporal_convolution-epoch=093-val_mae=0.00186606.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004744`
- val_mae: `0.001866`
- val_rmse: `0.002614`
- val_pointwise_loss: `0.004744`
- val_centered_curve_shape_loss: `0.004313`
- val_curve_offset_loss: `0.000431`
- val_curve_amplitude_loss: `0.025040`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.005447`
- test_mae: `0.002001`
- test_rmse: `0.003009`
- test_pointwise_loss: `0.005447`
- test_centered_curve_shape_loss: `0.004902`
- test_curve_offset_loss: `0.000544`
- test_curve_amplitude_loss: `0.028376`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001866 deg and RMSE=0.002614 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002001 deg and RMSE=0.003009 deg, which indicates a numerically stable baseline run.
