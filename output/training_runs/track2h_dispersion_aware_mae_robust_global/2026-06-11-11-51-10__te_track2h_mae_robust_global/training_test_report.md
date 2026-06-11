# Track2H Dispersion Aware Mae Robust Global Training And Testing Report

## Overview

- Run Name: `te_track2h_mae_robust_global`
- Model Family: `track2h_dispersion_aware_mae_robust_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_mae_robust_global\2026-06-11-11-51-10__te_track2h_mae_robust_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=026-val_mae=0.00364502.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.078353`
- val_mae: `0.003645`
- val_rmse: `0.004164`
- val_pointwise_loss: `0.078353`
- val_centered_curve_shape_loss: `0.006557`
- val_curve_offset_loss: `0.004578`
- val_curve_amplitude_loss: `0.049895`
- val_sparse_harmonic_shape_loss: `0.000156`
- val_structured_mae: `0.025583`
- val_structured_rmse: `0.029459`
- val_residual_offset_mean_abs: `0.025414`

## Test Metrics

- test_loss: `0.073211`
- test_mae: `0.003406`
- test_rmse: `0.003807`
- test_pointwise_loss: `0.073211`
- test_centered_curve_shape_loss: `0.003299`
- test_curve_offset_loss: `0.005063`
- test_curve_amplitude_loss: `0.022220`
- test_sparse_harmonic_shape_loss: `7.204121e-05`
- test_structured_mae: `0.028167`
- test_structured_rmse: `0.032446`
- test_residual_offset_mean_abs: `0.028308`

## Interpretation

The held-out val error stayed finite with MAE=0.003645 deg and RMSE=0.004164 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003406 deg and RMSE=0.003807 deg, which indicates a numerically stable baseline run.
