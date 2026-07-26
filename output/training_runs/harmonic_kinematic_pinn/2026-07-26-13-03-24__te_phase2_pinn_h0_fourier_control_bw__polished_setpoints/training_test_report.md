# Phase2 Pinn H0 Fourier Control Bw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h0_fourier_control_bw__polished_setpoints`
- Model Family: `phase2_pinn_h0_fourier_control_bw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-13-03-24__te_phase2_pinn_h0_fourier_control_bw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=009-val_mae=0.00184669.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.018737`
- val_mae: `0.001847`
- val_rmse: `0.002245`
- val_pointwise_loss: `0.014850`
- val_centered_curve_shape_loss: `0.012261`
- val_curve_offset_loss: `0.003576`
- val_curve_amplitude_loss: `0.058531`
- val_sparse_harmonic_shape_loss: `0.000280`
- val_physics_oscillator_residual_loss: `0.000000e+00`
- val_physics_periodic_value_loss: `0.000000e+00`
- val_physics_periodic_slope_loss: `0.000000e+00`
- val_physics_analytical_anchor_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.012804`
- test_mae: `0.001703`
- test_rmse: `0.002137`
- test_pointwise_loss: `0.010302`
- test_centered_curve_shape_loss: `0.008399`
- test_curve_offset_loss: `0.003584`
- test_curve_amplitude_loss: `0.033820`
- test_sparse_harmonic_shape_loss: `0.000176`
- test_physics_oscillator_residual_loss: `0.000000e+00`
- test_physics_periodic_value_loss: `0.000000e+00`
- test_physics_periodic_slope_loss: `0.000000e+00`
- test_physics_analytical_anchor_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001847 deg and RMSE=0.002245 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001703 deg and RMSE=0.002137 deg, which indicates a numerically stable baseline run.
