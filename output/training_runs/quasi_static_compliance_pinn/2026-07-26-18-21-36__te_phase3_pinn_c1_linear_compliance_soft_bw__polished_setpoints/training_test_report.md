# Phase3 Pinn C1 Linear Compliance Soft Bw Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c1_linear_compliance_soft_bw__polished_setpoints`
- Model Family: `phase3_pinn_c1_linear_compliance_soft_bw`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-21-36__te_phase3_pinn_c1_linear_compliance_soft_bw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=017-val_mae=0.00196967.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.020416`
- val_mae: `0.001970`
- val_rmse: `0.002471`
- val_pointwise_loss: `0.016350`
- val_centered_curve_shape_loss: `0.013642`
- val_curve_offset_loss: `0.002591`
- val_curve_amplitude_loss: `0.057447`
- val_sparse_harmonic_shape_loss: `0.000293`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000407`
- val_physics_zero_torque_boundary_loss: `3.097389e-06`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `1.131307e-13`
- val_effective_stiffness_nm_per_deg: `28797.414062`
- val_elastic_prediction_mean_abs_deg: `0.032107`

## Test Metrics

- test_loss: `0.019579`
- test_mae: `0.001877`
- test_rmse: `0.002386`
- test_pointwise_loss: `0.016043`
- test_centered_curve_shape_loss: `0.012950`
- test_curve_offset_loss: `0.002825`
- test_curve_amplitude_loss: `0.045359`
- test_sparse_harmonic_shape_loss: `0.000277`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000347`
- test_physics_zero_torque_boundary_loss: `2.971201e-06`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `1.041458e-13`
- test_effective_stiffness_nm_per_deg: `28797.414062`
- test_elastic_prediction_mean_abs_deg: `0.026423`

## Interpretation

The held-out val error stayed finite with MAE=0.001970 deg and RMSE=0.002471 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001877 deg and RMSE=0.002386 deg, which indicates a numerically stable baseline run.
