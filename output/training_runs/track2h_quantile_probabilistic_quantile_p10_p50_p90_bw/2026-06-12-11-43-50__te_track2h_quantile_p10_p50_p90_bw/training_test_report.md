# Track2H Quantile Probabilistic Quantile P10 P50 P90 Bw Training And Testing Report

## Overview

- Run Name: `te_track2h_quantile_p10_p50_p90_bw`
- Model Family: `track2h_quantile_probabilistic_quantile_p10_p50_p90_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_quantile_p10_p50_p90_bw\2026-06-12-11-43-50__te_track2h_quantile_p10_p50_p90_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=206-val_mae=0.00343553.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.042796`
- val_mae: `0.003436`
- val_rmse: `0.004112`
- val_pointwise_loss: `0.042796`
- val_centered_curve_shape_loss: `0.029474`
- val_curve_offset_loss: `0.014461`
- val_curve_amplitude_loss: `0.242526`
- val_sparse_harmonic_shape_loss: `0.000717`
- val_interval_coverage: `0.718052`
- val_interval_width: `0.009399`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.005910`
- val_structured_rmse: `0.007176`
- val_residual_offset_mean_abs: `0.004266`

## Test Metrics

- test_loss: `0.037860`
- test_mae: `0.002927`
- test_rmse: `0.003519`
- test_pointwise_loss: `0.037860`
- test_centered_curve_shape_loss: `0.014412`
- test_curve_offset_loss: `0.014007`
- test_curve_amplitude_loss: `0.102080`
- test_sparse_harmonic_shape_loss: `0.000329`
- test_interval_coverage: `0.709944`
- test_interval_width: `0.007536`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.005787`
- test_structured_rmse: `0.006995`
- test_residual_offset_mean_abs: `0.004089`

## Interpretation

The held-out val error stayed finite with MAE=0.003436 deg and RMSE=0.004112 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002927 deg and RMSE=0.003519 deg, which indicates a numerically stable baseline run.
