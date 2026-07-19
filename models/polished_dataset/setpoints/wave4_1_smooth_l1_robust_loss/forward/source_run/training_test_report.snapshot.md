# Wave4 1 Smooth L1 Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints`
- Model Family: `wave4_1_smooth_l1_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-23-00-14__te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=079-val_mae=0.00192933.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002528`
- val_mae: `0.001929`
- val_rmse: `0.002678`
- val_pointwise_loss: `0.002528`
- val_centered_curve_shape_loss: `0.004536`
- val_curve_offset_loss: `0.000520`
- val_curve_amplitude_loss: `0.032778`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.044412`
- val_structured_rmse: `0.048822`
- val_residual_offset_mean_abs: `0.044314`

## Test Metrics

- test_loss: `0.004244`
- test_mae: `0.002233`
- test_rmse: `0.003602`
- test_pointwise_loss: `0.004244`
- test_centered_curve_shape_loss: `0.005428`
- test_curve_offset_loss: `0.003090`
- test_curve_amplitude_loss: `0.043246`
- test_sparse_harmonic_shape_loss: `0.000109`
- test_structured_mae: `0.040963`
- test_structured_rmse: `0.045784`
- test_residual_offset_mean_abs: `0.040896`

## Interpretation

The held-out val error stayed finite with MAE=0.001929 deg and RMSE=0.002678 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002233 deg and RMSE=0.003602 deg, which indicates a numerically stable baseline run.
