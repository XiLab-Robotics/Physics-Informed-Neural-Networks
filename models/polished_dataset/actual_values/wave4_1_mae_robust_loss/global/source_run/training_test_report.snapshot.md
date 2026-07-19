# Wave4 1 Mae Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_global__polished_actual_values`
- Model Family: `wave4_1_mae_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-17-35-21__te_wave4_1_mae_robust_loss_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=157-val_mae=0.00176826.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.037987`
- val_mae: `0.001768`
- val_rmse: `0.002535`
- val_pointwise_loss: `0.037987`
- val_centered_curve_shape_loss: `0.004574`
- val_curve_offset_loss: `0.000286`
- val_curve_amplitude_loss: `0.037487`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.009295`
- val_structured_rmse: `0.010463`
- val_residual_offset_mean_abs: `0.008947`

## Test Metrics

- test_loss: `0.043985`
- test_mae: `0.002047`
- test_rmse: `0.003417`
- test_pointwise_loss: `0.043985`
- test_centered_curve_shape_loss: `0.005371`
- test_curve_offset_loss: `0.002867`
- test_curve_amplitude_loss: `0.046123`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.009511`
- test_structured_rmse: `0.011031`
- test_residual_offset_mean_abs: `0.008926`

## Interpretation

The held-out val error stayed finite with MAE=0.001768 deg and RMSE=0.002535 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002047 deg and RMSE=0.003417 deg, which indicates a numerically stable baseline run.
