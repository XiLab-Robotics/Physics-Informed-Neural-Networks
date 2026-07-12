# Wave4 1 Mae Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_fw__simplified_setpoints`
- Model Family: `wave4_1_mae_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-14-40-52__te_wave4_1_mae_robust_loss_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=085-val_mae=0.00364418.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.078335`
- val_mae: `0.003644`
- val_rmse: `0.004529`
- val_pointwise_loss: `0.078335`
- val_centered_curve_shape_loss: `0.006462`
- val_curve_offset_loss: `0.004839`
- val_curve_amplitude_loss: `0.047283`
- val_sparse_harmonic_shape_loss: `0.000154`
- val_structured_mae: `0.028033`
- val_structured_rmse: `0.032743`
- val_residual_offset_mean_abs: `0.027305`

## Test Metrics

- test_loss: `0.076537`
- test_mae: `0.003561`
- test_rmse: `0.004316`
- test_pointwise_loss: `0.076537`
- test_centered_curve_shape_loss: `0.003199`
- test_curve_offset_loss: `0.005763`
- test_curve_amplitude_loss: `0.020522`
- test_sparse_harmonic_shape_loss: `6.954232e-05`
- test_structured_mae: `0.027267`
- test_structured_rmse: `0.033284`
- test_residual_offset_mean_abs: `0.026761`

## Interpretation

The held-out val error stayed finite with MAE=0.003644 deg and RMSE=0.004529 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003561 deg and RMSE=0.004316 deg, which indicates a numerically stable baseline run.
