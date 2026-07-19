# Periodic Temporal Convolution Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_fw__polished_setpoints`
- Model Family: `periodic_temporal_convolution_fw`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-19-59-14__te_periodic_temporal_convolution_fw__polished_setpoints/checkpoints/periodic_temporal_convolution-epoch=040-val_mae=0.00194544.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004880`
- val_mae: `0.001945`
- val_rmse: `0.002696`
- val_pointwise_loss: `0.004880`
- val_centered_curve_shape_loss: `0.004314`
- val_curve_offset_loss: `0.000566`
- val_curve_amplitude_loss: `0.024155`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008320`
- test_mae: `0.002252`
- test_rmse: `0.003578`
- test_pointwise_loss: `0.008320`
- test_centered_curve_shape_loss: `0.004992`
- test_curve_offset_loss: `0.003328`
- test_curve_amplitude_loss: `0.033496`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001945 deg and RMSE=0.002696 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002252 deg and RMSE=0.003578 deg, which indicates a numerically stable baseline run.
