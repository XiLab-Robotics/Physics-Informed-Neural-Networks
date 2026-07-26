# Phase3 Pinn C3 Nonlinear Compliance Soft Fw Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c3_nonlinear_compliance_soft_fw__polished_setpoints`
- Model Family: `phase3_pinn_c3_nonlinear_compliance_soft_fw`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-44-42__te_phase3_pinn_c3_nonlinear_compliance_soft_fw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=019-val_mae=0.00194237.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.017579`
- val_mae: `0.001942`
- val_rmse: `0.002475`
- val_pointwise_loss: `0.013889`
- val_centered_curve_shape_loss: `0.007783`
- val_curve_offset_loss: `0.006094`
- val_curve_amplitude_loss: `0.053222`
- val_sparse_harmonic_shape_loss: `0.000137`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000333`
- val_physics_zero_torque_boundary_loss: `9.327822e-06`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `7.162134e-15`
- val_effective_stiffness_nm_per_deg: `29116.525391`
- val_elastic_prediction_mean_abs_deg: `0.032783`

## Test Metrics

- test_loss: `0.014765`
- test_mae: `0.001745`
- test_rmse: `0.002209`
- test_pointwise_loss: `0.011279`
- test_centered_curve_shape_loss: `0.007755`
- test_curve_offset_loss: `0.003477`
- test_curve_amplitude_loss: `0.056071`
- test_sparse_harmonic_shape_loss: `0.000150`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000254`
- test_physics_zero_torque_boundary_loss: `1.017237e-05`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `9.723895e-15`
- test_effective_stiffness_nm_per_deg: `29116.529297`
- test_elastic_prediction_mean_abs_deg: `0.027083`

## Interpretation

The held-out val error stayed finite with MAE=0.001942 deg and RMSE=0.002475 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001745 deg and RMSE=0.002209 deg, which indicates a numerically stable baseline run.
