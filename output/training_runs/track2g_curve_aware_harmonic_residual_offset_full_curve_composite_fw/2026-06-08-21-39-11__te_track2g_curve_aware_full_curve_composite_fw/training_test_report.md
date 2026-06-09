# Track2G Curve Aware Harmonic Residual Offset Full Curve Composite Fw Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_full_curve_composite_fw`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw\2026-06-08-21-39-11__te_track2g_curve_aware_full_curve_composite_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=034-val_mae=0.00332007.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.048175`
- val_mae: `0.003320`
- val_rmse: `0.003801`
- val_pointwise_loss: `0.031927`
- val_centered_curve_shape_loss: `0.015781`
- val_curve_offset_loss: `0.016146`
- val_curve_amplitude_loss: `0.066001`
- val_sparse_harmonic_shape_loss: `0.000346`
- val_structured_mae: `0.015151`
- val_structured_rmse: `0.016838`
- val_residual_offset_mean_abs: `0.015086`

## Test Metrics

- test_loss: `0.038297`
- test_mae: `0.003260`
- test_rmse: `0.003630`
- test_pointwise_loss: `0.026854`
- test_centered_curve_shape_loss: `0.008107`
- test_curve_offset_loss: `0.018747`
- test_curve_amplitude_loss: `0.028319`
- test_sparse_harmonic_shape_loss: `0.000152`
- test_structured_mae: `0.015176`
- test_structured_rmse: `0.017321`
- test_residual_offset_mean_abs: `0.015249`

## Interpretation

The held-out val error stayed finite with MAE=0.003320 deg and RMSE=0.003801 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003260 deg and RMSE=0.003630 deg, which indicates a numerically stable baseline run.
