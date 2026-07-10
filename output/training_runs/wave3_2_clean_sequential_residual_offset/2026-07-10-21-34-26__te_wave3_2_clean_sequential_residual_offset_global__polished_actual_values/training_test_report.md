# Wave3 2 Clean Sequential Residual Offset Global Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values`
- Model Family: `wave3_2_clean_sequential_residual_offset_global`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-21-34-26__te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=151-val_mae=0.00216362.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005779`
- val_mae: `0.002164`
- val_rmse: `0.003001`
- val_pointwise_loss: `0.005779`
- val_centered_curve_shape_loss: `0.005400`
- val_curve_offset_loss: `0.000379`
- val_curve_amplitude_loss: `0.059675`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.023048`
- val_base_rmse: `0.028087`
- val_residual_offset_mean_abs: `0.022787`

## Test Metrics

- test_loss: `0.006698`
- test_mae: `0.002302`
- test_rmse: `0.003369`
- test_pointwise_loss: `0.006698`
- test_centered_curve_shape_loss: `0.006235`
- test_curve_offset_loss: `0.000463`
- test_curve_amplitude_loss: `0.065675`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.021889`
- test_base_rmse: `0.027058`
- test_residual_offset_mean_abs: `0.021643`

## Interpretation

The held-out val error stayed finite with MAE=0.002164 deg and RMSE=0.003001 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002302 deg and RMSE=0.003369 deg, which indicates a numerically stable baseline run.
