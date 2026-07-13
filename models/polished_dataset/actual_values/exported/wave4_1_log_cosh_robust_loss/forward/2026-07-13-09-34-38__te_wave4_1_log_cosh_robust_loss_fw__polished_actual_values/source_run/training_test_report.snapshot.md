# Wave4 1 Log Cosh Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values`
- Model Family: `wave4_1_log_cosh_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-09-34-38__te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=193-val_mae=0.00182691.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002361`
- val_mae: `0.001827`
- val_rmse: `0.002586`
- val_pointwise_loss: `0.002361`
- val_centered_curve_shape_loss: `0.004486`
- val_curve_offset_loss: `0.000318`
- val_curve_amplitude_loss: `0.034249`
- val_sparse_harmonic_shape_loss: `9.911907e-05`
- val_structured_mae: `0.006936`
- val_structured_rmse: `0.008388`
- val_residual_offset_mean_abs: `0.006516`

## Test Metrics

- test_loss: `0.002763`
- test_mae: `0.001955`
- test_rmse: `0.002994`
- test_pointwise_loss: `0.002763`
- test_centered_curve_shape_loss: `0.005271`
- test_curve_offset_loss: `0.000355`
- test_curve_amplitude_loss: `0.038877`
- test_sparse_harmonic_shape_loss: `0.000108`
- test_structured_mae: `0.007273`
- test_structured_rmse: `0.009029`
- test_residual_offset_mean_abs: `0.006635`

## Interpretation

The held-out val error stayed finite with MAE=0.001827 deg and RMSE=0.002586 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001955 deg and RMSE=0.002994 deg, which indicates a numerically stable baseline run.
