# Periodic Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_bw`
- Model Family: `periodic_temporal_convolution_bw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_temporal_convolution\2026-06-30-01-59-09__te_periodic_temporal_convolution_bw\checkpoints\periodic_temporal_convolution-epoch=064-val_mae=0.00207692.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005140`
- val_mae: `0.002077`
- val_rmse: `0.002526`
- val_pointwise_loss: `0.005140`
- val_centered_curve_shape_loss: `0.004406`
- val_curve_offset_loss: `0.000734`
- val_curve_amplitude_loss: `0.029972`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.005813`
- test_mae: `0.002174`
- test_rmse: `0.002734`
- test_pointwise_loss: `0.005813`
- test_centered_curve_shape_loss: `0.005158`
- test_curve_offset_loss: `0.000656`
- test_curve_amplitude_loss: `0.034975`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002077 deg and RMSE=0.002526 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002174 deg and RMSE=0.002734 deg, which indicates a numerically stable baseline run.
