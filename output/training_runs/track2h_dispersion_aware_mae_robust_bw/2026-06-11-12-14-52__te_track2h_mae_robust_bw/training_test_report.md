# Track2H Dispersion Aware Mae Robust Bw Training And Testing Report

## Overview

- Run Name: `te_track2h_mae_robust_bw`
- Model Family: `track2h_dispersion_aware_mae_robust_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_mae_robust_bw\2026-06-11-12-14-52__te_track2h_mae_robust_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=145-val_mae=0.00357893.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.143402`
- val_mae: `0.003579`
- val_rmse: `0.004200`
- val_pointwise_loss: `0.143402`
- val_centered_curve_shape_loss: `0.029367`
- val_curve_offset_loss: `0.014486`
- val_curve_amplitude_loss: `0.232027`
- val_sparse_harmonic_shape_loss: `0.000714`
- val_structured_mae: `0.007730`
- val_structured_rmse: `0.008924`
- val_residual_offset_mean_abs: `0.007080`

## Test Metrics

- test_loss: `0.137430`
- test_mae: `0.003430`
- test_rmse: `0.004029`
- test_pointwise_loss: `0.137430`
- test_centered_curve_shape_loss: `0.014319`
- test_curve_offset_loss: `0.017756`
- test_curve_amplitude_loss: `0.099398`
- test_sparse_harmonic_shape_loss: `0.000326`
- test_structured_mae: `0.008599`
- test_structured_rmse: `0.009694`
- test_residual_offset_mean_abs: `0.007849`

## Interpretation

The held-out val error stayed finite with MAE=0.003579 deg and RMSE=0.004200 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003430 deg and RMSE=0.004029 deg, which indicates a numerically stable baseline run.
