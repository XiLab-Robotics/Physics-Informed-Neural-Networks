# Wave3 3 Curve Aware Pointwise Control Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values`
- Model Family: `wave3_3_curve_aware_pointwise_control_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-14-43-50__te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=175-val_mae=0.00184976.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004825`
- val_mae: `0.001850`
- val_rmse: `0.002602`
- val_pointwise_loss: `0.004825`
- val_centered_curve_shape_loss: `0.004479`
- val_curve_offset_loss: `0.000346`
- val_curve_amplitude_loss: `0.033533`
- val_sparse_harmonic_shape_loss: `9.882321e-05`
- val_structured_mae: `0.011695`
- val_structured_rmse: `0.014149`
- val_residual_offset_mean_abs: `0.011260`

## Test Metrics

- test_loss: `0.005683`
- test_mae: `0.001984`
- test_rmse: `0.003019`
- test_pointwise_loss: `0.005683`
- test_centered_curve_shape_loss: `0.005321`
- test_curve_offset_loss: `0.000362`
- test_curve_amplitude_loss: `0.037806`
- test_sparse_harmonic_shape_loss: `0.000107`
- test_structured_mae: `0.011936`
- test_structured_rmse: `0.014690`
- test_residual_offset_mean_abs: `0.011495`

## Interpretation

The held-out val error stayed finite with MAE=0.001850 deg and RMSE=0.002602 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001984 deg and RMSE=0.003019 deg, which indicates a numerically stable baseline run.
