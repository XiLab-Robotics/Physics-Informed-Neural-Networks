# Stage4 A04 R5 Compact Training And Testing Report

## Overview

- Run Name: `te_stage4_a04_r5_compact__polished_setpoints_fw`
- Model Family: `stage4_a04_r5_compact`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-11-16-12__te_stage4_a04_r5_compact__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=007-val_mae=0.00306547.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028782`
- val_mae: `0.003065`
- val_rmse: `0.003772`
- val_pointwise_loss: `0.028782`
- val_residual_energy_loss: `0.505021`
- val_centered_curve_shape_loss: `0.015703`
- val_curve_offset_loss: `0.013073`
- val_curve_amplitude_loss: `0.049372`
- val_sparse_harmonic_shape_loss: `0.000357`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000000e+00`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `0.000000e+00`
- val_analytical_prediction_deg_mean_abs: `0.044291`
- val_frozen_analytical_prediction_deg_mean_abs: `0.025562`
- val_residual_prediction_deg_mean_abs: `0.015089`

## Test Metrics

- test_loss: `0.025896`
- test_mae: `0.002846`
- test_rmse: `0.003546`
- test_pointwise_loss: `0.025896`
- test_residual_energy_loss: `0.397525`
- test_centered_curve_shape_loss: `0.013877`
- test_curve_offset_loss: `0.011868`
- test_curve_amplitude_loss: `0.049472`
- test_sparse_harmonic_shape_loss: `0.000320`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000000e+00`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `0.000000e+00`
- test_analytical_prediction_deg_mean_abs: `0.042070`
- test_frozen_analytical_prediction_deg_mean_abs: `0.021736`
- test_residual_prediction_deg_mean_abs: `0.013362`

## Interpretation

The held-out val error stayed finite with MAE=0.003065 deg and RMSE=0.003772 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002846 deg and RMSE=0.003546 deg, which indicates a numerically stable baseline run.
