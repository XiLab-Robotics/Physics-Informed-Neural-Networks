# Periodic Temporal Convolution Global Training And Testing Report

## Overview

- Run Name: `te_periodic_temporal_convolution_global__polished_setpoints`
- Model Family: `periodic_temporal_convolution_global`
- Model Type: `periodic_temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_temporal_convolution/2026-07-08-19-44-50__te_periodic_temporal_convolution_global__polished_setpoints/checkpoints/periodic_temporal_convolution-epoch=050-val_mae=0.00196079.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004867`
- val_mae: `0.001961`
- val_rmse: `0.002706`
- val_pointwise_loss: `0.004867`
- val_centered_curve_shape_loss: `0.004340`
- val_curve_offset_loss: `0.000527`
- val_curve_amplitude_loss: `0.025695`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008162`
- test_mae: `0.002236`
- test_rmse: `0.003541`
- test_pointwise_loss: `0.008162`
- test_centered_curve_shape_loss: `0.005089`
- test_curve_offset_loss: `0.003073`
- test_curve_amplitude_loss: `0.035592`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001961 deg and RMSE=0.002706 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002236 deg and RMSE=0.003541 deg, which indicates a numerically stable baseline run.
