# Stage4 H03 R3 Compact Training And Testing Report

## Overview

- Run Name: `te_stage4_h03_r3_compact__polished_setpoints_fw`
- Model Family: `stage4_h03_r3_compact`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-10-36-11__te_stage4_h03_r3_compact__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=016-val_mae=0.05829076.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `8.783639`
- val_mae: `0.058291`
- val_rmse: `0.065202`
- val_pointwise_loss: `8.783639`
- val_residual_energy_loss: `0.450334`
- val_centered_curve_shape_loss: `0.014254`
- val_curve_offset_loss: `8.666101`
- val_curve_amplitude_loss: `0.042119`
- val_sparse_harmonic_shape_loss: `0.000317`
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
- val_residual_prediction_deg_mean_abs: `0.015790`

## Test Metrics

- test_loss: `6.301252`
- test_mae: `0.046115`
- test_rmse: `0.055988`
- test_pointwise_loss: `6.301252`
- test_residual_energy_loss: `0.425837`
- test_centered_curve_shape_loss: `0.012737`
- test_curve_offset_loss: `6.193267`
- test_curve_amplitude_loss: `0.049010`
- test_sparse_harmonic_shape_loss: `0.000288`
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
- test_residual_prediction_deg_mean_abs: `0.015286`

## Interpretation

The held-out val error stayed finite with MAE=0.058291 deg and RMSE=0.065202 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.046115 deg and RMSE=0.055988 deg, which indicates a numerically stable baseline run.
