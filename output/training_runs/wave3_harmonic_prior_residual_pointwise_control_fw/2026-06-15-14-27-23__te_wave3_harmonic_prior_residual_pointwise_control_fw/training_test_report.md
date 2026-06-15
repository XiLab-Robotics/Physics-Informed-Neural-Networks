# Wave3 Harmonic Prior Residual Pointwise Control Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_harmonic_prior_residual_pointwise_control_fw`
- Model Family: `wave3_harmonic_prior_residual_pointwise_control_fw`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_pointwise_control_fw\2026-06-15-14-27-23__te_wave3_harmonic_prior_residual_pointwise_control_fw\checkpoints\wave3_harmonic_prior_residual-epoch=013-val_mae=0.00331506.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.032866`
- val_mae: `0.003315`
- val_rmse: `0.003845`
- val_pointwise_loss: `0.032866`
- val_centered_curve_shape_loss: `0.015754`
- val_curve_offset_loss: `0.017112`
- val_curve_amplitude_loss: `0.101714`
- val_sparse_harmonic_shape_loss: `0.000342`
- val_structured_mae: `0.018768`
- val_structured_rmse: `0.020856`

## Test Metrics

- test_loss: `0.028910`
- test_mae: `0.003382`
- test_rmse: `0.003779`
- test_pointwise_loss: `0.028910`
- test_centered_curve_shape_loss: `0.008204`
- test_curve_offset_loss: `0.020706`
- test_curve_amplitude_loss: `0.038518`
- test_sparse_harmonic_shape_loss: `0.000152`
- test_structured_mae: `0.020047`
- test_structured_rmse: `0.022384`

## Interpretation

The held-out val error stayed finite with MAE=0.003315 deg and RMSE=0.003845 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003382 deg and RMSE=0.003779 deg, which indicates a numerically stable baseline run.
