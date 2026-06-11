# Track2H Dispersion Aware Log Cosh Robust Fw Training And Testing Report

## Overview

- Run Name: `te_track2h_log_cosh_robust_fw`
- Model Family: `track2h_dispersion_aware_log_cosh_robust_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_log_cosh_robust_fw\2026-06-11-13-43-04__te_track2h_log_cosh_robust_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=016-val_mae=0.00327980.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.015374`
- val_mae: `0.003280`
- val_rmse: `0.003775`
- val_pointwise_loss: `0.015374`
- val_centered_curve_shape_loss: `0.015062`
- val_curve_offset_loss: `0.016533`
- val_curve_amplitude_loss: `0.097017`
- val_sparse_harmonic_shape_loss: `0.000327`
- val_structured_mae: `0.015448`
- val_structured_rmse: `0.017241`
- val_residual_offset_mean_abs: `0.015460`

## Test Metrics

- test_loss: `0.013937`
- test_mae: `0.003355`
- test_rmse: `0.003708`
- test_pointwise_loss: `0.013937`
- test_centered_curve_shape_loss: `0.007693`
- test_curve_offset_loss: `0.020544`
- test_curve_amplitude_loss: `0.042866`
- test_sparse_harmonic_shape_loss: `0.000141`
- test_structured_mae: `0.016999`
- test_structured_rmse: `0.018751`
- test_residual_offset_mean_abs: `0.017653`

## Interpretation

The held-out val error stayed finite with MAE=0.003280 deg and RMSE=0.003775 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003355 deg and RMSE=0.003708 deg, which indicates a numerically stable baseline run.
