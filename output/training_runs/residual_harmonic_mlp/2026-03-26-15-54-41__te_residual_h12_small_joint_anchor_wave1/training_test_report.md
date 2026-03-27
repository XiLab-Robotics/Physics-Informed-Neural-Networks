# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_small_joint_anchor_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-15-54-41__te_residual_h12_small_joint_anchor_wave1\checkpoints\residual_harmonic_mlp-epoch=017-val_mae=0.00308991.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007708`
- val_mae: `0.003090`
- val_rmse: `0.003651`
- val_structured_mae: `0.040603`
- val_structured_rmse: `0.042556`

## Test Metrics

- test_loss: `0.008477`
- test_mae: `0.003557`
- test_rmse: `0.004064`
- test_structured_mae: `0.039440`
- test_structured_rmse: `0.042864`

## Interpretation

The held-out val error stayed finite with MAE=0.003090 deg and RMSE=0.003651 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003557 deg and RMSE=0.004064 deg, which indicates a numerically stable baseline run.

