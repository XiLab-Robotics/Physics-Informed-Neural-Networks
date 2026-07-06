# Wave3 1 Sequential Residual Offset Probe Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_fw`
- Model Family: `wave3_1_sequential_residual_offset_probe_fw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_1_sequential_residual_offset_probe\2026-06-30-16-25-21__te_wave3_1_sequential_residual_offset_probe_fw\checkpoints\sequential_residual_offset_probe-epoch=110-val_mae=0.00215428.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005763`
- val_mae: `0.002154`
- val_rmse: `0.002676`
- val_pointwise_loss: `0.005763`
- val_centered_curve_shape_loss: `0.005392`
- val_curve_offset_loss: `0.000371`
- val_curve_amplitude_loss: `0.059777`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.021542`
- val_base_rmse: `0.024853`
- val_residual_offset_mean_abs: `0.021437`

## Test Metrics

- test_loss: `0.006535`
- test_mae: `0.002246`
- test_rmse: `0.002893`
- test_pointwise_loss: `0.006535`
- test_centered_curve_shape_loss: `0.006193`
- test_curve_offset_loss: `0.000342`
- test_curve_amplitude_loss: `0.065535`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.020416`
- test_base_rmse: `0.023964`
- test_residual_offset_mean_abs: `0.020293`

## Interpretation

The held-out val error stayed finite with MAE=0.002154 deg and RMSE=0.002676 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002246 deg and RMSE=0.002893 deg, which indicates a numerically stable baseline run.
