# Wave4 2 Quantile P10 P50 P90 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values`
- Model Family: `wave4_2_quantile_p10_p50_p90_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-15-32-15__te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=180-val_mae=0.00177392.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012440`
- val_mae: `0.001774`
- val_rmse: `0.002553`
- val_pointwise_loss: `0.012440`
- val_centered_curve_shape_loss: `0.004570`
- val_curve_offset_loss: `0.000334`
- val_curve_amplitude_loss: `0.036488`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_interval_coverage: `0.838609`
- val_interval_width: `0.006063`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.008632`
- val_structured_rmse: `0.009932`
- val_residual_offset_mean_abs: `0.008978`

## Test Metrics

- test_loss: `0.013626`
- test_mae: `0.001934`
- test_rmse: `0.003029`
- test_pointwise_loss: `0.013626`
- test_centered_curve_shape_loss: `0.005453`
- test_curve_offset_loss: `0.000444`
- test_curve_amplitude_loss: `0.042143`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_interval_coverage: `0.835696`
- test_interval_width: `0.006254`
- test_quantile_crossing_rate: `5.369416e-05`
- test_structured_mae: `0.008615`
- test_structured_rmse: `0.010497`
- test_residual_offset_mean_abs: `0.008936`

## Interpretation

The held-out val error stayed finite with MAE=0.001774 deg and RMSE=0.002553 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001934 deg and RMSE=0.003029 deg, which indicates a numerically stable baseline run.
