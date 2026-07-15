# Wave5 1 Harmonic Prior Pointwise Control Fw Training And Testing Report

## Overview

- Run Name: `te_wave5_1_harmonic_prior_pointwise_control_fw__simplified_setpoints`
- Model Family: `wave5_1_harmonic_prior_pointwise_control_fw`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-15-23-51-01__te_wave5_1_harmonic_prior_pointwise_control_fw__simplified_setpoints/checkpoints/wave3_harmonic_prior_residual-epoch=223-val_mae=0.00356285.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010616`
- val_mae: `0.003563`
- val_rmse: `0.004405`
- val_pointwise_loss: `0.010616`
- val_centered_curve_shape_loss: `0.006341`
- val_curve_offset_loss: `0.004275`
- val_curve_amplitude_loss: `0.046722`
- val_sparse_harmonic_shape_loss: `0.000150`
- val_structured_mae: `0.021279`
- val_structured_rmse: `0.025251`

## Test Metrics

- test_loss: `0.008120`
- test_mae: `0.003386`
- test_rmse: `0.004122`
- test_pointwise_loss: `0.008120`
- test_centered_curve_shape_loss: `0.003130`
- test_curve_offset_loss: `0.004989`
- test_curve_amplitude_loss: `0.020256`
- test_sparse_harmonic_shape_loss: `6.756214e-05`
- test_structured_mae: `0.023410`
- test_structured_rmse: `0.026813`

## Interpretation

The held-out val error stayed finite with MAE=0.003563 deg and RMSE=0.004405 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003386 deg and RMSE=0.004122 deg, which indicates a numerically stable baseline run.
