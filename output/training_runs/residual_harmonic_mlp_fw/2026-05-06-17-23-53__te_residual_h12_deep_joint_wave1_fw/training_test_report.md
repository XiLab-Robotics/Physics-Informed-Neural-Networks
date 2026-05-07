# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp_fw\2026-05-06-17-23-53__te_residual_h12_deep_joint_wave1_fw\checkpoints\residual_harmonic_mlp-epoch=018-val_mae=0.00285191.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026043`
- val_mae: `0.002852`
- val_rmse: `0.003464`
- val_structured_mae: `0.016809`
- val_structured_rmse: `0.019134`

## Test Metrics

- test_loss: `0.032574`
- test_mae: `0.003530`
- test_rmse: `0.004145`
- test_structured_mae: `0.020170`
- test_structured_rmse: `0.022272`

## Interpretation

The held-out val error stayed finite with MAE=0.002852 deg and RMSE=0.003464 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003530 deg and RMSE=0.004145 deg, which indicates a numerically stable baseline run.
