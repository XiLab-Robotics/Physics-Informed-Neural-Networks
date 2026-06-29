# Periodic Mlp Harmonic Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_bw`
- Model Family: `periodic_mlp_harmonic_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp_harmonic\2026-06-26-05-40-23__te_periodic_mlp_harmonic_bw\checkpoints\periodic_mlp-epoch=126-val_mae=0.00110253.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001723`
- val_mae: `0.001103`
- val_rmse: `0.001442`
- val_pointwise_loss: `0.001723`
- val_centered_curve_shape_loss: `0.002078`
- val_curve_offset_loss: `0.000315`
- val_curve_amplitude_loss: `0.017442`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.002977`
- test_mae: `0.001279`
- test_rmse: `0.001719`
- test_pointwise_loss: `0.002977`
- test_centered_curve_shape_loss: `0.002861`
- test_curve_offset_loss: `0.001176`
- test_curve_amplitude_loss: `0.026171`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001103 deg and RMSE=0.001442 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001279 deg and RMSE=0.001719 deg, which indicates a numerically stable baseline run.
