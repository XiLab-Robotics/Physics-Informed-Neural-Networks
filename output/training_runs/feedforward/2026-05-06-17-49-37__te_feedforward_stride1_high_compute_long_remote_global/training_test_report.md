# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\2026-05-06-17-49-37__te_feedforward_stride1_high_compute_long_remote_global\checkpoints\feedforward-epoch=180-val_mae=0.00305586.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007338`
- val_mae: `0.003056`
- val_rmse: `0.003510`

## Test Metrics

- test_loss: `0.007049`
- test_mae: `0.003150`
- test_rmse: `0.003603`

## Interpretation

The held-out val error stayed finite with MAE=0.003056 deg and RMSE=0.003510 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003150 deg and RMSE=0.003603 deg, which indicates a numerically stable baseline run.
