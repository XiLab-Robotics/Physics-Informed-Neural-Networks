# Wave4 2 Quantile P10 P50 P90 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_bw`
- Model Family: `wave4_2_quantile_p10_p50_p90_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_quantile_p10_p50_p90\2026-07-01-10-36-43__te_wave4_2_quantile_p10_p50_p90_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=163-val_mae=0.00174118.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011623`
- val_mae: `0.001741`
- val_rmse: `0.002157`
- val_pointwise_loss: `0.011623`
- val_centered_curve_shape_loss: `0.004627`
- val_curve_offset_loss: `0.000201`
- val_curve_amplitude_loss: `0.037298`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_interval_coverage: `0.813547`
- val_interval_width: `0.005811`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.009131`
- val_structured_rmse: `0.010551`
- val_residual_offset_mean_abs: `0.007794`

## Test Metrics

- test_loss: `0.012496`
- test_mae: `0.001888`
- test_rmse: `0.002435`
- test_pointwise_loss: `0.012496`
- test_centered_curve_shape_loss: `0.005453`
- test_curve_offset_loss: `0.000235`
- test_curve_amplitude_loss: `0.042815`
- test_sparse_harmonic_shape_loss: `0.000113`
- test_interval_coverage: `0.801869`
- test_interval_width: `0.005937`
- test_quantile_crossing_rate: `2.684708e-05`
- test_structured_mae: `0.009342`
- test_structured_rmse: `0.010697`
- test_residual_offset_mean_abs: `0.007848`

## Interpretation

The held-out val error stayed finite with MAE=0.001741 deg and RMSE=0.002157 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001888 deg and RMSE=0.002435 deg, which indicates a numerically stable baseline run.
