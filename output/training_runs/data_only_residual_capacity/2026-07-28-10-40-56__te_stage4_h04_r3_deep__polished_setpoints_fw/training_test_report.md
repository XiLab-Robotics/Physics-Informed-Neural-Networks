# Stage4 H04 R3 Deep Training And Testing Report

## Overview

- Run Name: `te_stage4_h04_r3_deep__polished_setpoints_fw`
- Model Family: `stage4_h04_r3_deep`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-10-40-56__te_stage4_h04_r3_deep__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=009-val_mae=0.05833042.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `8.786392`
- val_mae: `0.058330`
- val_rmse: `0.065231`
- val_pointwise_loss: `8.786392`
- val_residual_energy_loss: `0.454812`
- val_centered_curve_shape_loss: `0.014409`
- val_curve_offset_loss: `8.668674`
- val_curve_amplitude_loss: `0.043330`
- val_sparse_harmonic_shape_loss: `0.000319`
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
- val_residual_prediction_deg_mean_abs: `0.015885`

## Test Metrics

- test_loss: `6.303269`
- test_mae: `0.046188`
- test_rmse: `0.055998`
- test_pointwise_loss: `6.303269`
- test_residual_energy_loss: `0.438485`
- test_centered_curve_shape_loss: `0.012731`
- test_curve_offset_loss: `6.195263`
- test_curve_amplitude_loss: `0.049840`
- test_sparse_harmonic_shape_loss: `0.000286`
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
- test_residual_prediction_deg_mean_abs: `0.015603`

## Interpretation

The held-out val error stayed finite with MAE=0.058330 deg and RMSE=0.065231 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.046188 deg and RMSE=0.055998 deg, which indicates a numerically stable baseline run.
