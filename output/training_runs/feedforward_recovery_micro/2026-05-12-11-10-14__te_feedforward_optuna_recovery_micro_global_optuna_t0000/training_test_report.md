# Feedforward Recovery Micro Training And Testing Report

## Overview

- Run Name: `te_feedforward_optuna_recovery_micro_global_optuna_t0000`
- Model Family: `feedforward_recovery_micro`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward_recovery_micro\2026-05-12-11-10-14__te_feedforward_optuna_recovery_micro_global_optuna_t0000\checkpoints\feedforward-epoch=000-val_mae=0.00426588.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.013578`
- val_mae: `0.004266`
- val_rmse: `0.005201`

## Test Metrics

- test_loss: `0.012697`
- test_mae: `0.004164`
- test_rmse: `0.005109`

## Interpretation

The held-out val error stayed finite with MAE=0.004266 deg and RMSE=0.005201 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.004164 deg and RMSE=0.005109 deg, which indicates a numerically stable baseline run.
