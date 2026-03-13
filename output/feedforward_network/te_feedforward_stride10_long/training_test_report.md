# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride10_long`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride10_long\checkpoints\feedforward-epoch=107-val_mae=0.00305276.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007750`
- val_mae: `0.003053`
- val_rmse: `0.003588`

## Test Metrics

- test_loss: `0.008709`
- test_mae: `0.003483`
- test_rmse: `0.004050`

## Interpretation

The held-out val error stayed finite with MAE=0.003053 deg and RMSE=0.003588 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003483 deg and RMSE=0.004050 deg, which indicates a numerically stable baseline run.
