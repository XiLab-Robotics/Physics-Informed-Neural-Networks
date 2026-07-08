# Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_fw__polished_actual_values`
- Model Family: `temporal_convolution_fw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-10-20-02__te_temporal_convolution_fw__polished_actual_values/checkpoints/temporal_convolution-epoch=064-val_mae=0.00227215.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006100`
- val_mae: `0.002272`
- val_rmse: `0.003128`
- val_pointwise_loss: `0.006100`
- val_centered_curve_shape_loss: `0.005546`
- val_curve_offset_loss: `0.000555`
- val_curve_amplitude_loss: `0.050441`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007044`
- test_mae: `0.002390`
- test_rmse: `0.003496`
- test_pointwise_loss: `0.007044`
- test_centered_curve_shape_loss: `0.006372`
- test_curve_offset_loss: `0.000672`
- test_curve_amplitude_loss: `0.055714`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002272 deg and RMSE=0.003128 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002390 deg and RMSE=0.003496 deg, which indicates a numerically stable baseline run.
