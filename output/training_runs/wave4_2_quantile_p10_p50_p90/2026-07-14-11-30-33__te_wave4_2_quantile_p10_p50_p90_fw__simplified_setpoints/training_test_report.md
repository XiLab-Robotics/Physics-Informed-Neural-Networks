# Wave4 2 Quantile P10 P50 P90 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-11-30-33__te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=098-val_mae=0.00349706.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.023529`
- val_mae: `0.003497`
- val_rmse: `0.004407`
- val_pointwise_loss: `0.023529`
- val_centered_curve_shape_loss: `0.006489`
- val_curve_offset_loss: `0.004426`
- val_curve_amplitude_loss: `0.052020`
- val_sparse_harmonic_shape_loss: `0.000154`
- val_interval_coverage: `0.856073`
- val_interval_width: `0.011566`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.031250`
- val_structured_rmse: `0.036874`
- val_residual_offset_mean_abs: `0.030897`

## Test Metrics

- test_loss: `0.022213`
- test_mae: `0.003496`
- test_rmse: `0.004299`
- test_pointwise_loss: `0.022213`
- test_centered_curve_shape_loss: `0.003183`
- test_curve_offset_loss: `0.005630`
- test_curve_amplitude_loss: `0.022830`
- test_sparse_harmonic_shape_loss: `6.900338e-05`
- test_interval_coverage: `0.850677`
- test_interval_width: `0.011074`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.034051`
- test_structured_rmse: `0.039516`
- test_residual_offset_mean_abs: `0.033721`

## Interpretation

The held-out val error stayed finite with MAE=0.003497 deg and RMSE=0.004407 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003496 deg and RMSE=0.004299 deg, which indicates a numerically stable baseline run.
