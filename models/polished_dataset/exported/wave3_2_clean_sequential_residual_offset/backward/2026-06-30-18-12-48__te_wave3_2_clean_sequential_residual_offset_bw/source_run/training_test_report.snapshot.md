# Wave3 2 Clean Sequential Residual Offset Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_bw`
- Model Family: `wave3_2_clean_sequential_residual_offset_bw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_clean_sequential_residual_offset\2026-06-30-18-12-48__te_wave3_2_clean_sequential_residual_offset_bw\checkpoints\sequential_residual_offset_probe-epoch=155-val_mae=0.00214982.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005762`
- val_mae: `0.002150`
- val_rmse: `0.002669`
- val_pointwise_loss: `0.005762`
- val_centered_curve_shape_loss: `0.005394`
- val_curve_offset_loss: `0.000369`
- val_curve_amplitude_loss: `0.057336`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.021306`
- val_base_rmse: `0.024580`
- val_residual_offset_mean_abs: `0.021111`

## Test Metrics

- test_loss: `0.006531`
- test_mae: `0.002242`
- test_rmse: `0.002885`
- test_pointwise_loss: `0.006531`
- test_centered_curve_shape_loss: `0.006201`
- test_curve_offset_loss: `0.000330`
- test_curve_amplitude_loss: `0.063146`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.020304`
- test_base_rmse: `0.023694`
- test_residual_offset_mean_abs: `0.020134`

## Interpretation

The held-out val error stayed finite with MAE=0.002150 deg and RMSE=0.002669 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002242 deg and RMSE=0.002885 deg, which indicates a numerically stable baseline run.
