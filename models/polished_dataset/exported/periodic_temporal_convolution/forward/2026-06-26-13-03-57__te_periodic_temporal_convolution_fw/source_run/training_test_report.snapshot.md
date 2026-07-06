# Periodic Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_fw`
- Model Family: `periodic_temporal_convolution_fw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_temporal_convolution\2026-06-26-13-03-57__te_periodic_temporal_convolution_fw\checkpoints\periodic_temporal_convolution-epoch=055-val_mae=0.00206541.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005202`
- val_mae: `0.002065`
- val_rmse: `0.002522`
- val_pointwise_loss: `0.005202`
- val_centered_curve_shape_loss: `0.004431`
- val_curve_offset_loss: `0.000772`
- val_curve_amplitude_loss: `0.030937`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.005942`
- test_mae: `0.002178`
- test_rmse: `0.002730`
- test_pointwise_loss: `0.005942`
- test_centered_curve_shape_loss: `0.005166`
- test_curve_offset_loss: `0.000776`
- test_curve_amplitude_loss: `0.035854`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002065 deg and RMSE=0.002522 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002178 deg and RMSE=0.002730 deg, which indicates a numerically stable baseline run.
