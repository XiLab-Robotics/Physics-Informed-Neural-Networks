# Wave4 1 Log Cosh Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_global__polished_actual_values`
- Model Family: `wave4_1_log_cosh_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-01-50__te_wave4_1_log_cosh_robust_loss_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=110-val_mae=0.00189902.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002450`
- val_mae: `0.001899`
- val_rmse: `0.002661`
- val_pointwise_loss: `0.002450`
- val_centered_curve_shape_loss: `0.004515`
- val_curve_offset_loss: `0.000471`
- val_curve_amplitude_loss: `0.034157`
- val_sparse_harmonic_shape_loss: `9.992567e-05`
- val_structured_mae: `0.026089`
- val_structured_rmse: `0.030967`
- val_residual_offset_mean_abs: `0.025936`

## Test Metrics

- test_loss: `0.002897`
- test_mae: `0.002046`
- test_rmse: `0.003090`
- test_pointwise_loss: `0.002897`
- test_centered_curve_shape_loss: `0.005458`
- test_curve_offset_loss: `0.000437`
- test_curve_amplitude_loss: `0.039340`
- test_sparse_harmonic_shape_loss: `0.000109`
- test_structured_mae: `0.024790`
- test_structured_rmse: `0.030011`
- test_residual_offset_mean_abs: `0.024696`

## Interpretation

The held-out val error stayed finite with MAE=0.001899 deg and RMSE=0.002661 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002046 deg and RMSE=0.003090 deg, which indicates a numerically stable baseline run.
