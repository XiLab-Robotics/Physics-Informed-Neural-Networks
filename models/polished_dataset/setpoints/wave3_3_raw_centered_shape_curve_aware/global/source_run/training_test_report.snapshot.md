# Wave3 3 Raw Centered Shape Curve Aware Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-17-26-29__te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=112-val_mae=0.00195150.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006710`
- val_mae: `0.001951`
- val_rmse: `0.002721`
- val_pointwise_loss: `0.005083`
- val_centered_curve_shape_loss: `0.004603`
- val_curve_offset_loss: `0.000480`
- val_curve_amplitude_loss: `0.033522`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.028264`
- val_structured_rmse: `0.032724`
- val_residual_offset_mean_abs: `0.028065`

## Test Metrics

- test_loss: `0.010505`
- test_mae: `0.002271`
- test_rmse: `0.003605`
- test_pointwise_loss: `0.008563`
- test_centered_curve_shape_loss: `0.005500`
- test_curve_offset_loss: `0.003063`
- test_curve_amplitude_loss: `0.044319`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.025881`
- test_structured_rmse: `0.030672`
- test_residual_offset_mean_abs: `0.025529`

## Interpretation

The held-out val error stayed finite with MAE=0.001951 deg and RMSE=0.002721 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002271 deg and RMSE=0.003605 deg, which indicates a numerically stable baseline run.
