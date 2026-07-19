# Wave4 1 Smooth L1 Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values`
- Model Family: `wave4_1_smooth_l1_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-54-21__te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=218-val_mae=0.00183482.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002416`
- val_mae: `0.001835`
- val_rmse: `0.002598`
- val_pointwise_loss: `0.002416`
- val_centered_curve_shape_loss: `0.004505`
- val_curve_offset_loss: `0.000328`
- val_curve_amplitude_loss: `0.034889`
- val_sparse_harmonic_shape_loss: `9.965653e-05`
- val_structured_mae: `0.007870`
- val_structured_rmse: `0.009414`
- val_residual_offset_mean_abs: `0.007594`

## Test Metrics

- test_loss: `0.002812`
- test_mae: `0.001956`
- test_rmse: `0.002999`
- test_pointwise_loss: `0.002812`
- test_centered_curve_shape_loss: `0.005318`
- test_curve_offset_loss: `0.000306`
- test_curve_amplitude_loss: `0.040047`
- test_sparse_harmonic_shape_loss: `0.000109`
- test_structured_mae: `0.008193`
- test_structured_rmse: `0.009984`
- test_residual_offset_mean_abs: `0.007884`

## Interpretation

The held-out val error stayed finite with MAE=0.001835 deg and RMSE=0.002598 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001956 deg and RMSE=0.002999 deg, which indicates a numerically stable baseline run.
