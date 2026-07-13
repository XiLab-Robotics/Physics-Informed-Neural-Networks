# Wave4 1 Log Cosh Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_global__polished_setpoints`
- Model Family: `wave4_1_log_cosh_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-05-22-10__te_wave4_1_log_cosh_robust_loss_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=155-val_mae=0.00191211.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002510`
- val_mae: `0.001912`
- val_rmse: `0.002683`
- val_pointwise_loss: `0.002510`
- val_centered_curve_shape_loss: `0.004574`
- val_curve_offset_loss: `0.000536`
- val_curve_amplitude_loss: `0.034179`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.030679`
- val_structured_rmse: `0.035790`
- val_residual_offset_mean_abs: `0.030729`

## Test Metrics

- test_loss: `0.004011`
- test_mae: `0.002200`
- test_rmse: `0.003572`
- test_pointwise_loss: `0.004011`
- test_centered_curve_shape_loss: `0.005472`
- test_curve_offset_loss: `0.002925`
- test_curve_amplitude_loss: `0.045371`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.029720`
- test_structured_rmse: `0.035139`
- test_residual_offset_mean_abs: `0.029685`

## Interpretation

The held-out val error stayed finite with MAE=0.001912 deg and RMSE=0.002683 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002200 deg and RMSE=0.003572 deg, which indicates a numerically stable baseline run.
