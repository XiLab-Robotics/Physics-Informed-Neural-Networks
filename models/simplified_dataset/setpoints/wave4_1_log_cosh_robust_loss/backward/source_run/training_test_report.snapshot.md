# Wave4 1 Log Cosh Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_bw__simplified_setpoints`
- Model Family: `wave4_1_log_cosh_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-04-12-33__te_wave4_1_log_cosh_robust_loss_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=099-val_mae=0.00352715.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005255`
- val_mae: `0.003527`
- val_rmse: `0.004378`
- val_pointwise_loss: `0.005255`
- val_centered_curve_shape_loss: `0.006387`
- val_curve_offset_loss: `0.004282`
- val_curve_amplitude_loss: `0.049032`
- val_sparse_harmonic_shape_loss: `0.000151`
- val_structured_mae: `0.033642`
- val_structured_rmse: `0.039287`
- val_residual_offset_mean_abs: `0.033690`

## Test Metrics

- test_loss: `0.004171`
- test_mae: `0.003402`
- test_rmse: `0.004189`
- test_pointwise_loss: `0.004171`
- test_centered_curve_shape_loss: `0.003167`
- test_curve_offset_loss: `0.005231`
- test_curve_amplitude_loss: `0.021378`
- test_sparse_harmonic_shape_loss: `6.871138e-05`
- test_structured_mae: `0.036482`
- test_structured_rmse: `0.041623`
- test_residual_offset_mean_abs: `0.036685`

## Interpretation

The held-out val error stayed finite with MAE=0.003527 deg and RMSE=0.004378 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003402 deg and RMSE=0.004189 deg, which indicates a numerically stable baseline run.
