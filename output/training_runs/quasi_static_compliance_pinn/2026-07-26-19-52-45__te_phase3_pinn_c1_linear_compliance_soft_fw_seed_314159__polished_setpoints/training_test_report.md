# Phase3 Pinn C1 Linear Compliance Soft Fw Seed 314159 Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints`
- Model Family: `phase3_pinn_c1_linear_compliance_soft_fw_seed_314159`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-19-52-45__te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=019-val_mae=0.00167640.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.013524`
- val_mae: `0.001676`
- val_rmse: `0.002152`
- val_pointwise_loss: `0.011036`
- val_centered_curve_shape_loss: `0.007320`
- val_curve_offset_loss: `0.003692`
- val_curve_amplitude_loss: `0.031603`
- val_sparse_harmonic_shape_loss: `0.000124`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.000280`
- val_physics_zero_torque_boundary_loss: `2.723979e-06`
- val_physics_compliance_monotonicity_loss: `0.000000e+00`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `1.004927e-14`
- val_effective_stiffness_nm_per_deg: `27259.390625`
- val_elastic_prediction_mean_abs_deg: `0.033919`

## Test Metrics

- test_loss: `0.011238`
- test_mae: `0.001472`
- test_rmse: `0.001864`
- test_pointwise_loss: `0.008952`
- test_centered_curve_shape_loss: `0.006831`
- test_curve_offset_loss: `0.002045`
- test_curve_amplitude_loss: `0.032762`
- test_sparse_harmonic_shape_loss: `0.000124`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.000305`
- test_physics_zero_torque_boundary_loss: `3.313897e-06`
- test_physics_compliance_monotonicity_loss: `0.000000e+00`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `1.099379e-14`
- test_effective_stiffness_nm_per_deg: `27259.396484`
- test_elastic_prediction_mean_abs_deg: `0.027914`

## Interpretation

The held-out val error stayed finite with MAE=0.001676 deg and RMSE=0.002152 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001472 deg and RMSE=0.001864 deg, which indicates a numerically stable baseline run.
