# Residual Harmonic Mlp Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_global__polished_actual_values`
- Model Family: `residual_harmonic_mlp_global`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-13-20-06__te_residual_harmonic_mlp_global__polished_actual_values/checkpoints/residual_harmonic_mlp-epoch=077-val_mae=0.00160259.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002703`
- val_mae: `0.001603`
- val_rmse: `0.002074`
- val_pointwise_loss: `0.002703`
- val_centered_curve_shape_loss: `0.003079`
- val_curve_offset_loss: `0.000317`
- val_curve_amplitude_loss: `0.046385`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040331`
- val_structured_rmse: `0.043867`

## Test Metrics

- test_loss: `0.004184`
- test_mae: `0.001795`
- test_rmse: `0.002375`
- test_pointwise_loss: `0.004184`
- test_centered_curve_shape_loss: `0.003887`
- test_curve_offset_loss: `0.001345`
- test_curve_amplitude_loss: `0.058604`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039626`
- test_structured_rmse: `0.043600`

## Interpretation

The held-out val error stayed finite with MAE=0.001603 deg and RMSE=0.002074 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001795 deg and RMSE=0.002375 deg, which indicates a numerically stable baseline run.
