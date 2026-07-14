# Wave4 2 Gaussian Nll Global Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_global__polished_setpoints`
- Model Family: `wave4_2_gaussian_nll_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-18-46-23__te_wave4_2_gaussian_nll_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=240-val_mae=0.00188169.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `-1.614685`
- val_mae: `0.001882`
- val_rmse: `0.002674`
- val_pointwise_loss: `-1.614685`
- val_centered_curve_shape_loss: `0.004674`
- val_curve_offset_loss: `0.000447`
- val_curve_amplitude_loss: `0.038683`
- val_sparse_harmonic_shape_loss: `0.000104`
- val_interval_coverage: `0.903565`
- val_interval_width: `0.008494`
- val_mean_sigma: `0.003314`
- val_structured_mae: `0.033748`
- val_structured_rmse: `0.042680`
- val_residual_offset_mean_abs: `0.071143`

## Test Metrics

- test_loss: `-1.533292`
- test_mae: `0.002210`
- test_rmse: `0.003605`
- test_pointwise_loss: `-1.533292`
- test_centered_curve_shape_loss: `0.005589`
- test_curve_offset_loss: `0.003023`
- test_curve_amplitude_loss: `0.049675`
- test_sparse_harmonic_shape_loss: `0.000113`
- test_interval_coverage: `0.889712`
- test_interval_width: `0.008459`
- test_mean_sigma: `0.003300`
- test_structured_mae: `0.031832`
- test_structured_rmse: `0.040823`
- test_residual_offset_mean_abs: `0.070993`

## Interpretation

The held-out val error stayed finite with MAE=0.001882 deg and RMSE=0.002674 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002210 deg and RMSE=0.003605 deg, which indicates a numerically stable baseline run.
