# Wave3 3 Curve Aware Pointwise Control Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints`
- Model Family: `wave3_3_curve_aware_pointwise_control_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-08-23-30__te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=105-val_mae=0.00363045.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011104`
- val_mae: `0.003630`
- val_rmse: `0.004495`
- val_pointwise_loss: `0.011104`
- val_centered_curve_shape_loss: `0.006435`
- val_curve_offset_loss: `0.004669`
- val_curve_amplitude_loss: `0.047514`
- val_sparse_harmonic_shape_loss: `0.000152`
- val_structured_mae: `0.023464`
- val_structured_rmse: `0.029088`
- val_residual_offset_mean_abs: `0.022807`

## Test Metrics

- test_loss: `0.008654`
- test_mae: `0.003495`
- test_rmse: `0.004252`
- test_pointwise_loss: `0.008654`
- test_centered_curve_shape_loss: `0.003216`
- test_curve_offset_loss: `0.005437`
- test_curve_amplitude_loss: `0.020353`
- test_sparse_harmonic_shape_loss: `6.945315e-05`
- test_structured_mae: `0.025283`
- test_structured_rmse: `0.031369`
- test_residual_offset_mean_abs: `0.024412`

## Interpretation

The held-out val error stayed finite with MAE=0.003630 deg and RMSE=0.004495 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003495 deg and RMSE=0.004252 deg, which indicates a numerically stable baseline run.
