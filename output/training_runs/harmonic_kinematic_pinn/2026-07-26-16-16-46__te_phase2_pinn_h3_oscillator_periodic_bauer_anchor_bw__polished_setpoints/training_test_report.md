# Phase2 Pinn H3 Oscillator Periodic Bauer Anchor Bw Training And Testing Report

## Overview

- Run Name: `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints`
- Model Family: `phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw`
- Model Type: `harmonic_kinematic_pinn`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_kinematic_pinn\2026-07-26-16-16-46__te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints\checkpoints\harmonic_kinematic_pinn-epoch=009-val_mae=0.00208700.ckpt`

## Dataset Split

- Train Curves: `675`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023987`
- val_mae: `0.002087`
- val_rmse: `0.002578`
- val_pointwise_loss: `0.017650`
- val_centered_curve_shape_loss: `0.012915`
- val_curve_offset_loss: `0.004635`
- val_curve_amplitude_loss: `0.102794`
- val_sparse_harmonic_shape_loss: `0.000274`
- val_physics_oscillator_residual_loss: `0.018385`
- val_physics_periodic_value_loss: `0.001546`
- val_physics_periodic_slope_loss: `0.000885`
- val_physics_analytical_anchor_loss: `0.005605`

## Test Metrics

- test_loss: `0.024567`
- test_mae: `0.001931`
- test_rmse: `0.002469`
- test_pointwise_loss: `0.018031`
- test_centered_curve_shape_loss: `0.013941`
- test_curve_offset_loss: `0.003777`
- test_curve_amplitude_loss: `0.108200`
- test_sparse_harmonic_shape_loss: `0.000305`
- test_physics_oscillator_residual_loss: `0.017941`
- test_physics_periodic_value_loss: `0.001408`
- test_physics_periodic_slope_loss: `0.000636`
- test_physics_analytical_anchor_loss: `0.004550`

## Interpretation

The held-out val error stayed finite with MAE=0.002087 deg and RMSE=0.002578 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001931 deg and RMSE=0.002469 deg, which indicates a numerically stable baseline run.
