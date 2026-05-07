# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp_bw\2026-05-06-17-34-34__te_residual_h12_deep_joint_wave1_bw\checkpoints\residual_harmonic_mlp-epoch=037-val_mae=0.00310962.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028329`
- val_mae: `0.003110`
- val_rmse: `0.003766`
- val_structured_mae: `0.017501`
- val_structured_rmse: `0.019774`

## Test Metrics

- test_loss: `0.030293`
- test_mae: `0.003493`
- test_rmse: `0.004108`
- test_structured_mae: `0.021552`
- test_structured_rmse: `0.023519`

## Interpretation

The held-out val error stayed finite with MAE=0.003110 deg and RMSE=0.003766 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003493 deg and RMSE=0.004108 deg, which indicates a numerically stable baseline run.
