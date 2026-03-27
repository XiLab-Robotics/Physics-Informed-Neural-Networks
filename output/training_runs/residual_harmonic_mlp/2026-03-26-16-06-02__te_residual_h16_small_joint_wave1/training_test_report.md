# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h16_small_joint_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-16-06-02__te_residual_h16_small_joint_wave1\checkpoints\residual_harmonic_mlp-epoch=074-val_mae=0.00302049.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007019`
- val_mae: `0.003020`
- val_rmse: `0.003527`
- val_structured_mae: `0.040556`
- val_structured_rmse: `0.042550`

## Test Metrics

- test_loss: `0.007190`
- test_mae: `0.003274`
- test_rmse: `0.003747`
- test_structured_mae: `0.039417`
- test_structured_rmse: `0.042812`

## Interpretation

The held-out val error stayed finite with MAE=0.003020 deg and RMSE=0.003527 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003274 deg and RMSE=0.003747 deg, which indicates a numerically stable baseline run.

