# Periodic Mlp Harmonic Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_bw__polished_setpoints`
- Model Family: `periodic_mlp_harmonic_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_mlp_harmonic/2026-07-08-02-29-32__te_periodic_mlp_harmonic_bw__polished_setpoints/checkpoints/periodic_mlp-epoch=081-val_mae=0.00121896.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001951`
- val_mae: `0.001219`
- val_rmse: `0.001732`
- val_pointwise_loss: `0.001951`
- val_centered_curve_shape_loss: `0.002456`
- val_curve_offset_loss: `0.000625`
- val_curve_amplitude_loss: `0.026840`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003321`
- test_mae: `0.001442`
- test_rmse: `0.002380`
- test_pointwise_loss: `0.003321`
- test_centered_curve_shape_loss: `0.004281`
- test_curve_offset_loss: `0.003655`
- test_curve_amplitude_loss: `0.046497`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001219 deg and RMSE=0.001732 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001442 deg and RMSE=0.002380 deg, which indicates a numerically stable baseline run.
