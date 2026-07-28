# Stage4 C02 R1 Deep Training And Testing Report

## Overview

- Run Name: `te_stage4_c02_r1_deep__polished_setpoints_fw`
- Model Family: `stage4_c02_r1_deep`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-10-06-00__te_stage4_c02_r1_deep__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=005-val_mae=0.00200130.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.014533`
- val_mae: `0.002001`
- val_rmse: `0.002547`
- val_pointwise_loss: `0.014533`
- val_residual_energy_loss: `0.000000e+00`
- val_centered_curve_shape_loss: `0.008170`
- val_curve_offset_loss: `0.006345`
- val_curve_amplitude_loss: `0.080238`
- val_sparse_harmonic_shape_loss: `0.000142`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000000e+00`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `0.000000e+00`
- val_direct_prediction_deg_mean_abs: `0.056210`

## Test Metrics

- test_loss: `0.012090`
- test_mae: `0.001760`
- test_rmse: `0.002226`
- test_pointwise_loss: `0.012090`
- test_residual_energy_loss: `0.000000e+00`
- test_centered_curve_shape_loss: `0.008294`
- test_curve_offset_loss: `0.003728`
- test_curve_amplitude_loss: `0.074976`
- test_sparse_harmonic_shape_loss: `0.000158`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000000e+00`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `0.000000e+00`
- test_direct_prediction_deg_mean_abs: `0.050629`

## Interpretation

The held-out val error stayed finite with MAE=0.002001 deg and RMSE=0.002547 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001760 deg and RMSE=0.002226 deg, which indicates a numerically stable baseline run.
