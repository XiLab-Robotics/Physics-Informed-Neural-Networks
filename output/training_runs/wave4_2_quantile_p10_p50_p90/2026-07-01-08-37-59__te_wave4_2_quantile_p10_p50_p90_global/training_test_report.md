# Wave4 2 Quantile P10 P50 P90 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_global`
- Model Family: `wave4_2_quantile_p10_p50_p90_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-01-08-37-59__te_wave4_2_quantile_p10_p50_p90_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=220-val_mae=0.00172811.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011614`
- val_mae: `0.001728`
- val_rmse: `0.002143`
- val_pointwise_loss: `0.011614`
- val_centered_curve_shape_loss: `0.004576`
- val_curve_offset_loss: `0.000225`
- val_curve_amplitude_loss: `0.037036`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_interval_coverage: `0.816191`
- val_interval_width: `0.005782`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.006210`
- val_structured_rmse: `0.006980`
- val_residual_offset_mean_abs: `0.005950`

## Test Metrics

- test_loss: `0.012569`
- test_mae: `0.001878`
- test_rmse: `0.002428`
- test_pointwise_loss: `0.012569`
- test_centered_curve_shape_loss: `0.005400`
- test_curve_offset_loss: `0.000243`
- test_curve_amplitude_loss: `0.042172`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_interval_coverage: `0.807050`
- test_interval_width: `0.006049`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.006066`
- test_structured_rmse: `0.006978`
- test_residual_offset_mean_abs: `0.005725`

## Interpretation

The held-out val error stayed finite with MAE=0.001728 deg and RMSE=0.002143 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001878 deg and RMSE=0.002428 deg, which indicates a numerically stable baseline run.
