# Wave4 1 Log Cosh Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_fw`
- Model Family: `wave4_1_log_cosh_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-01-06-59-33__te_wave4_1_log_cosh_robust_loss_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=121-val_mae=0.00180694.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002397`
- val_mae: `0.001807`
- val_rmse: `0.002224`
- val_pointwise_loss: `0.002397`
- val_centered_curve_shape_loss: `0.004558`
- val_curve_offset_loss: `0.000326`
- val_curve_amplitude_loss: `0.036037`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.007707`
- val_structured_rmse: `0.008219`
- val_residual_offset_mean_abs: `0.007372`

## Test Metrics

- test_loss: `0.002769`
- test_mae: `0.001921`
- test_rmse: `0.002465`
- test_pointwise_loss: `0.002769`
- test_centered_curve_shape_loss: `0.005311`
- test_curve_offset_loss: `0.000330`
- test_curve_amplitude_loss: `0.041108`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.007874`
- test_structured_rmse: `0.008522`
- test_residual_offset_mean_abs: `0.007436`

## Interpretation

The held-out val error stayed finite with MAE=0.001807 deg and RMSE=0.002224 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001921 deg and RMSE=0.002465 deg, which indicates a numerically stable baseline run.
