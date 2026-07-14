# Wave4 2 Quantile P10 P50 P90 Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values`
- Model Family: `wave4_2_quantile_p10_p50_p90_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-16-15-03__te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=250-val_mae=0.00176755.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012516`
- val_mae: `0.001768`
- val_rmse: `0.002539`
- val_pointwise_loss: `0.012516`
- val_centered_curve_shape_loss: `0.004540`
- val_curve_offset_loss: `0.000299`
- val_curve_amplitude_loss: `0.037190`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_interval_coverage: `0.795251`
- val_interval_width: `0.005743`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.006681`
- val_structured_rmse: `0.008749`
- val_residual_offset_mean_abs: `0.006898`

## Test Metrics

- test_loss: `0.013543`
- test_mae: `0.001918`
- test_rmse: `0.003007`
- test_pointwise_loss: `0.013543`
- test_centered_curve_shape_loss: `0.005428`
- test_curve_offset_loss: `0.000376`
- test_curve_amplitude_loss: `0.043053`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_interval_coverage: `0.804392`
- test_interval_width: `0.006091`
- test_quantile_crossing_rate: `5.369416e-05`
- test_structured_mae: `0.007114`
- test_structured_rmse: `0.009434`
- test_residual_offset_mean_abs: `0.007295`

## Interpretation

The held-out val error stayed finite with MAE=0.001768 deg and RMSE=0.002539 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001918 deg and RMSE=0.003007 deg, which indicates a numerically stable baseline run.
