# Wave4 2 Quantile P10 P50 P90 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-12-03-07__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=136-val_mae=0.00353663.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.023580`
- val_mae: `0.003537`
- val_rmse: `0.004379`
- val_pointwise_loss: `0.023580`
- val_centered_curve_shape_loss: `0.006513`
- val_curve_offset_loss: `0.004231`
- val_curve_amplitude_loss: `0.050404`
- val_sparse_harmonic_shape_loss: `0.000155`
- val_interval_coverage: `0.824071`
- val_interval_width: `0.011005`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.032208`
- val_structured_rmse: `0.038912`
- val_residual_offset_mean_abs: `0.032133`

## Test Metrics

- test_loss: `0.021919`
- test_mae: `0.003411`
- test_rmse: `0.004192`
- test_pointwise_loss: `0.021919`
- test_centered_curve_shape_loss: `0.003191`
- test_curve_offset_loss: `0.005223`
- test_curve_amplitude_loss: `0.021936`
- test_sparse_harmonic_shape_loss: `6.924636e-05`
- test_interval_coverage: `0.809359`
- test_interval_width: `0.010507`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.034964`
- test_structured_rmse: `0.041639`
- test_residual_offset_mean_abs: `0.035229`

## Interpretation

The held-out val error stayed finite with MAE=0.003537 deg and RMSE=0.004379 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003411 deg and RMSE=0.004192 deg, which indicates a numerically stable baseline run.
