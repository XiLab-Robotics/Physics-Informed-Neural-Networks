# Wave4 2 Gaussian Nll Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_fw`
- Model Family: `wave4_2_gaussian_nll_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_gaussian_nll\2026-07-01-11-54-11__te_wave4_2_gaussian_nll_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=204-val_mae=0.00173884.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.960230`
- val_mae: `0.001739`
- val_rmse: `0.002154`
- val_pointwise_loss: `-1.960230`
- val_centered_curve_shape_loss: `0.004674`
- val_curve_offset_loss: `0.000233`
- val_curve_amplitude_loss: `0.037917`
- val_sparse_harmonic_shape_loss: `0.000104`
- val_interval_coverage: `0.826702`
- val_interval_width: `0.005739`
- val_mean_sigma: `0.002239`
- val_structured_mae: `0.054304`
- val_structured_rmse: `0.073918`
- val_residual_offset_mean_abs: `0.029949`

## Test Metrics

- test_loss: `-1.882719`
- test_mae: `0.001914`
- test_rmse: `0.002482`
- test_pointwise_loss: `-1.882719`
- test_centered_curve_shape_loss: `0.005685`
- test_curve_offset_loss: `0.000384`
- test_curve_amplitude_loss: `0.044936`
- test_sparse_harmonic_shape_loss: `0.000114`
- test_interval_coverage: `0.814863`
- test_interval_width: `0.006131`
- test_mean_sigma: `0.002392`
- test_structured_mae: `0.055060`
- test_structured_rmse: `0.074886`
- test_residual_offset_mean_abs: `0.029725`

## Interpretation

The held-out val error stayed finite with MAE=0.001739 deg and RMSE=0.002154 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001914 deg and RMSE=0.002482 deg, which indicates a numerically stable baseline run.
