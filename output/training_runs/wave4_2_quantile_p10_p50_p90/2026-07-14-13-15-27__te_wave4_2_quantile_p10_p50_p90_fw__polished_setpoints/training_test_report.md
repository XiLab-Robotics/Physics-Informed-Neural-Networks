# Wave4 2 Quantile P10 P50 P90 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-15-27__te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=157-val_mae=0.00180121.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.013436`
- val_mae: `0.001801`
- val_rmse: `0.002583`
- val_pointwise_loss: `0.013436`
- val_centered_curve_shape_loss: `0.004600`
- val_curve_offset_loss: `0.000357`
- val_curve_amplitude_loss: `0.036001`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_interval_coverage: `0.868610`
- val_interval_width: `0.007180`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.027706`
- val_structured_rmse: `0.032714`
- val_residual_offset_mean_abs: `0.027729`

## Test Metrics

- test_loss: `0.016205`
- test_mae: `0.002141`
- test_rmse: `0.003552`
- test_pointwise_loss: `0.016205`
- test_centered_curve_shape_loss: `0.005550`
- test_curve_offset_loss: `0.003021`
- test_curve_amplitude_loss: `0.047129`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_interval_coverage: `0.848824`
- test_interval_width: `0.007120`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.025437`
- test_structured_rmse: `0.030870`
- test_residual_offset_mean_abs: `0.025235`

## Interpretation

The held-out val error stayed finite with MAE=0.001801 deg and RMSE=0.002583 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002141 deg and RMSE=0.003552 deg, which indicates a numerically stable baseline run.
