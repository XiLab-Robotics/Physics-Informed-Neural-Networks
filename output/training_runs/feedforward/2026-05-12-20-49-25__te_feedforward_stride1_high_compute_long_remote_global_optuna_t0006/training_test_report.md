# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0006`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-05-12-20-49-25__te_feedforward_stride1_high_compute_long_remote_global_optuna_t0006\checkpoints\feedforward-epoch=095-val_mae=0.00304407.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007580`
- val_mae: `0.003044`
- val_rmse: `0.003503`

## Test Metrics

- test_loss: `0.008327`
- test_mae: `0.003436`
- test_rmse: `0.003857`

## Interpretation

The held-out val error stayed finite with MAE=0.003044 deg and RMSE=0.003503 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003436 deg and RMSE=0.003857 deg, which indicates a numerically stable baseline run.
