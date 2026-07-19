# Wave3 1 Sequential Residual Offset Probe Global Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values`
- Model Family: `wave3_1_sequential_residual_offset_probe_global`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-10-48-41__te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=077-val_mae=0.00220916.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005890`
- val_mae: `0.002209`
- val_rmse: `0.003051`
- val_pointwise_loss: `0.005890`
- val_centered_curve_shape_loss: `0.005419`
- val_curve_offset_loss: `0.000471`
- val_curve_amplitude_loss: `0.060356`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.024273`
- val_base_rmse: `0.029417`
- val_residual_offset_mean_abs: `0.024105`

## Test Metrics

- test_loss: `0.006988`
- test_mae: `0.002379`
- test_rmse: `0.003463`
- test_pointwise_loss: `0.006988`
- test_centered_curve_shape_loss: `0.006323`
- test_curve_offset_loss: `0.000665`
- test_curve_amplitude_loss: `0.066052`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.022979`
- test_base_rmse: `0.028307`
- test_residual_offset_mean_abs: `0.022764`

## Interpretation

The held-out val error stayed finite with MAE=0.002209 deg and RMSE=0.003051 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002379 deg and RMSE=0.003463 deg, which indicates a numerically stable baseline run.
