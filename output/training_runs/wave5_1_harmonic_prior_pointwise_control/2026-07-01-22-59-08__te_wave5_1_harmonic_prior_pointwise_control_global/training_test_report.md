# Wave5 1 Harmonic Prior Pointwise Control Global Training And Testing Report

## Overview

- Run Name: `te_wave5_1_harmonic_prior_pointwise_control_global`
- Model Family: `wave5_1_harmonic_prior_pointwise_control_global`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-01-22-59-08__te_wave5_1_harmonic_prior_pointwise_control_global\checkpoints\wave3_harmonic_prior_residual-epoch=080-val_mae=0.00189408.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005072`
- val_mae: `0.001894`
- val_rmse: `0.002321`
- val_pointwise_loss: `0.005072`
- val_centered_curve_shape_loss: `0.004627`
- val_curve_offset_loss: `0.000445`
- val_curve_amplitude_loss: `0.037407`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_structured_mae: `0.008586`
- val_structured_rmse: `0.009019`

## Test Metrics

- test_loss: `0.008499`
- test_mae: `0.002159`
- test_rmse: `0.002754`
- test_pointwise_loss: `0.008499`
- test_centered_curve_shape_loss: `0.005585`
- test_curve_offset_loss: `0.002914`
- test_curve_amplitude_loss: `0.048125`
- test_sparse_harmonic_shape_loss: `0.000113`
- test_structured_mae: `0.009013`
- test_structured_rmse: `0.009534`

## Interpretation

The held-out val error stayed finite with MAE=0.001894 deg and RMSE=0.002321 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002159 deg and RMSE=0.002754 deg, which indicates a numerically stable baseline run.
