# Periodic Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_bw`
- Model Family: `periodic_temporal_convolution_bw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution\2026-06-26-13-35-38__te_periodic_temporal_convolution_bw\checkpoints\periodic_temporal_convolution-epoch=043-val_mae=0.00216132.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005437`
- val_mae: `0.002161`
- val_rmse: `0.002622`
- val_pointwise_loss: `0.005437`
- val_centered_curve_shape_loss: `0.004440`
- val_curve_offset_loss: `0.000997`
- val_curve_amplitude_loss: `0.030731`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006049`
- test_mae: `0.002238`
- test_rmse: `0.002791`
- test_pointwise_loss: `0.006049`
- test_centered_curve_shape_loss: `0.005145`
- test_curve_offset_loss: `0.000904`
- test_curve_amplitude_loss: `0.035284`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002161 deg and RMSE=0.002622 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002238 deg and RMSE=0.002791 deg, which indicates a numerically stable baseline run.
