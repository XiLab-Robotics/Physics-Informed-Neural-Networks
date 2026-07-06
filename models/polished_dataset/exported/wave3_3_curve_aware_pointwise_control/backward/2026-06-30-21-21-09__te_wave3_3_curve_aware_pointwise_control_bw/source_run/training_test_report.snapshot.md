# Wave3 3 Curve Aware Pointwise Control Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_bw`
- Model Family: `wave3_3_curve_aware_pointwise_control_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_curve_aware_pointwise_control\2026-06-30-21-21-09__te_wave3_3_curve_aware_pointwise_control_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=103-val_mae=0.00181463.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004871`
- val_mae: `0.001815`
- val_rmse: `0.002238`
- val_pointwise_loss: `0.004871`
- val_centered_curve_shape_loss: `0.004559`
- val_curve_offset_loss: `0.000312`
- val_curve_amplitude_loss: `0.034895`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.006344`
- val_structured_rmse: `0.006763`
- val_residual_offset_mean_abs: `0.005762`

## Test Metrics

- test_loss: `0.005586`
- test_mae: `0.001925`
- test_rmse: `0.002473`
- test_pointwise_loss: `0.005586`
- test_centered_curve_shape_loss: `0.005341`
- test_curve_offset_loss: `0.000245`
- test_curve_amplitude_loss: `0.039909`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.006257`
- test_structured_rmse: `0.006877`
- test_residual_offset_mean_abs: `0.005558`

## Interpretation

The held-out val error stayed finite with MAE=0.001815 deg and RMSE=0.002238 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001925 deg and RMSE=0.002473 deg, which indicates a numerically stable baseline run.
