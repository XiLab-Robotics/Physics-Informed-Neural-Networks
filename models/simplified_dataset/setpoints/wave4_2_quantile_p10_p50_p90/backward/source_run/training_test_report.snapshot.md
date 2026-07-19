# Wave4 2 Quantile P10 P50 P90 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-58-31__te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=087-val_mae=0.00355108.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.024158`
- val_mae: `0.003551`
- val_rmse: `0.004410`
- val_pointwise_loss: `0.024158`
- val_centered_curve_shape_loss: `0.006429`
- val_curve_offset_loss: `0.004426`
- val_curve_amplitude_loss: `0.048556`
- val_sparse_harmonic_shape_loss: `0.000152`
- val_interval_coverage: `0.882517`
- val_interval_width: `0.013086`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.034427`
- val_structured_rmse: `0.040009`
- val_residual_offset_mean_abs: `0.033779`

## Test Metrics

- test_loss: `0.023109`
- test_mae: `0.003466`
- test_rmse: `0.004275`
- test_pointwise_loss: `0.023109`
- test_centered_curve_shape_loss: `0.003161`
- test_curve_offset_loss: `0.005525`
- test_curve_amplitude_loss: `0.021318`
- test_sparse_harmonic_shape_loss: `6.847555e-05`
- test_interval_coverage: `0.864664`
- test_interval_width: `0.012418`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.037339`
- test_structured_rmse: `0.042736`
- test_residual_offset_mean_abs: `0.036659`

## Interpretation

The held-out val error stayed finite with MAE=0.003551 deg and RMSE=0.004410 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003466 deg and RMSE=0.004275 deg, which indicates a numerically stable baseline run.
