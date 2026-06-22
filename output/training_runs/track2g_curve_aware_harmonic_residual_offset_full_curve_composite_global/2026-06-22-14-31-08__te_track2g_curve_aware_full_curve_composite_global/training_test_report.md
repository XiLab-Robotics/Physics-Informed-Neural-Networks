# Track2G Curve Aware Harmonic Residual Offset Full Curve Composite Global Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_full_curve_composite_global`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global\2026-06-22-14-31-08__te_track2g_curve_aware_full_curve_composite_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=136-val_mae=0.00187186.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008253`
- val_mae: `0.001872`
- val_rmse: `0.002321`
- val_pointwise_loss: `0.005209`
- val_centered_curve_shape_loss: `0.004862`
- val_curve_offset_loss: `0.000347`
- val_curve_amplitude_loss: `0.016915`
- val_sparse_harmonic_shape_loss: `0.000107`
- val_structured_mae: `0.006810`
- val_structured_rmse: `0.007251`
- val_residual_offset_mean_abs: `0.006159`

## Test Metrics

- test_loss: `0.009803`
- test_mae: `0.002008`
- test_rmse: `0.002581`
- test_pointwise_loss: `0.006064`
- test_centered_curve_shape_loss: `0.005661`
- test_curve_offset_loss: `0.000403`
- test_curve_amplitude_loss: `0.021657`
- test_sparse_harmonic_shape_loss: `0.000117`
- test_structured_mae: `0.006631`
- test_structured_rmse: `0.007274`
- test_residual_offset_mean_abs: `0.005865`

## Interpretation

The held-out val error stayed finite with MAE=0.001872 deg and RMSE=0.002321 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002008 deg and RMSE=0.002581 deg, which indicates a numerically stable baseline run.
