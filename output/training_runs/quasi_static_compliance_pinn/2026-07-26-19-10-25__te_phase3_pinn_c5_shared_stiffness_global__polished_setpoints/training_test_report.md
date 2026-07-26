# Phase3 Pinn C5 Shared Stiffness Global Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c5_shared_stiffness_global__polished_setpoints`
- Model Family: `phase3_pinn_c5_shared_stiffness_global`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-19-10-25__te_phase3_pinn_c5_shared_stiffness_global__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=013-val_mae=0.00244802.ckpt`

## Dataset Split

- Train Curves: `1350`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006655`
- val_mae: `0.002448`
- val_rmse: `0.002930`
- val_pointwise_loss: `0.005372`
- val_centered_curve_shape_loss: `0.002591`
- val_curve_offset_loss: `0.002773`
- val_curve_amplitude_loss: `0.016846`
- val_sparse_harmonic_shape_loss: `4.938801e-05`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.001981`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `1.439067e-06`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `3.614511e-15`
- val_effective_stiffness_nm_per_deg: `26954.585938`
- val_elastic_prediction_mean_abs_deg: `0.034302`

## Test Metrics

- test_loss: `0.005822`
- test_mae: `0.002103`
- test_rmse: `0.002550`
- test_pointwise_loss: `0.004614`
- test_centered_curve_shape_loss: `0.002625`
- test_curve_offset_loss: `0.001967`
- test_curve_amplitude_loss: `0.017286`
- test_sparse_harmonic_shape_loss: `5.258301e-05`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.001506`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `1.094447e-06`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `3.491809e-15`
- test_effective_stiffness_nm_per_deg: `26954.593750`
- test_elastic_prediction_mean_abs_deg: `0.028229`

## Interpretation

The held-out val error stayed finite with MAE=0.002448 deg and RMSE=0.002930 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002103 deg and RMSE=0.002550 deg, which indicates a numerically stable baseline run.
