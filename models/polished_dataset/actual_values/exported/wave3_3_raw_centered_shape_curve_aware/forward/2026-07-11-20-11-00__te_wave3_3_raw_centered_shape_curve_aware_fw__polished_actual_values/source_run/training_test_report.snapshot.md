# Wave3 3 Raw Centered Shape Curve Aware Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-11-00__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=095-val_mae=0.00193478.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006553`
- val_mae: `0.001935`
- val_rmse: `0.002699`
- val_pointwise_loss: `0.004963`
- val_centered_curve_shape_loss: `0.004500`
- val_curve_offset_loss: `0.000463`
- val_curve_amplitude_loss: `0.034023`
- val_sparse_harmonic_shape_loss: `9.927749e-05`
- val_structured_mae: `0.028647`
- val_structured_rmse: `0.032537`
- val_residual_offset_mean_abs: `0.028841`

## Test Metrics

- test_loss: `0.007790`
- test_mae: `0.002074`
- test_rmse: `0.003111`
- test_pointwise_loss: `0.005906`
- test_centered_curve_shape_loss: `0.005337`
- test_curve_offset_loss: `0.000569`
- test_curve_amplitude_loss: `0.038166`
- test_sparse_harmonic_shape_loss: `0.000107`
- test_structured_mae: `0.027632`
- test_structured_rmse: `0.031675`
- test_residual_offset_mean_abs: `0.027801`

## Interpretation

The held-out val error stayed finite with MAE=0.001935 deg and RMSE=0.002699 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002074 deg and RMSE=0.003111 deg, which indicates a numerically stable baseline run.
