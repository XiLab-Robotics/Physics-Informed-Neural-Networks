# Phase3 Pinn C4 Hard Elastic Offset Bw Training And Testing Report

## Overview

- Run Name: `te_phase3_pinn_c4_hard_elastic_offset_bw__polished_setpoints`
- Model Family: `phase3_pinn_c4_hard_elastic_offset_bw`
- Model Type: `quasi_static_compliance_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\quasi_static_compliance_pinn\2026-07-26-19-06-07__te_phase3_pinn_c4_hard_elastic_offset_bw__polished_setpoints\checkpoints\quasi_static_compliance_pinn-epoch=003-val_mae=0.00275818.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.030064`
- val_mae: `0.002758`
- val_rmse: `0.003307`
- val_pointwise_loss: `0.024303`
- val_centered_curve_shape_loss: `0.013787`
- val_curve_offset_loss: `0.010405`
- val_curve_amplitude_loss: `0.076188`
- val_sparse_harmonic_shape_loss: `0.000297`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`
- val_physics_compliance_equation_loss: `0.001972`
- val_physics_zero_torque_boundary_loss: `0.000000e+00`
- val_physics_compliance_monotonicity_loss: `1.432306e-06`
- val_physics_stiffness_bounds_loss: `0.000000e+00`
- val_physics_periodic_mean_loss: `7.528478e-14`
- val_effective_stiffness_nm_per_deg: `26948.283203`
- val_elastic_prediction_mean_abs_deg: `0.034310`

## Test Metrics

- test_loss: `0.026638`
- test_mae: `0.002350`
- test_rmse: `0.002859`
- test_pointwise_loss: `0.021273`
- test_centered_curve_shape_loss: `0.013690`
- test_curve_offset_loss: `0.007297`
- test_curve_amplitude_loss: `0.075886`
- test_sparse_harmonic_shape_loss: `0.000297`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`
- test_physics_compliance_equation_loss: `0.001503`
- test_physics_zero_torque_boundary_loss: `0.000000e+00`
- test_physics_compliance_monotonicity_loss: `1.091564e-06`
- test_physics_stiffness_bounds_loss: `0.000000e+00`
- test_physics_periodic_mean_loss: `5.592387e-14`
- test_effective_stiffness_nm_per_deg: `26948.283203`
- test_elastic_prediction_mean_abs_deg: `0.028236`

## Interpretation

The held-out val error stayed finite with MAE=0.002758 deg and RMSE=0.003307 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002350 deg and RMSE=0.002859 deg, which indicates a numerically stable baseline run.
