# Periodic Mlp Harmonic Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_bw__simplified_setpoints`
- Model Family: `periodic_mlp_harmonic_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-01-19-22__te_periodic_mlp_harmonic_bw__simplified_setpoints/checkpoints/periodic_mlp-epoch=053-val_mae=0.00280310.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006649`
- val_mae: `0.002803`
- val_rmse: `0.003472`
- val_pointwise_loss: `0.006649`
- val_centered_curve_shape_loss: `0.002773`
- val_curve_offset_loss: `0.004955`
- val_curve_amplitude_loss: `0.030666`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007942`
- test_mae: `0.003377`
- test_rmse: `0.004054`
- test_pointwise_loss: `0.007942`
- test_centered_curve_shape_loss: `0.002448`
- test_curve_offset_loss: `0.006087`
- test_curve_amplitude_loss: `0.028299`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002803 deg and RMSE=0.003472 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003377 deg and RMSE=0.004054 deg, which indicates a numerically stable baseline run.
