# Periodic Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_fw`
- Model Family: `periodic_temporal_convolution_fw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_temporal_convolution\2026-06-30-01-43-44__te_periodic_temporal_convolution_fw\checkpoints\periodic_temporal_convolution-epoch=076-val_mae=0.00220865.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005423`
- val_mae: `0.002209`
- val_rmse: `0.002667`
- val_pointwise_loss: `0.005423`
- val_centered_curve_shape_loss: `0.004508`
- val_curve_offset_loss: `0.000914`
- val_curve_amplitude_loss: `0.028449`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006042`
- test_mae: `0.002280`
- test_rmse: `0.002848`
- test_pointwise_loss: `0.006042`
- test_centered_curve_shape_loss: `0.005149`
- test_curve_offset_loss: `0.000893`
- test_curve_amplitude_loss: `0.032710`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002209 deg and RMSE=0.002667 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002280 deg and RMSE=0.002848 deg, which indicates a numerically stable baseline run.
