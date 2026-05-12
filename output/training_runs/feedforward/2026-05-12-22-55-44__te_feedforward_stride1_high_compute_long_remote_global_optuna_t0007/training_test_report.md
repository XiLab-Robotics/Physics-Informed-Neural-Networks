# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0007`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-05-12-22-55-44__te_feedforward_stride1_high_compute_long_remote_global_optuna_t0007\checkpoints\feedforward-epoch=112-val_mae=0.00296247.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007280`
- val_mae: `0.002962`
- val_rmse: `0.003626`

## Test Metrics

- test_loss: `0.007669`
- test_mae: `0.003317`
- test_rmse: `0.003936`

## Interpretation

The held-out val error stayed finite with MAE=0.002962 deg and RMSE=0.003626 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003317 deg and RMSE=0.003936 deg, which indicates a numerically stable baseline run.
