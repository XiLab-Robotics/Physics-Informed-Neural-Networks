# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_baseline`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\legacy__te_feedforward_baseline\checkpoints\feedforward-epoch=022-val_mae=0.00314821.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007930`
- val_mae: `0.003148`
- val_rmse: `0.003655`

## Test Metrics

- test_loss: `0.008453`
- test_mae: `0.003504`
- test_rmse: `0.003969`

## Interpretation

The held-out val error stayed finite with MAE=0.003148 deg and RMSE=0.003655 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003504 deg and RMSE=0.003969 deg, which indicates a numerically stable baseline run.
