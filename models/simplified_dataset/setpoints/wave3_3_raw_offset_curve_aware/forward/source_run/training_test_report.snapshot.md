# Wave3 3 Raw Offset Curve Aware Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints`
- Model Family: `wave3_3_raw_offset_curve_aware_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-26-25__te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=132-val_mae=0.00358121.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012835`
- val_mae: `0.003581`
- val_rmse: `0.004427`
- val_pointwise_loss: `0.010826`
- val_centered_curve_shape_loss: `0.006362`
- val_curve_offset_loss: `0.004464`
- val_curve_amplitude_loss: `0.047192`
- val_sparse_harmonic_shape_loss: `0.000151`
- val_structured_mae: `0.030716`
- val_structured_rmse: `0.037953`
- val_residual_offset_mean_abs: `0.031176`

## Test Metrics

- test_loss: `0.010943`
- test_mae: `0.003464`
- test_rmse: `0.004225`
- test_pointwise_loss: `0.008528`
- test_centered_curve_shape_loss: `0.003161`
- test_curve_offset_loss: `0.005367`
- test_curve_amplitude_loss: `0.020346`
- test_sparse_harmonic_shape_loss: `6.837832e-05`
- test_structured_mae: `0.034032`
- test_structured_rmse: `0.041179`
- test_residual_offset_mean_abs: `0.034781`

## Interpretation

The held-out val error stayed finite with MAE=0.003581 deg and RMSE=0.004427 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003464 deg and RMSE=0.004225 deg, which indicates a numerically stable baseline run.
