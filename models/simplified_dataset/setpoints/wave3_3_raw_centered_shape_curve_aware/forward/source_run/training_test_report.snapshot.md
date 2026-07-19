# Wave3 3 Raw Centered Shape Curve Aware Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-12-47__te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=119-val_mae=0.00356710.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.013171`
- val_mae: `0.003567`
- val_rmse: `0.004427`
- val_pointwise_loss: `0.010889`
- val_centered_curve_shape_loss: `0.006453`
- val_curve_offset_loss: `0.004436`
- val_curve_amplitude_loss: `0.052745`
- val_sparse_harmonic_shape_loss: `0.000153`
- val_structured_mae: `0.021759`
- val_structured_rmse: `0.026358`
- val_residual_offset_mean_abs: `0.021608`

## Test Metrics

- test_loss: `0.009532`
- test_mae: `0.003429`
- test_rmse: `0.004190`
- test_pointwise_loss: `0.008401`
- test_centered_curve_shape_loss: `0.003202`
- test_curve_offset_loss: `0.005199`
- test_curve_amplitude_loss: `0.024522`
- test_sparse_harmonic_shape_loss: `6.958596e-05`
- test_structured_mae: `0.024753`
- test_structured_rmse: `0.028792`
- test_residual_offset_mean_abs: `0.024669`

## Interpretation

The held-out val error stayed finite with MAE=0.003567 deg and RMSE=0.004427 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003429 deg and RMSE=0.004190 deg, which indicates a numerically stable baseline run.
