# Wave3 3 Raw Offset Curve Aware Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_global__polished_actual_values`
- Model Family: `wave3_3_raw_offset_curve_aware_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-12-01-40-59__te_wave3_3_raw_offset_curve_aware_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=155-val_mae=0.00187021.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005037`
- val_mae: `0.001870`
- val_rmse: `0.002625`
- val_pointwise_loss: `0.004874`
- val_centered_curve_shape_loss: `0.004513`
- val_curve_offset_loss: `0.000362`
- val_curve_amplitude_loss: `0.033771`
- val_sparse_harmonic_shape_loss: `9.964712e-05`
- val_structured_mae: `0.025036`
- val_structured_rmse: `0.030101`
- val_residual_offset_mean_abs: `0.025103`

## Test Metrics

- test_loss: `0.005872`
- test_mae: `0.002001`
- test_rmse: `0.003029`
- test_pointwise_loss: `0.005712`
- test_centered_curve_shape_loss: `0.005355`
- test_curve_offset_loss: `0.000357`
- test_curve_amplitude_loss: `0.038109`
- test_sparse_harmonic_shape_loss: `0.000108`
- test_structured_mae: `0.024653`
- test_structured_rmse: `0.029855`
- test_residual_offset_mean_abs: `0.024701`

## Interpretation

The held-out val error stayed finite with MAE=0.001870 deg and RMSE=0.002625 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002001 deg and RMSE=0.003029 deg, which indicates a numerically stable baseline run.
