# Wave5 1 Harmonic Prior Pointwise Control Global Training And Testing Report

## Overview

- Run Name: `te_wave5_1_harmonic_prior_pointwise_control_global__simplified_setpoints`
- Model Family: `wave5_1_harmonic_prior_pointwise_control_global`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-15-23-32-06__te_wave5_1_harmonic_prior_pointwise_control_global__simplified_setpoints/checkpoints/wave3_harmonic_prior_residual-epoch=120-val_mae=0.00359724.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010645`
- val_mae: `0.003597`
- val_rmse: `0.004400`
- val_pointwise_loss: `0.010645`
- val_centered_curve_shape_loss: `0.006319`
- val_curve_offset_loss: `0.004326`
- val_curve_amplitude_loss: `0.046013`
- val_sparse_harmonic_shape_loss: `0.000149`
- val_structured_mae: `0.029513`
- val_structured_rmse: `0.035384`

## Test Metrics

- test_loss: `0.008163`
- test_mae: `0.003417`
- test_rmse: `0.004130`
- test_pointwise_loss: `0.008163`
- test_centered_curve_shape_loss: `0.003149`
- test_curve_offset_loss: `0.005014`
- test_curve_amplitude_loss: `0.019611`
- test_sparse_harmonic_shape_loss: `6.810375e-05`
- test_structured_mae: `0.032526`
- test_structured_rmse: `0.038208`

## Interpretation

The held-out val error stayed finite with MAE=0.003597 deg and RMSE=0.004400 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003417 deg and RMSE=0.004130 deg, which indicates a numerically stable baseline run.
