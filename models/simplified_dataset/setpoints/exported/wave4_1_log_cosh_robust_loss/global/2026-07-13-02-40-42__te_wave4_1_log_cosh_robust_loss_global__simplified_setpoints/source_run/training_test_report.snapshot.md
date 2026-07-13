# Wave4 1 Log Cosh Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_global__simplified_setpoints`
- Model Family: `wave4_1_log_cosh_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-02-40-42__te_wave4_1_log_cosh_robust_loss_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=120-val_mae=0.00357307.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005196`
- val_mae: `0.003573`
- val_rmse: `0.004393`
- val_pointwise_loss: `0.005196`
- val_centered_curve_shape_loss: `0.006339`
- val_curve_offset_loss: `0.004199`
- val_curve_amplitude_loss: `0.044605`
- val_sparse_harmonic_shape_loss: `0.000150`
- val_structured_mae: `0.025028`
- val_structured_rmse: `0.030282`
- val_residual_offset_mean_abs: `0.025029`

## Test Metrics

- test_loss: `0.003910`
- test_mae: `0.003339`
- test_rmse: `0.004048`
- test_pointwise_loss: `0.003910`
- test_centered_curve_shape_loss: `0.003185`
- test_curve_offset_loss: `0.004685`
- test_curve_amplitude_loss: `0.019515`
- test_sparse_harmonic_shape_loss: `6.908580e-05`
- test_structured_mae: `0.027180`
- test_structured_rmse: `0.032331`
- test_residual_offset_mean_abs: `0.027296`

## Interpretation

The held-out val error stayed finite with MAE=0.003573 deg and RMSE=0.004393 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003339 deg and RMSE=0.004048 deg, which indicates a numerically stable baseline run.
