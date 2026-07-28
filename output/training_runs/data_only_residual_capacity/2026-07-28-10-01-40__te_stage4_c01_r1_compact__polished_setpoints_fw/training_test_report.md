# Stage4 C01 R1 Compact Training And Testing Report

## Overview

- Run Name: `te_stage4_c01_r1_compact__polished_setpoints_fw`
- Model Family: `stage4_c01_r1_compact`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-10-01-40__te_stage4_c01_r1_compact__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=013-val_mae=0.00183508.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.013363`
- val_mae: `0.001835`
- val_rmse: `0.002368`
- val_pointwise_loss: `0.013363`
- val_residual_energy_loss: `0.000000e+00`
- val_centered_curve_shape_loss: `0.007076`
- val_curve_offset_loss: `0.006271`
- val_curve_amplitude_loss: `0.060832`
- val_sparse_harmonic_shape_loss: `0.000118`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000000e+00`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `0.000000e+00`
- val_direct_prediction_deg_mean_abs: `0.056377`

## Test Metrics

- test_loss: `0.011012`
- test_mae: `0.001624`
- test_rmse: `0.002065`
- test_pointwise_loss: `0.011012`
- test_residual_energy_loss: `0.000000e+00`
- test_centered_curve_shape_loss: `0.007093`
- test_curve_offset_loss: `0.003859`
- test_curve_amplitude_loss: `0.060240`
- test_sparse_harmonic_shape_loss: `0.000131`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000000e+00`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `0.000000e+00`
- test_direct_prediction_deg_mean_abs: `0.050935`

## Interpretation

The held-out val error stayed finite with MAE=0.001835 deg and RMSE=0.002368 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001624 deg and RMSE=0.002065 deg, which indicates a numerically stable baseline run.
