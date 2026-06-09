# Track2G Curve Aware Harmonic Residual Offset Raw Offset Fw Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_raw_offset_fw`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_raw_offset_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_offset_fw\2026-06-08-20-43-53__te_track2g_curve_aware_raw_offset_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=009-val_mae=0.00332750.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.039221`
- val_mae: `0.003328`
- val_rmse: `0.003864`
- val_pointwise_loss: `0.032055`
- val_centered_curve_shape_loss: `0.016130`
- val_curve_offset_loss: `0.015924`
- val_curve_amplitude_loss: `0.078387`
- val_sparse_harmonic_shape_loss: `0.000335`
- val_structured_mae: `0.012787`
- val_structured_rmse: `0.014840`
- val_residual_offset_mean_abs: `0.012417`

## Test Metrics

- test_loss: `0.036213`
- test_mae: `0.003279`
- test_rmse: `0.003698`
- test_pointwise_loss: `0.027727`
- test_centered_curve_shape_loss: `0.008869`
- test_curve_offset_loss: `0.018858`
- test_curve_amplitude_loss: `0.039795`
- test_sparse_harmonic_shape_loss: `0.000153`
- test_structured_mae: `0.013136`
- test_structured_rmse: `0.015309`
- test_residual_offset_mean_abs: `0.013093`

## Interpretation

The held-out val error stayed finite with MAE=0.003328 deg and RMSE=0.003864 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003279 deg and RMSE=0.003698 deg, which indicates a numerically stable baseline run.
