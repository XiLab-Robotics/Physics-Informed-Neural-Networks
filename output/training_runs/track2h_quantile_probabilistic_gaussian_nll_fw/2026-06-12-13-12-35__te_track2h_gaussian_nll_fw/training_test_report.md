# Track2H Quantile Probabilistic Gaussian Nll Fw Training And Testing Report

## Overview

- Run Name: `te_track2h_gaussian_nll_fw`
- Model Family: `track2h_quantile_probabilistic_gaussian_nll_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_quantile_probabilistic_gaussian_nll_fw\2026-06-12-13-12-35__te_track2h_gaussian_nll_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=056-val_mae=0.00329281.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `-0.346384`
- val_mae: `0.003293`
- val_rmse: `0.003801`
- val_pointwise_loss: `-0.346384`
- val_centered_curve_shape_loss: `0.015167`
- val_curve_offset_loss: `0.016497`
- val_curve_amplitude_loss: `0.106729`
- val_sparse_harmonic_shape_loss: `0.000330`
- val_interval_coverage: `0.893820`
- val_interval_width: `0.011958`
- val_mean_sigma: `0.004665`
- val_structured_mae: `0.018325`
- val_structured_rmse: `0.022879`
- val_residual_offset_mean_abs: `0.017159`

## Test Metrics

- test_loss: `-0.385690`
- test_mae: `0.003165`
- test_rmse: `0.003548`
- test_pointwise_loss: `-0.385690`
- test_centered_curve_shape_loss: `0.007739`
- test_curve_offset_loss: `0.018125`
- test_curve_amplitude_loss: `0.048700`
- test_sparse_harmonic_shape_loss: `0.000143`
- test_interval_coverage: `0.902921`
- test_interval_width: `0.011687`
- test_mean_sigma: `0.004560`
- test_structured_mae: `0.017001`
- test_structured_rmse: `0.021331`
- test_residual_offset_mean_abs: `0.018020`

## Interpretation

The held-out val error stayed finite with MAE=0.003293 deg and RMSE=0.003801 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003165 deg and RMSE=0.003548 deg, which indicates a numerically stable baseline run.
