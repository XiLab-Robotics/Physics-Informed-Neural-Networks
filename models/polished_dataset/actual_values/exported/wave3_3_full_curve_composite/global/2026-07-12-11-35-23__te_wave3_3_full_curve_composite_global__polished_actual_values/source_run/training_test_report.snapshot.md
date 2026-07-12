# Wave3 3 Full Curve Composite Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_global__polished_actual_values`
- Model Family: `wave3_3_full_curve_composite_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-11-35-23__te_wave3_3_full_curve_composite_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=131-val_mae=0.00200797.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008341`
- val_mae: `0.002008`
- val_rmse: `0.002796`
- val_pointwise_loss: `0.005219`
- val_centered_curve_shape_loss: `0.004825`
- val_curve_offset_loss: `0.000393`
- val_curve_amplitude_loss: `0.017628`
- val_sparse_harmonic_shape_loss: `0.000106`
- val_structured_mae: `0.018212`
- val_structured_rmse: `0.021403`
- val_residual_offset_mean_abs: `0.018153`

## Test Metrics

- test_loss: `0.009715`
- test_mae: `0.002169`
- test_rmse: `0.003232`
- test_pointwise_loss: `0.006228`
- test_centered_curve_shape_loss: `0.005682`
- test_curve_offset_loss: `0.000547`
- test_curve_amplitude_loss: `0.018579`
- test_sparse_harmonic_shape_loss: `0.000114`
- test_structured_mae: `0.018566`
- test_structured_rmse: `0.022184`
- test_residual_offset_mean_abs: `0.018422`

## Interpretation

The held-out val error stayed finite with MAE=0.002008 deg and RMSE=0.002796 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002169 deg and RMSE=0.003232 deg, which indicates a numerically stable baseline run.
