# Wave4 1 Smooth L1 Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_smooth_l1_robust_loss_bw`
- Model Family: `wave4_1_smooth_l1_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_smooth_l1_robust_loss\2026-07-01-05-54-19__te_wave4_1_smooth_l1_robust_loss_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=083-val_mae=0.00185081.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002470`
- val_mae: `0.001851`
- val_rmse: `0.002284`
- val_pointwise_loss: `0.002470`
- val_centered_curve_shape_loss: `0.004570`
- val_curve_offset_loss: `0.000370`
- val_curve_amplitude_loss: `0.036590`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.006528`
- val_structured_rmse: `0.006954`
- val_residual_offset_mean_abs: `0.006211`

## Test Metrics

- test_loss: `0.002854`
- test_mae: `0.001968`
- test_rmse: `0.002515`
- test_pointwise_loss: `0.002854`
- test_centered_curve_shape_loss: `0.005413`
- test_curve_offset_loss: `0.000294`
- test_curve_amplitude_loss: `0.041621`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.006988`
- test_structured_rmse: `0.007493`
- test_residual_offset_mean_abs: `0.006588`

## Interpretation

The held-out val error stayed finite with MAE=0.001851 deg and RMSE=0.002284 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001968 deg and RMSE=0.002515 deg, which indicates a numerically stable baseline run.
