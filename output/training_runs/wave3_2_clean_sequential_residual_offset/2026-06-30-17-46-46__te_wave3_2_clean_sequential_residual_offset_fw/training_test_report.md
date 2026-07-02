# Wave3 2 Clean Sequential Residual Offset Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_fw`
- Model Family: `wave3_2_clean_sequential_residual_offset_fw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_clean_sequential_residual_offset\2026-06-30-17-46-46__te_wave3_2_clean_sequential_residual_offset_fw\checkpoints\sequential_residual_offset_probe-epoch=127-val_mae=0.00215929.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005761`
- val_mae: `0.002159`
- val_rmse: `0.002681`
- val_pointwise_loss: `0.005761`
- val_centered_curve_shape_loss: `0.005389`
- val_curve_offset_loss: `0.000372`
- val_curve_amplitude_loss: `0.056989`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.021063`
- val_base_rmse: `0.024344`
- val_residual_offset_mean_abs: `0.020883`

## Test Metrics

- test_loss: `0.006542`
- test_mae: `0.002258`
- test_rmse: `0.002897`
- test_pointwise_loss: `0.006542`
- test_centered_curve_shape_loss: `0.006207`
- test_curve_offset_loss: `0.000334`
- test_curve_amplitude_loss: `0.063258`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.020001`
- test_base_rmse: `0.023549`
- test_residual_offset_mean_abs: `0.019841`

## Interpretation

The held-out val error stayed finite with MAE=0.002159 deg and RMSE=0.002681 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002258 deg and RMSE=0.002897 deg, which indicates a numerically stable baseline run.
