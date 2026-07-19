# Periodic Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_fw__simplified_setpoints`
- Model Family: `periodic_temporal_convolution_fw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-19-19-28__te_periodic_temporal_convolution_fw__simplified_setpoints/checkpoints/periodic_temporal_convolution-epoch=050-val_mae=0.00364466.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010608`
- val_mae: `0.003645`
- val_rmse: `0.004463`
- val_pointwise_loss: `0.010608`
- val_centered_curve_shape_loss: `0.006021`
- val_curve_offset_loss: `0.004587`
- val_curve_amplitude_loss: `0.039749`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008344`
- test_mae: `0.003474`
- test_rmse: `0.004188`
- test_pointwise_loss: `0.008344`
- test_centered_curve_shape_loss: `0.002982`
- test_curve_offset_loss: `0.005362`
- test_curve_amplitude_loss: `0.015289`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003645 deg and RMSE=0.004463 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003474 deg and RMSE=0.004188 deg, which indicates a numerically stable baseline run.
