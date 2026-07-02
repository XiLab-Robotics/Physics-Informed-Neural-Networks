# Wave3 1 Sequential Residual Offset Probe Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_bw`
- Model Family: `wave3_1_sequential_residual_offset_probe_bw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_1_sequential_residual_offset_probe\2026-06-30-16-49-34__te_wave3_1_sequential_residual_offset_probe_bw\checkpoints\sequential_residual_offset_probe-epoch=152-val_mae=0.00214684.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005756`
- val_mae: `0.002147`
- val_rmse: `0.002668`
- val_pointwise_loss: `0.005756`
- val_centered_curve_shape_loss: `0.005380`
- val_curve_offset_loss: `0.000375`
- val_curve_amplitude_loss: `0.057334`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.020985`
- val_base_rmse: `0.024314`
- val_residual_offset_mean_abs: `0.020618`

## Test Metrics

- test_loss: `0.006488`
- test_mae: `0.002225`
- test_rmse: `0.002871`
- test_pointwise_loss: `0.006488`
- test_centered_curve_shape_loss: `0.006171`
- test_curve_offset_loss: `0.000317`
- test_curve_amplitude_loss: `0.063266`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.019923`
- test_base_rmse: `0.023433`
- test_residual_offset_mean_abs: `0.019579`

## Interpretation

The held-out val error stayed finite with MAE=0.002147 deg and RMSE=0.002668 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002225 deg and RMSE=0.002871 deg, which indicates a numerically stable baseline run.
