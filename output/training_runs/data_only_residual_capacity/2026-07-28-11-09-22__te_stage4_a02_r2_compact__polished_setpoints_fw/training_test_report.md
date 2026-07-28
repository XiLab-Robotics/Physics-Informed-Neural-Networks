# Stage4 A02 R2 Compact Training And Testing Report

## Overview

- Run Name: `te_stage4_a02_r2_compact__polished_setpoints_fw`
- Model Family: `stage4_a02_r2_compact`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-11-09-22__te_stage4_a02_r2_compact__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=012-val_mae=0.00633605.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `1.189699`
- val_mae: `0.006336`
- val_rmse: `0.007517`
- val_pointwise_loss: `0.136302`
- val_residual_energy_loss: `10.533969`
- val_centered_curve_shape_loss: `0.008367`
- val_curve_offset_loss: `0.125821`
- val_curve_amplitude_loss: `0.053162`
- val_sparse_harmonic_shape_loss: `0.000134`
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
- val_residual_prediction_deg_mean_abs: `0.067856`

## Test Metrics

- test_loss: `0.891422`
- test_mae: `0.005241`
- test_rmse: `0.006491`
- test_pointwise_loss: `0.089806`
- test_residual_energy_loss: `8.016158`
- test_centered_curve_shape_loss: `0.008631`
- test_curve_offset_loss: `0.079780`
- test_curve_amplitude_loss: `0.054895`
- test_sparse_harmonic_shape_loss: `0.000152`
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
- test_residual_prediction_deg_mean_abs: `0.056241`

## Interpretation

The held-out val error stayed finite with MAE=0.006336 deg and RMSE=0.007517 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.005241 deg and RMSE=0.006491 deg, which indicates a numerically stable baseline run.
