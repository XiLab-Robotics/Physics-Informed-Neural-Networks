# Wave4 1 Mae Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_bw__polished_setpoints`
- Model Family: `wave4_1_mae_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-51-03__te_wave4_1_mae_robust_loss_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=088-val_mae=0.00183184.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.039353`
- val_mae: `0.001832`
- val_rmse: `0.002604`
- val_pointwise_loss: `0.039353`
- val_centered_curve_shape_loss: `0.004590`
- val_curve_offset_loss: `0.000395`
- val_curve_amplitude_loss: `0.036537`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.042340`
- val_structured_rmse: `0.047343`
- val_residual_offset_mean_abs: `0.042471`

## Test Metrics

- test_loss: `0.046192`
- test_mae: `0.002150`
- test_rmse: `0.003545`
- test_pointwise_loss: `0.046192`
- test_centered_curve_shape_loss: `0.005530`
- test_curve_offset_loss: `0.003044`
- test_curve_amplitude_loss: `0.048071`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_structured_mae: `0.040711`
- test_structured_rmse: `0.046208`
- test_residual_offset_mean_abs: `0.040612`

## Interpretation

The held-out val error stayed finite with MAE=0.001832 deg and RMSE=0.002604 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002150 deg and RMSE=0.003545 deg, which indicates a numerically stable baseline run.
