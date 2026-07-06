# Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_bw`
- Model Family: `temporal_convolution_bw`
- Model Type: `temporal_convolution`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\temporal_convolution\2026-06-29-22-25-32__te_temporal_convolution_bw\checkpoints\temporal_convolution-epoch=100-val_mae=0.00223589.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005941`
- val_mae: `0.002236`
- val_rmse: `0.002765`
- val_pointwise_loss: `0.005941`
- val_centered_curve_shape_loss: `0.005431`
- val_curve_offset_loss: `0.000511`
- val_curve_amplitude_loss: `0.054835`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006751`
- test_mae: `0.002348`
- test_rmse: `0.002988`
- test_pointwise_loss: `0.006751`
- test_centered_curve_shape_loss: `0.006236`
- test_curve_offset_loss: `0.000515`
- test_curve_amplitude_loss: `0.060769`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002236 deg and RMSE=0.002765 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002348 deg and RMSE=0.002988 deg, which indicates a numerically stable baseline run.
