# Wave4 2 Quantile P10 P50 P90 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_fw`
- Model Family: `wave4_2_quantile_p10_p50_p90_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-01-09-37-14__te_wave4_2_quantile_p10_p50_p90_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=202-val_mae=0.00173095.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011311`
- val_mae: `0.001731`
- val_rmse: `0.002143`
- val_pointwise_loss: `0.011311`
- val_centered_curve_shape_loss: `0.004655`
- val_curve_offset_loss: `0.000209`
- val_curve_amplitude_loss: `0.036485`
- val_sparse_harmonic_shape_loss: `0.000104`
- val_interval_coverage: `0.850811`
- val_interval_width: `0.005717`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.004446`
- val_structured_rmse: `0.005248`
- val_residual_offset_mean_abs: `0.003691`

## Test Metrics

- test_loss: `0.012540`
- test_mae: `0.001914`
- test_rmse: `0.002457`
- test_pointwise_loss: `0.012540`
- test_centered_curve_shape_loss: `0.005423`
- test_curve_offset_loss: `0.000398`
- test_curve_amplitude_loss: `0.041777`
- test_sparse_harmonic_shape_loss: `0.000113`
- test_interval_coverage: `0.835884`
- test_interval_width: `0.006119`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.004602`
- test_structured_rmse: `0.005531`
- test_residual_offset_mean_abs: `0.003705`

## Interpretation

The held-out val error stayed finite with MAE=0.001731 deg and RMSE=0.002143 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001914 deg and RMSE=0.002457 deg, which indicates a numerically stable baseline run.
