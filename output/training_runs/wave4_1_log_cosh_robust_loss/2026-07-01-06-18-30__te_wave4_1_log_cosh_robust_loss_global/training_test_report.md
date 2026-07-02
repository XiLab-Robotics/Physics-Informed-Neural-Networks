# Wave4 1 Log Cosh Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_global`
- Model Family: `wave4_1_log_cosh_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-01-06-18-30__te_wave4_1_log_cosh_robust_loss_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=154-val_mae=0.00177642.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002386`
- val_mae: `0.001776`
- val_rmse: `0.002190`
- val_pointwise_loss: `0.002386`
- val_centered_curve_shape_loss: `0.004577`
- val_curve_offset_loss: `0.000287`
- val_curve_amplitude_loss: `0.037241`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.005268`
- val_structured_rmse: `0.005639`
- val_residual_offset_mean_abs: `0.004863`

## Test Metrics

- test_loss: `0.002785`
- test_mae: `0.001913`
- test_rmse: `0.002459`
- test_pointwise_loss: `0.002785`
- test_centered_curve_shape_loss: `0.005306`
- test_curve_offset_loss: `0.000370`
- test_curve_amplitude_loss: `0.042837`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.005390`
- test_structured_rmse: `0.005932`
- test_residual_offset_mean_abs: `0.004873`

## Interpretation

The held-out val error stayed finite with MAE=0.001776 deg and RMSE=0.002190 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001913 deg and RMSE=0.002459 deg, which indicates a numerically stable baseline run.
