# Phase3 Pinn C2 Temperature Compliance Soft Fw Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints`
- Model Family: `phase3_pinn_c2_temperature_compliance_soft_fw`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-29-09__te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=019-val_mae=0.00167166.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.013308`
- val_mae: `0.001672`
- val_rmse: `0.002123`
- val_pointwise_loss: `0.010927`
- val_centered_curve_shape_loss: `0.007465`
- val_curve_offset_loss: `0.003423`
- val_curve_amplitude_loss: `0.029364`
- val_sparse_harmonic_shape_loss: `0.000128`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000236`
- val_physics_zero_torque_boundary_loss: `1.196663e-06`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `1.088231e-14`
- val_effective_stiffness_nm_per_deg: `27503.796875`
- val_elastic_prediction_mean_abs_deg: `0.033629`

## Test Metrics

- test_loss: `0.011827`
- test_mae: `0.001551`
- test_rmse: `0.001950`
- test_pointwise_loss: `0.009581`
- test_centered_curve_shape_loss: `0.007130`
- test_curve_offset_loss: `0.002371`
- test_curve_amplitude_loss: `0.029993`
- test_sparse_harmonic_shape_loss: `0.000133`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000319`
- test_physics_zero_torque_boundary_loss: `1.395037e-06`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `9.456721e-15`
- test_effective_stiffness_nm_per_deg: `27461.250000`
- test_elastic_prediction_mean_abs_deg: `0.027701`

## Interpretation

The held-out val error stayed finite with MAE=0.001672 deg and RMSE=0.002123 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001551 deg and RMSE=0.001950 deg, which indicates a numerically stable baseline run.
