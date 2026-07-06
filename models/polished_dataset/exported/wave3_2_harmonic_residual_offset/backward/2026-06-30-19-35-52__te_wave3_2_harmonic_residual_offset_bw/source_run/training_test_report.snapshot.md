# Wave3 2 Harmonic Residual Offset Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_bw`
- Model Family: `wave3_2_harmonic_residual_offset_bw`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_harmonic_residual_offset\2026-06-30-19-35-52__te_wave3_2_harmonic_residual_offset_bw\checkpoints\harmonic_residual_offset_probe-epoch=192-val_mae=0.00179089.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004921`
- val_mae: `0.001791`
- val_rmse: `0.002208`
- val_pointwise_loss: `0.004921`
- val_centered_curve_shape_loss: `0.004631`
- val_curve_offset_loss: `0.000289`
- val_curve_amplitude_loss: `0.036126`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.006684`
- val_structured_rmse: `0.007115`
- val_residual_offset_mean_abs: `0.006276`

## Test Metrics

- test_loss: `0.005649`
- test_mae: `0.001894`
- test_rmse: `0.002440`
- test_pointwise_loss: `0.005649`
- test_centered_curve_shape_loss: `0.005430`
- test_curve_offset_loss: `0.000219`
- test_curve_amplitude_loss: `0.041335`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.006415`
- test_structured_rmse: `0.007049`
- test_residual_offset_mean_abs: `0.005929`

## Interpretation

The held-out val error stayed finite with MAE=0.001791 deg and RMSE=0.002208 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001894 deg and RMSE=0.002440 deg, which indicates a numerically stable baseline run.
