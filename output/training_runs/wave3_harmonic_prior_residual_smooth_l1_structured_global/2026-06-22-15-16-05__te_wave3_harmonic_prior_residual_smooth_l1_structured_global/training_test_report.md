# Wave3 Harmonic Prior Residual Smooth L1 Structured Global Training And Testing Report

## Overview

- Run Name: `te_wave3_harmonic_prior_residual_smooth_l1_structured_global`
- Model Family: `wave3_harmonic_prior_residual_smooth_l1_structured_global`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_smooth_l1_structured_global\2026-06-22-15-16-05__te_wave3_harmonic_prior_residual_smooth_l1_structured_global\checkpoints\wave3_harmonic_prior_residual-epoch=043-val_mae=0.00188941.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002481`
- val_mae: `0.001889`
- val_rmse: `0.002320`
- val_pointwise_loss: `0.002481`
- val_centered_curve_shape_loss: `0.004586`
- val_curve_offset_loss: `0.000375`
- val_curve_amplitude_loss: `0.034845`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.008708`
- val_structured_rmse: `0.009083`

## Test Metrics

- test_loss: `0.004147`
- test_mae: `0.002168`
- test_rmse: `0.002763`
- test_pointwise_loss: `0.004147`
- test_centered_curve_shape_loss: `0.005531`
- test_curve_offset_loss: `0.002805`
- test_curve_amplitude_loss: `0.044154`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.008543`
- test_structured_rmse: `0.009067`

## Interpretation

The held-out val error stayed finite with MAE=0.001889 deg and RMSE=0.002320 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002168 deg and RMSE=0.002763 deg, which indicates a numerically stable baseline run.
