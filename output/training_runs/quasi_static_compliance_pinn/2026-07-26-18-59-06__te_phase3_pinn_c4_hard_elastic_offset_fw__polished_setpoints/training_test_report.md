# Phase3 Pinn C4 Hard Elastic Offset Fw Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c4_hard_elastic_offset_fw__polished_setpoints`
- Model Family: `phase3_pinn_c4_hard_elastic_offset_fw`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-59-06__te_phase3_pinn_c4_hard_elastic_offset_fw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=012-val_mae=0.00230064.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.020347`
- val_mae: `0.002301`
- val_rmse: `0.002729`
- val_pointwise_loss: `0.016666`
- val_centered_curve_shape_loss: `0.006986`
- val_curve_offset_loss: `0.009648`
- val_curve_amplitude_loss: `0.044521`
- val_sparse_harmonic_shape_loss: `0.000115`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.001986`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `1.432274e-06`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `8.593212e-15`
- val_effective_stiffness_nm_per_deg: `26857.775391`
- val_elastic_prediction_mean_abs_deg: `0.034426`

## Test Metrics

- test_loss: `0.018206`
- test_mae: `0.002087`
- test_rmse: `0.002481`
- test_pointwise_loss: `0.014661`
- test_centered_curve_shape_loss: `0.006806`
- test_curve_offset_loss: `0.007770`
- test_curve_amplitude_loss: `0.047208`
- test_sparse_harmonic_shape_loss: `0.000124`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.001513`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `1.091564e-06`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `8.513463e-15`
- test_effective_stiffness_nm_per_deg: `26857.777344`
- test_elastic_prediction_mean_abs_deg: `0.028331`

## Interpretation

The held-out val error stayed finite with MAE=0.002301 deg and RMSE=0.002729 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002087 deg and RMSE=0.002481 deg, which indicates a numerically stable baseline run.
