# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_medium_joint_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-16-26-11__te_residual_h12_medium_joint_wave1\checkpoints\residual_harmonic_mlp-epoch=082-val_mae=0.00296847.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007188`
- val_mae: `0.002968`
- val_rmse: `0.003468`
- val_structured_mae: `0.040608`
- val_structured_rmse: `0.042558`

## Test Metrics

- test_loss: `0.008086`
- test_mae: `0.003406`
- test_rmse: `0.003863`
- test_structured_mae: `0.039442`
- test_structured_rmse: `0.042870`

## Interpretation

The held-out val error stayed finite with MAE=0.002968 deg and RMSE=0.003468 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003406 deg and RMSE=0.003863 deg, which indicates a numerically stable baseline run.

