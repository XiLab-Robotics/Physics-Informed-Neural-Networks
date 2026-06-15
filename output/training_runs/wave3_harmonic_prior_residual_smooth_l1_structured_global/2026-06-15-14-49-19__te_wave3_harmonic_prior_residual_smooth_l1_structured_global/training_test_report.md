# Wave3 Harmonic Prior Residual Smooth L1 Structured Global Training And Testing Report

## Overview

- Run Name: `te_wave3_harmonic_prior_residual_smooth_l1_structured_global`
- Model Family: `wave3_harmonic_prior_residual_smooth_l1_structured_global`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_smooth_l1_structured_global\2026-06-15-14-49-19__te_wave3_harmonic_prior_residual_smooth_l1_structured_global\checkpoints\wave3_harmonic_prior_residual-epoch=050-val_mae=0.00363290.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005323`
- val_mae: `0.003633`
- val_rmse: `0.004121`
- val_pointwise_loss: `0.005323`
- val_centered_curve_shape_loss: `0.006365`
- val_curve_offset_loss: `0.004281`
- val_curve_amplitude_loss: `0.048201`
- val_sparse_harmonic_shape_loss: `0.000151`
- val_structured_mae: `0.020979`
- val_structured_rmse: `0.022191`

## Test Metrics

- test_loss: `0.004022`
- test_mae: `0.003403`
- test_rmse: `0.003785`
- test_pointwise_loss: `0.004022`
- test_centered_curve_shape_loss: `0.003199`
- test_curve_offset_loss: `0.004846`
- test_curve_amplitude_loss: `0.021201`
- test_sparse_harmonic_shape_loss: `6.943693e-05`
- test_structured_mae: `0.023431`
- test_structured_rmse: `0.024612`

## Interpretation

The held-out val error stayed finite with MAE=0.003633 deg and RMSE=0.004121 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003403 deg and RMSE=0.003785 deg, which indicates a numerically stable baseline run.
