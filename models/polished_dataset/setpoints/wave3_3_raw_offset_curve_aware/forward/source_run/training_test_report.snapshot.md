# Wave3 3 Raw Offset Curve Aware Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_fw__polished_setpoints`
- Model Family: `wave3_3_raw_offset_curve_aware_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-12-00-23-59__te_wave3_3_raw_offset_curve_aware_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=119-val_mae=0.00195047.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005364`
- val_mae: `0.001950`
- val_rmse: `0.002719`
- val_pointwise_loss: `0.005120`
- val_centered_curve_shape_loss: `0.004577`
- val_curve_offset_loss: `0.000543`
- val_curve_amplitude_loss: `0.029806`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.026465`
- val_structured_rmse: `0.031639`
- val_residual_offset_mean_abs: `0.026546`

## Test Metrics

- test_loss: `0.010019`
- test_mae: `0.002285`
- test_rmse: `0.003630`
- test_pointwise_loss: `0.008605`
- test_centered_curve_shape_loss: `0.005465`
- test_curve_offset_loss: `0.003140`
- test_curve_amplitude_loss: `0.039532`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.026514`
- test_structured_rmse: `0.031862`
- test_residual_offset_mean_abs: `0.026281`

## Interpretation

The held-out val error stayed finite with MAE=0.001950 deg and RMSE=0.002719 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002285 deg and RMSE=0.003630 deg, which indicates a numerically stable baseline run.
