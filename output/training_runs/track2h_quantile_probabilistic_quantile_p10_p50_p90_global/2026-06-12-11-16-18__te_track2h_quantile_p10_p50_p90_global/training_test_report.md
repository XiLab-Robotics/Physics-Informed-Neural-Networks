# Track2H Quantile Probabilistic Quantile P10 P50 P90 Global Training And Testing Report

## Overview

- Run Name: `te_track2h_quantile_p10_p50_p90_global`
- Model Family: `track2h_quantile_probabilistic_quantile_p10_p50_p90_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_quantile_p10_p50_p90_global\2026-06-12-11-16-18__te_track2h_quantile_p10_p50_p90_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=030-val_mae=0.00360589.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.024195`
- val_mae: `0.003606`
- val_rmse: `0.004094`
- val_pointwise_loss: `0.024195`
- val_centered_curve_shape_loss: `0.006805`
- val_curve_offset_loss: `0.004498`
- val_curve_amplitude_loss: `0.046060`
- val_sparse_harmonic_shape_loss: `0.000163`
- val_interval_coverage: `0.831709`
- val_interval_width: `0.011370`
- val_quantile_crossing_rate: `0.000000e+00`
- val_structured_mae: `0.026859`
- val_structured_rmse: `0.029636`
- val_residual_offset_mean_abs: `0.026467`

## Test Metrics

- test_loss: `0.022226`
- test_mae: `0.003383`
- test_rmse: `0.003764`
- test_pointwise_loss: `0.022226`
- test_centered_curve_shape_loss: `0.003386`
- test_curve_offset_loss: `0.005242`
- test_curve_amplitude_loss: `0.019879`
- test_sparse_harmonic_shape_loss: `7.439520e-05`
- test_interval_coverage: `0.849227`
- test_interval_width: `0.011449`
- test_quantile_crossing_rate: `0.000000e+00`
- test_structured_mae: `0.029379`
- test_structured_rmse: `0.031828`
- test_residual_offset_mean_abs: `0.029049`

## Interpretation

The held-out val error stayed finite with MAE=0.003606 deg and RMSE=0.004094 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003383 deg and RMSE=0.003764 deg, which indicates a numerically stable baseline run.
