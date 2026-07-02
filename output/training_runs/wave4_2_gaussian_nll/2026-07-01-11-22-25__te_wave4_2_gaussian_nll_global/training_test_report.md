# Wave4 2 Gaussian Nll Global Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_global`
- Model Family: `wave4_2_gaussian_nll_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_gaussian_nll\2026-07-01-11-22-25__te_wave4_2_gaussian_nll_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=108-val_mae=0.00182486.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.832194`
- val_mae: `0.001825`
- val_rmse: `0.002248`
- val_pointwise_loss: `-1.832194`
- val_centered_curve_shape_loss: `0.004677`
- val_curve_offset_loss: `0.000366`
- val_curve_amplitude_loss: `0.037277`
- val_sparse_harmonic_shape_loss: `0.000104`
- val_interval_coverage: `0.817520`
- val_interval_width: `0.006033`
- val_mean_sigma: `0.002354`
- val_structured_mae: `0.026592`
- val_structured_rmse: `0.036049`
- val_residual_offset_mean_abs: `0.054728`

## Test Metrics

- test_loss: `-1.757005`
- test_mae: `0.002001`
- test_rmse: `0.002576`
- test_pointwise_loss: `-1.757005`
- test_centered_curve_shape_loss: `0.005614`
- test_curve_offset_loss: `0.000641`
- test_curve_amplitude_loss: `0.044108`
- test_sparse_harmonic_shape_loss: `0.000115`
- test_interval_coverage: `0.806513`
- test_interval_width: `0.006273`
- test_mean_sigma: `0.002447`
- test_structured_mae: `0.027005`
- test_structured_rmse: `0.036698`
- test_residual_offset_mean_abs: `0.054457`

## Interpretation

The held-out val error stayed finite with MAE=0.001825 deg and RMSE=0.002248 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002001 deg and RMSE=0.002576 deg, which indicates a numerically stable baseline run.
