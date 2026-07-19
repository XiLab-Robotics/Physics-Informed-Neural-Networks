# Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_bw__simplified_setpoints`
- Model Family: `temporal_convolution_bw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-04-21-12__te_temporal_convolution_bw__simplified_setpoints/checkpoints/temporal_convolution-epoch=091-val_mae=0.00381312.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012086`
- val_mae: `0.003813`
- val_rmse: `0.004732`
- val_pointwise_loss: `0.012086`
- val_centered_curve_shape_loss: `0.007326`
- val_curve_offset_loss: `0.004760`
- val_curve_amplitude_loss: `0.079423`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009213`
- test_mae: `0.003547`
- test_rmse: `0.004393`
- test_pointwise_loss: `0.009213`
- test_centered_curve_shape_loss: `0.004020`
- test_curve_offset_loss: `0.005193`
- test_curve_amplitude_loss: `0.043683`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003813 deg and RMSE=0.004732 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003547 deg and RMSE=0.004393 deg, which indicates a numerically stable baseline run.
