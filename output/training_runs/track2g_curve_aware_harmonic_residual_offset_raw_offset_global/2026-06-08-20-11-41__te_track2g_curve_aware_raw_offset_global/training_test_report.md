# Track2G Curve Aware Harmonic Residual Offset Raw Offset Global Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_raw_offset_global`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_raw_offset_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_offset_global\2026-06-08-20-11-41__te_track2g_curve_aware_raw_offset_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=091-val_mae=0.00356422.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012737`
- val_mae: `0.003564`
- val_rmse: `0.004044`
- val_pointwise_loss: `0.010772`
- val_centered_curve_shape_loss: `0.006405`
- val_curve_offset_loss: `0.004367`
- val_curve_amplitude_loss: `0.045992`
- val_sparse_harmonic_shape_loss: `0.000151`
- val_structured_mae: `0.026043`
- val_structured_rmse: `0.026953`
- val_residual_offset_mean_abs: `0.026065`

## Test Metrics

- test_loss: `0.010868`
- test_mae: `0.003465`
- test_rmse: `0.003829`
- test_pointwise_loss: `0.008482`
- test_centered_curve_shape_loss: `0.003179`
- test_curve_offset_loss: `0.005303`
- test_curve_amplitude_loss: `0.019797`
- test_sparse_harmonic_shape_loss: `6.864010e-05`
- test_structured_mae: `0.029096`
- test_structured_rmse: `0.029598`
- test_residual_offset_mean_abs: `0.029359`

## Interpretation

The held-out val error stayed finite with MAE=0.003564 deg and RMSE=0.004044 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003465 deg and RMSE=0.003829 deg, which indicates a numerically stable baseline run.
