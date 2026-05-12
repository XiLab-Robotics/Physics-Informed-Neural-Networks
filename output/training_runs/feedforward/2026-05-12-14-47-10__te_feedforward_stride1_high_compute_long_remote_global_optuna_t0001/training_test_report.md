# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0001`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-05-12-14-47-10__te_feedforward_stride1_high_compute_long_remote_global_optuna_t0001\checkpoints\feedforward-epoch=198-val_mae=0.00295772.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007306`
- val_mae: `0.002958`
- val_rmse: `0.003607`

## Test Metrics

- test_loss: `0.008555`
- test_mae: `0.003446`
- test_rmse: `0.004158`

## Interpretation

The held-out val error stayed finite with MAE=0.002958 deg and RMSE=0.003607 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003446 deg and RMSE=0.004158 deg, which indicates a numerically stable baseline run.
