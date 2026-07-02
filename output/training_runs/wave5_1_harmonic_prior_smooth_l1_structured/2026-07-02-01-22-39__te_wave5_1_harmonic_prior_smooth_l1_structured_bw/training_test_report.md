# Wave5 1 Harmonic Prior Smooth L1 Structured Bw Training And Testing Report

## Overview

- Run Name: `te_wave5_1_harmonic_prior_smooth_l1_structured_bw`
- Model Family: `wave5_1_harmonic_prior_smooth_l1_structured_bw`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-02-01-22-39__te_wave5_1_harmonic_prior_smooth_l1_structured_bw\checkpoints\wave3_harmonic_prior_residual-epoch=080-val_mae=0.00192112.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002564`
- val_mae: `0.001921`
- val_rmse: `0.002355`
- val_pointwise_loss: `0.002564`
- val_centered_curve_shape_loss: `0.004654`
- val_curve_offset_loss: `0.000473`
- val_curve_amplitude_loss: `0.036761`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_structured_mae: `0.008541`
- val_structured_rmse: `0.008978`

## Test Metrics

- test_loss: `0.004196`
- test_mae: `0.002178`
- test_rmse: `0.002776`
- test_pointwise_loss: `0.004196`
- test_centered_curve_shape_loss: `0.005649`
- test_curve_offset_loss: `0.002767`
- test_curve_amplitude_loss: `0.048051`
- test_sparse_harmonic_shape_loss: `0.000115`
- test_structured_mae: `0.008336`
- test_structured_rmse: `0.008961`

## Interpretation

The held-out val error stayed finite with MAE=0.001921 deg and RMSE=0.002355 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002178 deg and RMSE=0.002776 deg, which indicates a numerically stable baseline run.
