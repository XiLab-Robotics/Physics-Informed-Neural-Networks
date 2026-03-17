# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride10_long_large_batch`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\legacy__te_feedforward_stride10_long_large_batch\checkpoints\feedforward-epoch=111-val_mae=0.00306641.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007708`
- val_mae: `0.003066`
- val_rmse: `0.003765`

## Test Metrics

- test_loss: `0.008467`
- test_mae: `0.003433`
- test_rmse: `0.004123`

## Interpretation

The held-out val error stayed finite with MAE=0.003066 deg and RMSE=0.003765 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003433 deg and RMSE=0.004123 deg, which indicates a numerically stable baseline run.
