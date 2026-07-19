# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_bw__polished_actual_values`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-14-15-24__te_residual_harmonic_mlp_bw__polished_actual_values/checkpoints/residual_harmonic_mlp-epoch=075-val_mae=0.00160615.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002696`
- val_mae: `0.001606`
- val_rmse: `0.002068`
- val_pointwise_loss: `0.002696`
- val_centered_curve_shape_loss: `0.003079`
- val_curve_offset_loss: `0.000318`
- val_curve_amplitude_loss: `0.047596`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040322`
- val_structured_rmse: `0.043858`

## Test Metrics

- test_loss: `0.004138`
- test_mae: `0.001771`
- test_rmse: `0.002344`
- test_pointwise_loss: `0.004138`
- test_centered_curve_shape_loss: `0.003884`
- test_curve_offset_loss: `0.001328`
- test_curve_amplitude_loss: `0.059836`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039690`
- test_structured_rmse: `0.043694`

## Interpretation

The held-out val error stayed finite with MAE=0.001606 deg and RMSE=0.002068 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001771 deg and RMSE=0.002344 deg, which indicates a numerically stable baseline run.
