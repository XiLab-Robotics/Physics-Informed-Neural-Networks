# Wave3 2 Clean Sequential Residual Offset Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints`
- Model Family: `wave3_2_clean_sequential_residual_offset_fw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-12-44__te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints/checkpoints/sequential_residual_offset_probe-epoch=092-val_mae=0.00219799.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005849`
- val_mae: `0.002198`
- val_rmse: `0.003012`
- val_pointwise_loss: `0.005849`
- val_centered_curve_shape_loss: `0.005373`
- val_curve_offset_loss: `0.000475`
- val_curve_amplitude_loss: `0.057891`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026769`
- val_base_rmse: `0.031277`
- val_residual_offset_mean_abs: `0.026822`

## Test Metrics

- test_loss: `0.009330`
- test_mae: `0.002484`
- test_rmse: `0.003853`
- test_pointwise_loss: `0.009330`
- test_centered_curve_shape_loss: `0.006285`
- test_curve_offset_loss: `0.003045`
- test_curve_amplitude_loss: `0.070131`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.025250`
- test_base_rmse: `0.029995`
- test_residual_offset_mean_abs: `0.025172`

## Interpretation

The held-out val error stayed finite with MAE=0.002198 deg and RMSE=0.003012 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002484 deg and RMSE=0.003853 deg, which indicates a numerically stable baseline run.
