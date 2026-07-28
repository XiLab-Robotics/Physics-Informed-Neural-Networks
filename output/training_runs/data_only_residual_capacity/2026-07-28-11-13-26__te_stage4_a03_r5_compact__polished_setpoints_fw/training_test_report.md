# Stage4 A03 R5 Compact Training And Testing Report

## Overview

- Run Name: `te_stage4_a03_r5_compact__polished_setpoints_fw`
- Model Family: `stage4_a03_r5_compact`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-11-13-26__te_stage4_a03_r5_compact__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=004-val_mae=0.00205668.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.015966`
- val_mae: `0.002057`
- val_rmse: `0.002640`
- val_pointwise_loss: `0.015966`
- val_residual_energy_loss: `0.398452`
- val_centered_curve_shape_loss: `0.006699`
- val_curve_offset_loss: `0.009307`
- val_curve_amplitude_loss: `0.054778`
- val_sparse_harmonic_shape_loss: `0.000107`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000000e+00`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `0.000000e+00`
- val_analytical_prediction_deg_mean_abs: `0.047306`
- val_frozen_analytical_prediction_deg_mean_abs: `0.025562`
- val_residual_prediction_deg_mean_abs: `0.013323`

## Test Metrics

- test_loss: `0.013333`
- test_mae: `0.001926`
- test_rmse: `0.002382`
- test_pointwise_loss: `0.013333`
- test_residual_energy_loss: `0.319096`
- test_centered_curve_shape_loss: `0.006922`
- test_curve_offset_loss: `0.006397`
- test_curve_amplitude_loss: `0.056939`
- test_sparse_harmonic_shape_loss: `0.000127`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000000e+00`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `0.000000e+00`
- test_analytical_prediction_deg_mean_abs: `0.045289`
- test_frozen_analytical_prediction_deg_mean_abs: `0.021736`
- test_residual_prediction_deg_mean_abs: `0.011910`

## Interpretation

The held-out val error stayed finite with MAE=0.002057 deg and RMSE=0.002640 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001926 deg and RMSE=0.002382 deg, which indicates a numerically stable baseline run.
