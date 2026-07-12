# Wave4 1 Smooth L1 Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints`
- Model Family: `wave4_1_smooth_l1_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-21-02-43__te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=142-val_mae=0.00357827.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005440`
- val_mae: `0.003578`
- val_rmse: `0.004439`
- val_pointwise_loss: `0.005440`
- val_centered_curve_shape_loss: `0.006347`
- val_curve_offset_loss: `0.004533`
- val_curve_amplitude_loss: `0.048479`
- val_sparse_harmonic_shape_loss: `0.000150`
- val_structured_mae: `0.033997`
- val_structured_rmse: `0.039233`
- val_residual_offset_mean_abs: `0.033418`

## Test Metrics

- test_loss: `0.004247`
- test_mae: `0.003462`
- test_rmse: `0.004219`
- test_pointwise_loss: `0.004247`
- test_centered_curve_shape_loss: `0.003143`
- test_curve_offset_loss: `0.005351`
- test_curve_amplitude_loss: `0.021016`
- test_sparse_harmonic_shape_loss: `6.778620e-05`
- test_structured_mae: `0.035562`
- test_structured_rmse: `0.041234`
- test_residual_offset_mean_abs: `0.035299`

## Interpretation

The held-out val error stayed finite with MAE=0.003578 deg and RMSE=0.004439 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003462 deg and RMSE=0.004219 deg, which indicates a numerically stable baseline run.
