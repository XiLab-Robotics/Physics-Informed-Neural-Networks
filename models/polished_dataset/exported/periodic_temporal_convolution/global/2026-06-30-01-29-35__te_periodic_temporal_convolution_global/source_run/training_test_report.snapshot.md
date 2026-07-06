# Periodic Temporal Convolution Global Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_global`
- Model Family: `periodic_temporal_convolution_global`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_temporal_convolution\2026-06-30-01-29-35__te_periodic_temporal_convolution_global\checkpoints\periodic_temporal_convolution-epoch=030-val_mae=0.00215997.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005392`
- val_mae: `0.002160`
- val_rmse: `0.002621`
- val_pointwise_loss: `0.005392`
- val_centered_curve_shape_loss: `0.004470`
- val_curve_offset_loss: `0.000922`
- val_curve_amplitude_loss: `0.028104`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006413`
- test_mae: `0.002302`
- test_rmse: `0.002863`
- test_pointwise_loss: `0.006413`
- test_centered_curve_shape_loss: `0.005106`
- test_curve_offset_loss: `0.001307`
- test_curve_amplitude_loss: `0.032326`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002160 deg and RMSE=0.002621 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002302 deg and RMSE=0.002863 deg, which indicates a numerically stable baseline run.
