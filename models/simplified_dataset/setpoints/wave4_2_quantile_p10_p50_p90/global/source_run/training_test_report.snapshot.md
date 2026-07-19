# Wave4 2 Quantile P10 P50 P90 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-05-29__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=096-val_mae=0.00351589.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.023266`
- val_mae: `0.003516`
- val_rmse: `0.004372`
- val_pointwise_loss: `0.023266`
- val_centered_curve_shape_loss: `0.006518`
- val_curve_offset_loss: `0.004227`
- val_curve_amplitude_loss: `0.050969`
- val_sparse_harmonic_shape_loss: `0.000155`
- val_interval_coverage: `0.857402`
- val_interval_width: `0.011559`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.034148`
- val_structured_rmse: `0.039298`
- val_residual_offset_mean_abs: `0.034109`

## Test Metrics

- test_loss: `0.021549`
- test_mae: `0.003378`
- test_rmse: `0.004183`
- test_pointwise_loss: `0.021549`
- test_centered_curve_shape_loss: `0.003191`
- test_curve_offset_loss: `0.005210`
- test_curve_amplitude_loss: `0.022204`
- test_sparse_harmonic_shape_loss: `6.922892e-05`
- test_interval_coverage: `0.853093`
- test_interval_width: `0.011052`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.037105`
- test_structured_rmse: `0.042047`
- test_residual_offset_mean_abs: `0.037151`

## Interpretation

The held-out val error stayed finite with MAE=0.003516 deg and RMSE=0.004372 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003378 deg and RMSE=0.004183 deg, which indicates a numerically stable baseline run.
