# Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_fw`
- Model Family: `temporal_convolution_fw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution\2026-06-29-22-10-26__te_temporal_convolution_fw\checkpoints\temporal_convolution-epoch=051-val_mae=0.00233879.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006212`
- val_mae: `0.002339`
- val_rmse: `0.002893`
- val_pointwise_loss: `0.006212`
- val_centered_curve_shape_loss: `0.005546`
- val_curve_offset_loss: `0.000665`
- val_curve_amplitude_loss: `0.055131`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007273`
- test_mae: `0.002470`
- test_rmse: `0.003146`
- test_pointwise_loss: `0.007273`
- test_centered_curve_shape_loss: `0.006238`
- test_curve_offset_loss: `0.001036`
- test_curve_amplitude_loss: `0.061553`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002339 deg and RMSE=0.002893 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002470 deg and RMSE=0.003146 deg, which indicates a numerically stable baseline run.
