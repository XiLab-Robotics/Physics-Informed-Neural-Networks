# Phase3 Pinn C1 Linear Compliance Soft Fw Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints`
- Model Family: `phase3_pinn_c1_linear_compliance_soft_fw`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-14-00__te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=017-val_mae=0.00170183.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.014435`
- val_mae: `0.001702`
- val_rmse: `0.002164`
- val_pointwise_loss: `0.011201`
- val_centered_curve_shape_loss: `0.007068`
- val_curve_offset_loss: `0.004108`
- val_curve_amplitude_loss: `0.049675`
- val_sparse_harmonic_shape_loss: `0.000117`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000243`
- val_physics_zero_torque_boundary_loss: `1.867518e-06`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `5.018377e-15`
- val_effective_stiffness_nm_per_deg: `28275.589844`
- val_elastic_prediction_mean_abs_deg: `0.032700`

## Test Metrics

- test_loss: `0.012041`
- test_mae: `0.001495`
- test_rmse: `0.001887`
- test_pointwise_loss: `0.009123`
- test_centered_curve_shape_loss: `0.006676`
- test_curve_offset_loss: `0.002375`
- test_curve_amplitude_loss: `0.047986`
- test_sparse_harmonic_shape_loss: `0.000120`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000218`
- test_physics_zero_torque_boundary_loss: `2.279187e-06`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `5.551145e-15`
- test_effective_stiffness_nm_per_deg: `28275.585938`
- test_elastic_prediction_mean_abs_deg: `0.026911`

## Interpretation

The held-out val error stayed finite with MAE=0.001702 deg and RMSE=0.002164 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001495 deg and RMSE=0.001887 deg, which indicates a numerically stable baseline run.
