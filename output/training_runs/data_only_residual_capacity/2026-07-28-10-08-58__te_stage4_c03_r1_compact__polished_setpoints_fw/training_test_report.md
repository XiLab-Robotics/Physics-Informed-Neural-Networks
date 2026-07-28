# Stage4 C03 R1 Compact Training And Testing Report

## Overview

- Run Name: `te_stage4_c03_r1_compact__polished_setpoints_fw`
- Model Family: `stage4_c03_r1_compact`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-10-08-58__te_stage4_c03_r1_compact__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=010-val_mae=0.00187407.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.013447`
- val_mae: `0.001874`
- val_rmse: `0.002400`
- val_pointwise_loss: `0.013447`
- val_residual_energy_loss: `0.000000e+00`
- val_centered_curve_shape_loss: `0.007578`
- val_curve_offset_loss: `0.005853`
- val_curve_amplitude_loss: `0.065260`
- val_sparse_harmonic_shape_loss: `0.000128`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000000e+00`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `0.000000e+00`
- val_direct_prediction_deg_mean_abs: `0.056326`

## Test Metrics

- test_loss: `0.010963`
- test_mae: `0.001620`
- test_rmse: `0.002066`
- test_pointwise_loss: `0.010963`
- test_residual_energy_loss: `0.000000e+00`
- test_centered_curve_shape_loss: `0.007630`
- test_curve_offset_loss: `0.003267`
- test_curve_amplitude_loss: `0.063526`
- test_sparse_harmonic_shape_loss: `0.000141`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000000e+00`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `0.000000e+00`
- test_direct_prediction_deg_mean_abs: `0.050774`

## Interpretation

The held-out val error stayed finite with MAE=0.001874 deg and RMSE=0.002400 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001620 deg and RMSE=0.002066 deg, which indicates a numerically stable baseline run.
