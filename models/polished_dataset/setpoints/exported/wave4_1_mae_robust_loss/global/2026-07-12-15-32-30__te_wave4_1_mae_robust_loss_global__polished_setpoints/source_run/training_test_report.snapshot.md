# Wave4 1 Mae Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_global__polished_setpoints`
- Model Family: `wave4_1_mae_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-15-32-30__te_wave4_1_mae_robust_loss_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=178-val_mae=0.00178795.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.038410`
- val_mae: `0.001788`
- val_rmse: `0.002563`
- val_pointwise_loss: `0.038410`
- val_centered_curve_shape_loss: `0.004609`
- val_curve_offset_loss: `0.000357`
- val_curve_amplitude_loss: `0.036739`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_structured_mae: `0.018679`
- val_structured_rmse: `0.022477`
- val_residual_offset_mean_abs: `0.018640`

## Test Metrics

- test_loss: `0.045394`
- test_mae: `0.002113`
- test_rmse: `0.003548`
- test_pointwise_loss: `0.045394`
- test_centered_curve_shape_loss: `0.005558`
- test_curve_offset_loss: `0.003104`
- test_curve_amplitude_loss: `0.048407`
- test_sparse_harmonic_shape_loss: `0.000113`
- test_structured_mae: `0.018168`
- test_structured_rmse: `0.022158`
- test_residual_offset_mean_abs: `0.017883`

## Interpretation

The held-out val error stayed finite with MAE=0.001788 deg and RMSE=0.002563 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002113 deg and RMSE=0.003548 deg, which indicates a numerically stable baseline run.
