# Track2H Quantile Probabilistic Gaussian Nll Global Training And Testing Report

## Overview

- Run Name: `te_track2h_gaussian_nll_global`
- Model Family: `track2h_quantile_probabilistic_gaussian_nll_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_gaussian_nll_global\2026-06-12-12-10-23__te_track2h_gaussian_nll_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=230-val_mae=0.00326664.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-0.996494`
- val_mae: `0.003267`
- val_rmse: `0.003749`
- val_pointwise_loss: `-0.996494`
- val_centered_curve_shape_loss: `0.006509`
- val_curve_offset_loss: `0.003904`
- val_curve_amplitude_loss: `0.049119`
- val_sparse_harmonic_shape_loss: `0.000154`
- val_interval_coverage: `0.779008`
- val_interval_width: `0.010252`
- val_mean_sigma: `0.004000`
- val_structured_mae: `0.048378`
- val_structured_rmse: `0.063959`
- val_residual_offset_mean_abs: `0.032589`

## Test Metrics

- test_loss: `-0.938582`
- test_mae: `0.003013`
- test_rmse: `0.003388`
- test_pointwise_loss: `-0.938582`
- test_centered_curve_shape_loss: `0.003203`
- test_curve_offset_loss: `0.004478`
- test_curve_amplitude_loss: `0.021581`
- test_sparse_harmonic_shape_loss: `6.934625e-05`
- test_interval_coverage: `0.746886`
- test_interval_width: `0.008761`
- test_mean_sigma: `0.003418`
- test_structured_mae: `0.050001`
- test_structured_rmse: `0.065944`
- test_residual_offset_mean_abs: `0.035388`

## Interpretation

The held-out val error stayed finite with MAE=0.003267 deg and RMSE=0.003749 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003013 deg and RMSE=0.003388 deg, which indicates a numerically stable baseline run.
