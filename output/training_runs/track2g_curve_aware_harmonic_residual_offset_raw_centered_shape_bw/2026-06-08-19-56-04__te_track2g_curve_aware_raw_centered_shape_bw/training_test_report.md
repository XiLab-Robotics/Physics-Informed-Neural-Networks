# Track2G Curve Aware Harmonic Residual Offset Raw Centered Shape Bw Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_raw_centered_shape_bw`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw\2026-06-08-19-56-04__te_track2g_curve_aware_raw_centered_shape_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=078-val_mae=0.00373978.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.052317`
- val_mae: `0.003740`
- val_rmse: `0.004334`
- val_pointwise_loss: `0.042356`
- val_centered_curve_shape_loss: `0.028167`
- val_curve_offset_loss: `0.014190`
- val_curve_amplitude_loss: `0.208757`
- val_sparse_harmonic_shape_loss: `0.000681`
- val_structured_mae: `0.012192`
- val_structured_rmse: `0.013595`
- val_residual_offset_mean_abs: `0.011487`

## Test Metrics

- test_loss: `0.035737`
- test_mae: `0.003465`
- test_rmse: `0.003998`
- test_pointwise_loss: `0.030823`
- test_centered_curve_shape_loss: `0.013904`
- test_curve_offset_loss: `0.016919`
- test_curve_amplitude_loss: `0.085012`
- test_sparse_harmonic_shape_loss: `0.000315`
- test_structured_mae: `0.011985`
- test_structured_rmse: `0.013121`
- test_residual_offset_mean_abs: `0.010766`

## Interpretation

The held-out val error stayed finite with MAE=0.003740 deg and RMSE=0.004334 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003465 deg and RMSE=0.003998 deg, which indicates a numerically stable baseline run.
