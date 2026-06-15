# Wave3 Harmonic Prior Residual Smooth L1 Structured Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_harmonic_prior_residual_smooth_l1_structured_fw`
- Model Family: `wave3_harmonic_prior_residual_smooth_l1_structured_fw`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_smooth_l1_structured_fw\2026-06-15-15-08-57__te_wave3_harmonic_prior_residual_smooth_l1_structured_fw\checkpoints\wave3_harmonic_prior_residual-epoch=016-val_mae=0.00331004.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.016269`
- val_mae: `0.003310`
- val_rmse: `0.003814`
- val_pointwise_loss: `0.016269`
- val_centered_curve_shape_loss: `0.015257`
- val_curve_offset_loss: `0.017281`
- val_curve_amplitude_loss: `0.104812`
- val_sparse_harmonic_shape_loss: `0.000332`
- val_structured_mae: `0.018792`
- val_structured_rmse: `0.020655`

## Test Metrics

- test_loss: `0.015324`
- test_mae: `0.003527`
- test_rmse: `0.003900`
- test_pointwise_loss: `0.015324`
- test_centered_curve_shape_loss: `0.007884`
- test_curve_offset_loss: `0.022765`
- test_curve_amplitude_loss: `0.041342`
- test_sparse_harmonic_shape_loss: `0.000146`
- test_structured_mae: `0.020145`
- test_structured_rmse: `0.022202`

## Interpretation

The held-out val error stayed finite with MAE=0.003310 deg and RMSE=0.003814 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003527 deg and RMSE=0.003900 deg, which indicates a numerically stable baseline run.
