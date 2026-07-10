# Wave3 1 Sequential Residual Offset Probe Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_bw__polished_setpoints`
- Model Family: `wave3_1_sequential_residual_offset_probe_bw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-10-05-23__te_wave3_1_sequential_residual_offset_probe_bw__polished_setpoints/checkpoints/sequential_residual_offset_probe-epoch=137-val_mae=0.00216898.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005801`
- val_mae: `0.002169`
- val_rmse: `0.002997`
- val_pointwise_loss: `0.005801`
- val_centered_curve_shape_loss: `0.005348`
- val_curve_offset_loss: `0.000453`
- val_curve_amplitude_loss: `0.059044`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.025502`
- val_base_rmse: `0.030200`
- val_residual_offset_mean_abs: `0.025411`

## Test Metrics

- test_loss: `0.009281`
- test_mae: `0.002450`
- test_rmse: `0.003838`
- test_pointwise_loss: `0.009281`
- test_centered_curve_shape_loss: `0.006261`
- test_curve_offset_loss: `0.003020`
- test_curve_amplitude_loss: `0.071519`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.024113`
- test_base_rmse: `0.028980`
- test_residual_offset_mean_abs: `0.023902`

## Interpretation

The held-out val error stayed finite with MAE=0.002169 deg and RMSE=0.002997 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002450 deg and RMSE=0.003838 deg, which indicates a numerically stable baseline run.
