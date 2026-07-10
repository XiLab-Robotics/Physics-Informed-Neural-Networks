# Wave3 1 Sequential Residual Offset Probe Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values`
- Model Family: `wave3_1_sequential_residual_offset_probe_bw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-11-35-18__te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=197-val_mae=0.00215382.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005758`
- val_mae: `0.002154`
- val_rmse: `0.002986`
- val_pointwise_loss: `0.005758`
- val_centered_curve_shape_loss: `0.005388`
- val_curve_offset_loss: `0.000370`
- val_curve_amplitude_loss: `0.057368`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.022167`
- val_base_rmse: `0.027188`
- val_residual_offset_mean_abs: `0.022041`

## Test Metrics

- test_loss: `0.006590`
- test_mae: `0.002262`
- test_rmse: `0.003326`
- test_pointwise_loss: `0.006590`
- test_centered_curve_shape_loss: `0.006211`
- test_curve_offset_loss: `0.000379`
- test_curve_amplitude_loss: `0.063368`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.021112`
- test_base_rmse: `0.026267`
- test_residual_offset_mean_abs: `0.020974`

## Interpretation

The held-out val error stayed finite with MAE=0.002154 deg and RMSE=0.002986 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002262 deg and RMSE=0.003326 deg, which indicates a numerically stable baseline run.
