# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_small_joint_low_dropout_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-17-48-36__te_residual_h12_small_joint_low_dropout_wave1\checkpoints\residual_harmonic_mlp-epoch=076-val_mae=0.00302673.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007305`
- val_mae: `0.003027`
- val_rmse: `0.003539`
- val_structured_mae: `0.040578`
- val_structured_rmse: `0.042548`

## Test Metrics

- test_loss: `0.007847`
- test_mae: `0.003359`
- test_rmse: `0.003852`
- test_structured_mae: `0.039428`
- test_structured_rmse: `0.042834`

## Interpretation

The held-out val error stayed finite with MAE=0.003027 deg and RMSE=0.003539 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003359 deg and RMSE=0.003852 deg, which indicates a numerically stable baseline run.

