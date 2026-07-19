# Wave4 1 Log Cosh Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_fw__simplified_setpoints`
- Model Family: `wave4_1_log_cosh_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-03-10-51__te_wave4_1_log_cosh_robust_loss_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=101-val_mae=0.00354228.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005358`
- val_mae: `0.003542`
- val_rmse: `0.004419`
- val_pointwise_loss: `0.005358`
- val_centered_curve_shape_loss: `0.006446`
- val_curve_offset_loss: `0.004443`
- val_curve_amplitude_loss: `0.045236`
- val_sparse_harmonic_shape_loss: `0.000153`
- val_structured_mae: `0.046689`
- val_structured_rmse: `0.052127`
- val_residual_offset_mean_abs: `0.046477`

## Test Metrics

- test_loss: `0.004169`
- test_mae: `0.003398`
- test_rmse: `0.004187`
- test_pointwise_loss: `0.004169`
- test_centered_curve_shape_loss: `0.003215`
- test_curve_offset_loss: `0.005180`
- test_curve_amplitude_loss: `0.019676`
- test_sparse_harmonic_shape_loss: `6.957194e-05`
- test_structured_mae: `0.049876`
- test_structured_rmse: `0.055479`
- test_residual_offset_mean_abs: `0.049660`

## Interpretation

The held-out val error stayed finite with MAE=0.003542 deg and RMSE=0.004419 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003398 deg and RMSE=0.004187 deg, which indicates a numerically stable baseline run.
