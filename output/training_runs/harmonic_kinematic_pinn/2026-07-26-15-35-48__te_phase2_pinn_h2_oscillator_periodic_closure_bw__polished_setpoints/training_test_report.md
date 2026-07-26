# Phase2 Pinn H2 Oscillator Periodic Closure Bw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h2_oscillator_periodic_closure_bw__polished_setpoints`
- Model Family: `phase2_pinn_h2_oscillator_periodic_closure_bw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-15-35-48__te_phase2_pinn_h2_oscillator_periodic_closure_bw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=007-val_mae=0.00201763.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023337`
- val_mae: `0.002018`
- val_rmse: `0.002516`
- val_pointwise_loss: `0.017124`
- val_centered_curve_shape_loss: `0.012943`
- val_curve_offset_loss: `0.004088`
- val_curve_amplitude_loss: `0.106576`
- val_sparse_harmonic_shape_loss: `0.000275`
- val_physics_oscillator_residual_loss: `0.024259`
- val_physics_periodic_value_loss: `5.639117e-05`
- val_physics_periodic_slope_loss: `0.002987`
- val_physics_analytical_anchor_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.025250`
- test_mae: `0.001966`
- test_rmse: `0.002545`
- test_pointwise_loss: `0.018751`
- test_centered_curve_shape_loss: `0.013991`
- test_curve_offset_loss: `0.004462`
- test_curve_amplitude_loss: `0.109982`
- test_sparse_harmonic_shape_loss: `0.000307`
- test_physics_oscillator_residual_loss: `0.025173`
- test_physics_periodic_value_loss: `6.464722e-05`
- test_physics_periodic_slope_loss: `0.001812`
- test_physics_analytical_anchor_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002018 deg and RMSE=0.002516 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001966 deg and RMSE=0.002545 deg, which indicates a numerically stable baseline run.
