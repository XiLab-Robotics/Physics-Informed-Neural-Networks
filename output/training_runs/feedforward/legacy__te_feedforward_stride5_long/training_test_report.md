# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride5_long`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\legacy__te_feedforward_stride5_long\checkpoints\feedforward-epoch=043-val_mae=0.00317790.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008188`
- val_mae: `0.003178`
- val_rmse: `0.003660`

## Test Metrics

- test_loss: `0.009152`
- test_mae: `0.003580`
- test_rmse: `0.004008`

## Interpretation

The held-out val error stayed finite with MAE=0.003178 deg and RMSE=0.003660 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003580 deg and RMSE=0.004008 deg, which indicates a numerically stable baseline run.
