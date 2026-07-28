# Stage4 H02 R2 Deep Training And Testing Report

## Overview

- Run Name: `te_stage4_h02_r2_deep__polished_setpoints_fw`
- Model Family: `stage4_h02_r2_deep`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-10-31-03__te_stage4_h02_r2_deep__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=023-val_mae=0.00163045.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.010292`
- val_mae: `0.001630`
- val_rmse: `0.002067`
- val_pointwise_loss: `0.010292`
- val_residual_energy_loss: `12.335116`
- val_centered_curve_shape_loss: `0.006744`
- val_curve_offset_loss: `0.003494`
- val_curve_amplitude_loss: `0.046512`
- val_sparse_harmonic_shape_loss: `0.000111`
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
- val_residual_prediction_deg_mean_abs: `0.072934`

## Test Metrics

- test_loss: `0.010435`
- test_mae: `0.001617`
- test_rmse: `0.002030`
- test_pointwise_loss: `0.010435`
- test_residual_energy_loss: `9.226137`
- test_centered_curve_shape_loss: `0.006906`
- test_curve_offset_loss: `0.003423`
- test_curve_amplitude_loss: `0.049025`
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
- test_residual_prediction_deg_mean_abs: `0.060217`

## Interpretation

The held-out val error stayed finite with MAE=0.001630 deg and RMSE=0.002067 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001617 deg and RMSE=0.002030 deg, which indicates a numerically stable baseline run.
