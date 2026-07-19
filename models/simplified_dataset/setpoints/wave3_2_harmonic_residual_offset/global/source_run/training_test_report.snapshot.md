# Wave3 2 Harmonic Residual Offset Global Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_global__simplified_setpoints`
- Model Family: `wave3_2_harmonic_residual_offset_global`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-18-29__te_wave3_2_harmonic_residual_offset_global__simplified_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=138-val_mae=0.00362371.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010720`
- val_mae: `0.003624`
- val_rmse: `0.004439`
- val_pointwise_loss: `0.010720`
- val_centered_curve_shape_loss: `0.006395`
- val_curve_offset_loss: `0.004325`
- val_curve_amplitude_loss: `0.043892`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.035195`
- val_structured_rmse: `0.041265`
- val_residual_offset_mean_abs: `0.035087`

## Test Metrics

- test_loss: `0.008163`
- test_mae: `0.003405`
- test_rmse: `0.004128`
- test_pointwise_loss: `0.008163`
- test_centered_curve_shape_loss: `0.003229`
- test_curve_offset_loss: `0.004934`
- test_curve_amplitude_loss: `0.018709`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039005`
- test_structured_rmse: `0.044853`
- test_residual_offset_mean_abs: `0.038935`

## Interpretation

The held-out val error stayed finite with MAE=0.003624 deg and RMSE=0.004439 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003405 deg and RMSE=0.004128 deg, which indicates a numerically stable baseline run.
