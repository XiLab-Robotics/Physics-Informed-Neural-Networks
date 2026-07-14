# Wave4 2 Quantile P10 P50 P90 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-12-41-50__te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=109-val_mae=0.00179474.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.013748`
- val_mae: `0.001795`
- val_rmse: `0.002573`
- val_pointwise_loss: `0.013748`
- val_centered_curve_shape_loss: `0.004581`
- val_curve_offset_loss: `0.000365`
- val_curve_amplitude_loss: `0.036645`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_interval_coverage: `0.877255`
- val_interval_width: `0.007214`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.032355`
- val_structured_rmse: `0.037089`
- val_residual_offset_mean_abs: `0.032682`

## Test Metrics

- test_loss: `0.016243`
- test_mae: `0.002095`
- test_rmse: `0.003519`
- test_pointwise_loss: `0.016243`
- test_centered_curve_shape_loss: `0.005526`
- test_curve_offset_loss: `0.002979`
- test_curve_amplitude_loss: `0.047952`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_interval_coverage: `0.861523`
- test_interval_width: `0.007091`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.030922`
- test_structured_rmse: `0.035664`
- test_residual_offset_mean_abs: `0.031271`

## Interpretation

The held-out val error stayed finite with MAE=0.001795 deg and RMSE=0.002573 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002095 deg and RMSE=0.003519 deg, which indicates a numerically stable baseline run.
