# Phase2 Pinn H0 Fourier Control Bw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h0_fourier_control_bw__polished_setpoints`
- Model Family: `phase2_pinn_h0_fourier_control_bw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-14-11-22__te_phase2_pinn_h0_fourier_control_bw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=005-val_mae=0.00207710.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.022198`
- val_mae: `0.002077`
- val_rmse: `0.002587`
- val_pointwise_loss: `0.017143`
- val_centered_curve_shape_loss: `0.013243`
- val_curve_offset_loss: `0.003815`
- val_curve_amplitude_loss: `0.083586`
- val_sparse_harmonic_shape_loss: `0.000282`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.024668`
- test_mae: `0.002066`
- test_rmse: `0.002643`
- test_pointwise_loss: `0.019168`
- test_centered_curve_shape_loss: `0.014220`
- test_curve_offset_loss: `0.004646`
- test_curve_amplitude_loss: `0.090423`
- test_sparse_harmonic_shape_loss: `0.000312`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002077 deg and RMSE=0.002587 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002066 deg and RMSE=0.002643 deg, which indicates a numerically stable baseline run.
