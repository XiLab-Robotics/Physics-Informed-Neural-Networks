# Wave4 1 Log Cosh Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_bw__polished_setpoints`
- Model Family: `wave4_1_log_cosh_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-08-11-55__te_wave4_1_log_cosh_robust_loss_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=044-val_mae=0.00196637.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002522`
- val_mae: `0.001966`
- val_rmse: `0.002734`
- val_pointwise_loss: `0.002522`
- val_centered_curve_shape_loss: `0.004623`
- val_curve_offset_loss: `0.000504`
- val_curve_amplitude_loss: `0.031052`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.046375`
- val_structured_rmse: `0.051481`
- val_residual_offset_mean_abs: `0.046268`

## Test Metrics

- test_loss: `0.004134`
- test_mae: `0.002290`
- test_rmse: `0.003645`
- test_pointwise_loss: `0.004134`
- test_centered_curve_shape_loss: `0.005504`
- test_curve_offset_loss: `0.003162`
- test_curve_amplitude_loss: `0.041425`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.042694`
- test_structured_rmse: `0.048662`
- test_residual_offset_mean_abs: `0.042570`

## Interpretation

The held-out val error stayed finite with MAE=0.001966 deg and RMSE=0.002734 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002290 deg and RMSE=0.003645 deg, which indicates a numerically stable baseline run.
