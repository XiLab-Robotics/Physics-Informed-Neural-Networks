# Wave4 1 Mae Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_fw`
- Model Family: `wave4_1_mae_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_mae_robust_loss\2026-07-01-03-49-36__te_wave4_1_mae_robust_loss_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=061-val_mae=0.00180646.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.038808`
- val_mae: `0.001806`
- val_rmse: `0.002229`
- val_pointwise_loss: `0.038808`
- val_centered_curve_shape_loss: `0.004641`
- val_curve_offset_loss: `0.000337`
- val_curve_amplitude_loss: `0.036792`
- val_sparse_harmonic_shape_loss: `0.000104`
- val_structured_mae: `0.010354`
- val_structured_rmse: `0.011175`
- val_residual_offset_mean_abs: `0.009841`

## Test Metrics

- test_loss: `0.042118`
- test_mae: `0.001961`
- test_rmse: `0.002502`
- test_pointwise_loss: `0.042118`
- test_centered_curve_shape_loss: `0.005399`
- test_curve_offset_loss: `0.000520`
- test_curve_amplitude_loss: `0.042323`
- test_sparse_harmonic_shape_loss: `0.000113`
- test_structured_mae: `0.010351`
- test_structured_rmse: `0.011375`
- test_residual_offset_mean_abs: `0.009748`

## Interpretation

The held-out val error stayed finite with MAE=0.001806 deg and RMSE=0.002229 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001961 deg and RMSE=0.002502 deg, which indicates a numerically stable baseline run.
