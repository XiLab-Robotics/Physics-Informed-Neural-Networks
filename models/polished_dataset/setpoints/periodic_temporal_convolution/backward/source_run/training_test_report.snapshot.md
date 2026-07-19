# Periodic Temporal Convolution Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_bw__polished_setpoints`
- Model Family: `periodic_temporal_convolution_bw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-20-12-10__te_periodic_temporal_convolution_bw__polished_setpoints/checkpoints/periodic_temporal_convolution-epoch=048-val_mae=0.00196877.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004922`
- val_mae: `0.001969`
- val_rmse: `0.002727`
- val_pointwise_loss: `0.004922`
- val_centered_curve_shape_loss: `0.004337`
- val_curve_offset_loss: `0.000585`
- val_curve_amplitude_loss: `0.023921`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008141`
- test_mae: `0.002264`
- test_rmse: `0.003555`
- test_pointwise_loss: `0.008141`
- test_centered_curve_shape_loss: `0.004984`
- test_curve_offset_loss: `0.003157`
- test_curve_amplitude_loss: `0.033801`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001969 deg and RMSE=0.002727 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002264 deg and RMSE=0.003555 deg, which indicates a numerically stable baseline run.
