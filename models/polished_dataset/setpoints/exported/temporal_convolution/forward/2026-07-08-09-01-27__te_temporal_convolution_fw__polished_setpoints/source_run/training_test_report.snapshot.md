# Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_fw__polished_setpoints`
- Model Family: `temporal_convolution_fw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-09-01-27__te_temporal_convolution_fw__polished_setpoints/checkpoints/temporal_convolution-epoch=042-val_mae=0.00225272.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006047`
- val_mae: `0.002253`
- val_rmse: `0.003091`
- val_pointwise_loss: `0.006047`
- val_centered_curve_shape_loss: `0.005431`
- val_curve_offset_loss: `0.000616`
- val_curve_amplitude_loss: `0.057373`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009546`
- test_mae: `0.002544`
- test_rmse: `0.003914`
- test_pointwise_loss: `0.009546`
- test_centered_curve_shape_loss: `0.006344`
- test_curve_offset_loss: `0.003203`
- test_curve_amplitude_loss: `0.069537`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002253 deg and RMSE=0.003091 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002544 deg and RMSE=0.003914 deg, which indicates a numerically stable baseline run.
