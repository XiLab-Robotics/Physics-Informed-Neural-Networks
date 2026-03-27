# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_small_joint_dense_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-19-34-28__te_residual_h12_small_joint_dense_wave1\checkpoints\residual_harmonic_mlp-epoch=038-val_mae=0.00296185.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007331`
- val_mae: `0.002962`
- val_rmse: `0.003390`
- val_structured_mae: `0.040566`
- val_structured_rmse: `0.040830`

## Test Metrics

- test_loss: `0.008414`
- test_mae: `0.003410`
- test_rmse: `0.003790`
- test_structured_mae: `0.039422`
- test_structured_rmse: `0.039740`

## Interpretation

The held-out val error stayed finite with MAE=0.002962 deg and RMSE=0.003390 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003410 deg and RMSE=0.003790 deg, which indicates a numerically stable baseline run.

