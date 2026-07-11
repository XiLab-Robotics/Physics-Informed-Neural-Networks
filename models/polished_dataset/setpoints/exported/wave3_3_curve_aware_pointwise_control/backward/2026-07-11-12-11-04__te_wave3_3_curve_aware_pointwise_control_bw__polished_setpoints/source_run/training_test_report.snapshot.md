# Wave3 3 Curve Aware Pointwise Control Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_bw__polished_setpoints`
- Model Family: `wave3_3_curve_aware_pointwise_control_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-12-11-04__te_wave3_3_curve_aware_pointwise_control_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=130-val_mae=0.00195353.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005166`
- val_mae: `0.001954`
- val_rmse: `0.002727`
- val_pointwise_loss: `0.005166`
- val_centered_curve_shape_loss: `0.004612`
- val_curve_offset_loss: `0.000553`
- val_curve_amplitude_loss: `0.031768`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_structured_mae: `0.024580`
- val_structured_rmse: `0.028028`
- val_residual_offset_mean_abs: `0.024456`

## Test Metrics

- test_loss: `0.008504`
- test_mae: `0.002254`
- test_rmse: `0.003612`
- test_pointwise_loss: `0.008504`
- test_centered_curve_shape_loss: `0.005488`
- test_curve_offset_loss: `0.003016`
- test_curve_amplitude_loss: `0.041865`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.024725`
- test_structured_rmse: `0.027969`
- test_residual_offset_mean_abs: `0.024389`

## Interpretation

The held-out val error stayed finite with MAE=0.001954 deg and RMSE=0.002727 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002254 deg and RMSE=0.003612 deg, which indicates a numerically stable baseline run.
