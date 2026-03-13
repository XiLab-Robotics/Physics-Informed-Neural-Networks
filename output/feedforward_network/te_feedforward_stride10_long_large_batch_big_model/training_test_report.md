# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride10_long_large_batch_big_model`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_stride10_long_large_batch_big_model\checkpoints\feedforward-epoch=067-val_mae=0.00303994.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007577`
- val_mae: `0.003040`
- val_rmse: `0.003702`

## Test Metrics

- test_loss: `0.008302`
- test_mae: `0.003413`
- test_rmse: `0.004063`

## Interpretation

The held-out val error stayed finite with MAE=0.003040 deg and RMSE=0.003702 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003413 deg and RMSE=0.004063 deg, which indicates a numerically stable baseline run.
