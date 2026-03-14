# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_best_training`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_best_training\checkpoints\feedforward-epoch=063-val_mae=0.00317104.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008015`
- val_mae: `0.003171`
- val_rmse: `0.003759`

## Test Metrics

- test_loss: `0.008817`
- test_mae: `0.003579`
- test_rmse: `0.004121`

## Interpretation

The held-out val error stayed finite with MAE=0.003171 deg and RMSE=0.003759 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003579 deg and RMSE=0.004121 deg, which indicates a numerically stable baseline run.
