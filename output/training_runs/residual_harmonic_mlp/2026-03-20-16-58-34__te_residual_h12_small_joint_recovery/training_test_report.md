# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_small_joint_recovery`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-20-16-58-34__te_residual_h12_small_joint_recovery\checkpoints\residual_harmonic_mlp-epoch=056-val_mae=0.00301633.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007436`
- val_mae: `0.003016`
- val_rmse: `0.003534`
- val_structured_mae: `0.040527`
- val_structured_rmse: `0.042576`

## Test Metrics

- test_loss: `0.008337`
- test_mae: `0.003466`
- test_rmse: `0.003967`
- test_structured_mae: `0.039405`
- test_structured_rmse: `0.042796`

## Interpretation

The held-out val error stayed finite with MAE=0.003016 deg and RMSE=0.003534 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003466 deg and RMSE=0.003967 deg, which indicates a numerically stable baseline run.
