# Wave3 2 Harmonic Residual Offset Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_bw__polished_actual_values`
- Model Family: `wave3_2_harmonic_residual_offset_bw`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-06-13-40__te_wave3_2_harmonic_residual_offset_bw__polished_actual_values/checkpoints/harmonic_residual_offset_probe-epoch=205-val_mae=0.00185299.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004880`
- val_mae: `0.001853`
- val_rmse: `0.002611`
- val_pointwise_loss: `0.004880`
- val_centered_curve_shape_loss: `0.004509`
- val_curve_offset_loss: `0.000371`
- val_curve_amplitude_loss: `0.034905`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.009592`
- val_structured_rmse: `0.011665`
- val_residual_offset_mean_abs: `0.009320`

## Test Metrics

- test_loss: `0.005672`
- test_mae: `0.001969`
- test_rmse: `0.003011`
- test_pointwise_loss: `0.005672`
- test_centered_curve_shape_loss: `0.005294`
- test_curve_offset_loss: `0.000378`
- test_curve_amplitude_loss: `0.039560`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.010088`
- test_structured_rmse: `0.012363`
- test_residual_offset_mean_abs: `0.009756`

## Interpretation

The held-out val error stayed finite with MAE=0.001853 deg and RMSE=0.002611 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001969 deg and RMSE=0.003011 deg, which indicates a numerically stable baseline run.
