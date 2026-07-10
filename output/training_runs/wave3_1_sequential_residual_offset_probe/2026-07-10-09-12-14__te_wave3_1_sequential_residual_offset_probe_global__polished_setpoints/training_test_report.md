# Wave3 1 Sequential Residual Offset Probe Global Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_global__polished_setpoints`
- Model Family: `wave3_1_sequential_residual_offset_probe_global`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-09-12-14__te_wave3_1_sequential_residual_offset_probe_global__polished_setpoints/checkpoints/sequential_residual_offset_probe-epoch=155-val_mae=0.00218350.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005818`
- val_mae: `0.002184`
- val_rmse: `0.003005`
- val_pointwise_loss: `0.005818`
- val_centered_curve_shape_loss: `0.005355`
- val_curve_offset_loss: `0.000463`
- val_curve_amplitude_loss: `0.057305`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.024582`
- val_base_rmse: `0.029195`
- val_residual_offset_mean_abs: `0.024439`

## Test Metrics

- test_loss: `0.009191`
- test_mae: `0.002475`
- test_rmse: `0.003835`
- test_pointwise_loss: `0.009191`
- test_centered_curve_shape_loss: `0.006267`
- test_curve_offset_loss: `0.002924`
- test_curve_amplitude_loss: `0.069807`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.023251`
- test_base_rmse: `0.028031`
- test_residual_offset_mean_abs: `0.022982`

## Interpretation

The held-out val error stayed finite with MAE=0.002184 deg and RMSE=0.003005 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002475 deg and RMSE=0.003835 deg, which indicates a numerically stable baseline run.
