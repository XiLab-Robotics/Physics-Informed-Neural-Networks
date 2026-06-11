# Track2H Dispersion Aware Smooth L1 Robust Bw Training And Testing Report

## Overview

- Run Name: `te_track2h_smooth_l1_robust_bw`
- Model Family: `track2h_dispersion_aware_smooth_l1_robust_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_smooth_l1_robust_bw\2026-06-11-12-56-26__te_track2h_smooth_l1_robust_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=231-val_mae=0.00337231.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.020357`
- val_mae: `0.003372`
- val_rmse: `0.004015`
- val_pointwise_loss: `0.020357`
- val_centered_curve_shape_loss: `0.028332`
- val_curve_offset_loss: `0.012715`
- val_curve_amplitude_loss: `0.212820`
- val_sparse_harmonic_shape_loss: `0.000685`
- val_structured_mae: `0.004269`
- val_structured_rmse: `0.004989`
- val_residual_offset_mean_abs: `0.003168`

## Test Metrics

- test_loss: `0.014269`
- test_mae: `0.003074`
- test_rmse: `0.003662`
- test_pointwise_loss: `0.014269`
- test_centered_curve_shape_loss: `0.013915`
- test_curve_offset_loss: `0.014624`
- test_curve_amplitude_loss: `0.087129`
- test_sparse_harmonic_shape_loss: `0.000315`
- test_structured_mae: `0.003913`
- test_structured_rmse: `0.004563`
- test_residual_offset_mean_abs: `0.003084`

## Interpretation

The held-out val error stayed finite with MAE=0.003372 deg and RMSE=0.004015 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003074 deg and RMSE=0.003662 deg, which indicates a numerically stable baseline run.
