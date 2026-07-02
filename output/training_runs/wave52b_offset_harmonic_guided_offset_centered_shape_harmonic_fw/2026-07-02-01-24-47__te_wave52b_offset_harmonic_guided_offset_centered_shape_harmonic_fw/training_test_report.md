# Wave52B Offset Harmonic Guided Offset Centered Shape Harmonic Fw Training And Testing Report

## Overview

- Run Name: `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw`
- Model Family: `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw`
- Model Type: `wave52b_offset_harmonic_guided`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw\2026-07-02-01-24-47__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw\checkpoints\wave52b_offset_harmonic_guided-epoch=116-val_mae=0.00180918.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.022212`
- val_mae: `0.001809`
- val_rmse: `0.002229`
- val_pointwise_loss: `0.016042`
- val_centered_curve_shape_loss: `0.014740`
- val_curve_offset_loss: `0.001302`
- val_curve_amplitude_loss: `0.059883`
- val_sparse_harmonic_shape_loss: `0.000320`
- val_structured_mae: `0.009778`
- val_structured_rmse: `0.010819`
- val_base_mae: `0.016051`
- val_base_rmse: `0.019192`
- val_residual_offset_mean_abs: `0.005232`

## Test Metrics

- test_loss: `0.011725`
- test_mae: `0.001392`
- test_rmse: `0.001771`
- test_pointwise_loss: `0.008862`
- test_centered_curve_shape_loss: `0.007541`
- test_curve_offset_loss: `0.001321`
- test_curve_amplitude_loss: `0.022848`
- test_sparse_harmonic_shape_loss: `0.000139`
- test_structured_mae: `0.008508`
- test_structured_rmse: `0.009495`
- test_base_mae: `0.016492`
- test_base_rmse: `0.019735`
- test_residual_offset_mean_abs: `0.004582`

## Interpretation

The held-out val error stayed finite with MAE=0.001809 deg and RMSE=0.002229 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001392 deg and RMSE=0.001771 deg, which indicates a numerically stable baseline run.
