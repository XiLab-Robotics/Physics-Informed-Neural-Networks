# Wave3 3 Curve Aware Pointwise Control Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_global`
- Model Family: `wave3_3_curve_aware_pointwise_control_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_curve_aware_pointwise_control\2026-06-30-20-13-16__te_wave3_3_curve_aware_pointwise_control_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=064-val_mae=0.00183684.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004947`
- val_mae: `0.001837`
- val_rmse: `0.002258`
- val_pointwise_loss: `0.004947`
- val_centered_curve_shape_loss: `0.004606`
- val_curve_offset_loss: `0.000341`
- val_curve_amplitude_loss: `0.034489`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.010386`
- val_structured_rmse: `0.010850`
- val_residual_offset_mean_abs: `0.009818`

## Test Metrics

- test_loss: `0.005814`
- test_mae: `0.001971`
- test_rmse: `0.002514`
- test_pointwise_loss: `0.005814`
- test_centered_curve_shape_loss: `0.005384`
- test_curve_offset_loss: `0.000430`
- test_curve_amplitude_loss: `0.039594`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_structured_mae: `0.010181`
- test_structured_rmse: `0.010813`
- test_residual_offset_mean_abs: `0.009606`

## Interpretation

The held-out val error stayed finite with MAE=0.001837 deg and RMSE=0.002258 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001971 deg and RMSE=0.002514 deg, which indicates a numerically stable baseline run.
