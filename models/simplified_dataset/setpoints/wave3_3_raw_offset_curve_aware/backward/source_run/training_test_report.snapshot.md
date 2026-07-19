# Wave3 3 Raw Offset Curve Aware Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints`
- Model Family: `wave3_3_raw_offset_curve_aware_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-22-59-48__te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=145-val_mae=0.00357142.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012676`
- val_mae: `0.003571`
- val_rmse: `0.004401`
- val_pointwise_loss: `0.010722`
- val_centered_curve_shape_loss: `0.006381`
- val_curve_offset_loss: `0.004341`
- val_curve_amplitude_loss: `0.046935`
- val_sparse_harmonic_shape_loss: `0.000151`
- val_structured_mae: `0.044255`
- val_structured_rmse: `0.050844`
- val_residual_offset_mean_abs: `0.044004`

## Test Metrics

- test_loss: `0.010710`
- test_mae: `0.003400`
- test_rmse: `0.004187`
- test_pointwise_loss: `0.008371`
- test_centered_curve_shape_loss: `0.003171`
- test_curve_offset_loss: `0.005199`
- test_curve_amplitude_loss: `0.020479`
- test_sparse_harmonic_shape_loss: `6.864850e-05`
- test_structured_mae: `0.047037`
- test_structured_rmse: `0.053520`
- test_residual_offset_mean_abs: `0.047117`

## Interpretation

The held-out val error stayed finite with MAE=0.003571 deg and RMSE=0.004401 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003400 deg and RMSE=0.004187 deg, which indicates a numerically stable baseline run.
