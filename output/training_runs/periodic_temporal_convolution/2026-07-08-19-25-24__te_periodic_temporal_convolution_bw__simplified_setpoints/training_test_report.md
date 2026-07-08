# Periodic Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_bw__simplified_setpoints`
- Model Family: `periodic_temporal_convolution_bw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-19-25-24__te_periodic_temporal_convolution_bw__simplified_setpoints/checkpoints/periodic_temporal_convolution-epoch=066-val_mae=0.00355314.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010357`
- val_mae: `0.003553`
- val_rmse: `0.004378`
- val_pointwise_loss: `0.010357`
- val_centered_curve_shape_loss: `0.005948`
- val_curve_offset_loss: `0.004409`
- val_curve_amplitude_loss: `0.043502`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008116`
- test_mae: `0.003388`
- test_rmse: `0.004127`
- test_pointwise_loss: `0.008116`
- test_centered_curve_shape_loss: `0.002938`
- test_curve_offset_loss: `0.005178`
- test_curve_amplitude_loss: `0.017874`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003553 deg and RMSE=0.004378 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003388 deg and RMSE=0.004127 deg, which indicates a numerically stable baseline run.
