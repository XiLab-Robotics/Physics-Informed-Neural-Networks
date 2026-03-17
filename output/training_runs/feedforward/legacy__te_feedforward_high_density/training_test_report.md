# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_high_density`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\feedforward\legacy__te_feedforward_high_density\checkpoints\feedforward-epoch=041-val_mae=0.00307732.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007662`
- val_mae: `0.003077`
- val_rmse: `0.003642`

## Test Metrics

- test_loss: `0.008528`
- test_mae: `0.003519`
- test_rmse: `0.004046`

## Interpretation

The held-out val error stayed finite with MAE=0.003077 deg and RMSE=0.003642 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003519 deg and RMSE=0.004046 deg, which indicates a numerically stable baseline run.
