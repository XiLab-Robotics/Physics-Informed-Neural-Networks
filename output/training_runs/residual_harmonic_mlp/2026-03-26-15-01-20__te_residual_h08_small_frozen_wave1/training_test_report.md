# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h08_small_frozen_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-15-01-20__te_residual_h08_small_frozen_wave1\checkpoints\residual_harmonic_mlp-epoch=063-val_mae=0.00300655.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007256`
- val_mae: `0.003007`
- val_rmse: `0.003549`
- val_structured_mae: `0.041095`
- val_structured_rmse: `0.044506`

## Test Metrics

- test_loss: `0.007990`
- test_mae: `0.003384`
- test_rmse: `0.003912`
- test_structured_mae: `0.040148`
- test_structured_rmse: `0.044895`

## Interpretation

The held-out val error stayed finite with MAE=0.003007 deg and RMSE=0.003549 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003384 deg and RMSE=0.003912 deg, which indicates a numerically stable baseline run.

