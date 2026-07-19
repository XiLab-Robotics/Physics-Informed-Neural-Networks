# Wave4 1 Mae Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_fw__polished_actual_values`
- Model Family: `wave4_1_mae_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-18-19-09__te_wave4_1_mae_robust_loss_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=202-val_mae=0.00173420.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.037256`
- val_mae: `0.001734`
- val_rmse: `0.002512`
- val_pointwise_loss: `0.037256`
- val_centered_curve_shape_loss: `0.004580`
- val_curve_offset_loss: `0.000247`
- val_curve_amplitude_loss: `0.038221`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.006549`
- val_structured_rmse: `0.007078`
- val_residual_offset_mean_abs: `0.006365`

## Test Metrics

- test_loss: `0.043191`
- test_mae: `0.002010`
- test_rmse: `0.003415`
- test_pointwise_loss: `0.043191`
- test_centered_curve_shape_loss: `0.005711`
- test_curve_offset_loss: `0.002673`
- test_curve_amplitude_loss: `0.047890`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_structured_mae: `0.006664`
- test_structured_rmse: `0.007620`
- test_residual_offset_mean_abs: `0.006307`

## Interpretation

The held-out val error stayed finite with MAE=0.001734 deg and RMSE=0.002512 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002010 deg and RMSE=0.003415 deg, which indicates a numerically stable baseline run.
