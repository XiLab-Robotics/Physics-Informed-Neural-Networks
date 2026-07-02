# Wave3 3 Raw Centered Shape Curve Aware Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_fw`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_centered_shape_curve_aware\2026-06-30-22-31-32__te_wave3_3_raw_centered_shape_curve_aware_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=094-val_mae=0.00178919.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006406`
- val_mae: `0.001789`
- val_rmse: `0.002211`
- val_pointwise_loss: `0.004806`
- val_centered_curve_shape_loss: `0.004530`
- val_curve_offset_loss: `0.000275`
- val_curve_amplitude_loss: `0.036106`
- val_sparse_harmonic_shape_loss: `0.000100`
- val_structured_mae: `0.005763`
- val_structured_rmse: `0.006176`
- val_residual_offset_mean_abs: `0.005089`

## Test Metrics

- test_loss: `0.007590`
- test_mae: `0.001917`
- test_rmse: `0.002466`
- test_pointwise_loss: `0.005713`
- test_centered_curve_shape_loss: `0.005316`
- test_curve_offset_loss: `0.000397`
- test_curve_amplitude_loss: `0.042002`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.005676`
- test_structured_rmse: `0.006291`
- test_residual_offset_mean_abs: `0.004853`

## Interpretation

The held-out val error stayed finite with MAE=0.001789 deg and RMSE=0.002211 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001917 deg and RMSE=0.002466 deg, which indicates a numerically stable baseline run.
