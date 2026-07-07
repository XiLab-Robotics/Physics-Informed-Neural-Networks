# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_bw__polished_setpoints`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-12-36-55__te_residual_harmonic_mlp_bw__polished_setpoints/checkpoints/residual_harmonic_mlp-epoch=093-val_mae=0.00162645.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002736`
- val_mae: `0.001626`
- val_rmse: `0.002082`
- val_pointwise_loss: `0.002736`
- val_centered_curve_shape_loss: `0.003036`
- val_curve_offset_loss: `0.000368`
- val_curve_amplitude_loss: `0.053932`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040344`
- val_structured_rmse: `0.043885`

## Test Metrics

- test_loss: `0.004021`
- test_mae: `0.001725`
- test_rmse: `0.002305`
- test_pointwise_loss: `0.004021`
- test_centered_curve_shape_loss: `0.003784`
- test_curve_offset_loss: `0.001305`
- test_curve_amplitude_loss: `0.067043`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039549`
- test_structured_rmse: `0.043482`

## Interpretation

The held-out val error stayed finite with MAE=0.001626 deg and RMSE=0.002082 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001725 deg and RMSE=0.002305 deg, which indicates a numerically stable baseline run.
