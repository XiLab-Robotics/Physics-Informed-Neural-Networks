# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_small_joint_no_layer_norm_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-18-31-09__te_residual_h12_small_joint_no_layer_norm_wave1\checkpoints\residual_harmonic_mlp-epoch=044-val_mae=0.00308930.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007495`
- val_mae: `0.003089`
- val_rmse: `0.003640`
- val_structured_mae: `0.040519`
- val_structured_rmse: `0.042613`

## Test Metrics

- test_loss: `0.007555`
- test_mae: `0.003360`
- test_rmse: `0.003835`
- test_structured_mae: `0.039402`
- test_structured_rmse: `0.042806`

## Interpretation

The held-out val error stayed finite with MAE=0.003089 deg and RMSE=0.003640 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003360 deg and RMSE=0.003835 deg, which indicates a numerically stable baseline run.

