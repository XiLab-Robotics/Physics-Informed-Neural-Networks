# Stage4 H05 R4 Compact Training And Testing Report

## Overview

- Run Name: `te_stage4_h05_r4_compact__polished_setpoints_fw`
- Model Family: `stage4_h05_r4_compact`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-10-44-29__te_stage4_h05_r4_compact__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=022-val_mae=0.00234579.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.019089`
- val_mae: `0.002346`
- val_rmse: `0.003034`
- val_pointwise_loss: `0.019089`
- val_residual_energy_loss: `12.455797`
- val_centered_curve_shape_loss: `0.014333`
- val_curve_offset_loss: `0.004596`
- val_curve_amplitude_loss: `0.040408`
- val_sparse_harmonic_shape_loss: `0.000315`
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
- val_residual_prediction_deg_mean_abs: `0.073376`

## Test Metrics

- test_loss: `0.015933`
- test_mae: `0.002111`
- test_rmse: `0.002707`
- test_pointwise_loss: `0.015933`
- test_residual_energy_loss: `9.343148`
- test_centered_curve_shape_loss: `0.012614`
- test_curve_offset_loss: `0.003112`
- test_curve_amplitude_loss: `0.047757`
- test_sparse_harmonic_shape_loss: `0.000284`
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
- test_residual_prediction_deg_mean_abs: `0.060668`

## Interpretation

The held-out val error stayed finite with MAE=0.002346 deg and RMSE=0.003034 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002111 deg and RMSE=0.002707 deg, which indicates a numerically stable baseline run.
