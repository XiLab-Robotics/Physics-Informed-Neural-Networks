# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_trial`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_trial\checkpoints\feedforward-epoch=003-val_mae=0.00375716.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011193`
- val_mae: `0.003757`
- val_rmse: `0.004555`

## Test Metrics

- test_loss: `0.009341`
- test_mae: `0.003583`
- test_rmse: `0.004295`

## Interpretation

The held-out val error stayed finite with MAE=0.003757 deg and RMSE=0.004555 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003583 deg and RMSE=0.004295 deg, which indicates a numerically stable baseline run.
