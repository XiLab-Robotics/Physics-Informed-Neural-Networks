# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-17-19-48__te_residual_h12_deep_joint_wave1\checkpoints\residual_harmonic_mlp-epoch=077-val_mae=0.00302384.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007314`
- val_mae: `0.003024`
- val_rmse: `0.003580`
- val_structured_mae: `0.040554`
- val_structured_rmse: `0.042550`

## Test Metrics

- test_loss: `0.006955`
- test_mae: `0.003152`
- test_rmse: `0.003640`
- test_structured_mae: `0.039416`
- test_structured_rmse: `0.042810`

## Interpretation

The held-out val error stayed finite with MAE=0.003024 deg and RMSE=0.003580 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003152 deg and RMSE=0.003640 deg, which indicates a numerically stable baseline run.

