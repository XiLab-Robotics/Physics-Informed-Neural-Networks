# Phase3 Pinn C2 Temperature Compliance Soft Bw Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c2_temperature_compliance_soft_bw__polished_setpoints`
- Model Family: `phase3_pinn_c2_temperature_compliance_soft_bw`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-18-37-03__te_phase3_pinn_c2_temperature_compliance_soft_bw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=019-val_mae=0.00172687.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.018371`
- val_mae: `0.001727`
- val_rmse: `0.002179`
- val_pointwise_loss: `0.014301`
- val_centered_curve_shape_loss: `0.012534`
- val_curve_offset_loss: `0.001675`
- val_curve_amplitude_loss: `0.063268`
- val_sparse_harmonic_shape_loss: `0.000262`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000251`
- val_physics_zero_torque_boundary_loss: `1.996963e-06`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `7.798616e-14`
- val_effective_stiffness_nm_per_deg: `28244.000000`
- val_elastic_prediction_mean_abs_deg: `0.032740`

## Test Metrics

- test_loss: `0.018422`
- test_mae: `0.001624`
- test_rmse: `0.002068`
- test_pointwise_loss: `0.014379`
- test_centered_curve_shape_loss: `0.012466`
- test_curve_offset_loss: `0.001635`
- test_curve_amplitude_loss: `0.062918`
- test_sparse_harmonic_shape_loss: `0.000263`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000201`
- test_physics_zero_torque_boundary_loss: `1.590869e-06`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `7.302596e-14`
- test_effective_stiffness_nm_per_deg: `28225.003906`
- test_elastic_prediction_mean_abs_deg: `0.026955`

## Interpretation

The held-out val error stayed finite with MAE=0.001727 deg and RMSE=0.002179 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001624 deg and RMSE=0.002068 deg, which indicates a numerically stable baseline run.
