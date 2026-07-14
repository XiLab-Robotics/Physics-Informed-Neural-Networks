# Wave4 2 Quantile P10 P50 P90 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-35-53__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=101-val_mae=0.00355780.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.023531`
- val_mae: `0.003558`
- val_rmse: `0.004387`
- val_pointwise_loss: `0.023531`
- val_centered_curve_shape_loss: `0.006450`
- val_curve_offset_loss: `0.004349`
- val_curve_amplitude_loss: `0.050083`
- val_sparse_harmonic_shape_loss: `0.000153`
- val_interval_coverage: `0.830273`
- val_interval_width: `0.011325`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.031220`
- val_structured_rmse: `0.036433`
- val_residual_offset_mean_abs: `0.030343`

## Test Metrics

- test_loss: `0.021763`
- test_mae: `0.003443`
- test_rmse: `0.004183`
- test_pointwise_loss: `0.021763`
- test_centered_curve_shape_loss: `0.003178`
- test_curve_offset_loss: `0.005227`
- test_curve_amplitude_loss: `0.021846`
- test_sparse_harmonic_shape_loss: `6.907688e-05`
- test_interval_coverage: `0.843777`
- test_interval_width: `0.010774`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.033522`
- test_structured_rmse: `0.038601`
- test_residual_offset_mean_abs: `0.032928`

## Interpretation

The held-out val error stayed finite with MAE=0.003558 deg and RMSE=0.004387 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003443 deg and RMSE=0.004183 deg, which indicates a numerically stable baseline run.
