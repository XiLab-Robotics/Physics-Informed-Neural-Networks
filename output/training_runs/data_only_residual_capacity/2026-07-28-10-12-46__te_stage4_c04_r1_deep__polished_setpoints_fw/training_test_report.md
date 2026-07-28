# Stage4 C04 R1 Deep Training And Testing Report

## Overview

- Run Name: `te_stage4_c04_r1_deep__polished_setpoints_fw`
- Model Family: `stage4_c04_r1_deep`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-10-12-46__te_stage4_c04_r1_deep__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=020-val_mae=0.00182815.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.012351`
- val_mae: `0.001828`
- val_rmse: `0.002303`
- val_pointwise_loss: `0.012351`
- val_residual_energy_loss: `0.000000e+00`
- val_centered_curve_shape_loss: `0.006950`
- val_curve_offset_loss: `0.005381`
- val_curve_amplitude_loss: `0.053814`
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
- val_direct_prediction_deg_mean_abs: `0.056126`

## Test Metrics

- test_loss: `0.010454`
- test_mae: `0.001609`
- test_rmse: `0.002010`
- test_pointwise_loss: `0.010454`
- test_residual_energy_loss: `0.000000e+00`
- test_centered_curve_shape_loss: `0.007021`
- test_curve_offset_loss: `0.003362`
- test_curve_amplitude_loss: `0.055119`
- test_sparse_harmonic_shape_loss: `0.000133`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000000e+00`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `0.000000e+00`
- test_direct_prediction_deg_mean_abs: `0.050592`

## Interpretation

The held-out val error stayed finite with MAE=0.001828 deg and RMSE=0.002303 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001609 deg and RMSE=0.002010 deg, which indicates a numerically stable baseline run.
