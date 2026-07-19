# Periodic Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_fw__polished_actual_values`
- Model Family: `periodic_temporal_convolution_fw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-21-06-17__te_periodic_temporal_convolution_fw__polished_actual_values/checkpoints/periodic_temporal_convolution-epoch=087-val_mae=0.00193888.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004830`
- val_mae: `0.001939`
- val_rmse: `0.002687`
- val_pointwise_loss: `0.004830`
- val_centered_curve_shape_loss: `0.004311`
- val_curve_offset_loss: `0.000519`
- val_curve_amplitude_loss: `0.024898`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.005666`
- test_mae: `0.002077`
- test_rmse: `0.003080`
- test_pointwise_loss: `0.005666`
- test_centered_curve_shape_loss: `0.005060`
- test_curve_offset_loss: `0.000606`
- test_curve_amplitude_loss: `0.029047`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001939 deg and RMSE=0.002687 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002077 deg and RMSE=0.003080 deg, which indicates a numerically stable baseline run.
