# Wave5 1 Harmonic Prior Pointwise Control Fw Training And Testing Report

## Overview

- Run Name: `te_wave5_1_harmonic_prior_pointwise_control_fw`
- Model Family: `wave5_1_harmonic_prior_pointwise_control_fw`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-01-23-29-08__te_wave5_1_harmonic_prior_pointwise_control_fw\checkpoints\wave3_harmonic_prior_residual-epoch=058-val_mae=0.00191340.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005043`
- val_mae: `0.001913`
- val_rmse: `0.002343`
- val_pointwise_loss: `0.005043`
- val_centered_curve_shape_loss: `0.004587`
- val_curve_offset_loss: `0.000456`
- val_curve_amplitude_loss: `0.035055`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.008567`
- val_structured_rmse: `0.008953`

## Test Metrics

- test_loss: `0.008332`
- test_mae: `0.002185`
- test_rmse: `0.002776`
- test_pointwise_loss: `0.008332`
- test_centered_curve_shape_loss: `0.005512`
- test_curve_offset_loss: `0.002820`
- test_curve_amplitude_loss: `0.045218`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.008514`
- test_structured_rmse: `0.009032`

## Interpretation

The held-out val error stayed finite with MAE=0.001913 deg and RMSE=0.002343 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002185 deg and RMSE=0.002776 deg, which indicates a numerically stable baseline run.
