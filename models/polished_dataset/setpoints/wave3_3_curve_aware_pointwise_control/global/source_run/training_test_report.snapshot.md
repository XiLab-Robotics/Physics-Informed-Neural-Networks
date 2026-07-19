# Wave3 3 Curve Aware Pointwise Control Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_global__polished_setpoints`
- Model Family: `wave3_3_curve_aware_pointwise_control_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-11-00-32__te_wave3_3_curve_aware_pointwise_control_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=141-val_mae=0.00193127.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005039`
- val_mae: `0.001931`
- val_rmse: `0.002696`
- val_pointwise_loss: `0.005039`
- val_centered_curve_shape_loss: `0.004554`
- val_curve_offset_loss: `0.000485`
- val_curve_amplitude_loss: `0.032194`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.034264`
- val_structured_rmse: `0.038608`
- val_residual_offset_mean_abs: `0.034228`

## Test Metrics

- test_loss: `0.008563`
- test_mae: `0.002241`
- test_rmse: `0.003595`
- test_pointwise_loss: `0.008563`
- test_centered_curve_shape_loss: `0.005427`
- test_curve_offset_loss: `0.003136`
- test_curve_amplitude_loss: `0.042560`
- test_sparse_harmonic_shape_loss: `0.000109`
- test_structured_mae: `0.031168`
- test_structured_rmse: `0.036193`
- test_residual_offset_mean_abs: `0.030957`

## Interpretation

The held-out val error stayed finite with MAE=0.001931 deg and RMSE=0.002696 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002241 deg and RMSE=0.003595 deg, which indicates a numerically stable baseline run.
