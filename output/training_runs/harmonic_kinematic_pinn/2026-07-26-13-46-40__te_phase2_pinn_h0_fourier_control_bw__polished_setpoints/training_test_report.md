# Phase2 Pinn H0 Fourier Control Bw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h0_fourier_control_bw__polished_setpoints`
- Model Family: `phase2_pinn_h0_fourier_control_bw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-13-46-40__te_phase2_pinn_h0_fourier_control_bw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=026-val_mae=0.00162406.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.013138`
- val_mae: `0.001624`
- val_rmse: `0.001979`
- val_pointwise_loss: `0.010506`
- val_centered_curve_shape_loss: `0.007981`
- val_curve_offset_loss: `0.002508`
- val_curve_amplitude_loss: `0.039657`
- val_sparse_harmonic_shape_loss: `0.000162`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.012041`
- test_mae: `0.001498`
- test_rmse: `0.001809`
- test_pointwise_loss: `0.009647`
- test_centered_curve_shape_loss: `0.006958`
- test_curve_offset_loss: `0.002809`
- test_curve_amplitude_loss: `0.035787`
- test_sparse_harmonic_shape_loss: `0.000143`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001624 deg and RMSE=0.001979 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001498 deg and RMSE=0.001809 deg, which indicates a numerically stable baseline run.
