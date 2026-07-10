# Wave3 2 Harmonic Residual Offset Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_bw__polished_setpoints`
- Model Family: `wave3_2_harmonic_residual_offset_bw`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-01-14-42__te_wave3_2_harmonic_residual_offset_bw__polished_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=120-val_mae=0.00193287.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005081`
- val_mae: `0.001933`
- val_rmse: `0.002702`
- val_pointwise_loss: `0.005081`
- val_centered_curve_shape_loss: `0.004604`
- val_curve_offset_loss: `0.000477`
- val_curve_amplitude_loss: `0.032181`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.024931`
- val_structured_rmse: `0.029272`
- val_residual_offset_mean_abs: `0.025132`

## Test Metrics

- test_loss: `0.008505`
- test_mae: `0.002256`
- test_rmse: `0.003593`
- test_pointwise_loss: `0.008505`
- test_centered_curve_shape_loss: `0.005470`
- test_curve_offset_loss: `0.003035`
- test_curve_amplitude_loss: `0.042755`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.025897`
- test_structured_rmse: `0.029956`
- test_residual_offset_mean_abs: `0.025862`

## Interpretation

The held-out val error stayed finite with MAE=0.001933 deg and RMSE=0.002702 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002256 deg and RMSE=0.003593 deg, which indicates a numerically stable baseline run.
