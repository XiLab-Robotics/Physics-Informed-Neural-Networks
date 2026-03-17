# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_trial`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\feedforward_network\te_feedforward_trial\checkpoints\feedforward-epoch=007-val_mae=0.00361790.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010227`
- val_mae: `0.003618`
- val_rmse: `0.004350`

## Test Metrics

- test_loss: `0.008881`
- test_mae: `0.003535`
- test_rmse: `0.004211`

## Interpretation

The held-out val error stayed finite with MAE=0.003618 deg and RMSE=0.004350 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003535 deg and RMSE=0.004211 deg, which indicates a numerically stable baseline run.
