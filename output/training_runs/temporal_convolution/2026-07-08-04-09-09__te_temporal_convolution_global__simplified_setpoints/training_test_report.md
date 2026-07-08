# Temporal Convolution Global Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_global__simplified_setpoints`
- Model Family: `temporal_convolution_global`
- Model Type: `temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-04-09-09__te_temporal_convolution_global__simplified_setpoints/checkpoints/temporal_convolution-epoch=016-val_mae=0.00380497.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012087`
- val_mae: `0.003805`
- val_rmse: `0.004749`
- val_pointwise_loss: `0.012087`
- val_centered_curve_shape_loss: `0.007551`
- val_curve_offset_loss: `0.004537`
- val_curve_amplitude_loss: `0.068362`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009553`
- test_mae: `0.003624`
- test_rmse: `0.004478`
- test_pointwise_loss: `0.009553`
- test_centered_curve_shape_loss: `0.004231`
- test_curve_offset_loss: `0.005322`
- test_curve_amplitude_loss: `0.033912`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003805 deg and RMSE=0.004749 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003624 deg and RMSE=0.004478 deg, which indicates a numerically stable baseline run.
