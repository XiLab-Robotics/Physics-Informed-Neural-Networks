# Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_bw__polished_setpoints`
- Model Family: `temporal_convolution_bw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-09-14-19__te_temporal_convolution_bw__polished_setpoints/checkpoints/temporal_convolution-epoch=125-val_mae=0.00222200.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005961`
- val_mae: `0.002222`
- val_rmse: `0.003063`
- val_pointwise_loss: `0.005961`
- val_centered_curve_shape_loss: `0.005375`
- val_curve_offset_loss: `0.000585`
- val_curve_amplitude_loss: `0.060713`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009321`
- test_mae: `0.002508`
- test_rmse: `0.003884`
- test_pointwise_loss: `0.009321`
- test_centered_curve_shape_loss: `0.006288`
- test_curve_offset_loss: `0.003032`
- test_curve_amplitude_loss: `0.074004`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002222 deg and RMSE=0.003063 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002508 deg and RMSE=0.003884 deg, which indicates a numerically stable baseline run.
