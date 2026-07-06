# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_fw`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-06-26-01-57-07__te_periodic_mlp_fw\checkpoints\periodic_mlp-epoch=144-val_mae=0.00159747.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002682`
- val_mae: `0.001597`
- val_rmse: `0.002061`
- val_pointwise_loss: `0.002682`
- val_centered_curve_shape_loss: `0.003081`
- val_curve_offset_loss: `0.000308`
- val_curve_amplitude_loss: `0.046714`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004030`
- test_mae: `0.001742`
- test_rmse: `0.002329`
- test_pointwise_loss: `0.004030`
- test_centered_curve_shape_loss: `0.004035`
- test_curve_offset_loss: `0.001071`
- test_curve_amplitude_loss: `0.060019`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001597 deg and RMSE=0.002061 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001742 deg and RMSE=0.002329 deg, which indicates a numerically stable baseline run.
