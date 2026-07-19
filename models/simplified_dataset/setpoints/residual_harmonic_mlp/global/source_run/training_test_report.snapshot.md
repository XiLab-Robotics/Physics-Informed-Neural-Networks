# Residual Harmonic Mlp Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_global__simplified_setpoints`
- Model Family: `residual_harmonic_mlp_global`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-10-46-08__te_residual_harmonic_mlp_global__simplified_setpoints/checkpoints/residual_harmonic_mlp-epoch=010-val_mae=0.00315844.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008042`
- val_mae: `0.003158`
- val_rmse: `0.003753`
- val_pointwise_loss: `0.008042`
- val_centered_curve_shape_loss: `0.003073`
- val_curve_offset_loss: `0.005585`
- val_curve_amplitude_loss: `0.051683`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040555`
- val_structured_rmse: `0.042554`

## Test Metrics

- test_loss: `0.008639`
- test_mae: `0.003548`
- test_rmse: `0.004086`
- test_pointwise_loss: `0.008639`
- test_centered_curve_shape_loss: `0.002168`
- test_curve_offset_loss: `0.006423`
- test_curve_amplitude_loss: `0.041084`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039417`
- test_structured_rmse: `0.042811`

## Interpretation

The held-out val error stayed finite with MAE=0.003158 deg and RMSE=0.003753 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003548 deg and RMSE=0.004086 deg, which indicates a numerically stable baseline run.
