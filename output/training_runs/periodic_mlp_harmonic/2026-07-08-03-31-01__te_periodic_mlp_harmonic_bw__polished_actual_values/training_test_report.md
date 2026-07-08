# Periodic Mlp Harmonic Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_bw__polished_actual_values`
- Model Family: `periodic_mlp_harmonic_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-03-31-01__te_periodic_mlp_harmonic_bw__polished_actual_values/checkpoints/periodic_mlp-epoch=128-val_mae=0.00117146.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001810`
- val_mae: `0.001171`
- val_rmse: `0.001653`
- val_pointwise_loss: `0.001810`
- val_centered_curve_shape_loss: `0.002525`
- val_curve_offset_loss: `0.000410`
- val_curve_amplitude_loss: `0.023631`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003101`
- test_mae: `0.001303`
- test_rmse: `0.002220`
- test_pointwise_loss: `0.003101`
- test_centered_curve_shape_loss: `0.004333`
- test_curve_offset_loss: `0.003351`
- test_curve_amplitude_loss: `0.040102`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001171 deg and RMSE=0.001653 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001303 deg and RMSE=0.002220 deg, which indicates a numerically stable baseline run.
