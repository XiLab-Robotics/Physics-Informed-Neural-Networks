# Track2H Dispersion Aware Log Cosh Robust Global Training And Testing Report

## Overview

- Run Name: `te_track2h_log_cosh_robust_global`
- Model Family: `track2h_dispersion_aware_log_cosh_robust_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_log_cosh_robust_global\2026-06-11-13-24-47__te_track2h_log_cosh_robust_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=037-val_mae=0.00364458.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005644`
- val_mae: `0.003645`
- val_rmse: `0.004174`
- val_pointwise_loss: `0.005644`
- val_centered_curve_shape_loss: `0.006562`
- val_curve_offset_loss: `0.004902`
- val_curve_amplitude_loss: `0.050268`
- val_sparse_harmonic_shape_loss: `0.000156`
- val_structured_mae: `0.024109`
- val_structured_rmse: `0.025985`
- val_residual_offset_mean_abs: `0.024518`

## Test Metrics

- test_loss: `0.004468`
- test_mae: `0.003505`
- test_rmse: `0.003935`
- test_pointwise_loss: `0.004468`
- test_centered_curve_shape_loss: `0.003285`
- test_curve_offset_loss: `0.005716`
- test_curve_amplitude_loss: `0.022691`
- test_sparse_harmonic_shape_loss: `7.166088e-05`
- test_structured_mae: `0.027341`
- test_structured_rmse: `0.028856`
- test_residual_offset_mean_abs: `0.028025`

## Interpretation

The held-out val error stayed finite with MAE=0.003645 deg and RMSE=0.004174 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003505 deg and RMSE=0.003935 deg, which indicates a numerically stable baseline run.
