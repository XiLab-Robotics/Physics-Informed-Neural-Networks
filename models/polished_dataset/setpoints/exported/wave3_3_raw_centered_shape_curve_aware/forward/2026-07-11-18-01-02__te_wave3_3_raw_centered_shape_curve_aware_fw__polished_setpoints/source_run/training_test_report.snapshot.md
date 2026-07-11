# Wave3 3 Raw Centered Shape Curve Aware Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-01-02__te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=068-val_mae=0.00194145.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006744`
- val_mae: `0.001941`
- val_rmse: `0.002714`
- val_pointwise_loss: `0.005119`
- val_centered_curve_shape_loss: `0.004599`
- val_curve_offset_loss: `0.000520`
- val_curve_amplitude_loss: `0.032592`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.050796`
- val_structured_rmse: `0.056479`
- val_residual_offset_mean_abs: `0.050953`

## Test Metrics

- test_loss: `0.010675`
- test_mae: `0.002276`
- test_rmse: `0.003645`
- test_pointwise_loss: `0.008735`
- test_centered_curve_shape_loss: `0.005496`
- test_curve_offset_loss: `0.003239`
- test_curve_amplitude_loss: `0.042476`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.049129`
- test_structured_rmse: `0.055340`
- test_residual_offset_mean_abs: `0.049136`

## Interpretation

The held-out val error stayed finite with MAE=0.001941 deg and RMSE=0.002714 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002276 deg and RMSE=0.003645 deg, which indicates a numerically stable baseline run.
