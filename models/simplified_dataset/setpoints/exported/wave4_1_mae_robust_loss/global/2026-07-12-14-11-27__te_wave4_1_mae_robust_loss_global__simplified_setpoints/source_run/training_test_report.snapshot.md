# Wave4 1 Mae Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_global__simplified_setpoints`
- Model Family: `wave4_1_mae_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-11-27__te_wave4_1_mae_robust_loss_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=143-val_mae=0.00355510.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.076421`
- val_mae: `0.003555`
- val_rmse: `0.004428`
- val_pointwise_loss: `0.076421`
- val_centered_curve_shape_loss: `0.006540`
- val_curve_offset_loss: `0.004443`
- val_curve_amplitude_loss: `0.050481`
- val_sparse_harmonic_shape_loss: `0.000156`
- val_structured_mae: `0.041662`
- val_structured_rmse: `0.047576`
- val_residual_offset_mean_abs: `0.041812`

## Test Metrics

- test_loss: `0.074757`
- test_mae: `0.003478`
- test_rmse: `0.004271`
- test_pointwise_loss: `0.074757`
- test_centered_curve_shape_loss: `0.003229`
- test_curve_offset_loss: `0.005493`
- test_curve_amplitude_loss: `0.022147`
- test_sparse_harmonic_shape_loss: `7.038957e-05`
- test_structured_mae: `0.045623`
- test_structured_rmse: `0.050468`
- test_residual_offset_mean_abs: `0.046013`

## Interpretation

The held-out val error stayed finite with MAE=0.003555 deg and RMSE=0.004428 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003478 deg and RMSE=0.004271 deg, which indicates a numerically stable baseline run.
