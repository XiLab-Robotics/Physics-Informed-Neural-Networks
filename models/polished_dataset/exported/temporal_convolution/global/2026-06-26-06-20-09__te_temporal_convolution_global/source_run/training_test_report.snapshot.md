# Temporal Convolution Global Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_global`
- Model Family: `temporal_convolution_global`
- Model Type: `temporal_convolution`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\temporal_convolution\2026-06-26-06-20-09__te_temporal_convolution_global\checkpoints\temporal_convolution-epoch=080-val_mae=0.00230806.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006116`
- val_mae: `0.002308`
- val_rmse: `0.002849`
- val_pointwise_loss: `0.006116`
- val_centered_curve_shape_loss: `0.005502`
- val_curve_offset_loss: `0.000614`
- val_curve_amplitude_loss: `0.052384`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006861`
- test_mae: `0.002411`
- test_rmse: `0.003063`
- test_pointwise_loss: `0.006861`
- test_centered_curve_shape_loss: `0.006241`
- test_curve_offset_loss: `0.000620`
- test_curve_amplitude_loss: `0.059464`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002308 deg and RMSE=0.002849 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002411 deg and RMSE=0.003063 deg, which indicates a numerically stable baseline run.
