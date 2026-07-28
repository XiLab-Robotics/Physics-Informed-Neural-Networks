# Stage4 H01 R2 Compact Training And Testing Report

## Overview

- Run Name: `te_stage4_h01_r2_compact__polished_setpoints_fw`
- Model Family: `stage4_h01_r2_compact`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-10-25-52__te_stage4_h01_r2_compact__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=023-val_mae=0.00212284.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.015270`
- val_mae: `0.002123`
- val_rmse: `0.002662`
- val_pointwise_loss: `0.015270`
- val_residual_energy_loss: `12.402090`
- val_centered_curve_shape_loss: `0.007078`
- val_curve_offset_loss: `0.008116`
- val_curve_amplitude_loss: `0.047771`
- val_sparse_harmonic_shape_loss: `0.000113`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000000e+00`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `0.000000e+00`
- val_analytical_prediction_deg_mean_abs: `0.025562`
- val_frozen_analytical_prediction_deg_mean_abs: `0.025562`
- val_residual_prediction_deg_mean_abs: `0.073068`

## Test Metrics

- test_loss: `0.012869`
- test_mae: `0.001940`
- test_rmse: `0.002397`
- test_pointwise_loss: `0.012869`
- test_residual_energy_loss: `9.299850`
- test_centered_curve_shape_loss: `0.007276`
- test_curve_offset_loss: `0.005487`
- test_curve_amplitude_loss: `0.052217`
- test_sparse_harmonic_shape_loss: `0.000129`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000000e+00`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `0.000000e+00`
- test_analytical_prediction_deg_mean_abs: `0.021736`
- test_frozen_analytical_prediction_deg_mean_abs: `0.021736`
- test_residual_prediction_deg_mean_abs: `0.060407`

## Interpretation

The held-out val error stayed finite with MAE=0.002123 deg and RMSE=0.002662 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001940 deg and RMSE=0.002397 deg, which indicates a numerically stable baseline run.
