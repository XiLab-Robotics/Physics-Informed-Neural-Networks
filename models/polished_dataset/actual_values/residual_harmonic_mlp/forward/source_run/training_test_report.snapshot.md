# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_fw__polished_actual_values`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-13-50-19__te_residual_harmonic_mlp_fw__polished_actual_values/checkpoints/residual_harmonic_mlp-epoch=052-val_mae=0.00163893.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002788`
- val_mae: `0.001639`
- val_rmse: `0.002117`
- val_pointwise_loss: `0.002788`
- val_centered_curve_shape_loss: `0.003080`
- val_curve_offset_loss: `0.000425`
- val_curve_amplitude_loss: `0.045794`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040331`
- val_structured_rmse: `0.043867`

## Test Metrics

- test_loss: `0.004240`
- test_mae: `0.001816`
- test_rmse: `0.002399`
- test_pointwise_loss: `0.004240`
- test_centered_curve_shape_loss: `0.003877`
- test_curve_offset_loss: `0.001428`
- test_curve_amplitude_loss: `0.058119`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039625`
- test_structured_rmse: `0.043598`

## Interpretation

The held-out val error stayed finite with MAE=0.001639 deg and RMSE=0.002117 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001816 deg and RMSE=0.002399 deg, which indicates a numerically stable baseline run.
