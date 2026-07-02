# Wave52B Offset Harmonic Guided Pointwise Control Fw Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_pointwise_control_fw`
- Model Family: `wave52b_offset_harmonic_guided_pointwise_control_fw`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_pointwise_control_fw\2026-07-01-19-54-22__te_wave52b_offset_harmonic_guided_pointwise_control_fw\checkpoints\wave52b_offset_harmonic_guided-epoch=062-val_mae=0.00234381.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.020981`
- val_mae: `0.002344`
- val_rmse: `0.002881`
- val_pointwise_loss: `0.020981`
- val_centered_curve_shape_loss: `0.018870`
- val_curve_offset_loss: `0.002110`
- val_curve_amplitude_loss: `0.182191`
- val_sparse_harmonic_shape_loss: `0.000434`
- val_structured_mae: `0.019635`
- val_structured_rmse: `0.023073`
- val_base_mae: `0.002344`
- val_base_rmse: `0.002881`
- val_residual_offset_mean_abs: `0.000000e+00`

## Test Metrics

- test_loss: `0.014297`
- test_mae: `0.002054`
- test_rmse: `0.002564`
- test_pointwise_loss: `0.014297`
- test_centered_curve_shape_loss: `0.011447`
- test_curve_offset_loss: `0.002850`
- test_curve_amplitude_loss: `0.115889`
- test_sparse_harmonic_shape_loss: `0.000246`
- test_structured_mae: `0.020063`
- test_structured_rmse: `0.023460`
- test_base_mae: `0.002054`
- test_base_rmse: `0.002564`
- test_residual_offset_mean_abs: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002344 deg and RMSE=0.002881 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002054 deg and RMSE=0.002564 deg, which indicates a numerically stable baseline run.
