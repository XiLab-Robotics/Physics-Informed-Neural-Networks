# Temporal Convolution Global Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_global`
- Model Family: `temporal_convolution_global`
- Model Type: `temporal_convolution`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution\2026-06-29-21-48-10__te_temporal_convolution_global\checkpoints\temporal_convolution-epoch=111-val_mae=0.00229596.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006151`
- val_mae: `0.002296`
- val_rmse: `0.002848`
- val_pointwise_loss: `0.006151`
- val_centered_curve_shape_loss: `0.005425`
- val_curve_offset_loss: `0.000726`
- val_curve_amplitude_loss: `0.057377`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006863`
- test_mae: `0.002385`
- test_rmse: `0.003048`
- test_pointwise_loss: `0.006863`
- test_centered_curve_shape_loss: `0.006192`
- test_curve_offset_loss: `0.000671`
- test_curve_amplitude_loss: `0.063929`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002296 deg and RMSE=0.002848 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002385 deg and RMSE=0.003048 deg, which indicates a numerically stable baseline run.
