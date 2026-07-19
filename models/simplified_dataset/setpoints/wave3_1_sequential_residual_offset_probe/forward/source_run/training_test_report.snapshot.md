# Wave3 1 Sequential Residual Offset Probe Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints`
- Model Family: `wave3_1_sequential_residual_offset_probe_fw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-24-57__te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints/checkpoints/sequential_residual_offset_probe-epoch=138-val_mae=0.00365466.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011385`
- val_mae: `0.003655`
- val_rmse: `0.004564`
- val_pointwise_loss: `0.011385`
- val_centered_curve_shape_loss: `0.007282`
- val_curve_offset_loss: `0.004102`
- val_curve_amplitude_loss: `0.075711`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026653`
- val_base_rmse: `0.030939`
- val_residual_offset_mean_abs: `0.026909`

## Test Metrics

- test_loss: `0.008823`
- test_mae: `0.003472`
- test_rmse: `0.004298`
- test_pointwise_loss: `0.008823`
- test_centered_curve_shape_loss: `0.003989`
- test_curve_offset_loss: `0.004834`
- test_curve_amplitude_loss: `0.041252`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.028531`
- test_base_rmse: `0.032629`
- test_residual_offset_mean_abs: `0.028854`

## Interpretation

The held-out val error stayed finite with MAE=0.003655 deg and RMSE=0.004564 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003472 deg and RMSE=0.004298 deg, which indicates a numerically stable baseline run.
