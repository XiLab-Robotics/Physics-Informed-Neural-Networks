# Wave52B Offset Harmonic Guided Pointwise Control Global Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_pointwise_control_global`
- Model Family: `wave52b_offset_harmonic_guided_pointwise_control_global`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_pointwise_control_global\2026-07-01-18-59-04__te_wave52b_offset_harmonic_guided_pointwise_control_global\checkpoints\wave52b_offset_harmonic_guided-epoch=112-val_mae=0.00221041.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005873`
- val_mae: `0.002210`
- val_rmse: `0.002733`
- val_pointwise_loss: `0.005873`
- val_centered_curve_shape_loss: `0.005436`
- val_curve_offset_loss: `0.000437`
- val_curve_amplitude_loss: `0.054659`
- val_sparse_harmonic_shape_loss: `0.000125`
- val_structured_mae: `0.040232`
- val_structured_rmse: `0.043958`
- val_base_mae: `0.002210`
- val_base_rmse: `0.002733`
- val_residual_offset_mean_abs: `0.000000e+00`

## Test Metrics

- test_loss: `0.008976`
- test_mae: `0.002461`
- test_rmse: `0.003142`
- test_pointwise_loss: `0.008976`
- test_centered_curve_shape_loss: `0.006867`
- test_curve_offset_loss: `0.002109`
- test_curve_amplitude_loss: `0.061810`
- test_sparse_harmonic_shape_loss: `0.000135`
- test_structured_mae: `0.037992`
- test_structured_rmse: `0.042295`
- test_base_mae: `0.002461`
- test_base_rmse: `0.003142`
- test_residual_offset_mean_abs: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002210 deg and RMSE=0.002733 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002461 deg and RMSE=0.003142 deg, which indicates a numerically stable baseline run.
