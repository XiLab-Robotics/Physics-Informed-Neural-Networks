# Track2G Curve Aware Harmonic Residual Offset Pointwise Control Fw Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_pointwise_control_fw`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw\2026-06-08-18-56-59__te_track2g_curve_aware_pointwise_control_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=043-val_mae=0.00329125.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.032633`
- val_mae: `0.003291`
- val_rmse: `0.003784`
- val_pointwise_loss: `0.032633`
- val_centered_curve_shape_loss: `0.015186`
- val_curve_offset_loss: `0.017447`
- val_curve_amplitude_loss: `0.104425`
- val_sparse_harmonic_shape_loss: `0.000331`
- val_structured_mae: `0.014476`
- val_structured_rmse: `0.015944`
- val_residual_offset_mean_abs: `0.014386`

## Test Metrics

- test_loss: `0.029178`
- test_mae: `0.003371`
- test_rmse: `0.003763`
- test_pointwise_loss: `0.029178`
- test_centered_curve_shape_loss: `0.007652`
- test_curve_offset_loss: `0.021525`
- test_curve_amplitude_loss: `0.048620`
- test_sparse_harmonic_shape_loss: `0.000141`
- test_structured_mae: `0.015150`
- test_structured_rmse: `0.016565`
- test_residual_offset_mean_abs: `0.015674`

## Interpretation

The held-out val error stayed finite with MAE=0.003291 deg and RMSE=0.003784 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003371 deg and RMSE=0.003763 deg, which indicates a numerically stable baseline run.
