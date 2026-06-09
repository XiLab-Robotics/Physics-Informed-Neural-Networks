# Track2G Curve Aware Harmonic Residual Offset Raw Offset Bw Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_raw_offset_bw`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_raw_offset_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_raw_offset_bw\2026-06-08-20-51-35__te_track2g_curve_aware_raw_offset_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=076-val_mae=0.00375122.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.049199`
- val_mae: `0.003751`
- val_rmse: `0.004351`
- val_pointwise_loss: `0.042606`
- val_centered_curve_shape_loss: `0.027955`
- val_curve_offset_loss: `0.014650`
- val_curve_amplitude_loss: `0.206323`
- val_sparse_harmonic_shape_loss: `0.000675`
- val_structured_mae: `0.017045`
- val_structured_rmse: `0.018736`
- val_residual_offset_mean_abs: `0.016800`

## Test Metrics

- test_loss: `0.038368`
- test_mae: `0.003471`
- test_rmse: `0.003992`
- test_pointwise_loss: `0.030734`
- test_centered_curve_shape_loss: `0.013768`
- test_curve_offset_loss: `0.016966`
- test_curve_amplitude_loss: `0.084309`
- test_sparse_harmonic_shape_loss: `0.000311`
- test_structured_mae: `0.017336`
- test_structured_rmse: `0.019128`
- test_residual_offset_mean_abs: `0.016627`

## Interpretation

The held-out val error stayed finite with MAE=0.003751 deg and RMSE=0.004351 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003471 deg and RMSE=0.003992 deg, which indicates a numerically stable baseline run.
