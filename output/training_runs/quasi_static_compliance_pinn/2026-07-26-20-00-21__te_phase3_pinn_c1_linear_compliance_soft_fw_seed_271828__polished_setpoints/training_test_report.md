# Phase3 Pinn C1 Linear Compliance Soft Fw Seed 271828 Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c1_linear_compliance_soft_fw_seed_271828__polished_setpoints`
- Model Family: `phase3_pinn_c1_linear_compliance_soft_fw_seed_271828`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-20-00-21__te_phase3_pinn_c1_linear_compliance_soft_fw_seed_271828__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=016-val_mae=0.00212320.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.017304`
- val_mae: `0.002123`
- val_rmse: `0.002636`
- val_pointwise_loss: `0.014485`
- val_centered_curve_shape_loss: `0.007654`
- val_curve_offset_loss: `0.006809`
- val_curve_amplitude_loss: `0.029400`
- val_sparse_harmonic_shape_loss: `0.000133`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000805`
- val_physics_zero_torque_boundary_loss: `1.742052e-06`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `5.835546e-15`
- val_effective_stiffness_nm_per_deg: `28958.119141`
- val_elastic_prediction_mean_abs_deg: `0.031929`

## Test Metrics

- test_loss: `0.014769`
- test_mae: `0.001898`
- test_rmse: `0.002340`
- test_pointwise_loss: `0.012057`
- test_centered_curve_shape_loss: `0.007516`
- test_curve_offset_loss: `0.004465`
- test_curve_amplitude_loss: `0.034165`
- test_sparse_harmonic_shape_loss: `0.000143`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000694`
- test_physics_zero_torque_boundary_loss: `2.031574e-06`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `3.515142e-15`
- test_effective_stiffness_nm_per_deg: `28958.111328`
- test_elastic_prediction_mean_abs_deg: `0.026276`

## Interpretation

The held-out val error stayed finite with MAE=0.002123 deg and RMSE=0.002636 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001898 deg and RMSE=0.002340 deg, which indicates a numerically stable baseline run.
