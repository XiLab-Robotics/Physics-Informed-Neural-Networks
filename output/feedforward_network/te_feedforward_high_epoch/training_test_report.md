# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_high_epoch`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_high_epoch\checkpoints\feedforward-epoch=094-val_mae=0.00300707.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007442`
- val_mae: `0.003007`
- val_rmse: `0.003451`

## Test Metrics

- test_loss: `0.007991`
- test_mae: `0.003335`
- test_rmse: `0.003767`

## Interpretation

The held-out val error stayed finite with MAE=0.003007 deg and RMSE=0.003451 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003335 deg and RMSE=0.003767 deg, which indicates a numerically stable baseline run.
