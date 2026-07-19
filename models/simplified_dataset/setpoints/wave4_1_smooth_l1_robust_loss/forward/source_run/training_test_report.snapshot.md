# Wave4 1 Smooth L1 Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints`
- Model Family: `wave4_1_smooth_l1_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-38-09__te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=086-val_mae=0.00353570.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005400`
- val_mae: `0.003536`
- val_rmse: `0.004407`
- val_pointwise_loss: `0.005400`
- val_centered_curve_shape_loss: `0.006464`
- val_curve_offset_loss: `0.004335`
- val_curve_amplitude_loss: `0.047343`
- val_sparse_harmonic_shape_loss: `0.000154`
- val_structured_mae: `0.026399`
- val_structured_rmse: `0.032509`
- val_residual_offset_mean_abs: `0.026540`

## Test Metrics

- test_loss: `0.004275`
- test_mae: `0.003411`
- test_rmse: `0.004234`
- test_pointwise_loss: `0.004275`
- test_centered_curve_shape_loss: `0.003234`
- test_curve_offset_loss: `0.005316`
- test_curve_amplitude_loss: `0.020570`
- test_sparse_harmonic_shape_loss: `7.048733e-05`
- test_structured_mae: `0.028148`
- test_structured_rmse: `0.034779`
- test_residual_offset_mean_abs: `0.028672`

## Interpretation

The held-out val error stayed finite with MAE=0.003536 deg and RMSE=0.004407 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003411 deg and RMSE=0.004234 deg, which indicates a numerically stable baseline run.
