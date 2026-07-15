# Wave5 1 Harmonic Prior Pointwise Control Bw Training And Testing Report

## Overview

- Run Name: `te_wave5_1_harmonic_prior_pointwise_control_bw__simplified_setpoints`
- Model Family: `wave5_1_harmonic_prior_pointwise_control_bw`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave5_1_harmonic_prior_pointwise_control/2026-07-16-00-17-20__te_wave5_1_harmonic_prior_pointwise_control_bw__simplified_setpoints/checkpoints/wave3_harmonic_prior_residual-epoch=063-val_mae=0.00364360.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010975`
- val_mae: `0.003644`
- val_rmse: `0.004498`
- val_pointwise_loss: `0.010975`
- val_centered_curve_shape_loss: `0.006376`
- val_curve_offset_loss: `0.004599`
- val_curve_amplitude_loss: `0.046060`
- val_sparse_harmonic_shape_loss: `0.000150`
- val_structured_mae: `0.043118`
- val_structured_rmse: `0.048206`

## Test Metrics

- test_loss: `0.008374`
- test_mae: `0.003434`
- test_rmse: `0.004181`
- test_pointwise_loss: `0.008374`
- test_centered_curve_shape_loss: `0.003208`
- test_curve_offset_loss: `0.005166`
- test_curve_amplitude_loss: `0.019312`
- test_sparse_harmonic_shape_loss: `6.862349e-05`
- test_structured_mae: `0.045924`
- test_structured_rmse: `0.050707`

## Interpretation

The held-out val error stayed finite with MAE=0.003644 deg and RMSE=0.004498 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003434 deg and RMSE=0.004181 deg, which indicates a numerically stable baseline run.
