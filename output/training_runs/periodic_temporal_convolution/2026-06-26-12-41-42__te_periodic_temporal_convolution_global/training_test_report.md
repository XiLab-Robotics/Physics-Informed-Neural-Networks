# Periodic Temporal Convolution Global Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_global`
- Model Family: `periodic_temporal_convolution_global`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution\2026-06-26-12-41-42__te_periodic_temporal_convolution_global\checkpoints\periodic_temporal_convolution-epoch=025-val_mae=0.00220180.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005561`
- val_mae: `0.002202`
- val_rmse: `0.002682`
- val_pointwise_loss: `0.005561`
- val_centered_curve_shape_loss: `0.004635`
- val_curve_offset_loss: `0.000926`
- val_curve_amplitude_loss: `0.032505`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006300`
- test_mae: `0.002319`
- test_rmse: `0.002900`
- test_pointwise_loss: `0.006300`
- test_centered_curve_shape_loss: `0.005375`
- test_curve_offset_loss: `0.000924`
- test_curve_amplitude_loss: `0.036809`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002202 deg and RMSE=0.002682 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002319 deg and RMSE=0.002900 deg, which indicates a numerically stable baseline run.
