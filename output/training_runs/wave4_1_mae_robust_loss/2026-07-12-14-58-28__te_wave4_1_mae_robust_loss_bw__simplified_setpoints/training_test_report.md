# Wave4 1 Mae Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_bw__simplified_setpoints`
- Model Family: `wave4_1_mae_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-58-28__te_wave4_1_mae_robust_loss_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=073-val_mae=0.00358581.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.077081`
- val_mae: `0.003586`
- val_rmse: `0.004455`
- val_pointwise_loss: `0.077081`
- val_centered_curve_shape_loss: `0.006490`
- val_curve_offset_loss: `0.004489`
- val_curve_amplitude_loss: `0.048390`
- val_sparse_harmonic_shape_loss: `0.000154`
- val_structured_mae: `0.025515`
- val_structured_rmse: `0.032064`
- val_residual_offset_mean_abs: `0.025464`

## Test Metrics

- test_loss: `0.075493`
- test_mae: `0.003512`
- test_rmse: `0.004289`
- test_pointwise_loss: `0.075493`
- test_centered_curve_shape_loss: `0.003210`
- test_curve_offset_loss: `0.005590`
- test_curve_amplitude_loss: `0.020295`
- test_sparse_harmonic_shape_loss: `6.977223e-05`
- test_structured_mae: `0.028753`
- test_structured_rmse: `0.034966`
- test_residual_offset_mean_abs: `0.029113`

## Interpretation

The held-out val error stayed finite with MAE=0.003586 deg and RMSE=0.004455 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003512 deg and RMSE=0.004289 deg, which indicates a numerically stable baseline run.
