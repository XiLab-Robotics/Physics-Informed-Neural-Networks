# Wave3 3 Raw Offset Curve Aware Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_global__polished_setpoints`
- Model Family: `wave3_3_raw_offset_curve_aware_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-23-47-11__te_wave3_3_raw_offset_curve_aware_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=122-val_mae=0.00189514.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005234`
- val_mae: `0.001895`
- val_rmse: `0.002654`
- val_pointwise_loss: `0.005023`
- val_centered_curve_shape_loss: `0.004556`
- val_curve_offset_loss: `0.000468`
- val_curve_amplitude_loss: `0.032837`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.026622`
- val_structured_rmse: `0.031273`
- val_residual_offset_mean_abs: `0.026555`

## Test Metrics

- test_loss: `0.009664`
- test_mae: `0.002203`
- test_rmse: `0.003560`
- test_pointwise_loss: `0.008355`
- test_centered_curve_shape_loss: `0.005446`
- test_curve_offset_loss: `0.002909`
- test_curve_amplitude_loss: `0.043017`
- test_sparse_harmonic_shape_loss: `0.000109`
- test_structured_mae: `0.025817`
- test_structured_rmse: `0.030932`
- test_residual_offset_mean_abs: `0.025472`

## Interpretation

The held-out val error stayed finite with MAE=0.001895 deg and RMSE=0.002654 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002203 deg and RMSE=0.003560 deg, which indicates a numerically stable baseline run.
