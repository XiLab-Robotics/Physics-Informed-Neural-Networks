# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_wide_joint_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-16-48-24__te_residual_h12_wide_joint_wave1\checkpoints\residual_harmonic_mlp-epoch=097-val_mae=0.00288380.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006948`
- val_mae: `0.002884`
- val_rmse: `0.003410`
- val_structured_mae: `0.040531`
- val_structured_rmse: `0.042569`

## Test Metrics

- test_loss: `0.007930`
- test_mae: `0.003376`
- test_rmse: `0.003906`
- test_structured_mae: `0.039406`
- test_structured_rmse: `0.042797`

## Interpretation

The held-out val error stayed finite with MAE=0.002884 deg and RMSE=0.003410 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003376 deg and RMSE=0.003906 deg, which indicates a numerically stable baseline run.

