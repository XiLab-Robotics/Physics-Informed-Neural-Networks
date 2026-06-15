# Wave3 Harmonic Prior Residual Pointwise Control Global Training And Testing Report

## Overview

- Run Name: `te_wave3_harmonic_prior_residual_pointwise_control_global`
- Model Family: `wave3_harmonic_prior_residual_pointwise_control_global`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_pointwise_control_global\2026-06-15-14-01-15__te_wave3_harmonic_prior_residual_pointwise_control_global\checkpoints\wave3_harmonic_prior_residual-epoch=085-val_mae=0.00361072.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010909`
- val_mae: `0.003611`
- val_rmse: `0.004118`
- val_pointwise_loss: `0.010909`
- val_centered_curve_shape_loss: `0.006367`
- val_curve_offset_loss: `0.004542`
- val_curve_amplitude_loss: `0.045520`
- val_sparse_harmonic_shape_loss: `0.000151`
- val_structured_mae: `0.023754`
- val_structured_rmse: `0.024681`

## Test Metrics

- test_loss: `0.008506`
- test_mae: `0.003451`
- test_rmse: `0.003851`
- test_pointwise_loss: `0.008506`
- test_centered_curve_shape_loss: `0.003220`
- test_curve_offset_loss: `0.005286`
- test_curve_amplitude_loss: `0.019362`
- test_sparse_harmonic_shape_loss: `7.002206e-05`
- test_structured_mae: `0.026762`
- test_structured_rmse: `0.027362`

## Interpretation

The held-out val error stayed finite with MAE=0.003611 deg and RMSE=0.004118 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003451 deg and RMSE=0.003851 deg, which indicates a numerically stable baseline run.
