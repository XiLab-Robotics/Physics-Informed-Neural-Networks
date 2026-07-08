# Temporal Convolution Global Training And Testing Report

## Overview

- Run Name: `te_temporal_convolution_global__polished_actual_values`
- Model Family: `temporal_convolution_global`
- Model Type: `temporal_convolution`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/temporal_convolution/2026-07-08-09-55-29__te_temporal_convolution_global__polished_actual_values/checkpoints/temporal_convolution-epoch=106-val_mae=0.00219077.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005863`
- val_mae: `0.002191`
- val_rmse: `0.003025`
- val_pointwise_loss: `0.005863`
- val_centered_curve_shape_loss: `0.005405`
- val_curve_offset_loss: `0.000457`
- val_curve_amplitude_loss: `0.055354`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006764`
- test_mae: `0.002327`
- test_rmse: `0.003391`
- test_pointwise_loss: `0.006764`
- test_centered_curve_shape_loss: `0.006253`
- test_curve_offset_loss: `0.000511`
- test_curve_amplitude_loss: `0.061512`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002191 deg and RMSE=0.003025 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002327 deg and RMSE=0.003391 deg, which indicates a numerically stable baseline run.
