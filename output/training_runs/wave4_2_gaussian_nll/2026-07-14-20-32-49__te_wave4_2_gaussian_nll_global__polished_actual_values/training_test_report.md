# Wave4 2 Gaussian Nll Global Training And Testing Report

## Overview

- Run Name: `te_wave4_2_gaussian_nll_global__polished_actual_values`
- Model Family: `wave4_2_gaussian_nll_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_2_gaussian_nll/2026-07-14-20-32-49__te_wave4_2_gaussian_nll_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=000-val_mae=0.10197201.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `11.635645`
- val_mae: `0.101972`
- val_rmse: `0.124727`
- val_pointwise_loss: `11.635645`
- val_centered_curve_shape_loss: `3.633823`
- val_curve_offset_loss: `3.632407`
- val_curve_amplitude_loss: `79.082306`
- val_sparse_harmonic_shape_loss: `0.100977`
- val_interval_coverage: `0.871470`
- val_interval_width: `4.684516`
- val_mean_sigma: `1.827674`
- val_structured_mae: `0.097140`
- val_structured_rmse: `0.120131`
- val_residual_offset_mean_abs: `0.068989`

## Test Metrics

- test_loss: `19.158119`
- test_mae: `0.101119`
- test_rmse: `0.123836`
- test_pointwise_loss: `19.158119`
- test_centered_curve_shape_loss: `3.686255`
- test_curve_offset_loss: `3.454516`
- test_curve_amplitude_loss: `80.092995`
- test_sparse_harmonic_shape_loss: `0.102097`
- test_interval_coverage: `0.864073`
- test_interval_width: `4.505394`
- test_mean_sigma: `1.757789`
- test_structured_mae: `0.096806`
- test_structured_rmse: `0.119822`
- test_residual_offset_mean_abs: `0.067948`

## Interpretation

The held-out val error stayed finite with MAE=0.101972 deg and RMSE=0.124727 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.101119 deg and RMSE=0.123836 deg, which indicates a numerically stable baseline run.
