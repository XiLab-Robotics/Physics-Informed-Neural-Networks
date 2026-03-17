# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_long`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\legacy__te_feedforward_stride1_long\checkpoints\feedforward-epoch=066-val_mae=0.00312552.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007726`
- val_mae: `0.003126`
- val_rmse: `0.003514`

## Test Metrics

- test_loss: `0.009383`
- test_mae: `0.003646`
- test_rmse: `0.003990`

## Interpretation

The held-out val error stayed finite with MAE=0.003126 deg and RMSE=0.003514 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003646 deg and RMSE=0.003990 deg, which indicates a numerically stable baseline run.
