# Track2G Curve Aware Harmonic Residual Offset Pointwise Control Bw Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_pointwise_control_bw`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw\2026-06-08-19-08-39__te_track2g_curve_aware_pointwise_control_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=106-val_mae=0.00374939.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.042945`
- val_mae: `0.003749`
- val_rmse: `0.004334`
- val_pointwise_loss: `0.042945`
- val_centered_curve_shape_loss: `0.028354`
- val_curve_offset_loss: `0.014592`
- val_curve_amplitude_loss: `0.214198`
- val_sparse_harmonic_shape_loss: `0.000686`
- val_structured_mae: `0.011483`
- val_structured_rmse: `0.012617`
- val_residual_offset_mean_abs: `0.010498`

## Test Metrics

- test_loss: `0.030920`
- test_mae: `0.003430`
- test_rmse: `0.003945`
- test_pointwise_loss: `0.030920`
- test_centered_curve_shape_loss: `0.013914`
- test_curve_offset_loss: `0.017007`
- test_curve_amplitude_loss: `0.087282`
- test_sparse_harmonic_shape_loss: `0.000315`
- test_structured_mae: `0.010688`
- test_structured_rmse: `0.011703`
- test_residual_offset_mean_abs: `0.009846`

## Interpretation

The held-out val error stayed finite with MAE=0.003749 deg and RMSE=0.004334 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003430 deg and RMSE=0.003945 deg, which indicates a numerically stable baseline run.
