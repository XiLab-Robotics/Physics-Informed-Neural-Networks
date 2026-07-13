# Wave4 1 Log Cosh Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values`
- Model Family: `wave4_1_log_cosh_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-10-23-44__te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=127-val_mae=0.00187102.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002398`
- val_mae: `0.001871`
- val_rmse: `0.002636`
- val_pointwise_loss: `0.002398`
- val_centered_curve_shape_loss: `0.004493`
- val_curve_offset_loss: `0.000384`
- val_curve_amplitude_loss: `0.034431`
- val_sparse_harmonic_shape_loss: `9.929178e-05`
- val_structured_mae: `0.010409`
- val_structured_rmse: `0.012212`
- val_residual_offset_mean_abs: `0.009859`

## Test Metrics

- test_loss: `0.002843`
- test_mae: `0.001995`
- test_rmse: `0.003057`
- test_pointwise_loss: `0.002843`
- test_centered_curve_shape_loss: `0.005337`
- test_curve_offset_loss: `0.000449`
- test_curve_amplitude_loss: `0.038639`
- test_sparse_harmonic_shape_loss: `0.000107`
- test_structured_mae: `0.010073`
- test_structured_rmse: `0.012363`
- test_residual_offset_mean_abs: `0.009397`

## Interpretation

The held-out val error stayed finite with MAE=0.001871 deg and RMSE=0.002636 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001995 deg and RMSE=0.003057 deg, which indicates a numerically stable baseline run.
