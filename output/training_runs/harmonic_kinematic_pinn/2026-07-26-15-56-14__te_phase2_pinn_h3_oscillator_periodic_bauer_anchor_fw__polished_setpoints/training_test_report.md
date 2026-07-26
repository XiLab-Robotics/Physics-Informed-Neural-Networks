# Phase2 Pinn H3 Oscillator Periodic Bauer Anchor Fw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_fw__polished_setpoints`
- Model Family: `phase2_pinn_h3_oscillator_periodic_bauer_anchor_fw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-15-56-14__te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_fw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=007-val_mae=0.00289816.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.631176`
- val_mae: `0.002898`
- val_rmse: `0.003573`
- val_pointwise_loss: `0.028940`
- val_centered_curve_shape_loss: `0.008729`
- val_curve_offset_loss: `0.020031`
- val_curve_amplitude_loss: `0.047430`
- val_sparse_harmonic_shape_loss: `0.000160`
- val_physics_oscillator_residual_loss: `0.021700`
- val_physics_periodic_value_loss: `0.004989`
- val_physics_periodic_slope_loss: `0.001638`
- val_physics_analytical_anchor_loss: `11.950954`

## Test Metrics

- test_loss: `0.475014`
- test_mae: `0.002389`
- test_rmse: `0.003042`
- test_pointwise_loss: `0.019906`
- test_centered_curve_shape_loss: `0.008966`
- test_curve_offset_loss: `0.010773`
- test_curve_amplitude_loss: `0.062595`
- test_sparse_harmonic_shape_loss: `0.000180`
- test_physics_oscillator_residual_loss: `0.022070`
- test_physics_periodic_value_loss: `0.005010`
- test_physics_periodic_slope_loss: `0.001813`
- test_physics_analytical_anchor_loss: `9.010452`

## Interpretation

The held-out val error stayed finite with MAE=0.002898 deg and RMSE=0.003573 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002389 deg and RMSE=0.003042 deg, which indicates a numerically stable baseline run.
