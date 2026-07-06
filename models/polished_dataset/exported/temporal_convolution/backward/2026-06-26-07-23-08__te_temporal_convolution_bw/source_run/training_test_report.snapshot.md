# Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_bw`
- Model Family: `temporal_convolution_bw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\temporal_convolution\2026-06-26-07-23-08__te_temporal_convolution_bw\checkpoints\temporal_convolution-epoch=071-val_mae=0.00230252.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006126`
- val_mae: `0.002303`
- val_rmse: `0.002846`
- val_pointwise_loss: `0.006126`
- val_centered_curve_shape_loss: `0.005454`
- val_curve_offset_loss: `0.000672`
- val_curve_amplitude_loss: `0.059223`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006908`
- test_mae: `0.002391`
- test_rmse: `0.003044`
- test_pointwise_loss: `0.006908`
- test_centered_curve_shape_loss: `0.006194`
- test_curve_offset_loss: `0.000714`
- test_curve_amplitude_loss: `0.064846`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002303 deg and RMSE=0.002846 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002391 deg and RMSE=0.003044 deg, which indicates a numerically stable baseline run.
