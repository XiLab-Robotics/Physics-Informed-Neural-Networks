# Phase3 Pinn C0 Learned Mean Control Bw Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c0_learned_mean_control_bw__polished_setpoints`
- Model Family: `phase3_pinn_c0_learned_mean_control_bw`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-17-53-30__te_phase3_pinn_c0_learned_mean_control_bw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=019-val_mae=0.00192717.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.019662`
- val_mae: `0.001927`
- val_rmse: `0.002392`
- val_pointwise_loss: `0.015557`
- val_centered_curve_shape_loss: `0.012287`
- val_curve_offset_loss: `0.003179`
- val_curve_amplitude_loss: `0.060414`
- val_sparse_harmonic_shape_loss: `0.000256`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000000e+00`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `0.000000e+00`
- val_effective_stiffness_nm_per_deg: `27249.990234`
- val_elastic_prediction_mean_abs_deg: `0.033930`

## Test Metrics

- test_loss: `0.019728`
- test_mae: `0.001825`
- test_rmse: `0.002313`
- test_pointwise_loss: `0.015669`
- test_centered_curve_shape_loss: `0.012207`
- test_curve_offset_loss: `0.003191`
- test_curve_amplitude_loss: `0.059433`
- test_sparse_harmonic_shape_loss: `0.000256`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000000e+00`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `0.000000e+00`
- test_effective_stiffness_nm_per_deg: `27250.000000`
- test_elastic_prediction_mean_abs_deg: `0.027923`

## Interpretation

The held-out val error stayed finite with MAE=0.001927 deg and RMSE=0.002392 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001825 deg and RMSE=0.002313 deg, which indicates a numerically stable baseline run.
