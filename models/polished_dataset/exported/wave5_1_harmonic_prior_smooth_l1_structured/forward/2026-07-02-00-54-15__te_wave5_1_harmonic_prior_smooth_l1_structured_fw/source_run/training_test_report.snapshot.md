# Wave5 1 Harmonic Prior Smooth L1 Structured Fw Training And Testing Report

## Overview

- Run Name: `te_wave5_1_harmonic_prior_smooth_l1_structured_fw`
- Model Family: `wave5_1_harmonic_prior_smooth_l1_structured_fw`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-02-00-54-15__te_wave5_1_harmonic_prior_smooth_l1_structured_fw\checkpoints\wave3_harmonic_prior_residual-epoch=073-val_mae=0.00191209.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002499`
- val_mae: `0.001912`
- val_rmse: `0.002344`
- val_pointwise_loss: `0.002499`
- val_centered_curve_shape_loss: `0.004577`
- val_curve_offset_loss: `0.000420`
- val_curve_amplitude_loss: `0.033724`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.006768`
- val_structured_rmse: `0.007182`

## Test Metrics

- test_loss: `0.004101`
- test_mae: `0.002151`
- test_rmse: `0.002745`
- test_pointwise_loss: `0.004101`
- test_centered_curve_shape_loss: `0.005428`
- test_curve_offset_loss: `0.002794`
- test_curve_amplitude_loss: `0.043507`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.006636`
- test_structured_rmse: `0.007249`

## Interpretation

The held-out val error stayed finite with MAE=0.001912 deg and RMSE=0.002344 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002151 deg and RMSE=0.002745 deg, which indicates a numerically stable baseline run.
