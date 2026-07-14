# Wave4 2 Quantile P10 P50 P90 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values`
- Model Family: `wave4_2_quantile_p10_p50_p90_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-17-11-13__te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=123-val_mae=0.00178818.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.013154`
- val_mae: `0.001788`
- val_rmse: `0.002557`
- val_pointwise_loss: `0.013154`
- val_centered_curve_shape_loss: `0.004536`
- val_curve_offset_loss: `0.000313`
- val_curve_amplitude_loss: `0.037180`
- val_sparse_harmonic_shape_loss: `0.000100`
- val_interval_coverage: `0.864033`
- val_interval_width: `0.006990`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.013057`
- val_structured_rmse: `0.015344`
- val_residual_offset_mean_abs: `0.012697`

## Test Metrics

- test_loss: `0.014219`
- test_mae: `0.001952`
- test_rmse: `0.003074`
- test_pointwise_loss: `0.014219`
- test_centered_curve_shape_loss: `0.005532`
- test_curve_offset_loss: `0.000486`
- test_curve_amplitude_loss: `0.043668`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_interval_coverage: `0.859939`
- test_interval_width: `0.007089`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.012720`
- test_structured_rmse: `0.015199`
- test_residual_offset_mean_abs: `0.012205`

## Interpretation

The held-out val error stayed finite with MAE=0.001788 deg and RMSE=0.002557 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001952 deg and RMSE=0.003074 deg, which indicates a numerically stable baseline run.
