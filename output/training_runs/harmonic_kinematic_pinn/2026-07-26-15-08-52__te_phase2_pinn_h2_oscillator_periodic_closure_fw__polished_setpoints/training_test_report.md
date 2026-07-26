# Phase2 Pinn H2 Oscillator Periodic Closure Fw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h2_oscillator_periodic_closure_fw__polished_setpoints`
- Model Family: `phase2_pinn_h2_oscillator_periodic_closure_fw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-15-08-52__te_phase2_pinn_h2_oscillator_periodic_closure_fw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=012-val_mae=0.00207442.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.018763`
- val_mae: `0.002074`
- val_rmse: `0.002610`
- val_pointwise_loss: `0.015491`
- val_centered_curve_shape_loss: `0.007768`
- val_curve_offset_loss: `0.007695`
- val_curve_amplitude_loss: `0.041044`
- val_sparse_harmonic_shape_loss: `0.000137`
- val_physics_oscillator_residual_loss: `0.016970`
- val_physics_periodic_value_loss: `0.002121`
- val_physics_periodic_slope_loss: `0.001526`
- val_physics_analytical_anchor_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.015281`
- test_mae: `0.001784`
- test_rmse: `0.002245`
- test_pointwise_loss: `0.011937`
- test_centered_curve_shape_loss: `0.007991`
- test_curve_offset_loss: `0.003865`
- test_curve_amplitude_loss: `0.049437`
- test_sparse_harmonic_shape_loss: `0.000156`
- test_physics_oscillator_residual_loss: `0.018614`
- test_physics_periodic_value_loss: `0.002293`
- test_physics_periodic_slope_loss: `0.001295`
- test_physics_analytical_anchor_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002074 deg and RMSE=0.002610 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001784 deg and RMSE=0.002245 deg, which indicates a numerically stable baseline run.
