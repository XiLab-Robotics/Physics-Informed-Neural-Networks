# Wave3 3 Raw Centered Shape Curve Aware Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-20-41-54__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=186-val_mae=0.00185514.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006436`
- val_mae: `0.001855`
- val_rmse: `0.002611`
- val_pointwise_loss: `0.004844`
- val_centered_curve_shape_loss: `0.004506`
- val_curve_offset_loss: `0.000338`
- val_curve_amplitude_loss: `0.034151`
- val_sparse_harmonic_shape_loss: `9.965147e-05`
- val_structured_mae: `0.012078`
- val_structured_rmse: `0.013694`
- val_residual_offset_mean_abs: `0.011797`

## Test Metrics

- test_loss: `0.007512`
- test_mae: `0.001987`
- test_rmse: `0.003023`
- test_pointwise_loss: `0.005666`
- test_centered_curve_shape_loss: `0.005229`
- test_curve_offset_loss: `0.000437`
- test_curve_amplitude_loss: `0.038407`
- test_sparse_harmonic_shape_loss: `0.000108`
- test_structured_mae: `0.012103`
- test_structured_rmse: `0.014508`
- test_residual_offset_mean_abs: `0.011806`

## Interpretation

The held-out val error stayed finite with MAE=0.001855 deg and RMSE=0.002611 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001987 deg and RMSE=0.003023 deg, which indicates a numerically stable baseline run.
