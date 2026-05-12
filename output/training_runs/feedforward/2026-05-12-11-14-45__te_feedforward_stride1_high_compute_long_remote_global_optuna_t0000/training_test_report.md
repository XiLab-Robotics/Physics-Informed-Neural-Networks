# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0000`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-05-12-11-14-45__te_feedforward_stride1_high_compute_long_remote_global_optuna_t0000\checkpoints\feedforward-epoch=105-val_mae=0.00301022.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007397`
- val_mae: `0.003010`
- val_rmse: `0.003481`

## Test Metrics

- test_loss: `0.008125`
- test_mae: `0.003446`
- test_rmse: `0.003871`

## Interpretation

The held-out val error stayed finite with MAE=0.003010 deg and RMSE=0.003481 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003446 deg and RMSE=0.003871 deg, which indicates a numerically stable baseline run.
