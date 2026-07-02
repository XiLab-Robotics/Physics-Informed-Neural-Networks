# Wave3 2 Clean Sequential Residual Offset Global Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_global`
- Model Family: `wave3_2_clean_sequential_residual_offset_global`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_clean_sequential_residual_offset\2026-06-30-17-18-40__te_wave3_2_clean_sequential_residual_offset_global\checkpoints\sequential_residual_offset_probe-epoch=133-val_mae=0.00215807.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005758`
- val_mae: `0.002158`
- val_rmse: `0.002680`
- val_pointwise_loss: `0.005758`
- val_centered_curve_shape_loss: `0.005382`
- val_curve_offset_loss: `0.000376`
- val_curve_amplitude_loss: `0.056548`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.021090`
- val_base_rmse: `0.024368`
- val_residual_offset_mean_abs: `0.020995`

## Test Metrics

- test_loss: `0.006622`
- test_mae: `0.002276`
- test_rmse: `0.002910`
- test_pointwise_loss: `0.006622`
- test_centered_curve_shape_loss: `0.006247`
- test_curve_offset_loss: `0.000375`
- test_curve_amplitude_loss: `0.062323`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.020030`
- test_base_rmse: `0.023597`
- test_residual_offset_mean_abs: `0.019925`

## Interpretation

The held-out val error stayed finite with MAE=0.002158 deg and RMSE=0.002680 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002276 deg and RMSE=0.002910 deg, which indicates a numerically stable baseline run.
