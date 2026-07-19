# Wave3 2 Harmonic Residual Offset Global Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_global__polished_setpoints`
- Model Family: `wave3_2_harmonic_residual_offset_global`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-24-33__te_wave3_2_harmonic_residual_offset_global__polished_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=124-val_mae=0.00190522.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005053`
- val_mae: `0.001905`
- val_rmse: `0.002679`
- val_pointwise_loss: `0.005053`
- val_centered_curve_shape_loss: `0.004568`
- val_curve_offset_loss: `0.000485`
- val_curve_amplitude_loss: `0.032333`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.031005`
- val_structured_rmse: `0.036472`
- val_residual_offset_mean_abs: `0.030757`

## Test Metrics

- test_loss: `0.008467`
- test_mae: `0.002220`
- test_rmse: `0.003587`
- test_pointwise_loss: `0.008467`
- test_centered_curve_shape_loss: `0.005460`
- test_curve_offset_loss: `0.003007`
- test_curve_amplitude_loss: `0.043291`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.029155`
- test_structured_rmse: `0.035128`
- test_residual_offset_mean_abs: `0.028782`

## Interpretation

The held-out val error stayed finite with MAE=0.001905 deg and RMSE=0.002679 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002220 deg and RMSE=0.003587 deg, which indicates a numerically stable baseline run.
