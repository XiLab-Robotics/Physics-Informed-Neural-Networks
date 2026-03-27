# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_wide_joint_low_lr_long_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-19-11-43__te_residual_h12_wide_joint_low_lr_long_wave1\checkpoints\residual_harmonic_mlp-epoch=124-val_mae=0.00292449.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007006`
- val_mae: `0.002924`
- val_rmse: `0.003449`
- val_structured_mae: `0.040532`
- val_structured_rmse: `0.042566`

## Test Metrics

- test_loss: `0.007447`
- test_mae: `0.003278`
- test_rmse: `0.003814`
- test_structured_mae: `0.039407`
- test_structured_rmse: `0.042797`

## Interpretation

The held-out val error stayed finite with MAE=0.002924 deg and RMSE=0.003449 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003278 deg and RMSE=0.003814 deg, which indicates a numerically stable baseline run.

