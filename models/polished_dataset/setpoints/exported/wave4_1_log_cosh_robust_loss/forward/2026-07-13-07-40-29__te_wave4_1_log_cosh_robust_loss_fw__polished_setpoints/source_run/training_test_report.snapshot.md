# Wave4 1 Log Cosh Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints`
- Model Family: `wave4_1_log_cosh_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `output/training_runs/wave4_1_log_cosh_robust_loss/2026-07-13-07-40-29__te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=089-val_mae=0.00196005.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002502`
- val_mae: `0.001960`
- val_rmse: `0.002721`
- val_pointwise_loss: `0.002502`
- val_centered_curve_shape_loss: `0.004581`
- val_curve_offset_loss: `0.000503`
- val_curve_amplitude_loss: `0.029930`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.022179`
- val_structured_rmse: `0.026740`
- val_residual_offset_mean_abs: `0.022047`

## Test Metrics

- test_loss: `0.004090`
- test_mae: `0.002289`
- test_rmse: `0.003641`
- test_pointwise_loss: `0.004090`
- test_centered_curve_shape_loss: `0.005457`
- test_curve_offset_loss: `0.003108`
- test_curve_amplitude_loss: `0.038618`
- test_sparse_harmonic_shape_loss: `0.000109`
- test_structured_mae: `0.021029`
- test_structured_rmse: `0.025864`
- test_residual_offset_mean_abs: `0.020609`

## Interpretation

The held-out val error stayed finite with MAE=0.001960 deg and RMSE=0.002721 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002289 deg and RMSE=0.003641 deg, which indicates a numerically stable baseline run.
