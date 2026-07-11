# Wave3 2 Harmonic Residual Offset Global Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_global__polished_actual_values`
- Model Family: `wave3_2_harmonic_residual_offset_global`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-04-51-02__te_wave3_2_harmonic_residual_offset_global__polished_actual_values/checkpoints/harmonic_residual_offset_probe-epoch=201-val_mae=0.00183635.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004832`
- val_mae: `0.001836`
- val_rmse: `0.002593`
- val_pointwise_loss: `0.004832`
- val_centered_curve_shape_loss: `0.004493`
- val_curve_offset_loss: `0.000338`
- val_curve_amplitude_loss: `0.035489`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.008075`
- val_structured_rmse: `0.009768`
- val_residual_offset_mean_abs: `0.007785`

## Test Metrics

- test_loss: `0.005659`
- test_mae: `0.001958`
- test_rmse: `0.003010`
- test_pointwise_loss: `0.005659`
- test_centered_curve_shape_loss: `0.005311`
- test_curve_offset_loss: `0.000348`
- test_curve_amplitude_loss: `0.040578`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.008574`
- test_structured_rmse: `0.010460`
- test_residual_offset_mean_abs: `0.008197`

## Interpretation

The held-out val error stayed finite with MAE=0.001836 deg and RMSE=0.002593 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001958 deg and RMSE=0.003010 deg, which indicates a numerically stable baseline run.
