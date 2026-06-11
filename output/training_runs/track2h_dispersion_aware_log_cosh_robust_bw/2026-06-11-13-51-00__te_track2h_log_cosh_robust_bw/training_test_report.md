# Track2H Dispersion Aware Log Cosh Robust Bw Training And Testing Report

## Overview

- Run Name: `te_track2h_log_cosh_robust_bw`
- Model Family: `track2h_dispersion_aware_log_cosh_robust_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_log_cosh_robust_bw\2026-06-11-13-51-00__te_track2h_log_cosh_robust_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=046-val_mae=0.00377404.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.020623`
- val_mae: `0.003774`
- val_rmse: `0.004372`
- val_pointwise_loss: `0.020623`
- val_centered_curve_shape_loss: `0.028583`
- val_curve_offset_loss: `0.015145`
- val_curve_amplitude_loss: `0.221009`
- val_sparse_harmonic_shape_loss: `0.000693`
- val_structured_mae: `0.018265`
- val_structured_rmse: `0.020016`
- val_residual_offset_mean_abs: `0.018113`

## Test Metrics

- test_loss: `0.015147`
- test_mae: `0.003481`
- test_rmse: `0.004029`
- test_pointwise_loss: `0.015147`
- test_centered_curve_shape_loss: `0.014009`
- test_curve_offset_loss: `0.017114`
- test_curve_amplitude_loss: `0.092520`
- test_sparse_harmonic_shape_loss: `0.000318`
- test_structured_mae: `0.020572`
- test_structured_rmse: `0.022977`
- test_residual_offset_mean_abs: `0.020249`

## Interpretation

The held-out val error stayed finite with MAE=0.003774 deg and RMSE=0.004372 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003481 deg and RMSE=0.004029 deg, which indicates a numerically stable baseline run.
