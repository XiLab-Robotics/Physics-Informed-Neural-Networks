# Wave4 1 Mae Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_bw__polished_actual_values`
- Model Family: `wave4_1_mae_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-19-08-24__te_wave4_1_mae_robust_loss_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=173-val_mae=0.00178689.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.038388`
- val_mae: `0.001787`
- val_rmse: `0.002557`
- val_pointwise_loss: `0.038388`
- val_centered_curve_shape_loss: `0.004558`
- val_curve_offset_loss: `0.000321`
- val_curve_amplitude_loss: `0.036227`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.016627`
- val_structured_rmse: `0.019348`
- val_residual_offset_mean_abs: `0.016321`

## Test Metrics

- test_loss: `0.043241`
- test_mae: `0.002013`
- test_rmse: `0.003329`
- test_pointwise_loss: `0.043241`
- test_centered_curve_shape_loss: `0.005892`
- test_curve_offset_loss: `0.001585`
- test_curve_amplitude_loss: `0.042887`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.016613`
- test_structured_rmse: `0.020147`
- test_residual_offset_mean_abs: `0.016182`

## Interpretation

The held-out val error stayed finite with MAE=0.001787 deg and RMSE=0.002557 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002013 deg and RMSE=0.003329 deg, which indicates a numerically stable baseline run.
