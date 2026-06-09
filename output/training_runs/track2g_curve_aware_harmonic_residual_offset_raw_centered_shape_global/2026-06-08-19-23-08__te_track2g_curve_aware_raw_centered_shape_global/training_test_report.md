# Track2G Curve Aware Harmonic Residual Offset Raw Centered Shape Global Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_raw_centered_shape_global`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global\2026-06-08-19-23-08__te_track2g_curve_aware_raw_centered_shape_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=086-val_mae=0.00363586.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.013208`
- val_mae: `0.003636`
- val_rmse: `0.004136`
- val_pointwise_loss: `0.010935`
- val_centered_curve_shape_loss: `0.006428`
- val_curve_offset_loss: `0.004507`
- val_curve_amplitude_loss: `0.044248`
- val_sparse_harmonic_shape_loss: `0.000152`
- val_structured_mae: `0.020503`
- val_structured_rmse: `0.022814`
- val_residual_offset_mean_abs: `0.020210`

## Test Metrics

- test_loss: `0.009305`
- test_mae: `0.003350`
- test_rmse: `0.003753`
- test_pointwise_loss: `0.008140`
- test_centered_curve_shape_loss: `0.003298`
- test_curve_offset_loss: `0.004841`
- test_curve_amplitude_loss: `0.019126`
- test_sparse_harmonic_shape_loss: `7.204743e-05`
- test_structured_mae: `0.023000`
- test_structured_rmse: `0.026200`
- test_residual_offset_mean_abs: `0.022908`

## Interpretation

The held-out val error stayed finite with MAE=0.003636 deg and RMSE=0.004136 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003350 deg and RMSE=0.003753 deg, which indicates a numerically stable baseline run.
