# Wave4 2 Quantile P10 P50 P90 Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-14-13-54-54__te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=063-val_mae=0.00181729.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.013911`
- val_mae: `0.001817`
- val_rmse: `0.002593`
- val_pointwise_loss: `0.013911`
- val_centered_curve_shape_loss: `0.004605`
- val_curve_offset_loss: `0.000409`
- val_curve_amplitude_loss: `0.033049`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_interval_coverage: `0.886746`
- val_interval_width: `0.007400`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.025308`
- val_structured_rmse: `0.030811`
- val_residual_offset_mean_abs: `0.024897`

## Test Metrics

- test_loss: `0.016530`
- test_mae: `0.002133`
- test_rmse: `0.003542`
- test_pointwise_loss: `0.016530`
- test_centered_curve_shape_loss: `0.005540`
- test_curve_offset_loss: `0.002981`
- test_curve_amplitude_loss: `0.043867`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_interval_coverage: `0.864073`
- test_interval_width: `0.007358`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.024533`
- test_structured_rmse: `0.029938`
- test_residual_offset_mean_abs: `0.023816`

## Interpretation

The held-out val error stayed finite with MAE=0.001817 deg and RMSE=0.002593 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002133 deg and RMSE=0.003542 deg, which indicates a numerically stable baseline run.
