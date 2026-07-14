# Wave4 2 Quantile P10 P50 P90 Global Training And Testing Report

## Overview

- Run Name: `te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints`
- Model Family: `wave4_2_quantile_p10_p50_p90_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_quantile_p10_p50_p90/2026-07-13-11-13-46__te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=091-val_mae=0.00353725.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.023641`
- val_mae: `0.003537`
- val_rmse: `0.004379`
- val_pointwise_loss: `0.023641`
- val_centered_curve_shape_loss: `0.006474`
- val_curve_offset_loss: `0.004230`
- val_curve_amplitude_loss: `0.049861`
- val_sparse_harmonic_shape_loss: `0.000154`
- val_interval_coverage: `0.885712`
- val_interval_width: `0.012485`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.038700`
- val_structured_rmse: `0.044138`
- val_residual_offset_mean_abs: `0.038399`

## Test Metrics

- test_loss: `0.021976`
- test_mae: `0.003342`
- test_rmse: `0.004121`
- test_pointwise_loss: `0.021976`
- test_centered_curve_shape_loss: `0.003212`
- test_curve_offset_loss: `0.004950`
- test_curve_amplitude_loss: `0.021752`
- test_sparse_harmonic_shape_loss: `6.990373e-05`
- test_interval_coverage: `0.881631`
- test_interval_width: `0.011939`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.041542`
- test_structured_rmse: `0.047105`
- test_residual_offset_mean_abs: `0.041368`

## Interpretation

The held-out val error stayed finite with MAE=0.003537 deg and RMSE=0.004379 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003342 deg and RMSE=0.004121 deg, which indicates a numerically stable baseline run.
