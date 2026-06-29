# Feedforward Global Training And Testing Report

## Overview

- Run Name: `te_feedforward_global`
- Model Family: `feedforward_global`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-06-25-17-47-36__te_feedforward_global\checkpoints\feedforward-epoch=123-val_mae=0.00163670.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002770`
- val_mae: `0.001637`
- val_rmse: `0.002033`
- val_pointwise_loss: `0.002770`
- val_centered_curve_shape_loss: `0.002453`
- val_curve_offset_loss: `0.000347`
- val_curve_amplitude_loss: `0.035739`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003998`
- test_mae: `0.001734`
- test_rmse: `0.002220`
- test_pointwise_loss: `0.003998`
- test_centered_curve_shape_loss: `0.003598`
- test_curve_offset_loss: `0.000942`
- test_curve_amplitude_loss: `0.051941`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001637 deg and RMSE=0.002033 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001734 deg and RMSE=0.002220 deg, which indicates a numerically stable baseline run.
