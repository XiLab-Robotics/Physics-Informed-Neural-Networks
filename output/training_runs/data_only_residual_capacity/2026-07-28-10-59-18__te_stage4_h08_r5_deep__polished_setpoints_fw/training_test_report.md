# Stage4 H08 R5 Deep Training And Testing Report

## Overview

- Run Name: `te_stage4_h08_r5_deep__polished_setpoints_fw`
- Model Family: `stage4_h08_r5_deep`
- Model Type: `data_only_residual_capacity`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\data_only_residual_capacity\2026-07-28-10-59-18__te_stage4_h08_r5_deep__polished_setpoints_fw\checkpoints\data_only_residual_capacity-epoch=021-val_mae=0.00148973.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.008973`
- val_mae: `0.001490`
- val_rmse: `0.001870`
- val_pointwise_loss: `0.008973`
- val_residual_energy_loss: `12.583871`
- val_centered_curve_shape_loss: `0.006647`
- val_curve_offset_loss: `0.002277`
- val_curve_amplitude_loss: `0.060984`
- val_sparse_harmonic_shape_loss: `0.000105`
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
- val_residual_prediction_deg_mean_abs: `0.073818`

## Test Metrics

- test_loss: `0.009246`
- test_mae: `0.001455`
- test_rmse: `0.001825`
- test_pointwise_loss: `0.009246`
- test_residual_energy_loss: `9.437678`
- test_centered_curve_shape_loss: `0.006935`
- test_curve_offset_loss: `0.002201`
- test_curve_amplitude_loss: `0.063758`
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
- test_analytical_prediction_deg_mean_abs: `0.021736`
- test_frozen_analytical_prediction_deg_mean_abs: `0.021736`
- test_residual_prediction_deg_mean_abs: `0.061106`

## Interpretation

The held-out val error stayed finite with MAE=0.001490 deg and RMSE=0.001870 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001455 deg and RMSE=0.001825 deg, which indicates a numerically stable baseline run.
