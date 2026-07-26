# Phase3 Pinn C0 Learned Mean Control Global Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c0_learned_mean_control_global__polished_setpoints`
- Model Family: `phase3_pinn_c0_learned_mean_control_global`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-00-41__te_phase3_pinn_c0_learned_mean_control_global__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=018-val_mae=0.00197682.ckpt`

## Dataset Split

- Train Curves: `1350`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005072`
- val_mae: `0.001977`
- val_rmse: `0.002449`
- val_pointwise_loss: `0.004006`
- val_centered_curve_shape_loss: `0.002905`
- val_curve_offset_loss: `0.001097`
- val_curve_amplitude_loss: `0.015676`
- val_sparse_harmonic_shape_loss: `5.809090e-05`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000000e+00`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `0.000000e+00`
- val_effective_stiffness_nm_per_deg: `27250.001953`
- val_elastic_prediction_mean_abs_deg: `0.033931`

## Test Metrics

- test_loss: `0.005543`
- test_mae: `0.002050`
- test_rmse: `0.002529`
- test_pointwise_loss: `0.004411`
- test_centered_curve_shape_loss: `0.002990`
- test_curve_offset_loss: `0.001405`
- test_curve_amplitude_loss: `0.016144`
- test_sparse_harmonic_shape_loss: `6.272183e-05`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000000e+00`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `0.000000e+00`
- test_effective_stiffness_nm_per_deg: `27249.998047`
- test_elastic_prediction_mean_abs_deg: `0.027923`

## Interpretation

The held-out val error stayed finite with MAE=0.001977 deg and RMSE=0.002449 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002050 deg and RMSE=0.002529 deg, which indicates a numerically stable baseline run.
