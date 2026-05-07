# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward_fw\2026-05-06-20-16-42__te_feedforward_stride1_high_compute_long_remote_fw\checkpoints\feedforward-epoch=033-val_mae=0.00291539.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025541`
- val_mae: `0.002915`
- val_rmse: `0.003406`

## Test Metrics

- test_loss: `0.033267`
- test_mae: `0.003563`
- test_rmse: `0.004009`

## Interpretation

The held-out val error stayed finite with MAE=0.002915 deg and RMSE=0.003406 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003563 deg and RMSE=0.004009 deg, which indicates a numerically stable baseline run.
