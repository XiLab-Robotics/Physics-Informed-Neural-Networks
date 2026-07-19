# Wave3 2 Clean Sequential Residual Offset Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_fw__simplified_setpoints`
- Model Family: `wave3_2_clean_sequential_residual_offset_fw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-12-54-53__te_wave3_2_clean_sequential_residual_offset_fw__simplified_setpoints/checkpoints/sequential_residual_offset_probe-epoch=074-val_mae=0.00371625.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011619`
- val_mae: `0.003716`
- val_rmse: `0.004620`
- val_pointwise_loss: `0.011619`
- val_centered_curve_shape_loss: `0.007404`
- val_curve_offset_loss: `0.004215`
- val_curve_amplitude_loss: `0.068533`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.027467`
- val_base_rmse: `0.032429`
- val_residual_offset_mean_abs: `0.027301`

## Test Metrics

- test_loss: `0.009249`
- test_mae: `0.003580`
- test_rmse: `0.004407`
- test_pointwise_loss: `0.009249`
- test_centered_curve_shape_loss: `0.004109`
- test_curve_offset_loss: `0.005139`
- test_curve_amplitude_loss: `0.034970`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.029578`
- test_base_rmse: `0.034226`
- test_residual_offset_mean_abs: `0.029565`

## Interpretation

The held-out val error stayed finite with MAE=0.003716 deg and RMSE=0.004620 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003580 deg and RMSE=0.004407 deg, which indicates a numerically stable baseline run.
