# Phase3 Pinn C0 Learned Mean Control Fw Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c0_learned_mean_control_fw__polished_setpoints`
- Model Family: `phase3_pinn_c0_learned_mean_control_fw`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-17-46-18__te_phase3_pinn_c0_learned_mean_control_fw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=016-val_mae=0.00177356.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.014138`
- val_mae: `0.001774`
- val_rmse: `0.002250`
- val_pointwise_loss: `0.011615`
- val_centered_curve_shape_loss: `0.007655`
- val_curve_offset_loss: `0.003937`
- val_curve_amplitude_loss: `0.031028`
- val_sparse_harmonic_shape_loss: `0.000133`
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
- val_elastic_prediction_mean_abs_deg: `0.033931`

## Test Metrics

- test_loss: `0.012426`
- test_mae: `0.001611`
- test_rmse: `0.002017`
- test_pointwise_loss: `0.009896`
- test_centered_curve_shape_loss: `0.007412`
- test_curve_offset_loss: `0.002419`
- test_curve_amplitude_loss: `0.036361`
- test_sparse_harmonic_shape_loss: `0.000140`
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

The held-out val error stayed finite with MAE=0.001774 deg and RMSE=0.002250 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001611 deg and RMSE=0.002017 deg, which indicates a numerically stable baseline run.
