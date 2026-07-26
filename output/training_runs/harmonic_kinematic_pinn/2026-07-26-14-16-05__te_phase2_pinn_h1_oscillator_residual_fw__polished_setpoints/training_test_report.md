# Phase2 Pinn H1 Oscillator Residual Fw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h1_oscillator_residual_fw__polished_setpoints`
- Model Family: `phase2_pinn_h1_oscillator_residual_fw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-14-16-05__te_phase2_pinn_h1_oscillator_residual_fw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=005-val_mae=0.00212674.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.017803`
- val_mae: `0.002127`
- val_rmse: `0.002614`
- val_pointwise_loss: `0.014333`
- val_centered_curve_shape_loss: `0.007518`
- val_curve_offset_loss: `0.006806`
- val_curve_amplitude_loss: `0.046911`
- val_sparse_harmonic_shape_loss: `0.000129`
- val_physics_oscillator_residual_loss: `0.025360`
- val_physics_periodic_value_loss: `0.000750`
- val_physics_periodic_slope_loss: `0.841197`
- val_physics_analytical_anchor_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.016388`
- test_mae: `0.001951`
- test_rmse: `0.002401`
- test_pointwise_loss: `0.012850`
- test_centered_curve_shape_loss: `0.007734`
- test_curve_offset_loss: `0.005060`
- test_curve_amplitude_loss: `0.051393`
- test_sparse_harmonic_shape_loss: `0.000148`
- test_physics_oscillator_residual_loss: `0.025851`
- test_physics_periodic_value_loss: `0.000832`
- test_physics_periodic_slope_loss: `0.900529`
- test_physics_analytical_anchor_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002127 deg and RMSE=0.002614 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001951 deg and RMSE=0.002401 deg, which indicates a numerically stable baseline run.
