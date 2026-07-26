# Phase2 Pinn H0 Fourier Control Fw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints`
- Model Family: `phase2_pinn_h0_fourier_control_fw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-14-03-44__te_phase2_pinn_h0_fourier_control_fw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=018-val_mae=0.00185231.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.014703`
- val_mae: `0.001852`
- val_rmse: `0.002321`
- val_pointwise_loss: `0.012250`
- val_centered_curve_shape_loss: `0.007103`
- val_curve_offset_loss: `0.005125`
- val_curve_amplitude_loss: `0.032236`
- val_sparse_harmonic_shape_loss: `0.000118`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.012627`
- test_mae: `0.001646`
- test_rmse: `0.002040`
- test_pointwise_loss: `0.010261`
- test_centered_curve_shape_loss: `0.006960`
- test_curve_offset_loss: `0.003240`
- test_curve_amplitude_loss: `0.034182`
- test_sparse_harmonic_shape_loss: `0.000128`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001852 deg and RMSE=0.002321 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001646 deg and RMSE=0.002040 deg, which indicates a numerically stable baseline run.
