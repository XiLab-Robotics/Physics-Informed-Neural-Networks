# Wave3 1 Sequential Residual Offset Probe Global Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints`
- Model Family: `wave3_1_sequential_residual_offset_probe_global`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-11-44__te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints/checkpoints/sequential_residual_offset_probe-epoch=095-val_mae=0.00372731.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011734`
- val_mae: `0.003727`
- val_rmse: `0.004647`
- val_pointwise_loss: `0.011734`
- val_centered_curve_shape_loss: `0.007308`
- val_curve_offset_loss: `0.004426`
- val_curve_amplitude_loss: `0.072753`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.025775`
- val_base_rmse: `0.030728`
- val_residual_offset_mean_abs: `0.025991`

## Test Metrics

- test_loss: `0.009235`
- test_mae: `0.003534`
- test_rmse: `0.004399`
- test_pointwise_loss: `0.009235`
- test_centered_curve_shape_loss: `0.004017`
- test_curve_offset_loss: `0.005218`
- test_curve_amplitude_loss: `0.038675`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.027752`
- test_base_rmse: `0.032439`
- test_residual_offset_mean_abs: `0.028197`

## Interpretation

The held-out val error stayed finite with MAE=0.003727 deg and RMSE=0.004647 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003534 deg and RMSE=0.004399 deg, which indicates a numerically stable baseline run.
