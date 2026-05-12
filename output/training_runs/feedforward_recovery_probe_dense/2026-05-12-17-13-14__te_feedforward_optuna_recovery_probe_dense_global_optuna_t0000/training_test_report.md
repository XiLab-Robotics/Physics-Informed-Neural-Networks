# Feedforward Recovery Probe Dense Training And Testing Report

## Overview

- Run Name: `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000`
- Model Family: `feedforward_recovery_probe_dense`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward_recovery_probe_dense\2026-05-12-17-13-14__te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000\checkpoints\feedforward-epoch=001-val_mae=0.00425682.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012861`
- val_mae: `0.004257`
- val_rmse: `0.004925`

## Test Metrics

- test_loss: `0.014400`
- test_mae: `0.004602`
- test_rmse: `0.005262`

## Interpretation

The held-out val error stayed finite with MAE=0.004257 deg and RMSE=0.004925 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.004602 deg and RMSE=0.005262 deg, which indicates a numerically stable baseline run.
