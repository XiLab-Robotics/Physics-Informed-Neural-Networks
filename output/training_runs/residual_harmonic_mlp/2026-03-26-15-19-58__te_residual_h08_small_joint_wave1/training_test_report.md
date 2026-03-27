# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h08_small_joint_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-15-19-58__te_residual_h08_small_joint_wave1\checkpoints\residual_harmonic_mlp-epoch=020-val_mae=0.00303040.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007215`
- val_mae: `0.003030`
- val_rmse: `0.003566`
- val_structured_mae: `0.040524`
- val_structured_rmse: `0.042587`

## Test Metrics

- test_loss: `0.007672`
- test_mae: `0.003385`
- test_rmse: `0.003862`
- test_structured_mae: `0.039404`
- test_structured_rmse: `0.042798`

## Interpretation

The held-out val error stayed finite with MAE=0.003030 deg and RMSE=0.003566 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003385 deg and RMSE=0.003862 deg, which indicates a numerically stable baseline run.

