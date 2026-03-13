# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_long_large_batch_big_model`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride1_long_large_batch_big_model\checkpoints\feedforward-epoch=078-val_mae=0.00308973.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007474`
- val_mae: `0.003090`
- val_rmse: `0.003585`

## Test Metrics

- test_loss: `0.007596`
- test_mae: `0.003308`
- test_rmse: `0.003779`

## Interpretation

The held-out val error stayed finite with MAE=0.003090 deg and RMSE=0.003585 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003308 deg and RMSE=0.003779 deg, which indicates a numerically stable baseline run.
