# Phase2 Pinn H1 Oscillator Residual Bw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints`
- Model Family: `phase2_pinn_h1_oscillator_residual_bw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-14-33-28__te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=018-val_mae=0.00185636.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.021541`
- val_mae: `0.001856`
- val_rmse: `0.002314`
- val_pointwise_loss: `0.015513`
- val_centered_curve_shape_loss: `0.012550`
- val_curve_offset_loss: `0.002865`
- val_curve_amplitude_loss: `0.105156`
- val_sparse_harmonic_shape_loss: `0.000264`
- val_physics_oscillator_residual_loss: `0.025667`
- val_physics_periodic_value_loss: `0.000769`
- val_physics_periodic_slope_loss: `5.739048`
- val_physics_analytical_anchor_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.022394`
- test_mae: `0.001723`
- test_rmse: `0.002210`
- test_pointwise_loss: `0.016178`
- test_centered_curve_shape_loss: `0.013535`
- test_curve_offset_loss: `0.002326`
- test_curve_amplitude_loss: `0.108270`
- test_sparse_harmonic_shape_loss: `0.000295`
- test_physics_oscillator_residual_loss: `0.025756`
- test_physics_periodic_value_loss: `0.000582`
- test_physics_periodic_slope_loss: `5.811735`
- test_physics_analytical_anchor_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001856 deg and RMSE=0.002314 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001723 deg and RMSE=0.002210 deg, which indicates a numerically stable baseline run.
