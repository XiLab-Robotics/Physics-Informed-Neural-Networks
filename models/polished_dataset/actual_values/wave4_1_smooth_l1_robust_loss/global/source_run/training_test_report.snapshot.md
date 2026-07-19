# Wave4 1 Smooth L1 Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values`
- Model Family: `wave4_1_smooth_l1_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-00-17-37__te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=151-val_mae=0.00188208.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002455`
- val_mae: `0.001882`
- val_rmse: `0.002642`
- val_pointwise_loss: `0.002455`
- val_centered_curve_shape_loss: `0.004489`
- val_curve_offset_loss: `0.000422`
- val_curve_amplitude_loss: `0.033565`
- val_sparse_harmonic_shape_loss: `9.921179e-05`
- val_structured_mae: `0.018046`
- val_structured_rmse: `0.021745`
- val_residual_offset_mean_abs: `0.017986`

## Test Metrics

- test_loss: `0.002908`
- test_mae: `0.002028`
- test_rmse: `0.003067`
- test_pointwise_loss: `0.002908`
- test_centered_curve_shape_loss: `0.005321`
- test_curve_offset_loss: `0.000495`
- test_curve_amplitude_loss: `0.038327`
- test_sparse_harmonic_shape_loss: `0.000107`
- test_structured_mae: `0.017504`
- test_structured_rmse: `0.021656`
- test_residual_offset_mean_abs: `0.017318`

## Interpretation

The held-out val error stayed finite with MAE=0.001882 deg and RMSE=0.002642 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002028 deg and RMSE=0.003067 deg, which indicates a numerically stable baseline run.
