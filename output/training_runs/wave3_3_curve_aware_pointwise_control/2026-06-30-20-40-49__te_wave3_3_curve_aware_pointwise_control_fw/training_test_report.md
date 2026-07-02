# Wave3 3 Curve Aware Pointwise Control Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_fw`
- Model Family: `wave3_3_curve_aware_pointwise_control_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_curve_aware_pointwise_control\2026-06-30-20-40-49__te_wave3_3_curve_aware_pointwise_control_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=119-val_mae=0.00179175.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004858`
- val_mae: `0.001792`
- val_rmse: `0.002208`
- val_pointwise_loss: `0.004858`
- val_centered_curve_shape_loss: `0.004591`
- val_curve_offset_loss: `0.000267`
- val_curve_amplitude_loss: `0.036942`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.005876`
- val_structured_rmse: `0.006298`
- val_residual_offset_mean_abs: `0.005608`

## Test Metrics

- test_loss: `0.005675`
- test_mae: `0.001919`
- test_rmse: `0.002463`
- test_pointwise_loss: `0.005675`
- test_centered_curve_shape_loss: `0.005295`
- test_curve_offset_loss: `0.000380`
- test_curve_amplitude_loss: `0.041854`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.005678`
- test_structured_rmse: `0.006319`
- test_residual_offset_mean_abs: `0.005249`

## Interpretation

The held-out val error stayed finite with MAE=0.001792 deg and RMSE=0.002208 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001919 deg and RMSE=0.002463 deg, which indicates a numerically stable baseline run.
