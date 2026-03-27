# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_small_joint_low_lr_long_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-18-43-58__te_residual_h12_small_joint_low_lr_long_wave1\checkpoints\residual_harmonic_mlp-epoch=134-val_mae=0.00298742.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007439`
- val_mae: `0.002987`
- val_rmse: `0.003499`
- val_structured_mae: `0.040645`
- val_structured_rmse: `0.042584`

## Test Metrics

- test_loss: `0.008583`
- test_mae: `0.003465`
- test_rmse: `0.003944`
- test_structured_mae: `0.039461`
- test_structured_rmse: `0.042931`

## Interpretation

The held-out val error stayed finite with MAE=0.002987 deg and RMSE=0.003499 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003465 deg and RMSE=0.003944 deg, which indicates a numerically stable baseline run.

