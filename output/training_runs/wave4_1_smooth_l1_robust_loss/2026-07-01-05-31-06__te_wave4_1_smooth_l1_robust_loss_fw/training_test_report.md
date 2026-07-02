# Wave4 1 Smooth L1 Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_smooth_l1_robust_loss_fw`
- Model Family: `wave4_1_smooth_l1_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_smooth_l1_robust_loss\2026-07-01-05-31-06__te_wave4_1_smooth_l1_robust_loss_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=082-val_mae=0.00184069.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002470`
- val_mae: `0.001841`
- val_rmse: `0.002270`
- val_pointwise_loss: `0.002470`
- val_centered_curve_shape_loss: `0.004563`
- val_curve_offset_loss: `0.000377`
- val_curve_amplitude_loss: `0.035150`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.008792`
- val_structured_rmse: `0.009191`
- val_residual_offset_mean_abs: `0.008837`

## Test Metrics

- test_loss: `0.002906`
- test_mae: `0.001986`
- test_rmse: `0.002536`
- test_pointwise_loss: `0.002906`
- test_centered_curve_shape_loss: `0.005319`
- test_curve_offset_loss: `0.000494`
- test_curve_amplitude_loss: `0.040451`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.009232`
- test_structured_rmse: `0.009751`
- test_residual_offset_mean_abs: `0.009143`

## Interpretation

The held-out val error stayed finite with MAE=0.001841 deg and RMSE=0.002270 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001986 deg and RMSE=0.002536 deg, which indicates a numerically stable baseline run.
