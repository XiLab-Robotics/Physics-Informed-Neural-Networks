# Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_fw__simplified_setpoints`
- Model Family: `temporal_convolution_fw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-04-14-38__te_temporal_convolution_fw__simplified_setpoints/checkpoints/temporal_convolution-epoch=031-val_mae=0.00377881.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011773`
- val_mae: `0.003779`
- val_rmse: `0.004669`
- val_pointwise_loss: `0.011773`
- val_centered_curve_shape_loss: `0.007437`
- val_curve_offset_loss: `0.004336`
- val_curve_amplitude_loss: `0.067190`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009010`
- test_mae: `0.003530`
- test_rmse: `0.004341`
- test_pointwise_loss: `0.009010`
- test_centered_curve_shape_loss: `0.004140`
- test_curve_offset_loss: `0.004869`
- test_curve_amplitude_loss: `0.033652`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003779 deg and RMSE=0.004669 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003530 deg and RMSE=0.004341 deg, which indicates a numerically stable baseline run.
