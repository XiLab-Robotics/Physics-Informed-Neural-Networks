# Wave4 1 Log Cosh Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_bw`
- Model Family: `wave4_1_log_cosh_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_log_cosh_robust_loss\2026-07-01-07-40-32__te_wave4_1_log_cosh_robust_loss_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=191-val_mae=0.00176554.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002368`
- val_mae: `0.001766`
- val_rmse: `0.002179`
- val_pointwise_loss: `0.002368`
- val_centered_curve_shape_loss: `0.004571`
- val_curve_offset_loss: `0.000256`
- val_curve_amplitude_loss: `0.036098`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.006320`
- val_structured_rmse: `0.006757`
- val_residual_offset_mean_abs: `0.005867`

## Test Metrics

- test_loss: `0.002752`
- test_mae: `0.001899`
- test_rmse: `0.002442`
- test_pointwise_loss: `0.002752`
- test_centered_curve_shape_loss: `0.005370`
- test_curve_offset_loss: `0.000239`
- test_curve_amplitude_loss: `0.041139`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.006113`
- test_structured_rmse: `0.006758`
- test_residual_offset_mean_abs: `0.005565`

## Interpretation

The held-out val error stayed finite with MAE=0.001766 deg and RMSE=0.002179 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001899 deg and RMSE=0.002442 deg, which indicates a numerically stable baseline run.
