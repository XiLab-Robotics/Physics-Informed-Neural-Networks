# Wave3 1 Sequential Residual Offset Probe Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_fw__polished_setpoints`
- Model Family: `wave3_1_sequential_residual_offset_probe_fw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-09-39-31__te_wave3_1_sequential_residual_offset_probe_fw__polished_setpoints/checkpoints/sequential_residual_offset_probe-epoch=111-val_mae=0.00217538.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005799`
- val_mae: `0.002175`
- val_rmse: `0.002996`
- val_pointwise_loss: `0.005799`
- val_centered_curve_shape_loss: `0.005358`
- val_curve_offset_loss: `0.000441`
- val_curve_amplitude_loss: `0.058172`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026300`
- val_base_rmse: `0.031067`
- val_residual_offset_mean_abs: `0.026169`

## Test Metrics

- test_loss: `0.009310`
- test_mae: `0.002465`
- test_rmse: `0.003849`
- test_pointwise_loss: `0.009310`
- test_centered_curve_shape_loss: `0.006272`
- test_curve_offset_loss: `0.003038`
- test_curve_amplitude_loss: `0.070586`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.024752`
- test_base_rmse: `0.029747`
- test_residual_offset_mean_abs: `0.024516`

## Interpretation

The held-out val error stayed finite with MAE=0.002175 deg and RMSE=0.002996 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002465 deg and RMSE=0.003849 deg, which indicates a numerically stable baseline run.
