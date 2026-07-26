# Phase3 Pinn C3 Nonlinear Compliance Soft Bw Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c3_nonlinear_compliance_soft_bw__polished_setpoints`
- Model Family: `phase3_pinn_c3_nonlinear_compliance_soft_bw`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-52-22__te_phase3_pinn_c3_nonlinear_compliance_soft_bw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=011-val_mae=0.00203792.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.021055`
- val_mae: `0.002038`
- val_rmse: `0.002543`
- val_pointwise_loss: `0.016369`
- val_centered_curve_shape_loss: `0.012746`
- val_curve_offset_loss: `0.003545`
- val_curve_amplitude_loss: `0.072163`
- val_sparse_harmonic_shape_loss: `0.000268`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000981`
- val_physics_zero_torque_boundary_loss: `3.525869e-06`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `7.364830e-14`
- val_effective_stiffness_nm_per_deg: `30195.335938`
- val_elastic_prediction_mean_abs_deg: `0.031786`

## Test Metrics

- test_loss: `0.021545`
- test_mae: `0.001926`
- test_rmse: `0.002441`
- test_pointwise_loss: `0.016752`
- test_centered_curve_shape_loss: `0.013176`
- test_curve_offset_loss: `0.003300`
- test_curve_amplitude_loss: `0.074435`
- test_sparse_harmonic_shape_loss: `0.000283`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000991`
- test_physics_zero_torque_boundary_loss: `2.944164e-06`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `6.094466e-14`
- test_effective_stiffness_nm_per_deg: `30195.335938`
- test_elastic_prediction_mean_abs_deg: `0.026276`

## Interpretation

The held-out val error stayed finite with MAE=0.002038 deg and RMSE=0.002543 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001926 deg and RMSE=0.002441 deg, which indicates a numerically stable baseline run.
