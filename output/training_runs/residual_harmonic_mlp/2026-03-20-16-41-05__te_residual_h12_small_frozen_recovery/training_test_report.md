# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_small_frozen_recovery`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-20-16-41-05__te_residual_h12_small_frozen_recovery\checkpoints\residual_harmonic_mlp-epoch=092-val_mae=0.00303009.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007543`
- val_mae: `0.003030`
- val_rmse: `0.003554`
- val_structured_mae: `0.041095`
- val_structured_rmse: `0.044506`

## Test Metrics

- test_loss: `0.008930`
- test_mae: `0.003554`
- test_rmse: `0.004061`
- test_structured_mae: `0.040148`
- test_structured_rmse: `0.044895`

## Interpretation

The held-out val error stayed finite with MAE=0.003030 deg and RMSE=0.003554 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003554 deg and RMSE=0.004061 deg, which indicates a numerically stable baseline run.
