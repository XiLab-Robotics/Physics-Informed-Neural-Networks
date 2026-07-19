# Temporal Convolution Global Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_global__polished_setpoints`
- Model Family: `temporal_convolution_global`
- Model Type: `temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-08-48-08__te_temporal_convolution_global__polished_setpoints/checkpoints/temporal_convolution-epoch=074-val_mae=0.00225012.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006036`
- val_mae: `0.002250`
- val_rmse: `0.003106`
- val_pointwise_loss: `0.006036`
- val_centered_curve_shape_loss: `0.005389`
- val_curve_offset_loss: `0.000647`
- val_curve_amplitude_loss: `0.066078`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009503`
- test_mae: `0.002538`
- test_rmse: `0.003933`
- test_pointwise_loss: `0.009503`
- test_centered_curve_shape_loss: `0.006296`
- test_curve_offset_loss: `0.003208`
- test_curve_amplitude_loss: `0.078438`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002250 deg and RMSE=0.003106 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002538 deg and RMSE=0.003933 deg, which indicates a numerically stable baseline run.
