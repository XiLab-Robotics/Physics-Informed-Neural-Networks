# Wave4 2 Gaussian Nll Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_bw`
- Model Family: `wave4_2_gaussian_nll_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_2_gaussian_nll\2026-07-01-12-57-10__te_wave4_2_gaussian_nll_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=168-val_mae=0.00177847.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.898429`
- val_mae: `0.001778`
- val_rmse: `0.002203`
- val_pointwise_loss: `-1.898429`
- val_centered_curve_shape_loss: `0.004738`
- val_curve_offset_loss: `0.000258`
- val_curve_amplitude_loss: `0.039108`
- val_sparse_harmonic_shape_loss: `0.000106`
- val_interval_coverage: `0.851401`
- val_interval_width: `0.006489`
- val_mean_sigma: `0.002532`
- val_structured_mae: `0.041754`
- val_structured_rmse: `0.056781`
- val_residual_offset_mean_abs: `0.040620`

## Test Metrics

- test_loss: `-1.855482`
- test_mae: `0.001927`
- test_rmse: `0.002482`
- test_pointwise_loss: `-1.855482`
- test_centered_curve_shape_loss: `0.005573`
- test_curve_offset_loss: `0.000272`
- test_curve_amplitude_loss: `0.044865`
- test_sparse_harmonic_shape_loss: `0.000115`
- test_interval_coverage: `0.858435`
- test_interval_width: `0.007019`
- test_mean_sigma: `0.002739`
- test_structured_mae: `0.042228`
- test_structured_rmse: `0.057678`
- test_residual_offset_mean_abs: `0.039519`

## Interpretation

The held-out val error stayed finite with MAE=0.001778 deg and RMSE=0.002203 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001927 deg and RMSE=0.002482 deg, which indicates a numerically stable baseline run.
