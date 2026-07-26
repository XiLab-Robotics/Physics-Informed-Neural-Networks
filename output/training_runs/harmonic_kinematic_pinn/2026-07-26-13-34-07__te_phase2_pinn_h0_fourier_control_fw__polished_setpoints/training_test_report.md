# Phase2 Pinn H0 Fourier Control Fw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Model Family: `phase2_pinn_h0_fourier_control_fw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-13-34-07__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=034-val_mae=0.00141771.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.009623`
- val_mae: `0.001418`
- val_rmse: `0.001741`
- val_pointwise_loss: `0.007742`
- val_centered_curve_shape_loss: `0.004643`
- val_curve_offset_loss: `0.003093`
- val_curve_amplitude_loss: `0.028613`
- val_sparse_harmonic_shape_loss: `7.367311e-05`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007723`
- test_mae: `0.001354`
- test_rmse: `0.001620`
- test_pointwise_loss: `0.006238`
- test_centered_curve_shape_loss: `0.004015`
- test_curve_offset_loss: `0.002267`
- test_curve_amplitude_loss: `0.021987`
- test_sparse_harmonic_shape_loss: `7.076084e-05`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001418 deg and RMSE=0.001741 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001354 deg and RMSE=0.001620 deg, which indicates a numerically stable baseline run.
