# Wave4 1 Mae Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_bw`
- Model Family: `wave4_1_mae_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_mae_robust_loss\2026-07-01-04-16-28__te_wave4_1_mae_robust_loss_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=170-val_mae=0.00175748.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.037756`
- val_mae: `0.001757`
- val_rmse: `0.002173`
- val_pointwise_loss: `0.037756`
- val_centered_curve_shape_loss: `0.004614`
- val_curve_offset_loss: `0.000275`
- val_curve_amplitude_loss: `0.038080`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_structured_mae: `0.006507`
- val_structured_rmse: `0.006924`
- val_residual_offset_mean_abs: `0.006196`

## Test Metrics

- test_loss: `0.040978`
- test_mae: `0.001907`
- test_rmse: `0.002455`
- test_pointwise_loss: `0.040978`
- test_centered_curve_shape_loss: `0.005483`
- test_curve_offset_loss: `0.000253`
- test_curve_amplitude_loss: `0.044135`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_structured_mae: `0.006883`
- test_structured_rmse: `0.007463`
- test_residual_offset_mean_abs: `0.006458`

## Interpretation

The held-out val error stayed finite with MAE=0.001757 deg and RMSE=0.002173 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001907 deg and RMSE=0.002455 deg, which indicates a numerically stable baseline run.
