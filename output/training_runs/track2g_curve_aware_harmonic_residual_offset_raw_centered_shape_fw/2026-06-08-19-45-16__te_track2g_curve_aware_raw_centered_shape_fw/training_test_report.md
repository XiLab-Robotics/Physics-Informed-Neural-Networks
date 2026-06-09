# Track2G Curve Aware Harmonic Residual Offset Raw Centered Shape Fw Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_raw_centered_shape_fw`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw\2026-06-08-19-45-16__te_track2g_curve_aware_raw_centered_shape_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=036-val_mae=0.00325058.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.036774`
- val_mae: `0.003251`
- val_rmse: `0.003734`
- val_pointwise_loss: `0.031475`
- val_centered_curve_shape_loss: `0.014999`
- val_curve_offset_loss: `0.016476`
- val_curve_amplitude_loss: `0.094356`
- val_sparse_harmonic_shape_loss: `0.000326`
- val_structured_mae: `0.019344`
- val_structured_rmse: `0.021402`
- val_residual_offset_mean_abs: `0.019207`

## Test Metrics

- test_loss: `0.029307`
- test_mae: `0.003181`
- test_rmse: `0.003571`
- test_pointwise_loss: `0.026596`
- test_centered_curve_shape_loss: `0.007685`
- test_curve_offset_loss: `0.018911`
- test_curve_amplitude_loss: `0.041964`
- test_sparse_harmonic_shape_loss: `0.000142`
- test_structured_mae: `0.022302`
- test_structured_rmse: `0.024404`
- test_residual_offset_mean_abs: `0.022851`

## Interpretation

The held-out val error stayed finite with MAE=0.003251 deg and RMSE=0.003734 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003181 deg and RMSE=0.003571 deg, which indicates a numerically stable baseline run.
